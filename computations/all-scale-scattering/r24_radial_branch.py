import numpy as np,json
from scipy.integrate import solve_ivp,solve_bvp,simpson
from scipy.optimize import brentq
from scipy.special import kv,kve
from scipy.linalg import eigh_tridiagonal
R=25.;x=np.linspace(0,R,901)
def shot(a,R=12.):
 return solve_ivp(lambda r,y:[y[1],-y[1]/r+y[0]-y[0]**3],[1e-6,R],[a+(a-a**3)*1e-12/4,(a-a**3)*1e-6/2],rtol=2e-10,atol=1e-12,dense_output=True)
def res(a):
 z=shot(a).y[:,-1];return z[1]+kve(1,12)/kve(0,12)*z[0]
a=brentq(res,3.331,3.332,xtol=1e-14)
shot0=shot(a); init=shot0.sol(np.minimum(x,12));tail=x>12
init[0,tail]=shot0.y[0,-1]*kv(0,x[tail])/kv(0,12);init[1,tail]=-shot0.y[0,-1]*kv(1,x[tail])/kv(0,12)
q=solve_bvp(lambda r,y:np.array([y[1],y[0]-y[0]**3]),lambda l,r:np.array([l[1],r[1]+kve(1,R)/kve(0,R)*r[0]]),x,init,S=np.diag([0.,-1.]),tol=1e-9,max_nodes=15000)
print('scalar',a,q.status,flush=True)
rr=(np.arange(5000)+.5)*R/5000;dr=rr[1]-rr[0];pot=q.sol(rr)[0]**2
diag=2/dr**2-pot;diag[0]=2/dr**2-pot[0]
off=-(rr[:-1]+.5*dr)/(dr**2*np.sqrt(rr[:-1]*rr[1:]))
vals,vec=eigh_tridiagonal(diag,off,select='i',select_range=(0,3));print('eigs',vals,flush=True)
e1=-vals[0];w=vec[:,0]/np.sqrt(rr);w*=np.sign(w[0]);w/=w[0];wx=np.interp(x,rr,w);wxp=np.gradient(wx,x)
initial=np.array([.1*wx,.1*wxp,q.sol(x)[0],q.sol(x)[1]])
S=np.diag([0.,-1.,0.,-1.]);sol=None;out=[]
for amp in [.1,.3,.5,.8,1.,1.3,1.6,2.,2.5,3.,3.5,4.,5.,6.,8.,10.]:
 def fun(r,y,p):
  rho=y[0]**2+y[2]**2
  return np.array([y[1],(p[0]-rho)*y[0],y[3],(1-rho)*y[2]])
 def bc(l,r,p):
  k=np.sqrt(max(p[0],1e-8));return np.array([l[1],l[3],r[1]+k*kve(1,k*R)/kve(0,k*R)*r[0],r[3]+kve(1,R)/kve(0,R)*r[2],l[0]-amp])
 if sol is not None: initial=sol.sol(x);initial[:2]*=amp/lastamp
 sol=solve_bvp(fun,bc,x,initial,p=[e1],S=S,tol=1e-7,max_nodes=30000)
 e1=float(sol.p[0]);lastamp=amp
 xx=np.linspace(1e-4,R,20001);yy=sol.sol(xx);mass=2*np.pi*np.array([simpson(xx*yy[0]**2,x=xx),simpson(xx*yy[2]**2,x=xx)])
 rec=dict(amp=amp,status=int(sol.status),e1=e1,mass=mass.tolist(),maxres=float(sol.rms_residuals.max()))
 if sol.status==0 and e1>1 and yy[0].min()>0:
  g=yy[1]/yy[0];vv=(yy[3]-g*yy[2])/np.sqrt(e1-1);ss=vv*vv;rho=yy[0]**2+yy[2]**2
  W=1/xx**2+2*g/xx+2*g*g+rho-2*e1+ss
  Wp=-(2*g+1/xx)*W-(rho+ss)/xx-1/xx**3
  mask=(xx>.03)&(xx<15)&(yy[0]>1e-8)
  rec.update(Wmin=float(W[mask].min()),Wpmax=float(Wp[mask].max()),Dmin=float((rho-ss)[mask].min()),gmax=float(g[mask].max()),virial=float(2*np.pi*simpson(xx*xx*Wp*ss,x=xx)),v_mass=float(2*np.pi*simpson(xx*ss,x=xx)))
  np.savez('research/r24_radial_branch_amp'+str(amp)+'.npz',r=xx,y=yy,W=W,Wp=Wp,S=ss,mass=mass,e1=e1)
 print(json.dumps(rec),flush=True);out.append(rec)
 if sol.status!=0:break
json.dump(out,open('research/r24_radial_branch.json','w'),indent=2)
