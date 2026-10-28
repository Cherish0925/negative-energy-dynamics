# Round 13: Gaussian projection, conserved occupations, and critical dynamics

## Scope and result

Fix the SAME local critical system from rounds 11–12,

    i U_t = (a+b)(D) U - ||U||_H^(2r) U,
    r=m/N>0, kappa=1+r,
    F(U)=integral ||U||^(2kappa),
    E(U)=(A(U)+B(U))/2-F(U)/(2kappa),

where H is a separable complex Hilbert space, a is a positive homogeneous scalar symbol of degree m, b>=0 is a common scalar addition, and scalar sharp interpolation is

    F(f) <= kappa Mc^(-r) M(f)^r A(f).

No new dispersion or nonlinear interaction is introduced. The conclusions about evolution assume the conservative local flow and continuation property stated and verified for quartic N<=3 in round 12.

The new proof below averages the SCALAR sharp inequality over internal Gaussian projections. It yields:

1. An explicit full-spectrum nonlinear bound whose coefficient is conserved by the evolution and equals the exact scalar coefficient on rank-one fields.
2. For r>=1, an explicit quantitative polarization inequality controlling BOTH mass and kinetic distance, replacing the previous compactness-plus-transverse-spectral proof in this local range.
3. An explicit improved global boundedness region, including a calculable interval above the scalar mass Mc for every non-rank-one occupation spectrum.

The resulting coefficient is NOT claimed to be the optimal coefficient at each fixed spectrum. Determining that coefficient enters sharp orthonormal kinetic inequalities; it cannot be replaced by an uncomputed variational definition and described as solved.

## 1. Covariances and exact polarization distance

Put

    Gamma = integral |U(x)><U(x)| dx,
    Gamma_A = integral a(xi)|Uhat(xi)><Uhat(xi)| dxi,
    X = Gamma/M, Y=Gamma_A/A.

These are positive trace-class operators; Tr X=Tr Y=1. Gamma is conserved by the common scalar nonlinear flow. Gamma_A need not be conserved. Let lambda_1>=lambda_2>=...>=0 be the spectrum of Gamma, M=sum lambda_j, mu=lambda_1. Zero eigenvalues can be omitted.

The squared distance to one internal direction, in the normalized mass-plus-kinetic Hilbert norm, is exactly

    p(U) = inf_{||zeta||=1,q} [M(U-zeta q)/M + A(U-zeta q)/A]
         = 2-lambda_max(X+Y).

For fixed zeta the minimizing q is its pointwise scalar component <zeta,U>; the scalar kinetic multiplier commutes with this projection. Taking the largest eigenvalue of the positive compact operator X+Y gives the formula, also in infinite dimension.

## 2. Gaussian projection theorem: full occupation spectrum

Let Z_j be independent standard circular complex Gaussian variables, normalized by E|Z_j|^2=1, and let X_j=|Z_j|^2 be independent exponential variables of mean one. (The symbols X_j in this probabilistic formula are scalars, unrelated to the operator X above.) Define

    S = sum_j lambda_j X_j,
    B_r(Gamma) = E[X_1 S^r]/Gamma_Euler(r+2).

The random series is finite almost surely since E S=M<infinity. The moment in B_r is finite by Holder and Jensen, as proved below.

THEOREM. For every nonzero U in the energy space,

    F(U) <= kappa Mc^(-r) B_r(Gamma) A(U).                (2.1)

Moreover B_r is homogeneous of degree r in Gamma, depends only on its spectrum, and

    B_r(Gamma) <= M^r,

with equality if and only if Gamma has rank one. In the rank-one case B_r=mu^r=M^r exactly.

PROOF, FINITE RANK. Rotate the internal basis so Gamma is diagonal and put f_Z=sum_j Z_j u_j. Pointwise f_Z is a complex Gaussian with variance rho_U; hence

    E F(f_Z)=Gamma_Euler(r+2) F(U).

Also M(f_Z)=S. If K_{ij} is the kinetic Gram matrix, then A(f_Z)=sum conjugate(Z_i)K_{ij}Z_j. Phase averaging kills every i!=j term, giving

    E[S^r A(f_Z)] = sum_j A(u_j) b_j,
    b_j=E[X_j S^r].

Scalar sharp interpolation therefore gives

    Gamma_Euler(r+2) F(U)
      <= kappa Mc^(-r) sum_j A(u_j)b_j.

If lambda_i>=lambda_j, interchange X_i and X_j in half of the expectation. This gives

    b_i-b_j = (1/2)E[(X_i-X_j)(S^r-S_swap^r)] >=0,

because S-S_swap=(lambda_i-lambda_j)(X_i-X_j) and t->t^r is increasing. Thus b_1 is largest and (2.1) follows.

For the upper bound, Holder and convex Jensen at exponent r+1>1 give

    E[X_1 S^r]
      <= (E X_1^(r+1))^(1/(r+1)) (E S^(r+1))^(r/(r+1))
      <= Gamma_Euler(r+2) M^r.

If some lambda_j>0 for j>=2, S is not proportional to X_1 almost surely, so Holder is strict. If rank one, the displayed expression is exactly M^r E X_1^(r+1). This proves the equality assertion.

INFINITE RANK. Use the eigenbasis of Gamma and truncate to the first J components. Then U_J->U in H^s, F(U_J)->F(U), A(U_J)->A(U). The moment coefficients B_r(Gamma_J) increase to B_r(Gamma) by monotone convergence and are bounded by M^r. Passing to the limit proves (2.1), including all countably many components. This proof does NOT posit an H-valued Gaussian with identity covariance; all Gaussian projections are performed in finite rank before the limit.

## 3. Explicit mass and kinetic alignment, r>=1

The full Gaussian expectation is often stronger than the following completely explicit bound. Convex Jensen gives

    S^r <= M^(r-1) sum_i lambda_i X_i^r.

Consequently, since E X_i^(r+1)=Gamma_Euler(r+2) and E X_i^r=Gamma_Euler(r+1),

    b_j/Gamma_Euler(r+2)
       <= M^(r-1) [lambda_j +(M-lambda_j)/(r+1)].

Returning to the exact weighted kinetic sum rather than immediately taking its maximum yields

    F(U) <= kappa Mc^(-r) M^r A(U)
                       [1+r Tr(XY)]/(r+1).             (3.1)

Thus, for the sharp scalar deficit

    d(U)=1-F(U)/[kappa(M/Mc)^r A(U)],

we have

    d(U) >= r/(r+1) [1-Tr(XY)].                         (3.2)

For positive trace-one X,Y,

    lambda_max(X+Y) >= Tr[(X+Y)^2]/Tr(X+Y)
                   >= 2 Tr(XY),

where the last inequality is Tr[(X-Y)^2]>=0. Combining this with the exact p formula gives

    p(U) <= 2(r+1)/r * d(U).                            (3.3)

This controls the entire normalized mass-plus-kinetic distance, not only mass polarization. It requires no optimizer uniqueness, no real-sector nondegeneracy, no compactness theorem, and no transverse spectral lower bound. The scalar sharp inequality alone suffices.

Also Tr(XY)<=||X||op=mu/M, so

    F(U) <= kappa (M/Mc)^r [1-r/(r+1)(1-mu/M)] A(U).   (3.4)

The coefficient c=r/(r+1) is explicit. No optimality claim for this c is made. Unlike a fitted correction, the stronger expression (3.1) records the relative alignment of the mass and kinetic covariances.

## 4. Real Gaussian version and scalar phase control

For a real Hilbert-valued field, use independent real standard Gaussians G_j and X_j=G_j^2. Their moments are

    a_q=E X_j^q=2^q Gamma_Euler(q+1/2)/sqrt(pi),
    a_{r+1}=(2r+1)a_r.

The same finite-rank averaging proof is valid, with Gamma_Euler(r+2) replaced by a_{r+1}. For r>=1 it gives

    F(U)/[kappa(M/Mc)^r A(U)]
      <= [1+2r Tr(XY)]/(2r+1),
    p_real(U) <= (2r+1)/r * d(U).                       (4.1)

In particular a complex SCALAR field u is a real two-component field (Re u,Im u). A one-dimensional real internal direction is exactly a constant complex phase times a real scalar field. Thus (4.1) gives a constant theta and a real q with

    M(u-e^(i theta)q)/M(u) + A(u-e^(i theta)q)/A(u)
       <= (2r+1)/r * d(u).                             (4.2)

One may choose q as the real projection of e^(-i theta)u; the error is its imaginary part. This is an explicit replacement for the phase-smallness input used in round12's quartic near-critical argument when N<=4. The minimizing phase is chosen at each time; no differentiability of that phase is asserted or needed.

Careful distinction: the REAL covariance of (Re u,Im u) is generally not conserved. It is used only instantaneously in (4.2). The COMPLEX internal covariance Gamma of the genuine multicomponent system is conserved and is the one entering the dynamical theorem below.

## 5. Actual dynamics from the conserved spectrum

THEOREM. Suppose the common scalar system has the conservative energy-space local flow and continuation property. If

    B_r(Gamma(U_0)) < Mc^r,                             (5.1)

then its maximal solution is global in both time directions and

    sup_t A(U(t)) <= 2E(U_0)/(1-B_r(Gamma(U_0))/Mc^r),
    sup_t B(U(t)) <= 2E(U_0).

Proof: Gamma is conserved, and (2.1) gives

    E(U(t)) >= (1/2)[1-B_r(Gamma(U_0))/Mc^r] A(U(t))
                         +(1/2)B(U(t)).

Conservation and continuation prove the statement. A lower-order nonnegative b is allowed exactly as in round12; no homogeneity of b is required for this argument.

For r>=1 the easily evaluated sufficient condition is

    M^r [1-r/(r+1)(1-mu/M)] < Mc^r.                    (5.2)

For any fixed normalized spectrum p_j=lambda_j/M of rank>1, let

    beta_r(p)=B_r(Gamma)/M^r <1.

Then every initial field with that normalized spectrum and

    M < Mc beta_r(p)^(-1/r)

has global uniformly bounded flow. This interval is strictly larger than M<Mc and is explicitly specified by a scalar probabilistic moment of the conserved spectrum, not by an unknown variational extremum.

For quartic dispersion in N=1,2,3, the local conservative H2 theory from round12 makes these unconditional evolution statements. For other dimensions/orders the local theory hypotheses remain explicit.

Conversely, an orbit with unbounded energy norm must obey

    B_r(Gamma(U_0)) >= Mc^r.

At M=Mc strictness of the Gaussian moment bound forces rank Gamma=1. Conservation then implies U(t,x)=zeta u(t,x) for one fixed zeta throughout the maximal interval. This reproves round12's exact scalar reduction without quantitative polarization or profile compactness.

## 6. Computable full-spectrum formulas

For integer r, let h_r be the complete homogeneous symmetric polynomial. Exponential tilting by X_1 changes X_1 from Gamma(shape1) to Gamma(shape2), equivalently replaces lambda_1 by two identical independent exponential weights. Hence

    B_r(Gamma)=h_r(lambda_1,lambda_1,lambda_2,...)/(r+1).

For r=1:

    B_1=(M+mu)/2.

For r=2, including pure quartic N=2:

    B_2=[M^2+Tr Gamma^2+2Mmu+2mu^2]/6.                 (6.1)

For r=4, including pure quartic N=1, put p_k=Tr Gamma^k+mu^k. Then

    B_4=[p_1^4+6p_1^2 p_2+3p_2^2+8p_1 p_3+6p_4]/120.

For k equal positive occupations lambda_j=M/k,

    B_r/M^r = Gamma_Euler(k+r+1)
                 /[k^r Gamma_Euler(k+1) Gamma_Euler(r+2)].

For quartic N=2 and two equal occupations, B_2=M^2/2. Therefore every such orthogonal two-component datum of mass M<sqrt(2)Mc has global bounded H2 flow. This is an explicit consequence with the exact scalar Mc retained. It is stronger than (5.2), which only gives M<sqrt(3/2)Mc in this case.

For r>=1, holding lambda_1 and M fixed, B_r is symmetric and convex in the remaining occupations: for fixed exponential variables, S->S^r is convex, and averaging preserves convexity. Therefore spreading the remaining occupation mass by pairwise averaging does not increase B_r. Formula (6.1) shows strict sensitivity to Tr Gamma^2 in the quartic two-dimensional system. This is a rigorous refinement beyond merely knowing total mass and largest occupation, although it does not establish that the exact optimal threshold depends on all those moments.

## 7. What cannot follow: maximum occupation alone and sharp thresholds

There is an important distinction between the explicit bound just proved and an optimal fixed-spectrum threshold. The strongest possible inequality at fixed spectrum is a form of the orthonormal Lieb--Thirring variational problem. The Gaussian bound is an upper bound, not an evaluation of that variational problem.

Moreover the tempting assertion 'all focusing critical systems can blow up only if mu>=Mc' is FALSE. This already fails for the same common scalar / total-density system with standard second-order dispersion in spatial dimension N>=3.

Let K_1=inf ||grad f||2^2 / integral |f|^(2+4/N), under ||f||2=1, and let K_2 be the corresponding infimum over two orthonormal spatial modes, with numerator sum_j||grad f_j||2^2 and denominator integral (|f_1|^2+|f_2|^2)^(1+2/N). Scalar sharp GN gives K_1=Mc^(2/N)/(1+2/N).

Frank--Gontier--Lewin, arXiv:2002.04964v3, Theorem 2, prove L_{gamma,N}^{(2)}>L_{gamma,N}^{(1)} for gamma>max(0,2-N/2). At gamma=1 this applies to every N>=3. Legendre duality between the gamma=1 spectral inequality and the orthonormal kinetic-density inequality reverses the constants, hence K_2<K_1. Choose orthonormal smooth compactly supported f_1,f_2 with ratio K<K_1 and choose

    [(1+2/N)K]^(N/2) < mu < Mc.

Then U_0=sqrt(mu)(f_1,f_2) has Gamma=mu I_2 and

    E(U_0) = (mu/2) A(f_1,f_2)
               -mu^(1+2/N) F(f_1,f_2)/[2(1+2/N)] <0.

The strict variational inequality survives smooth approximation and exact Gram orthonormalization. The data have finite variance. The usual mass-critical vector NLS identity V''(t)=16E(U_0)<0 then gives finite-time blowup. Yet mu<Mc, while every rank-one datum at the SAME mu is globally bounded by scalar sharp coercivity.

This establishes that largest occupation alone cannot determine the exact spectrum-resolved global/blowup boundary across the whole model class. It is a rigorous consequence of established strict binding, not a new solution of the Lieb--Thirring conjecture and not a quartic blowup result. It does not justify claiming identical behavior for m=4, N<=3, where the necessary sharp rank dependence remains unproved here.

## 8. Literature and novelty status

Primary sources opened in this task:

- Frank, Gontier, Lewin, The nonlinear Schroedinger equation for orthonormal functions II: Application to Lieb--Thirring inequalities, https://arxiv.org/pdf/2002.04964 (Theorem 2, page 3; gamma=1 specialization above).
- Frank, Gontier, Lewin, Optimizers for the finite-rank Lieb--Thirring inequality, https://arxiv.org/abs/2109.05984 (later American Journal of Mathematics 147(2), 2025).
- Hong, Kwon, Yoon, https://arxiv.org/pdf/1712.06811 (already fully checked round12): conservation of component overlaps and density-matrix framework are prior work.

The Gaussian averaging proofs in Sections 2–6 were independently derived in this round. Initial searches did not locate this precise coefficient and covariance-alignment form. That is not an exhaustive priority determination. Scalar sharp interpolation, Gaussian moment formulas, Gram conservation, ordinary virial blowup, and finite-rank Lieb--Thirring strict binding are established ingredients and must remain credited as such.

The Gaussian identity used here is specifically for LOCAL powers. It does not automatically extend to Hartree: a Gaussian fourth-moment calculation produces an additional exchange term rather than twice the direct density interaction. No Hartree version is claimed in this note.
