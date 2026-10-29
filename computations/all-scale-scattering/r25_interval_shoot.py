"""Validated Townes shooting with mpmath interval arithmetic.
Every ODE step uses Picard tube inclusion and interval Taylor remainder.
The only external theorem is existence/uniqueness and shooting characterization
of the positive decaying radial solution. No floating numerical Q is trusted.
"""
from mpmath import iv, mp
from pathlib import Path
import json, sys, time
iv.dps=60
mp.dps=60
I=iv.mpf

def ends(x):
    return mp.mpf(x._mpi_[0]),mp.mpf(x._mpi_[1])
def hull(a,b):
    return I([a,b])
def wid(x):
    a,b=ends(x);return b-a
def contained(x,y):
    a,b=ends(x);c,d=ends(y);return a>=c and b<=d

def jet(q,p,r,N):
    qj=[q];pj=[p];q2=[]
    ri=[1/r]
    for n in range(N):
        if n: ri.append(-ri[-1]/r)
        q2.append(sum((qj[j]*qj[n-j] for j in range(n+1)),I(0)))
        cube=sum((q2[j]*qj[n-j] for j in range(n+1)),I(0))
        rp=sum((ri[j]*pj[n-j] for j in range(n+1)),I(0))
        qj.append(pj[n]/(n+1));pj.append((qj[n]-cube-rp)/(n+1))
    return qj,pj

def initial(a,N=70):
    # Complex analytic fixed point on |t|<=1/100, |Q-a|<=1/10.
    # |a|<=2.21; Q bound2.31; rho*(2.31+2.31^3)/4<.1,
    # rho*(1+3*2.31^2)/4<1. Cauchy remainder at t=r0^2.
    r=I(1)/20;t=r*r;rho=I(1)/100;z=t/rho
    cs=[a];q2=[]
    for n in range(N-1):
        q2.append(sum((cs[j]*cs[n-j] for j in range(n+1)),I(0)))
        cube=sum((q2[j]*cs[n-j] for j in range(n+1)),I(0))
        cs.append((cs[n]-cube)/(4*(n+1)**2))
    q=sum((cs[n]*t**n for n in range(N)),I(0))
    p=2*r*sum((n*cs[n]*t**(n-1) for n in range(1,N)),I(0))
    eq=I('2.31')*z**N/(1-z)
    ep=2*r*I('2.31')/rho*(N*z**(N-1)/(1-z)+z**N/(1-z)**2)
    eqU=ends(eq)[1];epU=ends(ep)[1]
    return q+hull(-eqU,eqU),p+hull(-epU,epU)

def step(q,p,r,h,N=20):
    R=r+I([0,1])*h
    # Picard tube constructed with interval outward expansion.
    qm=max(abs(x) for x in ends(q));pm=max(abs(x) for x in ends(p));rm=ends(r)[0]
    dp=2*h*(qm+qm**3+pm/rm)+I('1e-50')
    dq=2*h*(pm+ends(dp)[1])
    for it in range(30):
        uq=ends(dq)[1];up=ends(dp)[1]
        Q=q+hull(-uq,uq);P=p+hull(-up,up)
        imageQ=q+I([0,1])*h*P
        imageP=p+I([0,1])*h*(Q-Q**3-P/R)
        if contained(imageQ,Q) and contained(imageP,P):break
        dq*=I('1.5');dp*=I('1.5')
    else: raise RuntimeError('tube inclusion failed')
    qj,pj=jet(q,p,r,N-1)
    qr,pr=jet(Q,P,R,N)
    qnew=sum((qj[n]*h**n for n in range(N)),I(0))+qr[N]*h**N
    pnew=sum((pj[n]*h**n for n in range(N)),I(0))+pr[N]*h**N
    return qnew,pnew,Q,P

def enc(x): return [mp.nstr(v,45) for v in ends(x)]
def raw(x): return [list(v) for v in x._mpi_]
def shoot(a,R='20',enclose=False,N=20):
    a=I(a.split(',')) if isinstance(a,str) and ',' in a else I(a);q,p=initial(a);r=I(1)/20;target=I(R)
    rows=[{'r':enc(r),'q':enc(q),'p':enc(p),'r_raw':raw(r),'q_raw':raw(q)}]
    count=0;status='target';all_positive_tubes=True
    while ends(r)[1]<ends(target)[0]:
        # exact rationals are enclosed, accumulated r widths retained
        h=min(I('0.01'),r/20,key=lambda x:ends(x)[1])
        if ends(r+h)[1]>ends(target)[0]:h=target-r
        q,p,Q,P=step(q,p,r,h,N);r+=h;count+=1
        all_positive_tubes=all_positive_tubes and ends(Q)[0]>0
        if enclose: rows.append({'r':enc(r),'q':enc(q),'p':enc(p),'tube_q':enc(Q),'r_raw':raw(r),'q_raw':raw(q)})
        if ends(q)[1]<0:status='overshoot';break
        if ends(p)[0]>0 and ends(q)[0]>0 and ends(q)[1]<1:
            assert all_positive_tubes, 'undershoot requires no earlier zero'
            status='undershoot';break
        if count%500==0:print('progress',count,float(ends(r)[0]),enc(q),flush=True)
        if count>5000: raise RuntimeError('too many steps')
    out={'a':enc(a),'r':enc(r),'q':enc(q),'p':enc(p),'steps':count,'status':status,'positive_on_all_step_tubes':all_positive_tubes,'a_raw':raw(a),'q_raw':raw(q),'p_raw':raw(p)}
    if enclose:out['rows']=rows
    print({k:v for k,v in out.items() if k!='rows'},flush=True)
    return out

if __name__=='__main__':
    if len(sys.argv)>1:
        out=shoot(sys.argv[1],sys.argv[2] if len(sys.argv)>2 else '20', '--enclose' in sys.argv)
        Path('r25_shoot_'+sys.argv[1].replace('.','_').replace('[','').replace(']','').replace(',','_')+'.json').write_text(json.dumps(out,indent=2)+'\n')
    else:
        out=[shoot(a) for a in ['2.2062008646507','2.2062008646508']]
        Path('r25_shoot_bracket.json').write_text(json.dumps(out,indent=2)+'\n')
