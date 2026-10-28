import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,sys
from types import SimpleNamespace
from scipy.interpolate import CubicHermiteSpline
from scipy.optimize import root
from scipy.sparse.linalg import gmres,LinearOperator
mode=int(sys.argv[1]) if len(sys.argv)>1 else 1
seed=np.load(f'round3_vortex_mode{mode}_radial.npz');r=seed['r'];y=seed['y'];R=float(r[-1]);q=CubicHermiteSpline(r,y[0],y[1]);z=CubicHermiteSpline(r,y[2],y[3]);ss=SimpleNamespace(sol=lambda x:np.array([q(x),q(x,1),z(x),z(x,1)]));hist=[]
N=int(sys.argv[2]) if len(sys.argv)>2 else 256;L=64.;dx=L/N;x=np.arange(N)*dx-L/2;X,Y=np.meshgrid(x,x,indexing='ij');rr=np.sqrt(X*X+Y*Y);k=2*np.pi*np.fft.fftfreq(N,dx);KX,KY=np.meshgrid(k,k,indexing='ij');sym=1+(KX*KX+KY*KY)**2
Kinv=lambda z:np.fft.ifft2(np.fft.fft2(z)/sym)
inner=lambda a,b:float(dx*dx*np.vdot(a,b).real)
pack=lambda z:np.r_[z.real.ravel(),z.imag.ravel()]
unpack=lambda z:z[:N*N].reshape(N,N)+1j*z[N*N:].reshape(N,N)
Q=ss.sol(np.minimum(rr,R).ravel())[0].reshape(rr.shape)*(X+1j*Y);Q[rr>R]=0
def F(z):
 w=unpack(z);return pack(w-Kinv(abs(w)**4*w))
rt=root(F,pack(Q),method='krylov',options={'fatol':2e-10,'maxiter':40});Q=unpack(rt.x)
dq=[np.fft.ifft2(1j*K*np.fft.fft2(Q))for K in [KX,KY]];kernels=[]
for zz in [1j*Q]+dq:
 zz=zz.copy()
 for g in kernels:zz-=g*inner(g,zz)
 zz/=np.sqrt(inner(zz,zz));kernels.append(zz)
kg=[Kinv(g)for g in kernels]
def nonlinear(z):return abs(Q)**4*z+4*abs(Q)**2*Q*(np.conj(Q)*z).real
def act(z):
 w=unpack(z);out=w-Kinv(nonlinear(w))
 for g,gi in zip(kernels,kg):out+=gi*inner(g,w)
 return pack(out)
op=LinearOperator((2*N*N,2*N*N),matvec=act);etas=[];rhs=[];infos=[];resids=[];projection=[]
for deriv in dq:
 b=-1j*deriv;projection.append([inner(g,b)for g in kernels])
 for g in kernels:b-=g*inner(g,b)
 eta,info=gmres(op,pack(Kinv(b)),rtol=3e-8,restart=160,maxiter=20);eta=unpack(eta);etas.append(eta);rhs.append(b);infos.append(int(info));res=np.fft.ifft2(sym*np.fft.fft2(eta))-nonlinear(eta)-b;resids.append(float(np.max(abs(res))))
A=np.array([[inner(etas[i],rhs[j])for j in range(2)]for i in range(2)]);lap=np.fft.ifft2(-(KX*KX+KY*KY)*np.fft.fft2(Q));res=np.fft.ifft2(sym*np.fft.fft2(Q))-abs(Q)**4*Q
result=dict(stage='fullFFT',mode=mode,m=1,grid=N,L=L,root_success=bool(rt.success),preconditioned_residual=float(max(abs(F(rt.x)))),elliptic_residual=float(np.max(abs(res))),mass=inner(Q,Q),energy=float(dx*dx*np.sum(.5*abs(lap)**2-abs(Q)**6/6)),matrix=A.tolist(),eigenvalues=np.linalg.eigvalsh((A+A.T)/2).tolist(),linear_infos=infos,linear_residuals=resids,kernel_rhs_projections=projection)
print(json.dumps(result),flush=True);hist.append(result);open(f'round3_vortex_mode{mode}_N{N}_log.json','w').write(json.dumps(hist,indent=2));np.savez_compressed(f'round3_vortex_mode{mode}_N{N}.npz',x=x,Q=Q,eta0=etas[0],eta1=etas[1],matrix=A)
