# Whole-plane optimization of genuinely two-dimensional orthonormal orbitals

12 October 2026. This is an exploratory computation, not a proof of the sharp
Lieb--Thirring conjecture or a proof that collective binding cannot occur.
It produces no above-threshold candidate.

The functional is

$$
R(\Phi)=\frac{\int_{\mathbb R^2}(\sum_{j=1}^{N}|\phi_j|^2)^2}
 {\sum_{j=1}^{N}\int_{\mathbb R^2}|\nabla\phi_j|^2},\qquad
\langle\phi_i,\phi_j\rangle=\delta_{ij}.
$$

The scalar comparison is `C1 = 0.17092707344864` (the approximate value
`2/Mc` used in the existing project). This decimal is a comparison value,
not a new interval enclosure of the Townes mass.

## What was varied

Every orbital is an arbitrary linear combination of the two-dimensional
Hermite functions `h_a(x) h_b(y)` with `a+b <= d`. Coefficients are optimized
jointly; no separation of variables, radiality, prescribed density or fixed
angular sector is imposed. Both real and complex coefficients are tested.
The tensor-product basis does **not** restrict orbitals to product functions.

The coefficient matrix is normalized by its polar factor,
`C=A(A* A)^(-1/2)`, so its columns are orthonormal in the continuum. The
functional is invariant under right unitary rotations. Its analytic gradient
is projected horizontally and differentiated through this normalization.
Directional finite differences were independently checked for every run.

The kinetic matrix is the exact full-line Hermite kinetic matrix. The quartic
integral is a polynomial Gaussian integral: Gauss--Hermite order `2d+3`
in each coordinate integrates its polynomial degree exactly in exact
arithmetic. Floating-point operations are not interval-certified.
There is no periodic computational box, no free constant mode and no
collocation aliasing from an insufficient quartic quadrature order.

Seeds include filled low-energy shells with perturbations, general random
real and complex orbitals, and orthogonalized displaced Gaussian cores.
The search uses L-BFGS in normalized coordinates. This is a local optimizer,
not an exhaustive search and not a certified global maximization.

## Main observations

| Rank | Best at degree 16 | Continued to degree 28 | Continued to degree 40 |
|---:|---:|---:|---:|
| 1 (calibration) | 0.1709037296 | 0.1709261617 | 0.1709270130 |
| 2 | 0.1706370095 | 0.1709024929 | 0.1709244491 |
| 3 | 0.1704222495 | 0.1708884989 | 0.1709222223 |
| 4 | 0.1701251214 | 0.1708560653 | 0.1709172289 |
| 6 | 0.1695894463 | 0.1707583577 | 0.1708976823 |

The high values do not reveal a new strongly overlapping collective core.
The density develops N separated peaks. Increasing the Hermite degree lets
these peaks move farther apart while keeping approximately fixed core width.
This is the important qualitative outcome: the optimizer uses the added
freedom mainly to approach separated scalar cores.

For a gauge-invariant localization check, divide physical space into Voronoi
cells around the density peaks and compute each local Gram matrix
`G_cell = integral_cell Phi* Phi`. A rank-one matrix with leading eigenvalue
one means one occupied orbital is almost entirely localized in that cell,
after a unitary change of orbital basis.

| Rank | Mean leading local Gram eigenvalue, degree 16 | Degree 40 |
|---:|---:|---:|
| 2 | 0.9949064 | 0.9997107 |
| 3 | 0.9894333 | 0.9992094 |
| 4 | 0.9877757 | 0.9989635 |
| 6 | 0.9799491 | 0.9978756 |

The minimum peak separation in units `sqrt(N/T)` changes, respectively,
from `(4.48, 4.36, 4.35, 3.83)` to `(7.31, 6.94, 6.77, 5.92)`.
These two independent observations distinguish fragmentation from simply
an improved numerical value. They do not prove asymptotic fragmentation of
all maximizing sequences, nor rule out another basin of attraction containing
a collective maximizer.

Additional rank 8 and 12 runs at degree 24 reached approximately
`0.1702572034` and `0.1697223095`, below the target. Some high-rank runs reached
the iteration cap; their results must not be called fully stationary.
Multi-seed real and complex searches are recorded separately. In total, 61
optimizations were performed across ranks 1, 2, 3, 4, 6, 8 and 12, Hermite
degrees 16, 24, 28 and 40, and seeds 21, 37, 271, 314 and 927. The full
run summary is [r21_orbital_summary.json](../../computations/hermite-optimization/r21_orbital_summary.json). No run exceeded the scalar target.

## Independent evaluation

For the displayed degree 16 and 40 orbitals, physical Hermite functions and
their analytic first derivatives were evaluated on an independent uniform
501-by-501 grid in `[-13,13]^2`. The direct values of F, T and the Gram matrix
were integrated there. The quotient agrees with the Gaussian-quadrature
value to about `1e-14`; Gram errors are below `2e-13`. Estimated mass outside
radius 10 in that check is at most `1.8e-9` for the degree 40 examples.
A higher-order Gauss--Hermite re-evaluation also agrees.

This provides a useful numerical consistency check. It is not a rigorous
floating-point error bound. No counterexample is claimed.

The projected Euler--Lagrange multipliers recorded in the JSON are for the
finite Galerkin optimization. They are **not** certified multipliers of exact
stationary solutions of the continuum nonlinear PDE.

## Reproduction

```
cd computations/hermite-optimization  # from the repository root
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python r21_orbital_search.py --cut 16 --steps 650
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python r21_orbital_refine.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python r21_orbital_search.py --cut 24 --steps 1000 --ranks 8,12 --kinds shell,random,complex --seed 314 --output r21_orbital_high_rank_results.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python r21_orbital_multiseed.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python r21_orbital_inspect.py
```

Scripts, JSON results, all coefficient matrices and the density figure are
retained as `r21_orbital_*`. They are actual optimization outputs, not
illustrations invented from the expected answer.

## Scientific interpretation

The computation broadens the search beyond low-parameter prescribed
potentials and complete Cartesian-product occupation. It does not settle
the full problem. In the tested basins, an improvement toward the scalar
constant is explained by spatial dissociation, rather than collective
binding. A proof must control the competition between these organizations
without assuming that the solution already has the separated-core form.

## Relation to prior computations

Spatial dissociation is not a new mechanism discovered by this computation.
Antoine Levitt, *Best constants in Lieb–Thirring inequalities: a numerical
investigation*, Journal of Spectral Theory 4 (2014), 153–175, Section 4.2,
already reported slowly separating two-dimensional bumps. Figure 4 uses
gamma=1.2; Figure 6 shows eight bumps at gamma=1.1. His radial branch scan
also includes gamma=1. The present endpoint calculation reproduces the same
type of phenomenon with a different discretization; the cited figures are
not themselves computations at exactly gamma=1.
Primary source: https://ems.press/content/serial-article-files/33509

The later Frank–Gontier–Lewin theorem in *The nonlinear Schrödinger equation
for orthonormal functions: II. Application to Lieb–Thirring inequalities*
proves that in two dimensions the one-state constant is strictly suboptimal
for gamma>1. Their interaction construction shows why failure to find
binding numerically cannot establish its absence. This theorem does not
settle gamma=1, the endpoint studied here.
Primary source: https://arxiv.org/abs/2002.04964

Accordingly, no original fragmentation mechanism or resolution of the
endpoint conjecture is attributed to the 61 searches in this note.
