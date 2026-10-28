import numpy as np
from scipy.integrate import solve_bvp,simpson
N=2;p=8/N;R=60.;r=np.linspace(0,R,1801)
S=np.zeros((4,4));S[1,1]=-(N-1);S[3,3]=-(N-1)
def fun(r,y):return np.array([y[1],y[2],y[3],abs(y[0])**p*y[0]-y[0]])
def bc(a,b):return np.array([a[1],a[3],b[0],b[1]])
def to_initial(q):
 v=np.gradient(q,r);dd=np.gradient(v,r);W=dd+(N-1)*np.divide(v,r,out=np.full_like(r,dd[0]),where=r!=0);z=np.gradient(W,r);v[0]=z[0]=0
 return np.array([q,v,W,z])
S2=np.zeros((4,4));S2[1,1]=S2[3,3]=-(N+1)
results=[]
for seed in ['g1','g2','g3','ring3','ring5','ring8','train3','train5','train10']:
 if seed[0]=='g':
  width=int(seed[1]);q=1.6*np.exp(-(r/width)**2/2)
 elif seed.startswith('ring'):
  pos=int(seed[4:]);q=1.3*np.exp(-(r-pos)**2/2)
 else:
  n=int(seed[5:]);q=sum(1.3*np.exp(-(r-3.5*j)**2/2) for j in range(n))
 sol=solve_bvp(fun,bc,r,to_initial(q),S=S,tol=1e-7,max_nodes=24000)
 if not sol.success:print('fail',seed,sol.message,flush=True);continue
 Q=sol.sol(r)[0];dq=sol.sol(r)[1]
 mass=2*np.pi*simpson(Q*Q*r,x=r)
 if mass<.1:print('trivial',seed,flush=True);continue
 def f(r,y):
  zz=sol.sol(r);rhs=np.divide(zz[1],r,out=zz[2]/N,where=r!=0)
  return np.array([y[1],y[2],y[3],rhs-(1-abs(zz[0])**p)*y[0]])
 vv=solve_bvp(f,bc,r,np.zeros((4,len(r))),S=S2,tol=1e-7,max_nodes=24000)
 I=np.pi*simpson(dq*vv.sol(r)[0]*r**2,x=r)
 print(seed,'mass',mass,'I',I,'success',vv.success,'peak',max(abs(Q)),flush=True)
 np.savez('./radial2_%s.npz'%seed,r=r,Q=Q,Qprime=dq,W=r*vv.sol(r)[0])
