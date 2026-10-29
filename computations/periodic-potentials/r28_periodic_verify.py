"""Hold the best saved trial potential fixed and change numerical resolution."""
import json
from pathlib import Path
import numpy as np
from r28_periodic_search import BlochProblem, resize_hat

data = np.load("r28_periodic_square_refined_D48.npz")
rows=[]
for cutoff,nq in [(10,16),(12,10),(14,8)]:
    p=BlochProblem(cutoff,nq,"square")
    hat=resize_hat(data["hat"],p.ngrid)
    info,_=p.evaluate(hat)
    rows.append(info)
    print(json.dumps(info),flush=True)
Path("r28_periodic_verification.json").write_text(json.dumps(rows,indent=2)+"\n")
