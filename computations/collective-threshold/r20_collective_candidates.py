# R20 collective periodic exploratory search.
# Numerical lower-bound candidates; quadrature is not certified.
# Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1.
import numpy as np
from scipy.linalg import eigvalsh
from scipy.optimize import differential_evolution, minimize
import time, json

# Bloch potential V=c+a(cos x+cos y)+b(cos2x+cos2y).
# Plane waves on period 2pi with k in [-1/2,1/2).
def evaluate_separable(params, nk=24, ncut=12, clip=False, return_details=False):
    c,a,b=params
    k=(np.arange(nk)+.5)/nk-.5
    ell=np.arange(-ncut,ncut+1)
    off=np.zeros((2*ncut+1,2*ncut+1))
    for d,amp in [(1,a),(2,b)]:
        for j in range(len(ell)-d):off[j,j+d]=off[j+d,j]=-amp/2
    ens=np.concatenate([eigvalsh(off+np.diag((ell+x)**2)) for x in k])
    # all combos but truncate levels unable to contribute
    ens=ens[ens<c-ens.min()]
    neg=np.maximum(c-ens[:,None]-ens[None,:],0)
    numerator=neg.sum()/nk**2/(2*np.pi)**2
    if clip:
        th=2*np.pi*(np.arange(256)+.5)/256
        ss=a*np.cos(th)+b*np.cos(2*th)
        den=np.mean(np.maximum(c+ss[:,None]+ss[None,:],0)**2)
    else:den=c*c+a*a+b*b
    den=max(den,1e-100)
    return (numerator/den, numerator,den) if return_details else numerator/den

import numpy as np
from scipy.linalg import eigvalsh
from scipy.optimize import differential_evolution,minimize
import time,json

def evaluate_gaussian(p,ncut=6,nk=4,ngrid=128):
 A,sig,b=p;c=A*b
 if A<=0 or sig<=0:return 0.
 ell=np.arange(-ncut,ncut+1); xx,yy=np.meshgrid(ell,ell,indexing='ij'); m=np.stack([xx.ravel(),yy.ravel()],1)
 dd=((m[:,None,:]-m[None,:,:])**2).sum(2)
 pot=A*sig**2/(2*np.pi)*np.exp(-.5*sig**2*dd)
 es=0.
 k=(np.arange(nk)+.5)/(2*nk)
 for i in range(nk):
  for j in range(i,nk):
   H=np.diag(((m+[k[i],k[j]])**2).sum(1)-c)-pot
   ev=eigvalsh(H,subset_by_value=(-max(1.,A*(abs(b)+5)),0),driver='evr')
   es-=ev.sum()*(1 if i==j else 2)
 es/=nk**2*(2*np.pi)**2
 x=2*np.pi*(np.arange(ngrid)+.5)/ngrid-np.pi
 g=sum(np.exp(-.5*((x+2*np.pi*s)/sig)**2) for s in range(-3,4))
 den=np.mean(np.maximum(c+A*g[:,None]*g[None,:],0)**2)
 return es/max(den,1e-100)

if __name__ == '__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--search',action='store_true')
    args=parser.parse_args()
    if args.search:
        opt=differential_evolution(lambda p:-evaluate_gaussian(p),[(.01,35),(.25,2.8),(-.8,.25)],maxiter=25,popsize=5,seed=12,polish=False,tol=1e-6)
        opt=minimize(lambda p:-evaluate_gaussian(p,ncut=8,nk=7),opt.x,method='Nelder-Mead',options={'maxiter':90,'fatol':1e-8})
        p=opt.x.tolist()
    else:
        p=[2.9414883,0.73521703,0.01513357]
    results={'status':'numerical candidates, not certified inequalities', 'gaussian_parameters':p, 'gaussian_checks':[], 'separable_checks':[]}
    for ncut,nk in [(8,12),(12,12),(16,12),(12,24)]:
        z={'ncut':ncut,'positive_quadrant_bloch_n':nk,'ratio':float(evaluate_gaussian(p,ncut=ncut,nk=nk,ngrid=512))}
        results['gaussian_checks'].append(z);print(z,flush=True)
    sp=[2.00054357,0.7283338,0.08201107]
    results['separable_parameters']=sp
    for nk in [40,80,160]:
        z={'bloch_n':nk,'ratio':float(evaluate_separable(sp,nk=nk,ncut=22,clip=True))}
        results['separable_checks'].append(z);print(z,flush=True)
    with open('research/r20_collective_candidates_results.json','w') as f:json.dump(results,f,indent=2)
