from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from r21_orbital_search import *
from scipy.ndimage import maximum_filter
from scipy.spatial.distance import pdist

def physical_basis(x,nmax):
 h=np.empty((len(x),nmax+1));h[:,0]=np.pi**(-.25)*np.exp(-x*x/2)
 if nmax:h[:,1]=np.sqrt(2)*x*h[:,0]
 for n in range(1,nmax):h[:,n+1]=np.sqrt(2/(n+1))*x*h[:,n]-np.sqrt(n/(n+1))*h[:,n-1]
 return h

def inspect(path,grid=501,L=13):
 d=np.load(Path(path).name);C=d['C'];ix=d['ix'];cut=ix.max();N=C.shape[1];x=np.linspace(-L,L,grid);dx=x[1]-x[0]
 h=physical_basis(x,cut+1);dh=np.zeros_like(h[:,:cut+1])
 for n in range(cut+1):
   dh[:,n]=-np.sqrt((n+1)/2)*h[:,n+1]
   if n:dh[:,n]+=np.sqrt(n/2)*h[:,n-1]
 # Direct equispaced full-plane-truncated quadrature, independent from GH.
 coeff=np.zeros((cut+1,cut+1,N),dtype=C.dtype)
 for k,(a,b) in enumerate(ix):coeff[a,b]=C[k]
 Y=np.einsum('ia,abn,jb->ijn',h[:,:cut+1],coeff,h[:,:cut+1],optimize=True)
 Yx=np.einsum('ia,abn,jb->ijn',dh,coeff,h[:,:cut+1],optimize=True)
 Yy=np.einsum('ia,abn,jb->ijn',h[:,:cut+1],coeff,dh,optimize=True)
 rho=np.sum(abs(Y)**2,2);F=np.sum(rho*rho)*dx*dx;T=(np.sum(abs(Yx)**2)+np.sum(abs(Yy)**2))*dx*dx
 gram=np.einsum('ijn,ijm->nm',Y.conj(),Y)*dx*dx
 mask=(rho==maximum_filter(rho,size=11))&(rho>.15*rho.max());ij=np.argwhere(mask);pts=np.array([(x[i],x[j],rho[i,j]) for i,j in ij]);pts=pts[np.argsort(-pts[:,2])]
 # Projected Euler-Lagrange Schr operator eigenvalues.
 ix2,D,K,xx=basis(cut,qextra=9);Z=D@C;rr=np.sum(abs(Z)**2,1);R=np.dot(rr,rr)/np.vdot(C,K@C).real
 ell=C.conj().T@K@C-(2/R)*(Z.conj().T@(rr[:,None]*Z));ev=la.eigvalsh(ell)
 tail=np.sum(rho[(x[:,None]**2+x[None,:]**2)>10**2])*dx*dx
 result=dict(path=path,rank=N,cut=int(cut),R_direct=float(F/T),R_GH_recheck=float(R),T_direct=float(T),F_direct=float(F),gram_error_direct=float(la.norm(gram-np.eye(N))),tail_mass_r_gt_10=float(tail),density_peaks=pts.tolist(),multipliers=ev.tolist())
 if len(pts)>1:
   result['minimum_peak_distance_in_core_units']=float(np.min(pdist(pts[:,:2]))*np.sqrt(T/N))
   # Gauge invariant localization: local Gram eigenvalues in Voronoi cells.
   X,Ygrid=np.meshgrid(x,x,indexing='ij');dist=(X[:,:,None]-pts[:,0])**2+(Ygrid[:,:,None]-pts[:,1])**2;labels=np.argmin(dist,2)
   spectra=[]
   for cell in range(len(pts)):
     W=Y[labels==cell];G=W.conj().T@W*dx*dx;spectra.append(la.eigvalsh(G)[::-1].tolist())
   result['local_gram_eigenvalues']=spectra
   result['mean_leading_local_eigenvalue']=float(np.mean([ev[0] for ev in spectra]))
 return result,rho,x

if __name__=='__main__':
 rows=json.load(open('r21_orbital_refinement.json'));out=[]
 import matplotlib;matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 fig,axs=plt.subplots(2,4,figsize=(12,6),layout='constrained')
 for col,N in enumerate([2,3,4,6]):
   for row,cut in enumerate([16,40]):
     allrows=json.load(open('r21_orbital_results.json')) if cut==16 else rows
     rr=max([r for r in allrows if r['rank']==N and r['cut']==cut],key=lambda r:r['quotient'])
     data,rho,x=inspect(rr['coefficients']);out.append(data);print(json.dumps(data),flush=True)
     axs[row,col].imshow(rho.T,origin='lower',extent=[x[0],x[-1],x[0],x[-1]],cmap='inferno');axs[row,col].set(xlim=(-9,9),ylim=(-9,9),title=f'N={N}, degree={cut}\nR={data["R_direct"]:.9f}',xlabel='x',ylabel='y')
 fig.savefig('r21_orbital_densities.png',dpi=160)
 with open('r21_orbital_independent_checks.json','w') as f:json.dump(out,f,indent=2)
