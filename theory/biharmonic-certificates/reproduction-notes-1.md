Exact N4 radial Hamiltonian quartet certificate

Run: python3 verify_quartet.py
Requires Python 3 and python-flint 0.9.0; no NumPy, SciPy or numerical ODE solver.

The proof is round5_radial_quartet.md. Its infinite-dimensional Schur theorem is
Section 7 of round5_radial_analytic.md. The final certificate establishes one
algebraically simple radial eigenvalue in 1.5<Re(lambda)<4.5, 4.5<Im(lambda)<7.5.
Hamiltonian symmetries give a radial quartet. The final Rouche bound is <0.365771.

This directory contains the complete NEW interval-verifier inputs. The prior
existence/full Morse proofs and original frozen certificates remain mathematical
dependencies; the encompassing package supplies them. Only the radial HS output
used by the new same-Q refinement is duplicated here.

The dyadic endpoint jets themselves define exact compact H6 trial functions.
Numerical candidate generation is not part of any verifier or existence claim.
