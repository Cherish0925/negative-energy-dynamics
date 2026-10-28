import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from scipy.integrate import solve_bvp, cumulative_trapezoid, simpson
from scipy.special import kv,kvp
import json
S=np.diag([0.,-1.,0.,-3.,0.])
rows=[]
for width in [2.]:
 R=65.;r=np.linspace(0,R,1100)
 f=2.2/np.cosh(r);v=2./width**2/np.cosh(r/width)
 y=np.vstack([f,-f*np.tanh(r),v,-v*np.tanh(r/width)/width,cumulative_trapezoid(r*(f*f-.5*r*r*v*v),r,initial=0)])
 def fun(r,y,p):
  e=np.exp(p[0]);f,df,v,dv,m=y;rho=f*f+r*r*v*v
  return np.vstack([df,(1-rho)*f,dv,(e-rho)*v,r*(f*f-.5*r*r*v*v)])
 def bc(a,b,p):
  e=np.exp(p[0]);k=np.sqrt(e)
  return [a[1],a[3],a[4],b[1]-kvp(0,R)/kv(0,R)*b[0],b[3]+(1/R-k*kvp(1,k*R)/kv(1,k*R))*b[2],b[4]]
 sol=solve_bvp(fun,bc,r,y,p=[np.log(.3)],S=S,tol=2e-10,max_nodes=25000)
 rr=np.linspace(0,R,20001);ff,df,v,dv,_=sol.sol(rr);g=rr*v;dg=v+rr*dv
 M0=2*np.pi*simpson(rr*ff**2,x=rr);M1=np.pi*simpson(rr*g*g,x=rr)
 T=2*np.pi*simpson(rr*(df**2+dg**2+v**2),x=rr);F=2*np.pi*simpson(rr*(ff**2+g**2)**2,x=rr)
 out=dict(width=width,success=sol.success,e=float(np.exp(sol.p[0])),M0=M0,M1=M1,F=F,T=T,residual=float(max(sol.rms_residuals)),f0=float(ff[0]),gmax=float(max(abs(g))))
 rows.append(out);print(json.dumps(out),flush=True)
 if sol.success and M0>1:
  np.savez('r24_shell.npz',r=rr,f=ff,df=df,g=g,dg=dg,e=np.exp(sol.p[0]))
open('r24_shell_refined_results.json','w').write(json.dumps(rows,indent=2))
