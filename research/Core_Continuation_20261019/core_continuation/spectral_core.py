"""DCT/Bessel pseudospectral independent discretization of axisymmetric cores.
Quasi-discrete Hankel matrix is orthogonalized by its polar factor.
Analytic Bessel derivatives are used for the angular-one response source.
Numerical evidence only, not a proof of whole-space existence.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy import special,linalg
from scipy.fft import dct,idct
from scipy.sparse.linalg import LinearOperator,minres
from scipy.interpolate import RectBivariateSpline

class Solver:
    def __init__(self,nt,nr,Lt,Lr,kind='mixed'):
        self.nt=nt;self.nr=nr;self.N=nt*nr;self.ht=Lt/nt;self.t=(np.arange(nt)+.5)*self.ht;self.Lr=Lr;self.kind=kind
        self.kt=(np.arange(nt)+.5)*np.pi/Lt;self.rs=[];self.ws=[];self.T=[];self.kr=[];self.zeros=[];self.jnorm=[];self.orth_error=[]
        for m in [0,1]:
            zz=special.jn_zeros(m,nr+1);end=zz[-1];zz=zz[:-1];jn=abs(special.jv(m+1,zz));r=Lr*zz/end;weights=2*Lr**2/(end**2*jn**2)
            mat=2*special.jv(m,np.outer(zz,zz)/end)/(end*np.outer(jn,jn));vals,vec=linalg.eigh(mat);self.orth_error.append(float(max(abs(abs(vals)-1))));mat=(vec*np.sign(vals))@vec.T
            self.rs.append(r);self.ws.append(np.sqrt(weights));self.T.append(mat);self.kr.append(zz/Lr);self.zeros.append(zz);self.jnorm.append(jn)
        self.wr=np.tile(self.ws[0],nt)
        self.eval01=np.sqrt(2)/Lr*special.jv(0,np.outer(self.rs[1],self.kr[0]))/self.jnorm[0][None,:]
        self.deriv01=-np.sqrt(2)/Lr*special.jv(1,np.outer(self.rs[1],self.kr[0]))*self.kr[0][None,:]/self.jnorm[0][None,:]
    def spec(self,s,m):
        a=self.kt[:,None]**2;b=self.kr[m][None,:]**2
        if self.kind=='mixed':return (1-s)*(a+b)**2+s*(a+b*b)+1,(8-2*s)/3
        if s<=1:return a*a+b*b+2*(1-s)*a*b+1,8/3
        order=6-2*s;return a**(order/2)+b*b+1,4*order/(order+2)
    def func(self,z,a,m,power):
        b=dct(z.reshape(self.nt,self.nr),type=4,norm='ortho',axis=0)@self.T[m]
        return idct((b*a**power)@self.T[m].T,type=4,norm='ortho',axis=0).ravel()
    def newton(self,w,s):
        a,alpha=self.spec(s,0);half=lambda v:self.func(v,a,0,-.5)
        def f(z):return self.func(z,a,0,1)-abs(z/self.wr)**alpha*z
        z=w.copy();den=max(np.linalg.norm(z),1);fz=f(z)
        for iteration in range(24):
            err=np.linalg.norm(fz)/den
            if err<2e-8:return z,float(err),iteration,True
            potential=(alpha+1)*abs(z/self.wr)**alpha;H=LinearOperator((self.N,self.N),matvec=lambda v:v-half(potential*half(v)))
            sol,info=minres(H,-half(fz),rtol=1e-12,maxiter=3000);dz=half(sol);step=1.
            while step>1/2048:
                trial=z+step*dz;ft=f(trial)
                if np.linalg.norm(ft)<np.linalg.norm(fz)*(1-1e-4*step):break
                step/=2
            if step<=1/2048:return z,float(err),iteration,False
            z=trial;fz=ft
        return z,float(np.linalg.norm(fz)/den),24,False
    def diag(self,w,s):
        a,alpha=self.spec(s,0);a1,_=self.spec(s,1);q=w.reshape(self.nt,self.nr)/self.ws[0][None,:];coef=w.reshape(self.nt,self.nr)@self.T[0];q1=coef@self.eval01.T;qr1=coef@self.deriv01.T;src=(qr1*self.ws[1][None,:]).ravel();v1=abs(q1.ravel())**alpha;half=lambda v:self.func(v,a1,1,-.5);H=LinearOperator((self.N,self.N),matvec=lambda v:v-half(v1*half(v)));sol,info=minres(H,half(src),rtol=1e-12,maxiter=4000);chi=half(sol);err=np.linalg.norm(self.func(chi,a1,1,1)-v1*chi-src)/np.linalg.norm(src)
        fac=4*np.pi*self.ht;M=fac*np.dot(w,w);A=fac*np.dot(w,self.func(w,a,0,1)-w);NL=fac*np.dot(w,abs(q.ravel())**alpha*w);I=fac/2*np.dot(src,chi);ft=dct(w.reshape(self.nt,self.nr),type=4,norm='ortho',axis=0)@self.T[0];tail=(np.sum(ft[-self.nt//8:,:]**2)+np.sum(ft[:,-self.nr//8:]**2))/np.sum(ft**2)
        return dict(s=s,alpha=alpha,mass=float(M),energy=float(A/2-NL/(alpha+2)),response_I=float(I),response_residual=float(err),response_info=info,peak=float(abs(q).max()),spectral_tail=float(tail),orthogonalization_correction=self.orth_error)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--nt',type=int,default=256);ap.add_argument('--nr',type=int,default=128);ap.add_argument('--Lt',type=float,default=24);ap.add_argument('--Lr',type=float,default=24);ap.add_argument('--kind',default='mixed');ap.add_argument('--ds',type=float,default=.005);ap.add_argument('--start',type=float,default=1);ap.add_argument('--end',type=float,default=1);ap.add_argument('--seed',required=True);ap.add_argument('--out',required=True);args=ap.parse_args();S=Solver(args.nt,args.nr,args.Lt,args.Lr,args.kind);out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    d=np.load(args.seed);t0=d['t'];r0=d['r'];q0=d['q'];tx=np.r_[-t0[:4][::-1],t0];rx=np.r_[-r0[:4][::-1],r0];qq=np.concatenate([q0[:4,:][::-1,:],q0]);qq=np.concatenate([qq[:,:4][:,::-1],qq],axis=1);interp=RectBivariateSpline(tx,rx,qq);q=interp(S.t,S.rs[0]);w=q.ravel()*S.wr;s=args.start;ds=args.ds;records=[];clock=time.time()
    while True:
        z,err,it,ok=S.newton(w,s)
        if not ok:
            print(json.dumps(dict(trial_s=s,residual=err,iterations=it,status='failed',step=ds)),flush=True)
            if not records or ds<.0002:break
            ds/=2;s=records[-1]['s']+ds;continue
        w=z;row=S.diag(w,s);row.update(residual=err,iterations=it,seconds=time.time()-clock,nt=args.nt,nr=args.nr,Lt=args.Lt,Lr=args.Lr,kind=args.kind);records.append(row);print(json.dumps(row),flush=True);np.savez_compressed(out/f'core_{s:.6f}.npz',q=w.reshape(S.nt,S.nr)/S.ws[0][None,:],t=S.t,r=S.rs[0],s=s);(out/'results.json').write_text(json.dumps(records,indent=2))
        if s>=args.end-1e-12:break
        ds=min(args.ds,ds*1.25);s=min(args.end,s+ds)
    (out/'config.json').write_text(json.dumps(vars(args),indent=2))
if __name__=='__main__':main()
