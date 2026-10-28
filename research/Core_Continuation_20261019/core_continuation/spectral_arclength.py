"""Bordered pseudo-arclength for the full spectral mixed-dispersion path."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator,minres
from spectral_core import Solver

ap=argparse.ArgumentParser();ap.add_argument('--first',required=True);ap.add_argument('--second',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=35);ap.add_argument('--step',type=float,default=.004);args=ap.parse_args();d0=np.load(args.first);d1=np.load(args.second);nt,nr=d1['q'].shape;Lt=(d1['t'][1]-d1['t'][0])*nt;S=Solver(nt,nr,Lt,24);w0=d0['q'].ravel()*S.wr;w=d1['q'].ravel()*S.wr;s0=float(d0['s']);s=float(d1['s']);weight=1/np.dot(w,w);tw=w-w0;ts=s-s0;norm=np.sqrt(weight*np.dot(tw,tw)+ts*ts);tw/=norm;ts/=norm;out=Path(args.out);out.mkdir(parents=True,exist_ok=True);records=[];clock=time.time();ds=args.step
da=S.spec(1,0)[0]-S.spec(0,0)[0]
for step in range(args.steps):
    wp=w+ds*tw;sp=s+ds*ts;z=wp.copy();p=sp;ok=False
    for iteration in range(16):
        a,alpha=S.spec(p,0);qabs=abs(z/S.wr);potential=qabs**alpha;F=S.func(z,a,0,1)-potential*z;g=weight*np.dot(tw,z-wp)+ts*(p-sp);err=np.sqrt(weight*np.dot(F,F)+g*g)
        if err<2e-8:ok=True;break
        half=lambda v:S.func(v,a,0,-.5);H=LinearOperator((S.N,S.N),matvec=lambda v:v-half((alpha+1)*potential*half(v)))
        fs=S.func(z,da+1,0,1)-z # func expects a power; da+1 can be signed, power=1 is valid.
        fs+=(2/3)*np.log(np.maximum(qabs,1e-250))*potential*z
        sol0,_=minres(H,-half(F),rtol=1e-12,maxiter=3500);b=half(sol0);sol1,_=minres(H,half(fs),rtol=1e-12,maxiter=3500);c=half(sol1);dp=(-g-weight*np.dot(tw,b))/(ts-weight*np.dot(tw,c));dz=b-c*dp;scale=1.
        while scale>1/1024:
            zz=z+scale*dz;pp=p+scale*dp;aa,al=S.spec(pp,0)
            if pp>=1:scale/=2;continue
            ff=S.func(zz,aa,0,1)-abs(zz/S.wr)**al*zz;gg=weight*np.dot(tw,zz-wp)+ts*(pp-sp);ee=np.sqrt(weight*np.dot(ff,ff)+gg*gg)
            if ee<err:break
            scale/=2
        if scale<=1/1024:break
        z=zz;p=pp
    if not ok:
        print(json.dumps(dict(step=step,status='failed',s=p,residual=err,arc_step=ds)),flush=True);ds/=2
        if ds<.0001:break
        continue
    ntw=z-w;nts=p-s;norm=np.sqrt(weight*np.dot(ntw,ntw)+nts*nts);ntw/=norm;nts/=norm
    if weight*np.dot(ntw,tw)+nts*ts<0:ntw=-ntw;nts=-nts
    w=z;s=p;tw=ntw;ts=nts;ds=min(args.step,ds*1.2)
    row=dict(step=step,s=float(s),residual=float(err),tangent_s=float(ts),iterations=iteration,seconds=time.time()-clock)
    if step%5==0:row.update(S.diag(w,s))
    records.append(row);print(json.dumps(row),flush=True);np.savez_compressed(out/f'core_step_{step:03d}.npz',q=w.reshape(S.nt,S.nr)/S.ws[0][None,:],t=S.t,r=S.rs[0],s=s);(out/'results.json').write_text(json.dumps(records,indent=2))
    if s>=.99999:break
