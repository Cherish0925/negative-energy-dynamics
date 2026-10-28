#!/usr/bin/env python3
"""Exact scalar Newton and spectral-transfer consequences of the new residual."""
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
import json,hashlib
ctx.prec=256
ROOT=Path(__file__).resolve().parent
res=json.loads((ROOT/'round5_n4_mixed_residual.json').read_text())
hs=json.loads((ROOT/'round4_morse_work/round2_certified_birman_l0_sub16.json').read_text())
profile=hashlib.sha256((ROOT/'round2_radial_H4_exact_h1_16.json').read_bytes()).hexdigest()
assert res['profile_sha256']==hs['profile_sha256']==profile
assert arb(hs['HS_squared_upper_endpoint_enclosure'])<arb('38.8')
rho=F(3,10**7);eps=F(4601,10**11);inv=F(25,4);C=F(1,256);q=F(104)
checks={
 'new_energy_dual_residual_lt_4_601e_8':bool(arb(res['Fq_Zdual_upper'])<arb(eps.numerator)/eps.denominator),
 'radial_BS_third_lt_0_84':F(194,5)-F(1079,200)**2-F(2999,1000)**2<F(21,25)**2,
 'radial_inverse_lt_25_over_4':1-F(21,25)==1/inv,
 'newton_ball_maps_strictly_inside':inv*(eps+C*(3*q+rho)*rho*rho)<rho,
 'newton_lipschitz_lt_1e_5':inv*C*(6*q*rho+3*rho*rho)<F(1,10**5),
 'uniqueness_through_old_ball':inv*C*(6*q*F(3,500)+3*F(3,500)**2)<1,
}
assert all(checks.values())
delta=C*(2*q*rho+rho*rho)
out={'verified':True,'profile_sha256':profile,'dependencies':'frozen radial Ritz lower bounds5.395,2.999; Arb HS^2<38.8; newly enclosed mixed H^-2 residual','exact_same_Q_as_prior_certificate':True,'Z_distance_upper':str(rho),'radial_inverse_upper':str(inv),'coefficient_one_potential_transfer_upper':str(delta),'coefficient_one_potential_transfer_diagnostic':float(delta),'newton_image_upper':str(inv*(eps+C*(3*q+rho)*rho*rho)),'newton_lipschitz_upper':str(inv*C*(6*q*rho+3*rho*rho)),'checks':checks}
(ROOT/'round5_n4_refinement_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
