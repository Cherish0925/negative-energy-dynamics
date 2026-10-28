# Equal-scale separated Townes cores: a fixed-rank calculation

Status: a proved asymptotic statement for the explicitly specified trial family below. It is not a proof of the sharp two-dimensional Lieb–Thirring conjecture, nor a statement about all nonlinearly relaxed multiple-core families. Historical novelty has not been established.

## Statement and normalization

Let the positive radial Townes ground state solve

$$
-\Delta Q+Q-Q^3=0\quad\text{on }\mathbb R^2,
\qquad M=\int Q^2.
$$

Set $q=Q/\sqrt M$. Then

$$
\|q\|_2^2=\|\nabla q\|_2^2=1,\qquad
\int q^4=C_1=\frac2M,
\qquad q(r)=A r^{-1/2}e^{-r}(1+O(r^{-1})),\quad A>0.
$$

Fix an integer $N\ge2$ and distinct points $a_1,\dots,a_N\in\mathbb R^2$. For $R\to\infty$, put

$$
q_i(x)=q(x-Ra_i),\qquad
P_R=\text{orthogonal projection onto }\operatorname{span}\{q_1,\dots,q_N\}.
$$

Define $d_{ij}=|a_i-a_j|$, $d_* =\min_{i<j}d_{ij}>0$, and let $m_*$ be the number of unordered pairs at distance $d_*$. Then

$$
\boxed{
C_1\operatorname{Tr}(-\Delta P_R)-\int\rho_{P_R}^2
=\frac{16\pi A^4}{M}\,m_*e^{-2Rd_*}(1+o(1)).
}
$$

In particular this finite-rank trial family lies strictly below the one-state quotient for all sufficiently large $R$. The result holds for arbitrary fixed center geometry, including collinear centers. It is not uniform when $N$ or the normalized geometry changes with $R$.

## Matrix expansion with the leading cancellations retained

Write

$$
G_{ij}=\langle q_i,q_j\rangle=\delta_{ij}+S_{ij},\quad
J_{ij}=\int q_i^3q_j,\quad
b_{ij}=\int q_i^2q_j^2.
$$

Here $S_{ii}=0$, $J_{ii}=C_1$, and $J_{ij}=J_{ji}$, the last fact following either from reflection about the midpoint or from the elliptic equation and integration by parts. Put $J_\circ=J-C_1I$. For large $R$, $G$ is positive definite and

$$
H=G^{-1}=I-S+S^2+O_N(\|S\|^3).
$$

The kinetic matrix satisfies the exact identity

$$
K_{ij}=\int\nabla q_i\cdot\nabla q_j=MJ_{ij}-G_{ij}.
$$

Consequently

$$
T_R=\operatorname{Tr}(HK)
=N+2\operatorname{Tr}S^2-M\operatorname{Tr}(SJ_\circ)
+O_N(s_0^2j_0+s_0^3),
$$

where $s_0=\max_{i\ne j}|S_{ij}|$ and $j_0=\max_{i\ne j}|J_{ij}|$. Boundedness of all other matrix entries is absorbed into the constant.

The projector density is exactly

$$
\rho_{P_R}(x)=\sum_{i,j}H_{ij}q_i(x)q_j(x).
$$

Let $\rho_0=\sum_iq_i^2$, $\rho_1=-\sum_{i,j}S_{ij}q_iq_j$, and $\rho_2=\sum_{i,j}(S^2)_{ij}q_iq_j$. The cubic remainder in $H$ has density $L^2$-norm $O_N(s_0^3)$, because all $\|q_iq_j\|_2$ are uniformly bounded. Thus

$$
F_R=\int\rho_0^2+2\int\rho_0\rho_1+2\int\rho_0\rho_2
+O_N(s_0^2b_0+s_0^3),
$$

where $b_0=\max_{i\ne j}b_{ij}$. In this formula the estimate on $\rho_1^2$ uses
$\|\rho_1\|_2\le C_Ns_0b_0^{1/2}$; the remaining quadratic cross terms are at most $O_N(s_0^3)$.

For three distinct indices introduce

$$
t_{kij}=\int q_k^2q_iq_j,\qquad
t_0=\max_{k,i,j\ \mathrm{distinct}}t_{kij},
$$

with $t_0=0$ for $N=2$. Directly separating repeated indices gives

$$
\int\rho_0^2=NC_1+2\sum_{i<j}b_{ij},
$$

$$
2\int\rho_0\rho_1=-8\sum_{i<j}S_{ij}J_{ij}+O_N(s_0t_0),
$$

$$
2\int\rho_0\rho_2=2C_1\operatorname{Tr}S^2
+O_N\bigl(s_0^2(b_0+j_0+t_0)\bigr).
$$

Since $C_1M=2$ and $\operatorname{Tr}(SJ_\circ)=2\sum_{i<j}S_{ij}J_{ij}$, subtraction yields

$$
\boxed{
C_1T_R-F_R
=4\sum_{i<j}S_{ij}J_{ij}-2\sum_{i<j}b_{ij}
+O_N\bigl(s_0^3+s_0^2(j_0+b_0+t_0)+s_0t_0\bigr).
}
$$

In particular the potentially larger terms of order $R e^{-2Rd_*}$, arising from $\operatorname{Tr}S^2$, cancel exactly. Keeping only density overlap and omitting Gram orthogonalization would miss the leading sign.

## Control of the three-core and higher terms

For any fixed $\eta\in(0,1)$, the global exponential bound on $q$ implies

$$
t_{kij}\le C_\eta
e^{-(1-\eta)R(d_{ki}+d_{kj})}.
$$

Indeed, writing $r_\ell=|x-Ra_\ell|$,

$$
2r_k+r_i+r_j\ge R(d_{ki}+d_{kj}),
$$

and one retains the factor $e^{-2\eta r_k}$ for integrability. Thus

$$
t_0=O_\eta(e^{-2(1-\eta)Rd_*}).
$$

The two-core asymptotics below give

$$
s_0=O(R^{1/2}e^{-Rd_*}),\quad
j_0=O(R^{-1/2}e^{-Rd_*}),\quad
b_0=O(R^{-1/2}e^{-2Rd_*}).
$$

Choose, for example, $\eta=1/4$. Then the entire displayed remainder is
$o(e^{-2Rd_*})$. In particular $s_0t_0=O(R^{1/2}e^{-(5/2)Rd_*})$. A sharper geometry-dependent bound uses the triangle perimeter $d_{ij}+d_{ki}+d_{kj}\ge3d_*$. Triangle equality for collinear centers never brings these terms down to the leading two-core exponential order.

## Two-core constants

For $\ell\to\infty$, let

$$
s(\ell)=\int q(x)q(x-\ell e_1),\quad
j(\ell)=\int q(x)^3q(x-\ell e_1),\quad
b(\ell)=\int q(x)^2q(x-\ell e_1)^2.
$$

Then

$$
s(\ell)=\sqrt{2\pi}\,A^2\ell^{1/2}e^{-\ell}(1+o(1)),
$$

$$
j(\ell)=\frac{\sqrt{8\pi}\,A^2}{M}\ell^{-1/2}e^{-\ell}(1+o(1)),
$$

$$
b(\ell)=O(\ell^{-1/2}e^{-2\ell}).
$$

Only the upper bound on $b$ is required for the theorem. It has a direct global proof: for $r>0$, $q(r)^2\le C e^{-2r}/r$. If $f(x)=e^{-2|x|}/|x|$, then the two-dimensional Fourier transform, with phase $e^{-ix\cdot\xi}$, gives

$$
\widehat f(\xi)=\frac{2\pi}{\sqrt{4+|\xi|^2}},\qquad
(f*f)(x)=2\pi K_0(2|x|).
$$

Therefore $b(\ell)\le C^2\,2\pi K_0(2\ell)=O(\ell^{-1/2}e^{-2\ell})$. A complete Laplace asymptotic gives $b(\ell)\sim\pi^{3/2}A^4\ell^{-1/2}e^{-2\ell}$; no second-order expansion of the final deficit is asserted here.

For completeness, the constants in $s$ and $j$ can be obtained without an interior-tube approximation. The Green function of $-\Delta+1$ is $g(x)=K_0(|x|)/(2\pi)$, so $q=M g*q^3$. Its tail gives

$$
\int e^{x_1}q(x)^3\,dx=\frac{\sqrt{8\pi}\,A}{M}.
$$

Dominated convergence then gives the stated $j$ asymptotic. Also

$$
(g*g)(x)=\frac{|x|K_1(|x|)}{4\pi}
\sim\frac1{4\sqrt{2\pi}}|x|^{1/2}e^{-|x|}.
$$

Since $q$ is even, $s(\ell)=(q*q)(\ell e_1)$. Applying this convolution asymptotic to
$M^2(g*g)*(q^3*q^3)$, whose source has exponential moments beyond exponent one, proves the stated constant for $s$.

It follows that

$$
4s(\ell)j(\ell)=\frac{16\pi A^4}{M}e^{-2\ell}(1+o(1)),
\qquad b(\ell)=o(e^{-2\ell}).
$$

There are only finitely many pair distances. Pairs with $d_{ij}>d_*$ contribute exponentially less than nearest pairs. Substitution into the matrix expansion proves the theorem.

## Corollary: the exact first $N$ eigenvalues of the fixed multiple-well potential

Keep the same fixed geometry and define the actual potential and Schrödinger operator

$$
V_R=M\sum_{i=1}^Nq_i^2=\sum_{i=1}^NQ(x-Ra_i)^2,
\qquad \mathcal H_R=-\Delta-V_R.
$$

For large $R$, its first $N$ eigenvalues are negative. Set
$S_N(\mathcal H_R)=-\sum_{i=1}^N\lambda_i(\mathcal H_R)$. Then

$$
\boxed{
\frac1{2M}\int V_R^2-S_N(\mathcal H_R)
=8\pi A^4m_*e^{-2Rd_*}(1+o(1)).
}
$$

Here $A$ is still the tail coefficient of the normalized $q$. Equivalently, if $a=\sqrt M A$ is the tail coefficient of $Q$, the coefficient is $8\pi a^4m_*/M^2$. This conclusion allows full relaxation of the first $N$ eigenfunctions for this fixed potential, not merely a restriction to the translated ground-state span. It concerns the first $N$ levels, not the sum over every negative eigenvalue.

### Exact finite-dimensional trace

Introduce the diagonal matrix $D$ and off-diagonal matrix $U$ by

$$
D_{ii}=\sum_{k\ne i}b_{ik},\qquad D_{ij}=0\ (i\ne j),
$$

$$
U_{ij}=\sum_{k\notin\{i,j\}}t_{kij}\ (i\ne j),\qquad U_{ii}=0.
$$

The potential matrix in the $q_i$ basis is

$$
\left(\int V_Rq_iq_j\right)_{ij}
=M(C_1I+2J_\circ+D+U).
$$

Combining this with $K=M(C_1I+J_\circ)-G$, the exact Hamiltonian matrix is

$$
\left(\langle q_i,\mathcal H_Rq_j\rangle\right)_{ij}
=-G-M(J_\circ+D+U).
$$

Thus its trace in an orthonormal basis of $\operatorname{Ran}P_R$ is obtained by multiplying by $G^{-1}$. The negative Ritz sum is exactly

$$
S_{N,\mathrm{Ritz}}
=N+M\operatorname{Tr}\bigl(G^{-1}(J_\circ+D+U)\bigr).
$$

Expanding $G^{-1}$, using $\operatorname{Tr}J_\circ=\operatorname{Tr}U=0$, $\operatorname{Tr}(SD)=0$, and the previous remainder estimates, gives

$$
S_{N,\mathrm{Ritz}}
=N+2M\sum_{i<j}b_{ij}-2M\sum_{i<j}S_{ij}J_{ij}
+o(e^{-2Rd_*}).
$$

Meanwhile

$$
\frac1{2M}\int V_R^2=N+M\sum_{i<j}b_{ij}.
$$

Therefore the Ritz deficit is

$$
2M\sum_{i<j}S_{ij}J_{ij}-M\sum_{i<j}b_{ij}
+o(e^{-2Rd_*})
=8\pi A^4m_*e^{-2Rd_*}(1+o(1)).
$$

### A uniform complementary gap for fixed $N$

The scalar operator $h=-\Delta-Q^2$ has simple ground eigenvalue $-1$, with normalized eigenfunction $q$, and essential spectrum $[0,\infty)$. Hence some $g_0\in(0,1]$ satisfies

$$
h+1\ge g_0(I-|q\rangle\langle q|).
$$

Choose smooth IMS cutoffs $\chi_1,\dots,\chi_N,\chi_0$ with $\sum_{i=0}^N\chi_i^2=1$. Each $\chi_i$, $i\ge1$, equals one within distance $Rd_*/6$ of $Ra_i$, vanishes outside distance $Rd_*/3$, and satisfies $|\nabla\chi_i|\le C/R$; $\chi_0$ covers the remaining region. Their core supports are disjoint. On any core support, all other wells are exponentially small. On the support of $\chi_0$, every well is exponentially small.

If $f\perp\operatorname{Ran}P_R$, then

$$
|\langle\chi_if,q_i\rangle|
=|\langle f,(\chi_i-1)q_i\rangle|
\le Ce^{-cR}\|f\|_2.
$$

Applying the scalar gap to the core pieces, positivity of $-\Delta+1$ to the exterior piece, and the IMS identity gives

$$
\langle f,(\mathcal H_R+1)f\rangle
\ge(g_0-CR^{-2}-Ce^{-cR})\|f\|_2^2.
$$

For all large $R$, this proves

$$
(I-P_R)\mathcal H_R(I-P_R)\ge(-1+g)(I-P_R)
$$

with a fixed $g>0$. Constants may depend on the fixed $N$ and center geometry. This proof does not assume absence of other negative levels away from $-1$.

### Exact spectral relaxation changes only a lower-order term

Write $\mathcal H_R$ in blocks relative to $P_R\oplus(I-P_R)$:

$$
\mathcal H_R=\begin{pmatrix}\mathsf A_R&\mathsf B_R^*\\
\mathsf B_R&\mathsf D_R\end{pmatrix}.
$$

All eigenvalues of $\mathsf A_R$ tend to $-1$, by its exact matrix representation above, whereas $\mathsf D_R\ge-1+g$. The residual of each original basis function is exactly

$$
(\mathcal H_R+1)q_i=-M\sum_{k\ne i}q_k^2q_i.
$$

The translated-core overlap bound

$$
\int q_k^4q_i^2=O\bigl((Rd_{ik})^{-1}e^{-2Rd_{ik}}\bigr)
$$

follows by convolution of $q^4$, which has exponential moments beyond exponent two, against the tail $q^2(r)=O(r^{-1}e^{-2r})$. Using Cauchy–Schwarz over the fixed finite sum and boundedness of $G^{-1}$, one gets

$$
\|\mathsf B_R\|_{\mathrm{HS}}^2
\le C\sum_i\|(\mathcal H_R+1)q_i\|_2^2
=O(R^{-1}e^{-2Rd_*}).
$$

For $v\in\operatorname{Ran}P_R$, $w\perp\operatorname{Ran}P_R$, Young's inequality gives

$$
2\operatorname{Re}\langle\mathsf B_Rv,w\rangle
\ge-\frac2g\|\mathsf B_Rv\|^2-\frac g2\|w\|^2.
$$

Consequently

$$
\mathcal H_R\ge
\left(\mathsf A_R-\frac2g\mathsf B_R^*\mathsf B_R\right)
\oplus\left(\mathsf D_R-\frac g2\right).
$$

For large $R$, the first $N$ levels of this lower comparison operator lie in its finite-dimensional first block. Min–max and the Ritz upper bound therefore imply

$$
0\le S_N(\mathcal H_R)-S_{N,\mathrm{Ritz}}
\le\frac2g\|\mathsf B_R\|_{\mathrm{HS}}^2
=O(R^{-1}e^{-2Rd_*}).
$$

This is $o(e^{-2Rd_*})$, proving the corollary. The IMS/Young argument is the fixed-$N$ version of the two-core proof recorded in [fixed-potential.md](fixed-potential.md); the details above make explicit why neither collinearity nor additional higher spectral levels invalidates it.

## What is and is not settled

This calculation extends the exact two-core Gram calculation to an arbitrary fixed finite collection of equally scaled translated Townes cores. Orthogonalization has a positive leading energy cost that exceeds the attractive density-overlap term in this family. The corollary also covers exact relaxation of the first $N$ eigenfunctions of the specified sum of fixed wells. These statements rule out these particular dilute-core constructions as counterexamples at rank $N$.

It does not rule out close cores, unequal scales, a number of cores increasing with separation, or deformations whose optimized contribution has not been bounded at the leading exponential order. In particular, an unrestricted minimizer need not be close to the trial span. The full sharp constant and the proposed instability of every genuinely better self-consistent state remain unproved. Related separated-well methods occur in the Lieb–Thirring literature; this note establishes a calculation, not a priority claim.
