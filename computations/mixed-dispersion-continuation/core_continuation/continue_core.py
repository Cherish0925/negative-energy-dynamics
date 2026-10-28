"""Axisymmetric real-state continuation from 3D BNLS to mixed optical dispersion.

Exploratory finite-volume calculation, not an interval certificate.
Q is even in tau and radial in the two transverse coordinates.
a_s=(1-s)(xi^2+eta^2)^2+s(xi^2+eta^4), alpha_s=(8-2s)/3.
The path is auxiliary and is not mass-critical at intermediate s.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse, json, time
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.interpolate import CubicHermiteSpline, RegularGridInterpolator

def operators(n,L):
    h=L/n; r=(np.arange(n)+.5)*h; t=r.copy()
    dd=np.full(n,-2/h**2);dd[0]=-1/h**2;dd[-1]=-3/h**2
    dt=sparse.diags([np.full(n-1,1/h**2),dd,np.full(n-1,1/h**2)],[-1,0,1],format='csr')
    rp=r+h/2;rm=r-h/2
    drdiag=-(rp+rm)/(r*h*h);drdiag[-1]-=rp[-1]/(r[-1]*h*h)
    off=rp[:-1]/(h*h*np.sqrt(r[:-1]*r[1:]))
    dr=sparse.diags([off,drdiag,off],[-1,0,1],format='csr')
    eye=sparse.eye(n,format='csr'); it=sparse.kron(dt,eye,format='csr')
    ir=sparse.kron(eye,dr,format='csr'); ir1=sparse.kron(eye,dr-sparse.diags(1/r**2),format='csr')
    ident=sparse.eye(n*n,format='csr')
    def path(rad):
        iso=(it+rad)@(it+rad)+ident
        mixed=-it+rad@rad+ident
        return iso.tocsc(),(mixed-iso).tocsc()
    return t,r,h,path(ir),path(ir1),it,ir

def solve(w, A, alpha, n, r, tol=1e-10, maximum=24):
    wr=np.tile(np.sqrt(r),n)
    def f(z): return A@z-np.abs(z/wr)**alpha*z
    z=w.copy(); fz=f(z); den=max(np.linalg.norm(z),1)
    for k in range(maximum):
        err=np.linalg.norm(fz)/den
        if err<tol:return z,err,k,True
        pot=(alpha+1)*np.abs(z/wr)**alpha
        dz=spsolve(A-sparse.diags(pot,format='csc'),-fz)
        lam=1.
        while lam>1/1024:
            trial=z+lam*dz; ft=f(trial)
            if np.linalg.norm(ft)<np.linalg.norm(fz)*(1-1e-4*lam):break
            lam/=2
        if lam<=1/1024:return z,err,k,False
        z=trial;fz=ft
    return z,float(np.linalg.norm(fz)/den),maximum,False

def measures(w,s,n,r,h,A,Lm):
    alpha=(8-2*s)/3; q=w.reshape(n,n)/np.sqrt(r)[None,:]
    # Even extension at axis and fourth-order centered radial derivative.
    ext=np.pad(q,((0,0),(2,2)),mode='symmetric')
    qr=(ext[:,0:-4]-8*ext[:,1:-3]+8*ext[:,3:-1]-ext[:,4:])/(12*h)
    src=(qr*np.sqrt(r)[None,:]).ravel()
    lm=Lm-sparse.diags(np.abs(q.ravel())**alpha,format='csc')
    chi=spsolve(lm,src)
    fac=4*np.pi*h*h
    mass=fac*np.dot(w,w); kinetic=fac*np.dot(w,(A@w-w))
    nonlin=fac*np.dot(w,w*np.abs(q.ravel())**alpha)
    energy=.5*kinetic-nonlin/(alpha+2)
    inertia=2*np.pi*h*h*np.dot(src,chi)
    err=np.linalg.norm(lm@chi-src)/np.linalg.norm(src)
    edge=fac*(np.sum(w.reshape(n,n)[-5:,:]**2)+np.sum(w.reshape(n,n)[:,-5:]**2))/mass
    return dict(s=float(s),alpha=alpha,mass=float(mass),energy=float(energy),response_I=float(inertia),response_residual=float(err),edge_mass=float(edge),peak=float(np.max(abs(q))))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=128);ap.add_argument('--L',type=float,default=24);ap.add_argument('--ds',type=float,default=.025);ap.add_argument('--end',type=float,default=1);ap.add_argument('--start',type=float,default=0);ap.add_argument('--seed');ap.add_argument('--out',default='run');args=ap.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    t,r,h,op,op1,it,ir=operators(args.n,args.L); n=args.n
    if args.seed:
        d=np.load(args.seed);t0=d['t'];r0=d['r'];q0=d['q']
        interp=RegularGridInterpolator((np.r_[0,t0],np.r_[0,r0]),np.pad(q0,((1,0),(1,0)),mode='edge'),bounds_error=False,fill_value=0)
        tt,rr=np.meshgrid(t,r,indexing='ij');q=interp(np.stack([tt,rr],axis=-1))
    else:
        p=Path(__file__).resolve().parents[1]/'core_sources/r4/BNLS_Dynamics_Package_20261007/verification/round4_n3_mixed_exact.json'
        d=json.loads(p.read_text());rad=np.array([x[0]/x[1] for x in d['nodes']]);states=np.array([[float.fromhex(x) for x in row] for row in d['states_hex']]);interp=CubicHermiteSpline(rad,states[:,0],states[:,1]);q=interp(np.sqrt(t[:,None]**2+r[None,:]**2))
    w=(q*np.sqrt(r)[None,:]).ravel();s=args.start;records=[];ds=args.ds;clock=time.time()
    while True:
        A=op[0]+s*op[1]; alpha=(8-2*s)/3
        z,err,its,ok=solve(w,A,alpha,n,r)
        if not ok:
            print(json.dumps(dict(trial_s=s,residual=err,iterations=its,status='failed',step=ds)),flush=True)
            if not records or ds<.0003:break
            ds/=2;s=records[-1]['s']+ds;continue
        w=z
        row=measures(w,s,n,r,h,A,op1[0]+s*op1[1]);row.update(residual=err,iterations=its,seconds=time.time()-clock,n=n,L=args.L)
        records.append(row);print(json.dumps(row),flush=True)
        np.savez_compressed(out/f'core_{s:.6f}.npz',q=w.reshape(n,n)/np.sqrt(r)[None,:],t=t,r=r,s=s)
        (out/'results.json').write_text(json.dumps(records,indent=2))
        if s>=args.end-1e-12:break
        ds=min(args.ds,ds*1.3);s=min(args.end,s+ds)
    (out/'config.json').write_text(json.dumps(vars(args),indent=2))

if __name__=='__main__':main()
