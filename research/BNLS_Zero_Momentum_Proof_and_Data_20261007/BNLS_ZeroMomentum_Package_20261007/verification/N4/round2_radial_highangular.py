from round2_radial_exact_common import *
from decimal import Decimal,localcontext,ROUND_CEILING
import hashlib
path='round2_radial_H4_exact_h1_16.json';nodes,polys=load_profile(path);results=[]
for beta,ell in [(1,5),(3,6)]:
 c=F(ell*(ell+2));theta=F(9,10);Bc=F(0);margin=None
 for j,p in enumerate(polys):
  a=nodes[j];h=nodes[j+1]-a;rp=[a,h];r2=mul(rp,rp);r4=mul(r2,r2);pot=scale(mul(r4,mul(p,p)),beta)
  Bc=max(Bc,*bernstein(add(pot,scale(r4,-1))))
  D=add(scale(add(r4,[c*c]),theta),scale(pot,-1));lo=min(bernstein(D));margin=lo if margin is None else min(margin,lo)
 assert margin>0
 with localcontext() as ctx:
  ctx.prec=70;ctx.rounding=ROUND_CEILING
  up=lambda x:str(Decimal(x.numerator)/Decimal(x.denominator))
  results.append({'beta':beta,'minimal_ell':ell,'c_ell_squared':str(c*c),'theta':str(theta),'all_Bernstein_coefficients_positive':True,'smallest_Bernstein_margin_exact':str(margin),'Bc_upper_exact':str(Bc),'Bc_upper_decimal':up(Bc),'verified_uniform_preconditioned_gap':'1/10','pointwise_statement':'beta r^4 q(r)^2 <= (9/10)(r^4+c_ell^2) for allr>=0','operator_statement':'Delta_l^2+1-betaq² >= (1/10)(Delta_l²+1) inquadraticformsfor ell>=minimal_ell'})
result={'canonical':path,'sha256':hashlib.sha256(open(path,'rb').read()).hexdigest(),'checks':results,'outside_support':'q=0 for r>=36, inequality immediate'}
open('round2_radial_highangular_certificate.json','w').write(json.dumps(result,indent=2));print(json.dumps({'canonical':path,'checks':[{k:v for k,v in r.items() if 'exact' not in k} for r in results]},indent=2))
