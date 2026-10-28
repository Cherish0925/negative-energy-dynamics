"""Interval inverse bound for the explicit seven-dimensional reference block."""
import json,hashlib
from pathlib import Path
from flint import arb,acb,acb_mat,ctx
ctx.prec=192
ROOT=Path(__file__).resolve().parent
j=json.loads((ROOT/'round5_radial_block_certificate_h2.json').read_text());B=[[arb(x) for x in row] for row in j['B0']]
# Boxes entirely in the first quadrant, one reference eigenvalue each.
rows=[]
for re0,re1,im0,im1 in [('1.5','4.5','4.5','7.5'),('1','5','4','8'),('1.5','4.5','3','9'),('2','5','3','9'),('1.5','6','2.5','10')]:
 corners=[acb(re0,im0),acb(re1,im0),acb(re1,im1),acb(re0,im1)];best=arb(0);N=160
 for a,b in zip(corners,corners[1:]+corners[:1]):
  for i in range(N):
   mid=a+(b-a)*arb(2*i+1)/(2*N);rad=b-a
   z=acb(mid.real+arb(0,abs(rad.real)/(2*N)),mid.imag+arb(0,abs(rad.imag)/(2*N)))
   M=acb_mat([[acb(B[k][l])-(z if k==l else 0) for l in range(7)] for k in range(7)]).inv()
   val=sum((abs(M[k,l])**2 for k in range(7) for l in range(7)),arb(0)).sqrt().upper()
   best=best.max(val).upper()
 row={'box':[re0,re1,im0,im1],'k_Frobenius_upper':str(best),'subintervals_per_side':N,'block_certificate_sha256':hashlib.sha256((ROOT/'round5_radial_block_certificate_h2.json').read_bytes()).hexdigest()};rows.append(row);print(row,flush=True)
(ROOT/'round5_radial_contour.json').write_text(json.dumps(rows,indent=2))
