# N3 mass-critical BNLS: a rigorous energy-dual residual and infinite angular-tail certificate

Date: 2026-10-07. This is a completed intermediate certificate, not a proof of an N3 negative-energy traveling wave. The two missing finite-dimensional spectral tasks are identified below.

## 1. What was actually certified

Let Z be real H²(R³), with ||u||Z²=||Δu||₂²+||u||₂², and let

F(q)=Δ²q+q−|q|^(8/3)q.

The file `round4_n3_mixed_exact.json` defines two explicit compactly supported radial functions q and z using exact rational coefficients. Every stored hexadecimal IEEE value is interpreted as its exact rational value, not as an enclosure of an exact PDE solution. The functions use quintic Hermite polynomials between 16,626 rational nodes, except for an even sextic first cell. Values and first two derivatives match at every positive interior node; q=z=0 beyond r=54. Thus q,z∈H²(R³). No H4 regularity of the approximating spline is asserted or needed.

The independent verifier `round4_n3_verify_mixed.py`, using 192-bit Arb balls, proves

- ||q||Z < 137;
- ||q||∞ < 6.3;
- ||Δq−z||₂ < 3.057×10^−8;
- ||Δz+q−|q|^(8/3)q||₂ < 1.225×10^−7;
- ||F(q)||Z* < 1.3×10^−7.

The profile hash is `5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b`.

The last inequality is a whole-space, distributional PDE residual bound. It is not a collocation diagnostic, a sampled residual, or a finite-box residual.

## 2. Why the mixed formulation matters

The direct fourth derivative of a polynomial reconstructed from numerical values amplified tiny interpolation inconsistencies. Merely refining that reconstruction worsened the cancellation. The relevant Newton equation is in the energy space Z, so a strong L² residual of the fourth-order operator is unnecessary.

Set d1=Δq−z and d2=Δz+q−|q|^(8/3)q. In distributions,

F(q)=Δd1+d2.

For every test φ∈Z,

|<F(q),φ>| = |<d1,Δφ>+<d2,φ>|
≤ (||d1||₂²+||d2||₂²)^(1/2) ||φ||Z.

Therefore ||F(q)||Z*≤sqrt(||d1||₂²+||d2||₂²). The exact solution, if a Newton theorem produces it, then gains H4 regularity by elliptic regularity. The approximation itself need only lie in H².

This is a general residual certification method for fourth-order semilinear equations. The auxiliary field z keeps the proof at the derivative order controlled by the numerical approximation.

## 3. How the enclosure is obtained

For radial f in three dimensions, rΔf=rf''+2f'. Consequently

||d1||₂² =4π∫[rq''+2q'−rz]² dr,

||d2||₂² =4π∫[rz''+2z'+rq−r|q|^(8/3)q]² dr.

The first integrand is polynomial on each cell, hence integrated exactly up to rigorous Arb rounding. For the second, the verifier expands g(s)=sign(s)|s|^(11/3) to degree eight about the cell midpoint value when the polynomial q stays away from zero. The remainder is bounded using

|g^(9)(s)|/9! = |binom(11/3,9)| |s|^(11/3−9).

Cells that meet zero use the direct safe bound |g(q)|≤sup|q|^(11/3). No differentiability across q=0 beyond what the equation supplies is assumed. The final polynomial squared integral and Taylor remainder are combined by the L² triangle inequality on each cell. All outer cells, including the cutoff to zero, are included.

Quintic endpoint constraints are checked as exact rational equalities. The origin polynomial is even, so no hidden singular origin term occurs. Since both q and z are C1, no interface measure occurs in Δq or Δz. The identity F(q)=Δd1+d2 already includes all possible higher-order interface distributions.

## 4. A certified infinite family of angular gaps

For a spherical harmonic of degree ell let lambda=ell(ell+1), and write Δell f=f''+2f'/r−lambda f/r². On the natural radial form domain,

∫r²|Δell f|²dr
=∫r²|Δ0 f|²dr+2lambda∫|f'|²dr+lambda(lambda−2)∫r^(−2)|f|²dr.

This follows by integration by parts on smooth compactly supported channel functions and closure. In particular, for ell≥1 the last coefficient is nonnegative.

The verifier gives the uniform bounds

sup_r r⁴ (|q(r)|^(8/3)−4/5) < 22,305,

sup_r r⁴ ((11/3)|q(r)|^(8/3)−4/5) < 126,624.

Compare

(4/5)·13·14·(13·14−2)=26,208,

(4/5)·20·21·(20·21−2)=140,448.

It follows that the exact approximating-profile operators

L−(q)=Δ²+1−|q|^(8/3),

L+(q)=Δ²+1−(11/3)|q|^(8/3)

satisfy <L−f,f>≥(1/5)||f||Z² for every odd ell≥13, and <L+f,f>≥(1/5)||f||Z² for every even ell≥20. These are form inequalities on infinite-dimensional whole-space channels, not finite-matrix eigenvalue checks.

The gaps persist for every real radial Q with ||Q−q||Z≤1/1000. Indeed the exact Fourier embedding constant obeys

||h||∞ ≤ [4 sqrt(2) π]^(−1/2)||h||Z < (1/4)||h||Z.

Thus ||Q−q||∞≤1/4000. The larger of the two potential changes is bounded by

(11/3)(8/3)(6.3+1/4000)^(5/3)/4000 <0.052535<1/10.

Hence both indicated channel families retain gap at least 1/10 throughout that ball. This eliminates infinitely many angular obligations before the exact profile has been found.

## 5. A quantitative conditional existence reduction

The remaining standing-profile condition can now be expressed simply:

If L+(q) restricted to real radial Z is an isomorphism Z→Z* with inverse norm at most 25, then there is an exact real radial solution Q of F(Q)=0 with ||Q−q||Z<4×10^−6.

Proof. On the ball of radius rho=4×10^−6 around q, g'' is bounded by

G=(11/3)(8/3)(6.3+rho/4)^(5/3)<211.

The Newton remainder obeys ||N(h)||Z*≤(G/8)||h||Z², since ||h||∞≤||h||Z/4 and ||h||₂≤||h||Z. The fixed point T(h)=−L+(q)^−1(F(q)−N(h)) therefore satisfies

||T(h)||Z ≤25·1.3×10^−7 + (25·211/8)rho² <rho,

Lip(T) ≤(25·211/4)rho <0.006.

The Banach theorem proves the claim; elliptic regularity gives Q∈H4. This conditional implication is fully analytic. Its hypothesis has not been certified here. The existing approximate radial BS gap ~0.0432 suggests an inverse norm below25, but approximate eigenvalues do not prove the hypothesis.

## 6. Finite-block spectral certification suited to the near-one pair

Let K≥0 be a compact self-adjoint Hilbert–Schmidt operator, P a finite orthogonal projection, A=PKP, B=(1−P)KP, D=(1−P)K(1−P). Suppose certified bounds give

||K||HS²≤tau, ||A||HS²≥a2, ||B||≤eta.

Then ||D||≤sqrt(tau−a2)=:b, because the full HS decomposition is

||K||HS²=||A||HS²+2||B||HS²+||D||HS².

For a real target lambda>b, the Schur complement is A−lambda−B*(D−lambda)^−1 B. The correction has norm at most eta²/(lambda−b). Therefore lambda is outside the spectrum of K whenever

dist(lambda,spec A)>eta²/(lambda−b).

In particular, all lambda∈[1−delta,1+delta] are excluded if b<1−delta and

dist([1−delta,1+delta],spec A)>eta²/(1−delta−b).

This resolves a concrete methodological obstacle in the N3 degree-one channel: the subspace should include the eigenvector just below one (~0.98847), as well as the three above one. Merely subtracting the three above-one Ritz squares from a total HS bound leaves too much tail mass.

For illustration only, the following sufficient inputs are exact rational targets, not measured certificates: tau≤8.20; four Ritz eigenvalues in [2.117,2.119], [1.227,1.230], [1.006,1.008], [.987,.990]; eta≤.001. They imply b<.5 and exclude [0.995,1.005]. None of these finite-block spectral inputs has been interval-verified in this round.

## 7. What remains for an N3 counterexample

1. Certify the radial inverse norm at most25. The residual and nonlinear radius bounds above would then prove an exact profile.
2. Certify all remaining finitely many symmetry channels: even ell=0,2,...,18 for L+, and odd ell=1,3,...,11 for L−. The high channels are finished by Section4. A sharper certified finite channel could reduce this list by angular monotonicity, but no such reduction is counted here.
3. Certify the negative inverse pairing at the exact profile; numerical I≈−1323.39702629 remains numerical evidence until that step is done.

The completed work is a small certified PDE residual, an infinite family of spectral inequalities, and a precise finite-block reduction. It does not claim that the full N3 traveling-wave theorem is already proved.

## 8. Reproduction

Install python-flint==0.9.0, then run

    python3 round4_n3_verify_mixed.py 1

The frozen exact input and verifier suffice; NumPy, SciPy, the floating sampler, and the previous numerical BVP are not needed for verification. `round4_n3_make_mixed.py` is supplied only to explain data provenance. Earlier `round4_n3_profile_*` experiments use strong residual reconstructions and are not the final mixed certificate.
