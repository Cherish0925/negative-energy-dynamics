# Nonstationary global negative-energy solutions with identical conserved charges

Research proof, 7 October 2026. This proof uses the exact four-dimensional cubic profile, the new complete angular certificate, and the Hamiltonian trichotomy established in [stability-theory.md](stability-theory.md). It is a nonlinear construction, not a sum of approximate profiles.

## Theorem

For each sufficiently small nonzero velocity v, fix the exact negative-energy wave exp(it) U_v(x-vt) of the companion construction. There is an integer d_s in {29,31}, a neighborhood B of zero in R^{d_s}, and a real-analytic injection a -> u_a(0) into H6(R4) such that:

1. Every u_a is an exact solution on [0,infinity), uniformly bounded in H6.
2. For constants eta>0 and C_v, depending on this fixed wave,

   || exp(-it) u_a(t, .+vt) - U_v ||_{H6} <= C_v |a| exp(-eta t).

3. M(u_a)=M(U_v), P(u_a)=P(U_v), and E(u_a)=E(U_v)<0 exactly.
4. The a=0 solution is the traveling wave; for a!=0 the solution is nonstationary in this fixed rotating/translating frame and is not another exact traveling wave.

The family is finite dimensional, not an open neighborhood of initial data. Forward global existence is asserted; backward global existence is not. Its existence is consistent with the orbital instability proved in the companion note.

## Functional framework

Write w(t,x)=exp(-it)u(t,x+vt)-U_v(x). Then

    w_t=A_v w+N_v(w),
    A_v=-i L_v,
    L_v h=(Delta^2+1+i v.grad)h-2|U_v|^2h-U_v^2 conjugate(h).

The nonlinearity N_v is quadratic plus cubic. The profile is in H^s for every finite s by elliptic bootstrap. X=H2 is the energy space. The form L_v has finite Morse index, finite kernel and a coercive positive complement. Lin-Zeng's Hamiltonian trichotomy therefore gives bounded commuting projections P_s,P_c,P_u. E_s and E_u are finite dimensional, dim E_s=dim E_u=d_s, and the center group has at most polynomial growth in both time directions.

Put Y=D(A_v:X->X)=H6 with its equivalent graph norm. Ellipticity of the principal fourth-order part proves this equality of spaces and norms. Since the projections commute with A_v, they are bounded on Y. The estimates on X lift to Y by applying each estimate to both w and A_v w. For some K, rho>0 and integer k>=0,

    ||exp(tA_v)P_s||_{Y->Y} <= K exp(-rho t), t>=0,
    ||exp(-tA_v)P_u||_{Y->Y} <= K exp(-rho t), t>=0,
    ||exp(tA_v)P_c||_{Y->Y} <= K(1+|t|^k), t real.

Polynomial factors on the finite hyperbolic blocks are absorbed by choosing rho strictly below their smallest nonzero exponential rate. This rho need not be uniform as v tends to zero.

H6(R4) is an algebra, so for ||w||_Y,||z||_Y <= r sufficiently small,

    ||N_v(w)||_Y <= C ||w||_Y^2,
    ||N_v(w)-N_v(z)||_Y <= C r ||w-z||_Y.

More specifically the Lipschitz estimate is C(||w||_Y+||z||_Y)||w-z||_Y; this gives the time-decay gain below. The map is real analytic. Local H6 existence and its continuation criterion follow directly from the C0 group and the locally Lipschitz nonlinearity.

## Lyapunov-Perron construction

Choose 0<eta<rho/2 and define

    W_eta={w in C([0,infinity),Y): ||w||_eta=sup_{t>=0} exp(eta t)||w(t)||_Y<infinity}.

For a in E_s define

    F_a(w)(t)=exp(tA_v)a
       + int_0^t exp((t-s)A_v) P_s N_v(w(s)) ds
       - int_t^infinity exp((t-s)A_v)(P_c+P_u) N_v(w(s)) ds.

All integrals converge in Y. To see both convergence and the contraction estimates, suppose ||w||_eta<=r. Then ||N_v(w(s))||_Y<=Cr^2 exp(-2eta s). The stable integral is bounded by

    KCr^2 exp(-2eta t)/(rho-2eta).

The unstable future integral is bounded by

    KCr^2 exp(-2eta t)/(rho+2eta).

The center future integral is bounded by

    KCr^2 exp(-2eta t) int_0^infinity (1+tau^k)exp(-2eta tau) dtau.

Their W_eta norms are therefore <=C_eta r^2. Applying the same estimates to the difference gives

    ||F_a(w)||_eta <= K||a||_Y+C_eta r^2,
    ||F_a(w)-F_a(z)||_eta <= C_eta r ||w-z||_eta.

For sufficiently small a the ball of radius 2K||a||_Y is invariant and F_a is a contraction. It has a unique fixed point w_a. This proves the asserted exponential estimate and global boundedness.

Subtracting the integral equations at two times shows that w_a obeys the usual Duhamel equation with initial value w_a(0). Thus it is a genuine solution, not only a formal solution of a terminal integral equation. Local uniqueness identifies it with the H6 Cauchy solution for all positive times. The bounded norm prevents finite-time breakdown.

At t=0,

    P_s w_a(0)=a,
    w_a(0)=a+h(a),  h(a) in E_c+E_u,  h(a)=O(||a||_Y^2).

The analytic implicit-function theorem on W_eta gives real-analytic dependence on a and hence the analytic graph h. Projection onto E_s proves injectivity. This is the local strong stable manifold with asymptotic phase and position fixed.

## Conservation, nonstationarity and dimension

The decay in H6 implies decay in H2. Mass, momentum and energy are continuous on H2 and are conserved by these smooth solutions. Taking t to infinity gives the three exact identities stated in the theorem. In particular every member has strictly negative energy, not merely energy close to the wave's energy.

If a!=0, the solution cannot be stationary in the rotating/translating frame: a constant w with exponential convergence to zero is identically zero, contrary to P_s w(0)=a. More generally another exact traveling wave cannot converge strongly to this particular profile in the prescribed frame unless its velocity, phase frequency, and profile coincide. Different velocities make the profiles separate spatially; a nonzero frequency mismatch has a nonconvergent relative phase; with matching parameters the profile difference is fixed. Thus these solutions are not other traveling waves obtained by shifting their parameters.

The new angular certificate gives a positive L_minus and one negative L_plus direction in every degree-2 and degree-3 angular channel at v=0. Their Hamiltonian pencils yield 9+16=25 unstable eigenvalues counted with multiplicity. The degree-one translation channels contribute four more: their total Morse index is two per channel and their generalized-zero quotient has negative index one because the response I is negative, so each channel has exactly one real unstable eigenvalue. Continuation therefore preserves at least 29 unstable dimensions for sufficiently small nonzero v. The complete index theorem gives dim E_u in {29,31}. Hamiltonian spectral symmetry gives dim E_s=dim E_u, establishing the parameter count used here.

## Consequences and limits

This supplies exact time-dependent, forward-global, negative-energy solutions in addition to the exact traveling waves. All share the same mass and momentum as their asymptotic wave, so it does not settle the zero-momentum problem.

The argument only needs a smooth cubic Hamiltonian profile with a finite-index Hessian, its associated exponential trichotomy, and a nonzero stable subspace. It therefore persists under sufficiently small cubic dispersion perturbations that preserve these properties. Combining such local persistence with the scaling in the previous supplement yields corresponding finite-dimensional nonstationary negative-energy families for every prescribed real symmetric quadratic dispersion matrix in four dimensions, with frequency free. The exponent-continuation result for stationary profiles alone does not justify applying this H6 algebra argument to arbitrary noninteger powers.

Source: Z. Lin and C. Zeng, Instability, index theorem, and exponential trichotomy for linear Hamiltonian PDEs, Memoirs AMS 275 (2022), no.1347; arXiv:1703.04016v4, Theorem2.2 and its graph-domain estimates. The contraction and charge identities above are explicitly proved here.
