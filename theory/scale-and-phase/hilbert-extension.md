# Countably many coherent modes: a Hilbert-valued threshold theorem

Date: 2026-10-10. This note extends the R16/R17 theorems to an arbitrary separable complex Hilbert space of components. Its new content is the complete passage from static trace-class inequalities to infinite-component dynamics, including the compactness needed for the one-dimensional terminal field and joint strong H1 radiation. It depends on the R16 two-dimensional occupation remainder, the R17 one-dimensional remainder, and their scalar profile stability input. In one dimension the full range of simple leading occupations continues to depend on Read–Schulz, arXiv:2609.10478v2. Historical priority is not asserted.

The extension concerns all actual H1 solutions in the stated classes. It does not assert an infinite-rank Bourgain–Wang construction for every trace-class spectrum, nor replace the finite-total-variance hypothesis by componentwise finite variance.

The infinite-component common-density framework is established prior work. Hong, Kwon and Yoon, *Global existence versus finite time blowup dichotomy for the system of nonlinear Schrödinger equations*, arXiv:1712.06811, formulate an infinite cubic system, conserved orthogonality and occupation spectrum, Hilbert-sequence H1 local theory, and its density-matrix equation. Their dynamical theorem treats the three-dimensional cubic equation, while their extremizer theorem excludes the mass-critical kinetic endpoint. The present note supplies the two-dimensional cubic and one-dimensional quintic endpoint consequences of the project's occupation remainder; it does not claim invention of the infinite-system or density-matrix formulation. Primary source checked: https://arxiv.org/pdf/1712.06811, introduction and Theorems 1.2–1.3.

## 1. The two models and the result

Let H be a separable complex Hilbert space. For d=2 or d=1, set p=1+4/d and consider

    i U_t + Delta U + ||U||_H^(p-1) U = 0,
    U : R_t x R_x^d -> H.

All Sobolev and Lebesgue norms below are Bochner norms. Define

    M(U) = integral ||U(x)||_H^2 dx,
    A(U) = integral ||grad U(x)||_H^2 dx,
    E(U) = A(U)/2 - (1/(p+1)) integral ||U(x)||_H^(p+1) dx,
    Gamma(U) = integral |U(x)><U(x)| dx.

Here Gamma is a positive trace-class operator on H, defined by a trace-norm Bochner integral. Its trace is M. Write its positive eigenvalues as

    m_1 >= m_2 >= ... > 0,     sum_j m_j < infinity.

The finite-rank case is included. At the endpoint assume m_1=Mc and either

* d=2, p=3: m_2/Mc <= epsilon_0, with epsilon_0 from [occupation-gap.md](../occupation-thresholds/occupation-gap.md);
* d=1, p=5: m_2/Mc < 1, with the variational dependence specified above.

For rank one put m_2=0. Q is the corresponding scalar ground state, and Mc=||Q||_2^2. The leading eigenvalue is simple; let c be a unit principal eigenvector. Let

    u_1(x)=<c,U(x)>_H,     V(x)=(I-|c><c|)U(x).

Then the following hold for arbitrary finite or countably infinite rank.

**Finite-time endpoint structure.** If the maximal H1 lifespan has a finite endpoint T, there are a unique point x_*, a unique W in H1(R^d;c-perp), phases theta(t), and centers x(t) such that

    U(t,x)=c exp(i theta(t)) lambda(t)^(-d/2)
                     Q((x-x(t))/lambda(t)) + W(x) + R(t,x),
    ||R(t)||_(H^sigma(H)) -> 0,                    0 <= sigma < 1,
    sup_(t near T) ||R(t)||_(H1(H)) < infinity,
    lambda(t) <= C(T-t),
    x(t) = x_* - [2 P_*/Mc](T-t) + o(T-t),
    Gamma(W) = Gamma(U)-Mc |c><c|.                 (1.1)

Here P_*=P(U)-P(W), with the Hilbert-valued momentum defined in Section 8. The primary approximation error has L2 norm O(lambda) and bounded gradient norm. For d=2 take lambda=sqrt(Mc)/||grad u_1||_2; for d=1 take lambda=sqrt(Mc/2)/||u_1'||_2.

The principal field has automatically finite variance about x_*:

    integral |x-x_*|^2 |u_1(t,x)|^2 dx
      <= [integral_t^T sqrt(8 E_1(r)) dr]^2
      <= 8 Ebar (T-t)^2.                          (1.2)

Here E_1 is the scalar principal energy and Ebar=2E in d=2; in d=1 use Ebar=E/a_epsilon from R17. No variance hypothesis is imposed in this assertion. Thus infinite initial principal variance implies global existence in both time directions. It does not imply a uniform global H1 bound.

In d=1, the continuous H-valued background additionally satisfies

    W(x_*)=0 in H.                                (1.3)

The entire secondary field, rather than only each fixed component, converges strongly in H^sigma for sigma<1. For d=2 the quantitative rate holds jointly:

    ||V(t)-W||_(H^sigma(H))
      <= C_(s,sigma) (T-t)^((1-sigma)/(s+1)),
      s>1, 0<=sigma<1.                            (1.4)

**Global endpoint alternative.** Put

    Sigma(H)=H1(R^d;H) cap {U: xU in L2(R^d;H)}.

Every forward-global endpoint solution with U(0) in Sigma(H) either scatters in H1(H), or has

    U(t,x)=c exp(i theta(t)+i v.x/2) ell(t)^(-d/2)
                    Q((x-X(t))/ell(t))
               + exp(it Delta)F(x) + R(t,x),
    ||R(t)||_(H1(H)) -> 0,
    0<ell(t)<=C,
    X(t)=v t+x_0+o(1),
    F(x) in c-perp a.e.,
    Gamma(F)=Gamma(U)-Mc |c><c|,
    v=(2/Mc)[P(U)-P(F)].                           (1.5)

The primary part of the error is O(t^-1) in H1. In d=2 the full L2 error is O(t^-alpha) for every alpha<1/2. The two alternatives are disjoint. No positive limiting width, exact phase law, or uniform lower bound on ell is claimed.

**Subthreshold dynamics.** In d=2 assume m_2/m_1<=epsilon_0; in d=1 no occupation-gap assumption is required for this subthreshold assertion. Then m_1<Mc gives global H1 solutions with uniformly bounded kinetic energy. If the initial field also belongs to Sigma(H), it scatters in Sigma(H) in both time directions. The two-dimensional small-gap hypothesis is on m_2/m_1, not m_2/Mc, when m_1 changes below Mc.

## 2. Hilbert-valued local theory, without a component-count constant

This section supplies the analytic obligation left open in the R15 density-matrix note.

Scalar admissible Strichartz estimates extend to H-valued functions with the same constants. To see this directly, use an orthonormal basis of H, apply the scalar estimate coordinatewise, and apply Minkowski twice. For q,r>=2,

    ||(sum_j |f_j|^2)^(1/2)||_(L_t^q L_x^r)
      <= (sum_j ||f_j||_(L_t^q L_x^r)^2)^(1/2).

For the dual exponents q',r'<=2 the reverse comparison gives

    (sum_j ||g_j||_(L_t^q' L_x^r')^2)^(1/2)
      <= ||(sum_j |g_j|^2)^(1/2)||_(L_t^q' L_x^r').

Combining these inequalities with scalar homogeneous and retarded inhomogeneous estimates gives the corresponding vector estimates. Truncation in the basis and completion remove the finite-coordinate restriction. The pairs needed here are (q,r)=(4,4) in d=2 and (6,6) in d=1, together with (infinity,2). Spatial derivatives commute with the propagator.

The pointwise nonlinearity N(z)=||z||_H^(p-1)z satisfies

    ||N(z)-N(w)||_H
       <= C_p (||z||_H^(p-1)+||w||_H^(p-1))||z-w||_H,
    ||grad N(U)||_H <= p ||U||_H^(p-1)||grad U||_H.

The differentiated difference has the standard bound

    ||grad[N(U)-N(V)]||_H
      <= C_p (||U||+||V||)^(p-1)||grad(U-V)||
        +C_p (||U||+||V||)^(p-2)
                      (||grad U||+||grad V||)||U-V||.

These follow by differentiating the real-smooth polynomial map on the underlying real Hilbert space; the constants depend on p, not dim H. Holder with q=r=p+1 closes the usual contraction in

    C(I;H1(H)) cap L^(p+1)(I;W^(1,p+1)(H)).

The free Strichartz norm is small on a sufficiently short interval by absolute continuity. This gives existence, uniqueness, continuous dependence, and a maximal H1 lifespan. For uniform continuation on an H1 ball one needs slightly more than that pointwise-in-data absolute continuity. Sobolev embedding and unitarity give

    ||exp(it Delta)f||_(L_t^(p+1)(I;L_x^(p+1)(H)))
       <= C |I|^(1/(p+1)) ||f||_H1.

The derivative Strichartz norm is bounded by C||f||_H1; it need not be uniformly small on the ball. Choosing the preceding critical norm sufficiently small relative to the fixed H1 radius closes the contraction and differentiated estimates above, giving a local time depending only on that radius. A bounded H1 norm on a sequence of times approaching a finite endpoint therefore supplies a uniform extension time; hence every finite maximal endpoint has ||U(t)||_H1 tending to infinity. The usual continuation statement also follows if the critical L^(p+1) spacetime norm stays finite.

Let P_N be any increasing finite-dimensional orthogonal projections converging strongly to the identity in H. Solutions from P_N U_0 remain in ran P_N because the nonlinearity is a scalar multiple of U. Local stability gives

    U_N -> U in C(K;H1(H))

and in the derivative Strichartz space on every compact K inside the maximal lifespan. The approximation is a local-theory argument; no uniform-in-N global bound is required to establish it.

Mass, energy and total momentum follow by passing from finite-dimensional smooth approximants. The Hilbert diamagnetic inequality |grad ||U||||<=||grad U|| ensures the required Sobolev embeddings and continuity of the nonlinear energy. The same approximation yields individual and total continuity equations in distributions. Thus none of these identities is merely a formal infinite sum.

## 3. Trace-norm conservation and the fixed spectral tail

For U,V in L2(R^d;H), rank-one algebra and Cauchy–Schwarz give

    ||Gamma(U)-Gamma(V)||_(S1)
      <= (||U||_2+||V||_2)||U-V||_2.              (3.1)

Indeed, write |U><U|-|V><V| as |U-V><U|+|V><U-V| and use |||a><b|||_(S1)=||a||||b|| before integrating. Consequently finite-dimensional Gram conservation and the preceding local convergence prove

    Gamma(U(t))=Gamma(U_0) in S1                   (3.2)

at every lifespan time. Diagonalize this one fixed compact operator. Components in its kernel vanish in L2 at every time, since their integrated squared norm is zero. If P_N projects onto its first N positive eigenvectors, then exactly

    ||(I-P_N)U(t)||_2^2 = sum_(j>N) m_j            (3.3)

for every lifespan time. This is uniform component-tail control, not merely a pointwise-in-time spectral approximation.

Equation (3.3) is the substantive compactness input that fails for an arbitrary bounded set in H1(R^d;H). Such a bounded set is not locally L2 compact when H is infinite dimensional. Here finite-coordinate Rellich compactness plus (3.3) repairs the failure. No uniform smallness of high-mode kinetic tails is asserted or needed for strong sub-H1 convergence.

At a fixed time, normalized nonzero components u_j/sqrt(m_j) are an orthonormal family in scalar L2 and belong to H1. Their total weighted kinetic energy is A(U). The finite-rank static inequalities apply to P_N U. Kinetic energy increases to A(U), densities increase pointwise to ||U||^2, and monotone convergence gives the full sharp inequalities and remainders. This proves

    E(U) >= a E_1(u_1)+b A(V),
    0<=E_1<=E/a,      A(V)<=E/b,                  (3.4)

with the same positive a,b as R16/R17: a=1/2,b=1/64 in d=2, and the R17 a_epsilon,b_epsilon in d=1. In particular the constants do not depend on rank or on secondary trace. The trace must nevertheless be finite for the H1 state itself.

For subthreshold m_1<Mc, the homogeneous sharp inequalities give

    E >= (1/2)(1-m_1/Mc) A,                       d=2,
    E >= (1/2)(1-(m_1/Mc)^2) A,                   d=1.

Local continuation and conservation therefore prove the asserted uniform global H1 bounds.

## 4. Scalar principal concentration and automatic variance

At finite blowup, (3.4) bounds all secondary kinetic energy; hence the scalar principal kinetic norm tends to infinity. Normalized scalar GN stability gives, for every sufficiently late time,

    u_1=exp(i theta)lambda^(-d/2)Q((.-x(t))/lambda)+r_1,
    ||r_1||_2=O(lambda),     ||grad r_1||_2=O(1).  (4.1)

This is the scalar R16/R17 argument without an infinite-dimensional compactness step.

Scalar positivity at exactly Mc, after multiplying u_1 alone by exp(i b phi), gives

    |integral Im(conjugate(u_1)grad u_1).grad phi|^2
      <= 2E_1 integral |u_1|^2|grad phi|^2.        (4.2)

The common nonlinear potential is real, so the principal density has its own continuity equation. The bounded-test transport proof in R16/R17 consequently gives, for the extended unnormalized quadratic cost,

    W2_ext(|u_1(t)|^2 dx,|u_1(s)|^2 dx)
       <= integral_t^s sqrt(8E_1(r)) dr.          (4.3)

Its proof uses bounded smooth tests and tight finite-mass plans, so finite second moments are not assumed. Tightness follows by comparison with a fixed time and bounded relative transport cost. The single-profile approximation (4.1) and uniqueness of the bounded-Lipschitz terminal measure identify a unique Mc delta_(x_*). Passing to that terminal measure in (4.3) proves (1.2). This also gives lambda<=C(T-t), |x(t)-x_*|<=C(T-t), and the infinite-primary-variance global class exactly as in R17.

## 5. Joint terminal convergence: the two-dimensional equation

Let V be the entire H-valued secondary field and set M_s=||V||_2^2. Its gradient is uniformly bounded by (3.4). The exact energy decomposition gives

    I=integral |u_1|^2 ||V||_H^2 <=66E.

The nonlinear source has bounds directly in Bochner L1:

    || |u_1|^2 V ||_(L1(H)) <=sqrt(Mc I),
    || ||V||_H^2 V ||_(L1(H))
       <= || ||V||_H^2 ||_2 sqrt(M_s).

The latter density norm is uniformly bounded by the vector GN inequality and A(V). For s>1, H^s(R^2;H) embeds into L-infinity(R^2;H), with dimension-independent constant. Thus L1(H) embeds in H^(-s)(H). Also Delta V is bounded in H^(-1)(H). The equation gives

    ||partial_t V||_(H^(-s)(H)) <= C_s.

Hilbert Sobolev interpolation then gives the joint Cauchy estimate

    ||V(t)-V(r)||_(H^sigma(H))
       <= C |t-r|^((1-sigma)/(s+1)),
       s>1, 0<=sigma<1.

The terminal W exists in H1 by weak lower semicontinuity. This proof does not require Rellich compactness, summation of componentwise rates, finite variance, or a blowup hypothesis. It holds at every finite endpoint interval on which (3.4) holds. Trace-norm continuity (3.1) yields the entire identity Gamma(W)=Gamma(U)-Mc|c><c|.

## 6. Joint terminal convergence and the node: the one-dimensional equation

The scalar error in (4.1) satisfies ||r_1||_infinity=O(sqrt(lambda)) by the one-dimensional Sobolev estimate. Exponential decay of Q gives u_1(t)->0 uniformly on each compact set disjoint from x_*. The secondary Hilbert field obeys

    sup_t ||V(t)||_(H1(H))<infinity,
    sup_t ||V(t)||_(L-infinity(H))<infinity.

For a scalar psi in C_c-infinity(R minus {x_*}), the Bochner pairing integral V psi has uniformly bounded time derivative in H. Its linear part is bounded by ||V||_2||psi''||_2, and its nonlinear part by the uniform bound for (|u_1|^2+||V||^2)^2 on supp psi. Therefore pairings against finite-coordinate such tests have limits. These tests are dense in L2(R;H), so boundedness identifies a unique weak L2(H) terminal limit W.

Strong L2 convergence requires two distinct tails to be controlled.

First, the aggregate secondary density mu_s=||V||_H^2 dx satisfies

    partial_t mu_s+2 partial_x Im<V,V_x>_H=0,
    |Im<V,V_x>|^2/||V||^2 <= ||V_x||^2.

Its relative quadratic transport speed is at most 2||V_x||_2. Thus comparison with one fixed time gives uniform spatial tightness up to T, even if all second moments are infinite.

Second, the conserved Gram identity (3.3) gives uniform component-tail smallness. Given eta>0, choose N so sum_(j>N)m_j<eta^2, and then choose a bounded interval outside which all secondary fields have total L2 mass less than eta^2. On this interval, the first N coordinates are precompact in L2 by scalar Rellich. The two tails prove precompactness in global L2(R;H). Every cluster point is W by the weak-limit uniqueness. Hence

    V(t)->W strongly in L2(H),
    V(t)->W strongly in H^sigma(H), sigma<1,
    V(t) converges weakly in H1(H).                (6.1)

There is no appeal to false Hilbert-valued Rellich compactness. In particular the vector Sobolev inequality gives

    sup_x ||V(t,x)-W(x)||_H^2
       <= C ||V(t)-W||_2 ||partial_x(V(t)-W)||_2 ->0.

The node also holds jointly. Exact Gram orthogonality is the Bochner identity integral conjugate(u_1)V=0 in c-perp. Inserting (4.1) gives

    ||integral Q(y)V(t,x(t)+lambda y)dy||_H
       <= C sqrt(lambda).

The constant uses the finite total secondary mass and the O(lambda) scalar residual, not a sum of coordinatewise constants. The Hilbert-valued fundamental theorem of calculus gives

    ||V(t,x(t)+lambda y)-V(t,x(t))||_H
       <= sqrt(lambda |y|)||V_x||_2.

Since integral Q>0 and integral Q(y)sqrt(|y|)dy<infinity, this proves ||V(t,x(t))||_H=O(sqrt(lambda)). Uniform convergence and x(t)->x_* give W(x_*)=0 in H. Formula (3.1) once again passes the full secondary Gram operator to the limit in trace norm.

## 7. Joint weighted convergence: the total moment is essential

Assume V has finite *total* variance at one lifespan time:

    integral |x|^2 ||V(x)||_H^2 dx < infinity.      (7.1)

It is insufficient to assume only that every fixed coordinate has finite variance: their sum can diverge. All weighted statements in this note use (7.1).

In either spatial dimension, the aggregate secondary density has transport speed at most 2||grad V||_2, uniformly bounded by (3.4). Starting from one finite-moment time, it is Cauchy in the finite-mass P2 space at the terminal time. Its limit is already identified by joint strong L2 convergence as ||W||_H^2 dx. Consequently the total second moments converge. Joint unweighted L2 convergence implies weak convergence of xV to xW against compactly supported H-valued L2 tests; the moment bound extends this to all L2 tests. Since their norms converge, uniform convexity of L2 yields

    ||x(V(t)-W)||_(L2(H)) ->0.                    (7.2)

This avoids an unjustified interchange of an infinite sum with componentwise weighted limits. No separate high-mode weighted-tail estimate is needed after the aggregate P2 argument.

Pseudoconformal images of the secondary fields therefore scatter jointly in H1(H). Indeed compare the physical V near T to free evolution from W; the L2 and weighted errors tend to zero and their gradients are bounded. For h=T-t, differentiating the conformal map bounds the gradient error by

    h ||grad error||_2 + (1/2)||x error||_2 ->0.

All norm statements are joint Hilbert norms, and trace-norm Gram conservation follows from (3.1). With finite total secondary variance, the complete conformal energy is carried by free secondary radiation, using the R17 energy decomposition: nonnegative mixed potential terms are bounded in physical variables and acquire a factor h^2. The resulting formula is

    E(conformal U)= (1/2)||grad F||_(L2(H))^2
                 = (1/8)|| (x-x_*)W ||_(L2(H))^2.

## 8. Momentum, core trajectory and the global alternative

Define the total momentum by the absolutely integrable Hilbert pairing

    P(U)=Im integral <U,grad U>_H dx.

Its norm is at most ||U||_2||grad U||_2. Equivalently it is the absolutely convergent sum of scalar component momenta. It is continuous on H^(1/2)(R^d;H): each coordinate of momentum is a quadratic form with Fourier multiplier xi_k, bounded from H^(1/2) to H^(-1/2). Joint secondary convergence in H^(1/2) therefore gives P(V(t))->P(W), without exchanging unbounded coordinatewise limits.

The scalar principal centroid b_1 exists by (1.2) and obeys b_1'=2P(u_1)/Mc. Conservation gives P(u_1)->P_*. Hence

    b_1(t)=x_*-[2P_*/Mc](T-t)+o(T-t).

The profile center differs from this centroid by O((T-t)^2): expand the centered first moment of core+r_1, using ||r_1||_2=O(lambda), ||(x-x(t))r_1||_2=O(T-t), and the core position norm O(lambda). This proves the trajectory in (1.1).

Local Sigma(H) persistence and the pseudoconformal identities follow from the local theory by approximating in Sigma(H). The commutator identity for J=x+2it grad is componentwise scalar, while nonlinear estimates use only Hilbert norms. Thus, writing V0=||xU(0)||_2^2,

    ||JU||_2^2 - [8/(p+1)]t^2 ||U||_(p+1)^(p+1)=V0,

for p=3 in d=2 and p=5 in d=1. For a forward-global U in Sigma(H), set

    Z(s,y)=|s|^(-d/2) exp(i|y|^2/(4s)) U(-1/s,y/s),
    s<0.

It solves the same Hilbert-valued equation, has the same Gamma, and

    A(Z(s))=||J(t)U(t)||_2^2/4,
    E(Z)=V0/8,     t=-1/s.

The maximal H1 lifespan of Z either extends through zero or has a finite blowup endpoint there. In the regular case local Sigma(H) persistence gives a Sigma endpoint. Comparison with the free flow from that endpoint and inversion of the conformal map gives full H1 scattering.

In the singular case Sections 4–7 give the complete primary profile and joint secondary weighted limit. The finite-dimensional R17 inversion proof now consists entirely of scalar primary estimates and the joint bounds already established here. Explicitly, ell(t)=t lambda(-1/t), X(t)=-t x(-1/t), v=-x_*, and the refined trajectory gives X(t)=v t+x_0+o(1). The primary residual has L2 size O(lambda), gradient size O(1), and position norm relative to x_* of size O(|s|). Its inverse conformal image is O(t^-1) in H1, uniformly even if ell tends to zero. Replacing the quadratic core phase by the fixed carrier exp(i v.x/2) has the same error: the factor ell from the phase variation cancels the ell^-1 derivative of the scaled profile. Section 7 proves joint strong H1 radiation, giving (1.5).

The velocity identity follows by momentum conservation. Integrating cross terms by parts places their derivative on the small H1 residual, so no possibly unbounded core gradient appears. The real Q core with carrier exp(i v.x/2) has momentum Mc v/2.

The alternatives are disjoint in the Hilbert setting for the same scalar reason: project onto c. A bounded-width scalar principal Q core has persistent local mass, whereas every free scalar L2 solution loses mass uniformly in balls of fixed radius. The secondary radiation is identically orthogonal to c pointwise.

### The spatial coherence operator

There is also a basis-independent spatial formulation. Define the positive operator gamma_U on scalar L2(R^d) by

    gamma_U(x,y)=<U(y),U(x)>_H
               =sum_j u_j(x) conjugate(u_j(y)).

It is positive trace class and has the same positive eigenvalues as Gamma(U). The Hilbert–Schmidt factorization of this kernel gives

    ||gamma_U-gamma_B||_(S1)
       <= (||U||_2+||B||_2)||U-B||_2.

If B=c S+V with V(x) in c-perp pointwise, its cross operators vanish exactly, so gamma_B=|S><S|+gamma_V. Consequently the global nonscattering alternative has the trace-norm asymptotic

    ||gamma_U(t)-|S_t><S_t|
          -exp(it Delta)gamma_F exp(-it Delta)||_(S1) ->0.

The finite-time analogue is gamma_U(t)=|S_t><S_t|+gamma_W+o_(S1)(1). These are consequences of joint L2 convergence, not a claim that the concentrating rank-one operator itself has a trace-norm limit. They describe one coherent spatial mode separating from the full trace-class radiation operator while retaining every secondary occupation. No weighted kinetic trace-norm convergence is inferred when the core width can shrink to zero.

## 9. Subthreshold Sigma scattering in both dimensions

In d=2 write r=m_1/Mc; in d=1 write r=(m_1/Mc)^2. The homogeneous sharp inequality is

    (2/(p+1)) ||U||_(p+1)^(p+1) <= r A(U).

A common spatial phase preserves the full Gamma. Apply coercivity to exp(-i|x|^2/(4t))U and combine with the pseudoconformal identity to obtain

    ||J(t)U(t)||_2^2 <= V0/(1-r),
    ||U(t)||_(p+1)^(p+1)
       <= [(p+1)r V0]/[8(1-r)t^2].

Thus the joint critical spacetime norm is finite on both infinite tails. The Hilbert-valued Strichartz and derivative bounds in Section 2 give H1 scattering. Conformal compactification has bounded H1 and extends through its endpoint; Sigma persistence and the identity between the interaction-picture position norm and the conformal derivative error give convergence in Sigma(H), exactly as in the finite-component R17 proof. None of these steps sums separately obtained scattering states or assumes a uniform-in-component nonlinear asymptotic rate.

## 10. Infinite-rank hypotheses that cannot be erased

There are genuine limits to the extension.

1. Trace class, equivalently finite total mass, is essential in the present H1 formulation. Bounded occupation operator norm alone permits infinite mass and does not define the same equation class.
2. Countably many separately finite coordinate variances do not imply Sigma(H). The global dichotomy assumes finite total variance.
3. Not every summable spectrum admits a Sigma(H) realization. The harmonic oscillator -Delta+|x|^2 has eigenvalues e_j comparable to j^(1/d). For an orthonormal orbital family the rearrangement/min–max principle gives

       sum_j m_j (||grad phi_j||_2^2+||x phi_j||_2^2)
          >= sum_j m_j e_j.

   Thus a necessary condition for any Sigma realization is sum_j m_j j^(1/d)<infinity. It is sufficient for some realization by taking harmonic-oscillator eigenfunctions. This concerns existence of a Sigma state, not existence of a critical blowup with that exact spectrum.
4. Uniformly small component L2 tails do not give uniformly small component kinetic tails. The terminal physical convergence remains sub-H1; the strong H1 *radiation* result comes from conformal scaling plus strong weighted convergence, not an unproved kinetic-tail argument.
5. The d=2 gap hypothesis remains m_2/m_1<=epsilon_0. The d=1 simple-gap hypothesis remains strict. This note does not settle equal leading occupations, remove physical finite variance from the global alternative, or prove exact collapse scales.
6. The external one-dimensional sharp inequality remains an explicit dependence. Infinite-component generality does not turn that literature input into an internally proved historical breakthrough.

The result is a genuine infinite-rank dynamical extension: the conserved positive trace-class operator supplies exactly the compactness absent from an arbitrary Hilbert-valued Sobolev bound, and aggregate transport supplies exactly the joint weighted convergence absent from componentwise arguments. The equations, constants, error norms, Gram identities and scattering fields are all defined directly in the same Hilbert space.
