import numpy as np
from scipy.integrate import solve_bvp,simpson
from scipy.special import gamma
z=np.load('./travel_bvp_14_False_4.75.npz');x=z['x'];q=z['Q'];dx=x[1]-x[0];k=2*np.pi*np.fft.fftfreq(len(x),dx);qf=np.fft.fft(q)
R=80;r=np.linspace(0,R,4001)
y=np.array([np.interp(r,x,np.fft.ifft((1j*k)**j*qf).real,left=0,right=0) for j in range(4)])
def bc(a,b):return np.array([a[1],a[3],b[0],b[1]])
prev=1.;step=.01;target=1.
while target<2.+1e-10:
 d=target;p=8/d;S=np.zeros((4,4));S[1,1]=S[3,3]=-(d-1)
 def fun(r,y):return np.array([y[1],y[2],y[3],abs(y[0])**p*y[0]-y[0]])
 ss=solve_bvp(fun,bc,r,y,S=S,tol=3e-7,max_nodes=30000)
 if not ss.success:
  step/=2;target=prev+step
  print('fail',d,'step',step,flush=True)
  if step<.0003:break
  continue
 prev=d;y=ss.sol(r)
 if abs((d*10)-round(d*10))<1e-7 or d>=2-1e-9:
  mass=2*np.pi**(d/2)/gamma(d/2)*simpson(y[0]**2*r**(d-1),x=r)
  print('dimension',d,'mass',mass,'nodes',len(ss.x),'peak',max(abs(y[0])),flush=True)
  np.savez('./dim_profile_%.5f.npz'%d,r=r,y=y)
 target=min(2.,prev+step)
 if d>=2-1e-9:break
