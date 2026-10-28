"""N2 excited m=1 vortex via fixed-disk nonlinear eigenmode continuation."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,sys
from scipy.integrate import solve_bvp,simpson
from scipy.special import jv,iv,ive
from scipy.optimize import brentq
from scipy.signal import find_peaks
mode=int(sys.argv[1])if len(sys.argv)>1 else 1;m=1;R=20.;r=np.linspace(0,R,1201);S=np.zeros((4,4));S[1,1]=S[3,3]=-3
f=lambda x:jv(m,x)*ive(m+1,x)+jv(m+1,x)*ive(m,x)
xx=np.linspace(.2,40,1600);roots=[brentq(f,a,b)for a,b in zip(xx[:-1],xx[1:])if f(a)*f(b)<0];k=roots[mode]/R;co=jv(m,k*R)/iv(m,k*R);rx=np.where(r==0,1,r);j=jv(m,k*r)/rx;i=iv(m,k*r)/rx;j[0]=i[0]=k/2
yp=-k*(jv(2,k*r)+co*iv(2,k*r))/rx;zp=k**3*(jv(2,k*r)-co*iv(2,k*r))/rx;y=np.array([j-co*i,yp,-k*k*(j+co*i),zp]);amp=.01;y*=amp/y[0,0];omega=-k**4;prev=amp;step=.02;out=[]
def fun(r,y,p):return np.array([y[1],y[2],y[3],r**4*y[0]**5-p[0]*y[0]])
for it in range(180):
 def bc(a,b,p):return np.array([a[1],a[3],b[0],b[1],a[0]-amp])
 sol=solve_bvp(fun,bc,r,y,p=[omega],S=S,tol=3e-7,max_nodes=25000)
 if not sol.success:
  step/=2;amp=prev+step
  print('FAIL',mode,amp,step,sol.message,flush=True)
  if step<.0002:break
  continue
 omega=float(sol.p[0]);prev=amp;r=sol.x;y=sol.y
 if it%10==0 or(omega>0 and R*omega**.25>42):
  row=dict(mode=mode,it=it,amp=amp,omega=omega,nodes=len(r),scaled_R=R*max(omega,0)**.25);out.append(row);print(json.dumps(row),flush=True)
 if omega>0 and R*omega**.25>42:
  rs=np.linspace(0,R*omega**.25,5001);ys=sol.sol(rs/omega**.25);U=ys[0]/omega**.5;Up=ys[1]/omega**.75;Z=ys[2]/omega;Zp=ys[3]/omega**1.25;q=rs*U;lap=rs*Z
  row.update(M=float(2*np.pi*simpson(q*q*rs,x=rs)),E=float(2*np.pi*simpson((.5*lap**2-q**6/6)*rs,x=rs)),peaks=rs[find_peaks(abs(q),height=.2)[0]].tolist())
  np.savez_compressed(f'round3_vortex_mode{mode}_radial.npz',r=rs,y=np.array([U,Up,Z,Zp]),m=m,omega=omega,original_x=sol.x,original_c=sol.sol.c);print('FINAL',json.dumps(row),flush=True);break
 if amp>8:break
 if len(r)>6000:r=np.linspace(0,R,3001);y=sol.sol(r)
 step=min(.09,step*1.12);amp=prev+step;y*=amp/prev
open(f'round3_vortex_eigen_mode{mode}.json','w').write(json.dumps(out,indent=2))
