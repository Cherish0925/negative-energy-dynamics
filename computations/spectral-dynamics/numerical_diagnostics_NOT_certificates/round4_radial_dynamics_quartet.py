import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time
from fractions import Fraction
from scipy.interpolate import BPoly
from scipy.sparse import diags,bmat
from scipy.sparse.linalg import eigs
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'round2_radial_H4_exact_h1_16.json').read_text());xs=np.array([float(Fraction(*v)) for v in raw['nodes']]);jets=np.array([[float.fromhex(v) for v in row] for row in raw['jets_hex']]);bp=BPoly.from_derivatives(xs,jets)
rows=[]
for R,h in [(30,.08),(40,.04),(40,.02),(40,.01),(50,.01),(40,.005)]:
 st=time.time();n=round(R/h)-1;r=np.arange(1,n+1)*h
 q=np.where(r<36,bp(np.minimum(r,36)),0)
 H=diags([-np.ones(n-1)/h**2,2*np.ones(n)/h**2+.75/r**2,-np.ones(n-1)/h**2],[-1,0,1],format='csc');A=H@H+diags(np.ones(n),format='csc');lm=A-diags(q*q,format='csc');lp=A-diags(3*q*q,format='csc')
 op=bmat([[None,lm],[-lp,None]],format='csc').astype(complex)
 ev,vec=eigs(op,k=3,sigma=3+6.4j,which='LM',tol=1e-10)
 j=np.argmin(abs(ev-(3+6.4j)));lam=ev[j];v=vec[:,j]
 row={'R':R,'h':h,'n':n,'quartet_eigenvalue':[float(lam.real),float(lam.imag)],'FD_residual_norm':float(np.linalg.norm(op@v-lam*v)),'seconds':time.time()-st}
 rows.append(row);print(json.dumps(row),flush=True)
 (ROOT/'round4_radial_dynamics_quartet.json').write_text(json.dumps(rows,indent=2))
 if h==.01 and R==40:np.savez(ROOT/'round4_radial_dynamics_quartet_vector.npz',r=r,real_component=v[:n],imag_component=v[n:],eigenvalue=lam)
