import numpy as np
from scipy.integrate import solve_bvp,simpson
z=np.load('./travel_bvp_14_False_4.75.npz');x=z['x'];q=z['Q'];dx=x[1]-x[0];k=2*np.pi*np.fft.fftfreq(len(x),dx);qf=np.fft.fft(q)
R=80;r=np.linspace(0,R,5001)
y0=np.array([np.interp(r,x,np.fft.ifft((1j*k)**j*qf).real,left=0,right=0) for j in range(4)])
def fun(r,y):return np.array([y[1],y[2],y[3],y[0]**9-y[0]])
def bc(a,b):return np.array([a[1],a[3],b[0],b[1]])
s=solve_bvp(fun,bc,r,y0,tol=1e-10,max_nodes=60000)
print('standing',s.success,len(s.x),max(s.rms_residuals),flush=True)
r=np.linspace(0,R,16001)
def lin(r,y):
 q=s.sol(r)[0];dq=s.sol(r)[1]
 return np.array([y[1],y[2],y[3],dq-(1-q**8)*y[0]])
def bclin(a,b):return np.array([a[0],a[2],b[0],b[1]])
w=solve_bvp(lin,bclin,r,np.zeros((4,len(r))),tol=1e-10,max_nodes=60000)
I=2*simpson(s.sol(r)[1]*w.sol(r)[0],x=r)
print('linear',w.success,len(w.x),max(w.rms_residuals),'I',I,flush=True)
results=[]
for v in [.005,.01,.02]:
 def twfun(r,y):
  a,aa,aaa,aaaa,b,bb,bbb,bbbb=y
  amp=(a*a+b*b)**4
  return np.array([aa,aaa,aaaa,(amp-1)*a+v*bb,bb,bbb,bbbb,(amp-1)*b-v*aa])
 def twbc(a,b):return np.array([a[1],a[3],a[4],a[6],b[0],b[1],b[4],b[5]])
 yy=np.concatenate([s.sol(r),-v*w.sol(r)],axis=0)
 tw=solve_bvp(twfun,twbc,r,yy,tol=2e-10,max_nodes=90000)
 yy=tw.sol(r);a,aa,aaa,aaaa,b,bb,bbb,bbbb=yy
 mass=2*simpson(a*a+b*b,x=r);P=2*simpson(a*bb-b*aa,x=r)
 E=simpson(aaa*aaa+bbb*bbb,x=r)-2/10*simpson((a*a+b*b)**5,x=r)
 discrepancy=E-v*P/8
 print('travel',v,tw.success,len(tw.x),max(tw.rms_residuals),'M',mass,'P',P,'E',E,'vP/8',v*P/8,'difference',discrepancy,flush=True)
 results.append([v,bool(tw.success),mass,P,E,v*P/8,discrepancy])
 np.savez('./negative_travel_1d_%s.npz'%v,r=r,profile=yy,standing=s.sol(r),linear=w.sol(r))
import json
open('./negative_travel_results.json','w').write(json.dumps(dict(I=I,results=results),indent=2))
