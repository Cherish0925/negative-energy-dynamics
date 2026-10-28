#!/usr/bin/env python3
"""Certify an H^-2 residual of the unchanged canonical N4 profile.
The auxiliary field is defined only from frozen exact nodal jets and the ODE.
All polynomial coefficients are rational; Arb encloses polynomial integrals.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time
from flint import arb,arb_poly,ctx
from round2_verify_frozen_ritz import load_jets,hermite
ctx.prec=256
ROOT=Path(__file__).resolve().parent
path=ROOT/'round2_radial_H4_exact_h1_16.json'
expected='c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627'
assert hashlib.sha256(path.read_bytes()).hexdigest()==expected
nodes,qjets=load_jets(path)
zjets=[]
for r,(q,qp,qpp,qppp) in zip(nodes,qjets):
 if r==0:
  z,zp,zpp,zppp=4*qpp,F(0),(q**3-q)/4,F(0)
 else:
  z=qpp+3*qp/r
  zp=qppp+3*qpp/r-3*qp/r**2
  zpp=q**3-q-3*zp/r
  zppp=(3*q*q-1)*qp-3*zpp/r+3*zp/r**2
 zjets.append([z,zp,zpp,zppp])
assert all(v==0 for v in zjets[-1]) and zjets[0][1]==zjets[0][3]==0

def A(q):return arb(q.numerator)/q.denominator

def integral(poly):return sum((v/(j+1) for j,v in enumerate(poly.coeffs())),arb(0))

e1=e2=arb(0);t0=time.time();worst=(arb(0),-1)
for i,(r,b) in enumerate(zip(nodes,nodes[1:])):
 h=b-r;rr=arb_poly([A(r),A(h)])
 q=arb_poly([A(x) for x in hermite(qjets[i],qjets[i+1],h)])
 z=arb_poly([A(x) for x in hermite(zjets[i],zjets[i+1],h)])
 qp=q.derivative()*(1/A(h));qpp=qp.derivative()*(1/A(h))
 zp=z.derivative()*(1/A(h));zpp=zp.derivative()*(1/A(h))
 n1=rr*qpp+3*qp-rr*z
 n2=rr*zpp+3*zp+rr*(q-q**3)
 b1=A(h)*integral(rr*n1*n1);b2=A(h)*integral(rr*n2*n2)
 e1+=b1;e2+=b2
 if b1+b2>worst[0]:worst=(b1+b2,i)
area=2*arb.pi()**2
r1=(area*e1).sqrt().upper();r2=(area*e2).sqrt().upper();res=(area*(e1+e2)).sqrt().upper()
out={'status':'whole-space mixed Hminus2 residual for the unchanged frozen q','profile_sha256':expected,'precision_bits':ctx.prec,'auxiliary_rule':'septic Hermite: z=Delta q and z_prime at nodes, z_second and third from stationary ODE; even origin jets','d1_L2_upper':str(r1),'d2_L2_upper':str(r2),'Fq_Zdual_upper':str(res),'worst_cell':worst[1],'seconds':time.time()-t0,'residual_lt_1e_6':bool(res<arb('1e-6')),'residual_lt_1e_7':bool(res<arb('1e-7')),'residual_lt_1e_8':bool(res<arb('1e-8'))}
(ROOT/'round5_n4_mixed_residual.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
