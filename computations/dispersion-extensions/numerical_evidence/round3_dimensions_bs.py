"""Numerical preconditioned/Birman--Schwinger gaps for the N3 candidate."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json
from scipy.interpolate import PPoly
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh,splu,LinearOperator
src=np.load('round3_dimensions_N3_mode4_R50_e0.005_stable.npz');q=PPoly.construct_fast(src['q_c'],src['q_x'],axis=1);p=8/3;R=40.;h=.01;n=int(R/h)-1;r=np.arange(1,n+1)*h;pot=abs(q(r)[0])**p;rows=[]
for name,c,ells in [('plus',p+1,list(range(0,21,2))),('minus',1,list(range(1,14,2)))]:
 for ell in ells:
  H=diags([-np.ones(n-1)/h**2,2*np.ones(n)/h**2+ell*(ell+1)/r**2,-np.ones(n-1)/h**2],[-1,0,1],format='csc');A=H@H+diags(np.ones(n),format='csc');lu=splu(A);vv=np.sqrt(c*pot);C=LinearOperator((n,n),matvec=lambda z:vv*lu.solve(vv*z));mu=np.sort(eigsh(C,k=10,which='LM',return_eigenvectors=False,tol=2e-10))[::-1]
  row=dict(channel=name,c=c,ell=ell,R=R,h=h,BS_top10=mu.tolist(),gap_sampled=float(min(abs(mu-1))));rows.append(row);print(json.dumps(row),flush=True)
  open('round3_dimensions_N3_bs.json','w').write(json.dumps(rows,indent=2))
