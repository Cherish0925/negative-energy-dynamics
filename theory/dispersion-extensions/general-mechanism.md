# General mass-critical traveling-wave criterion, including noninteger powers

Research note, 2026-10-07. This note proves an analytic **conditional criterion**. It does not assert that the required stationary state and negative inverse pairing exist in every dimension. In the ongoing project, the verified four-dimensional cubic example is a separate input; numerical candidates in other dimensions are not supplied by this theorem.

## 1. The result for pure biharmonic NLS

Let $N\geq1$, $\alpha=8/N$, and consider
$$
 i\partial_tu=\Delta^2u-|u|^\alpha u,\qquad
 E(u)=\frac12\|\Delta u\|_2^2-\frac1{2+\alpha}\|u\|_{2+\alpha}^{2+\alpha}.
$$
All spaces are on $\mathbb R^N$. Complex Banach spaces below are regarded as real Banach spaces. Put $Z=H^2$, with real dual $Z^*=H^{-2}$.

**Biharmonic criterion.** Suppose $Q\in H^2$ is a real, inversion-even, nonzero distributional solution of
$$
 \Delta^2Q+\omega_0Q-|Q|^\alpha Q=0,\qquad \omega_0>0. \tag{1.1}
$$
Define the form operators
$$
 L_+=\Delta^2+\omega_0-(1+\alpha)|Q|^\alpha,\qquad
 L_-=\Delta^2+\omega_0-|Q|^\alpha.
$$
Assume
$$
 \ker(L_+:H^2_{\mathrm{even}}\to H^{-2}_{\mathrm{even}})=\{0\},
 \qquad
 \ker(L_-:H^2_{\mathrm{odd}}\to H^{-2}_{\mathrm{odd}})=\{0\}. \tag{1.2}
$$
Here even and odd mean under full inversion $x\mapsto-x$, not separate reflection in each coordinate. Set
$$
 I_{jk}=\big\langle\partial_jQ,L_-^{-1}\partial_kQ\big\rangle,
 \qquad 1\leq j,k\leq N. \tag{1.3}
$$
The inverse is on the real odd sector. Initially the pairing is $H^{-2},H^2$ duality; it is also an ordinary $L^2$ pairing after the regularity argument below. If the real symmetric matrix $I$ has a negative direction $e^TIe<0$, then for every sufficiently small nonzero real $a$ there is $Q_{ae}\in H^4\cap L^\infty$ such that
$$
 u_a(t,x)=e^{i\omega_0t}Q_{ae}(x-aet),\qquad t\in\mathbb R, \tag{1.4}
$$
is a global strong solution, has constant finite $H^2$ norm, and satisfies
$$
 E(Q_{ae})=\frac14a^2e^TIe+o(a^2)<0. \tag{1.5}
$$
These profiles are therefore counterexamples, in the dimension in which the hypotheses are established, to the unconditional negative-energy finite-time-blowup assertion.

There is a local real $C^1$ branch for all vector velocities near zero. With
$$
 P_j(f)=\operatorname{Im}\int\overline f\,\partial_j f,
$$
it satisfies
$$
 E(Q_v)=\frac{v\cdot P(Q_v)}8,\qquad
 Q_v=Q-i\sum_kv_kL_-^{-1}\partial_kQ+o_{H^2}(|v|),
$$
$$
 P(Q_v)=2Iv+o(|v|),\qquad E(Q_v)=\frac14v^TIv+o(|v|^2). \tag{1.6}
$$
Negative energy forces $P(Q_v)\ne0$, so these profiles cannot be radial about any point: a radial $H^2$ profile has zero momentum.

The assumptions can be weakened to the corresponding symmetry sectors for one velocity direction, as specified in Section 4. For example, radial $Q$, axial spatial symmetry, and real-even/imaginary-odd longitudinal parity suffice for the one-direction conclusion. No stability assumption is used.

## 2. Energy-space differentiability in every dimension

The correct general construction is $H^2\to H^{-2}$. An $H^4\to L^2$ construction based on a Banach algebra would not give a dimension-independent proof. High regularity composition theorems are unnecessary.

More generally let $m\geq1$, $s=m/2$, and
$$
 \alpha=\frac{2m}{N},\qquad p=2+\alpha,\qquad Z=H^s.
$$
The embedding $Z\hookrightarrow L^p$ holds for every $N$. When $N>m$,
$$
 2<p=\frac{2(N+m)}N<\frac{2N}{N-m}.
$$
When $N=m$, the critical Sobolev space embeds in every finite $L^p$; when $N<m$, it embeds into $L^\infty$ and, by interpolation, the required finite $L^p$.

For $F(z)=|z|^\alpha z$, as a map $\mathbb R^2\to\mathbb R^2$,
$$
 DF(z)w=|z|^\alpha w+\alpha|z|^{\alpha-2}z\operatorname{Re}(\overline zw),
 \qquad DF(0)=0. \tag{2.1}
$$
This derivative is continuous for every $\alpha>0$. With $\beta=\min\{1,\alpha\}$,
$$
 \|DF(z)-DF(w)\|\leq C_\alpha|z-w|^\beta
       (|z|+|w|)^{\alpha-\beta}. \tag{2.2}
$$
For $\alpha\leq1$, split into $ |z-w|\geq\frac12\max\{|z|,|w|\}$, where homogeneity proves the bound, and its complement, where a segment derivative bound
$C(|z|+|w|)^{\alpha-1}|z-w|$ implies (2.2). For $\alpha\geq1$ the same argument gives the weighted Lipschitz estimate.

Hölder's inequality gives
$$
 \|DF(u)-DF(v)\|_{\mathcal L(L^p,L^{p'})}
 \leq C_\alpha\|u-v\|_p^\beta(\|u\|_p+\|v\|_p)^{\alpha-\beta},
 \quad p'=\frac p{1+\alpha}. \tag{2.3}
$$
Indeed the multiplying coefficient lies in $L^{p/\alpha}$, and $1/p'=\alpha/p+1/p$. Integration along a segment now proves the Fréchet remainder estimate and hence
$$
 F:L^p\longrightarrow L^{p'},\qquad F:Z\longrightarrow Z^*
 \quad\text{are real }C^1. \tag{2.4}
$$
Their derivatives are locally Hölder of exponent $\beta$. This proof never differentiates the nonlinearity twice.

For BNLS, $N>8$ gives $0<\alpha<1$. The nonlinearity is then generally not $C^2$ at zero, but (2.4) remains valid, and the implicit-function theorem needs only $C^1$. Neither an analytic branch nor an $O(|v|^4)$ energy remainder is asserted for general noninteger powers. The remainder $o(|v|^2)$ suffices for a strict sign conclusion.

## 3. General positive homogeneous dispersion

Let $h:\mathbb R^N\to[0,\infty)$ be a real even homogeneous symbol such that
$$
 h(\lambda\xi)=\lambda^mh(\xi),\qquad
 c|\xi|^m\leq h(\xi)\leq C|\xi|^m,\qquad m\geq1. \tag{3.1}
$$
The variational and implicit-function arguments require only these bounds and the stated symmetries. For the strong-solution conclusion, also assume that $h$ is smooth on the unit sphere, hence smooth away from zero with homogeneous derivative bounds. This includes $h(\xi)=|\xi|^m$ and positive elliptic homogeneous differential symbols.

Write $D=-i\nabla$. Consider
$$
 i\partial_tu=h(D)u-|u|^\alpha u,\qquad \alpha=\frac{2m}N. \tag{3.2}
$$
Using a unitary Fourier transform, put
$$
 E(u)=\frac12\int h(\xi)|\widehat u(\xi)|^2\,d\xi
       -\frac1{2+\alpha}\int|u|^{2+\alpha},\quad M(u)=\|u\|_2^2,
$$
$$
 P_j(u)=\int\xi_j|\widehat u(\xi)|^2\,d\xi. \tag{3.3}
$$
Because $m\geq1$, momentum is an absolutely convergent continuous quadratic form on $Z=H^{m/2}$, and its real derivative is
$$
 DP_j(u)=-2i\partial_ju=2D_ju\quad\text{in }Z^*. \tag{3.4}
$$
Indeed $\partial_j:Z\to Z^*$ is bounded, since
$$
 \sup_\xi\frac{|\xi|}{1+|\xi|^m}<\infty.
$$
This is one reason for requiring $m\geq1$. The present energy-space argument makes no claim for $0<m<1$.

Let $Q\in Z$ be real, even, nonzero and solve
$$
 h(D)Q+\omega_0Q-|Q|^\alpha Q=0,\qquad\omega_0>0. \tag{3.5}
$$
Set $L_+=h(D)+\omega_0-(1+\alpha)|Q|^\alpha$ and $L_-=h(D)+\omega_0-|Q|^\alpha$, as bounded form operators $Z\to Z^*$.

The assertions of Section 1 then hold with $H^2,H^4,1/4,1/8$ replaced by $H^{m/2},H^m,1/m,1/(2m)$, respectively:
$$
 \boxed{E(Q_v)=\frac{v\cdot P(Q_v)}{2m}},\qquad
 \boxed{D_vP(Q_v)|_{v=0}=2I},\qquad
 \boxed{E(Q_v)=\frac1m v^TIv+o(|v|^2)}. \tag{3.6}
$$
Thus the effective inertia, if defined as $D_vP(0)$, is $2I$ with normalization (3.3). This specifies the factor of two explicitly.

## 4. Symmetry reduction and minimal kernel assumptions

Let $G\subset O(N)$ be a compact group with $h(g\xi)=h(\xi)$ and $Q(gx)=Q(x)$ for every $g\in G$. Define
$$
 V=\{v\in\mathbb R^N:gv=v\text{ for every }g\in G\},\qquad d=\dim V\geq1,
$$
$$
 Z_G^+=\{a\in Z:a\text{ real},\ a(gx)=a(x),\ a(-x)=a(x)\},
$$
$$
 Z_G^-=\{b\in Z:b\text{ real},\ b(gx)=b(x),\ b(-x)=-b(x)\},
$$
$$
 X_G=Z_G^+\oplus iZ_G^-=
 \{f\in Z:f(gx)=f(x),\ f(-x)=\overline{f(x)}\}. \tag{4.1}
$$
The real dual $X_G^*$ can be identified with distributions in $Z^*$ having the same symmetries. Averaging over $G$ and over the real-linear parity-conjugation involution is a bounded projection in both spaces. An equivariant distribution that vanishes on $X_G$ thus vanishes on the full space after averaging.

**General criterion.** In addition to (3.1), (3.5), and these symmetries, assume only
$$
 \ker(L_+|_{Z_G^+})=\{0\},\qquad
 \ker(L_-|_{Z_G^-})=\{0\}. \tag{4.2}
$$
Choose an orthonormal basis $e_1,\dots,e_d$ of $V$, and set
$$
 g_j=\partial_{e_j}Q,\quad
 z_j=(L_-|_{Z_G^-})^{-1}g_j,\quad I_{jk}=\langle g_j,z_k\rangle. \tag{4.3}
$$
There are neighborhoods of $\omega_0$, $0\in V$, and $Q\in X_G$, and a unique local real $C^1$ map
$$
 (\omega,v)\longmapsto Q_{\omega,v}\in X_G \tag{4.4}
$$
solving
$$
 h(D)Q_{\omega,v}+\omega Q_{\omega,v}
       +iv\cdot\nabla Q_{\omega,v}
       -|Q_{\omega,v}|^\alpha Q_{\omega,v}=0,
 \qquad Q_{\omega_0,0}=Q. \tag{4.5}
$$
All identities (3.6) hold, with the matrix on $V$, at fixed $\omega_0$. A negative direction of $I$ gives negative-energy global traveling waves at every sufficiently small nonzero velocity along that direction.

Taking $G=\{1\}$ gives the full vector theorem. For isotropic $h$ and radial $Q$, $G=O(N-1)$ fixing an axis gives the axial scalar-velocity theorem. In that subspace, full inversion and longitudinal reflection give the same parity, since transverse inversion lies in $O(N-1)$.

These conditions remove the unavoidable symmetry kernels: the phase mode $Q$ is even and excluded from the imaginary odd sector; translation derivatives are odd and excluded from the real even sector. Accidental zero modes must still be excluded. For a nonradial state of a rotation-invariant equation, rotation derivatives can be real-even and survive, so inversion alone does not automatically establish (4.2).

### Why zero-kernel conditions suffice

Multiplication by $|Q|^\alpha$ is compact $Z\to Z^*$. In fact $Q\in L^p$ gives $|Q|^\alpha\in L^{p/\alpha}$, and
$$
 \left|\int Whk\right|\leq\|W\|_{p/\alpha}\|h\|_p\|k\|_p. \tag{4.6}
$$
Approximate $|Q|^\alpha$ in this coefficient space by bounded compactly supported functions. Each induces a compact form map by local Rellich compactness $H^s\hookrightarrow L^2_{\rm loc}$, $s>0$; (4.6) passes compactness to the limit.

The operator $A=h(D)+\omega_0:Z\to Z^*$ is a coercive isomorphism, also on each invariant parity sector. Thus $L_\pm$ are Fredholm of index zero, and (4.2) makes them bounded isomorphisms. Positivity, a count of negative eigenvalues, and a separate quantitative inverse assumption are unnecessary for the qualitative theorem.

### Proof of the implicit branch

Set
$$
 \mathcal F(\omega,v,f)=h(D)f+\omega f+iv\cdot\nabla f-|f|^\alpha f.
$$
For $v\in V$, this preserves (4.1). Section 2 and (3.4) show that
$\mathcal F:\mathbb R\times V\times X_G\to X_G^*$ is real $C^1$. Its profile derivative at $(\omega_0,0,Q)$ is
$$
 D_f\mathcal F(a+ib)=L_+a+iL_-b,
$$
an isomorphism by (4.2) and compactness. The real Banach-space implicit-function theorem proves (4.4), local uniqueness, and the full distributional equation (4.5). This establishes existence without high-order differentiability of the noninteger power.

## 5. Momentum expansion and sign

Differentiate (4.5) in the $e_k$ velocity direction at the base point. Its real part is zero by invertibility of $L_+$; its imaginary part solves $L_-b=-g_k$. Hence
$$
 \partial_{v_k}Q_{\omega_0,v}|_{v=0}=-iz_k. \tag{5.1}
$$
The matrix is symmetric by form self-adjointness:
$$
 I_{jk}=\langle L_-z_j,z_k\rangle
        =\langle z_j,L_-z_k\rangle=I_{kj}. \tag{5.2}
$$
These are form dualities, not assumptions of additional differentiability.

From (3.4), (5.1), and real duality,
$$
 \left.\partial_{v_k}P_j(Q_{\omega_0,v})\right|_{v=0}
 =2\langle\partial_{e_j}Q,z_k\rangle=2I_{jk}. \tag{5.3}
$$
At sufficient regularity this is just
$$
 \int(z_k\partial_{e_j}Q-Q\partial_{e_j}z_k)
 =2\int z_k\partial_{e_j}Q.
$$
Thus $P(Q_{\omega_0,v})=2Iv+o(|v|)$ in $V$. The full momentum vector lies in $V$, since a $G$-invariant function has $G$-fixed momentum.

Complex conjugation maps the equation at $v$ to the equation at $-v$, preserves $X_G$, and fixes the real base state. Local uniqueness gives
$$
 Q_{\omega,-v}=\overline{Q_{\omega,v}}. \tag{5.4}
$$
Momentum is odd and energy even in velocity. With only $C^1$ regularity, this parity alone does not justify cubic or quartic Taylor remainders.

## 6. Exact Pohozaev identity without spatial weights

We justify dilation differentiation directly on the local branch. No finite variance, spatial decay rate, or prior assumption $x\cdot\nabla Q_{\omega,v}\in Z$ is needed.

For fixed parameters let
$$
 S_{\omega,v}(f)=E(f)+\frac\omega2M(f)-\frac12v\cdot P(f). \tag{6.1}
$$
It is $C^1$ on $Z$, and $DS_{\omega,v}(Q_{\omega,v})=0$ in $Z^*$, by the full profile equation.

Define $T_\lambda f(x)=\lambda^{N/2}f(\lambda x)$. For every $f\in Z$, this is strongly continuous in $\lambda>0$. Homogeneity and the critical relation $N\alpha/2=m$ show that $T_\lambda Q_{\omega,v}$ solves the profile problem at
$$
 (\omega_\lambda,v_\lambda)=(\lambda^m\omega,\lambda^{m-1}v). \tag{6.2}
$$
For $\lambda$ near one, the scaled profile and parameters remain in the implicit-function uniqueness neighborhoods. Local uniqueness implies
$$
 T_\lambda Q_{\omega,v}
 =Q_{\lambda^m\omega,\,\lambda^{m-1}v}. \tag{6.3}
$$
The right side is a $C^1$ curve in $Z$. Thus the left side, initially only known to be strongly continuous, is itself $C^1$ along this particular branch. This is the purpose of including frequency together with velocity in the implicit-function theorem. The symmetry spaces used above are invariant under this scaling.

Direct change of variables gives
$$
 E(T_\lambda f)=\lambda^mE(f),\qquad
 M(T_\lambda f)=M(f),\qquad P(T_\lambda f)=\lambda P(f). \tag{6.4}
$$
Differentiate $S_{\omega,v}(T_\lambda Q_{\omega,v})$ at $\lambda=1$, using (6.3) for the chain rule and (6.4) for its value:
$$
 0=DS_{\omega,v}(Q_{\omega,v})
    \left[\left.\partial_\lambda T_\lambda Q_{\omega,v}\right|_{\lambda=1}\right]
  =mE(Q_{\omega,v})-\frac12v\cdot P(Q_{\omega,v}). \tag{6.5}
$$
This proves the exact formula (3.6). At $v=0$, it gives $E(Q)=0$ without a separate Pohozaev regularity hypothesis. Together with (5.3), it gives
$$
 E(Q_{\omega_0,v})=\frac1m v^TIv+o(|v|^2),
$$
and therefore negative energy along every negative direction for sufficiently small nonzero speed.

Criticality is essential: at other powers the kinetic and nonlinear terms scale differently, so the energy identity does not have this form.

## 7. Elliptic bootstrap and global strong solutions

For a smooth elliptic symbol as in Section 3, choose the parameter neighborhood small enough that
$$
 b_{\omega,v}(\xi)=h(\xi)+\omega-v\cdot\xi
 \geq c_0(1+|\xi|^m). \tag{7.1}
$$
For $m>1$, this follows from boundedness of
$|\xi|/(\omega_0+h(\xi))$; for $m=1$, choose the speed below the ellipticity threshold. For every $1<q<\infty$, the standard Fourier multiplier estimate then gives
$$
 b_{\omega,v}(D)^{-1}:L^q\longrightarrow H^{m,q}. \tag{7.2}
$$
Indeed $(1+|\xi|^2)^{m/2}/b_{\omega,v}(\xi)$ and its derivatives satisfy the Mikhlin bounds. A fractional homogeneous symbol need not be smooth at zero: positivity of the denominator and the factors $|\xi|^{|\gamma|}$ in these bounds handle the homogeneous derivatives there. The $L^q$ resolvent agrees with the energy-space resolvent on common data, by simultaneous smooth approximation. Apply (7.2) to
$$
 b_{\omega,v}(D)Q_{\omega,v}=|Q_{\omega,v}|^\alpha Q_{\omega,v}. \tag{7.3}
$$

Here is the full integrability bootstrap. For $N>m$, initially
$$
 Q_{\omega,v}\in L^{r_0},\qquad
 r_0=\frac{2N}{N-m},\qquad
 a_0=\frac1{r_0}=\frac12-\frac m{2N}.
$$
If $Q_{\omega,v}\in L^{r_k}$, then its nonlinearity lies in $L^{q_k}$, $q_k=r_k/(1+\alpha)$. Initially
$$
 q_0=\frac{2N^2}{(N-m)(N+2m)}>1,
$$
and subsequent $q_k$ only increase. While $mq_k<N$, (7.2) and Sobolev embedding give a larger exponent determined by
$$
 a_{k+1}=(1+\alpha)a_k-\frac mN,\qquad a_k=1/r_k.
$$
Since $\alpha=2m/N$,
$$
 a_k-\frac12=(1+\alpha)^k\left(a_0-\frac12\right). \tag{7.4}
$$
After finitely many steps, $mq_k>N$ and the embedding gives $L^\infty$. If equality occurs, the critical Bessel-potential embedding gives every sufficiently large finite $L^r$; choose one to obtain a strict inequality at the next step. For $N=m$, start with any sufficiently large finite exponent from the critical energy-space embedding. For $N<m$, the initial energy space already embeds in $L^\infty$.

Consequently $Q_{\omega,v}\in L^\infty\cap L^2$. Its nonlinearity belongs to $L^2$, and (7.2) at $q=2$ gives
$$
 Q_{\omega,v}\in H^m\cap L^\infty. \tag{7.5}
$$
Since $m\geq1$, translations of the profile are differentiable in $L^2$. Thus
$$
 u(t,x)=e^{i\omega t}Q_{\omega,v}(x-vt)
 \in C(\mathbb R;H^m)\cap C^1(\mathbb R;L^2)
$$
solves (3.2) in $L^2$ at every time and has constant $H^{m/2}$ norm. This is an explicit global strong solution; no general nonlinear-flow theorem is needed to construct it.

The bootstrap uses improved integrability, not high-order differentiation of the nonlinearity. It applies to BNLS for $N>8$, $\alpha<1$, and gives $H^4$ profiles in every dimension where the spectral and pairing assumptions hold. Unlimited smoothness, analyticity in velocity, and unlimited Sobolev persistence across zeros of noninteger-power profiles are not asserted.

If the symbol is only as in (3.1) and not smooth on the sphere, the implicit branch and exact energy identity still hold in the form setting and give energy-space distributional traveling solutions. The strong-solution conclusion uses the smooth-symbol assumption via (7.2).

## 8. Scaling consequences and normalization checks

The stationary frequency family is
$$
 Q_{\omega,0}=T_\lambda Q,\qquad
 \lambda=(\omega/\omega_0)^{1/m}, \tag{8.1}
$$
locally by uniqueness, and globally as a scaled family of exact stationary solutions. Along this family
$$
 L_{-,\omega}T_\lambda=\lambda^mT_\lambda L_{-,\omega_0},
 \qquad
 \partial_jQ_{\omega,0}=\lambda T_\lambda\partial_jQ.
$$
Therefore
$$
 \boxed{I(\omega)=(\omega/\omega_0)^{(2-m)/m}I(\omega_0).} \tag{8.2}
$$
For BNLS the exponent is $-1/2$. The sign of each inertia eigenvalue is independent of frequency along this mass-critical scaled family.

If one exact negative-energy traveling profile $q$ exists at $(\omega,v)$, every $\lambda>0$ gives another exact profile $T_\lambda q$ at $(\lambda^m\omega,\lambda^{m-1}v)$, with
$$
 M(T_\lambda q)=M(q),\qquad
 E(T_\lambda q)=\lambda^mE(q)<0. \tag{8.3}
$$
Hence every prescribed negative energy value is realized by a global traveling wave with the same mass as that chosen wave. This consequence of one example is confined to the dimension in which that example exists.

For isotropic dispersion and radial $Q$, rotation invariance gives $I=\iota\,\mathrm{Id}$. One negative axial pairing gives negative energy for all sufficiently small nonzero speeds by rotations. If an axial spectral verification excludes zero in every relevant spherical harmonic degree, it also excludes zero in the full even/odd sectors: all harmonics of one degree have the same radial operator, and axial zonal harmonics provide a copy of every degree.

As a normalization and sign check, quadratic NLS has $m=2$, $h(\xi)=|\xi|^2$. Its Galilean family at fixed frequency has
$$
 P(Q_v)=\frac12M(Q)v,\qquad
 I=\frac14M(Q)\,\mathrm{Id},\qquad
 E(Q_v)=\frac18M(Q)|v|^2.
$$
Thus its inertia is positive. The negative-inertia mechanism is not a negative-energy Galilean transform of ordinary NLS.

## 9. Scope

We proved a dimension-independent $C^1$ criterion for pure mass-critical BNLS, and a version for positive even smooth homogeneous dispersion of order $m\geq1$. Its substantive assumptions are a real even stationary state, no zero mode in specified symmetry sectors, and a strictly negative inverse pairing. Compactness supplies bounded inverses; critical scaling supplies the exact energy identity; elliptic integrability bootstrap supplies strong global waves.

We did not prove those stationary or spectral assumptions in arbitrary dimensions. A numerical negative pairing without validated invertibility does not establish them. We did not prove stability of the traveling waves, which is unnecessary for their role as exact counterexamples to a statement about every initial datum.

