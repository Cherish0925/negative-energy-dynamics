# the two-dimensional gamma = 1 Lieb–Thirring endpoint

Date: 2026-10-11. Literature check and deductions from established theorems; this note does not prove the endpoint conjecture.

## Normalization and the precise question

Let Q solve −ΔQ + Q − Q³ = 0 on R², and write Mc = ||Q||₂². For an orthonormal finite family, put ρ = Σ |u_j|² and K = Σ ||∇u_j||₂². The conjectural inequality is

    ∫ρ² ≤ (2/Mc) K.

Its dual statement is L_{1,2} = L^{(1)}_{1,2} = 1/(2Mc), where

    L^{(N)}_{1,2} = sup_{V≥0} [Σ_{j=1}^N |λ_j(−Δ−V)|] / ∫V².

The factor relating the two constants is L = C/4. Negative eigenvalues are counted with multiplicity; missing eigenvalues contribute zero. No radial symmetry or finite prescribed rank is part of the conjecture.

## Established structural input

Frank–Gontier–Lewin, *Optimizers for the finite-rank Lieb–Thirring inequality*, arXiv:2109.05984, version 2, May 2023:

https://arxiv.org/pdf/2109.05984

Theorem 1 (pp. 6–7) gives bubble compactness of every normalized rank-N maximizing sequence. Each bubble has rank N_k, Σ N_k = N, and L^{(N_k)} = L^{(N)}. Corollary 2 gives a finite-rank optimizer for every N. Theorem 3 (pp. 7–8) makes its potential real analytic and exponentially decaying, with finitely many negative eigenvalues. In our case its Euler equation is V = ρ/(2L^{(N)}), with the first N orbitals occupied if they exist. If additional negative eigenvalues exist, the occupied shell is separated from the next one. These results include d = 2, gamma = 1.

Theorem 4's unconditional compactness and strict rank improvement require gamma > max(0, 2−d/2), so do not cover our endpoint.

## A rigorous reduction of any strict counterexample

The following are direct deductions from those established results.

1. Since L^{(N)} increases to L, a strict failure L > 1/(2Mc) occurs already at a finite rank. Choose the smallest such rank N*. Then N* ≥ 2 and L^{(k)} = L^{(1)} for k < N*.

2. Normalize a maximizing sequence by ∫V_n² = 1. Theorem 1 cannot split it into two or more bubbles: each bubble would have rank less than N* but the same, strictly larger constant L^{(N*)}. Thus this sequence is compact modulo translations, and an optimizer V* exists.

3. Its total number M of negative eigenvalues satisfies M ≥ N*. Otherwise the optimizer itself would violate the inequality at the smaller rank M. It is not justified to assume M = N*: unoccupied negative eigenvalues are allowed, with λ_{N*} < λ_{N*+1} when M > N*.

4. Choose normalized eigenfunctions u_j, j ≤ N*, and set

       β = 1/(2L^{(N*)}) < Mc,      ψ_j = sqrt(β) u_j.

   Then the optimizer becomes a common-density stationary system:

       −Δψ_j − ρ_ψ ψ_j = −e_j ψ_j,
       ρ_ψ = Σ |ψ_k|² = V*,
       <ψ_i,ψ_j> = β δ_ij,         e_j > 0.

   In particular all occupied modes have the same subcritical mass β. Under ∫V*² = 1,

       Σ ||∇ψ_j||₂² = 1/2,      ∫ρ_ψ² = 1,
       E(Ψ) = (1/2)Σ||∇ψ_j||₂² − (1/4)∫ρ_ψ² = 0.

   The kinetic identity follows from Σe_j = L^{(N*)} and ∫V*Σ|u_j|² = 2L^{(N*)}. No assumption of radial symmetry has been obtained.

Thus a strict failure cannot hide exclusively in infinite rank, fractional occupations, or a diffuse maximizing sequence. It produces a compact self-consistent stationary configuration with equal modal masses below Mc. Excluding every such maximizing configuration, at arbitrary N*, would prove the sharp endpoint. Present results provide neither that exclusion nor a universal bound on N*.

Fractional occupations do not enlarge the necessary search. If 0 ≤ n_j ≤ 1, independent Bernoulli variables X_j with mean n_j give

    (Σ n_j|u_j|²)² ≤ E[(Σ X_j|u_j|²)²].

An inequality valid for every finite orthogonal projector therefore holds for every finite positive contraction by taking expectations. Monotone truncation gives the countable case. For a general density matrix, restore its operator norm by homogeneity.

The mass-critical pseudoconformal symmetry also turns the stationary solution above into an exact finite-time blow-up solution with the same Gram matrix. This is a standard symmetry consequence, not a new blow-up construction. It is precisely why the spectral inequality controls the allowed coherent structures and dynamics.

## What the known rank-binding proof does not settle

Frank–Gontier–Lewin, *The nonlinear Schrödinger equation for orthonormal functions II: Application to Lieb–Thirring inequalities*, arXiv:2002.04964:

https://arxiv.org/pdf/2002.04964

Their strict improvement over the one-state constant in dimension two requires gamma > 1. Hence that theorem cannot be substituted at gamma = 1. Conversely, the fact that the one-state problem is stable does not generally imply that the many-state optimum is one state: this nearby parameter range supplies a concrete obstruction to such an inference.

The endpoint issue can be located in the finite-rank paper's proof, Section 6, formula (78) and Lemma 24. Its interaction exponent is

    p = (gamma+d/2)/(gamma+d/2−1).

For two distant copies it obtains a positive leading gain A_R, but must dominate an orbital-overlap remainder e_R². The displayed estimates give exponential factors

    A_R ≳ polynomial(R) exp(−p sqrt(|λ_N|) R),
    e_R² ≲ polynomial(R) exp(−2 sqrt(|λ_N|) R).

The strict hypothesis gives p < 2; our endpoint is p = 2. The exponential advantage then disappears. The existing estimates do not show e_R² = o(A_R). It is incorrect to say that the leading positive coefficient vanishes, or to infer that endpoint binding is impossible. Likewise, showing nonbinding for a particular pair of Townes profiles would not exclude another compact optimizer.

## More recent sources and their scope

Duong–Le–Nam–Nguyen, *Finite-Rank Optimizers for the mass-supercritical Lieb–Thirring and Hardy–Lieb–Thirring Inequalities*, October 2025:

https://arxiv.org/pdf/2510.24148

Theorem 2.1 imposes 0 < s ≤ 1, s < d/2 and (d+2s)/d < q < d/(d−2s). It proves a finite-rank global optimizer and a rank bound in that range. Neither d = 2, s = 1 nor the critical q = 2 endpoint is included. Its rank control uses a strictly sublinear rank exponent; it does not provide the missing bound on N* here.

Carvalho Corso–Ried, *On a Variational Problem Related to the Cwikel–Lieb–Rozenblum and Lieb–Thirring Inequalities*, CMP, February 2025:

https://link.springer.com/article/10.1007/s00220-024-05216-y

This work optimizes an auxiliary variational method and identifies its best attainable bounds. Its optimality concerns that method, not the conjectural sharp Lieb–Thirring constant. An optimized cutoff or Fourier decomposition should therefore not be mistaken for resolution of the spectral optimization problem.

Read–Schulz, *The sharp one-dimensional Lieb–Thirring inequality for the sum of eigenvalues*, September 2026 preprint:

https://arxiv.org/html/2609.10478v2

Theorem 1 states the sharp d = 1, gamma = 1 result. Theorem 2 gives L_{1,d} ≤ (2/sqrt(3)) L^{cl}_{1,d}. In dimension two this yields 1/(4 sqrt(3) π), which is strictly above the proposed 1/(2Mc). Its stated result does not settle our two-dimensional endpoint. This note has not independently verified the full proof of this recent preprint.

## Remaining mathematical gap

The exact unresolved step is to rule out, or construct, a compact rank-N extremizer with L^{(N)} > 1/(2Mc), equivalently an extremizing equal-occupation stationary system as above with β < Mc. Scalar local stability controls potentials close to the one-state manifold; it does not place an arbitrary minimal-rank counterexample in that neighborhood. A finite set of checked ranks also leaves an unbounded-rank possibility.

None of the inspected recent sources supplies this step. This is a statement about the checked theorems, not a claim that a finite search proves the absence of every possible 2026 result.
