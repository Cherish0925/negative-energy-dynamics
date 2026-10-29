import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from r21_orbital_search import *
results=[]
for sd in [37,271,927]:
 for N in [2,3,4,6]:
  for kind in ['random','complex']:
   r,C=optimize(24,N,kind,sd,1000,tag='multiseed_');results.append(r)
   with open('r21_orbital_multiseed_results.json','w') as f:json.dump(results,f,indent=2)
