"""Targeted, non-certified projected-resolvent calibration of the R24 shell.

The five-dimensional trace-free real potential family splits into sectors
l=0,1,2 of multiplicities 1,2,2. This computes all sectors and includes the
unoccupied continuum by a large-radius Dirichlet resolvent, followed by mesh
and radius convergence checks. It is not an interval-arithmetic certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from pathlib import Path
import json
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import simpson
from scipy.sparse import diags, bmat, csc_matrix
from scipy.sparse.linalg import splu
from scipy.linalg import eigh

ROOT = Path(__file__).resolve().parent
z = np.load(ROOT / 'r24/r24_shell.npz')
fs = CubicSpline(z['r'], z['f'])
gs = CubicSpline(z['r'], z['g'])
energy = float(z['e'])
beta_f = 2*np.pi*simpson(z['r']*z['f']**2, x=z['r'])
beta_g = np.pi*simpson(z['r']*z['g']**2, x=z['r'])

def calculate(radius, target_h):
    n = round(radius/target_h)
    h = radius/n
    r = (np.arange(n)+0.5)*h
    f, g = fs(r), gs(r)
    sr = np.sqrt(r)
    rho = f*f+g*g
    # Conservative radial finite volumes, conjugated by sqrt(r). The inner
    # boundary has zero flux; outer ghost value is zero. The effective outer
    # Dirichlet radius is R+h/2, whose shift is negligible after decay.
    diagonal = np.full(n, 2.0/h**2)
    off = -(np.arange(n-1)+1)/(h**2*np.sqrt((np.arange(n-1)+.5)*(np.arange(n-1)+1.5)))
    cache = {}
    def resolvent(m, e, source):
        key = (m, e)
        if key not in cache:
            A = diags([off, diagonal+m*m/(r*r)-rho+e, off], [-1,0,1], format='csc')
            u = (sr*f if m == 0 else sr*g if m == 1 else None)
            if u is not None:
                u = u / np.linalg.norm(u)
                ucol = csc_matrix(u[:,None])
                AA = bmat([[A, ucol],[ucol.T,csc_matrix((1,1))]], format='csc')
            else:
                AA = A
            cache[key] = (splu(AA), u)
        lu, u = cache[key]
        s = sr*source
        rhs = np.r_[s,0.] if u is not None else s
        sol = lu.solve(rhs)
        y = sol[:n]
        return dict(value=float(h*np.dot(s,y)),
                    projection_error=float(abs(np.dot(u,y))) if u is not None else 0.)
    sectors=[]
    specifications=[('tracefree_l0',0,g*g-2*f*f),
                    ('tracefree_l1',1,f*g),('tracefree_l2',2,g*g),
                    ('common_scale_control',0,2*rho+2*r*(f*fs(r,1)+g*gs(r,1))),
                    ('relative_core_scale_control',0,f*(f+r*fs(r,1)))]
    for name,ell,w in specifications:
        J=float(h*np.dot(r,w*w))
        ff=resolvent(ell,1.,w*f)
        if ell==0:
            gg=[resolvent(1,energy,w*g)]
            total=ff['value']+gg[0]['value']
        else:
            gg=[resolvent(ell-1,energy,w*g),resolvent(ell+1,energy,w*g)]
            total=ff['value']+.5*sum(t['value'] for t in gg)
        sectors.append(dict(name=name,ell=ell,multiplicity=1 if ell==0 else 2,
                            ratio=2*total/J,source_norm_radial=J,
                            f_response=ff,g_responses=gg))
    # Check whether simply removing Tr(A)=0 repairs the missed instability.
    # The additional trace direction only enlarges the radial block to
    # span{f^2,g^2}; angular sectors are unchanged.
    def radial_response(w):
        return (resolvent(0,1.,w*f)['value']
                +resolvent(1,energy,w*g)['value'])
    def radial_pair(basis):
        values=[radial_response(w) for w in basis]
        mixed=.5*(radial_response(basis.sum(0))-sum(values))
        response=2*np.array([[values[0],mixed],[mixed,values[1]]])
        norm=h*(basis*r)@basis.T
        eigenvalues,eigenvectors=eigh(response,norm)
        return eigenvalues,eigenvectors,response,norm
    radial_eigenvalues,_,response_matrix,norm_matrix=radial_pair(np.array([f*f,g*g]))
    df=f+r*fs(r,1)
    dg=g+r*gs(r,1)
    derivative_basis=np.array([f*df,g*dg])
    derivative_values,derivative_vectors,derivative_response,derivative_norm=radial_pair(derivative_basis)
    # The restricted orbital response only allows independent dilation of
    # the core and shell orbitals. Project those dilation vectors against
    # the occupied states in the same discrete inner product as the full
    # resolvent, then evaluate their exact discrete quadratic cost.
    restricted_cost=[]
    restricted_coupling=[]
    for m,e,u,du in [(0,1.,f,df),(1,energy,g,dg)]:
        v=sr*du
        occ=sr*u
        v=v-occ*np.dot(occ,v)/np.dot(occ,occ)
        a=diagonal+m*m/(r*r)-rho+e
        cost=h*(np.dot(a*v,v)+2*np.dot(off*v[:-1],v[1:]))
        restricted_cost.append(cost)
        restricted_coupling.append(h*(derivative_basis*(sr*u))@v)
    B=np.array(restricted_coupling).T
    restricted_response=2*B@np.diag(1/np.array(restricted_cost))@B.T
    restricted_values=eigh(restricted_response,derivative_norm,eigvals_only=True)
    return dict(radius=radius,h=h,n=n,sectors=sectors,
                full_quadratic_radial_eigenvalues=radial_eigenvalues.tolist(),
                full_quadratic_response_matrix=response_matrix.tolist(),
                full_quadratic_norm_matrix=norm_matrix.tolist(),
                derivative_response_eigenvalues=derivative_values.tolist(),
                derivative_response_eigenvectors=derivative_vectors.tolist(),
                derivative_response_matrix=derivative_response.tolist(),
                derivative_norm_matrix=derivative_norm.tolist(),
                restricted_dilation_cost=restricted_cost,
                restricted_dilation_response_matrix=restricted_response.tolist(),
                restricted_dilation_response_eigenvalues=restricted_values.tolist())

if __name__=='__main__':
    results=[]
    for R,h in [(45.,.04),(45.,.02),(45.,.01),(45.,.005),(65.,.01),(65.,.005),(65.,.0025)]:
        result=calculate(R,h)
        results.append(result)
        print(R,h,[t['ratio'] for t in result['sectors']],flush=True)
    result=dict(source='r24/r24_shell.npz',energy=energy,
                beta_f=beta_f,beta_g=beta_g,
                interpretation='Numerical calibration only; no rigorous error certificate.',
                results=results)
    (ROOT/'r31_response_calibration.json').write_text(json.dumps(result,indent=2)+'\n')
