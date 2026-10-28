# Compact radial states, component virials, and the angular obstruction

Date: 2026-10-15. This note concerns the two-dimensional cubic common-density
system. It proves identities for exact stationary profiles and records a small
radial Galerkin experiment. It does not prove the two-dimensional exponent-one
Lieb–Thirring conjecture. Historical originality of the identities below has not
been established.

## 1. Exact setting and the radial rank-two restriction

Let real smooth exponentially decaying profiles solve

    -Delta u_i - rho u_i = -e_i u_i,   rho=sum_j u_j^2,   e_i>0.

Write M_i=int u_i^2 and T_i=int |grad u_i|^2. In the equal-occupation optimizing
problem, int u_i u_j=beta delta_ij and beta=2/C. A strict improvement over the
one-state quotient would have beta<M_c, where -Delta Q+Q-Q^3=0 and M_c=int Q^2.

Existing finite-rank optimizer theory supplies occupation of the lowest
eigenvalues of -Delta-rho and a strict gap above the occupied space. For a
radial potential in two dimensions, every nonzero angular-momentum eigenvalue
has multiplicity at least two, whereas the lowest eigenvalue is simple and
radial. Therefore a **radial rank-two optimizer** must occupy two radial m=0
eigenfunctions. It cannot occupy just one of an m=1 pair.

This does not prove that rank-two optimizers are radial. Nor does it prove that
the first m=1 level lies below the second m=0 level. A level-ordering assertion
requires additional potential hypotheses; no such ordering is assumed here.

## 2. A componentwise virial identity in two dimensions

Assume all u_i are radial and the nonzero components have distinct e_i. Put

    W_ij = u_i u_j' - u_i' u_j,
    G_i = u_i'^2 - e_i u_i^2 + (1/2)u_i^2 rho
          + (1/2)sum_(j!=i) W_ij^2/(e_i-e_j).

The radial equations give, by direct differentiation,

    W_ij' = (e_j-e_i)u_i u_j - W_ij/r,
    G_i' = -2u_i'^2/r - sum_(j!=i)W_ij^2/[r(e_i-e_j)],
    (r^2 G_i)' = r u_i^2 (rho-2e_i).                 (1)

Every term is regular at zero: u_i'(0)=0 and W_ij=O(r). Exponential decay at
infinity gives r^2G_i -> 0 at both endpoints. Integrating (1), multiplying by
2pi, and then multiplying the PDE by u_i proves **for each component**

    int rho u_i^2 = 2e_i M_i,       T_i=e_i M_i.      (2)

Thus the usual summed Pohozaev relation separates component by component in
this radial two-dimensional cubic setting. The cancellation is specific: it
uses the cubic common density and the coefficient 1/r of radial friction.

Distinct frequencies cause no loss for an orthogonal family consisting entirely
of radial functions. If e_i=e_j, then (r W_ij)'=0. Regularity at zero forces
W_ij=0, so the radial solutions are proportional by uniqueness of their scalar
linear ODE, and cannot be nonzero orthogonal components.

The two-component differentiation in (1) was additionally checked by exact
SymPy substitution; both residual polynomials simplify to zero. The proof is
the displayed differentiation and endpoint integration, not that symbolic test.

## 3. What replaces (2) without radial symmetry

There is an exact formula for the missing term. Define the mixed vector field

    J_ij = u_i grad u_j - u_j grad u_i,
    div J_ij = (e_j-e_i)u_i u_j,
    omega_ij = partial_1 J_(ij,2) - partial_2 J_(ij,1).

Separate Pohozaev identities, obtained by multiplying the i-th PDE by
x dot grad u_i, yield

    T_i-e_i M_i = -sum_(j!=i) D_ij,
    D_ij = int u_i u_j (x dot J_ij).                (3)

For completeness, set R_i=int rho u_i^2 and
K_ij=int u_i^2 u_j(x dot grad u_j). In d=2,
K_ij+K_ji=-int u_i^2u_j^2, K_ii=-(1/2)int u_i^4,
and D_ij=K_ij-K_ji. Hence sum_j K_ij=-R_i/2+(1/2)sum_(j!=i)D_ij.
The separate Pohozaev equation is -e_iM_i+R_i+sum_j K_ij=0, whereas the
component equation gives T_i+e_iM_i=R_i. These prove (3).

For any smooth decaying vector field J in two dimensions, integration by parts
gives

    int (x dot J) div J = int (x_1 J_2-x_2 J_1) curl J.      (4)

Indeed the two terms involving int |J|^2 cancel precisely in dimension two.
For distinct e_i, equations (3)-(4) give

    T_i-e_i M_i
      = sum_(j!=i) [1/(e_i-e_j)]
          int (x_1 J_(ij,2)-x_2 J_(ij,1)) omega_ij.          (5)

For radial profiles J_ij is radial and the right side vanishes. Equation (5)
identifies an angular mixed-current contribution that a nonradial argument must
control; it does not establish its sign. These are mixed currents of real
orbitals, not the quantum probability current of an individual real wave.
If frequencies coincide, (3) remains valid but division in (5) is unavailable.

## 4. A frequency restriction for exact radial equal-mass states

Let M_i=beta. From (2), R_i=2beta e_i and F=int rho^2=2beta sum_j e_j.
Cauchy–Schwarz applied to rho and u_i^2, followed by the sharp scalar
Gagliardo–Nirenberg inequality, gives

    (2beta e_i)^2 <= F int u_i^4,
    int u_i^4 <= (2beta/M_c)T_i = 2beta^2 e_i/M_c.

Consequently

    beta/M_c >= e_i/(sum_j e_j) for each i.         (6)

For rank two, with e_1>e_2, the inequality is strict. Equality in the first
Cauchy inequality would make rho proportional to u_1^2, hence u_2^2 a constant
multiple of u_1^2. Since the first occupied eigenfunction u_1 is strictly
positive, continuity would make u_2 proportional to u_1, contrary to
orthogonality. Therefore

    beta/M_c > e_1/(e_1+e_2),
    delta := M_c/beta-1 < e_2/e_1.                  (7)

This is a restriction on any exact radial two-component optimizing candidate:
a fixed nonzero improvement requires the binding frequencies to be comparable.
It does not exclude arbitrarily small improvement with extreme scale separation,
and it does not apply unchanged to nonradial profiles because (5) then enters.

## 5. An exact angular translation test

For a radial stationary family, independently translate the components to first
order, h_i=a_i partial_1u_i. These are tangent to every Gram constraint because
the inner product of a radial function and its first derivative is zero.
For E(U)=sum_i T_i-(1/2)int rho^2, the constrained quadratic form is

    Q(h)=sum_i <h_i,(-Delta-rho+e_i)h_i>
         -2 int (sum_i u_i h_i)^2.

Differentiating the stationary equations and collecting the terms gives

    Q(h)=2 sum_(i<j) I_ij (a_i-a_j)^2,
    I_ij=int u_i partial_1u_i u_j partial_1u_j
        =pi int_0^infinity r u_i u_i' u_j u_j' dr.           (8)

A constrained local minimizer must make this weighted graph quadratic form
nonnegative. In rank two it requires I_12>=0. The common translation is exactly
the zero direction a_1=a_2. No sign theorem for I_12 follows from (2) or (6).
In particular this note does not turn the translation zero mode into a strict
instability merely by counting components.

## 6. Actual radial Galerkin experiment and its interpretation

The script r23_radial_compact.py uses the whole-plane radial basis

    g_n(r)=pi^(-1/2) exp(-r^2/2) L_n(r^2),  n=0,...,d.

Coefficient polar normalization enforces exact continuum orthonormality in exact
arithmetic. Kinetic integrals use their analytic tridiagonal matrix, and quartic
integrals use Gauss–Laguerre quadrature of sufficient degree. Six real rank-two
runs were performed: d=20,40,60 with seeds 13 and 31. Their quotients agree
between seeds to about 1e-12 and are below C_1=0.17092707344864.

| degree | quotient F/T | first occupied multiplier | second occupied multiplier | rms core radius | rms diffuse radius |
|---|---:|---:|---:|---:|---:|
| 20 | 0.16725468382456 | -4.86188017 | +0.03835809 | 0.50362 | 4.90210 |
| 40 | 0.16978028280241 | -6.58089304 | +0.01390193 | 0.42750 | 6.55785 |
| 60 | 0.17036445462266 | -8.16774401 | +0.00728635 | 0.38258 | 7.82085 |

An independent 30001-point radial quadrature up to r=35 reproduced F/T within
2.1e-11 and the Gram matrix within 1.9e-11. These are floating-point checks,
not interval-certified enclosures. Positive second multipliers and growing
scale separation show that these are not exact compact two-bound-state
optimizers. Finite Galerkin stationarity must not be used in (2).

The m=1 angular Hessian has negative computed directions, but the negative
eigenvalues shrink with degree and the profiles themselves are not continuum
stationary solutions. Thus this experiment gives no theorem excluding exact
compact radial states. The relative-translation I_12 is positive in these
examples, so the simple exact test (8) would not resolve them even if they were
stationary. Further repetitions of the same radial maximization are not an
identified path to the global theorem.

## 7. Sources and what remains open

1. R. L. Frank, D. Gontier, M. Lewin, *Optimizers for the finite-rank
   Lieb–Thirring inequality*, Amer. J. Math. 147 (2025), 503–560.
   https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-frank-gontier-lewin-FINAL.pdf
   Finite-rank existence, self-consistency, and the occupied spectral gap are
   existing results, not new results of this note.
2. A. Levitt, *Best constants in Lieb–Thirring inequalities: a numerical
   investigation*, J. Spectr. Theory 4 (2014), 153–175.
   https://ems.press/content/serial-article-files/33509
   Radial self-consistent searches and splitting under nonradial perturbations
   have already been investigated there.
3. B. Chen, Y. Guo, Y. Luo, J. Wei, *Cubic Nonlinear Schrödinger Systems and
   Orthonormal Fermionic Ground States in R*, arXiv:2610.17941v1, submitted
   2026-10-13. https://arxiv.org/html/2610.17941v1
   This newly located preprint claims arbitrary-rank one-dimensional cubic
   classification, mass identities and a local transition near the cubic
   exponent. It is not a two-dimensional endpoint result. Its full proof has
   not been independently checked here. Classical first integrals of coupled
   cubic ODEs motivate G_i; no novelty assertion is made for that antecedent.

The concrete analytical gain in this note is the complete derivation of
(2)-(7), including the nonradial angular term. The decisive missing step is a
sign or coercivity argument that excludes all compact self-consistent improving
profiles. Neither the identities nor the numerical runs supply it.
