# Nonlinear orbital instability of slowly moving critical quartic ground waves

Date: 2026-10-08. This note continues the pure homogeneous mass-critical model. It adds no modified dispersion or different nonlinearity. The spectral input is the small-velocity spectral pair in [spectral-section.tex](../../manuscripts/critical-structures/spectral-section.tex). In this concrete quartic N≤3 setting, the branch, weighted regularity, and complementary gap follow from real-profile nondegeneracy; the latter remains explicit. The nonlinear argument below is an elementary one-negative-direction Hamiltonian argument, consistent with the general Lin–Zeng trichotomy theory; it is not asserted to be a new general instability principle.

## 1. Statement

Let N = 1, 2, or 3 and consider

    i u_t = Δ²u − |u|^(8/N) u       on R^N,

in X = H²(R^N; C), viewed as a real Hilbert space. Let Q be a real sharp critical optimizer solving

    Δ²Q + Q − |Q|^(8/N) Q = 0.

Assume only the material real-profile nondegeneracy ker L_+ = span{∂_jQ}. The local C² branch, admissible scaling derivative, and complementary spectral gap follow as proved in the added Section 8 below and in the companion TeX lemma. In particular, for U_v = U_(1,v), the Hessian L_v has kernel exactly

    K_v = span_R {iU_v, ∂_1 U_v, ..., ∂_N U_v}.

For every sufficiently small fixed v ≠ 0, the wave

    u_v(t,x) = exp(it) U_v(x − vt)

is nonlinearly orbitally unstable in H², even among perturbations having exactly the same mass, all components of momentum, and energy as U_v. More precisely, there are ρ_v > 0 and initial data u_(δ,v) such that

    M(u_(δ,v)) = M(U_v),    P(u_(δ,v)) = P(U_v),
    E(u_(δ,v)) = E(U_v),
    ||u_(δ,v) − U_v||_H² = δ + O_v(δ^(1+β)),

and their solutions have a first exit time τ_(δ,v) from the H² distance ρ_v to

    O_v = {exp(iθ) U_v(· − y): θ ∈ R, y ∈ R^N},

with

    τ_(δ,v) = (1/λ_v) log(1/δ) + O_v(1),        δ ↓ 0.

Here β = 1 in dimensions 1,2 and β = 2/3 in dimension 3, and λ_v is the positive eigenvalue from round 11:

    λ_v = sqrt(2 v^T T v / D_Q) + o(|v|),

where

    T_ij = <∂_i Q, L_-^(-1) ∂_j Q>,
    D_Q = <ΛQ, L_-^(-1)ΛQ> − c^T T^(-1)c > 0,
    c_j = <ΛQ, L_-^(-1) ∂_j Q>.

The constants ρ_v and the additive remainder may depend on v. No uniform simultaneous (δ,v) limit is claimed. For a fixed unit direction e one obtains the rigorous iterated limit

    lim_(r↓0) r [ lim_(δ↓0) τ_(δ,re)/log(1/δ) ]
       = sqrt(D_Q/(2 e^T T e)).

This proves actual departure from the phase-and-translation orbit, rather than just growth in a fixed gauge. It does not prove finite-time blowup, scattering, or the later fate of the departing trajectory.

## 2. The phase space and its nonlinear flow

Write α = 8/N and F(z) = |z|^α z, treating z ∈ C as a two-dimensional real vector. For N ≤ 3,

    H² ↪ L∞ ∩ W^(1,4),

and H² is an algebra. The Nemytskii map F: H² → H² is locally C^(1,β), with

    β = 1 for N = 1,2;       β = 2/3 for N = 3.

Here the assertion β = 2/3 is intentional: an unjustified quadratic H² remainder is not used for the nonintegral three-dimensional power.

A direct verification is as follows. For w ∈ H²,

    ∇F(w) = DF(w)∇w,
    ∇²F(w) = DF(w)∇²w + D²F(w)[∇w,∇w].

These terms lie in L², using L∞ for coefficients and W^(1,4) for the quadratic gradient product. For DF(w)h, differentiate twice; the terms are sums of

    DF(w) ∇²h,
    D²F(w)[∇w, ∇h],
    D²F(w)[∇²w,h],
    D³F(w)[∇w,∇w,h].

For N = 3, D³F is 2/3-Hölder on bounded sets; for N = 1,2 it is Lipschitz there. Subtracting the displayed expressions at two bounded H² arguments gives

    ||DF(w_1) − DF(w_2)||_(B(H²,H²))
      ≤ C_R ||w_1 − w_2||_H²^β

when their difference is at most 1. The L² and first derivative terms satisfy the same (weaker) bound. Smooth approximation justifies the weak chain rules. Integration along the segment gives

    ||F(U+h) − F(U) − DF(U)h||_H²
      ≤ C_R ||h||_H²^(1+β).                      (2.1)

The group exp(−itΔ²) is unitary on H². The usual contraction argument applied to its integral equation therefore gives local existence, uniqueness, continuous dependence, and continuation as long as the H² norm stays bounded. This uses no dispersive estimate. Mass, momentum, and energy are conserved: one can first insert a selfadjoint Fourier truncation P_n in the Hamiltonian nonlinearity P_n F(P_nu), where the differentiated conservation identities are valid, and then pass to the H² solution uniformly on compact existence intervals. The cutoffs commute with translations and phase rotations.

In the co-moving, co-rotating frame

    w(t,x) = exp(−it) u(t,x+vt) = U_v + h(t,x),

the equation is

    h_t = A_v h + R_v(h),       A_v = J L_v,  J = −i,

where R_v satisfies (2.1). All phase and translation transformations are isometries of H², so orbital distance in this frame agrees with orbital distance in the original frame.

## 3. Exactly one negative direction

At v = 0, the full real Hessian is diag(L_+,L_-). Sharp critical optimality gives nonnegativity of L_+ on {h: <Q,h> = 0}, and

    <Q,L_+Q> = −α ||Q||_(α+2)^(α+2) < 0.

Since L_- ≥ 0, its full negative index is exactly one.

For small v, write L_v as the constant-coefficient operator

    H_v = Δ² + 1 + i v·∇

minus the real symmetric matrix multiplier DF(U_v). The symbol of H_v is |ξ|⁴+1−v·ξ, bounded below by a positive constant for small v and comparable to 1+|ξ|⁴. Since U_v → Q in H² ↪ L∞, the potential converges in L∞. The drift is small as an operator H⁴ → L². Hence L_v converges to L_0 in norm-resolvent sense, with a common lower bound; the compact decaying potential and positive free symbol also keep the essential spectrum uniformly positive. The zero cluster has exactly dimension N+1 by the assumed exact symmetry kernel and spectral gap. Consequently no additional negative eigenvalue appears from zero, the essential spectrum, or −∞. Therefore

    n_−(L_v) = 1.                               (3.1)

This concrete perturbation argument is necessary: abstract continuity of a pseudoinverse alone would not rule out eigenvalues coming from −∞ in an unrelated operator family.

The profile equation and F(U_v) ∈ H² imply U_v ∈ H⁶ by elliptic inversion of H_v. Thus the symmetry vectors belong at least to H⁵. Every H² vector in ker L_v, and every H² eigenvector of A_v, improves to H⁶ because DF(U_v) is a bounded H² multiplier. These observations justify all pairings below; in particular A_v^*g ∈ L² for g ∈ K_v.

## 4. A semigroup estimate without spectral mapping

Fix one sufficiently small v ≠ 0 and suppress v. Let λ > 0 be the real eigenvalue. Choose real-space eigenvectors

    A Y_+ = λY_+,        A Y_- = −λY_-,

and normalize ||Y_+||_H² = 1. Let B(f,g) = <Lf,g> be the real symmetric action form. The Hamiltonian identity

    B(Af,g) + B(f,Ag) = 0                         (4.1)

implies B(Y_+,Y_+) = B(Y_-,Y_-) = 0. Moreover

    b = B(Y_+,Y_-) ≠ 0.

For example, if b = 0, their two-dimensional span would be totally isotropic modulo ker L. It is disjoint from ker L because applying A and A² to a linear combination gives both coefficients zero. A real symmetric Fredholm form of negative index one and positive coercive complement has isotropic dimension at most one modulo its kernel. This contradicts (3.1). Equivalently, algebraic simplicity of the two eigenvalues gives the nonzero right-left eigenvector pairing.

Thus W = span{Y_+,Y_-} is form-nondegenerate, has one negative and one positive direction, and

    X = W ⊕ Z,
    Z = {z: B(z,Y_+) = B(z,Y_-) = 0}.             (4.2)

The associated bounded projection is explicit:

    Π_W h = [B(h,Y_-)/b]Y_+ + [B(h,Y_+)/b]Y_-.

Both summands are invariant under exp(tA), by (4.1). Since W already consumes the sole negative direction, B is nonnegative on Z. Its null space there is exactly K = ker L. To see the latter assertion, B(z,z)=0 implies B(z,x)=0 for every x∈Z by polarization and nonnegativity, and also for x∈W by definition, so Lz=0.

Let Π_K be the L² orthogonal projection onto K. It maps Z into Z. There exists c_v>0 such that

    B(z,z) ≥ c_v ||(I−Π_K)z||_H²²,       z∈Z.  (4.3)

For completeness, the usual compactness proof is short. If (4.3) failed, there would be z_n∈Z∩K^⊥ with ||z_n||_H²=1 and B(z_n,z_n)→0. The positive free form is coercive on H². The decaying L∞ potential is compact from H² to H^(−2). Passing to a subsequence, weak lower semicontinuity of the free form plus compactness of the potential gives a limit z with B(z,z)≤0. Nonnegativity and the previous null-space statement force z∈K, while orthogonality forces z=0. Compactness then makes the potential term vanish, contradicting free coercivity and norm one.

The operator A generates a C⁰ group on H²: its free part −iH_v is skew-adjoint on H², and iDF(U_v) is a bounded real-linear H² operator. For data in its dense generator domain, differentiation gives conservation of B(exp(tA)z,exp(tA)z); approximation extends this to all H² data. Equation (4.3) controls the component orthogonal to K uniformly in time.

To control the remaining symmetry component, take an L² orthonormal basis g_j of K. Since Ag_j=0, writing h=z+k with z=(I−Π_K)h gives

    d/dt <h,g_j> = <Az,g_j> = −<Lz,Jg_j>,
    |d/dt <h,g_j>| ≤ C_v ||z||_H².

The last pairing is the H^(−2)-H² form pairing and needs only g_j∈H². It is valid for the continuous H² solution, whose derivative belongs to H^(−2), or by density from generator-domain solutions. Consequently

    ||exp(tA)|_Z||_(B(H²)) ≤ C_v(1+|t|).         (4.4)

On W the flow is exactly exp(±λt). Combining (4.2)–(4.4), and absorbing 1+t into a λ-dependent constant, yields

    ||exp(tA)||_(B(H²)) ≤ C_v exp(λt),    t≥0.  (4.5)

This proves the required growth estimate from the form geometry. It also excludes any faster hidden unstable modes. Neither spectral mapping nor an unverified semigroup theorem is being assumed.

## 5. An ancient trajectory on exactly the same mass, momentum, and energy levels

The exponentially growing mode can be realized by an actual nonlinear solution which converges to U in H² as t→−∞. This gives all conserved quantities exactly, without a finite-dimensional charge correction.

The nonlinear remainder obeys, on a small H² ball,

    ||R(h)|| ≤ C_R ||h||^(1+β),
    ||R(h_1)−R(h_2)||
      ≤ C_R (||h_1||^β+||h_2||^β)||h_1−h_2||.  (5.1)

The second inequality follows by integrating DR(h)=i[DF(U+h)−DF(U)], using Section 2. For ε>0 define the weighted Banach space of continuous functions h:(−∞,0]→H² with

    ||h||_* = sup_(t≤0) exp(−λt)||h(t)||_H².

On its closed ball ||h||_*≤2ε consider

    Φ(h)(t) = ε exp(λt)Y_+
      + integral_(−∞)^t exp((t−s)A) R(h(s)) ds.  (5.2)

The integral is a convergent H² Bochner integral, since t−s≥0 and (4.5) gives

    ||Φ(h)(t)−εexp(λt)Y_+||
      ≤ [C_v C_R 2^(1+β)/(βλ)]
           ε^(1+β) exp((1+β)λt).                (5.3)

The weighted Lipschitz constant of Φ on the ball is bounded by

    C'_v ε^β/(βλ).

Choose ε_v sufficiently small that this is less than 1/2 and that (5.3) is at most ε_v exp(λt). Banach contraction gives h_v on (−∞,0] satisfying (5.2). Splitting the integral at an arbitrary finite t_0 and using the group law shows that this is the mild solution of the nonlinear equation on [t_0,0]; local uniqueness identifies it with the H² flow. In particular,

    h_v(t) = ε_v exp(λt)Y_+
        + O_v(ε_v^(1+β) exp((1+β)λt)),   t≤0.  (5.4)

Because h_v(t)→0 strongly in H² as t→−∞, continuity and conservation of M,P,E yield, for every t≤0,

    M(U+h_v(t)) = M(U),
    P(U+h_v(t)) = P(U),
    E(U+h_v(t)) = E(U).                         (5.5)

The co-moving phase and translation transformations preserve these quantities, so conservation is valid in this frame too. Equation (5.5) is stronger than a first-order tangency statement. It also explains why the perturbation energy need not be adjusted separately: the unstable trajectory approaches the wave backward in time.

## 6. Actual orbital exit and its logarithmic time

The symmetry orbit has tangent K at U. Its parameter map (θ,y)↦exp(iθ)U(·−y) is C² into H², with injective differential. It has no nontrivial stabilizer: a phase-periodic nonzero translation would make |U|² periodic in one direction and contradict integrability. Also, translations tending to infinity cannot approach U in H² (already in L²). Hence the local orbit chart describes every orbit point sufficiently close to U.

Put

    η_v = dist_H²(Y_+,K) > 0.

Positivity follows because A annihilates K but AY_+=λY_+≠0. Taylor expansion of the local orbit chart gives, for 0<a≤a_(0,v),

    dist_H²(U+aY_+, O_v) ≥ (η_v/2) a.           (6.1)

For clarity, this does not presume existence of a global nearest orbit point. Every competitor with distance at most twice the distance to U lies in the local chart, its parameters have size O(a), and projecting its Taylor expansion orthogonally off K gives the bound. All remaining competitors are farther away.

Let

    C_(nl,v) = C_v C_R 2^(1+β)/(βλ).

In addition to the contraction requirements, choose ε_v≤min{a_(0,v),r/4} so that

    C_(nl,v) ε_v^β ≤ η_v/4.                          (6.2)

Then (5.3), (6.1), and the triangle inequality give

    dist_H²(U+h_v(0), O_v) ≥ η_v ε_v/4.         (6.3)

Take ρ_v=η_vε_v/8. For δ∈(0,ε_v) define

    t_δ = λ^(-1) log(δ/ε_v)<0,
    u_(δ,v) = U+h_v(t_δ).

By (5.4),

    u_(δ,v)−U = δY_+ + O_v(δ^(1+β)),

and all conserved quantities agree exactly by (5.5). Its co-moving solution is U+h_v(t+t_δ), up to time

    T_δ = −t_δ = λ^(-1) log(ε_v/δ).

It exists throughout this interval by the constructed ancient solution. Its orbital distance at T_δ exceeds ρ_v by (6.3), while initially it tends to zero. Let τ_δ be its first hitting time of ρ_v. Since

    ||h_v(t+t_δ)||_H² ≤ 2δexp(λt),

one has

    λ^(-1) log(ρ_v/(2δ)) ≤ τ_δ
      ≤ λ^(-1) log(ε_v/δ).

This proves the first-exit asymptotic and the theorem.

The choices above explicitly display the dependence on the semigroup constant, the nonlinear Hölder bound, and the transversality η_v. They do not establish a uniform lower bound for ε_v or ρ_v as v→0. The unstable eigenvectors approach the neutral sector, and spectral projections can become ill-conditioned in that limit. The fixed-v theorem and the iterated time-scale limit in Section 1 are what is proved.

## 7. Relation to prior work and proof scope

Primary sources checked on 2026-10-08:

1. Z. Lin and C. Zeng, *Instability, index theorem, and exponential trichotomy for Linear Hamiltonian PDEs*, arXiv:1703.04016v4, https://arxiv.org/abs/1703.04016. Their theory establishes a general Hamiltonian decomposition and polynomially bounded center dynamics. Section 4 above proves the required special case directly using the single negative direction, so none of their abstract hypotheses is imported without verification.
2. D. Bonheure, J.-B. Castéras, E. Moreira dos Santos, R. Nascimento, *Orbitally stable standing waves of a mixed dispersion nonlinear Schrödinger equation*, arXiv:1710.09775v2, https://arxiv.org/abs/1710.09775. Their abstract includes nondegeneracy under suitable conditions; it must not be used to assert the pure quartic mass-critical nondegeneracy needed here. Their full text identifies their Theorem 3.16 as a regime β≥2√α for a mixed fourth/second-order ODE, excluding β=0.
3. V. Iyer, R. Parker, A. G. Stefanov, *Existence and stability for traveling waves of fourth order semilinear wave and Schrodinger equations*, arXiv:2512.12390v1, https://arxiv.org/abs/2512.12390. It concerns a different mixed-dispersion/cubic setting in its Schrödinger section and explicitly uses nondegeneracy. It does not discharge our pure quartic hypothesis.

The new step relative to round 11 is the complete nonlinear orbital conclusion, its realization by an ancient trajectory on exact mass-momentum-energy level sets, and the first-exit time controlled by the previously calculated small-velocity eigenvalue. The nonlinear instability mechanism itself is classical. The unresolved profile hypothesis is clearly retained, and no universal blowup or scattering assertion is made.

## 8. Removing the redundant branch, decay, and gap assumptions in the concrete quartic class

The final theorem in [nonlinear-flow-section.tex](../../manuscripts/constrained-dynamics/nonlinear-flow-section.tex) has only one extra material hypothesis beyond Q being a real sharp ground profile: ker L_+ consists exactly of translations. The other inputs of round 11 follow here, as follows.

First, sharp phase coercivity supplies L_-≥0, ker L_-=RQ and its complementary inverse. From Q∈H² and the Nemytskii estimates, the equation gives Q∈H⁶. Thus V=|Q|^(8/N) lies in W^(2,∞) and tends to zero at infinity.

Choose φ_R smooth bounded truncations of a<x>, with all derivative bounds uniform and |∇φ_R|+|Δφ_R|≤Ca. Set w_R=e^(φ_R)Q. Testing (Δ²+1−V)Q=0 with e^(2φ_R)Q gives the exact real quadratic identity

    Re<Δ²Q,e^(2φ_R)Q>
      = ||Δw_R+|∇φ_R|²w_R||²
         − ||2∇φ_R·∇w_R+(Δφ_R)w_R||².

Its difference from ||Δw_R||² is at most Ca²||w_R||_H²². Choose a fixed ball outside which V≤1/4. Its interior weighted potential contribution is bounded independently of R; the exterior and the small-a error are absorbed. Hence e^(a<x>)Q∈H². Conjugating the equation gives Δ²+1 plus smooth bounded coefficients of order at most three. Since V∈W^(2,∞), successive elliptic gains H²→H³→H⁴→H⁵→H⁶ show e^(a<x>)Q∈H⁶. Therefore ΛQ∈H⁴ and L_+ΛQ=−4Q. This is an elementary fourth-order exponential-weight argument and does not assume Q is positive.

Second, use the profile map Fcal:H⁴×R^(N+1)→L² and its symmetry slice. Augment Fcal(U,ω,v)=Σ b_j g_j, <U−Q,g_j>=0, where g=(iQ,∂Q). The derivative in (U,b) is invertible by selfadjoint Fredholm decomposition and the assumed real nondegeneracy. The map is C², so the implicit-function theorem produces a C² branch. Invariance implies <Fcal(U),iU>=<Fcal(U),∂_jU>=0. The pairing matrix of fixed and moving symmetry vectors is invertible near Q, forcing b=0. Local uniqueness in the slice makes the branch scaling-closed up to phase/translation, gives the action derivatives, and yields D_(v_j)U|_0=−iL_-^(-1)∂_jQ.

Finally, potentials converge in L∞ and drift is small H⁴→L², so Hessians converge in norm resolvent on common domain H⁴. The isolated zero cluster keeps dimension N+1; the actual symmetry vectors already give N+1 independent kernel vectors and therefore fill it. The complementary inverse, extended by zero, is norm-continuous. This verifies the fourth assumption of the general spectral theorem without adding a new hypothesis.
