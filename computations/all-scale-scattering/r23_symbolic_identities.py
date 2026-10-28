"""Exact algebra checks for R23. The analytic arguments are in the notes."""
import json
from pathlib import Path
import sympy as s

r, a, omega = s.symbols('r a omega', positive=True)
p, z, vz = s.symbols('p z vz', real=True)
# z=V(Q), vz=Q V'(Q), so z'=p*vz.
U = a/r**2 + 2*a*p/r + 2*p**2 + z - 2*omega
deriv = s.diff(U,r) + s.diff(U,p)*(omega-z-p**2-a*p/r) + s.diff(U,z)*p*vz
weighted = deriv + (a/r+2*p)*U
target = a*(a-2)/r**3-a*z/r+p*(vz-2*z)
general_residual = s.factor(weighted-target)

u,v,du,dv,e,f = s.symbols('u v du dv e f', real=True)
rho=u*u+v*v
W=u*dv-du*v
G=du*du-e*u*u+s.Rational(1,2)*u*u*rho+W*W/(2*(e-f))
def d_rad(expr):
    return (s.diff(expr,r)+s.diff(expr,u)*du+s.diff(expr,v)*dv
            +s.diff(expr,du)*(e*u-rho*u-du/r)
            +s.diff(expr,dv)*(f*v-rho*v-dv/r))
wronskian_residual=s.factor(d_rad(W)-((f-e)*u*v-W/r))
component_residual=s.factor(d_rad(r*r*G)-r*u*u*(rho-2*e))
result={"general_partner_residual":str(general_residual),
        "radial_wronskian_residual":str(wronskian_residual),
        "component_virial_residual":str(component_residual),
        "scope":"Exact algebra only; operator domains, boundary terms and spectral implications are proved in the notes."}
assert general_residual==0 and wronskian_residual==0 and component_residual==0
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
