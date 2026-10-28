# Nonlinear orbital instability and unstable dimension of the negative-energy branch

Research proof, 7 October 2026. This note takes the exact base profile and full angular spectral certificate as its finite inputs. It supplies the remaining analytic deductions. All conclusions are for sufficiently small nonzero speed; the existing explicit existence interval does not by itself quantify this smaller instability interval.

## 1. The theorem

Let Q be the certified real radial solution of

    Δ²Q + Q − Q³ = 0  on R⁴,

and set L+ = Δ²+1−3Q² and L− = Δ²+1−Q². Assume the completed exact certificates establish

- n(L+) = 31, ker L+ = span{∂₁Q,...,∂₄Q};
- n(L−) = 5, ker L− = span{Q};
- all remaining preconditioned spectral values are separated from zero;
- I = <∂₁Q,L−⁻¹∂₁Q> < 0, with the inverse taken in the odd sector.

These are the conclusions of `round4_morse_certificate.md`, rather than new numerical assumptions about a traveling profile.

Let U_{ω,v} be the analytic branch constructed by the inversion-conjugation implicit-function theorem. For every sufficiently small nonzero vector v, at ω=1, the following hold.

1. The exact traveling wave exp(it) U_v(x−vt) is spectrally and nonlinearly orbitally unstable.
2. Its real unstable generalized eigenspace has dimension in {29,31}. In particular, it has at least twenty-nine unstable directions. The Hamiltonian-Krein index equals 31; this number is not automatically the unstable dimension.
3. Nonlinear orbital instability holds in H² even when perturbations are chosen smooth and with exactly the same mass and all four components of momentum as U_v. The perturbing initial data can all have negative energy.
4. No statement of finite-time blowup of those perturbations follows from this theorem. Orbital escape is the conclusion.

The orbit used here is O(U_v)={e^{iθ}U_v(·−y): θ∈R,y∈R⁴}. Explicitly, there is ε_v>0 and a sequence of smooth initial data u_{0,n} with ||u_{0,n}−U_v||_{H²}→0, M(u_{0,n})=M(U_v), P(u_{0,n})=P(U_v), E(u_{0,n})<0, and times t_n>0 before the solutions' maximal existence times such that

    inf_{θ,y} ||u_n(t_n)−e^{iθ}U_v(·−y)||_{H²} ≥ ε_v.

The initial data can converge in every fixed high Sobolev norm. The proof below uses H⁶.

## 2. Signs, smoothness, and the action Hessian

On the real Hilbert space underlying complex functions use <f,g>=Re∫f̄g. Define

    C₀(u)=M(u)/2,     C_j(u)=−P_j(u)/2  (j=1,...,4),
    S_{ω,v}=E+ω C₀+Σ v_j C_j,
    d(ω,v)=S_{ω,v}(U_{ω,v}).

Then C₀'(U)=U, C_j'(U)=i∂_jU, and S'(U)=Δ²U+ωU+i v·∇U−|U|²U. The co-moving, co-rotating evolution has Hamiltonian operator J=−i:

    w_t = A_v w + N_v(w),      A_v=J L_v,      L_v=S''_{1,v}(U_v),

where N_v(w) is quadratic plus cubic in w. At v=0, in real-imaginary coordinates,

    A₀ = [[0,L−],[-L+,0]].

The cubic profile map H²→H⁻² is real analytic. The verified inverse on real-even/imaginary-odd functions therefore gives a joint real-analytic map in (ω,v). Rotations preserve this full symmetry space; local uniqueness implies covariance under rotations, and conjugation changes v to −v. Consequently d(1,v) is an even, rotation-invariant analytic function.

The profile is H⁴ by elliptic regularity. Since H⁴(R⁴) is an algebra, repeated elliptic bootstrap gives U_{ω,v}∈H^s for every finite s. The branch is continuous in each such space, either by the elliptic equation and bootstrap or by the higher-regularity implicit-function theorem. No spatial analyticity is needed.

Critical scaling gives the exact relation

    d(ω,v)=ω d(1,v ω^(−3/4)).

Since P(U_v)=2Iv+O(|v|³), differentiation in v gives

    d(ω,v)=ω d₀−(I/2)ω^(−1/2)|v|²+O(|v|⁴),

with the analytic remainder differentiable to any fixed finite order near ω=1. Put a=−I/2>0. Along v=r e₁, at ω=1,

    d_{vv}=2a Id₄+O(r²),
    d_{ωv}=−a v+O(r³),
    d_{ωω}=(3a/4)r²+O(r⁴).

The velocity block is positive. Its Schur complement is

    d_{ωω}−d_{ωv}(d_{vv})⁻¹d_{vω}
       = (a/4)r²+O(r⁴)>0.

Thus d''(1,v) is positive definite with five positive eigenvalues for sufficiently small v≠0. At v=0 it is degenerate: no nondegenerate index formula is being applied there.

## 3. Persistence of the full Morse count and kernel

The traveling Hessian is the self-adjoint real-linear operator

    L_v h=(Δ²+1+i v·∇)h−2|U_v|²h−U_v² h̄.

Its form domain is X=H² and its L² operator domain is H⁴. The free scalar Fourier symbol is |ξ|⁴+1−v·ξ. Its minimum is

    c_v=1−3(|v|/4)^(4/3)>0

for small speed. The decaying profile potential is relatively compact; preconditioning by (Δ²+1)^(−1/2) produces a bounded self-adjoint form operator, depending continuously on v in operator norm. At v=0 its isolated zero eigenspace has dimension five and the negative index is 36. The spectral projection onto a small interval about zero therefore has dimension five for small v. The five independent vectors

    iU_v, ∂₁U_v,...,∂₄U_v

belong to the kernel by phase and translation invariance; their independence persists from v=0. They exhaust the small spectral projection. Hence

    n(L_v)=36,     ker L_v=span{iU_v,∂₁U_v,...,∂₄U_v}.

The remaining form spectrum stays away from zero. In particular the positive subspace has a uniform positive lower bound in the H² norm for each sufficiently small v. In fact the companion exact certificate proves the stronger quantitative statement throughout 0<|v|≤10⁻⁶: the preconditioned form perturbation is at most 492.7875|v|+468.75|v|²<0.000493, so the full Morse count and five-dimensional kernel persist with nonzero preconditioned spectral gap greater than 1/30. The action-Hessian positivity and the unstable-cluster continuation used below still use a possibly smaller, unquantified speed interval.

The essential spectrum of A_v lies on the imaginary axis outside the gap (−ic_v,ic_v); the index argument below also permits embedded purely imaginary eigenvalues and does not assume their absence.

## 4. The generalized zero eigenspace and the index 31

Write α=(ω,v), q_α=C_α'(U), e_α=Jq_α, and η_α=−∂_αU. Differentiation of the profile equation gives

    Lη_α=q_α,       Aη_α=e_α,       Ae_α=0.

The matrix of the quadratic form L on the span of the five η_α is

    D_{αβ}=<Lη_α,η_β>=−d''_{αβ}.

It is negative definite. The conserved charges commute: <q_α,Jq_β>=0. Therefore no nonzero linear combination of the η_α can have another preimage under A. Indeed, solving Aw=Σc_αη_α+Σb_αe_α requires J⁻¹ of the right-hand side to be orthogonal to ker L. Pairing with e_β gives −ΣD_{βα}c_α=0, hence c=0. Consequently

    generalized ker A = span{e_α,η_α: α=0,...,4},

with precisely five Jordan chains of length two. The negative index on its quotient by ker L is exactly five.

Apply Lin–Zeng, Theorem 2.3 and Corollary 2.2, in X=H². Their assumptions are checked as follows:

- L:X→X* is a bounded symmetric form with finite negative index, finite kernel, and coercive positive complement (Section 3).
- J:X*⊃D(J)→X is multiplication by −i, with D(J)=H² regarded as a dense subspace of H⁻²; it is anti-self-dual under the real L² dual pairing.
- Their additional domain condition (H3) can be arranged automatically because ker L is finite dimensional (their Remark 2.3). Here smooth kernel vectors also give it directly with a smooth complementary projection.

The index identity is

    k_r + 2 k_c + 2 k_i^{≤0} = 36−5=31.

Here k_r counts positive real eigenvalues with algebraic multiplicity, k_c counts first-quadrant eigenvalues, and k_i^{≤0} is the nonpositive energy index on the positive-imaginary generalized eigenspaces. This last definition is important when embedded eigenvalues are present. It must not be silently replaced by a negative index without proving nondegeneracy.

Since the right side is odd, k_r≥1. Thus there is a positive real eigenvalue. No unverified numerical eigenvalue of the non-self-adjoint operator has been used.

## 5. A sharper lower bound: twenty-nine unstable dimensions

First consider one degree-one (dipole) channel at v=0. Its Hessian has n(L)=2 and kernel spanned by e=(g,0), where g is the degree-one radial part of ∂₁Q. Let z=L−⁻¹g and η=(0,z). Then Aη=e and <Lη,η>=<g,z>=I<0, up to a harmless positive angular normalization. A further preimage would require L+a=−z, whose solvability condition is <g,z>=0; this is excluded. Thus its generalized-zero quotient has exactly one negative direction. The channel version of Lin–Zeng gives k_r+2k_c+2k_i^{≤0}=2−1=1. It follows that there is exactly one positive real eigenvalue, algebraically simple, per degree-one channel. The four degree-one harmonics therefore supply four unstable dimensions.

Next, at v=0 the full certificate gives, in each single angular channel of degrees ℓ=2 and ℓ=3,

    L−,ℓ>0,      n(L+,ℓ)=1,      ker L+,ℓ={0}.

The degree-two positivity of L− also follows directly from the old bound ||K_{3,q,2}||²_HS<4.80: the c=1 norm is <sqrt(4.80)/3, still well below one after transfer to Q. The degree-three positivity was already certified.

For λ>0 the eigenvalue equations λa=L−b and λb=−L+a reduce to the self-adjoint pencil

    [L+ + λ² L−⁻¹]a=0,       b=λ L−⁻¹a.

At λ=0 this pencil has exactly one negative direction. It increases strictly on every nonzero vector as λ² increases. It is positive for sufficiently large λ, because L+=L−−2Q² and

    L− + λ²L−⁻¹ ≥ 2λ Id,

by the spectral theorem. Thus for λ>||Q||∞² the pencil is strictly positive. Its isolated negative eigenvalue crosses zero exactly once. The crossing is simple, since the kernel can have dimension at most one and its derivative 2λ<a,L−⁻¹a> is strictly positive. This gives exactly one positive real Hamiltonian eigenvalue in each single channel. The domain and min-max argument use the common H² form domain; the essential form part remains positive.

On S³, degree-ℓ harmonics have dimension (ℓ+1)². Hence degrees 2 and 3 supply 9+16=25 positive real eigenvalues counted with multiplicity at v=0. Together with the four degree-one modes, this gives 29. Small nonzero v can split degeneracies and move eigenvalues off the real axis, but analytic Riesz projection continuity preserves at least 29 real unstable dimensions. To justify this continuation, view A_v:H⁶⊂H²→H²; its coefficients depend continuously on v, and A_v−A₀ is small in H⁶→H². Isolated finite spectral clusters strictly in the right half-plane therefore persist.

Combining this lower bound with Section 4 yields

    dim_R E^u = k_r+2k_c ∈ {29,31}.

The note does not determine which of these two values actually occurs.

## 6. From spectrum to nonlinear orbital instability in H²

This step cannot be replaced by the sentence “spectral instability implies nonlinear instability.” We give the argument and the function spaces.

Lin–Zeng Theorem 2.2 gives an invariant splitting X=E^u⊕E^c⊕E^s, finite-dimensional E^u,E^s, polynomial growth on E^c, and the corresponding estimates on graph domains. Let σ>0 be the largest real part of the unstable spectrum. For every 0<ε<σ there is C_ε such that

    ||e^{tA}||_{H²→H²} ≤ C_ε e^{(σ+ε)t},     t≥0.

Ellipticity gives D(A:H²→H²)=H⁶ with equivalent graph norm. Their graph-domain conclusion gives the same exponential rate on H⁶. Smooth coefficients imply all unstable eigenvectors and generalized eigenvectors are smooth.

Choose a real linear solution z(t) from an eigenvector whose eigenvalue has real part σ. If the eigenvalue is not real, take its real two-dimensional invariant plane. There are positive constants c,C such that

    ||z(t)||_{H⁶}≤Ce^{σt},
    dist_{H²}(z(t),ker L)≥ce^{σt}.

For a nonreal pair the second inequality follows because the rotating ellipse in that two-dimensional plane never reaches zero, and the plane is transverse to ker L. For a real eigenvalue the assertion is immediate.

Because H⁶(R⁴) is an algebra and U is smooth, the nonlinear remainder satisfies

    ||N(w)||_{H⁶}≤C||w||²_{H⁶}

in a fixed small ball. The standard semilinear Duhamel fixed point gives the local H⁶ flow, with continuation as long as that norm remains bounded. Starting at w(0)=δz(0), a bootstrap and the growth estimate yield

    ||w(t)−δz(t)||_{H⁶}≤C δ²e^{2σt},
    ||w(t)||_{H⁶}≤C δe^{σt},

while δe^{σt}≤η, with η>0 fixed sufficiently small. Indeed, in the Duhamel integral the kernel exponent σ+ε is strictly smaller than 2σ. This also ensures existence up to T_δ=σ⁻¹ log(η/δ).

The smooth phase-translation orbit has tangent space ker L at U. Its local Taylor expansion and local properness give

    dist_{H²}(U+w,O(U))
      ≥ dist_{H²}(w,ker L)−C||w||²_{H²}

for small w. Local properness follows because a localized nonzero profile cannot converge strongly to itself under translations tending to infinity, or under a nontrivial limiting phase outside its stabilizer. The orbit is a smooth embedded manifold locally, since its five tangent vectors are independent.

At T_δ the lower bound is cη−Cη². Fix η so this is at least cη/2. The initial perturbation tends to zero while the final orbital distance is bounded below independently of δ. Returning from the rotating/translating frame preserves the orbital distance, proving nonlinear H² orbital instability.

## 7. Instability on the exact mass-momentum surface

The preceding perturbations can be chosen to have exactly the same five conserved charges. For every generalized unstable eigenvector, and in particular z(0),

    <C_α'(U),z(0)>=0.

Indeed A* C_α'(U)=−LJ C_α'(U)=0, so the charge derivatives annihilate generalized eigenspaces at nonzero eigenvalues.

Choose a correction in the fixed generalized-zero space:

    w_δ(0)=δz(0)+Σ b_α(δ)η_α.

The derivative in b of the five equations C(U+w_δ(0))=C(U) is the invertible matrix

    <C_β'(U),η_α>=D_{βα}=−d''_{βα}.

The finite-dimensional implicit-function theorem gives b(δ)=O(δ²). Since Aη_α=e_α and Ae_α=0, this correction has linear evolution O(δ²(1+t)); it fits the same quadratic error bound used in Section 6. The orbital escape conclusion therefore remains valid on the exact charge surface.

Finally E is continuous on H² and E(U)<0. Thus all sufficiently small initial perturbations in this sequence also have negative energy. This does not require prescribing their energies exactly.

## 8. Source and scope

The analytic external input is Z. Lin and C. Zeng, *Instability, index theorem, and exponential trichotomy for linear Hamiltonian PDEs*, Memoirs of the AMS 275 (2022), no. 1347; arXiv:1703.04016v4 (28 June 2021). Specifically: assumptions (H1)–(H3), Remark 2.3, Theorem 2.2 (including graph domains), Theorem 2.3, and Corollary 2.2.

Primary source: https://arxiv.org/pdf/1703.04016
Publication DOI: https://doi.org/10.1090/memo/1347

The source was read in full for the cited theorem statements and assumptions. The application, Hessian signs, generalized-kernel computation, twenty-nine-mode bound, charge-preserving nonlinear argument, and profile regularity verification above are deductions made in this research session.

This theorem answers the local dynamical stability question for the constructed four-dimensional branch. It does not prove that every nearby datum blows up, prove an open set of globally bounded negative-energy solutions, settle the zero-momentum two-wave problem, or give an explicit instability growth rate. Those are separate mathematical statements.
