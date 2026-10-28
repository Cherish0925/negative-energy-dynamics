# pure critical BNLS: exact comparison for kinetic amplification

Checked 2026-10-08. This is a targeted primary-source comparison for the proposed theorem in [critical-dynamics.md](critical-dynamics.md); it is not a certification of priority or of that proof.

## Proposed project statement being compared

For the pure equation `i u_t = Delta^2 u - |u|^(8/N)u`, let

`A=||Delta u||_2^2`, `M_c=sharp mass`, `d=(M/M_c)^(4/N)-1`, `E=-e<0`.

The proposed result says that every forward-global uniformly H2-bounded solution with zero momentum and sufficiently small positive `d` obeys

`e <= C_N d^(5/3) sup_{t>=0} A(u(t))`.

For a real sharp optimizer and `u(0)=sqrt(alpha)Q`, one has exactly

`M=alpha M_c`, `d=alpha^(4/N)-1`, `e=d A(u(0))/2`, `P=0`.

Thus its proposed consequence is `sup_t A(u(t))/A(u(0)) >= c_N d^(-2/3)`, unless the solution is nonglobal or its kinetic norm is unbounded. This is stronger than the pointwise sharp-GN consequence `A(t)>=2e/d`, but does not itself rule out very large bounded global motion. Finite-time blowup is not a consequence of this inequality alone.

## Primary sources and exact match

### 1. Boulenger–Lenzmann, *Blowup for biharmonic NLS*

Full paper: https://arxiv.org/pdf/1503.01741 (v2, 2015); published Ann. Sci. ENS 50 (2017), DOI 10.24033/asens.2326.

Theorem 3 assumes radial H2 data, N>=2, critical power and negative energy. Pure dispersion gives finite-time blowup or global growup, including quantitative time-growth estimates. With positive second-order dispersion, it gives finite-time blowup. Section 1.5 explicitly identifies the nonradial error estimates as an open issue. These conclusions neither imply the proposed estimate on unrestricted nonradial bounded trajectories nor duplicate its mass-excess exponent. For radial negative-energy solutions the old theorem is stronger in another direction: it excludes bounded global motion entirely. Its approach does not assume linearized nondegeneracy.

Web retrieval: ``, ``; Theorem 3 starts at PDF p.4, future problems at p.8.

### 2. Bonheure–Casteras–Gou–Jeanjean, *Strong instability of ground states to a fourth order Schrödinger equation*

Full paper: https://arxiv.org/pdf/1703.07977; published IMRN 2019(17), 5299–5315.

Theorem 1.2 covers pure mass-critical dispersion, N>=2, and any **radial** ground state: instability by finite or infinite-time blowup. Remark 1.1 explains that the variational problem may be considered on the radial subspace, and ties the restriction to the blowup input. Theorem 1.1 gives stronger finite-time conclusions in other dispersion/exponent ranges. No L+ nondegeneracy is assumed. Consequently avoiding L+ nondegeneracy is not new by itself; the proposed result's distinct features are the trajectory-wide nearcritical quantitative bound and application without a radial-profile hypothesis.

Crucial logical distinction: instability proved using radial perturbations already implies instability in the full H2 perturbation class. Thus “instability against unrestricted perturbations of radial ground states” is not an additional result.

Retrieval: ``, ``; main statements PDF p.3.

### 3. Leonard Dinh with Muse Spark, *Finite-Time Blow-Up of Radial Negative-Energy Solutions for the Mass-Critical Biharmonic Nonlinear Schrödinger Equation*

Official primary landing page (2026-10-02):
https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/

Read the complete 20-page PDF from its “Download the Paper” link. Theorem 1.1 states finite-time blowup forward and backward for every radial negative-energy H2 solution, N>=2. Corollary 1.2 states radial-ground strong instability by finite-time blowup. The proof uses exponential localization and a radial weighted interpolation estimate. Remark 1.4 explicitly leaves the nonradial issue open and discusses a moving center or interaction virial. Thus the project theorem, if proved, treats a different and broader spatial class under additional small-excess/zero-momentum conditions, with a weaker dynamical conclusion. It should not be called an improvement of this radial finite-time result.

Retrieval: landing ``; full paper ``; Theorem/Corollary PDF pp.2–3, Remark 1.4 p.5.

### 4. Gou, *Blowup of cylindrically symmetric solutions for biharmonic NLS*

Full paper: https://arxiv.org/pdf/2205.08167 (current retrieved version v3, 2024-11-04).

Theorem 1.2 assumes N>=4 and `Sigma_N={u in H2: u(y,z)=u(|y|,z), z u in L2}`. In the pure critical case it claims finite-or-infinite-time blowup for negative energy. It does not state a theorem for arbitrary nonradial data or give the proposed mass-excess amplification law. Its final closure after (2.25)/(2.29) is delegated to the BL proof. However its multiplier is `phi_R(y,z)=psi_R(|y|)+z^2/2`, whose gradient is unbounded in z. The axial virial cannot be bounded by the H2 norm alone. This is a concrete issue with importing the bounded localized-virial closure, separately from whether a different argument could establish the theorem.

Retrieval: ``, ``, ``, ``, ``; multiplier PDF p.3, final closure p.9.

The project comparison should distinguish “the stated theorem is cylindrical” from “the written endpoint closure has an uncontrolled axial term.” Neither the new nearcritical estimate nor this textual gap alone disproves Gou's stated theorem.

### 5. Lenzmann–Sok, *A sharp rearrangement principle in Fourier space and symmetry results for PDEs with arbitrary order*

Full paper: https://arxiv.org/pdf/1805.06294 (v4); IMRN 2021(19), 15040–15081.

Theorem 2 proves every sharp GN optimizer radial up to translation and real up to a constant phase when its Lebesgue exponent p>2 is even. For pure critical BNLS, `p=2+8/N`, this covers N=1,2,4. In N=2,4 the older radial-ground instability already covers all sharp ground states after symmetries. N=1 lies outside the N>=2 blowup theorems above. N=3 has p=14/3 and is outside this Fourier-rearrangement theorem. Hence an all-real-ground result without any radiality assertion may genuinely enlarge the covered profile class, but one must not overlook the N=2,4 automatic-radiality overlap.

Retrieval: ``, ``; Theorem 2 PDF p.5.

### 6. Dinh, *Non-radial finite time blow-up for the fourth-order nonlinear Schrödinger equations*

Primary publisher: https://www.sciencedirect.com/science/article/abs/pii/S089396592200101X
DOI: 10.1016/j.aml.2022.108084.

The publisher's visible introduction and Theorem 1.2 concern `i u_t-mu Delta^2 u+Delta u=-|x|^-2 |u|^(4/N)u`, N>=3, mu>0. The spatially decaying coefficient is an essential source of nonradial control. This is not the pure homogeneous model in the present project, despite the broad title. The same caveat applies to Cho–Ozawa–Wang's earlier fourth-order blowup work: BL discusses its inhomogeneous setting explicitly in the remarks after Theorem 3.

Retrieval: ``, ``, ``. Full Dinh manuscript was not retrieved; only the exact publisher-visible equation and theorem are used here.

### 7. Chang–Hajaiej–Ma–Song, *Existence and instability of standing waves for the biharmonic nonlinear Schrödinger equation with combined nonlinearities*

Full paper: https://arxiv.org/html/2305.00327v1

Theorems 1.6–1.7 address normalized ground states for combined powers, and the text immediately after Theorem 1.7 explicitly restricts the instability argument to H2_rad because of the virial error terms. It does not remove radiality for the pure critical equation or supply the proposed nearthreshold exponent.

Retrieval: ``, ``, ``.

## Gou axial-virial issue: direct mathematical check

The cylindrical virial contains `2 Im int z conjugate(u) partial_z u`. Its Cauchy–Schwarz bound involves `||z u||_2 ||partial_z u||_2`. Membership in Sigma_N makes it finite at an individual time; it supplies no uniform-in-time bound from conservation of mass and an H2 bound.

Even adding zero momentum does not supply a functional H2 bound: choose real smooth compactly supported `f(y,z)` radial in y, with two far-separated packets

`u_L(y,z)=exp(i k z) f(y,z-L)+exp(-i k z) f(y,z+L)`.

For disjoint supports, its H2 norm and mass are independent of L, its total axial momentum is zero, and `Im int z conjugate(u_L) partial_z u_L = 2 k L ||f||_2^2` (take f even in z). Thus the axial virial is unbounded as L grows. This is a functional obstruction to the missing estimate, not a PDE counterexample to the stated theorem.

## Recommended precise contribution statement

Subject to complete proof verification, the strongest distinct statement supported by this comparison is:

> Near the sharp mass, a zero-momentum negative-energy trajectory of pure mass-critical BNLS cannot remain within a kinetic bound unless its energy deficit is smaller than that bound by a factor of order d^(5/3). Amplitude perturbations of real sharp optimizers therefore make an arbitrarily large kinetic excursion as d tends to zero, or have unbounded H2 evolution. Neither radial symmetry, finite variance, nor L+ nondegeneracy enters this conclusion.

Do not state that it solves the unrestricted negative-energy finite-time blowup question, proves a sharp amplification exponent, classifies growup, or establishes priority. No matching theorem with the exponents 5/3 and -2/3 was found in this targeted primary-source audit.
