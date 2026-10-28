import numpy as np,json,sys,time
from pathlib import Path
from scipy.interpolate import CubicHermiteSpline
from scipy.optimize import root
from scipy.sparse.linalg import gmres,LinearOperator
base=Path(__file__).resolve().parent
def save_npz(path,**arrays):
 tmp=path.with_name(path.name+'.part')
 with tmp.open('wb') as file:np.savez_compressed(file,**arrays)
 tmp.replace(path)
N=int(sys.argv[1]) if len(sys.argv)>1 else 256
L=float(sys.argv[2]) if len(sys.argv)>2 else 56.
seedfile=sys.argv[3] if len(sys.argv)>3 else 'round2_radial_mode1_dim4.npz'
z=np.load(base/seedfile);rr=z['r'];qsp=CubicHermiteSpline(rr,z['y'][0],z['y'][1]);vsp=CubicHermiteSpline(rr,z['V'][0],z['V'][1])
h=L/N;x=np.arange(N)*h-L/2;X,Y=np.meshgrid(x,x,indexing='ij');R=np.sqrt(X*X+Y*Y)
k=2*np.pi*np.fft.fftfreq(N,h);KX,KY=np.meshgrid(k,k,indexing='ij');ksq=KX*KX+KY*KY;sym=1+ksq**2
idx=(-np.arange(N))%N
realproj=lambda a:(a-a[:,idx]-a[idx,:]+a[idx,:][:,idx])/4 # oddx, oddr
# Complex travel symmetry: even real x, odd imaginary x; odd r.
def proj(a):
 a=(a-a[:,idx])/2
 return (a+np.conj(a[idx,:]))/2
size=N*N;pack=lambda a:np.r_[a.real.ravel(),a.imag.ravel()]
unpack=lambda a:a[:size].reshape(N,N)+1j*a[size:].reshape(N,N)
def divr(w):return np.divide(w,Y,out=np.zeros_like(w),where=Y!=0)
def nlin(w):return abs(divr(w))**2*w
quad=lambda f:float(2*np.pi*h*h*np.sum(f))
W=proj(Y*qsp(R));chi_seed=realproj(Y*X*vsp(R))
results=[]
def solve(v,initial):
 symbol=sym-v*KX
 def F(z):
  w=unpack(z);wp=proj(w)
  return pack(w-proj(np.fft.ifft2(np.fft.fft2(nlin(wp))/symbol)))
 t=time.time();rt=root(F,pack(initial),method='krylov',options={'fatol':2e-11,'maxiter':80});w=proj(unpack(rt.x));f=np.fft.fft2(w);lap=np.fft.ifft2(-ksq*f);wx=np.fft.ifft2(1j*KX*f)
 M=quad(abs(w)**2);P=quad((np.conj(w)*wx).imag);E=quad(.5*abs(lap)**2-.25*abs(divr(w))**2*abs(w)**2)
 res=np.fft.ifft2(symbol*f)-nlin(w)
 result=dict(N=N,L=L,v=v,seed=seedfile,success=bool(rt.success),preconditioned_residual=float(max(abs(F(rt.x)))),elliptic_residual=float(np.max(abs(res))),mass=M,P=P,E=E,pohozaev=E-v*P/8,elapsed=time.time()-t)
 print(json.dumps(result),flush=True)
 with open(base/'round2_N4_axial_results.jsonl','a') as ff:ff.write(json.dumps(result)+'\n')
 save_npz(base/f'round2_N4_axial_N{N}_L{L:g}_v{v:g}.npz',x=x,W=w)
 return w,result
W,r0=solve(0.,W)
# Independent Cartesian two-dimensional Fourier inversion of the l=1 response.
q2=abs(divr(W))**2;wx=np.fft.ifft2(1j*KX*np.fft.fft2(W)).real;Kinv=lambda a:np.fft.ifft2(np.fft.fft2(a)/sym).real
rhs=realproj(wx)
def mv(z):
 a=z.reshape(N,N);ap=realproj(a)
 return (a-realproj(Kinv(q2*ap))).ravel()
op=LinearOperator((size,size),matvec=mv)
chi,info=gmres(op,Kinv(rhs).ravel(),x0=chi_seed.ravel(),rtol=2e-10,restart=120,maxiter=20);chi=realproj(chi.reshape(N,N));I=quad(chi*rhs)
linres=np.fft.ifft2(sym*np.fft.fft2(chi)).real-q2*chi-rhs
lin=dict(N=N,L=L,I=I,info=int(info),residual=float(np.max(abs(linres))))
print('LINEAR '+json.dumps(lin),flush=True)
with open(base/'round2_N4_axial_linear.jsonl','a')as ff:ff.write(json.dumps(lin)+'\n')
save_npz(base/f'round2_N4_axial_N{N}_L{L:g}_linear.npz',x=x,W=W,chi=chi)
velocities=[float(t) for t in sys.argv[4].split(',')] if len(sys.argv)>4 else [.002,.005,.01,.02]
for v in velocities:
 ww,r=solve(v,W-1j*v*chi)
