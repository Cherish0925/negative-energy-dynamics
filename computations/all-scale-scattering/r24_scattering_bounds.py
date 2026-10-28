"""Quantitative companion to r24_scattering.md.

Floating-point exploration of an ANALYTIC upper bound, not an interval proof.
No scattering ODE or spectrum truncation is used in this bound.
"""
import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_bvp, quad, cumulative_trapezoid
from scipy.optimize import minimize_scalar
from scipy.special import k0, k1, ive, kve

def run():
    r = np.linspace(0, 35, 1601)
    v = 2.2 / np.cosh(r)
    sol = solve_bvp(
        lambda x, y: np.vstack((y[1], y[0] - y[0] ** 3)),
        lambda a, b: np.array([a[1], b[1] + k1(35) / k0(35) * b[0]]),
        r, np.vstack((v, -v * np.tanh(r))),
        S=np.array([[0., 0.], [0., -1.]]), tol=1e-11, max_nodes=40000)
    assert sol.success and sol.y[0, 0] > 2
    btail = float(sol.sol(18)[0] / k0(18))
    x = np.linspace(1e-6, 40, 160001)
    v2 = np.where(x < 18, sol.sol(x)[0] ** 2,
                  btail ** 2 * kve(0, x) ** 2 * np.exp(-2*x))
    mass = float(2*np.pi*np.trapezoid(x*v2, x))
    hs = {}
    for m in range(1, 9):
        accum = cumulative_trapezoid(x**(2*m+1)*v2, x, initial=0)
        hs[m] = float(np.sqrt(np.trapezoid(x**(1-2*m)*v2*accum, x)/(2*m*m)))

    def integrals(k, L):
        end = max(80., 20/(1-k))
        def weight(r):
            if r < 18:
                return r*float(sol.sol(r)[0])**2*np.exp(2*k*r)
            return r*btail**2*kve(0, r)**2*np.exp(-2*(1-k)*r)
        born = [quad(lambda r: weight(r)*ive(m,k*r)**2, 0, end,
                     epsabs=1e-10, epsrel=2e-10)[0]
                for m in range(1, L+1)]
        total = quad(lambda r: weight(r)*(ive(0,2*k*r)-ive(0,k*r)**2),
                     0, end, epsabs=1e-10, epsrel=2e-10)[0]
        return born, total

    def bound(k, L):
        born, total = integrals(k, L)
        # ||B_m(0)||_HS <= hs[1]/m, so this controls every omitted mode.
        tailden = 1-hs[1]/(L+1)
        upper = 2*sum(born[m-1]/(1-hs[m]) for m in range(1,L+1))
        upper += (total-2*sum(born))/tailden
        return float(upper)

    results = []
    for L in (1,2,4,8):
        ans = minimize_scalar(lambda k: -np.log(1/k)*bound(k,L),
                              bounds=(.01,.995), method='bounded',
                              options={'xatol':1e-8})
        results.append({'L':L, 'candidate_max_k':float(ans.x),
                        'candidate_max_log_weighted_bound':float(-ans.fun),
                        'candidate_margin_to_one':float(1+ans.fun)})
    rows = [{'k':k, 'H4':bound(k,4),
             'log_weighted_H4':float(np.log(1/k)*bound(k,4))}
            for k in (.01,.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95,.98,.99)]
    out={'status':'floating-point analytic-bound exploration; no interval certification',
         'Q0':float(sol.sol(0)[0]), 'M':mass, 'HS0':hs,
         'optimization':results, 'rows':rows}
    Path('research/r24_scattering_bounds.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    run()
