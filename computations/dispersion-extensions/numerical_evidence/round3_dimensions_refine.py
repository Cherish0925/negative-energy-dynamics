"""Numerical, not validated: critical p=8/N radial standing and l=1 response.
Regular origin Taylor start with unknown first two even coefficients; stable
or clamped outer boundary, intervalwise Gaussian integration. Frozen output
keeps the actual collocation PPoly and mesh, avoiding resampling as input.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,sys
from scipy.integrate import solve_bvp
from scipy.interpolate import CubicHermiteSpline
from scipy.special import kv,kvp,gamma
from numpy.polynomial.legendre import leggauss

def power(c,a):
 out=np.zeros(len(c));out[0]=c[0]**a
 for n in range(1,len(c)):
  out[n]=sum(((a+1)*k-n)*c[k]*out[n-k] for k in range(1,n+1))/(n*c[0])
 return out

def qs(a,b,d,p,K=10):
 c=np.zeros(K);c[:2]=[a,b]
 for j in range(K-2):
  n=2*j+4;c[j+2]=(power(c[:j+1],p+1)[j]-c[j])/(n*(n+d-2)*(n-2)*(n+d-4))
 return c

def vs(a,b,q,d,p,K=10):
 c=np.zeros(K);c[:2]=[a,b];qp=power(q,p)
 for j in range(K-2):
  n=2*j+4;c[j+2]=(sum(qp[k]*c[j-k] for k in range(j+1))-c[j]+2*(j+1)*q[j+1])/(n*(n+d)*(n-2)*(n+d-2))
 return c

def es(c,r,d):
 r=np.asarray(r);z=np.zeros((4,)+r.shape)
 for k,a in enumerate(c):
  z[0]+=a*r**(2*k)
  if k:z[1]+=2*k*a*r**(2*k-1);z[2]+=2*k*(2*k+d-2)*a*r**(2*k-2)
  if k>=2:z[3]+=2*k*(2*k+d-2)*(2*k-2)*a*r**(2*k-3)
 return z

def stable(d,R):
 nu=(d-2)/2;k=np.exp(1j*np.pi/4)
 f=R**(-nu)*kv(nu,k*R);fp=R**(-nu)*(k*kvp(nu,k*R)-nu/R*kv(nu,k*R))
 z=np.array([f,fp,1j*f,1j*fp]);a=np.column_stack([z.real,z.imag]);a/=np.linalg.norm(a,axis=0)
 return np.linalg.svd(a,full_matrices=True)[0][:,2:].T

def inte(f,meshes,n=10):
 x=np.unique(np.concatenate(meshes));g,w=leggauss(n);pts=(x[:-1,None]+x[1:,None])/2+(x[1:,None]-x[:-1,None])/2*g
 return float(np.sum(f(pts.ravel()).reshape(pts.shape)*w[None,:]*(x[1:,None]-x[:-1,None])/2))

def make_seed(a,key):
 r=a['r'];y=a[key];q=CubicHermiteSpline(r,y[0],y[1]);z=CubicHermiteSpline(r,y[2],y[3])
 return lambda r:np.array([q(r),q(r,1),z(r),z(r,1)])

jobs=[(3,4,.01,40.,2e-9,'stable'),(3,4,.005,50.,3e-10,'stable'),(3,4,.02,60.,2e-9,'clamped'),(5,1,.01,40.,2e-9,'stable'),(5,1,.005,50.,3e-10,'stable'),(5,1,.02,60.,2e-9,'clamped')]
if len(sys.argv)>1:jobs=[j for j in jobs if j[0]==int(sys.argv[1])]
if len(sys.argv)>2 and sys.argv[2]=='extra':jobs=[(5,1,.02,50.,1e-9,'stable')]
outs=[]
for d,mode,eps,R,tol,bctype in jobs:
 p=8/d;seed=np.load(f'round2_radial_mode{mode}_dim{d}.npz');Q0=make_seed(seed,'y');V0=make_seed(seed,'V')
 r=np.linspace(eps,R,int(R*80)+1);B=stable(d,R) if bctype=='stable' else np.eye(4)[:2];BV=stable(d+2,R) if bctype=='stable' else np.eye(4)[:2]
 def fun(r,y,t):return np.array([y[1],y[2]-(d-1)*y[1]/r,y[3],abs(y[0])**p*y[0]-y[0]-(d-1)*y[3]/r])
 def bc(a,b,t):return np.r_[a-es(qs(*t,d,p),eps,d),B@b]
 q=solve_bvp(fun,bc,r,Q0(r),p=[Q0(0)[0],Q0(0)[2]/(2*d)],tol=tol,max_nodes=65000)
 qc=qs(*q.p,d,p)
 def vf(r,y,t):
  yy=q.sol(r);return np.array([y[1],y[2]-(d+1)*y[1]/r,y[3],(abs(yy[0])**p-1)*y[0]+yy[1]/r-(d+1)*y[3]/r])
 def vbc(a,b,t):return np.r_[a-es(vs(*t,qc,d,p),eps,d+2),BV@b]
 v=solve_bvp(vf,vbc,r,V0(r),p=[V0(0)[0],V0(0)[2]/(2*(d+2))],tol=tol,max_nodes=65000);vc=vs(*v.p,qc,d,p)
 def qe(x):
  y=q.sol(x);mask=x<eps
  if mask.any():y[:,mask]=es(qc,x[mask],d)
  return y
 def ve(x):
  y=v.sol(x);mask=x<eps
  if mask.any():y[:,mask]=es(vc,x[mask],d+2)
  return y
 meshes=[np.r_[0,q.x],np.r_[0,v.x]];surf=2*np.pi**(d/2)/gamma(d/2)
 M=surf*inte(lambda x:qe(x)[0]**2*x**(d-1),meshes);K=surf*inte(lambda x:qe(x)[2]**2*x**(d-1),meshes);L=surf*inte(lambda x:abs(qe(x)[0])**(p+2)*x**(d-1),meshes)
 I=surf/d*inte(lambda x:qe(x)[1]*ve(x)[0]*x**d,meshes);Iq=surf/d*inte(lambda x:(ve(x)[2]**2+(1-abs(qe(x)[0])**p)*ve(x)[0]**2)*x**(d+1),meshes)
 # Dense differential-system defect at 3 interior points per collocation cell;
 # a diagnostic, not an H4 residual certificate for piecewise cubic states.
 def ode_defect(sol,fn):
  xx=(sol.x[:-1,None]+(sol.x[1:]-sol.x[:-1])[:,None]*np.array([.2113248654,.5,.7886751346])).ravel();return float(np.max(abs(sol.sol(xx,1)-fn(xx,sol.sol(xx),sol.p))))
 row=dict(N=d,p=p,mode=mode,eps=eps,R=R,tol=tol,bc=bctype,q_success=bool(q.success),v_success=bool(v.success),q_nodes=len(q.x),v_nodes=len(v.x),q_rms=float(max(q.rms_residuals)),v_rms=float(max(v.rms_residuals)),q_dense_ODE_defect=ode_defect(q,fun),v_dense_ODE_defect=ode_defect(v,vf),q_bc_residual=float(max(abs(bc(q.y[:,0],q.y[:,-1],q.p)))),v_bc_residual=float(max(abs(vbc(v.y[:,0],v.y[:,-1],v.p)))),q0=float(qc[0]),M=M,K=K,L=L,E=K/2-L/(p+2),stationary_identity=K+M-L,I=I,Iquadratic=Iq,I_discrepancy=Iq-I,tail_q=float(max(abs(q.y[:,-1]))),tail_v=float(max(abs(v.y[:,-1]))))
 out=f'round3_dimensions_N{d}_mode{mode}_R{int(R)}_e{eps:.3f}_{bctype}'
 np.savez_compressed(out+'.npz',N=d,p=p,mode=mode,q_x=q.x,q_c=q.sol.c,q_y=q.y,q_yp=q.yp,q_series=qc,v_x=v.x,v_c=v.sol.c,v_y=v.y,v_yp=v.yp,v_series=vc,eps=eps,R=R,tol=tol,q_bc=B,v_bc=BV)
 row['file']=out+'.npz';outs.append(row);print(json.dumps(row),flush=True)
 open(f'round3_dimensions_refine_N{d}'+('_extra' if len(sys.argv)>2 else '')+'.json','w').write(json.dumps([o for o in outs if o['N']==d],indent=2))
