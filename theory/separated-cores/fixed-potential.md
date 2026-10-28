# Two distant Townes wells: the full two-eigenvalue sum

Research derivation, 12 October 2026. This statement concerns a specified potential family, not all rank-two potentials. Historical originality has not been established.

## Statement

Let the positive radial Townes solution satisfy

$$
-\Delta Q+Q-Q^3=0\quad\text{on }\mathbb R^2,
\qquad m=\int Q^2,\qquad
a=\lim_{r\to\infty}r^{1/2}e^rQ(r)>0.
$$

Set $Q_\pm(x)=Q(x\pm Re_1/2)$, $V_R=Q_+^2+Q_-^2$, and $H_R=-\Delta-V_R$. If $S_2(H_R)=|\lambda_1(H_R)|+|\lambda_2(H_R)|$, then

$$
\boxed{\frac1{2m}\int V_R^2-S_2(H_R)
=\frac{8\pi a^4}{m^2}e^{-2R}(1+o(1))>0}
$$

for sufficiently large $R$. Thus these fixed two-well potentials approach the scalar one-bound-state constant $L_{1,2}^{(1)}=1/(2m)$ from below even when their eigenfunctions are fully relaxed, rather than restricted to the two translated ground states.

No assertion is made about all negative eigenvalues, optimization over deformed wells, unequal scales, or the global rank-two sharp constant.

## 1. Exact Ritz trace

Define

$$
E=\int Q_+Q_-,\qquad B=\int Q_+^3Q_-=
\int Q_+Q_-^3,\qquad A=\int Q_+^2Q_-^2.
$$

Pohozaev identities give $\int|\nabla Q|^2=m$ and $\int Q^4=2m$. The Gram matrix in the unnormalized two-function basis is

$$
G=\begin{pmatrix}m&E\\E&m\end{pmatrix}.
$$

Let $P_R$ project onto its span. Because
$(H_R+1)Q_\pm=-Q_\mp^2Q_\pm$, its Hamiltonian matrix has diagonal entries $-m-A$ and off-diagonal entries $-E-B$. Consequently

$$
S_{2,\mathrm{Ritz}}=-\operatorname{Tr}(P_RH_RP_R)
=2+\frac{2(mA-EB)}{m^2-E^2}.
$$

Also $\int V_R^2=4m+2A$, hence the exact deficit is

$$
\boxed{\frac1{2m}\int V_R^2-S_{2,\mathrm{Ritz}}
=\frac{2EB-mA-AE^2/m}{m^2-E^2}.}
$$

The positive contribution $EB$, resulting from orthogonalization, cannot be discarded at the endpoint. In the $\gamma>1$ argument of Frank--Gontier--Lewin it is lower order, which is precisely the distinction at issue here.

## 2. Overlap sizes

The necessary asymptotics are

$$
E\sim\sqrt{2\pi}\,a^2 R^{1/2}e^{-R},\qquad
B\sim2\sqrt{2\pi}\,a^2R^{-1/2}e^{-R},
$$
$$
A\sim\pi^{3/2}a^4R^{-1/2}e^{-2R}.
$$

In particular $EB\sim4\pi a^4e^{-2R}$ and $A=o(EB)$.

For an independent route to the first two constants, write $f=Q^3$, $Q=G_1*f$, with $G_1(x)=K_0(|x|)/(2\pi)$. Its convolution square is $G_1*G_1(x)=|x|K_1(|x|)/(4\pi)$. With $I=\int e^{x_1}f(x)\,dx$, the exponential decay of $f$ gives $a=I/\sqrt{8\pi}$; convolution against $f*f$ multiplies both kernel tails by $I^2$. This gives the displayed asymptotics for $B=f*G_1*f$ and $E=f*(G_1*G_1)*f$.

For $A$, use coordinates $x=(s,y)$ between centers at $0$ and $Re_1$. Away from endpoint neighborhoods, transverse Gaussian integration gives

$$
a^4e^{-2R}\sqrt{\frac\pi R}
\int_0^R\frac{ds}{\sqrt{s(R-s)}}
=\pi^{3/2}a^4R^{-1/2}e^{-2R}.
$$

The endpoints can be cut off first at $s=L$ and $R-L$; their contribution relative to the displayed scale tends to zero as $R\to\infty$, followed by $L\to\infty$. Bounds $Q(r)\le C(1+r)^{-1/2}e^{-r}$ provide domination. Only $A=O(R^{-1/2}e^{-2R})$, rather than its coefficient, is needed for the theorem.

The exact Ritz deficit therefore equals $8\pi a^4m^{-2}e^{-2R}(1+o(1))$.

## 3. A uniform gap outside the two-dimensional space

The scalar operator $h=-\Delta-Q^2$ has simple ground eigenvalue $-1$, with eigenfunction $q=Q/\sqrt m$. Since its essential spectrum starts at zero, there is $g_0>0$ such that

$$
h+1\ge g_0(I-|q\rangle\langle q|).
$$

Choose smooth IMS functions $\chi_+,\chi_-,\chi_0$ with $\sum\chi_j^2=1$, $|\nabla\chi_j|\le C/R$, the first two supported in radius-$R/3$ neighborhoods of their respective centers and equal to one in radius-$R/6$ neighborhoods. For $f\perp\operatorname{Ran}P_R$,

$$
|\langle\chi_\pm f,q_\pm\rangle|
=|\langle f,(\chi_\pm-1)q_\pm\rangle|
\le Ce^{-cR}\|f\|_2.
$$

The other well is exponentially small on each core cutoff. Both wells are exponentially small on the support of the exterior cutoff. Applying the scalar gap in the two core regions and IMS yields

$$
\langle f,(H_R+1)f\rangle
\ge\left(\min(g_0,1)-CR^{-2}-Ce^{-cR}\right)\|f\|_2^2.
$$

Thus, for some fixed $g>0$ and all large $R$,
$$
(1-P_R)H_R(1-P_R)\ge(-1+g)(1-P_R).
$$

This concerns the spectral neighborhood of $-1$. It does not require the absence of additional bound states near zero.

## 4. Quadratic control of the Ritz error

Write $H_R$ in blocks on $P_R\oplus(1-P_R)$:
$$
H_R=\begin{pmatrix}\mathsf A_R&\mathsf B_R^*\\
\mathsf B_R&\mathsf D_R\end{pmatrix}.
$$

The two eigenvalues of $\mathsf A_R$ converge to $-1$, while $\mathsf D_R\ge-1+g$. The off-diagonal block satisfies

$$
\|\mathsf B_R\|_{\mathrm{HS}}^2
\le C\sum_{\pm}\|Q_\mp^2Q_\pm\|_2^2
=O(R^{-1}e^{-2R}).
$$

Indeed, near the opposite core the squared tail of $Q_\pm$ contributes $R^{-1}e^{-2R}$; the fourth power of the core profile is integrable even after the required exponential weight. The remainder of space is exponentially smaller. The inverse Gram matrix is uniformly bounded for large $R$.

For $v\in P_R$, $w\in1-P_R$, Young's inequality gives

$$
2\operatorname{Re}\langle\mathsf B_Rv,w\rangle
\ge-\frac2g\|\mathsf B_Rv\|^2-\frac g2\|w\|^2.
$$

Therefore

$$
H_R\ge
\left(\mathsf A_R-\frac2g\mathsf B_R^*\mathsf B_R\right)
\oplus\left(\mathsf D_R-\frac g2\right).
$$

For large $R$, the two lowest levels of this direct sum lie in its two-dimensional first block. Min--max, together with the usual Ritz upper bound, yields

$$
0\le S_2(H_R)-S_{2,\mathrm{Ritz}}
\le\frac2g\|\mathsf B_R\|_{\mathrm{HS}}^2
=O(R^{-1}e^{-2R}).
$$

This is smaller than the leading positive deficit by a factor of order $R^{-1}$, completing the stated asymptotic.

## Scope of the advance

The calculation rules out a specific counterexample strategy using the sum of two widely separated identical Townes potentials, including exact spectral relaxation. It does not give a neighborhood theorem for arbitrary potential perturbations: scalar shape coercivity, modulation in independent translations and scales, and interaction errors would be needed for that. It also does not give $L_{1,2}^{(2)}=L_{1,2}^{(1)}$.

## Source relation

Frank, Gontier and Lewin, *The nonlinear Schrödinger equation for orthonormal functions II. Application to Lieb--Thirring inequalities*, arXiv:2002.04964v3, Theorem 2 and Section 4 (especially Lemma 12 and its exact expression for the Ritz diagonal). https://arxiv.org/html/2002.04964v3

Their binding range is $\gamma>\max(0,2-d/2)$, which excludes the present endpoint. The fixed-potential endpoint estimate above is a derivation in the accompanying derivations, rather than a theorem attributed to that paper. A literature search did not locate this exact endpoint statement; that is not proof of originality.
