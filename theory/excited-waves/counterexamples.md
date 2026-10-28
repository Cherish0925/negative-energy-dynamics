# Round 2 counterexample search: N>=2

## Outcome of this subtask

The initial N=2 searches did not find a negative response direction. The decisive lead came from the independently constructed N=4 excited radial profile: its negative response form was independently reproduced with a different, two-dimensional Fourier discretization, then continued to actual full complex traveling profiles. Their computed energies are negative and agree across several grids and domains.

For the complete numerical recipe, identities, units, endpoint assumptions, checks, and data map, see [N4-reproduction.md](N4-reproduction.md). The strongest snapshot is [round2_N4_axial_N384_L72_v0.02.npz](../../computations/excited-waves/axial-profiles/round2_N4_axial_N384_L72_v0.02.npz), with an independent `N512_L64` snapshot agreeing in direct energy to about 2e-12. These numerical files by themselves do not certify an exact R^4 solution.

Subsequent verification work produced [round2_verify_frozen_ritz.py](../../computations/excited-waves/axial-profiles/round2_verify_frozen_ritz.py): an independent standard-library-only verifier of the frozen canonical profile residual, its Z norm, and the exact Ritz lower inequalities. Its results are in [round2_verify_frozen_ritz_results.json](../../computations/excited-waves/axial-profiles/round2_verify_frozen_ritz_results.json). This verifies specified components; the complete nonlinear proof and its assembled inequalities are handled separately by the root research task.

## Completed N=2 experiments

- 79 distinct geometry seeds on 192x128 Fourier grids: alternating chains, checkerboard and striped rectangles, triangles and pentagons, alternating even rings, zigzags, and denser grids.
- 11 converged seeds produced full two-by-two response matrices. All had positive eigenvalues; the smallest was approximately 4.11909936. Repeated seeds may converge to the same profile and are not counted as distinct solutions.
- Complex vortices with charges m=1,2,3,4 were continued in the radial charge parameter and then refined in the full complex Fourier equation. The full real Hessian, projected away from phase/translation kernels, gave positive response eigenvalues approximately 6.2774, 10.5764, 15.3459, and 20.3948.
- Finite-velocity signed-chain, striped-grid and triangular branches were tested. The successfully followed branches retained positive energy. Failed Newton continuation steps do not establish that the corresponding branch ends or does not exist.
- Brief duplicate same-sign finite-velocity runs were superseded by the root task's finite-velocity study; the raw JSON log retains them for provenance rather than representing them as additional independent evidence.

Files: `round2_search.py`, `round2_dense.py`, `round2_vortex_continue.py`, `round2_travel_continue.py`, associated JSONL files and logs. The early vortex file obtained from piecewise linear radial interpolation was superseded by exact BVP evaluation and full complex refinement; the latter are the `round2_vortex_cont_*` outputs.

## N=4 independent verification

The exact axial transform W(x,r)=rQ(x,r), with transverse dimension three, turns the four-dimensional cubic profile equation into

(∂x²+∂r²)²W+W+i v∂xW−|W|²W/r²=0.

With odd extension in r, all original mass, momentum and energy integrals equal 2π times the appropriate two-dimensional W integrals. This is an exact reduction within O(3) transverse symmetry, not an approximation replacing four dimensions by two.

The independent Fourier inverse gave I approximately -273.47386191. Direct nonlinear branches at v=0.002,0.005,0.01,0.02 all had negative energy. At v=0.02:

- E approximately -0.02704284764;
- P approximately -10.81713905658;
- M approximately 5317.73876402;
- E-vP/8 near 10^-12 on the larger boxes;
- the independent third-moment identity vM=4J3 also agrees near 10^-12.

Analytically, a real localized standing wave multiplied by one linear phase cannot be an exact nonzero-speed BNLS traveling wave. Numerically, even the best such boost with optimized frequency has residual about 0.36544 and positive energy; the full complex candidate has residual about 3.56e-9 and negative energy. Thus the negative candidate is not merely an incorrect use of Galilean invariance.

The symmetry-restricted compact spectra have numerical gaps about 0.04261 (imaginary response operator) and 0.18512 (real operator). These initially guided, but do not replace, the later exact certificate calculations.

## Frozen-input verifier

Run:

```
python round2_verify_frozen_ritz.py
```

Its only data inputs are [round2_radial_H4_exact_h1_16.json](../../computations/excited-waves/axial-profiles/round2_radial_H4_exact_h1_16.json) and [round2_ritz_exact_data.json](../../computations/excited-waves/axial-profiles/round2_ritz_exact_data.json). Polynomial helpers come from [round2_radial_exact_common.py](../../computations/excited-waves/axial-profiles/round2_radial_exact_common.py). It reads no NPZ and calls no solver or numerical library. It parses hexadecimal jets directly into rational numbers and recomputes all stored A/M/V matrices from the frozen trial jets.

All of the following passed as exact rational comparisons:

- canonical residual norm less than 0.000242;
- canonical Z norm at most 104;
- l=0 top compact eigenvalue at least 5.395;
- l=0 second compact eigenvalue greater than 2.999;
- l=2 top compact eigenvalue greater than 2.11;
- l=1 top compact eigenvalue greater than 1.04;
- l=1 gamma=1/2 top quotient at least 1.5.

The output includes SHA256 hashes of both frozen inputs, the helper module, and the verifier itself. Time measurements are diagnostic only; no acceptance decision uses floating-point arithmetic.
