"""Radial rank-two whole-plane Laguerre search, with angular Hessian.
Exploratory floating point, not a rigorous eigenvalue enclosure.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import numpy as np, scipy.linalg as la, scipy.optimize as so
from scipy.special import roots_laguerre, eval_genlaguerre, gammaln
import json

def kinetic(d,m):
    n=np.arange(d+1)
    off=np.sqrt((n[:-1]+1)*(n[:-1]+m+1))
    return np.diag(2*n+m+1.)+np.diag(off,1)+np.diag(off,-1)

def polys(x,d,m):
    return np.stack([x**(m/2)*eval_genlaguerre(n,m,x)*np.exp(.5*(gammaln(n+1)-gammaln(n+m+1))) for n in range(d+1)],axis=1)/np.sqrt(np.pi)

def run(d,seed):
    y,w=roots_laguerre(2*d+5);x=y/2;measure=np.pi*w/2
    B=polys(x,d,0);D=B*measure[:,None]**.25;K=kinetic(d,0)
    rng=np.random.default_rng(seed)
    A=np.eye(d+1,2)+.1*rng.normal(size=(d+1,2))*np.exp(-np.arange(d+1)[:,None]/4)
    def calc(a,ret=False):
        A=a.reshape(d+1,2);ee,V=la.eigh(A.T@A);H=(V/np.sqrt(ee))@V.T;C=A@H
        Z=D@C;rho=(Z**2).sum(1);F=rho@rho;T=np.sum(C*(K@C));R=F/T
        G=-(4*D.T@(rho[:,None]*Z)-2*R*K@C)/T
        G=(G-C@(C.T@G))@H
        if ret:return C,R,F,T,float(la.norm(G))
        return -R,G.ravel()
    z=so.minimize(calc,A.ravel(),jac=True,method='L-BFGS-B',options={'maxiter':2500,'gtol':1e-10,'ftol':1e-14,'maxcor':20})
    C,R,F,T,gn=calc(z.x,True)
    # Diagonalize occupied Lagrange multipliers.
    U=B@C;dens=(U**2).sum(1)
    Vmat=(2/R)*B.T@((measure*dens)[:,None]*B)
    H0=K-Vmat
    occ,rot=la.eigh(C.T@H0@C);C=C@rot;U=B@C
    hm={};hes={}
    for m in (1,2,3):
        Bm=polys(x,d,m);Km=kinetic(d,m)
        Hm=Km-(2/R)*Bm.T@((measure*dens)[:,None]*Bm)
        hm[m]=la.eigvalsh(Hm)[:4].tolist()
        blocks=[]
        for i in range(2):
            row=[]
            for j in range(2):
                M=-(4/R)*Bm.T@((measure*U[:,i]*U[:,j])[:,None]*Bm)
                if i==j:M=M+Hm-occ[i]*np.eye(d+1)
                row.append(M)
            blocks.append(row)
        hes[m]=la.eigvalsh(np.block(blocks))[:4].tolist()
    res={'degree':d,'seed':seed,'R':R,'F':F,'T':T,'gradnorm':gn,'iterations':z.nit,'success':bool(z.success),'occ':occ.tolist(),'lowest_m0':la.eigvalsh(H0)[:4].tolist(),'lowest_m':hm,'hessian_lowest_m':hes,'edge_weight':float(np.sum(C[-4:]**2))}
    np.savez_compressed(f'r23_radial_d{d}_s{seed}.npz',C=C)
    print(json.dumps(res),flush=True)
    return res

if __name__=='__main__':
    results=[]
    for d in (20,40,60):
        for seed in (13,31):results.append(run(d,seed))
    with open('r23_radial_results.json','w') as f:json.dump(results,f,indent=2)
