# Local-mass replacement for the nonradial BNLS weighted interpolation

Research note, 7 October 2026. This note proves a conditional nonradial result and several symmetry-class consequences. It does **not** prove the unrestricted negative-energy conjecture, and it makes no priority claim for the consequences.

## 1. Equation and the correct exponential defect

Let (N\ge2), (p=2+8/N), and

$$
i u_t=\Delta^2u-|u|^{p-2}u,\qquad
m=\|u\|_2^2,\qquad E=\tfrac12\|\Delta u\|_2^2-\tfrac1p\|u\|_p^p.
$$

The 2026 Dinh manuscript uses the **quartic**, not quadratic, weight

$$
h_R(x)=e^{-|x-c|^4/R^4},\quad
w_R(x)=1-h_R(x),\quad
\nabla\phi_{R,c}(x)=(x-c)h_R(x),\quad
D_{R,c}(u)=\int w_R|D^2u|_F^2.
$$

Here (c\in\mathbb R^N) is fixed. The mass in this note means the squared (L^2) norm. All constants below depend only on dimension unless specified.

## 2. A valid weighted inequality, with no radial hypothesis

For (0<\delta<1/4), define

$$
\mu_{\delta,c}(u)=\sup_{a\ne c}
\int_{B(a,\delta|a-c|)}|u(x)|^2\,dx.
$$

**Proposition.** There is (C_N>0), independent of (u,R,c,\delta), such that every (u\in H^2(\mathbb R^N)) satisfies

$$
\boxed{\quad
\int w_R|u|^p
\le C_N\mu_{\delta,c}(u)^{4/N}
\bigl[D_{R,c}(u)+\delta^{-4}R^{-4}m\bigr].
\quad} \tag{2.1}
$$

### Proof of the local estimate

First, for any ball (B(a,r)), put

$$
m_a=\int_{B(a,4r)}|u|^2,\qquad
H_a=\int_{B(a,4r)}|D^2u|_F^2.
$$

Take smooth cutoffs $\eta=1$ on (B(a,r)), supported in (B(a,2r)), and $\chi=1$ on (B(a,2r)), supported in (B(a,4r)), with derivatives bounded at their natural scales. Integration by parts gives

$$
A^2:=\int\chi^2|\nabla u|^2
=-\Re\int\chi^2\bar u\Delta u
-2\Re\int\chi\bar u\nabla\chi\cdot\nabla u.
$$

Consequently

$$
A^2\le \sqrt N\,m_a^{1/2}H_a^{1/2}+C_Nr^{-1}m_a^{1/2}A,
$$

and absorption and Young's inequality imply

$$
r^{-2}\int_{B(a,2r)}|\nabla u|^2
\le C_N H_a+C_Nr^{-4}m_a.
$$

The product rule therefore gives

$$
\|D^2(\eta u)\|_2^2\le C_N(H_a+r^{-4}m_a),\qquad
\|\eta u\|_2^2\le m_a.
$$

Apply the global mass-critical Gagliardo–Nirenberg inequality

$$
\|f\|_p^p\le C_N\|f\|_2^{8/N}\|D^2f\|_2^2
$$

to (f=\eta u). This proves

$$
\int_{B(a,r)}|u|^p
\le C_Nm_a^{4/N}(H_a+r^{-4}m_a). \tag{2.2}
$$

No gradient norm has been left uncontrolled.

### An explicit covering with constants uniform in $\delta$

By translation set (c=0). On each dyadic annulus

$$
A_j=\{2^j\le |x|<2^{j+1}\},\quad j\in\mathbb Z,
$$

choose a maximal (r_j)-separated family of centers (a_{j,k}\in A_j), where

$$
r_j=\delta 2^j/64.
$$

The balls (B(a_{j,k},r_j)) cover (A_j). The enlarged balls (B(a_{j,k},4r_j)) have overlap bounded by a dimensional constant: within an annulus this follows by packing disjoint balls of radius (r_j/2), and across annuli each point lies in only a bounded number of enlarged radial annuli. These bounds are independent of $\delta$.

Every enlarged ball lies inside (B(a_{j,k},\delta|a_{j,k}|)), so its mass is at most $\mu_{\delta,0}(u)$. On each enlarged ball

$$
w_R(x)\asymp_N w_R(a_{j,k}),
$$

uniformly in all parameters, since (w_R(x)\asymp\min\{|x|^4/R^4,1\}$ and the radii are a small fixed fraction of $|a_{j,k}|$. Moreover

$$
w_R(a_{j,k})r_j^{-4}\le C_N\delta^{-4}R^{-4}.
$$

Multiply (2.2) by (w_R(a_{j,k})), sum over the covering, and use bounded overlap. The Hessian contribution is at most (C_N\mu^{4/N}D_{R,0}$, and the cutoff contribution is at most (C_N\mu^{4/N}\delta^{-4}R^{-4}m$. This proves (2.1). Approximation by smooth functions, or the cutoff argument directly for (H^2), completes the justification.

## 3. A precise conditional finite-time theorem

There is a dimensional (m_*(N)>0) with the following property. Let (u) be a maximal (H^2) solution with (E(u_0)<0). If a fixed center (c) and a fixed $\delta\in(0,1/4)$ satisfy

$$
\sup_{0\le t<T_+}\mu_{\delta,c}(u(t))\le m_*(N), \tag{3.1}
$$

then (T_+<\infty). The same holds backward if (3.1) holds on the backward lifespan.

### Proof, including the closure

Define

$$
V_R(t)=2\Im\int\bar u\,\nabla\phi_{R,c}\cdot\nabla u.
$$

The nonradial parts of the localized biharmonic virial computation give

$$
V_R'\le16E-6D_{R,c}+8\int w_R|u|^p+C_NR^{-4}m. \tag{3.2}
$$

Here the principal Hessian defect has coefficient $-8$; the lower-order linear errors cost at most $2D+C_NR^{-4}m$. The exact nonlinear error is

$$
\frac8{N+4}\int [Nw_R+4s^4e^{-s^4}]|u|^p\le8\int w_R|u|^p,
\quad s=|x-c|/R,
$$

using $s^4e^{-s^4}\le1-e^{-s^4}$. These steps require no symmetry.

Choose (m_*) so that (C_Nm_*^{4/N}\le1/4) in (2.1). Under (3.1), (3.2) implies

$$
V_R'\le16E-4D_{R,c}
+C_NR^{-4}m\bigl(1+\delta^{-4}m_*^{4/N}\bigr).
$$

Choose a single sufficiently large (R), depending on (E,m,\delta,N), to obtain

$$
V_R'\le-8|E|-4D_{R,c}. \tag{3.3}
$$

For completeness, the other needed nonradial estimate follows from (g_R=\sqrt{w_R}$:

$$
\int g_R|\nabla u|^2
=-\Re\int g_R\bar u\Delta u+\tfrac12\int\Delta g_R|u|^2
\le C_Nm^{1/2}D_{R,c}^{1/2}+C_NR^{-2}m.
$$

Since $|\nabla\phi_{R,c}|^4\le C_NR^4w_R$, Cauchy–Schwarz gives

$$
|V_R|\le C_Nm+C_NRm^{3/4}D_{R,c}^{1/4}. \tag{3.4}
$$

Let (y=-V_R). Equation (3.3) gives (y'\ge8|E|+4D$. If a forward global solution existed, (y$ would reach (2C_Nm) in finite time. Subsequently (3.4) gives

$$
D_{R,c}\ge c_NR^{-4}m^{-3}y^4,\qquad
y'\ge c_NR^{-4}m^{-3}y^4.
$$

Integrating $(y^{-3})'\le-3c_NR^{-4}m^{-3}$ contradicts existence for all positive time. This proves the theorem. In particular the proof produces a finite upper bound of the form

$$
T_+\le \frac{(2C_Nm+V_R(0))_+}{8|E|}+C_NR^4.
$$

The constants in this upper bound can be enlarged from those in (3.4); no optimality is claimed.

## 4. An initial-data class preserved by the evolution

The time-uniform hypothesis above is not automatic. Nevertheless it follows from sufficiently dispersed group orbits, giving concrete nonradial classes.

### Finite cyclic symmetry in every even dimension

Let (N=2d), identify $\mathbb R^N=\mathbb C^d$, and let

$$
g(z)=e^{2\pi i/K}z,\qquad K\ge2.
$$

Suppose (u_0(gx)=\chi u_0(x)), where $\chi^K=1$. Rotation and phase invariance plus uniqueness preserve this equivariance. In particular $|u(t,gx)|^2=|u(t,x)|^2$.

For any (x\ne0), the points (g^jx), (0\le j<K), obey

$$
|g^jx-g^\ell x|\ge2|x|\sin(\pi/K),\qquad j\ne\ell.
$$

For $0<\delta<\min\{1/4,\sin(\pi/K)\}$, the (K) balls (B(g^jx,\delta|x|)) are disjoint and have equal mass. Hence

$$
\mu_{\delta,0}(u(t))\le m/K
$$

for every time in the lifespan. Therefore

$$
\boxed{E(u_0)<0,\quad m/K\le m_*(N)
\quad\Longrightarrow\quad T_+,T_-<\infty.}
$$

This permits genuinely nonradial data and nontrivial phase characters. It is a sufficient condition, not a statement that an arbitrary datum can be given a symmetry it does not possess.

### Infinite-orbit symmetry groups

More generally, let a compact subgroup (G\le O(N)) have an infinite orbit (Gx) for every (x\ne0). For each integer (K), there is (d_K>0) such that every unit-vector orbit contains (K) points with pairwise distances at least (d_K). To see this, choose (K) distinct orbit points separately for each unit vector; their separation remains positive in a neighborhood of that vector, and use a finite subcover of the unit sphere.

If the solution density is (G)-invariant, taking $\delta<d_K/2$ gives $\mu_{\delta,0}\le m/K$. Since (K) can be arbitrarily large, (3.1) holds for some fixed $\delta$. Thus negative-energy solutions in such a preserved symmetry class blow up in both time directions, with no restriction on total mass.

The group symmetry must be imposed at the level of the complex initial datum (invariance or a unitary character equivariance) so that it persists; initial density symmetry by itself is not sufficient.

A concrete example for **every (N\ge4)** is (G=O(2)\times O(N-2)). Writing (x=(y,z)), at least one component has norm at least $|x|/\sqrt2$; rotating that component in a two-dimensional plane constructs (K) points with separation at least $\sqrt2|x|\sin(\pi/K)$. This yields a genuine biradial, generally nonradial blow-up class. In even dimensions, simultaneous continuous complex rotation gives another example.

## 5. What negative energy provides, and what it does not

Applying (2.2) to a fixed-scale bounded-overlap covering gives the familiar local-mass estimate

$$
\|u\|_p^p\le C_N\nu_\rho(u)^{4/N}
\bigl(\|D^2u\|_2^2+\rho^{-4}m\bigr),\qquad
\nu_\rho(u)=\sup_a\int_{B(a,C\rho)}|u|^2.
$$

Set (H=\|D^2u\|_2^2>0) and $\rho=(m/H)^{1/4}$. Negative energy implies $\|u\|_p^p>(p/2)H$, and therefore

$$
\nu_\rho(u)\ge c_N>0.
$$

So negative energy forces some mass concentration at the natural scale, at every time. This is a **lower** bound on mass in some ball, whereas the closure needs **upper** bounds in all sufficiently narrow relative balls away from one center. The estimate gives neither one persistent concentration center nor a speed bound for that center, and does not prohibit several separated concentrating components.

For each individual (u\in L^2$, $\mu_{\delta,c}(u)\to0$ as $\delta\downarrow0$. Indeed, handle centers near (c$ by small mass in a small ball, far-away centers by a small spatial tail, and remaining centers by absolute continuity of the mass integral on sets of vanishing volume. The convergence is uniform over any compact subset of (L^2$. Consequently it is uniform on each compact time interval of an (L^2)-continuous solution, but the required $\delta$ may shrink as the time interval grows. Choosing a new $\delta$ for each time interval is not enough for the fixed-(R$ Riccati contradiction.

This is the exact unresolved dynamical step in this route. Negative energy alone has not been shown to supply (3.1), and the static translated-bump counterexample precludes obtaining its effect from an unconditional arbitrarily-small-coefficient weighted interpolation inequality.

### A necessary concentration condition for any global negative-energy solution

**Corollary.** Suppose (T_+=\infty$ and (E(u_0)<0$. For every fixed (c\in\mathbb R^N$, there exist $\delta_n\downarrow0$, $t_n\to\infty$, and $x_n\ne c$ such that

$$
\int_{B(x_n,\delta_n|x_n-c|)}|u(t_n,x)|^2\,dx
\ge \tfrac12m_*(N). \tag{5.1}
$$

**Proof.** For any fixed $\delta\in(0,1/4)$, the contrapositive of §3 gives
$\sup_{t\ge0}\mu_{\delta,c}(u(t))>m_*(N)$; otherwise the solution could not be global. Take, for example, $\delta_n=2^{-n-3}$, and choose (t_n,x_n$ with the ball mass greater than $m_*/2$. No supremum is required to be attained. For any fixed (T<\infty$, the set $\{u(t):0\le t\le T\}$ is compact in (L^2$, so

$$
\lim_{\delta\downarrow0}\sup_{0\le t\le T}\mu_{\delta,c}(u(t))=0.
$$

For clarity, the uniformity follows from a finite (L^2$ net and

$$
|\mu_{\delta,c}(f)-\mu_{\delta,c}(g)|
\le(\|f\|_2+\|g\|_2)\|f-g\|_2,
$$

together with the pointwise-in-(u$ result above. Thus for sufficiently large (n$ the chosen time cannot lie in $[0,T]$. Since (T$ was arbitrary, (t_n\to\infty$. This proves (5.1).

The corollary forces a fixed positive amount of mass into balls arbitrarily narrow relative to their distance from **each fixed center**. It does not exclude the phenomenon: neither the locations nor their speeds are controlled here.

A related consequence is that a global negative-energy solution cannot have a trajectory precompact in (L^2$ after dilation about one fixed center. Indeed, $\mu_{\delta,c}$ is invariant under mass-preserving dilations about (c$, and compactness of the normalized profiles would give precisely the uniform smallness prohibited by (5.1). Allowing unrestricted time-dependent translations is an additional problem and is not covered by this argument.

### Quantitative mass flux does not supply the missing uniformity

For a fixed smooth real cutoff (a(x)=\chi((x-b)/r)$, direct use of the equation and integration by parts twice gives

$$
\frac{d}{dt}\int a|u|^2
=2\Im\int \Delta(a\bar u)\,\Delta u
=2\Im\int \bigl[2\nabla a\cdot\nabla\bar u+(\Delta a)\bar u\bigr]\Delta u.
$$

The nonlinearity makes no contribution. With (H(t)=\|\Delta u(t)\|_2^2$ and $\|\nabla u\|_2\le m^{1/4}H^{1/4}$, this yields

$$
\left|\frac{d}{dt}\int a|u|^2\right|
\le C_\chi\left(r^{-1}m^{1/4}H(t)^{3/4}
+r^{-2}m^{1/2}H(t)^{1/2}\right). \tag{5.2}
$$

Thus mass tightness can be propagated on an interval only with a quantitative bound on the corresponding time integrals of (H^{3/4}$ and (H^{1/2}$, or additional structure. Negative energy and conservation of mass/energy alone give no such upper bounds. In particular using this flux estimate to assert a uniform-in-time localization would be a circular step in a proof intended to rule out global grow-up.

## Source checked

Leonard Dinh, *Finite-Time Blow-Up of Radial Negative-Energy Solutions for the Mass-Critical Biharmonic Nonlinear Schrödinger Equation*, Meta AI Research, 2 October 2026, 20-page manuscript. In particular §§4–6 provide the nonradial multiplier identities used above; the only radial input in the original proof is Proposition 3.1. Official landing page:

https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/

