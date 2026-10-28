# Uniform robust obstruction for mixed quadratic–quartic cubic dispersion

Research derivation, 2026-10-18. This combines the anisotropic mass-gap theorem with the moment-free residual theorem. It is a genuine joint extension: the coefficient of positive quadratic dispersion is arbitrary, and the energy is measured in the quadratic momentum rest frame. The proof does not assume optimizer uniqueness, real-sector nondegeneracy or a spatial moment.

## Statement

Let x in R, y in R^2, and let K be any real symmetric positive-semidefinite 2 x 2 matrix. Define

    a(xi,eta)=xi^2+|eta|^4,
    A(U)=||partial_x U||_2^2+||Delta_y U||_2^2,
    B_K(U)=int eta^T K eta |Uhat(xi,eta)|^2 dxi deta,
    E_K(U)=(A(U)+B_K(U))/2-||U||_4^4/4,
    M(U)=||U||_2^2,
    H_a={U:M(U)+A(U)<infinity}.

The scalar coefficient case is K=mu I, mu>=0. Let Mc be the sharp principal critical mass:

    ||U||_4^4 <= 2 (M(U)/Mc) A(U).

Define the frame-invariant energy

    E_int,K(U)=E_K(U)-P_x(U)^2/(2M(U)),
    P_x(U)=Im int bar U partial_x U.

For U nonzero, set k=P_x(U)/M(U) and V=e^(-ikx)U. Then P_x(V)=0, M(V)=M(U), and E_K(V)=E_int,K(U).

There exist delta>0 and C<infinity depending only on the principal model, independent of K>=0, omega and v, such that whenever

    A(V)=1, Mc<=M(U)<=Mc+delta, E_int,K(U)<0,

one has

    |E_int,K(U)| <= C inf_{omega,v_x,v_y}
          ||R_{K,omega,v}(V)||_{H_a^*},                  (1)

where

    R_{K,omega,v}(V)
      =[-partial_x^2+Delta_y^2+D_y^T K D_y+omega
                    +i v_x partial_x+i v_y.grad_y]V-|V|^2V,

and the dual norm has Fourier denominator 1+xi^2+|eta|^4.

Without the normalization A(V)=1, the equivalent estimate is

    |E_int,K(U)| <= C inf_{omega,v}
       [int |Rhat_{K,omega,v}(V)(xi,eta)|^2
             /(1+(xi^2+|eta|^4)/A(V)) dxi deta]^(1/2).    (2)

No estimate for an uncentered, unshifted Fourier residual norm is being claimed; the centering boost and the displayed norm are part of the statement.

## Proof

### 1. Exact quadratic rest frame

For k=P_x(U)/M(U), direct differentiation gives

    P_x(e^(-ikx)U)=P_x(U)-kM(U)=0,
    A(e^(-ikx)U)=A(U)-P_x(U)^2/M(U),
    E_K(e^(-ikx)U)=E_K(U)-P_x(U)^2/(2M(U)).

All y terms and the nonlinear term are invariant under this boost. If an original profile residual is used, the parameters transform by

    v_x' = v_x-2k,
    omega' = omega+k^2-v_x k,
    v_y'=v_y,

and R(U)=e^(ikx)R'(V). Since the infimum is over all real parameters, the parameter transformation causes no restriction. We work with the centered V from now on.

### 2. Negative energy forces the normalized lower-order coefficient small

Write d=M(V)/Mc-1. At A(V)=1, principal GN implies

    E_K(V) >= (B_K(V)-d)/2.

Consequently

    0<=B_K(V)<d,
    |E_K(V)|<=d/2,
    2<||V||_4^4<=2(1+d).

As d tends to zero, V approaches the normalized principal optimizer family G in H_a, modulo translation and phase. Every member Q of G is real after a constant phase and solves

    (-partial_x^2+Delta_y^2+omega_c)Q-Q^3=0,
    omega_c=1/Mc.

For a real optimizer Q, define its y-gradient covariance matrix

    C_Q,ij=Re int partial_{y_i}Q partial_{y_j}Q.

It is positive definite. Otherwise a nonzero vector e would satisfy e.grad_y Q=0, forcing an L^2 function on R^3 to vanish. The map Q->C_Q is continuous in H_a: the y-gradient is controlled by the L^2 norm and the y second derivative. Compactness of G modulo translations and phases therefore gives C_Q>=c I uniformly over normalized optimizers. For V sufficiently close to G,

    C_V>= (c/2)I,
    B_K(V)=tr(K C_V)>= (c/2)tr K.

Thus

    ||K|| <= tr K <= C d.                               (3)

In particular, mu<=C d in the scalar case. This is stronger than merely knowing B_K(V) is small and is what makes the arbitrary-coefficient residual argument uniform.

### 3. Uniform control of frequency and velocity

In a normalized optimizer chart V=Q+h, the real-linear map

    (alpha,b_x,b_y) -> alpha Q+i b_x partial_x Q
                                      +i b_y.grad_y Q

is injective into H_a^*. Real and imaginary parts separate, and a nonzero L^2 function cannot be invariant along a nonzero direction. All first derivatives map H_a continuously into H_a^*. The cubic map is C^1 from H_a to H_a^*. Hence, with rho=||R_{K,omega,v}(V)||_{H_a^*}, absorption for h small gives

    |omega-omega_c|+|v_x|+|v_y|
            <= C(rho+||h||_{H_a}+||K||).                (4)

For rho larger than a fixed small rho_0, (1) already follows from |E_K(V)|<=d/2. For rho<rho_0, (3), (4) and delta sufficiently small place all parameters in a fixed small neighborhood of (omega_c,0,0,0), uniformly in the original K.

### 4. The same bordered reduction, now with K as a parameter

At (Q;omega_c,0,0,0), the derivative of R in V is the real selfadjoint Fredholm operator

    L=diag(a(D)+omega_c-3Q^2, a(D)+omega_c-Q^2).

The multiplication form Q^2 is relatively compact by local anisotropic Rellich compactness and the H_a->L^4 embedding. Choose C_c^infinity test functions chi_j pairing nondegenerately with ker L. The bordered system

    R_{K,omega,v}(W)+sum_j c_j chi_j=g,
    <W-Q,chi_j>=z_j

has a local C^1 inverse for (W,c), uniformly for small (K,omega-omega_c,v,z,g). The real symmetric K parameter may be allowed on both sides of zero for this local inverse; the actual theorem retains K>=0.

Set z_j=<V-Q,chi_j>. At g=R(V) its solution is (V,0). At g=0 its solution (W,c) satisfies

    ||W-V||_{H_a}+|c| <= C rho,
    f:=R_{K,omega,v}(W)=-sum_j c_j chi_j,
    ||f||_{H_a^*}<=C rho.                              (5)

It is neither necessary nor asserted that W has zero x momentum. Since V has zero x momentum and P_x is a locally Lipschitz quadratic form on H_a,

    |P_x(W)|<=C rho.                                   (6)

### 5. Anisotropic scaling gives a uniform dilation-domain bound

Let

    T_lambda W(x,y)=lambda^2 W(lambda^2 x,lambda y),
    Lambda_a=2+2x partial_x+y.grad_y.

The correct parameter scaling is

    omega_lambda=lambda^4 omega,
    (v_x)_lambda=lambda^2 v_x,
    (v_y)_lambda=lambda^3 v_y,
    K_lambda=lambda^2 K.

Then

    R_{K_lambda,omega_lambda,v_lambda}(T_lambda W)
                       =lambda^4 T_lambda f.

As in the homogeneous residual proof, (T_lambda W,c) solves the bordered system with smooth parameter path

    z_lambda,j=<W,T_lambda^(-1)chi_j>-<Q,chi_j>,
    g_lambda=sum_j c_j[chi_j-lambda^4 T_lambda chi_j],

and the scaled K,omega,v above. All of these are C^1 in lambda because chi_j is smooth and compactly supported. Continuity of T_lambda W in H_a plus local IFT uniqueness identifies it with the C^1 solution curve. Therefore

    Lambda_a W in H_a,  ||Lambda_a W||_{H_a}<=C.          (7)

No moment or spatial weight of V or W was assumed.

### 6. Phase coercivity and the residual dilation identity

Rotate W=X+iY so <Y,Q>=0. The principal phase form is uniformly coercive on Q-perp in the fixed chart. Adding D_y^T K D_y is nonnegative, so

    <Y,L_WY>>=c||Y||_{H_a}^2,
    L_W=a(D)+D_y^T K D_y+omega-|W|^2.

The imaginary equation gives

    <Y,L_WY>=(v_x P_x(W)+v_y.P_y(W))/2+<Y,Im f>.         (8)

For S=E_K+omega M/2-v.P/2, differentiate the anisotropic scaling at fixed K. Since the principal kinetic and quartic terms have degree four and B_K has degree two,

    Re<f,Lambda_a W>
       =4E_K(W)-B_K(W)-v_x P_x(W)-v_y.P_y(W)/2.         (9)

Combining (8), (9),

    4E_K(W)=B_K(W)+<Y,L_WY>+v_x P_x(W)/2
                            -<Y,Im f>+Re<f,Lambda_a W>.

The first term is nonnegative. The second term absorbs <Y,Im f> by Young's inequality. Equations (4), (6) bound the x-momentum error by C rho, and (7) bounds the final pairing by C rho. Thus

    E_K(W)>=-C(rho+rho^2).

Since K is uniformly small in the normalized chart, E_K is locally Lipschitz on H_a with a uniform constant. Equation (5) gives E_K(V)>=-C rho. This proves (1). A finite cover of the compact optimizer family makes all constants uniform.

Finally, for general A(V)>0 use lambda=A(V)^(-1/4). The scaled coefficient is K_lambda=lambda^2 K>=0, and the scaled energy and residual are lambda^4 E_K(V), lambda^4 T_lambda R. Fourier change of variables gives exactly (2).

## Consequences and scope

* Taking residual zero recovers the anisotropic negative-internal-energy traveling-profile mass gap, uniformly over every K>=0. This is now a corollary of one robust theorem.
* The scalar case covers every mu>=0 without moment assumptions. It does not assume the existence of any negative-energy traveling profile for this mixed model.
* In normalized variables, negative internal energy near Mc forces ||K||<=C d. Restoring scaling yields the necessary principal-kinetic scale bound

      A(e^(-iP_x x/M)U) >= c ||K||^2/d^2

  for K nonzero. In particular A>=c mu^2/d^2 when K=mu I. This is a necessary intensity/scale condition, not an existence or blowup theorem.
* For K=0, amplitude perturbations of a real optimizer give negative energy and residual both of order epsilon, so the linear energy power cannot be improved uniformly over the coefficient class.
* The same proof works with a positive even elliptic quartic polynomial b(eta) replacing |eta|^4, using the already established anisotropic optimizer and phase-coercivity foundations. More general n_2,n_4 and their corresponding mass-critical powers are also compatible with the bordered argument; the displayed theorem is stated in the concrete three-variable cubic case to keep its physical content explicit.
* A residual lower bound measures forced deformation relative to phase/translation motion. It does not by itself imply finite-time blowup, finite residence time, or exclusion of recurrent bounded dynamics.
