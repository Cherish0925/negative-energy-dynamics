"""Partial-wave calculation for the unequal-scale spectral interaction.

Exploratory floating-point calculation; no certified ODE errors.
"""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp, quad
from scipy.special import k0,k1,ive,kve

def run():
    r=np.linspace(0,35,1201)
    v=2.2/np.cosh(r)
    sol=solve_bvp(lambda x,y:np.vstack((y[1],y[0]-y[0]**3)),
        lambda a,b:np.array([a[1],b[1]+k1(35)/k0(35)*b[0]]),
        r,np.vstack((v,-v*np.tanh(r))),S=np.array([[0.,0.],[0.,-1.]]),
        tol=2e-10,max_nodes=30000)
    assert sol.success and sol.y[0,0]>2
    b=float(sol.sol(18)[0]/k0(18))
    def potential(x):
        return float(sol.sol(x)[0])**2 if x<=18 else b*b*kve(0,x)**2*np.exp(-2*x)
    rows=[]
    for k in (.1,.3,.5,.7,.85,.9):
        end=max(40,20/(1-k))
        modes=[]
        for mode in range(41):
            start=1e-5
            c=(k*k-potential(0))/(4*(mode+1))
            def fun(x,y):
                z,p,J=y
                v=potential(x)
                if x<=18:
                    source=v*ive(mode,k*x)*np.exp(k*x)
                else:
                    source=b*b*kve(0,x)**2*ive(mode,k*x)*np.exp(-(2-k)*x)
                return [p,-(2*mode+1)*p/x+(k*k-v)*z,
                        x**(mode+1)*source*z]
            ans=solve_ivp(fun,(start,end),[1+c*start**2,2*c*start,0.],
                          rtol=2e-10,atol=1e-12,method='DOP853',max_step=.25)
            assert ans.success
            z,p,J=ans.y[:,-1]
            yy=end**mode*z
            yp=end**mode*p+(mode*end**(mode-1)*z if mode else 0)
            kval=kve(mode,k*end)*np.exp(-k*end)
            kp=-.5*k*(kve(abs(mode-1),k*end)+kve(mode+1,k*end))*np.exp(-k*end)
            cI=end*(yp*kval-yy*kp)
            am=J/cI
            modes.append(dict(m=mode,a=am,cI=cI,steps=len(ans.t)))
        partial={str(L):2*np.pi*(modes[0]['a']+2*sum(z['a'] for z in modes[1:L+1]))
                 for L in (8,16,24,32,40)}
        row=dict(k=k,modes=modes,partial_sums=partial)
        rows.append(row)
        print('k',k,'T partial',partial,flush=True)
        Path('r22_scattering_check.json').write_text(json.dumps(dict(
            status='exploratory non-interval partial-wave calculation',
            normalization='Q solves -Delta Q+Q-Q^3=0; T=2pi(a0+2sum a_m)',
            rows=rows),indent=2)+'\n')

if __name__=='__main__':
    run()
