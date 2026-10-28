"""Exact response certificate against the frozen canonical stationary trial.

Imports a pure helper module with no input/output or regeneration. This verifier
uses ONLY the canonical q JSON and the saved exact response jets. No approximate
ODE solver or source NPZ is read or run.
"""
import json,time
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
from round2_certificate_polynomial_common import (trim,add,scale,mul,power,derivative,integ01,
                                                bernstein_range,inv,ang_lo,ang_hi,angular_bound)
ROOT=str(Path(__file__).resolve().parent)+'/'
start=time.monotonic()
raw=json.load(open(ROOT+'round2_certificate_exact_rational_data.json'))
canon=json.load(open(ROOT+'round2_radial_H4_exact_h1_16.json'))
qx=[F(*v) for v in canon['nodes']]
qj=[[F(float.fromhex(v)) for v in row] for row in canon['jets_hex']]
vx=[F(raw['h'])*j for j in range(raw['count']+1)]
vj=[[F(v) for v in row] for row in raw['vjets']]

def herm(left,right,h):
 a=[left[j]*h**j/F(factorial(j)) for j in range(4)]
 rhs=[right[j]*h**j-sum((a[k]*F(factorial(k),factorial(k-j)) for k in range(j,4)),F(0)) for j in range(4)]
 return trim(a+[sum((inv[i][j]*rhs[j] for j in range(4)),F(0)) for i in range(4)])
def restrict(p,alpha,beta):
 return trim([sum((p[j]*comb(j,k)*alpha**(j-k)*beta**k for j in range(k,len(p))),F(0)) for k in range(len(p))])
qp=[herm(qj[j],qj[j+1],qx[j+1]-qx[j]) for j in range(len(qx)-1)]
vp=[herm(vj[j],vj[j+1],vx[j+1]-vx[j]) for j in range(len(vx)-1)]
nodes=sorted(set(qx+vx));qi=vi=0
names=['pair','kinetic','norm2','potential','source2','qmass','qkinetic','res2','psi4','qpsi4','psiD1']
tot={k:F(0) for k in names};maxq=maxpsi=F(0)
for a,b in zip(nodes[:-1],nodes[1:]):
 h=b-a
 while qi+1<len(qx) and a>=qx[qi+1]:qi+=1
 while vi+1<len(vx) and a>=vx[vi+1]:vi+=1
 q=restrict(qp[qi],(a-qx[qi])/(qx[qi+1]-qx[qi]),h/(qx[qi+1]-qx[qi])) if qi<len(qp) else [F(0)]
 v=restrict(vp[vi],(a-vx[vi])/(vx[vi+1]-vx[vi]),h/(vx[vi+1]-vx[vi])) if vi<len(vp) else [F(0)]
 rr=[a,h];rp=[power(rr,k) for k in range(8)]
 qd=[q]+[scale(derivative(q,k),h**(-k)) for k in range(1,5)]
 vd=[v]+[scale(derivative(v,k),h**(-k)) for k in range(1,5)]
 q2=mul(q,q);v2=mul(v,v);v4=mul(v2,v2)
 lo,hi=bernstein_range(q);maxq=max(maxq,abs(lo),abs(hi))
 lo,hi=bernstein_range(mul(rr,v));maxpsi=max(maxpsi,abs(lo),abs(hi))
 tot['pair']+=h*integ01(mul(mul(qd[1],v),rp[4]))
 dvnum=add(mul(rr,vd[2]),scale(vd[1],F(5)))
 dqnum=add(mul(rr,qd[2]),scale(qd[1],F(3)))
 tot['kinetic']+=h*integ01(mul(mul(dvnum,dvnum),rp[3]))
 tot['norm2']+=h*integ01(mul(v2,rp[5]))
 tot['potential']+=h*integ01(mul(mul(q2,v2),rp[5]))
 tot['source2']+=h*integ01(mul(mul(qd[1],qd[1]),rp[3]))
 tot['qmass']+=h*integ01(mul(q2,rp[3]))
 tot['qkinetic']+=h*integ01(mul(mul(dqnum,dqnum),rr))
 tot['psi4']+=h*integ01(mul(v4,rp[7]))
 tot['qpsi4']+=h*integ01(mul(mul(mul(q2,q2),v4),rp[7]))
 tot['psiD1']+=h*integ01(mul(mul(vd[1],vd[1]),rp[5]))
 Hv=mul(rp[2],qd[1])
 for poly,c in [(mul(rp[3],vd[4]),-1),(mul(rp[2],vd[3]),-10),(mul(rr,vd[2]),-15),(vd[1],15),(mul(rp[3],v),-1),(mul(mul(rp[3],q2),v),1)]:Hv=add(Hv,scale(poly,F(c)))
 Hv2=mul(Hv,Hv)
 if not a:
  assert all(not x for x in Hv[:3])
  tot['res2']+=sum((z/F(k) for k,z in enumerate(Hv2) if k),F(0))
 else:tot['res2']+=h/a*integ01(Hv2)
form=tot['kinetic']+tot['norm2']-tot['potential'];J=2*tot['pair']-form
checks={
 'canonical_q_Z_le_104':4*ang_hi*(tot['qmass']+tot['qkinetic'])<=104**2,
 'response_Z_le_132':ang_hi*(tot['kinetic']+tot['norm2'])<=132**2,
 'J_le_minus273':angular_bound(J)[1]<=-273,
 'form_le_minus273':angular_bound(form)[1]<=-273,
 'response_residual_le_0.000662':ang_hi*tot['res2']<=F(662,10**6)**2,
 'response_residual_le_0.001':ang_hi*tot['res2']<=F(1,1000)**2,
 'q_sup_le_6.73':maxq<=F(673,100),
 'psi_sup_le_6':maxpsi<=6,
 'psi_L2_le_104':ang_hi*tot['norm2']<=104**2,
 'psi_L4_le_18':ang_hi/2*tot['psi4']<=18**4,
 'qpsi_L4_le_26':ang_hi/2*tot['qpsi4']<=26**4,
 'qpsi_L2_le_133':ang_hi*tot['potential']<=133**2,
 'q_mass_norm_le_73':4*ang_hi*tot['qmass']<=73**2,
 'Tform_le_11950':ang_hi*(tot['kinetic']+tot['norm2']/2)<=11950,
 'potential_ge_17540':ang_lo*tot['potential']>=17540}
result={'canonical_q':'round2_radial_H4_exact_h1_16.json','response':'vjets in round2_certificate_exact_rational_data.json',
 'arithmetic':'exact rational polynomial integration; exact conservative weighted residual bound; Machin-series pi enclosure',
 'seconds':time.monotonic()-start,'common_intervals':len(nodes)-1,
 'q_Z2_upper':float(4*ang_hi*(tot['qmass']+tot['qkinetic'])),
 'response_Z2_upper':float(ang_hi*(tot['kinetic']+tot['norm2'])),
 'J_upper':float(angular_bound(J)[1]),'form_upper':float(angular_bound(form)[1]),
 'response_residual2_upper':float(ang_hi*tot['res2']),
 'q_sup_upper':float(maxq),'psi_sup_upper':float(maxpsi),
 'psi_L4_fourth_upper':float(ang_hi/2*tot['psi4']),
 'qpsi_L4_fourth_upper':float(ang_hi/2*tot['qpsi4']),
 'qpsi_L2_squared_upper':float(ang_hi*tot['potential']),
 'exact_boolean_checks':checks}
print(json.dumps(result,indent=2),flush=True)
with open(ROOT+'round2_certificate_canonical_results.json','w') as f:json.dump(result,f,indent=2)
with open(ROOT+'round2_certificate_canonical_integrals.json','w') as f:json.dump({k:str(v) for k,v in tot.items()},f)
assert all(checks.values())
