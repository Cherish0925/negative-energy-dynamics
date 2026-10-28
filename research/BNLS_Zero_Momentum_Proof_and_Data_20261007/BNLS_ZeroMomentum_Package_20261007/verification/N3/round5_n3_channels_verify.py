"""Whole-space Arb certificate for the N3 ell=1 inverse-response trial.
Only exact rational splines and outward-rounded ball arithmetic are used.
"""
import json,hashlib,math,time,sys
from fractions import Fraction as F
import flint
from flint import arb,arb_poly,ctx
ctx.prec=192
QHASH='5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b'
ell=int(sys.argv[1]);num=int(sys.argv[2]);D=2*ell+3;beta=F(11,3) if ell%2==0 else F(1)
qraw=open('round4_n3_mixed_exact.json','rb').read();zraw=open(f'round5_n3_channel_l{ell}_exact.json','rb').read()
assert hashlib.sha256(qraw).hexdigest()==QHASH
ZHASH=hashlib.sha256(zraw).hexdigest()
qobj=json.loads(qraw);zobj=json.loads(zraw)
assert zobj['ell']==ell and len(zobj['trials'])==num and zobj['profile_sha256']==QHASH
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
 zs=[[F(float.fromhex(v)) for v in row] for row in trial['states_hex']];mu=F(float.fromhex(trial['mu_hex']));assert mu>0
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
  delF=R**(ell+1)*fpp+(D-1)*R**ell*fp
  mass+=intsquare((R**(ell+1)*f)(T),length);kin+=intsquare(delF(T),length)
  pair+=integral((R*R*R*qp*f)(T),length)
  err1+=intsquare((delF-R**(ell+1)*h)(T),length)
  lin=R**(ell+1)*hpp+(D-1)*R**ell*hp+R**(ell+1)*f
  ns=max(1,math.ceil(float(length*80)))
  for j in range(ns):
   S=arb_poly([A(F(2*j+1,2*ns)),A(F(1,2*ns))]);Q=q(S);a0=Q[0];d=upper(sum((abs(v) for v in Q.coeffs()[1:]),arb(0)));qb=upper(abs(a0)+d)
   if abs(a0)>2*d and abs(a0)>arb('1e-30'):
    W=Q*(1/a0)-1;WP=arb_poly([1]);P=arb_poly([1])
    for k in range(1,M+1):WP*=W;P+=WP*A(bc[k])
    V=P*abs(a0)**A(power);rem=A(abs(bc[M+1]))*(abs(a0)-d)**A(power-M-1)*d**(M+1)
   else:nz+=1;V=arb_poly([0]);rem=qb**A(power)
   rf=(R**(ell+1)*f)(S);rff=upper(sum((abs(v) for v in rf.coeffs()),arb(0)))
   residual=lin(S)-rf*V*(A(beta)/A(mu));ip=intsquare(residual,length/ns)
   err2+=upper((ip.sqrt()+rff*rem*A(beta)/A(mu)*A(length/ns).sqrt())**2)
  if i%4000==0:print('cells',i,'elapsed',round(time.time()-start,1),flush=True)
 fac=arb(1)
 r1=upper((fac*err1).sqrt());r2=upper((fac*err2).sqrt());res=upper((r1*r1+r2*r2).sqrt());znorm=(fac*(mass+kin)).sqrt();pair*=fac
 radius=upper(A(mu)*res/znorm)
 row={'trial':trial_index,'mu_exact':str(mu),'mu_ball':str(A(mu)),'Z_norm':str(znorm),'PDE_residual_Zdual_upper':str(res),'BS_spectral_distance_bound':str(radius),'spectral_interval':str(A(mu)+arb(0,radius)),'radius_lt_1e_3':bool(radius<arb(1)/10**3)};rows.append(row);print(json.dumps(row),flush=True)
 assert row['radius_lt_1e_3']
# Disjoint spectral inclusion intervals plus a whole-space HS budget.
mu=[A(F(float.fromhex(t['mu_hex']))) for t in zobj['trials']];eps=arb(1)/10**3
assert all(mu[i]-eps>mu[i+1]+eps for i in range(num-1))
hsdata=json.load(open(f'round5_n3_channels_hs_l{ell}_sub1.json'))
assert hsdata['profile_sha256']==QHASH and hsdata['ell']==ell
hs=arb(hsdata['HS_squared_upper']);assert hs.is_finite()
remainder=hs-sum(((m-eps)**2 for m in mu),arb(0))
assert remainder>0 and remainder<1
remaining_bound=upper(remainder.sqrt())
gap=min([abs(m-1)-eps for m in mu]+[1-remaining_bound])
pert=A(beta)*arb(58)/10**6
assert gap-pert>arb(1)/200
out={'ell':ell,'beta':str(A(beta)),'q_sha256':QHASH,'trials_sha256':ZHASH,'trial_certificates':rows,'HS_squared_upper':str(hs),'sum_Ritz_squared_lower':str(sum(((m-eps)**2 for m in mu),arb(0))),'remaining_HS_squared_upper':str(remainder),'remaining_spectral_upper':str(remaining_bound),'q_preconditioned_gap_lower':str(gap.lower()),'Q_ball_radius':'4e-6','Q_preconditioned_gap_lower':str((gap-pert).lower()),'Q_inverse_norm_lt':200,'Q_negative_index_per_angular_mode':sum(bool(m-eps>1) for m in mu),'all_checks_pass':True,'precision_bits':ctx.prec}
print(json.dumps(out,indent=2));open(f'round5_n3_channels_certificate_l{ell}.json','w').write(json.dumps(out,indent=2)+'\n')
