#!/usr/bin/env python3
"""Exact-Q transfer and final finite-block Rouché inequalities (Arb).
Depends on the proved positive-complement finite-block theorem and frozen N4
existence/Morse certificates. Does not infer existence from a small residual.
"""
from pathlib import Path
import json,hashlib
from fractions import Fraction as F
from flint import arb,ctx
from round2_verify_frozen_ritz import parse_hex_rational
ctx.prec=256
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'round5_radial_block_certificate_h2.json').read_text());cont=json.loads((ROOT/'round5_radial_contour.json').read_text())[0]
assert raw['profile_sha256']==hashlib.sha256((ROOT/'round5_radial_block_exact_h2.json').read_bytes()).hexdigest()
assert raw['whitening_sha256']==hashlib.sha256((ROOT/'round5_radial_block_whitening.json').read_bytes()).hexdigest()
assert cont['block_certificate_sha256']==hashlib.sha256((ROOT/'round5_radial_block_certificate_h2.json').read_bytes()).hexdigest()
refine=json.loads((ROOT/'round5_n4_refinement_certificate.json').read_text())
assert refine['verified'] and refine['exact_same_Q_as_prior_certificate'] and all(refine['checks'].values())
assert F(refine['Z_distance_upper'])<=F(3,10**7)
assert refine['profile_sha256']==hashlib.sha256((ROOT/'round2_radial_H4_exact_h1_16.json').read_bytes()).hexdigest()
C=[[arb(parse_hex_rational(v).numerator)/parse_hex_rational(v).denominator for v in row] for row in json.loads((ROOT/'round5_radial_block_whitening.json').read_text())]
rho=arb('0.0000003');qmax=arb('6.73');qZ=arb(104);eta=arb('0.000242');X=arb('0.0003');embedding=arb('0.088');sinf=arb('0.00000084')
# ||w||infty <= (24 sqrt3 pi)^-1/2 sqrt(||w||Z ||Aw||2).
emb_exact=1/(24*arb(3).sqrt()*arb.pi()).sqrt()
assert emb_exact<embedding
bootstrap_rhs=3*qmax*qmax*rho+3*qmax*embedding*rho**arb('1.5')*X.sqrt()+embedding**2*rho*rho*X+eta
assert bootstrap_rhs<X
assert embedding*(rho*X).sqrt()<sinf
area=2*arb.pi()**2;er=rho/area.sqrt()
sups=[[[arb(v) for v in row] for row in col] for col in raw['sup_U_Uprime_DeltaU_2qU_derivs']]
deltaR2=arb(0);deltaL2=arb(0)
for col in sups:
 for aa,(u0,u1,ul,g0,g1,gl) in enumerate(col):
  coefficient=3 if aa==0 else 1
  lin=er*(g0*g0+(g0+arb(2).sqrt()*g1+gl)**2).sqrt()
  quad0=sinf*u0*er
  # ||grad w||_4^2 <= rho X /16 follows from the frozen Z->L4 estimate.
  quadlap=sinf*er*(ul+2*arb(2).sqrt()*u1+2*u0)+2*u0*rho*X/(16*area.sqrt())
  bound=lin+(quad0**2+quadlap**2).sqrt()
  deltaR2+=(coefficient*bound)**2
  deltaL2+=(coefficient*(er*g0+quad0))**2
deltaR=deltaR2.sqrt();deltaL=deltaL2.sqrt()
phase=er*sum((v*v for v in C[4]),arb(0)).sqrt()
epsilon=arb(raw['residual_frobenius_Z_upper'])+deltaR+phase
# Exact G does not depend on the phase projection, because H_Q Q=0.
rawtrace=arb(raw['raw_W_Z_frobenius_squared']);deltaBS=(2*qZ*rho+rho*rho)/256
deltaG=3*deltaBS*rawtrace
gq=arb(raw['G_inverse_frobenius_upper']);assert gq*deltaG<1
g=gq/(1-gq*deltaG)
# Transfer P_q to P_Q in the Z Hilbert norm.
qrad=arb(raw['q_Z_radial_squared']).sqrt();zdev=arb(raw['quotient_Z_minus_identity_frobenius_upper'])
w=(1+zdev).sqrt()+4*er/(qrad-er)*rawtrace.sqrt()
Lq=arb(raw['L_W_L2_frobenius_upper']);deltaK=(2*Lq+deltaL)*deltaL
BC=[[arb(x) for x in row] for row in raw['BC']];normBC=sum((v*v for row in BC for v in row),arb(0)).sqrt()
deltaB=arb(raw['compressed_B_minus_B0_frobenius_upper'])+g*(deltaK+deltaG*normBC)
M=arb(6);projection=1+w*w*g*M
alpha=arb(cont['box'][0]);k=arb(cont['k_Frobenius_upper'])
rouche=k*(deltaB+g*M*projection**2*epsilon**2/alpha)
checks={'bootstrap_Aw_lt_0.0003':bool(bootstrap_rhs<X),'Q_minus_q_Linfty_lt_8.4e-7':bool(embedding*(rho*X).sqrt()<sinf),'trial_Gram_has_exactly_three_negative_directions':raw['negative_pivots']==3,'Gram_transfer_nonsingular':bool(gq*deltaG<1),'exact_G_inverse_lt_6':bool(g<6),'exact_projected_basis_norm_lt_1.001':bool(w<arb('1.001')),'exact_block_residual_lt_0.0031':bool(epsilon<arb('0.0031')),'finite_block_reference_inverse_lt_1.34':bool(k<arb('1.34')),'Rouche_strictly_lt_one':bool(rouche<1)}
assert all(checks.values())
# These exact reference eigenvalue parameters lie strictly inside the contour.
al,be=[arb(parse_hex_rational(v).numerator)/parse_hex_rational(v).denominator for v in raw['lambda_hex']]
assert arb(cont['box'][0])<al<arb(cont['box'][1]) and arb(cont['box'][2])<be<arb(cont['box'][3])
values={'rho_Z_global':rho,'Aw_L2_bound':X,'w_Linfty_bound':sinf,'Q_transfer_H2_residual':deltaR,'phase_quotient_residual':phase,'exact_residual_epsilon':epsilon,'G_perturbation':deltaG,'exact_G_inverse':g,'exact_basis_norm':w,'L2_potential_transfer':deltaL,'K_perturbation':deltaK,'B_perturbation_from_explicit_reference':deltaB,'L_orthogonal_complement_projection_bound':projection,'contour_inverse':k,'Rouche_bound':rouche}
out={'status':'PASS: one algebraically simple exact-Q radial eigenvalue in the first-quadrant rectangle, conditional only on the stated previously proved base/Morse and finite-block theorems','rectangle':cont['box'],'precision_bits':ctx.prec,'checks':checks,'bounds':{key:str(v.upper()) for key,v in values.items()},'conclusion':'The Hamiltonian symmetry produces one simple complex quartet, providing two radial real unstable dimensions. Together with the 29 nonradial unstable dimensions and the index bound, the sufficiently small nonzero-speed branch has exactly 31 unstable dimensions.','dependencies':['round5_radial_analytic.md Section 7','round4_morse_certificate.md','round5_n4_refinement_certificate.json','round5_radial_block_certificate_h2.json','round5_radial_contour.json']}
(ROOT/'round5_radial_quartet_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
