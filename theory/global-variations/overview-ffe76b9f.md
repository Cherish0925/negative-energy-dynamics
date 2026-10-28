# Full two-dimensional sharp Lieb–Thirring problem

16 October 2026.

Target: for every finite orthonormal family on R², prove

    integral (sum_j |phi_j|²)² <= (2/M_c) sum_j ||grad phi_j||²,

or construct a rigorously verified violating family. M_c is the mass of the
Townes solution -Delta Q+Q-Q³=0. This is equivalent to the fixed-occupation
collapse-threshold law M_*(p)=M_c/p_1 for all finite occupation spectra in the
two-dimensional common-density focusing system. It does not resolve the
fourth-order BNLS dynamics by itself.

## Result of this attempt

The full conjecture is not solved. No improving counterexample, improved
unrestricted constant, universal rank bound, or exclusion of all minimal
violating optimizers has been obtained.

The minimal-rank optimizer reduction is inherited from Frank–Gontier–Lewin,
not a new result. The R21/R23 compression, overlap, and occupied-frequency
bounds remain inherited project results and have not been counted again.

[finite-rank.md](finite-rank.md) gives an exact finite-amplitude occupied/unoccupied
rotation formula, independently checked algebraically. Its 2-by-2 matrix
condition is stronger than the infinitesimal test for the same pair. No proof
forces every hypothetical violating optimizer to fail that condition.

[global-instability.md](global-instability.md) carries local internal rotations and sphere
conformal variations through the full Gram correction. The uncorrected
negative trace does not establish a constrained negative direction. A bounded
rank-two angular test removes the fourth-moment restriction of the older
ratio-polynomial test, but its sign is not controlled in general.

[density-geometry.md](density-geometry.md) records a tensor-product bound inherited directly
from the known one-dimensional inequality and explicit counterexamples to
proposed orientation-cost shortcuts. These do not improve the unrestricted
constant. [rank-induction.md](rank-induction.md) records the unresolved integrated sign in
the radial deletion argument; no additional radial exclusion theorem is claimed.

These are calculations and failed proof routes retained for further work.
They are not a resolution or a claim of historical novelty.
