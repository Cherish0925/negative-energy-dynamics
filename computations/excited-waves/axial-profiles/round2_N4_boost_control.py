import numpy as np,json
from pathlib import Path
from scipy.optimize import minimize_scalar
base=Path(__file__).resolve().parent
z=np.load(base/'round2_N4_axial_N384_L72_v0.npz');x=z['x'];w0=z['W'].real
z=np.load(base/'round2_N4_axial_N384_L72_v0.02.npz');w=z['W'];N=len(x);h=x[1]-x[0];v=.02
X,Y=np.meshgrid(x,x,indexing='ij');k=2*np.pi*np.fft.fftfreq(N,h);KX,KY=np.meshgrid(k,k,indexing='ij');ksq=KX*KX+KY*KY;f=np.fft.fft2(w0)
quad=lambda a:float(2*np.pi*h*h*np.sum(a))
wx=np.fft.ifft2(1j*KX*f).real;wy=np.fft.ifft2(1j*KY*f).real;wxx=np.fft.ifft2(-KX*KX*f).real;lap=np.fft.ifft2(-ksq*f).real;dxlap=np.fft.ifft2(-1j*KX*ksq*f).real
M=quad(w0*w0);A=quad(wx*wx+wy*wy);Ax=quad(wx*wx)
def controls(k):
 Rreal=-2*k*k*lap-4*k*k*wxx;alpha=-quad(w0*Rreal)/M
 Rreal+=alpha*w0
 Rimag=4*k*dxlap+(v-4*k**3)*wx
 omega=1-k**4+v*k+alpha
 return quad(Rreal**2+Rimag**2),omega
opt=minimize_scalar(lambda k:controls(k)[0],bounds=(-.1,.1),method='bounded',options={'xatol':1e-13});kb=opt.x
fit=minimize_scalar(lambda k:quad(abs(w-np.exp(1j*k*X)*w0)**2),bounds=(-.1,.1),method='bounded',options={'xatol':1e-13})
f=np.fft.fft2(w);wxt=np.fft.ifft2(1j*KX*f);lapt=np.fft.ifft2(-ksq*f);Q=np.divide(w,Y,out=np.zeros_like(w),where=Y!=0)
R=np.fft.ifft2((1+ksq*ksq-v*KX)*f)-abs(Q)**2*w
Mt=quad(abs(w)**2);Pt=quad((np.conj(w)*wxt).imag);J3=quad((np.conj(wxt)*lapt).imag)
result=dict(v=v,best_residual_boost_k=float(kb),optimized_boost_frequency=float(controls(kb)[1]),boost_residual_L2=float(np.sqrt(opt.fun)),boost_P=float(kb*M),boost_E=float(.5*kb**4*M+kb**2*(A+2*Ax)),best_profile_fit_k=float(fit.x),best_profile_fit_relative_L2=float(np.sqrt(fit.fun/Mt)),actual_residual_L2=float(np.sqrt(quad(abs(R)**2))),actual_M=Mt,actual_P=Pt,third_moment=J3,velocity_moment_difference=float(v*Mt-4*J3))
print(json.dumps(result,indent=2));(base/'round2_N4_boost_controls.json').write_text(json.dumps(result,indent=2))
