# Final independent mathematical review

Reviewed: `BNLS_Mass_Gap_and_Momentum_20261007.tex`, 7 October 2026.

This is an independent internal proof check, not external peer review or a publication-priority determination. I independently reconstructed the principal identities and inequalities, then checked their implementation in the final manuscript. I found no blocking mathematical gap in the two stated theorems or the anisotropic corollary.

## Uniform traveling-profile mass gap

The proof applies to every dimension `N >= 1`, every real frequency and velocity, and every nonzero weak `H^2` traveling profile. Its conclusion is a qualitative positive mass gap above the sharp Gagliardo–Nirenberg mass for profiles of negative energy. It does not assert a corresponding gap for arbitrary bounded global solutions, nor existence of negative-energy traveling waves in every dimension.

The following potentially delicate points pass the check:

- **Weak-profile regularity.** For `N <= 8`, `H^2` directly embeds in the exponent needed to put the nonlinearity in `L^2`. For `N > 8`, the inverse of the positive shifted elliptic operator maps `L^s` to `W^{4,s}`. The manuscript correctly treats its nonlinear and linear inputs separately. The nonlinear reciprocal exponent improves by at least a positive amount until `q = 2(1+8/N)`, while the linear `L^2` input lies in `L^{2N/(N-8)}`; this latter exponent is strictly larger than the target. Every nonlinear input exponent is greater than one. Endpoints can be avoided by a small loss. The finite iteration yields `H^4` without weighted assumptions.
- **Profile identities.** The cutoff phase and cutoff dilation directions belong to `H^2` after this regularity step. Integration by parts leaves integrable unweighted tails. The signs and factors are consistent with the stated PDE and profile convention: `v·P = 8E`, `W = Mv/4`, `omega M = (4/N)A + (8-p)E`, and `E = <b,A_U b>/4`.
- **Complex optimizer rigidity.** Equality in Minkowski, the real-component sharp inequalities, and two-term Hölder gives proportional squared components. Applying the same argument after a rotation by `pi/4` excludes a varying relative sign. The optimizer therefore has a constant phase without radial symmetry, Fourier positivity, or uniqueness.
- **Phase kernel.** The nonnegative second-order pointwise remainder legitimately permits Fatou even when the second derivative has an infinite value on the zero set of `Q`. The manuscript's three interpretations for `r<1`, `r=1`, and `r>1` are correct. The upper bound for `D`, together with Cauchy–Schwarz, gives precisely `(C_1-AB/M)^2 <= 0`. Equality yields `b^2=(B/M)Q^2`; the mass identity excludes extra support on `Q=0`. Applying the same conclusion to the kernel vector `b+Q` then gives a constant multiple of `Q`. This proves the full phase-kernel statement, not merely pointwise modulus agreement.
- **Coercivity and compactness.** The potential is compact from `H^2` to `H^{-2}` by the strictly subcritical `L^p` embedding, local Rellich compactness and a small tail. Thus kernel simplicity gives `H^2` coercivity on the `L^2` orthogonal complement. Normalized near-optimizers are compact modulo translations by nonvanishing, Hilbert splitting, Brezis–Lieb and the strict mass splitting inequality.
- **Uniform quantifiers.** Strong convergence to one real optimizer is sufficient; neither a uniform coercivity constant across all optimizers nor real-part nondegeneracy is required. The frequency limit follows from the scalar identity, without estimating the velocity. The form perturbation uses the valid Hölder identity `2r/p + 2/p = 1`. After phase adjustment, positivity contradicts the exact imaginary-part energy identity. This establishes a gap uniform over all frequencies and velocities, though no numerical gap is supplied.

## Anisotropic extension

The corollary remains valid for each real positive elliptic homogeneous quartic polynomial `a(xi)`. A degree-four polynomial is even; its real kinetic form splits over real and imaginary components, is equivalent to the homogeneous `H^2` form, and has the required fourth-order scaling. Its shifted operator has the same elliptic multiplier regularity. The mass-gap argument needs the dilation identity and imaginary-part identity, both unchanged. It does not use the isotropic cubic-moment formula for the current. The gap may depend on the symbol; the manuscript correctly makes no uniform claim across all symbols.

## Fixed-momentum geometry

For the original isotropic dispersion, independent quartic Fourier expansion gives the stated factorization along the curve preserving `M` and `P`. Jensen gives `B >= 3m`, so negative energy makes all three coefficients strictly positive. The second derivative `2B-12E` and the momentum-neutralizing boost energy `B-3m/2-3E` agree with direct expansion. The strict minimum is on that particular curve, not on the entire constraint surface. The manuscript preserves this distinction and does not extend the exact isotropic factorization to arbitrary anisotropic symbols.

## Scope of this review

The radiation-budget inequality is a valid necessary condition under the stated asymptotic decoupling assumptions, and is not presented as a construction theorem. The manuscript separates the established profile theorem from the proposed dynamical threshold and further stability questions. The proof does not depend on the earlier numerical certificates. This review does not certify bibliographic priority or the correctness of those separate computational and multiwave constructions.
