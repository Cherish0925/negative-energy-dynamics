# Round 13: primary-source techniques for critical focusing dynamics

Checked 2026-10-08. This targeted continuation supplements `round12_pure_bnls_instability_comparison.md`; it does not repeat its radial-BNLS comparisons or establish priority. Equations below use the project convention `i u_t = Delta^2 u - |u|^(8/N)u` unless otherwise stated. Public references have been read beyond abstracts at the exact statements identified here.

## 1. The most directly relevant antecedent: compact trajectories, center motion, and momentum

**Pausader–Shao**, *The mass-critical fourth-order Schrödinger equation in high dimensions*, J. Hyperbolic Differ. Equ. 7 (2010), 651–705. [Full text](https://arxiv.org/html/0906.1547v2), [PDF](https://arxiv.org/pdf/0906.1547).

Section 6 is directly pertinent. Proposition 6.1 assumes a global solution, fixed-scale precompact orbit in L2, and H^(2+1/(N+5)) regularity. It proves a time-averaged relation between translation, momentum and energy: `y(t)·Mom(u)=8E(u)t+o(t)` (their signs differ from ours). Proposition 6.2 combines localized first moment with that relation to connect the average quartic mass current and energy. Section 6.3 optimizes the energy of `exp(i X x_1)u` as a quartic polynomial. These are explicit existing antecedents of moving-center virial and modulation-sensitive interpolation.

Their scattering theorems concern N>=5: radial data below ground mass and unrestricted data below a smaller mass threshold. They do not exclude all nonradial negative-energy bounded trajectories. Their extra regularity is obtained by double Duhamel for the compact critical element; it is not an assumption that an arbitrary bounded trajectory automatically satisfies.

**Implication for this project (our analysis).** At zero momentum, a fully compact bounded-scale trajectory must have E=0, so negative-energy rigidity is already available after full compactness. The outstanding work is to promote the nearcritical concentration decomposition (one core plus small mass radiation) to a sufficiently strong dynamical separation or to control the remaining radiation current. Reproving the compact case is not a new breakthrough. For round 11 generalized transport, cite this source as the pure-quartic antecedent.

## 2. Very recent perpendicular-to-momentum virial, and its exact range

**Inui–Komada–Nishimura**, *Scattering of non-radial solutions for the fourth-order Schrödinger equation with Hdot^(1/2)-critical and supercritical nonlinearity*, arXiv:2610.05802v1, posted 2026-10-05. [Full text](https://arxiv.org/html/2610.05802v1).

Theorem 1.1 treats `i u_t + mu Delta u - Delta^2 u = -|u|^(p-1)u`, mu>=0, N>=2, `1+8/(N-1)<=p<1+8/(N-4)_+`. Data satisfy subground action and nonnegative full virial K. Conclusion: global H2 scattering both ways, with no radial assumption.

Lemma 2.2 supplies positivity of the transverse virial `K_perp`. Its proof scales only N-1 coordinates. The nonlinear term then scales with exponent `(N-1)(p-1)/2`, which must be at least four. Sections 3–4 construct the compact critical solution and exclude it using the transverse virial, whose center-motion term is perpendicular to the conserved momentum.

**Implication (our analysis).** At our critical power `p=1+8/N`, the transverse nonlinear exponent is `4(N-1)/N<4`. Thus their monotonicity proof does not pass to the endpoint. The paper gives an important recent comparison and a geometric tool, but does not answer our critical problem. At P=0 all directions are available; the remaining issue is not choosing the direction, but spatial tails of a noncompact orbit.

## 3. Known nonradial blowup/growup for dispersion order below two

**Van Duong Dinh**, *Blow-up criteria for fractional nonlinear Schrödinger equations*, arXiv:1808.07368; Nonlinear Analysis: Real World Applications (2019). [Full text](https://arxiv.org/html/1808.07368v1).

Proposition 1.5 covers `(-Delta)^s`, N>=1, 1/2<s<1, mass-critical nonlinearity `|u|^(4s/N)u`, negative energy, and no radial assumption. Every solution either blows up in finite time or has an unbounded kinetic norm along a sequence tending to infinity. Section 4, particularly Lemmas 4.5 and 4.7, derives localized mass and virial identities from the positive resolvent representation of `(-Delta)^s`. Section 5 combines exterior mass propagation with these identities.

**Implication (our analysis).** In symbol-degree notation this is 1<m<2, not quartic or general m>2. The resolvent representation with positive weight used there is specific to 0<s<1. An m>2 extension requires new commutator analysis; simply replacing the exponent in that formula is invalid. It also means that a proposed all-order theorem needs to explain which portion is already contained in Dinh's theorem.

## 4. Higher-order mass concentration is already established, but is conditional on singular evolution

**Chae–Hong–Lee**, *Mass concentration for the L2-critical nonlinear Schrödinger equations of higher orders*, DCDS 29 (2011), 909–928. [PDF](https://arxiv.org/pdf/0904.3021), [Publisher](https://www.aimsciences.org/article/doi/10.3934/dcds.2011.29.909).

This paper establishes mass concentration on the natural higher-order dispersive scale for finite-time singular evolution, using refined Strichartz estimates and wave-packet bilinear interaction. It does not establish negative-energy finite-time blowup, nor a near-ground quantitative amplification law. It is appropriate background for a theory that links kinetic growth to concentration, but should not be described as a precursor proving the required singularity mechanism.

## 5. Conserved occupations and fractional kinetic-energy estimates

**Hong–Kwon–Yoon**, *Global existence versus finite time blowup dichotomy for the system of nonlinear Schrödinger equations*, arXiv:1712.06811. [Full PDF](https://arxiv.org/pdf/1712.06811).

Theorem 2.3, PDF pp. 11–12, establishes an operator kinetic-energy inequality for arbitrary fractional differentiation order alpha>0. At density exponent `q=1+2alpha/N`, it yields the familiar occupation-operator-norm bound on the critical density integral. Proposition 7.3, pp. 31–32, proves conservation of every component pairing by the common self-adjoint nonlinear Hamiltonian; the proof does not require orthogonality at the differentiation step. The evolutionary theorem itself is for the three-dimensional cubic common-density system, not all fractional critical systems.

**Implication (our analysis).** Conservation of the Gram spectrum and the nonsharp fractional operator inequality must be credited. The distinct round-12 argument is how sharp scalar-ground polarization controls that conserved spectrum and forces exact rank one at scalar-threshold singularity. General critical flow well-posedness remains a separate analytical input.

## 6. Full covariance spectrum leads to a genuinely difficult variational problem

**Frank–Gontier–Lewin**, *The Nonlinear Schrödinger Equation for Orthonormal Functions II: Application to Lieb–Thirring Inequalities*, CMP 384 (2021), 1783–1828. [Full text](https://link.springer.com/article/10.1007/s00220-021-04039-5).

Section 1.2 and equation (36) give the density/kinetic dual inequality, with an optimal constant depending on allowed rank and an operator-norm factor at the mass-critical endpoint. Theorem 1 says the infinite-rank Lieb–Thirring optimum is not attained at finite rank in its stated exponent range; in spatial N>=3 it includes the kinetic endpoint corresponding to eigenvalue moment kappa=1. Theorem 2 proves strict improvement of the two-bound-state constant over the one-bound-state constant for kappa>max(0,2-N/2). Their proof studies binding of separated scalar optimizers. Appendix B contrasts trace/operator-norm interpolation with Schatten-norm interpolation.

**Implication (our analysis).** For standard dispersion in N>=3, replacing total mass by the largest occupation while retaining the scalar sharp constant is false in general: finite-rank binding gives a better constant than rank one. A sharp theory for fixed full occupation sequence must optimize over orthogonal spatial orbitals and account for binding versus spatial splitting. This is a real connection to a major variational problem, not an automatic corollary of Gram conservation. The paper concerns second-order dispersion; quartic analogues must be proved separately.

## 7. Direct mathematical obstruction: zero momentum does not suppress instantaneous mass current

This paragraph is our independent derivation, not a quoted theorem. It identifies what a successful improved moving-center argument must use.

In one dimension let Q be any nonzero real sufficiently regular localized standing ground, and let

`a=<Q''',Q'>/||Q'||_2^2`, `Y=Q'''-a Q'`.

Then `<Y,Q'>=0`, and Y is not zero: otherwise Q' would be a nonzero L2 solution of a constant-coefficient second-order ODE, which is impossible. For

`u_epsilon=b_epsilon Q+i epsilon Y`, `b_epsilon=1+K epsilon^2`,

direct integration by parts gives exactly

`P(u_epsilon)=Im integral conjugate(u_epsilon) u_epsilon'= -2 b_epsilon epsilon <Y,Q'> = 0`,

whereas the quartic mass-current moment is

`J(u_epsilon)=Im integral conjugate(u_epsilon') u_epsilon'' = 2 b_epsilon epsilon <Q''',Y> = 2 b_epsilon epsilon ||Y||_2^2`.

Since the standing-wave equation implies `E'(Q)=-omega Q`, Taylor expansion gives

`E(u_epsilon)=epsilon^2[-K omega M(Q)+(1/2)<E''(Q)iY,iY>]+o(epsilon^2)`.

Choose K fixed and large. Then E<0, the mass excess is positive of order epsilon^2, and J has size epsilon. Consequently a pointwise improvement `|J|<=C d` for nearcritical negative-energy zero-momentum data is impossible, while the existing `|J|<=C sqrt(d)` scale is consistent and saturated. This does not obstruct time-averaged cancellation, a corrected center, or a modulation equation that couples the current to radiation.

## 8. Status of negative-energy counterexamples and next mathematically substantial step

The present targeted searches did not locate a public primary-source construction of a global H2 nonradial negative-energy solution of pure mass-critical BNLS, or of a zero-momentum one. Search results referring to nonzero-background NLS, lower-order/mixed models, or inhomogeneous nonlinearities do not furnish such counterexamples. This is a bounded search finding, not proof that no construction exists. Project-specific earlier proposed counterexamples require their own full evidence and cannot be certified by this literature review.

For a stronger continuation of the actual critical problem, the most concrete missing statement is a long-time control of radiation-induced translation or of the moving-cutoff momentum flux. Instantaneous zero momentum is insufficient (Section 7). Full compactness would suffice by an existing theorem (Section 1). The research lies precisely between those two facts: establish dynamically that the small excess-mass radiation cannot keep supplying the nonzero mean moving-boundary correction needed to balance negative energy.

### Browser references for root verification

- Pausader–Shao exact Section 6: `turn403view0`, `turn404view0`; PDF `turn415view0`.
- Inui–Komada–Nishimura: `turn403view1` Theorem 1.1; `turn403view2` Lemma 2.2.
- Dinh: `turn416view2` Proposition 1.5; `turn416view3` commutator identities.
- Chae–Hong–Lee: `turn416view0`.
- Hong–Kwon–Yoon: `turn412view0` Theorem 2.3, `turn412view1` Proposition 7.3.
- Frank–Gontier–Lewin: `turn407view2`, `turn408view2`.

Root must reopen any page it intends to cite in a user-facing response.

## 9. Round-13 Gaussian lifting: verification and literature placement

The invariant-dynamics agent proposed an explicit occupation-dependent improvement. I independently checked its algebra. Let r=m/N>=1, let `Gamma=(<u_j,u_k>)`, let its eigenvalues be `lambda_1>=lambda_2>=...>=0`, and set `M=Tr Gamma`, `A=sum a_jj`, where `(a_jk)` is the kinetic Gram matrix in this eigenbasis. If scalar sharp GN reads

`||f||_(2r+2)^(2r+2) <= (1+r) Mc^(-r) M(f)^r A(f)`,

then circular complex Gaussian randomization `f_g=sum g_j u_j` gives, with independent mean-one exponential X_j,

`F(U) <= (1+r) Mc^(-r) B_r(Gamma) A(U)`,

`B_r(Gamma) = E[X_1 (sum lambda_j X_j)^r] / Gamma(r+2)`.

Phase averaging eliminates the off-diagonal kinetic entries. Swapping X_1 and X_j proves `E[X_1 S^r]>=E[X_j S^r]` when lambda_1>=lambda_j. Jensen's inequality yields

`B_r <= M^r[1-r chi/(r+1)]`, `chi=1-lambda_1/M`.

At r=2 the exact moment is

`B_2=(M^2+Tr(Gamma^2)+2M lambda_1+2lambda_1^2)/6`.

There is a stronger useful matrix form before replacing all kinetic weights by their maximum:

`F(U) <= (1+r) Mc^(-r) M^(r-1) [M A/(r+1) + r Tr(Gamma K)/(r+1)]`.

This supplies an explicit quantitative polarization estimate by elementary averaging and convexity. The r>=1 restriction in this Jensen proof must be retained.

### Real Gaussian version and a direct scalar phase estimate

For a real Hilbert-valued field, use real standard normal coefficients, hence X_j distributed as chi-square with one degree of freedom. The moment recurrence is `E X^(r+1)=(2r+1) E X^r`. Starting from **real** scalar sharp GN gives

`F(U) <= (1+r) Mc,real^(-r) M^(r-1) [M A/(2r+1) + 2r Tr(Gamma K)/(2r+1)]`.

Apply this to U=(Re u, Im u). Diagonalizing the real 2x2 mass matrix is a constant phase rotation (with an optional reflection). Put `chi=lambda_2/M<=1/2`, and `a=A(second component)/A`. If delta is the normalized scalar GN deficit, then

`delta >= [2r/(2r+1)] (chi+a-2chi a) >= [2r/(3(2r+1))](chi+a)`.

Therefore the same phase choice controls **both** squared mass and kinetic distance to a real function, with an explicit constant and without any spectral assertion about L_minus or L_plus. This also shows the complex scalar sharp constant equals the real one and forces its optimizers to have constant phase, in the range r>=1. For pure critical BNLS this covers N<=4. This derivation is a proposed streamlined foundation, not a claim about priority.

### Precise limitation and primary-source comparison

For K equal occupations lambda_j=M/K, the Gaussian moment is exactly

`B_r=M^r Gamma(K+r+1)/[K^(r+1) Gamma(K) Gamma(r+2)]`,

which tends to `M^r/Gamma(r+2)` as K grows. Thus the Gaussian bound allows total mass of order Mc even for large K. The operator-norm Lieb–Thirring bound allows total mass of order K under equal occupations. Gaussian lifting is particularly useful near scalar rank one and for explicit low-rank refinements; it is not the exact optimal full-spectrum threshold.

The targeted searches did not locate this precise B_r formula. Beyond the papers already listed, I read the main interpolation statements and proofs in:

- **Dolbeault–Felmer–Mayorga-Zambrano**, *Compactness properties for trace-class operators and applications to quantum mechanics*, Monatshefte Math. 155 (2008), 43–66. [Author PDF](https://www.ceremade.dauphine.fr/~dolbeaul/Preprints/Fichiers/DFM17.pdf). Theorems 3.2–3.3 derive trace-class interpolation from spectral inequalities and entropy duality, with a bounded-domain compactness theory. Their displayed inequalities are not the above Gaussian occupation-moment expression.
- **Dolbeault–Felmer–Loss–Paturel**, *Lieb–Thirring type inequalities and Gagliardo–Nirenberg inequalities for systems*, JFA 238 (2006), 193–220. [PDF](https://arxiv.org/pdf/math-ph/0506052). It studies generalized occupation-number inequalities and free energy via spectral traces, including a logarithmic Sobolev inequality for mixed states. This establishes that occupation-sensitive GN methods have a substantial prior history; a Gaussian lifting refinement should be located within that history.

No claim of first use of random projection, first occupation-sensitive inequality, or resolution of a Lieb–Thirring conjecture is justified by this search. The derivation does provide a substantially simpler verified route to the project's existing polarization inputs in r>=1.

Additional browser refs: `turn420view0`, `turn421view1`, `turn421view0`.

### A sharper dimension-independent consequence of the retained matrix bound

Let `G=Gamma/M`, `H=K/A`, both positive trace-one operators. The optimal squared common-direction distance is

`p(U)=inf_|zeta|=1 [M(U-zeta<zeta,U>)/M + A(U-zeta<zeta,U>)/A] =2-lambda_max(G+H)`.

One has `lambda_max(G+H)>=2 Tr(GH)`: Hilbert–Schmidt Cauchy–Schwarz guarantees that at least one of `Tr G^2` and `Tr H^2` is at least `Tr GH`; test the positive density matrix G or H against G+H. Therefore

`p(U)<=2[1-Tr(GH)]`.

Consequently the retained Gaussian inequalities above give explicit global quantitative polarization constants:

- complex internal space: `p(U)<=2(r+1) delta/r`;
- real internal space: `p(U)<=(2r+1) delta/r`.

These conclusions hold for r>=1 and require only the corresponding scalar sharp GN inequality and a common quadratic kinetic form. For infinite-dimensional internal space, approximate by finite-rank projections; the covariance and kinetic matrices are trace-class. This proof is stronger and shorter than the earlier 2x2 case split.
