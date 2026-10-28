# Exact zero-momentum BNLS: a single-wave spectral reduction

Research continuation, 2026-10-07. This note proves a conditional gluing theorem. It does **not** assert that the additional spectral hypothesis has already been certified for the project's excited traveling wave.

## 1. Equation, known wave, and the remaining target

Consider the four-dimensional cubic equation

$$
i u_t=\Delta^2u-|u|^2u,
\qquad E(u)=\tfrac12\|\Delta u\|_2^2-\tfrac14\|u\|_4^4,
\qquad P(u)=\operatorname{Im}\int\bar u\nabla u.
$$

Assume that a smooth exponentially localized traveling profile $Q_v$ is available, with $0<v<1/2$,

$$
(\Delta^2+1)Q_v+iv\partial_1Q_v-|Q_v|^2Q_v=0,
\qquad E(Q_v)<0.
$$

The project's proposed certified branch has this form. Put $Q_{-v}(x)=Q_v(-x)$, and

$$
R(t,x)=e^{it}S(t,x),\qquad
S(t,x)=Q_v(x-vte_1)+Q_{-v}(x+vte_1).
$$

This sum is even under full inversion. Its defect is exponentially small in every fixed Sobolev norm. The desired exact solution would satisfy
$$
\|u(t)-R(t)\|_{H^2}\longrightarrow0.
$$
Conservation and separation would then give
$$
P(u)=0,\qquad E(u)=2E(Q_v)<0,
\qquad \sup_{t\ge T}\|u(t)\|_{H^2}<\infty.
$$
These are exact conservation identities, not approximate cancellations.

## 2. The extra single-wave hypothesis

Regard complex functions as a real Hilbert space. Set $J=-i$ and
$$
L_v h=(\Delta^2+1)h+iv\partial_1h-2|Q_v|^2h-Q_v^2\bar h,
\qquad A_v=JL_v.
$$

The following hypothesis is stronger and more concrete than merely knowing a finite Morse index.

**Spectral-coercive splitting (SC).** There are a finite-dimensional real vector space $D$, a real matrix $B$, a synthesis map $Z:D\to H^k$, and an analysis map $W:H^2\to D$, such that:

1. $WZ=I$, $A_vZ=ZB$, and $WA_v=BW$ on the generator domain.
2. The basis functions defining $Z$ and the dual functions defining $W$ are smooth and exponentially localized, including their derivatives. It suffices to impose enough derivatives for the $H^6$ argument below, with one additional differentiated generator; assuming all derivatives avoids bookkeeping.
3. On $C=\ker W$, the quadratic form is uniformly positive:
   $$
   \langle L_vh,h\rangle\ge c\|h\|_{H^2}^2
   \quad(h\in C)
   $$
   for some $c>0$.
4. The standard closed realizations of $A_v$ generate the linear flow on $H^2$ and $H^6$. For a fourth-order constant-coefficient skew-adjoint principal part plus smooth bounded real-linear multiplication and a first derivative, these are the usual bounded-perturbation/graph-domain realizations.

The reflected wave inherits the same hypothesis. The matrix $B$ may have positive and negative real parts, imaginary eigenvalues, and Jordan blocks. No sign restriction is imposed on its finite-dimensional dynamics.

Condition (SC) says that all directions which can invalidate positive quadratic energy are captured by finitely many localized modes. It includes the full generalized symmetry space, not just the kernel. Off-axis isolated eigenmodes are natural candidates. Embedded modes of negative Krein signature and threshold effects are reasons not to infer (SC) from a Morse count alone.

## 3. Conditional gluing theorem

**Theorem.** Suppose the profiles above are smooth, exponentially localized, and satisfy (SC). Then there is $T<\infty$ and an exact solution
$$
u\in C([T,\infty);H^6)
$$
of cubic BNLS such that, for some $\gamma>0$,
$$
\|u(t)-R(t)\|_{H^6}\le C e^{-\gamma t}\qquad(t\ge T).
$$
It can be chosen even under inversion. In particular it has exactly zero momentum, strictly negative energy, and a uniformly bounded $H^2$ norm for all forward times. Time translation gives initial time zero.

**There is no lower bound on $v$ in this theorem other than $v>0$.** Its constants and starting time may deteriorate as $v\to0$.

### 3.1 Smooth exponentially small defect

Let $F(z)=|z|^2z$. Each summand solves the equation exactly. The error therefore contains only mixed cubic terms. If derivatives of each profile have tails bounded by $C e^{-a|x|}$, splitting space according to the nearer center and using $|x-vte_1|+|x+vte_1|\ge2vt$ gives, for any fixed number of derivatives and a possibly smaller $a$,
$$
\|iR_t-\Delta^2R+F(R)\|_{H^6}\le A e^{-\kappa t},
\qquad \kappa>0.
$$
One may take a conservative $\kappa<av$. No comparison with an unstable eigenvalue is needed.

### 3.2 Moving finite-dimensional modes

Work after removing the common factor $e^{it}$. The linearization at $S$ is
$$
\partial_t h=\mathcal A(t)h,
\qquad \mathcal A(t)=J\mathcal L(t),
$$
$$
\mathcal L(t)=\Delta^2+1-\mathcal V(t),
\qquad \mathcal V(t)h=2|S|^2h+S^2\bar h.
$$

Translate the two copies of $Z,W$ with the two centers. Their off-diagonal pairings are exponentially small. For sufficiently large $T$, the finite Gram matrix is invertible; multiplying the raw analysis map by its inverse produces maps $Z(t),W(t)$ satisfying $W(t)Z(t)=I$. Let $B_0$ be the block diagonal matrix with the two individual matrices. Direct differentiation, using (SC), gives
$$
\dot Z+ZB_0-\mathcal A Z=\mathcal E_Z(t),
\qquad
\dot W+W\mathcal A-B_0W=\mathcal E_W(t),
$$
where the operator norms of both errors, including the derivatives needed below, are $O(e^{-\kappa t})$. The only new multiplication potentials are those of the distant wave and mixed products. Exponential localization of modes and dual modes is precisely what makes these operator errors exponentially small.

Put $\Pi(t)=I-Z(t)W(t)$. A projected center evolution preserving $\ker W(t)$ is
$$
\partial_t w=\mathcal C(t)w,
\qquad \mathcal C(t)=\mathcal A(t)-Z(t)\mathcal E_W(t),
\qquad W(t)w(t)=0.
$$
Indeed $(Ww)'=B_0Ww$. Its difference from the physical generator is an exponentially small finite-rank operator.

### 3.3 A moving quadratic action with no derivative loss

Choose a smooth real scalar field $b(t,x_1)$ which equals $+v$ near the right center and $-v$ near the left center, with transition width proportional to $vt$. Arrange $|b|\le v$,
$$
\|\partial_x^j b\|_\infty\le C_v t^{-j}\quad(1\le j\le3),
\qquad \|b_t\|_\infty\le C_v/t,
\qquad \|\partial_x b_t\|_\infty\le C_v/t^2.
$$
Set
$$
D_b=b\partial_1+\tfrac12\partial_1b,
\qquad
\mathcal H(t)=\mathcal L(t)+iD_b.
$$
The added term is the Hessian of localized velocity times momentum. It agrees with the traveling action Hessian near each wave. Away from the waves the form $\Delta^2+1+iD_b$ is positive when $v<1/2$.

An IMS partition into the two cores and the exterior, whose derivatives are $O_v(t^{-1})$, together with (SC), yields for all sufficiently large times
$$
c_0\|w\|_{H^2}^2\le\langle\mathcal H(t)w,w\rangle
\le C_0\|w\|_{H^2}^2,
\qquad W(t)w=0.
$$
For clarity, the localized single-wave constraints are only exponentially violated: each dual mode is concentrated where its core cutoff is identically one, and the global constraint is exactly zero. The errors are absorbed. Fourth-order IMS errors are bounded quadratic forms of size $O_v(t^{-1})$ on $H^2$.

For the unprojected linearized equation the exact quadratic-form derivative is
$$
\frac d{dt}\langle\mathcal Hh,h\rangle
=\langle[\dot{\mathcal H}+D_b\mathcal L-\mathcal L D_b]h,h\rangle.
$$
Thus the operator in brackets is
$$
iD_{b_t}+[D_b,\Delta^2]-\{\mathcal V_t+b\partial_1\mathcal V\}.
$$
The last braces are exponentially small: in each core the potential moves at exactly the local value of $b$, while the transition region lies in exponential tails. The commutator is a bounded fourth-order quadratic form. In particular, writing $D_b=b\cdot\nabla+\frac12\operatorname{div}b$ in vector notation,
$$
\begin{aligned}
\big|\langle h,[D_b,\Delta^2]h\rangle\big|
\le C(&\|\nabla b\|_\infty\|h\|_{H^2}^2
+\|\nabla^2b\|_\infty\|h\|_{H^1}\|h\|_{H^2}\\
&+\|\nabla^3b\|_\infty\|h\|_2\|h\|_{H^2}).
\end{aligned}
$$
To verify the absence of derivative loss, use skew-adjointness of $D_b$: the form equals $-2\operatorname{Re}\langle\Delta h,\Delta D_bh\rangle$; the term $D_b\Delta h$ cancels, leaving only the displayed derivatives of $b$.

The finite-rank correction in $\mathcal C$ contributes only an exponentially small form error. Consequently its center propagator $U_C(t,s)$ satisfies
$$
\|U_C(t,s)\|_{H^2\to H^2}
\le C\max(t/s,s/t)^K
\le C(1+|t-s|)^K,
\qquad t,s\ge T\ge1.
$$

### 3.4 Higher regularity without an algebra error

Using $H^2$ alone for a cubic Banach-algebra contraction in dimension four would be incorrect. We work in $H^6$, which is an algebra.

The center estimate upgrades to $H^6$ with a larger polynomial exponent. Here are the details. On the center bundle put $\mathcal D(t)=\Pi(t)\mathcal A(t)\Pi(t)$. This differs from $J\Delta^2$ by smooth bounded multiplication and finite-rank operators with smooth localized range and dual range. Elliptic graph norm equivalence gives
$$
\|w\|_{H^6}\asymp\|w\|_{H^2}+\|\mathcal D(t)w\|_{H^2}
$$
uniformly for large $t$. If $z=\mathcal D(t)w$, then
$$
z_t=\mathcal C(t)z+
\{\mathcal D_t+[\mathcal D,\mathcal C]\}w.
$$
The braces define a uniformly bounded operator $H^2\to H^2$: the time derivative of the principal part is zero; derivatives of the potential are bounded multipliers; and every remaining commutator is finite rank with smooth range and dual range. In Duhamel retain the sharper ratio bound $\max(t/s,s/t)^K$; ratios multiply exactly along an ordered time interval, so the time integral costs only one additional power. This gives
$$
\|U_C(t,s)\|_{H^6\to H^6}
\le C(1+|t-s|)^{K+1}.
$$
The finite-dimensional modes enjoy the same regularity automatically.

### 3.5 The Green operator and why small velocity is allowed

Write $h=Za+w$. The exact linear equation becomes a direct sum of the fixed finite system $a'=B_0a$ and the center equation, plus exponentially small bounded coupling. Split the finite matrix into stable, unstable, and imaginary-axis generalized eigenspaces. Let $\alpha>0$ be smaller than the minimum nonzero absolute real part of its eigenvalues; if there are no hyperbolic modes choose any $\alpha>0$. Polynomial factors in hyperbolic Jordan blocks can be absorbed by decreasing $\alpha$.

Choose
$$
0<\gamma<\min(\kappa,\alpha).
$$
For stable modes integrate forcing forward from $T$, with zero initial stable component. For unstable and center modes integrate backward from infinity. The center integral converges because the forcing has the exponential weight. In the norm
$$
\|h\|_{X_\gamma}=\sup_{t\ge T}e^{\gamma(t-T)}\|h(t)\|_{H^6},
$$
this direct-sum Green operator has a finite norm bounded by
$$
G\le C\left\{
\frac1{\alpha-\gamma}+\frac1{\alpha+\gamma}
+\int_0^\infty(1+r)^m e^{-\gamma r}\,dr\right\},
$$
where $m$ dominates the center growth exponents. Terms absent from the splitting are omitted. If $m$ is chosen integral, the last integral is
$\sum_{j=0}^m\binom mj j!/\gamma^{j+1}$.

The exponentially small linear coupling has norm at most $C e^{-\kappa T}$ on this space. Taking $T$ large enough gives an inverse by a Neumann series. Thus the full two-center linearized operator has a bounded right inverse on $X_\gamma$.

This proves the relevant point: a large unstable eigenvalue is handled by the backward unstable integral. It need not be dominated by the much smaller interaction decay rate. The smallness cost is instead a large starting separation/time.

### 3.6 Nonlinear completion

In the equation for the correction $h$, the defect is $O(e^{-\kappa t})$, and the nonlinear remainder satisfies, on a bounded $H^6$ ball,
$$
\|\mathcal N(h)\|_{H^6}\le L\|h\|_{H^6}^2,
$$
$$
\|\mathcal N(h)-\mathcal N(k)\|_{H^6}
\le L(\|h\|_{H^6}+\|k\|_{H^6})\|h-k\|_{H^6}.
$$
Let the full Green operator norm be $G_1$. Choose $T$ so large that
$$
2G_1A e^{-\kappa T}\le(4G_1L)^{-1}.
$$
The Green fixed-point map is then a contraction on the ball of radius $2G_1A e^{-\kappa T}$ in $X_\gamma$. It gives an exact solution. Reflection averaging makes the linear right inverse preserve inversion-even functions, and the defect and nonlinear map preserve this symmetry. The fixed point is therefore even and has exactly zero momentum.

Finally, separation and $H^2$ convergence make mass, momentum, and energy asymptotically additive. Conservation converts their limits into exact values. The $H^2$ norm is bounded on the tail by the approximation and on every compact initial interval by continuity. This completes the conditional theorem.

## 4. What this proves, and the precise missing certificate

This argument reduces the zero-momentum extension to a **single-wave spectral-coercive splitting with localized dual modes**. It does not require a new dispersive estimate for the full two-center problem, a large dimensionless relative speed, or linear stability of the excited wave.

The existing static inverse and Morse certificates do not yet contain (SC). In particular they do not list the complete Hamiltonian root spaces or exclude pathological nonpositive-energy continuous components. Lin--Zeng's Hamiltonian trichotomy theory is a relevant tool, but its hypotheses and its block decomposition must be checked; its abstract title is not a substitute for the required coercive invariant complement.

For the project's radial zero-speed profile, the positive $L_-$ sectors of angular degree two and three, combined with one negative $L_+$ eigenvalue per channel, already suggest respectively 9 and 16 real unstable directions. A complete treatment of the low angular sectors, zero-mode unfolding at $v\ne0$, and any embedded internal modes remains necessary. The anticipated total Morse count alone does not prove a count of 31 real unstable eigenvalues.

### 4.1 A finite-index exhaustion criterion that would remove the conditional gap

There is a sharper way to discharge (SC) without classifying every internal mode. Suppose, at one fixed small nonzero velocity, the following statements are all rigorously established:

* $n^-(L_v)=36$, the kernel consists exactly of phase and four translations, and the free essential quadratic form is strictly positive.
* The five-parameter traveling-wave action Hessian $d''(\omega,\mathbf v)$ is positive definite. The corresponding generalized symmetry space therefore has dimension ten; its five parameter derivatives have quadratic-form matrix $-d''$, its five symmetry generators span the kernel, and the associated symplectic pairing is nondegenerate.
* The unstable spectral subspace of $A_v$ has real dimension at least 31.

Then the unstable dimension is exactly 31 by the Hamiltonian index bound. The full stable-plus-unstable root space has dimension 62 and negative quadratic index 31. Its symplectic direct sum with the ten-dimensional generalized symmetry space exhausts the 36 negative directions and the entire kernel. Let $D$ be this 72-dimensional space and let $C$ be its symplectic orthogonal. The latter is invariant and is also $L_v$-orthogonal to $D$. The form on $C$ is positive; Fredholmness and the positive essential part strengthen this to uniform $H^2$ coercivity. This is the required complement in (SC).

The hyperbolic root vectors decay exponentially because their eigenvalues lie off the imaginary essential spectrum. Symmetry and parameter derivatives decay exponentially by weighted elliptic estimates for the free positive symbol $|\xi|^4+1-v\xi_1$. The dual basis can be chosen as finite linear combinations of $J$ times the basis vectors, using the inverse symplectic Gram matrix, so it decays exponentially as well. This establishes the localization part of (SC).

The required exponential estimates admit a direct tail argument: conjugation by a sufficiently small smooth exponential weight is a small form perturbation of the free elliptic operator (or the off-axis matrix resolvent); cut off beyond a large radius so the decaying profile potential is small enough to absorb. The cutoff forcing is compactly supported. Uniform bounds for truncated weights and passage to the limit give exponential $H^2$ control; elliptic bootstrap gives the higher derivatives.

Companion analysis has reduced the remaining question to low angular channels. One sufficient route would be 31 rigorously enclosed unstable directions at zero speed, which persist to small nonzero speed. A weaker route would be 30 persistent directions together with odd Hamiltonian index 31; nonreal hyperbolic quartets contribute even real dimensions. Current radial numerical diagnostics favor a genuine hyperbolic quartet, which would contribute two directions, but its nonselfadjoint spectral enclosure has not yet been certified. **These are sufficient implications, not a report that the companion calculation has succeeded.**

## 5. A competing radiation route and its sharp quantitative limitation

A single traveling wave plus outgoing radiation could also produce $P=0$. This is useful only if an exact asymptotic solution is constructed; negative-energy zero-momentum initial data by themselves are elementary and are not an advance on the target.

For any radiation profile $f$, Plancherel and Holder give the sharp kinetic lower bound
$$
|P(f)|\le M(f)^{3/4}\|\Delta f\|_2^{1/2},
\qquad
\tfrac12\|\Delta f\|_2^2\ge\frac{|P(f)|^4}{2M(f)^3}.
$$
Thus cancelling $|P(Q_v)|\asymp v$ while spending only $O(v^2)$ positive radiative energy requires mass at least of order $v^{2/3}$, hence $H^2$ norm at least of order $v^{1/3}$. This is much larger than the wave's $O(v)$ profile perturbation. Moving the packet farther away reduces interaction, but not this global norm cost.

The bound is asymptotically attained by a broad packet whose Fourier mass is concentrated near a single small frequency. Taking carrier $k=v^\theta$, $1/3<\theta<1$, and mass $m\asymp v/k$, gives momentum $O(v)$, mass $O(v^{1-\theta})$, and kinetic energy $O(v^{1+3\theta})=o(v^2)$. Its group speed is $O(k^3)=o(v)$. A wave outrunning the packet therefore has favorable geometry. However, an unknown center-stable neighborhood may shrink faster than $v^{1/3}$, so this observation does not complete that alternative construction. A spatially separated wave-operator theorem would be needed to exploit geometry instead of a uniform global smallness assumption.

## 6. Primary sources consulted

1. Z. Lin and C. Zeng, *Instability, index theorem, and exponential trichotomy for Linear Hamiltonian PDEs*, arXiv:1703.04016. The abstract and theorem development establish finite-dimensional hyperbolic directions and at most polynomial center growth under their Hamiltonian hypotheses. <https://arxiv.org/abs/1703.04016>
2. R. Cote and S. Le Coz, *High-speed excited multi-solitons in nonlinear Schrodinger equations*, arXiv:1007.3034; J. Math. Pures Appl. 96 (2011), 135--166. This is a second-order NLS theorem with a large relative-speed requirement, not a ready-made theorem for the current BNLS. <https://arxiv.org/abs/1007.3034>
3. Z. Wang, *Multi solitary waves for a fourth order nonlinear Schrodinger type equation*, Nonlinear Analysis: Real World Applications 37 (2017), 287--308. The equation contains derivative nonlinearities of the vortex-filament/Hasimoto model; it is not pure cubic BNLS.
4. R. Parker and A. Aceves, *Multi-pulse solitary waves in a fourth-order nonlinear Schrodinger equation*, arXiv:2009.01647. This concerns one-dimensional spatial multi-pulse standing profiles, not outgoing opposite-speed waves in four dimensions.

No directly applicable published theorem for the exact four-dimensional small-speed excited pair was found in the searches for this note. This bounded search statement does not claim exhaustive worldwide novelty of the conditional argument.
