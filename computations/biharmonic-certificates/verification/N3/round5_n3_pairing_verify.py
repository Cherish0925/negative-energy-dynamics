"""Whole-space Arb certificate for the N3 ell=1 inverse-response trial.
Only exact rational splines and outward-rounded ball arithmetic are used.
"""
import json,hashlib,math,time,sys
from fractions import Fraction as F
import flint
from flint import arb,arb_poly,ctx
ctx.prec=192
QHASH='5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b'
ZHASH='cfb526600b18373ba274a8960909ef2e10a3a5939dde1150c4d755387677635f'
qraw=open('round4_n3_mixed_exact.json','rb').read();zraw=open('round5_n3_pairing_exact.json','rb').read()
assert hashlib.sha256(qraw).hexdigest()==QHASH and hashlib.sha256(zraw).hexdigest()==ZHASH
qobj=json.loads(qraw);zobj=json.loads(zraw)
nodes=[F(*v) for v in qobj['nodes']]
qs=[[F(float.fromhex(v)) for v in row] for row in qobj['states_hex']]
zs=[[F(float.fromhex(v)) for v in row] for row in zobj['states_hex']]
assert len(nodes)==len(qs)==len(zs) and nodes[0]==0 and all(x==0 for x in zs[-1])
assert zs[0][1]==zs[0][4]==0
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

def integral(poly,length):
 cc=poly.coeffs();return A(length)*sum((cc[j]/(j+1) for j in range(0,len(cc),2)),arb(0))
M=8;power=F(8,3);bc=[F(1)]
for k in range(1,M+2):bc.append(bc[-1]*(power-k+1)/k)
err1=arb(0);err2=arb(0);mass=arb(0);kin=arb(0);pair=arb(0);nz=0;start=time.time()
for i in range(len(nodes)-1):
 a=nodes[i];length=nodes[i+1]-a
 q=poly(*qs[i][:3],*qs[i+1][:3],length,origin=i==0)
 f=poly(*zs[i][:3],*zs[i+1][:3],length,origin=i==0)
 h=poly(*zs[i][3:],*zs[i+1][3:],length,origin=i==0)
 R=arb_poly([A(a),A(length)]);T=arb_poly([arb(1)/2,arb(1)/2])
 qp=q.derivative()*(1/A(length));fp=f.derivative()*(1/A(length));fpp=fp.derivative()*(1/A(length));hp=h.derivative()*(1/A(length));hpp=hp.derivative()*(1/A(length))
 delF=R*R*fpp+4*R*fp
 mass+=intsquare((R*R*f)(T),length);kin+=intsquare(delF(T),length)
 pair+=integral((R*R*R*qp*f)(T),length)
 err1+=intsquare((delF-R*R*h)(T),length)
 lin=R*R*hpp+4*R*hp+R*R*f-R*qp
 ns=max(1,math.ceil(float(length*80)))
 for j in range(ns):
  S=arb_poly([A(F(2*j+1,2*ns)),A(F(1,2*ns))]);Q=q(S);a0=Q[0];d=upper(sum((abs(v) for v in Q.coeffs()[1:]),arb(0)));qb=upper(abs(a0)+d)
  if abs(a0)>2*d and abs(a0)>arb('1e-30'):
   W=Q*(1/a0)-1;WP=arb_poly([1]);P=arb_poly([1])
   for k in range(1,M+1):WP*=W;P+=WP*A(bc[k])
   V=P*abs(a0)**A(power);rem=A(abs(bc[M+1]))*(abs(a0)-d)**A(power-M-1)*d**(M+1)
  else:nz+=1;V=arb_poly([0]);rem=qb**A(power)
  rf=(R*R*f)(S);rff=upper(sum((abs(v) for v in rf.coeffs()),arb(0)))
  residual=lin(S)-rf*V;ip=intsquare(residual,length/ns)
  err2+=upper((ip.sqrt()+rff*rem*A(length/ns).sqrt())**2)
 if i%4000==0:print('cells',i,'elapsed',round(time.time()-start,1),flush=True)
fac=4*arb.pi()/3
r1=upper((fac*err1).sqrt());r2=upper((fac*err2).sqrt());res=upper((r1*r1+r2*r2).sqrt());znorm=upper((fac*(mass+kin)).sqrt());pair*=fac
rho=arb(4)/10**6
Vchange=upper(arb(8)/3*(arb(63)/10+rho/4)**(arb(5)/3)*rho/4)
gchange=arb(3)/5*rho
rq=upper(res+gchange+Vchange*znorm)
gnorm=arb(3)/5*(arb(137)+rho)
cert=json.load(open('round5_n3_pairing_bs_certificate.json'));assert cert['q_sha256']==QHASH and cert['all_checks_pass'] and cert['Lminus_Q_ell1_inverse_norm_lt']==200
B=arb(200)
Ierr=upper(res*znorm+2*gchange*znorm+Vchange*znorm**2+B*rq**2)
out={'status':'rigorous negative inverse pairing at the exact Q in the certified 4e-6 ball','q_sha256':QHASH,'z_sha256':ZHASH,'precision_bits':ctx.prec,'cells':len(nodes)-1,'C2_constraints_exact_except_origin_even_sextic':True,'norm_Z_trial_upper':str(znorm),'L2_DeltaZ_minus_H_upper':str(r1),'L2_DeltaH_plus_Z_minus_VZ_minus_dq_upper':str(r2),'Lminus_q_trial_minus_dq_Zdual_upper':str(res),'pair_dq_trial_interval':str(pair),'Q_ball_Z_radius':'4e-6','Lminus_potential_change_upper':str(Vchange),'exact_Q_response_residual_upper':str(rq),'certified_Lminus_Q_ell1_inverse_bound':200,'I_Q_error_upper':str(Ierr),'I_Q_upper':str(upper(pair+Ierr)),'pair_q_lt_minus1323':bool(pair<-1323),'Z_norm_lt_809':bool(znorm<809),'I_Q_negative':bool(pair+Ierr<0),'zero_safe_cells':nz,'seconds':time.time()-start,'python_flint_version':flint.__version__}
print(json.dumps(out,indent=2));open('round5_n3_pairing_certificate.json','w').write(json.dumps(out,indent=2)+'\n')
assert out['pair_q_lt_minus1323'] and out['Z_norm_lt_809'] and out['I_Q_negative']
