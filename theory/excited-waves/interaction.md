# exact interaction primitive and optimized-center obstruction

Date: 2026-10-07. This note contains new derivations in the session. It does not prove the unrestricted nonradial blowup statement.

Set $p=2+8/N$, $N\ge2$, and use
$$
E(u)=\tfrac12\|\Delta u\|_2^2-\tfrac1p\|u\|_p^p,
\quad M(u)=\|u\|_2^2,
\quad P(u)=\operatorname{Im}\int\bar u\nabla u.
$$

## 1. An exact positive translation-invariant interaction Riesz primitive

This calculation is initially on Schwartz functions, or compactly supported smooth functions. It does not assert finiteness of the functional for every unweighted $H^2$ datum.

Let $\Psi(x,y)=u(x)u(y)$, $r=x-y$, and let $(\xi,\eta)$ denote the Fourier variables. Put
$$
q=\xi-\eta,\qquad h(\xi,\eta)=|\xi|^4+|\eta|^4.
$$
Define the matrix
$$
L(\xi,\eta)=\int_0^1
\left[4|\eta+s(\xi-\eta)|^2 I
+8(\eta+s(\xi-\eta))\otimes(\eta+s(\xi-\eta))\right]ds.
$$
The fundamental theorem of calculus gives
$$
Lq=4(|\xi|^2\xi-|\eta|^2\eta)
=(\nabla_\xi-\nabla_\eta)h.
$$
Moreover, with $Q=|\xi|^2+|\eta|^2$,
$$
\tfrac23 Q I\le L(\xi,\eta)\le6QI.
$$
Indeed,
$\int_0^1|\eta+s(\xi-\eta)|^2ds=(|\xi|^2+\xi\cdot\eta+|\eta|^2)/3$, which lies between $Q/6$ and $Q/2$.
Set $A=L^{-1}$ off the origin. It is a positive, smooth, degree $-2$ matrix symbol there.

Define the nonnegative quadratic form on the tensor product
$$
J(u)=\sum_{i,j}\langle r_i\Psi,A_{ij}(D_x,D_y)r_j\Psi\rangle
=\int (\mathcal D\widehat\Psi)^*A(\mathcal D\widehat\Psi)\,d\xi\,d\eta,
\quad \mathcal D=\nabla_\xi-\nabla_\eta.
$$
No prefactor of $i$ is needed in the second expression because it cancels in the quadratic form. The low-frequency singularity is integrable for smooth data because the Fourier-space dimension is $2N\ge4$ and $A=O(Q^{-1})$. Unlike a one-particle inverse-Laplacian construction in dimension two, this tensor-product form has no dimension-two logarithmic divergence at zero frequency.

Write $B=\sum r_i A_{ij}r_j$, $H=\Delta_x^2+\Delta_y^2$, and
$\mathcal A=\tfrac12[r\cdot(D_x-D_y)+(D_x-D_y)\cdot r]$, where $D=-i\nabla$.
Since $[H,r_i]=-i\mathcal D_i h$, the preceding matrix identity proves the exact commutator
$$
i[H,B]=2\mathcal A.
$$
Thus the inverse secant Hessian removes the nonlinear dependence of the *linear dispersive velocity* exactly, without a frequency approximation.

Let
$$
\mathsf D(u)=\operatorname{Im}\int\bar u\,x\cdot\nabla u,
\quad X(u)=\int x|u|^2,
\quad V_{\mathrm{int}}(u)=2[M\mathsf D-X\cdot P].
$$
Then $\langle\Psi,\mathcal A\Psi\rangle=V_{\mathrm{int}}$. This expression is invariant under spatial translations. Along BNLS the tensor product solves
$$
i\Psi_t=[H-F_u]\Psi,
\quad F_u(x,y)=|u(x)|^{p-2}+|u(y)|^{p-2}.
$$
Therefore
$$
J'(t)=2V_{\mathrm{int}}(u(t))+\mathcal C(u(t)),
\qquad
\mathcal C(u)=-i\langle\Psi,[F_u,B]\Psi\rangle.
$$
The nonlinear commutator has not disappeared.

With unitary Fourier normalization and
$S(u)=\int\xi|\xi|^2|\widehat u(\xi)|^2d\xi$, one has
$$
X'=4S,\qquad \mathsf D'=8E,
\quad
V_{\mathrm{int}}'=16ME-8P\cdot S.
$$
Convexity gives $MK-P\cdot S\ge0$, where $K=\|\Delta u\|_2^2$, because this is half the pair covariance of the monotone map $\xi\mapsto|\xi|^2\xi$. It does **not** give $P\cdot S\ge0$. Thus convex dispersion alone does not make the right side negative for every negative-energy datum.

If $P=0$, the momentum term vanishes and
$$
J(t)=J(0)+2V_{\mathrm{int}}(0)t+16MEt^2+
\int_0^t\mathcal C(u(s))ds.
$$
A control $\int_0^t\mathcal C=o(t^2)$ would consequently exclude a global negative-energy solution in the domain of $J$. No such control follows from the present calculations.

## 2. The nonlinear commutator really changes sign, even at negative energy and zero momentum

The preceding commutator cannot be dropped on a sign argument. Here is a proof specific to product states $\Psi=u\otimes u$, not merely arbitrary tensor-product vectors.

Choose a nonzero real radial bump $u_0\in C_c^\infty$, positive and strictly radially decreasing in the interior of its support, flat at its boundary. Set
$$
f_0(x)=|u_0(x)|^{p-2},\qquad u_s(x)=e^{isf_0(x)}u_0(x).
$$
This is the exact nonlinear-only flow $i\partial_su_s=-|u_s|^{p-2}u_s$. Its tensor phase is $e^{is(f_0(x)+f_0(y))}$.

The coefficients of $A$ are real and even under simultaneous frequency reversal, so $B$ is real under complex conjugation. Consequently $J(u_s)=J(u_{-s})$.
Furthermore,
$$
J(u_s)\longrightarrow0\quad\text{as }|s|\longrightarrow\infty,
\qquad J(u_0)>0.
$$
To justify the limit, all tensor states have one fixed compact support and converge weakly to zero in $L^2$: the phase gradient is nonzero almost everywhere on the nonzero amplitude, and the coarea formula followed by the Riemann--Lebesgue lemma applies to every $L^1$ test amplitude. On this fixed support the operator $B$ is compact. Its inverse Fourier kernel is homogeneous of degree $-(2N-2)$, with smooth angular factors; deleting a diagonal strip of width $\varepsilon$ gives a Hilbert--Schmidt operator, while the omitted strip has operator norm $O(\varepsilon^2)$ by Schur's test. Multiplication by the bounded relative positions does not change compactness. Strict positivity of $J(u_0)$ follows from positivity of $A$ and $r\Psi_0\not\equiv0$.

Since $J(u_s)$ is differentiable, even, positive at zero, and tends to zero, its derivative takes both signs. Under this nonlinear-only flow,
$$
\frac d{ds}J(u_s)=\mathcal C(u_s).
$$
Thus $\mathcal C$ takes both signs. All these functions are radial, so $P=0$.
For any one of the fixed profiles at which the derivative is nonzero, replace $u_s$ by $a u_s$ with $a$ sufficiently large. Then
$$
E(au_s)=a^2K_s/2-a^p\|u_0\|_p^p/p<0,
\qquad \mathcal C(au_s)=a^{p+2}\mathcal C(u_s).
$$
Its conjugate has the same negative energy, mass, and zero momentum, but opposite commutator sign. Hence neither $\mathcal C\le0$ nor $\mathcal C\ge0$ holds on the negative-energy, zero-momentum class.

This does not preclude a quantitative spacetime commutator estimate. It identifies precisely the remaining term for the new positive interaction primitive, and proves that a simple sign claim would be false.

## 3. Optimizing the single localization center still cannot yield a universal quartic Riccati inequality

The round-one obstruction used a fixed center. The following construction also rules out the optimized-center envelope
$$
v_*(u)=\inf_{c\in\mathbb R^N}V_{R,c}(u),
\qquad \nabla\phi_{R,c}(x)=(x-c)e^{-|x-c|^4/R^4},
$$
for every fixed $R>0$.

### 3.1 A zero-energy packet with nonzero momentum and exactly isotropic fourth-order kinetic tensor

Take real, nonzero, radial $w\in C_c^\infty$, fix $k>0$, and put
$$
w_L(x_1,x')=L^{(N-1)/2}w(x_1,Lx'),\qquad f_L=e^{ikx_1}w_L.
$$
Let
$$
S_{ij}(f)=\operatorname{Re}\sum_\ell\int\bar f_{\ell i}f_{\ell j}.
$$
Parity and transverse rotational symmetry imply $S$ is diagonal, with equal entries $S_{22}=\cdots=S_{NN}$. At $L=1$, the shifted-radial Fourier calculation gives
$$
S_{11}-S_{22}
=k^2\left[(N+4)\|\nabla w\|_2^2/N+k^2M(w)\right]>0.
$$
As $L\to\infty$, $S_{11}=O(L^2)$, whereas $S_{22}$ has a strictly positive term of order $L^4$. Therefore continuity gives some $L_*>1$ with $S_{11}=S_{22}$. At this value,
$$
S_{ij}(f_{L_*})=\frac{\|\Delta f_{L_*}\|_2^2}{N}\delta_{ij},
\qquad P(f_{L_*})=kM(w)e_1\ne0.
$$
Choose an amplitude $a>0$ so that $f=af_{L_*}$ has $E(f)=0$. Amplitude multiplication preserves tensor isotropy and nonzero momentum. The conjugate $\bar f$ has the same isotropic tensor and opposite momentum.

### 3.2 Fixed invariants, large negative envelope, and inadequate derivative size

Choose $a_0>0$, and a real compact packet $g$ of energy $-1$, supported away from $\pm a_0e_1$. For sufficiently large $\lambda$, define the disjoint sum
$$
U_\lambda(x)=\lambda^{N/2}\bar f(\lambda(x-a_0e_1))
+\lambda^{N/2}f(\lambda(x+a_0e_1))+g(x).
$$
It has exactly fixed mass $2M(f)+M(g)$, energy $-1$, and total momentum zero. At center zero,
$$
V_{R,0}(U_\lambda)
=-4\lambda a_0e^{-a_0^4/R^4}|P(f)|+O(1).
$$
Since $|V_{R,c}(U_\lambda)|\le C_R\lambda$ uniformly in $c$,
$$
-C\lambda\le v_*(U_\lambda)\le-c\lambda<0
$$
for some fixed positive constants and all large $\lambda$.

At **every** center, the order-$\lambda^4$ contribution to the frozen virial derivative cancels: zero energy and exact tensor isotropy give
$$
8\operatorname{tr}(D^2\phi_{R,c}(a)S(f))
-\frac8{N+4}\Delta\phi_{R,c}(a)\|f\|_p^p=0.
$$
Uniform bounds on multiplier derivatives give
$$
\left|\mathcal V_{\phi_{R,c}}(U_\lambda)\right|
\le C_R\lambda^3
\quad\text{for every }c.
$$
An improved $O(\lambda^2)$ estimate follows from the parity of the stress densities, but is unnecessary here.

Let $u_\lambda(t)$ be the local BNLS solution from $U_\lambda$, and define $v_\lambda(t)=\inf_cV_{R,c}(u_\lambda(t))$. The infimum is attained at $t=0$: the function of $c$ is continuous, tends to zero at infinity, and has a negative value. Its minimizers remain in a compact set for small time, by continuity of $u(t)$ in $H^1$, uniformly in the bounded multiplier. The localized virial derivative is continuous in $(t,c)$. The minimum-envelope differentiation theorem therefore gives
$$
\partial_{t+}v_\lambda(0)
=\min_{c\in\operatorname{argmin}V_{R,c}(U_\lambda)}
\mathcal V_{\phi_{R,c}}(U_\lambda)
\ge-C_R\lambda^3.
$$
In particular, $y_\lambda=-v_\lambda\asymp\lambda$, but
$\partial_{t+}y_\lambda(0)\le C_R\lambda^3$.
No universal instantaneous inequality
$$
\partial_{t+}y\ge b(y-B)_+^4,
\qquad b>0,
$$
can hold for this optimized-center envelope with constants determined only by the fixed invariants and $R$: its right side would be order $\lambda^4$.

This obstruction includes exact zero total momentum and optimizes the center separately for each datum. It does not exclude variable scales, multiple centers, different functionals, or inequalities that become valid only after a nontrivial dynamical argument.

## Current status

The inverse-secant-Hessian interaction form is a genuine positive translation-invariant primitive of the *linear* relative dilation. Its nonlinear commutator is rigorously sign-indefinite, and the domain issue for general $H^2$ data remains. Separately, the optimized-center quartic envelope fails even after exact momentum cancellation. Neither a full proof nor a global negative-energy counterexample has been obtained.
