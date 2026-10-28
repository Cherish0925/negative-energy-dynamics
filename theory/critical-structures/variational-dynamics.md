# a sharp high-frequency energy barrier and actual conservative dynamics

Date: 2026-10-08. This note proves a dynamic consequence of the round 10 constrained-variational analysis. It does not assume that every negative-energy state blows up. The central new deduction is that the high-frequency homogeneous optimizer manifold fixes the energy level at which kinetic concentration can first escape.

## 1. Setting and precise hypotheses

Let N>=1, m>1, s=m/2, r=m/N, p=2+2r. Let a be a real, even, positive elliptic m-homogeneous Fourier symbol. Define

    M(f)=||f||_2^2,
    A(f)= integral a(xi)|fhat(xi)|^2 dxi,
    E_a(f)= A(f)/2 - ||f||_p^p/p.

Let Mc be the sharp mass in

    ||f||_p^p/p <= (M(f)/Mc)^r A(f)/2.

Use the normalized equality manifold

    G = {Q: M(Q)=Mc, A(Q)=1, E_a(Q)=0}.

We use the sharp-GN compactness proved in the earlier foundation: every normalized near-equality sequence is strongly compact in H^s after translations and extraction. No uniqueness or linearized nondegeneracy is assumed. This is the sole non-elementary compactness input below.

Let d be a real, even, bounded measurable symbol, and suppose

    d(R theta) -> d_inf(theta), uniformly on S^{N-1}, R -> infinity,

where d_inf is bounded and even. No sign assumption on d or d_inf is needed. Set

    k = a-d,
    D(f)= integral d(xi)|fhat(xi)|^2 dxi,
    E_k(f)=E_a(f)-D(f)/2.

Since d is bounded, k differs from a by a bounded self-adjoint operator on every H^sigma. In particular E_k is continuous on H^s. Define

    e_inf = -(1/2) max_{Q in G} integral d_inf(xi/|xi|)|Qhat(xi)|^2 dxi.        (1)

The maximum exists: the bounded multiplier form is strongly L2 continuous and translation/phase invariant, and G is compact modulo those symmetries. The kinetic normalization in G is immaterial because d_inf is degree zero.

## 2. Energy of every concentrating sequence

THEOREM 1. Suppose M(f_n)<=Mc, A(f_n)->infinity, and sup_n E_k(f_n)<infinity. Then, after extraction,

(a) M(f_n)->Mc;
(b) writing t_n=A(f_n)^{1/m} and f_n(x)=t_n^{N/2} V_n(t_n x), the V_n converge strongly in H^s, after translations, to some Q in G;
(c)

    D(f_n) -> integral d_inf(xi/|xi|)|Qhat(xi)|^2 dxi,
    liminf E_k(f_n) >= -(1/2) integral d_inf |Qhat|^2 >= e_inf.              (2)

PROOF. Since M(f_n)<=Mc, E_a(f_n)>=0. Boundedness of d and the energy upper bound give

    0 <= E_a(f_n)=E_k(f_n)+D(f_n)/2 <= C.

Thus A(V_n)=1 and E_a(V_n)=t_n^{-m}E_a(f_n)->0. The sharp inequality also gives

    0 <= [1-(M(f_n)/Mc)^r]/2 <= E_a(V_n)->0,

which proves M(f_n)->Mc. Normalize the masses to Mc by factors tending to one; the resulting sequence remains a normalized sharp-GN near-optimizer. Sharp-GN compactness, followed by undoing those vanishing normalizations, proves (b).

The translations are irrelevant to all Fourier modulus integrals. Strong L2 convergence and boundedness of d imply

    integral d(t_n xi)(|Vhat_n|^2-|Qhat|^2) ->0.

For each xi!=0, d(t_n xi)->d_inf(xi/|xi|). Dominated convergence gives the first line of (2). Since E_a(f_n)>=0, the energy lower bound follows. QED.

COROLLARY 2 (uniform boundedness strictly below the concentration energy). For every e<e_inf,

    sup { A(f): M(f)<=Mc, E_k(f)<=e } < infinity.                           (3)

The set may of course be empty. If (3) failed, Theorem 1 would contradict e<e_inf. Notice that this is a uniform statement including masses approaching Mc from below, not just a bound on a single exact mass surface.

SHARPNESS. Choose Q in G attaining the maximum in (1), and put Q_lambda=lambda^{N/2}Q(lambda x). Then

    M(Q_lambda)=Mc, A(Q_lambda)=lambda^m,
    E_k(Q_lambda)=-D(Q_lambda)/2 -> e_inf.

Therefore for every e>e_inf, the sublevel {M=Mc,E_k<=e} is unbounded in H^s. This proves the optimality of e_inf as a strict energy barrier for mass-energy coercivity. It does not by itself produce a blow-up orbit at or above the barrier. At equality e=e_inf, whether the sublevel is bounded depends on the symbol; in the decaying positive-deficit example below it is unbounded.

### Independence from the zero of frequency

At critical mass the comparison is invariant under k->k+c. Such a change merely multiplies solutions by exp(-ict); it changes the energy by cM/2 and changes e_inf by cMc/2. Thus E_k-e_inf at M=Mc is unchanged. The concentration energy is a physical comparison level for the fixed equation, not an arbitrary choice of energy zero.

## 3. Global dynamics below this energy

Explicit flow hypothesis (F): for every initial datum in H^s the equation

    i u_t = k(D)u - |u|^{p-2}u                                           (4)

has a unique maximal solution u in C((T_-,T_+),H^s), continuous dependence in H^s, conservation of M and E_k, and the continuation property that a finite endpoint forces ||u(t)||_{H^s}->infinity. The assertions below require exactly this flow hypothesis; ellipticity of an arbitrary homogeneous symbol alone is not silently substituted for a dispersive local theory.

THEOREM 3. Under (F), if

    M(u_0)<=Mc,  E_k(u_0)<e_inf,

then T_-=-infinity, T_+=infinity and

    sup_{t in R} ||u(t)||_{H^s}<infinity.

PROOF. Conservation places the entire maximal orbit in the fixed strict sublevel (3). Its H^s norm is bounded, so the continuation property excludes either finite endpoint. QED.

All strictly subcritical masses M(u_0)<Mc are global and uniformly H^s bounded, with no energy restriction: the direct inequality

    E_k(f) >= [1-(M(f)/Mc)^r] A(f)/2 - ||d||_infty M(f)/2                  (5)

already gives coercivity. The significance of Theorem 3 is precisely the critical mass M=Mc, where the coefficient in (5) vanishes.

### A complete unconditional local theory in a concrete quartic class

For m=4 and N=1,2,3, (F) follows directly for every real even symbol k comparable with |xi|^4 up to bounded lower terms, including arbitrary elliptic anisotropy in a. No dispersive estimate is needed in these dimensions.

Indeed, H2(R^N) embeds into Linfinity and W^{1,4}. For alpha=8/N>2, the function F(z)=|z|^alpha z has locally Lipschitz second derivative on C identified with R2. The ordinary chain/product rule therefore gives, for bounded H2 balls,

    ||F(u)-F(v)||_{H2} <= C_R ||u-v||_{H2}.

For clarity, the second-derivative terms are F'(u)D2u and F''(u)(Du)^2: the H2 difference is controlled using H2->Linfinity, H2->W^{1,4}, and local Lipschitz continuity of F' and F''. The real multiplier generates a unitary group on H2, so the Duhamel map is a contraction in C([-T,T],H2) for T depending only on the initial H2 norm. This yields uniqueness, continuous dependence, and the H2 blow-up alternative.

Mass and energy conservation can be justified without presuming an unavailable arbitrary-order smoothness of the power. Let P_R be the orthogonal Fourier projection to |xi|<=R and solve

    i (u_R)_t = k(D)u_R - P_R F(u_R),  u_R(0)=P_R u_0.

The band-limited subspace is preserved. There k(D) is bounded; taking the real L2 pairing with the energy gradient yields dE_k(u_R)/dt=0 because P_R is self-adjoint and u_R lies in its range. Mass is conserved for the same reason. The uniform local H2 contraction and P_R->Id strongly on H2 imply u_R->u in C([-T,T],H2). Continuity of mass and energy passes conservation to u. Iterate on its maximal lifespan. Thus Theorem 3 is an actual PDE theorem, without an external well-posedness hypothesis, in this quartic N<=3 class.

For arbitrary dimensions and homogeneous symbols the broader version remains conditional only on the explicitly stated local flow theory. In particular, a citation proving a pure radial |xi|^4 propagator estimate is not enough to license arbitrary anisotropic symbols.

## 4. Application to the two-threshold interpolation model

Take

    k_q(xi)=a_0(xi)+h(xi)|xi|^q/(1+|xi|^q)
           =a_infinity(xi)-d_q(xi),
    h=a_infinity-a_0>0,
    d_q(xi)=h(xi)/(1+|xi|^q),

with a_0,a_infinity positive elliptic m-homogeneous and h positive elliptic. Write M_0 and M_infinity for the two sharp homogeneous masses.

For EVERY q>0 and every M<M_infinity, the round 10 estimate k_q>=(1-eta)a_infinity-C_eta and conservation prove global bounded evolution under (F). This includes negative-energy data in the window M_0<M<M_infinity.

At the upper endpoint:

* q>m: d_q is bounded and tends uniformly to zero at infinity. Thus e_inf=0. EVERY datum with M=M_infinity and E_{k_q}<0 generates a global uniformly H^s-bounded solution. This is not restricted to a minimizer, a near-ground state, radial symmetry, small perturbations, or a sign of momentum. The conclusion rules out both finite-time blow-up and unbounded infinite-time growth in this whole endpoint class.

* q=m: d_q tends to the degree-zero symbol h(theta). The exact energy barrier is the optimizer-dependent number (1). If the constrained infimum I(M_infinity)<e_inf, its sublevel supplies nonempty globally bounded endpoint dynamics. For isotropic h=epsilon|xi|^m, e_inf=-epsilon M_infinity/2; every nonzero admissible function has energy strictly larger than this number, so the theorem is empty there. No endpoint global assertion is inferred in the isotropic borderline case.

* q<m: d_q is unbounded at high frequencies, so Theorem 1 does not apply. Round 10 gives I(M_infinity)=-infinity, which is a variational statement and does not itself prove finite-time blow-up.

For q>m, sharpness at zero is especially transparent. If Q is an a_infinity optimizer, then E_{k_q}(Q_lambda)<0 for every finite lambda and tends to zero while A_infinity(Q_lambda)->infinity. Thus one cannot replace the strict fixed negative energy by a uniform statement covering all negative energies arbitrarily close to zero.

## 5. Orbital stability: exact perturbation classes

Let

    Sigma_c={U: M(U)=c, E_k(U)=I(c)}.

Distances to this entire set already include translations and constant phases. No uniqueness is claimed.

THEOREM 4.

(i) In the round 10 open mass window M_0<c<M_infinity, Sigma_c is orbitally stable in H^s under arbitrary sufficiently small H^s perturbations, provided (F) holds.

(ii) At c=M_infinity, assume I(c)<e_inf and minimizing sequences at mass c are precompact in H^s modulo translation (as already proved for q>m). Then Sigma_c is orbitally stable against sufficiently small H^s perturbations satisfying M(u_0)<=c. In particular it is stable on the exact mass surface M=c. Every such perturbed orbit is global.

PROOF. If stability fails, choose initial data u_{0,n} with distance to Sigma_c tending to zero, and times t_n in their maximal lifespans with distance of f_n=u_n(t_n) bounded away from zero. Conservation gives

    M(f_n)->c, E_k(f_n)->I(c).

In (i), all masses are eventually uniformly below M_infinity, and the subcritical coercivity estimate bounds f_n in H^s. In (ii), I(c)<e_inf and M(f_n)<=c allow Corollary 2 to give the same bound. The same energy estimates prove all these solutions global before any contradiction argument.

Define g_n=sqrt(c/M(f_n)) f_n. Because f_n is bounded in H^s, g_n-f_n->0 in H^s and E_k(g_n)->I(c). The g_n are an exact-mass minimizing sequence. Its compactness modulo translations implies distance(g_n,Sigma_c)->0, hence the same for f_n, a contradiction. QED.

The one-sided condition in (ii) is essential to the proof. Arbitrarily small perturbations may otherwise cross above M_infinity, where the energy is unbounded below and the kinetic coercivity used here is lost. We have NOT proved ordinary unconstrained orbital stability of the endpoint set, nor proved its instability. The standard Cazenave--Lions compactness argument does not erase this distinction.

## 6. Exact lifting of the critical scale degeneracy

For k_q above, let U be any mass-constrained energy minimizer and let

    U_t(x)=exp(Nt/2)U(exp(t)x).

This scalar energy curve is twice differentiable by dominated convergence of the Fourier integrals; it does not require that t->U_t be differentiable in H^s, hence imposes no spatial moment on U. Its first derivative at zero vanishes. Define its curvature

    K(U)=d²/dt² E_{k_q}(U_t)|_{t=0}.

Put z=|xi|^q. Direct differentiation and elimination of the first derivative give the exact identity

    K(U) = (q/2) integral h(xi) z [(m+q)+(m-q)z]/(1+z)^3 |Uhat(xi)|² dxi.  (6)

Derivation: with D=xi dot grad_xi and b=h z/(1+z),

    E(U_t)=exp(mt)E_{a_0}(U)+B(U_t)/2,
    0=m E_{a_0}(U)+(1/2) integral D b |Uhat|²,
    K=(1/2) integral (D²-mD)b |Uhat|²,
    (D²-mD)b=q h z [(m+q)+(m-q)z]/(1+z)^3.

For 0<q<=m the integrand in (6) is strictly positive for every xi!=0, hence K(U)>0 for every nonzero constrained minimizer. Thus the perturbation removes the exactly flat scale direction of the homogeneous critical optimizer. This is a precise energy statement, not a claim that the full Hamiltonian spectrum has been calculated.

For q>m the integrand changes sign at z=(m+q)/(q-m). Minimality still gives K(U)>=0, but strict positivity globally does not follow from the pointwise formula.

### Sharp stiffness at the lower threshold

Use the round 10 assumptions ensuring profile selection. Write

    alpha=M/M_0, d=alpha^(m/N)-1,
    U_M(x)=sqrt(alpha) lambda_M^{N/2} V_M(lambda_M x),
    A_0(V_M)=1, M(V_M)=M_0.

Round 10 proves lambda_M~beta_* d^(1/q), normalized optimizer selection, and

    B(U_M)/A_0(U_M) = m d/(m+q)+o(d).

Then (6) gives, for ANY q>0,

    K(U_M) ~ (m q/2) d A_0(U_M),                                        (7)
    K(U_M)/|I(M)| -> m(m+q).                                            (8)

In particular the scale curvature is strictly positive sufficiently near the lower threshold even when q>m.

A technical point in (7): strong H^s convergence alone does not imply convergence of the higher moment. The round 10 proof additionally establishes convergence of the normalized correction energy D_lambda(V_M) to C_min. Together with local Fourier convergence, this makes the nonnegative correction-energy measures tight. The factor multiplying that measure in (6) is bounded and converges on every compact annulus to q(m+q)/2. Tightness therefore proves K/B -> q(m+q)/2; combine with B/A_0 above. No extra uniform high-moment assumption on actual minimizers is introduced.

For the fixed-scale joint limit k_epsilon=a+epsilon b_0, alpha_epsilon=(1+epsilon tau)^(1/r), the exact same identity gives, along any selected-profile subsequence U_epsilon/sqrt(alpha_epsilon)->Q,

    K(U_epsilon)/(alpha_epsilon epsilon)
      -> (1/2) integral (D²-mD)b_0 |Qhat|².

This uses ordinary H^s continuity of the order-m differentiated multiplier. For q<=m the limiting number is positive. Consequently an arbitrarily weak perturbation produces a positive restoring curvature of order epsilon at the selected finite spatial scale.

### What this does not yet determine: oscillation frequency

The curvature K is not, by itself, the frequency of a genuine oscillatory eigenmode. In Hamiltonian linearization one must also solve for the conjugate phase and remove translation/phase modes. Under a separate isolated simple constrained-scale mode hypothesis, with Lambda Q in the required energy domain, adequate operator convergence, and control of its couplings to other modes, the formal leading denominator is the phase-metric norm after removing translation coupling:

    Lambda Q=N Q/2+x dot grad Q,
    T_ij=<partial_i Q,L_{-,Q}^{-1} partial_j Q>,
    c_i=<partial_i Q,L_{-,Q}^{-1} Lambda Q>,
    D_Lambda=<Lambda Q,L_{-,Q}^{-1} Lambda Q>-c^T T^{-1}c.

For an even Q, parity gives c=0. The lower-threshold frequency would then obey

    nu_M² ~ [m q/(2 D_Lambda)] d lambda_M^(2m).

This last formula is a derived candidate, NOT a theorem in this note. Establishing existence/isolation of that spectral pair for the singular symbol limit remains a separate problem. It is not needed for any global existence, stability-of-set, or exact-curvature assertion above.

## 7. Extension beyond the local power nonlinearity

Theorems 1--3 use only: (a) a mass-critical homogeneous energy E_a=A/2-F with E_a>=0 at M<=Mc; (b) compactness of normalized zero-energy sequences; (c) a bounded quadratic change -D/2. Their proofs do not use locality of F or a polynomial expansion. They therefore apply verbatim to a mass-critical Hartree interaction whenever its sharp inequality and optimizer compactness are available. The exact curvature calculation in section 6 likewise uses only F(U_t)=exp(mt)F(U). The orbital stability argument additionally requires energy continuity and compactness of the corresponding constrained minimizers. These hypotheses must be verified for the interaction under study; they are already verified for the local model used for the concrete PDE result here.

## 8. Relation to established methods and source checking

The set-stability step is the classical concentration-compactness mechanism of Cazenave and Lions; it is not asserted as a new method. The actual additional conclusion is the critical-mass energy bound obtained from the full high-frequency optimizer manifold, including an angular limiting symbol, and its consequence for ALL endpoint negative-energy data in the decaying-deficit class. Novelty priority for this precise class has not been established by an exhaustive literature comparison.

Primary sources:

1. T. Cazenave and P.-L. Lions, "Orbital stability of standing waves for some nonlinear Schrödinger equations", Communications in Mathematical Physics 85 (1982), 549--561. Publisher URL: https://link.springer.com/article/10.1007/BF01403504 . Tool reference .
2. A. Fernández, L. Jeanjean, R. Mandel, M. Mariș, "Non-homogeneous Gagliardo--Nirenberg inequalities in R^N and application to a biharmonic non-linear Schrödinger equation", https://arxiv.org/pdf/2010.01448 . Tool reference . This is relevant prior work on compact constrained minimizers and orbital stability for nonhomogeneous dispersion; its concrete mixed symbol differs from the bounded high-frequency deficit considered here.
3. B. Pausader, "The cubic fourth-order Schrödinger equation", https://arxiv.org/pdf/0807.4916 . Tool reference . Its Section 3 supplies a primary source for biharmonic dispersive/Strichartz local theory, but does not establish arbitrary-symbol local well-posedness. The explicit N<=3 argument above is independent of that extension.

No claim of finite-time collapse above a variational threshold is made. No ordinary endpoint orbital stability across supercritical mass perturbations is claimed. The principal conclusions are genuine nonlinear-in-time statements at and below the critical high-frequency mass, not merely stationary-profile results.
