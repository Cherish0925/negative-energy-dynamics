# R30  arbitrary-rank integrable Stein-defect remainder

This is an algebraic consequence of the Read–Schulz exact one-dimensional remainder and the quantitative Hilbert embedding in their Lemma 6. It does not solve the planar sharp inequality. It replaces the nonintegrable Tr(C^3) normalization by Tr(Q^3), where Q is a bounded congruence of the actual slice Gram matrix.

## Statement

Let W have finitely many orthonormal rows in H^1(R; H), where H is a separable Hilbert space. Write Gamma=WW*, A(x)=integral_{-infinity}^x Gamma(t) dt, and

    D_x = integral ||W'||_HS^2 - (pi^2/4) integral Tr(Gamma^3).

Define, by matrix functional calculus,

    Theta = (pi/2)(A-I/2),
    X = tan(Theta),
    Q = sec(Theta) Gamma sec(Theta).

Then, with 0/0 interpreted as zero,

    D_x >= c_* integral ||[X,Q^(3/2)]||_HS^4 / Tr(Q^3),
    c_* = (4-pi)^2 / 2916 > 0.                       (1)

The assertion is invariant under a constant change of orthonormal row basis. Since ||sec Theta||<=sqrt(2),

    Tr(Q^3) <= 8 Tr(Gamma^3),
    ||[X,Q^(3/2)]||_HS^2 <= 4 Tr(Q^3),

so the right side has an integrable density. It vanishes pointwise exactly when [A,Gamma]=0.

An immediate integrated consequence is

    integral ||[X,Q^(3/2)]||_HS^2
       <= sqrt(8/c_*) sqrt(D_x * integral Tr(Gamma^3)).  (2)

No estimate controlling the first-order residual, the transverse kinetic deficit, or a planar constant improvement is asserted here.

## Read–Schulz inputs and normalization

For 0<alpha<pi put Theta_alpha=(alpha/2)(A-I/2), with eigenvalues theta_i. In an eigenbasis of A let

    C_ik = Gamma_ik / cos(theta_i+theta_k),
    h(d) = sin(d)/d - cos(d),
    g_ik = cos(theta_i+theta_k) h(theta_i-theta_k).

Their exact identity is

    T_x-alpha^2 S/4 = integral ||W'-B_alpha W/2||_HS^2
                         + (1/4) integral G_alpha,
    G_alpha = alpha^2 sum_ik g_ik Re((C^2)_ik C_ki),
    S = integral Tr(Gamma^3).

They construct a real Hilbert space and vectors v_i with

    g_ik = ||v_i-v_k||^4.

For a standard real Gaussian z on the finite span of the v_i set sigma_i=<z,v_i> and

    K_z,ik = (sigma_i-sigma_k)^2 C_ik.

Their trace identity, equivalently the Gaussian fourth moment, gives

    G_alpha = (2 alpha^2/3) E Tr(C K_z^2).              (3)

The quantitative part of Lemma 6 has

    D(s)=2 sqrt(cos(2s))/sqrt(3),
    B(f,f) >= (1-pi/4) integral D(s) |f(s)|^2 ds,
    v(theta)=chi_theta/sqrt(2)

in the B-inner product, where chi_theta is an oriented interval indicator relative to an arbitrary fixed anchor in (-pi/4,pi/4). The off-diagonal kernel of B is -partial_s partial_t sqrt(g(s,t)).

## A uniformly bounded coordinate functional

There is a vector w in the embedding Hilbert space such that

    <w,v(theta_i)-v(theta_k)> = tan(theta_i)-tan(theta_k),
    ||w||^2 <= L,
    L = 8 pi sqrt(6)/(4-pi).                           (4)

Indeed define the linear functional on interval indicators by

    ell(f)=sqrt(2) integral sec^2(s) f(s) ds.

The coercivity of B and weighted Cauchy–Schwarz imply

    ||ell||^2 <= [2/(1-pi/4)] integral sec^4(s)/D(s) ds
              = [sqrt(3)/(1-pi/4)]
                  integral sec^4(s)/sqrt(cos(2s)) ds.

With t=tan(s), the last integral over (-pi/4,pi/4) is

    integral_{-1}^1 (1+t^2)^(3/2)/sqrt(1-t^2) dt
       <= 2 sqrt(2) pi.

Riesz representation gives (4); projection of w onto the finite span of the v_i preserves its required coordinate values and cannot increase its norm. The bound is uniform in alpha, the number of points, and their locations including limiting endpoints.

## Stein-defect factorization

For the moment fix alpha<pi and write

    X=tan Theta_alpha,
    Q=sec Theta_alpha Gamma sec Theta_alpha.

The addition formula for cosine gives the exact relation

    Q = C-XCX >= 0.                                    (5)

Since ||X||<1,

    C = sum_{n>=0} X^n Q X^n = VV*,
    V=[Q^(1/2), XQ^(1/2), X^2 Q^(1/2), ...].             (6)

Define the Hermitian matrix

    Z=Q^2-XQ^2X.

It admits the factorization Z=VU with block column

    U_0=Q^(3/2), U_1=-Q^(3/2)X, U_n=0 (n>=2).

Consequently, with C^dagger the Moore–Penrose inverse,

    Tr(C^dagger Z^2)
       = ||C^(dagger/2) Z||_HS^2
       <= ||U||_HS^2
       = Tr Q^3 + Tr(X Q^3 X)
       <= 2 Tr Q^3.                                   (7)

The range condition needed in the pseudoinverse calculation follows from Z=VU. Equivalently one can first work with positive definite Gamma and pass to the limit.

## Gaussian duality

Set

    q(z)=<z,w>^2-||w||^2,
    E_Q = Tr(Q^2 [X,[X,Q]])
        = 2 Tr(Q [X,Q]^* [X,Q]) >= 0.

The Gaussian second-chaos identity gives

    E q(z)^2 = 2 ||w||^4,
    E[q(z) K_z,ik] = 2 (X_i-X_k)^2 C_ik.

Since Q_ik=(1-X_i X_k)C_ik and Z_ik=(1-X_i X_k)(Q^2)_ik,

    E_Q = (1/2) E[q(z) Tr(K_z Z)].                      (8)

Weighted matrix Cauchy–Schwarz and scalar Gaussian Cauchy–Schwarz imply

    E_Q^2 <= (1/4) E q^2 * E|Tr(K_z Z)|^2
           <= (1/2)||w||^4 Tr(C^dagger Z^2)
                                * E Tr(C K_z^2)
           <= [3 L^2/(2 alpha^2)] G_alpha Tr(Q^3),

where (3) and (7) were used. Thus the all-rank pointwise bound is

    G_alpha >= [2 alpha^2/(3 L^2)] E_Q^2/Tr(Q^3).       (9)

This argument does not compare signed closed-triangle products termwise.

## Power commutator and endpoint limit

Diagonalize Q. For a,b>=0,

    (a+b)(a-b)^2 >= (8/9)(a^(3/2)-b^(3/2))^2.

Therefore

    E_Q >= (8/9)||[X,Q^(3/2)]||_HS^2,

and (9) yields

    G_alpha >= [128 alpha^2/(243 L^2)]
                  ||[X,Q^(3/2)]||_HS^4/Tr(Q^3).        (10)

The exact remainder identity gives

    D_x+(pi^2-alpha^2)S/4 >= (1/4) integral G_alpha.

As alpha increases to pi, the bounded functional-calculus matrices X and Q converge pointwise. The integrand in (10) is bounded by 16 Tr(Q^3)<=128 Tr(Gamma^3), including at Q=0 by continuity. Dominated convergence, or Fatou alone for the lower bound, yields

    D_x >= [32 pi^2/(243 L^2)]
              integral ||[X,Q^(3/2)]||_HS^4/Tr(Q^3).

Using L^2=384 pi^2/(4-pi)^2 gives exactly c_* in (1).

Finally [X,Q^(3/2)]=0 iff [X,Q]=0. Since tan is injective on the relevant interval and sec(Theta) commutes with X, this is equivalent to [A,Gamma]=0. Cauchy–Schwarz with the denominator Tr(Q^3) gives (2).

## Scope

This proves a weaker, quartic-over-cubic arbitrary-rank remainder. It does not establish the stronger quadratic conjecture

    G_alpha >= (2 alpha^4/27)||[A,Gamma^(3/2)]||_HS^2,

and it does not by itself resolve the two-dimensional sharp orthonormal GN/Lieb–Thirring conjecture.

## Further consequence: a scale-free approximate Riccati equation

This consequence concerns the bounded variables X and Q. It does not establish that the scale matrix C(x) is approximately constant, and therefore is not a channel-extraction theorem.

For each 0<alpha<=pi write Theta=(alpha/2)(A-I/2), X=tan Theta, Q=sec Theta Gamma sec Theta, and let ad_Theta(H)=[Theta,H]. The divided-difference differentiation formula gives, almost everywhere,

    X' = (alpha/2) sinc(ad_Theta) Q.                    (11)

Indeed in an eigenbasis of Theta,

    (tan theta_i-tan theta_j)/(theta_i-theta_j)
       = sinc(theta_i-theta_j)/(cos theta_i cos theta_j).

Define the bounded-variable Riccati defect by

    R_alpha = X'-(alpha/2)Q.

For alpha<pi this is exactly X'-(alpha/2)(C-XCX), using (5). The definition X'-(alpha/2)Q remains unambiguous at alpha=pi even where a formal endpoint quotient defining C has a zero denominator.

Pointwise one has

    ||R_alpha||_S3^3
       <= (27 alpha^3/1000) ||[X,Q^(3/2)]||_HS^2.      (12)

To prove this, use the standard Ando/Birman–Koplienko–Solomyak inequality for positive matrices H,J,

    ||H^(2/3)-J^(2/3)||_S3^3 <= ||H-J||_S2^2.

One primary source is T. Ando, "Comparison of norms ||f(A)-f(B)|| and ||f(|A-B|)||", Math. Z. 197 (1988), 403–409. The original fractional-power source is M. Sh. Birman, L. S. Koplienko and M. Z. Solomyak, "Estimates of the spectrum of a difference of fractional powers of selfadjoint operators", Izv. Vyssh. Uchebn. Zaved. Mat. 1975, no. 3, 3–10; https://www.mathnet.ru/eng/ivm/y1975/i3/p3.

For U_t=exp(i t Theta), this gives

    ||U_t Q U_t^*-Q||_S3
       <= ||U_t Q^(3/2) U_t^*-Q^(3/2)||_HS^(2/3)
       <= |t|^(2/3)||[Theta,Q^(3/2)]||_HS^(2/3).

Since arctan is scalar 1-Lipschitz on [-1,1], entrywise comparison in the eigenbasis of X yields

    ||[Theta,Q^(3/2)]||_HS <= ||[X,Q^(3/2)]||_HS.

Also sinc(ad_Theta) is the average over t in [0,1] of cos(t ad_Theta). The cosine map is the average of conjugation by U_t and U_t^*. Minkowski's inequality and integral_0^1 t^(2/3) dt=3/5 therefore give

    ||R_alpha||_S3
       <= (3 alpha/10)||[X,Q^(3/2)]||_HS^(2/3),

which is (12).

At alpha=pi, combining (12) with (2) yields the global, rank-independent estimate

    integral ||X'-(pi/2)Q||_S3^3
       <= (27 pi^3/1000) sqrt(8/c_*) sqrt(D_x S).       (13)

This estimate has no largest eigenvalue, minimum occupation, or endpoint cutoff in its constant. The remaining constructive stability problem must still control the variation of C(x), or otherwise produce actual fixed transverse channels / separated blocks while retaining the physical kinetic-energy bound.

## Auxiliary constructive scalar stability and its fixed-frame sum

The result in this section is a scalar mass-coordinate argument. It does not repair a moving transverse frame. It does, however, remove all scale and rank restrictions from the amplitude part of such a repair.

Let a>=0 belong to H^1(R), integral a^2=1, and put

    q(x)=a(x)^2,
    T=integral |a'|^2,
    S=integral a^6,
    D=T-(pi^2/4)S.

There is a normalized sech density

    q_0(x)=c_bar sech(pi c_bar (x-x_0)),

such that

    integral |q-q_0|^3 <= 2048 S^(1/4) D^(3/4),         (14)
    integral |(sqrt(q_0))'|^2 = pi^2 c_bar^2/8 <= T.    (15)

The center x_0 can be chosen at a median of q. The right side of (14) is zero when D=0, with the usual exact equality conclusion.

### Mass coordinates and the sharp spectral gap

Let t=A(x)=integral_{-infinity}^x a^2 and use the generalized inverse x(t). Define

    p(t)=a(x(t))^2,   0<t<1.

Then p belongs to H^1_0(0,1), including when a has zeros or separated support components, and

    integral_0^1 |p'|^2 dt = 4T,
    integral_0^1 p^2 dt = S.

These follow first on positive support intervals from p'(t)=2a'(x(t))/a(x(t)), then by approximation or summing the intervals. Endpoint zero traces also follow from the one-dimensional Sobolev estimate. Flat intervals of A correspond to zero points of p; they do not create a nonzero jump in p.

Write w(t)=sin^2(pi t), c(t)=p(t)/sin(pi t), and

    c_bar=2 integral_0^1 w(t)c(t) dt >0.

The ground-state transform and the Dirichlet spectral gap between pi^2 and 4pi^2 give

    D=(1/4) integral_0^1 w(t)|c'(t)|^2 dt,
    V:=integral_0^1 w(t)|c(t)-c_bar|^2 dt
       <=4D/(3pi^2),
    S=c_bar^2/2+V.                                    (16)

The natural form domain in the first identity is the weighted Sobolev space obtained from p in H^1_0(0,1). No pointwise boundary condition is imposed on c itself. The boundary terms vanish in the ground-state transform by approximation in H^1_0. In particular c may have an admissible endpoint singularity, while p has zero trace.

Equation (15) follows immediately from c_bar^2/2<=S and the sharp scalar inequality.

### Actual physical-space density estimate

Here are explicit bounds, including the logarithmic transport loss. If D/S>=1/512, then

    integral |q-q_0|^3 <=4(S+c_bar^2/2)<=8S
       <= 8*512^(3/4) S^(1/4)D^(3/4),

so (14) holds for every median center.

Otherwise rescale z=c_bar(x-x_0), and divide densities by c_bar. In these variables c_bar=1; write d=D/c_bar^2. Equation (16) shows d<1/256. Set

    epsilon=d^(1/4),   e=2 sqrt(d/epsilon)=2 epsilon^(3/2).

For epsilon<=1/4, select t_0 in [1/4,3/4] using the variance bound in (16), then apply weighted Cauchy–Schwarz to c(t)-c(t_0). Since

    integral_epsilon^(1-epsilon) 1/w(t) dt
       =2 cot(pi epsilon)/pi <=2/(pi^2 epsilon),

one obtains

    sup_[epsilon,1-epsilon] |c(t)-1| <= e <=1/4.        (17)

Thus p is positive throughout this quantile interval; in particular the generalized inverse has no jumps there even if the original a has gaps elsewhere. Normalize the inverse by z(1/2)=0 and compare it with

    z_0(t)=pi^(-1) log tan(pi t/2).

Their derivatives are 1/[c(t)sin(pi t)] and 1/sin(pi t), respectively. Hence on the quantile core,

    |z(t)-z_0(t)| <= h:=(2e/pi)log(1/epsilon)<=1/4.      (18)

The physical core length is at most [8/(3pi)]log(1/epsilon). The normalized target density is sech(pi z), whose Lipschitz constant is at most pi. Therefore its pointwise difference from q(z(t)) is at most

    e+pi h <=3e log(1/epsilon).

Its core L^3 error is bounded by

    (576/pi) epsilon^(9/2) log^4(1/epsilon)
       <=200 epsilon^3.                              (19)

Indeed sup_(0<epsilon<=1/4) epsilon^(3/2)log^4(1/epsilon)
=4096/(81 exp(4)), which makes the displayed numerical coefficient smaller than 200.

For the original density, (16) gives

    integral_outside-core q^3 dz
       =integral_quantile-tails c^2 w dt
       <= (4pi^2/3)epsilon^3+8d/(3pi^2)
       <14 epsilon^3.                                (20)

For the target density, use sech(pi z)<=2exp(pi z) on the left (and its symmetric right version), (18), and tan(pi epsilon/2)<=2epsilon. Then

    integral_outside-physical-core sech^3(pi z) dz
       <= [128/(3pi)]exp(3pi/4) epsilon^3
       <150 epsilon^3.                               (21)

Equations (19)–(21), together with |u-v|^3<=4(u^3+v^3), give total error less than 1000 d^(3/4). Restoring scale gives

    error <=1000 c_bar^(1/2) D^(3/4)
          <=1000*2^(1/4) S^(1/4)D^(3/4),

which proves (14) with the stated universal constant 2048.

### Arbitrary-rank consequence when the transverse frame is fixed

Suppose the physical slice operator already has the form

    gamma(x)=sum_i a_i(x)^2 |b_i><b_i|,

where the b_i form a fixed orthonormal family in H^1(R_y), each a_i is real nonnegative and normalized in L^2(R_x), and the sum is finite. Apply the scalar construction separately, allowing completely arbitrary scales and centers, to obtain gamma_0(x)=sum_i q_{0,i}(x)|b_i><b_i|. Then

    integral ||gamma-gamma_0||_S3^3
       =sum_i integral |a_i^2-q_{0,i}|^3
       <=2048 S_total^(1/4) D_total^(3/4),             (22)

by Holder's inequality. Moreover

    T_x(gamma_0)<=T_x(gamma),
    T_y(gamma_0)=T_y(gamma),

and the associated product orbitals remain orthonormal. Thus this is an actual density-operator approximation with no excess total kinetic energy, uniform in rank and all profile scales. It relies on a fixed transverse orthonormal frame; neither the Stein remainder nor the approximate Riccati estimate has yet supplied that frame for a general family.

## Constructive moving-frame extraction for a common row Gram matrix

This section treats a genuine moving transverse frame, with no rank bound or scale bound, under the explicit additional condition

    Gamma(x)=a(x)^2 I_N,
    a>=0, integral a^2=1.                              (23)

It does not establish (23), or an approximation to (23) by separated blocks, for a general near-extremizer.

Write W(x)=a(x)U(x) on the set where a>0, so U(x)U(x)^*=I_N, and put P(x)=U(x)^*U(x), an orthogonal projection of rank N on the physical transverse Hilbert space. Let

    S_a=integral a^6,   D_a=integral |a'|^2-(pi^2/4)S_a,
    E_or=integral a^2 ||U'||_HS^2.

Differentiating UU*=I gives the exact decomposition

    T_x=N integral |a'|^2+E_or,
    S=N S_a,
    D_x=N D_a+E_or.                                   (24)

Define a constant physical density matrix by averaging projections:

    sigma=integral a(x)^2 P(x) dx.                     (25)

Then 0<=sigma<=I and Tr sigma=N. It may have infinite rank, but it is trace class. Let q_0 be the scalar sech density constructed in (14), and define

    gamma_0(x)=q_0(x) sigma.

The full physical density operator is |sqrt(q_0)><sqrt(q_0)| tensor sigma on L^2(R_x) tensor L^2(R_y). It is a positive contraction, generally a mixed state rather than an orthonormal pure frame. Its diagonal slice is gamma_0(x). It has the following bounds:

    integral ||gamma(x)-gamma_0(x)||_S3^3 dx
       <=16384 S^(1/4) D_x^(3/4),                     (26)
    T_x(gamma_0)<=T_x(W),
    T_y(gamma_0)=T_y(W).                              (27)

Here T_x(gamma_0)=Tr(sigma) integral |(sqrt(q_0))'|^2, and transverse kinetic energy is understood through its nonnegative closed quadratic form. Equation (27) follows from (15), Tr sigma=N, and Tonelli's theorem applied to (25).

### Orientation estimate

The only extra step beyond the scalar lemma is to show

    I:=integral a^6 ||P-sigma||_S3^3 dx
       <=128 S^(1/4)D_x^(3/4)                         (28)

when delta=D_x/S<=1/512. Put epsilon=delta^(1/4) and let the physical core correspond to quantiles t in [epsilon,1-epsilon]. Its q=a^2 mass is m=1-2epsilon>=1/2. In the notation of (16), D_a/c_bar^2<=delta for this range, and the same core estimate gives

    |c/c_bar-1|<=e:=2sqrt(delta/epsilon)<=1/4.

In particular q is positive throughout the core. Put sigma_c and sigma_t for the conditional q-averages of P on the core and its complement. Both are positive contractions of trace N, and

    sigma=m sigma_c+(1-m)sigma_t.

On the core,

    q_max^2 <= (25/16)c_bar^2,
    R_c:=integral_core 1/q(x) dx
       =integral_epsilon^(1-epsilon) 1/[c(t)^2 sin^2(pi t)]dt
       <=32/[9pi^2 c_bar^2 epsilon].                  (29)

The Hilbert–Schmidt projection derivative satisfies

    ||P'||_HS^2 <=2||U'||_HS^2.

For completeness, decompose U'=Omega U+V with Omega=U'U* skew-Hermitian and VU*=0. Then P'=V*U+U*V and ||P'||_HS^2=2||V||_HS^2<=2||U'||_HS^2.

The elementary pairwise variance formula and weighted Cauchy–Schwarz give

    J_c:=integral_core q||P-sigma_c||_HS^2 dx
       = [1/(2m)] integral_core integral_core
              q(x)q(y)||P(x)-P(y)||_HS^2 dx dy
       <=(m/2)R_c integral_core q||P'||_HS^2 dx
       <=32/[9pi^2 c_bar^2 epsilon] E_or.              (30)

Because differences of positive contractions have operator norm at most one,

    ||P-sigma_c||_S3^3 <=||P-sigma_c||_HS^2,
    ||sigma_c-sigma_t||_S3^3 <=2N.

Apply the triangle inequality cubed to
P-sigma=(P-sigma_c)+(1-m)(sigma_c-sigma_t). This yields

    I_core <=4q_max^2 J_c
                +4(2epsilon)^3 (2N) S_a
           <= [200/(9pi^2 epsilon)]E_or
                +64S epsilon^3.                     (31)

On the tail, ||P-sigma||_S3^3<=2N, and the scalar tail estimate yields

    I_tail <=(16pi^2/3)S epsilon^3
                  +[16/(3pi^2)]N D_a.               (32)

Since E_or<=D_x, N D_a<=D_x, and epsilon=delta^(1/4), the sum of (31) and (32) is less than 128S delta^(3/4). This proves (28).

Finally,

    gamma-gamma_0=q(P-sigma)+(q-q_0)sigma.

Use the Schatten triangle inequality cubed, Tr sigma^3<=N, (14), and (28):

    integral ||gamma-gamma_0||_S3^3
       <=4I+4N integral |q-q_0|^3
       <=8704 S^(1/4)D_x^(3/4).

If delta>=1/512, the elementary bound

    integral ||gamma-gamma_0||_S3^3
       <=4(S+Tr sigma^3 integral q_0^3)<=8S

suffices. Thus the uniform constant 16384 in (26) covers both cases. If D_x=0, (24) implies D_a=E_or=0, so the construction is exact.

Zeros or gaps of a cause no difficulty: U and P need only be defined on the positive set of a; the weighted integrals ignore the rest, and the small-deficit quantile core contains no gap by its positive lower bound for c.

### Exact-sech common-profile refinement

When a^2=(lambda/pi)sech(lambda(x-x_0)) already, one has D_a=0 and D_x=E_or. The weighted Poincare inequality for the normalized sech measure has constant 4/lambda^2. This follows by conjugating to the operator

    H=-partial_x^2+lambda^2/4-(3lambda^2/4)sech^2(lambda(x-x_0))
      =A^*A,
    A=partial_x+(lambda/2)tanh(lambda(x-x_0)).

Its partner AA*=-partial_x^2+lambda^2/4+(lambda^2/4)sech^2 is bounded below by lambda^2/4; hence H has a gap at least lambda^2/4 above its ground state sqrt(a^2). Apply the resulting Poincare inequality to P-sigma, use ||P'||_HS^2<=2||U'||_HS^2 and a^4<=(lambda/pi)^2. One obtains the sharper bound

    integral ||gamma-a^2 sigma||_S3^3 <=(8/pi^2)D_x.    (33)

### Mixed states, finite truncation, and the product coefficient

If sigma has infinite rank, take its finite spectral truncations sigma_j. They satisfy 0<=sigma_j<=I, converge to sigma in S3, and have no larger transverse kinetic energy. The model density operators q_0 sigma_j converge in L^3_x(S3); the density-transfer inequality can be applied to finite truncations and then passed to the limit with the same kinetic bound. Thus no finite-rank assumption about sigma is concealed in (26)–(27).

For the untruncated model, put lambda=pi c_bar. The sharp one-dimensional transverse gamma=3/2 inequality gives

    (integral rho_sigma^2 dy)^2
       <= (Tr sigma^3/3) T_y(sigma)
       <= (N/3)T_y(sigma).

Since integral q_0^2 dx=2lambda/pi^2 and T_x(gamma_0)=Nlambda^2/8,

    T(gamma_0)>= [pi^2 sqrt(6)/4] F(gamma_0).           (34)

The coefficient is approximately 6.044. This applies to the extracted common-profile mixed model. Transferring it to a general family still requires either the additional common-Gram hypothesis (23) or a proved general block-extraction theorem; the latter has not been obtained here.
