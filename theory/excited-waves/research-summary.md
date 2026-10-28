See round2_N4_reproduction.md for numerical evidence and its precise limits. The bundle contains representative high-resolution profiles, all numerical measurement logs, frozen exact Ritz/profile inputs, and a pure-rational verifier. All grids and other velocities can be regenerated from the supplied scripts and radial seed. Large numerical eigensolver eigenvector arrays are intentionally omitted: the eigensolver scripts recreate them in seconds. Numerical profiles alone do not certify the R4 counterexample. Exact theorem assembly is a separate deliverable.

Run the exact frozen-input component verifier with:
  python round2_verify_frozen_ritz.py
It requires only Python standard library and the included helper module.
Numerical reproduction additionally requires NumPy and SciPy.
