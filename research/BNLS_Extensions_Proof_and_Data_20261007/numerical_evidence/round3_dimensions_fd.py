"""Independent finite differences for l=1 susceptibility; floating-point only."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,sys
from scipy.interpolate import PPoly
from scipy.sparse import diags
from scipy.sparse.linalg import splu,eigsh
from scipy.linalg import eigvals_banded
from scipy.special import gamma
outs=[]
for d,mode in [(3,4),(5,1)]:
 a=np.load(f'round3_dimensions_N{d}_mode{mode}_R50_e0.005_stable.npz');qp=PPoly.construct_fast(a['q_c'],a['q_x'],axis=1,extrapolate=False);p=8/d;surf=2*np.pi**(d/2)/gamma(d/2)
 for R,h in [(40.,.04),(40.,.02),(40.,.01),(40.,.005),(50.,.01)]:
  n=int(R/h)-1;r=np.arange(1,n+1)*h;q=qp(r);H=diags([-np.ones(n-1)/h**2,2*np.ones(n)/h**2+(d*d-1)/(4*r*r),-np.ones(n-1)/h**2],[-1,0,1],format='csc');L=H@H+diags(1-abs(q[0])**p,format='csc');rhs=r**((d-1)/2)*q[1];lu=splu(L);z=lu.solve(rhs);I=surf/d*h*np.dot(rhs,z)
  ev=np.sort(eigsh(L,k=6,sigma=0.,which='LM',return_eigenvectors=False,tol=2e-9));ab=np.zeros((3,n));ab[2]=L.diagonal();ab[1,1:]=L.diagonal(1);ab[0,2:]=L.diagonal(2);neg=eigvals_banded(ab,lower=False,select='v',select_range=(-500,0),check_finite=False)
  row=dict(N=d,mode=mode,p=p,R=R,h=h,n=n,I_fd=float(I),nearzero_eigs=ev.tolist(),negative_eigs=neg.tolist(),residual_norm=float(np.linalg.norm(L@z-rhs)*np.sqrt(h)))
  print(json.dumps(row),flush=True);outs.append(row);np.savez_compressed(f'round3_dimensions_fd_N{d}_R{int(R)}_h{h:.4f}.npz',r=r,z=z,rhs=rhs,eigenvalues=ev,negative_eigenvalues=neg)
  open('round3_dimensions_fd_results.json','w').write(json.dumps(outs,indent=2))
