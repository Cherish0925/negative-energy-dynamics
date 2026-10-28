import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time
from fractions import Fraction
from scipy.interpolate import BPoly
from scipy.integrate import solve_bvp
from numpy.polynomial.legendre import leggauss
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'round2_radial_H4_exact_h1_16.json').read_text());xs=np.array([float(Fraction(*v)) for v in raw['nodes']]);jets=np.array([[float.fromhex(v) for v in row] for row in raw['jets_hex']]);bp=BPoly.from_derivatives(xs,jets)
def qfun(r):return np.where(r<36,bp(np.minimum(r,36)),0)
def ffun(r):return np.where(r<36,bp(np.minimum(r,36))/2+r*bp(np.minimum(r,36),1)/4,0)
rows=[]
for R,tol in [(30,1e-7),(40,1e-8),(50,1e-8)]:
 st=time.time();r=np.linspace(0,R,2001);y=np.zeros((5,len(r)))
 S=np.zeros((5,5));S[1,1]=S[3,3]=-3
 def fun(r,y,p):return np.array([y[1],y[2],y[3],(qfun(r)**2-1)*y[0]+ffun(r)+p[0]*qfun(r),y[0]*qfun(r)*r**3])
 def bc(a,b,p):return np.r_[a[1],a[3],b[0],b[1],a[4],b[4]]
 sol=solve_bvp(fun,bc,r,y,p=[0.],S=S,tol=tol,max_nodes=50000)
 g,w=leggauss(16);mid=(sol.x[:-1]+sol.x[1:])/2;half=np.diff(sol.x)/2;rr=mid[:,None]+half[:,None]*g;z=sol.sol(rr.flatten())[0].reshape(rr.shape)
 gamma=2*np.pi**2*np.sum(half[:,None]*w*(ffun(rr)*z*rr**3))
 row={'R':R,'tol':tol,'success':sol.success,'nodes':len(sol.x),'gamma':gamma,'max_rms_residual':float(max(sol.rms_residuals)),'saddle_multiplier':float(sol.p[0]),'seconds':time.time()-st}
 rows.append(row);print(json.dumps(row),flush=True)
 np.savez(ROOT/f'round4_radial_dynamics_chain_R{R}.npz',x=sol.x,y=sol.y,yp=sol.yp,coeff=sol.sol.c,alpha=sol.p)
 (ROOT/'round4_radial_dynamics_chain.json').write_text(json.dumps(rows,indent=2))
