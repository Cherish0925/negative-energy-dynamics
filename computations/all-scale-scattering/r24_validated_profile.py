#!/usr/bin/env python3
"""Outward interval Taylor enclosure for the two-dimensional Townes ODE.

Only mpmath.iv arithmetic is used for mathematical inclusions. Decimal/Fraction
grid calculations are exact. Serialized interval endpoints are rounded out to
40 decimal places directly from their binary integer representation.

The initial even-series enclosure follows from the analytic fixed point on
|r| <= 1/10, |Q-a| <= 1/10. Each subsequent step has a strict Picard tube and
uses a Taylor remainder whose normalized derivatives are evaluated over that
tube. Run with --help for the shooting/profile options.
"""
import argparse
import json
from fractions import Fraction
from pathlib import Path
import time
import mpmath as mp

I = mp.iv.mpf

def ivfrac(f):
    f = Fraction(f)
    return I(f.numerator) / I(f.denominator)

def hull(*xs):
    return I([min(x.a for x in xs), max(x.b for x in xs)])

def mag(x):
    return max(abs(x.a), abs(x.b))

def symmetric(x):
    u = mag(x)
    return I([-u, u])

def strict_inside(x, y):
    return bool(y.a < x.a and x.b < y.b)

def binary_fraction(t):
    sign, man, exp, bc = t
    v = Fraction((-1 if sign else 1) * man)
    return v * (2 ** exp) if exp >= 0 else v / (2 ** (-exp))

def fixed_string(n, digits):
    sign = '-' if n < 0 else ''
    n = abs(n)
    s = str(n).zfill(digits + 1)
    return sign + s[:-digits] + '.' + s[-digits:]

def serial(x, digits=40):
    a, b = (binary_fraction(t) for t in x._mpi_)
    fac = 10 ** digits
    lo = (a * fac).numerator // (a * fac).denominator
    hi = -((-b * fac).numerator // (-b * fac).denominator)
    return [fixed_string(lo, digits), fixed_string(hi, digits)]

def initial(a, n=16, r_string='0.01'):
    radius = I('0.1')
    eta = I('0.1')
    bound = mag(a) + eta
    image = radius ** 2 * (bound + bound ** 3) / 4
    contraction = radius ** 2 * (1 + 3 * bound ** 2) / 4
    assert bool(image < eta) and bool(contraction < 1)
    cs = [a]
    square = []
    for j in range(n):
        square.append(sum((cs[i] * cs[j-i] for i in range(j+1)), I(0)))
        cube = sum((square[i] * cs[j-i] for i in range(j+1)), I(0))
        cs.append((cs[j] - cube) / (4 * (j+1) ** 2))
    r = I(r_string)
    z = (r/radius) ** 2
    qtail = eta * z ** (n+1) / (1-z)
    ptail = (2*eta/r) * z ** (n+1) * ((n+1)-n*z) / (1-z)**2
    q = sum((cs[j] * r ** (2*j) for j in range(n+1)), I(0))
    p = sum((2*j*cs[j] * r ** (2*j-1) for j in range(1,n+1)), I(0))
    q += symmetric(qtail)
    p += symmetric(ptail)
    return q, p, {'analytic_radius': '0.1', 'fixed_point_radius': '0.1',
                  'series_order_in_r_squared': n,
                  'fixed_point_image_bound': serial(image),
                  'contraction_bound': serial(contraction),
                  'q_initial_tail': serial(qtail),
                  'p_initial_tail': serial(ptail)}

def coefficients(q0, p0, r0, n):
    """c_j encloses y^(j)/j! for every initial state and radius supplied."""
    qc = [q0]
    pc = [p0]
    qq = []
    inv = [1/r0]
    for j in range(1, n):
        inv.append(-inv[-1]/r0)
    for j in range(n):
        qq.append(sum((qc[i]*qc[j-i] for i in range(j+1)), I(0)))
        cube = sum((qq[i]*qc[j-i] for i in range(j+1)), I(0))
        pr = sum((pc[i]*inv[j-i] for i in range(j+1)), I(0))
        qc.append(pc[j]/(j+1))
        pc.append((qc[j]-cube-pr)/(j+1))
    return qc, pc

def evalpoly(cs, h):
    ans = cs[-1]
    for c in reversed(cs[:-1]):
        ans = ans*h+c
    return ans

def tube(q, p, rf, hf):
    h = ivfrac(hf)
    r = I([ivfrac(rf).a, ivfrac(rf+hf).b])
    timeiv = I([0, h.b])
    # Inflate first-order increments; repeated inclusion checks certify the tube.
    dq = h*(mag(p)+1)
    dp = h*(mag(q-q**3-p/ivfrac(rf))+1)
    qt = q+symmetric(dq)
    pt = p+symmetric(dp)
    for iteration in range(20):
        qimage = q+timeiv*pt
        pimage = p+timeiv*(qt-qt**3-pt/r)
        if strict_inside(qimage, qt) and strict_inside(pimage, pt):
            # Sup-norm Lipschitz constant of (p,q-q^3-p/r) on the tube.
            lip = h*max(I(1), 1+3*mag(qt)**2+1/r.a)
            if not bool(lip < 1):
                raise ValueError('Picard contraction requires smaller step')
            return qt, pt, r, iteration, lip
        qt = hull(qt, qimage)
        pt = hull(pt, pimage)
        qt += symmetric((qt.b-qt.a)/10 + I('1e-70'))
        pt += symmetric((pt.b-pt.a)/10 + I('1e-70'))
    raise ValueError('No strict Picard tube')

def step(q, p, rf, hf, order):
    qt, pt, rt, iterations, lip = tube(q,p,rf,hf)
    h = ivfrac(hf)
    qc, pc = coefficients(q,p,ivfrac(rf),order)
    qr, pr = coefficients(qt,pt,rt,order+1)
    qnext = evalpoly(qc,h)+qr[-1]*h**(order+1)
    pnext = evalpoly(pc,h)+pr[-1]*h**(order+1)
    hi = I([0,h.b])
    qrange = evalpoly(qc,hi)+qr[-1]*hi**(order+1)
    prange = evalpoly(pc,hi)+pr[-1]*hi**(order+1)
    return qnext,pnext,qt,pt,iterations,lip,qrange,prange

def run(a, stop, maxstep, order, retain=True, shooting=False):
    q,p,init = initial(a)
    r = Fraction(1,100)
    stop = Fraction(stop)
    maxstep = Fraction(maxstep)
    records = []
    node0 = {'r':str(r),'q':serial(q),'p':serial(p)}
    count = 0
    start = time.time()
    classification = None
    positive_history = True  # The analytic disk bound covers [0,0.01].
    while r < stop:
        h = min(maxstep,r/16,stop-r)
        while True:
            try:
                qn,pn,qt,pt,iters,lip,qrange,prange = step(q,p,r,h,order)
                break
            except ValueError:
                h /= 2
                if h < Fraction(1,10**8):
                    raise
        if retain:
            records.append({'r0':str(r),'r1':str(r+h),
                            'q0':serial(q),'p0':serial(p),
                            'q1':serial(qn),'p1':serial(pn),
                            'q_tube':serial(qt),'p_tube':serial(pt),
                            'q_range':serial(qrange),'p_range':serial(prange),
                            'picard_lipschitz':serial(lip)})
        positive_history = positive_history and bool(qrange.a > 0)
        r += h
        q,p = qn,pn
        count += 1
        if shooting:
            if bool(q.b < 0):
                classification = 'crosses_zero'
            elif positive_history and bool(q.a > 0 and p.a > 0):
                classification = 'turns_while_positive'
            if classification:
                break
        if count % 200 == 0:
            print(json.dumps({'steps':count,'r':float(r),
                              'q':serial(q,20),'p':serial(p,20),
                              'seconds':time.time()-start}),flush=True)
    qhalf, phalf, _ = initial(a, r_string='0.005')
    origin_nodes=[{'r':'0','q':serial(a),'p':serial(I(0))},
                  {'r':'1/200','q':serial(qhalf),'p':serial(phalf)},
                  node0]
    return {'a':serial(a),'initial':init,'first_node':node0,
            'origin_nodes':origin_nodes,
            'end_r':str(r),'end_q':serial(q),'end_p':serial(p),
            'classification':classification,'steps':count,
            'positive_entire_history':positive_history,
            'elapsed_seconds':time.time()-start,'records':records}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['shoot','profile'],required=True)
    ap.add_argument('--a-low',default='2.206200864650')
    ap.add_argument('--a-high',default='2.206200864651')
    ap.add_argument('--stop',default=None)
    ap.add_argument('--step',default='0.02')
    ap.add_argument('--order',type=int,default=18)
    ap.add_argument('--dps',type=int,default=70)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    mp.iv.dps=args.dps
    meta={'method':'mpmath.iv outward interval Taylor with strict Picard tubes',
          'mpmath_version':mp.__version__,'interval_dps':args.dps,
          'taylor_order':args.order,'maximum_step':args.step,
          'endpoint_serialization':'outward 40-place decimal via exact dyadic fractions'}
    if args.mode=='shoot':
        meta['lower_shot']=run(I(args.a_low),args.stop or '20',args.step,args.order,
                              retain=False,shooting=True)
        meta['upper_shot']=run(I(args.a_high),args.stop or '20',args.step,args.order,
                              retain=False,shooting=True)
        meta['bracket_success']=(meta['lower_shot']['classification']=='turns_while_positive'
                                and meta['upper_shot']['classification']=='crosses_zero')
    else:
        meta['profile']=run(I([args.a_low,args.a_high]),args.stop or '8',args.step,
                            args.order,retain=True,shooting=False)
    Path(args.output).write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps({k:v for k,v in meta.items() if k not in ['profile','lower_shot','upper_shot']},indent=2))

if __name__=='__main__':
    main()
