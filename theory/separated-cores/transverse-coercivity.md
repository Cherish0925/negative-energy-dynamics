# transverse coercivity at separated equal-scale Townes subspaces

This note proves a fixed-rank, equal-scale transverse coercivity statement and strict positivity of the deficit on a specified nonlinear modulation slice. Section 6 closes the normal-residual estimate and combines it with the interaction expansion proved in [multicore.md](multicore.md). No assertion is made here about every nearby subspace with independently varying scales, arbitrary rank, or arbitrary relative scale ratios.

## 1. Definitions and standard scalar input

Let the positive radial Townes state solve
$$
-\Delta Q+Q-Q^3=0\quad\text{on }\mathbb R^2.
$$
Write $M_c=\|Q\|_2^2$, $q=Q/\sqrt{M_c}$, and $C_1=2/M_c$. Thus $\|q\|_2=1$,
$$
-\Delta q+q-M_cq^3=0.
$$
Fix an integer $N$. For centers $a_1,\ldots,a_N$ with minimum separation
$R=\min_{j\ne k}|a_j-a_k|$, put
$$
q_j(x)=q(x-a_j),\qquad X=(q_1,\ldots,q_N),\qquad
S=X^*X,\qquad \Phi=XS^{-1/2}.
$$
For sufficiently large $R$, $S$ is positive definite, $\Phi^*\Phi=I$, and $P=\Phi\Phi^*$ is the projector on the raw-core span. All estimates below are uniform over center configurations with minimum separation at least $R$, at fixed $N$.

Define
$$
D(\Phi)=C_1\sum_i\|\nabla\phi_i\|_2^2
-\int\rho_\Phi^2,\qquad \rho_\Phi=\sum_i\phi_i^2.
$$
This depends only on the occupied subspace.

The scalar spectral facts used are
$$
L_-=-\Delta+1-Q^2\ge0,\quad\ker L_-=\operatorname{span}\{Q\},
$$
$$
L_+=-\Delta+1-3Q^2,\quad
\ker L_+=\operatorname{span}\{\partial_1Q,\partial_2Q\},\quad
L_+\Lambda Q=-2Q,
$$
where $\Lambda Q=Q+x\cdot\nabla Q$ and $\langle Q,\Lambda Q\rangle=0$. The sharp scalar Gagliardo–Nirenberg inequality implies nonnegativity of the $L_+$ quadratic form on $Q^\perp$. Its nullspace as a constrained quadratic form is
$\operatorname{span}\{\Lambda Q,\partial_1Q,\partial_2Q\}$.
Consequently there are $c_*>0,C_*<\infty$ such that
$$
\langle L_-f,f\rangle\ge c_*\|f\|_{H^1}^2-C_*|\langle f,q\rangle|^2,
\tag{1}
$$
$$
\langle L_+f,f\rangle\ge c_*\|f\|_{H^1}^2-C_*\left(
|\langle f,q\rangle|^2+|\langle f,\Lambda q\rangle|^2
+\sum_{\nu=1}^2|\langle f,\partial_\nu q\rangle|^2\right).
\tag{2}
$$
These are standard scalar ground-state spectral facts, not a new spectral assumption. To see why the constrained kernel has this form: a null vector on $Q^\perp$ satisfies $L_+f=\alpha Q$; the scaling identity and the kernel description then give the asserted span. Compactness of the decaying potential and the positive essential-spectrum threshold give a positive gap on its orthogonal complement. The finite-dimensional error terms in (1)–(2) follow by projection and absorption.

Background: M. I. Weinstein, *Nonlinear Schrödinger equations and sharp interpolation estimates*, Commun. Math. Phys. 87 (1983), 567–576; *Modulational Stability of Ground States of Nonlinear Schrödinger Equations*, SIAM J. Math. Anal. 16 (1985), 472–491, https://doi.org/10.1137/0516034. The scalar spectral facts here are distinct from stronger, model-dependent coercivity assertions used in log-log blow-up analysis.

## 2. Exact chart and Hessian away from a critical point

For a real horizontal perturbation $\eta=(\eta_1,\ldots,\eta_N)\in H^1(\mathbb R^2;\mathbb R)^N$ with $\Phi^*\eta=0$, use the exact orthonormal chart
$$
\Phi(\eta)=(\Phi+\eta)(I+\eta^*\eta)^{-1/2}.
\tag{3}
$$
Set
$$
K_{ij}=\langle\nabla\phi_i,\nabla\phi_j\rangle,
\quad V_{ij}=\int\rho_\Phi\phi_i\phi_j,
\quad A=C_1K-2V,
\quad s_\eta=\sum_i\phi_i\eta_i.
$$
Then
$$
D(\Phi(\eta))=D(\Phi)+\ell_\Phi(\eta)+\mathcal Q_\Phi(\eta)
+O_N(\|\eta\|_{H^1}^3),
\tag{4}
$$
uniformly for large $R$ and sufficiently small $\|\eta\|_{H^1}$, where
$$
\ell_\Phi(\eta)=2\sum_i\langle C_1(-\Delta)\phi_i-2\rho_\Phi\phi_i,\eta_i\rangle,
\tag{5}
$$
$$
\boxed{\mathcal Q_\Phi(\eta)=C_1\sum_i\|\nabla\eta_i\|_2^2
-2\int\rho_\Phi\sum_i\eta_i^2-4\int s_\eta^2
-\operatorname{Tr}[A\,\eta^*\eta].}
\tag{6}
$$
Thus the second derivative along $t\mapsto\Phi(t\eta)$ is $2\mathcal Q_\Phi(\eta)$. Formula (6) uses the full multiplier matrix $A$; replacing it by a diagonal eigenvalue matrix at this noncritical point would be unjustified.

Proof of expansion: $(I+\eta^*\eta)^{-1/2}=I-\eta^*\eta/2+O(\|\eta\|_{H^1}^4)$. Hence
$$
\rho_{\Phi(\eta)}=\rho_\Phi+2s_\eta+\sum_i\eta_i^2
-\sum_{ij}\phi_i(\eta^*\eta)_{ij}\phi_j+O_{L^2,N}(\|\eta\|_{H^1}^3).
$$
Expanding kinetic energy and the quartic term gives (4)–(6). Uniformity follows from bounded $\|\Phi\|_{H^1}$ at fixed rank, bounded $S^{-1/2}$, and $H^1(\mathbb R^2)\hookrightarrow L^4$.

## 3. Uniform transverse coercivity theorem

Let $E_\Phi$ be the real linear space of horizontal perturbations satisfying
$$
\Phi^*\eta=0,
\qquad \langle\eta_j,\Lambda q_j\rangle=0,
\qquad\langle\eta_j,\partial_\nu q_j\rangle=0
\quad(j=1,\ldots,N;\ \nu=1,2).
\tag{7}
$$
Here $\Lambda q_j=q_j+(x-a_j)\cdot\nabla q_j$. Since $S^{-1/2}$ is invertible, horizontality is exactly
$$
\langle q_j,\eta_i\rangle=0\quad\text{for every }i,j.
\tag{8}
$$

**Theorem.** For each fixed $N$, there exist $R_N,c_N>0$ such that every center configuration of minimum separation $R\ge R_N$ satisfies
$$
\boxed{\mathcal Q_\Phi(\eta)\ge c_N\sum_i\|\eta_i\|_{H^1}^2
\quad\text{for all }\eta\in E_\Phi.}
\tag{9}
$$

**Proof.** Exponential decay of $q$ and its first derivatives gives, uniformly over these configurations at fixed rank,
$$
S=I+o_R(1),\quad\Phi-X=o_R(1)\text{ in }H^1\cap L^\infty,
\quad \rho_\Phi-\sum_jq_j^2=o_R(1)\text{ in }L^\infty.
$$
Since a single core obeys $C_1(-\Delta)q-2q^3=-C_1q$, the same decoupling gives
$A=-C_1I+o_R(1)$. Therefore (6) differs, by at most $o_R(1)\|\eta\|_{H^1}^2$, from
$$
\mathcal Q_0(\eta)=C_1\sum_i\|\eta_i\|_{H^1}^2
-2\sum_{ij}\int q_j^2\eta_i^2-4\sum_j\int q_j^2\eta_j^2.
\tag{10}
$$
In obtaining (10), mixed terms $\int q_jq_k\eta_j\eta_k$ have been bounded by $o_R(1)\|\eta\|_2^2$.

Choose a smooth quadratic partition $\chi_0^2+\sum_j\chi_j^2=1$, where $\chi_j=1$ on $B(a_j,R/8)$, vanishes outside $B(a_j,R/4)$, and $\sum_j|\nabla\chi_j|^2+|\nabla\chi_0|^2\le C_N/R^2$. The core supports are disjoint. IMS decomposes the free part of (10) into the localized pieces with an error bounded by $C_N R^{-2}\|\eta\|_2^2$. All core potentials outside their corresponding localization balls are exponentially small.

On the ball around core $j$, the diagonal component $\chi_j\eta_j$ is governed by $C_1L_{+,j}$; each off-diagonal component $\chi_j\eta_i$, $i\ne j$, is governed by $C_1L_{-,j}$. The exterior has the strictly positive free form $C_1(-\Delta+1)$.

The localized orthogonality errors are exponentially small. For example,
$$
|\langle q_j,\chi_j\eta_i\rangle|
=|\langle(1-\chi_j)q_j,\eta_i\rangle|
\le C_Ne^{-cR}\|\eta_i\|_2,
$$
and the same estimate applies to $\Lambda q_j$ and $\partial_\nu q_j$ for the diagonal component, using (7). Apply (1)–(2), sum over the partition and components, then use IMS once more to compare localized $H^1$ norms with the full norm. This yields
$$
\mathcal Q_0(\eta)\ge c\|\eta\|_{H^1}^2
-C_N(R^{-2}+e^{-cR})\|\eta\|_{H^1}^2.
$$
Absorb these errors and the $o_R(1)$ error between (6) and (10) by increasing $R_N$. This proves (9). ∎

## 4. Why mass transfer and occupied degeneracy do not spoil this theorem

At infinite separation, a putative local amplitude-transfer direction is a linear combination of the $q_j$ in some component $\eta_i$. Every such coefficient is excluded by (8). Variations rotating the occupied basis are gauge directions; the horizontal chart removes them. Thus the mass-constrained $L_+$ negative direction does not survive in the allowed normal space.

Cross-component perturbations on core $j$ see $L_-$, not $L_+$. Its sole zero direction $q_j$ is again removed by (8). This is the relevant check when the occupied cores have degenerate energies.

Relative translations and dilations **do** become neutral at infinite separation. They are excluded explicitly in (7). Treating them as uniformly coercive would be an error. The theorem concerns the transverse directions after these parameters have been fixed.

## 5. Nonlinear estimate on the fixed modulation slice

Define the dual norm of the linear term restricted to the slice by
$$
g_\Phi=\sup\{\,|\ell_\Phi(\eta)|:\eta\in E_\Phi,
\ \|\eta\|_{H^1}=1\,\}.
$$
By (4), (9), and a uniform choice of $\varepsilon_N>0$, every $\eta\in E_\Phi$ with $\|\eta\|_{H^1}\le\varepsilon_N$ obeys
$$
D(\Phi(\eta))\ge D(\Phi)-g_\Phi\|\eta\|_{H^1}
+\frac{c_N}{2}\|\eta\|_{H^1}^2
\ge\boxed{D(\Phi)-\frac{g_\Phi^2}{2c_N}}.
\tag{11}
$$
The last step is completion of the square. This is a nonlinear estimate over an infinite-dimensional slice; it is not confined to a finite ansatz for shape changes.

The gradient may be written as the horizontal projection of
$2[C_1(-\Delta)-2\rho_\Phi]\Phi$; hence an $H^{-1}$ (or stronger $L^2$) normal-residual estimate controls $g_\Phi$. No stationarity of $\Phi$ has been assumed.

## 6. Quantitative residual and strict positivity on the slice

Let $R_{ij}=|a_i-a_j|$ and $R=\min_{i<j}R_{ij}$. We now prove that there are $a_N,b_N>0$, uniform over all equal-scale center configurations of sufficiently large minimum separation, such that
$$
D(\Phi)\ge a_N\sum_{j<k}e^{-2R_{jk}},\qquad
g_\Phi^2\le b_N\sum_{j<k}\frac{e^{-2R_{jk}}}{R_{jk}},
\quad R_{jk}=|a_j-a_k|.
\tag{12}
$$
This will make (11) give
$$
D(\Phi(\eta))\ge
\left(a_N-\frac{b_N}{2c_NR}\right)
\sum_{j<k}e^{-2R_{jk}}>0
\tag{13}
$$
for sufficiently large $R$, on the specified slice. Thus the gain from arbitrary sufficiently small shape relaxation in this slice is at most a relative $O_N(R^{-1})$ of the positive raw deficit.

### 6.1 The residual estimate, including near the endpoints

The global Townes tail bound is
$$
q(x)\le C\frac{e^{-|x|}}{\sqrt{1+|x|}}.
$$
For $r_i=|x-a_i|$, $r_j=|x-a_j|$, the triangle inequality and
$(1+r_i)(1+r_j)\ge1+r_i+r_j\ge1+R_{ij}$ give the uniform bound
$$
\|q_iq_j\|_\infty\le C\frac{e^{-R_{ij}}}{\sqrt{1+R_{ij}}}.
\tag{14}
$$
This estimate includes both endpoints of the segment between the centers; it does not use an interior-tube approximation. Since $\|q_j\|_2=1$, it immediately implies
$$
\|q_j^2q_i\|_2^2
\le\|q_iq_j\|_\infty^2\|q_j\|_2^2
\le C R_{ij}^{-1}e^{-2R_{ij}}\qquad(R_{ij}\ge1).
\tag{15}
$$

Put $s_0=\max_{i\ne j}|S_{ij}|$, where the diagonal of the Gram matrix $S=X^*X$ is one. The two-core overlap asymptotic implies
$s_0\le C R^{1/2}e^{-R}$. Since the off-diagonal Gram perturbation has zero diagonal, the diagonal entries of $S^{-1}-I$ are $O_N(s_0^2)$, and its off-diagonal entries are $O_N(s_0)$. Writing
$\rho_0=\sum_jq_j^2$ and using (14),
$$
\|\rho_\Phi-\rho_0\|_\infty
\le C_N\left(s_0^2+s_0R^{-1/2}e^{-R}\right)
\le C_NR e^{-2R}.
\tag{16}
$$

Write $H_\Phi=-\Delta-M_c\rho_\Phi$. For each raw core,
$$
(H_\Phi+1)q_i
=-M_c\sum_{j\ne i}q_j^2q_i
+M_c\left(\sum_jq_j^2-\rho_\Phi\right)q_i.
\tag{17}
$$
Because $\Phi=XS^{-1/2}$,
$(H_\Phi+1)\Phi=[(H_\Phi+1)X]S^{-1/2}$. Cauchy–Schwarz in the finite core sums, (15), (16), boundedness of $S^{-1/2}$, and $\|q_i\|_2=1$ imply
$$
\sum_i\|(H_\Phi+1)\phi_i\|_2^2
\le C_N\left[\sum_{i<j}R_{ij}^{-1}e^{-2R_{ij}}
+R^2e^{-4R}\right].
\tag{18}
$$
The sum in brackets is at least $R^{-1}e^{-2R}$, because a closest pair exists. Hence the second term is absorbed by the first for large $R$. For horizontal $\eta$, the added $+1$ term has zero pairing with $\eta$, and (5) becomes
$$
\ell_\Phi(\eta)=2C_1\sum_i\langle(H_\Phi+1)\phi_i,\eta_i\rangle.
$$
Since the $H^{-1}$ norm is bounded by the $L^2$ norm, (18) proves the residual half of (12). The apparently larger overlap coefficient multiplying a whole $q_j$ is harmless: it is treated using the exact equation before norms are taken. No unknown elliptic correction is hidden in this estimate.

### 6.2 Uniformity of the positive raw deficit at fixed rank

The matrix expansion proved in [multicore.md](multicore.md) is
$$
D(\Phi)=4\sum_{i<j}s(R_{ij})j(R_{ij})-2\sum_{i<j}b(R_{ij})
+O_N\left(s_0^3+s_0^2(j_0+b_0+t_0)+s_0t_0\right),
\tag{19}
$$
where $s,j,b$ are radial two-core overlap functions and $t_0$ bounds the three-core integrals. If $q(r)\sim A r^{-1/2}e^{-r}$, that calculation gives
$$
4s(d)j(d)=\kappa e^{-2d}(1+o(1)),\quad
\kappa=16\pi A^4/M_c>0,\qquad
b(d)=O(d^{-1/2}e^{-2d}).
$$
These are scalar limits as $d\to\infty$, so their errors are automatically uniform for all $d\ge R$ as $R\to\infty$. The bounds from the same expansion are
$$
s_0=O(R^{1/2}e^{-R}),\quad j_0=O(R^{-1/2}e^{-R}),\quad
b_0=O(R^{-1/2}e^{-2R}),\quad t_0=O(e^{-3R/2}).
$$
The last estimate follows from the triangle inequality retaining an integrable exponential factor, with constants independent of the center geometry at fixed $N$. Thus the entire remainder in (19) is $o_N(e^{-2R})$. Since
$\sum_{i<j}e^{-2R_{ij}}\ge e^{-2R}$, it follows that
$$
\boxed{D(\Phi)=\kappa\sum_{i<j}e^{-2R_{ij}}\,[1+o_N(1)]}
\tag{20}
$$
uniformly as the minimum separation tends to infinity, at fixed rank. In particular, the first bound in (12) holds, for example with $a_N=\kappa/2$, after increasing the separation threshold. This deduction strengthens the fixed-normalized-geometry statement in [multicore.md](multicore.md); it uses its already displayed remainder estimates rather than a new leading-order expansion.

### 6.3 Fixed-slice nonbinding conclusion

Combining Sections 3, 5, 6.1 and 6.2 proves: for every fixed $N\ge2$, there exist $R_N,\varepsilon_N,c'_N>0$ such that every equal-scale core configuration with minimum separation $R\ge R_N$ and every $\eta\in E_\Phi$ satisfying $\|\eta\|_{H^1}\le\varepsilon_N$ obey
$$
\boxed{D(\Phi(\eta))\ge c'_N\sum_{i<j}e^{-2R_{ij}}>0.}
\tag{21}
$$
The deformation $\eta$ is an arbitrary real $H^1$ function in the stated transverse slice, rather than a finite-dimensional profile ansatz. The scalar spectral input and the two-core overlap asymptotics are the only external analytic inputs to this conclusion; all orthonormalization, residual and nonlinear remainder terms have been included above.

## 7. Exact scope

1. The transverse theorem (9) and nonlinear slice estimate (11) hold at equal scale, fixed rank and sufficiently large minimum separation, using the stated standard scalar ground-state spectral facts.
2. Sections 6.1–6.2 establish the quantitative input (12), completing strict positivity (21) on the specified nonlinear slice. This is a local fixed-slice statement, not the full sharp Lieb–Thirring theorem.
3. A full neighborhood requires modulation of each center and scale. A nearby subspace generally lands on a slice based at **unequal** scales. Equal-scale positivity alone cannot cover those slices.
4. A sufficiently small relative scale perturbation preserves transverse coercivity by continuity. For unrestricted comparable scales, cross-sector operators become $-\Delta+\lambda_i^2-M_cq_{j,\lambda_j}^2$. Their gaps must be checked rather than assumed; equal-scale arguments are not uniform over arbitrary ratios.
5. Constants here may depend on $N$. Uniformity as $N\to\infty$, hierarchical core clusters, and states far from separated Townes cores are not addressed.

