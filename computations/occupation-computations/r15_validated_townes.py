"""Directed IEEE-754 interval Taylor shooting; no scipy solver is trusted.

All finite input floats are interpreted as exact dyadic real numbers. Each
arithmetic operation is widened one representable float on both sides.
Only addition, multiplication, division and integer powers enter the proof.
"""
import math, json, time

def down(x): return math.nextafter(x,-math.inf)
def up(x): return math.nextafter(x,math.inf)
class I:
    __slots__=('lo','hi')
    def __init__(self,a,b=None): self.lo=float(a);self.hi=float(a if b is None else b)
    def __add__(a,b):
        if not isinstance(b,I): b=I(b)
        return I(down(a.lo+b.lo),up(a.hi+b.hi))
    __radd__=__add__
    def __neg__(a): return I(-a.hi,-a.lo)
    def __sub__(a,b): return a+-asI(b)
    def __rsub__(a,b): return asI(b)+-a
    def __mul__(a,b):
        if not isinstance(b,I): b=I(b)
        z=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
        return I(down(min(z)),up(max(z)))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=asI(b)
        if b.lo<=0<=b.hi: raise ValueError(('zero division',b))
        return a*I(down(1/b.hi),up(1/b.lo))
    def __repr__(a): return f'[{a.lo:.17g},{a.hi:.17g}]'
    def abs(a): return max(abs(a.lo),abs(a.hi))
def asI(x): return x if isinstance(x,I) else I(x)
def hull(a,b): return I(min(a.lo,b.lo),max(a.hi,b.hi))
def subset(a,b): return b.lo<=a.lo and a.hi<=b.hi
def power(a,n):
    z=I(1)
    for _ in range(n): z=z*a
    return z
def polynomial(c,x):
    y=c[-1]
    for ci in c[-2::-1]: y=ci+x*y
    return y
def origin(a,K=20):
    # On complex |r|<=1/10, Picard maps |q-a|<=1/10 into itself:
    # |q|<=2.31, displacement <=.01/4*(2.31+2.31^3)<.1;
    # contraction <=.01/4*(1+3*2.31^2)<1.
    assert 2.20<=a.lo<=a.hi<=2.21
    c=[a]
    for n in range(K):
        cubic=sum((c[i]*c[j]*c[n-i-j] for i in range(n+1) for j in range(n-i+1)),I(0))
        c.append((c[n]-cubic)/(4*(n+1)**2))
    r=I(1/128); x=r*r
    q=polynomial(c,x)
    p=r*polynomial([2*(n+1)*c[n+1] for n in range(K)],x)
    # Cauchy coefficients |c_n|<=2.31/(.1)^(2n).
    # rho=r/.1 < .101; deliberately rounded-up coarse bound.
    eq=1e-39; ep=1e-35
    # K=20 omitted q begins degree42: 2.31*.101^42/(1-.101^2)<1e-39.
    # derivative tail <= (2.31/.1)*sum_{n>=21}2n*.101^(2n-1)<1e-35.
    return 1/128,[q+I(-eq,eq),p+I(-ep,ep)]
def jets(r,y,N):
    inv=[I(1)/r]
    for n in range(N): inv.append(-inv[-1]/r)
    q=[y[0]];p=[y[1]]
    sq=[]
    for n in range(N):
        sq.append(sum((q[j]*q[n-j] for j in range(n+1)),I(0)))
        cubic=sum((sq[j]*q[n-j] for j in range(n+1)),I(0))
        pr=sum((p[j]*inv[n-j] for j in range(n+1)),I(0))
        q.append(p[n]/(n+1))
        p.append((q[n]-cubic-pr)/(n+1))
    return [q,p]
def tube(r,y,h):
    rt=I(r,up(r+h));t=I(0,h)
    f=[y[1],y[0]-power(y[0],3)-y[1]/rt]
    Y=[]
    for yi,fi in zip(y,f):
        z=hull(yi,yi+t*fi);d=up(max(z.hi-z.lo,1e-15))
        Y.append(z+I(-d*.125,d*.125))
    for _ in range(12):
        f=[Y[1],Y[0]-power(Y[0],3)-Y[1]/rt]
        Z=[yi+t*fi for yi,fi in zip(y,f)]
        if all(subset(z,b) for z,b in zip(Z,Y)): return Y
        Y=[hull(b,z)+I(-up((z.hi-z.lo)*.125+1e-16),up((z.hi-z.lo)*.125+1e-16)) for b,z in zip(Y,Z)]
    raise RuntimeError('Picard tube failed')
def step(r,y,h,N=16):
    Y=tube(r,y,h)
    c=jets(I(r),y,N-1)
    rem=jets(I(r,up(r+h)),Y,N)
    out=[polynomial(cj,I(h))+rj[N]*power(I(h),N) for cj,rj in zip(c,rem)]
    return out,Y
def shoot(a,b=None,R=16,hmax=.025,check_envelope=False):
    r,y=origin(I(a,b));n=0; record=[];worst=0;positive=True;negative_derivative=True
    while r<R:
        h=2.**math.floor(math.log2(min(hmax,r*.125,R-r)))
        # A dyadic mesh with these small numerators adds exactly in binary64.
        end=r+h
        assert end-r==h and r<end
        assert (r*1024).is_integer() and (h*1024).is_integer() and end<=16
        yn,Y=step(r,y,h)
        positive=positive and Y[0].lo>0
        negative_derivative=negative_derivative and Y[1].hi<0
        if check_envelope:
            # Verify Q^2(1+r^2)^2 <6 on entire interval using Picard tube.
            ratio=power(Y[0],2)*power(I(1)+power(I(r,end),2),2)
            worst=max(worst,ratio.hi)
            if ratio.hi>=6: return {'status':'envelope failed','r':r,'Y':repr(Y),'ratio':repr(ratio)}
        r=end;y=yn;n+=1
        if n%100==0: record.append([r,y[0].lo,y[0].hi,y[1].lo,y[1].hi])
        if y[0].hi<0: return {'status':'overshoot','r':r,'q':repr(y[0]),'p':repr(y[1]),'steps':n,'negative_derivative_throughout':negative_derivative,'record':record}
        if y[0].lo>0 and y[1].lo>0: return {'status':'undershoot','r':r,'q':repr(y[0]),'p':repr(y[1]),'steps':n,'positive_throughout':positive,'record':record}
        if y[0].hi-y[0].lo>.1: return {'status':'width failed','r':r,'q':repr(y[0]),'steps':n,'record':record}
    return {'status':'reached','r':r,'q':repr(y[0]),'p':repr(y[1]),'steps':n,'worst_envelope_coefficient':worst,'record':record}
def certify():
    from fractions import Fraction as F
    aL=2.20620086;aU=2.20620087
    z={
       'arithmetic':'binary64 outward intervals; exact dyadic input endpoints',
       'order':16,
       'a_lower_dyadic':aL.as_integer_ratio(),
       'a_upper_dyadic':aU.as_integer_ratio(),
       'lower_shot':shoot(aL,R=16,hmax=.02),
       'upper_shot':shoot(aU,R=16,hmax=.02),
       'whole_bracket':shoot(aL,aU,R=6,hmax=.02,check_envelope=True)}
    assert z['lower_shot']['status']=='undershoot' and z['lower_shot']['positive_throughout']
    assert z['upper_shot']['status']=='overshoot' and z['upper_shot']['negative_derivative_throughout']
    assert z['whole_bracket']['status']=='reached'
    assert z['whole_bracket']['worst_envelope_coefficient']<6
    # Exact rational check of the Cauchy tail bounds used by origin().
    rho=F(101,1000);M=F(231,100);R=F(1,10);K=20
    qtail=M*rho**(2*K+2)/(1-rho*rho)
    ptail=M/R*(2*(K+1)*rho**(2*K+1)/(1-rho*rho)+2*rho**(2*K+3)/(1-rho*rho)**2)
    assert qtail<F(1,10**39) and ptail<F(1,10**35)
    # Analytic-ball mapping and contraction; no transcendental numerics.
    assert R*R*(M+M**3)/4 < F(1,10)
    assert R*R*(1+3*M*M)/4 < 1
    assert M*M*(1+F(1,16384))**2<6
    # The endpoint itself is parsed back as a dyadic rational from the
    # round-trip float representation; I.__repr__ prints 17 significant digits.
    q6hi=float(z['whole_bracket']['q'][1:-1].split(',')[1])
    assert F(q6hi)<F(1,200)
    assert F(37,200)**2<6
    z['certificate_passed']=True
    return z
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=float,default=2.20620086);ap.add_argument('--b',type=float);ap.add_argument('--R',type=float,default=16);ap.add_argument('--h',type=float,default=.025);ap.add_argument('--envelope',action='store_true');ap.add_argument('--certificate',action='store_true');args=ap.parse_args()
    t=time.time();z=certify() if args.certificate else shoot(args.a,args.b,args.R,args.h,args.envelope);z['runtime']=time.time()-t
    print(json.dumps(z,indent=2))
