#!/usr/bin/env python3
"""Outward bounds for the COMPLETE angular sum in r24_scattering.md.

This consumes a validated Townes shooting bracket and interval ODE enclosure.
It does not treat a floating-point profile as a proof. Vector arithmetic uses
IEEE-754 binary64 basic operations, enlarged by nextafter at every operation;
transcendental constants use mpmath.iv. All Bessel and Laplace evaluations are
positive series with explicit geometric tails. No numerical quadrature rule
without a remainder is used: monotonicity gives upper/lower Riemann sums.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path

import mpmath as mp
import numpy as np

mp.iv.dps = 50
I = mp.iv.mpf
down = lambda x: np.nextafter(x, -np.inf)
up = lambda x: np.nextafter(x, np.inf)

def dec(x):
    """Outward float interval for an exact decimal or rational string."""
    f = float(Fraction(str(x)))
    return (down(f), up(f))

def exact(x):
    f = np.asarray(x, dtype=float)
    return (f, f)

def ivfloat(x):
    # float conversion is nearest; one extra ulp encloses the iv endpoints.
    return down(float(x.a)), up(float(x.b))

def add(a,b): return down(a[0]+b[0]), up(a[1]+b[1])
def sub(a,b): return down(a[0]-b[1]), up(a[1]-b[0])
def mul(a,b):
    assert np.all(a[0]>=0) and np.all(b[0]>=0)
    return np.maximum(0.,down(a[0]*b[0])), up(a[1]*b[1])
def div(a,b):
    assert np.all(a[0]>=0) and np.all(b[0]>0)
    return np.maximum(0.,down(a[0]/b[1])), up(a[1]/b[0])
def positive(a): return np.maximum(0.,a[0]), np.maximum(0.,a[1])
def sq(a): return mul(a,a)
def power(a,n):
    out=exact(1)
    for _ in range(n): out=mul(out,a)
    return out
def sum_positive(a,axis=-1):
    # Sequential addition, with explicit directed enlargement at each step.
    lo=np.moveaxis(a[0],axis,-1); hi=np.moveaxis(a[1],axis,-1)
    out=exact(np.zeros(lo.shape[:-1]))
    for j in range(lo.shape[-1]): out=positive(add(out,(lo[...,j],hi[...,j])))
    return out

def bessel(z,m,terms=72):
    """I_m(z), m=0 or1; tail after last positive term is geometric."""
    assert m in (0,1) and np.all(z[0]>=0)
    quarter=div(sq(z),exact(4))
    term=exact(np.ones_like(z[0])) if m==0 else div(z,exact(2))
    total=term
    for n in range(1,terms+1):
        term=div(mul(term,quarter),exact(n*(n+m)))
        total=positive(add(total,term))
    nxt=div(mul(term,quarter),exact((terms+1)*(terms+1+m)))
    rat=div(quarter,exact((terms+2)*(terms+2+m)))
    den=sub(exact(1),rat)
    assert np.all(den[0]>0)
    tail=div(nxt,den)
    return total[0], up(total[1]+tail[1])

def kernel(z,c0,c1):
    i0=bessel(z,0); i1=bessel(z,1); i02=bessel(mul(exact(2),z),0)
    var=positive(sub(i02,sq(i0)))
    return positive(add(mul(c0,var),mul(c1,sq(i1))))

def laplace(k,c0,c1,terms=4000):
    """Integral exp(-2r) kernel(k r) dr, positive exact coefficient series."""
    kk=sq(k); kn=exact(np.ones_like(k[0])); cn=exact(1)
    total=exact(np.zeros_like(k[0]))
    for n in range(1,terms+1):
        cn=mul(cn,div(exact(2*n-1),exact(2*n)))
        cn2=sq(cn)
        coef=div(add(mul(c0,positive(sub(cn,cn2))),
                     mul(c1,mul(cn2,div(exact(n),exact(n+1))))),exact(2))
        kn=mul(kn,kk)
        total=positive(add(total,mul(coef,kn)))
    # Every remaining coefficient is at most (c0+c1)/2.
    tail=div(mul(div(add(c0,c1),exact(2)),mul(kn,kk)),sub(exact(1),kk))
    return total[0],up(total[1]+tail[1])

def load_mesh(profile):
    p=profile['profile']; records=p['records']
    # The tiny first cell [0,.01] is bounded by the exact amplitude bracket.
    cells=[('0',p['first_node']['r'],p['a'][1])]
    for rec in records: cells.append((rec['r0'],rec['r1'],rec['q0'][1]))
    al,ah,bl,bh,ql,qh=[],[],[],[],[],[]
    for a,b,q in cells:
        aa=exact(0) if a=='0' else dec(a)
        bb=dec(b); qq=dec(q)
        al.append(aa[0]);ah.append(aa[1]);bl.append(bb[0]);bh.append(bb[1])
        ql.append(qq[0]);qh.append(qq[1])
    return (np.array(al),np.array(ah)),(np.array(bl),np.array(bh)),(np.array(ql),np.array(qh))

def hs_bound(a,b,q,R,D):
    q2=sq(q)
    fourth=sub(power(b,4),power(a,4))
    aincr=div(mul(q2,positive(fourth)),exact(4))
    cumulative=exact(0); outer=exact(0)
    for j in range(len(a[0])):
        if j==0:
            # Exact first-cell estimate, including the varying inner integral.
            outer=div(mul(sq((q2[0][0],q2[1][0])),
                          power((b[0][0],b[1][0]),4)),exact(32))
            cumulative=positive(add(cumulative,(aincr[0][j],aincr[1][j])))
            continue
        logratio=ivfloat(mp.iv.log(I([I(float(b[0][j])).a,I(float(b[1][j])).b])/
                                     I([I(float(a[0][j])).a,I(float(a[1][j])).b])))
        qj=(q2[0][j],q2[1][j])
        fourdiff=(fourth[0][j],fourth[1][j])
        correction=positive(sub(div(fourdiff,exact(4)),
                                 mul(power((a[0][j],a[1][j]),4),logratio)))
        inner=positive(add(mul(cumulative,logratio),
                           div(mul(qj,correction),exact(4))))
        outer=positive(add(outer,div(mul(qj,inner),exact(2))))
        cumulative=positive(add(cumulative,(aincr[0][j],aincr[1][j])))
    # A_infty <= A_R + D exp(-2R)(R^2/2+R/2+1/4).
    rr=dec(R); ee=ivfloat(mp.iv.exp(-2*I(str(R))))
    tailpoly=add(add(div(sq(rr),exact(2)),div(rr,exact(2))),dec('0.25'))
    ainf=add(cumulative,mul(mul(D,ee),tailpoly))
    thtail=div(mul(mul(D,ainf),ee),mul(exact(4),sq(rr)))
    theta2=add(outer,thtail)
    return theta2, ainf

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--profile',required=True)
    ap.add_argument('--shooting',required=True)
    ap.add_argument('--output',default='r24_certified_angular.json')
    ap.add_argument('--theta',default='0.55')
    ap.add_argument('--C',default='2.81')
    ap.add_argument('--k-start',default='0.02')
    ap.add_argument('--k-end',default='0.991')
    ap.add_argument('--k-step',default='0.001')
    args=ap.parse_args()
    profile=json.loads(Path(args.profile).read_text())
    shots=json.loads(Path(args.shooting).read_text())
    assert shots['bracket_success'] is True
    assert profile['profile']['a']==[shots['lower_shot']['a'][0],shots['upper_shot']['a'][1]]
    p=profile['profile']; R=Fraction(p['end_r']); U=I(p['end_q'][1])
    # Elementary K0 lower bound from its positive integral representation.
    ri=I(R.numerator)/I(R.denominator)
    klow=mp.iv.exp(-ri)*mp.iv.sqrt(mp.iv.pi/(2*ri))*(1-1/(8*ri))
    aa=mp.iv.sqrt(1-U*U); cc=3*aa+1
    Cbound=U/klow*mp.iv.exp(U*U/(2*aa)*(1/cc+1/(ri*cc*cc)))
    assert bool(Cbound<I(args.C)), (Cbound,args.C)
    C=dec(args.C); theta=dec(args.theta)
    D=div(mul(sq(C),ivfloat(mp.iv.pi)),exact(2))
    a,b,q=load_mesh(profile)
    theta2,ainf=hs_bound(a,b,q,R,D)
    assert theta2[1]<sq(theta)[0],(theta2,sq(theta))
    c0=div(exact(1),sub(exact(1),div(theta,exact(2))))
    c1=positive(sub(div(exact(2),sub(exact(1),theta)),mul(exact(2),c0)))
    width=positive(sub(b,a)); radial=div(positive(sub(sq(b),sq(a))),exact(2))
    q2=sq(q)
    expb=tuple(np.array([ivfloat(mp.iv.exp(-2*I(float(x))))[i]
                         for x in b[1]]) for i in [0,1])
    # expb uses the upper endpoint of b, so its lower bound is valid throughout cell.
    start,end,step=map(Fraction,[args.k_start,args.k_end,args.k_step])
    lower=[];upper=[];cur=start
    while cur<end:
        nxt=min(cur+step,end);lower.append(cur);upper.append(nxt);cur=nxt
    k=(np.array([dec(x)[0] for x in upper]),np.array([dec(x)[1] for x in upper]))
    whole=laplace(k,c0,c1)
    values=[]
    for base in range(0,len(upper),32):
        sl=slice(base,base+32)
        kb=(k[0][sl,None],k[1][sl,None])
        highker=kernel(mul(kb,(b[0][None,:],b[1][None,:])),c0,c1)
        lowker=kernel(mul(kb,(a[0][None,:],a[1][None,:])),c0,c1)
        core=sum_positive(mul(mul((q2[0][None,:],q2[1][None,:]),
                                   (radial[0][None,:],radial[1][None,:])),highker))
        lowlap=sum_positive(mul(mul((expb[0][None,:],expb[1][None,:]),
                                     (width[0][None,:],width[1][None,:])),lowker))
        tail=mul(D,positive(sub((whole[0][sl],whole[1][sl]),lowlap)))
        total=positive(add(core,tail))
        for j,val in enumerate(total[1]):
            idx=base+j; lf=lower[idx]
            ell=ivfloat(mp.iv.log(I(lf.denominator)/I(lf.numerator)))
            certified=float(up(val*ell[1]))
            values.append({'k_lower':str(lf),'k_upper':str(upper[idx]),
                           'log_H_upper':certified})
        print(json.dumps({'cells_done':len(values),'maximum':max(v['log_H_upper'] for v in values)}),flush=True)
    # Explicit global-envelope endpoint bounds from r24_scattering.md.
    ci=I(args.C); ti=I(args.theta); k0=I(args.k_start); k1=I(args.k_end)
    small=ci**2*mp.iv.pi*k0**2*mp.iv.log(1/k0)/(16*(1-ti)*(1-k0)**3)
    large=ci**2*mp.iv.pi*mp.iv.sqrt(1-k1)/(4*(1-ti)*k1**2*mp.iv.sqrt(1+k1))
    mx=max(v['log_H_upper'] for v in values)
    ok=bool(mx<1 and small.b<1 and large.b<1)
    out={'status':'completed rigorous enclosure under stated IEEE-754 and mpmath.iv arithmetic assumptions' if ok else 'bound does not close',
         'all_k_bound_closes':ok,'profile_source':args.profile,'shooting_source':args.shooting,
         'profile_C_upper':float(up(float(Cbound.b))),'C_used':args.C,'theta_used':args.theta,
         'theta_squared_upper':float(theta2[1]),'theta_upper':float(up(np.sqrt(theta2[1]))),
         'small_endpoint_upper':float(up(float(small.b))),'large_endpoint_upper':float(up(float(large.b))),
         'compact_max_upper':mx,'maximizing_cell':max(values,key=lambda x:x['log_H_upper']),
         'cell_count':len(values),'radial_cells':len(a[0]),'cells':values}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cells'},indent=2))

if __name__=='__main__': main()
