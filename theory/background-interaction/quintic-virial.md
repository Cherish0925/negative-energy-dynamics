# A dynamic virial check of the quadratic quintic branch

Date: 2026-10-11. This note establishes the candidate one-dimensional quintic branch identified in [quintic-closure.md](quintic-closure.md). It solves a linear half-line boundary problem exactly and computes its moments. Its transfer to the coupled nonlinear singular solution remains a matched-asymptotic statement, not an existence theorem.

## 1. The conservation-law requirement

Consider the common-density quintic system

    i partial_t u_j+partial_x^2 u_j+rho^2 u_j=0,
    rho=sum_j |u_j|^2,
    E(U)=1/2 sum ||partial_x u_j||2^2-1/6 int rho^3.

Put T=0, h=-t>0. Take an even principal core and smooth odd terminal secondary data W=(w_j), with

    a_j=w_j'(0), A=sum |a_j|^2>0.

Let Z(t) be the secondary-only quintic evolution with Z(0)=W. It has conserved energy E(W). Suppose a candidate full solution has E(U)=E(W), the required terminal variance/current matching, and a primary scale

    lambda(t)=C h^2+o(h^2), C>0.

The exact total virial law is V_total''=16E(U); the background-only law is V_Z''=16E(W). Equal terminal variance and first derivative then imply exactly

    V_secondary(t)-V_Z(t)=-I_primary(t).

Consequently a coherent primary with I_primary=V_Q lambda^2+o(h^4) requires

    V_secondary-V_Z=-V_Q C^2 h^4+o(h^4).                (1)

This is a genuine dynamical constraint. A correction confined to the much narrower scale lambda cannot produce a second-moment change of that order.

## 2. The boundary value supplied by the transverse layer

The odd zero-energy profile in the companion note satisfies

    F(y)=y+c sign(y)+exponentially small remainder,
    c=pi/4+log(2)-1>0.

Thus the inner secondary profile a_j lambda F(x/lambda), matched against the smooth odd background a_j x, supplies the outer correction

    r_j(t,0+)=c a_j lambda(t)~b_j h^2,
    b_j=c C a_j.

The negative half-line is obtained by odd reflection. These are extrapolated boundary values for an outer problem. The actual coupled secondary field is continuous and vanishes at zero; its inner layer removes the apparent jump. In particular, the half-line outer correction alone is not a global smooth Schrödinger solution.

At distance x of order sqrt(h), the smooth background is a_j x+O(h^(3/2)). The leading equation for r is free Schrödinger: the quintic linearized background coefficient is of order x^4=O(h^2), whereas the leading time and second-space derivatives of the correction are of order h. Accordingly consider the exact auxiliary problem

    i partial_h r=partial_x^2 r, x>0, h>0,
    r(h,0)=b h^2,
    r(0,x)=0.

The sign is the backward physical-time sign, since h=-t.

## 3. Exact half-line solution and its self-similar equation

Taking the Laplace transform in h gives

    partial_x^2 r_hat=i p r_hat,
    r_hat(p,x)=2b p^-3 exp(-sqrt(i p) x), Re sqrt(i p)>0.

Equivalently,

    r(h,x)=h^2 R(x/sqrt(h)),
    R(xi)=2b int_0^1 (1-tau)
                  erfc(exp(i pi/4) xi/(2sqrt(tau))) d tau.   (2)

The integral can be obtained as the boundary convolution with the step-response erfc. It defines the branch with zero terminal data at every fixed x>0. Direct differentiation gives

    R''+(i xi/2)R'-2i R=0,
    R(0)=b.                                                (3)

For a completely explicit verification, put q=exp(i pi/4)/sqrt(pi), k=exp(i pi/4)/2. Then

    R(xi)/b=(1+i xi^2-xi^4/12) erfc(k xi)
              -q (5xi/3+i xi^3/6) exp(-i xi^2/4).          (4)

Equation (4) satisfies (3) and agrees with (2). The standard erfc expansion on this ray, or integrations by parts in (2), gives

    R(xi)=O(xi^-5), R'(xi)=O(xi^-4), xi->infinity.

The estimates include the oscillatory factor exp(-i xi^2/4). Therefore the moments int xi R and int xi^3 R are absolutely convergent. No nonphysical exponentially growing self-similar branch is used.

## 4. Exact moments and the variance coefficient

Define I1=int_0^infinity xi R(xi)d xi and I3=int_0^infinity xi^3R(xi)d xi. Multiply (3) by xi, integrate, and use the boundary decay:

    int xi R''=R(0)=b,
    (i/2)int xi^2 R'=-i I1.

Thus b-3i I1=0, or

    I1=-i b/3.                                             (5)

Multiplying (3) by xi^3 similarly gives

    6 I1-4i I3=0,
    I3=-b/2.                                               (6)

Integration can first be done on [0,R] and then R taken to infinity; the boundary terms vanish with the displayed decay. Some intermediate second-derivative integrals are conditionally oscillatory, but (5) and (6) involve absolutely convergent final moments.

An independent computation avoids these intermediate oscillatory integrals. For real p>0, the Laplace representation has exponentially decaying spatial factor, and

    int_0^infinity x r_hat(p,x)dx=-2i b p^-4,
    int_0^infinity x^3 r_hat(p,x)dx=-12 b p^-5.

Inverse Laplace transformation gives -i b h^3/3 and -b h^4/2 respectively, exactly (5) and (6) after self-similar scaling. The explicit polynomial-erfc expression (4) was also checked by direct symbolic substitution: both its erfc and Gaussian coefficients in (3) vanish identically.

For the linear background a x on the positive half-line and its odd reflection, the cross contribution to the variance is exactly

    2 Re int_R x^2 conjugate(a x) r(h,x)dx
       =4 h^4 Re(conjugate(a) I3)
       =-2 Re(conjugate(a)b) h^4.

The correction's own variance is O(h^(11/2)), since int xi^2|R|^2 is finite. With b_j=c C a_j, summing gives

    V_secondary-V_Z=-2 c C A h^4+o(h^4),                   (7)

provided the actual nonlinear remainder is small enough in this weighted cross pairing. Comparison of (7) with the exact conservation requirement (1) gives

    V_Q C^2=2c C A,
    C=2c A/V_Q.                                            (8)

This is exactly the coefficient derived from the matched energy calculation. The independent dynamic virial computation therefore finds no contradictory sign or factor. It supports the same candidate branch, without constructing it.

## 5. Gram, current, and energy checks

The leading scalar mass cross term has size h^3:

    2 Re int_R conjugate(a x)r dx
       =4 h^3 Re(conjugate(a) I1).

Since b=c C a with c C real, equation (5) makes this zero. The same cancellation holds for every entry of the secondary Gram matrix: the leading matrix correction is a purely imaginary scalar times aa*, plus its adjoint. Thus the outer layer does not violate conserved occupations at its leading cross order. The correction's own mass is O(h^(9/2)); subleading matching and evolution must handle that and subsequent orders.

The current moment D=Im int x conjugate(w) w_x has leading correction

    Delta D=2 h^3 Im[-2 conjugate(a) I1+a conjugate(I1)]
           =2c C |a|^2 h^3.

This is consistent with d_t Delta V=4 Delta D, since d_t=-d_h and Delta V=-2c C |a|^2h^4. Thus the continuity equation and virial first derivative give the same sign.

The outer kinetic cross term is also informative:

    Re int_R conjugate(a) partial_x r dx
       =-2 Re(conjugate(a)b) h^2
       =-2c A lambda, after summing components.

The raw inner transverse energy is +c A lambda, as computed before matching in the companion note. Their sum is -c A lambda. The outer self-energy is O(h^(7/2))=o(lambda). This recovers the matched static energy sign by a genuinely dispersive outer correction on scale sqrt(h), rather than by an arbitrary spatial cutoff.

## 6. What is proved and what still needs construction

Proved here: the exact half-line solution (2)–(4), its exact moments (5)–(6), and its mass, variance, current, and kinetic cross terms. These give a formal coupled-system compatibility condition (8) agreeing with the independent energy law.

To turn this into a coupled singular solution, one still has to construct and control the inner primary correction, the transverse layer, and the outer remainder simultaneously. In particular, transferring (7) requires an o(h^4) bound for the secondary variance cross-error; ordinary strong H1 convergence alone does not provide that rate. The exact conserved Gram matrix must hold beyond the leading cancellation, and primary modulation remainders must be controlled without differentiating an unspecified asymptotic error.

The calculation resolves a specific potential objection: total virial conservation does not rule out the candidate lambda~(2cA/V_Q)h^2 branch. It forces precisely the same coefficient once the dispersive secondary layer is included. It does not establish existence or a new classification theorem.

## 7. The effective Robin boundary preserves the full Gram matrix

The inner matching has a more structured interpretation than prescribed boundary forcing. If the outer slope is a_j(t), the offset supplied by F is c lambda a_j. Hence the natural leading effective boundary condition is

    w_j(t,0+)=ell(t) partial_x w_j(t,0+),
    ell(t)=c lambda(t)>0.                                  (9)

It is common to all components and has a real coefficient. Consider, as an auxiliary effective problem on x>0,

    i partial_t w_j+partial_x^2 w_j+S^2 w_j=0,
    S=sum |w_j|^2,

with boundary (9). Whenever the solution is regular enough for integration by parts, every half-line Gram entry is exactly conserved. Indeed,

    d_t int_0^infinity w_j conjugate(w_k)
      =-i [w_j' conjugate(w_k)-w_j conjugate(w_k')]_(x=0)=0.

This property uses the same real ell for every component. It supplies the missing feedback beyond the first Dirichlet approximation: the actual outer slope is a_j+r_{j,x}(0)+..., so the boundary value has the corresponding correction ell r_{j,x}(0). For the half-line solution above this term is of order h^(7/2). Its mass cross effect is of order h^(9/2), exactly the order of the leading outer correction's own mass. Consequently that nonzero higher-order mass is not, by itself, a contradiction with Gram conservation.

The exact effective energy for the pair of reflected half-lines is

    E_eff(w,ell)
       =1/2 int_(R\{0}) sum |w_j'|^2
          -1/6 int_(R\{0}) S^3
          +sum_j |w_j(0+)|^2/ell.                           (10)

The positive boundary term is part of the Robin quadratic form. On one half-line, the bulk energy derivative has boundary term -Re sum w_j'(0) conjugate(w_{j,t}(0)). The derivative of half the boundary term in (10) cancels it. Adding the two reflected halves yields the exact work identity

    d_t E_eff=-ell'(t) sum_j |w_j'(t,0+)|^2.                (11)

It does not involve differentiating an unspecified asymptotic error.

Near a smooth odd terminal background, the outer bulk cross energy is -2ell A+o(ell); the Robin term contributes +ell A+o(ell). Thus E_eff-E(W)=-ell A+o(ell), agreeing with the matched energy -cA lambda. Coupling this exact effective work to the primary chirp energy V_Q lambda'^2/8 would give

    (V_Q/4)lambda'lambda''
        =c lambda' sum |w_j'(t,0+)|^2.

On a collapsing interval where lambda' is nonzero, this reduces to

    lambda''=(4c/V_Q) sum |w_j'(t,0+)|^2.                  (12)

If the slope tends to a_j at the endpoint and lambda=lambda'=0 there, (12) gives lambda~(2cA/V_Q)h^2. Equations (9)–(12) make the shared sign and coefficient transparent: the shrinking scattering length transfers energy between the coherent primary and the dispersive secondary field.

The Robin flux and work formulas are exact identities for the auxiliary boundary problem. The original whole-line nonlinear system has no physical boundary. Deriving this boundary problem as its controlled asymptotic limit, including error bounds strong enough for (1), remains unproved here. Thus the effective formulation strengthens the consistency calculation; it is not a construction of the original faster-collapse solution.
