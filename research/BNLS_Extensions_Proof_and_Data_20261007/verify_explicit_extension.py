"""Exact arithmetic for the new explicit-velocity implication.

This verifies consequences of the separately certified round-2 profile,
spectral and response bounds. It does not replace those input certificates.
All assertions use fractions; decimal values are display-only.
"""
from fractions import Fraction as F
from pathlib import Path
import json

alpha, G, H = F(1,256), F(3,5), F(1,2)
qnorm, rho, psinorm = F(104), F(3,500), F(132)
dminus = alpha*(2*qnorm*rho+rho*rho)
dplus = 3*dminus
gaps = [F(1,20)-dplus, F(2,5)-dplus,
        F(1,10)-dplus, F(1,25)-dminus, F(1,10)-dminus]
response_residual = F(331,500000)+dminus*psinorm+G*rho
z_bound = psinorm + response_residual/(F(1,25)-dminus)

C, m, b, R = F(29), F(105), F(151), F(200)
vmax, kappa, D = F(1,10**6), F(1,1000), F(1500000)
remainder_coefficient = C*(kappa*H*m+G*R+kappa*H*R*vmax
                           +alpha*(3*m*R*R+R**3*vmax))
lipschitz = C*(G*vmax+H*kappa*vmax*vmax
                +alpha*(6*m*R*vmax+3*R*R*vmax*vmax))
momentum_error = 2*G*m*D+G*R*R
gradient_squared = H*(m+R*vmax)**2
energy_coefficient = kappa*gradient_squared/4 + (-350+momentum_error*vmax)/8

checks = {
    'profile_norm_below_m': qnorm+rho < m,
    'all_even_odd_inverse_bounds_below_C': all(gap>1/C for gap in gaps),
    'response_norm_below_b': z_bound < b,
    'remainder_coefficient_below_D': remainder_coefficient < D,
    'ball_maps_strictly_inside': b+D*vmax < R,
    'contraction_below_0015': lipschitz < F(15,1000),
    'gradient_squared_below_5513': gradient_squared < 5513,
    'momentum_error_coefficient_exact': momentum_error == 189024000,
    'energy_below_minus18_v_squared': energy_coefficient < -18,
    'sample_mu_is_on_wedge': kappa*vmax*vmax == F(1,10**15),
}
assert all(checks.values()), checks
values = {
    'vmax': vmax, 'kappa': kappa, 'full_inverse_bound': C,
    'z_bound': z_bound, 'remainder_coefficient': remainder_coefficient,
    'contraction': lipschitz, 'momentum_error_coefficient':momentum_error,
    'gradient_squared_bound':gradient_squared,
    'energy_coefficient_upper':energy_coefficient,
    'sample_v':vmax,'sample_mu':kappa*vmax*vmax,
}
result = {
    'status':'all exact implication checks passed; round-2 certificates remain premises',
    'checks':checks,
    'values':{name:{'exact':str(value),'display':float(value)}
              for name,value in values.items()},
}
out = Path(__file__).with_name('explicit_extension_results.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
