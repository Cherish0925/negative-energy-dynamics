"""Pure exact polynomial helpers. No input/output, solver calls, or regeneration.

All numbers are fractions.Fraction. Polynomials use increasing power order.
The pi enclosure follows Machin's identity and alternating-series bounds.
"""
from fractions import Fraction as F
from math import comb

def trim(a):
 a=list(a)
 while len(a)>1 and not a[-1]:a.pop()
 return a
def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return trim(c)
def scale(a,c):return trim([v*c for v in a])
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  if v:
   for j,w in enumerate(b):
    if w:c[i+j]+=v*w
 return trim(c)
def power(a,k):
 z=[F(1)]
 for _ in range(k):z=mul(z,a)
 return z
def derivative(a,k=1):
 for _ in range(k):a=[(i+1)*a[i+1] for i in range(len(a)-1)] or [F(0)]
 return trim(a)
def integ01(a):return sum((v/F(i+1) for i,v in enumerate(a)),F(0))
def bernstein_range(a):
 n=len(a)-1
 b=[sum((a[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)),F(0)) for k in range(n+1)]
 return min(b),max(b)

mat=[[F(v) for v in row] for row in [[1,1,1,1],[4,5,6,7],[12,20,30,42],[24,60,120,210]]]
aug=[row+[F(int(i==j)) for j in range(4)] for i,row in enumerate(mat)]
for k in range(4):
 piv=aug[k][k];aug[k]=[x/piv for x in aug[k]]
 for i in range(4):
  if i!=k:
   fac=aug[i][k];aug[i]=[x-fac*y for x,y in zip(aug[i],aug[k])]
inv=[row[4:] for row in aug]

def atan_bounds(x,n):
 s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
 nxt=x**(2*n+1)/F(2*n+1)
 return (s,s+nxt) if n%2==0 else (s-nxt,s)
a5,b5=atan_bounds(F(1,5),30)
a239,b239=atan_bounds(F(1,239),10)
pi_lo=16*a5-4*b239;pi_hi=16*b5-4*a239
assert F(3)<pi_lo<pi_hi<F(355,113)
ang_lo=pi_lo*pi_lo/2;ang_hi=pi_hi*pi_hi/2
def angular_bound(x):return (x*ang_lo,x*ang_hi) if x>=0 else (x*ang_hi,x*ang_lo)
