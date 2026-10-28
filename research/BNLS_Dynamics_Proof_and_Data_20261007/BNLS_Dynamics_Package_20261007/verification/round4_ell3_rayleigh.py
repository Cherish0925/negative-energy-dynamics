#!/usr/bin/env python3
"""Exact ell=3 Ritz lower bound using the frozen ell=2 reduced radial trial.
No numerical solve: the trial f is re-used in the new harmonic r^3 f(r)Y_3.
All decisions are rational, with canonical input hashes checked.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time,sys
from round2_verify_frozen_ritz import load_jets,hermite,power,integral01,add,mul,scale,deriv
ROOT=Path(__file__).resolve().parent
st=time.monotonic()
qpath=ROOT/'round2_radial_H4_exact_h1_16.json';rpath=ROOT/'round2_ritz_exact_data.json'
assert hashlib.sha256(qpath.read_bytes()).hexdigest()=='c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627'
nodes,qjets=load_jets(qpath)
data=json.loads(rpath.read_text());assert nodes==[F(*x) for x in data['nodes']]
jets=[[F(x) for x in row] for row in data['channels']['2']['trial_jets']]
assert len(nodes)==len(jets) and jets[0][1]==jets[0][3]==0 and all(x==0 for x in jets[-1])
M=K=V=F(0);dim=10
for j,(a,b) in enumerate(zip(nodes,nodes[1:])):
 h=b-a;r=[a,h];q=hermite(qjets[j],qjets[j+1],h);f=hermite(jets[j],jets[j+1],h)
 Dnum=add(mul(r,scale(deriv(f,2),h**-2)),scale(deriv(f),F(dim-1)/h))
 f2=mul(f,f);rw=power(r,dim-1)
 M+=h*integral01(mul(rw,f2))
 K+=h*integral01(mul(power(r,dim-3),mul(Dnum,Dnum)))
 V+=3*h*integral01(mul(rw,mul(mul(q,q),f2)))
A=M+K
out={'verified':True,'trial_description':'r^3 f(r)Y_3 with f the frozen ell2 reduced trial','profile_sha256':hashlib.sha256(qpath.read_bytes()).hexdigest(),'ritz_sha256':hashlib.sha256(rpath.read_bytes()).hexdigest(),'A':str(A),'V':str(V),'M':str(M),'quotient_exact':str(V/A),'quotient_float_diagnostic':float(V/A),'checks':{'positive_denominator':A>0,'lambda1_gt_1.25':V>F(5,4)*A,'lambda1_gt_1.30':V>F(13,10)*A},'seconds':time.monotonic()-st}
assert all(out['checks'].values())
(ROOT/'round4_ell3_rayleigh_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['A','V','M','quotient_exact']},indent=2))
