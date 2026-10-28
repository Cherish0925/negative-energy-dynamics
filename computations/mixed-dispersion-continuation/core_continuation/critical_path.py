"""Mass-critical homotopy: remove quartic cross term, then vary temporal order.
Finite-volume radial and temporal spectral functional calculus; exploratory.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy import sparse,linalg
from scipy.fft import dct,idct
from scipy.sparse.linalg import LinearOperator,minres
from scipy.interpolate import RegularGridInterpolator
from continue_core import operators

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=128);ap.add_argument('--L',type=float,default=24);ap.add_argument('--ds',type=float,default=.05);ap.add_argument('--start',type=float,default=0);ap.add_argument('--end',type=float,default=2);ap.add_argument('--seed',required=True);ap.add_argument('--out',required=True);args=ap.parse_args();n=args.n;N=n*n;h=args.L/n
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    t,r,h,_,_,_,ir=operators(n,args.L)
    dr=ir[:n,:n].toarray(); ev0,R0=linalg.eigh(-dr);ev1,R1=linalg.eigh(-dr+np.diag(1/r**2))
    evT=4*np.sin((np.arange(n)+.5)*np.pi/(2*n))**2/h**2
    def spectrum(s,ev):
        if s<=1:return evT[:,None]**2+ev[None,:]**2+2*(1-s)*evT[:,None]*ev[None,:]+1,8/3
        order=6-2*s;return evT[:,None]**(order/2)+ev[None,:]**2+1,4*order/(order+2)
    def func(z,R,a,power):
        a0=dct(z.reshape(n,n),type=4,norm='ortho',axis=0)@R
        return idct((a0*a**power)@R.T,type=4,norm='ortho',axis=0).ravel()
    seed=np.load(args.seed);interp=RegularGridInterpolator((np.r_[0,seed['t']],np.r_[0,seed['r']]),np.pad(seed['q'],((1,0),(1,0)),mode='edge'),bounds_error=False,fill_value=0);tt,rr=np.meshgrid(t,r,indexing='ij');q=interp(np.stack([tt,rr],axis=-1));wr=np.tile(np.sqrt(r),n);w=q.ravel()*wr
    def newton(w,s):
        a,alpha=spectrum(s,ev0);solvehalf=lambda v:func(v,R0,a,-.5);apply=lambda v:func(v,R0,a,1)
        def f(z):return apply(z)-np.abs(z/wr)**alpha*z
        z=w.copy();den=max(np.linalg.norm(z),1);fz=f(z)
        for iteration in range(20):
            err=np.linalg.norm(fz)/den
            if err<1e-8:return z,float(err),iteration,True
            potential=(alpha+1)*np.abs(z/wr)**alpha
            H=LinearOperator((N,N),matvec=lambda v:v-solvehalf(potential*solvehalf(v)))
            sol,info=minres(H,-solvehalf(fz),rtol=1e-11,maxiter=2000)
            dz=solvehalf(sol);step=1.
            while step>1/1024:
                trial=z+step*dz;ft=f(trial)
                if np.linalg.norm(ft)<np.linalg.norm(fz)*(1-1e-4*step):break
                step/=2
            if step<=1/1024:return z,float(err),iteration,False
            z=trial;fz=ft
        return z,float(np.linalg.norm(fz)/den),20,False
    def diagnostics(w,s):
        a,alpha=spectrum(s,ev0);a1,_=spectrum(s,ev1);q=w.reshape(n,n)/np.sqrt(r)[None,:]
        ext=np.pad(q,((0,0),(2,2)),mode='symmetric');qr=(ext[:,0:-4]-8*ext[:,1:-3]+8*ext[:,3:-1]-ext[:,4:])/(12*h);src=qr.ravel()*wr;potential=abs(q.ravel())**alpha
        half=lambda v:func(v,R1,a1,-.5);H=LinearOperator((N,N),matvec=lambda v:v-half(potential*half(v)));sol,info=minres(H,half(src),rtol=1e-11,maxiter=3000);chi=half(sol)
        err=np.linalg.norm(func(chi,R1,a1,1)-potential*chi-src)/np.linalg.norm(src);fac=4*np.pi*h*h
        M=fac*np.dot(w,w);A=fac*np.dot(w,func(w,R0,a,1)-w);NL=fac*np.dot(w,potential*w);I=fac/2*np.dot(src,chi)
        return dict(s=s,alpha=alpha,mass=float(M),energy=float(A/2-NL/(alpha+2)),response_I=float(I),response_residual=float(err),linear_info=info,peak=float(abs(q).max()))
    s=args.start;ds=args.ds;records=[];clock=time.time()
    while True:
        z,err,it,ok=newton(w,s)
        if not ok:
            print(json.dumps(dict(trial_s=s,residual=err,iterations=it,status='failed',step=ds)),flush=True)
            if not records or ds<.0005:break
            ds/=2;s=records[-1]['s']+ds;continue
        w=z;row=diagnostics(w,s);row.update(residual=err,iterations=it,seconds=time.time()-clock,n=n,L=args.L);records.append(row);print(json.dumps(row),flush=True)
        np.savez_compressed(out/f'core_{s:.6f}.npz',q=w.reshape(n,n)/np.sqrt(r)[None,:],t=t,r=r,s=s);(out/'results.json').write_text(json.dumps(records,indent=2))
        if s>=args.end-1e-12:break
        ds=min(args.ds,ds*1.25);s=min(args.end,s+ds)
    (out/'config.json').write_text(json.dumps(vars(args),indent=2))
if __name__=='__main__':main()
