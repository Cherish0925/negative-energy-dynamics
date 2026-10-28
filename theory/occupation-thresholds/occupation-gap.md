# Exact critical threshold with a separated largest occupation

Date: 2026-10-09. Main R16 analytic development. This note replaces the R15 small-total-secondary-occupation condition by a condition on the ratio of the two largest occupations. The number of secondary modes and their total occupation do not enter the smallness constant. The proof uses the already certified Townes envelope through the explicit homogeneous gap in r16_quantitative_gap.md, and the normalized scalar GN stability lemma proved in Appendix A of r15_imbalanced.md. Historical priority is not asserted.

## Theorem

Let Q be the two-dimensional positive radial solution of -Delta Q+Q-Q^3=0. Put Mc=||Q||_2^2, q=Q/sqrt(Mc), C1=2/Mc. Let delta0,K>0 be constants in the scalar stability statement:

    ||phi||_2=||grad phi||_2=1,
    delta=C1-integral |phi|^4<=delta0
      implies inf_{theta,y}||phi-exp(i theta)q(.-y)||_{H1}^2<=K delta.

The R15 appendix proves that such constants exist. Set

    epsilon0=min{1/96, delta0/(8C1), 28/(6795 C1 K)}.  (T0)

For every finite or countably infinite orthonormal family in H1(R2), with occupations

    n_1=1,  0<=n_j<=epsilon0 for j>=2,

assume finite kinetic energy, and in the countable case finite total occupation. Then

    integral (sum_j n_j|phi_j|^2)^2
       <= C1 sum_j n_j||grad phi_j||_2^2.             (T1)

The optimal constant is exactly C1. If any secondary occupation is positive, the supremum is not attained. Every optimizing sequence, normalized so that the primary kinetic norm is one, has a scalar Townes primary core after translation and phase, while its total secondary kinetic energy and local secondary density tend to zero.

In fact a global remainder holds for every family, with no closeness or small-deficit assumption. In the normalization ||grad phi_1||_2=1, put delta=C1-integral|phi_1|^4 and B=sum_{j>=2}n_j||grad phi_j||_2^2. Then

    C1(1+B)-integral(sum_j n_j|phi_j|^2)^2
       >=delta/2+(C1/32)B.                           (T3)

Section 7 proves this stronger statement. The second entry in (T0) has been halved from the preliminary version precisely to obtain this global remainder.

The condition is epsilon=max_{j>=2}n_j<=epsilon0, not a bound on sum_{j>=2}n_j. For normalized occupations p_1>=p_2>=... with sum p_j=1, it becomes

    p_2/p_1<=epsilon0,
    C(p)=p_1 C1,
    M_*(p)=Mc/p_1.                                  (T2)

Thus p_1 itself may be arbitrarily small when the number of weakly occupied modes grows. The permitted spectra are not limited to almost-pure states. For finite rank, the strict-side NLS consequences established in R14 apply: all data of the specified occupation spectrum are global with bounded H1 kinetic norm below M_*, and smooth compactly supported data with that exact spectrum and finite-time blowup exist above M_*. No assertion that all above-threshold data blow up, or that all threshold dynamics have been classified, is made.

## 1. A self-contained kinetic bound for the secondary density

Let gamma=sum_j t_j |phi_j><phi_j| with 0<=gamma<=epsilon I, density S, and kinetic energy B=Tr(-Delta gamma). The following nonsharp, classical type of fermionic kinetic estimate is enough:

    integral S^2 <= (3 epsilon/(2 pi))B.              (1)

Here is a direct Fourier-cutoff proof, included so that no sharp Lieb--Thirring input is required. Let P_{<=E} be the Fourier projection onto |xi|^2<=E. The diagonal of its kernel is E/(4pi). Bessel's inequality gives

    sum_j t_j |P_{<=E}phi_j(x)|^2 <= epsilon E/(4pi).

The Hilbert-space triangle inequality, applied to the vector with components sqrt(t_j)phi_j(x), gives

    S_{>E}(x):=sum_j t_j |P_{>E}phi_j(x)|^2
      >= (sqrt(S(x))-sqrt(epsilon E/(4pi)))_+^2.

Integrating E and using the spectral layer-cake formula for B yields

    B=integral_0^infty integral S_{>E}(x) dx dE
      >= integral [4pi S(x)^2/epsilon]
                  integral_0^1(1-sqrt(s))^2 ds dx
      = (2pi/(3epsilon)) integral S^2.

Approximation handles infinite rank and finite kinetic energy. The constant in (1) is not claimed sharp or original.

The Gaussian trial in scalar sharp GN, together with the fact that a Gaussian is not an optimizer, gives Mc<4pi. Therefore a convenient weaker form of (1) is

    integral S^2 <= 3 C1 epsilon B.                  (2)

For epsilon=0 there is no secondary density, and the theorem reduces to scalar sharp GN. Below assume epsilon>0.

## 2. Any violation forces a nearly optimal primary mode

A common mass-preserving spatial scaling normalizes ||grad phi_1||_2^2=1. Put

    delta=C1-integral |phi_1|^4,
    S=sum_{j>=2}n_j|phi_j|^2,
    B=sum_{j>=2}n_j||grad phi_j||_2^2,
    a=3epsilon.

By (2), Cauchy--Schwarz, and scalar GN,

    integral (|phi_1|^2+S)^2
      <= C1-delta+2C1 sqrt(aB)+C1 aB.

If (T1) failed, then

    B<4a/(1-a)^2=12epsilon/(1-3epsilon)^2,
    delta<C1 a/(1-a).                                (3)

For epsilon<=1/96, in particular epsilon<=1/12, the last bound gives delta<4 C1 epsilon<=delta0. After applying the common translation and the primary phase, write

    phi_1=q+eta,  ||eta||_{H1}^2<=K delta.            (4)

No factor involving the secondary trace appears in (2)--(4).

## 3. Weighted Bessel replaces the secondary trace

For j>=2, let alpha_j=<q,phi_j> and chi_j=phi_j-alpha_j q. Orthogonality to phi_1 gives alpha_j=-<eta,phi_j>. Consequently

    sum_{j>=2} n_j |alpha_j|^2
       <= epsilon sum_{j>=2}|<eta,phi_j>|^2
       <= epsilon ||eta||_2^2
       <= epsilon K delta.                          (5)

This is the step that removes the small-total-secondary-occupation restriction. It uses the entire orthonormal family, rather than estimating each overlap separately and summing its occupation.

The explicit gap note gives, for v perpendicular to q,

    h_Q[v]:=||grad v||_2^2-integral Q^2|v|^2
       >= (1/4)||grad v||_2^2.

Since Hq=-q, h_Q[chi_j,q]=0 and h_Q[q]=-1. Using ||grad q||_2=1,

    h_Q[phi_j]
      =h_Q[chi_j]-|alpha_j|^2
      >= (1/4)||grad phi_j-alpha_j grad q||_2^2-|alpha_j|^2
      >= (1/8)||grad phi_j||_2^2-(5/4)|alpha_j|^2.

After multiplying by n_j, summing, and dividing by Mc, this yields

    I_q:=integral q^2 S
      <= (1/Mc)[(7/8)B+(5/4)K delta epsilon].         (6)

Let J=integral |eta|^2 S. Scalar GN, (2), and the elementary product bound ||eta||_2||grad eta||_2<=||eta||_{H1}^2/2 give

    J <= ||eta||_4^2 ||S||_2
      <= (C1 K delta/2)sqrt(3epsilon B)
      <= 3 C1 K delta epsilon/(1-3epsilon)
      <= 4 C1 K delta epsilon,                      (7)

where the third inequality uses (3), and the last uses epsilon<=1/12.

Using (sqrt(I_q)+sqrt(J))^2<=(15/14)I_q+15J,

    2 integral |phi_1|^2 S
      <= C1(15/16)B
         +C1 K delta epsilon [(15/14)(5/4)+120]
      = C1(15/16)B+(6795/56)C1 K delta epsilon.      (8)

Combining (2) and (8) gives the decisive estimate

    integral (|phi_1|^2+S)^2-C1(1+B)
      <=-[1-(6795/56)C1 K epsilon]delta
        -C1[1/16-3epsilon]B
      <=-delta/2-(C1/32)B,                          (9)

by (T0). This contradicts a strict violation. Every estimate remains valid for an alleged equality case, using the nonstrict versions of (3). If at least one secondary occupation is positive, then B>0, so equality is also impossible.

## 4. Sharpness and infinite rank

For finite rank, keep phi_1=q and choose normalized secondary functions of zero angular mean supported on mutually disjoint annuli. After dilating all secondary modes by a large common factor R, they remain exactly orthonormal and perpendicular to q, and their weighted kinetic energy tends to zero. Equation (2) makes their density L2 norm tend to zero. The quotient therefore tends to C1.

For a fixed countable trace-class occupation sequence, first select such annular modes with each kinetic energy at most one. The weighted kinetic sum is then finite. Common dilation again sends it to zero. This proves sharpness in the countable setting. The upper bound follows either from the direct convergent sums above or from applying the finite theorem to initial segments and using monotone convergence for the density square and the kinetic sum.

## 5. Structure of every optimizing sequence

Fix an occupation sequence satisfying the theorem with epsilon>0, and let the quotient of an optimizing sequence be C1-zeta_m with zeta_m->0. Normalize its primary kinetic energy to one. The crude estimate from Section 2 implies, with alpha_m=1-3epsilon-zeta_m/C1,

    alpha_m B_m <= 2sqrt(3epsilon B_m)+zeta_m/C1,
    delta_m <= zeta_m+3 C1 epsilon/alpha_m.           (10)

Thus B_m is bounded, and

    limsup B_m <=12epsilon/(1-3epsilon)^2,
    limsup delta_m <=3 C1 epsilon/(1-3epsilon)<delta0.

The second strict inequality follows from epsilon<=delta0/(8C1) and epsilon<=1/96. Scalar stability applies eventually. Also the displayed upper bound on B_m is strictly smaller than (64/3)epsilon, so eventually

    J_m <= (C1 K delta_m/2)sqrt(3epsilon B_m)
        <=4 C1 K delta_m epsilon.

Therefore the same refined bound (9) applies. Its left side equals -zeta_m(1+B_m)->0. It follows that delta_m->0 and B_m->0. After phase and translation, phi_{1,m}->q strongly in H1, while

    ||S_m||_2^2 <=3 C1 epsilon B_m->0.

In particular the total secondary density vanishes in L1 on every fixed bounded set. Every fixed positive occupation has ||grad phi_{j,m}||_2->0 and ||phi_{j,m}||_4->0. This is a variational concentration statement, not a classification of time-dependent threshold solutions.

## 6. Spectral interpretation

Let e_1(V)>=e_2(V)>=...>=0 denote the absolute values of negative eigenvalues of -Delta-V for nonnegative V in L2(R2), with zeros appended. Let L1=C1/4=1/(2Mc). The theorem implies the global remainder estimate

    e_1(V)+epsilon0 sum_{j>=2}e_j(V)
       <=L1 integral V^2.                           (11)

For each finite eigenfamily, (T1) gives F<=C1 A. Thus

    sum n_j e_j=integral V rho-A
      <=||V||_2 sqrt(C1 A)-A
      <=(C1/4)||V||_2^2.

Take n_1=1 and n_j=epsilon0, then pass to the increasing finite-rank limit. If there is no negative eigenvalue the assertion is immediate. Equation (11) controls the sum of all excited-state binding energies by the deficit in the sharp one-state bound. It is not the full rank-two Lieb--Thirring conjecture, which would require coefficient one in front of e_2.

## 7. A global deficit bound, without a near-optimizer hypothesis

The preceding local proof actually yields a global estimate after the smaller choice (T0). For every family normalized by ||grad phi_1||_2=1, write

    D=C1(1+B)-integral(|phi_1|^2+S)^2.

We claim D>=delta/2+C1 B/32. Suppose instead that this inequality failed. The unconditional crude bound from Section 2 is

    D>=delta+C1[(1-3epsilon)B-2sqrt(3epsilon B)].

Combining it with the alleged failure gives

    delta/2+C1[b B-2sqrt(3epsilon B)]<0,
    b=31/32-3epsilon>=15/16,

where epsilon<=1/96 was used. Since delta>=0,

    B<12epsilon/b^2<=12epsilon/(15/16)^2
      <(64/3)epsilon.                               (12)

Maximizing 2sqrt(3epsilon B)-bB over B>=0 also gives

    delta<6 C1 epsilon/b<8 C1 epsilon<=delta0.        (13)

Thus scalar stability applies, and (12) gives exactly the bound J<=4C1 K delta epsilon used in Sections 3 and 5. Weighted Bessel, the explicit spectral gap, and the refined estimate (9) now give D>=delta/2+C1B/32, contradicting the failure. This proves (T3) for all families. The epsilon=0 case follows directly from scalar GN.

Removing the kinetic normalization, let a_1=||grad phi_1||_2^2, A_secondary=sum_{j>=2}n_j||grad phi_j||_2^2, and A=a_1+A_secondary. Common scaling gives the equivalent homogeneous inequality

    C1 A-integral(sum_j n_j|phi_j|^2)^2
      >=(1/2)[C1 a_1-integral|phi_1|^4]
        +(C1/32)A_secondary.                        (14)

Both sides are homogeneous of degree two under the mass-preserving spatial dilation. Equation (14) is valid for finite and countable trace-class families under the same finite-energy hypotheses as the theorem.

## 8. Uniform control of secondary kinetic energy at the threshold

For the common-density cubic NLS, work in a fixed basis diagonalizing the conserved Gram matrix. At the critical largest mode mass ||u_1||_2^2=Mc, write

    u_1=sqrt(Mc)phi_1,
    u_j=sqrt(Mc n_j)phi_j,  j>=2.

Let A_secondary(U)=sum_{j>=2}||grad u_j||_2^2 and let

    E(U)=(1/2)sum_j||grad u_j||_2^2
           -(1/4)integral(sum_j|u_j|^2)^2,
    E_scalar(u_1)=(1/2)||grad u_1||_2^2
           -(1/4)integral|u_1|^4.

Multiplying (14) by Mc^2/4 gives the all-state inequality

    E(U)>= (1/2)E_scalar(u_1)+(1/64)A_secondary(U).   (15)

Scalar sharp GN makes E_scalar(u_1)>=0 at mass Mc. Along every solution for which the standard Gram and energy conservation laws hold, (15) therefore gives, at every time in its lifespan,

    A_secondary(U(t))<=64 E(U(0)),
    E_scalar(u_1(t))<=2 E(U(0)).                     (16)

Thus even if the primary kinetic energy diverges at a threshold singularity, the total secondary kinetic energy stays uniformly bounded. This statement is stronger than convergence of secondary kinetic energy relative to the diverging primary scale. It does not by itself prove the existence or absence of a threshold singularity, nor classify the primary blowup law.

For infinite rank, (15) is an all-state functional inequality. Using it dynamically requires the corresponding infinite-component solution and its conservation laws; those are separate well-posedness hypotheses, not supplied by this inequality alone.

## Scope and remaining quantitative issue

The proof is uniform in rank and secondary trace. The positive cutoff epsilon0 is explicit in the normalized scalar GN stability constants K and delta0; these constants were established existentially in R15 and have not been assigned certified numerical values. The homogeneous spectral gap is now fully numerical and rational, kappa>=47/175, and does not remain an unspecified constant. No claim of a sharp occupation-ratio cutoff, a full equal-occupation theorem, a physical experiment, or historical first priority is made here.
