import json
import numpy as np
from scipy.integrate import simpson
from scipy.interpolate import CubicSpline
z=np.load('r24_shell.npz');r,f,df,g,dg=[z[k] for k in ['r','f','df','g','dg']]
I=2*np.pi*simpson(r*f*(f+r*df)*g*(g+r*dg),x=r)
sp=CubicSpline(r,f);a=2*np.pi*simpson(r*(df**2-.5*f**4),x=r)
def energy(s):
 return np.exp(2*s)*a-2*np.pi*simpson(r*np.exp(2*s)*sp(np.exp(s)*r)**2*g*g,x=r)
res=dict(I=float(I),quadratic_coefficient=float(2*I),finite_differences={str(t):float((energy(t)+energy(-t)-2*energy(0))/(2*t*t)) for t in [1e-2,3e-3,1e-3]})
print(json.dumps(res,indent=2))
open('r24_dilation_check.json','w').write(json.dumps(res,indent=2))
