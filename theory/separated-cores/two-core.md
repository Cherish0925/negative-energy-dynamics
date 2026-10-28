# exact two-core interaction at the two-dimensional cubic endpoint

Date: 2026-10-12. This note treats the **orthogonal projection onto two prescribed Townes profiles**. It does not prove the full two-dimensional Lieb–Thirring conjecture or exclude arbitrary deformed collective states. The equal-scale sign, bounded near-equal-scale crossover, and fixed unequal-scale coefficient below follow analytically. Historical priority is not claimed.

## 1. Normalization and an exact identity

Let the positive radial Townes profile satisfy

$$
-\Delta Q+Q-Q^3=0,\qquad M=\int Q^2,\qquad q=Q/\sqrt M.
$$

Pohozaev identities give

$$
\int q^2=\int|\nabla q|^2=1,\qquad \int q^4=C_1=2/M,
\qquad -\Delta q+q=Mq^3.
$$

Write $q_\lambda(x)=\lambda q(\lambda x)$, and set
$a=q_\lambda(x)$, $b=q_\mu(x-Re_1)$. Define

$$
s=\int ab,\quad j_1=\int a^3b,\quad j_2=\int ab^3,
\quad B=\int a^2b^2,\quad t=\int\nabla a\cdot\nabla b.
$$

For the rank-two orthogonal projector $P$ onto $\operatorname{span}\{a,b\}$, its density and kinetic energy are exactly

$$
\rho_P=\frac{a^2+b^2-2sab}{1-s^2},\qquad
T(P)=\frac{\lambda^2+\mu^2-2st}{1-s^2}.
$$

The equations for the profiles yield

$$
t=Mj_1-\lambda^2s=Mj_2-\mu^2s.
$$

Consequently, with $D(P)=C_1T(P)-\int\rho_P^2$, direct expansion gives

$$
\boxed{
D(P)(1-s^2)^2
=2s(j_1+j_2)(1+s^2)-2B(1+2s^2)
-C_1(\lambda^2+\mu^2)s^4.}
\tag{1}
$$

For equal scales $\lambda=\mu=1$, symmetry gives $j_1=j_2=j$, recovering

$$
D(P)(1-s^2)^2=4sj(1+s^2)-2B(1+2s^2)-2C_1s^4.
\tag{2}
$$

No neglect of overlap or approximate orthogonalization is used in (1)–(2).

## 2. Equal scales: rigorous leading sign and constants

The radial ODE implies the tail expansion

$$
q(r)=A r^{-1/2}e^{-r}(1+O(r^{-1})),\qquad A>0.
\tag{3}
$$

The three interaction integrals satisfy

$$
\begin{aligned}
s(R)&\sim \sqrt{2\pi}\,A^2R^{1/2}e^{-R},\\
j(R)&\sim \frac{\sqrt{8\pi}\,A^2}{M}R^{-1/2}e^{-R},\\
B(R)&\sim \pi^{3/2}A^4R^{-1/2}e^{-2R}.
\end{aligned}
\tag{4}
$$

Here is a dominated-convergence proof which also handles the apparent singularities at the endpoints of the line joining the cores. Put the two centers at $\pm Re_1/2$ and use elliptic coordinates

$$
x_1=\frac R2\cosh\eta\cos\theta,\qquad
x_2=\frac R2\sinh\eta\sin\theta,
\quad \eta\ge0,\quad0\le\theta<2\pi.
$$

The distances $r_1,r_2$ to the centers satisfy

$$
r_1+r_2=R\cosh\eta,\qquad
r_1r_2=\frac{R^2}{4}(\sinh^2\eta+\sin^2\theta),
\qquad dx=r_1r_2\,d\eta\,d\theta.
$$

Define $h(r)=r e^{2r}q(r)^2$. This function is bounded on $[0,\infty)$ and tends to $A^2$. The exact formulas are

$$
B=\int_0^\infty\!\int_0^{2\pi}
h(r_1)h(r_2)e^{-2R\cosh\eta}\,d\theta d\eta,
$$

$$
s=\int_0^\infty\!\int_0^{2\pi}
\sqrt{h(r_1)h(r_2)}\sqrt{r_1r_2}
e^{-R\cosh\eta}\,d\theta d\eta.
$$

Set $\eta=u/\sqrt R$. For almost every $\theta$, both radii tend to infinity. Since $R(\cosh(u/\sqrt R)-1)\ge u^2/2$, dominated convergence gives

$$
\lim_{R\to\infty}R^{1/2}e^{2R}B
=A^4(2\pi)\int_0^\infty e^{-u^2}du=\pi^{3/2}A^4,
$$

$$
\lim_{R\to\infty}R^{-1/2}e^Rs
=\frac{A^2}{2}\int_0^{2\pi}|\sin\theta|d\theta
\int_0^\infty e^{-u^2/2}du=\sqrt{2\pi}A^2.
$$

For the latter integral, the additional factor is bounded by a constant times $1+\sinh u$ when $R\ge1$, which is still integrable against $e^{-u^2/2}$.

For $j$, the pointwise tail limit and dominated convergence give

$$
j(R)\sim A R^{-1/2}e^{-R}\int q(x)^3e^{x_1}dx.
$$

A suitable dominating function is a constant times
$q(x)^3(1+|x|)^{1/2}e^{|x|}$, which is integrable. Finally, the Green representation

$$
q=M(-\Delta+1)^{-1}q^3,\qquad
(-\Delta+1)^{-1}(x)=\frac1{2\pi}K_0(|x|)
$$

and $K_0(r)\sim\sqrt{\pi/(2r)}e^{-r}$ imply

$$
\int q^3e^{x_1}=\frac{\sqrt{8\pi}A}{M}.
$$

Substitution into (2) proves

$$
\boxed{D(P_R)\sim\frac{16\pi A^4}{M}e^{-2R}>0.}
\tag{5}
$$

Thus two distant equal-scale Townes profiles, when projected and orthogonalized exactly, approach the scalar sharp constant **from below**. The positive leading interaction is of order $e^{-2R}$; the direct density-overlap term $2B$ is smaller by $R^{-1/2}$. Formula (5) is an asymptotic sign statement, not an explicit numerical threshold for how large $R$ must be.

## 3. The crossover when scale differences are of order 1/R

Let $\lambda_R=1-c/R$, $\mu_R=1+c/R$, where $c$ stays in a fixed bounded interval as $R\to\infty$. The same elliptic-coordinate proof gives, uniformly for bounded $c$,

$$
\begin{aligned}
s&\sim \sqrt{2\pi}A^2R^{1/2}e^{-R}\frac{\sinh c}{c},\\
j_1+j_2&\sim\frac{2\sqrt{8\pi}A^2}{M}R^{-1/2}e^{-R}\cosh c,\\
B&\sim\pi^{3/2}A^4R^{-1/2}e^{-2R}I_0(2c).
\end{aligned}
\tag{6}
$$

The ratios at $c=0$ are defined by continuity. Indeed the exponential factors in elliptic coordinates acquire respectively $e^{c\cos\theta}$ and $e^{2c\cos\theta}$, and the boundedness of $c$ supplies a common integrable majorant. The localized cubic integrals acquire $e^{-c}$ and $e^c$.

Equation (1) now yields

$$
\boxed{D(P_R)\sim\frac{16\pi A^4}{M}
\frac{\sinh(2c)}{2c}e^{-2R}>0.}
\tag{7}
$$

Hence a bounded detuning of size $1/R$ does not reverse the leading sign. This is not uniform for unbounded $|c|$, and should not be extrapolated to fixed unequal scales.

## 4. Fixed unequal scales: an exact one-core coefficient

Fix $0<\lambda<\mu$, put $k=\lambda/\mu$, and define finite moments

$$
I_1(k)=\int q(x)e^{kx_1}dx,\quad
I_2(k)=\int q(x)^2e^{2kx_1}dx,\quad
I_3(k)=\int q(x)^3e^{kx_1}dx.
$$

The profile equation, integrated against $e^{kx_1}$, gives

$$
MI_3(k)=(1-k^2)I_1(k).
$$

The slower tail of $a$ sampled around the core of $b$ gives

$$
\begin{aligned}
s&\sim A\sqrt\lambda\,\mu^{-1}I_1(k)R^{-1/2}e^{-\lambda R},\\
j_2&\sim A\sqrt\lambda\,\mu I_3(k)R^{-1/2}e^{-\lambda R},\\
B&\sim A^2\lambda I_2(k)R^{-1}e^{-2\lambda R},\qquad j_1=o(s).
\end{aligned}
$$

All follow by the same tail dominated-convergence argument; the strict inequality $\lambda<\mu$ supplies integrable exponential majorants. Therefore

$$
\boxed{D(P_R)\sim2A^2\lambda G(k)R^{-1}e^{-2\lambda R},\qquad
G(k)=\frac{1-k^2}{M}I_1(k)^2-I_2(k),}
\tag{8}
$$

where the displayed equivalent with $\sim$ presumes $G(k)\ne0$; without that presumption the always-valid statement is
$R e^{2\lambda R}D(P_R)\to2A^2\lambda G(k)$.

Two portions of the sign can be settled without numerical input:

* At $k=0$,
  $G(0)=(\int q)(\int q^3)-(\int q^2)^2>0$
  by strict Cauchy–Schwarz, since $q$ is nonconstant. Analyticity in $|k|<1$ gives positivity for all sufficiently small positive $k$.
* As $k\uparrow1$, radial integration and the Bessel asymptotic give
  $$
  I_1(k)\sim\frac{A\sqrt{2\pi}}{1-k},\qquad
  I_2(k)\sim\frac{\pi A^2}{\sqrt{2(1-k)}}.
  $$
  Consequently $G(k)\sim4\pi A^2/[M(1-k)]>0$.

**The sign of G over the remaining compact interval is not proved here.** An informal nonrigorous quadrature was positive at sampled points, but that does not establish positivity on an interval, much less the unrestricted projector inequality.

## 5. What profile relaxation can and cannot currently change

Let $\Pi_R=1-P_R$ and $H_R=-\Delta-M\rho_{P_R}$ for the equal-scale pair. The exact equation gives

$$
\Pi_RH_Ra=-\frac{M}{1-s^2}\Pi_R
\bigl(ab^2-2sa^2b+s^2a^3\bigr).
$$

The tail bounds yield
$\|ab^2\|_2+\|a^2b\|_2=O(R^{-1/2}e^{-R})$, while
$s=O(R^{1/2}e^{-R})$. Thus the normal first-variation residual of the prescribed projection is

$$
\|\nabla_{\mathrm{normal}}D(P_R)\|=O(R^{-1/2}e^{-R}).
\tag{9}
$$

This supplies a precise **conditional** local argument. If a uniform positive lower bound for the constrained Hessian is established after modulating all individual-core translation and dilation modes (and removing occupied-space gauge), shape relaxation in the resulting normal directions lowers D by at most $O(R^{-1}e^{-2R})$. That would be too small to overturn (5). However, this note does not establish the required uniform modulation/coercivity theorem or all regimes of the relative scale. Soft modes cannot simply be dropped from the proof. Equations (5)–(9) alone therefore do not prove a local nonbinding theorem for every nearby profile, and certainly not a global theorem.

For fixed unequal scales, there is an additional obstruction: the squared normal residual is generally of order $R^{-1}e^{-2\lambda R}$, the **same** order as the interaction in (8). Profile relaxation can therefore alter its leading coefficient. Even a proof that the raw coefficient $G(k)$ is positive for every $k$ would not by itself exclude binding through unequal-scale deformation.

## 6. Relation to established work

Frank, Gontier and Lewin, *The Nonlinear Schrödinger Equation for Orthonormal Functions II: Application to Lieb–Thirring Inequalities*, Commun. Math. Phys. 384 (2021), 1783–1828, arXiv:2002.04964v3, DOI 10.1007/s00220-021-04039-5.

Primary PDF: https://arxiv.org/pdf/2002.04964 .

Their Sections 3–4 already use separated nonlinear optimizers, Gram-matrix orthogonalization and exponentially small interactions to prove strict improvement in the range $p<2$, corresponding in dimension two to $\gamma>1$. Their theorems explicitly exclude the endpoint studied here. We have independently expanded the prescribed two-Townes projection at that endpoint, retaining the terms which their strict-inequality parameter range can discard. This is a continuation of an established method; this note does **not** establish that the endpoint expansion or its refinements are historically new.

## 7. Status

Proved within this note: exact projector identity; large-separation equal-scale positivity; bounded $1/R$-scale-detuning positivity; the fixed unequal-scale interaction coefficient and its positivity near the two ends of $0<k<1$; the normal residual estimate.

Not proved: all-ratio positivity; a uniform theorem allowing arbitrary profile relaxation; exclusion of compact collective optimizers; the rank-two or unrestricted sharp Lieb–Thirring inequality.
