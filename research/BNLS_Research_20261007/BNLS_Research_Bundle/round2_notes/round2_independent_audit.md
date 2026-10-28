# Independent targeted audit of the N=4 traveling-wave certificate

Date: 7 October 2026. This is an internal independent mathematical and source-code audit by a collaborating agent. It is not external peer review.

**Result:** no unresolved mathematical error was found in the analytic conversion or the certified integral construction inspected below. Two implementation/reporting defects were identified in earlier scripts; both have been corrected in the final verification workflow. The actual five channel records inspected have their required Arb comparisons equal to `true`.

## 1. Analytic conversion checked

- For the equation `i u_t=Δ²u−|u|²u` in R⁴, the ansatz `u=e^{it}Q_v(x−vt e₁)` gives `Δ²Q_v+Q_v+iv∂₁Q_v−|Q_v|²Q_v=0`. The signs are consistent.
- The traveling action is `E+M/2−vP₁/2`. Mass-preserving dilation gives `4E−vP₁/2=0`, hence `E=vP₁/8`. A cutoff Pohozaev derivation needs no unproved finite-variance assumption; H⁴ regularity and the integrable energy densities suffice for the cutoff errors.
- The O(3)-invariant PT space `f(−s,y)=conjugate(f(s,y))` is preserved by the profile equation. Its real component has even angular degree, and its imaginary component has odd angular degree. The phase and translation kernels are excluded exactly as stated. The remaining accidental kernels are addressed by the spectral certificate rather than assumed away.
- The derivative of the branch is `Q'_0=−iL_-^{-1}∂₁Q`; differentiation of momentum gives `P₁'(0)=2I`. Conjugation relates opposite velocities, so `E(Q_v)=Iv²/4+O(v⁴)`. A strictly negative certified I therefore gives negative energy for every sufficiently small nonzero v.
- H²(R⁴) embeds into L⁶. A stationary H² solution thus has cubic nonlinearity in L² and belongs to H⁴ by elliptic inversion. The certified form inverse also yields the H⁴-to-L² inverse needed for the real-analytic implicit-function theorem. No unproved H²-to-L∞ embedding is used.
- The resulting exact translated profile is a global strong solution with constant finite H² norm. No stability assertion is needed. Since its momentum is nonzero at sufficiently small nonzero velocity, it cannot be radial about any spatial center.

## 2. Scalar and Ritz arithmetic checked

Files inspected: `round2_certificate_canonical.py`, its exact polynomial helper, `round2_ritz_exact.py`, the frozen canonical profile, and the resulting JSON records.

- Binary64 sample values are used only to define exact rational trial functions. Fraction arithmetic then decides all advertised scalar and Ritz inequalities. These trials need not themselves equal the unknown exact stationary solution.
- Shared derivatives through order three give C³ piecewise septic functions with compact zero extensions in H⁴. The origin conditions eliminate the singular residual terms. There is no omitted derivative-jump distribution in the fourth derivative.
- For `ψ(x)=x₁V(r)`, the full-space angular factor is `|S³|/4=π²/2`. The radial profile factor is `|S³|=2π²`. The response pair, kinetic term, potential term, residual and fourth-power norms use these factors consistently.
- The response residual is represented as `H_v=r³[q'/r−(D₆²+1−q²)V]`. Its squared norm has radial weight `H_v²/r`. The exact origin integral and the conservative non-origin bound in the code have the correct powers of the mesh length and radius.
- The Ritz transformation `f_l(r)r^lY_l` changes the effective radial dimension to `4+2l`. The kinetic and potential forms in the exact script match that transformation. The positive-definiteness test of `V−μA` on the two-dimensional radial trial space is a valid min–max lower bound for the second eigenvalue; exact orthogonality of the two trials is unnecessary.
- Machin's alternating-series π bounds have the correct directions, including the subtraction of the second arctangent. The required canonical scalar checks, including the response residual below 0.000662, are actually true in the inspected result.

## 3. Birman–Schwinger kernel and normalization checked

File inspected: `round2_certified_birman_hs.py`.

Let H_l be the positive second-order radial Laplacian in dimension four, ν=l+1, and κ=(1+i)/sqrt(2). Its whole-space resolvent kernel is

    (H_l+i)^(-1)(r,s)=(rs)^(-1)I_ν(κr_<)K_ν(κr_>).

The kernel of `(H_l²+1)^(-1)` is minus the imaginary part of this expression. The script has the correct sign and no missing factor of κ, π, or spherical area.

For the radial BS operator `β M_q(H_l²+1)^(-1)M_q`, the trace integrand is

    −β r q(r)² Im[I_ν(κr)K_ν(κr)].

The HS square is twice the lower-triangle integral. Expanding `(Im(IK))²` gives precisely the three F/B terms in the script, including the factor two in the mixed term and the outer factor `2β²`.

The nonzero eigenvalues coincide with those of `A^(-1/2)βq²A^(-1/2)`. Thus these trace/HS enclosures and the exact Ritz inequalities refer to the same spectrum.

## 4. Arb ODE and integration enclosures checked

The implementation evaluates the Bessel functions at a rigorously enclosed midpoint and encloses their cellwise variation through

    W=(f,rf'),  W'=[[0,1/r],[ν²/r+ir,0]]W.

The chosen matrix norm upper bound is conservative. Gronwall yields the two error radii used for f and rf'; division by the positive radius interval and the Bessel equation then enclose f' and f''. The midpoint derivative recurrences for both I and K have the correct signs.

For an interval of length h, the accumulated primitive at its midpoint is enclosed by

    J(a)+hF(mid)/2−h²F'(mid)/8 ± h³ sup|F''|/48.

The coefficient 1/48 is correct. For G=BJ, the script uses exactly `G''=B''J+2B'F+BF'`; the outer midpoint integration error `h³ sup|G''|/24` is correct. Signed mixed components are enclosed using full intervals, not treated as positive.

The Python–Flint constructor behavior was independently tested: uncertain Arb midpoint/radius arguments include both midpoint uncertainty and an outward upper bound for the supplied radius. The source expressions that decide bounds use Arb or Fraction arithmetic. The floating choice of a cell count does not affect validity: it only selects a finite exact rational partition, on which every cell enclosure remains rigorous.

## 5. Origin and infinite-domain treatment checked

The omitted origin strip is controlled by

    (H_l²+1)^(-1) <= (2H_l)^(-1).

The diagonal kernel of the latter is `1/(4νr²)`. Therefore the code's bounds

    trace_origin <= β ||q||∞² ε²/(8ν),
    trace_total <= β/(4ν) ∫r q(r)²dr

are correct. Positivity of the operator gives the kernel Cauchy inequality. Thus the omitted HS strip is at most twice the product of these trace bounds, exactly as implemented. This does not require the off-diagonal biharmonic Green kernel to be pointwise positive.

The frozen q is exactly zero after r=36, so no numerical tail of q is omitted. The unknown exact Q is not assumed compactly supported: its difference from q is handled globally by the H² form perturbation estimate.

The higher-angular-mode exclusion is also valid. On the common form core for l>=1,

    ||A_l f||²_(r³dr)
     =||A_0 f||²_(r³dr)+2λ_l∫r|f'|²+λ_l²∫r^(-1)|f|².

This yields monotonicity and a uniform gap on every remaining angular degree, not merely the five explicitly computed channels.

## 6. Concrete defects identified and resolved

1. An older residual generator used `Decimal.sqrt` while labeling its output an outward upper bound. Decimal square roots are rounded to nearest even, independently of the surrounding ceiling mode. The final frozen-profile verifier `round2_radial_canonical_residual.py` now asserts the squared residual against the exact decimal threshold and applies `next_plus` to the square root. The reported margin was much larger than one rounding unit.
2. An earlier final assertion in the canonical response script excluded the required 0.000662 residual predicate. The predicate was already true, and the current script asserts all predicates.
3. The HS records now include direct Arb comparisons against each actual target: 39, 4.80, 0.73, 1.70 for the trace, and 0.22. Their inspected values are all true in the relevant channels. Default abbreviated interval strings are deliberately coarser than the underlying Arb balls; the direct Arb comparisons are the controlling predicates. For reproducibility, the final aggregate verifier should bind these records to the frozen profile hash and assert the relevant channel predicates.

## 7. Overall conclusion of this audit

The mathematical chain from the frozen rational trials through the stationary fixed point, symmetry-sector invertibility, negative inverse pairing, analytic traveling branch, and global negative-energy solution is coherent. The targeted examination found no remaining sign, angular-normalization, origin-regularity, integration-error, or implicit-function-theorem gap. This conclusion concerns the inspected code and the actual certificate predicates, not merely agreement between floating-point numerical approximations.
