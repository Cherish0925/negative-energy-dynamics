"""Whole-plane Hermite Galerkin search for the 2D orthonormal kinetic quotient.
All integrals are polynomial Gaussian quadratures exact in exact arithmetic;
there is no periodic box or zero-kinetic constant mode. Finite calculations
are exploratory, not interval-certified. OPENBLAS_NUM_THREADS=1 recommended.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np, scipy.linalg as la, scipy.optimize as so
from scipy.special import roots_hermite, eval_hermite, gammaln
import json, time, argparse
TARGET=0.17092707344864

def basis(cut,qextra=3):
    ix=np.array([(a,d-a) for d in range(cut+1) for a in range(d+1)],int)
    z,w=roots_hermite(2*cut+qextra);x=z/np.sqrt(2)
    P=np.stack([eval_hermite(n,x)*np.exp(-.5*(n*np.log(2)+gammaln(n+1)))/np.pi**.25 for n in range(cut+1)],axis=1)
    B=(P[:,None,ix[:,0]]*P[None,:,ix[:,1]]).reshape(len(x)**2,-1)
    weights=np.outer(w,w).ravel()/2
    # Absorb quadrature weights to avoid huge intermediate polynomial values.
    # If Z=weights^(1/4) B C then integral rho^2 = sum (sum |Z|^2)^2.
    D=B*weights[:,None]**.25
    K=np.diag(ix.sum(axis=1)+1.).astype(float)
    lookup={tuple(k):j for j,k in enumerate(ix)}
    for j,k in enumerate(ix):
      for axis in (0,1):
        kk=k.copy();kk[axis]+=2
        if tuple(kk) in lookup:
          l=lookup[tuple(kk)];K[j,l]=K[l,j]=-.5*np.sqrt((k[axis]+1)*(k[axis]+2))
    return ix,D,K,x

def seed(ix,N,kind,rng):
    m=len(ix)
    if kind=='shell':
      A=np.eye(m,N)+.01*rng.normal(size=(m,N))*np.exp(-ix.sum(axis=1)[:,None]/4)
    elif kind=='random':
      A=rng.normal(size=(m,N))*np.exp(-ix.sum(axis=1)[:,None]/3)
    elif kind=='complex':
      A=(rng.normal(size=(m,N))+1j*rng.normal(size=(m,N)))*np.exp(-ix.sum(axis=1)[:,None]/3)
    elif kind=='multicore':
      radius=1.8 if N<4 else 2.5
      theta=2*np.pi*np.arange(N)/N+.21
      centers=np.stack([radius*np.cos(theta),radius*np.sin(theta)],1)
      if N==1:centers*=0
      A=np.stack([np.exp(-np.dot(c,c)/4)*np.prod((c/np.sqrt(2))[None,:]**ix*np.exp(-.5*gammaln(ix+1)),axis=1) for c in centers],axis=1)
      A+=.002*rng.normal(size=A.shape)*np.exp(-ix.sum(axis=1)[:,None]/3)
    return la.qr(A,mode='economic')[0]

def optimize(cut,N,kind,seednum=1,steps=700,initial=None,tag=''):
    ix,D,K,x=basis(cut);rng=np.random.default_rng(seednum)
    A=seed(ix,N,kind,rng) if initial is None else initial
    isc=np.iscomplexobj(A);shape=A.shape;m=A.size
    def pack(A):return np.r_[A.real.ravel(),A.imag.ravel()] if isc else A.ravel()
    def unpack(a):return (a[:m]+1j*a[m:]).reshape(shape) if isc else a.reshape(shape)
    def calc(a,details=False):
      A=unpack(a);ee,V=la.eigh(A.conj().T@A);H=(V/np.sqrt(np.maximum(ee,1e-16)))@V.conj().T;C=A@H
      Z=D@C;rho=np.sum(abs(Z)**2,axis=1);F=np.dot(rho,rho);KC=K@C;T=np.vdot(C,KC).real;R=F/T
      G=-(4*D.T@(rho[:,None]*Z)-2*R*KC)/T
      G=(G-C@(C.conj().T@G))@H
      if details:return C,dict(quotient=float(R),F=float(F),T=float(T),orth_error=float(la.norm(C.conj().T@C-np.eye(N))),gradnorm=float(la.norm(G)),edge_weight=float(np.sum(abs(C[ix.sum(axis=1)>=cut-2])**2)/N))
      return -R,pack(G)
    a=pack(A);direction=rng.normal(size=a.size);direction/=la.norm(direction);eps=1e-5
    f,g=calc(a);fd=(calc(a+eps*direction)[0]-calc(a-eps*direction)[0])/(2*eps)
    gradcheck=abs(fd-np.dot(g,direction));start=time.time()
    opt=so.minimize(calc,a,jac=True,method='L-BFGS-B',options=dict(maxiter=steps,ftol=2e-13,gtol=1e-8,maxls=30,maxcor=15))
    C,result=calc(opt.x,True)
    result.update(cut=cut,rank=N,kind=kind,seed=seednum,iterations=int(opt.nit),message=str(opt.message),success=bool(opt.success),seconds=time.time()-start,gradcheck=float(gradcheck),relative_gap=float((TARGET-result['quotient'])/TARGET))
    path=f'research/r21_orbital_{tag}{kind}_n{N}_c{cut}_s{seednum}.npz';np.savez_compressed(path,C=C,ix=ix)
    result['coefficients']=path
    print(json.dumps(result),flush=True)
    return result,C

if __name__=='__main__':
  p=argparse.ArgumentParser();p.add_argument('--cut',type=int,default=16);p.add_argument('--steps',type=int,default=700);p.add_argument('--ranks',default='1,2,3,4,6');p.add_argument('--kinds',default='shell,random,multicore,complex');p.add_argument('--seed',type=int,default=21);p.add_argument('--output',default='research/r21_orbital_results.json');a=p.parse_args()
  results=[]
  for N in map(int,a.ranks.split(',')):
    for kind in a.kinds.split(','):
      if N==1 and kind!='shell':continue
      r,C=optimize(a.cut,N,kind,a.seed,a.steps);results.append(r)
      with open(a.output,'w') as f:json.dump(results,f,indent=2)
