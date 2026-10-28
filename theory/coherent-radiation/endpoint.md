# Negative-energy traveling-wave threshold: endpoint analysis

Date: 2026-10-18. Scope: the first research class, principally the pure mass-critical BNLS equation. This note advances the Fourier-moment and parameter geometry; it does not decide attainment of the minimum traveling-wave mass.

## 1. Setting and the unresolved endpoint

Let

$$
 \Delta^2U+\omega U+i v\cdot\nabla U-|U|^{8/N}U=0,
 \quad U\in H^2(\mathbb R^N)\setminus\{0\}.
$$

Write

$$
 M=\|U\|_2^2,\quad A=\|\Delta U\|_2^2,
 \quad E=\frac12A-\frac1{2+8/N}\|U\|_{2+8/N}^{2+8/N},
 \quad P=\int\xi|\widehat U(\xi)|^2d\xi.
$$

The established Pohozaev and group-velocity identities are

$$
 v\cdot P=8E,\qquad
 \omega M=\frac4N A+\left(6-\frac8N\right)E,
 \qquad
 vM=4\int|\xi|^2\xi|\widehat U(\xi)|^2d\xi.
$$

Define

$$
 M_{\rm tr}=\inf\{M(U):U\text{ is an exact traveling profile},\ E(U)<0\}.
$$

R10 proves a uniform gap above the sharp GN mass and the following compactification: after fixing A=1, a minimizing sequence either converges strongly to a negative-energy minimizer, or has energy tending to zero and decomposes strongly into finitely many zero-energy exact profiles with common limiting parameters. That dichotomy remains valid and unresolved.

The three negative action directions of R10 are directions in the ambient function space. They do not produce nearby exact profiles. Decreasing mass by an amplitude change does not preserve the profile equation, so it cannot eliminate the negative-energy attainment alternative.

## 2. A sharp universal Fourier-moment identity

Let $\nu$ be a probability measure on $\mathbb R^N$ with finite fourth moment. Set

$$
 \mu=\int\xi\,d\nu,\qquad q=\int|\xi|^2\xi\,d\nu,
 \qquad a_4=\int|\xi|^4d\nu.
$$

Then the exact identity

$$
\begin{aligned}
 a_4+8\mu\cdot q
 =\int\Big[&\big(|\xi|^2+4\mu\cdot\xi-8|\mu|^2\big)^2\\
 &+16\big(|\mu|^2|\xi|^2-(\mu\cdot\xi)^2\big)\Big]d\nu
\end{aligned}
$$

implies

$$
 \boxed{\ \mu\cdot q\ge-\frac18a_4.\ }
$$

Proof: expansion of the integrand gives

$$
 |\xi|^4+8(\mu\cdot\xi)|\xi|^2
 -64|\mu|^2(\mu\cdot\xi)+64|\mu|^4.
$$

The last two terms cancel on integration because $\int\xi d\nu=\mu$. Both original summands are nonnegative.

If $\nu$ is absolutely continuous and nonzero, the inequality is strict. When $\mu=0$, its left residual is $a_4>0$. When $\mu\ne0$, equality forces $\xi$ to be parallel to $\mu$ and to solve

$$
 |\xi|^2+4\mu\cdot\xi-8|\mu|^2=0.
$$

The support must therefore lie in the two points

$$
 \xi_\pm=(-2\pm2\sqrt3)\mu,
$$

which is impossible for an absolutely continuous probability measure.

### Sharpness as a probability-moment inequality

Take $|e|=1$, $\xi_\pm=(-2\pm2\sqrt3)e$, and weights

$$
 p_+=\frac{3+2\sqrt3}{4\sqrt3},\qquad
 p_-=\frac{2\sqrt3-3}{4\sqrt3}.
$$

Then

$$
 \mu=e,\qquad q=-8e,\qquad a_4=64,
$$

and equality holds. Replacing these atoms by smooth, disjoint narrow densities gives absolutely continuous measures approaching equality. Such densities can be realized as normalized $|\widehat U|^2$ with smooth compactly supported Fourier amplitudes.

Thus the moment constant $1/8$ is optimal, including over Fourier densities of smooth functions. This does **not** establish optimality among exact nonlinear traveling profiles.

## 3. Consequences for every exact pure-BNLS traveling profile

Apply the identity to $d\nu=|\widehat U|^2d\xi/M$. Then $\mu=P/M$, $q=v/4$, and $a_4=A/M$. Consequently

$$
 \boxed{\ E(U)>-\frac1{16}A(U).\ }
$$

In fact there is an exact positive remainder:

$$
 \boxed{\ A+16E
 =\int\left[\big(|\xi|^2+4\mu\cdot\xi-8|\mu|^2\big)^2
 +16\big(|\mu|^2|\xi|^2-(\mu\cdot\xi)^2\big)\right]
 |\widehat U|^2d\xi>0.\ }
$$

This needs only H2 regularity and the already proved profile identities; no spatial moment, nondegeneracy, symmetry or spectral-gap assumption is needed.

For negative-energy profiles and $2\le N<12$, substituting in the second Pohozaev identity yields

$$
 \frac{3(12-N)}{8N}A<\omega M<\frac4N A.
$$

Hence $\omega>0$ automatically, and

$$
 \frac{N\omega}{4}<\frac AM<\frac{8N\omega}{3(12-N)},\qquad
 -\frac{N\omega M}{6(12-N)}<E<0.
$$

The group-velocity bound further gives

$$
 |v|<4\left(\frac{8N\omega}{3(12-N)}\right)^{3/4}.
$$

At N=12, $\omega>0$ is still strict, but this argument gives no uniform positive lower bound for $\omega M/A$. At N=1, negative energy directly gives $4A<\omega M<33A/8$. No positive-frequency conclusion is inferred here for N>12.

In the dimension N=4 of the original validated construction, these formulas are particularly simple:

$$
 \boxed{\quad \omega<\frac AM<\frac43\omega,
 \qquad -\frac1{12}\omega M<E<0,
 \qquad |v|<4\left(\frac43\omega\right)^{3/4}.\quad}
$$

For N=3:

$$
 \frac34\omega<\frac AM<\frac89\omega,
 \qquad -\frac1{18}\omega M<E<0.
$$

These are universal necessary parameter restrictions for the exact profiles, not a numerical description of one branch.

### Effect on the threshold problem

In dimensions 3 and 4, every negative-energy profile can be normalized to frequency one. Under that normalization, A/M stays in a fixed compact interval and the velocity is uniformly bounded. A mass-minimizing sequence therefore cannot lose compactness by letting its frequency collapse relative to kinetic scale. This improves the parameter normalization of R10, but does not exclude either endpoint alternative.

### A stronger frequency-speed restriction in four dimensions

There is a second sharp moment identity. Let $q\ne0$, put

$$
 e=q/|q|,\qquad d=(2|q|)^{1/3}.
$$

Expansion shows

$$
\begin{aligned}
 &\int\left[\big(|\xi|^2-d e\cdot\xi-d^2/2\big)^2
 +d^2\big(|\xi|^2-(e\cdot\xi)^2\big)\right]d\nu\\
 &\hspace{2em}=a_4+2\mu\cdot q-\frac34d^4.
\end{aligned}
$$

Indeed the polynomial expands to
$ |\xi|^4-2d(e\cdot\xi)|\xi|^2+d^3(e\cdot\xi)+d^4/4$, and $d^3=2|q|$.
Thus

$$
 \boxed{\ a_4+2\mu\cdot q\ge\frac3{2^{2/3}}|q|^{4/3}.\ }
$$

For absolutely continuous probability measures the inequality is strict, because equality forces support on the two points $d(1\pm\sqrt3)e/2$. The constant is sharp for probability measures: select these two points with weights

$$
 p_+=\frac{\sqrt3-1}{2\sqrt3},\qquad
 p_-=\frac{\sqrt3+1}{2\sqrt3}.
$$

They have $\mu=0$, $q=d^3e/2$, and $a_4=3d^4/4$. Smooth approximation yields sharpness over smooth Fourier densities. Equality is not asserted for nonlinear profiles.

For N=4, the profile identities imply $\omega=a_4+2\mu\cdot q$ and $q=v/4$. Every exact profile therefore satisfies

$$
 \boxed{\quad \omega>\frac3{2^{10/3}}|v|^{4/3},
 \qquad |v|<\frac{4\sqrt2}{3^{3/4}}\omega^{3/4}.
 \quad}
$$

The first bound includes v=0, where directly $\omega=a_4>0$. This statement does not require negative energy. The speed coefficient is approximately 2.48161, improving the rougher bound above.

The same frequency bound is not the positivity condition for the free symbol $|\xi|^4+\omega-v\cdot\xi$. That condition would require the stronger inequality $\omega>3(|v|/4)^{4/3}$. No Fredholm spectral gap is inferred from the new necessary condition.

### Negative-energy velocity bound in every dimension

Writing $a_2=\int|\xi|^2d\nu$, Cauchy–Schwarz gives

$$
 |q-a_2\mu|^2
 =\left|\int(|\xi|^2-a_2)\xi\,d\nu\right|^2
 \le a_2(a_4-a_2^2).
$$

If $\mu\cdot q<0$, the left side is strictly larger than $|q|^2$, while maximizing the right side over a2 yields

$$
 |q|^2<\frac2{3\sqrt3}a_4^{3/2}.
$$

Thus every negative-energy pure-BNLS profile satisfies the dimension-independent improvement

$$
 \boxed{\ |v|<4\left(\frac4{27}\right)^{1/4}(A/M)^{3/4}.\ }
$$

This bound and the preceding N=4 frequency-speed bound have numerically equal coefficients, but apply to different right-hand scales, A/M and omega, respectively. They should not be conflated.

## 4. What negative-energy attainment would force

Suppose a minimizer $U_*$ with $E(U_*)<0$ exists, and suppose it belongs to a C1 family $U_{\omega,v}$ on an open parameter neighborhood; let its reduced action be C2 and assume the established critical charge-scaling covariance. These are extra hypotheses about an actual profile family, not automatic consequences of the profile equation.

Negative energy persists in an open neighborhood. By minimality,

$$
 M_\omega(U_*)=0,\qquad D_vM(U_*)=0.
$$

Let $d=S_{\omega,v}(U_{\omega,v})$, $H=d''$, and $B=D_vP$. Since $d_\omega=M/2$ and $d_v=-P/2$, equality of mixed derivatives gives

$$
 P_\omega=-D_vM=0.
$$

Differentiating the momentum scaling law gives, for general homogeneous degree m,

$$
 m\omega P_\omega+(m-1)Bv=P.
$$

Therefore

$$
 \boxed{\quad (m-1)Bv=P,\qquad H(1,0,\ldots,0)^T=0.\quad}
$$

If B is invertible, the bordered-charge scalar of R10 must vanish:

$$
 \kappa=P^TB^{-1}P-(m-1)v\cdot P=0.
$$

In the pure quartic isotropic case $P=p(c)e$, c=|v|>0, this becomes

$$
 \boxed{\quad 3c p'(c)=p(c)<0.\quad}
$$

Thus a negative-energy minimizing profile cannot occur at a point where this smooth charge Hessian is invertible. If the exact-profile solution set is singular instead, the smooth-family hypothesis is precisely what fails. Excluding both possibilities would decide nonattainment; R10 does not do so.

### Why the established identities do not already exclude such a point

This can be checked without guessing a PDE solution. In the quartic one-speed charge algebra, let

$$
 d(\omega,c)=\omega D(c\omega^{-3/4}),\qquad
 D(q)=3+(q-1)+\frac16(q-1)^2-\frac16(q-1)^3.
$$

Define M=2d_omega, P=-2d_c, and E=cP/8. These charges obey the critical scaling and first-law identities exactly. At (omega,c)=(1,1),

$$
 M=\frac92,\quad P=-2,\quad E=-\frac14,\quad
 B=-\frac23,\quad M_c=0,\quad M_{cc}=\frac76>0.
$$

Here the subscript c denotes the speed derivative, not the GN critical mass. There is a strict local minimum of mass in the dimensionless speed while energy remains negative; scaling supplies the neutral direction. Also B is invertible and kappa=0. In N=4, the associated algebraic kinetic energy is A=M-4E=11/2 and respects E>-A/16.

This construction is only a consistency example for the charge identities. It is not an exact PDE profile or a counterexample to endpoint nonattainment. Its role is to show concretely that Pohozaev, scaling, the first law and the new moment bound alone cannot rule out an interior negative-energy mass minimum.

## 5. Precise remaining obstacle

To prove that the threshold is necessarily attained only at zero energy, one needs a new global property of the actual nonlinear profile set: for example, a proved absence of negative-energy charge-turning minima (including singular branches), or a mass-decreasing continuation through every negative-energy profile. Three ambient negative Hessian directions do not provide this continuation.

An equally meaningful alternative outcome would be a validated negative-energy turning branch with a local mass minimum, followed by a global lower-mass exclusion. That would establish genuine negative-energy attainment instead. Current results do not distinguish the two possibilities.

The concrete new result of this note is the sharp Fourier-moment identity and its universal negative-energy/frequency/speed restrictions. The actual minimum-mass endpoint remains open.
