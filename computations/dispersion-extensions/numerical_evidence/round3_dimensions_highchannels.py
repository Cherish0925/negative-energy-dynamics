"""N3 mass-critical channel spectra via independent radial finite differences.
Numerical diagnostics only, not eigenvalue enclosures on the half-line.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json
from scipy.interpolate import PPoly
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from scipy.linalg import eigvals_banded
N=3;p=8/N;src=np.load('round3_dimensions_N3_mode4_R50_e0.005_stable.npz');q=PPoly.construct_fast(src['q_c'],src['q_x'],axis=1);out=[]
for R,h in [(40.,.01)]:
 n=int(R/h)-1;r=np.arange(1,n+1)*h;V=abs(q(r)[0])**p
 for label,c,ells in [('plus',p+1,[8,10,12,14,16,18,20]),('minus',1,[9,11,13,15])]:
  for ell in ells:
   cent=(N-1)*(N-3)/4+ell*(ell+N-2)
   H=diags([-np.ones(n-1)/h**2,2*np.ones(n)/h**2+cent/r**2,-np.ones(n-1)/h**2],[-1,0,1],format='csc');A=H@H+diags(1-c*V,format='csc')
   ev=np.sort(eigsh(A,k=8,sigma=0.,which='LM',return_eigenvectors=False,tol=1e-9));ab=np.zeros((3,n));ab[2]=A.diagonal();ab[1,1:]=A.diagonal(1);ab[0,2:]=A.diagonal(2);neg=eigvals_banded(ab,lower=False,select='v',select_range=(-1000,0),check_finite=False)
   row=dict(N=N,p=p,channel=label,c=c,ell=ell,R=R,h=h,nearzero_eigs=ev.tolist(),min_abs_nearzero=float(min(abs(ev))),negative_count=len(neg),negative_eigs=neg.tolist());out.append(row);print(json.dumps(row),flush=True)
   open('round3_dimensions_N3_highchannels.json','w').write(json.dumps(out,indent=2))
