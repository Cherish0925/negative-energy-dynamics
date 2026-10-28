# A chirp normal form at a critical endpoint

Date: 2026-10-11. This note independently continues the R18 rough-background phase calculation. Its new statement is a modulation normal form with a quadratically small scale-equation remainder. It does not prove that the conformal width has a positive limit. All conclusions are conditional on the endpoint decomposition and secondary-gradient bounds already established in R16–R18; no new historical-priority claim is made.

## 1. Equation and exact input

Let d=2, p=2, or d=1, p=4, so dp=4. Consider

    i u_{j,t}+Delta u_j+(sum_k |u_k|^2)^(p/2)u_j=0,
    -Delta Q+Q-Q^(p+1)=0,
    M=||Q||_2^2, I_Q=integral |y|^2 Q(y)^2 dy.

Use the fixed Gram eigenbasis. The principal mass is exactly M, and every secondary mode is L2-orthogonal to the principal mode. The occupation restrictions remain exactly those of the prior notes. Assume the previously established endpoint estimates: there is a primary profile of physical scale lambda_0 tending to zero, center a_0, and normalized H1 error O(lambda_0), and the total secondary H1 seminorm is bounded. A finite number of components is enough for this argument. The Hilbert-valued version follows with the joint bounds already proved in R18.

Define

    Lambda=d/2+y.grad,
    L_+=-Delta+1-(p+1)Q^p, L_-=-Delta+1-Q^p.

Two exact identities drive the argument:

    L_+ Lambda Q=-2Q,
    L_-(|y|^2 Q)=-4 Lambda Q.                         (1)

Also <Q,Lambda Q>=0 and <|y|^2Q,Lambda Q>=-I_Q. The first identity in (1) follows by differentiating the ground-state scaling family; the second follows by differentiating the product |y|^2Q and using L_-Q=0.

## 2. Gauge and the weighted-norm issue

Choose parameters gamma, lambda>0, a in R^d, and real b such that

    u_1=e^(i gamma)lambda^(-d/2)e^(-i b|y|^2/4)(Q+eta),
    y=(x-a)/lambda,

with real L2 orthogonality conditions

    <Im eta,Q>=<Im eta,Lambda Q>=0,
    <Re eta,|y|^2Q>=0,
    <Re eta,partial_k Q>=0, k=1,...,d.              (2)

This fixes d+3 real parameters. At Q, the real scale/translation block is nonsingular: its scale entry is -I_Q and the translation block is the positive Gram matrix of partial_k Q. The imaginary phase/chirp block is nonsingular because <Q,Lambda Q>=0 but <|y|^2Q,Lambda Q>=-I_Q. The implicit function theorem gives a unique nearby gauge after a continuous phase lift is fixed.

It follows from the original approximation that

    lambda/lambda_0=1+O(lambda_0),
    |a-a_0|=O(lambda_0^2), |gamma-gamma_0|+|b|=O(lambda),
    ||eta||_2<=C lambda.                             (3)

For every fixed smooth exponentially decaying weight w, with its polynomial multiples and derivatives,

    ||w eta||_H1<=C_w lambda.                        (4)

A full, unweighted bound ||eta||_H1=O(lambda) is not used and need not follow. Multiplying the residual by the quadratic chirp differentiates to a term b y times that residual. Its global first moment may be large when lambda is much smaller than T-t. In contrast, (4) follows directly from the original H1 error: on exponentially weighted sets multiplication by exp(i b|y|^2/4) costs O(|b|), and the derivative of the phase is harmless. The global L2 norm in (3) is unchanged by this multiplication.

Every modulation pairing is against a Schwartz function, including the quadratic phase. On compact physical-time intervals it is differentiated by the physical H^-1 equation. This justifies locally C1 parameters without assuming the global chirped residual is differentiable in H1.

Let psi_j=lambda^(d/2)u_j(a+lambda y) for j>=2 and S=sum|psi_j|^2. The R18 weighted anchoring argument gives

    sum_(j>=2)||w psi_j||_H1^2<=C_w lambda^2.        (5)

Indeed their gradients have joint size O(lambda), and exact Gram orthogonality combined with (3), |b|=O(lambda), and the exponential moments of Q gives |<psi_j,Q>| with joint size O(lambda). A common phase factor does not change S. Therefore all fixed weighted pairings of

    G=[(|Q+eta|^2+S)^(p/2)-|Q+eta|^p](Q+eta)

are O(lambda^2). In d=2, G=S(Q+eta); in d=1, G=(2|Q+eta|^2 S+S^2)(Q+eta). Weighted Sobolev estimates prove this using (4)–(5).

## 3. Exact modulation equation

Use rescaled time d tau/dt=lambda^(-2), and define

    A=gamma_tau-1,
    D=lambda_tau/lambda+b,
    C=a_tau/lambda,
    K=b_tau+b^2-2bD.

Set P=Q+eta and

    N=|P|^pP-Q^(p+1)-(p+1)Q^p Re eta-iQ^p Im eta.

Direct substitution, with no discarded terms, gives

    i eta_tau-L_+Re eta-iL_-Im eta-A P
       -iD Lambda P-i C.grad P
       +(K/4)|y|^2P-(b/2)(C.y)P+N+G=0.             (6)

The sign of K can be checked on a chirped exact scaled profile with lambda_tau/lambda=-b: the quadratic coefficient is then (b_tau+b^2)/4. The center term -(b/2)(C.y)P is retained in (6).

The real and imaginary equations are

    -(Im eta)_tau-L_+Re eta-A(Q+Re eta)
       +D Lambda Im eta+C.grad Im eta
       +(K/4)|y|^2(Q+Re eta)
       -(b/2)(C.y)(Q+Re eta)+Re(N+G)=0,              (7)

    (Re eta)_tau-L_-Im eta-A Im eta
       -D Lambda(Q+Re eta)-C.grad(Q+Re eta)
       +(K/4)|y|^2 Im eta-(b/2)(C.y)Im eta
       +Im(N+G)=0.                                 (8)

All nonlinear Taylor-remainder pairings in these equations are O(lambda^2), by (3)–(4). No uniform global H1 norm of eta is invoked.

## 4. The two cancellations

Project (7) on Lambda Q. The time derivative vanishes by (2). Exact mass conservation yields

    2<Re eta,Q>+||eta||_2^2=0.

Using L_+Lambda Q=-2Q removes the entire linear amplitude term, leaving the exact relation

    (I_Q/4)K
      = <Re(N+G),Lambda Q>-||eta||_2^2
        -A<Re eta,Lambda Q>
        +D<Lambda Im eta,Lambda Q>
        +C.<grad Im eta,Lambda Q>
        +(K/4)<|y|^2 Re eta,Lambda Q>
        -(b/2)C.<y Re eta,Lambda Q>.                (9)

The leading constant center term vanishes by radial parity. This is the critical-mass cancellation: no linear amplitude error remains in the chirp equation.

Next project (8) on |y|^2Q. Its time derivative vanishes by (2), and (1) removes the entire linear imaginary-error term. The leading translation term vanishes by parity. Thus

    I_Q D
      = A<Im eta,|y|^2Q>
        +D<Lambda Re eta,|y|^2Q>
        +C.<grad Re eta,|y|^2Q>
        -(K/4)<|y|^2 Im eta,|y|^2Q>
        +(b/2)C.<y Im eta,|y|^2Q>
        -<Im(N+G),|y|^2Q>.                         (10)

Projecting (7) on Q and (8) on partial_k Q gives, for lambda small,

    |A|<=C(lambda+|K|)+C lambda(|D|+|C|+|A|),
    |C|<=C lambda+C lambda(|A|+|D|+|C|+|K|).

Equations (9)–(10), (3)–(5), and absorption now imply

    |A|+|C|<=C lambda,
    |D|+|K|<=C lambda^2.                            (11)

Since b=O(lambda), 2bD=O(lambda^3). Consequently

    lambda lambda_t+b=O(lambda^2),
    lambda^2 b_t+b^2=O(lambda^2).                   (12)

This is the claimed chirp normal form. Compared with a scale equation tested against a generic gauge, its mismatch is quadratic rather than linear in the normalized profile error.

The phase estimate in this gauge is only |gamma_tau-1|=O(lambda). The stronger R18 phase-defect statement used a different real scale gauge, perpendicular to Q^(p+1), and cannot be transferred to (2) without checking the integrated scale change. The two gauges serve different cancellations.

## 5. Conformal version and its precise limitation

Apply the same construction to the conformal primary at large time s. R18 supplies a profile of scale 0<mu<=C, bounded center, and weighted normalized error O(mu/s). Removing the secondary quadratic phase before applying the anchoring lemma gives the same secondary bound. Thus, with d tau/ds=mu^(-2),

    |b|<=C mu/s,
    mu mu_s+b=O(mu^2/s^2),
    mu^2 b_s+b^2=O(mu^2/s^2).                      (13)

The leading chirp Riccati remainder is still of physical conformal-time size s^(-2). No second spatial derivative of the background has been used.

These estimates do not force a positive limiting mu. For example, for any alpha>0, the functions

    mu(s)=s^(-alpha), b(s)=alpha mu(s)^2/s

satisfy the size bounds and the first relation in (13) exactly. The second left-hand side is

    mu^2 b_s+b^2=-alpha(alpha+1)mu^4/s^2,

which obeys the asserted remainder bound. This is an example of compatible parameter functions, not a solution of the coupled PDE. It proves only that (13) alone does not exclude conformal shrinkage.

## 6. Why Gram orthogonality supplies no sign for the forcing

In the cubic case, the leading term in (9) contributed by the background is

    (4/I_Q) integral S Q Lambda Q.                 (14)

For smooth S, integration by parts gives the equivalent form

    integral S Q Lambda Q=-(1/2)integral Q^2 y.grad S.

The first form makes sense at the available regularity. It has no universal sign even for exact Gram-orthogonal secondary modes.

A rigorous static demonstration in d=2 is as follows. Q is positive, smooth and radial. Q Lambda Q is positive in a sufficiently small punctured neighborhood of the origin; it is negative on some radial annulus, since integral Q Lambda Q=0, it is continuous, and it is strictly positive near the origin. Choose a nonzero smooth radial bump f supported in either region, away from the origin, and put

    psi(r,theta)=f(r)e^(i theta).

Then <psi,Q>=0 exactly by angular integration, while integral |psi|^2 Q Lambda Q has the sign of the chosen region. Normalize and multiply psi by any desired sufficiently small occupation amplitude. This obeys the small-occupation condition and can be realized as smooth initial data with primary exactly Q. At that instant eta=b=0, and (9) gives the sign in (14) exactly. In d=1, a smooth odd secondary bump supported in two symmetric intervals gives the same conclusion for the leading quintic forcing 2Q^3 S.

Therefore a one-sided chirp acceleration cannot follow from positivity of S and Gram orthogonality alone. This is not a counterexample to a universal endpoint theorem: the constructed instantaneous data are not asserted to produce any specified terminal behavior. It identifies the missing input as time-dependent control, rather than a static sign concealed in the orthogonality constraint.

## 7. Consequence for the research direction

The exact critical mass gives a second useful cancellation in addition to R18's phase cancellation. It produces a clean scale/chirp system at the original H1 regularity and isolates its background term. It also shows exactly why the rough-background question remains: the leading background force can have either sign and remains at the borderline temporal order allowed by the existing estimates.

A further proof must use an additional dynamical property of the secondary equation—for example, quantitative exclusion of persistent secondary kinetic concentration on the shrinking principal scale. Such a property has not been proved in this note. Merely differentiating the same modulation system again or replacing the background by a smooth potential would not establish the original rough-background statement.
