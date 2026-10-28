# Time-averaged kinetic control, intrinsic spreading, and quantitative grow-up for BNLS

Research note, 7 October 2026. This is a purely analytic extension of `round4_escape_theory.md`. No numerical profile, spectral certification, or traveling-wave construction is used. The new step is an endpoint-selection argument that removes every a priori pointwise-in-time kinetic bound. The interaction virial itself is inherited from the fourth-order virial literature, in particular Komada's Proposition 5.2; no priority claim is made for that functional.

## 1. Setup and principal conclusions

Consider a standard strong solution on its maximal forward lifespan of

\[
 i\partial_tu=\Delta^2u-|u|^{8/N}u,\qquad u(t)\in H^2(\mathbb R^N),\quad N\ge1.
\]

Write

\[
 M=\|u\|_2^2>0,\quad E=\tfrac12\|\Delta u\|_2^2-
 \tfrac1{2+8/N}\|u\|_{2+8/N}^{2+8/N}<0,\quad
 P=\operatorname{Im}\int\bar u\nabla u=0.
\]

For the principal theorems assume the solution exists globally forward. Define

\[
 K(t)=\|\Delta u(t)\|_2,\quad h(t)=1+K(t)^2,\quad
 \Lambda=16M|E|,\quad \theta=\min\{4/N,1/4\}>0,
\]

\[
 d_R(t)=M^{-2}\iint_{|x-y|>R}|u(t,x)|^2|u(t,y)|^2\,dx\,dy\in[0,1].
\]

The results below show the following.

1. Bounded time averages of \(1+\|\Delta u\|_2^2\) alone suffice for intrinsic linear-scale spreading at a fixed positive density of ordinary time. Arbitrarily large narrow kinetic spikes are permitted; no higher time moment or uniform-integrability assumption is needed.
2. The proof first obtains a kinetic-weighted separation estimate, then uses the mass-transport equation to show that spatial separation cannot exist only during arbitrarily short spikes. The transport step closes the first-moment endpoint. Higher time moments give a second, sometimes sharper quantitative density estimate.
3. A uniformly mass-tight global solution modulo arbitrary translations must have kinetic energy averages diverging to infinity, uniformly over starting times. A prescribed algebraic localization modulus gives an explicit polynomial lower rate. No prior kinetic bound is used in this conclusion.
4. A finite-window theorem quantifies the alternative without any global bound at all.

All conclusions are necessary conditions for global solutions. They do not construct zero-momentum negative-energy solutions or prove that every such solution blows up.

## 2. The instantaneous estimate with its kinetic dependence exposed

Use the cutoff \(\phi_R\) and interaction virial from the previous note:

\[
 I_R(t)=2\iint |u(t,y)|^2\nabla\phi_R(x-y)\cdot
             \operatorname{Im}(\bar u(t,x)\nabla u(t,x))\,dx\,dy.
\]

There are constants \(A,B,C>0\), depending only on \(N,M\) and the fixed cutoff, such that for every \(R\ge1\), in integrated form on every compact time interval,

\[
 |I_R(t)|\le A R h(t)^{1/4},                                      \tag{2.1}
\]

\[
 I_R'(t)\le-\Lambda+B R^{-2}h(t)^{1/2}+C h(t)d_R(t)^\theta.          \tag{2.2}
\]

Here the constants do **not** depend on \(\sup_tK(t)\). To see this explicitly, put

\[
 G=M^{1/4}K^{1/2},\qquad H_R=K+cG/R+c\sqrt M/R^2.
\]

The exact fourth-order commutator and the mass equation give the previous note's estimates before taking any temporal supremum. The derivative-of-cutoff terms are bounded by

\[
 C_MR^{-2}(K+1)\le C'_M R^{-2}h^{1/2}.
\]

The nonlinear pair tail is at most

\[
 C_M H_{2R}^2d_R^{\min(4/N,1)}\le C'_M h\,d_R^\theta.
\]

The cross-flux tail is at most

\[
 C_M K^{3/2}H_{2R}^{1/2}d_R^{1/4}
 \le C'_M (K^2+K^{7/4}+K^{3/2})d_R^{1/4}
 \le C''_M h\,d_R^\theta.
\]

Finally, \(|I_R|\le C_M R K^{1/2}\le A R h^{1/4}\). This proves (2.1)--(2.2). For nonzero momentum the additional exact term is \(-8P\cdot W(t)\), where \(W=\operatorname{Im}\int\Delta u\nabla\bar u\); see Section 8.

The localization and approximation justification is unchanged from the previous note: on each finite interval a strong global \(H^2\) solution has a finite local \(H^2\) bound. The virial identity is obtained by smoothing and strong \(H^2\) approximation on that interval. The constants displayed above are then kept as functions of \(K(t)\), rather than replaced by a global supremum.

## 3. Low-kinetic endpoints: the basic finite-window inequality

Let \(J=[S,S+T]\), and put

\[
 H_J=\frac1T\int_Jh(t)\,dt\ge1.
\]

There exist \(a\in[S,S+T/4]\) and \(b\in[S+3T/4,S+T]\) with

\[
 h(a),h(b)\le4H_J,\qquad b-a\ge T/2.
\]

Indeed, if either end quarter had \(h>4H_J\) everywhere, its contribution alone would exceed \(TH_J\). Continuity of \(h\) removes any ambiguity about endpoint selection.

Integrate (2.2) over \([a,b]\), estimate the endpoint values by (2.1), enlarge the nonnegative integrals to \(J\), and use Jensen for \(h^{1/2}\). With \(A_0=2\,4^{1/4}A\),

\[
 \boxed{\quad
 \frac\Lambda2\le
 A_0\frac{R H_J^{1/4}}{T}
 +B\frac{H_J^{1/2}}{R^2}
 +\frac CT\int_Jh(t)d_R(t)^\theta\,dt,
 \qquad R\ge1.\quad}                                           \tag{3.1}
\]

This estimate uses no global kinetic hypothesis and is valid on every finite time interval inside the lifespan. It is the main new reduction. A large kinetic value at a specified window endpoint no longer spoils the estimate, because suitable nearby endpoints are selected from the solution itself.

## 4. Finite-window grow-up or spreading, with explicit exponents

Fix \(1<p<\infty\), let \(p'=p/(p-1)\), and define

\[
 H_{p,J}=\left(\frac1T\int_Jh(t)^p\,dt\right)^{1/p}\ge1.
\]

Since \(H_J\le H_{p,J}\), (3.1) remains valid when its two explicit occurrences of \(H_J\) are replaced by \(H_{p,J}\). Put

\[
 a_0=\frac\Lambda{8A_0},\qquad
 L=\max\left\{a_0^{-1},\sqrt{\frac{8B}{\Lambda a_0^2}}\right\},\qquad
 \varepsilon_0=\min\left\{\frac12,\frac\Lambda{4C}\right\}>0.
\]

**Theorem 4.1.** For each window \(J=[S,S+T]\), one of the following holds:

\[
 H_{p,J}>(T/L)^2,                                                \tag{4.1}
\]

or, with

\[
 R_J=a_0T H_{p,J}^{-1/4},\qquad
 \delta_J=2^{-1/(\theta p')}
                 (\varepsilon_0/H_{p,J})^{1/\theta},\qquad
 \eta_J=\tfrac12(\varepsilon_0/H_{p,J})^{p'},
\]

\[
 |\{t\in J:d_{R_J}(t)\ge\delta_J\}|\ge\eta_JT.                   \tag{4.2}
\]

At all of those times, simultaneously for every center \(x_0\in\mathbb R^N\),

\[
 \int_{|x-x_0|>R_J/2}|u(t,x)|^2\,dx\ge\frac{\delta_JM}{2}.         \tag{4.3}
\]

**Proof.** If (4.1) fails then \(T\ge L H_{p,J}^{1/2}\), hence \(R_J\ge1\). The first two errors in (3.1) are each at most \(\Lambda/8\), so

\[
 \frac1T\int_Jh\,d_{R_J}^\theta\,dt\ge\frac\Lambda{4C}.
\]

Hölder gives

\[
 \left(\frac1T\int_Jd_{R_J}^{\theta p'}\,dt\right)^{1/p'}
 \ge\frac\Lambda{4CH_{p,J}}
 \ge\frac{\varepsilon_0}{H_{p,J}}.
\]

The contribution from \(d_{R_J}<\delta_J\) to this last average, before taking its \(1/p'\) power, is at most \(\tfrac12(\varepsilon_0/H_{p,J})^{p'}\); the integrand is everywhere at most one. Thus (4.2) follows. Finally,

\[
 d_{2r}(t)\le\frac2M\int_{|x-x_0|>r}|u(t,x)|^2\,dx
\]

for every center, because a pair at distance greater than \(2r\) has at least one point outside that ball. This proves (4.3). \(\square\)

The alternative (4.1) concerns an averaged curvature energy, not a pointwise claim at all times. If the averaged curvature energy remains controlled, the radius is proportional to \(T\) and the escaped mass and time fractions are fixed. If it grows, (4.2) gives the exact deterioration of all three quantities; it is not legitimate to keep a fixed escaped fraction without an additional hypothesis.

**Corollary 4.2 (ordinary-time ballistic spreading from averaged kinetic control).** Suppose for some \(p>1,H_0<\infty,T_*\),

\[
 \sup_{S\ge0,\ T\ge T_*}
 \frac1T\int_S^{S+T}(1+\|\Delta u(t)\|_2^2)^p\,dt\le H_0^p.       \tag{4.4}
\]

Then there are \(c,\delta,\eta,T_0>0\) such that every \(S\ge0,T\ge T_0\) satisfies

\[
 |\{t\in[S,S+T]:d_{cT}(t)\ge\delta\}|\ge\eta T.
\]

The all-centers mass conclusion (4.3) follows. One can take \(c=a_0H_0^{-1/4}\), \(\delta=2^{-1/(\theta p')}(\varepsilon_0/H_0)^{1/\theta}\), \(\eta=\tfrac12(\varepsilon_0/H_0)^{p'}\), and \(T_0=\max(T_*,LH_0^{1/2})\). This uses monotonicity of \(d_R\) in \(R\).

If (4.4) is assumed only for the prefix intervals \([0,T]\), the same conclusion holds on each sufficiently long prefix interval. No uniform statement over arbitrary starting times is then asserted.

## 5. The first-moment endpoint: transport turns one separated time into an interval

First record the weighted estimate, which follows directly from the virial inequality. We then strengthen it to ordinary time density using mass transport, without any additional time integrability.

**Theorem 5.1.** Suppose

\[
 H_J\le H_0
\]

on a family of sufficiently long intervals \(J=[S,S+T]\). There are \(c,\delta,q>0\), independent of the interval, such that

\[
 \int_{\{t\in J:d_{cT}(t)\ge\delta\}}h(t)\,dt\ge qT.             \tag{5.1}
\]

Consequently these separated states account for at least \(q/H_0\) of the total \(h(t)dt\)-measure of the window.

**Proof.** Choose \(c=a_0H_0^{-1/4}\) as above and take \(T\) large enough to absorb the cutoff error. Equation (3.1) gives

\[
 \frac1T\int_Jh(t)d_{cT}(t)^\theta\,dt\ge Q,
 \qquad Q=\frac\Lambda{4C}>0.
\]

Replace \(Q\) by \(\widetilde Q=\min(Q,H_0)\), which preserves the bound, and choose \(\delta^\theta=\widetilde Q/(2H_0)\). If \(A_J=\{d_{cT}\ge\delta\}\), then

\[
 \widetilde Q T\le\delta^\theta\int_Jh+\int_{A_J}h
 \le\tfrac12\widetilde Q T+\int_{A_J}h.
\]

Thus (5.1) holds with \(q=\widetilde Q/2\). \(\square\)

Taken alone, the weighted estimate gives the following concentration implication: if \(|A_J|/T\to0\) along such a sequence of windows, then for every fixed kinetic threshold \(B_0\),

\[
 \liminf\frac1T\int_Jh(t)\mathbf1_{h(t)>B_0}\,dt\ge q.
\]

Indeed, the portion of \(\int_{A_J}h\) on \(h\le B_0\) is at most \(B_0|A_J|=o(T)\). The transport argument below shows that ordinary-time separation at a slightly smaller spatial radius actually persists: the wave cannot hide that spatial separation entirely in short kinetic spikes. This is a stricter conclusion than the weighted estimate by itself.

**Corollary 5.2 (uniform integrability is sufficient).** Suppose the family of time-normalized kinetic densities is uniformly integrable:

\[
 \sup_J\frac1{|J|}\int_Jh<\infty,\qquad
 \lim_{B_0\to\infty}\sup_J\frac1{|J|}\int_Jh\mathbf1_{h>B_0}=0.    \tag{5.2}
\]

Then the ordinary-time conclusion of Corollary 4.2 holds on that family of long intervals, without assuming any \(L^p\) moment. To prove this, choose \(B_0\) so the second expression in (5.2) is at most \(q/2\). Equation (5.1) implies

\[
 qT\le B_0|A_J|+qT/2,
\]

hence \(|A_J|\ge qT/(2B_0)\). A uniform bound on the averages of any superlinear Young function \(\Phi(h)\), with \(\Phi(s)/s\to\infty\), is one sufficient way to verify (5.2). This remains a valid alternative proof, but the next theorem makes the extra assumption unnecessary.

### 5.3 The mass-transport modulus

Choose a smooth radial function \(\psi\) with \(0\le\psi\le1\), \(\psi(z)=0\) for \(|z|\le1/2\), and \(\psi(z)=1\) for \(|z|\ge1\). Define

\[
 F_R(t)=M^{-2}\iint\psi((x-y)/R)\rho(t,x)\rho(t,y)\,dx\,dy,
 \qquad \rho=|u|^2.
\]

Then

\[
 d_R(t)\le F_R(t)\le d_{R/2}(t).                                 \tag{5.3}
\]

**Lemma 5.3 (kinetic-budget transport continuity).** There is a constant \(D>0\), depending only on \(M,N,\psi\), such that on every finite interval \(J\), for all \(s,t\in J\),

\[
 |F_R(t)-F_R(s)|
 \le D\left[
 R^{-1}\left(\int_JK^2\right)^{3/4}|t-s|^{1/4}
 +R^{-2}\left(\int_JK^2\right)^{1/2}|t-s|^{1/2}
 \right].                                                       \tag{5.4}
\]

**Proof.** The mass equation tested against a real bounded smooth function \(f\) is

\[
 \int f\rho_t
 =2\operatorname{Im}\int(\Delta f)\bar u\Delta u
 +4\operatorname{Im}\int\nabla f\cdot(\Delta u\nabla\bar u).
\]

Its right side has absolute value at most

\[
 2\|\Delta f\|_\infty M^{1/2}K
 +4\|\nabla f\|_\infty M^{1/4}K^{3/2}.
\]

Differentiate the two factors of \(\rho\) in \(F_R\); symmetry gives twice the same expression. With \(f(x)=\psi((x-y)/R)\), integrate the bound against \(\rho(y)/M^2\). Thus

\[
 |F_R'(t)|\le D(R^{-1}K(t)^{3/2}+R^{-2}K(t)).                    \tag{5.5}
\]

Integrating and applying Hölder with exponents \((4/3,4)\) and \((2,2)\) proves (5.4). Smoothing and strong \(H^2\) approximation justify the integrated identity for the stated solution class. \(\square\)

The key exponent is \(3/2<2\): the transport flux is lower order than the kinetic budget. Consequently an arbitrarily high kinetic spike with bounded integrated \(K^2\) cannot instantaneously move a fixed mass fraction a distance comparable with the full window length.

### 5.4 Ordinary-time spreading from the first kinetic moment alone

**Theorem 5.4 (first-moment endpoint).** Suppose that for some \(H_0<\infty,T_*\),

\[
 \sup_{S\ge0,\ T\ge T_*}
 \frac1T\int_S^{S+T}(1+\|\Delta u(t)\|_2^2)\,dt\le H_0.           \tag{5.6}
\]

Then there are \(c,\delta_*,\eta,T_0>0\), depending only on \(N,M,|E|,H_0\) and the cutoffs, such that every \(S\ge0,T\ge T_0\) satisfies

\[
 |\{t\in[S,S+T]:d_{cT}(t)\ge\delta_*\}|\ge\eta T.                \tag{5.7}
\]

At those same times, every ball of radius \(cT/2\) misses at least \(\delta_*M/2\) mass. The good set contains an interval of length \(\eta T\); this is stronger than merely having that measure.

**Proof.** From Theorem 5.1 obtain constants \(c_0,\delta>0\) and at least one \(t_0\in J\) such that \(d_{c_0T}(t_0)\ge\delta\). Put \(R=c_0T\). By (5.3), \(F_R(t_0)\ge\delta\). Formula (5.4), using \(\int_JK^2\le H_0T\), gives, when \(|t-t_0|\le\eta T\),

\[
 |F_R(t)-F_R(t_0)|
 \le D\left(c_0^{-1}H_0^{3/4}\eta^{1/4}
            +c_0^{-2}H_0^{1/2}T^{-1}\eta^{1/2}\right).
\]

Choose \(T_0\ge1\) and \(0<\eta\le1/2\) so that the right side is at most \(\delta/2\), uniformly for \(T\ge T_0\). Then

\[
 d_{R/2}(t)\ge F_R(t)\ge\delta/2
\]

on \(J\cap[t_0-\eta T,t_0+\eta T]\). This intersection contains an interval of length \(\eta T\), even if \(t_0\) is a window endpoint. Set \(c=c_0/2\) and \(\delta_*=\delta/2\). The all-centers assertion again follows from the pairwise mass bound. \(\square\)

As before, the hypothesis restricted to prefix windows gives the conclusion on prefix windows. More generally, the theorem applies to any family of long windows on which the same first-moment bound holds.

**Theorem 5.5 (no-prior-bound endpoint alternative).** There exist constants \(L,a_0,c_\delta,c_\eta>0\), depending only on \(N,M,|E|\) and the cutoffs, such that, with \(H_J=T^{-1}\int_Jh\), every finite window inside the lifespan satisfies either

\[
 H_J>(T/L)^2,
\]

or, for an interval of times of length at least

\[
 c_\eta H_J^{-4(1+1/\theta)}T,
\]

one has

\[
 d_{(a_0/2)T H_J^{-1/4}}(t)\ge c_\delta H_J^{-1/\theta}.          \tag{5.8}
\]

**Proof.** Assume \(T\ge L H_J^{1/2}\), with \(L\) from Section 4 increased to at least one, and set \(R=a_0TH_J^{-1/4}\). Equation (3.1) implies \(T^{-1}\int_Jh d_R^\theta\ge Q=\Lambda/(4C)\). With \(b_0=\min\{1/2,Q/2\}>0\), there is \(t_0\in J\) with

\[
 d_R(t_0)\ge\delta_J=(b_0/H_J)^{1/\theta}.
\]

Otherwise the weighted integral would be at most \(b_0<Q\). For \(|t-t_0|\le\eta T\), (5.4) gives

\[
 |F_R(t)-F_R(t_0)|
 \le D\left(a_0^{-1}H_J\eta^{1/4}
           +a_0^{-2}H_JT^{-1}\eta^{1/2}\right)
 \le D_0H_J\eta^{1/4},
\]

using \(T\ge1\) and \(\eta\le1\). Choose

\[
 \eta=c_\eta H_J^{-4(1+1/\theta)},\qquad
 c_\eta=\min\left\{\frac12,
       \left(\frac{b_0^{1/\theta}}{2D_0}\right)^4\right\}.
\]

Then the last bound is at most \(\delta_J/2\). On the resulting interval, \(d_{R/2}\ge F_R\ge\delta_J/2\), proving (5.8) with \(c_\delta=b_0^{1/\theta}/2\). \(\square\)

## 6. Cesàro grow-up forced by uniform mass localization

Assume that the global orbit is uniformly tight in mass modulo arbitrary translations:

\[
 \lim_{R\to\infty}\sup_{t\ge0}\inf_{a\in\mathbb R^N}
 \frac1M\int_{|x-a|>R}|u(t,x)|^2\,dx=0.                          \tag{6.1}
\]

No continuity or bounded velocity of the chosen centers is assumed. By the pair bound, (6.1) implies

\[
 \mu(R):=\sup_{t\ge0}d_R(t)\longrightarrow0.
\]

**Theorem 6.1 (uniform long-window kinetic grow-up).** Under (6.1),

\[
 \boxed{\quad
 \lim_{T\to\infty}\inf_{S\ge0}
 \frac1T\int_S^{S+T}\|\Delta u(t)\|_2^2\,dt=+\infty.
 \quad}                                                        \tag{6.2}
\]

**Proof.** Otherwise there exist \(T_n\to\infty\), \(S_n\ge0\), and a fixed \(H_0\) with \(H_{J_n}\le H_0\). Choose \(R=cT_n\) with \(c>0\) so small that the first term on the right of (3.1) is at most \(\Lambda/8\). The second tends to zero. The final term is at most

\[
 CH_0\mu(cT_n)^\theta\longrightarrow0.
\]

This contradicts the positive left side of (3.1). \(\square\)

This is stronger than merely ruling out a bounded \(H^2\) orbit: it rules out any sequence of arbitrarily long low-average-kinetic windows. It does not imply that \(K(t)\to\infty\) pointwise; downward excursions may remain.

**Theorem 6.2 (quantitative rate from algebraic mass tails).** Suppose, for some \(q\in(0,2]\) and \(D<\infty\),

\[
 \sup_{t\ge0}\inf_a\frac1M\int_{|x-a|>R}|u(t,x)|^2\,dx
 \le D R^{-q},\qquad R\ge1.                                    \tag{6.3}
\]

Then there are constants \(c_1>0,T_1<\infty\) such that for every \(S\ge0,T\ge T_1\),

\[
 \frac1T\int_S^{S+T}\|\Delta u(t)\|_2^2\,dt
 \ge c_1 T^{\frac{4q\theta}{4+q\theta}}.                         \tag{6.4}
\]

**Proof.** The pairwise tail satisfies \(\mu(R)\le D_1 R^{-q}\) for \(R\ge1\), with a larger constant covering \(1\le R<2\). Set \(\alpha=q\theta\in(0,1/2]\). Choose

\[
 R=L_1H_J^{1/\alpha},
\]

where \(L_1\ge1\) is so large that \(BL_1^{-2}\le\Lambda/8\) and \(CD_1^\theta L_1^{-\alpha}\le\Lambda/8\). Then

\[
 BH_J^{1/2}R^{-2}
 =BL_1^{-2}H_J^{1/2-2/\alpha}\le\Lambda/8,
\]

and

\[
 C H_J\mu(R)^\theta\le CD_1^\theta L_1^{-\alpha}\le\Lambda/8.
\]

Equation (3.1) therefore yields

\[
 \frac\Lambda4\le\frac{A_0L_1}{T}H_J^{1/4+1/\alpha},
\]

or \(H_J\ge cT^{4\alpha/(4+\alpha)}\). For sufficiently large \(T\), subtracting the one in \(H_J=1+T^{-1}\int_JK^2\) only halves the constant. This proves (6.4). \(\square\)

The range \(q\le2\) is emphasized because (6.3) can then hold while all variances are infinite; thus the argument is not a disguised finite-variance virial proof. For \(q>2\), uniform finite centered variance follows and the familiar unlocalized dilation identity provides a stronger estimate under its moment-persistence hypotheses; see Section 7.

## 7. Relation to the elementary finite-variance tradeoff

For completeness, suppose the centered second moment exists and the unlocalized dilation identity is justified, for example by sufficient smoothness and weighted decay on each compact time interval. Let

\[
 V(t)=\inf_a\int|x-a|^2|u(t,x)|^2\,dx,\qquad
 J(t)=2\operatorname{Im}\int x\cdot\bar u\nabla u.
\]

Since \(P=0\), \(J\) is independent of the spatial origin. The standard identity and Cauchy--Schwarz give

\[
 J(t)=J(0)+16Et,\qquad
 |J(t)|^2\le4M^{1/2}V(t)K(t).
\]

Thus

\[
 V(t)K(t)\ge\frac{(J(0)-16|E|t)^2}{4M^{1/2}}.                   \tag{7.1}
\]

Uniform variance forces \(K(t)\gtrsim t^2\). This is a straightforward consequence of the classical dilation identity and is included for comparison, not claimed as a new theorem. The results in Sections 3--6 instead require neither finite moments nor precompactness in \(H^2\).

## 8. Nonzero momentum and mass-supercritical powers

### 8.1 Averaged transport defect

For arbitrary conserved \(P\), replace \(-\Lambda\) in (2.2) by

\[
 -F(t),\qquad F(t)=16M|E|+8P\cdot W(t),\qquad
 W(t)=\operatorname{Im}\int\Delta u(t)\nabla\bar u(t).
\]

Every argument remains valid if all sufficiently long subintervals have a uniformly positive average of \(F\). The selected interval \([a,b]\) is itself long, so the same forcing estimate applies. This is an averaged flux condition, not a claim that momentum can be removed by a Galilean transformation; the fourth-order equation lacks that invariance.

A directly checkable sufficient condition can use only the first kinetic time moment. Suppose \(H_J\le H_0\) on all sufficiently long windows and

\[
 \Delta_*:=16M|E|-8|P|M^{1/4}H_0^{3/4}>0.                       \tag{8.1}
\]

Select endpoints from the first and last \(\varepsilon\)-fractions of a window instead of quarters, where \(0<\varepsilon<1/4\) and \(2\varepsilon\Lambda\le\Delta_*/2\). Their kinetic values are at most \(H_0/\varepsilon\). Since

\[
 |W(t)|\le M^{1/4}K(t)^{3/2},\qquad
 \int_J K^{3/2}\le T H_0^{3/4},
\]

the integrated forcing on the selected middle interval is at least

\[
 \Lambda(1-2\varepsilon)T-8|P|M^{1/4}H_0^{3/4}T
 \ge\tfrac12\Delta_*T.
\]

The weighted spreading theorem and the first-moment ordinary-time spreading theorem follow with modified constants: the transport modulus does not use \(P=0\). This extends the previous pointwise kinetic flux criterion to first-moment time-averaged control.

### 8.2 Mass-supercritical, energy-subcritical nonlinearities

For \(\beta\ge8/N\), with \(\beta<8/(N-4)\) when \(N\ge5\), the same reduction works for \(iu_t=\Delta^2u-|u|^\beta u\). Set

\[
 a=N\beta/4\ge2,\quad
 h_\beta(t)=1+K(t)^a,\quad
 \Lambda_\beta=2N\beta M|E_\beta|,\quad
 \theta_\beta=\min\{1-\beta(N-4)/8,1/4\}>0.
\]

The one-particle virial has main term

\[
 2N\beta E_\beta-(N\beta-8)K^2\le2N\beta E_\beta.
\]

The nonlinear pair tail is bounded by \(C h_\beta d_R^{\theta_\beta}\), the cross-flux tail by the same quantity, the endpoints by \(AR h_\beta^{1/(2a)}\), and the cutoff error by \(BR^{-2}h_\beta^{1/a}\). Therefore, with \(H_J=|J|^{-1}\int_Jh_\beta\),

\[
 \frac{\Lambda_\beta}{2}\le
 A_0\frac{RH_J^{1/(2a)}}T+
 B\frac{H_J^{1/a}}{R^2}+
 \frac C T\int_Jh_\beta d_R^{\theta_\beta}.                     \tag{8.2}
\]

Consequently:

- bounded first averages of \(h_\beta\) give both kinetic-weighted and ordinary-time ballistic spreading: they imply bounded first averages of \(K^2\), so the transport argument in Theorem 5.4 applies;
- bounded averages of \(h_\beta^p\), \(p>1\), give the additional explicit Hölder-based quantitative density estimate;
- uniform mass tightness forces the long-window averages of \(K^a\) to diverge;
- the finite-window radius becomes \(R\asymp T H_{p,J}^{-1/(2a)}\), and its alternative is \(H_{p,J}\gtrsim T^a\);
- an algebraic tail \(d_R\lesssim R^{-q}\) with \(q\theta_\beta\le2a\) gives the lower rate \(H_J\gtrsim T^{2a q\theta_\beta/(2a+q\theta_\beta)}\), by the same optimization.

These statements follow from (8.2) exactly as in the complete mass-critical proofs above. The energy-critical endpoint is excluded because the mass-tail exponent vanishes there.

## 9. What is inherited, and what has been established in this note

The fourth-order dilation commutator is standard; Boulenger--Lenzmann, *Blowup for biharmonic NLS*, arXiv:1503.01741, is a primary source. Komada, *Scattering of group-invariant solutions below the ground state for the fourth-order NLS*, arXiv:2609.33381v1, Section 5, uses the interaction functional and momentum-flux term under orbit-precompactness hypotheses. The preceding project note supplied a one-sided mass-tail inequality and a bounded-orbit spreading consequence.

The present note exposes the kinetic dependence, selects controlled endpoints using time averages, and proves the finite-window estimate (3.1). The mass-transport modulus (5.4) then closes the first kinetic moment endpoint, without a uniform-integrability assumption. Consequences include ordinary-time averaged-control spreading and uniform long-window Cesàro grow-up under mass localization. These are actual deductions with complete proofs, independent of the project's computer-assisted traveling waves. A web search on 7 October 2026 located the cited antecedents but is insufficient to certify worldwide priority for each precise formulation; no such priority is asserted here.

Primary source checked directly this turn:

- https://arxiv.org/html/2609.33381v1, in particular Section 5 and Proposition 5.2.
- The previous note records direct examination of https://arxiv.org/pdf/1503.01741, commutator equations (3.7)--(3.9).
