# Slice Schatten control implies physical density control

This is a rank-independent transfer lemma. It does not prove a joint-deficit gap, construct soliton channels, or improve the unrestricted planar constant by itself.

Let $A(x),B(x)\geq0$ be finite-rank positive operators on $L^2(\mathbb R_y)$, with measurable dependence on $x$, finite transverse kinetic energy, and physical densities $\rho_A(x,y)=A(x;y,y)$, $\rho_B(x,y)=B(x;y,y)$. Put

$$
E=\int_{\mathbb R}\|A(x)-B(x)\|_{\mathfrak S^3}^3\,dx,
\qquad
T=\int_{\mathbb R}\operatorname{Tr}\bigl(-\partial_y^2\bigr)(A(x)+B(x))\,dx.
$$

Assume the densities belong to $L^2(\mathbb R^2)$, and write $F_A=\int\rho_A^2$, $F_B=\int\rho_B^2$. Then

$$
\boxed{\quad
\|\sqrt{\rho_A}-\sqrt{\rho_B}\|_{L^4(\mathbb R^2)}
\leq (2/3)^{1/8}(ET)^{1/8}.
\quad}
$$

Consequently,

$$
|F_A^{1/4}-F_B^{1/4}|\leq (2/3)^{1/8}(ET)^{1/8},
$$

$$
\|\rho_A-\rho_B\|_{L^2}
\leq (2/3)^{1/8}(ET)^{1/8}(F_A^{1/4}+F_B^{1/4}).
$$

No orthogonality relation between $A$ and $B$, no fixed rank, and no full $H^1$ approximation are required.

## Proof

First prove the needed square-root Schatten estimate directly. For positive finite-rank $A,B$, set

$$
X=\sqrt A,\quad Y=\sqrt B,\quad D=X-Y,\quad S=X+Y,
\quad M=A-B=(SD+DS)/2.
$$

Let $K=\operatorname{sgn}(D)|D|^4$. In an eigenbasis of $D$, positivity of $S+D=2X$ and $S-D=2Y$ gives $S_{ii}\geq|d_i|$. Therefore

$$
\operatorname{Tr}(MK)=\operatorname{Tr}(S|D|^5)
\geq\operatorname{Tr}|D|^6.
$$

Schatten Holder gives

$$
\operatorname{Tr}(MK)
\leq\|M\|_{\mathfrak S^3}\|K\|_{\mathfrak S^{3/2}}
=\|A-B\|_{\mathfrak S^3}(\operatorname{Tr}|D|^6)^{2/3}.
$$

Thus

$$
\operatorname{Tr}|\sqrt A-\sqrt B|^6
\leq\|A-B\|_{\mathfrak S^3}^3. \tag{1}
$$

Now apply this for each $x$, and put

$$
D(x)=\sqrt{A(x)}-\sqrt{B(x)},\qquad q(x,y)=\rho_{D(x)^2}(y).
$$

Viewing the diagonal density as the squared norm of the corresponding kernel row, the reverse triangle inequality gives

$$
|\sqrt{\rho_A(x,y)}-\sqrt{\rho_B(x,y)}|\leq\sqrt{q(x,y)}. \tag{2}
$$

The sharp one-dimensional kinetic inequality dual to the $\gamma=3/2$ Lieb–Thirring inequality is

$$
\int\rho_\gamma(y)^2\,dy
\leq\frac1{\sqrt3}(\operatorname{Tr}\gamma^3)^{1/2}
\bigl(\operatorname{Tr}(-\partial_y^2)\gamma\bigr)^{1/2}.
$$

Apply it to $\gamma=D(x)^2$. The Hilbert–Schmidt triangle inequality gives

$$
\operatorname{Tr}(-\partial_y^2)D(x)^2
=\|\partial_yD(x)\|_{\mathfrak S^2}^2
\leq 2\operatorname{Tr}(-\partial_y^2)(A(x)+B(x)). \tag{3}
$$

Integrating in $x$, and using Cauchy–Schwarz, (1), and (3), yields

$$
\int_{\mathbb R^2}q^2
\leq\sqrt{\frac23}\,E^{1/2}T^{1/2}.
$$

Combining this with (2) proves the main estimate. Reverse triangle in $L^4$ proves the first consequence. The factorization
$\rho_A-\rho_B=(\sqrt{\rho_A}-\sqrt{\rho_B})(\sqrt{\rho_A}+\sqrt{\rho_B})$
and Holder prove the second.

For the proposed R30 pruning estimate $E=O(\delta^{3/4}T_x)$, with bounded $T$ proportional to the original transverse energy, this transfers to an $O(\delta^{3/32}(T_xT_y)^{1/8})$ error in the fourth root of the quartic density norm. The separately required construction of spatial soliton blocks is not supplied by this lemma.
