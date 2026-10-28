# targeted two-dimensional rank-two variational search

2026-10-09. This is a numerical research record, not a proof of an optimal constant.

We tested whether

    C2 = sup [ integral (|phi_1|^2+|phi_2|^2)^2 / sum_j integral |grad phi_j|^2 ]

for two orthonormal functions exceeds the scalar value C1 = 2/Mc.
No above-scalar candidate was found.

## Discretization and search

The domain is (-12,12)^2 with homogeneous Dirichlet boundary conditions. Each component uses a sine spectral representation. Its kinetic energy uses the exact sine eigenvalues of -Delta. This avoids the constant-mode artifact of a periodic box. A two-column complex or real array X is mapped to Y=X(X*X)^(-1/2), so that the two functions have exactly unit discrete mass and are orthogonal to roundoff. The nonlinear integral is evaluated by collocation and checked by zero-padding the sine coefficients to a 320-by-320 grid.

We used analytic gradients and L-BFGS on all grid values, not only within the initial ansatz family. The objective is -F/K + 0.04 log(K/K_target)^2, with K_target=2 for pairs and 1 for the scalar check. The scale penalty prevents numerical grid concentration; it does not supply a proof of global optimization. Directional finite-difference checks of the implemented gradient had absolute discrepancies below 1.5e-10 in the refined runs. Gram residuals were below 1.4e-15.

Initial configurations included a scalar Gaussian, ground plus real dipole, ground plus complex vortex, radial ground plus excited profile, opposite-winding vortex pair, separated Gaussian wells, unequal anisotropic wells, and random nonradial perturbations. Runs used 80 and 160 points per direction. Promising 80-grid results were spectrally prolonged to 160 points, perturbed to break exact symmetry, and optimized for up to 1500 steps.

## Refined values

| Initial configuration | C evaluated on 320 grid | K | Status |
|---|---:|---:|---|
| Scalar calibration | 0.1709270734484682 | 1.00000050056 | L-BFGS converged |
| Separated wells | 0.17092698746138194 | 2.00006091830 | 1500-step limit |
| Ground plus real dipole | 0.17092696508475022 | 2.00016527406 | 1500-step limit |
| Unequal anisotropic wells | 0.17092687219193187 | 2.00007426475 | 1500-step limit |
| Ground plus complex vortex, perturbed | 0.16961201259292755 (160 grid) | 2.03417161455 | penalized-gradient tolerance reached |

The scalar calibration gives Mc = 11.7008965265. The best rank-two result lies 8.60e-8 below the scalar calibration. The 320-grid reevaluation changes the first four ratios by at most 6e-15. The best pair has about 5.33e-6 mass outside the square [-10,10]^2, so small boundary effects remain relevant to its final approach to the scalar level. The zero boundary trace means these finite-domain trial functions extend to admissible H1 functions on the full plane.

The unconstrained ground-plus-vortex run increased after a symmetry-breaking perturbation, from approximately 0.16452 on the initial coarse optimized grid to 0.16961. This agrees qualitatively with the need to leave a symmetry-restricted excited shell, but is not a certificate of either a local or global maximum.

## What this resolves

This run does not disprove or prove C2=C1. It supplies actual calibrated searches against the conjecture and shows that several overlapping, complex, anisotropic and separated candidates do not presently exceed the one-state level. The most successful candidates approach the separated-state boundary, rather than exhibiting a demonstrably better compact two-state structure. Absence of a candidate is not an upper bound.

Reproduction:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/r15_numerics_search.py 80 scalar dipole ground_vortex radial vortex two_well asymmetric
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/r15_numerics_search.py 160 scalar dipole ground_vortex radial vortex two_well asymmetric random

The script also supports init_path, perturb, steps, and tag arguments through its run() function. Raw outcomes are in r15_numerics_results_80.json, r15_numerics_results_160.json, r15_numerics_refined.json, and r15_numerics_fine_evaluation.json. Trial functions are saved as NPZ arrays.
