import numpy as np
from scipy.optimize import root
from scipy.sparse.linalg import gmres,LinearOperator
Nx=256;Ny=128;Lx=48.;Ly=32.;dx=Lx/Nx;dy=Ly/Ny
x=np.arange(Nx)*dx-Lx/2;y=np.arange(Ny)*dy-Ly/2
X,Y=np.meshgrid(x,y,indexing='ij');KX,KY=np.meshgrid(2*np.pi*np.fft.fftfreq(Nx,dx),2*np.pi*np.fft.fftfreq(Ny,dy),indexing='ij');sym=1+(KX*KX+KY*KY)**2
Kinv=lambda f:np.fft.ifft2(np.fft.fft2(f)/sym).real
D=lambda f:np.fft.ifft2(1j*KX*np.fft.fft2(f)).real
z=np.load('./radial2_g1.npz');r=z['r'];qr=z['Q']
integ=lambda f:dx*dy*np.sum(f)
for n in [2,3,4]:
 for sep in [4.5,5.5,6.5]:
  q0=sum(np.interp(np.sqrt((X-((j-(n-1)/2)*sep))**2+Y*Y),r,qr,right=0) for j in range(n))
  F=lambda q:(q.reshape(Nx,Ny)-Kinv(q.reshape(Nx,Ny)**5)).ravel()
  s=root(F,q0.ravel(),method='krylov',options={'fatol':2e-8,'maxiter':65})
  q=s.x.reshape(Nx,Ny);err=max(abs(F(s.x)))
  if err>1e-6:print('fail',n,sep,err,flush=True);continue
  dq=D(q);op=LinearOperator((Nx*Ny,Nx*Ny),matvec=lambda w:(w.reshape(Nx,Ny)-Kinv(q**4*w.reshape(Nx,Ny))).ravel())
  w,info=gmres(op,Kinv(dq).ravel(),rtol=1e-7,restart=150,maxiter=25);w=w.reshape(Nx,Ny)
  I=integ(w*dq);M=integ(q*q)
  print('2D',n,sep,'M',M,'I',I,'error',err,'info',info,flush=True)
  np.savez('./travel2d_%s_%s.npz'%(n,sep),x=x,y=y,Q=q,W=w)
