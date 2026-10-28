"""Exact rational arithmetic for the analytic certificate implication.

This checks ONLY the implication from the declared norm, residual and spectral
premises. It does not independently certify the Birman--Schwinger upper bounds.
No floating-point operation is used in a mathematical comparison.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import json
from pathlib import Path

alpha=F(1,256)  # justified by ||h||_4 <= ||h||_Z / 4
G=F(3,5)       # ||partial_1 h||_(Z*) <= G ||h||_Z
m=F(104)
b=F(132)
eta_q=F(121,500000)
eta_psi=F(331,500000)
rho=F(3,500)
gamma_radial=F(1,20)
gamma_minus=F(1,25)
J_upper=F(-273)

radius=(eta_q+alpha*(3*m*rho*rho+rho**3))/gamma_radial
contraction=alpha*(6*m*rho+3*rho*rho)/gamma_radial
d_minus=alpha*(2*m*rho+rho*rho)
d_plus=3*d_minus
exact_minus_gap=gamma_minus-d_minus
J_shift=2*G*rho*b+d_minus*b*b
response_residual=eta_psi+d_minus*b+G*rho
quadratic=response_residual**2/exact_minus_gap
I_upper=J_upper+J_shift+quadratic

# The following spectral input bounds may be weakened to the displayed gaps.
radial_HS=F(39)
a1,a2=F(1079,200),F(2999,1000)
radial_remainder=radial_HS-a1*a1-a2*a2
plus2_HS=F(24,5)
plus2_a1=F(211,100)
plus2_gap=F(2,5)
minus1_trace=F(17,10)
minus1_a1=F(26,25)
high_gap=F(1,10)

checks={
 'Sobolev_constant_reduction_sufficient': F(6)<F(3)**2,
 'derivative_constant_reduction_sufficient': F(27,256)<G**4,
 'radial_two_Ritz_above_one_plus_gap': min(a1,a2)>=1+gamma_radial,
 'radial_remaining_BS_eigenvalues_below_one_minus_gap': radial_remainder<(1-gamma_radial)**2,
 'plus2_Ritz_above_one_plus_gap': plus2_a1>=1+plus2_gap,
 'plus2_remaining_BS_eigenvalues_below_one_minus_gap': plus2_HS-plus2_a1**2<(1-plus2_gap)**2,
 'minus1_Ritz_above_one_plus_gap': minus1_a1>=1+gamma_minus,
 'minus1_remaining_BS_eigenvalues_below_one_minus_gap': minus1_trace-minus1_a1<1-gamma_minus,
 'optional_plus4_HS_implies_high_gap': F(73,100)<(1-high_gap)**2,
 'optional_minus3_HS_implies_high_gap': F(11,50)<(1-high_gap)**2,
 'Newton_ball_invariant': radius<rho,
 'Newton_strict_contraction': contraction<1,
 'radial_gap_survives': gamma_radial>d_plus,
 'plus2_gap_survives': plus2_gap>d_plus,
 'all_high_plus_gaps_survive': high_gap>d_plus,
 'minus1_gap_survives': exact_minus_gap>0,
 'all_high_minus_gaps_survive': high_gap>d_minus,
 'negative_inverse_pairing': I_upper<0,
 'convenient_negative_pairing_margin': I_upper<F(-175),
}

values={
 'alpha':alpha,'G':G,'m':m,'b':b,'eta_q':eta_q,
 'eta_psi':eta_psi,'rho':rho,'gamma_radial':gamma_radial,
 'gamma_minus':gamma_minus,'radius_bound':radius,
 'contraction_bound':contraction,'d_minus':d_minus,'d_plus':d_plus,
 'exact_minus_gap_lower':exact_minus_gap,'J_shift_upper':J_shift,
 'response_residual_upper':response_residual,
 'quadratic_residual_upper':quadratic,'I_upper':I_upper,
 'radial_HS_remainder_upper':radial_remainder,
}

def record(x):
    with localcontext() as ctx:
        ctx.prec=35
        decimal=str(Decimal(x.numerator)/Decimal(x.denominator))
    return {'exact_fraction':str(x),'decimal_display_only':decimal}

out={
 'status':'conditional analytic implication; spectral and scalar premises must be independently certified',
 'comparison_arithmetic':'exact rational',
 'checks':checks,'all_checks_pass':all(checks.values()),
 'values':{k:record(v) for k,v in values.items()},
}
Path('round2_final_rational_implication.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
assert all(checks.values())
