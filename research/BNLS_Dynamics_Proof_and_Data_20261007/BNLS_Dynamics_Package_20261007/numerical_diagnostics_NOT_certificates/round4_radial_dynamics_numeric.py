import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time
from fractions import Fraction
from scipy.interpolate import BPoly
from scipy.sparse import diags,bmat,csc_matrix
from scipy.sparse.linalg import splu,eigs
from scipy.linalg import eigvals
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'round2_radial_H4_exact_h1_16.json').read_text());xs=np.array([float(Fraction(*v)) for v in raw['nodes']]);jets=np.array([[float.fromhex(v) for v in row] for row in raw['jets_hex']]);bp=BPoly.from_derivatives(xs,jets)
rows=[]
for R,h in [(30,.08),(40,.04),(40,.02),(40,.01),(50,.01)]:
 st=time.time();n=round(R/h)-1;r=np.arange(1,n+1)*h
 q=np.where(r<36,bp(np.minimum(r,36)),0);qp=np.where(r<36,bp(np.minimum(r,36),1),0)
 qw=q*r**1.5;fw=(q/2+r*qp/4)*r**1.5
 M=h*qw@qw;FQ=h*fw@qw;fw=fw-(FQ/M)*qw
 H=diags([-np.ones(n-1)/h**2,2*np.ones(n)/h**2+.75/r**2,-np.ones(n-1)/h**2],[-1,0,1],format='csc');A=H@H+diags(np.ones(n),format='csc')
 lm=A-diags(q*q,format='csc');lp=A-diags(3*q*q,format='csc')
 saddle=bmat([[lm,csc_matrix(qw[:,None])],[csc_matrix(qw[None,:]),None]],format='csc')
 sol=splu(saddle).solve(np.r_[fw,0]);z=sol[:-1]
 op=bmat([[None,lm],[-lp,None]],format='csc')
 if n<500:
  ev=eigvals(op.toarray());unst=ev[ev.real>1e-5];unst=unst[np.argsort(unst.real)[::-1]];spectra=[{'sigma':'all','eigenvalues':[[float(a.real),float(a.imag)] for a in unst[:16]]}]
 else:
  spectra=[]
  for sig in [0.1,0.5,1.,2.,4.]:
   ev=eigs(op,k=6,sigma=sig,which='LM',return_eigenvectors=False,tol=1e-8)
   spectra.append({'sigma':sig,'eigenvalues':[[float(a.real),float(a.imag)] for a in ev]})
 row={'R':R,'h':h,'n':n,'mass_radial':M,'uncorrected_f_Q':FQ,'H_radial_no_sphere':float(h*fw@z),'H_full':float(2*np.pi**2*h*fw@z),'z_norm_full':float(np.sqrt(2*np.pi**2*h*z@z)),'constraint_z_Q':float(h*qw@z),'saddle_multiplier':float(sol[-1]),'spectra':spectra,'seconds':time.time()-st}
 rows.append(row);print(json.dumps(row),flush=True)
 (ROOT/'round4_radial_dynamics_numeric.json').write_text(json.dumps(rows,indent=2))
