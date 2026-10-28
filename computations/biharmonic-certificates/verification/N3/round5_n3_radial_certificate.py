"""Whole-space radial N3 Birman--Schwinger spectral gap.
Frozen rational q, rigorous Arb potential interpolation + FFT moments,
finite-rank resolvent tail, explicit half-line/box Green error.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,math,hashlib,time,sys
from fractions import Fraction as F
import flint
from flint import arb,acb,arb_poly,arb_mat,ctx
ctx.prec=128
EXPECTED='5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b'
raw=open('round4_n3_mixed_exact.json','rb').read();assert hashlib.sha256(raw).hexdigest()==EXPECTED
obj=json.loads(raw);nodes=[F(*v) for v in obj['nodes']];states=[[F(float.fromhex(v)) for v in row] for row in obj['states_hex']]
R=64;ngrid=65536;m=640;h=F(R,ngrid);power=F(8,3);c=F(11,3)
def A(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def up(x):return x.upper()
def maxa(x,y):return x if x>y else y if y>x else up((x+y+abs(x-y))/2)
def solve3(M,r):
 rows=[[F(v) for v in row]+[rhs] for row,rhs in zip(M,r)]
 for i in range(3):
  fac=rows[i][i];rows[i]=[v/fac for v in rows[i]]
  for j in range(3):
   if i!=j:
    fac=rows[j][i];rows[j]=[v-fac*w for v,w in zip(rows[j],rows[i])]
 return [row[-1] for row in rows]
def poly(f0,fp0,fpp0,f1,fp1,fpp1,h,origin=False):
 if origin:
  a2,a4,a6=solve3([[1,1,1],[2,4,6],[2,12,30]],[f1-f0,h*fp1,h*h*fpp1]);co=[f0,F(0),a2,F(0),a4,F(0),a6]
 else:
  co=[f0,h*fp0,h*h*fpp0/2];co+=solve3([[1,1,1],[3,4,5],[6,12,20]],[f1-sum(co),h*fp1-co[1]-2*co[2],h*h*fpp1-2*co[2]])
 return arb_poly([A(v) for v in co])
def sup_poly(p):return up(sum((abs(v) for v in p(arb_poly([arb(1)/2,arb(1)/2])).coeffs()),arb(0)))
start=time.time();polys=[];potsecond=arb(0);potsup=arb(0);weighted=arb(0)
for i in range(len(nodes)-1):
 a=nodes[i];l=nodes[i+1]-a;pp=poly(*states[i][:3],*states[i+1][:3],l,origin=i==0);polys.append(pp)
 qp=pp.derivative()*(1/A(l));qpp=qp.derivative()*(1/A(l));qb=sup_poly(pp);qpb=sup_poly(qp);qppb=sup_poly(qpp)
 vb=A(c)*qb**A(power);vs=A(c)*(A(power*(power-1))*qb**A(power-2)*qpb*qpb+A(power)*qb**A(power-1)*qppb)
 potsup=maxa(potsup,vb);potsecond=maxa(potsecond,vs);weighted+=A(l)*vb*(arb(2).sqrt()*A(nodes[i+1])).exp()
interp=up(potsecond*A(h*h)/8)
boundary=up(2/( (2*arb(2).sqrt()*R/2).exp()-1 )*weighted)
# 2 exp(-sqrt(2) R)/(1-exp(-sqrt(2) R)) times integral V exp(sqrt(2)r).
print('polynomials',len(polys),'Vsup',potsup,'Vsecond',potsecond,'interp',interp,'boundary',boundary,'sec',time.time()-start,flush=True)
# Exact equally spaced samples of the rational spline; interval-powered V.
vals=[];ix=0
for j in range(ngrid+1):
 rr=F(j)*h
 while ix<len(nodes)-2 and rr>nodes[ix+1]:ix+=1
 if rr>=nodes[-1]:vals.append(arb(0));continue
 qq=polys[ix](A((rr-nodes[ix])/(nodes[ix+1]-nodes[ix])))
 vals.append(A(c)*abs(qq)**A(power))
print('sampled',len(vals),'sec',time.time()-start,flush=True)
# Even extension; radix-two FFT in complex balls is a rigorous DCT-I.
arr=[acb(v) for v in vals[:-1]]+[acb(v) for v in vals[-1:0:-1]]
n=len(arr);rev=0
for i in range(1,n):
 bit=n>>1
 while rev&bit:rev^=bit;bit>>=1
 rev^=bit
 if i<rev:arr[i],arr[rev]=arr[rev],arr[i]
length=2
while length<=n:
 root=acb(0,-2*arb.pi()/length).exp();half=length//2
 tw=[acb(1)]
 for j in range(1,half):tw.append(tw[-1]*root)
 for a in range(0,n,length):
  for j in range(half):
   x=arr[a+j];y=arr[a+j+half]*tw[j];arr[a+j]=x+y;arr[a+j+half]=x-y
 print('fft',length,'sec',round(time.time()-start,2),flush=True);length*=2
mom=[]
for k in range(2*m+1):
 t=arb.pi()*k/(2*ngrid);sinc=arb(1) if k==0 else t.sin()/t
 mom.append(A(h)/2*arr[k].real*sinc*sinc)
weights=[1/((arb.pi()*i/R)**4+1).sqrt() for i in range(1,m+1)]
B=arb_mat(m,m)
for i in range(m):
 for j in range(m):B[i,j]=weights[i]*weights[j]*(mom[abs(i-j)]-mom[i+j+2])/R
print('matrix','sec',time.time()-start,flush=True)
# Store rigorous balls; spectral verification below uses exact IEEE witnesses.
npzfile='round5_n3_radial_spectral_witness.npz'
import numpy as np
from scipy.linalg import eigh
mid=np.array([[float(B[i,j].mid()) for j in range(m)] for i in range(m)])
eig,O=eigh(mid)
np.savez_compressed(npzfile,eigenvalues=eig,eigenvectors=O)
# Arb products certify orthogonality and residual of the exact IEEE witnesses.
Om=arb_mat([[arb(F(float(O[i,j])).numerator)/F(float(O[i,j])).denominator for j in range(m)] for i in range(m)])
lam=[A(F(float(v))) for v in eig]
print('eigh first top',eig[-10:],'gap',min(abs(eig-1)),'sec',time.time()-start,flush=True)
G=Om.transpose()*Om
orth2=arb(0)
for i in range(m):
 for j in range(m):orth2+=abs(G[i,j]-(1 if i==j else 0))**2
orth=up(orth2.sqrt());print('orth',orth,'sec',time.time()-start,flush=True)
Res=B*Om
res2=arb(0)
for i in range(m):
 for j in range(m):res2+=abs(Res[i,j]-Om[i,j]*lam[j])**2
res=up(res2.sqrt())
# If ||O^T O-I|| <= e<1, each exact spectrum point of symmetric B
# lies within ||BO-O Lambda|| / sqrt(1-e) of some stored lambda.
# This follows by O^{-1} B O = Lambda+O^{-1} Res and Bauer--Fike for diagonal Lambda.
spectral=up(res/(1-orth).sqrt())
tail=up(potsup/(1+(arb.pi()*(m+1)/R)**4))
err=up(interp+boundary+tail+spectral)
finitegap=min(abs(v-1) for v in lam);gap=finitegap-err
out={'profile_sha256':EXPECTED,'precision_bits':ctx.prec,'box_R':R,'linear_potential_intervals':ngrid,'sine_rank':m,'potential_sup':str(potsup),'potential_second_derivative_bound':str(potsecond),'potential_Linfty_interpolation_error':str(interp),'whole_space_box_kernel_error':str(boundary),'high_frequency_operator_error':str(tail),'eigenvector_orthogonality_Frobenius':str(orth),'eigensystem_residual_Frobenius':str(res),'finite_matrix_spectral_error':str(spectral),'total_spectral_error':str(err),'finite_matrix_gap_at_1':str(finitegap),'whole_space_gap_lower':str(gap.lower()),'inverse_norm_lt25':bool(gap>arb(1)/25),'eigenvalues_near_one':[float(v) for v in eig if .5<v<2],'seconds':time.time()-start,'python_flint_version':flint.__version__}
print(json.dumps(out,indent=2),flush=True);open('round5_n3_radial_certificate.json','w').write(json.dumps(out,indent=2)+'\n')
assert out['inverse_norm_lt25']
