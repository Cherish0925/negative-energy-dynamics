# Exact sharp thresholds for small secondary occupation

Status: updated analytic proof, 2026-10-09. The nonlinear argument below is proved as an implication from the homogeneous Townes spectral gap (S). The separate interval certificate and independent mathematical audit in [spectral-details.md](spectral-details.md) now supply (S), via the verified envelope Q(r)^2<=6/(1+r^2)^2. Thus (S) is no longer an unresolved mathematical input. The certificate uses the IEEE-754 arithmetic assumptions detailed in its audit; final independent code-audit reporting is maintained separately. The result proves a nonempty, rank-independent small-secondary-occupation range, not the full equal-occupation rank-two Lieb--Thirring conjecture. Historical priority is not asserted.

## Normalization

Let Q be the positive radial solution of

    -Delta Q + Q - Q^3 = 0  on R^2.

Write Mc=||Q||_2^2, q=Q/sqrt(Mc), C1=2/Mc. Pohozaev gives ||grad q||_2^2=1 and integral |q|^4=C1. For orthonormal phi_1,...,phi_k in H^1, and weights n=(1,t_2,...,t_k), define

    rho=|phi_1|^2 + sum_{j>=2} t_j |phi_j|^2,
    A=||grad phi_1||_2^2 + sum_{j>=2} t_j ||grad phi_j||_2^2,
    tau=sum_{j>=2} t_j.

The sharp weighted constant is C(n)=sup integral rho^2/A. Always C(n)>=C1, by one Townes mode and finitely many orthogonal modes diluted and translated to infinity.

## Exact theorem, uniform in the number of modes

Assume the following homogeneous spectral gap for H=-Delta-Q^2:

    integral Q^2 |v|^2 <= (1-kappa) ||grad v||_2^2
    whenever v in H^1(R^2) and <v,Q>=0,                  (S)

for some kappa>0. Then there is tau_0>0, depending only on Q and kappa, such that

    C(1,t_2,...,t_k)=C1  whenever tau<=tau_0.

The number of modes k and their individual secondary weights do not enter tau_0. After normalizing weights p_j=n_j/(1+tau), this gives

    C(p)=p_max C1,
    M_*(p)=Mc/p_max

for every finite spectrum with p_max>=1/(1+tau_0). We first prove the implication from (S); the independently audited envelope argument described below establishes (S) for the actual Townes profile. The exact strict-side dynamical threshold implication uses the already established energy/virial argument. Neither kappa nor tau_0 has yet been assigned an explicit numerical value.

### Scalar stability input

For ||phi||_2=||grad phi||_2=1 let delta=C1-integral |phi|^4. There exist delta_0,K>0 such that, when delta<=delta_0, phase and translation can be chosen so that

    phi=q+eta,   ||eta||_{H^1}^2 <= K delta.            (G)

This input is proved in detail in Appendix A below. In particular, it is not being imported from a subcritical orbital-stability theorem. The fixed kinetic norm removes the additional mass-critical scaling degeneracy. The precise classical linear facts used in the proof are Lemma 2.1 and Lemma 2.2(2.6),(2.8) of Chang--Gustafson--Nakanishi--Tsai (2007), checked in the authors' full published PDF.

### Proof of the implication from the homogeneous spectral gap

Suppose a counterexample integral rho^2>C1 A exists. Simultaneous spatial scaling normalizes a_1=||grad phi_1||_2^2=1. Put

    B=sum t_j b_j,   b_j=||grad phi_j||_2^2,
    S=sum t_j |phi_j|^2,   X=integral |phi_1|^4=C1-delta.

The vector-valued scalar GN inequality gives

    integral S^2 <= C1 tau B.                          (1)

Indeed ||sqrt(S)||_2^2=tau and ||grad sqrt(S)||_2^2<=B. By Cauchy--Schwarz,

    integral rho^2 <= C1-delta + 2 C1 sqrt(tau B) + C1 tau B.

Consequently a counterexample satisfies

    delta < C1[2 sqrt(tau B)-(1-tau)B],
    B < 4 tau/(1-tau)^2,
    delta < C1 tau/(1-tau).                            (2)

Thus for small tau, (G) applies to phi_1. Write phi_1=q+eta. For j>=2 put alpha_j=<q,phi_j>=-<eta,phi_j> and chi_j=phi_j-alpha_j q. Hence chi_j is orthogonal to Q and |alpha_j|^2<=K delta. Applying (S), then the triangle inequality and Young's inequality, yields a constant C independent of j and k such that

    integral Q^2 |phi_j|^2 <= (1-kappa/2)b_j+C delta.

Summing with weights gives

    I_q := integral |q|^2 S
       <= (1-kappa/2)B/Mc + C delta tau.               (3)

Also scalar GN and (G) imply

    J := integral |eta|^2 S
       <= ||eta||_4^2 sum t_j ||phi_j||_4^2
       <= C delta sum t_j sqrt(b_j)
       <= C delta sqrt(tau B)
       <= C delta tau,                                (4)

where the last inequality uses (2) and, say, tau<=1/2. Since

    integral |phi_1|^2 S <= I_q+2 sqrt(I_q J)+J,

another Young inequality, absorbing a fixed portion of kappa B, gives

    2 integral |phi_1|^2 S
       <= C1(1-kappa/4)B+C delta tau.                  (5)

Combining (1) and (5),

    integral rho^2-C1(1+B)
       <= -(1-C tau)delta-C1(kappa/4-tau)B.

This is nonpositive for sufficiently small tau. For definiteness, enlarge C so that the estimates also hold whenever B<=25 tau, and take

    tau_0 <= min(1/4,delta_0/(4C1),1/(2C),kappa/8).

These choices give positive margins in both final coefficients, contradicting the assumed strict counterexample. The constant tau_0 works for every finite k. Sharpness follows from the dilute-mode construction noted above. This proves the implication from (S); Appendix A proves (G), and the separate audited envelope proof supplies (S).

### Attainment and nonattainment

Take tau_0 small enough that both final coefficients have a positive margin. The same proof applies to an alleged equality case: replace the initial strict counterexample inequality by a nonstrict one, and replace (2) by its nonstrict versions. It gives

    0 <= integral rho^2-C1 A <= -delta/2-C1 kappa B/8.

If tau>0, some t_j>0 and ||grad phi_j||_2>0 for every L2-normalized H1 function. Thus B>0, a contradiction. Therefore, for 0<tau<=tau_0, the optimal constant equals C1 but is never attained by a finite orthonormal family with the specified positive secondary weights. This is a sharp supremum, not a new stationary multimode optimizer.

For an explicit sharpness sequence take phi_1=q. For each j>=2 choose a fixed smooth annular radial amplitude g_j and a distinct nonzero integer angular harmonic ell_j, and set

    phi_{j,R}(r,theta)=R^{-1} g_j(r/R) exp(i ell_j theta),

with normalization 2 pi integral |g_j(s)|^2 s ds=1. These functions are exactly orthonormal and orthogonal to q for every R, and each kinetic energy is O(R^{-2}). The weighted tail density has L2 norm squared O(R^{-2}); its overlap with q^2 tends to zero. The quotient tends to C1. Every profile has finite variance for fixed R (Q decays exponentially, and the other modes are compactly supported annular functions).

No conclusion about all dynamics at M=M_* follows from nonattainment. In particular, positivity of the energy there does not supply a uniform bound on the primary-mode kinetic energy.

### Every optimizing sequence has a scalar core and diluted secondary modes

Fix finitely many weights with 0<tau<=tau_0 and omit zero-weight modes. Let an orthonormal sequence of families have quotient integral rho_n^2/A_n->C1. After a common mass-preserving spatial scaling, normalize ||grad phi_(1,n)||_2^2=1. Write its quotient as C1-epsilon_n with epsilon_n->0, and let B_n,delta_n be defined as in the proof.

The crude bound used there implies, with alpha_n=1-tau-epsilon_n/C1,

    alpha_n B_n <= 2 sqrt(tau B_n)+epsilon_n/C1,
    delta_n <= epsilon_n+C1 tau/alpha_n.              (6)

For large n, epsilon_n/C1<=tau and tau<=1/4, so alpha_n>=1/2 and (6) gives B_n<=25 tau. Also

    limsup delta_n <= C1 tau/(1-tau)<delta_0.

Thus the scalar stability argument applies eventually. Since B_n is bounded, the unnormalized excess tends to zero:

    D_n=integral rho_n^2-C1(1+B_n)
       =-epsilon_n(1+B_n)->0.

The refined estimate, with the uniform constants chosen above, now gives

    D_n <= -delta_n/2-C1 kappa B_n/8.

Consequently delta_n->0 and B_n->0. Suitable phases and translations give phi_(1,n)->q strongly in H1. Every fixed positive secondary weight satisfies

    ||grad phi_(j,n)||_2->0,
    ||phi_(j,n)||_4->0.

Their local L2 masses also vanish on every fixed bounded set, by Holder's inequality; this remains true after the common translations. Their full L2 norms remain one. Hence every optimizing sequence, not merely the example constructed above, consists after scaling and modulation of one Townes core and secondary mass that becomes locally dilute. This describes variational loss of compactness; it is not a classification of time-dependent solutions at the dynamical threshold.

## What the spectral hypothesis really requires

Nonnegativity of H on Q-perp is NOT enough for the argument: a homogeneous gap, rather than an L2 gap, is needed because the essential spectrum starts at zero. A positive L2 spectral gap on Q-perp is impossible.

A sufficient spectral route to (S) is:

1. H has exactly one negative eigenvalue, with eigenfunction Q;
2. H has no nonzero zero-energy solution in the anchored finite-Dirichlet-energy space
   X={v in H1_loc: grad v in L2, integral Qv=0}.

Indeed the embedding X -> L2(Q^2 dx) is compact (the anchoring fixes the two-dimensional additive constant and exponential decay controls the tails). If the supremum c of integral Q^2v^2/integral |grad v|^2 exceeds 1, cutoff and re-orthogonalization produce a negative H direction perpendicular to Q, contrary to item 1. If c=1, a maximizer satisfies -Delta v=Q^2v+mu Q. Testing against Q and using <v,Q>=0 gives mu=0, contrary to item 2. Thus c<1 and kappa=1-c>0.

The compact weighted embedding and logarithmic-cutoff argument are supplied in Section E of [spectral-details.md](spectral-details.md). Absence of a second negative eigenvalue alone would not exclude c=1; the verified envelope gives the stronger finite-energy comparison needed here.

### Verification of (S) for the Townes profile

The interval certificate establishes the global estimate

    Q(r)^2 <= 6/(1+r^2)^2,   r>=0.

Under stereographic projection, the comparison quadratic form is

    integral_{S2} |grad_S v|^2 - (3/2) integral_{S2} |v|^2.

The sphere eigenvalues 0,2,6,... imply that this form has only one nonpositive direction. On the anchored finite-Dirichlet-energy space X, any nonzero v with h_Q[v]<=0 would, together with Q, span a two-dimensional nonpositive subspace: h_Q[Q,v]=-integral Q conjugate(v)=0. This contradicts the comparison. Hence h_Q is strictly positive on X. The compact embedding X into L2(Q^2 dx), established using annular Poincare estimates and the exponentially decaying anchor, upgrades strict positivity to (S).

The interval proof controls the entire initial-value bracket and whole step tubes, identifies a ground-state initial value by the overshoot/undershoot topology, and proves the remaining tail with an exterior linear comparison. It does not infer the envelope from point samples or from an invalid nonlinear supersolution comparison. See [spectral-details.md](spectral-details.md) and [r15_validated_townes.py](../../computations/occupation-computations/r15_validated_townes.py) for the detailed certificate and its computational assumptions.

## Unconditional angular result

For every v with angular mean zero, the angular Birman--Schwinger trace estimate gives

    integral Q^2 |v|^2 <= c_ang ||grad v||_2^2,
    c_ang=Mc/(4 pi)<1.

The strict inequality Mc<4 pi follows from the Gaussian trial in sharp scalar GN, since a Gaussian is not an optimizer. This fact and the angular estimate are analytic, requiring no computed Q profile.

Fix phi_1=q exactly, and suppose every secondary phi_j has zero angular mean. Then, with tau and B as above,

    integral rho^2
       <= C1 + C1 c_ang B + C1 tau B
       <= C1(1+B)             if tau<=1-Mc/(4 pi).

This inequality is sharp by taking mutually orthogonal angular modes diluted to infinity. It rules out an improvement of the scalar sharp constant by adding any finite number of small angular secondary modes to an exact Townes primary mode. It controls the full nonlinear density, including every cross term; it is stronger than merely checking the first derivative in t.

It is a restricted variational result, not a universal dynamical threshold for arbitrary primary modes. The restriction that the primary be exactly Townes is not flow invariant. It should not be advertised as solving the physical two-mode threshold problem.

## Convex spectral interpretation of the imbalance question

Let e_j(V)=|lambda_j(-Delta-V)|, zero-filled, and let

    L(t)=sup_{V>=0,V in L2} [e_1(V)+t e_2(V)]/integral V^2.

Quadratic density/spectral duality gives C(1,t)=4L(t). The function L(t) is convex and nondecreasing because it is a supremum of affine functions. Its maximal flat interval starting at zero has endpoint

    t_crit=inf_{V:e_2(V)>0}
        [L(0) integral V^2-e_1(V)]/e_2(V).

The theorem, combined with the verified envelope and the audit of (S), proves t_crit>0. The full rank-two conjecture requires t_crit>=1. These are distinct targets: the first is the exact small-occupation range established here; the second controls the entire occupation interval and remains a global variational problem.

## Primary references consulted

Frank--Gontier--Lewin, The Nonlinear Schrodinger Equation for Orthonormal Functions II: Application to Lieb--Thirring Inequalities, CMP (2021), DOI 10.1007/s00220-021-04039-5, arXiv:2002.04964. Their rank-one nonoptimality theorem requires kappa>max(0,2-d/2), so does not settle d=2,kappa=1.

Dolbeault--Felmer--Loss--Paturel, Lieb--Thirring type inequalities and Gagliardo--Nirenberg inequalities for systems, JFA 238 (2006), 193--220, DOI 10.1016/j.jfa.2005.11.008. Occupation-number duality predates the present derivation; no novelty claim for that bridge is made here.

Chang--Gustafson--Nakanishi--Tsai, Spectra of Linearized Operators for NLS Solitary Waves, SIAM J. Math. Anal. 39 (2007), 1070--1111, DOI 10.1137/050648389, arXiv:math/0611483. Lemma 2.1 proves ker L_+=span{partial_j Q} for all subcritical powers relative to Sobolev embedding; Lemma 2.2(2.6),(2.8) gives positivity of L_- and nonnegativity of L_+ on Q-perp in the mass-critical case. Author-hosted published PDF: https://personal.math.ubc.ca/~ttsai/publications/cgnt-sima07.pdf . Exact statements and their proofs on pp.1078--1080 were checked.

Kwong, Uniqueness of positive solutions of Delta u-u+u^p=0 in R^n, Arch. Rational Mech. Anal. 105 (1989), 243--266, DOI 10.1007/BF00251502. Used for the classical uniqueness of the scalar positive radial optimizer.

## Appendix A. Complete derivation of the normalized scalar stability estimate

We prove (G), making every role of the normalization explicit. Let

    v=sqrt(Mc) phi,
    ||v||_2^2=||grad v||_2^2=Mc,
    E(v)=1/2 ||grad v||_2^2-1/4 ||v||_4^4=Mc^2 delta/4.

The scalar ground state has E(Q)=0. Write

    L_+=-Delta+1-3Q^2,    L_-=-Delta+1-Q^2,
    Lambda Q=Q+x.grad Q.

The standard linear facts needed are:

    L_- >= 0,    ker L_-=span{Q};
    <f,L_+ f> >= 0 for real f perpendicular to Q;
    ker L_+=span{partial_1 Q,partial_2 Q};
    L_+ Lambda Q=-2Q,
    <Q,Lambda Q>=0,
    <grad Q,grad Lambda Q>=Mc.                         (A1)

The last three identities follow directly by differentiating the mass-preserving scaling lambda Q(lambda x). The kernel and positivity assertions are precisely the classical lemmas cited above. Alternatively, nonnegativity on Q-perp follows by differentiating twice E on the mass sphere ||v||_2^2=Mc, since sharp GN makes E nonnegative on that entire sphere. L_- positivity follows from the ground-state transform. Nondegeneracy of L_+ is the sole non-elementary linear theorem needed here.

### A1. Tangent-space coercivity

Define the closed real subspace

    T={f in H1(R^2;R): <f,Q>=0,
         <grad f,grad Q>=0, <f,partial_j Q>=0 for j=1,2}.

Then for a constant c_+>0,

    <f,L_+ f> >= c_+ ||f||_{H1}^2  for f in T.         (A2)

To identify the only possible null directions, suppose f perpendicular to Q and <f,L_+f>=0. Positivity on Q-perp implies by polarization that <L_+f,g>=0 for every g perpendicular to Q. Hence L_+f=alpha Q in H^{-1}. By (A1) and elliptic regularity,

    f=-(alpha/2)Lambda Q+c_1 partial_1 Q+c_2 partial_2 Q.

For f in T, the kinetic tangent condition forces alpha=0, since the derivative directions are odd and <grad Q,grad Lambda Q>=Mc. Translation orthogonality then forces c_1=c_2=0.

To turn this strict positivity into (A2), assume ||f_n||_{H1}=1 and <f_n,L_+f_n>->0 with f_n in T. Pass to a weak H1 limit f. Since Q is bounded and decays, multiplication by Q is compact from H1 to L2. Thus 3 integral Q^2 f^2=1, while weak lower semicontinuity gives <f,L_+f><=0. Positivity forces equality and ||f||_{H1}=1, so convergence is strong. The null-space characterization above gives f=0, a contradiction. The same argument gives c_->0 such that

    <g,L_-g> >= c_- ||g||_{H1}^2  whenever <g,Q>=0.    (A3)

This use of an H1 gap for L_- is legitimate: its essential spectrum starts at 1. It is different from the homogeneous gap (S) for H=L_--1, whose essential spectrum starts at 0.

### A2. Local nonlinear estimate

For v sufficiently close to the phase/translation orbit of Q, the implicit function theorem selects phase theta and translation y so that

    exp(-i theta)v(.+y)=Q+h_1+i h_2,
    <h_2,Q>=0,
    <h_1,partial_j Q>=0, j=1,2.                       (A4)

The modulation Jacobian at Q is nonsingular: its diagonal blocks are Mc and the positive matrix <partial_i Q,partial_j Q>. Put h=h_1+i h_2. The two exact normalizations imply

    <Q,h_1>=-||h||_2^2/2,
    <grad Q,grad h_1>=-||grad h||_2^2/2.              (A5)

Define

    a=-||h||_2^2/(2Mc),
    b=(||h||_2^2-||grad h||_2^2)/(2Mc),
    f=h_1-aQ-b Lambda Q.

By (A1),(A4),(A5), f belongs exactly to T, and ||f-h_1||_{H1}=O(||h||_{H1}^2). Therefore (A2),(A3) and boundedness of the quadratic forms give

    <h_1,L_+h_1>+<h_2,L_-h_2>
      >= c ||h||_{H1}^2-C||h||_{H1}^3.

The exact action expansion, using the mass constraint, is

    E(Q+h)=1/2[<h_1,L_+h_1>+<h_2,L_-h_2>]
             - integral Q h_1 |h|^2 - 1/4 integral |h|^4.

In two dimensions the remainder is O(||h||_{H1}^3+||h||_{H1}^4). Taking the neighborhood sufficiently small gives

    E(v) >= c' ||h||_{H1}^2.                          (A6)

Dividing by Mc converts this to the desired bound for eta=phi-q, with a fixed constant K. This explains precisely why the mass-critical scaling degeneracy causes no loss: it is killed by the exact kinetic normalization, through the second condition in (A5).

### A3. Small deficit implies entry into the local neighborhood

For completeness, the standard compactness argument is especially short under both normalizations. Suppose ||v_n||_2^2=||grad v_n||_2^2=Mc and E(v_n)->0. Their L4 norms stay away from zero, so the H1 vanishing lemma provides translations for which v_n converges weakly in H1 to v!=0. Pass to a subsequence with local almost-everywhere convergence. Hilbert norm splitting and the Brezis--Lieb lemma give, writing

    a=||v||_2^2/Mc,   b=||grad v||_2^2/Mc,

and applying sharp GN to v and the remainders,

    1 <= ab+(1-a)(1-b) <= 1.

Here a,b lie in (0,1]. The strict identity

    1-[ab+(1-a)(1-b)]=a(1-b)+b(1-a)

forces a=b=1. Thus convergence is strong H1, v is a sharp GN optimizer, and its fixed mass and kinetic norms identify it as exp(i theta)Q(. -y). This proves that all sufficiently small deficits enter the local neighborhood used in (A6). Combining A2 and A3 proves (G).

The scalar optimizer classification is classical (sharp GN, constant-phase equality in the diamagnetic inequality, and uniqueness of the positive radial ground state). It does not assert or require orbital stability of the mass-critical standing wave.

## Appendix B. Scope of the novelty search

The primary literature checks made on 2026-10-09 included the occupation-number GN/LT paper of Dolbeault--Felmer--Loss--Paturel, the finite-rank work of Frank--Gontier--Lewin, and targeted searches for sharp weighted eigenvalue sums, small secondary occupation, and near-rank-one exact constants. These searches did not locate this exact arbitrary-finite-rank plateau theorem. They do not establish priority or prove that it is absent from the literature. Until a broader source comparison is completed, describe this as a newly derived theorem in this project, not a confirmed first solution of a named historical conjecture.

Two neighboring facts must not be confused with it: occupation-number duality is old, and the scalar GN stability argument in Appendix A is classical. The specific content advanced here is the implication from the homogeneous Townes gap to an exact finite interval of occupation spectra, together with the separate computer-assisted envelope proof and independent mathematical audit establishing that gap.
