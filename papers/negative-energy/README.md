# Negative-Energy Global Solutions and Traveling-Wave Mass Gaps in Mass-Critical Dispersive Equations

Shuxing Yang

**质量临界色散方程中的负能量全局解与行波质量间隙**

[English abstract](abstract.md) · [中文摘要](abstract.zh-CN.md) · [Title and abstract source](title-and-abstract.tex) · [Detailed proof sequence](PROOFS.md) · [Repository overview](../../README.md)

## The central result

Negative energy does not determine the long-time behavior of a mass-critical dispersive wave. Excited-state phase response produces exact global coherent motion; optimizer phase coercivity prevents its traveling profiles from approaching the scalar critical mass. These two facts give the organizing structure of this work.

For the biharmonic equation

$$
i\partial_tu=\Delta^2u-|u|^{8/N}u,\qquad
M=\|u\|_2^2,\qquad
E=\frac12\|\Delta u\|_2^2-\frac1{2+8/N}\|u\|_{2+8/N}^{2+8/N},
$$

the three- and four-dimensional constructions give negative-energy traveling waves. In four dimensions, exact forward-global zero-momentum solutions are obtained from two separating waves and, subsequently, from one excited core with radiation. A uniform profile mass gap holds in every dimension:

$$
E(U)<0\quad\Longrightarrow\quad M(U)\ge M_c+\delta.
$$

Here $U$ solves the exact traveling-profile equation, and the gap is uniform in its frequency and speed.

![Excited wave and its phase response](../../figures/coherent-profiles.svg)

## One mechanism, two spectral regimes

The traveling branch comes from an excited real profile $Q$ with

$$
I=\langle\partial_1Q,L_-^{-1}\partial_1Q\rangle<0.
$$

Consequently $P_1(U_v)=2Iv+O(v^3)$ and $E(U_v)=Iv^2/4+O(v^4)$. The wave moves while retaining negative energy.

At the sharp mass, normalized near-optimizers converge to the optimizer family. After removing the phase direction, the optimizer phase form is coercive. The negative-energy profile identity would require that same form to be negative. This contradiction produces the mass gap without requiring radial symmetry, finite variance, optimizer uniqueness or real-sector nondegeneracy.

The construction and obstruction refer to different parts of the same constrained energy geometry.

![Radiation budget and profile exclusion interval](../../figures/radiation-and-gap.svg)

## Complete mathematical scope

The result identifiers below match [RESULTS.md](../../RESULTS.md). Each group links to its proof or manuscript.

| Development | Content | Proofs and manuscripts |
|---|---|---|
| Initial virial question · A00, A08 | Nonradial weighted-estimate obstructions, conditional collapse results and the exact comparison with Gou v3 Theorem 1.2 | [Initial manuscript](../../manuscripts/excited-waves/BNLS-Round1-20261007.pdf) · [Cylindrical comparison](../../manuscripts/cylindrical-comparison/BNLS-Cylindrical-Claim-Adjudication-20261007.pdf) |
| Exact excited waves · A01–A03 | N4 and N3 continuum constructions; specified dispersion and power continuations | [N4](../../manuscripts/biharmonic-certificates/BNLS-Nonradial-Research-20261007.pdf) · [N3](../../theory/zero-momentum/n3-full-theorem.md) · [Extensions](../../manuscripts/dispersion-extensions/BNLS-Extensions-20261007.pdf) |
| Dynamics and zero momentum · A04–A06 | Two-wave gluing, Morse counts, radial quartet, strong-stable nonstationary solutions and orbital instability | [Zero-momentum manuscript](../../manuscripts/biharmonic-certificates/BNLS-Zero-Momentum-and-Three-Dimensions-20261007.pdf) · [Final gluing proof](../../theory/zero-momentum/gluing-general.md) · [Radial quartet](../../theory/zero-momentum/radial-quartet.md) · [Stable manifold](../../theory/spectral-dynamics/stable-manifold.md) |
| Uniform gaps and dispersion structure · A07, A09–A11 | Biharmonic and homogeneous-symbol gaps, free-radiation cost, dilation assumptions and a small-perturbation counterexample | [Mass gap](../../manuscripts/profile-mass-gap/BNLS-Mass-Gap-and-Momentum-20261007.pdf) · [Homogeneous dispersion](../../manuscripts/homogeneous-dispersion/BNLS-Homogeneous-Dispersion-and-Dynamics-20261007.pdf) · [Dilation structure](../../manuscripts/dilation-structure/BNLS-Dilation-Structure-and-Profile-Gaps-20261008.pdf) |
| Threshold and constrained geometry · A12–A16 | Static concentration boundaries, least-profile-mass alternatives, action index, Hartree/vector extensions and global sublevels | [Threshold manuscript](../../manuscripts/critical-structures/BNLS-Thresholds-Spectral-Geometry-and-Radiation-20261008.pdf) · [Further critical structures](../../manuscripts/critical-structures/Critical-Focusing-Waves-Spectral-Bifurcation-and-Global-Dynamics-20261008.pdf) |
| Motion and transport · A17–A18 | Slow-wave constrained curvature, nonlinear departure, mass separation and averaged kinetic amplification | [Constrained dynamics](../../manuscripts/constrained-dynamics/Critical-Focusing-Dynamics-20261008-R12.pdf) · [Transport](../../manuscripts/transport-and-occupation/Critical-Focusing-Dynamics-20261008-R13.pdf) |
| Single core and quantitative obstruction · A19–A20 | Momentum-cancelling radiation with a sharp fixed-core mass infimum; moment-free profile residual linear in energy magnitude | [18 October manuscript](../../manuscripts/coherent-radiation/Negative-Energy-Coherent-Dynamics-Advances-20261018.pdf) · [Single-core proof](../../theory/coherent-radiation/wave-radiation.md) · [Residual proof](../../theory/coherent-radiation/robust-gap.md) |
| Mixed dispersion and endpoint geometry · A21–A23 | Intrinsic-energy gap and joint residual in the quadratic–quartic model; universal Fourier-moment energy/frequency/speed restrictions | [Mixed gap](../../theory/coherent-radiation/anisotropic-gap.md) · [Mixed residual](../../theory/coherent-radiation/robust-mixed-extension.md) · [Endpoint identities](../../theory/coherent-radiation/endpoint.md) |

## The three questions that remain

**General near-critical trajectories.** The profile obstruction does not classify recurrent or continually deforming solutions. The open problem concerns bounded negative-energy general trajectories near $M_c$.

**The least traveling-wave mass.** Compactification yields either a negative-energy strong minimizer or a finite zero-energy profile decomposition. The endpoint alternative is not yet selected.

**The mixed optical model.** The intrinsic-energy gap is proved for the specified quadratic–quartic equation. The [19 October continuation](../../theory/mixed-dispersion-continuation/README.md) has not constructed a negative intrinsic-energy traveling wave in that equation.

These questions identify the remaining mathematical scope; the construction and mass-gap results above already form a closed statement-and-proof sequence. The occupation-spectrum and collective-binding developments have their own equations and are linked through the [broader research narrative](../../RESEARCH.md).
