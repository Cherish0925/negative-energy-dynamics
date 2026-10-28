# Dini curvature, critical coherent collapse, and the sharp logarithmic boundary

Date: 2026-10-11. This note contains a scalar theorem derived in this research turn, its application to the existing vector setting, and exact forced-scalar examples. The moving-frame and conformal identities were independently checked by the `rough_virial` branch. Historical priority for the theorem is not established. The lens construction itself is established mathematics, not a new invention.

## 1. A stronger scalar statement

Let `d >= 1`, and let Q be the positive ground state

    -Delta Q + Q - Q^(1+4/d) = 0,
    M = integral Q^2,  A_Q = integral |grad Q|^2,
    V_Q = integral |x|^2 Q^2.

Consider

    i u_t + Delta u + |u|^(4/d) u + V(t,x) u = 0,

with real V on a finite terminal interval `[t0,T)`. Assume:

1. u is an H1 solution of mass M, with the continuity, scalar-energy, momentum, and localized virial identities justified by approximation. Locally in time the potential is sufficiently regular for the stated identities. No bound on V_t is required.
2. Its **scalar** energy, excluding the external potential,

       E0(u) = (1/2) integral |grad u|^2
             - d/[2(d+2)] integral |u|^(2+4/d),

   is uniformly bounded on this interval. Sharp scalar Gagliardo–Nirenberg gives E0 >= 0.
3. `||grad u(t)||_2 -> infinity` as t tends to T. Equivalently for the proof it suffices to assume the already established full atomic terminal density and the usual full-mass ground-state concentration property; the argument below derives these from items 1–3.
4. Put `h=T-t` and

       L(h) = ||Hess_x V(T-h)||_infinity.

   The Dini curvature condition is

       D(h0) := integral_0^h0 r L(r) dr < infinity.                (1)

The Hessian norm is the operator norm. Its global spatial bound is an actual extra assumption on V. For a solution-generated potential, it must be verified from that solution.

Then there is a unique terminal concentration point x*, and the following centered quantities are well defined:

    rho=|u|^2, J=Im(conj(u) grad u), P=integral J,
    b=M^(-1) integral x rho, p=P/M,
    e=E0-|P|^2/(2M), I=integral |x-b|^2 rho.

There is a strictly positive e* such that

    e(t) -> e* > 0,
    I(t)/h^2 -> 8 e*,
    lambda_kin(t)/h -> mu* := sqrt(8 e*/V_Q) > 0,               (2)

where `lambda_kin = sqrt(A_Q)/||grad u||_2`.

After removing the physical centroid and mean momentum, the conformal primary tends strongly in H1, modulo a scalar phase, to one fixed ground-state profile:

    w(t,z) = exp(-i p(t).z) u(t,b(t)+z),
    v(s,y) = h^(d/2) exp(i h|y|^2/4) w(T-h,hy),  s=1/h,

    inf_theta ||v(s)-exp(i theta) mu*^(-d/2)Q(./mu*)||_H1
         -> 0.                                                (3)

No phase-asymptotic formula is asserted from curvature alone. A spatially constant potential changes the phase arbitrarily while preserving (1). No finite initial variance is assumed. No quantitative scalar stability theorem is needed for the qualitative conclusion (3).

The power hypothesis in R18, `L(h) <= K h^(-alpha)` with alpha<2, implies (1). The new statement also permits

    L(h) <= C/[h^2 log(1/h)^p],  p>1.                          (4)

## 2. Compactness at the scalar threshold

The proof uses the familiar compactness of scalar sharp-GN optimizing sequences. Here is the precise form and the reason it applies.

If f_n have mass M, gradient squared A_Q, and E0(f_n)->0, then, after translations and constant phases, f_n converges strongly in H1 to Q. Nonvanishing follows because their critical-power norm approaches the nonzero sharp value. Translate to obtain a nonzero weak profile f. Write m=||f||_2^2 and a=||grad f||_2^2. Hilbert norm splitting and the Brezis–Lieb splitting, followed by sharp GN on f and its remainder, give

    limsup ||f_n||_(2+4/d)^(2+4/d)
       <= C_GN [m^(2/d) a + (M-m)^(2/d)(A_Q-a)].               (5)

If 0<m<M, both mass coefficients are strictly below M^(2/d), contradicting the limiting sharp value `C_GN M^(2/d) A_Q`. Thus m=M. Strong L2 convergence and H1 boundedness imply strong convergence at the critical nonlinear exponent, which is H1-subcritical in every finite dimension. Equality in GN then forces a=A_Q; this gives strong H1 convergence. Equality cases are the phase, translation, and scaling orbit of Q, and the prescribed gradient fixes the scaling. These are standard scalar-GN facts; the current work uses, rather than claims to originate, their compactness and ground-state characterization.

Apply this to

    f_n(y)=lambda_n^(d/2)u(t_n,lambda_n y),
    lambda_n=sqrt(A_Q)/||grad u(t_n)||_2.

The normalized energy is `lambda_n^2 E0(u(t_n))->0`. Thus every sequence t_n->T admits a full-mass concentrating ground-state subsequence.

## 3. The atom and finite variance follow from bounded scalar energy

At mass M, applying sharp GN after the phase change `u -> exp(i a theta)u` gives

    |integral J.grad theta|^2
        <= 2 E0(u) integral rho |grad theta|^2.                 (6)

Together with `rho_t+2 div J=0`, this gives both the bounded-Lipschitz estimate and the extended unnormalized quadratic-transport estimate

    W2(rho(t),rho(r)) <= integral_t^r sqrt(8 E0(u(tau))) d tau. (7)

The extended formulation permits individual second moments to be infinite; it follows first for bounded transport costs/cutoffs and then by monotone approximation. Uniform bounded-Lipschitz continuity and mass tightness give a unique narrow terminal measure of total mass M. Tightness follows by testing a large-radius cutoff: its time derivative is O(1/R), uniformly on the finite interval. The ground-state concentration subsequence from Section 2 must have bounded centers by tightness and hence an atomic terminal measure. Uniqueness of the terminal measure forces it to be M delta_(x*) for one x*.

Taking the terminal limit in (7), using lower semicontinuity of the transport cost, gives

    integral |x-x*|^2 rho(t,x) dx <= 8 C_E h^2.                 (8)

This is a bound on the **entire** primary density. In particular b and I are finite and b(t)->x*. The same phase inequality with a linear theta gives `|P|^2 <= 2 M E0`, so the physical mean momentum is bounded.

## 4. Centered identities and positive limiting intrinsic energy

With the plus-V convention on the left-hand side of the equation,

    b'=2p,
    P'=integral rho grad V,
    E0'=integral J.grad V,
    e'=integral (J-p rho).grad V,
    I''=16e+4 integral (x-b).grad V rho.                       (9)

The force in the last line may use `grad V(x)-grad V(b)`. Its magnitude is at most L(h) I. Applying (6) after the Galilean phase, with the affine part of V removed, gives

    |(sqrt e)'| <= L(h) sqrt(I/2).                             (10)

The centered density has current J-p rho, so its transport distance to its terminal atom gives

    I(t) <= 8 [integral_t^T sqrt(e(r)) dr]^2.                  (11)

Write f=sqrt e. Boundedness of f and (10)–(11) give `|f'| <= C h L(h)`. Condition (1) therefore gives a terminal limit f*, with

    |f(t)-f*| <= C D(h).                                      (12)

If f*=0, integrate (10) backwards and use (11). On a sufficiently short terminal interval, with F_h the supremum of f there,

    F_h <= 2 D(h) F_h.

Since D(h)->0, f vanishes on that interval. Equation (11) would force I=0 for a nonzero absolutely continuous density, which is impossible. Hence e*=f*^2>0.

The phase estimate gives I'=O(h), and (8) gives I=O(h^2); thus their terminal values are both zero. Integrating (9) twice yields

    I(h)=16 integral_0^h (h-r)e(r) dr
         +4 integral_0^h (h-r) F(r) dr,
    |F(r)| <= C r^2 L(r).

In particular

    e=e*+O(D(h)),
    I/h^2=8e*+O(D(h)).                                        (13)

Here and below time derivatives in identities such as (9) refer to t. The last display writes I as a function of h only for the terminal integration.

## 5. Exact accelerated frame: all affine terms retained

Define w as in (3). A direct differentiation, using b'=2p, gives

    i w_t+Delta w+|w|^(4/d)w+W(t,z)w=0,
    W(t,z)=V(t,b(t)+z)-p'(t).z+|p(t)|^2.                     (14)

An additional time-dependent scalar phase can remove the last term, but is unnecessary. The minus sign in `-p'.z` is the inertial force. Both the mean position and momentum of w are zero. Its scalar energy is e and its variance is I.

Now perform the conformal change in (3). It satisfies

    i v_s+Delta v+|v|^(4/d)v+B(s,y)v=0,
    B(s,y)=h^2 W(T-h,hy),
    ||Hess_y B(s)||_infinity <= h^4 L(h).                    (15)

The conformal field also has zero mean and zero momentum. Put

    epsilon(s)=E0(v(s)),  J_v=Im(conj(v) grad v).

Direct expansion, with the chirp gradient `h y/2`, gives

    epsilon = h^2 e + (h/8) I' + I/8 >= 0,
    integral |y|^2 |v|^2 = I/h^2 <= C.                       (16)

Each term in (16) is O(h^2), by the already proved bounds, hence epsilon->0. This preliminary limit uses no conformal scale estimate.

## 6. The new cancellation: integrate the conformal energy equation backwards

The exact scalar energy equation for v is

    epsilon'(s)=integral J_v.grad B.

Since P(v)=0, subtracting `grad B(s,0)` does not change this integral. Apply scalar phase positivity to the test `B-grad B(s,0).y`. From (15)–(16),

    |d_s sqrt(epsilon)|
        <= (1/sqrt 2) ||Hess B||_infinity
                            (integral |y|^2 |v|^2)^(1/2)
        <= C s^(-4) L(1/s).                                 (17)

The estimate is valid also at zeros, by the regularized square-root argument. Because epsilon tends to zero, integrate (17) from s **to infinity**, obtaining

    sqrt(epsilon(s)) <= C A(h),
    A(h):=integral_0^h r^2 L(r) dr.                          (18)

This is stronger than taking a square root after separately estimating the terms in (16). In particular, for a power curvature bound it gives

    sqrt(epsilon) = O(h^(3-alpha)),  alpha<2.                (19)

The conformal quadratic-transport speed is at most sqrt(8 epsilon). Tonelli's theorem gives the exact useful kernel

    integral_s^infinity A(1/tau) d tau
       = integral_0^h [r-r^2/h] L(r) dr
       = D(h)-A(h)/h.                                      (20)

Consequently the conformal density converges in W2 to a unique measure eta*, and

    W2(|v(s)|^2,eta*) <= C [D(h)-A(h)/h] <= C D(h).          (21)

Its mean is zero and its variance, by (13), is 8e*>0. The integral condition ensuring this full weighted compactness is precisely the same condition (1) that ensured positive limiting intrinsic energy. This is the substantive improvement over the R18 power argument.

## 7. Strong coherent-profile conclusion without an assumed profile

We first rule out an unbounded conformal gradient. If along s_n it diverged, apply the normalized scalar-GN compactness lemma of Section 2. Since epsilon(s_n)->0, it would force the conformal density to become a full-mass point concentration. Bounded second moments keep the concentration centers bounded. After a subsequence the narrow limit would be one atom. But the W2 limit in (21) has positive centered variance, an impossibility. Thus the conformal gradient is uniformly bounded above.

The uncertainty inequality and bounded variance give a positive lower bound on that gradient. Apply the same scalar-GN compactness lemma now at its bounded, nonzero scale. Every sequence has a subsequence converging strongly in H1, after scalar phase removal, to a translated Q profile. Equation (21) fixes its density uniquely. Zero mean fixes the translation at zero; variance fixes its scale at mu*=sqrt(8e*/V_Q). This proves (3) along the full time evolution.

Finally the kinetic identity is

    ||grad v||_2^2
      = h^2 (||grad u||_2^2-|P|^2/M) + I/4 + h I'/4.        (22)

The last three correction terms, relative to `h^2 ||grad u||_2^2`, are O(h^2). Therefore (3) identifies the actual physical kinetic scale and proves (2), rather than only a root-mean-square width.

If a quantitative scalar-GN stability theorem is separately available, the centered conformal profile residual improves to `O(A(h))` in H1. The qualitative theorem above does not require this strengthening.

## 8. Exact boundary examples: power and logarithmic faster collapse

Before the examples, one can make the spatial hypothesis more intrinsic. The proof remains valid if the global Hessian bound is replaced by

    inf_a integral rho(t,x) |grad V(t,x)-a|^2 dx
         <= k(h)^2 I(t),
    integral_0^h0 h k(h) dh < infinity.                     (23a)

Here a ranges over constant real vectors, and its minimizer is the mean force `M^(-1) integral rho grad V=p'`. All the force and energy identities must still be justified. Cauchy–Schwarz bounds the virial force by k I. Scalar phase positivity bounds `|(sqrt e)'|` by `k sqrt(I/2)`. In the centered conformal frame the square root of the weighted force variance is exactly h^3 times its physical value, and hence is bounded by `h^4 k sqrt(I/h^2)`. Thus (17)–(21) hold with k in place of L. This version measures variation of the force only where the collapsing primary has density. A global Lipschitz bound on grad V implies (23a), but is not required by it. Condition (23a) is not automatically available from a bare H1 bound on a vector secondary field.

For any positive C2 scale lambda(t), define

    theta'(t)=lambda(t)^(-2),
    u(t,x)=lambda(t)^(-d/2) Q(x/lambda(t))
             exp(i theta(t)+i lambda'(t)|x|^2/[4lambda(t)]).

Direct substitution gives

    i u_t+Delta u+|u|^(4/d)u
       = -[lambda''(t)/(4lambda(t))]|x|^2 u.                (23)

Thus this is an **exact** solution with real potential

    V(t,x)=[lambda''(t)/(4lambda(t))]|x|^2,
    ||Hess V||=|lambda''|/(2lambda).                        (24)

Its conserved mass and scalar quantities are

    mass=M, P=b=0,
    I=V_Q lambda^2,
    E0=V_Q (lambda')^2/8,
    ||grad u||_2^2=A_Q/lambda^2+V_Q(lambda')^2/4.             (25)

The exact physical kinetic scale has the same leading asymptotic as lambda whenever lambda lambda'->0. Each field is smooth, exponentially localized in amplitude, and has finite variance at each t<T. The potential is smooth in space, locally regular in time away from T, and quadratic in space. The scalar energy need not be conserved because the potential depends on time.

### 8.1 Power boundary

Take lambda=h^a, a>1. Then

    L(h)=a(a-1)/(2h^2),
    E0=V_Q a^2 h^(2a-2)/8 ->0,
    lambda/h=h^(a-1)->0.

Hence the old endpoint alpha=2 genuinely permits faster-than-linear collapse while every scalar mass, energy, and variance hypothesis other than Dini integrability is satisfied.

### 8.2 Logarithmic boundary

Let ell=log(1/h), restrict 0<h<exp(-1), and choose beta>0 with

    lambda(h)=h ell^(-beta).

Since the second t derivative equals the second h derivative,

    lambda_h=ell^(-beta)(1+beta/ell),
    lambda_hh=beta h^(-1) ell^(-beta-1)
                 [1+(beta+1)/ell],
    L(h)= beta/[2 h^2 ell] [1+(beta+1)/ell].                (26)

Again E0->0, the full density collapses, and lambda/h->0. The curvature is `o(h^(-2))`, yet the Dini integral diverges logarithmically. Thus even replacing alpha<2 by the bare condition `h^2 L(h)->0` would be false for forced scalar NLS.

Together, (4) and (26) locate the exact dividing logarithmic exponent within the family `h^(-2) log(1/h)^(-p)`: the theorem covers every p>1, while an exact faster-collapse example occurs at p=1. This does **not** assert necessity of (1) for every potential: divergent curvature can include spatial oscillations or cancellations, and some such potentials can still have linear-rate collapse.

## 9. What this does and does not establish for the autonomous vector system

For the two-dimensional common-density cubic vector equation, the primary equation has precisely the scalar form above with

    V=S=sum_(j>=2) |u_j|^2.

R16–R18 supply the required critical primary mass and uniform scalar-energy bound in the established occupation range. Thus the Dini theorem applies whenever its curvature assumption holds, including the borderline logarithmic class (4). Countably many secondary modes are permitted if the previously established Hilbert-valued hypotheses justify S and the local identities.

The boundary examples (23)–(26) are **not** vector solutions. For a pure chirped Q primary, (23) and Q>0 force its effective scalar potential, up to an irrelevant function of time from phase choice, to be a quadratic polynomial at every x. A nonzero such polynomial cannot equal S with finite total secondary mass, because S>=0 and S is in L1. A spatially constant phase correction does not repair this incompatibility. Consequently no finite-mass autonomous vector realization of these exact lens profiles exists.

This observation does not exclude a vector solution whose primary is only asymptotically such a profile. Near a shrinking core, the required quadratic background has small amplitude even when its curvature is singular. For the power example its size on |x|~lambda is `O(h^(2a-2))`; its variation can fit inside a bounded H1 budget. Therefore a crude local size or gradient-energy argument alone does not settle realizability. Constructing such a vector evolution, or excluding it using the secondary equation and exact Gram orthogonality, remains a separate open step. No forced-scalar counterexample is presented as a counterexample to the autonomous vector conclusions.

## 10. Primary literature checked for the lens mechanism

Rémi Carles, *Nonlinear Schrödinger equation with time dependent potential*, arXiv:0910.4893v2, 7 July 2010, especially Section 4, Proposition 4.1, and Section 4.2. The paper derives the generalized time-dependent lens transform and explicit critical-mass blowup profiles for isotropic harmonic potentials. Its Laplacian normalization is 1/2; equations (23)–(25) above have been derived directly for our normalization. The examples here use potentials singular at the terminal endpoint, so one must not replace the present direct verification by a theorem whose potential is continuous across that endpoint.

Primary text: https://arxiv.org/pdf/0910.4893

This reference establishes that generalized lens transforms and forced critical collapse are longstanding tools. The present note's specific additional derivation is the Dini-curvature implication obtained by applying phase positivity **again in the centered conformal frame**, integrating its scalar-energy equation backwards, and using the resulting W2 convergence to fix the true coherent width. Further literature comparison is needed before claiming this theorem is historically new.
