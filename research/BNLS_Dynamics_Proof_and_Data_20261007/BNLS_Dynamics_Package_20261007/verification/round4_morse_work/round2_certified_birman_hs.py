"""Rigorous Arb interval midpoint enclosures of radial BS trace and HS square.

The profile is the EXACT rational C3 septic Hermite function exported by the
radial agent. No floating Bessel evaluation, quadrature-error guess, or mesh
convergence assertion enters the certificate. Each cell uses a midpoint rule
with an interval enclosure of its second-derivative error. The omitted tiny origin square is
bounded by the positive resolvent inequality (H^2+1)^-1 <= (2H)^-1.
"""
import sys,os,json,time,math,hashlib,platform
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'rigorous_deps'))
import flint
from flint import arb,acb,ctx
from fractions import Fraction as F
ctx.prec=192

def aa(x):
    if isinstance(x,F):return arb(x.numerator)/x.denominator
    return arb(x)

def inverse(M):
    n=len(M);a=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
    for i in range(n):
        s=a[i][i];a[i]=[x/s for x in a[i]]
        for j in range(n):
            if i!=j:
                s=a[j][i];a[j]=[x-s*y for x,y in zip(a[j],a[i])]
    return [r[n:] for r in a]

inv=inverse([[1,1,1,1],[4,5,6,7],[12,20,30,42],[24,60,120,210]])
fn='round2_radial_H4_exact_h1_16.json'
EXPECTED_PROFILE_SHA256='c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627'
profile_bytes=open(fn,'rb').read()
profile_hash=hashlib.sha256(profile_bytes).hexdigest()
assert profile_hash==EXPECTED_PROFILE_SHA256, 'Canonical profile hash mismatch; no profile is regenerated.'
data=json.loads(profile_bytes); nodes=[F(*x) for x in data['nodes']]
jets=[[F(float.fromhex(x)) for x in row] for row in data['jets_hex']]
polys=[];rqn=F(0);qsup=F(0)
for i in range(len(nodes)-1):
    h=nodes[i+1]-nodes[i]
    low=[jets[i][j]*h**j/math.factorial(j) for j in range(4)]
    rhs=[jets[i+1][j]*h**j-sum(low[k]*F(math.factorial(k),math.factorial(k-j)) for k in range(j,4)) for j in range(4)]
    coef=low+[sum(row[j]*rhs[j] for j in range(4)) for row in inv]
    # Exact Bernstein convex-hull bound.
    bern=[sum(coef[k]*F(math.comb(j,k),math.comb(7,k)) for k in range(j+1)) for j in range(8)]
    qsup=max(qsup,max(abs(b) for b in bern))
    prod=[sum(coef[k]*coef[j-k] for k in range(max(0,j-7),min(7,j)+1)) for j in range(15)]
    rqn+=h*sum(prod[j]*(nodes[i]/(j+1)+h/F(j+2)) for j in range(15))
    polys.append([aa(c) for c in coef])

ell=int(sys.argv[1]) if len(sys.argv)>1 else 0
assert ell in (0,1,2,3,4), 'Only the five specified channels are certified.'
beta=3 if ell in (0,2,4) else 1
sub=int(sys.argv[2]) if len(sys.argv)>2 else 16
nu=ell+1;eps=F(1,100000) # endpoint cut; error is bounded explicitly below.
kap=acb(1,1)/arb(2).sqrt()
J1=arb(0);J2=arb(0);J3=arb(0);HS=arb(0);TR=arb(0)
start=time.time(); count=0

def consume(a,b,base,h,co):
    global J1,J2,J3,HS,TR,count
    step=aa(b-a);x=arb(aa((a+b)/2),aa((b-a)/2))
    def poly_at(xx,order):
        t=(xx-aa(base))/aa(h)
        cc=[co[k]*math.factorial(k)/math.factorial(k-order)/aa(h)**order for k in range(order,8)]
        val=cc[-1]
        for c in cc[-2::-1]:val=val*t+c
        return val
    # Direct complex-ball K evaluation suffers severe dependency inflation.
    # Evaluate rigorously at the exact midpoint, then enclose variation by
    # the weighted Bessel ODE W=(f,r f'), W'=[[0,1/r],[nu^2/r+i*r,0]]W.
    mid=aa((a+b)/2);rad=aa((b-a)/2);z=kap*mid
    ip=z.bessel_i(nu);kp=z.bessel_k(nu)
    dip=kap*z.bessel_i(nu-1)-nu/mid*ip
    dkp=-kap*z.bessel_k(nu-1)-nu/mid*kp
    odeL=nu**2/aa(a)+aa(b)+1/aa(a) # safe matrix infinity norm upper bound
    growth=(odeL*rad).exp()
    def enclosure(f,df):
        err=rad/aa(a)*growth*(abs(f)+mid*abs(df))
        v=f+acb(arb(0,err),arb(0,err))
        err2=rad*(nu**2/aa(a)+aa(b))*growth*(abs(f)+mid*abs(df))
        dp=(mid*df+acb(arb(0,err2),arb(0,err2)))/x
        ddp=(acb(0,1)+nu**2/x**2)*v-dp/x
        return (v,dp,ddp)
    ijet=enclosure(ip,dip);kjet=enclosure(kp,dkp)
    bi=ijet[0];bk=kjet[0]
    if not bi.is_finite() or not bk.is_finite():
        raise ArithmeticError('nonfinite Bessel cell '+str((a,b)))
    def mul(f,g):return (f[0]*g[0],f[1]*g[0]+f[0]*g[1],f[2]*g[0]+2*f[1]*g[1]+f[0]*g[2])
    def add(f,g):return tuple(u+v for u,v in zip(f,g))
    def scalar(c,f):return tuple(c*u for u in f)
    def components(xx,ij,kj):
        qq=poly_at(xx,0);qp=poly_at(xx,1);qpp=poly_at(xx,2)
        A=(xx*qq**2,qq**2+2*xx*qq*qp,4*qq*qp+2*xx*(qp**2+qq*qpp))
        ir=tuple(z.real for z in ij);ii=tuple(z.imag for z in ij)
        kr=tuple(z.real for z in kj);ki=tuple(z.imag for z in kj)
        Fs=[mul(A,mul(ir,ir)),mul(A,mul(ir,ii)),mul(A,mul(ii,ii))]
        Bs=[mul(A,mul(ki,ki)),scalar(2,mul(A,mul(kr,ki))),mul(A,mul(kr,kr))]
        trace=mul(A,add(mul(ir,ki),mul(ii,kr)))
        return Fs,Bs,trace
    imid=(ip,dip,(acb(0,1)+nu**2/mid**2)*ip-dip/mid)
    kmid=(kp,dkp,(acb(0,1)+nu**2/mid**2)*kp-dkp/mid)
    Fr,Br,Tr=components(x,ijet,kjet)
    Fm,Bm,Tm=components(mid,imid,kmid)
    old=[J1,J2,J3];partial=arb(step/2,step/2)
    jr=[old[j]+partial*Fr[j][0] for j in range(3)]
    jm=[old[j]+step/2*Fm[j][0]-step**2/8*Fm[j][1]+arb(0,step**3/48*abs(Fr[j][2])) for j in range(3)]
    gm=sum(Bm[j][0]*jm[j] for j in range(3))
    gpp=sum(Br[j][2]*jr[j]+2*Br[j][1]*Fr[j][0]+Br[j][0]*Fr[j][1] for j in range(3))
    HS+=2*beta**2*(step*gm+arb(0,step**3/24*abs(gpp)))
    TR+=-beta*(step*Tm[0]+arb(0,step**3/24*abs(Tr[2])))
    J1,J2,J3=[old[j]+step*Fm[j][0]+arb(0,step**3/24*abs(Fr[j][2])) for j in range(3)]
    count+=1

for i,co in enumerate(polys):
    left,right=nodes[i],nodes[i+1];h=right-left
    if i==0:
        a=eps
        while a<right:
            b=min(right,a*F(21,20),a+F(1,16*sub))
            consume(a,b,left,h,co);a=b
    else:
        # Preserve a maximum physical cell length even on the four-unit tail.
        ns=max(sub,math.ceil(float(h*16*sub)))
        for j in range(ns):consume(left+h*j/ns,left+h*(j+1)/ns,left,h,co)
    if i%64==0:print('progress',ell,sub,i,count,'HS',HS.str(10),'TR',TR.str(10),'sec',round(time.time()-start,1),flush=True)

trace_origin=aa(F(beta,8*nu)*qsup**2*eps**2)
trace_coarse=aa(F(beta,4*nu)*rqn)
hs_origin=2*trace_origin*trace_coarse
TR+=arb(trace_origin/2,trace_origin/2)
HS+=arb(hs_origin/2,hs_origin/2)
out={'profile':fn,'ell':ell,'beta':beta,'sub':sub,'precision_bits':ctx.prec,'cells':count,
     'trace':str(TR),'HS_squared':str(HS),'origin_trace_bound':str(trace_origin),
     'trace_upper_endpoint_enclosure':str(TR.upper()),
     'HS_squared_upper_endpoint_enclosure':str(HS.upper()),
     'origin_HS_bound':str(hs_origin),'coarse_trace_bound':str(trace_coarse),
     'profile_sup_bound':str(aa(qsup)),'seconds':time.time()-start,
     'profile_sha256':profile_hash,
     'verifier_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest(),
     'python_version':platform.python_version(),'python_flint_version':flint.__version__,
     'HS_lt_39':bool(HS<39),'HS_lt_38_9':bool(HS<arb('38.9')),
     'HS_lt_38_80':bool(HS<arb('38.80')),'HS_lt_4_80':bool(HS<arb('4.80')),
     'HS_lt_0_73':bool(HS<arb('0.73')),'HS_lt_0_22':bool(HS<arb('0.22')),
     'HS_lt_5_0':bool(HS<5),'HS_lt_1':bool(HS<1),'trace_lt_1_70':bool(TR<arb('1.70'))}
required={0:('HS_lt_38_80','HS squared < 38.80'),
          1:('trace_lt_1_70','trace < 1.70'),
          2:('HS_lt_4_80','HS squared < 4.80'),
          3:('HS_lt_0_22','HS squared < 0.22'),
          4:('HS_lt_0_73','HS squared < 0.73')}[ell]
out['required_inequality']=required[1]
out['required_pass']=out[required[0]]
assert out['required_pass'], 'The required rigorous scalar inequality was not enclosed.'
print(json.dumps(out),flush=True)
open('round2_certified_birman_l%d_sub%d.json'%(ell,sub),'w').write(json.dumps(out,indent=2))
