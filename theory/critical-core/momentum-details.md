# R17 Proof details: core velocity and angular-momentum transfer

Date: 2026-10-09. This note checks the root derivation of a first-order collapse trajectory and angular-momentum splitting. Its inputs are [threshold-rigidity.md](../occupation-thresholds/threshold-rigidity.md), [primary-variance-details.md](primary-variance-details.md), and the finite-variance secondary convergence in [critical-rate.md](critical-rate.md).

## 1. Setup and precise statements

Consider the finite-component, two-dimensional common-density focusing cubic system under the R16 separated-largest-occupation assumptions, at the exact fixed-spectrum threshold. Work in the constant Gram eigenbasis. The principal mode u_1 has mass Mc, and a finite forward H1 blowup occurs at T and x_*. Put h=T-t.

Use momentum and scalar angular momentum in the conventions

    P(f)=Im integral conjugate(f) grad f,
    L_a(f)=Im integral conjugate(f) [(x-a) cross grad f],
    x cross y=x_1 y_2-x_2 y_1.

For vector fields, sum these quantities over the components. Write L=L_0. Total momentum P_tot is conserved. R16 gives secondary limits w_j in H1 with

    u_j(t)->w_j strongly in H^sigma for every sigma<1,
    u_j(t) weakly ->w_j in H1,                  j>=2.

Set W=(0,w_2,...,w_k) and

    P_*:=P_tot-P(W).

The audited conclusions are:

    P(u_1(t))->P_*,
    b_1(t):=Mc^(-1) integral x |u_1(t,x)|^2 dx
       =x_*-(2P_*/Mc)(T-t)+o(T-t),                         (1)

and every R16 modulation center x_c(t), with its accompanying phase and scale satisfying the stated quantitative Townes approximation, obeys

    x_c(t)=x_*-(2P_*/Mc)(T-t)+o(T-t).                       (2)

The primary angular momentum about the collapse point satisfies

    L_(x_*)(u_1(t))=O(T-t)->0.                             (3)

If all secondary modes have finite variance at one lifespan time, then total angular momentum is defined and conserved, and

    L_tot=x_* cross P_*+L(W).                              (4)

Equivalently, all angular momentum about the collapse point is retained by the limiting background:

    L_tot-x_* cross P_tot=L_(x_*)(W).                      (5)

The velocity in (2) is an asymptotic displacement coefficient. Differentiability or pointwise convergence of x_c'(t) is not asserted.

## 2. Momentum limit from strong H^(1/2) convergence

For an H1 scalar field, Plancherel gives

    P(f)=integral xi |Fourier(f)(xi)|^2 d xi.

The same quadratic form extends continuously to H^(1/2). In particular,

    |P(f)-P(g)|
       <=||f-g||_(dot H^(1/2))
           [||f||_(dot H^(1/2))+||g||_(dot H^(1/2))].

R16 strong secondary H^(1/2) convergence therefore implies P_sec(t)->P(W). Translation invariance of the common-density Hamiltonian gives conservation of P_tot for the H1 vector solution. Consequently

    P(u_1(t))=P_tot-P_sec(t)->P_*.

This avoids estimating the time derivative of the primary momentum or requiring integrability of the force transferred between components.

## 3. Primary centroid and its first-order terminal expansion

The independent primary-variance result gives

    ||(x-x_*)u_1(t)||_2<=4sqrt(E)h.                         (6)

Thus the primary first moment is absolutely integrable, and

    |b_1(t)-x_*|<=4sqrt(E/Mc)h.

The individual continuity equation is

    partial_t |u_1|^2+2 div J_1=0.

Apply it first to smooth bounded truncations of the coordinate functions x_l. On every compact lifespan time interval, H1 continuity provides uniform H1 bounds, while (6) provides a uniform second-moment bound. The cutoff first moments and their distributional derivatives pass to the limit by Cauchy--Schwarz and dominated convergence. Hence b_1 is locally absolutely continuous and

    b_1'(t)=2P(u_1(t))/Mc.                                 (7)

The primary momentum is bounded up to T, since it is total momentum minus the uniformly bounded secondary momentum. Since b_1(t)->x_*, integration of (7) gives the exact identity

    b_1(t)=x_*-(2/Mc) integral_t^T P(u_1(r)) dr.

The momentum limit from Section 2 proves (1). No conservation of the individual primary momentum is presumed.

## 4. The modulation center and centroid agree to second order

At each sufficiently late time, use the R16 decomposition

    u_1=a+e,
    a(t,x)=exp(i theta(t))lambda(t)^(-1)
                      Q((x-x_c(t))/lambda(t)).

The R16 and R17 estimates give

    ||e||_2<=C lambda,
    ||grad e||_2<=C,
    lambda<=C h,
    |x_c-x_*|<=C h.                                       (8)

The Townes profile is radial, real up to the constant phase, exponentially decaying, and has mass Mc. Therefore

    integral (x-x_c)|a|^2=0,
    ||(x-x_c)a||_2=lambda ||yQ||_2.

Equation (6) and (8) imply

    ||(x-x_c)e||_2
      <=||(x-x_*)u_1||_2+|x_c-x_*|||u_1||_2
                            +||(x-x_c)a||_2
      <=C h.                                              (9)

The centroid identity can now be expanded with absolutely integrable terms:

    Mc(b_1-x_c)
       =2 Re integral (x-x_c)conjugate(a)e
           +integral (x-x_c)|e|^2.

Consequently

    Mc|b_1-x_c|
       <=2||(x-x_c)a||_2||e||_2
                     +||(x-x_c)e||_2||e||_2
       <=C(lambda^2+h lambda)
       <=C h^2.                                           (10)

Combining (10) with (1) proves (2). This conclusion is independent, to first order in h, of the allowed choice of quantitative modulation parameters.

## 5. Vanishing angular momentum of the primary core

Define the formally self-adjoint first-order operator

    mathcal_L_(x_*)=-i[(x-x_*) cross grad].

Because Q is radial about x_c,

    mathcal_L_(x_*)a
       =-i[(x_c-x_*) cross grad a].                         (11)

The angular momentum of a itself is zero: its spatial phase is constant. Equation (11), ||grad a||_2=lambda^(-1)||grad Q||_2, and (8) show that the cross term obeys

    |2 Re <e,mathcal_L_(x_*)a>|
       <=2||e||_2 |x_c-x_*| ||grad a||_2
       <=C h.                                              (12)

Self-adjoint integration by parts here is justified by smooth cutoff approximation: a and its derivatives decay exponentially, and e is H1 with a finite weighted L2 norm. The latter follows from (9):

    ||(x-x_*)e||_2
       <=||(x-x_c)e||_2+|x_c-x_*|||e||_2<=C h.

The error's own angular momentum is therefore bounded by

    |L_(x_*)(e)|
       <=||(x-x_*)e||_2||grad e||_2<=C h.                   (13)

Expanding the quadratic form and using (12)--(13) proves (3). In particular,

    L(u_1(t))=L_(x_*)(u_1(t))+x_* cross P(u_1(t))
       ->x_* cross P_*.

The same argument also gives vanishing primary angular momentum relative to its instantaneous centroid, since b_1-x_*=O(h) and P(u_1) stays bounded.

## 6. Secondary angular momentum and the conserved total

Now assume every secondary component belongs to Sigma at one lifespan time. The R17 critical-rate note proves

    (x-x_*)u_j(t)->(x-x_*)w_j strongly in L2,
    grad u_j(t) weakly ->grad w_j in L2.

These two convergences, and the uniform gradient bound, imply directly

    L_(x_*)(u_j(t))->L_(x_*)(w_j),
    L(u_j(t))->L(w_j).

Indeed, write the difference as a term containing the strong weighted difference paired with grad u_j, plus a fixed weighted w_j paired with the weak gradient difference. Both terms tend to zero. Strong physical H1 convergence is not needed.

The primary is automatically in Sigma by (6), so the entire vector lies in Sigma on every compact lifespan interval. The rotationally invariant common-density equation conserves total angular momentum there. One justification is to prove conservation for smooth decaying solutions, where the summed nonlinear torque is

    integral rho [x cross grad rho]
       =(1/2)integral x cross grad(rho^2)=0,

and the Laplacian commutes with rotations. Approximation in Sigma, using local H1 well-posedness and persistence/continuity of the spatial L2 weight, passes the identity to the present solution. Thus conservation, the primary limit from Section 5, and the secondary limits yield (4), equivalently (5).

## 7. derivation verdict

All proposed implications close under their stated assumptions. The center expansion (2) does not require any secondary spatial moments; the total angular-momentum identity (4) is asserted with finite secondary variance. The crucial estimates are strong secondary H^(1/2) convergence for momentum, automatic primary weighted control for the centroid comparison, and strong weighted L2 plus weak H1 convergence for secondary angular momentum.

These statements give a first-order collapse trajectory and an exact terminal split of conserved momentum and angular momentum. They do not determine lambda(t)/(T-t), prove differentiability of the chosen modulation center, or give a complete classification of the blowup solutions. This document records an independent internal analytic audit; historical priority and external validation are separate questions.
