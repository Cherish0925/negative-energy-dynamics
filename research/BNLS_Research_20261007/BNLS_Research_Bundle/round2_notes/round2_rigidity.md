# Round 2: intrinsic rigidity, transport, and the failed minimal-counterexample reduction

7 October 2026. The unrestricted nonradial negative-energy theorem is not proved here. This round identifies exactly what the earlier angular growth estimate measures, proves a transport identity for genuinely compact global dynamics, and checks why a standard concentration-compactness reduction does not automatically produce a usable negative-energy critical element.

We use

    i u_t=Δ²u−|u|^(8/N)u,     N≥2,
    m=||u||₂²,  E=(1/2)||Δu||₂²−[N/(2N+8)]||u||_(2+8/N)^(2+8/N),
    P=Im∫conjugate(u)∇u.

Mass, energy, and vector momentum P are conserved. The equation does not have Galilean boost symmetry.

## 1. The T⁵ angular-integral lower bound can be saturated by rigid translation

Let u(t,x)=exp(iωt)Q(x−vt), and suppose Q has the weighted regularity needed for the following polynomial expansion in L² (Schwartz regularity is sufficient). Set y=x−vt. In Cartesian coordinates,

    Δ_S=(|x|²δ_ij−x_ix_j)∂_ij−(N−1)x·∇.

Therefore, acting on Q(y),

    Δ_S^x Q = t² A_v Q+t B_v Q+Δ_S^y Q,
    A_v=|v|²Δ−(v·∇)²,
    B_v=2(v·y)Δ−2Σ_ij v_i y_j∂_ij−(N−1)v·∇.

Consequently

    K(t)=||(1−Δ_S^x)u(t)||₂²
        =t⁴||A_vQ||₂²+O(t³).

For every nonzero Q∈H² and v≠0 in N≥2, ||A_vQ||₂>0: its Fourier multiplier is −(|v|²|ξ|²−(v·ξ)²), whose zero set is the line parallel to v; a nonzero L² Fourier transform cannot be supported on that measure-zero set. Thus

    ∫₀^T K(t)dt=(1/5)||A_vQ||₂² T⁵+O(T⁴).

The growth is measured about a fixed spatial origin. It is therefore incorrect to interpret the earlier lower bound alone as an intrinsic angular-frequency cascade or increasing shape complexity. A rigidly moving smooth profile has exactly this growth. Centering the angular operator at vt instead leaves K constant.

This does not construct a negative-energy traveling wave. It shows that the angular lower bound is fully compatible with that possible escape mechanism.

## 2. A rigorous compact-orbit transport identity

**Proposition.** Suppose u is a global forward H² solution and there is a spatial center x(t) such that

    {u(t,·+x(t)):t≥0}

is precompact in H²(R^N). Then one can choose another center a(t), a bounded distance from x(t), which is Lipschitz with uniformly bounded derivative and preserves the precompactness property. For every such choice,

    lim_(T→∞) P·[a(T)−a(0)]/T = 8E.             (1)

In particular, there is no global negative-energy solution with H²-precompact orbit modulo translations and P=0. When P≠0, the stronger full-vector conclusion is

    lim_(T→∞)[a(T)−a(0)]/T=(8E/|P|²)P.         (1a)

Thus a compact global orbit with E<0 must have P≠0 and move asymptotically opposite its momentum.

The word compact here concerns the complete complex-valued profile in H². No radial assumption or angular derivative bound is used.

### 2.1 Constructing a bounded-speed center

Precompactness gives a uniform H² bound A_*≥sup_t||Δu(t)||₂ and uniform spatial tightness after translation. Fix a radius L such that at least 0.9m lies in B(x(t),L) for every t. Let χ be a smooth cutoff equal to one on a ball and zero outside a ball of twice the radius. The local mass identity is

    d/dt ∫χ|u|²
       =4 Im∫∇χ·∇conjugate(u)Δu
          +2 Im∫Δχ conjugate(u)Δu.

Thus, for a cutoff on scale L,

    |d/dt∫χ_L|u|²|
       ≤C L^(−1)m^(1/4)A_*^(3/2)
           +C L^(−2)m^(1/2)A_*.

For a sufficiently short fixed time δ, a ball of radius comparable to L around x(t) therefore still contains more than 0.8m at any time s with |s−t|≤δ. Since B(x(s),L) contains at least 0.9m, the two balls cannot be disjoint. Hence |x(s)−x(t)|≤C L whenever |s−t|≤δ. Piecewise linear interpolation of x(nδ) supplies a Lipschitz a(t), with bounded speed and bounded distance from x(t). Translating a precompact family by a bounded set of shifts preserves precompactness.

### 2.2 Moving localized virial

Choose a smooth truncated quadratic φ_R(y)=R²φ(y/R), with φ(y)=|y|²/2 for |y|≤1 and ∇φ compactly supported. Let

    V_R(t)=2 Im∫conjugate(u(t,x))∇φ_R(x−a(t))·∇u(t,x)dx.

The exact virial identity, including the center derivative, gives for almost every t

    V_R'(t)=16E−2a'(t)·P+Err_R(t).              (2)

Precompactness of the centered orbit in H² yields uniform tails of u, ∇u, D²u, and |u|^(2+8/N). The cutoff errors in the standard virial identity therefore vanish uniformly as R→∞. The extra center error is

    2 a'(t)·Im∫conjugate(u)[I−D²φ_R(x−a(t))]∇u,

which also vanishes uniformly because its support is outside the centered ball of radius R and a' is bounded. Thus

    sup_(t≥0)|Err_R(t)|→0 as R→∞.

For each fixed R, uniform H² control gives |V_R(t)|≤C R. Integrating (2), dividing by T, letting T→∞ and then R→∞ proves (1). The limiting scalar displacement is independent of the bounded change of center.

### 2.3 Localized angular momentum gives the full drift vector

For each skew-symmetric matrix A, use the localized rotation field b_R(y)=χ(|y|/R)Ay, where χ=1 near zero and vanishes outside a fixed larger ball. Define

    L_(R,A)(t)=Im∫conjugate(u)b_R(x−a(t))·∇u.

Because b_R is divergence-free, its nonlinear contribution vanishes. The principal commutator with Δ² vanishes inside the centered ball, since Ay generates rotations and Δ² is rotationally invariant. All remaining commutator terms are supported in the tail and are bounded by its H² energy, with lower-order terms gaining powers of R^(−1). The center derivative has bulk term a'·AP. Hence

    L_(R,A)'(t)=a'(t)·AP+err_(R,A)(t),
    sup_t|err_(R,A)(t)|→0 as R→∞.

Since L_(R,A)=O(R), integration and successive limits imply

    ([a(T)−a(0)]/T)·AP→0

for every skew-symmetric A. If P≠0, the vectors AP span the space perpendicular to P. Thus the component of the averaged velocity perpendicular to P tends to zero. Equation (1) determines its parallel component and proves (1a). This argument does not assume that the full unlocalized angular momentum is finite.

### 2.4 Traveling profiles are the exact boundary case

For u(t,x)=exp(iωt)Q(x−vt), use a(t)=vt. The centered V_R is constant, so (2) gives in the limit

    16E(Q)−2v·P(Q)=0,
    E(Q)=v·P(Q)/8.                              (3)

This is exactly the mass-preserving Pohozaev identity for the traveling-wave elliptic equation

    Δ²Q+ωQ+i v·∇Q−|Q|^(8/N)Q=0.

It demonstrates why simply tracking a moving core does not close the original theorem: the center correction is of the same size as the negative-energy term, and it cancels that term exactly for a traveling wave. Any proof of the unrestricted theorem must, among other things, exclude profiles satisfying v·P<0. The positivity of this pairing is automatic for some variational ground-wave families but has not been proved here for arbitrary excited profiles.

## 3. Why momentum cannot be treated as center velocity

For sufficiently localized smooth solutions, the first moment X=∫x|u|² obeys

    X'=4J₃,     J₃=∫ξ|ξ|² |û(ξ)|²dξ.

By contrast, P=∫ξ|û(ξ)|²dξ. Therefore P=0 does not imply X'=0. Likewise P·J₃ need not be nonnegative for a general Fourier mass distribution. For example, in one direction take a smooth distribution concentrated with weight 0.99 near +1 and weight 0.01 near −10. Its mean frequency is positive while its cubic mean is negative. Smooth localized wave packets realize the same strict signs.

This example is not an elliptic solution, but it disproves any proof step that tries to obtain P·J₃≥0 from convexity of |ξ|⁴ alone. Convexity gives monotonicity of the covariance

    ∬(ξ−η)·[ξ|ξ|²−η|η|²]ρ(ξ)ρ(η)dξdη≥0,

which is a different statement.

## 4. Why the negative-energy minimal-counterexample argument is not automatic

One might define m_c as the infimum of masses of global negative-energy solutions and invoke a standard critical-element argument. There are two separate problems.

### 4.1 Negative energy vanishes under concentration normalization

Suppose ||Δu(t_n)||₂=A_n→∞. Choose the concentration length ℓ_n=A_n^(−1/2), and write

    v_n(y)=ℓ_n^(N/2)u(t_n,x_n+ℓ_n y).

Then

    ||Δv_n||₂=1,    E(v_n)=ℓ_n⁴E(u₀)→0 from below.

Thus even strong H² convergence of the normalized profiles only forces a limiting profile to have zero energy, not negative energy. A ground state is entirely compatible with this limit. The strict conserved negative number is lower order relative to the diverging kinetic and nonlinear energies.

This is not only a formal possibility. Let f be a smooth compactly supported nonzero profile with E(f)=0, obtained by amplitude adjustment, and let g be a disjoint smooth compactly supported profile with E(g)=−1. Then

    u_n(x)=λ_n^(N/2)f(λ_n(x−x₀))+g(x),   λ_n→∞,

has fixed mass and exactly E(u_n)=−1. Its leading concentrating profile has zero energy; the full negative energy sits in the lower-scale remainder g. This is a sequence of initial states, not a claimed trajectory. It is sufficient to refute the inference “total negative energy implies the leading normalized bubble has negative energy.”

A profile decomposition which only retains leading normalized energy cannot remove g and still claim to carry the hypothesis of the target theorem.

### 4.2 The usual scattering-threshold compactness argument has a different closure property

Standard minimal-nonscattering constructions exploit finite spacetime norms of all subthreshold profiles and long-time perturbation theory. Here a smaller-mass negative-energy profile would, by a hypothetical induction, blow up in finite time. That is not a finite-norm scattering profile through which one may run long-time perturbation theory.

Local perturbation theory transfers approximations on intervals strictly before its singular time. It does not by itself prove that adding distant or small radiation preserves that finite-time singularity. In particular, large but finite H² norms of approximating global solutions do not contradict their global existence. One would need an independent stability-of-blowup theorem for the relevant core, or a localized coercive blowup mechanism stable under the interaction errors.

Therefore neither the attainment of m_c by a global negative-energy critical element nor compactness of such an element has been justified merely by naming concentration compactness.

## 5. What a successful core argument still needs to prove

The preceding calculations identify two genuinely dynamical requirements for the full problem.

1. **Carry the negative energy across scales.** A decomposition must retain an actual negative-energy component or remainder at its own physical scale, even when arbitrarily energetic zero-energy spectators dominate the normalized profile. A leading-bubble argument alone cannot do this.
2. **Control translation in the correct frame.** Even a perfectly localized, fixed-shape core obeys the corrected virial balance 16E−2a'·P. Core tracking is useful only after controlling this term. The compact-orbit identity shows the exact surviving obstruction: negative-energy compact motion must exhibit average transport opposite momentum.

The zero-momentum compact-orbit rigidity proposition is a complete theorem proved above. It removes that specific dynamical branch. It does not exclude nonzero-momentum counterflow, nor unbounded-scale cascades, and therefore does not complete the user's general theorem.

## Sources and verification scope

The localized virial normalization is the one checked against Boulenger–Lenzmann, *Blowup for Biharmonic NLS*, arXiv:1503.01741, https://arxiv.org/pdf/1503.01741 . The results in Sections 1–4 here are derived directly from the equation and its symmetries; no novelty claim is made. The compact-center drift and localized-rotation arguments were independently checked by a collaborating agent. In particular, the transport identity is not a citation-based assertion that the general theorem has already been resolved.
