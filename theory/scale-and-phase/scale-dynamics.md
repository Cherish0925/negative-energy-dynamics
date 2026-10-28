# Differentiable core parameters and convergent phase defects

Date: 2026-10-10. This note continues the proved endpoint decomposition in R16/R17. It supplies a phase refinement for the two-dimensional cubic and one-dimensional quintic common-density systems. It does not prove convergence of the core width under the original H1 assumptions. Section 7 independently closes the phase of a fixed-width conformal soliton if a separate regular-background argument supplies the stronger amplitude and scale estimates stated there.

## 1. Equations and inputs

Write d=2, p=2, or d=1, p=4, and consider

    i u_{j,t}+Delta u_j+(sum_k |u_k|^2)^(p/2) u_j=0,
    -Delta Q+Q-Q^(p+1)=0,     Mc=||Q||_2^2.

There are finitely many components. Work in the fixed Gram eigenbasis, with principal mass Mc and exactly orthogonal secondary modes. The admissible spectra are those established in R16/R17: in two dimensions, all secondary eigenvalues are at most epsilon0 Mc; in one dimension, the largest Gram eigenvalue is simple. The one-dimensional use of the full occupation range retains R17's explicit dependence on Read--Schulz arXiv:2609.10478v2.

Let T be a finite forward H1 endpoint. The inputs from the preceding notes are:

1. The secondary gradients are uniformly bounded on a terminal interval.
2. There is a whole-trajectory scalar approximation

       u_1=e^(i theta_0) lambda_0^(-d/2)
                 [Q+epsilon_0]((x-a_0)/lambda_0),
       ||epsilon_0||_H1<=C lambda_0,
       lambda_0(t)->0, lambda_0(t)<=C(T-t).

3. The principal component has automatic centered variance O((T-t)^2), and a_0 approaches the unique concentration point x_* at rate O(T-t).

Constants below depend on the individual solution and spectrum, but are uniform as t approaches T. This note does not replace the variational input or enlarge its two-dimensional occupation range.

## 2. A weighted anchoring lemma

Let Q be the positive exponentially decaying ground state above. For each fixed smooth exponentially decaying weight w, and f in H1(R^d), d=1 or 2,

    ||w f||_H1 <= C_w (||grad f||_2+|<f,Q>|).              (A)

The assertion holds for any fixed finite collection of exponentially decaying weights and their derivatives. No unweighted L2 term occurs on the right.

Here is a proof covering the borderline two-dimensional case. Let c be the average of f on the unit ball. On the ball of radius R>=1, Poincare's inequality and telescoping averages over dyadic balls give

    ||f-c||_(L2(B_R)) <= C R (1+log(2R)) ||grad f||_2

in d=2. The exact power and logarithm are immaterial; a polynomial upper bound suffices. In d=1, the fundamental theorem of calculus and Cauchy--Schwarz give the analogous polynomial bound. Split space into unit/dyadic annuli and use the exponential decay of Q. It follows that

    |<f-c,Q>| <= C ||grad f||_2.

Since integral Q is positive, |c|<=C(|<f,Q>|+||grad f||_2). Applying the same annular estimate to w and grad w gives ||w f||_2 and ||(grad w)f||_2 bounded by the right side of (A); ||w grad f||_2 is bounded directly. Density extends the argument from smooth f to H1. Complex-valued f are handled by their real and imaginary parts.

Sobolev embedding applied to w f gives weighted local Lq control for every finite q when d=2, and weighted local Linfinity control when d=1. These are the only embeddings used below.

For a rescaled secondary family

    psi_j(y)=lambda^(d/2) u_j(a+lambda y), j>=2,

we have sum ||grad psi_j||_2^2<=C lambda^2. If the normalized primary differs from Q by O(lambda) in L2, exact Gram orthogonality gives

    |<psi_j,Q>|<=||psi_j||_2 O(lambda).

Therefore (A), summed over the finite family, implies

    sum_(j>=2) ||w psi_j||_H1^2 <= C_w lambda^2.            (B)

The constants can depend on the finite total secondary mass. The estimate does not require pointwise traces of secondary H1 fields in dimension two. In particular it avoids using the false two-dimensional embedding H1 into C0.

## 3. Choice and regularity of the modulation parameters

For all sufficiently late t, choose the parameters theta(t), lambda(t)>0, a(t) so that

    u_1(t,x)=e^(i theta(t))lambda(t)^(-d/2)[Q+epsilon(t)](y),
    y=(x-a(t))/lambda(t), epsilon=epsilon_R+i epsilon_I,

and impose the explicit gauge

    <epsilon_I,Q>=0,
    <epsilon_R,Q^(p+1)>=0,
    <epsilon_R,partial_k Q>=0, k=1,...,d.                 (C)

All inner products in (C) are real L2 pairings. This is a normalization of the core parameters, not an extra assumption on the solution.

The Jacobian with respect to phase, logarithmic scale and translation at Q is block diagonal by parity. Its relevant entries are ||Q||_2^2, the positive matrix <partial_j Q,partial_k Q>, and

    <Lambda Q,Q^(p+1)>
      = [d/2-d/(p+2)] integral Q^(p+2)>0,
    Lambda=d/2+y.grad.

The implicit function theorem thus supplies locally unique nearby parameters satisfying (C). Parameters on overlapping intervals agree after choosing a continuous lift of the phase. They satisfy

    lambda/lambda_0=1+O(lambda_0),
    |a-a_0|=O(lambda_0^2),
    |theta-theta_0|=O(lambda_0),
    eta(t):=||epsilon(t)||_H1<=C lambda(t).                 (D)

The local modulation functions are C1 in time. For completeness, the H1 solution is C1 into H^-1; each defining pairing in (C), with its scaled Schwartz test function, is differentiable by the equation. The finite-dimensional Jacobian remains invertible. The ordinary implicit differentiation argument therefore applies to those pairings even though the full H1-valued solution need not be C1 into H1.

The scale in (C) is not identically the gradient-normalized scale used initially in R16/R17. One must not transfer the phase estimate below to a different scale without estimating the change in the integrated reciprocal square.

## 4. The rescaled forcing is quadratic in the endpoint error size

Set S(y)=sum_(j>=2)|psi_j(y)|^2, and q=Q+epsilon. In rescaled coordinates the additional coupling in the principal equation is

    G=((|q|^2+S)^(p/2)-|q|^p)q.

For d=2, G=S q. For d=1, G=(2|q|^2 S+S^2)q. From (B), the weighted Sobolev bounds and ||epsilon||_H1<=C lambda, for each of the fixed tests

    Z in {Q, Q^(p+1), partial_1 Q,...,partial_d Q}

we obtain

    |<G,Z>| <= C lambda^2.                                (E)

For example, in d=2 the Q part is a weighted integral of S, of size O(lambda^2); the epsilon part is bounded by weighted Holder and H1-to-L4 estimates, giving O(lambda^3). In d=1, the leading 2 Q^3 S contribution is O(lambda^2), and all other terms have at least this order by the weighted Linfinity estimate. Polynomial factors from derivatives of Q may be absorbed into slightly weaker exponential weights.

Similarly, the scalar nonlinear Taylor remainder

    N=|Q+epsilon|^p(Q+epsilon)-Q^(p+1)
                  -(p+1)Q^p epsilon_R-i Q^p epsilon_I

satisfies |<N,Z>|<=C eta^2 for the same tests. Thus each tested nonlinear remainder is O(lambda^2). These are weak tested estimates, not an assertion that the entire coupled nonlinearity has a small global H1 norm.

## 5. Modulation equations and the phase cancellation

Define

    L_+=-Delta+1-(p+1)Q^p,  L_-=-Delta+1-Q^p,
    A=lambda^2 theta'-1, B=lambda lambda', C=lambda a'.

Direct substitution in the principal equation gives

    i lambda^2 epsilon_t-L_+ epsilon_R-i L_- epsilon_I
        -A(Q+epsilon)-i B Lambda(Q+epsilon)
        -i C.grad(Q+epsilon)+N+G=0.                        (F)

The real and imaginary parts are respectively

    -lambda^2 (epsilon_I)_t-L_+epsilon_R-A(Q+epsilon_R)
        +B Lambda epsilon_I+C.grad epsilon_I+Re(N+G)=0,

    lambda^2 (epsilon_R)_t-L_-epsilon_I-A epsilon_I
        -B Lambda(Q+epsilon_R)-C.grad(Q+epsilon_R)
        +Im(N+G)=0.

Project the real equation onto Q. The differentiated phase condition removes the time-derivative term. The exact identity

    L_+ Q=-p Q^(p+1)

and the scale orthogonality in (C) remove the entire linear epsilon_R term. Consequently

    |A| <= C[(|B|+|C|)eta+lambda^2].                      (G)

Project the imaginary equation onto Q^(p+1) and partial_k Q. The differentiated real orthogonality conditions remove the time derivatives. The invertible matrix described in Section 3 gives

    |B|+|C| <= C eta+C eta(|A|+|B|+|C|)+C lambda^2.       (H)

For eta small, (G)--(H) imply

    |B|+|C|<=C lambda,  |A|<=C lambda^2.

Therefore

    |lambda'(t)|+|a'(t)|<=C,
    |theta'(t)-lambda(t)^(-2)|<=C.                         (I)

This proves that a C1, uniformly Lipschitz scale and center can be selected near every admissible finite endpoint. More importantly, there is a finite real phase defect theta_* such that

    theta(t)-integral_(t_a)^t lambda(r)^(-2)dr
           =theta_*+O(T-t).                               (J)

The phase is a continuous real lift. The value theta_* changes by a constant if the lift or lower integration limit is changed. No conclusion lambda(t)/(T-t)->constant follows from (I) or (J).

## 6. A conformal phase defect without a positive lower scale bound

Apply R17's principal conformal transform about (T,x_*): h=T-t, s=1/h,

    v_1(s,y)=h^(d/2)exp(i h|y|^2/4)u_1(T-h,x_*+h y).

The whole principal field belongs to H1 by its automatic variance. The secondary conformal fields need not belong to H1 if they lack finite physical variance; this does not prevent the following local tested principal equation.

R17 gives a modulated Q approximation with bounded center and bounded positive scale mu, whose normalized H1 error is O(mu/s). To check the sharper normalized estimate explicitly, the physical residual has L2 norm O(lambda), bounded gradient and position norm O(h). After conformal transformation its L2 norm is O(lambda)=O(mu/s), and its gradient norm is O(1/s). Rescaling by mu gives an H1 error O(mu/s). Removing the core's nonconstant quadratic phase has the same bound because the center and mu are bounded and Q has exponential moments.

Apply the gauge (C) to this approximation. Then

    0<mu(s)<=C, |a(s)|<=C,
    ||epsilon(s)||_H1<=C mu(s)/s.                          (K)

The secondary anchoring bound also has size O((mu/s)^2), although their global conformal gradients need not be O(1/s). To see this correctly, remove their common quadratic phase before applying (A). In rescaled coordinates their modulus is that of

    chi_j(z)=(h mu)^(d/2)u_j(T-h,x_*+h a+h mu z),

whose gradients have norm O(h mu), and whose Q pairings are O(h mu) by exact physical Gram orthogonality and the corresponding physical primary approximation. The difference between that primary approximation and the conformal one is a quadratic phase with normalized weighted size O(h mu). Thus (B)--(E) apply with lambda replaced by mu/s. It would be incorrect to infer this estimate directly from a global conformal H1 bound on secondary fields.

Equations (F)--(H), now with time s and scale mu, prove

    |mu'(s)|+|a'(s)|<=C/s,
    |vartheta'(s)-mu(s)^(-2)|<=C/s^2.                      (L)

There is consequently a finite conformal phase defect vartheta_* satisfying

    vartheta(s)-integral_(s_a)^s mu(r)^(-2)dr
         =vartheta_*+O(1/s).                              (M)

The width mu may still approach zero. The estimate is uniform through that possibility because it controls the dimensionless phase equation at order (mu/s)^2 before dividing by mu^2. Equations (L)--(M) give a precise phase law relative to the explicitly normalized core width, not a fixed-frequency standing-wave classification.

## 7. Independent phase closure under a regular-background fixed-width theorem

This section is a conditional implication and does not assert its hypotheses follow from H1 alone. Suppose a separate argument for a conformal principal field provides, as s tends to infinity,

    v_1(s)=e^(i theta_0(s))mu_0(s)^(-d/2)
                  Q((.-a_0(s))/mu_0(s))+r_0(s),
    ||r_0(s)||_H1=O(s^-2),
    mu_0(s)=mu_*+O(s^-2),  mu_*>0,

with bounded centers, and a principal extra real potential V_conf whose tested coupling is O(s^-2). In particular, in the two-dimensional cubic system a physical secondary density bounded in Linfinity gives

    V_conf(s,y)=s^-2 S(T-1/s,x_*+y/s),
    ||V_conf(s)||_infinity<=C s^-2.

Use either gauge (C) or the usual scale gauge Re epsilon perpendicular to Lambda Q. Since the scale is bounded above and below, the implicit function theorem changes theta_0, mu_0 and a_0 by O(s^-2), while the normalized error remains O(s^-2). The ordinary modulation system gives

    |vartheta'(s)-mu(s)^(-2)|<=C s^-2.

Here no special quadratic cancellation is required: the linear epsilon term is already O(s^-2), and the external forcing has that size. Since mu(s)-mu_*=O(s^-2),

    |vartheta'(s)-mu_*^(-2)|<=C s^-2.

It follows rigorously that

    vartheta(s)=s/mu_*^2+vartheta_*+O(1/s).                (N)

This supplies the missing fixed frequency and phase offset if the stated amplitude and width estimates have already been proved. A mere convergence mu(s)->mu_* without an integrable rate would not suffice for (N); it would only give the integral phase law. Center convergence, and its rate if a fixed spatial soliton is desired, must likewise come from the separate dynamical argument.

## 8. What has and has not changed

Under the original R16/R17 endpoint assumptions, this note adds a differentiable core choice, a Lipschitz physical scale and center, an O(T-t) convergent physical phase defect, and an O(1/s) convergent conformal phase defect. The result uses the exact critical identity L_+Q=-pQ^(p+1), the full Gram orthogonality, and an anchored weighted estimate for the secondary fields.

These calculations do not remove rough-background conformal grow-up or prove universal exact pseudoconformal width. The local forcing is of the borderline order s^-2, and a width shrinking to zero is compatible with the proved bounds on its derivative. No new classification of all critical dispersive systems, and no resolution of the original nonradial BNLS question, is claimed here. The special gauge must be retained in any statement of the quantitative phase result. Historical novelty has not been established by this calculation alone.
