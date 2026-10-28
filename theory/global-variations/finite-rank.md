# Finite-rank counterexample reduction, spectral completeness, and finite rotations

Date: 2026-10-16. Scope: the full two-dimensional exponent-one Lieb–Thirring problem. The finite-rank existence and compactness statements below are consequences of established results, not new existence theorems. The finite-rotation calculation in Section 5 is an additional necessary test, not a proof of the sharp conjecture.

## 1. Constants and the exact finite-rank reduction

Let

$$
 C_N=\sup_{0<\operatorname{rank}P\le N}
 \frac{\int\rho_P^2}{\operatorname{Tr}(-\Delta P)},\qquad
 L_N=\sup_{0\ne V\ge0}
 \frac{S_N(V)}{\int V^2},
$$

where the supremum defining $C_N$ is over orthogonal projections with finite kinetic energy and $S_N$ is the sum of the first $N$ negative eigenvalue magnitudes, with zeros appended. Write $C_1=2/M_c$. Then

$$
 C_N=4L_N,\qquad L_N\nearrow L_{1,2}.
\tag{1}
$$

For completeness, for a projection with $F=\int\rho_P^2$ and $T=\operatorname{Tr}(-\Delta P)$, the trial potential $V=t\rho_P$ gives $S_N(V)\ge tF-T$. Optimizing $(tF-T)/(t^2F)$ gives $L_N\ge F/(4T)$. Conversely, a spectral projection onto at most $N$ negative levels gives

$$
 S_N(V)\le \|V\|_2\sqrt F-T
 \le \|V\|_2\sqrt F-F/C_N
 \le C_N\|V\|_2^2/4.
$$

Consequently, **if** $L_{1,2}>L_1$, there is a smallest finite integer

$$
 N_*:=\min\{N:L_N>L_1\}\ge2.
\tag{2}
$$

This follows from convergence in (1); it does not require an optimizer for the unrestricted constant. For this $N=N_*$,

$$
 C_N=(1+\delta)C_1,\quad \delta>0,
 \qquad C_k=C_1\quad(1\le k<N).
\tag{3}
$$

## 2. What the finite-rank optimizer theorem actually supplies

Frank–Gontier–Lewin (FGL), Theorem 1, Corollary 2, and Theorem 3 apply at $(d,\gamma)=(2,1)$. Their admissibility condition here is $\gamma>0$. The compactness and strict-doubling conclusion of their Theorem 4 instead requires $\gamma>1$, so it does **not** cover this endpoint.

At the minimal rank (2), these results yield a normalized optimizer $V$, a finite total number $M$ of negative eigenvalues, and a real orthonormal occupied basis $\phi_1,\ldots,\phi_N$, with

$$
 \begin{split}
 H&=-\Delta-V, & H\phi_i&=-e_i\phi_i,\\
 e_1&\ge\cdots\ge e_N>0, &
 V&=\frac{\rho}{2L_N}=\frac{2\rho}{C_N},
 \qquad \rho=\sum_{i=1}^N\phi_i^2.
 \end{split}
\tag{4}
$$

Here $M\ge N$. If $M<N$, the same potential would optimize a lower-rank constant greater than $L_1$, contradicting (2). FGL proves analyticity, exponential decay, finiteness of $M$, and the strict occupied boundary gap

$$
 \lambda_N(H)<\lambda_{N+1}(H)\le0.
\tag{5}
$$

Degeneracies inside the occupied cluster are allowed. Equation (5) means that an eigenvalue shell cannot be partly occupied; it does **not** mean that every negative eigenvalue is occupied. In particular, **$M=N$ is not a consequence of minimal violating rank.** If $M>N$, then the very same potential gives

$$
 L_{N+1}\ge L_N+\frac{e_{N+1}}{\int V^2}>L_N.
\tag{6}
$$

This is consistent with minimality of $N$, which constrains only smaller ranks. Thus “complete occupied shells” and “complete negative spectrum” must remain distinct.

The equal component masses of the NLS form are also exact. With

$$
 \beta=2/C_N=M_c/(1+\delta),\qquad u_i=\sqrt\beta\,\phi_i,
$$

one has $V=\sum_i u_i^2$, $\langle u_i,u_j\rangle=\beta\delta_{ij}$, and $(-\Delta-\sum_j u_j^2)u_i=-e_i u_i$. Summing (4) and using $F=C_NT$ gives $\sum_i e_i=T$.

## 3. Minimal-rank compactness and the precise meaning of binding

FGL's bubble decomposition assigns each nonzero bubble a rank $N_j$, with $\sum_jN_j=N$ and $L_{N_j}=L_N$. At the minimal violating rank, (3) makes $N_j<N$ impossible. There is therefore one bubble. **Every $L^2$-normalized maximizing sequence for $L_N$ is precompact in $L^2$, modulo translations.** Normalization fixes the spatial dilation freedom.

The strict inequality used here is

$$
 L_N>\max_{k<N}L_k=L_1.
\tag{7}
$$

It excludes spatial splitting of a maximizing sequence into smaller-rank clusters. It must not be replaced by an unproved inequality $L_{2N}>L_N$ at $\gamma=1$. Nor is there an additive binding identity $L_N>L_k+L_{N-k}$: for far-separated potentials the normalized spectral quotient is an integral-weighted average of the cluster quotients, not their sum.

The reduction leaves a compact, strongly interacting, equal-occupation candidate. The earlier restrictions $\delta\le1/(N+1)$, $e_N/e_1\ge\delta$, and the occupied-subspace overlap identities are already proved in R21/R23 and are not new results of this note.

## 4. Occupation saturation, including a direct quantitative proof

An alternative formulation permits a finite-rank positive density matrix $0\le\Gamma\le1$ with $\operatorname{rank}\Gamma\le N$. Let its largest eigenvalue be 1 and write

$$
 P_t=\mathbf1_{\Gamma>t},\qquad
 \Gamma=\int_0^1P_t\,dt.
$$

The exact identity

$$
 \begin{split}
 C_NT(\Gamma)-\|\rho_\Gamma\|_2^2
 &=\int_0^1\big(C_NT(P_t)-\|\rho_{P_t}\|_2^2\big)\,dt\\
 &\quad+\frac12\int_0^1\int_0^1
 \|\rho_{P_t}-\rho_{P_s}\|_2^2\,ds\,dt
 \end{split}
\tag{8}
$$

follows by expanding the squared norm. Each term is nonnegative. If $\Gamma$ has rank $N$ and smallest occupation $n_N<1$, minimality gives the sharper bound

$$
 C_NT(\Gamma)-\|\rho_\Gamma\|_2^2
 \ge (C_N-C_1)\int_{n_N}^1T(P_t)\,dt>0.
\tag{9}
$$

The integral is strictly positive because the top occupation is 1 and a nonzero finite-rank projection in $L^2(\mathbb R^2)$ has positive kinetic energy. A matrix of smaller rank cannot attain $C_N$ either. Thus equality at the first violating constant forces $\Gamma$ to be a rank-$N$ projection. This explains occupation saturation without confusing it with the spectral completeness excluded after (5). The density-matrix layer-cake method is standard; (8)–(9) are a direct proof in the present normalization, without a historical novelty claim.

## 5. An additional finite-rotation obstruction

R21 contains the complete infinitesimal Hessian. Here is an exact finite-amplitude consequence that is stronger than its single occupied-to-unoccupied test and supplies an explicit way to reject a candidate which passes that infinitesimal test.

Let $P$ be a real rank-$N$ optimizer, $C=C_N$, and take real unit vectors

$$
 \psi\in\operatorname{Ran}P,\qquad
 \chi\in H^1\cap(\operatorname{Ran}P)^\perp.
$$

The vector $\psi$ need not itself be an eigenfunction. Define

$$
 \begin{split}
 \Delta&=\langle\chi,H\chi\rangle-\langle\psi,H\psi\rangle,\\
 A&=\int\psi^2\chi^2,\qquad
 B=\int\psi\chi(\chi^2-\psi^2),\\
 D&=\int(\chi^2-\psi^2)^2.
 \end{split}
\tag{10}
$$

**Proposition.** Every such pair necessarily satisfies

$$
 C\Delta\ge
 \lambda_{\max}\begin{pmatrix}4A&2B\\2B&D\end{pmatrix}
 =\frac{4A+D+\sqrt{(4A-D)^2+16B^2}}2.
\tag{11}
$$

Equivalently,

$$
 C\Delta\ge4A,\qquad C\Delta\ge D,\qquad
 (C\Delta-4A)(C\Delta-D)\ge4B^2.
\tag{12}
$$

**Proof.** Replace $\psi$ in an occupied orthonormal basis by $\psi_\theta=\cos\theta\,\psi+\sin\theta\,\chi$. This preserves all Gram constraints exactly. For the resulting projection $P_\theta$, put

$$
 d_\theta=\rho_{P_\theta}-\rho_P
 =2\sin\theta\cos\theta\,\psi\chi
 +\sin^2\theta\,(\chi^2-\psi^2).
$$

Since $H$ preserves the occupied space, $\langle\chi,H\psi\rangle=0$. Using $2\rho=CV$, the exact deficit is

$$
 \begin{split}
 CT(P_\theta)-F(P_\theta)
 &= C\operatorname{Tr}H(P_\theta-P)-\|d_\theta\|_2^2\\
 &=\sin^2\theta\big[
 C\Delta-4A\cos^2\theta
 -4B\sin\theta\cos\theta-D\sin^2\theta\big].
 \end{split}
\tag{13}
$$

Global optimality makes (13) nonnegative for every $\theta$. Maximizing its bracketed quadratic expression in $(\cos\theta,\sin\theta)$ proves (11). A maximizing direction with $\sin\theta=0$ is approached by nearby nonzero angles, so no endpoint is lost. The matrix criterion (12) is equivalent to positive semidefiniteness of $C\Delta I-M$. $\square$

For actual occupied and unoccupied bound eigenfunctions, $\Delta=e_i-e_a>0$. Thus (11) is a quantitative energy-gap/coherence restriction on the *complete* Schrödinger spectrum, including any extra negative states. For general $\chi$, it also tests continuum wave packets. It does not assume radiality, simple occupied eigenvalues, or weak overlap.

The extra information beyond the existing single-column Hessian is explicit. Set

$$
 \eta=C\Delta-4A,\qquad \zeta=C\Delta-D.
$$

Even if the Hessian passes, $\eta\ge0$, the candidate is excluded whenever $\zeta<0$ or $4B^2>\eta\zeta$. The maximizing eigenvector of the displayed two-by-two matrix gives a concrete finite rotation with larger $F/T$. In particular, infinitesimal saturation $C\Delta=4A$ forces $B=0$ and $D\le4A$; a nonzero quartic coherence $B$ rules out such a saturated candidate. This is a genuine finite-amplitude restriction, but not a demonstration that every violating candidate contains such a pair. For reflection-symmetric pairs, $B$ can vanish, so the new term cannot be assumed positive.

## 6. Outcome and what remains open

The exact conditional reduction is: **failure of the full sharp inequality produces a smooth, exponentially localized, equal-occupation optimizer at a smallest finite rank, compact modulo translations and satisfying (4)–(5), the R21/R23 conditions, and (11).** Its occupied spectral shells are complete, but its full negative spectrum need not be exhausted.

The finite-rank existence/compactness portion is inherited from FGL plus minimality. The quantitative finite-rotation criterion adds a rejectable class of candidates, including cases with a nonnegative single-pair Hessian but excessive finite-amplitude coherence. No argument in this note proves that such excessive coherence must occur for every $C_N>C_1$; therefore this route has not closed the full conjecture or excluded all strongly overlapping optimizers.

## 7. Primary reference and attribution

R. L. Frank, D. Gontier, M. Lewin, *Optimizers for the finite-rank Lieb–Thirring inequality*, American Journal of Mathematics **147** (2025), 503–560; arXiv:2109.05984. The inspected author/publisher PDF is dated May 5, 2023.

- Publisher-hosted author text: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-frank-gontier-lewin-FINAL.pdf
- arXiv PDF: https://arxiv.org/pdf/2109.05984
- Exact locations in the inspected 52-page PDF: Theorem 1 and (11)–(12), printed p. 6; Corollary 2 and Theorem 3, printed pp. 7–8; Theorem 4 and condition (17), printed p. 8. Printed p. 5 explicitly allows an optimizer to have more or fewer negative eigenvalues than the rank cutoff.

The direct proofs of duality, minimal-rank compactness, occupation saturation, and finite rotations above specialize or supplement those established results. No historical priority is claimed for these elementary deductions. R21/R23/R24/R25 remain the sources for the earlier project-specific constraints and unresolved radial/deletion/variation routes.
