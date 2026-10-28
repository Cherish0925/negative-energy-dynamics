"""Pseudo-arclength continuation through folds of the critical quartic path."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu
from continue_core import operators

ap=argparse.ArgumentParser();ap.add_argument('--first',required=True);ap.add_argument('--second',required=True);ap.add_argument('--out',required=True);ap.add_argument('--steps',type=int,default=45);ap.add_argument('--step',type=float,default=.02);args=ap.parse_args()
d0=np.load(args.first);d1=np.load(args.second);n=len(d1['r']);h=float(d1['r'][1]-d1['r'][0]);L=n*h;t,r,h,op,op1,it,ir=operators(n,L);wr=np.tile(np.sqrt(r),n);w0=d0['q'].ravel()*wr;w=d1['q'].ravel()*wr;s0=float(d0['s']);s=float(d1['s']);D=(-2*it@ir).tocsc();base=op[0];alpha=8/3;weight=1/np.dot(w,w);out=Path(args.out);out.mkdir(exist_ok=True,parents=True)
tw=w-w0;ts=s-s0;norm=np.sqrt(weight*np.dot(tw,tw)+ts*ts);tw/=norm;ts/=norm;records=[];clock=time.time();ds=args.step
for step in range(args.steps):
    wp=w+ds*tw;sp=s+ds*ts;z=wp.copy();p=sp;ok=False
    for iteration in range(18):
        A=base+p*D;pot=abs(z/wr)**alpha;F=A@z-pot*z;g=weight*np.dot(tw,z-wp)+ts*(p-sp);err=np.sqrt(np.dot(F,F)*weight+g*g)
        if err<1e-8:ok=True;break
        lu=splu(A-sparse.diags((alpha+1)*pot,format='csc'));sol=lu.solve(np.column_stack((-F,D@z)));b=sol[:,0];c=sol[:,1];den=ts-weight*np.dot(tw,c);dp=(-g-weight*np.dot(tw,b))/den;dz=b-c*dp
        scale=1.
        while scale>1/512:
            zz=z+scale*dz;pp=p+scale*dp;ff=(base+pp*D)@zz-abs(zz/wr)**alpha*zz;gg=weight*np.dot(tw,zz-wp)+ts*(pp-sp);ee=np.sqrt(weight*np.dot(ff,ff)+gg*gg)
            if ee<err:break
            scale/=2
        if scale<=1/512:break
        z=zz;p=pp
    if not ok:
        print(json.dumps(dict(step=step,status='failed',s=p,residual=err,arc_step=ds)),flush=True);ds/=2
        if ds<.0003:break
        continue
    ntw=z-w;nts=p-s;norm=np.sqrt(weight*np.dot(ntw,ntw)+nts*nts);ntw/=norm;nts/=norm
    if weight*np.dot(ntw,tw)+nts*ts<0:ntw=-ntw;nts=-nts
    w=z;s=p;tw=ntw;ts=nts;ds=min(args.step,ds*1.2)
    row=dict(step=step,s=float(s),residual=float(err),tangent_s=float(ts),iterations=iteration,mass=float(4*np.pi*h*h*np.dot(w,w)),seconds=time.time()-clock);records.append(row);print(json.dumps(row),flush=True);np.savez_compressed(out/f'core_step_{step:03d}.npz',q=w.reshape(n,n)/np.sqrt(r)[None,:],t=t,r=r,s=s);(out/'results.json').write_text(json.dumps(records,indent=2))
    if s>=1:break
