# Literature check: the two-dimensional endpoint and separated wells

Checked 12 October 2026. Scope: the scalar, nonmagnetic Schrödinger operator on the full plane, eigenvalue exponent $\gamma=1$. Here $L_{1,2}^{(N)}$ controls the first $N$ negative eigenvalues, allowing fewer than $N$ negative levels. The scalar candidate is $L_{1,2}^{(1)}=1/(2M_c)$.

## Primary papers and exact restrictions

1. Rupert L. Frank, David Gontier, Mathieu Lewin, *The nonlinear Schrödinger equation for orthonormal functions II. Application to Lieb--Thirring inequalities*, arXiv:2002.04964v3; published in Communications in Mathematical Physics 384 (2021), 1783–1828. https://arxiv.org/html/2002.04964v3 ; https://doi.org/10.1007/s00220-021-04039-5

   Theorem 2 gives $L_{\gamma,d}^{(2)}>L_{\gamma,d}^{(1)}$ for $\gamma>\max(0,2-d/2)$, strictly excluding $(d,\gamma)=(2,1)$. Proposition 11 requires the dual density exponent $p<2$. Section 4, Lemma 12 uses two distant copies of the one-state optimizer. It discards $E^2$, $EB$, and the squared eigenvalue splitting as smaller than the density interaction $A$, using $p<2$. At the endpoint $p=2$, this comparison fails. The exact Ritz diagonal in that proof retains $EB$, which must be analyzed rather than discarded.

2. Rupert L. Frank, David Gontier, Mathieu Lewin, *Optimizers for the finite-rank Lieb--Thirring inequality*, arXiv:2109.05984v2. https://arxiv.org/html/2109.05984v2 ; published-paper PDF: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-frank-gontier-lewin-FINAL.pdf

   Theorem 1 gives bubble decomposition; Corollary 2 gives existence of finite-rank optimizers and includes the present endpoint. An optimizer need not have exactly the allowed number of eigenvalues. Theorem 3 gives the self-consistent equation, analyticity, exponential decay and the occupied/unoccupied spectral gap. Theorem 4 and its binding Lemma 23 require $\gamma>\max(0,2-d/2)$; they cannot be applied at $(2,1)$. The authors explicitly leave open whether this restriction is optimal in dimensions two and three. Their sharp rank-two CLR statement, Corollary 14, concerns $\gamma=0,d\ge3$, not the problem here.

3. Antoine Levitt, *Best constants in Lieb--Thirring inequalities: a numerical investigation*, Journal of Spectral Theory 4 (2014), 153–175. https://ems.press/content/serial-article-files/33509 ; https://doi.org/10.4171/JST/65

   The two-dimensional numerical study already observed dissociation into separated bumps. The subsequent strict-binding result above shows why such numerical dissociation cannot certify a sharp constant. Our previous Hermite computations reproduce this established phenomenon.

4. Larry Read, Marvin R. Schulz, *The sharp one-dimensional Lieb--Thirring inequality for the sum of eigenvalues*, arXiv:2609.10478v2. https://arxiv.org/html/2609.10478v2

   This recent preprint states the sharp one-dimensional $\gamma=1$ inequality and the higher-dimensional upper bound $L_{1,d}\le(2/\sqrt3)L_{1,d}^{\rm cl}$ (Theorem 2). In two dimensions its upper bound is $1/(4\sqrt3\pi)$, larger than the Townes candidate. It does not state the two-dimensional sharp endpoint equality. This check records its theorem statements; it is not an independent validation of its proof.

## What was and was not located

Targeted searches for the two-dimensional rank-two endpoint, nonbinding, multiple Townes wells, and finite-rank sharp constants did not locate a theorem settling $L_{1,2}^{(2)}=L_{1,2}^{(1)}$, nor a full local nonbinding theorem for arbitrarily perturbed multi-Townes configurations. Search coverage cannot establish absence or novelty.

The retrieved recent one-dimensional claims do not automatically settle the two-dimensional problem. Dimension lifting gives an upper bound with a larger constant, and the endpoint in FGL must not be filled by continuity from a strict-inequality theorem above it.

## Actual endpoint calculation in the preliminary calculations

The proof in [fixed-potential.md](fixed-potential.md) uses the exact two-well Ritz trace and controls the full spectral relaxation. For fixed $V_R=Q_+^2+Q_-^2$, it gives

$$
\frac1{2M_c}\int V_R^2-S_2(-\Delta-V_R)
\sim\frac{8\pi a^4}{M_c^2}e^{-2R}>0,
\qquad Q(r)\sim ar^{-1/2}e^{-r}.
$$

The dominating correction is the orthogonalization term $EB$, whereas the direct density interaction is smaller by $R^{-1/2}$. Full eigenfunction relaxation for this fixed potential changes the sum by only $O(R^{-1}e^{-2R})$. This rules out this specified family as distant-well counterexamples. It does not rule out profile deformation, scale asymmetry, a compact collective optimizer, or an unbounded number of centers.

The missing estimate for a genuine neighborhood theorem is quantitative shape coercivity after removing each core's translation and scale directions, coupled to interaction errors smaller than the leading orthogonalization cost. No such estimate has been proved in the preliminary calculations. The present calculation is not being presented as a proof of the global sharp constant or as an established historical first.
