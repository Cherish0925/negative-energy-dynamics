# Source comparison and a shorter spectral derivation

Date: 2026-10-09. This note compares the R16 statements with primary literature cited below. It does not establish historical priority through absence of search results. It also gives a new derivation within this project of the weighted spectral statement; the inherited inputs are identified explicitly.

## 1. Exact statement being compared

In two dimensions, let Q solve −ΔQ+Q−Q³=0, let Mc=∫Q², and let L1=1/(2Mc). R16 claims that for some rank-independent ε>0,

    e1(V)+ε Σ_{j≥2} ej(V) ≤ L1 ∫V²,                 (1)

for V≥0 in L²(R²), where ej are the ordered absolute values of the negative eigenvalues of −Δ−V. Equivalently, occupations n1=1 and 0≤nj≤ε for j≥2 have the exact orthonormal kinetic constant 4L1=2/Mc, with no restriction on the sum of the secondary occupations.

The model for its dynamical application is

    i∂t uj+Δuj+(Σk |uk|²)uj=0.

This is a common-density, unitary-invariant vector equation. It preserves the entire matrix Γjk=∫uj conjugate(uk), not merely the individual component masses.

## 2. A direct derivation from a published stability theorem and the R16 homogeneous gap

Carlen–Frank–Lieb, *Stability estimates for the lowest eigenvalue of a Schrödinger operator*, GAFA 24 (2014), 63–84, arXiv:1301.5032, Theorem 2.2, specializes at d=2 and γ=1 to

    L1 ||V||²_2−e1(V) ≥ a inf_{W∈M} ||V−W||²_2,    (2)

with a>0 and M={b²Q²(b(·−y)): b>0,y∈R²}. The normalization in their theorem absorbs a factor L1 into a. Their Theorem 5.1 also supplies a published scalar GNS H¹ stability result. The real-valued formulation and complex phase extension should be distinguished when discussing the kinetic proof.

Source: https://arxiv.org/html/1301.5032v2 , Theorem 2.2 and Theorem 5.1. The article's Remark 5.2 explicitly identifies the noncomputability of its compactness-based constant. Thus scalar quadratic stability itself is inherited work, not an original R15/R16 theorem.

The genuinely additional input required for the following deduction is the project’s certified homogeneous estimate

    ⟨f,(−Δ−Q²)f⟩ ≥ κ ||∇f||²_2 for f⊥Q, κ>0.    (3)

R16 gives κ=47/175. Translation and critical dilation give the same κ for every W∈M, on the orthogonal complement of its normalized ground state qW. This is stronger than the usual positivity of −Δ+1−Q² on Q⊥; that familiar positivity is not a substitute for (3).

Fix W∈M. Let AV be the selfadjoint form compression of −Δ−V to qW⊥. Its form domain is H¹∩qW⊥. On that subspace,

    AV ≥ κ(−Δ)−(V−W)+.                             (4)

Codimension-one min–max interlacing gives λj+1(−Δ−V)≥λj(AV). Removing the codimension-one restriction on the right of (4) can only lower its min–max levels. Hence, for any finite N and then by monotone passage to the limit,

    Σ_{j≥2} ej(V)
      ≤ Tr(AV)−
      ≤ Tr[κ(−Δ)−(V−W)+]−
      ≤ (B/κ)||(V−W)+||²_2
      ≤ (B/κ)||V−W||²_2.                           (5)

Here B is any valid, not necessarily sharp, two-dimensional exponent-one Lieb–Thirring constant. It can be taken from the elementary Fourier-cutoff argument already contained in R16: the kinetic bound ∫ρ²≤(3/(2π))Tr(−Δγ), 0≤γ≤1, implies B=3/(8π) by optimizing ∫Vρ−Tr(−Δγ). Thus (5) requires no conjectural sharp constant and no recent preprint.

Take the infimum over W in (5), combine with (2), and obtain

    e1(V)+(aκ/B)Σ_{j≥2} ej(V) ≤ L1 ||V||²_2.        (6)

If desired replace aκ/B by its minimum with 1. For V=0 the statement is immediate. For nonzero V, all compressions and negative traces are well-defined by the standard L² potential form bounds; finite-dimensional min–max interlacing suffices before taking the trace limit. No attainment of the infimum in (2) is needed.

Conversely, weighted Ky Fan maximization applies to any density matrix whose largest occupation is 1 and whose remaining occupations are at most the coefficient in (6). It gives

    ∫Vργ−Tr(−Δγ) ≤ L1 ||V||²_2.

Optimize over V≥0 to obtain ∫ργ²≤4L1 Tr(−Δγ). This recovers the exact plateau, with a possibly different nonnumerical allowed occupation ratio. The direct R16 kinetic proof remains useful because it also gives the stronger global primary-deficit/secondary-kinetic remainder used in the dynamics; that remainder is not asserted to follow immediately from (6).

This proof shows precisely how the result is related to previous mathematics: global one-state stability plus homogeneous excited-space coercivity imply a trace-wide spectral remainder. Whether this combination was previously stated or used remains a priority question. Its short derivation neither proves previous publication nor establishes that the required homogeneous coercivity was already available in the same form.

## 3. Earlier occupation-number theory and the named Lieb–Thirring problem

Dolbeault–Felmer–Loss–Paturel, *Lieb–Thirring type inequalities and Gagliardo–Nirenberg inequalities for systems*, JFA 238 (2006), 193–220, already develop inequalities for orthonormal systems with arbitrary occupation numbers and spectral/kinetic duality. See Theorem 15 and its examples. The verified source does not state (1) with its sharp single-state right side and one separated largest occupation. Occupations, mixed states and the duality are established structures and should be attributed as such.

Source: https://arxiv.org/pdf/math-ph/0506052 ; DOI https://doi.org/10.1016/j.jfa.2005.11.008 .

Frank–Gontier–Lewin, *The nonlinear Schrödinger equation for orthonormal functions II: Application to Lieb–Thirring inequalities*, CMP 384 (2021), 1783–1828, prove nonoptimality of the one-state constant when γ>max(0,2−d/2). At d=2 this is strictly γ>1. Their Theorems 1–2 therefore do not contradict the d=2,γ=1 endpoint studied here. Their paper also explains finite-rank constants and the exact kinetic/spectral correspondence.

Source: https://arxiv.org/html/2002.04964v3 ; DOI https://doi.org/10.1007/s00220-021-04039-5 .

The concrete named target is the two-dimensional exponent-one sharp Lieb–Thirring problem:

    Σj ej(V) ?≤ (1/(2Mc))∫V².                       (7)

Already the rank-two specialization e1+e2≤(1/(2Mc))∫V² is a precise subproblem. R16 proves (1) with a small positive coefficient ε, not coefficient 1. It establishes no resolution of (7), of the rank-two specialization, or of the original nonradial biharmonic-NLS blowup problem. This review did not locate an earlier named conjecture whose text exactly asks for (1) or for the separated-occupation critical mass formula; do not invent such an attribution.

## 4. September 2026 update: the one-dimensional problem has a new claimed proof

Larry Read and Marvin R. Schulz, *The sharp one-dimensional Lieb–Thirring inequality for the sum of eigenvalues*, arXiv:2609.10478, submitted 9 September 2026, latest version v2 dated 14 September 2026, states in Theorem 1 the sharp scalar d=1,γ=1 constant 4/(3√3π). The v2 author line includes both authors; search/abstract metadata initially exposed the v1 single-author entry. Proposition 4 is the Hilbert-space-valued kinetic extension. Theorem 2 states L1,d≤(2/√3)L1,d^cl in all dimensions. The source located is a preprint; no journal acceptance or independent verification is inferred here.

Source: https://arxiv.org/abs/2609.10478 and https://arxiv.org/html/2609.10478v2 .

In d=2 the latter estimate is L1,2≤1/(4√3π), which is not the Townes value 1/(2Mc). Therefore it neither subsumes nor contradicts the R16 sharp-right-side small-weight estimate. It does mean that a new d=1,γ=1 partial-occupation extension must not be advertised as progress toward a still-untouched one-dimensional conjecture. Its comparison target is now at least the full theorem claimed in the Read–Schulz preprint.

## 5. Vector blowup and the exact equation match

Bourgain–Wang (1997), *Construction of blowup solutions for the nonlinear Schrödinger equation with critical nonlinearity*, provides the scalar pseudo-conformal-core plus flat regular-tail mechanism and the linearized-flow estimates used by the R16 construction. The vector extension is an adaptation of that mechanism, not discovery of a new collapse rate or a new blowup mechanism.

Source: https://numdam.org/item/ASNSP_1997_4_25_1-2_197_0/ and its linked PDF.

Su–Guo, *Blow-up solutions to nonlinear Schrödinger system at multiple points*, ZAMP 70,20 (2019), published online 19 December 2018, treats i∂tφj+Δφj+Σk ajk|φk|²φj=0 with symmetric coefficients and positive diagonal. The source abstract constructs concentration at K≥N prescribed points. All ajk=1 includes the present common-density equation. This is a direct predecessor for vector-system blowup. The accessible abstract does not state a single core with arbitrary regular transverse masses and an exact full Gram matrix, and the subscription-only full article was not inspected. Accordingly a blanket first-vector-blowup claim would be wrong, while priority of the exact-Gram construction is unresolved.

Source: https://link.springer.com/article/10.1007/s00033-018-1065-z .

Cheng–Ma–Zheng, *Classification of the minimal-mass blowup solutions to the two dimensional focusing cubic nonlinear Schrödinger system*, arXiv:2504.01674v2, has on its first page

    Fj(U)=2(Σk|uk|²)uj−|uj|²uj.

This differs from Fj(U)=ρuj. For two components its cross-phase coefficient is 2 whereas its self-phase coefficient is 1. Its unconstrained minimum-total-mass classification therefore cannot be cited as if it already proved the R16 fixed-Gram classification; conversely R16 does not extend that result merely because both titles say cubic NLS system.

Source: https://arxiv.org/pdf/2504.01674 , Eq. (1.1) and the following definition.

Banica (2004) proves critical-mass lower blowup-rate bounds for scalar cubic NLS on plane domains. The phase-variation and critical-mass rigidity lineage belongs here. A fixed-Gram rank-one core plus a nonzero transverse H¹ background is a different statement. The present review found no primary-source theorem exactly matching the full-time R16 decomposition; this observation is not a proof of novelty.

Source: https://numdam.org/item/ASNSP_2004_5_3_1_139_0.pdf .

## 6. Physical relevance and the accurate contribution statement

Bang–Edmundson–Królikowski (1999), *Collapse of Incoherent Light Beams in Inertial Bulk Kerr Media*, PRL83,5479, already studies collapse of partially coherent beams through coherent-density theory. Dependence of collapse on coherence is therefore an established physical question. R16 potentially supplies a precise conserved-occupation answer in a specified coefficient regime; it does not originate the question or establish a laboratory operating range while ε remains nonnumerical.

Source: https://doi.org/10.1103/PhysRevLett.83.5479 ; publisher abstract retrieved, full text not inspected in this review.

An accurate description is: a proposed sharp occupation-resolved threshold and accompanying threshold dynamics, resting on a verified Townes homogeneous estimate, classical one-state stability, orthonormal kinetic theory and a Bourgain–Wang extension. The strongest genuinely new-to-this-project object is the trace-independent exact plateau together with its global energy remainder and fixed-Gram dynamical consequences. Historical novelty of those combined statements has not been established by the present search.

The useful next comparison is with the exact same equation, conserved constraints, function space and constants. It is not scientifically valid to count each corollary as a separately resolved named historical conjecture without a primary statement of that conjecture.
