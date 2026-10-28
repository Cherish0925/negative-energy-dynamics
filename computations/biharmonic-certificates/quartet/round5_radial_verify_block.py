"""Arb certificate of rational radial block forms and H2 residuals.
This is a trial-space certificate; final spectral transfer is separate.
"""
import json,math,time,sys,hashlib
from pathlib import Path
from fractions import Fraction as F
from flint import arb,arb_poly,arb_mat,ctx
from round2_verify_frozen_ritz import load_jets,hermite,parse_hex_rational
ctx.prec=384
ROOT=Path(__file__).resolve().parent
level=int(sys.argv[1]) if len(sys.argv)>1 else 4
assert hashlib.sha256((ROOT/'round2_radial_H4_exact_h1_16.json').read_bytes()).hexdigest()=='c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627'
raw=json.loads((ROOT/f'round5_radial_block_exact_h{level}.json').read_text());tn=[F(*v) for v in raw['nodes']];tj=[[[parse_hex_rational(v) for v in row] for row in arr] for arr in raw['jets_hex']]
qn,qj=load_jets(ROOT/'round2_radial_H4_exact_h1_16.json')
assert len(tj)==7 and tn[0]==0 and all(b>a for a,b in zip(tn,tn[1:]))
assert all(len(arr)==len(tn) and all(len(row)==6 for row in arr) for arr in tj)
assert all(arr[0][k]==0 for arr in tj for k in (1,3,5))
assert all(v==0 for arr in tj for v in arr[-1])
assert qn[0]==0 and qj[0][1]==qj[0][3]==0 and all(v==0 for v in qj[-1])
def A(x):
 x=F(x);return arb(x.numerator)/x.denominator

def hermn(left,right,h):
 m=len(left);mat=arb_mat([[math.factorial(k)//math.factorial(k-j) for k in range(m,2*m)] for j in range(m)])
 low=[A(left[j])*A(h)**j/math.factorial(j) for j in range(m)]
 rhs=arb_mat([[A(right[j])*A(h)**j-sum(low[k]*(math.factorial(k)//math.factorial(k-j)) for k in range(j,m))] for j in range(m)])
 hi=mat.solve(rhs)
 return arb_poly(low+[hi[j,0] for j in range(m)])

def integral(p):return sum((v/(j+1) for j,v in enumerate(p.coeffs())),arb(0))
def diff(p,h,k=1):
 for i in range(k):p=p.derivative()*(1/A(h))
 return p

def lap0(p,h):
 return arb_poly([p[k]*k*(k+2)/A(h)**2 for k in range(2,len(p))])
def bih0(p,h):
 return arb_poly([p[k]*k*k*(k+2)*(k-2)/A(h)**4 for k in range(4,len(p))])
def tri0(p,h):
 return arb_poly([p[k]*k*k*(k+2)*(k-2)*(k-2)*(k-4)/A(h)**6 for k in range(6,len(p))])
def bernsup(p):
 n=len(p)-1
 if n<0:return arb(0)
 best=arb(0)
 for j in range(n+1):
  bb=sum((p[k]*arb(math.comb(j,k))/math.comb(n,k) for k in range(j+1)),arb(0))
  best=best.max(abs(bb))
 return best.upper()
sups=[[[arb(0) for k in range(6)] for aa in range(2)] for j in range(7)]
# Freeze whitening as exact dyadic numbers (taken only as a choice of basis).
cf=ROOT/'round5_radial_block_whitening.json'
assert cf.is_file(), 'Frozen whitening input is required.'
C=[[A(parse_hex_rational(x)) for x in row] for row in json.loads(cf.read_text())]
al,be=[A(parse_hex_rational(v)) for v in raw['lambda_hex']]
B=[[arb(0) for j in range(7)] for i in range(7)]
B[0][0]=B[1][1]=al;B[0][1]=be;B[1][0]=-be;B[2][2]=B[3][3]=-al;B[2][3]=-be;B[3][2]=be;B[4][5]=arb(1);B[5][6]=arb(-1)
zero=arb_poly([0]);qpol=[arb_poly([A(v) for v in hermite(qj[i],qj[i+1],qn[i+1]-qn[i])]) for i in range(len(qn)-1)]
tpol=[[hermn(arr[i],arr[i+1],tn[i+1]-tn[i]) for i in range(len(tn)-1)] for arr in tj]
nodes=sorted(set(tn+qn));G=[[arb(0) for _ in range(8)] for _ in range(8)];Z=[[arb(0) for _ in range(8)] for _ in range(8)];res2=[arb(0) for _ in range(7)];respart=[arb(0),arb(0)];Kmat=[[arb(0) for _ in range(7)] for _ in range(7)];LW2=arb(0);t0=time.time();qi=ti=0;worst=[0,-1]
for ix,(r,b) in enumerate(zip(nodes,nodes[1:])):
 h=b-r;hh=A(h);rr=arb_poly([A(r),hh]);rp=[rr**k for k in range(8)]
 while qi+1<len(qn) and r>=qn[qi+1]:qi+=1
 while ti+1<len(tn) and r>=tn[ti+1]:ti+=1
 q=qpol[qi](arb_poly([A((r-qn[qi])/(qn[qi+1]-qn[qi])),A(h/(qn[qi+1]-qn[qi]))])) if qi<len(qpol) else zero
 vals=[p[ti](arb_poly([A((r-tn[ti])/(tn[ti+1]-tn[ti])),A(h/(tn[ti+1]-tn[ti]))])) for p in tpol]
 ar,ai,br,bi,f,z,he=vals
 V=[[ar,br],[ai,bi],[ar,-br],[ai,-bi],[f,zero],[zero,z],[he,zero],[zero,q]]
 d1=[[diff(v,h) for v in row] for row in V];d2=[[diff(v,h,2) for v in row] for row in V]
 ln=[[rr*d2[j][k]+3*d1[j][k] for k in range(2)] for j in range(8)]
 for j in range(8):
  for k in range(j,8):
   zz=hh*integral(sum((ln[j][a]*ln[k][a]*rr+V[j][a]*V[k][a]*rp[3] for a in range(2)),zero))
   gg=zz-hh*integral(q*q*rp[3]*(3*V[j][0]*V[k][0]+V[j][1]*V[k][1]))
   Z[j][k]+=zz;G[j][k]+=gg
 for j in range(7):
  for aa in range(2):
   uu=sum((V[k][aa]*C[k][j] for k in range(7)),zero);gg=2*q*uu
   for off,pp in [(0,uu),(3,gg)]:
    pd=diff(pp,h);pl=lap0(pp,h) if not r else rr*diff(pp,h,2)+3*pd
    bb=[bernsup(pp),bernsup(pd),bernsup(pl)/(A(r) if r else 1)]
    for kk in range(3):sups[j][aa][off+kk]=sups[j][aa][off+kk].max(bb[kk])
 # Exact Hamiltonian compressed matrix: Kij=<L vi,J L vj>.
 HV=[]
 for j in range(7):
  pair=[]
  for aa in range(2):
   u=V[j][aa];cc=3 if aa==0 else 1
   if r==0:hhv=bih0(u,h)+(1-cc*q*q)*u
   else:hhv=rp[3]*diff(u,h,4)+6*rp[2]*diff(u,h,3)+3*rr*diff(u,h,2)-3*diff(u,h)+rp[3]*(1-cc*q*q)*u
   pair.append(hhv)
  HV.append(pair)
 # A rigorous polynomial expansion of r^-3 about each cell midpoint.
 if r:
  assert h/(2*r+h)<=F(1,3)
  mid=A(r+h/2);rat=hh/(2*mid);assert rat*43/41<1
  tt=arb_poly([-arb(1)/2,1]);invweight=zero
  for nn in range(40):invweight+=((-1)**nn*math.comb(nn+2,2)*(hh/mid)**nn/mid**3)*(tt**nn)
  tail=math.comb(42,2)*rat**40/mid**3/(1-rat*43/41)
  def weightint(poly):
   sup=sum((abs(v) for v in poly.coeffs()),arb(0))
   return hh*(integral(poly*invweight)+arb(0,tail*sup))
 else:
  def weightint(poly):return hh*integral(poly*rp[3])
 for j in range(7):
  for k in range(j+1,7):Kmat[j][k]+=weightint(HV[j][0]*HV[k][1]-HV[j][1]*HV[k][0])
 for j in range(7):
  for aa in range(2):
   vv=sum((HV[k][aa]*C[k][j] for k in range(7)),zero);LW2+=weightint(vv*vv)
 # Construct numerator r^3 residual and r^5 Laplacian-residual.
 R=[];LR=[];q2=q*q
 for j in range(7):
  pair=[];lpair=[]
  for a in range(2):
   u=V[j][1-a];coef=1 if a==0 else 3;sgn=1 if a==0 else -1
   vu=(1-coef*q2)*u
   rhs=sum((V[k][a]*B[k][j] for k in range(7)),zero)+(q if j==4 and a==1 else zero)
   if r==0:
    # All trial odd jets 1,3,5 and q odd jets1,3 vanish exactly.
    rr0=sgn*(bih0(u,h)+vu)-rhs
    ll0=sgn*(tri0(u,h)+lap0(vu,h))-lap0(rhs,h)
    pair.append(rr0);lpair.append(ll0)
   else:
    ud=[u]+[diff(u,h,k) for k in range(1,7)]
    bi=rp[3]*ud[4]+6*rp[2]*ud[3]+3*rr*ud[2]-3*ud[1]
    tr=rp[5]*ud[6]+9*rp[4]*ud[5]+9*rp[3]*ud[4]-12*rp[2]*ud[3]+9*rr*ud[2]-9*ud[1]
    pair.append(sgn*(bi+rp[3]*vu)-rp[3]*rhs)
    lpair.append(sgn*(tr+rp[5]*diff(vu,h,2)+3*rp[4]*diff(vu,h))-rp[5]*diff(rhs,h,2)-3*rp[4]*diff(rhs,h))
  R.append(pair);LR.append(lpair)
 cell=arb(0)
 for j in range(7):
  for a in range(2):
   rrj=sum((R[k][a]*C[k][j] for k in range(7)),zero);lrj=sum((LR[k][a]*C[k][j] for k in range(7)),zero)
   if r==0:
    lo=hh*integral(rrj*rrj*rp[3]);hi=hh*integral(lrj*lrj*rp[3])
   else:
    lo=hh*integral(rrj*rrj)/A(r)**3;hi=hh*integral(lrj*lrj)/A(r)**7
   res2[j]+=lo+hi;cell+=lo+hi;respart[0]+=lo;respart[1]+=hi
 if float(cell.upper())>worst[0]:worst=[float(cell.upper()),ix]
 if ix%200==0:print('progress',ix,len(nodes),'res',sum(res2).sqrt().str(8),flush=True)
for j in range(8):
 for k in range(j):Z[j][k]=Z[k][j];G[j][k]=G[k][j]
Zm=arb_mat(Z);Gm=arb_mat(G);Cm=arb_mat(C)
# H2 orthogonal quotient against q (Q transfer is performed separately).
Z7=arb_mat([[Z[j][k]-Z[j][7]*Z[7][k]/Z[7][7] for k in range(7)] for j in range(7)])
GW=Cm.transpose()*arb_mat([row[:7] for row in G[:7]])*Cm;ZW=Cm.transpose()*Z7*Cm
Zraw=Cm.transpose()*arb_mat([row[:7] for row in Z[:7]])*Cm
rawtrace=sum((Zraw[j,j] for j in range(7)),arb(0))
B0=Cm.inv()*arb_mat(B)*Cm
for j in range(7):
 for k in range(j):Kmat[j][k]=-Kmat[k][j]
KW=Cm.transpose()*arb_mat(Kmat)*Cm
BC=GW.inv()*KW
Bdev=sum(((BC[i,j]-B0[i,j])**2 for i in range(7) for j in range(7)),arb(0)).sqrt().upper()
GI=GW.inv();ginv=sum((GI[i,j]**2 for i in range(7) for j in range(7)),arb(0)).sqrt().upper()
zdev=sum(((ZW[i,j]-(1 if i==j else 0))**2 for i in range(7) for j in range(7)),arb(0)).sqrt().upper()
# LDL without pivoting; nonzero pivots verify inertia for this explicit basis.
ldl=[[GW[i,j] for j in range(7)] for i in range(7)];piv=[]
for k in range(7):
 d=ldl[k][k];assert not d.contains(0);piv.append(d)
 for i in range(k+1,7):
  for j in range(i,7):ldl[j][i]=ldl[i][j]=ldl[i][j]-ldl[i][k]*ldl[k][j]/d
out={'status':'rigorous trial space only; exact-Q transfer and contour theorem required','precision_bits':ctx.prec,'profile_file':f'round5_radial_block_exact_h{level}.json','profile_sha256':hashlib.sha256((ROOT/f'round5_radial_block_exact_h{level}.json').read_bytes()).hexdigest(),'whitening_sha256':hashlib.sha256(cf.read_bytes()).hexdigest(),'lambda_hex':raw['lambda_hex'],'radial_measure':'r^3 dr; omitting common surface area leaves operator estimates unchanged','residual_frobenius_Z_upper':str(sum(res2).sqrt().upper()),'residual_columns_Z_upper':[str(v.sqrt().upper()) for v in res2],'residual_L2_upper':str(respart[0].sqrt().upper()),'residual_laplacian_L2_upper':str(respart[1].sqrt().upper()),'G_inverse_frobenius_upper':str(ginv),'q_Z_radial_squared':str(Z[7][7]),'raw_W_Z_frobenius_squared':str(rawtrace),'sup_U_Uprime_DeltaU_2qU_derivs':[[[str(v.upper()) for v in row] for row in col] for col in sups],'L_W_L2_frobenius_upper':str(LW2.sqrt().upper()),'compressed_B_minus_B0_frobenius_upper':str(Bdev),'BC':[[str(BC[i,j]) for j in range(7)] for i in range(7)],'quotient_Z_minus_identity_frobenius_upper':str(zdev),'LDL_pivots':[str(v) for v in piv],'negative_pivots':sum(bool(v<0) for v in piv),'GW':[[str(GW[i,j]) for j in range(7)] for i in range(7)],'B0':[[str(B0[i,j]) for j in range(7)] for i in range(7)],'ZW':[[str(ZW[i,j]) for j in range(7)] for i in range(7)],'G_phase_cross_upper':str(sum((G[j][7]**2 for j in range(8)),arb(0)).sqrt().upper()),'worst_cell':worst,'seconds':time.time()-t0}
fn=ROOT/f'round5_radial_block_certificate_h{level}.json';fn.write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ['GW','B0','ZW','BC']},indent=2))
