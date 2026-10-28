# Robust profile gap from a moment-free bordered reduction

## Relation to previous work

This proof derivation has received a separate internal mathematical check, recorded in `robust_gap_independent_review.It uses the project's already established optimizer compactness and phase coercivity. The actual R9 text has been checked (PDF: BNLS_Dilation_Structure_and_Profile_Gaps_20261008, Theorem 3.3, pp. 12–13).

At A=1, R9 Theorem 3.3 proves

    v.P >= c|v|^2-C rho^2,
    rho=||R||_{H^-s}.

To infer an energy lower bound rho^2 >= c_theta(|E|+|v|^2), R9 additionally assumes the scalar dilation defect

    D=mE-v.P/2 >= -theta*m|E|, 0<=theta<1.

The new theorem below removes that extra defect assumption entirely and concludes rho >= c|E|. These are complementary statements: the old theorem is stronger in the power of |E| on its restricted class; the new theorem holds for every nearcritical negative-energy state. An amplitude-increased real optimizer has v=0, D=mE=-m|E|, so it is excluded by every theta<1 in the old energy estimate while being covered by the new theorem. It also makes the linear power optimal.

The bordered implicit-function construction and scaling covariance are the new mechanism in this derivation. Neither the old nor the new residual speed estimate alone implies finite-time blowup or finite residence in a bounded neighborhood.

## Theorem

Let m>1, s=m/2, N>=1, p=2+2m/N. Let a be a real even positive elliptic m-homogeneous symbol in the previously established symbol class. Set

    A(U)=int a(xi)|Uhat(xi)|^2 dxi,
    M(U)=||U||_2^2,
    E(U)=A(U)/2-||U||_p^p/p.

Let Mc be the sharp critical mass. Assume the already proved foundations: normalized optimizer compactness, real constant-phase optimizers, and phase-sector coercivity. Then there exist delta>0 and C<infinity such that every U in H^s with

    A(U)=1, Mc <= M(U) <= Mc+delta, E(U)<0

satisfies, for every real omega and every v in R^N,

    |E(U)| <= C ||R_{omega,v}(U)||_{H^-s},                 (1)
    R_{omega,v}(U)=a(D)U+omega U+i v.grad U-|U|^(p-2)U.

No spatial moment of U is assumed. No uniqueness of optimizers and no real-sector nondegeneracy are assumed. Constants depend on the fixed symbol and dimension and are not presently explicit.

The H^-s norm can be defined with Fourier denominator 1+a(xi), equivalent to the ordinary Sobolev norm.

## Proof

### 1. Normalized ground-state charts and parameter control

Let G denote the normalized optimizer set: A(Q)=1, M(Q)=Mc, E(Q)=0. It is compact modulo phase and translation. Every Q is real after phase rotation and solves

    a(D)Q+omega_c Q-|Q|^(p-2)Q=0,
    omega_c=(m/N)/Mc.

Sharp GN gives

    -1/2[(M(U)/Mc)^(m/N)-1] <= E(U)<0.

Thus delta small forces U, modulo translation and phase, uniformly close to G in H^s. Fix a ground-state chart U=Q+h.

The real-linear finite-dimensional map

    (alpha,b) -> alpha Q+i b.grad Q

is injective R x R^N -> H^-s. Its real and imaginary parts decouple, and a nonzero L^2 function cannot have zero derivative along a nonzero direction. Hence its norm is bounded below by c_Q(|alpha|+|b|). Since m>1, grad:H^s -> H^-s is bounded. Local C^1 continuity of the nonlinearity yields, after absorbing the parameter terms multiplying h,

    |omega-omega_c|+|v|
       <= C_Q (||R_{omega,v}(U)||_{H^-s}+||h||_{H^s}).      (2)

Take a finite chart cover of G. All constants can be chosen uniformly over this cover.

If rho=||R(U)||>=rho_0 for a fixed small rho_0, (1) follows directly from |E(U)|<=C delta. In the remaining regime choose delta and rho_0 small: (2) places (U,omega,v) in a small fixed neighborhood of (Q,omega_c,0).

### 2. A bordered implicit function theorem

Work over real Banach spaces H^s(C), H^-s(C). Define F(U;omega,v)=R_{omega,v}(U). Its derivative at (Q;omega_c,0) is

    L=diag(L_+,L_-),
    L_+=a(D)+omega_c-(p-1)|Q|^(p-2),
    L_-=a(D)+omega_c-|Q|^(p-2).

The potential is compact relative to a(D)+omega_c, so L:H^s -> H^-s is selfadjoint Fredholm of index zero. Let K=ker L, which is finite-dimensional; its dimension is not assumed to equal the number of symmetries.

Choose complex-valued smooth compactly supported functions chi_1,...,chi_k such that the real pairing matrix between chi_j and a basis of K is invertible. Density of C_c^infinity guarantees this choice. The bordered operator

    (h,c) -> (Lh+sum_j c_j chi_j, (<h,chi_j>)_j)

is an isomorphism H^s x R^k -> H^-s x R^k. Indeed projection onto K first determines c; the range equation determines h modulo K; the final k constraints determine the K component.

The C^1 implicit function theorem therefore uniquely solves

    F(V;omega,v)+sum_j c_j chi_j=g,
    <V-Q,chi_j>=z_j,                                     (3)

for (V,c) near (Q,0), as a C^1 function of (omega,v,z,g) near (omega_c,0,0,0).

For the original U, let z_j=<U-Q,chi_j>. The solution of (3) at g=F(U) is (U,0). Let (V,c) instead be the solution at g=0. Uniform local inverse bounds imply

    ||U-V||_{H^s}+|c| <= C rho,
    F(V)=-sum_j c_j chi_j,
    ||F(V)||_{H^-s} <= C rho.                            (4)

Thus V is close to U at cost O(rho), and its residual belongs to a fixed smooth, localized finite-dimensional space.

### 3. Scaling covariance supplies the missing dilation regularity

This is the useful step: no spatial-moment or weighted-regularity theorem is required.

Let T_lambda f(x)=lambda^(N/2)f(lambda x). Homogeneity and mass-criticality give

    F(T_lambda V; lambda^m omega, lambda^(m-1)v)
        = lambda^m T_lambda F(V).

Consequently (T_lambda V,c) solves the same bordered system (3) with parameters

    omega_lambda=lambda^m omega,
    v_lambda=lambda^(m-1)v,
    z_lambda,j=<V,T_lambda^(-1)chi_j>-<Q,chi_j>,
    g_lambda=sum_j c_j[chi_j-lambda^m T_lambda chi_j].     (5)

These parameters are C^1 in lambda. This follows because the test functions chi_j are smooth and compactly supported; it does not require differentiating V. The curve T_lambda V is initially known only to be continuous in H^s, so it stays in the local uniqueness neighborhood for lambda near 1. By uniqueness in the bordered IFT it must equal its C^1 solution curve with the parameters (5). Therefore

    Lambda V=(N/2+x.grad)V belongs to H^s,
    ||Lambda V||_{H^s} <= C,                             (6)

uniformly in the fixed chart. The derivative bounds in (5) are controlled by ||V||_2, |c|, |omega| and |v|, all uniformly bounded. This argument also proves dilation-domain regularity for an exact nearby stationary point without assuming a moment in advance.

### 4. Phase coercivity plus the exact defect identity

Rotate V by a constant phase so V=X+iY, X,Y real, and <Y,Q>=0. This changes neither its energy nor the residual norm or (6). Because V and omega remain close to Q and omega_c, the proved phase coercivity is stable under form perturbation:

    <Y,B_V Y> >= c ||Y||_{H^s}^2,
    B_V=a(D)+omega-|V|^(p-2).

Put f=F(V). The imaginary equation f_I=B_VY+v.grad X gives, with P(V)=Im int bar V grad V,

    <Y,B_VY> = v.P(V)/2 + <Y,f_I>.                       (7)

The action S=E+omega M/2-v.P/2 is C^1 on H^s and has derivative F. The now legitimate H^s scaling differentiation, using (6), gives

    mE(V)-v.P(V)/2 = Re<f,Lambda V>.                     (8)

Combine (7) and (8):

    mE(V)=<Y,B_VY>-<Y,f_I>+Re<f,Lambda V>.

Hence

    E(V) >= -C(||f||_{H^-s}+||f||_{H^-s}^2).

On the bounded H^s chart, E is locally Lipschitz. Together with (4), this yields E(U)>=-C rho. This proves (1). The finite cover of G supplies uniform constants without any optimizer-uniqueness or real-kernel hypothesis.

## Scale-invariant formulation

For arbitrary A(U)>0 let lambda=A(U)^(-1/m). Since A(T_lambda U)=1,

    |E(U)| <= C [ int |Rhat(xi)|^2/(1+a(xi)/A(U)) dxi ]^(1/2). (9)

Equivalently, |E|/A is bounded by C/A times the displayed residual norm. The parameters in the normalized equation are omega_lambda=lambda^m omega and v_lambda=lambda^(m-1)v.

## Optimal exponent

Amplitude perturbations (1+epsilon)Q, normalized back to A=1, have negative energy of order epsilon and residual of order epsilon at a suitable bounded frequency. Thus no inequality rho>=c|E|^beta can hold uniformly with beta<1. The exponent 1 in (1) is the strongest compatible power. This corrects the tentative exponent direction in the task prompt.

## Dynamics: the exact consequence and the remaining obstruction

For an actual solution written as u(t,x)=e^{i theta(t)}U(t,x-a(t)),

    R_{theta',a'}(U)=i partial_t U.

The theorem therefore gives a lower bound on deformation speed modulo phase and translation. Unlike a qualitative exact-profile gap, it rules out arbitrarily accurate negative-energy traveling pseudoprofiles with residual small relative to their energy.

It still does NOT prove finite-time exit from a bounded neighborhood: a curve may have nonzero speed and remain on a closed orbit. It gives a cumulative path-length bound, not a signed displacement. A lifetime theorem needs a monotone observable or a dynamical reduction that excludes recurrence. This is precisely the distinction already emphasized in the R10 audit.

A uniform centered dilation-moment bound plus a negative-energy virial identity can yield a finite residence bound, but that is a standard additional localization hypothesis. Neither H^s boundedness nor the exact traveling-profile mass gap supplies that hypothesis automatically.

## Meaning for the first research class

The result extends the uniform mass-gap mechanism from exact coherent structures to a robust functional obstruction for all nearcritical negative-energy states, with arbitrary frequency/velocity and no spatial moment. The proof device is the bordered reduction plus scaling covariance; it avoids both a real-sector nondegeneracy assumption and a direct unjustified dilation test on a rough state.

The R9 comparison is complete as stated above. The separate internal check supplies the full C1 nonlinearity and compact-potential arguments and verifies the bordered scaling argument and chart uniformity. No finite-time blowup, full soliton resolution, numerical gap constant, or publication priority follows from this note.
