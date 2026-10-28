# Proof details: superlinear homogeneous-dispersion mass gap

Derived file: `round8_fractional_mass_gap.md`.

## Verdict and scope

I independently recomputed the central analytic steps for **fixed m>1**. I found no substantive gap or counterexample in Theorems A and B as stated. In particular, the nonlocal cutoff argument supplies the missing justification that a formal homogeneous Pohozaev calculation alone would not provide.

This audit does not certify the optional m=1 endpoint, any existence of negative-energy waves, a general dynamical mass gap, or publication priority. It checks the mathematical extension for real, even, positive elliptic homogeneous symbols with the stated smoothness.

## 1. Resolvent and weak-profile regularity

For m>1, the linear drift is lower order. Young's inequality bounds |v||xi| by a small multiple of |xi|^m plus a constant depending on v, so a sufficiently large mu makes

$$
a(\xi)-v\cdot\xi+\mu\asymp1+|\xi|^m.
$$

The multiplier mapping L^q to H^{m,q} is valid. The lack of smooth extension of a at xi=0 is not an obstruction to Mihlin: differentiating a homogeneous order-m symbol produces |xi|^{m-k}, and multiplication by the required |xi|^k removes that singularity. At large frequency the elliptic denominator gives the required decay. C^{N+2} sphere regularity is more than the necessary number of Mihlin derivatives.

For N>m, put x=m/N in (0,1). The initial exponent satisfies

$$
\frac2{1-x}>1+2x,
$$

because 2-(1-x)(1+2x)=1-x+2x^2>0. Thus the first nonlinear input exponent exceeds one; all later inputs are larger. The reciprocal recurrence

$$
\beta_{j+1}=(1+2x)\beta_j-x,
\qquad \beta_j=\frac12-\frac x2(1+2x)^j
$$

is correct. It strictly improves integrability and reaches an input exponent above N/m after finitely many steps, with harmless endpoint weakening. The linear resolvent term can indeed be interpolated between its L^2 bound and its better Sobolev output; its potentially different integrability does not block adding the two summands.

For N=m, initial energy regularity supplies every finite L^q, and for N<m it supplies L^infinity. These cases also give boundedness. Once U is bounded, F(U)=|U|^{2m/N}U is in L^2; hence U is in H^m, which is contained in H^1 for m>1. The real two-component map F is C^1 with derivative bounded on bounded sets even for exponent 2m/N<1. Therefore the Sobolev chain rule gives F(U) in H^1 and the resolvent gives U in H^{m+1}. No unproved higher differentiability of the power is used.

## 2. The nonlocal cutoff estimate

The Fourier kernel of the skew dilation cutoff is

$$
\widehat{L_Ru}(\xi)=\frac i2\int(\xi+\eta)\cdot\widehat f_R(\xi-\eta)\widehat u(\eta)\,d\eta,
$$

up to normalization. Consequently the claimed commutator kernel has the correct sign and frequency factor.

For k=xi-eta, the mean-value bound for the degree-m symbol gives

$$
|a(\xi)-a(\eta)|\le C|k|(|\xi|+|\eta|)^{m-1}.
$$

It remains valid across a segment passing through the origin because m>1 and the first derivative extends continuously there as zero. Dividing the resulting degree-m numerator by the two energy weights yields

$$
\frac{(|\xi|+|\eta|)^m}{\langle\xi\rangle^{m/2}\langle\eta\rangle^{m/2}}
\le C\left[\left(\frac{\langle\xi\rangle}{\langle\eta\rangle}\right)^{m/2}
+\left(\frac{\langle\eta\rangle}{\langle\xi\rangle}\right)^{m/2}\right]
\le C\langle k\rangle^{m/2}.
$$

Thus equation (11) is correct, including unequal and low frequencies. Since

$$
\widehat f_R(k)=R^{N+1}\widehat f(Rk),
$$

the weighted convolution-kernel L^1 norm is bounded independently of R>=1. Young's inequality proves the H^{m/2} to H^{-m/2} bound with no locality assumption.

For Schwartz u, L_Ru converges to Lu in L^2 and a(D)u is in L^2. Hence the commutator form tends to 2 Re<a(D)u,Lu>. Fourier integration by parts gives m A_a(u); the boundary at zero vanishes because a is of positive degree. Uniform form boundedness and density then justify passage to arbitrary energy-space u. The degree-one drift version uses the weaker H^{1/2} form norm, which is controlled because m>1.

## 3. Exact identities and factors

The improved regularity makes L_RU an admissible energy-space weak test. Nonlinear integration by parts is justified since F(U) and grad U are in L^2; consequently grad |U|^p is integrable. The limit of the nonlinear factor is

$$
N\left(\frac12-\frac1p\right)=\frac mp.
$$

The resulting identities were recomputed:

$$
v\cdot P=2mE_a,
\qquad \omega M=rA_a+(2m-p)E_a.
$$

Writing U=A+iB, evenness and reality of the symbol imply a(D) preserves real functions. Thus

$$
\langle B,(a(D)+\omega-|U|^{2r})B\rangle
=-\int B\,v\cdot\nabla A
=\tfrac12v\cdot P=mE_a.
$$

The crucial coefficient in equation (15) is therefore 1/m, as written. A sign or factor error here would have invalidated the gap argument; none was found.

## 4. Variational and phase claims

The mass-critical exponent lies strictly below the energy-space Sobolev critical exponent whenever that exponent is finite. The nonvanishing, local compactness, Hilbert splitting and Brezis--Lieb proof therefore applies for every positive s=m/2 under consideration. The same argument works for normalized maximizing sequences with energy tending to zero from either side; negativity is not needed for the attainment step.

The real/imaginary quadratic splitting follows from the real-even symbol. Equality in Minkowski and then a pi/4 rotation really does force constant phase, even when a real optimizer changes sign; no positivity-preserving property of the multiplier is being assumed.

For the phase kernel, I recomputed the decisive algebra. Combining the upper and lower second-remainder bounds gives

$$
(r+1)A\left[(r-1)AB^2/M^2+2BC_1/M\right]
-(C_1+rAB/M)^2
=-(C_1-AB/M)^2.
$$

Thus equality is forced. The handling of the zero set is sufficient: when r<1 the convex remainder forces b to vanish there; when r>=1 the equality b^2=(B/M)Q^2 off that set already accounts for the entire b mass. Applying the same property to b+Q removes the possible sign variation. This establishes ker L_-=span{Q} without a maximum principle.

The potential is compact from H^{m/2} to H^{-m/2}, by local Rellich at exponent p and L^{p/(2r)} approximation/tail control. Its compactness plus the positive free form and the identified one-dimensional kernel yields H^{m/2} coercivity on the L^2 phase orthogonal complement.

## 5. Uniformity over compact symbol families

If a_n tends to a_infinity on the sphere with a common ellipticity bound, their forms are multiplicatively close. This squeezes the sharp GN constants and hence the critical masses. Normalization A_{a_n}(U_n)=1 produces an optimizing sequence for the limit symbol, even though its limiting-symbol kinetic norms are only 1+o(1). The compactness proof is unchanged by that o(1).

The frequency identity depends on the normalized kinetic form and energy only, so it yields omega_n to omega_Q without any bound on v_n. The kinetic form difference tends to zero in H^{m/2} to H^{-m/2} norm, and the nonlinear potential difference does likewise. Therefore the single limiting optimizer's phase coercivity transfers to all sufficiently large n, contradicting negative energy through the exact imaginary identity. No uniform regularity estimate in velocities or prior uniform coercivity over all optimizers is required.

## 6. Recommended boundaries in the final manuscript

- Keep m>1, fixed N and fixed m in the main theorem and in the compact-family result.
- Keep real-even homogeneity, positive ellipticity, and stated sphere smoothness explicit.
- Do not describe a compact-symbol-family gap as uniform over all anisotropies or all orders.
- Describe it as a traveling-profile exclusion theorem, not a global-dynamics or existence theorem.
- Optional endpoint m=1 statements were not audited here and are unnecessary for this proof.

## Addendum: stronger local C0 robustness

Derived the new final theorem in [fractional-section.tex](../../manuscripts/homogeneous-dispersion/fractional-section.tex). The stronger statement is valid: for each fixed admissible symbol a0 there are delta>0 and epsilon>0 such that all individually admissible smooth real-even homogeneous symbols with

$$
\|a/a_0-1\|_{L^\infty(S^{N-1})}<\delta
$$

have the same positive mass-gap lower bound epsilon. Neither compactness of that neighborhood nor uniform derivative bounds is needed.

The quantifier negation is used correctly: failure supplies, for every n, a symbol within relative distance 1/n of a0 and a negative-energy profile whose mass exceeds its own critical mass by less than 1/n. Uniform symbol convergence supplies norm convergence of the energy forms and continuity of the sharp critical masses. The optimizing-sequence argument then uses only the single limiting smooth symbol a0. Individual symbol derivatives and velocity-dependent regularity constants occur only in establishing each exact identity; no such constant is used in the final contradiction. The imaginary-component form identity therefore retains its force even if those derivative bounds diverge along the sequence.

The C0-compact-family proposition follows by a finite subcover. Its compactness must mean an actually compact subset whose members all satisfy the stated smoothness and strict positivity, not merely a precompact family with possibly inadmissible limit symbols. Under the written statement this distinction is already respected. The local delta can be shrunk to below 1/2 to make positivity of all nearby symbols explicit.

Verdict: the local C0 strengthening is closed and strictly stronger than the originally audited C^{N+2}-compact-family formulation.
