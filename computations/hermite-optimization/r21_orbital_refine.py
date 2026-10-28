import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from r21_orbital_search import *
base=json.load(open('research/r21_orbital_results.json'));results=[]
for N in [1,2,3,4,6]:
  rr=sorted([r for r in base if r['rank']==N],key=lambda r:-r['quotient'])
  chosen=rr[:1] if N<4 else rr[:1]+[r for r in rr if r['kind']=='multicore']
  for src in chosen:
    dat=np.load(src['coefficients']);C=dat['C'];tag='refine_'
    for cut in [28,40]:
      ix,_,_,_=basis(cut);A=np.zeros((len(ix),N),dtype=C.dtype);A[:len(C)]=C
      r,C=optimize(cut,N,src['kind'],21,1200,A,tag);results.append(r)
      with open('research/r21_orbital_refinement.json','w') as f:json.dump(results,f,indent=2)
