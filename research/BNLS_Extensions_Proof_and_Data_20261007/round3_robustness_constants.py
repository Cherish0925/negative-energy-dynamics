"""Exact rational checks for the cubic mixed/anisotropic extension.

Uses only the already certified base constants C<=29, ||Q||_Z<105,
||L_-^{-1} partial_e Q||_Z<151 and I<-175. No profile is regenerated.
The perturbation budget is 2*delta_a+||B|| <= |v|^2/1000.
"""
from fractions import Fraction as F
import json

s=F(1,10**6)
C,m,Z,G,alpha=F(29),F(105),F(151),F(3,5),F(1,256)
r=200*s
d=s*s/2000
W=C*(d*m+(d+G*s)*r+alpha*(3*m*r*r+r**3))
ball=(Z*s+W)/r
lip=C*(d+G*s+alpha*(6*m*r+3*r*r))
energy=(m+r)**2/F(8000)-F(175,4)+(G*m/4)*(W/s)+(G/8)*(r*r/s)

gamma=F(2247991,64000000)
response_residual=F(10364489,16000000)
checks={
    'base_inverse_below_29':1/gamma<29,
    'base_response_below_151':132+response_residual/gamma<151,
    'fixed_point_ball_invariant':ball<1,
    'fixed_point_contraction':lip<1,
    'energy_coefficient_below_minus_18':energy < -18,
}
assert all(checks.values())
def exact(x):return {'fraction':str(x),'decimal_for_orientation':float(x)}
out={'all_pass':all(checks.values()),'checks':checks,
     'speed_upper_bound':str(s),
     'static_operator_budget':'delta_a + ||B||/2 <= |v|^2/2000',
     'W_over_s_squared':exact(W/s**2),
     'ball_fraction':exact(ball),'contraction_constant':exact(lip),
     'energy_over_s_squared_upper_bound':exact(energy),
     'note':'Exact Fraction comparisons prove the claims; decimal fields are explanatory only.'}
print(json.dumps(out,indent=2))
with open('round3_robustness_constants.json','w') as f:json.dump(out,f,indent=2)
