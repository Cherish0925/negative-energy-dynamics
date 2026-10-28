# Open parameter families of negative-energy global traveling waves

This note extends the certified four-dimensional cubic profile. It does not claim dynamical stability. A family of exact traveling waves persists under changes of the equation; this does not imply that arbitrary nearby initial data remain close to that family.

The base construction supplies a nonzero real radial Q satisfying

\[
\Delta^2Q+Q-Q^3=0,
\quad \|Q\|_Z<105,
\quad Z=H^2(\mathbb R^4),\quad
\|f\|_Z^2=\|f\|_2^2+\|\Delta f\|_2^2.
\]

Its linearizations are invertible on the full real-even and imaginary-odd inversion sectors, with inverse norm at most 29 from Z* to Z. If z_e=L_-^{-1}(e·∇Q) for a unit vector e, the certified response bounds give ||z_e||_Z<151 and

\[
\langle e\cdot\nabla Q,z_e\rangle=I<-175.
\]

Rotational symmetry makes the full inertia matrix exactly I times the four-by-four identity. No additional spectral computation is needed below.

## 1. A quantitative extension, including genuinely anisotropic dispersion

Let a(ξ) be a real homogeneous quartic polynomial and B a real symmetric four-by-four matrix. Define

\[
\delta_a=\sup_{|\xi|=1}|a(\xi)-|\xi|^4|,
\qquad
K_a(U)=\int a(\xi)|\widehat U(\xi)|^2\,d\xi,
\qquad
K_B(U)=\int (\nabla\overline U)^T B\nabla U.
\]

Consider

\[
i u_t=a(D)u-\nabla\cdot B\nabla u-|u|^2u,
\qquad
E_{a,B}(u)=\tfrac12K_a(u)+\tfrac12K_B(u)-\tfrac14\|u\|_4^4.
\]

**Quantitative theorem.** For every vector v satisfying

\[
0< s:=|v|\le10^{-6},\qquad
2\delta_a+\|B\|_{\rm op}\le s^2/1000,
\]

there is a unique profile U in the ball ||U−Q||_Z≤200s, in the symmetry space specified below, solving

\[
a(D)U-\nabla\cdot B\nabla U+U+i v\cdot\nabla U-|U|^2U=0.
\]

It satisfies

\[
E_{a,B}(U)<-18s^2<0.
\]

Consequently u(t,x)=exp(it)U(x−vt) is an exact all-time H4 solution whose H2 norm is constant. In particular, positive mixed dispersion is allowed: B=μ Id with 0<μ≤|v|²/1000. The inequalities with strict signs specify an open subset of the 35-dimensional quartic-coefficient space, the ten-dimensional symmetric-matrix space, and the four-dimensional velocity space. The bound on δ_a automatically makes a positive elliptic.

These moving profiles are nonradial about every center. If a profile were radial about a center, it would be even under inversion about that center. The principal operator, second-order operator, mass term and nonlinearity would all remain even, whereas i v·∇U would be odd. The equation would force v·∇U=0. A nonzero function constant along a nonzero direction cannot be in L2.

### Symmetry space and why arbitrary quartic coefficients are admissible

Use

\[
X=\{U\in H^2(\mathbb R^4;\mathbb C):U(-x)=\overline{U(x)}\}.
\]

Thus Re U is even under central inversion and Im U is odd. All even spherical-harmonic degrees occur in the real part and all odd degrees in the imaginary part, with their full multiplicities. The certified radial spectral bounds already cover these direct sums uniformly. Every real homogeneous quartic symbol commutes with central inversion and conjugation. The terms −∇·B∇ and i v·∇ preserve X as well. No axial symmetry, separate coordinate-reflection symmetry, or special orientation of B or v is imposed.

### Exact contraction estimates

Write L=D_U(Δ²U+U−|U|²U)|_Q and D=a(D)−Δ²−∇·B∇. The multiplier bounds are

\[
\|D\|_{Z\to Z^*}\le\delta_a+\|B\|/2=:d,
\qquad
\|i v\cdot\nabla\|_{Z\to Z^*}\le Gs,\quad G=3/5.
\]

Set m=105, C=29, α=1/256 and r=200s. The cubic remainder R(h) obeys

\[
\|R(h)\|_{Z^*}\le\alpha(3m r^2+r^3),
\qquad
\operatorname{Lip}_{\|h\|\le r}R\le\alpha(6m r+3r^2).
\]

The equation is equivalent to

\[
h=-i z_v-L^{-1}\{DQ+(D+i v\cdot\nabla)h-R(h)\},
\quad z_v=L_-^{-1}(v\cdot\nabla Q),\quad\|z_v\|_Z\le151s.
\]

The error w=h+i z_v has norm at most

\[
W(s)=C\{d m+(d+Gs)r+\alpha(3m r^2+r^3)\},
\qquad d\le s^2/2000.
\]

All upper bounds after division by the displayed powers of s are increasing for 0<s≤10⁻⁶. At s=10⁻⁶, exact rational arithmetic gives

\[
\frac{151s+W(s)}{200s}
=\frac{1524308261787529}{2000000000000000}<1,
\]

\[
C\{d+Gs+\alpha(6mr+3r^2)\}
=\frac{28581702187529}{2000000000000000}<1.
\]

These prove existence and uniqueness in the stated ball. The exact comparisons are independently executed by `round3_robustness_constants.py`, with results in `round3_robustness_constants.json`.

The constants C and 151 follow directly from already certified quantities: the least base preconditioned gap is γ=2247991/64000000, so γ⁻¹<29; and

\[
132+\frac{10364489/16000000}{\gamma}<151.
\]

### Quantitative energy sign

For every cubic profile above, the exact Pohozaev identity is

\[
4E_{a,B}(U)-K_B(U)-\tfrac12v\cdot P(U)=0,
\quad P(U)=\operatorname{Im}\int\overline U\nabla U.
\]

The homogeneous quartic perturbation makes no extra term in this identity. Since h=−i z_v+w,

\[
v\cdot P(U)\le2I s^2+2Gm sW(s)+Gs r^2.
\]

Also K_B(U)≤||B||(m+r)²/2. Therefore

\[
\frac{E_{a,B}(U)}{s^2}
\le\frac{(m+r)^2}{8000}-\frac{175}{4}
 +\frac{Gm}{4}\frac{W(s)}s+\frac G8\frac{r^2}s.
\]

At the largest permitted speed the right side is exactly

\[
-\frac{793334297385473}{40000000000000}
<-19.83<-18.
\]

This computation proves an actual uniform parameter region; it is not an unquantified appeal to continuity of a negative energy.

## 2. Removing the smallness restriction on the second-order dispersion

At cubic power, if u solves the equation with parameters (a,B), then

\[
u_\lambda(t,x)=\lambda^2 u(\lambda^4t,\lambda x)
\]

solves the equation with the same a and with B_λ=λ²B. Its frequency, velocity and energy satisfy

\[
\omega_\lambda=\lambda^4\omega,\qquad
v_\lambda=\lambda^3v,\qquad
E_{a,\lambda^2B}(u_\lambda)=\lambda^4E_{a,B}(u).
\]

**Corollary.** For every real symmetric matrix B_target, and every quartic a with δ_a<10⁻¹⁶, there is a negative-energy global traveling wave for the equation with exactly those coefficients. The frequency is allowed to vary. In particular this holds for every prescribed scalar μ>0 in

\[
i u_t=\Delta^2u-\mu\Delta u-|u|^2u.
\]

For a concrete parameter choice, take s*=10⁻⁶ and any unit propagation direction e. Choose λ≥1 with

\[
\lambda^2\ge\max\{1,\ 2\cdot10^{15}\|B_{\rm target}\|\},
\quad B_0=B_{\rm target}/\lambda^2,
\quad v_0=s_*e.
\]

Then ||B_0||≤5·10⁻¹⁶ and 2δ_a+||B_0||<10⁻¹⁵=s*²/1000. Apply the quantitative theorem at frequency one and rescale. This gives frequency λ⁴, velocity λ³s*e, and energy less than −18λ⁴s*². No statement that the physical velocity remains small after this rescaling is intended.

## 3. General powers near the cubic: the exact Pohozaev signs

Now let p denote the power in |u|^(p−1)u; thus p=3 is cubic. Define

\[
E_{a,B,p}(U)=\tfrac12K_a(U)+\tfrac12K_B(U)
 -\frac1{p+1}L_p(U),\qquad L_p(U)=\int|U|^{p+1}.
\]

A traveling profile at frequency ω solves

\[
a(D)U-\nabla\cdot B\nabla U+\omega U
 +i v\cdot\nabla U-|U|^{p-1}U=0.
\]

Mass-preserving dilation U_λ(x)=λ²U(λx) gives

\[
2K_a(U)+K_B(U)-\frac{2(p-1)}{p+1}L_p(U)
 -\tfrac12v\cdot P(U)=0.
\]

Equivalently,

\[
\boxed{\ E_{a,B,p}(U)=\frac14K_B(U)
 +\frac{p-3}{2(p+1)}L_p(U)+\frac18v\cdot P(U).\ }
\]

There is no ω term because the dilation preserves mass. The identity is justified for H4 profiles by the same compactly supported skew-adjoint dilation multiplier as in the base proof; the constant-coefficient quartic commutator has its principal homogeneous factor four and only H2-tail errors. Alternatively one can adjoin ω, B and the nonlinear coefficient to the local implicit-function parameters and use uniqueness plus strong continuity of dilations to prove differentiability of the dilation curve in H2 before differentiating the action.

For scalar B=μ Id the sign consequences are unambiguous:

* Cubic standing profiles have E=μ||∇U||²/4. Positive μ raises their energy, rather than making it negative.
* At μ=0, standing profiles have the sign of p−3 in their energy.
* The negative velocity contribution comes from the certified negative inertia. It must overcome the positive μ and p−3 terms when these are positive.

In particular, at frequency one a fixed positive μ does not give negative energy all the way down to zero speed. The negative-energy region is a wedge in the joint parameters. The scaling corollary above allows arbitrary positive μ by adjusting the frequency as well.

## 4. Noninteger powers and the parameter continuation theorem

The map

\[
(a,B,p,v,U)\longmapsto
a(D)U-\nabla\cdot B\nabla U+U+i v\cdot\nabla U-|U|^{p-1}U
\]

is jointly C2 from a neighborhood of (|ξ|⁴,0,3,0,Q) in the real parameter space times X to X*. It is real analytic when p is fixed at 3.

Here is why noninteger p and zeros of Q are harmless for C2. For p in a compact interval inside (5/2,7/2), the pointwise map z↦|z|^(p−1)z on the real plane is C2, with its second derivative bounded by a constant times |z|^(p−2). Hölder estimates for the second profile derivative use three L4 factors and a coefficient in L4, hence the norm ||U||_(4(p−2)), which is controlled by H2 in four dimensions. Work, for instance, with p in [11/4,13/4], leaving room in the exponents. Parameter derivatives introduce powers of log|z|; define the products at z=0 by continuity and use

\[
|\log r|^k\le C_{\varepsilon,k}(r^{-\varepsilon}+r^{\varepsilon})
\quad(r>0).
\]

Choosing a small epsilon keeps every required Lebesgue exponent between 2 and a finite number. The embedding H2(R4) into every finite Lq with q≥2, Hölder's inequality, and the usual continuous superposition estimates give the stated joint C2 regularity. C3 or analyticity across noninteger powers is not asserted.

The profile derivative at the base is the already invertible block operator L_+⊕L_- on X. The real C2 implicit-function theorem therefore gives a unique C2 family U(a,B,p,v) in a common neighborhood. At v=0, conjugation and uniqueness make the profile real. For all parameters, uniqueness gives U(a,B,p,−v)=conj U(a,B,p,v).

Every such profile is H4: H2 in four dimensions controls L^(2p), so the nonlinearity is L2; the second-order and first-order terms are L2; and the positive elliptic quartic principal operator then gives H4 regularity. These profiles define exact all-time traveling solutions.

The same argument can be centered at the quantitative nonzero-speed profiles of Section 1. Their linearizations remain invertible because the displayed contraction constant is below 0.015. This makes a genuinely open neighborhood in the exponent parameter available at every point of the explicit cubic negative-energy family.

## 5. An open wedge with positive mixed dispersion and slightly supercritical powers

The continuation theorem can be made substantially more informative than an unspecified open neighborhood. Shrink one common parameter neighborhood so that

\[
\|U\|_Z<105,\qquad L_p(U)<12000,\qquad p>2,
\]

and the quadratic form of the velocity Jacobian satisfies

\[
w^T D_vP(a,B,p,v)w\le-300|w|^2.
\]

These simultaneous bounds follow from strict inequalities at the base: ||Q||_Z<105, L_3(Q)=||Q||_Z²<11025 and D_vP(0)=2I Id<−350 Id. Since P(a,B,p,0)=0, integration along the velocity segment gives

\[
v\cdot P(a,B,p,v)\le-300|v|^2.
\]

The exact Pohozaev identity consequently yields the uniform bound

\[
\boxed{\ E_{a,B,p}(U)
\le1500\|B\|+2000(p-3)_+-\frac{75}{2}|v|^2.\ }
\]

Thus, throughout a sufficiently small common parameter neighborhood,

\[
0<|v|,\quad \|B\|<|v|^2/100,\quad
(p-3)_+<|v|^2/200
\]

imply

\[
E_{a,B,p}(U)<-\frac{25}{2}|v|^2<0.
\]

Taking B positive definite and 3<p<3+|v|²/200 gives a nonempty open set of positive second-order dispersion and noninteger, slightly mass-supercritical nonlinearities. The quartic coefficients vary independently in a sufficiently small open neighborhood. The radii of this last common neighborhood and the exponent interval are existence bounds from the proved C2 continuation; they are not claimed to have been numerically quantified. Section 1 supplies the separate fully numerical cubic region.

## 6. The sharp first-order boundary and its certified conservative slope

At the isotropic base write G0=||∇Q||² and L0=||Q||4⁴. If v=epsilon e, μ=κ epsilon² and p=3+τ epsilon², then

\[
\boxed{\
E_{\mu,p}(U)=\frac{\epsilon^2}{4}
\left(I+\kappa G_0+\frac\tau2L_0\right)+o(\epsilon^2).
\ }
\]

In particular the cubic boundary to leading order is

\[
\mu\sim\left(-I/G_0\right)|v|^2,
\]

with a strictly positive coefficient. The standing branch instead has

\[
E_{\mu,3}(U_{\mu,0})=\mu G_0/4+o(\mu),
\qquad E_{0,p}(U_{p,0})=(p-3)L_0/8+o(|p-3|).
\]

Existing certified bounds alone give G0<11025/2, L0<11025 and I<−175. Hence any fixed κ,τ≥0 with

\[
\kappa+\tau<2/63
\]

has negative energy for all sufficiently small nonzero epsilon. For example κ=1/100, τ=0 yields a quadratic energy coefficient less than −959/32. This is a proved conservative range, not an assertion that 2/63 is the actual boundary.

For a fixed nearby anisotropic quartic a, replace Q by its standing profile Q_a and I by the symmetric inertia matrix

\[
\mathcal I_{jk}(a)=\langle\partial_jQ_a,
 L_{-,a}^{-1}\partial_kQ_a\rangle.
\]

It remains negative definite by continuity. For B=epsilon²C and p=3+τepsilon², the leading coefficient becomes

\[
\frac14\left[e^T\mathcal I(a)e+K_C(Q_a)+\tfrac\tau2L_3(Q_a)\right].
\]

This identifies explicitly how dispersion anisotropy changes the energy boundary and the direction dependence of the traveling family.

## 7. Fixed nearby exponents and arbitrary second-order matrices

For general p near 3 the exact scaling is

\[
u_\lambda(t,x)=\lambda^{4/(p-1)}u(\lambda^4t,\lambda x).
\]

It preserves p and a, replaces B by λ²B, changes frequency and velocity by λ⁴ and λ³, and satisfies

\[
E_{a,\lambda^2B,p}(u_\lambda)
=\lambda^{8/(p-1)}E_{a,B,p}(u).
\]

The factor is positive. Choose a fixed sufficiently small nonzero dimensionless velocity, a fixed strict quartic neighborhood, and an exponent interval around 3 whose width is smaller than that velocity squared divided by 200. For any prescribed symmetric B_target, take λ large enough that B_target/λ² lies in the strict wedge of Section 5. Construct the negative-energy wave there and rescale.

It follows that there exist positive constants delta and epsilon such that, for every quartic a with δ_a<delta, every p in (3−epsilon,3+epsilon), and every real symmetric B_target of arbitrary size, the corresponding equation possesses a global H2-bounded negative-energy traveling wave. The frequency is free. This includes a fixed open interval of powers strictly above three, not merely a sequence p→3 coupled to v→0.

Finally, linear coordinate changes extend the quartic statement to neighborhoods of any ellipsoidal symbol (ξ^TCξ)² with C positive definite. With y=C^(−1/2)x, the principal part becomes Δ_y², B becomes C^(−1/2)BC^(−1/2), velocity becomes C^(−1/2)v, and energy is multiplied by the positive factor det(C)^(1/2). This does not establish the result for every positive quartic polynomial; it establishes open coefficient neighborhoods around all such ellipsoidal quartics.

The conclusions concern persistent exact solutions of varying equations. They do not prove spectral, orbital, or asymptotic stability, and do not give an open set of globally bounded initial data for any one fixed equation.
