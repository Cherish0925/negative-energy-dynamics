# Nonradial mass-critical BNLS: alternative routes and exact obstructions

Date: 2026-10-07. These are mathematical working notes, not a proof of the full nonradial blowup conjecture.

We write

$$
p=2+8/N,\quad M(u)=\int |u|^2,\quad
E(u)=\frac12\int|\Delta u|^2-\frac1p\int |u|^p,
\quad P(u)=\operatorname{Im}\int\bar u\nabla u.
$$

The equation is $iu_t=\Delta^2u-|u|^{p-2}u$. For a real smooth multiplier $\phi$, put
$V_\phi=2\operatorname{Im}\int\bar u\nabla\phi\cdot\nabla u$.
Its derivative has principal terms

$$
\mathcal V_\phi(u)
=8\operatorname{Re}\sum_{i,j,k}\int\phi_{jk}u_{ik}\bar u_{ij}
-\frac{8}{N+4}\int\Delta\phi |u|^p
+\mathcal L_\phi(u),
$$

where $\mathcal L_\phi$ comprises terms bounded by a constant times
$\|\nabla u\|_2^2+\|u\|_2^2$ when derivatives of $\phi$ through order six are bounded. Thus $V'_{|x|^2/2}=16E$. The identity is from Boulenger--Lenzmann and appears as Proposition 5.1 in Dinh's 2026 radial preprint.

## 1. The proposed weighted interpolation cannot extend to all nonradial data

Let $R>0$ be fixed and
$$
w_{R,z}(x)=1-\exp(-|x-z|^4/R^4),\qquad
D_{R,z}(u)=\int w_{R,z}|D^2u|_F^2.
$$

**Proposition.** There are a fixed mass $M_*$ and a sequence $u_\lambda\in C_c^\infty(\mathbb R^N)$ with
$$
M(u_\lambda)=M_*,\quad E(u_\lambda)=-1,\quad P(u_\lambda)=0
$$
such that, uniformly over all centers $z\in\mathbb R^N$,
$$
\frac{\int w_{R,z}|u_\lambda|^p}{D_{R,z}(u_\lambda)}
\longrightarrow \frac p2,
\qquad
\inf_z D_{R,z}(u_\lambda)\longrightarrow\infty.
$$
Consequently no inequality
$$
\int w_{R,z(u)}|u|^p\leq\varepsilon D_{R,z(u)}(u)+C
$$
can hold for this invariant class for any $\varepsilon<p/2$, even if the center is chosen separately and optimally for every datum, and even if $C$ depends on $M_*,E=-1,P=0,R$.

**Proof.** Choose any nonzero real radial compactly supported smooth function $h$. There is a unique positive amplitude $A$ such that $f=Ah$ has zero energy: explicitly,
$A^{p-2}=p\|\Delta h\|_2^2/(2\|h\|_p^p)$.
Let $K=\|\Delta f\|_2^2$ and $B=\|f\|_p^p=(p/2)K$.
Choose another real compactly supported smooth $g$ with $E(g)=-1$; amplitude enlargement first makes the energy negative and critical spatial scaling then normalizes it.

Fix distinct centers $a_1,a_2$, with supports of the shrinking packets separated from the support of $g$, and let
$$
u_\lambda(x)=\lambda^{N/2}f(\lambda(x-a_1))
+\lambda^{N/2}f(\lambda(x-a_2))+g(x).
$$
For sufficiently large $\lambda$, supports are disjoint. Mass and energy are exactly additive, and all functions are real; hence the stated invariant identities hold.
Set $W_z=w_{R,z}(a_1)+w_{R,z}(a_2)$. If $d=|a_1-a_2|>0$, then at least one center is at distance at least $d/2$ from $z$. Thus
$$
W_z\geq 1-e^{-d^4/(16R^4)}=:c_{d,R}>0.
$$
The first derivatives of all translated weights are uniformly bounded by $C/R$. Critical scaling, the mean value theorem, and bounded support therefore give, uniformly in $z$,
$$
\int w_{R,z}|u_\lambda|^p=\lambda^4W_zB+O(\lambda^3)+O(1),
$$
$$
D_{R,z}(u_\lambda)=\lambda^4W_zK+O(\lambda^3)+O(1).
$$
The denominator diverges uniformly, and the ratio tends to $B/K=p/2$. This proves the proposition.

The fixed negative-energy packet is not asserted to stay disjoint under evolution. Only the instantaneous inequality is being disproved. This is not a counterexample to finite-time blowup.

## 2. Keeping signed kinetic and nonlinear defects does not restore the same coercive estimate

The obstruction above is stronger than a failure of one use of Young's inequality.
For real radial $f$, rotational invariance gives
$$
\operatorname{Re}\sum_i\int f_{ik}\bar f_{ij}
=\frac KN\delta_{jk}.
$$
For a packet $f_{\lambda,a}=\lambda^{N/2}f(\lambda(x-a))$, the leading contribution to the full virial derivative is
$$
\lambda^4\Delta\phi(a)
\left(\frac{8K}{N}-\frac{8B}{N+4}\right)=0,
$$
because $B=(N+4)K/N$. For a smooth bounded multiplier the error is $O(\lambda^3)$; the lower-order virial terms are $O(\lambda^2)$.
Applying this to both packets in the preceding construction gives
$\mathcal V_\phi(u_\lambda)=O(\lambda^3)$, while
$D_{R,z}(u_\lambda)\geq c\lambda^4$.
For translated exponential multipliers the bounds are uniform in the center.
Therefore a bound of the form
$$
\mathcal V_{\phi_{R,z}}(u)\leq16E(u)-cD_{R,z}(u)+C,
\qquad c>0,
$$
also fails on the fixed-invariant nonradial class, even when signed terms are estimated together and the center is selected optimally for each datum.

What would have to change is the coercive object itself, or the use of dynamical information unavailable from instantaneous mass, energy and momentum alone.

## 3. Direct quartic Riccati closure for a fixed exponential multiplier also fails

One might try to avoid the Hessian defect and prove directly that sufficiently negative $V_{\phi_R}$ forces $V'_{\phi_R}<0$. That implication is false for general nonradial states with fixed mass, energy and zero total momentum.

Here is an explicit asymptotic construction for $N\geq2$. Fix a real radial $w\in C_c^\infty$, a nonzero vector $k$, and an amplitude $A$ such that
$f(x)=Ae^{ik\cdot x}w(x)$ has energy zero. Such $A$ exists by the same amplitude formula. Write
$$
m_w=\|w\|_2^2,\quad a_w=\frac1N\|\nabla w\|_2^2,
\quad b_k=(N+4)a_w+|k|^2m_w>0.
$$
The traceless kinetic tensor of this packet is exactly
$$
T_{jk}:=\operatorname{Re}\sum_i\int f_{ik}\bar f_{ij}
-\frac{\|\Delta f\|_2^2}{N}\delta_{jk}
=A^2b_k\left(k_jk_k-\frac{|k|^2}{N}\delta_{jk}\right).
$$
This follows either by expanding $\Delta(e^{ik\cdot x}w)$, or by shifting the radial Fourier density.

Choose packet positions $\pm ae$, where $a>0$ and $|e|=1$. Put momentum $k$ at $+ae$ and momentum $-k$ at $-ae$. Choose
$$
-|k|/\sqrt N<k\cdot e<0.
$$
Add a disjoint fixed real packet $g$ of energy $-1$. After critical rescaling of the two zero-energy packets, total mass is fixed, total momentum is exactly zero, and energy is exactly $-1$.

For the exponential multiplier $\nabla\phi_R(x)=xe^{-|x|^4/R^4}$, the localized virial of the pair has leading term
$$
V_{\phi_R}(u_\lambda)
=4\lambda a e^{-a^4/R^4} A^2m_w(k\cdot e)+O(1)
\longrightarrow-\infty.
$$
At either packet center the Hessian eigenvalues are
$h_r=e^{-s}(1-4s)$, $h_t=e^{-s}$, where $s=a^4/R^4>0$.
The leading virial derivative from each zero-energy packet is
$$
8\lambda^4(h_r-h_t)A^2b_k
\left((k\cdot e)^2-|k|^2/N\right)>0.
$$
The strict sign follows because both parenthesized factors are negative. Therefore
$$
V_{\phi_R}(u_\lambda)\to-\infty,
\qquad \mathcal V_{\phi_R}(u_\lambda)\to+\infty
$$
with the second divergence of order $\lambda^4$. Hence an instantaneous universal inequality
$V'_{\phi_R}\leq-c(-V_{\phi_R})^4$ after a mass-dependent negative threshold cannot hold for this fixed multiplier. This is again an obstruction to a proof architecture, not a global solution or a disproof of the main conjecture.

## 4. A moving center incurs a genuinely new term

Let $z=z(t)$. Then
$$
\frac d{dt}V_{\phi_R(\cdot-z(t))}(u(t))
=\mathcal V_{\phi_R(\cdot-z(t))}(u(t))
-2\dot z(t)\cdot\operatorname{Im}\int\bar u\,D^2\phi_R(x-z(t))\nabla u.
$$
Inside a concentrated packet the additional term approximates $-2\dot z\cdot P$. Unlike second-order NLS, BNLS has no Galilean symmetry that sets momentum to zero while preserving the equation. Even if total momentum is zero, different packets can carry opposite large momenta; the construction above illustrates this exactly.

Using $D^2\phi_R-I=O(w_R)$, when total momentum vanishes one can estimate the remainder schematically by
$$
\varepsilon D_R+C_\varepsilon |\dot z|^{4/3}M
+\text{lower-order terms}.
$$
There is no bound on $|\dot z|$ from mass and negative energy alone. Thus moving-center arguments require a substantive dynamical control of center speed or a different cancellation.

## 5. Angular-regularity argument

The proposed anisotropic inequality on a fixed cylinder is dimensionally and analytically consistent:
$$
\|v\|_p^p\leq C
Q^{1/N}A^{(N-1)/N}\mu^{4/N},
$$
with $\mu=\|v\|_2^2$, $Q=\|\partial_r^2v\|_2^2+\mu$, and
$A=\|v\|_{L_r^2H_\theta^2}^2$. Hausdorff--Young followed by Fourier Hölder with weight
$1+(\xi/a)^4+|\eta/b|^4$, $a=(Q/\mu)^{1/4}$, $b=(A/\mu)^{1/4}$, gives exactly those exponents. The integrability exponent is
$p/(p-2)=(N+4)/4>N/4$.

On dyadic annuli the ensuing weighted estimate is
$$
\int w_R|u|^p\leq\varepsilon D_R
+C_\varepsilon R^{-4}
\left[K M^{4/(N-1)}+K^{(N-1)/N}M^{5/N}\right],
$$
where $K$ is the global angular $H^2$ mass, defined using rotations through order two. Rescaling and summation were independently checked. A bound uniform in time on $K$, combined with the nonradial virial--defect estimate, therefore gives a conditional finite-time blowup theorem.

A concrete invariant class is available in dimension two:
$$
u(t,r,\theta)=e^{im\theta}v(t,r),\qquad m\in\mathbb Z.
$$
The equation preserves this equivariance. With $K=\|u\|_2^2+\|\partial_\theta u\|_2^2+\|\partial_\theta^2u\|_2^2$,
$K=(1+m^2+m^4)M$ is uniformly bounded. Thus the proposed theorem implies finite-time blowup for every negative-energy $H^2$ datum in this fixed vortex class, including $m\ne0$. This does not cover arbitrary nonradial data. Novelty of the vortex corollary has not been established here.

## Sources actually read

- Thomas Boulenger and Enno Lenzmann, *Blowup for Biharmonic NLS*, arXiv:1503.01741, https://arxiv.org/abs/1503.01741 .
- Leonard Dinh, *Finite-Time Blow-Up of Radial Negative-Energy Solutions for the Mass-Critical Biharmonic Nonlinear Schrödinger Equation*, Meta research page dated 2026-10-02 and linked 20-page manuscript; Proposition 5.1 for the virial identity, Remark 1.4 for the proposed nonradial extension: https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/ .

The counterexamples to inequalities in Sections 1--3 are direct derivations in the preliminary calculations. They establish no counterexample to the evolution conjecture.
