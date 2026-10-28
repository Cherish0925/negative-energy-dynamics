# Quintic endpoint dynamics: automatic principal variance and a global class

Date: 2026-10-09. This note combines the one-dimensional occupation remainder in [variational-extension.md](variational-extension.md) with the individual-principal-mode transport argument proved and independently checked in [critical-rate.md](critical-rate.md) and [primary-variance-details.md](primary-variance-details.md). Sections 2--5 do not assume a secondary terminal field. Section 6 then proves such a limit by localizing the equation away from the already identified collapse point, bypassing the singular global quintic forcing estimate.

## 1. Assumptions and constants

Consider a finite-component H1 solution of

    i partial_t u_j=-partial_x^2 u_j-rho^2 u_j,
    rho=sum_j |u_j|^2,
    E=(1/2)sum_j ||u_j'||_2^2-(1/6)integral rho^3,

in one space dimension. Work in a fixed eigenbasis of the conserved Gram matrix. Assume the largest eigenvalue is exactly

    m_1=M_c=pi sqrt(3)/2,
    epsilon=m_2/m_1<1.

There is no upper bound on the sum of secondary masses, and no initial variance hypothesis. For one component take epsilon=0. Let t_0>0 be the constant established in Section 5 of the companion variational note. Define

    a_epsilon=1/2,                         0<=epsilon<=t_0,
    a_epsilon=(1-epsilon)/(2(1-t_0)),       t_0<=epsilon<1,
    E_bar=E/a_epsilon.

The variational theorem gives throughout the H1 lifespan

    0<=E_1(t):=(1/2)||u_1'||_2^2-(1/6)||u_1||_6^6<=E_bar,
    A_secondary(t)<=E/b_epsilon,                             (1)

with b_epsilon=1/64 for epsilon<=t_0 and

    b_epsilon=t_0(1-epsilon)/(64epsilon(1-t_0))

otherwise. These constants are explicit in t_0, which itself depends on existential scalar stability constants.

The extension from small epsilon to arbitrary epsilon<1 uses Read--Schulz arXiv:2609.10478v2. This external dependence is maintained here. The subsequent dynamical argument uses only the estimates (1), critical scalar mass, the scalar concentration statement and the individual continuity equation.

## 2. The principal density converges to one terminal atom

Suppose the maximal forward H1 endpoint T is finite. The bounded secondary kinetic energy in (1) and the blowup alternative force ||u_1'(t)||_2 to tend to infinity. Set

    lambda(t)=sqrt(M_c/2)/||u_1'(t)||_2.

The scalar stability statement in the companion note gives, along all t increasing to T and after choosing phase and position,

    ||lambda(t)^(1/2)e^(-i theta(t))
          u_1(t,x(t)+lambda(t).)-Q||_H1 <= C_E lambda(t),     (2)

where Q(x)=3^(1/4)sech(2x)^(1/2). In particular the principal density differs in L1 by O(lambda) from a single translated and scaled density Q^2 of total mass M_c.

It remains to prove that its center has a unique finite limit. This does not require a terminal secondary field or finite second moments. Write

    mu_t=|u_1(t,x)|^2 dx,
    J_1=Im(conjugate(u_1)u_1').

The real common potential gives partial_t mu_t+2 partial_x J_1=0. For every bounded real smooth theta with bounded derivative, scalar GN at mass M_c gives

    0<=E_scalar(e^(ib theta)u_1)
       =E_1+b integral J_1 theta'+(b^2/2)integral |u_1|^2|theta'|^2.

The discriminant inequality is

    |integral J_1 theta'|^2
          <=2E_1 integral |u_1|^2|theta'|^2.                 (3)

Changing the phase of only this mode need not preserve the vector Gram matrix: (3) invokes scalar positivity and requires only its own exactly critical mass. Also, E_1 is bounded and continuous, not generally conserved.

Let W be the extended, unnormalized quadratic transport distance between finite measures of the same mass. The bounded-test Hamilton--Jacobi argument in the cited transport notes applies to (3), without assuming either marginal has finite second moment. It gives

    W(mu_t,mu_s)<=integral_t^s sqrt(8E_1(r))dr
                <=sqrt(8E_bar)|s-t|.                        (4)

For completeness, (4) supplies the needed tightness directly. Fix a lifespan time t_a<T. Every t in [t_a,T) has a coupling to mu_(t_a) of uniformly bounded quadratic cost. Splitting that coupling into |x|>R/2 or |x-y|>R/2 gives

    mu_t({|y|>R})
       <=mu_(t_a)({|x|>R/2})+C/R^2,

uniformly in t. Thus the principal measures are tight. Moreover, for every bounded Lipschitz test f,

    |integral f d(mu_t-mu_s)|
       <=Lip(f) sqrt(M_c) W(mu_t,mu_s),

so (4) makes them Cauchy in bounded-Lipschitz distance at T. Their weak terminal limit is unique and retains the whole mass. By (2), along every sequence t_n increasing to T, tightness forces the concentration centers x(t_n) to remain bounded; a convergent subsequence of centers identifies the limit as a point mass. Uniqueness consequently gives one x_* in R such that

    mu_t -> M_c delta_(x_*),
    x(t)->x_*,                                             (5)

along the full trajectory. No property of the secondary terminal fields has been used.

## 3. Automatic finite variance and quantitative rate

Fix t<T and let s increase to T in almost optimal couplings in (4). Their marginals are tight by (5); weak compactness of plans and lower semicontinuity of the quadratic cost yield

    W(mu_t,M_c delta_(x_*))
       <=integral_t^T sqrt(8E_1(r))dr.

The only coupling to a point mass sends each x to x_*. Therefore, including the possibility that the left side was initially infinite,

    I_1(t):=integral |x-x_*|^2 |u_1(t,x)|^2 dx
       <=[integral_t^T sqrt(8E_1(r))dr]^2
       <=8E_bar(T-t)^2.                                   (6)

This proves finite variance of the entire principal component, not just of its concentrating core. The one-dimensional Heisenberg inequality is

    I_1(t)||u_1'(t)||_2^2>=M_c^2/4.

For E_bar>0, (6) therefore gives

    ||u_1'(t)||_2>=M_c/[4sqrt(2E_bar)(T-t)],
    lambda(t)<=4sqrt(E_bar/M_c)(T-t).                       (7)

The principal centroid is now defined and satisfies

    |M_c^(-1)integral x|u_1(t,x)|^2 dx-x_*|
       <=sqrt(8E_bar/M_c)(T-t).

For E=0, (6) would force a positive absolutely continuous mass to be a point mass at every earlier time, which is impossible. Thus finite-time blowup requires E>0. Bound (7) is one-sided: it excludes slower-than-pseudoconformal collapse at this fixed-spectrum threshold, but does not exclude faster collapse or prove an exact asymptotic coefficient.

## 4. An explicitly described global class on the exact threshold

If the principal Gram eigenmode at one lifespan time has infinite variance,

    integral |x|^2 |u_1(t_0,x)|^2 dx=infinity,               (8)

then the finite-component H1 solution exists in both time directions. Indeed, a finite forward endpoint would contradict (6) at t_0. The time-reversed, conjugated solution has the same occupation and energy hypotheses, so a finite backward endpoint is equally impossible. Standard H1 local theory and continuation finish the argument.

Infinite variance is unchanged by translating the origin. The principal eigenspace is one-dimensional because epsilon<1, so (8) also does not depend on the phase chosen for its eigenvector. This is a nonempty class of actual exact-threshold data: choose a smooth H1 primary with a nonzero |x|^-1 tail and normalize its mass to M_c, then choose the finite secondary family in disjoint compact intervals, each orthogonal to that primary by a two-bump linear combination, with the prescribed masses. All Gram entries are exact.

The result asserts global existence, not a uniform H1 bound or scattering as time tends to infinity. Finite primary variance alone does not decide the fate of an initial state.

## 5. The conformal principal field

For an actual finite-time singularity, write h=T-t, s=1/h and define

    v_1(s,y)=h^(1/2)exp(i h y^2/4)u_1(T-h,x_*+hy).

Its H1 membership follows from the automatic variance (6). The critical quintic scaling gives the same scalar conformal identities as in the two-dimensional cubic case:

    ||y v_1(s)||_2^2=h^(-2)I_1(t)<=8E_bar,
    E_scalar(v_1(s))=h^2 E_1(t)+(h/8)I_1'(t)+I_1(t)/8.

After establishing finite variance, cutoff approximation in (3) with theta=(x-x_*)^2/2 and the continuity equation give

    I_1'(t)=4 integral (x-x_*)J_1(t,x)dx,
    |I_1'(t)|<=4sqrt(2E_1(t)I_1(t))<=16E_bar h.

Hence

    0<=E_scalar(v_1(s))<=4E_bar/s^2.                        (9)

This is information about the principal conformal field alone; secondary fields with infinite variance need not become H1 conformal fields. A faster physical collapse would correspond to principal kinetic grow-up in this conformal regime with bounded variance and scalar energy tending to zero. Neither (6) nor (9) by itself excludes that possibility.

## 6. The secondary terminal field exists and vanishes at the collapse point

The one-dimensional Sobolev estimate supplies an additional argument not available in this form in two dimensions. Let

    S_core(t,x)=exp(i theta(t))lambda(t)^(-1/2)
                  Q((x-x(t))/lambda(t)),
    r_1(t)=u_1(t)-S_core(t).

Equation (2) gives ||r_1||_2<=C lambda and ||r_1'||_2<=C. Consequently

    ||r_1||_infinity<=C sqrt(lambda).                        (10)

The exponential decay of Q and x(t)->x_* imply that u_1 tends to zero uniformly on every compact set disjoint from x_*. It is uniformly bounded on each such set for all times sufficiently close to T. Every secondary u_j is uniformly H1 bounded by (1), and therefore uniformly bounded in L-infinity globally.

Fix a smooth compactly supported test psi whose support avoids x_*. The equation gives

    d/dt <u_j,psi>=i<u_j,psi''>+i<rho^2 u_j,psi>,

with the sign depending only on the inner-product convention and irrelevant to the bound. Both terms are uniformly bounded near T by the preceding local bounds. Hence <u_j(t),psi> has a limit at T. Since C_c-infinity(R minus {x_*}) is dense in L2(R), and ||u_j||_2 is fixed, these limits determine a unique weak L2 limit w_j along the entire trajectory.

Strong convergence follows from compactness, with no global estimate of rho_1^2 u_j. The separate continuity equation and the elementary bound |J_j|^2/|u_j|^2<=|u_j'|^2 give

    W(|u_j(t)|^2dx,|u_j(s)|^2dx)
       <=2 integral_t^s ||u_j'(r)||_2 dr <=C_j |s-t|.        (11)

As in Section 2, the uniformly bounded relative transport cost to one fixed time gives uniform spatial tightness. Together with the uniform H1 bound, Rellich compactness on bounded intervals and tightness give relative compactness in global L2. Uniqueness of the weak limit then proves

    u_j(t)->w_j strongly in L2 and in every H^sigma, sigma<1,
    u_j(t) converges weakly in H1, and w_j belongs to H1.     (12)

The one-dimensional inequality ||f||_infinity^2<=C||f||_2||f'||_2 also gives uniform convergence u_j(t)->w_j on R.

In fact the secondary background has a node at the collapse point:

    w_j(x_*)=0, j>=2.                                      (13)

To prove this, use exact Gram orthogonality <u_1,u_j>=0 and ||r_1||_2=O(lambda). Changing variables in the core contribution gives

    | integral Q(y) conjugate(u_j(t,x(t)+lambda y))dy |
        <=C sqrt(lambda).

Uniform derivative bounds imply

    |u_j(t,x(t)+lambda y)-u_j(t,x(t))|
        <=C sqrt(lambda)|y|^(1/2).

Since integral Q>0 and integral |y|^(1/2)Q<infinity, it follows that |u_j(t,x(t))|<=C sqrt(lambda). Uniform convergence in (12) and x(t)->x_* prove (13).

In the original fixed component coordinates, if c is the unit principal Gram eigenvector, set W=sum_{j>=2} c_j w_j using the remaining Gram eigenbasis. The resulting full-time decomposition is

    U(t,x)=c S_core(t,x)+W(x)+R(t,x),
    ||R(t)||_H^sigma->0 for every 0<=sigma<1,
    sup_(t close to T)||R(t)||_H1<infinity,
    c^*W=0 pointwise,
    integral W W^*=Gamma-M_c c c^*,
    W(x_*)=0.                                             (14)

The background is unique because (12) holds for the whole trajectory. Strong L2 convergence preserves the complete secondary Gram matrix. In particular the total density converges weakly to M_c delta_(x_*)+|W|^2dx.

## 7. Weighted secondary convergence and conformal free radiation

Assume an individual secondary component has finite variance at one time. The finite-cost bound (11) propagates this property on every finite lifespan segment and makes its densities Cauchy in the usual finite-mass P2 space as t increases to T. Their weak limit is already identified in (12), so w_j has finite variance and

    W(|u_j(t)|^2dx,|w_j|^2dx)<=C_j(T-t),
    ||(x-x_*)u_j(t)||_2->||(x-x_*)w_j||_2.

Strong unweighted L2 convergence gives weak convergence of the weighted fields against compactly supported tests. Boundedness and convergence of their norms then give strong weighted convergence:

    ||(x-x_*)(u_j(t)-w_j)||_2->0.                           (15)

Suppose all secondary components have finite variance. The automatic principal variance then puts the complete vector in Sigma, so its pseudoconformal image

    v_j(s,y)=h^(1/2)exp(i h y^2/4)u_j(T-h,x_*+hy), s=1/h,

is an H1 solution for all large s. For j>=2, let W_j(x)=w_j(x+x_*) and z_j(t)=exp(it partial_x^2)W_j. Free evolution is continuous in Sigma at t=0, as follows from

    x exp(it partial_x^2)W_j
       =exp(it partial_x^2)(x W_j-2it W_j').

Equations (12) and (15) therefore imply that the physical difference between u_j(T-h,x_*+.) and z_j(-h) tends to zero in L2 and in the weighted L2 norm. Its derivative stays uniformly L2 bounded. The conformal image z_j^C is an exact free H1 solution, so z_j^C(s)=exp(is partial_y^2)f_j for a fixed f_j in H1. Differentiating the conformal transform gives

    ||v_j-z_j^C||_2=||u_j-z_j||_2->0,
    ||(v_j-z_j^C)'||_2
       <=h||(u_j-z_j)'||_2+(1/2)||x(u_j-z_j)||_2->0.

Consequently

    ||v_j(s)-exp(is partial_y^2)f_j||_H1->0,
    <f_i,f_j>=<w_i,w_j>,
    ||f_j'||_2^2=(1/4)||x W_j||_2^2.                        (16)

Thus every finite-variance conformal secondary field scatters freely in H1. This is proved directly from the terminal background; no general nonlinear scattering theorem has been assumed.

The entire conserved conformal energy is carried asymptotically by this radiation. To check the nonlinear terms, write rho_s=sum_{j>=2}|u_j|^2. The energy decomposition is

    E=E_1+A_secondary/2
         -(1/2)integral rho_1^2 rho_s
         -(1/2)integral rho_1 rho_s^2
         -(1/6)integral rho_s^3.

The three subtracted terms are nonnegative, and E_1 and A_secondary are uniformly bounded. Hence all three integrals are bounded. Critical scaling multiplies them by h^2 in conformal variables, so they vanish as s increases to infinity. Using (9) and (16), conservation of the full conformal energy gives

    E(V)=(1/2)sum_{j>=2}||f_j'||_2^2
        =(1/8)sum_{j>=2}||(x-x_*)w_j||_2^2.                 (17)

## 8. A global finite-variance alternative for every simple leading occupation

Assume now that U is forward global, U(0) belongs to Sigma, and its Gram spectrum has m_1=M_c and m_2<m_1. Then precisely one of the following alternatives holds:

1. U scatters in H1 as t tends to infinity.
2. There are a unit principal Gram eigenvector c, a free scattering vector F in H1 with c^*F=0, real constants v,x_0, a positive scale ell(t)<=C, centers X(t)=vt+x_0+o(1), and phases theta(t), such that

       U(t,x)=c exp(i theta(t)+i v x/2) ell(t)^(-1/2)
                       Q((x-X(t))/ell(t))
                 +exp(it partial_x^2)F(x)+R(t,x),
       ||R(t)||_H1->0,
       integral F F^*=Gamma-M_c c c^*,                     (18)
       v=(2/M_c)[P(U)-sum_{j>=2}P(F_j)].

Here P(U)=Im sum_j integral conjugate(u_j)u_j' is the conserved total momentum, and the last sum is in a fixed Gram eigenbasis. The principal component of the approximation error is O(t^-1) in H1. No quantitative convergence rate is asserted for the full radiation error. Neither a positive limit of ell nor a phase law is proved.

We verify the conformal reduction and every scaling constant for this quintic equation. For s<0 close to zero, put t=-1/s and

    W(s,y)=|s|^(-1/2)exp(i y^2/(4s))U(-1/s,y/s).            (19)

The mass-critical identity is obtained directly from differentiating this transformation: iW_s+W_yy+|W|^4 W is the original equation multiplied by the common phase and |s|^(-5/2). Thus W solves the same vector equation and has exactly the same Gram matrix. The modulus power is essential: the fifth-power nonlinearity transforms by |s|^(-5/2), the same power as the second derivative.

For J(t)=x+2it partial_x and V_0=||xU(0)||_2^2, the quintic pseudoconformal conservation law reads

    ||J(t)U(t)||_2^2-(4/3)t^2 integral rho(t)^3=V_0.         (20)

One can verify the coefficient without an appeal to dimension analogy: the virial identities give V''=16E and ||JU||^2=V-tV'+4t^2A. Substituting V(t)=V_0+V'(0)t+8Et^2 and E=A/2-F/6 yields (20). Direct differentiation of (19) gives

    A(W(s))=||J(t)U(t)||_2^2/4,
    integral |W(s)|^6=t^2 integral |U(t)|^6,
    E(W)=V_0/8.                                           (21)

All these identities extend to Sigma data by standard smooth approximation and local Sigma persistence.

The H1 lifespan of W either extends through s=0 or has a finite endpoint there. In the extension case, local Sigma persistence gives W(0) in Sigma. Let W_lin(s)=exp(is partial_y^2)W(0). Both W-W_lin and y(W-W_lin) tend to zero in L2, while their derivatives stay bounded. The inverse of (19) is

    U(t,x)=t^(-1/2)exp(i x^2/(4t))W(-1/t,-x/t).             (22)

Applied to W_lin it is an exact free H1 solution. The L2 error tends to zero, and its derivative is bounded by t^-1 times the derivative error plus one half of the weighted L2 error. This proves H1 scattering of the complete U in the first alternative.

In the singular case, Sections 2--7 applied to W at s=0 give

    W_1(s,y)=exp(i theta_s)lambda(s)^(-1/2)
                    Q((y-x(s))/lambda(s))+r_1(s,y),
    lambda(s)<=C|s|,
    ||r_1(s)||_2=O(lambda(s)), ||r_1'(s)||_2=O(1),
    ||(y-x_*)W_1(s)||_2=O(|s|).                            (23)

The core approximation and the last bound force |x(s)-x_*|=O(|s|): a fixed fraction of the principal mass lies within O(lambda) of its profile center, so (23)'s full variance bounds its center distance. The core and the error separately have position norm relative to x_* of order |s|. Equation (22) therefore maps r_1 to an error O(t^-1) in H1.

The secondary fields W_j converge strongly below H1 to w_j by Section 6. They have finite variance at each negative s because U(0) belongs to Sigma. Section 7 gives their strong weighted limit and shows that their inverse conformal images scatter freely in H1. Denote these free states by F_j. The exact Gram identities in (18) follow from their strong L2 convergence.

The inverse image of the primary core in (23) has width and center

    ell(t)=t lambda(-1/t)<=C,
    X(t)=-t x(-1/t),

using the evenness of Q. Its phase is initially quadratic, exp(i x^2/(4t)), and its center satisfies X(t)=-x_* t+O(1). To refine that O(1) to a limit, secondary H^(1/2) convergence gives convergence of their momenta. Conservation of total momentum of W then gives P(W_1(s))->P_* for some real P_*. Its finite-variance centroid b_1 obeys b_1'=2P(W_1)/M_c and tends to x_*. Hence

    b_1(s)=x_*+(2P_*/M_c)s+o(|s|).

The centroid differs from the profile center by O(s^2): expand W_1=core+r_1 in the centered first moment. The core has zero centered first moment; the cross term is O(lambda^2), and the error's own first moment is bounded by ||(y-x(s))r_1||_2||r_1||_2=O(|s|lambda). Thus

    X(t)=-x_* t+2P_*/M_c+o(1),                             (24)

giving v=-x_* and x_0=2P_*/M_c in these coordinates.

The quadratic phase can now be replaced by exp(i v x/2), after absorbing a scalar phase into theta(t). Write x=X(t)+ell(t)z. The nonconstant difference of phases is

    [(X(t)/t-v)ell(t)z]/2+ell(t)^2z^2/(4t).

Since X(t)/t-v=O(t^-1) and ell is bounded, this replacement has L2 error O(t^-1). It also has H1 error O(t^-1) uniformly even if ell tends to zero: the derivative of the scaled Q contributes ell^-1, canceled by the factor ell in the phase difference, and the phase-gradient difference is O(t^-1)(1+ell|z|). All polynomial moments of Q and Q' are finite. Combining this with the transformed r_1 and the H1 scattering of the secondary modes proves (18).

Finally the velocity expression in terms of physical momentum remains valid even if the core kinetic energy grows. The primary error is O(t^-1) in H1. Integrating the linear cross term by parts puts its derivative on the error, so the primary momentum discrepancy is bounded by

    2||core||_2||error'||_2+||error||_2||error'||_2=O(t^-1),

without multiplying by the possibly diverging core derivative. The real Q profile with carrier exp(i v x/2) has momentum M_c v/2. Conservation of total momentum and convergence of secondary momenta then give the last line of (18).

The alternatives are disjoint. A scaled Q core with width bounded above retains a fixed positive mass in a ball of fixed radius centered at X(t). Every free L2 Schrodinger solution has mass in any fixed-radius ball tending uniformly in the center to zero, by approximation with L1 intersect L2 data and the dispersive estimate. Free secondary radiation and an L2-small error cannot remove the principal component's persistent local mass.

## Scope

The statements now proved for every strict one-dimensional leading-occupation gap are: a unique terminal principal atom at finite blowup, automatic full principal variance, a quantitative pseudoconformal lower rate for the gradient, two-sided global existence for infinite-variance principal data at the exact threshold, a unique H1 secondary background with a node at the collapse point, and a full-time core-plus-background decomposition below H1. With finite secondary variance, the conformal secondary modes scatter freely in H1 and carry all conserved conformal energy. Every forward-global Sigma solution has the H1 alternative (18): full scattering or one bounded-width principal core plus free secondary radiation. These results follow from the variational remainder, scalar phase positivity, individual continuity, local testing away from the collapse point, and the explicitly verified quintic conformal identities.

Strong physical secondary H1 convergence and an exact primary asymptotic rate remain outside this note. The secondary-field argument uses one-dimensional Sobolev continuity; it does not copy the two-dimensional global forcing estimate, which would be inadequate for the quintic cross term.
