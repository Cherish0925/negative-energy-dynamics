import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from scipy.special import roots_laguerre,eval_genlaguerre,gammaln
from scipy.interpolate import CubicSpline
from scipy.linalg import block_diag,null_space,eigh
z=np.load('r24_shell.npz');fs=CubicSpline(z['r'],z['f']);gs=CubicSpline(z['r'],z['g']);e=z['e'].item()
results=[]
for d in (18,30,45,60):
 mmax=3;L=2.; x,w=roots_laguerre(180);r=L*np.sqrt(x);nt=32;th=np.arange(nt)*2*np.pi/nt
 parts=[];ks=[]
 for m in range(mmax+1):
  n=np.arange(d+1);off=np.sqrt((n[:-1]+1)*(n[:-1]+m+1));K=(np.diag(2*n+m+1.)+np.diag(off,1)+np.diag(off,-1))/L**2
  B=np.stack([x**(m/2)*eval_genlaguerre(j,m,x)*np.exp(.5*(gammaln(j+1)-gammaln(j+m+1))) for j in n],axis=1)/(np.sqrt(np.pi)*L)
  for a in ([np.ones(nt)] if m==0 else [np.sqrt(2)*np.cos(m*th),np.sqrt(2)*np.sin(m*th)]):
   parts.append((B[:,None,:]*a[None,:,None]).reshape(-1,d+1));ks.append(K)
 B=np.concatenate(parts,axis=1);K=block_diag(*ks);dim=K.shape[0]
 # Product B_i B_j includes e^-x; Gauss weight already carries it.
 W=np.repeat(np.pi*L**2*w/nt,nt); U=np.stack([np.repeat(fs(r),nt),(gs(r)[:,None]*np.cos(th)).ravel(),(gs(r)[:,None]*np.sin(th)).ravel()],axis=1);rho=(U*U).sum(1)
 H=block_diag(*[K+ee*np.eye(dim) for ee in [1,e,e]])
 VR=B.T@((W*rho)[:,None]*B)
 for i in range(3):
  for j in range(3):
   H[i*dim:(i+1)*dim,j*dim:(j+1)*dim]-=2*B.T@((W*U[:,i]*U[:,j])[:,None]*B)+(VR if i==j else 0)
 # <basis,u> has e^-x/2, cancel half the quadrature exponential.
 coef=B.T@((W*np.repeat(np.exp(x/2),nt))[:,None]*U)
 C=[]
 for i in range(3):
  for j in range(i,3):
   row=np.zeros(3*dim);row[i*dim:(i+1)*dim]+=coef[:,j];row[j*dim:(j+1)*dim]+=coef[:,i];C.append(row)
 Z=null_space(np.array(C));vals=eigh(Z.T@H@Z,subset_by_index=[0,9],eigvals_only=True)
 results.append(dict(degree=d,lowest=vals.tolist()))
 print(d,vals,flush=True)

import json
open('r24_hessian_results.json','w').write(json.dumps(results,indent=2))
