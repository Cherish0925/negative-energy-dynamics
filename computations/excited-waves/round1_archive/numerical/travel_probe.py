import numpy as np
from scipy.optimize import root
from scipy.sparse.linalg import gmres,LinearOperator,eigsh
N=1024; L=80.; dx=L/N
x=np.arange(N)*dx-L/2
k=2*np.pi*np.fft.fftfreq(N,dx); sym=(1+k**4)
Kinv=lambda f:np.fft.ifft(np.fft.fft(f)/sym).real
D=lambda f:np.fft.ifft(1j*k*np.fft.fft(f)).real
integ=lambda f:dx*np.sum(f)
Q=np.exp(-x*x)
for j in range(10000):
    b=Q**9; r=Kinv(b)
    scale=integ(Q*np.fft.ifft(sym*np.fft.fft(Q)).real)/integ(Q*b)
    Qn=r*scale**(9/8)
    if np.linalg.norm(Q-Qn)<1e-12: break
    Q=Qn
np.savez('./travel_ground.npz',x=x,Q=Q)
print('ground',j,np.max(abs(Q-Kinv(Q**9))),integ(Q*Q),flush=True)
for sign in [1,-1]:
 for sep in [6,8,10,12,14,16,18,20,24]:
    q0=np.interp(x-sep/2,x,Q,left=0,right=0)+sign*np.interp(x+sep/2,x,Q,left=0,right=0)
    sol=root(lambda q:q-Kinv(q**9),q0,method='krylov',options={'fatol':2e-10,'maxiter':100})
    q=sol.x
    err=max(abs(q-Kinv(q**9)))
    if err>1e-7:
       print('fail',sign,sep,err,flush=True);continue
    # rhs derivative has opposite parity to q, so kernel q not excited.
    dq=D(q)
    op=LinearOperator((N,N),matvec=lambda w:w-Kinv(q**8*w))
    w,info=gmres(op,Kinv(dq),rtol=1e-8,restart=200,maxiter=50)
    form=integ(w*dq)
    print('excited',sign,sep,'mass',integ(q*q),'peak',max(q),'err',err,'gmres',info,'form',form,flush=True)
    np.savez('./travel_profile_%s_%s.npz'%(sign,sep),x=x,Q=q,W=w)
