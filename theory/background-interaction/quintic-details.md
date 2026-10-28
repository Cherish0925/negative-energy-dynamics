# Proof details of the exact-Gram quintic matched layer

Date: 2026-10-11. Companion source: [quintic-closure.md](quintic-closure.md). This review re-derives the identities and the asymptotic orders needed for its static theorem. It does not infer the existence of a collapsing trajectory from a family of initial states.

**Verdict:** the stated finite-component static theorem passes this review. In particular the complete Gram matrix is fixed exactly, the matched interaction energy has coefficient **minus** c A lambda, the density has a uniform W^{2,infinity} bound, and the chirp permits exact total-energy matching. The suggested quadratic collapse rate remains an unproved dynamical implication, as the source note states.

## 1. Equation identities and constants

For the one-dimensional mass-critical scalar energy

    E1(u)=1/2 integral |u_x|^2-1/6 integral |u|^6,

write the primary equation with V=2S|u|^2+S^2 as

    i u_t+u_xx+|u|^4u+Vu=0.

Taking the real energy pairing and using rho_t=-2J_x yields

    E1'=1/2 integral V rho_t=integral V_x J.

No V_t term enters, because this is the scalar energy without the extra coupling. Differentiating the primary variance gives

    I1''=16E1+4 integral x V_x rho.

Expanding V and integrating 8 integral x S rho rho_x by parts produces exactly

    I1''=16E1-4 integral S rho^2
                +4 integral x S_x rho^2+8 integral x SS_x rho.

Thus the displayed distinction from the two-dimensional additive-potential equation is correct.

For Q=3^(1/4)sqrt(sech(2y)), the Fourier identity

    integral exp(i xi y) sech(2y)dy=(pi/2)sech(pi xi/4)

at xi=0 and after two derivatives gives

    Mc=pi sqrt(3)/2, V_Q=pi^3 sqrt(3)/32.

## 2. Odd profile and the sign after matching

The substitution z=tanh(2y) converts F''+3 sech^2(2y)F=0 to

    (1-z^2)F_zz-2z F_z+(3/4)F=0.

The odd solution in the reviewed note has the stated normalization. I independently opened NIST DLMF 14.9.10 and 14.8.3. At nu=1/2, mu=0, these give

    P_(1/2)(-z)=-(2/pi)Q_(1/2)(z),
    Q_(1/2)(z)=1/2 log(2/(1-z))-gamma-psi(3/2)
                  +O((1-z)log(1-z)).

Together with 1-tanh(2y)=2e^(-4y)(1+O(e^(-4y))) and psi(3/2)=2-gamma-2log 2, they yield

    F(y)=y+c+O((1+y)e^(-4y)),
    c=pi/4+log 2-1>0

as y tends to positive infinity. The ODE gives the derivative decay needed in the construction. Oddness gives the negative endpoint. Uniqueness follows from uniqueness of an odd ODE solution after fixing its nonzero asymptotic slope.

Put g=F-y. The exact integration-by-parts identity on [-R,R] is

    integral_(−R)^R (F'^2-Q^4F^2-1)
       =F(R)F'(R)-F(-R)F'(-R)-2R.

Its limit is 2c. Moreover integral g'=2c. Hence

    integral (g'^2-Q^4F^2)=2c-2(2c)=-2c.          (A)

The sign is not optional. The positive 2c identity is for the raw inner profile at fixed asymptotic slope. The actual cutoff-matched correction has derivative g', not F'. Substituting the raw identity into the matched energy would reverse the answer incorrectly.

Sources opened for these special-function inputs:
- https://dlmf.nist.gov/14.9.E10
- https://dlmf.nist.gov/14.8.E3

## 3. Complete Gram matrix

For delta=sqrt(lambda), the correction r_j=lambda a_j chi(x/delta)g(x/lambda) is smooth and odd. Since g is bounded and w_j(x)=a_jx+O(x^3),

    ||r_j||_2^2=O(lambda^2 delta),
    |integral w_i conjugate(r_j)|=O(lambda delta^2).

Thus the finite matrix perturbation obeys

    G_tilde-G=O(lambda^2)+O(lambda^(5/2))=O(lambda^2).

On the occupied space G is positive definite. Set H=G^(-1/2)G_tilde G^(-1/2) and B=G^(1/2)H^(-1/2)G^(-1/2). Then

    B G_tilde B*=G,
    B-I=O(lambda^2).

This verifies the formula even when G and G_tilde do not commute. B need not itself be Hermitian; no such condition is required. It is a constant spatial matrix and preserves oddness. The primary is even for every real chirp k, so every primary-secondary Gram entry vanishes exactly. The complete Gram matrix is therefore diag(Mc,G), not merely a matrix with the same trace or approximately the same eigenvalues.

## 4. Secondary energy and mixed nonlinear terms

The derivative is

    r_j'=a_j chi(x/delta)g'(x/lambda)
           +lambda a_j chi'(x/delta)g(x/lambda)/delta.

The first squared term is lambda |a_j|^2 integral g'^2+o(lambda), and the cutoff term is O(lambda^2/delta)=O(lambda^(3/2)). Their cross term is o(lambda); in fact g' is exponentially small on the support of chi'. For the cross term with the unchanged outer field, integration by parts is decisive:

    Re integral w_j' conjugate(r_j')
       =-Re integral w_j'' conjugate(r_j)
       =O(lambda delta^2)=O(lambda^2),

because w_j'' is odd and O(|x|) near zero. This term therefore makes no order-lambda contribution. Consequently the secondary kinetic energy changes by

    (lambda A/2) integral g'^2+o(lambda).

The pure secondary nonlinear energy changes by o(lambda), and the constant Gram correction changes both secondary energy terms by O(lambda^2).

For all real y and small lambda,

    lambda^(-1)|W_lambda(lambda y)|<=C(1+|y|).

At each fixed y the left field converges to a F(y). Exponential decay of Q therefore justifies dominated convergence in

    integral |q_lambda|^4 S_lambda
       =lambda A integral Q^4F^2+o(lambda).

The next mixed term satisfies

    integral |q_lambda|^2 S_lambda^2=O(lambda^4).

Expanding (|q|^2+S)^3 supplies coefficient -1/2 for each mixed integral. Combining the first one with the kinetic correction and (A) gives

    E(U_lambda,0)-E(W)=-c A lambda+o(lambda).

Every retained error is strictly smaller than lambda. The finite-dimensional Gram correction does not alter the coefficient.

## 5. Uniform second derivatives of the density

For the uncorrected fields, W_tilde and W_tilde' are uniformly bounded. In the inner region, the only apparently unbounded second derivative is

    (a_j/lambda)g''(x/lambda).

Writing x=lambda y, its product with W_tilde is bounded by a constant times (1+|y|)|g''(y)|. This is uniformly bounded by the exponential decay from the ODE. The cutoff-second-derivative contribution is O(lambda/delta^2)=O(1), and the term involving chi' g' is exponentially small. The unchanged w_j'' are uniformly bounded.

Multiplication by the uniformly bounded constant B does not affect this reasoning. In

    S_lambda''=2|W_lambda'|^2
                   +2 Re <W_lambda,W_lambda''>,

every term is uniformly bounded. The lower derivative bounds follow from the same estimates. Thus S_lambda is uniformly bounded in W^{2,infinity}, despite the absence of a uniform W^{2,infinity} bound on each field separately. This part of the theorem is valid.

## 6. Chirp and exact energy matching

For the primary phase phi=kx^2/(4lambda), one has phi_x=kx/(2lambda). The unchirped Q profile is real, so the kinetic cross term with the phase is exactly zero. Since the scalar ground-state energy is zero,

    E1(q_lambda,k)=1/2 integral phi_x^2 |q_lambda|^2
                  =V_Q k^2/8.

All nonlinear terms depend only on the density, and all secondary fields are independent of k. Thus the energy contribution is exact for every real k, with an error term independent of k.

If A>0, E(W)-E(U_lambda,0)>0 for all sufficiently small lambda. The chosen negative square root therefore exists and enforces E(U_lambda,k_lambda)=E(W) exactly. Its asymptotic expansion follows directly:

    k_lambda=-sqrt(8cA/V_Q)sqrt(lambda)+o(sqrt(lambda)).

The continuity equation of a pure scaled Q density identifies k with the instantaneous scale velocity: rho_t+2J_x=0 reduces to

    (k-lambda_t)(rho+x rho_x)/lambda=0.

If an actual solution were shown to preserve the energy expansion, matched background, and corresponding modulation accuracy, integrating lambda_t=-sqrt(8cA/V_Q)sqrt(lambda)(1+o(1)) would give lambda~(2cA/V_Q)(T-t)^2. No such trajectory theorem follows from the static family. The reviewed text correctly leaves it as the dynamical problem rather than asserting it has been proved.

## 7. Scope of this verdict

No substantive algebraic, asymptotic, parity, Gram, or regularity gap was found in the stated static theorem. The calculation establishes a negative first-order interaction energy in this matched odd sector. It does not prove a complete asymptotic classification, the existence of a faster critical blow-up solution, stability of such a solution, or historical novelty. Those are separate mathematical tasks, and the reviewed note does not claim them as completed.
