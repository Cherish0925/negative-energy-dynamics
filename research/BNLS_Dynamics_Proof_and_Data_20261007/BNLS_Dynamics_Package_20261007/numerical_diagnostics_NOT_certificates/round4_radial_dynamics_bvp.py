import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time
from fractions import Fraction
from scipy.interpolate import BPoly,CubicSpline
from scipy.integrate import solve_bvp
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'round2_radial_H4_exact_h1_16.json').read_text());xs=np.array([float(Fraction(*v)) for v in raw['nodes']]);jets=np.array([[float.fromhex(v) for v in row] for row in raw['jets_hex']]);bp=BPoly.from_derivatives(xs,jets)
def qfun(r):return np.where(r<36,bp(np.minimum(r,36)),0)
z=np.load(ROOT/'round4_radial_dynamics_quartet_vector.npz');rr=z['r'];av=z['real_component']/rr**1.5;bv=z['imag_component']/rr**1.5
ca=CubicSpline(np.r_[0,rr,40],np.r_[av[0],av,0],bc_type=((1,0),(1,0)));cb=CubicSpline(np.r_[0,rr,40],np.r_[bv[0],bv,0],bc_type=((1,0),(1,0)))
rows=[];previous=None
for R,tol in [(30,1e-7),(40,1e-8),(50,1e-8)]:
 st=time.time();r=np.linspace(0,R,2001)
 def jets(c):
  a=c(np.minimum(r,40));ap=c(np.minimum(r,40),1);a[r>40]=ap[r>40]=0
  lap=c(np.minimum(r,40),2)+3*np.divide(ap,r,out=np.full_like(ap,c(0,2)),where=r!=0);lap[r>40]=0
  return np.array([a,ap,lap,np.gradient(lap,r)])
 y=np.r_[jets(ca),jets(cb)];y/=y[0,0]
 if previous is not None:
  y=previous.sol(np.minimum(r,previous.x[-1]));y[:,r>previous.x[-1]]=0
 S=np.zeros((8,8),dtype=complex)
 for j in [1,3,5,7]:S[j,j]=-3
 def fun(r,y,p):
  q=qfun(r);lam=p[0]
  return np.array([y[1],y[2],y[3],(3*q*q-1)*y[0]-lam*y[4],y[5],y[6],y[7],(q*q-1)*y[4]+lam*y[0]])
 def bc(a,b,p):return np.r_[a[1],a[3],a[5],a[7],b[0],b[1],b[4],b[5],a[0]-1]
 sol=solve_bvp(fun,bc,r,y,p=[complex(z['eigenvalue']) if previous is None else previous.p[0]],S=S,tol=tol,max_nodes=50000)
 if sol.success:previous=sol
 row={'R':R,'tol':tol,'success':sol.success,'nodes':len(sol.x),'lambda':[sol.p[0].real,sol.p[0].imag],'max_rms_residual':float(max(sol.rms_residuals)),'seconds':time.time()-st}
 rows.append(row);print(json.dumps(row),flush=True)
 np.savez(ROOT/f'round4_radial_dynamics_bvp_R{R}.npz',x=sol.x,y=sol.y,yp=sol.yp,coeff=sol.sol.c,lam=sol.p)
 (ROOT/'round4_radial_dynamics_bvp.json').write_text(json.dumps(rows,indent=2))
