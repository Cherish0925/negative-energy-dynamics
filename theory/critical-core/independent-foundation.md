# Proof details and conformal scattering consequences

Date: 2026-10-09. This note establishes the R16 occupation deficit,
transport argument, and vector Bourgain–Wang construction, then derives new
consequences for terminal secondary fields and finite-variance dynamics.
It does not edit R16 or claim historical priority.

## 1. Proof details of the R16 chain

The following claims survive direct examination of their displayed proofs.

1. The all-state remainder in [occupation-gap.md](../occupation-thresholds/occupation-gap.md) follows from the
   contradiction argument as written. If
   `D < delta/2 + C1 B/32`, the unconditional bound gives
   `B < 12 epsilon/beta^2 < (64/3)epsilon` and
   `delta < 6 C1 epsilon/beta < 8 C1 epsilon`, where
   `beta=31/32-3epsilon>=15/16`. These are sufficient for the local scalar
   stability estimate and the refined cross-term estimate. There is no
   circular use of a small-deficit hypothesis. Weighted Bessel bounds the
   sum of projection errors by the largest secondary occupation, rather
   than their trace. Scaling gives exactly

       E(U) >= E_scalar(u_1)/2 + A_sec(U)/64.          (1.1)

2. Common spatial phases preserve the complete Gram matrix. The phase
   discriminant therefore gives

       |integral J.grad theta|^2
           <= 2 E integral rho |grad theta|^2.       (1.2)

   The factor in the continuity equation is `partial_t rho+2 div J=0`.
   Young's inequality consequently gives relative transport speed
   `W(mu_t,mu_s)<=sqrt(8E)|t-s|`, with the unnormalized transport cost.
   Truncating `|x-y|^2/(2h)` makes the Kantorovich argument valid without
   finite second moments. Compactness of couplings with fixed finite
   marginals and monotone convergence justify the full extended cost.
   The terminal atom then forces the stated bound `lambda<=C(T-t)`.

3. In the vector Bourgain–Wang construction, the transverse blocks are
   selfadjoint copies of `-Delta+1-Q^2`; the scalar block remains real
   linear. The terminal integral correctly places multiplication by `i`
   inside the propagator. The distinction between globally `s^-2` linear
   perturbations and rapidly small localized secular projections is
   essential and is made explicitly. All polynomial convolution powers
   in the displayed contraction are integrable for the chosen exponents.
   Higher moments, rather than higher Sobolev norms alone, supply physical
   smoothness after the quadratic conformal phase is inverted. The exact
   Gram matrix follows from conservation and the terminal limit, not an
   invalid Gram–Schmidt operation on a nonlinear solution.

This audit accepts the stated classical scalar linear input and the R15
validated Townes envelope as dependencies; it is not a second independent
implementation of the ODE certificate. No mathematical incompatibility was
found in these three chains. The terminal-field argument can be strengthened
and simplified as follows.

## 2. Quantitative terminal limits of secondary fields

Consider a finite-component solution of

    i U_t + Delta U + |U|^2 U = 0,
    E(U)=A(U)/2-integral |U|^4/4,

in the endpoint Gram class of R16: in a fixed eigenbasis,

    ||u_1||_2^2=Mc,   <u_i,u_j>=0 (i!=j),
    max_{j>=2}||u_j||_2^2/Mc <= epsilon_0.

Let `U_sec=(u_2,...,u_k)` and `M_sec=||U_sec||_2^2`. The total secondary
mass need not be small. Suppose the solution is defined on a finite
interval `[a,T)`. The endpoint remainder (1.1) gives, throughout that
interval,

    A_sec<=64E,   0<=E_scalar(u_1)<=2E.              (2.1)

Set `I=integral |u_1|^2 |U_sec|^2` and
`F_sec=integral |U_sec|^4`. The exact energy decomposition yields

    I=2 E_scalar(u_1)+A_sec-F_sec/2-2E<=66E.        (2.2)

For every `s>1`, the embedding `H^s(R2) -> L_infinity(R2)` and
Cauchy–Schwarz give a uniform bound on the vector nonlinear source in
`H^{-s}`:

    || |u_1|^2 U_sec ||_{L1(l2)} <= sqrt(Mc I),
    || |U_sec|^2 U_sec ||_{L1(l2)}
        <= || |U_sec|^2 ||_2 sqrt(M_sec).

The secondary density has a uniform L2 bound from (2.1), either by the
scalar vector-valued GN inequality or by the sharper R16 kinetic bound.
Also `Delta U_sec` is bounded in `H^{-s}`. Thus

    ||partial_t U_sec||_{H^{-s}(l2)}<=L_s.          (2.3)

For `a<t<r<T`, interpolation gives the global estimate

    ||U_sec(t)-U_sec(r)||_2
      <= ||U_sec(t)-U_sec(r)||_{H^{-s}}^{1/(s+1)}
         ||U_sec(t)-U_sec(r)||_{H1}^{s/(s+1)}
      <= C_s |t-r|^{1/(s+1)}.                     (2.4)

Hence there is a unique `W_sec in H1` such that

    ||U_sec(t)-W_sec||_{H^sigma}
      <= C_{s,sigma}(T-t)^{(1-sigma)/(s+1)},
       0<=sigma<1, s>1.                            (2.5)

Equivalently, every exponent strictly below `(1-sigma)/2` is allowed.
The convergence is weak in H1. Its strong L2 part preserves every
secondary Gram entry. This proof needs neither a blowup hypothesis,
spatial compactness, tightness, finite variance, nor a subsequence. It
strengthens the qualitative secondary-field assertion in R16.

## 3. Scattering below the fixed-spectrum threshold with finite variance

Write `Sigma=H1 cap {xU in L2}`. For a fixed normalized Gram spectrum `p`,
let `C(p)` be the optimal orthonormal density constant, so that every field
with total mass `M` and spectrum `p` obeys

    integral |U|^4 <= M C(p) A(U).

Put

    r=M C(p)/2=M/M_*(p),   M_*(p)=2/C(p).

Suppose `r<1` and `U(0) in Sigma`. Then the corresponding solution is
global and scatters in Sigma in both time directions, in the precise
sense `exp(-it Delta)U(t)->U_+/-` in Sigma. This statement applies to any fixed spectrum for
which the sharp constant is defined; explicit knowledge of it is needed
only to turn the condition into a numerical threshold. In the R16
occupation range, `M_*(p)=Mc/p_1`.

The all-state coercivity is

    E(U)>=(1-r) A(U)/2.                             (3.1)

Let `V0=||xU(0)||_2^2` and `J(t)=x+2it grad`. The critical cubic
pseudoconformal conservation law is

    ||J(t)U(t)||_2^2-2t^2 integral |U(t)|^4=V0.    (3.2)

It follows by the usual mass, momentum-current and virial identities,
or by differentiating this expression for smooth finite-variance data
and passing to Sigma by approximation. It is unchanged by the vector
common-density nonlinearity. The common phase
`exp(-i|x|^2/(4t))` preserves the full Gram matrix, and its gradient norm
is `||J(t)U||_2/(2|t|)`. Applying (3.1) to this phase-twisted field gives

    ||J(t)U(t)||_2^2 <= V0/(1-r),                  (3.3)
    integral |U(t)|^4 <= r V0/[2(1-r)t^2].         (3.4)

The critical spacetime norm is therefore finite:

    integral_R integral_R2 |U(t,x)|^4 dx dt < infinity.

Finite intervals follow from ordinary local H1 theory; (3.4) treats both
infinite tails. The cubic Strichartz estimates and the inequalities

    || |U|^2 U ||_{L^{4/3}_{t,x}} <= ||U||_{L4}^3,
    ||grad(|U|^2 U)||_{L^{4/3}_{t,x}}
        <= C||U||_{L4}^2 ||grad U||_{L4}

give H1 scattering by absorption on tails with small L4 norm. Uniform
H1 boundedness follows from (3.1). If `U_+` is the future scattering state,
then for large positive t,

    ||U(t)-exp(it Delta)U_+||_2 = O(t^{-3/4}),
    ||U(t)-exp(it Delta)U_+||_{H1} = O(t^{-1/2}).  (3.5)

Indeed `||U||_{L4([t,infinity))}=O(t^{-1/4})`; on that tail the derivative
Strichartz norm is bounded by the uniform H1 norm of the initial state at
time t. Dual Strichartz applied to the Duhamel remainder then gives (3.5).
The same proof applies backward in time.

For the additional Sigma assertion, pseudoconformally compactify the
future half-line. The transformed field has bounded H1 by (3.3), hence
extends through the finite conformal endpoint. Its finite first moment
persists there, by the usual Sigma local theory. Inverting the conformal
map identifies `U_+` as a scaled Fourier transform of this Sigma endpoint,
which again belongs to Sigma. This assertion is about the regularity of
the scattering state. In fact the interaction-picture convergence also
holds in the position norm. If W_lin is the conformal image of the free
asymptotic state, regularity at the conformal endpoint gives
`||grad(W-W_lin)||_2->0`. The transformation identity is

    ||x[exp(-it Delta)U(t)-U_+]||_2
       =||J(t)[U(t)-exp(it Delta)U_+]||_2
       =2||grad[W(s)-W_lin(s)]||_2 ->0.

Together with (3.5), this proves scattering in Sigma. The displayed
polynomial rates in (3.5) concern the unweighted norms only.

## 4. Every global endpoint solution in Sigma radiates its secondary modes

Now assume the endpoint Gram class of Section 2, and suppose `U(t)` is a
forward-global solution with `U(0) in Sigma`. No global bound for its
primary kinetic energy and no complete classification of its primary
component is assumed.

There exist `F_j in H1`, `j>=2`, with the exact secondary Gram matrix, such
that

    ||u_j(t)-exp(it Delta)F_j||_{H1} -> 0.           (4.0)

Moreover, for every `0<=sigma<1` and every
`0<eta<(1-sigma)/2`,

    ||u_j(t)-exp(it Delta)F_j||_{H^sigma}
          =O(t^{-eta}),    t -> infinity.           (4.1)

The assertions are joint vector estimates for a fixed finite number of
components. The stated polynomial rates are for sub-H1 norms; the H1
convergence in (4.0) is qualitative.

### Proof

For `s<0` close to zero set `t=-1/s` and define

    W(s,y)=|s|^{-1} exp(i|y|^2/(4s)) U(-1/s,y/s).

This is a solution of the same vector equation and has the same Gram
matrix. Direct differentiation and (3.2) show

    A(W(s))=||J(t)U(t)||_2^2/4,
    E(W)=V0/8.                                    (4.2)

Apply (2.5) to W near s=0. Its secondary components have a terminal state
`w_sec in H1` and

    ||W_sec(s)-w_sec||_2=O(|s|^alpha)
       for every alpha<1/2.                       (4.3)

This applies whether or not W's primary component blows up. In addition,
the endpoint deficit for U and W gives

    ||grad U_sec(t)||_2^2<=64E(U),
    ||J(t)U_sec(t)||_2^2<=32V0.

Therefore

    ||y W_sec(s)||_2
       =t^{-1}||x U_sec(t)||_2
       <=t^{-1}sqrt(32V0)+16sqrt(E(U)).            (4.4)

Weak compactness and (4.3) imply `y w_sec in L2`, so the terminal state
lies in Sigma. Let `W_lin(s)=exp(is Delta)w_sec`. Since

    ||W_lin(s)-w_sec||_2
       <=C |s|^{1/2}||w_sec||_{H1},

(4.3) also compares W to W_lin. The inverse pseudoconformal transform of
W_lin is an exact free Schrödinger solution `exp(it Delta)F_sec`.
Its initial datum is H1 because `w_sec in Sigma`. The transform is L2
unitary at each pair of corresponding times; consequently

    ||U_sec(t)-exp(it Delta)F_sec||_2=O(t^{-alpha}).

The first line of (4.4) and unitarity of free evolution bound both terms
in H1 uniformly. Interpolation gives (4.1). Gram conservation and strong
L2 convergence prove that the scattering states have exactly the original
secondary Gram matrix.

For strong H1 scattering one needs strong weighted convergence of the
transformed secondary fields. This additional step was independently
developed in [critical-rate.md](critical-rate.md) and is checked here. Each transformed
secondary density satisfies its own continuity equation, and its current
obeys `|J_j|^2/rho_j<=|grad W_j|^2`. Thus its unnormalized quadratic
transport speed is at most `2||grad W_j||_2`, uniformly bounded by (2.1).
As s increases to zero, these measures are Cauchy in finite-mass P2;
their second moments converge to those of `|w_j|^2`. Strong complex L2
convergence from (4.3), together with convergence of second moments,
gives `y W_j(s)->y w_j` strongly in L2: the weighted fields converge
weakly against compactly supported tests, and their norms converge.

Since the free group is continuous on Sigma, this also gives
`y[W_j(s)-W_lin,j(s)]->0` in L2. Inverting the conformal transform,

    ||grad[U_j(t)-exp(it Delta)F_j]||_2
       <= t^{-1}||grad[W_j(s)-W_lin,j(s)]||_2
           +(1/2)||y[W_j(s)-W_lin,j(s)]||_2 ->0.

The first term tends to zero because both transformed gradients remain
bounded. This proves (4.0), without assuming strong H1 convergence at
the finite conformal endpoint.

## 5. A finite-variance endpoint dichotomy at infinite time

The same compactification yields a more detailed, complete alternative
for a forward-global endpoint solution in Sigma:

* Either U scatters in H1 as `t -> infinity`;
* or it has one persistent Townes core, of uniformly bounded width,
  plus freely scattering secondary radiation, with a remainder tending
  to zero in H1.

More precisely, in the second alternative there are a constant vector
`v,x_0 in R2`, a positive scale `ell(t)<=C`, a center `X(t)` satisfying
`X(t)=vt+x_0+o(1)`, and phases `theta(t)` such that

    U(t,x)=c exp(i theta(t)+i v.x/2) ell(t)^{-1}
               Q((x-X(t))/ell(t))
             +exp(it Delta)F(x)+R(t,x),

    ||R(t)||_2=O(t^{-alpha}) for every alpha<1/2,
    ||R(t)||_{H1}->0,
    c^*F=0,
    integral F F^* dx=Gamma-Mc c c^*.              (5.1)

Here c is the principal Gram eigenvector. The velocity is determined by
the conserved momentum minus the radiation momentum:

    v=(2/Mc)[P(U)-sum_{j>=2}P(F_j)].                (5.2)

A positive limiting width and a phase law are not asserted. Thus this
is not a theorem identifying
the core with one exact traveling soliton of fixed scale.

To prove the alternative, use W from Section 4. Its lifespan either
extends in H1 through s=0 or has a finite-time H1 blowup there. In the
extension case, weighted persistence gives a Sigma endpoint and the
inverse conformal argument proves H1 scattering of the entire field.

In the blowup case R16 gives, through all s increasing to zero,

    W_1(s,y)=exp(i theta_s) lambda(s)^{-1}
               Q((y-x(s))/lambda(s))+r_1(s,y),
    ||r_1(s)||_2=O(lambda(s)),
    lambda(s)<=C|s|,
    |x(s)-x_*|<=C|s|.

The inverse conformal image of the core has

    ell(t)=t lambda(-1/t)<=C,
    X(t)=-t x(-1/t),
    v=-x_*,
    |X(t)-vt|<=C.

The momentum refinement established in [momentum-details.md](momentum-details.md) upgrades
the last bound to a limit. For clarity, its proof and signs can be checked
directly here. The transformed secondary fields converge strongly in
H^{1/2}, so their momenta converge. Total momentum conservation gives
`P(W_1(s))->P_*`. The primary centroid satisfies
`b_1'(s)=2P(W_1(s))/Mc`, while full primary variance gives `b_1(s)->x_*`.
Thus

    b_1(s)=x_*+(2P_*/Mc)s+o(|s|).

The R16 profile center differs from this centroid by O(s^2). Indeed the
primary L2 residual is O(lambda), its position norm relative to the
profile center is O(|s|), and the core position norm is O(lambda).
Expanding the centroid difference gives O(lambda^2+|s|lambda)=O(s^2).
Consequently

    x(s)=x_*+(2P_*/Mc)s+o(|s|),
    X(t)=-t x(-1/t)=-x_* t+2P_*/Mc+o(1).

This proves the asserted intercept with `x_0=2P_*/Mc`.

Its quadratic phase can be replaced in L2, with error O(t^{-1}), by
the linear Galilean phase `exp(i v.x/2)` and a scalar time phase. Indeed,
write `x=X(t)+ell(t)z`; the phase difference after its constant term is
removed is bounded by

    C t^{-1} (|z|+|z|^2),

using bounded ell and `X(t)/t-v=O(t^{-1})`. The exponential decay of Q
makes this an L2 error O(t^{-1}). The transformed primary remainder is
also O(t^{-1}) in L2. Section 4 supplies the secondary free radiation and
its quantitative error. This proves (5.1).

There is also an absolute H1 bound for the primary remainder, even if
`ell(t)` tends to zero. The primary phase-current argument proved in
[critical-rate.md](critical-rate.md), independently checked here, yields

    ||(y-x_*)W_1(s)||_2 <= 4sqrt(E(W)) |s|.

Indeed the scalar mass is exactly Mc, so sharp scalar GN gives positivity
after every phase imposed on that primary alone; its scalar energy is
bounded by `2E(W)`. The primary transport distance to its terminal atom
therefore gives the displayed full variance bound, without a vector Gram
invariance requirement for this individual phase test.

Subtract the modulated Townes core. Its gradient residual is O(1) by R16,
and both the full primary and its core have position norm relative to
x_* of order |s|. Their residual therefore satisfies

    ||r_1(s)||_2=O(lambda(s)),
    ||grad r_1(s)||_2=O(1),
    ||(y-x_*)r_1(s)||_2=O(|s|).

Apply the conformal map centered at x_* and then the fixed Galilean
transformation associated with v. Its physical residual is O(t^{-1}) in
H1. Replacing the quadratic core phase by the fixed Galilean phase also
has H1 error O(t^{-1}) uniformly for `0<ell<=C`. To see the potentially
delicate derivative term, use `x=X+ell z`: the phase variation is
`O(t^{-1})(ell|z|+ell^2|z|^2)`, whereas differentiating the scaled profile
costs a factor `ell^{-1}`. These factors cancel. The remaining phase
gradient term is also O(t^{-1}) against Q, and its moments are finite.
Section 4 supplies strong H1 convergence of the radiation. Thus the full
remainder in (5.1) tends to zero in H1.

Finally, (5.2) remains valid even if the core scale tends to zero. The
primary approximation error is O(t^{-1}) in H1. In the expansion of its
momentum, integrate by parts to put each derivative from a linear error
term on that error. Its momentum discrepancy is therefore bounded by
`2||core||_2||grad error||_2+||error||_2||grad error||_2=O(t^{-1})`.
There is no factor involving the possibly unbounded gradient norm of
the shrinking core. The real Townes profile with carrier
`exp(i v.x/2)` has momentum `Mc v/2`; the secondary momenta converge to
those of their free scattering states. Conservation proves (5.2).

The alternatives are disjoint: a core of mass Mc, with bounded width
and center on a fixed-velocity ray up to a bounded displacement, prevents
L2 scattering. For a free L2 Schrödinger solution the mass inside any
ball of fixed radius tends uniformly in the ball center to zero; this
follows from density of L1 cap L2 and the L1-to-L_infinity dispersive
bound. Equation (5.1) retains a fixed positive mass in such a ball.

## 6. What this does not settle

The all-H1, no-variance subthreshold scattering problem does not follow
merely from the coercive inequality. Gram majorization allows each
concentration profile to inherit the parent's coercive bound, but a
mass-critical compactness argument still has to exclude frequency
cascades and obtain enough control of translation and kinetic tails.
Compactness in L2 modulo symmetries is not compactness in H1: positive
conserved energy could remain in a small high-frequency tail invisible
to L2 compactness. A localized virial argument must actually control
that tail. Scalar nonradial scattering theorems cannot be declared to
cover this vector occupation-constrained problem without checking their
full nonlinear argument.

Sections 2–5 are complete deductions from the verified R16 functional
and dynamical statements plus the classical cubic NLS local theory,
pseudoconformal identity, and Strichartz estimates. Their historical
novelty has not been established here.
