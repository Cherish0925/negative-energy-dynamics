"""Numerical consistency check of analytic two-Townes interaction asymptotics.

This is floating-point quadrature, not an interval proof or a counterexample.
Run from this computation directory. Dependencies: numpy, scipy.
"""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp, quad
from scipy.special import k0, k1, k0e, i0, i0e
from numpy.polynomial.legendre import leggauss

def main():
    end = 35.0
    r = np.linspace(0, end, 1201)
    initial = 2.2 / np.cosh(r)
    guess = np.vstack((initial, -initial * np.tanh(r)))
    sol = solve_bvp(
        lambda x, y: np.vstack((y[1], y[0] - y[0] ** 3)),
        lambda left, right: np.array([left[1], right[1] + k1(end)/k0(end)*right[0]]),
        r, guess, S=np.array([[0., 0.], [0., -1.]]),
        tol=2e-10, max_nodes=30000,
    )
    if not sol.success or sol.y[0, 0] < 2:
        raise RuntimeError(sol.message)
    mass = 2*np.pi*quad(lambda x: x*sol.sol(x)[0]**2, 0, end,
                         epsabs=1e-10, epsrel=1e-11, limit=300)[0]
    # Exact Bessel tail beyond 18; omitted nonlinear correction is exponentially small.
    # Differential-equation residual is not a certified error enclosure.
    join = 18.0
    bessel_coeff = float(sol.sol(join)[0]/k0(join))
    tail_a = bessel_coeff*np.sqrt(np.pi/2)/np.sqrt(mass)
    def q(x):
        x = np.asarray(x)
        return np.where(x <= join, sol.sol(np.minimum(x,join))[0],
                        bessel_coeff*k0(np.maximum(x,join)))/np.sqrt(mass)
    c1 = 2/mass
    rows=[]
    for order in (192, 320):
        nodes, weights = leggauss(order)
        nu=np.pi*(nodes+1)
        wnu=np.pi*weights
        for distance in (8.,12.,16.,24.,32.,48.,64.):
            # Elliptic coordinates with foci +/- distance/2; tails extend 30 units.
            mumax=np.arccosh(1+60/distance)
            mu=(nodes+1)*mumax/2
            wmu=weights*mumax/2
            cm=np.cosh(mu)[:,None]
            cn=np.cos(nu)[None,:]
            qa=q(distance/2*(cm-cn))
            qb=q(distance/2*(cm+cn))
            jac=(distance/2)**2*(np.sinh(mu)[:,None]**2+np.sin(nu)[None,:]**2)
            weight=jac*wmu[:,None]*wnu[None,:]
            overlap=float(np.sum(weight*qa*qb))
            cubic=float(np.sum(weight*qa**3*qb))
            quartic=float(np.sum(weight*qa**2*qb**2))
            deficit=(4*overlap*cubic*(1+overlap**2)
                     -2*quartic*(1+2*overlap**2)-2*c1*overlap**4)/(1-overlap**2)**2
            e=np.exp(-distance)
            rows.append(dict(order=order,R=distance,s=overlap,j=cubic,b22=quartic,
                deficit=deficit,
                s_ratio=overlap/(np.sqrt(2*np.pi)*tail_a**2*np.sqrt(distance)*e),
                j_ratio=cubic/(np.sqrt(8*np.pi)*tail_a**2/mass/np.sqrt(distance)*e),
                b22_ratio=quartic/(np.pi**1.5*tail_a**4/np.sqrt(distance)*e**2),
                deficit_ratio=deficit/(16*np.pi*tail_a**4/mass*e**2)))
    moment_rows=[]
    for k in np.concatenate((np.linspace(0,.95,39),[.98,.99,.995])):
        i3=2*np.pi*quad(lambda x: x*float(q(x))**3*i0(k*x),0,35,
                       epsabs=1e-11,epsrel=1e-10)[0]
        i1=mass*i3/(1-k*k)
        i2core=2*np.pi*quad(lambda x: x*float(q(x))**2*i0(2*k*x),0,join,
                           epsabs=1e-11,epsrel=1e-10)[0]
        i2tail=2*np.pi*bessel_coeff**2/mass*quad(
            lambda x: x*k0e(x)**2*i0e(2*k*x)*np.exp(-2*(1-k)*x),
            join,np.inf,epsabs=1e-11,epsrel=1e-10)[0]
        g=(1-k*k)*i1*i1/mass-i2core-i2tail
        moment_rows.append(dict(k=float(k),I1=i1,I2=i2core+i2tail,G=g))
    output=dict(method='radial BVP and independent elliptic-coordinate Gauss quadrature',
        status='floating-point consistency check; not interval-certified',
        q0=float(sol.y[0,0]),mass=mass,c1=c1,normalized_tail_a=tail_a,
        bvp_max_rms_residual=float(sol.rms_residuals.max()),nodes=sol.x.size,
        unequal_scale_moments=moment_rows,rows=rows)
    Path('r22_interaction_check.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('rows','unequal_scale_moments')},indent=2))
    print('Unequal-scale G(k) sampled minimum:',min(z['G'] for z in moment_rows))
    for z in rows:
        if z['order']==320:
            print('R={R:2.0f} s/asym={s_ratio:.7f} j/asym={j_ratio:.7f} '
                  'b/asym={b22_ratio:.7f} D/asym={deficit_ratio:.7f}'.format(**z))

if __name__=='__main__':
    main()
