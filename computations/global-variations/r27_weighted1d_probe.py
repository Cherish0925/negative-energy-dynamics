"""Exploratory test of a proposed weighted 1D lemma, not a certified proof.

This lemma would control the exact equality class of a 2D slicing bound.
The original 2D Lieb--Thirring conjecture is not the numerical objective here.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import json
from pathlib import Path
import numpy as np
from scipy import linalg as la, optimize as so
from scipy.special import roots_hermite, eval_hermite, gammaln

def run(rank, cut, seed):
    rng = np.random.default_rng(seed)
    z, w = roots_hermite(2 * cut + 5)
    x = z / np.sqrt(2)
    n = np.arange(cut + 1)
    pol = np.stack([eval_hermite(k, x) * np.exp(-.5 * (k*np.log(2)+gammaln(k+1))) / np.pi**.25 for k in n], 1)
    D = pol * (w/np.sqrt(2))[:, None]**.25
    K = np.diag(n + .5)
    for k in range(cut-1):
        K[k, k+2] = K[k+2, k] = -.5*np.sqrt((k+1)*(k+2))
    m = (cut+1)*rank
    def calc(v, detail=False):
        A = v[:m].reshape(cut+1, rank)
        ee, V = la.eigh(A.T @ A)
        h = np.sqrt(np.maximum(ee, 1e-14))
        Hinv = (V/h)@V.T
        C = A@Hinv
        c = np.exp(v[m:])
        Z = D@C
        rho = Z**2@c
        F = rho@rho
        KC = K@C
        T = np.sum(C*KC)
        c4 = np.sum(c**4)
        den = np.sqrt(c4*T)
        R = F/den
        G = (4*D.T@(rho[:,None]*Z*c)-F*KC/T)/den
        B = C.T@G
        BV = V.T@(B-B.T)@V
        L = V@(BV/(h[:,None]+h[None,:]))@V.T
        GA = (G-C@B)@Hinv+C@L
        gc = (2*(Z**2).T@rho-2*F*c**3/c4)/den*c
        if detail:
            return dict(rank=rank,cut=cut,seed=seed,ratio=float(3*R**2),weights=(c/np.max(c)).tolist(),orth_error=float(la.norm(C.T@C-np.eye(rank)))), C, c
        return -R, -np.r_[GA.ravel(),gc]
    A = np.eye(cut+1,rank)+.12*rng.normal(size=(cut+1,rank))*np.exp(-n[:,None]/7)
    v = np.r_[A.ravel(),rng.normal(size=rank)*.5]
    d = rng.normal(size=v.size);d/=la.norm(d);eps=2e-6
    f,g=calc(v)
    check=abs((calc(v+eps*d)[0]-calc(v-eps*d)[0])/(2*eps)-g@d)
    result=so.minimize(calc,v,jac=True,method='L-BFGS-B',bounds=[(None,None)]*m+[(-8,8)]*rank,options={'maxiter':1200,'ftol':1e-13,'gtol':2e-8,'maxls':30})
    out,C,c=calc(result.x,True)
    out.update(iterations=int(result.nit),gradient_check=check)
    if out['ratio']>1.000001:
        path=Path(__file__).with_name(f'r27_weighted1d_n{rank}_s{seed}.npz')
        np.savez_compressed(path,C=C,c=c)
        out['candidate']=str(path)
    return out

if __name__=='__main__':
    rows=[]
    for rank in [2,3,4]:
        for seed in [27,53,91]:
            row=run(rank,36,seed);rows.append(row);print(json.dumps(row),flush=True)
    Path(__file__).with_name('r27_weighted1d_probe.json').write_text(json.dumps(rows,indent=2)+'\n')
