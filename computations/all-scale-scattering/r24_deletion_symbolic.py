"""Verify the differential identity; analytical proof is in r24_global_route.md."""
import sympy as s
import json
r,g,e,rho,S,G,w,a=s.symbols('r g e rho S G w a',nonzero=True)
gp=e-rho-g*g-a*g/r
Gp=-a*w*w*(2*g*g+S)/r
W=a/r**2+2*a*g/r+2*G/w**2
Wp=s.diff(W,r)+s.diff(W,g)*gp+s.diff(W,G)*Gp+s.diff(W,w)*g*w
res=s.expand(Wp+(2*g+a/r)*W+a*(rho+S)/r-a*(a-2)/r**3)
res=s.simplify(res.subs(G,w*w*(g*g-e+rho/2+S/2)))
result={'general_dimension_weighted_derivative_residual':str(res)}
print(result)
json.dump(result,open('research/r24_deletion_symbolic.json','w'),indent=2)
