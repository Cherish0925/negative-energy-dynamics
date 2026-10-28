import numpy as np,json,time
from pathlib import Path
from scipy.sparse.linalg import eigsh,LinearOperator
from scipy.interpolate import CubicHermiteSpline
base=Path(__file__).resolve().parent
z=np.load(base/'round2_N4_axial_N256_L56_v0.npz');x=z['x'];w=z['W'].real;N=len(x);h=x[1]-x[0];X,Y=np.meshgrid(x,x,indexing='ij');k=2*np.pi*np.fft.fftfreq(N,h);KX,KY=np.meshgrid(k,k,indexing='ij');sym=1+(KX*KX+KY*KY)**2;idx=(-np.arange(N))%N
q2=np.divide(w,Y,out=np.zeros_like(w),where=Y!=0)**2
G=lambda a:np.fft.ifft2(np.fft.fft2(a)/np.sqrt(sym)).real
rows=[]
for name,c,parity in [('minus',1.,-1),('plus',3.,1)]:
 def proj(a):
  a=(a-a[:,idx])/2
  return (a+parity*a[idx,:])/2
 def matvec(v):return proj(G(c*q2*G(proj(v.reshape(N,N))))).ravel()
 op=LinearOperator((N*N,N*N),matvec=matvec)
 v0=proj(np.random.default_rng(715).standard_normal((N,N))).ravel()
 t=time.time();evals,evecs=eigsh(op,k=16,which='LA',tol=1e-10,v0=v0,maxiter=1500);ii=np.argsort(evals)[::-1];evals=evals[ii];evecs=evecs[:,ii]
 residuals=[float(np.linalg.norm(matvec(evecs[:,j])-evals[j]*evecs[:,j])) for j in range(len(evals))]
 result=dict(operator=name,c=c,grid=N,largest_compact_eigenvalues=evals.tolist(),preconditioned_hessian_eigenvalues=(1-evals).tolist(),residuals=residuals,elapsed=time.time()-t)
 print(json.dumps(result),flush=True);rows.append(result)
 np.savez_compressed(base/f'round2_N4_spectrum_{name}.npz',eigenvalues=evals,eigenvectors=evecs,x=x)
zz=np.load(base/'round2_radial_mode1_dim4.npz');sp=CubicHermiteSpline(zz['r'],zz['y'][0],zz['y'][1]);rr=np.linspace(0,12,120001);q=sp(rr)
for c in [1.,3.]:
 b=float(np.max(rr**4*np.maximum(c*q*q-1,0)));l=0
 while (l*(l+2))**2<=b:l+=1
 print('RELlICH',c,b,l,flush=True)
 rows.append(dict(c=c,sampled_sup_r4_potential=b,high_angular_modes_positive_from_l=l))
(base/'round2_N4_spectrum_results.json').write_text(json.dumps(rows,indent=2))
