# Independent mathematical derivation of the four-dimensional foundation

Date: 7 October 2026.

## Outcome

I independently rederived the mathematical reductions in the original manuscript and inspected the implementing polynomial and interval arithmetic routines. I found no fatal flaw in the chain from the frozen finite data to the negative-energy traveling waves. In particular, the sign of the energy is not a convention error, the symmetry restriction does not retain the translation or phase kernel, and the Birman–Schwinger estimates do control all required angular degrees.

 It did not rerun the existing `PASS` pipeline as a substitute for mathematical review. It also produced a separate, explicitly nonrigorous spectral calculation from the frozen jets, using none of the certificate implementation; those values are useful consistency checks and are not additional premises of the proof.

Files inspected:

* [BNLS-Nonradial-Research-20261007.tex](../../manuscripts/biharmonic-certificates/BNLS-Nonradial-Research-20261007.tex).
* The finite data and implementations in `research/BNLS_Research_Bundle/round2_certificate/`, especially [round2_certified_birman_hs.py](../../computations/spectral-dynamics/verification/round2_certified_birman_hs.py), [round2_verify_frozen_ritz.py](../../computations/spectral-dynamics/verification/round2_verify_frozen_ritz.py), [round2_certificate_canonical.py](../../computations/spectral-dynamics/verification/round2_certificate_canonical.py), and both exact polynomial helper modules.
* [gou-details.md](../dispersion-extensions/gou-details.md).
* Gou, *Blowup of cylindrically symmetric solutions for biharmonic NLS*, arXiv:2205.08167v3, independently reopened from the original source.

## 1. Energy and velocity signs

Fix the equation and normalization

$$
i u_t=\Delta^2u-|u|^2u,\qquad
E(u)=\tfrac12\|\Delta u\|_2^2-\tfrac14\|u\|_4^4,
\quad P_1(u)=\operatorname{Im}\int\bar u\partial_1u.
$$

The ansatz $u(t,x)=e^{it}W(x-vte_1)$ gives

$$
(\Delta^2+1)W+i v\partial_1W-|W|^2W=0.
$$

The profile is a critical point of

$$
S_v(W)=E(W)+\tfrac12 M(W)-\tfrac v2P_1(W),
$$

because the real gradient of $P_1$ is $-2i\partial_1W$. For the mass-preserving dilation $W_\lambda(x)=\lambda^2W(\lambda x)$, the three quantities scale as $E(W_\lambda)=\lambda^4E(W)$, $M(W_\lambda)=M(W)$, and $P_1(W_\lambda)=\lambda P_1(W)$. Thus the justified dilation identity is

$$
4E(W)-\tfrac v2P_1(W)=0.
$$

At a real stationary state $Q$, writing $z=L_-^{-1}\partial_1Q$, differentiation of the profile equation gives $W_v=Q-i v z+O(v^2)$. Direct differentiation of the momentum gives

$$
P_1'(0)=\int (z\partial_1Q-Q\partial_1z)=2\langle\partial_1Q,z\rangle=2I.
$$

Consequently $E(W_v)=Iv^2/4+O(v^4)$. The factors and signs in the manuscript are correct.

The localized skew-adjoint dilation proof is also valid: its kinetic error is supported in an annulus and bounded by products of unweighted $H^2$ tails; its momentum error is dominated by $|W||\nabla W|\in L^1$. It does not conceal a finite-variance assumption.

## 2. Energy-space estimates

The sharp four-dimensional Sobolev constant is consistent with direct evaluation on $(1+|x|^2)^{-1}$:

$$
\|h\|_4^2\le\frac{\sqrt6}{8\pi}\|\nabla h\|_2^2.
$$

Fourier interpolation gives $2\|\nabla h\|_2^2\le\|h\|_Z^2$. Therefore $\|h\|_4\le\|h\|_Z/4$ is a valid conservative bound, including complex functions by the usual modulus inequality. Four applications of this bound give the product constant $1/256$ in $Z^*$.

The derivative estimate is exactly the multiplier bound

$$
\sup_{r\ge0}\frac r{1+r^4}=\frac{3^{3/4}}4<\frac35.
$$

Here the denominator is $1+r^4$, rather than its square root, because the operator maps $Z$ to $Z^*$. This distinction is handled correctly throughout.

## 3. Angular operators and all-degree control

Let $D_\ell=\partial_r^2+3r^{-1}\partial_r-\lambda_\ell r^{-2}$, with $\lambda_\ell=\ell(\ell+2)$. Expanding the square and integrating its cross term independently gives

$$
\int r^3|D_\ell f|^2
=\int r^3|D_0f|^2+2\lambda_\ell\int r|f'|^2
+\lambda_\ell^2\int r^{-1}|f|^2,
\qquad \ell\ge1.
$$

On a compactly supported core away from zero the identity is immediate. The weighted domain supplied by its right side is common to all $\ell\ge1$, and closure gives the claimed form identity and monotonicity. There is no use of operator monotonicity of squaring: the monotonicity is established directly at the quadratic-form level. That is essential because $H_\ell^2\ge H_k^2$ would not follow merely from $H_\ell\ge H_k$ for arbitrary operators.

The max–min quotient $c\int q^2|f|^2/\langle f,A_\ell f\rangle$ thus decreases in its largest value as $\ell$ increases. The degree-four plus estimate and degree-three minus estimate cover every required higher even/odd sector. Angular multiplicities do not multiply a single-sector spectral radius or spectral gap.

For the axial PT space, the real part consists of even zonal harmonics and the imaginary part of odd zonal harmonics. The phase kernel is radial and imaginary-even, and the translation kernels are real-odd or non-axial; all are excluded. For the larger full inversion–conjugation space, real-even and imaginary-odd contain every angular multiplicity, but the same uniform gaps still suffice. No new low-mode assumption is needed for that enlargement.

## 4. Birman–Schwinger reduction and kernel normalization

With $H_\ell=-D_\ell$, $A_\ell=H_\ell^2+1$, and $T=\sqrt c\,M_qA_\ell^{-1/2}$, the two positive operators are $T^*T$ and $TT^*$. Thus replacing $A_\ell^{-1/2}c q^2A_\ell^{-1/2}$ by $cM_qA_\ell^{-1}M_q$ preserves its nonzero eigenvalues, even when $q$ changes sign.

Let $\nu=\ell+1$ and $\kappa=e^{i\pi/4}$. The radial solutions $r^{-1}I_\nu(\kappa r)$, $r^{-1}K_\nu(\kappa r)$ have Wronskian $-r^{-3}$. Hence the $(H_\ell+i)^{-1}$ Green kernel in measure $s^3ds$ has coefficient exactly

$$
\frac1{rs}I_\nu(\kappa r_<)K_\nu(\kappa r_>).
$$

Since $(H^2+1)^{-1}=-\operatorname{Im}(H+i)^{-1}$, conjugation to Lebesgue measure yields exactly the kernel

$$
-c\sqrt{rs}\,q(r)q(s)\operatorname{Im}\{I_\nu(\kappa r_<)K_\nu(\kappa r_>)\}.
$$

There is no missing factor $2$, $\pi$, or spherical area. In the HS square, the two open triangular halves supply the factor $2$; the diagonal has zero two-dimensional measure. Squaring the imaginary part produces the three terms and the cross coefficient $2$ used in the code.

The origin bound follows from the positive spectral inequality $(H^2+1)^{-1}\le(2H)^{-1}$. The diagonal of $H_\ell^{-1}$ in radial measure is $1/(2\nu r^2)$; multiplication by $r^3q^2$ gives the trace majorant $c r q^2/(4\nu)$. Its integral on $[0,\epsilon]$ is at most $c\|q\|_\infty^2\epsilon^2/(8\nu)$, matching the implementation. Positivity here means positive semidefiniteness, not entrywise positivity. The resulting Cauchy–Schwarz kernel inequality is sufficient for the two omitted strips.

## 5. Implemented interval enclosures

The interval procedure encloses values throughout each quadrature cell, not only at sampled points. I checked the following reductions against the code:

1. For $Y=(f,rf')$, the Bessel system matrix is $\bigl(\begin{smallmatrix}0&1/r\\ \nu^2/r+ir&0\end{smallmatrix}\bigr)$. Its infinity norm is bounded by $L=\nu^2/a+b+1/a$ on $[a,b]$. Using $|f(m)|+m|f'(m)|$ as an initial upper bound is conservative. The code's exponential variation bound applies in both directions from the midpoint.
2. The enclosure for $rf'$, division by the positive radial interval, and the ODE expression for $f''$ correctly produce whole-cell derivative enclosures.
3. The radial polynomial, first derivative, and second derivative are evaluated in ball arithmetic. In particular the apparently ordinary factorial divisions occur after multiplication by an Arb coefficient, so they are not floating-point divisions of integers.
4. The half-cell cumulative integral uses
   $hF(m)/2-h^2F'(m)/8$, with error $h^3\sup|F''|/48$; these constants follow by integrating the quadratic Taylor remainder on $[-h/2,0]$.
5. If $G=\sum b_jJ_j$, then $G''=\sum(b_j''J_j+2b_j'F_j+b_jF_j')$. This is the formula in the code. Uncertainty in the earlier cumulative integrals is retained in both midpoint values and whole-cell bounds.
6. The outer midpoint error $h^3\sup|G''|/24$ and the origin-strip correction are added as balls before the strict comparisons. The canonical profile is exactly zero beyond radius 36, so there is no unestimated far-field tail in these BS calculations.

The finite arithmetic still relies on the documented outward-enclosure behavior of Python-FLINT/Arb, including the special functions and ball-radius constructors. This is an explicit computational trusted base, rather than a mathematical approximation claim.

## 6. Frozen polynomials, regularity, and inverse pairing

The frozen profile's hexadecimal mantissas have at most 13 fractional hexadecimal digits. They are exactly representable binary64 values, so the interval and response routines' `Fraction(float.fromhex(...))` reads the same rational as the exact parser in the Ritz verifier. The nodal derivatives at zero have vanishing first and third derivatives; all four derivatives vanish at the compact endpoint. The response data have these same endpoint properties. Thus both radial extensions have the required Sobolev regularity, and there are no unaccounted interface distributions in fourth derivatives.

The radial residual numerator is $r^3F$; its squared norm has weight $r^{-3}$. The response numerator has the same $r^3$ factor but the dipole norm has weight $r^5$, so its squared residual weight is $r^{-1}$. Both conventions and their different origin integrations are correct in the exact verifiers. The full-space dipole area is $\pi^2/2$, versus $2\pi^2$ for a scalar radial function; those factors are consistent.

The negative inverse pairing is not inferred from a negative Rayleigh quotient alone. For $r=g-L\psi$,

$$
\langle g,L^{-1}g\rangle
=2\langle g,\psi\rangle-\langle\psi,L\psi\rangle
+\langle r,L^{-1}r\rangle.
$$

This identity holds for indefinite $L$. The final term has upper bound $\|L^{-1}\|\|r\|_{Z^*}^2$. The spectral transfer controls the inverse on the exact stationary profile, and the source and potential perturbations are both included in $r$ and the quadratic expression. Thus the inverse pairing bound does not assume positivity where the operator actually has a negative mode.

## 7. Independent spectral diagnostic and interpretation

A separately written 600-node Gauss–Legendre Nyström calculation used SciPy's Bessel functions and `BPoly.from_derivatives` on the frozen jets. It imported no certificate helper or verifier. Its output is [round4_independent_bs_diagnostic.json](../../computations/spectral-dynamics/numerical_diagnostics_NOT_certificates/round4_independent_bs_diagnostic.json); it is ordinary numerical evidence, not interval certification.

The principal results are:

| Channel $(c,\ell)$ | First eigenvalue | Next eigenvalue | HS square |
|---|---:|---:|---:|
| $(3,0)$ | 5.39609160 | 3.00000007 | 38.79220807 |
| $(1,1)$ | 1.04260971 | 0.33333335 | 1.23330621 |
| $(3,2)$ | 2.11809791 | 0.47631695 | 4.79621435 |
| $(1,3)$ | 0.44461534 | 0.10724251 | 0.21168712 |
| $(3,4)$ | 0.81487530 | 0.22296117 | 0.72330242 |

All five values fit the rigorous bounds. Two exact symmetries explain nontrivial numerical checks: $AQ=Q^3$ produces the exact eigenvalue 3 in the plus radial BS channel, and $A\partial_jQ=3Q^2\partial_jQ$ produces the exact eigenvalue $1/3$ in the minus dipole BS channel. The independent calculations reproduce both.

The rigorous bounds themselves imply that $L_-$ has exactly one negative radial eigenmode in angular degree one, and none in higher odd degrees. In the full odd space this one radial mode has the four dipole angular multiplicities. The mechanism is therefore a particular negative dipole response of an excited stationary state; it does not presume a positive ground state has negative inertia.

The negative momentum–velocity pairing is physically and mathematically consistent with fourth-order dispersion. Momentum weights the Fourier density by $\xi$, whereas the center-of-mass velocity weights it by $4|\xi|^2\xi$. The two vector integrals need not point in the same direction. The usual second-order Galilean relation cannot be imported.

## 8. Published cylindrical claim

I independently checked the original statement in Gou's arXiv v3. Theorem 1.2 has $d\ge4$, $\mu\ge0$, the mass-critical exponent, negative energy, cylindrical symmetry, and the finite axial moment. It does not impose zero momentum, a ground-state condition, or a bounded axial moment uniformly for all time. Its positive-$\mu$ conclusion is explicitly finite-time blowup.

The weighted elliptic lemma in [gou-details.md](../dispersion-extensions/gou-details.md) is valid for the small-velocity branch: the free profile symbol has a positive lower bound, the profile is $H^4\subset C_0$, and the commutator with a truncated coordinate has a uniform $L^2$ bound. Absorbing the small far-field potential gives $x_jW\in H^4$. Therefore an absent axial moment does not explain the conflict.

The cylindrical multiplier contains an unbounded axial derivative. Its exact translation identity is

$$
M_{\phi_R}(e^{it}W(\cdot-vte_1))
=M_{\phi_R}(W)+2vtP_1(W).
$$

A negative slope is compatible with a constant $H^2$ norm because $\|x_1u(t)\|_2$ grows under translation. Thus the bounded-gradient closure used in the radial setting is unavailable for that cylindrical multiplier. This supplies a mathematically coherent location for the published conflict; the counterexample claim should still be assessed through its own complete proof and finite certificates.

## Final disposition

The analytic existence theorem, indefinite inverse-pairing reduction, angular spectral bounds, and implemented interval formulas survive this independent challenge. I found no unclosed mathematical premise specific to the original N=4 construction beyond the explicitly supplied finite certificates and the standard computational trusted base. External replication and review remain separate from this internal outcome. Extensions to other dimensions, dynamical stability, and exact zero-total-momentum multiwaves are not certified by this audit.
