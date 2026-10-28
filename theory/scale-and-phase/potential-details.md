# Proof details: collapse under a real potential with controlled curvature

Date: 2026-10-10. This is an independent derivation of the potential argument. It records a conditional mathematical theorem, with the precise inputs separated from its conclusions. No historical-priority claim is made here.

## 1. Assumptions and notation

Let a scalar solution on a terminal interval satisfy

$$
i u_t=-\Delta u-|u|^{4/d}u-V(t,x)u,\qquad \|u(t)\|_2^2=M_c=\|Q\|_2^2,
$$

where $-\Delta Q+Q-Q^{1+4/d}=0$. Put

$$
E_0(u)=\tfrac12\|\nabla u\|_2^2-
\frac{d}{2(d+2)}\|u\|_{2+4/d}^{2+4/d},\quad
\rho=|u|^2,\quad J=\operatorname{Im}(\bar u\nabla u).
$$

Assume:

1. (u) is an (H^1) solution on (t<T), with the continuity, momentum, energy, and localized virial identities justified by approximation. The potential is real, locally regular enough for these identities, and may depend on time. No bound on (V_t) is used below.
2. (0\le E_0(u(t))\le C_E<\infty), and the entire density converges narrowly to (M_c\delta_{x_*}) as (t\uparrow T).
3. With (h=T-t),
   $$
   \|\nabla_x^2V(t)\|_{L^\infty}\le K h^{-\alpha},\qquad 0\le\alpha<2.
   \tag{A}
   $$
4. For identifying the limiting scale with (Q), assume a full-mass (Q) profile with an (L^2) error tending to zero and scale bounded above by (Ch). A sufficient quantitative input, available in the R17 applications, is a phase and center such that
   $$
   u(t)=e^{i\theta(t)}\lambda(t)^{-d/2}Q((x-x_c(t))/\lambda(t))+r(t),
   \quad \|r(t)\|_2\le C\lambda(t),\quad
   \|\nabla r(t)\|_2\le C,\quad \lambda(t)\le Ch.
   \tag{B}
   $$

The first part of the theorem, including positivity of the terminal intrinsic energy, does **not** need input (B). The sharper scale error below additionally uses quantitative scalar Gagliardo–Nirenberg stability on a compact range of kinetic normalizations. This is an explicit input, not asserted here for every dimension.

If the affine part of (V) has singular time dependence, the intrinsic conclusions remain valid as long as the local identities are meaningful. A physical limiting momentum requires a separate time-integrability assumption on that affine force. Bounded spatial curvature alone does not provide it.

## 2. Centering and all signs

First, scalar sharp Gagliardo–Nirenberg at mass (M_c), applied after the phase change (u\mapsto e^{ia\vartheta}u), gives

$$
\left|\int J\cdot\nabla\vartheta\right|^2
\le 2E_0(u)\int\rho|\nabla\vartheta|^2.
\tag{1}
$$

Together with $\rho_t+2\operatorname{div}J=0$, this yields the extended unnormalized quadratic transport bound

$$
W_2(\rho(t),\rho(s))\le\int_t^s\sqrt{8E_0(u(r))}\,dr.
\tag{2}
$$

The limiting atom therefore implies finite variance at every preceding time. This does not assume finite variance initially.

Define

$$
P=\int J,\quad b=M_c^{-1}\int x\rho,\quad p=P/M_c,
$$
$$
e=E_0(u)-\frac{|P|^2}{2M_c}\ge0,\qquad
I=\int|x-b|^2\rho.
\tag{3}
$$

The nonnegativity of (e) is sharp scalar Gagliardo–Nirenberg applied after a constant Galilean phase. Direct calculation, with the sign (-Vu) in the equation, gives

$$
b'=2P/M_c=2p,\qquad P'=\int\rho\nabla V,\qquad
E_0'=\int J\cdot\nabla V,
\tag{4}
$$

and consequently

$$
e'=\int(J-p\rho)\cdot\nabla V.
\tag{5}
$$

The sign in both force terms in (4) is positive. Also (P^2\le2M_cE_0$, so (b') is bounded and (b(t)\to x_*).

Set (w(t,z)=e^{-ip(t)\cdot z}u(t,b(t)+z)), allowing an irrelevant additional time-dependent scalar phase. It has zero mean position, zero momentum, and scalar energy (e). Its current is the translated (J-p\rho), and it obeys the usual continuity equation, because (b'=2p). The transformed potential, up to a scalar function of time, is

$$
V(t,b+z)-p'(t)\cdot z.
\tag{6}
$$

This explicitly checks the acceleration term; it cannot be omitted from the equation. It remains real and thus does not modify continuity.

Applying (1) to (w), using the test (V(t,b+z)-\nabla V(t,b)\cdot z), and approximating unbounded tests by cutoffs, gives

$$
|e'|\le\sqrt{2e}\,K h^{-\alpha}\sqrt I,
\qquad
\left|\frac{d}{dt}\sqrt e\right|
\le\frac K{\sqrt2}h^{-\alpha}\sqrt I.
\tag{7}
$$

The square-root statement remains valid at zeros, by applying the estimate to $\sqrt{e+\varepsilon}$ and passing to the limit.

The centered density tends to (M_c\delta_0). Its own transport estimate gives

$$
I(t)\le 8\left(\int_t^T\sqrt{e(r)}\,dr\right)^2.
\tag{8}
$$

Finally the centered virial identity is

$$
I'=4\int(x-b)\cdot(J-p\rho),
$$
$$
I''=16e+4\int\rho(x-b)\cdot\nabla V.
\tag{9}
$$

Since $\int(x-b)\rho=0$, the last integral can equally use $\nabla V(x)-\nabla V(b)$; its absolute value is at most (K h^{-\alpha}I). Formula (9) includes the subtraction (8|P|^2/M_c) from the uncentered virial, which is why (16e), not (16E_0), appears.

## 3. Positive terminal intrinsic energy

Write (q=\sqrt e). Bounded scalar energy and (8) imply (I=O(h^2)). Therefore (7) yields

$$
|q'|=O(h^{1-\alpha}),\qquad
q(t)=q_*+O(h^{2-\alpha}),
\tag{10}
$$

where the terminal limit exists because $\alpha<2$.

Suppose (q_*=0). Integrating (7) toward (T), then using (8), gives

$$
q(t)\le2K\int_t^T(T-s)^{-\alpha}
\int_s^Tq(r)\,dr\,ds.
\tag{11}
$$

If (Q_t=\sup_{t\le r<T}q(r)), then the same inequality at every (s\in[t,T)) implies

$$
Q_t\le\frac{2K}{2-\alpha}h^{2-\alpha}Q_t.
\tag{12}
$$

For sufficiently small (h), this forces (Q_t=0). Equation (8) then forces (I(t)=0), impossible for a nonzero (L^2) density. Hence

$$
e_*:=q_*^2>0,\qquad e(t)=e_*+O(h^{2-\alpha}).
\tag{13}
$$

This argument excludes a vanishing terminal intrinsic energy without an assumed lower bound on it.

The phase estimate gives $|I'|\le4\sqrt{2eI}=O(h)$. Thus (I(T)=I'(T)=0). Integrating (9) twice yields

$$
I''=16e_*+O(h^{2-\alpha}),
$$
$$
I'=-16e_*h+O(h^{3-\alpha}),\qquad
I=8e_*h^2+O(h^{4-\alpha}).
\tag{14}
$$

For uniformly bounded Hessian, $\alpha=0$: (e-e_*=O(h^2)), and the variance remainder is (O(h^4)).

## 4. Conformal transport excludes a collapsing conformal scale

Set (s=h^{-1}) and

$$
v(s,y)=h^{d/2}e^{ih|y|^2/4}w(T-h,hy).
\tag{15}
$$

The coefficient in the chirp gradient is (hy/2), not (y/2). Exact expansion gives

$$
E_0(v)=h^2e+\frac h8I'+\frac18I\ge0,
\tag{16}
$$
$$
\int|y|^2|v|^2=I/h^2,
\quad \int y|v|^2=0,\quad P(v)=0.
\tag{17}
$$

Combining (13)–(14),

$$
0\le E_0(v)\le C s^{-(4-\alpha)},\qquad
\int|y|^2|v|^2=8e_*+O(s^{-(2-\alpha)}).
\tag{18}
$$

The exact moving and conformal transformations preserve the standard continuity equation. Consequently

$$
W_2(|v(s_1)|^2,|v(s_2)|^2)
\le\int_{s_1}^{s_2}\sqrt{8E_0(v(\sigma))}\,d\sigma.
\tag{19}
$$

Its speed is (O(s^{-2+\alpha/2})), which is integrable precisely in the range used here. Thus there is a limit measure $\nu_\infty$ with

$$
W_2(|v(s)|^2,\nu_\infty)=O(s^{-1+\alpha/2}),\quad
\int y\,d\nu_\infty=0,\quad
\int|y|^2d\nu_\infty=8e_*>0.
\tag{20}
$$

Under (B), the conformal density is (L^1)-close to a (Q) density of scale $\mu=\lambda/h$, with bounded scale and bounded center. A subsequence with $\mu\to0$ would have a point-mass narrow limit. The (W_2) convergence in (20) would then force its variance to vanish, contradicting (e_*>0). Every positive limiting scale gives a (Q) density. Its center is zero, and its variance uniquely fixes the scale. Therefore

$$
\nu_\infty(y)=\mu_*^{-d}Q(y/\mu_*)^2,\qquad
\mu_*^2\int|y|^2Q^2=8e_*,\qquad
\frac{\lambda(t)}{T-t}\longrightarrow\mu_*>0.
\tag{21}
$$

In particular, the faster-than-pseudoconformal collapse left open by energy and variance control alone cannot occur under assumption (A).

## 5. Sharper scale error with quantitative scalar stability

Assume quantitative scalar Gagliardo–Nirenberg stability, and normalize the scale convention by

$$
\lambda(t)=\|\nabla Q\|_2/\|\nabla u(t)\|_2.
\tag{22}
$$

The positive scale limit, bounded momentum, and (17) imply upper and lower positive bounds on $\|\nabla v\|_2$. Scalar stability applied to (18) then provides parameters (a(s),\eta(s),\widetilde\mu(s)), with scale bounded above and below, such that

$$
v=e^{i\eta}\widetilde\mu^{-d/2}
Q((y-a)/\widetilde\mu)+r_s,
\qquad \|r_s\|_{H^1}=O(h^{2-\alpha/2}).
\tag{23}
$$

Denote the coherent term by (q_s). The (W_2) bound provides weighted control that (23) alone does not provide. If $\pi$ couples $|v|^2$ with $\nu_\infty$,

$$
\int_{|y|>R}|y|^2|v(y)|^2dy
\le4\int|y-z|^2d\pi+2\int_{|z|>R/2}|z|^2d\nu_\infty.
\tag{24}
$$

Use (R=C|\log h|), with (C) large. The limiting (Q) and the coherent (q_s) have uniformly exponential tails, whereas (20) gives transport cost (O(h^{2-\alpha})). Splitting the residual at (R),

$$
\int|y|^2|r_s|^2
\le R^2\|r_s\|_2^2+
2\int_{|y|>R}|y|^2(|v|^2+|q_s|^2)
=O(h^{2-\alpha}).
\tag{25}
$$

The cross term obeys

$$
\left|\int|y|^2q_s\overline{r_s}\right|
\le\||y|^2q_s\|_2\|r_s\|_2
=O(h^{2-\alpha/2}).
\tag{26}
$$

The zero mean of (v) also gives (a=O(h^{2-\alpha/2})). Combining (18), (25), and (26),

$$
\widetilde\mu-\mu_*=O(h^{2-\alpha}).
\tag{27}
$$

To compare this scale to (22), use the exact kinetic identity

$$
\|\nabla v\|_2^2
=h^2\left(\|\nabla u\|_2^2-|P|^2/M_c\right)
+\frac14I+\frac h4I'.
\tag{28}
$$

The difference between the left side and (h^2\|\nabla u\|_2^2) is (O(h^2)). From (23), its difference from $\|\nabla Q\|_2^2/\widetilde\mu^2$ is (O(h^{2-\alpha/2})). Both are (O(h^{2-\alpha})). Therefore

$$
\boxed{\frac{\lambda(t)}{T-t}=\mu_*+O((T-t)^{2-\alpha}),\qquad
\lambda(t)=\mu_*(T-t)+O((T-t)^{3-\alpha}).}
\tag{29}
$$

For bounded curvature, the physical scale remainder is cubic: $\lambda(t)=\mu_*(T-t)+O((T-t)^3)$. This is a parameter statement, not a bound obtained solely from unweighted (H^1) convergence; the transport-tail step (24) is essential.

## 6. Scope of this independent derivation

- The identities, Volterra positivity, conformal transport, and nondegenerate scale limit hold dimension-independently for the mass-critical power, conditional on the stated solution and profile inputs.
- The sharper quantitative scale uses a specified scalar stability input. It is established for the R17 one- and two-dimensional settings when that input is imported.
- Sections 1–5 of this independent derivation do not by themselves prove a phase equation. The separate projection argument checked in Section 7 below does prove it for the bounded-potential, two-dimensional cubic application.
- No assertion is made that an arbitrary vector background has a uniformly bounded spatial Hessian. Applying the theorem to a coupled system requires proving its effective real potential meets (A).
- The condition $\alpha<2$ is the natural integrability boundary of this argument. The endpoint $\alpha=2$ is not settled by the estimates above.

## 7. Derivation of the companion full statement and phase projection

The full text of [regular-background.md](regular-background.md) was read after completing the preceding derivation. Its Sections 1–8 pass the following independent checks.

For the two-dimensional common-density cubic model, the additional assumption is the explicitly stated uniform (W^{2,\infty}) bound on (S=\sum_{j\ge2}|u_j|^2). It supplies bounded force, bounded curvature, and bounded potential. The R16 energy remainder and R17 full primary concentration are imported inputs; this audit does not reprove them. In particular, uniform secondary (H^1) control alone does not supply this added hypothesis.

For a conformal transformation around the fixed terminal point, with (x_*=0), direct calculation verifies

$$
P(v)=hP(u)+\frac{M_c}{2}b(u),
$$
$$
E_0(v)=h^2e+\frac h8I'+\frac18I+
\frac{|P(v)|^2}{2M_c}.
\tag{30}
$$

Bounded force gives (P(u)=P_*+O(h)) and (b(u)=-2P_*h/M_c+O(h^2)), so (P(v)=O(h^2)). Consequently (E_0(v)=O(h^4)) also holds for this fixed-center conformal field. The terms involving the physical momentum have not been discarded. Its center converges to (y_*=-2P_*/M_c).

The transformed potential is

$$
B(s,y)=s^{-2}S(T-s^{-1},x_*+y/s),\qquad
\|B(s)\|_\infty=O(s^{-2}).
\tag{31}
$$

Let (\Phi(\theta,\mu,a)=e^{i\theta}Q_{\mu,a}), and impose real (L^2) orthogonality of (r=v-\Phi) to the phase, scale, and translation tangent vectors (T_j=\partial_j\Phi). Their real Gram matrix is uniformly invertible when the scale lies in the compact positive interval already proved. These are ordinary manifold tangent projections; no unsupported symplectic invertibility is required.

The evolution is (v_s=i(\Delta v+|v|^2v+Bv)). At a pure profile, its unforced vector field is (i\mu^{-2}\Phi), exactly the phase tangent with coefficient (\mu^{-2}). Differentiating the orthogonality conditions gives

$$
(T_k,T_j)_{\mathbb R}\,\dot z_k
=\bigl(i\mu^{-2}\Phi,T_j\bigr)_{\mathbb R}
+O(\|r\|_{H^1}+\|B\|_\infty)
+O(\|r\|_{H^1}|\dot z|),
\tag{32}
$$

where (z=(\theta,\mu,a)); repeated parameter indices are summed. In the two-dimensional cubic equation, the linearization maps (H^1$ to (H^{-1}), and the nonlinear remainder is bounded by (C(\|r\|_{H^1}^2+\|r\|_{H^1}^3)) there. Pairing against the uniformly smooth localized (T_j) justifies every term. The (Br) term is smaller than the displayed bound. The final coefficient perturbation is absorbed because (r\to0).

Thus the companion estimate is valid:

$$
|\theta'-\mu^{-2}|+|\mu'|+|a'|=O(s^{-2}).
\tag{33}
$$

The previously proved scale rate $\mu-\mu_*=O(s^{-2})$ now yields

$$
\theta(s)=s/\mu_*^2+\theta_*+O(s^{-1}).
\tag{34}
$$

Together with the center rate (a-y_*=O(s^{-1})), this proves the fixed standing-wave (H^1) asymptotic with error (O(s^{-1})). The smoothly selected manifold parameters are differentiable to the degree supplied by the solution; almost-everywhere derivatives suffice for integration. This phase conclusion follows from (31)–(34), not from density convergence alone.

The companion conversion from its modulation scale to the R17 physical kinetic scale is also correct. Equation (28) above supplies a short independent verification. For the curvature-only extension, the (O(h)) conformal mean momentum is enough to contribute only (O(h^2)) to this comparison; a bounded affine force is not silently needed for the width statement.

The companion's warning about the one-dimensional quintic vector model is essential and correct: its primary mixed term is (2S|u_1|^2u_1+S^2u_1), not simply (S u_1). The dimension-independent scalar potential derivation does not automatically close that coupled model.

## 8. Derivation of the regular-background node and energy coefficient

The subsequently added Section 9 of [regular-background.md](regular-background.md) was independently checked in full. Its assumption is stronger than a density bound: every secondary component remains uniformly bounded in (H^k(\mathbb R^2)), (k>3), with finitely many components. Interpolation of the R17 strong (L^2) terminal convergence with this bound gives strong (H^r) convergence for every (r<k), hence strong (H^1) and (C^1) convergence.

The conformal primary residual has (L^2) norm (O(h^2)), and conformal scaling preserves that norm. Pairing its physical expansion with a secondary component and using exact Gram orthogonality gives a remainder (O(h^2)). The core pairing has the two-dimensional Jacobian/amplitude factor (h), so it equals

$$
h e^{i\theta}\left[\mu\!\int Q\right]\overline{u_j(t,x_*)}+O(h^2).
\tag{35}
$$

Uniform Lipschitz bounds give the (O(h^2)) spatial error. Keeping the primary quadratic phase changes the integral by (O(h^2)), since $|e^{-ih|y|^2/4}-1|\le h|y|^2/4$ and the profile has uniform moments. The coefficient $\mu\int Q$ stays strictly positive. Thus

$$
u_j(t,x_*)=O(h),\qquad w_j(x_*)=0.
\tag{36}
$$

The improved (O(h^2)) residual is essential here: dividing the older (O(h)) pairing error by (h) would only yield an (O(1)) value bound.

Equation (36) and uniform Lipschitz bounds yield

$$
S(t,x)\le C(h^2+|x-x_*|^2),\qquad
\int S|u_1|^2=O(h^2).
\tag{37}
$$

The exact energy splitting is

$$
E_{\rm total}=E_1(t)+E_{\rm sec}(U_{\rm sec}(t))-
\frac12\int S|u_1|^2.
\tag{38}
$$

Strong secondary (H^1) convergence makes its energy converge. Therefore the companion coefficient is correct:

$$
e_*=E_{\rm total}-E_{\rm sec}(W)-\frac{|P_*|^2}{2M_c}>0,
\qquad \mu_*^2=\frac{8e_*}{\int|x|^2Q^2}.
\tag{39}
$$

There is also a direct sharper motion estimate under this stronger hypothesis. From (36),

$$
|\nabla S(t,x)|\le C(h+|x-x_*|).
$$

The whole-primary variance estimate and Cauchy–Schwarz then give (P_1'(t)=O(h)). Hence

$$
P_1(t)=P_*+O(h^2),\qquad
b(t)=x_*-\frac{2P_*}{M_c}h+O(h^3).
\tag{40}
$$

The conformal profile center differs from the conformal mean by (O(h^2)), as already proved by the weighted residual argument, so its convergence to (-2P_*/M_c) is also (O(h^2)) in this regular-secondary subcase. These extra conclusions require the component regularity assumption used in this section; they do not follow from a bound on (S) alone.

