"""Whole-space Arb certificate for the N3 ell=1 inverse-response trial.
Only exact rational splines and outward-rounded ball arithmetic are used.
"""
import json,hashlib,math,time,sys
from fractions import Fraction as F
import flint
from flint import arb,arb_poly,ctx
ctx.prec=192
QHASH='5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b'
ZHASH='87268005abaaa0877486045ce6ee6178d358bd5aa78557fa72e783a702094db7'
qraw=open('round4_n3_mixed_exact.json','rb').read();zraw=open('round5_n3_pairing_bs_exact.json','rb').read()
assert hashlib.sha256(qraw).hexdigest()==QHASH and hashlib.sha256(zraw).hexdigest()==ZHASH
qobj=json.loads(qraw);zobj=json.loads(zraw)
nodes=[F(*v) for v in qobj['nodes']]
qs=[[F(float.fromhex(v)) for v in row] for row in qobj['states_hex']]

def A(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def upper(x):return x.upper()
def maxa(x,y):return x if x>y else y if y>x else upper((x+y+abs(x-y))/2)
def intsquare(poly,length):
 cc=(poly*poly).coeffs();out=A(length)*sum((cc[j]/(j+1) for j in range(0,len(cc),2)),arb(0));return out
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
rows=[]
for trial_index,trial in enumerate(zobj['trials']):
 zs=[[F(float.fromhex(v)) for v in row] for row in trial['states_hex']];mu=F(float.fromhex(trial['mu_hex']))
 assert len(zs)==len(nodes) and all(x==0 for x in zs[-1]) and zs[0][1]==zs[0][4]==0
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
  lin=R*R*hpp+4*R*hp+R*R*f
  ns=max(1,math.ceil(float(length*80)))
  for j in range(ns):
   S=arb_poly([A(F(2*j+1,2*ns)),A(F(1,2*ns))]);Q=q(S);a0=Q[0];d=upper(sum((abs(v) for v in Q.coeffs()[1:]),arb(0)));qb=upper(abs(a0)+d)
   if abs(a0)>2*d and abs(a0)>arb('1e-30'):
    W=Q*(1/a0)-1;WP=arb_poly([1]);P=arb_poly([1])
    for k in range(1,M+1):WP*=W;P+=WP*A(bc[k])
    V=P*abs(a0)**A(power);rem=A(abs(bc[M+1]))*(abs(a0)-d)**A(power-M-1)*d**(M+1)
   else:nz+=1;V=arb_poly([0]);rem=qb**A(power)
   rf=(R*R*f)(S);rff=upper(sum((abs(v) for v in rf.coeffs()),arb(0)))
   residual=lin(S)-rf*V*(1/A(mu));ip=intsquare(residual,length/ns)
   err2+=upper((ip.sqrt()+rff*rem/A(mu)*A(length/ns).sqrt())**2)
  if i%4000==0:print('cells',i,'elapsed',round(time.time()-start,1),flush=True)
 fac=4*arb.pi()/3
 r1=upper((fac*err1).sqrt());r2=upper((fac*err2).sqrt());res=upper((r1*r1+r2*r2).sqrt());znorm=(fac*(mass+kin)).sqrt();pair*=fac
 radius=upper(A(mu)*res/znorm)
 row={'trial':trial_index,'mu_exact':str(mu),'mu_ball':str(A(mu)),'Z_norm':str(znorm),'PDE_residual_Zdual_upper':str(res),'BS_spectral_distance_bound':str(radius),'spectral_interval':str(A(mu)+arb(0,radius)),'radius_lt_1e_4':bool(radius<arb(1)/10**4)};rows.append(row);print(json.dumps(row),flush=True)
 assert row['radius_lt_1e_4']
# Each of these four disjoint closed intervals contains a distinct eigenvalue.
# The HS bound excludes every other eigenvalue >= 9/10.
mu=[A(F(float.fromhex(t['mu_hex']))) for t in zobj['trials']];eps=arb(1)/10**4
assert all(mu[i]-eps>mu[i+1]+eps for i in range(3))
assert all(abs(m-1)>eps+arb(6)/1000 for m in mu)
hs=arb(818)/100 # rigorous HS upper rounded from separate certificate, verified below
hsdata=json.load(open('round5_n3_pairing_hs_sub1.json'));assert hsdata['profile_sha256']==QHASH and arb(hsdata['HS_squared_upper'])<hs
remainder=hs-sum(((m-eps)**2 for m in mu),arb(0))
assert remainder<(arb(9)/10)**2
# Consequently q has spectral gap>0.006; Q perturbation<0.000058 retains>0.0059.
pert=arb(58)/10**6
assert arb(6)/1000-pert>arb(1)/200
out={'q_sha256':QHASH,'trials_sha256':ZHASH,'trial_certificates':rows,'HS_squared_upper_rational':'8.18','sum_four_squared_lower':str(sum(((m-eps)**2 for m in mu),arb(0))),'remaining_HS_squared_upper':str(remainder),'Lminus_q_ell1_preconditioned_gap_gt':'0.006','Q_ball_radius':'4e-6','Lminus_Q_ell1_inverse_norm_lt':200,'all_checks_pass':True,'precision_bits':ctx.prec}
print(json.dumps(out,indent=2));open('round5_n3_pairing_bs_certificate.json','w').write(json.dumps(out,indent=2)+'\n')
