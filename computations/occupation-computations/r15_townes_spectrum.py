from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp, simpson
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

r=np.linspace(1e-6,40,2400)
def fun(r,y): return np.array([y[1], y[0]-y[0]**3-y[1]/r])
def bc(a,b): return np.array([a[1],b[0]])
guess=np.array([2.2/np.cosh(r),-2.2*np.sinh(r)/np.cosh(r)**2])
sol=solve_bvp(fun,bc,r,guess,tol=2e-10,max_nodes=40000)
print('status',sol.status,sol.message,'Q0',sol.sol(0)[0], 'nodes',sol.x.size)
rs=np.linspace(1e-6,40,20001); q,dq=sol.sol(rs)
mc=2*np.pi*simpson(rs*q*q,x=rs)
A=2*np.pi*simpson(rs*dq*dq,x=rs)
F=2*np.pi*simpson(rs*q**4,x=rs)
var=2*np.pi*simpson(rs**3*q*q,x=rs)/mc
print('M A F variance',mc,A,F,var)
for ell in range(4):
    eps=1e-6
    def zero(r,y):
        # y(r)=r^ell*z(r), z''+(2ell+1)/r*z'+Q² z=0
        return [y[1],-(2*ell+1)*y[1]/r-float(sol.sol(r)[0])**2*y[0]]
    s=solve_ivp(zero,(eps,35),(1.,0.),rtol=2e-11,atol=1e-12,dense_output=True,max_step=.01)
    zz=s.sol(rs[rs<35])[0]
    nodes=np.sum(zz[:-1]*zz[1:]<0)
    z,zp=s.y[:,-1]; R=s.t[-1]
    if ell==0:
        b=R*zp; a=z-b*np.log(R)
    else:
        a=z+R*zp/(2*ell); b=-zp*R**(2*ell+1)/(2*ell)
    print('l',ell,'nodes',nodes,'a',a,'b',b)
for h in [.025,.0125]:
    R=30.; n=int(R/h); rr=(np.arange(n)+.5)*h
    faces=np.arange(1,n)*h
    off=-faces/h
    diag=np.r_[faces, R]/h+np.r_[0,faces]/h
    # Boundary value zero at R (half-cell distance).
    diag[-1]+=R/h
    W=rr*h
    for ell in [0,1,2]:
        d=diag+W*(ell**2/rr**2-sol.sol(rr)[0]**2)
        mat=diags([off/np.sqrt(W[:-1]*W[1:]),d/W,off/np.sqrt(W[:-1]*W[1:])],[-1,0,1])
        ev=eigsh(mat,k=4,sigma=-1.1,which='LM',return_eigenvectors=False,tol=1e-10)
        print('h l eig',h,ell,np.sort(ev))

np.savez(str(Path(__file__).with_name('r15_townes_profile.npz')),r=rs,q=q,dq=dq,mc=mc)
