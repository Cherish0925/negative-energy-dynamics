# Extension of the dipole certificate to all required three-dimensional symmetry channels

This note records the generalization actually implemented in `round5_n3_channels_freeze.py` and `round5_n3_channels_verify.py`. All listed runs passed. The radial degree-zero proof and the Green-kernel HS bounds were produced separately by the N3 finite-channel task.

For a spherical harmonic Y_ell normalized in L²(S²), set

φ(x)=r^ell Y_ell(x/r) f(r),   D=2ell+3,

H(x)=r^ell Y_ell(x/r) h(r).

Then Δφ=r^ell Y_ell D_D f, where D_D f=f″+(D−1)f′/r. Thus the H² energy norm equals

∫₀∞ [(r^(ell+1)f″+(D−1)r^ell f′)²+(r^(ell+1)f)²] dr.

For K=A⁻¹β|q|^(8/3), β=11/3 in even real channels and β=1 in odd imaginary channels, an exact rational μ>0 and a mixed trial f,h satisfy

||Kφ−μφ||Z ≤ μ (||d₁||₂²+||d₂||₂²)^(1/2),

d₁=Δφ−H,

d₂=ΔH+φ−β|q|^(8/3)φ/μ.

After integrating angular variables, the first radial polynomial is

r^(ell+1)f″+(D−1)r^ell f′−r^(ell+1)h,

and the second is

r^(ell+1)h″+(D−1)r^ell h′+r^(ell+1)f−(β/μ)|q|^(8/3)r^(ell+1)f.

Both have nonnegative integer powers of r for ell≥1. The noninteger potential is treated by the same Taylor/remainder method used for the dipole certificate. A direct ball integral supplies a lower bound for ||φ||Z, so normalization is certified, not borrowed from a numerical eigenvector normalization.

The frozen functions are C² quintics on the canonical q mesh, with an even sextic origin cell and compact support ending at54. At the origin the auxiliary h jets for f=a₀+a₁r²+a₂r⁴+... are h(0)=2D a₁ and h″(0)=8(D+2)a₂. The generator constructs these values from the floating candidate and then freezes them as exact rationals. The verifier independently checks the polynomial endpoint constraints.

Each listed trial has certified relative BS residual smaller than0.001. The resulting disjoint intervals [μ_j−0.001,μ_j+0.001] each contain a distinct eigenvalue. If τ is the independent whole-space HS² bound, then all remaining eigenvalues are at most

b=[τ−Σ_j(μ_j−0.001)²]^(1/2).

The proof needs b<1, not exact orthogonality of trials. The gap at1 is bounded below by min_j(|μ_j−1|−0.001,1−b). The q→Q potential change is smaller than β·0.000058.

The following lower bounds are rounded downward from the successful exact-Q certificate outputs; each implies inverse norm<200.

| ell | operator | exact-Q gap exceeds | negative directions per angular harmonic |
|---:|:---|---:|---:|
| 1 | L− | .005 | 3 |
| 2 | L+ | .1045 | 4 |
| 3 | L− | .0405 | 1 |
| 4 | L+ | .1935 | 3 |
| 5 | L− | .0752 | 0 |
| 6 | L+ | .0997 | 3 |
| 8 | L+ | .1509 | 2 |
| 10 | L+ | .0851 | 1 |
| 12 | L+ | .2865 | 1 |
| 14 | L+ | .0643 | 1 |

The exact-Q ell0 L+ inverse norm<25 follows separately from the radial whole-space certificate. The even ell16 Green-kernel result gives HS²<.702, hence K norm<sqrt(.702) and strict positivity after the q→Q perturbation.

To cover infinitely many channels, write a physical radial amplitude a(r) times Y_ell, let λ=ell(ell+1), and use

∫r²|Δ_ell a|²dr = ∫r²|Δ_0 a|²dr
 +2λ∫|a′|²dr+λ(λ−2)∫r⁻²|a|²dr.

For ell≥1 this quadratic form is monotone in ell. Consequently positivity at ell5 for L− covers all odd ell≥5, and positivity at ell16 for L+ covers all even ell≥16. A positive relative energy gap propagates by the same identity: if L_ell≥αA_ell with α≤1, then L_j≥αA_j for j≥ell.

The real Banach symmetry space is X={u∈H²(C):u(−x)=conjugate(u(x))}. Its real part contains precisely even spherical harmonics, and its imaginary part precisely odd spherical harmonics. The certificates therefore supply a uniformly bounded direct-sum inverse on all of X; no unexamined angular channel remains. The phase and translation kernels lie outside the respective parity blocks.

The nonlinearity |u|^(8/3)u is continuously differentiable H²(R³)→L²(R³) because H² embeds in L∞; thus the ordinary real Banach implicit-function theorem applies to the small-velocity profile equation. The fully assembled existence and traveling-wave conclusion is documented by the main N3 proof. This file documents the finite-channel verification and infinite-angular closure, not a separate assumption about numerical spectral completeness.
