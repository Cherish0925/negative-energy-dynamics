# Round 10: phase geometry, action Morse index, and momentum response

The definitive, complete proof is `round10_inertia_section.tex`. This note records the scientific scope and source comparison for integration, rather than duplicating the full proof.

## What has actually been proved

For every exact mass-critical homogeneous traveling profile with negative energy:

1. The real scalar frozen-amplitude operator `A_U=a(D)+ω−|U|^α` has variational negative index at least two.
2. The full real action Hessian has variational negative index at least three, with an explicit three-dimensional strictly negative subspace `span_R{U,conj(U),i conj(U)}`.
3. The index-three argument extends to any monotone focusing local nonlinearity whenever `v·P<0`, and to the positive-type Hartree setting with the exact corresponding Hessian form. Homogeneity/criticality only supply the link from negative energy to `v·P<0`.

This is an elementary exact compression of the Hessian, not a general instability theorem. In particular these need not be three discrete negative eigenvalues if the essential spectrum reaches the negative axis. No regularity beyond the energy-space forms is required for the local-power theorem.

For an explicitly supplied C1 velocity family:

4. If `B=∂_vP`, then `n_-(L)≥3+n_-(B restricted to P-perp)`.
5. For a family satisfying `P(v)=p(|v|)v/|v|`, negative energy implies `n_-(L)≥N+2`. This prevents a constrained local energy minimum at fixed mass and all momenta. The charge gradients are independent by a Fourier-hyperplane argument, so the needed constraint manifold is not an additional unresolved nondegeneracy problem.

For a C1 profile family with C2 action and critical scaling covariance:

6. The entire frequency-velocity charge Hessian is congruent to
   `−1/2 [[(m−1)v·P,P^T],[P,B]]`.
7. If B is invertible, its frequency Schur complement equals
   `[P^T B^{-1}P−(m−1)v·P]/(2m²ω²)`.
8. At a real standing profile, if the effective tensor `T_ij=<∂iQ,L_-^{-1}∂jQ>` has k negative eigenvalues, then the standing Hessian and its sufficiently nearby profile perturbations have at least `2k+1` negative directions. This refinement was independently suggested and checked by the dynamics agent.
9. Along a regular small-speed branch, `P=2Tv+o(v)`, energy is `(v^TTv)/m+o(v²)`, mass shift is `((m−2)/m)v^TTv+o(v²)`, and the Schur sign is controlled by `2(2−m)v^TTv+o(v²)`. The order m=2 is where the leading quadratic test degenerates. General 2-homogeneous dispersion is not necessarily Galilean.

Branch existence and real-block nondegeneracy are explicitly hypotheses where needed. The unconditional index-three theorem needs neither. The last Hamiltonian-index corollary in the TeX is explicitly conditional on all hypotheses of the index theorem; there is no unconditional stability claim.

## Relation to the main line

The action ground state has index one. A negative-energy traveling wave has index at least three. Therefore a Fredholm continuation from a ground state cannot reach negative energy while preserving only its symmetry kernel and the gap of all other spectral values. At least two additional negative directions must be gained, counting multiplicity, or the spectral gap/Fredholm framework must fail. This is a concrete continuation obstruction, complementary to the mass-gap obstruction.

The response formula gives a computable finite-speed criterion. In an isotropic branch, charge-Hessian degeneracy is exactly `c p'(c)/p(c)=1/(m−1)` when `p p'≠0`. A zero of this scalar expression is not automatically a stability exchange; one must still know the full action index and the Hamiltonian operator hypotheses.

## Sources checked

- Zhiwu Lin and Chongchun Zeng, *Instability, index theorem, and exponential trichotomy for Linear Hamiltonian PDEs*, arXiv:1703.04016, version 4 (2021), published Memoirs AMS 275 (2022), no. 1347. Primary page opened in this turn: https://arxiv.org/abs/1703.04016. This is the established Hamiltonian index framework, not a new result of this project.
- Ivan Naumkin and Pierre Raphaël, *On small travelling waves to the mass critical fractional NLS*, arXiv:1712.04484. Primary page opened: https://arxiv.org/abs/1712.04484. It establishes sub-ground-mass traveling waves in its fractional setting; the small-speed mass-shift sign obtained here must not be advertised as the first discovery of that phenomenon.
- Lars Bugiera, Enno Lenzmann, Armin Schikorra, Jérémy Sok, *On symmetry of traveling solitary waves for dispersion generalized NLS*, arXiv:1908.06771, Nonlinearity, DOI 10.1088/1361-6544/ab74b2. Primary page opened: https://arxiv.org/abs/1908.06771. General-dispersion traveling waves and their symmetry have a substantial prior theory.

The search was not an exhaustive priority review. No assertion of first publication is justified from this check. The exact finite-dimensional formulas and proofs above are independently derived and internally checked; standard charge-Hessian and Hamiltonian-index methods must remain credited as standard methods.

## Independent checks

The root and dynamics agents separately checked the three-negative-plane proof and the velocity-tangent orthogonality. The dynamics agent is also checking the final bordered-matrix formulas. All conclusions use real variational index consistently and distinguish it from unstable spectral dimension.
