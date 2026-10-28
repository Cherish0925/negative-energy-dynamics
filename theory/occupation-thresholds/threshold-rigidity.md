# Dynamics at the fixed-occupation collapse boundary

Date: 2026-10-09. This note proves dynamical consequences of the R16 separated-largest-occupation inequality and a global quantitative deficit estimate established below. It concerns the common-density system, not a system whose cross-phase coefficient is twice its self-phase coefficient. Its theorem describes every endpoint finite-time blowup in this occupation class. Existence of such solutions is established separately in [endpoint-construction.md](endpoint-construction.md); this note supplies their necessary structure and a rate bound.

## 1. Setup and theorem

Consider a finite-component H1 solution on its maximal forward interval [0,T):

    i partial_t u_j = -Delta u_j-rho u_j,
    rho=sum_j |u_j|^2,
    E=1/2 sum_j ||grad u_j||_2^2-1/4 integral rho^2.

The conserved Gram matrix can be diagonalized once, by a constant unitary change of the component coordinates. Work in that eigenbasis and assume

    <u_i,u_j>=0 (i!=j),
    ||u_1||_2^2=Mc,
    ||u_j||_2^2=Mc t_j (j>=2),
    epsilon=max_{j>=2}t_j<=epsilon_0,
    0<tau=sum_{j>=2}t_j<infinity,
    epsilon_0=min{1/96,delta0/(8C1),28/(6795 C1 K)}.

Here Mc=||Q||_2^2, -Delta Q+Q-Q^3=0, C1=2/Mc, and delta0,K are the normalized scalar GN stability constants proved in R15. This is the cutoff used in the global-deficit version of the R16 occupation-gap theorem. Zero-weight components are omitted. In normalized occupation variables, these assumptions are exactly M=M_*(p)=Mc/p_1 and p_2/p_1<=epsilon_0. The total secondary occupation tau has no smallness restriction. In particular, the largest Gram eigenvalue is simple, but the total mass M=Mc(1+tau) can be arbitrarily large.

Assume T<infinity is an H1 blowup time. Then the following statements hold.

**A. All unbounded kinetic energy belongs to the principal eigenmode.** Define

    lambda(t)=sqrt(Mc)/||grad u_1(t)||_2.

Then lambda(t)->0. On the entire lifespan,

    A_sec(t):=sum_{j>=2}||grad u_j(t)||_2^2 <=64E,
    0<=E_scalar(u_1(t))<=2E.                         (1)

For all sufficiently late times there are phase and center choices theta(t),x(t) such that

    ||lambda(t) exp(-i theta(t))
          u_1(t,x(t)+lambda(t) .)-Q||_{H1}^2
        <=(8K E/Mc) lambda(t)^2.                     (2)

K is the scalar normalized-GN stability constant in R15. In physical coordinates, the error from the modulated Townes profile has uniformly bounded gradient norm and L2 norm O(lambda). No time differentiability of the chosen modulation parameters is used.

**B. Exactly one Townes mass concentrates at one point.** There are a unique x_* in R2 and a nonnegative f with

    f in L1(R2) cap L2(R2),
    integral f=Mc tau,
    sqrt(f) in H1(R2),

such that, as t increases to T,

    x(t)->x_*,
    rho(t,x) dx -> Mc delta_(x_*)+f(x)dx

weakly as finite measures. More precisely,

    rho_sec(t):=sum_{j>=2}|u_j(t)|^2 -> f
       strongly in Lp(R2), every 1<=p<infinity,      (3)
    integral |grad sqrt(f)|^2 <=64E.

Thus the secondary modes cannot contribute an atom of concentrating mass. For every fixed R>0,

    integral_(|x-x(t)|<R lambda(t)) rho(t,x)dx
       -> integral_(|y|<R) Q(y)^2dy.                 (4)

For any r(t)->0 with r(t)/lambda(t)->infinity,

    integral_(|x-x(t)|<r(t))rho(t,x)dx -> Mc.         (5)

In the Gram eigenbasis the limiting local matrix of component masses in (5) is Mc e_1 e_1^*. In any original component basis it is Mc c c^*, where c is the normalized principal Gram eigenvector. The concentrated core is therefore completely coherent in the precise rank-one sense, even though the full field has nonzero secondary occupation.

In fact there is a unique secondary vector limit such that, for every 0<=sigma<1,

    (u_2(t),...,u_k(t))->(w_2,...,w_k)
       strongly in (H^sigma)^(k-1) and weakly in (H1)^(k-1),
    <w_i,w_j>=Mc t_i delta_ij,
    sum_{j>=2}|w_j|^2=f.                            (5a)

Thus the regular background retains the complete secondary occupation spectrum, not merely its total mass. Strong H1 convergence of the secondary fields is not asserted.

**C. A pseudoconformal lower bound on the blowup rate follows without a finite-variance assumption.** One has

    lambda(t)<=C(T-t),
    |x(t)-x_*|<=C(T-t),
    ||grad u_1(t)||_2 >= c/(T-t)                    (6)

for sufficiently late times. This is a one-sided rate bound, not a proof that lambda(t)/(T-t) has a nonzero limit. In particular it excludes the usual scalar log-log scale at this fixed-occupation boundary. It does not identify the solution with an exact pseudoconformal Townes solution: a diffuse background of mass Mc tau remains present.

No spatial radiality is assumed. All constants in the secondary kinetic estimate are independent of the number of components. The qualitative choice of a sufficiently late time can depend on the individual solution.

**Equivalent full-trajectory decomposition near T.** In the original component coordinates there is a fixed W in (H1)^k such that, through all times approaching T,

    U(t,x)=c exp(i theta(t)) lambda(t)^(-1)
                   Q((x-x(t))/lambda(t))+W(x)+R(t,x),
    ||R(t)||_(H^sigma)->0 for every 0<=sigma<1,
    sup_(t near T)||R(t)||_(H1)<infinity,
    c^* W(x)=0 almost everywhere,
    integral W W^* dx=Gamma-Mc c c^*.

The primary part of R has L2 norm O(lambda) and bounded gradient norm; interpolation makes its H^sigma norm O(lambda^(1-sigma)). The secondary part converges strongly in H^sigma by (5a). This gives the decomposition without selecting a time subsequence. It does not classify all possible phase or scale trajectories, nor assert strong H1 convergence of R.

## 2. Global energy control at the fixed-occupation endpoint

We first strengthen the R16 variational estimate to a global deficit bound. Normalize ||grad phi_1||_2^2=1, put B=sum t_j||grad phi_j||_2^2, delta=C1-integral |phi_1|^4, and let

    D=C1(1+B)-integral (|phi_1|^2+sum t_j|phi_j|^2)^2.

The R16 Fourier-cutoff kinetic estimate gives, with a=3epsilon,

    D>=delta+C1[(1-a)B-2sqrt(aB)].

We claim for every such orthonormal family that

    D>=delta/2+C1 B/32.                             (G)

Suppose instead that this bound fails, and write beta=31/32-a>=15/16. The crude estimate implies

    delta/2+C1[beta B-2sqrt(aB)]<0.

Since delta>=0, this forces

    B<4a/beta^2<(64/3)epsilon,
    delta<2C1 a/beta<8C1 epsilon<=delta0.

Scalar stability therefore applies. These two bounds are exactly sufficient for Sections 3 and 5 of r16_occupation_gap.md: weighted Bessel controls the projection error, and

    J<= (C1 K delta/2)sqrt(3epsilon B)
       <=4C1 K delta epsilon.

The refined R16 estimate consequently gives D>=delta/2+C1 B/32, a contradiction. This proves the global bound (G). There is no near-optimizer hypothesis in (G).

Now rescale a general physical field at the endpoint. Write u_1=sqrt(Mc) phi_1 and u_j=sqrt(Mc t_j) phi_j for j>=2, so that the phi_j are orthonormal. Put a_1=||grad phi_1||_2^2>0 and lambda=a_1^(-1/2). After applying the common spatial scaling, the normalized primary has kinetic norm one. Energy and scalar-primary energy scale quadratically. Multiplying (G) by Mc^2/(4lambda^2) yields the global physical inequality

    E(U)>=E_scalar(u_1)/2+A_sec/64.                  (7)

Scalar sharp GN gives E_scalar(u_1)>=0 because its mass is exactly Mc. Thus (7) proves both uniform bounds (1) for every time at which the solution exists. In particular E>0 for a genuinely non-pure spectrum.

The finite-time H1 blowup alternative implies total kinetic energy tends to infinity as t->T: otherwise bounded H1 states along times approaching T have a uniform local continuation interval beyond T. Since A_sec stays bounded by (7), ||grad u_1(t)||_2 tends to infinity and lambda(t)->0.

At each late time write

    psi_j(y)=lambda phi_j(x(t)+lambda y),
    B=lambda^2 A_sec/Mc,
    delta=C1-integral |psi_1|^4.

Energy conservation and (G) give

    4lambda^2 E/Mc^2>=delta/2+C1 B/32.

In particular

    delta<=8E lambda^2/Mc^2.                        (10)

This tends to zero, so normalized scalar stability applies directly and supplies theta(t),x(t). Its estimate ||exp(-i theta)psi_1-Q/sqrt(Mc)||_H1^2<=K delta proves (2). No extraction of a time subsequence is required.

One immediate useful estimate is

    || |u_1(t)|^2-lambda^(-2)Q^2((.-x(t))/lambda)||_1
       <=sqrt(32 K E) lambda.                       (11)

This is global L1 control of the primary intensity, including its tails.

## 3. Uniform control of the secondary density

The vector diamagnetic inequality and the R16 secondary kinetic bound give

    ||sqrt(rho_sec)||_2^2=Mc tau,
    ||grad sqrt(rho_sec)||_2^2<=A_sec,
    ||rho_sec||_2^2<=6epsilon A_sec<=384epsilon E.   (12)

In particular, for every center z and radius r,

    integral_(B(z,r))rho_sec
       <=sqrt(pi) r sqrt(384epsilon E).            (13)

Thus secondary mass in any ball of shrinking radius tends to zero uniformly in the ball's center and uniformly in late times. This is stronger than disappearance only after the blowup rescaling. Equations (11) and (13) already prove (4) and (5).

For each secondary component, Cauchy--Schwarz also gives

    ||u_1(t) conjugate(u_j(t))||_1 ->0.              (14)

To prove (14), split at a ball centered at x(t) of radius r(t), with r(t)->0 and r(t)/lambda(t)->infinity. The inside contribution tends to zero by (13), and the outside contribution by (11). The same estimates applied to a shrinking ball prove the rank-one local Gram assertion in Part B.

## 4. Phase positivity controls the density current

Define J=Im sum_j conjugate(u_j) grad u_j. The density satisfies

    partial_t rho+2 div J=0.                        (15)

Multiplication of every component by the same spatial phase preserves its complete Gram matrix, not just total mass. For a bounded smooth real theta with bounded gradient and every real s,

    E(exp(is theta)U)
       =E+s integral J.grad theta
          +(s^2/2) integral rho |grad theta|^2 >=0.  (16)

The final inequality follows from the sharp fixed-spectrum R16 inequality at the endpoint. The discriminant of this quadratic polynomial is nonpositive, giving

    |integral J.grad theta|^2
       <=2E integral rho |grad theta|^2.            (17)

Consequently

    |d/dt integral theta rho|
       <=sqrt(8E integral rho |grad theta|^2)
       <=sqrt(8EM)||grad theta||_infinity.          (18)

The identity is first proved for smooth states and tests and extended by H1 approximation. Equation (18) shows that the finite density measures are uniformly Lipschitz in the bounded-Lipschitz metric, even though the total kinetic energy diverges.

The common spatial phase is essential here. A phase imposed only on the primary component does not generally preserve off-diagonal Gram entries and cannot be inserted into (16).

## 5. A unique terminal point and a regular background

Equation (18) makes integral theta rho(t) Cauchy for each bounded Lipschitz theta. There is no loss of total mass to infinity: choose a cutoff chi_R equal to one in B(0,R), zero outside B(0,2R), with ||grad chi_R||_infinity<=C/R. Then

    integral chi_R rho(t)
       >=integral chi_R rho(0)-C sqrt(8EM) T/R.

Hence the measures rho(t)dx are tight uniformly in t<T and converge weakly to one finite measure mu_T of total mass M.

Their primary intensities carry mass Mc near x(t) on the vanishing scale lambda(t), by (11). Uniform tightness therefore keeps x(t) bounded. Given any sequence t_n->T, pass to a subsequence with x(t_n)->a. Equation (11) implies

    |u_1(t_n)|^2 dx ->Mc delta_a.

By (12), along a further subsequence rho_sec(t_n) converges weakly in L2 to some nonnegative f_a. Its measure limit is absolutely continuous. Thus

    mu_T=Mc delta_a+f_a dx.

The atomic part of a measure is unique. Therefore a is independent of the chosen subsequence: a=x_*, x(t)->x_*, and mu_T=Mc delta_(x_*)+f dx. Tightness and conservation of secondary mass show integral f=Mc tau.

First obtain strong convergence of the secondary density. By (12), sqrt(rho_sec(t)) is bounded in H1. On every bounded domain the compact embedding H1 into L4 implies precompactness of rho_sec(t) in L2. All subsequential local limits have already been identified as f, so the full trajectory converges strongly in L2_loc. Uniform tightness plus local L1 convergence gives strong L1 convergence globally. Weak H1 lower semicontinuity for sqrt(rho_sec) gives sqrt(f) in H1 and the Dirichlet bound stated in Part B.

For the more detailed assertion (5a), the secondary component fields are uniformly bounded in H1 by (1) and their conserved masses. Rellich compactness gives L2 convergence on every bounded set after a subsequence. Uniform tightness of rho_sec bounds all their L2 tails, upgrading this to strong global L2 convergence. Thus their full vector trajectory is L2-precompact.

There is a unique complex-field limit, not just subsequential convergence. To see this, let

    I_cross=integral |u_1|^2 rho_sec,
    F_sec=integral rho_sec^2.

The exact decomposition of the conserved energy gives

    I_cross=2E_scalar(u_1)+A_sec-F_sec/2-2E
       <=2E+A_sec <=66E.                          (24)

For each secondary j,

    integral |u_1|^2 |u_j|
       <=sqrt(Mc) sqrt(integral |u_1|^2 |u_j|^2)
       <=sqrt(Mc I_cross),
    integral rho_sec |u_j|
       <=||rho_sec||_2 ||u_j||_2.                  (25)

Fix any s>1. The embedding H^s(R2) into L_infinity, (25), and boundedness of grad u_j show directly from the equation that ||partial_t u_j||_(H^(-s)) is uniformly bounded near T. Hence u_j(t) has a unique strong H^(-s) limit as t->T. Every L2 subsequential limit must equal this limit, so L2-precompactness proves strong L2 convergence of the entire trajectory. Boundedness in H1 then gives weak H1 convergence and strong H^sigma convergence for every sigma<1 by interpolation.

The finite-dimensional Gram matrix passes to this limit unchanged. Its entries remain Mc t_i delta_ij. Two-dimensional Sobolev interpolation also gives strong L^q convergence of each field for every 2<=q<infinity; consequently rho_sec converges strongly in Lp globally for every 1<=p<infinity. Its limit is f=sum |w_j|^2. In the original component basis the full matrix-valued intensity measures therefore have the unique limit

    Mc c c^* delta_(x_*)+W(x)W(x)^* dx,
    integral W W^* dx=Gamma-Mc c c^*.

The vanishing of primary-secondary cross terms follows from (14). This is an exact splitting of the conserved occupation matrix between a rank-one singular core and a regular background, with a strong sub-H1 limit of all secondary fields.

## 6. Relative transport estimate and the blowup rate

Individual density measures need not have finite second moments. Use the extended relative quadratic transport cost

    W(mu,nu)^2=inf_{pi with marginals mu,nu}
                      integral |x-y|^2 d pi(x,y)

for measures of the same finite mass M. The value is allowed to be infinite initially; the argument below proves it is finite between two states on this trajectory. If both measures have finite second moments this equals sqrt(M) times the usual W_2 distance between their probability normalizations. No finite second moment is needed for the duality used below.

Equation (17) implies

    2 integral J.grad theta
       <=(1/2) integral rho|grad theta|^2+4E.       (19)

For a smooth Hamilton--Jacobi subsolution satisfying

    partial_t Phi+(1/2)|grad Phi|^2<=0,

the continuity equation and (19) give

    d/dt integral Phi(t)rho(t)<=4E.

Integrate on [t,s]. The Hamilton--Jacobi/Kantorovich dual formula for bounded Lipschitz endpoint potentials (proved below in precisely the needed generality) yields

    W(mu_t,mu_s)^2/(2(s-t)) <=4E(s-t),

or

    W(mu_t,mu_s)<=sqrt(8E)|s-t|.                    (20)

Fix t and let s increase to T. Transport plans between mu_t and mu_s with costs approaching the infimum are tight, because both families of marginals are tight. A weakly convergent subsequence has marginals mu_t and mu_T; lower semicontinuity of the nonnegative quadratic cost gives

    W(mu_t,Mc delta_(x_*)+f dx)^2<=8E(T-t)^2.       (21)

Here is an elementary extraction of the blowup rate from (21). Choose c0>0 so small that

    pi c0^2 ||Q||_infinity^2<Mc/4.

By (11) and (13), uniformly in z and at all sufficiently late times,

    mu_t(B(z,c0 lambda(t)))<=Mc/2.                 (22)

Every transport plan with target mu_T must send mass Mc to x_*. By (22), at least Mc/2 of this mass must originate at distance at least c0 lambda(t) from x_*. Therefore

    W(mu_t,mu_T)^2 >=(Mc/2)c0^2 lambda(t)^2.

Combined with (21), this gives lambda(t)<=C(T-t).

For the center, put h=T-t and choose a fixed R large enough that 8E/R^2<Mc/4. The mass sent to x_* from outside B(x_*,Rh) costs at least (Rh)^2 per unit mass. Thus (21) gives

    mu_t(B(x_*,Rh))>=3Mc/4.

By (13), the secondary contribution to this ball is o(1). By (11), there is a fixed L such that the primary intensity carries at least 3Mc/4 inside B(x(t),L lambda(t)). At late times the primary mass in B(x_*,Rh) exceeds Mc/2, so those two balls must intersect. Hence

    |x(t)-x_*|<=Rh+L lambda(t)<=C(T-t).

This proves (6) under H1 alone.

### Why bounded-test transport duality needs no second moment

For h>0 put c(x,y)=|x-y|^2/(2h), and define the Hopf--Lax operation

    Q_h psi(y)=inf_x [psi(x)+c(x,y)].

For any two finite measures of the same mass, the extended-cost formula is

    inf_pi integral c d pi
       =sup_(psi bounded Lipschitz)
             [integral Q_h psi d nu-integral psi d mu]. (23)

The right side is at most the left by integrating the defining inequality Q_h psi(y)-psi(x)<=c(x,y). For the reverse inequality, truncate the cost to c_N=min(c,N). This is a bounded continuous cost, globally Lipschitz in both coordinates. Its ordinary Kantorovich dual can be approached by bounded Lipschitz c_N-transformed potentials psi_N; their oscillation is at most N. Their c-transform for the full cost is at least their c_N-transform, so the right side of (23) is at least inf_pi integral c_N d pi for every N.

These truncated infima increase to the full infimum. Indeed, choose minimizing plans pi_N and extract a weakly convergent subsequence using compactness of the set of couplings with fixed finite marginals. For every fixed K, bounded continuity gives

    integral c_K d pi=lim_N integral c_K d pi_N
       <=lim_N inf_pi integral c_N d pi.

Then take K to infinity by monotone convergence. This proves the required reverse inequality and (23), including when either side is infinite.

For bounded Lipschitz psi, Phi(r,x)=Q_(r-t)psi(x) is bounded, Lipschitz in space and time, and satisfies the Hamilton--Jacobi equation almost everywhere. Convolution on interior time intervals gives smooth subsolutions because the Hamiltonian |p|^2/2 is convex; endpoint limits follow by uniform convergence. Thus it is an admissible limiting test in (19). Applying (23) proves (20) without introducing a finite-variance condition.

This use of Hopf--Lax duality and tight transport plans is standard optimal transport, not an originality claim for a new transport principle. The new input in this application is that fixed-spectrum endpoint energy is nonnegative under all common spatial phases even though total mass is greater than Mc.

## 7. Scope and relation to classical results

The mass concentration/normalized-Townes argument descends from classical scalar minimal-mass NLS theory. The phase-current discriminant estimate is the same mechanism used by Banica in critical-mass blowup analysis. What changes here is the invariant set: the complete non-pure Gram spectrum is fixed, total mass can be arbitrarily larger than Mc, and the sharp R16 occupation inequality still forces nonnegative energy after every common phase. The global deficit estimate additionally keeps all secondary kinetic energy bounded. The regular background and the rank-one concentrated atom follow from those two inputs together. The common-density structure preserves the full Gram spectrum and makes this stronger invariant set available.

These statements are newly derived consequences within this project. They have not been established here to be historically first theorems. This note proves the necessary structure of every endpoint finite-time blowup. The companion r16_endpoint_construction.md separately establishes that such non-pure endpoint blowups do exist, and that global solutions with the same spectrum also exist. Neither note proves exact pseudoconformal asymptotics for every threshold solution, all-time soliton resolution, scattering below the fixed-spectrum boundary, or the equal-occupation two-mode Lieb--Thirring endpoint.

Useful primary-source comparison checked on 2026-10-09:

* V. Banica, Remarks on the blow-up for the Schrodinger equation with critical mass on a plane domain, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (5) 3 (2004), 139--170. https://numdam.org/item/ASNSP_2004_5_3_1_139_0/ . The phase-current method and scalar critical-mass lower rate are prior work.
* X. Cheng, Z. Ma, J. Zheng, Classification of the minimal-mass blowup solutions to the two dimensional focusing cubic nonlinear Schrodinger system, arXiv:2504.01674v2 (30 April 2025), https://arxiv.org/pdf/2504.01674 . Its equation on p.1 has F_j=2rho u_j-|u_j|^2u_j. This is not the common-density F_j=rho u_j system used here; its theorem fixes the unconstrained total-mass scattering threshold, not the complete Gram spectrum. Therefore its stated classification does not directly imply the present endpoint assertions.

Independent internal analytic audit on 2026-10-09 by the rank2_global_structure branch checked the phase-current identity, unnormalized transport coefficient, truncated-cost duality without second moments, concentration argument, and the added complex-field limit proof (24)--(25). Those checks found no remaining gap.
