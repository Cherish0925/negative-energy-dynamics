# Independent checks of the refined N4 certificate and the transport endpoint

7 October 2026. This note records an independent derivation and actual rerun of the two N4 verification scripts, followed by a check of Sections 5.3–5.5 of round5_analytic_dynamics.md.

## 1. The unchanged canonical N4 profile

I read the complete files round5_n4_mixed_residual.py, round5_n4_refinement_certificate.py and round5_n4_refinement.md, including the imported exact hexadecimal parsing and Hermite interpolation routines. I then reran both scripts. Every required scalar check passed.

The auxiliary z is legitimate: its nodal jets are rational definitions, not assertions that q satisfies the stationary ODE. At the origin z'=z'''=0 and at the compact endpoint all four jets vanish. Common jets at internal nodes give C³ matching. These facts give radial whole-space H² regularity; the stronger H4 regularity available here is not necessary for the mixed estimate. The radial origin has no hidden singular distribution and the compact cutoff has no jump contribution to Δz.

With d1=Δq−z and d2=Δz+q−q³, the exact distributional identity is

    (Δ²+1)q−q³ = Δd1+d2.

Testing against h∈H² gives the bound

    |<Δd1+d2,h>|
       ≤ sqrt(||d1||₂²+||d2||₂²) sqrt(||Δh||₂²+||h||₂²).

No extra norm constant or sign correction is needed. In four radial dimensions, d1=(rq''+3q'−rz)/r, so the volume factor 2π²r³ gives precisely the integrand 2π²r(rq''+3q'−rz)². The same calculation applies to d2. The script integrates exact polynomials in the local variable over every frozen cell with 256-bit enclosing ball arithmetic; it does not use quadrature sampling as a bound.

The independently reproduced upper bounds are

    ||d1||₂ < 1.9206685514e−8,
    ||d2||₂ < 4.1805837651e−8,
    ||F(q)||Z* < 4.6006791131e−8 < 4.601e−8.

## 2. Inverse, Newton radius, and identity with the old profile

The frozen lower bounds μ1≥5.395, μ2>2.999 and the full radial Hilbert–Schmidt upper bound 38.80 imply

    μ3² < 38.80−5.395²−2.999² < .84².

Since K is positive compact, its first two eigenvalues are above one and all the rest below .84. Therefore the whole radial spectrum of I−K has distance strictly greater than .16 from zero. The inverse norm is strictly below 25/4. This is a full-space radial statement.

The nonlinear remainder is 3qh²+h³. Its derivative on the radius-ρ ball is bounded by (1/256)(6||q||Z ρ+3ρ²). The exact rational scalar inequalities in the verifier give invariance and contraction at ρ=3e−7. They also give contraction on the old radius-.006 ball. For identification of two fixed points, only the contraction inequality on that old ball is needed; the refined map need not be proved anew to map the entire old ball into itself. Thus the new fixed point and the previously certified real radial Q coincide.

The improved potential-transfer bound is consequently for the same Q:

    ||A^−1/2(Q²−q²)A^−1/2||
       ≤ (208ρ+ρ²)/256
       = 6240000009/25600000000000000.

No frozen input was replaced. The script still imports the prior exact Ritz inequalities; it does not independently regenerate those Ritz certificates, and its conclusion retains that explicit dependency.

## 3. Mass-transport endpoint

For iu_t=Δ²u−|u|^{8/N}u, the sign in the density identity is

    ρ_t=2 Im(bar u Δ²u).

Testing with a real bounded smooth f and integrating by parts gives

    ∫fρ_t = 2 Im∫(Δf)bar u Δu
             +4 Im∫∇f·(Δu∇bar u).

The nonlinear term is real and cancels exactly. Cauchy–Schwarz and ||∇u||₂≤M^{1/4}K^{1/2} give the absolute bound

    2||Δf||∞ M^{1/2}K
      +4||∇f||∞ M^{1/4}K^{3/2}.

The cutoff ψ((x−y)/R) is even in x−y, so differentiation of the two density factors gives twice the same term. This proves

    |F'_R|≤D(R^−1 K^{3/2}+R^−2K).

Hölder on the time segment yields the stated 1/4 and 1/2 time moduli using only ∫K². Replacing the segment integral by the full-window budget only enlarges the bound.

When R=c0T and |t−t0|≤ηT, the first term becomes D c0^−1 H0^{3/4}η^{1/4}, independent of T; the second is D c0^−2 H0^{1/2}η^{1/2}/T. Thus a fixed η>0 preserves at least half of an existing fixed separated mass fraction throughout a one-sided or two-sided interval of length ηT inside the window. This conclusion does not require any higher time moment or uniform integrability.

For the no-prior-bound version, R=a0T H_J^−1/4 changes the modulus to at most D0 H_J η^{1/4}. Choosing η=cη H_J^−4(1+1/θ) makes this at most half the required threshold (b0/H_J)^{1/θ}. The radius, time exponent, and escaped-mass exponent in Theorem 5.5 are consistent.

I found no gap in these endpoint deductions. Their dependency is the earlier interaction-virial inequality (3.1), whose proof is separate. The present checks do not assert an independent new literature-priority claim for these statements.

## 4. Weighted regularity and cylindrical symmetry of the gluing construction

I also checked Section 9 of round5_gluing_general.md. The projected position identity is correct. For Π=I−ZW and a center solution w, put z=Πx_jw and B=Π_t+ΠC−CΠ. Moving-center invariance gives BΠ=0, hence

    z_t−Cz=B(I−Π)x_jw+Π[x_j,C]w.

The source jointly lies in the center. Each raw hyperbolic coordinate of w vanishes separately because the finite Gram correction is invertible. Therefore the potentially large wave-center term in W x_jw cancels exactly:

    <ψ(·−c_k),x_jw>=<(x_j−c_{k,j})ψ(·−c_k),w>.

The right-hand dual functions have uniform Sobolev bounds. This controls the first source term without a factor growing like t. The free commutator has order three and is controlled from H10 to H6. Finite-rank projection commutators have the same cancellation within a core; cross-core coefficients are exponentially small, so their polynomial center differences remain bounded.

The unweighted H10 graph estimate and the projected H6 position equation consequently give the same arbitrarily small exponential rate in Y=H10∩{x_jh∈H6}, with enlarged polynomial time factors only. Initial and final center projections are uniformly bounded on Y by the commutator identity xΠ=Πx+[x,Π]. On the separated finite hyperbolic range, its Y norm is equivalent to (1+t)|a| for fixed nonzero v, so the additional transport ratio costs only a polynomial in |t−s|.

Every nonlinear remainder term contains at least two correction factors. In its position-weighted estimate the coordinate x_j can be put on a correction factor, never requiring a growing weighted norm of the background wave. Hence the Y contraction estimates have uniform nonlinear constants. The interaction defect remains exponentially small in Y after a slight reduction of its decay rate.

Finally, averaging a bounded linear Green right inverse over the compact spatial symmetry group preserves the right-inverse identity. This argument is applied to the Green operator, not to the finite-rank metric. It therefore avoids any false assertion that a continuous-group average of finite-rank operators must retain finite rank. The claimed transverse O(3), inversion symmetry, and finite variance follow from the weighted fixed-point construction under the main gluing theorem's hypotheses.

No new fatal gap was found in this weighted and symmetry extension.
