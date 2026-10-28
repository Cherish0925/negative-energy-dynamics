#!/usr/bin/env python3
"""Verify all scalar implications used in the full N4 Morse/kernel theorem.

The exact stationary profile Q and ||Q-q||_Z<=.006 are supplied by the frozen
base existence certificate. This script does not assume that numerical
elliptic eigenvalues equal exact eigenvalues. It checks the Rayleigh/HS bounds,
form perturbation bounds, and arithmetic spectral separations in the proof.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'rigorous_deps'))
from flint import arb,ctx
ctx.prec=192
PROFILE_HASH='c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627'
assert hashlib.sha256((ROOT/'round2_radial_H4_exact_h1_16.json').read_bytes()).hexdigest()==PROFILE_HASH
ritz=json.loads((ROOT/'round4_ell3_rayleigh_results.json').read_text())
assert ritz['profile_sha256']==PROFILE_HASH
assert ritz['ritz_sha256']==hashlib.sha256((ROOT/'round2_ritz_exact_data.json').read_bytes()).hexdigest()
assert F(ritz['V'])>F(13,10)*F(ritz['A'])>0
checks={'ell3_exact_Rayleigh_gt_13_over_10':True}
thresholds={0:F(194,5),1:F(31,25),2:F(24,5),3:F(11,50),4:F(73,100)}
for ell,threshold in thresholds.items():
 row=json.loads((ROOT/'round4_morse_work'/f'round2_certified_birman_l{ell}_sub16.json').read_text())
 assert row['profile_sha256']==PROFILE_HASH
 hs=arb(row['HS_squared_upper_endpoint_enclosure'])
 checks[f'ell{ell}_HS_squared_bound']=bool(hs<arb(threshold.numerator)/threshold.denominator)
delta=F(312009,64000000);delta3=3*delta;gap=F(1,29)
s0=F(1,10**6)
traveling_perturbation=3*F(1,256)*(210+200*s0)*200*s0+F(3,5)*s0
checks.update({
 'traveling_Hessian_perturbation_lt_0.000493':traveling_perturbation<F(493,10**6),
 'traveling_nonzero_gap_gt_1_over_30':gap-traveling_perturbation>F(1,30),
 'traveling_zero_cluster_separated':traveling_perturbation<gap/3,
 'base_form_transfer_equal_product_estimate':delta==F(1,256)*(2*104*F(3,500)+F(3,500)**2),
 'radial_plus_remainder_lt_0.95_squared':F(39)-F(1079,200)**2-F(2999,1000)**2<F(19,20)**2,
 'radial_plus_gap_gt_1_over_29':F(1,20)-delta3>gap,
 'radial_minus_top_gt_1':(F(1079,200)-delta3)/3>1+gap,
 'radial_minus_third_lt_1':(F(19,20)+delta3)/3<1-gap,
 'ell1_minus_gap_gt_1_over_29':F(1,25)-delta>gap,
 'ell1_minus_second_lt_1':F(17,10)-F(26,25)+delta<1-gap,
 'ell1_plus_third_q_lt_0.23':F(31,25)-F(26,25)**2-(F(1,3)-delta)**2<F(23,100)**2,
 'ell1_plus_third_Q_lt_1_over_3':3*(F(23,100)+delta)<1-gap,
 'ell1_plus_top_gt_1':3*(F(26,25)-delta)>1+gap,
 'ell2_plus_remainder_lt_0.6_squared':F(24,5)-F(211,100)**2<F(3,5)**2,
 'ell2_plus_gap_gt_1_over_29':F(2,5)-delta3>gap,
 'ell2_minus_norm_lt_0.75':F(24,5)<(3*(F(3,4)-delta))**2,
 'ell3_plus_remainder_lt_0.54_squared':9*F(11,50)-F(13,10)**2<F(27,50)**2,
 'ell3_plus_top_gt_1':F(13,10)-delta3>1+gap,
 'ell3_plus_remainder_lt_1':F(27,50)+delta3<1-gap,
 'ell4_plus_HS_lt_0.9_squared':F(73,100)<F(9,10)**2,
 'ell4_plus_gap_gt_1_over_29':F(1,10)-delta3>gap,
})
assert all(checks.values())
counts={'L_plus_negative':2+4+9+16,'L_minus_negative':1+4,'L_plus_kernel':4,'L_minus_kernel':1}
assert counts=={'L_plus_negative':31,'L_minus_negative':5,'L_plus_kernel':4,'L_minus_kernel':1}
out={'verified':True,'scope':'Full-space Morse/kernel scalar separation, conditional only on the frozen stationary existence certificate and established Birman-Schwinger/form identities.','profile_sha256':PROFILE_HASH,'delta_minus_exact':str(delta),'delta_plus_exact':str(delta3),'nonzero_preconditioned_spectral_gap_lower':'1/29','counts':counts,'traveling_speed_radius':'1/1000000','traveling_Hessian_perturbation_exact':str(traveling_perturbation),'traveling_nonzero_preconditioned_gap_lower':'1/30','checks':checks,'ell3_trial_Rayleigh_float_diagnostic':ritz['quotient_float_diagnostic'],'exact_channel_table':[{'ell':0,'multiplicity':1,'plus_negative_per_channel':2,'plus_kernel_per_channel':0,'minus_negative_per_channel':1,'minus_kernel_per_channel':1},{'ell':1,'multiplicity':4,'plus_negative_per_channel':1,'plus_kernel_per_channel':1,'minus_negative_per_channel':1,'minus_kernel_per_channel':0},{'ell':2,'multiplicity':9,'plus_negative_per_channel':1,'plus_kernel_per_channel':0,'minus_negative_per_channel':0,'minus_kernel_per_channel':0},{'ell':3,'multiplicity':16,'plus_negative_per_channel':1,'plus_kernel_per_channel':0,'minus_negative_per_channel':0,'minus_kernel_per_channel':0},{'ell':'all >=4','multiplicity':'(ell+1)^2','plus_negative_per_channel':0,'plus_kernel_per_channel':0,'minus_negative_per_channel':0,'minus_kernel_per_channel':0}]}
(ROOT/'round4_morse_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
