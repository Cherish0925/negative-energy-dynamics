# Continuation toward the mixed optical model

[Research overview](../../README.md) · [Mixed-model theorem](../coherent-radiation/anisotropic-gap.md) · [Code and data](../../computations/mixed-dispersion-continuation/)

The target is the cubic, mass-critical equation

$$
i u_z=(-\partial_\tau^2+\Delta_\perp^2)u-|u|^2u.
$$

The computation starts from the previously constructed three-dimensional excited biharmonic profile and follows two different paths. It asks whether a negative response in a quartic direction survives to the target model, enabling a negative intrinsic-energy traveling wave. The saved runs do not reach that target.

![Mixed dispersion and the two continuation paths](../../figures/mixed-dispersion.svg)

## Auxiliary mixed path

The interpolating symbol and power are

$$
a_s(\xi,\eta)=(1-s)(\xi^2+|\eta|^2)^2+s(\xi^2+|\eta|^4),
\qquad \alpha_s=(8-2s)/3.
$$

Only the endpoints have the intended critical scaling. Finite-volume and independent DCT/Bessel discretizations give:

| Scheme | Parameter | Phase response $I$ | Recorded state |
|---|---:|---:|---|
| Finite volume, 128 × 128 | 0.975 | −45.809645 | [NPZ](../../computations/mixed-dispersion-continuation/core_continuation/run128/core_0.975000.npz) |
| Finite volume, 192 × 192 | 0.975 | +379.918221 | [NPZ](../../computations/mixed-dispersion-continuation/core_continuation/refine192/core_0.975000.npz) |
| DCT/Bessel, 256 × 128 | 0.980 | +435.723587 | [NPZ](../../computations/mixed-dispersion-continuation/core_continuation/spectral256/core_0.980000.npz) |
| DCT/Bessel, 256 × 128 | 0.990 | +28.345896 | [NPZ](../../computations/mixed-dispersion-continuation/core_continuation/spectral256/core_0.990000.npz) |
| DCT/Bessel, 256 × 128 | 0.991015625 | +40.959704 | [Final saved state](../../computations/mixed-dispersion-continuation/core_continuation/spectral256/core_0.991016.npz) |

At the same parameter $s=0.975$, refinement changes the sign. The coarse negative response therefore cannot establish the desired mechanism. The spectral endpoint remains an intermediate state with positive response. Negative energies along this auxiliary path do not establish negative intrinsic energy in the target equation.

## Mass-critical path

A separate path first removes the quartic cross term while keeping $\alpha=8/3$. The planned second stage lowers the temporal Fourier order $p$ from 4 to 2 with $\alpha=4p/(p+2)$.

The first stage reaches a fold near $s=0.6566$. Pseudo-arclength continuation passes the fold and follows the branch back to $s=0.1132$. This is finite-grid branch geometry. The second stage was not completed.

[Ordinary branch data](../../computations/mixed-dispersion-continuation/core_continuation/critical128/results.json) · [Arclength branch data](../../computations/mixed-dispersion-continuation/core_continuation/arc128/results.json)

## Programs

Run these commands from the repository root. Output goes to a new directory.

~~~sh
cd computations/mixed-dispersion-continuation
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python core_continuation/continue_core.py --n 128 --L 24 --out new_run
~~~

The independent spectral starting-state calculation is:

~~~sh
cd computations/mixed-dispersion-continuation
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python core_continuation/spectral_core.py --nt 256 --nr 128 --start 0 --end 0 --seed core_continuation/run128/core_0.000000.npz --out new_baseline
~~~

| Program | Role |
|---|---|
| [continue_core.py](../../computations/mixed-dispersion-continuation/core_continuation/continue_core.py) | Finite-volume auxiliary path |
| [critical_path.py](../../computations/mixed-dispersion-continuation/core_continuation/critical_path.py) | Critical path and cross-term removal |
| [arclength.py](../../computations/mixed-dispersion-continuation/core_continuation/arclength.py) | Finite-volume pseudo-arclength continuation |
| [spectral_core.py](../../computations/mixed-dispersion-continuation/core_continuation/spectral_core.py) | Independent DCT/Bessel discretization |
| [spectral_arclength.py](../../computations/mixed-dispersion-continuation/core_continuation/spectral_arclength.py) | Bordered spectral continuation |

The last spectral arclength run has no successful saved endpoint. The retained configs, JSON records and NPZ checkpoints define the completed computations. [The dated research account](Core-Continuation-State-20261019.md) records their numerical values.
