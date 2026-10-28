# a matched transverse layer and its exact energy in the quintic system

Date: 2026-10-11. This note concerns the one-dimensional common-density quintic equation

$$
 i\partial_tu_j=-\partial_x^2u_j-\rho^2u_j,
 \qquad \rho=\sum_j|u_j|^2,
 \qquad E(U)=\tfrac12\sum_j\|u_j'\|_2^2-\tfrac16\int\rho^3.
$$

It proves a static, exact-Gram, matched-profile theorem. It does **not** construct an evolution with the suggested faster collapse rate. Historical priority has not been established. The calculation identifies an actual first-order energy effect that prevents importing the two-dimensional linear-potential argument without modification.

## 1. Why the quintic case has a different leading interaction

Put $u=u_1$, $\rho_1=|u|^2$, and $S=\sum_{j\ge2}|u_j|^2$. The primary equation is

$$
 iu_t+u_{xx}+|u|^4u+2S|u|^2u+S^2u=0.
$$

The additional term contains a spatially inhomogeneous cubic nonlinearity. Treating it as an external potential independent of the primary density would lose a derivative term. In particular, if $J=\operatorname{Im}(\bar u u_x)$, the exact identities are

$$
 E_1'=\int (2S\rho_1+S^2)_xJ,
$$

and, when the origin is the symmetry center and the relevant moments exist,

$$
 \begin{aligned}
 I_1''
 &=16E_1+4\int x(2S\rho_1+S^2)_x\rho_1\\
 &=16E_1-4\int S\rho_1^2
       +4\int xS_x\rho_1^2+8\int xSS_x\rho_1.
 \end{aligned}
$$

Thus a bound on $S_{xx}$ alone does not reproduce the two-dimensional estimate $|I''-16e|\lesssim I$. The term involving $S\rho_1^2$ has a different scaling.

## 2. The odd zero-energy profile

The scalar critical ground state and its moments are

$$
 Q(y)=3^{1/4}\sqrt{\operatorname{sech}(2y)},\qquad
 M_c=\frac{\pi\sqrt3}{2},\qquad
 V_Q=\int y^2Q(y)^2\,dy=\frac{\pi^3\sqrt3}{32}.
$$

Consider $H=-\partial_y^2-Q^4=-\partial_y^2-3\operatorname{sech}^2(2y)$. There is a unique real odd solution $F$ of

$$
 HF=0,\qquad F'(y)\longrightarrow1\quad(y\to+\infty).
$$

It has the explicit expression

$$
 F(y)=\frac\pi4\big[P_{1/2}(\tanh2y)-P_{1/2}(-\tanh2y)\big],
$$

and

$$
 F(y)=y+c\operatorname{sgn}y+O((1+|y|)e^{-4|y|}),\qquad
 c=\frac\pi4+\log2-1>0.
$$

The corresponding differentiated estimates hold to every finite order away from the irrelevant asymptotic sign notation. To verify the expression, substitute $z=\tanh2y$ in $HF=0$: the result is Legendre's equation with $\nu(\nu+1)=3/4$, hence $\nu=1/2$. The connection formula

$$
 P_{1/2}(-z)=-\frac2\pi Q_{1/2}(z)
$$

and the endpoint expansion

$$
 Q_{1/2}(z)=\tfrac12\log\frac2{1-z}-\gamma-\psi(3/2)+o(1)
$$

give the stated constant, since $\psi(3/2)=2-\gamma-2\log2$. Here $P_\nu,Q_\nu$ denote the Ferrers functions on $(-1,1)$; the ground state $Q(y)$ is a different symbol.

Multiplication of $F''=-Q^4F$ by $F$, with integration on $[-R,R]$, gives

$$
 \int_{\mathbb R}(F'^2-Q^4F^2-1)=2c.
$$

This is the raw inner, fixed-slope energy. It is **not** the energy of a profile matched to an unchanged outer field. The identity needed for matching is

$$
 \boxed{\int_{\mathbb R}\big((F'-1)^2-Q^4F^2\big)=-2c.} \tag{1}
$$

Indeed, $\int(F'-1)=2c$, so subtracting the linear cross term changes the sign. Every integrand in (1) is absolutely integrable.

## 3. Exact-Gram matched-profile theorem

Let $W=(w_2,\dots,w_N)$ be a finite family of complex, smooth, compactly supported odd functions. Suppose its Gram matrix $G=\int WW^*$ is positive definite on the occupied secondary space. Set

$$
 a_j=w_j'(0),\qquad A=\sum_{j=2}^N|a_j|^2.
$$

Let $\chi$ be a fixed smooth even cutoff, equal to one on $[-1,1]$, supported on $[-2,2]$. For $\lambda\downarrow0$, set $\delta=\sqrt\lambda$ and

$$
 r_{j,\lambda}(x)=\lambda a_j\chi(x/\delta)
             \big(F(x/\lambda)-x/\lambda\big),\qquad
 \widetilde w_{j,\lambda}=w_j+r_{j,\lambda}.
$$

There are constant, positive-Gram-correcting matrices $B_\lambda=I+o(\lambda)$ such that

$$
 W_\lambda=B_\lambda\widetilde W_\lambda,\qquad
 \int W_\lambda W_\lambda^*=G.
$$

For every real $k$, define the primary

$$
 q_{\lambda,k}(x)=\lambda^{-1/2}Q(x/\lambda)
                    \exp\!\left(\frac{ikx^2}{4\lambda}\right),
 \qquad U_{\lambda,k}=(q_{\lambda,k},W_\lambda).
$$

Then:

1. The complete Gram matrix is exactly $\operatorname{diag}(M_c,G)$. The primary-secondary entries vanish by even-odd parity, including the quadratic primary phase.
2. $W_\lambda\to W$ strongly in $H^1$.
3. The secondary density $S_\lambda=|W_\lambda|^2$ is uniformly bounded in $W^{2,\infty}(\mathbb R)$.
4. Uniformly in the primary chirp $k$, whose energy contribution is exact,

$$
 \boxed{E(U_{\lambda,k})=E(W)+\frac{V_Q}{8}k^2-cA\lambda+o(\lambda).} \tag{2}
$$

Here $E(W)=\tfrac12\sum\|w_j'\|_2^2-\tfrac16\int|W|^6$, with the common-density interpretation $|W|^6=(\sum|w_j|^2)^3$. The error in (2) does not depend on $k$, since the density and all secondary fields are independent of $k$.

### Proof

Write $g(y)=F(y)-y$. Then $g$ is bounded and smooth, $g'$ decays exponentially, and $g''$ decays exponentially with a polynomial factor. Consequently

$$
 \|r_{j,\lambda}\|_2^2=O(\lambda^2\delta),\qquad
 \|r_{j,\lambda}'\|_2^2=O(\lambda)+O(\lambda^2/\delta).
$$

Thus the secondary convergence is strong in $H^1$. Since $w_j(x)=a_jx+O(x^3)$ on the shrinking support,

$$
 \left\|\int\widetilde W_\lambda\widetilde W_\lambda^*-G\right\|
       =O(\lambda\delta^2+\lambda^2\delta)=o(\lambda).
$$

For $\widetilde G_\lambda=\int\widetilde W_\lambda\widetilde W_\lambda^*$, one possible correction is

$$
 B_\lambda=G^{1/2}
       (G^{-1/2}\widetilde G_\lambda G^{-1/2})^{-1/2}G^{-1/2}.
$$

It satisfies the stated identity and $B_\lambda-I=o(\lambda)$. All fields remain odd.

The secondary kinetic cross term obeys

$$
 \operatorname{Re}\int w_j'\overline{r_{j,\lambda}'}
 =-\operatorname{Re}\int w_j''\overline{r_{j,\lambda}}
 =O(\lambda\delta^2)=o(\lambda).
$$

The quadratic correction is

$$
 \int|r_{j,\lambda}'|^2
   =\lambda|a_j|^2\int(F'-1)^2+o(\lambda).
$$

The derivative of the cutoff contributes $O(\lambda^2/\delta)=o(\lambda)$; its cross term is also $o(\lambda)$. The pure secondary nonlinear energy changes by $o(\lambda)$, because the correction is pointwise $O(\lambda)$, supported where $|W|=O(\delta)$. The Gram correction changes the pure secondary energy by $o(\lambda)$.

At every fixed rescaled position,

$$
 \lambda^{-1}W_\lambda(\lambda y)\longrightarrow (a_jF(y))_{j=2}^N.
$$

The same expression is bounded by $C(1+|y|)$ uniformly in $\lambda$, since a smooth odd compactly supported field satisfies $|W(x)|\le C|x|$. Dominated convergence against the exponentially decaying ground state yields

$$
 \int|q_{\lambda,k}|^4 S_\lambda
   =\lambda A\int Q^4F^2+o(\lambda),\qquad
 \int|q_{\lambda,k}|^2S_\lambda^2=O(\lambda^4).
$$

Expansion of the total nonlinear energy gives coefficients $-1/2$ for each of these mixed terms. Combining the first with the secondary kinetic correction and applying (1) proves the term $-cA\lambda$. The principal scalar energy is exactly $V_Qk^2/8$, by the mass-critical ground-state identity and direct differentiation of its phase. This proves (2).

Finally, $W_\lambda$ and $W_\lambda'$ are uniformly bounded. Although $W_\lambda''$ can be $O(\lambda^{-1})$ in the inner layer, it is multiplied by $W_\lambda=O(\lambda(1+|y|))$ there when differentiating the density. The resulting products $(1+|y|)|F''(y)|$ are bounded. In the cutoff region, the second-derivative terms have size $O(\lambda/\delta^2)=O(1)$; the mixed cutoff terms are exponentially small. Therefore

$$
 S_\lambda''=2\sum_j|w_{j,\lambda}'|^2
             +2\operatorname{Re}\sum_j\overline{w_{j,\lambda}}
                                    w_{j,\lambda}''
$$

is uniformly bounded. The lower derivative bounds follow directly. This proves all assertions.

## 4. An exact energy-matched family and the dynamical question it isolates

If $A>0$, (2) with $k=0$ is strictly below $E(W)$ for every sufficiently small $\lambda$. Since the chirp adds the exact positive quantity $V_Qk^2/8$, choose the negative square root

$$
 k_\lambda=-\sqrt{\frac8{V_Q}
                  \big(E(W)-E(U_{\lambda,0})\big)}.
$$

This gives smooth, exact-Gram data satisfying **exactly**

$$
 E(U_{\lambda,k_\lambda})=E(W),\qquad
 k_\lambda=-\sqrt{\frac{8cA}{V_Q}}\sqrt\lambda+o(\sqrt\lambda).
$$

All these are actual initial states for the local PDE, not merely formal field expressions. They are not asserted to lie on a common singular trajectory.

The primary chirp has the instantaneous continuity-equation interpretation $k=\dot\lambda$. If one could construct a solution maintaining this expansion with sufficiently controlled time-dependent error and background, the zero-excess-energy branch would obey

$$
 \lambda(t)\sim\frac{2cA}{V_Q}(T-t)^2.
$$

This last statement is a **candidate dynamical law**, not a proved collapse theorem. The energy identity alone does not justify differentiating an asymptotic remainder or selecting one PDE trajectory from the static family. Establishing such a trajectory requires control of the evolving transverse layer, primary shape correction, dispersive radiation, and a remainder stronger than the currently available general endpoint estimates.

The proved conclusion is already specific: a regular-density odd background has a nonzero, negative, linear-in-width interaction energy after correct matching. It remains present despite strong secondary $H^1$ convergence, exact Gram constraints, and a uniform density $W^{2,\infty}$ bound. Therefore these static properties cannot remove this mechanism from a quintic dynamical analysis.

## 5. Relation to the earlier endpoint theorems

When the eigenvalues of $G$ are below $M_c$, these data belong to R17's simple-leading-occupation regime. They are consistent with its uniform secondary kinetic bound, primary critical mass, node at the collapse point, and one-sided estimate $\lambda\lesssim T-t$. A candidate quadratic law is faster and does not contradict that bound. The theorem does not dispute the R18 two-dimensional result: that equation has the additive potential $Su$, while the present equation contains $2S|u|^2u$.

The odd profile and matched energy coefficient have been independently computed in a parallel branch. They are elementary consequences of the explicit transverse operator and matching identities, rather than a claimed resolution of a named historical conjecture. A literature check is still needed before asserting novelty of this particular coupled-system application.

Special-function inputs were checked against the NIST Digital Library of Mathematical Functions on 2026-10-11: [DLMF 14.9.10, connection formula](https://dlmf.nist.gov/14.9.E10) and [DLMF 14.8, endpoint expansions](https://dlmf.nist.gov/14.8). The differential equation, matching sign, exact-Gram adjustment, and energy asymptotic above are derived in this note.
