# A one-dimensional extension and propagation of the kinetic remainder

Date: 2026-10-09. This note extends the occupation-gap argument to the one-dimensional mass-critical quintic system. A literature update changes the attribution materially: Read--Schulz, arXiv:2609.10478v2 (14 September 2026), proves the full sharp one-dimensional Lieb--Thirring inequality with eigenvalue exponent one. Thus the unrestricted one-dimensional threshold formula below is an application of that external theorem, not a newly solved conjecture in this project. The additional derivation here is a global secondary-kinetic remainder for every strictly separated leading occupation, obtained from an explicit homogeneous gap, the local nonlinear argument, and concavity in occupations. Historical priority for this remainder has not been established.

## 1. The model and the current external input

Consider a finite vector of complex fields on the line,

    i partial_t u_j = -partial_x^2 u_j - rho^2 u_j,
    rho = sum_j |u_j|^2,
    E(U) = (1/2) sum_j ||u_j'||_2^2 - (1/6) integral rho^3.

Its conserved Gram matrix is Gamma_ij=integral u_i conjugate(u_j). The scalar ground state is explicit:

    Q(x)=3^(1/4) sech(2x)^(1/2),
    -Q''+Q-Q^5=0,
    M_c=||Q||_2^2=pi sqrt(3)/2,
    ||Q'||_2^2=M_c/2.

Put q=Q/sqrt(M_c) and C=3/M_c^2=4/pi^2. Then ||q||_2=1, ||q'||_2^2=1/2 and integral q^6=C/2.

Read--Schulz Theorem 1, and equivalently equation (1.1), gives the sharp orthonormal inequality

    integral (sum_j |phi_j|^2)^3 <= C sum_j ||phi_j'||_2^2.       (1)

The scalar-potential spectral theorem applies to complex orthonormal families by its usual variational duality. Fractional occupations 0<=n_j<=1 follow without any new spectral input: for a finite family, independently select each member with probability n_j, apply (1) to the selected subfamily, and use convexity of z^3 and expectation. Truncation gives trace-class infinite families with finite kinetic energy. Hence

    integral (sum_j n_j |phi_j|^2)^3 <= C sum_j n_j ||phi_j'||_2^2,
    0<=n_j<=1.                                                (2)

The sharp constant in (2), for every fixed spectrum having max n_j=1, is C. To see sharpness, approximate q by a normalized smooth compactly supported primary, then put finitely many normalized secondary modes in disjoint remote intervals with their kinetic energies tending to zero. A diagonal limit recovers the scalar constant. Trace-class infinite rank can be handled by assigning disjoint intervals with sufficiently small individual kinetic energies and by approximating q first; no exact overlap with the primary is needed.

For normalized occupations p_j, sum p_j=1, the weighted sharp constant is p_1^2 C. Standard energy and finite-variance virial arguments therefore give the exact strict-side threshold

    M_*(p)=M_c/p_1                                             (3)

for every finite occupation spectrum, including equal leading occupations. Below this mass all H1 data with the specified Gram spectrum are global with bounded kinetic energy. Above it there are smooth compactly supported data with that exact spectrum and negative energy, hence finite-time blowup. This does not assert that every superthreshold datum blows up, or settle all threshold dynamics.

The proof of the lower side is E >= (1/2)[1-(m_1/M_c)^2]A, where m_1 is the largest absolute Gram eigenvalue. For the upper side, let the primary approximate Q at mass m_1>M_c, so that its scalar energy is negative, and make all orthogonal secondary modes remote and dilute. Orthogonality and prescribed masses are exact. The critical virial identity is V''=16E.

## 2. An explicit homogeneous gap, with no numerical ODE input

Define h[v]=integral |v'|^2-integral Q^4 |v|^2. Then

    h[v] >= (10/21) ||v'||_2^2 whenever <Q,v>=0.                (4)

Here is a direct proof. Set z=tanh(2x). With f(z)=v(x),

    D[v]=2 integral_{-1}^1 (1-z^2)|f_z|^2 dz,
    integral Q^4 |v|^2=(3/2) integral_{-1}^1 |f|^2 dz.

The Legendre Poincare inequality on the subspace of zero unweighted mean is

    integral (1-z^2)|f_z|^2 >= 2 integral |f|^2.

Thus h[u]>=(5/8)D[u] for functions u whose transformed Legendre mean vanishes. This weighted Sobolev inequality extends from smooth functions by closure; H1(R) functions belong to its form domain.

For an arbitrary v perpendicular to Q, choose t so that u=v+tQ has zero Legendre mean. Since Q is positive this is possible. The equation (-partial_x^2-Q^4)Q=-Q gives h[u]=h[v]-M_c|t|^2. Put beta=5/8. Therefore

    h[v] >= beta D[u]+M_c|t|^2,
    D[v] <= (sqrt(D[u])+sqrt(M_c/2)|t|)^2
         <= (1/beta+1/2)[beta D[u]+M_c|t|^2].

This yields beta/(1+beta/2)=10/21 in (4). The proof is valid for complex functions. In the estimates below we use the weaker kappa=1/4 to keep coefficients simple.

## 3. Scalar stability normalization

There exist K>0 and delta_0>0 such that

    ||phi||_2=1, ||phi'||_2^2=1/2,
    delta=C/2-integral |phi|^6 <= delta_0
      implies inf_{theta,y}||phi-exp(i theta)q(.-y)||_{H1}^2
                   <=K delta.                                (5)

We reduce delta_0 if necessary so that K delta_0<=1. This is the classical normalized scalar GN stability argument, not a new stability theorem. The proof in R15 Appendix A applies with the following substitutions: L_+=-partial_x^2+1-5Q^4, L_-=-partial_x^2+1-Q^4 and Lambda Q=Q/2+xQ'. One has L_+ Lambda Q=-2Q, <Q,Lambda Q>=0, <Q', (Lambda Q)'>=M_c/2, ker L_+=span{Q'}, and ker L_-=span{Q}. The exact mass and kinetic constraints remove the mass-critical scaling direction. Taylor expansion of the polynomial quintic energy is cubic or higher in the H1 error because H1(R) embeds into L-infinity. The usual compactness argument for a normalized GN optimizing sequence supplies the small-deficit neighborhood. These standard nondegeneracy statements are also covered by Chang--Gustafson--Nakanishi--Tsai (2007), Lemmas 2.1--2.2.

For clarity, in the normalized compactness argument the scalar GN splitting becomes

    1 <= a^2 b+(1-a)^2(1-b) <= 1,

where a and b are the fractions of mass and kinetic energy of a nonzero weak limit. Since a,b>0, equality forces a=b=1. This is the one-dimensional quintic replacement for the bilinear splitting in the two-dimensional cubic proof.

## 4. Two elementary secondary-density estimates

Let gamma_s=sum t_j |phi_j><phi_j| satisfy 0<=gamma_s<=epsilon I. Write S=sum t_j |phi_j|^2 and B=sum t_j ||phi_j'||_2^2. Then

    integral S^3 <= (15/pi^2) epsilon^2 B
                 = (15/4) C epsilon^2 B,                      (6)
    ||S||_infinity <= (4/pi) sqrt(epsilon B).                  (7)

For (6), the Fourier projector onto |xi|^2<=E has diagonal sqrt(E)/pi. The same layer-cake argument as R16 gives

    B >= integral integral_0^infinity
              (sqrt(S)-sqrt(epsilon sqrt(E)/pi))_+^2 dE dx
      = pi^2/(15 epsilon^2) integral S^3,

because integral_0^1 (1-z^(1/4))^2 dz=1/15.

For (7), split at frequency R>0. The low-frequency vector has squared pointwise norm at most epsilon R/pi. Cauchy--Schwarz against |xi|^-1 bounds the high-frequency vector by B/(pi R). Their square-root norms add. Choosing R=sqrt(B/epsilon) gives (7). These are nonsharp classical-type kinetic estimates; no priority is asserted.

## 5. A complete local global-remainder theorem

Let phi_1,phi_2,... be orthonormal, n_1=1, 0<=n_j<=epsilon for j>=2. Normalize ||phi_1'||_2^2=1/2 and set

    a=|phi_1|^2,
    S=sum_{j>=2}n_j|phi_j|^2,
    B=sum_{j>=2}n_j||phi_j'||_2^2,
    delta=C/2-integral a^3,
    D=C(1/2+B)-integral(a+S)^3.

Let A_0=3295502 and define the positive, non-numerically-certified constant

    t_0=min{1/512, delta_0/(6C), 1/(2 A_0 C K)}.               (8)

Then epsilon<=t_0 implies the all-state estimate

    D >= delta/2+(C/32)B.                                    (9)

The large coefficient A_0 is chosen for proof simplicity, not optimized. K and delta_0 are existential scalar stability constants, so (8) does not certify a practical numerical occupation interval.

Proof. Expand the density cube exactly. Holder and (6) bound its term linear in S; (7) gives integral aS^2<=||S||_infinity^2 because integral a=1. Consequently

    D >= delta+C[(1-r)B-3(1/2)^(2/3)(15/4)^(1/3)
                                    epsilon^(2/3)B^(1/3)],
    r=12epsilon+(15/4)epsilon^2.                             (10)

Suppose (9) failed. For epsilon<=1/512, r<=1/32 and beta=31/32-r>=15/16>1/2. Equation (10) and the alleged failure yield

    B<16epsilon,
    delta<6Cepsilon<=delta_0.                                (11)

For explicit verification: writing L=3(1/2)^(2/3)(15/4)^(1/3), the inequality is delta/(2C)+beta B<L epsilon^(2/3)B^(1/3). Hence B<(L/beta)^(3/2)epsilon<16epsilon. Maximizing the right-hand side minus beta B gives delta<sqrt(30)Cepsilon<6Cepsilon.

Choose phase and translation so that phi_1=q+eta and ||eta||_H1^2<=Kdelta. Put alpha_j=<q,phi_j> and chi_j=phi_j-alpha_jq. Weighted Bessel gives

    sum_{j>=2}n_j|alpha_j|^2<=epsilon Kdelta.

The weaker gap kappa=1/4 from (4), D[q]=1/2 and h[q]=-1 give

    integral Q^4|phi_j|^2
       <=(7/8)||phi_j'||_2^2+(9/8)|alpha_j|^2.

Therefore, putting I_q=integral q^4 S,

    3I_q<=C[(7/8)B+(9/8)epsilon Kdelta].                    (12)

The pointwise weighted convexity bound

    |q+eta|^4 <= (65/64)^3 q^4+65^3 |eta|^4
               <=(15/14)q^4+65^3 |eta|^4

and Holder imply, with J=integral |eta|^4S,

    J <= ||eta||_6^4 ||S||_3
      <= C(15/4)^(1/3)K^2 delta^2 epsilon^(2/3)B^(1/3)
      <=4C K^2 delta^2 epsilon.

Here scalar GN gives ||eta||_6^4<=C^(2/3)||eta||_H1^4; (11) gives the last line. Since Kdelta<=1, (12) yields

    3 integral a^2 S
      <= (15/16)CB + A_0 C K epsilon delta.                  (13)

Indeed the exact coefficient is 135/112+12*65^3<3295502. Also 3 integral aS^2+integral S^3<=CrB. Substituting (13) into the exact cube expansion proves

    D >= (1-A_0CKepsilon)delta+C(1/16-r)B
      >= delta/2+(C/32)B,

contradicting the alleged failure. Thus (9) holds for every family, not just near optimizers. Removing the spatial normalization gives

    C A-integral rho^3
       >=(1/2)[C||phi_1'||_2^2-integral|phi_1|^6]
           +(C/32)A_secondary.                             (14)

All terms scale quadratically under the common mass-preserving dilation. Infinite trace-class families follow by truncation or the convergent estimates above.

## 6. Propagation to every strict occupation gap

This step uses the full sharp external theorem (2), whereas Section 5 did not. Suppose epsilon=max_{j>=2}n_j<1. If epsilon<=t_0, (14) applies. If epsilon>=t_0, put n_j=epsilon r_j with 0<=r_j<=1 and define

    S_*=sum r_j|phi_j|^2, B_*=sum r_j||phi_j'||_2^2,
    D(t)=C(a_1+tB_*)-integral(|phi_1|^2+tS_*)^3.

D(t) is concave in t. Equation (2) gives D(1)>=0, and (14) gives D(t_0)>=delta/2+(C/32)t_0 B_*, where now delta=C a_1-integral|phi_1|^6. Interpolating gives the global estimate

    D(epsilon) >= [(1-epsilon)/(2(1-t_0))]delta
            + [C t_0(1-epsilon)/(32epsilon(1-t_0))]B,        (15)

where B=epsilon B_*. Both coefficients are strictly positive for every epsilon<1. They tend to zero when the largest occupation becomes degenerate, as they must: two widely separated copies of Q with equal occupation defeat a uniform positive secondary-kinetic remainder.

Thus the threshold formula is unrestricted in one dimension, and all spectra having a simple largest eigenvalue enjoy a positive global secondary-kinetic remainder. This is a genuinely larger parameter range than the small-ratio hypothesis alone. Its dependence on the recent sharp one-dimensional theorem is explicit.

The interpolation mechanism itself is dimension-independent: for any exponent p>1, t -> C A(t)-integral(a+tS)^p is concave. An established local positive remainder plus a sharp full-occupation endpoint inequality therefore propagates that remainder to every strict occupation gap. It does not prove the missing endpoint inequality in any other dimension. In particular, it cannot be used as an unconditional solution of the two-dimensional rank-two problem.

## 7. Consequences at the quintic threshold

Work in the fixed basis diagonalizing the Gram matrix and assume m_1=M_c and epsilon=m_2/m_1<1. For epsilon<=t_0, (14) gives

    E(U)>=(1/2)E_scalar(u_1)+(1/64)A_secondary.               (16)

For t_0<=epsilon<1, (15) gives

    E(U)>=a_epsilon E_scalar(u_1)+b_epsilon A_secondary,
    a_epsilon=(1-epsilon)/(2(1-t_0)),
    b_epsilon=t_0(1-epsilon)/(64epsilon(1-t_0)).              (17)

Scalar sharp GN makes E_scalar(u_1)>=0. Conservation of energy therefore bounds the total secondary kinetic energy for the entire lifespan of every finite-component H1 solution, even if the primary mode blows up. This conclusion holds without a bound on the total secondary mass.

If such a solution blows up at finite time T, then ||u_1'(t)||_2 diverges, and lambda(t)=sqrt(M_c/2)/||u_1'(t)||_2 tends to zero. Applying normalized scalar stability at each time, after phase and translation,

    ||lambda^(1/2)e^(-i theta)u_1(x(t)+lambda .)-Q||_H1
          <= C_E lambda(t).                                (18)

Indeed scalar energy of the scaled primary is lambda^2 E_scalar(u_1), which tends to zero by (16) or (17). This is a full-time core-convergence statement. Together with bounded A_secondary it shows that only the principal Gram eigenmode can form the singular kinetic core.

We do not import the stronger two-dimensional fixed-background results automatically. In one dimension the quintic cross nonlinearity is rho_1^2 u_j, whose global negative-Sobolev estimate is inadequate. Equations (16)--(18) are the immediate dynamical conclusions established here. The companion [quintic-dynamics.md](quintic-dynamics.md) subsequently proves unique principal concentration, automatic principal variance, a quantitative one-sided pseudoconformal rate and an infinite-principal-variance global class by an individual-mode transport argument. It then closes the secondary-background problem by testing locally away from the collapse point and exploiting one-dimensional Sobolev continuity, obtaining a unique background that vanishes at the collapse point and, with finite secondary variance, conformal free scattering. Its final section gives a forward-global Sigma alternative: full H1 scattering or one bounded-width principal core moving on an asymptotically straight trajectory, plus free secondary radiation and an H1-small error. An exact primary asymptotic rate and strong physical H1 terminal-background convergence are not claimed.

## 8. What is and is not generalized

The actual new applicable model here is one-dimensional quintic common-density focusing NLS. Its unrestricted threshold follows from a newly available external sharp theorem, while the explicit transverse gap and occupation interpolation yield the additional remainder and core conclusion above.

The abstract concavity step works in any dimension and for other convex density powers. A full general-dimensional threshold theorem is not asserted. For d>=3, neither the required homogeneous Q-perp gap nor the appropriate global scalar-stability perturbation estimates have been verified here. Moreover, Frank--Gontier--Lewin's rank-one nonoptimality theorem applies to eigenvalue exponent one in dimensions d>=3, so a universal full-occupation scalar constant in those dimensions is false. One must not claim a dimension-independent full threshold M_c/p_1 on the basis of the d=1 or d=2 arguments.

## Primary sources and attribution

1. Larry Read and Marvin R. Schulz, *The sharp one-dimensional Lieb--Thirring inequality for the sum of eigenvalues*, arXiv:2609.10478v2, 14 September 2026. https://arxiv.org/html/2609.10478v2 . Theorem 1 / equation (1.1) is the external unrestricted one-dimensional input. This is a recently posted preprint; the present note does not substitute for Proof details of its proof.
2. Shu-Ming Chang, Stephen Gustafson, Kenji Nakanishi, Tai-Peng Tsai, *Spectra of Linearized Operators for NLS Solitary Waves*, SIAM J. Math. Anal. 39 (2007), 1070--1111. https://personal.math.ubc.ca/~ttsai/publications/cgnt-sima07.pdf . Classical scalar nondegeneracy and coercivity input.
3. Rupert L. Frank, David Gontier, Mathieu Lewin, *The Nonlinear Schroedinger Equation for Orthonormal Functions II: Application to Lieb--Thirring Inequalities*, CMP (2021), DOI 10.1007/s00220-021-04039-5. Their strict parameter condition at exponent one covers d>=3 and does not cover d=1 or d=2.

The Fourier cutoff estimates, Legendre Poincare inequality, scalar GN stability method, and spectral/kinetic duality are classical tools. This note claims only the displayed derivations and implications, not that these underlying ideas were invented here.
