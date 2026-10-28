import numpy as np, scipy.optimize as so, scipy.fft as fft, scipy.linalg as la, json, time, sys

# Exact Dirichlet kinetic quadratic form on a sine collocation grid.
# Nonlinear quadrature is collocation, so all values require refinement.
def run(n=96,L=12.,kind='scalar',steps=400,complex_=False,seed=1,init_path=None,perturb=0.,tag=''):
    h=2*L/(n+1); xx=-L+h*np.arange(1,n+1); x,y=np.meshgrid(xx,xx,indexing='ij'); r2=x*x+y*y
    k=np.pi*np.arange(1,n+1)/(2*L); eig=k[:,None]**2+k[None,:]**2
    def lap(a): return fft.idstn(fft.dstn(a.reshape(n,n,-1),type=1,norm='ortho',axes=(0,1))*eig[:,:,None],type=1,norm='ortho',axes=(0,1)).reshape(n*n,-1)
    g=np.exp(-r2/2)
    if kind=='scalar': X=g[:,:,None]
    elif kind=='dipole': X=np.stack([g,x*g],axis=-1)
    elif kind=='radial': X=np.stack([g,(1-r2)*g],axis=-1)
    elif kind=='vortex': X=np.stack([(x+1j*y)*g,(x-1j*y)*g],axis=-1); complex_=True
    elif kind=='ground_vortex': X=np.stack([g,(x+1j*y)*g],axis=-1); complex_=True
    elif kind=='two_well': X=np.stack([np.exp(-((x-2)**2+y*y)/2),np.exp(-((x+2)**2+y*y)/2)],axis=-1)
    elif kind=='asymmetric': X=np.stack([np.exp(-((x-1.5)**2+2*y*y)/2),np.exp(-((x+1.5)**2+.5*y*y)/2)],axis=-1)
    elif kind=='random':
        rng=np.random.default_rng(seed); X=np.stack([g*(1+.4*rng.normal(size=g.shape)),x*g+.4*g*rng.normal(size=g.shape)],axis=-1)
    if init_path:
        init=np.load(init_path);YY=init['Y'];nn=YY.shape[0];coef=fft.dstn(YY,type=1,norm='ortho',axes=(0,1));cc=np.zeros((n,n,YY.shape[2]),dtype=YY.dtype);lim=min(n,nn);cc[:lim,:lim]=coef[:lim,:lim];X=fft.idstn(cc,type=1,norm='ortho',axes=(0,1));complex_=np.iscomplexobj(X)
    if perturb:
        rng=np.random.default_rng(seed);X=X+perturb*np.max(abs(X))*g[:,:,None]*rng.normal(size=X.shape)
    X=X.reshape(n*n,-1).astype(np.complex128 if complex_ else np.float64); rank=X.shape[1]; Ktarget=1. if rank==1 else 2.
    def pack(z): return np.concatenate([z.real.ravel(),z.imag.ravel()]) if complex_ else z.ravel()
    def unpack(z): return (z[:n*n*rank]+1j*z[n*n*rank:]).reshape(n*n,rank) if complex_ else z.reshape(n*n,rank)
    def calc(z,grad=True):
        a=unpack(z); w,v=la.eigh(a.conj().T@a); Hi=(v/w**.5)@v.conj().T; Y=a@Hi
        LY=lap(Y); K=np.vdot(Y,LY).real; rho=(abs(Y)**2).sum(axis=1); F=np.dot(rho,rho)/h**2; R=F/K
        penalty=.04*np.log(K/Ktarget)**2
        val=-R+penalty
        G=-(4*rho[:,None]*Y/h**2-R*2*LY)/K + .08*np.log(K/Ktarget)/K*2*LY
        G=(G-Y@(Y.conj().T@G))@Hi
        if grad:return val,pack(G)
        return dict(kind=kind,n=n,L=L,C=R,K=K,F=F,penalty=penalty,mass_error=float(np.max(abs(Y.conj().T@Y-np.eye(rank))))),Y
    z=pack(X); rng=np.random.default_rng(332); d=rng.normal(size=z.shape);d/=la.norm(d);f,df=calc(z); eps=1e-5;fd=(calc(z+eps*d)[0]-calc(z-eps*d)[0])/(2*eps)
    err=abs(fd-np.dot(df,d)); t=time.time()
    opt=so.minimize(calc,z,jac=True,method='L-BFGS-B',options={'maxiter':steps,'ftol':1e-13,'gtol':1e-9,'maxcor':10,'maxls':30})
    result,Y=calc(opt.x,False);result.update(iterations=opt.nit,success=bool(opt.success),message=str(opt.message),seconds=time.time()-t,gradcheck=err)
    np.savez_compressed(f'research/r15_numerics_{kind}_{n}{tag}.npz',Y=Y.reshape(n,n,rank),h=h,**result)
    print(json.dumps(result),flush=True); return result

if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 96
    kinds=sys.argv[2:] or ['scalar','dipole','ground_vortex','radial','vortex','two_well','asymmetric']
    rr=[run(n=n,kind=s) for s in kinds]
    with open(f'research/r15_numerics_results_{n}.json','w') as f:json.dump(rr,f,indent=2)
