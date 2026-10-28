Numerical exploration only; not a certified counterexample. The requested N>=2 theorem remains unsolved. See counterexample_notes.md for complete limitations and results.

Dependencies: Python, NumPy, SciPy.
Run from THIS DIRECTORY so relative file paths resolve.
To rerun the strongest 1D cross-check using the supplied 14-pulse seed:
  OPENBLAS_NUM_THREADS=1 python travel_negative_verify.py
The supplied negative_travel_results.json contains the original measured result. Rerunning overwrites output files.
For N2 collinear and square-array probes:
  OPENBLAS_NUM_THREADS=1 python travel2d_probe.py
  OPENBLAS_NUM_THREADS=1 python travel2d_grid_probe.py

All source computations have finished; no background process remains.
