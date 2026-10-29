"""Several genuinely multiband and multiwell starts for the R28 search."""
import json
from pathlib import Path
import numpy as np
from r28_periodic_search import BlochProblem

out = []
for lattice in ["square", "triangular"]:
    problem = BlochProblem(6, 8, lattice)
    freqs = np.fft.fftfreq(problem.ngrid)*problem.ngrid
    kx, ky = np.meshgrid(freqs, freqs, indexing="ij")
    for norm in [12., 24., 48.]:
        for start in ["flat", "two_wells", "three_wells"]:
            hat = problem.initial(norm, width=.65, perturb=.04, seed=29)
            if start == "flat":
                hat *= .15
                hat[0, 0] += 1
            elif start == "two_wells":
                hat *= (1+np.exp(1j*np.pi*kx))/2
            else:
                hat *= (1+np.exp(2j*np.pi*(kx+ky)/3)+np.exp(4j*np.pi*(kx+ky)/3))/3
            hat *= np.sqrt(norm/(problem.area*np.sum(abs(hat)**2)))
            hat, info = problem.optimize(norm, steps=45, initial_hat=hat)
            info["start"] = start
            name=f"r28_periodic_multi_{lattice}_{start}_D{norm:g}.npz"
            np.savez(name, hat=hat, **info)
            out.append(info)
            print(json.dumps(info), flush=True)
Path("r28_periodic_multistart.json").write_text(json.dumps(out, indent=2)+"\n")
