# Proof details: supersymmetric partner of the Townes potential

The proposed identity is correct. It proves a genuine spectral statement; it does not, by itself, determine the full scattering interaction coefficient or the many-orbital sharp constant. Historical novelty has not been established here.

## 1. Exact radial factorization in two dimensions

Let (Q>0) be the radial decaying solution of

$$
-Q''-r^{-1}Q'+Q-Q^3=0,
$$

and write (p=Q'/Q). On $L^2((0,\infty),r\,dr)$, set

$$
A=\partial_r-p,\qquad A^*=-\partial_r-r^{-1}-p.
$$

The Riccati equation is

$$
p'+p^2+p/r=1-Q^2.
$$

Consequently, for the physical radial Friedrichs realization of $h=-\Delta-Q^2$,

$$
h+1=A^*A,
\qquad AA^*-1=-\partial_r^2-r^{-1}\partial_r+U,
$$

where

$$
U=r^{-2}+2p/r+2p^2+Q^2-2.
$$

Direct expansion gives

$$
\boxed{\ (rQ^2U)'=-Q^2/r^2-Q^4.\ }
$$

For example, expand (rQ^2U=Q^2/r+2QQ'+2r(Q')^2+rQ^4-2rQ^2), differentiate, and substitute (Q''=Q-Q^3-Q'/r). Every remaining mixed term cancels.

Exponential decay, (p(r)\to-1), and the radial equation imply (rQ^2U\to0) at infinity. Therefore

$$
\boxed{\ U(r)=\frac1{rQ(r)^2}\int_r^\infty
\left(\frac{Q(s)^2}{s^2}+Q(s)^4\right)ds>0.\ }
$$

The formula has the correct origin behavior (U=r^{-2}-1+O(r^2)). At infinity the potential is positive and tends to zero; its leading algebraic term is (1/(2r^3)).

## 2. Operator domains and the spectral conclusion

Define (A) as the closed first-order operator with domain radial (H^1(\mathbb R^2)), identified with the weighted half-line space. Multiplication by (p) is bounded. The quadratic form of (A^*A) is the ordinary radial Friedrichs form of (h+1), so no logarithmically singular origin extension is being introduced.

The partner (AA^*-1) has the displayed differential expression. After conjugation by (r^{1/2}), its potential has leading term (3/(4r^2)) at the origin. Thus this endpoint is limit point; infinity is also limit point. Its self-adjoint realization agrees with the Friedrichs realization of its form

$$
\int_0^\infty r\bigl(|v'|^2+U|v|^2\bigr)dr\ge0.
$$

In particular (AA^*\ge1). The nonzero spectra of (A^*A) and (AA^*) agree by polar decomposition, and $\ker A=\operatorname{span}\{Q\}$. Hence

$$
h\big|_{Q^\perp}\ge0.
$$

Thus the radial operator has exactly one negative eigenvalue, namely (-1), with eigenfunction (Q). Strict positivity of (U) excludes a zero eigenfunction of the partner, and therefore a radial zero eigenfunction of (h).

Equivalently, this gives the exact constrained quadratic inequality

$$
\int_{\mathbb R^2}|\nabla f|^2\ge
\int_{\mathbb R^2}Q^2|f|^2,
\qquad f\text{ radial},\quad \langle f,Q\rangle=0.
$$

The lower edge (0) is still the essential-spectrum threshold; no positive uniform gap above (0) is asserted for (h|_{Q^\perp}).

## 3. Absence of a radial zero resonance

Suppose (h\psi=0) has a nonzero regular bounded radial solution. Normalize $\psi(0)>0$ and put (y=A\psi$. Origin expansions give

$$
\psi'= -Q(0)^2\psi(0)r/2+O(r^3),
\quad p=(1-Q(0)^2)r/2+O(r^3),
$$

and therefore

$$
y=-\psi(0)r/2+O(r^3).
$$

Intertwining gives

$$
(ry')'=rUy.
$$

Starting from the negative regular branch, (y<0) and (ry'<0) persist for all (r>0): while (y<0), the latter quantity strictly decreases, so a first zero of (y) is impossible. Fixing any (r_0>0) yields (y'(r)\le-c/r) for (r\ge r_0), whence (y(r)\to-\infty).

On the other hand, boundedness of $\psi$ in
$(r\psi')'=-rQ^2\psi$ forces the logarithmic coefficient to vanish and gives $\psi'=O(e^{-cr})$ for some (c>0). As (p$ is bounded, (y=\psi'-p\psi$ is bounded. This contradiction excludes a radial zero resonance.

## 4. Completing the full two-dimensional spectral statement

Let (M=\int_{\mathbb R^2}Q^2$. The sharp scalar Gagliardo–Nirenberg constant is (2/M). Testing its quotient on a Gaussian, which is not an optimizer, gives the strict inequality (M<4\pi).

For angular momentum (m\ge1), the zero-energy free radial Green kernel, relative to measure (s\,ds), is

$$
G_m(r,s)=\frac1{2m}\left(\frac{\min(r,s)}{\max(r,s)}\right)^m.
$$

Thus the positive Birman–Schwinger operator obeys

$$
\|QH_{m,0}^{-1}Q\|\le\operatorname{Tr}(QH_{m,0}^{-1}Q)
=\frac{M}{4\pi m}<1.
$$

This excludes negative angular eigenvalues. It also excludes a regular zero solution with decaying (r^{-m}) asymptotics: such a solution has finite homogeneous angular energy, and the strict form bound, applied by cutoff, forces it to vanish. The radial argument handles the bounded (m=0) threshold branch.

Therefore the full two-dimensional operator (h=-\Delta-Q^2$ has exactly one negative eigenvalue (-1), simple, and no bounded zero-energy resonance. In particular its second min-max value is (0), and the earlier ordering assumption

$$
\lambda_2(h)>-k^2
$$

holds automatically for every fixed (0<k<1).

## 5. General power and dimension identity

Let (a=d-1) and suppose a positive strictly decreasing decaying radial ground state exists for

$$
-Q''-a r^{-1}Q'+Q-Q^{\sigma+1}=0.
$$

Set (p=Q'/Q$, (h_d=-\partial_r^2-a r^{-1}\partial_r-Q^\sigma$, and

$$
U_d=a/r^2+2ap/r+2p^2+Q^\sigma-2.
$$

The same factorization holds in $L^2(r^a dr)$, and direct differentiation yields

$$
\boxed{
(r^aQ^2U_d)'=r^aQ^2\left[
\frac{a(a-2)}{r^3}-\frac{aQ^\sigma}{r}
+(\sigma-2)pQ^\sigma\right].
}
$$

For (d=1,2,3$ and (\sigma\ge2$, every term in brackets is nonpositive. The boundary term at infinity vanishes, so (U_d\ge0$. It is strictly positive except for (d=1,\sigma=2$, where it vanishes identically. Consequently (h_d$ has exactly one negative eigenvalue in the radial sector, equal to (-1), and no radial zero eigenfunction. The assertion is conditional on existence of the stated decaying ground state; for example in (d=3) the usual finite-energy range requires (\sigma<4$.

Domain distinctions matter. In (d=1), radial means the even/Neumann half-line sector, and its partner has Dirichlet boundary condition. This statement says nothing about the odd full-line sector; the one-dimensional cubic problem indeed has an odd threshold resonance. In (d=3), the usual threshold resonance behaves like (c/r$, not like a nonzero constant. For this decaying branch, (A\psi\to0$, whereas the negative regular partner solution is strictly decreasing; this excludes the radial threshold resonance. The argument does not exclude ordinary bounded nondecaying zero-energy scattering solutions in three dimensions.

No conclusion about all angular channels in three dimensions follows from this identity alone.

## 6. Prior-work boundary

The three-dimensional cubic radial gap statement for both (L_-=h_3+1) and (L_+=-\Delta+1-3Q^2) was proved by Costin, Huang and Schlag, *On the spectral properties of (L_\pm) in three dimensions*, Nonlinearity 25 (2012), 125–164, [arXiv:1107.0323](https://arxiv.org/abs/1107.0323). Their theorem includes absence of threshold resonances. Li and Yang's *On the gap property of a linearized NLS operator*, [arXiv:2110.14393](https://arxiv.org/abs/2110.14393), treats the fully nonradial three-dimensional cubic problem. Therefore the three-dimensional cubic (L_-) spectral conclusion above is not a newly solved open problem. Whether the present short partner-potential proof and its power-law extension appear in prior literature remains to be determined. The argument above establishes only the (L_-) part, not the (L_+) part or the gap property of the coupled matrix linearization.
