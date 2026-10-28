"""Exact rational evaluation of canonical and preceding C3 septic radial profiles.
No numerical solver is used in these functions. Coefficients use t=(r-a)/(b-a).
"""
import json,math,bisect
from fractions import Fraction as F

def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for k,v in enumerate(a):c[k]+=v
 for k,v in enumerate(b):c[k]+=v
 return c

def scale(a,b):return [v*b for v in a]
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def deriv(a,k=1):
 for _ in range(k):a=[i*a[i] for i in range(1,len(a))]
 return a

def hermite(left,right,h):
 c=[left[0],h*left[1],h*h*left[2]/2,h**3*left[3]/6]
 A=right[0]-sum(c);B=h*right[1]-sum(i*c[i] for i in range(4));C=h*h*right[2]-sum(i*(i-1)*c[i] for i in range(4));D=h**3*right[3]-6*c[3]
 return c+[35*A-15*B+F(5,2)*C-D/6,-84*A+39*B-7*C+D/2,70*A-34*B+F(13,2)*C-D/2,-20*A+10*B-2*C+D/6]

def bernstein(c):
 n=len(c)-1
 return [sum(c[j]*F(math.comb(k,j),math.comb(n,j)) for j in range(k+1)) for k in range(n+1)]

def compose_affine(c,offset,slope):
 out=[F(0)]*len(c)
 for k,x in enumerate(c):
  for j in range(k+1):out[j]+=x*math.comb(k,j)*offset**(k-j)*slope**j
 return out

def load_profile(path):
 d=json.load(open(path))
 if 'nodes' in d:
  nodes=[F(*x) for x in d['nodes']];jets=[[F(float.fromhex(v)) for v in row] for row in d['jets_hex']]
 else:
  h=F(d['h']);jets=[[F(v) for v in row] for row in d['qjets']];nodes=[i*h for i in range(len(jets))]
 return nodes,[hermite(jets[j],jets[j+1],nodes[j+1]-nodes[j]) for j in range(len(nodes)-1)]

def on_interval(profile,a,b):
 nodes,polys=profile
 if a>=nodes[-1]:return [F(0)]
 j=bisect.bisect_right(nodes,a)-1;left=nodes[j];h=nodes[j+1]-left
 assert b<=nodes[j+1]
 return compose_affine(polys[j],(a-left)/h,(b-a)/h)
