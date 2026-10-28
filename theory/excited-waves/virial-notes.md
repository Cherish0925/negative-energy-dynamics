# Nonradial mass-critical BNLS: checked virial route and angular-regularity extension

Research notes, 7 October 2026. These notes do **not** establish finite-time blowup for every nonradial negative-energy H² datum. They establish an obstruction to a tempting interpolation step and a conditional extension of the radial defect argument. The mathematical derivations below have been independently checked at the level indicated; no priority claim is made for the conditional extension.

## 1. Equation, normalization, and exact localized identity

Let N≥2, p=2+8/N, and

    i u_t = Δ²u − |u|^(p−2)u,
    m = ||u||₂²,
    E = (1/2)||Δu||₂² − (1/p)||u||_p^p < 0.

For real smooth φ with bounded first through sixth derivatives, put

    M_φ(u) = 2 Im ∫ conjugate(u) ∇φ·∇u.

For smooth solutions, integration by parts gives

    M_φ' = 8 Re Σ_ijk ∫ φ_jk conjugate(u_ij)u_ik
           − 4 Re Σ_jk ∫ (Δφ)_jk conjugate(u_j)u_k
           − 2∫Δ²φ |∇u|² + ∫Δ³φ |u|²
           − [8/(N+4)]∫Δφ |u|^p.

The conjugates are essential. This identity extends to H² solutions through the usual solution approximation/localized multiplier argument. For the unbounded quadratic φ=|x|²/2, when the virial itself and the integrations are justified,

    M_φ' = 16E.

This identity alone is not a finite-time contradiction: M_φ is not nonnegative, and its linear decrease can coexist algebraically with infinite-time norm growth. The usual second-order NLS variance identity does not carry over unchanged.

## 2. Exponential weight: all steps except nonlinear absorption are nonradial

Set r=|x|, h=exp(−r⁴/R⁴), ∇φ_R=xh,

    ω_R = 1−h,
    D_R = ∫ω_R |D²u|_F²,
    M_R = M_{φ_R}.

The Hessian eigenvalues are h tangentially and h(1−4r⁴/R⁴) radially. Consequently I−D²φ_R≥ω_R I. Also

    Δφ_R = h(N−4r⁴/R⁴),
    0 ≤ N−Δφ_R ≤ (N+4)ω_R,
    |∇²Δφ_R|+|Δ²φ_R| ≤ C_N R^(−2)√ω_R,
    |Δ³φ_R| ≤ C_N R^(−4).

The elementary inequality z exp(−z)≤1−exp(−z), z≥0, supplies the nonlinear coefficient bound.

Let g_R=√ω_R. It is smooth (g_R behaves as r²/R² at the origin), and ||Δg_R||∞≤C_N R^(−2). Integration by parts and Cauchy–Schwarz give

    ∫g_R|∇u|²
      = −Re∫g_R conjugate(u)Δu +(1/2)∫Δg_R|u|²
      ≤ √N m^(1/2)D_R^(1/2)+C_N R^(−2)m.

Thus, for each η>0, the exact identity implies

    M_R' ≤ 16E −(8−η)D_R
             +8∫ω_R|u|^p +C_(N,η) R^(−4)m.       (V)

No radial assumption has been used.

Since |∇φ_R|²≤R²√ω_R, another Cauchy–Schwarz estimate gives

    |M_R| ≤ C_N m+C_N R m^(3/4)D_R^(1/4).         (B)

In particular, with B₀=C_Nm,

    D_R ≥ c_N R^(−4)m^(−3)(|M_R|−B₀)_+⁴.        (B')

The obstacle is therefore precise: absorption of the weighted nonlinear term into D_R with a time-uniform remainder.

## 3. A proposed unrestricted absorption inequality is false

The inequality

    ∫ω_R|u|^p ≤ ε D_R(u)+C_(ε,m)R^(−4)           (F)

cannot hold for all nonradial H² functions and every ε>0.

Fix x₀≠0 and nonzero f∈C_c^∞. Let

    u_λ(x)=λ^(N/2)f(λ(x−x₀)).

Its mass is independent of λ. By change of variables and dominated convergence,

    λ^(−4)∫ω_R|u_λ|^p → ω_R(x₀)||f||_p^p,
    λ^(−4)D_R(u_λ) → ω_R(x₀)||D²f||₂².

Dividing (F) by λ⁴ and letting λ→∞ forces ||f||_p^p≤ε||D²f||₂² for every ε, a contradiction. This is a counterexample to a functional inequality, **not** a counterexample to finite-time blowup.

Even allowing C to depend on fixed negative energy does not fix the obstruction. Choose f∈C_c^∞ nonzero with E(f)=0 by adjusting its amplitude: for any nonzero f₀, solve a^(p−2)=p||Δf₀||₂²/(2||f₀||_p^p). Choose another smooth compactly supported g, disjoint from x₀, with E(g)=E₀<0. Then u_λ=f_λ+g has the same mass and energy E₀ for all sufficiently large λ. For any ε<p/2, the same λ⁴ contradiction remains because ||f||_p^p=(p/2)||D²f||₂².

Allowing a single arbitrary center a(u) does not rescue a universal small-ε estimate either: use two identical concentrating zero-energy bumps around distinct fixed points, plus a disjoint negative-energy background. For every center, at least one bump remains a fixed distance from it. Uniform Lipschitz bounds on ω_R show the leading positive defect is cλ⁴+O(λ³), uniformly over the center. Thus a moving center needs a genuinely dynamical argument; it is not merely a missing minimization of a static inequality.

## 4. A nonradial replacement controlled by angular regularity

Here is a valid replacement. Use polar coordinates only to define the angular operator; no radial symmetry is imposed. Set

    K(u)=∫₀^∞ ||(1−Δ_{S^{N−1}})u(r,·)||²_{L²(S^{N−1})} r^(N−1)dr.

This is equivalent to the sum of the L² norms squared of u and all first and second rotation derivatives. In particular K≥m. It need not be finite for arbitrary H² data, and it is not a conserved quantity.

**Weighted angular interpolation lemma.** For N≥2, u∈H² with K(u)<∞, R>0, and ε>0,

    ∫ω_R|u|^p ≤ εD_R
      +C_(N,ε)R^(−4)[K m^(4/(N−1))
                        +K^((N−1)/N)m^(5/N)].   (A)

For radial u, K=m, recovering the mass powers m^(1+4/(N−1)) and m^(1+4/N). For nonradial u, the missing quantity is explicit rather than hidden in an invalid small-ε constant.

### 4.1 Fixed-cylinder anisotropic Gagliardo–Nirenberg estimate

On a fixed compact radial interval times S^(N−1), localize smoothly away from interval endpoints. Write

    μ=||v||₂²,
    Q=||∂_r²v||₂²+μ,
    A=||v||²_{L²_r H²_θ}.

Then

    ||v||_p^p ≤ C_N Q^(1/N)A^((N−1)/N)μ^(4/N). (G)

A direct proof uses finitely many smooth sphere charts. In each chart use Fourier variables ξ∈R in the radial direction and η∈R^(N−1) in the angular directions. Fourier Hausdorff–Young and weighted Hölder with

    w=1+(ξ/a)⁴+|η/b|⁴

show

    ||v||_p ≤ C (∫w|v̂|²)^(1/2)
                    (∫w^(−p/(p−2)))^(1/2−1/p).

The last integral is finite because p/(p−2)=(N+4)/4>N/4. Set a=(Q/μ)^(1/4), b=(A/μ)^(1/4), taking equivalent norms with Q,A≥μ. Then ∫w|v̂|²≤Cμ and ∫w^(−p/(p−2))=C a b^(N−1). Raising to p yields exactly (G). The compact chart cutoffs only change uniform constants. Summing finitely many charts uses Hölder and the fact that each local μ is at most the global μ.

### 4.2 Dyadic rescaling and summation

Let ρ_j=2^jR, j∈Z; use annuli ρ_j≤r≤2ρ_j and fixed enlargements with bounded overlap. On such an enlargement,

    ω_R ≍ d_j=min{1,(ρ_j/R)⁴},
    α_j=d_j ρ_j^(−4)≤R^(−4).

Let μ_j, A_j, D_j denote mass, angular H² mass, and weighted Hessian energy on the enlarged annulus. After radial cutoff and rescaling v_j(s,θ)=ρ_j^(N/2)χ(s)u(ρ_js,θ),

    Q_j≤C(α_j^(−1)D_j+μ_j).

The cutoff-gradient term is controlled by a local second-order interpolation inequality on a slightly larger annulus; all enlarged families retain bounded overlap.

Estimate (G) gives

    ∫_{annulus j}ω_R|u|^p
      ≤C α_j^(1−1/N)D_j^(1/N)A_j^((N−1)/N)μ_j^(4/N)
        +Cα_j A_j^((N−1)/N)μ_j^(5/N).

Young's inequality with exponents N and N/(N−1) bounds the first term by

    δD_j+C_(N,δ)α_j A_j μ_j^(4/(N−1)).

Use ΣD_j≤CD_R, Σμ_j≤Cm, ΣA_j≤CK. The first remainder sums to at most C R^(−4)K m^(4/(N−1)). For the second, Hölder gives

    Σ A_j^((N−1)/N) μ_j^(5/N)
       ≤ (ΣA_j)^((N−1)/N)(Σμ_j^5)^(1/N)
       ≤ C K^((N−1)/N)m^(5/N).

Choose δ to absorb the finite overlap and obtain (A).

## 5. Conditional finite-time theorem and sharper time-average alternative

Combining (A) with (V), choosing ε small once, gives

    M_R' ≤16E−c_ND_R
      +C_N R^(−4)[m+K m^(4/(N−1))
                      +K^((N−1)/N)m^(5/N)].    (C)

**Conditional theorem.** If E(u₀)<0 and a putative global forward H² solution has K(u(t)) measurable with

    limsup_{T→∞} (1/T)∫₀^T K(u(t))dt <∞,

then this is impossible. In particular, a solution with uniformly bounded angular H² mass must blow up in finite forward time. This condition is automatic for radial solutions because K=m.

**Proof.** Write E=−e. Since K≥m>0, concavity implies

    K^((N−1)/N)m^(5/N) ≤ K m^(4/N).

The assumed bound on Cesàro averages gives ∫₀^t K≤L t+C₀. Choose a fixed R sufficiently large that the time-integrated positive error in (C) is at most 8et+C₁. Set y=−M_R. Integration yields

    y(t)≥8et−C₂+c_N∫₀^tD_R(s)ds.              (I)

Consequently y eventually exceeds B₀+1, where B₀ is from (B'). For t≥t₀, combine (I) and (B') and increase t₀ so the affine part is at least B₀+1:

    y(t)−B₀ ≥1+b∫_{t₀}^t(y(s)−B₀)⁴ds,
    b=c_N R^(−4)m^(−3)>0.

Let z(t)=1+b∫_{t₀}^t(y(s)−B₀)⁴ds. Then y−B₀≥z≥1, so z'≥bz⁴. Integration gives z(t)^(−3)≤1−3b(t−t₀), impossible for all t. This contradicts global H² continuity, which keeps M_R finite on compact time intervals. The ordinary H² blowup alternative gives finite-time divergence of ||Δu||₂.

For backward time apply the same argument to conjugate(u(−t,x)), the correct time-reversal transform.

Equivalently, any global negative-energy solution with finite K(t) must have unbounded upper time average of K. This identifies a necessary nonradial mechanism for evading the radial argument. It does not prove that such a global solution exists, and does not rule it out.

### 5.1 Quantitative strengthening: necessary fifth-power angular integral growth

The same method yields more than exclusion of bounded time averages.

**Quantitative alternative.** If a negative-energy H² solution is global forward, there are constants c=c(N,u₀)>0 and T₀=T₀(N,u₀)>0 such that

    ∫₀^T K(u(t))dt ≥ c T⁵,    T≥T₀.             (Q)

The statement is substantive when K is locally integrable; if an integral is infinite the corresponding inequality holds in the extended sense. Thus a global branch must have time-averaged angular H² mass at least of order T⁴.

**Proof.** Inequality (C), K≥m, and concavity give constants c₀,C₀,A_m>0 such that

    M_R'≤−16e−c₀D_R+C₀R^(−4)(m+A_mK),
    |M_R(0)|≤C₁R m^(1/2)||∇u₀||₂.

Fix a prospective horizon T and use R=δT, held fixed throughout [0,T]. First choose δ>0 small enough that |M_R(0)|≤eT. Suppose, seeking a contradiction, ∫₀^TK≤κT⁵. Choose κ>0 sufficiently small that C₀δ^(−4)A_mκ≤e/2. For all large T the mass-only error C₀δ^(−4)mT^(−3) is also at most eT/2. Since K≥0, these upper bounds control accumulated error up to every s≤T. For T/2≤s≤T,

    y(s)=−M_R(s)≥6eT+c₀∫₀^sD_R(t)dt.

Increase the lower threshold on T so that subtracting B₀ from (B') still leaves at least 4eT. Dropping the nonnegative earlier-time integral and applying (B') yields

    y(s)−B₀≥4eT+b∫_{T/2}^s(y(t)−B₀)⁴dt,
    b=c₂δ^(−4)T^(−4)m^(−3).

The comparison function starting at 4eT blows up within

    [3b(4eT)³]^(−1)=C₂δ⁴m³e^(−3)T.

Further decrease δ, before choosing κ, so that this duration is strictly below T/2. This contradicts H² continuity on [0,T]. Therefore the assumed bound ∫₀^TK≤κT⁵ fails for every sufficiently large T, proving (Q). There is no time derivative of R: a different fixed multiplier is chosen for each prospective horizon.

## 6. An unconditional nonradial subclass: fixed-charge vortices in N=2

The preceding theorem immediately gives a concrete extension beyond radial complex-valued solutions.

**Vortex corollary.** Let N=2, k∈Z, and u₀∈H²(R²) satisfy

    u₀(r,θ)=exp(ikθ)v₀(r),    E(u₀)<0.

Then its maximal solution of i u_t=Δ²u−|u|⁴u blows up in finite time in both directions.

Indeed, rotations and constant phase shifts commute with the equation. Uniqueness therefore preserves the equivariance u(t,r,θ+α)=exp(ikα)u(t,r,θ). Equivalently, both Δ² and |u|⁴u preserve this one-angular-mode class. Since Δ_{S¹}=∂_θ²,

    K(u(t))=(1+k²)²m

at every time, so the conditional theorem applies without an extra dynamical assumption. Conjugation in time reversal replaces k by −k, which is allowed.

The class is nonempty at negative energy for every k. Take any nonzero smooth compactly supported radial amplitude v₀ supported in an annulus away from r=0, multiply exp(ikθ)v₀ by a sufficiently large real amplitude a, and use E(au)=a²||Δu||₂²/2−a⁶||u||₆⁶/6<0 for large a.

For k≠0 these are not radial complex-valued solutions, although their modulus is radial. Thus this corollary is a restricted nonradial theorem; it must not be presented as the unrestricted nonradial problem. A targeted search did not identify an earlier identical statement, but this does not establish novelty.

## 7. What remains genuinely open in this route

The general hypothesis u₀∈H² and E(u₀)<0 does not provide finite or bounded K. Rotational invariance conserves the expectations of angular momentum generators, not their squared norms or K. Hence conservation laws alone do not close (C).

An adaptive center a(t) changes the virial derivative by

    −2 Im∫conjugate(u)[a'(t)·D²φ_R(x−a(t))]∇u.

This term has no automatic sign. Moreover, the two-bump counterexample rules out unrestricted static absorption even after optimizing a single center. A successful extension must control either angular concentration dynamically, center-motion errors, or a multi-center/multi-scale defect that treats separated concentrating components.

## Primary sources checked

1. Thomas Boulenger and Enno Lenzmann, *Blowup for Biharmonic NLS*, arXiv:1503.01741; published Ann. Sci. Éc. Norm. Supér. 50 (2017), 503–544. https://arxiv.org/pdf/1503.01741 . Checked exact localized virial normalization and distinction between finite-time blowup and growup.
2. Leonard Dinh, *Finite-Time Blow-Up of Radial Negative-Energy Solutions for the Mass-Critical Biharmonic Nonlinear Schrödinger Equation*, Meta research page dated 2 October 2026, linked 20-page PDF. https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/ . Checked exponential weight, quartic defect closure, and Remark 1.4. The counterexample and angular interpolation derivation in these notes should not be confused with a result asserted in that paper.
