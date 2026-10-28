# Primary-source verification and the exact comparison class

Date: 2026-10-10. This is a source and dependency check, not a declaration of historical priority. The R17 statements are internal project statements; the sources below do not independently review them.

## 1. The one-dimensional external input is present with the stated scope

**Larry Read and Marvin R. Schulz**, *The sharp one-dimensional Lieb–Thirring inequality for the sum of eigenvalues*, arXiv:2609.10478v2, 14 September 2026.

Primary sources: <https://arxiv.org/abs/2609.10478>, <https://arxiv.org/html/2609.10478v2>, <https://arxiv.org/pdf/2609.10478>.

The abstract page still identifies v2 as the latest version. Theorem 1 states, for every real (V\in L^{3/2}(\mathbb R)),

$$
\operatorname{Tr}(-\partial_x^2-V)_-
\le \frac{4}{3\sqrt3\pi}\int V_+^{3/2}.
$$

Equation (1.1) is the equivalent kinetic inequality with constant $\pi^2/4$ for every finite real orthonormal family. Proposition 4 explicitly includes complex Hilbert-valued families; taking the Hilbert space to be $\mathbb C$ covers complex scalar orbitals. Theorem 2 gives $L_{1,d}\le(2/\sqrt3)L_{1,d}^{\rm cl}$. No journal publication or acceptance is recorded on the abstract page.

The proof uses a cumulative mass matrix, a polynomial identity, completion of squares and a divided-difference inequality for a tangent function. I checked the scalar proof's factors, index relabelling, boundary terms and trigonometric sign. No error was found in these checked steps. This is not a complete independent validation of every argument in the preprint.

## 2. The fractional-occupation consequence used in R17

The following deduction is ours from the preceding input, rather than an additional assertion quoted from it. If $0\le n_j\le1$ and $\phi_j$ are complex orthonormal functions, let independent Bernoulli variables $X_j$ have means $n_j$. Pointwise convexity gives

$$
\Big(\sum_j n_j|\phi_j|^2\Big)^3
\le \mathbb E\Big(\sum_jX_j|\phi_j|^2\Big)^3.
$$

Apply the unweighted finite-family inequality to each selected subfamily and average. Thus

$$
\int\Big(\sum_jn_j|\phi_j|^2\Big)^3
\le\frac4{\pi^2}\sum_jn_j\|\phi_j'\|_2^2.
$$

Truncation and monotone convergence cover countable families with finite kinetic trace. Consequently the sharp scalar threshold formula for all one-dimensional occupation spectra is an application of the Read–Schulz input. It must not be counted as our resolution of the one-dimensional Lieb–Thirring conjecture. The quantitative control of the secondary kinetic energy and subsequent fixed-Gram dynamics require further arguments, as supplied in R17.

## 3. A directly relevant predecessor missing from the R17 short comparison

**Younghun Hong, Soonsik Kwon and Haewon Yoon**, *Global existence versus finite time blowup dichotomy for the system of nonlinear Schrödinger equations*, arXiv:1712.06811; journal version J. Math. Pures Appl. 125 (2019), 283–320.

Primary sources: <https://arxiv.org/abs/1712.06811>, <https://arxiv.org/pdf/1712.06811>.

Their equation (1.1) is exactly the common-density cubic system, in **three spatial dimensions**. Equations (1.2)–(1.7) record orthogonality, occupation spectrum, energy, and the density-matrix evolution $i\partial_t\gamma=[-\Delta-\rho_\gamma,\gamma]$. They prove a global-existence/blowup dichotomy through an orthonormal kinetic optimizer. Their extremizer theorem excludes the mass-critical endpoint: Theorem 1.2 requires $q>(d+2)/d$.

This is a close conceptual predecessor: using conserved occupations and orthonormal kinetic energy in focusing dynamics is established work. The R17 comparison should focus on its **critical endpoint**, sharp one-state plateau and one-core-plus-transverse-background conclusions, not on inventing the density-matrix framework or the occupation-dynamics connection.

## 4. A recent minimal-mass classification has a different coupling

**Xing Cheng, Zuyu Ma and Jiqiang Zheng**, *Classification of the minimal-mass blowup solutions to the two dimensional focusing cubic nonlinear Schrödinger system*, arXiv:2504.01674v2, 30 April 2025.

Primary sources: <https://arxiv.org/abs/2504.01674>, <https://arxiv.org/pdf/2504.01674>.

The first page explicitly defines

$$
F_j(U)=2\rho U_j-|U_j|^2U_j,
$$

which differs from the unitary-invariant common-density equation $F_j=\rho U_j$. The paper classifies minimum-total-mass nonscattering solutions for its finite system as solitons or pseudoconformal transforms; it also treats an infinite resonant system. These statements cannot be silently transferred to a fixed-Gram threshold in the common-density system. Conversely, the R17 project must not claim to generalize this theorem merely from similarity of titles.

A third-party machine-written summary encountered during search replaced their nonlinearity by $\rho U_j$. The actual primary PDF resolves the discrepancy; only the PDF formula is used here.

## 5. Stability and homogeneous coercivity are distinct ingredients

**Eric A. Carlen, Rupert L. Frank and Elliott H. Lieb**, *Stability estimates for the lowest eigenvalue of a Schrödinger operator*, GAFA 24 (2014), 63–84.

Primary source: <https://arxiv.org/html/1301.5032v2>.

Theorem 2.2, with $d=2,\gamma=1$, supplies the quadratic $L^2$ distance remainder from an arbitrary potential to the one-state optimal-potential family. Theorem 5.1 supplies scalar GNS stability. These are inherited inputs, not project discoveries. They do not alone give the project's homogeneous estimate

$$
\langle v,(-\Delta-Q^2)v\rangle\ge\kappa\|\nabla v\|_2^2,
\qquad v\perp Q.
$$

The positive shift in $-\Delta+1-Q^2$ matters: ordinary nonnegativity of this shifted linearization is insufficient. The R17 min–max/Lieb–Thirring derivation correctly identifies homogeneous coercivity as a separate requirement before converting one-state stability into a weighted full negative-trace estimate. This search did not locate a prior source stating the same weighted sharp-right-side plateau; absence of a located source is not proof of novelty.

## 6. The dimension restriction has a genuine mathematical obstruction

**Rupert L. Frank, David Gontier and Mathieu Lewin**, *The nonlinear Schrödinger equation for orthonormal functions II: Application to Lieb–Thirring inequalities*, CMP 384 (2021), 1783–1828.

Primary source: <https://arxiv.org/pdf/2002.04964>.

Theorem 2 proves $L_{\gamma,d}^{(2)}>L_{\gamma,d}^{(1)}$ whenever $\gamma>\max(0,2-d/2)$. In particular, at $\gamma=1$ this applies in every $d\ge3$, but does **not** apply at the two-dimensional endpoint. Consequently a universal claim that the one-state constant governs all occupation spectra in every dimension is false. This does not contradict a small-secondary-occupation plateau. The two-dimensional equal-occupation endpoint remains beyond what the R17 project has proved.

## 7. What this comparison establishes

The checked external input supports the scope stated in R17; its strongest one-dimensional threshold extension is explicitly dependent on a September 2026 preprint. The common-density/occupation/density-matrix architecture has important predecessors, especially Hong–Kwon–Yoon. Neither that predecessor nor the differently coupled Cheng–Ma–Zheng theorem matches the complete set of R17 hypotheses and conclusions. Historical priority of the proposed endpoint remainder and fixed-Gram dynamics remains unestablished. No result here settles the original nonradial negative-energy BNLS question or the full two-dimensional sharp Lieb–Thirring problem.

