"""Interval proof of log(1/k) H4(k)<1, conditional on enclosed shooting output.
All interval arithmetic is mpmath.iv at 60 decimal places; output reports
rational rounded upper bounds, and each inequality is checked at runtime.
"""
import sys,json,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from r25_interval_shoot import I,iv,mp,ends,enc,raw

def val(raw):return iv.make_mpf(tuple(tuple(v) for v in raw))
def up(x):return I(ends(x)[1])
def positive(x):return ends(x)[0]>0

def run():
 bracket=json.loads(Path('research/r25_shoot_bracket.json').read_text())
 assert bracket[0]['status']=='undershoot' and bracket[0]['positive_on_all_step_tubes']
 assert bracket[1]['status']=='overshoot'
 assert positive(val(bracket[0]['p_raw'])) and positive(-val(bracket[1]['q_raw']))
 data=json.loads(Path('research/r25_shoot_2_2062008646507_2_2062008646508.json').read_text())
 rows=data['rows'];nodes=[I(0)]+[val(t['r_raw']) for t in rows]
 values=[up(val(data['a_raw']))]+[up(val(t['q_raw'])) for t in rows]
 # values[i] bounds Q at nodes[i], hence on interval i by strict decrease.
 assert len(nodes)==len(values)
 A=I('2.82');R=I(8);qr=values[-1];beta=I('.9999999')
 assert positive(1-beta**2-qr**2)
 Bl=iv.sqrt(iv.pi/(2*R))*iv.exp(-R)*(1-1/(8*R))
 Abound=qr/Bl+qr**3*iv.exp(R)*(R/(3*beta-1)+1/(3*beta-1)**2)
 assert ends(Abound)[1]<ends(A)[0]
 print('tail coefficient upper',enc(Abound),flush=True)
 N=512
 moments=[I(0) for _ in range(N+1)]
 for i in range(len(nodes)-1):
  l,u=nodes[i:i+2];V=values[i]**2
  pl=l*l;pu=u*u
  for n in range(N+1):
   moments[n]+=V*(pu-pl)/(2*n+2)
   pl*=l*l/(n+1)**2;pu*=u*u/(n+1)**2
  if i%200==0:print('moment panels',i,flush=True)
 # Tail: Q² <= A²*pi/(2r)*exp(-2r).  t_n=integral_R∞ r^(2n)e^-2r/(n!)².
 expR=iv.exp(-2*R);tn=expR/2;rp=I(1)
 for n in range(N+1):
  if n:
   rp*=R*R/(n*n)
   tn=expR*rp*(I(1)/2+I(n)/(2*R))+I(2*n-1)/(2*n)*tn
  moments[n]+=A*A*iv.pi/2*tn
 # Exact compact triangular integration of HS norm, with elementary tail bound.
 theta=[]
 for m in range(1,5):
  acc=I(0);outer=I(0)
  for i in range(len(nodes)-1):
   l,u=nodes[i:i+2];V=values[i]**2
   if i==0:outer+=V*V*u**4/(4*(2*m+2))
   else:
    J=iv.log(u/l) if m==1 else (u**(2-2*m)-l**(2-2*m))/(2-2*m)
    outer+=V*(acc*J+V/(2*m+2)*((u**4-l**4)/4-l**(2*m+2)*J))
   acc+=V*(u**(2*m+2)-l**(2*m+2))/(2*m+2)
  # Full moment mu_m=(m!)² moments[m].
  fac=1
  for j in range(1,m+1):fac*=j
  outer+=moments[m]*fac*fac*A*A*iv.pi/(4*R**(2*m))*expR
  theta.append(up(iv.sqrt(outer/(2*m*m))))
 print('theta upper', [enc(x) for x in theta],flush=True)
 assert all(ends(t)[1]<1 for t in theta)
 assert all(ends(t)[1]<=ends(theta[0])[1] for t in theta)
 dtail=1-theta[0]/5
 coeff=[];central=I(1)
 for n in range(N+1):
  if n:central*=I(2*n-1)/(2*n)
  weight=(1-central)/dtail
  for m in range(1,min(4,n)+1):
   ratio=I(1)
   for j in range(m):ratio*=I(n-j)/(n+j+1)
   weight+=2*central*ratio*(1/(1-theta[m-1])-1/dtail)
  if n:assert positive(weight)
  coeff.append(up(weight*moments[n]))
 C=A*A*iv.pi/(4*(1-theta[0]))
 def H(k):
  # Positive series partial sum, plus global rough envelope for all omitted terms.
  z=k*k;ans=I(0)
  for c in reversed(coeff):ans=ans*z+c
  return ans+C*z**(N+1)/(1-z)
 # low endpoint, using log(1/k)k² increasing on (0,.01].
 low=I('.01')
 low_bound=A*A*iv.pi*low**2*iv.log(1/low)/(16*(1-theta[0])*(1-low)**3)
 assert ends(low_bound)[1]<1
 # high endpoint via I0(z)<=exp(z)*sqrt(pi)/(2sqrt(2z)).
 high=I('.997')
 # log(1/k)<= (1-k)/k: resulting sqrt(1-k)/k^(3/2) decreases with k.
 high_bound=A*A*iv.pi**2*iv.sqrt(1-high)/(8*iv.sqrt(2)*(1-theta[0])*high**(I(3)/2))
 assert ends(high_bound)[1]<1
 # Full interval coverage by monotonic H(k); exact rational partition.
 points=[I(j)/1000 for j in range(10,998)]
 bounds=[]
 for a,b in zip(points[:-1],points[1:]):
  bound=iv.log(1/a)*H(b)
  assert ends(bound)[1]<ends(I(24)/25)[0],(enc(a),enc(b),enc(bound))
  bounds.append(ends(bound)[1])
 maximum=max(bounds);imax=bounds.index(maximum)
 out={'status':'interval certificate; requires verified shooting bracket and standard uniqueness/shooting theorem',
      'precision_decimal':iv.dps,'series_terms':N+1,'profile_panels':len(nodes)-1,
      'global_Q_over_K0_upper':'2.82','tail_coefficient_bound':enc(Abound),
      'theta_upper':[enc(x) for x in theta],
      'low_endpoint_bound':enc(low_bound),'high_endpoint_bound':enc(high_bound),
      'compact_intervals':len(bounds),'compact_maximum_upper':mp.nstr(maximum,40),
      'maximizing_interval':[enc(points[imax]),enc(points[imax+1])],
      'rational_uniform_upper':'24/25',
      'all_k_upper':mp.nstr(max(maximum,ends(low_bound)[1],ends(high_bound)[1]),40)}
 Path('research/r25_uniform_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2),flush=True)
 return out
if __name__=='__main__':run()
