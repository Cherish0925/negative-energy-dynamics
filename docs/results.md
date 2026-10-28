# Complete first-class results and proof map

The common problem is global persistence of negative energy and its separation from the critical variational threshold. “Completed” below describes the result stated and argued in the archived research manuscripts, with their specified computational inputs. This consolidation preserves the evidence; it is not a new independent proof audit.

## Construction and mechanism

| Result | Scope and conclusion | Primary source package / location |
|---|---|---|
| Negative-energy traveling waves | Mass-critical biharmonic NLS in N=4; continuation of a certified excited standing wave; global for all real times with constant H² norm | `BNLS_Research_20261007`, `round2_notes/n4_negative_energy_traveling_wave_theorem.md`; N4 certificate |
| Three-dimensional construction | N=3, nonlinearity \(|u|^{8/3}u\); explicit certified range \(0<|v|\le10^{-9}\), \(E(U_v)<-180v^2\) | `BNLS_Zero_Momentum_Proof_and_Data_20261007`, `proof_notes/round5_n3_full_theorem.md`; `verification/N3/` |
| Zero-momentum two-wave dynamics | N=4, exact forward-global solutions; negative energy, uniformly bounded H¹⁰; finite variance at each finite time; separating wave cores | Same package, `round5_gluing_general.md` and main manuscript |
| One core plus radiation | N=4, exact forward-global, zero total momentum, negative energy, bounded H¹⁰; mass approaches the excited-state mass as speed tends to zero | `First_Class_Research_Advances_20261018`, `wave_radiation.md` and main manuscript Theorem 2.2 |
| Sharp radiation mass infimum for a fixed core | For core speed \(v>0\), momentum \(-q e_1\), \(\mu_{\rm crit}=q(4/v)^{1/3}\). Every strictly larger radiation mass is attainable in the specified asymptotic class. The endpoint cannot have negative total energy. | Same source; this is not the minimum mass of all bounded global solutions |
| Robustness of construction | Stated small perturbations, ellipsoidal principal quartic symbols, second-order dispersion matrices with frequency/scaling adjustment, and nearby nonlinear powers under the respective assumptions | `BNLS_Extensions_Proof_and_Data_20261007`, `BNLS_Extensions_20261007.tex` |

The N4 organizing identities, with the conventions of the original manuscript, are

\[
I=\langle\partial_1Q,L_-^{-1}\partial_1Q\rangle<0,\qquad
P_1(U_v)=2Iv+O(v^3),\qquad E(U_v)=Iv^2/4+O(v^4).
\]

Negative momentum response at the excited state provides the moving coherent mechanism. Momentum cancellation can be achieved by another wave or by radiation; zero total momentum alone does not remove this mechanism.

## Thresholds and variational structure

| Result | Scope and conclusion | Primary source |
|---|---|---|
| Uniform traveling-wave mass gap | For mass-critical biharmonic NLS in every dimension, \(E(U)<0\) implies \(M(U)\ge M_c+\delta\), uniformly in frequency and velocity | `BNLS_Mass_Gap_Proof_Source_20261007` |
| Homogeneous-dispersion gap | Real-even positive elliptic homogeneous symbol of order \(m>1\), with the regularity/multiplier hypotheses stated in the source; no optimizer uniqueness or real-part nondegeneracy | `BNLS_Homogeneous_Dispersion_Proof_Source_20261007`; later foundation sections |
| Quantitative profile obstruction | Near \(M_c\), after \(A(U)=1\) normalization, \(\inf_{\omega,v}\|R_{\omega,v}(U)\|_{H^{-m/2}}\ge c|E(U)|\). No spatial moment or extra dilation-defect assumption; the linear energy scale is optimal in the stated class. | `First_Class_Research_Advances_20261018`, `robust_gap.md`, independent review and main manuscript |
| Mixed-dispersion gap and residual estimate | Cubic model with one quadratic and two quartic directions. After removing quadratic-direction momentum, negative intrinsic energy implies a uniform mass gap, including every positive-semidefinite transverse quadratic correction. The joint residual version is uniform as well. | Same package, `anisotropic_gap.md`, `robust_mixed_extension.md` |
| Fixed-mass, fixed-momentum energy geometry | Exact positive factorization along the specified dilation-plus-phase curve; associated constrained negative directions and response/inertia refinements | `BNLS_Mass_Gap_Proof_Source_20261007`; `BNLS_Thresholds_Proof_Source_20261008` |
| Radiation variational problem | Exact infimum through the convex envelope of the dispersion symbol at prescribed mass and momentum; recovery by suitable radiation packets | `BNLS_Homogeneous_Dispersion_Proof_Source_20261007/round8_radiation_section.tex`; R10 symbol section |
| Minimum-wave-mass compactification | Alternatives: a strong negative-energy minimizer or a finite zero-energy profile collection at common parameters, with no diffuse remainder | `BNLS_Thresholds_Proof_Source_20261008/round10_threshold_section.tex`. Which alternative occurs is unresolved. |
| Generalized profile exclusions | Specified subhomogeneous positive corrections, defocusing terms, positive-definite Hartree interactions, and common-frequency multicomponent profiles | R9/R10/R11 source sections; retain each hypothesis |
| Scaling and concentration boundaries | Sharp-symbol and high-frequency bounds, bounded energy-sublevel boundaries, and superorder changes | `BNLS_Dilation_Structure_Proof_Source_20261008`; these are not by themselves dynamic blowup theorems |
| Fourier-moment restrictions | Explicit energy/frequency/velocity bounds, including \(E(U)>-\|\Delta U\|_2^2/16\) in the specified pure BNLS setting | Oct18 manuscript Appendix; moment-problem sharpness is not nonlinear-profile sharpness |

## Dynamics and spectral consequences

| Result | Scope and conclusion | Primary source |
|---|---|---|
| Certified excited-wave spectrum | N4 Morse counts \(n_-(L_+)=31\), \(n_-(L_-)=5\); certified radial quartet; for sufficiently small nonzero speed, stable and unstable dimensions exactly 31 | `BNLS_Dynamics_Proof_and_Data_20261007`; R5 `quartet/` and `round5_radial_quartet.md` |
| Instability and asymptotic families | Orbital/spectral instability and strong-stable families of nonstationary exact global trajectories under the stated spectral framework | R4 dynamics and stable-manifold notes; R5 refinements. No open basin of stable preparation is asserted. |
| Slow ground-wave curvature | For dispersion order greater than two, constrained negative curvature; spectral bifurcation and nonlinear exit laws require the additional hypotheses explicitly stated | `Critical_Focusing_Systems_Proofs_20261008`; R12 spectral and nonlinear-flow sections |
| Mass transport and spreading | Bounded negative-energy zero-momentum dynamics obey separation/transport restrictions; confinement forces kinetic growth | R5 `round5_analytic_dynamics.md`; R11 transport; R12/R13 dynamics sections |
| Averaged near-critical kinetic amplification | Actual-time averaged kinetic lower bounds with exponent \(1+m/[2(m-1)]\) in the general theorem; quartic refinements have additional nondegeneracy assumptions | `Critical_Focusing_Dynamics_Proofs_20261008_R13` |

## Scope of the collected source packages

R11–R13 were comprehensive snapshots containing both first-class profile/dynamical material and shared multicomponent foundations. They are preserved intact so their TeX dependencies and historical arguments remain reproducible. Occupation-spectrum/orthogonal GN results in those snapshots are contextual material, not additional first-class achievements. The later R23–R31 Lieb–Thirring project has not been imported into this repository.

The 19 October continuation package records attempts toward existence in the mixed optical model, including mesh-dependent false signals and the last reproducible stopping state. It is an exploration archive, not an existence certificate.
