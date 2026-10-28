"""Rigorous N3 mixed residual and angular-tail certificate.
All inputs are frozen exact rationals. Arb handles outward rounding and
noninteger real powers; no sampled residual or floating quadrature is used.
"""
import json,hashlib,math,time,sys
from fractions import Fraction as F
import flint
from flint import arb,arb_poly,ctx
ctx.prec=192
EXPECTED='5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b'
raw=open('round4_n3_mixed_exact.json','rb').read();assert hashlib.sha256(raw).hexdigest()==EXPECTED
obj=json.loads(raw);nodes=[F(*v) for v in obj['nodes']];states=[[F(float.fromhex(v)) for v in row] for row in obj['states_hex']]
assert nodes[0]==0 and states[0][1]==states[0][4]==0 and all(v==0 for v in states[-1])
def A(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def upper(x):return x.upper()
def maxa(x,y):return x if x>y else y if y>x else upper((x+y+abs(x-y))/2)
def intsquare(poly,length):
 cc=(poly*poly).coeffs();out=A(length)*sum((cc[j]/(j+1) for j in range(0,len(cc),2)),arb(0));return upper(out)
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
  a2,a4,a6=solve3([[1,1,1],[2,4,6],[2,12,30]],[f1-f0,h*fp1,h*h*fpp1]);c=[f0,F(0),a2,F(0),a4,F(0),a6]
 else:
  c=[f0,h*fp0,h*h*fpp0/2]
  rhs=[f1-sum(c),h*fp1-c[1]-2*c[2],h*h*fpp1-2*c[2]]
  c+=solve3([[1,1,1],[3,4,5],[6,12,20]],rhs)
 assert c[0]==f0 and c[1]==h*fp0
 assert sum(c)==f1 and sum(j*c[j] for j in range(len(c)))==h*fp1
 assert sum(j*(j-1)*c[j] for j in range(len(c)))==h*h*fpp1
 if not origin:assert 2*c[2]==h*h*fpp0
 return arb_poly([A(v) for v in c])

M=8;beta=F(11,3);power=F(8,3);bc=[F(1)]
for k in range(1,M+2):bc.append(bc[-1]*(beta-k+1)/k)
SUB=int(sys.argv[1]) if len(sys.argv)>1 else 1
err1=arb(0);err2=arb(0);mass=arb(0);kin=arb(0);qmax=arb(0);cminus=arb(0);cplus=arb(0);nz=0;worst=arb(0);wi=None;start=time.time()
for i in range(len(nodes)-1):
 a=nodes[i];h=nodes[i+1]-a;assert h>0
 q=poly(*states[i][:3],*states[i+1][:3],h,origin=i==0);z=poly(*states[i][3:],*states[i+1][3:],h,origin=i==0)
 rp=arb_poly([A(a),A(h)]);qp=q.derivative()*(1/A(h));qpp=qp.derivative()*(1/A(h));zp=z.derivative()*(1/A(h));zpp=zp.derivative()*(1/A(h))
 trans=arb_poly([arb(1)/2,arb(1)/2]);mass+=intsquare((rp*q)(trans),h);kin+=intsquare((rp*qpp+2*qp)(trans),h)
 e1=rp*qpp+2*qp-rp*z;err1+=intsquare(e1(trans),h)
 lin=rp*zpp+2*zp+rp*q
 ns=max(SUB,math.ceil(float(h*80*SUB)))
 for j in range(ns):
  T=arb_poly([A(F(2*j+1,2*ns)),A(F(1,2*ns))]);Q=q(T);R=rp(T);a0=Q[0];d=upper(sum((abs(v) for v in Q.coeffs()[1:]),arb(0)));qb=upper(abs(a0)+d);qmax=maxa(qmax,qb)
  right=A(a+h*F(j+1,ns));length=h/ns
  vm=upper(right**4*(qb**A(power)-A(F(4,5))));vp=upper(right**4*(A(F(11,3))*qb**A(power)-A(F(4,5))))
  cminus=maxa(cminus,vm);cplus=maxa(cplus,vp)
  if abs(a0)>2*d and abs(a0)>arb('1e-30'):
   W=Q*(1/a0)-1;WP=arb_poly([1]);P=arb_poly([1])
   for k in range(1,M+1):WP*=W;P+=WP*A(bc[k])
   NF=P*((1 if a0>0 else -1)*abs(a0)**A(beta))
   rem=A(abs(bc[M+1]))*(abs(a0)-d)**A(beta-M-1)*d**(M+1)
  else:nz+=1;NF=arb_poly([0]);rem=qb**A(beta)
  residual=lin(T)-R*NF;ip=intsquare(residual,length);assert ip>=0
  e=upper(right*rem);ib=upper((ip.sqrt()+e*A(length).sqrt())**2);err2+=ib
  if ib>worst:worst=ib;wi=(i,j,float(a))
 if i%3000==0:print('progress',i,'dual residual',((4*arb.pi()*err1).sqrt()+(4*arb.pi()*err2).sqrt()).str(9),'sec',round(time.time()-start,1),flush=True)
factor=4*arb.pi();r1=upper((factor*err1).sqrt());r2=upper((factor*err2).sqrt());res=upper((r1*r1+r2*r2).sqrt());znorm=upper((factor*(mass+kin)).sqrt())
# H2(R3)->Linf norm is 1/sqrt(4 sqrt(2) pi) < 1/4.
# A perturbation of Z norm <=1/1000 changes the linearized potential by <1/10.
# For both c=1 and 11/3 use q_bound <63/10, delta<=1/4000.
delta=arb(1)/4000;change=upper(A(F(11,3))*A(F(8,3))*(A(F(63,10))+delta)**A(F(5,3))*delta)
out={'status':'exact H2 approximate profile with certified H−2 residual; existence not yet certified','profile_sha256':EXPECTED,'verifier_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest(),'precision_bits':ctx.prec,'subdivision_multiplier':SUB,'profile_cells':len(nodes)-1,'C2_constraints_exact_except_no_second_jet_assumed_at_origin':True,'origin_even_sextics':True,'Delta_q_minus_z_L2_upper':str(r1),'Delta_z_plus_q_minus_nonlinearity_L2_upper':str(r2),'PDE_residual_Hminus2_Zdual_upper':str(res),'Z_norm_upper':str(znorm),'Linfty_upper':str(upper(qmax)),'minus_angular_budget_upper':str(upper(cminus)),'plus_angular_budget_upper':str(upper(cplus)),'minus_ell_ge13_gap_ge_one_fifth':bool(cminus<A(F(4,5)*13*14*(13*14-2))),'plus_ell_ge20_gap_ge_one_fifth':bool(cplus<A(F(4,5)*20*21*(20*21-2))),'Zball_1over1000_linearization_change_upper':str(change),'Zball_1over1000_tail_gap_ge_1over10':bool(change<arb(1)/10),'zero_safe_cells':nz,'worst_second_defect_cell':wi,'residual_lt_13e_8':bool(res<arb(13)/10**8),'residual_lt_1e_6':bool(res<arb(1)/10**6),'residual_lt_1e_7':bool(res<arb(1)/10**7),'Znorm_lt137':bool(znorm<137),'Linfty_lt6_3':bool(qmax<arb(63)/10),'seconds':time.time()-start,'python_flint_version':flint.__version__}
print(json.dumps(out,indent=2));open(f'round4_n3_mixed_certificate_sub{SUB}.json','w').write(json.dumps(out,indent=2)+'\n')
assert out['minus_ell_ge13_gap_ge_one_fifth'] and out['plus_ell_ge20_gap_ge_one_fifth'] and out['Zball_1over1000_tail_gap_ge_1over10']

assert out['residual_lt_13e_8'] and out['Znorm_lt137'] and out['Linfty_lt6_3']
