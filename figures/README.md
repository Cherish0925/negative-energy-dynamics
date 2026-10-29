# Research figures

[English overview](../README.md) · [中文总览](../README.zh-CN.md)

Each figure connects a physical mechanism to a mathematical statement or a saved computation. SVG files are embedded in the overview; PNG copies are supplied for slides and documents. The numerical arrays retain their original values.

| Figure | What is plotted | Inputs and interpretation |
|---|---|---|
| [Coherent profiles](coherent-profiles.svg) | Signed N4 radial seed; intensity and imaginary response of the moving state | [Radial NPZ](../computations/excited-waves/axial-profiles/round2_radial_mode1_dim4.npz), [moving NPZ](../computations/excited-waves/axial-profiles/round2_N4_axial_N512_L64_v0.02.npz). The axial solver stores $W(x,r)=rU(x,r)$; the plot divides by $r$ and uses the centered derivative on the axis. Continuum certificates are separate. |
| [Radiation and mass gap](radiation-and-gap.svg) | Exact normalized free-radiation cost; schematic excluded mass interval | [Radiation theorem](../theory/coherent-radiation/wave-radiation.md), [mass gap](../theory/profile-mass-gap/traveling-mass-gap.md). The gap has no assigned numerical width. The radiation cost is an infimum approached by narrow Fourier packets. |
| [Occupations and core](occupations-and-core.svg) | The 1D threshold law; scaled 2D Townes densities; normalized asymptotic scale laws | [Fixed occupations](../manuscripts/fixed-occupation/Fixed-Occupation-Thresholds.tex), [Townes NPZ](../computations/occupation-computations/r15_townes_profile.npz), [curvature theorem](../theory/background-interaction/modulation.md), [quintic interaction](../theory/background-interaction/quintic-closure.md). Density curves are spatial rescalings. The dashed quadratic rate is a candidate, not a constructed singular solution. |
| [Collective binding](collective-binding.svg) | Rank-two and rank-four densities; best recorded relative quotient gaps | [Summary](../computations/hermite-optimization/r21_orbital_summary.json) and the coefficient files named there. Normalized Hermite functions reconstruct the physical fields. Twenty of 61 runs reached the iteration limit. |
| [Spectral response](spectral-response.svg) | Response ratios at the finest saved resolution; two large-separation leading orders | [Calibration JSON](../computations/full-response/r31_response_calibration.json), [response identity](../theory/full-response/response-schur.md), [density-gradient obstruction](../theory/full-response/density-gradient.md). The asymptotic terms are divided by their different positive prefactors. |
| [Mixed dispersion](mixed-dispersion.svg) | Exact dispersion contours; response near the optical target; a fold on a separate critical path | The [continuation guide](../theory/mixed-dispersion-continuation/README.md) identifies paths, grids and source files. The $s$ axes in the last two panels refer to different paths. |

## Regeneration

From the repository root, with the environment in [COMPUTATIONS.md](../COMPUTATIONS.md):

    OPENBLAS_NUM_THREADS=1 python scripts/build_research_figures.py

The script reads recorded data and evaluates the displayed formulas. It writes the six SVG/PNG pairs and [sources.json](sources.json), without running the PDE searches or modifying their inputs. All plot definitions are in [build_research_figures.py](../scripts/build_research_figures.py).
