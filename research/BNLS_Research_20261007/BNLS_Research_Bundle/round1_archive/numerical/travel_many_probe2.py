from scipy.integrate import solve_bvp
import numpy as np
from scipy.sparse.linalg import gmres,LinearOperator
N=4096;L=200.;dx=L/N;x=np.arange(N)*dx-L/2;k=2*np.pi*np.fft.fftfreq(N,dx);sym=1+k**4
Kinv=lambda f:np.fft.ifft(np.fft.fft(f)/sym).real
D=lambda f:np.fft.ifft(1j*k*np.fft.fft(f)).real
z=np.load('./travel_ground.npz');xg=z['x'];qg=z['Q'];kg=2*np.pi*np.fft.fftfreq(len(xg),xg[1]-xg[0]);qgf=np.fft.fft(qg)
xx=np.linspace(0,85,2400)
res=[]
for n in [8,10,12,14,16,20]:
 for alternate in [False]:
  for sep in [4.75]:
   shifts=(np.arange(n)-(n-1)/2)*sep
   signs=(-1)**np.arange(n) if alternate else np.ones(n)
   parity=int(signs[0]*signs[-1])
   yy=np.array([sum(s*np.interp(xx-shift,xg,np.fft.ifft((1j*kg)**j*qgf).real,left=0,right=0) for s,shift in zip(signs,shifts)) for j in range(4)])
   def fun(t,y):return np.array([y[1],y[2],y[3],y[0]**9-y[0]])
   def bc(a,b):return np.array([a[1],a[3],b[0],b[1]]) if parity==1 else np.array([a[0],a[2],b[0],b[1]])
   ss=solve_bvp(fun,bc,xx,yy,tol=2e-7,max_nodes=24000)
   if not ss.success: print('fail',n,alternate,sep,flush=True);continue
   q=ss.sol(np.minimum(abs(x),85))[0]*(np.where(x>=0,1,parity));q[abs(x)>85]=0
   dq=D(q);op=LinearOperator((N,N),matvec=lambda w:w-Kinv(q**8*w))
   w,info=gmres(op,Kinv(dq),rtol=1e-8,restart=300,maxiter=50)
   form=dx*np.dot(w,dq);mass=dx*np.dot(q,q)
   item=dict(n=n,alternate=alternate,sep=sep,peak=float(max(abs(q))),mass=float(mass),form=float(form),info=int(info))
   res.append(item);print(item,flush=True)
   np.savez('./travel_bvp_%s_%s_%s.npz'%(n,alternate,sep),x=x,Q=q,W=w)
import json
open('./travel_many_results.json','w').write(json.dumps(res,indent=2))
