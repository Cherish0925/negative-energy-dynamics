# targeted literature comparison

Date: 2026-10-08. Scope: the slow-travel spectral bifurcation and the conserved internal spectrum of common-density systems. Read against [spectral-section.tex](../../manuscripts/critical-structures/spectral-section.tex) and [systems-section.tex](../../manuscripts/critical-structures/systems-section.tex). This is a primary-source comparison, not an assertion of exhaustive priority.

## Conclusions that affect the current proofs

1. No checked source supplies real-part nondegeneracy for the pure mass-critical biharmonic ground state in dimensions 1, 2, or 3. Thus the round-11 spectral theorem and its nonlinear continuation must retain that hypothesis. Nondegeneracy of the phase operator does not replace it.
2. The existence of common-density systems, conservation of all component inner products, the density-matrix commutator formulation, and occupation-dependent Lieb–Thirring bounds are established mathematical structures. They must be attributed, not presented as discoveries of this project.
3. The useful new statement to test is the **scalar-sharp quantitative improvement by the unpolarized mass fraction**, rather than the mere appearance of the largest occupation number. None of the checked papers states the proposed factor `1-c(1-mu/M)` with a constant uniform in internal dimension for arbitrary higher-order homogeneous dispersion and the project's positive Hartree class.
4. The existing 2025 complete minimal-mass classification for a coupled 2D system concerns a different nonlinearity, `F_j=2 rho u_j-|u_j|^2 u_j`. It cannot be substituted for the common-density `F_j=rho u_j` theory.

## A. Pure quartic ground nondegeneracy and moving waves

### A1. Boulenger–Lenzmann, *Blowup for biharmonic NLS*

Primary full text: https://arxiv.org/pdf/1503.01741

Checked: introduction paragraph on ground waves (PDF pp. 7–8), Appendix A (PDF p. 30). The equation is `Delta^2 Q+Q-|Q|^(2 sigma)Q=0`. The authors identify ground-state uniqueness and nondegeneracy of the associated linearization as open in their treatment. This is historical evidence of the obstacle, not proof that no later result exists. Our targeted newer-source check below found only additional hypotheses or mixed-dispersion regimes.

Retrieval: ``; find results ``, ``.

### A2. Bonheure–Casteras–Moreira dos Santos–Nascimento, *Orbitally stable standing waves of a mixed dispersion nonlinear Schrödinger equation*

Primary full text: https://arxiv.org/pdf/1710.09775

Checked exact results:

- Theorem 3.16 proves one-dimensional nondegeneracy for `U''''-beta U''+alpha U-|U|^(2 sigma)U=0` **when `beta >= 2 sqrt(alpha)`** (coefficient of the fourth derivative normalized to one).
- Theorem 1.3 gives uniqueness and nondegeneracy for a small positive fourth-order perturbation of a second-order equation with `0<sigma<2/N` and fixed positive second-order coefficient.

Neither includes the pure quartic equation `beta=0`, `alpha=1`, `sigma=4/N`. Extrapolation from the small-fourth-order regime to pure quartic would require additional continuation and exclusion of kernel crossings. The paper also provides decay and profile regularity useful for checking domains once nondegeneracy is assumed.

Retrieval: ``, ``, ``.

### A3. Iyer–Parker–Stefanov, *Existence and stability for traveling waves of fourth order semilinear wave and Schrödinger equations*

Primary full text: https://arxiv.org/html/2512.12390v1

Checked Section 6, Theorems 5–6. The Schrödinger application is a **one-dimensional cubic standing wave** with profile `phi''''+mu phi''+omega phi-phi^3=0`, `mu<2 sqrt(omega)`. Theorem 6 explicitly assumes `ker L_+=span(phi')`; the main beam equation has a separate wave-speed-dependent operator. This paper does not establish real-part nondegeneracy for the pure mass-critical quartic profile and does not give the present small-velocity complex-profile coefficient. It is directly relevant to the spectral-index background. Its numerical unstable-to-stable transition belongs to the beam problem and must not be cited as a theorem about our mass-critical traveling Schrödinger branch.

Retrieval: ``, especially ``.

### A4. Bonheure–Casteras–Gou–Jeanjean, *Strong instability of ground states to a fourth order Schrödinger equation*

Primary full text: https://arxiv.org/pdf/1703.07977

Checked Theorems 1.1–1.2. For pure quartic dispersion at mass criticality, Theorem 1.2 treats **radial standing ground waves in N>=2**, and proves instability through finite- or infinite-time norm growth. The finite-time result in Theorem 1.1 requires either positive second-order dispersion at or above mass criticality, or strictly mass-supercritical pure quartic dispersion (with additional stated exponent restrictions).

This makes the distinction concrete: merely proving an unstable standing quartic ground wave is not new. A quantified real spectral pair created by nonzero translation, and a nonlinear instability theorem preserving the relevant charges, are more specific conclusions not supplied there. The proof mechanism in that paper is variational/virial, so no general `L_+` nondegeneracy theorem follows from it.

Retrieval: ``, ``.

### A5. Naumkin–Raphaël, *On small traveling waves to the mass critical fractional NLS*

Primary full text: https://arxiv.org/pdf/1712.04484

Theorems 1.1–1.4 concern one spatial dimension and dispersion order `1<s<2`. They establish constrained traveling minimizers and their small-mass asymptotics, uniqueness and tails. The small parameter is the **mass tending to zero**, after a substantial frequency modulation, rather than speed tending to zero near the mass-critical standing ground wave. The paper does not provide the current `lambda^2=(m-2)v^T T v/D_Q+o(|v|^2)` calculation or its `m>2` case. It does show that moving-wave branches below quadratic order already have a rich variational theory.

Retrieval: ``, ``.

### A6. Bugiera–Lenzmann–Schikorra–Sok, *On symmetry of traveling solitary waves for dispersion generalized NLS*

Primary full text: https://arxiv.org/pdf/1908.06771

Theorem 1 supplies boosted ground-state existence and minimizing-sequence compactness for broad elliptic Fourier symbols whenever the shifted kinetic quadratic form is coercive. Theorems 2–3 give cylindrical/conjugation symmetry under their symbol and integer-power assumptions. These are direct predecessors for profile existence and symmetry. They do not prove uniqueness, the required `L_+` kernel description, or the small-speed unstable spectral asymptotic.

Retrieval: ``, ``.

### A7. Curran–Marangell, *Detecting eigenvalues in a fourth-order nonlinear Schrödinger equation with a non-regular Maslov box*

Primary author full text: https://www.maths.usyd.edu.au/u/marangel/publications/NLS424.pdf

The paper develops a Maslov-index count for standing waves of the one-dimensional cubic fourth-order equation, including multipulses. Its Hypothesis 1.1 explicitly assumes `ker L_-=span(phi)` and `ker L_+=span(phi_x)`. Theorem 1.2 also assumes two nonzero integral coefficients. It therefore provides another useful spectral method, but does not remove the pure quartic mass-critical nondegeneracy hypothesis. “Non-regular” in the title concerns crossings in the Maslov-index construction, not an unconditional treatment of an enlarged profile kernel.

Retrieval: ``, ``.

## B. Internal covariance, occupation numbers and criticality

### B1. Hong–Kwon–Yoon, *Global existence versus finite time blowup dichotomy for the system of nonlinear Schrödinger equations*

Primary full text: https://arxiv.org/pdf/1712.06811

The equation is the infinite common-density 3D cubic system `i phi_j,t+Delta phi_j+rho phi_j=0`. Section 1 gives the density-matrix commutator flow and its operator norm, trace and energy invariants. Proposition 7.3 proves preservation of every component inner product. Theorem 2.3 already extends the kinetic-density inequality to **all derivative orders alpha>0**, including the critical density exponent `q=1+2alpha/d`. Theorem 1.2 constructs extremizers only away from endpoint exponents. The dynamical Theorem 1.3 is stated for 3D cubic, hence mass-supercritical, and uses a kinetic extremizer; finite-time blowup additionally assumes finite variance.

Consequences: a higher-order occupation-norm bound and its standard coercive global corollary alone are not the project’s distinguishing claim. The scalar-sharp deficit depending on `1-mu/M`, and the resulting exact rank-one conclusion at minimal total mass, are not stated in this paper.

Retrieval: ``, ``, ``, ``.

### B2. Dolbeault–Felmer–Loss–Paturel, *Lieb–Thirring type inequalities and Gagliardo–Nirenberg inequalities for systems*

Primary full text: https://arxiv.org/pdf/math-ph/0506052

Theorem 15 writes the system inequality in terms of orthonormal spatial orbitals and arbitrary nonnegative occupation numbers: a kinetic term plus an occupation functional bounds a density functional. It is an explicit earlier bridge between scalar interpolation and inequalities for mixed states. The paper also discusses stability of mixed states. It does not state the proposed uniform `1-c(1-mu/M)` scalar-sharp deficit, or a mass-critical higher-order flow theorem based on that deficit.

Retrieval: ``, ``.

### B3. Gontier–Lewin–Nazar, *The nonlinear Schrödinger equation for orthonormal functions I. Existence of ground states*

Primary full text: https://arxiv.org/pdf/2002.04963

The paper minimizes second-order nonlinear energy subject to orthonormality. Ground states solve a common self-consistent potential equation with **different frequency multipliers**. The main existence/binding theorems treat the subcritical range, including all particle counts for a restricted exponent interval and an unbounded sequence of counts in the wider range. This is an important predecessor for genuinely multiprofile bound states. It is not contradicted by our near-threshold complete polarization theorem, which requires **one common frequency** and proximity to the unrestricted scalar critical mass.

Retrieval: ``, ``.

### B4. Frank–Gontier–Lewin, *The nonlinear Schrödinger equation for orthonormal functions II. Application to Lieb–Thirring inequalities*

Primary full text: https://arxiv.org/html/2002.04964v3

This develops the finite-rank optimal Lieb–Thirring problem, its dual density-matrix formulation, optimizer equations and ranks. Theorem 1 proves strict improvement of finite-rank spectral constants along an increasing sequence of ranks in its specified ranges. These constants constrain operator/Schatten norms rather than fixing the unrestricted trace-mass scalar GN constant. Thus their rank effects cannot be identified with our polarization deficit without a separate argument. In particular, scalar sharpness does not justify replacing a many-orbital Lieb–Thirring constant by its one-orbital value.

Retrieval: ``, ``.

### B5. Cheng–Ma–Zheng, *Classification of the minimal-mass blowup solutions to the two dimensional focusing cubic nonlinear Schrödinger system*

Primary full text: https://arxiv.org/pdf/2504.01674

Checked Eq. (1.1) and introduction: `F_j=2(sum_k|u_k|^2)u_j-|u_j|^2u_j`. This is not the common-density U(d)-invariant Manakov coupling. The finite-component threshold profiles have equal component magnitudes; the infinite-component sharp threshold is unattained. The paper classifies finite-component minimal-threshold nonscattering and proves scattering for infinite-component data at or sufficiently close to its threshold. Those conclusions are substantially stronger than global norm bounds within that model, but do not imply our higher-order/Hartree common-density assertions. The full internal Gram conservation is unavailable for their component-dependent potential.

Retrieval: ``.

### B6. Wu–Zeng–Zhang, *Gagliardo–Nirenberg–Sobolev inequalities and ground states of Fermions in relativistic Hartree–Fock model*

Primary full text: https://arxiv.org/html/2505.06613v1

Theorems 1.1–1.2 study finite-rank density matrices with kinetic operator `sqrt(-Delta)` in three dimensions and Hartree interaction `|x|^{-alpha}`, including Schatten occupation constraints and dual spectral inequalities. The rank-dependent constants, existence and concentration results are relevant to extension toward fermionic constraints. This is dispersion order one, not our `m>1` class; it does not contain the proposed uniform scalar-sharp polarization remainder. Its fermionic variational setting should not be conflated with unconstrained internal polarization.

Retrieval: ``, ``, ``.

## C. Mathematical inference for the round-12 work

For a common scalar selfadjoint spatial Hamiltonian, write the solution as a Hilbert–Schmidt map from internal space to spatial L2. The internal Gram operator and spatial density matrix have the same nonzero eigenvalues. The former is constant under evolution, and the latter evolves by unitary conjugation. Thus `mu=||C||op` is a genuine invariant, not a freely adjustable decomposition parameter.

If the project proves

`F(U) <= kappa (M/Mc)^(kappa-1) [1-c(1-mu/M)] A(U)`,

then at fixed `mu/M<1` the coercive region extends strictly above `Mc` and remains dimension-independent. At `M=Mc`, unbounded kinetic energy at any finite or infinite sequence of times would force `mu=M`, hence rank one of the **initial** covariance and exact scalar polarization for the whole lifespan. The novelty candidate is the quantitative link between scalar sharpness and the conserved internal spectrum. It neither computes the optimal fermionic Lieb–Thirring constant nor classifies scalar minimal-mass singularity dynamics.

These comparisons support a focused contribution statement. They do not establish publication priority; no wording such as “first ever” is warranted from this targeted search alone.
