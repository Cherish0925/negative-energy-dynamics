"""Whole-space Arb certificate for the N3 ell=1 inverse-response trial.
Only exact rational splines and outward-rounded ball arithmetic are used.
"""
import json,hashlib,math,time,sys
from fractions import Fraction as F
import flint
from flint import arb,acb,arb_poly,ctx
ctx.prec=192
QHASH='5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b'
qraw=open('round4_n3_mixed_exact.json','rb').read()
assert hashlib.sha256(qraw).hexdigest()==QHASH
qobj=json.loads(qraw)
nodes=[F(*v) for v in qobj['nodes']]
qs=[[F(float.fromhex(v)) for v in row] for row in qobj['states_hex']]
def A(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def upper(x):return x.upper()
def maxa(x,y):return x if x>y else y if y>x else upper((x+y+abs(x-y))/2)
def intsquare(poly,length):
 cc=(poly*poly).coeffs();out=A(length)*sum((cc[j]/(j+1) for j in range(0,len(cc),2)),arb(0));return upper(out)
def solve3(M,r):
 rows=[[F(v) for v in row]+[rhs] for row,rhs in zip(M,r)]
 for i in range(3):
  fac=rows[i][i];rows[i]=[v/fac for v in rows[i]]
  for j in range(3):
   if i!=j:
    fac=rows[j][i];rows[j]=[v-fac*w for v,w in zip(rows[j],rows[i])]
 return [row[-1] for row in rows]
def poly(f0,fp0,fpp0,f1,fp1,fpp1,h,origin=False):
 if origin:
  a2,a4,a6=solve3([[1,1,1],[2,4,6],[2,12,30]],[f1-f0,h*fp1,h*h*fpp1]);c=[f0,F(0),a2,F(0),a4,F(0),a6]
 else:
  c=[f0,h*fp0,h*h*fpp0/2]
  rhs=[f1-sum(c),h*fp1-c[1]-2*c[2],h*h*fpp1-2*c[2]]
  c+=solve3([[1,1,1],[3,4,5],[6,12,20]],rhs)
 assert c[0]==f0 and c[1]==h*fp0
 assert sum(c)==f1 and sum(j*c[j] for j in range(len(c)))==h*fp1
 assert sum(j*(j-1)*c[j] for j in range(len(c)))==h*h*fpp1
 if not origin:assert 2*c[2]==h*h*fpp0
 return arb_poly([A(v) for v in c])


ell=int(sys.argv[1]);beta=arb(11)/3 if ell%2==0 else arb(1);sub=int(sys.argv[2]) if len(sys.argv)>2 else 1;nu=arb(2*ell+1)/2;eps=F(1,10**7)
kap=acb(1,1)/arb(2).sqrt()
J1=arb(0);J2=arb(0);J3=arb(0);HS=arb(0);TR=arb(0)
start=time.time();count=0
aa=A
def consume(a,b,base,h,co):
    global J1,J2,J3,HS,TR,count
    step=aa(b-a);x=arb(aa((a+b)/2),aa((b-a)/2))
    def poly_at(xx,order):
        t=(xx-aa(base))/aa(h)
        cc=[co[k]*math.factorial(k)/math.factorial(k-order)/aa(h)**order for k in range(order,len(co))]
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
        t=abs(qq)**(arb(2)/3) if not qq.contains(0) else arb((abs(qq).upper()**(arb(2)/3))/2,(abs(qq).upper()**(arb(2)/3))/2)
        V=qq**2*t;Vp=arb(8)/3*qq*t*qp
        Vpp=arb(8)/3*(arb(5)/3*t*qp**2+qq*t*qpp)
        A=(xx*V,V+xx*Vp,2*Vp+xx*Vpp)
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

for i in range(len(nodes)-1):
 left,right=nodes[i],nodes[i+1];h=right-left
 co=poly(*qs[i][:3],*qs[i+1][:3],h,origin=i==0).coeffs()
 if i==0:
  a=eps
  while a<right:
   b=min(right,2*a);ns=10*sub*(ell+1)**2
   for k in range(ns):consume(a+(b-a)*k/ns,a+(b-a)*(k+1)/ns,left,h,co)
   a=b
 else:
  ns=max(sub,math.ceil(float(h*100*sub)),math.ceil(float(h/left)*10*sub*(ell+1)**2))
  for j in range(ns):consume(left+h*j/ns,left+h*(j+1)/ns,left,h,co)
 if i%3000==0:print('progress',i,count,'HS',HS.str(10),'TR',TR.str(10),'sec',round(time.time()-start,1),flush=True)
Vmax=(arb(63)/10)**(arb(8)/3)
trace_origin=beta*Vmax*A(eps)**2/(8*nu)
trace_coarse=beta*Vmax*54**2/(8*nu)
hs_origin=2*trace_origin*trace_coarse
TR+=arb(trace_origin/2,trace_origin/2);HS+=arb(hs_origin/2,hs_origin/2)
out={'status':'whole-space radial Birman Schwinger Hilbert Schmidt bound','ell':ell,'beta':str(beta),'profile_sha256':QHASH,'precision_bits':ctx.prec,'subdivision_multiplier':sub,'cells':count,'trace':str(TR),'HS_squared':str(HS),'HS_squared_upper':str(HS.upper()),'origin_HS_bound':str(hs_origin),'HS_squared_lt_8_8':bool(HS<arb(88)/10),'seconds':time.time()-start}
print(json.dumps(out,indent=2));open(f'round5_n3_channels_hs_l{ell}_sub{sub}.json','w').write(json.dumps(out,indent=2)+'\n')
assert HS.is_finite()
