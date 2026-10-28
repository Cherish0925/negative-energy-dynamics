"""Numerical radial quartet BVP with exact free decaying boundary conditions.
This is discovery evidence, NOT an interval or eigenvalue existence certificate.
Frozen input: the canonical q plus one saved initial-guess profile.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time
from fractions import Fraction
from scipy.interpolate import BPoly,PPoly
from scipy.integrate import solve_bvp
from scipy.special import kv
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'round2_radial_H4_exact_h1_16.json').read_text());xs=np.array([float(Fraction(*v)) for v in raw['nodes']]);jets=np.array([[float.fromhex(v) for v in row] for row in raw['jets_hex']]);bp=BPoly.from_derivatives(xs,jets)
def qfun(r):return np.where(r<36,bp(np.minimum(r,36)),0)
rows=[]
seed=np.load(ROOT/'round4_radial_dynamics_bvp_R30.npz');seedpp=PPoly.construct_fast(seed['coeff'],seed['x'],axis=1)
for R,tol in [(30,1e-7),(36,1e-8),(40,1e-8)]:
 st=time.time();r=np.linspace(0,R,2001)
 y=seedpp(np.minimum(r,30));y[:,r>30]=0
 S=np.zeros((8,8),dtype=complex)
 for j in [1,3,5,7]:S[j,j]=-3
 def fun(r,y,p):
  q=qfun(r);lam=p[0]
  return np.array([y[1],y[2],y[3],(3*q*q-1)*y[0]-lam*y[4],y[5],y[6],y[7],(q*q-1)*y[4]+lam*y[0]])
 def stable_matrix(c):
  k=(-c)**.25;kk=[k,1j*k];kk=[z if z.real>0 else -z for z in kk]
  ds=[-2/R-z*kv(0,z*R)/kv(1,z*R) for z in kk]
  return np.array([[kk[0]**2,kk[1]**2],[kk[0]**2*ds[0],kk[1]**2*ds[1]]])@np.linalg.inv(np.array([[1,1],ds]))
 def bc(a,b,p):
  z=b[:4]+1j*b[4:];w=b[:4]-1j*b[4:]
  bz=z[2:]-stable_matrix(1-1j*p[0])@z[:2];bw=w[2:]-stable_matrix(1+1j*p[0])@w[:2]
  return np.r_[a[1],a[3],a[5],a[7],bz,bw,a[0]-1]
 fun_c,bc_c=fun,bc
 def fun_real(r,Y,p):
  val=fun_c(r,Y[:8]+1j*Y[8:],[p[0]+1j*p[1]]);return np.r_[val.real,val.imag]
 def bc_real(a,b,p):
  val=bc_c(a[:8]+1j*a[8:],b[:8]+1j*b[8:],[p[0]+1j*p[1]]);return np.r_[val.real,val.imag]
 SS=np.zeros((16,16));SS[:8,:8]=S.real;SS[8:,8:]=S.real
 lam=seed['lam'][0]
 sol=solve_bvp(fun_real,bc_real,r,np.r_[y.real,y.imag],p=[lam.real,lam.imag],S=SS,tol=tol,max_nodes=50000)
 row={'R':R,'tol':tol,'success':sol.success,'nodes':len(sol.x),'lambda':[float(sol.p[0]),float(sol.p[1])],'max_rms_residual':float(max(sol.rms_residuals)),'seconds':time.time()-st}
 rows.append(row);print(json.dumps(row),flush=True)
 np.savez(ROOT/f'round4_radial_dynamics_outgoing_real_R{R}.npz',x=sol.x,y=sol.y,yp=sol.yp,coeff=sol.sol.c,lam=sol.p)
 (ROOT/'round4_radial_dynamics_outgoing_real.json').write_text(json.dumps(rows,indent=2))
