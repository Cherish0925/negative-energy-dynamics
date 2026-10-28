# Periodic endpoint trial: normalization and a rigorous Bloch-cell lower bound

This is an audit of a counterexample search, not a proof or disproof of the sharp two-dimensional endpoint inequality.

## Normalization

Let the columns of a real matrix $A_\Lambda$ generate the direct lattice, let $a=|\det A_\Lambda|$ be its cell area, and put $B=2\pi A_\Lambda^{-T}$. Write the attractive Hamiltonian as $H=-\Delta-V$, with $V\ge0$. Any reciprocal fundamental cell is valid; it need not be the Wigner--Seitz cell. In fractional coordinates $q\in[-1/2,1/2)^2$,

$$
\operatorname{Tr}_{\mathrm{vol}}H_-
=a^{-1}\int_{[-1/2,1/2)^2}\sum_j(-\varepsilon_j(Bq))_+\,dq.
$$

Thus the spectral ratio is

$$
R(V)=\frac{\int_q\sum_j(-\varepsilon_j(Bq))_+\,dq}{\int_C V^2}.
$$

The denominator is the cell integral, not the cell average. For cell area one they coincide. The endpoint target is $1/(2M_c)$, with $M_c=\|Q\|_2^2$.

The normalized plane waves are $a^{-1/2}e^{iBn\cdot x}$, so a finite Galerkin matrix is

$$
H_{nm}(q)=|B(n+q)|^2\delta_{nm}-\widehat V(B(n-m)),\qquad
\widehat V(G)=a^{-1}\int_C V(x)e^{-iG\cdot x}\,dx.
$$

Ritz eigenvalues are upper bounds for the corresponding fiber eigenvalues; their negative sum is therefore a lower bound. One must integrate over quasimomentum. The zero-twist fiber alone does not approximate the periodic trace.

## Lower bound with no assumed quadrature convergence

Partition the fractional reciprocal cell into $m\times m$ equal squares and denote their midpoints by $q_\alpha$. Set

$$
c_m=\frac{\operatorname{tr}(B^TB)}{12m^2}.
$$

Let $\varepsilon_j^G(q_\alpha)$ be the eigenvalues of a finite plane-wave Galerkin matrix at that midpoint. Then

$$
\boxed{\quad
R(V)\ \ge\
\frac{m^{-2}\sum_\alpha\sum_j
 (-\varepsilon_j^G(q_\alpha)-c_m)_+}{\int_CV^2}.
\quad}
$$

Proof: For any fixed finite-rank projector $\Gamma$ on the chosen plane waves,
$\operatorname{Tr}H(q)_-\ge-\operatorname{Tr}(H(q)\Gamma)$.
Average over a patch. The linear momentum term vanishes about its midpoint, and the quadratic kinetic increment has average $c_m I$. Optimizing the fixed projector on that patch gives the negative trace of $H^G(q_\alpha)+c_mI$. Sum the patches. No isolated-band hypothesis, band smoothness, or fixed occupied rank is needed.

For a unit-area square lattice, $c_m=2\pi^2/(3m^2)$. For a unit-area triangular lattice, $c_m=4\pi^2/(3\sqrt3m^2)$. Floating-point eigenvalues and truncated Gaussian denominator sums still require separate error control before this becomes a numerical certificate. Omitting Galerkin modes is conservative; underestimating the denominator is not.

## Analytic periodized Gaussian data

Define $W_\sigma(x)=\sum_{R\in\Lambda}\exp(-|x-R|^2/(2\sigma^2))$. Then

$$
\widehat W_\sigma(G)=\frac{2\pi\sigma^2}{a}e^{-\sigma^2|G|^2/2},\qquad
\int_CW_\sigma=2\pi\sigma^2,
$$

$$
\int_CW_\sigma W_\tau
=\frac{2\pi\sigma^2\tau^2}{\sigma^2+\tau^2}
\sum_{R\in\Lambda}e^{-|R|^2/[2(\sigma^2+\tau^2)]}.
$$

A nonnegative combination of two or three such widths, plus a nonnegative constant, is a low-dimensional way to fit a Townes-shaped well while retaining analytic Fourier coefficients. This family is only a trial class.

## Baseline optimization without repeated eigensolves

For $V=b+W$, the eigenvalues shift by $-b$, whereas
$D(b)=ab^2+2b\int_CW+\int_CW^2$.
After flattening sampled fiber eigenvalues, the numerator on each fixed-occupation interval is $rb-e$, where $r$ includes the quadrature weights. The possible interior stationary point is

$$
b=\frac er+\sqrt{\left(\frac er\right)^2+
\frac{\int_CW^2+2(e/r)\int_CW}{a}}.
$$

Check this point only when real and inside its occupation interval, as well as interval endpoints and $b\ge0$. For the certified patch lower bound, use the shifted base eigenvalues $\varepsilon_j^G+c_m$. Baseline changes then need no new diagonalization.

## Primary source

R. L. Frank, D. Gontier and M. Lewin, *The periodic Lieb--Thirring inequality*, arXiv:2010.02981v2, Theorem 1.1 and equations (1.3)--(1.5): the best periodic constant equals the finite-system constant. Their reported two-dimensional numerical improvements concern exponents near 1.1653, not the endpoint exponent 1.

https://arxiv.org/html/2010.02981v2
