# The full negative spectrum of a finite hierarchy of two-dimensional wells

15 October 2026. This note proves a negative-eigenvalue count, including eigenvalues arbitrarily close to zero. It uses the free zero-energy logarithmic kernel and an exact finite-dimensional inertia calculation. It makes no claim of historical originality.

## 1. Result for the Townes pair

Let Q be the positive radial Townes solution of

    -Delta Q + Q - Q^3 = 0  on R^2,

let M = int Q^2, q = Q/sqrt(M), and fix z in R^2. For

    H_k = -Delta - Q(x)^2 - k^2 Q(kx-z)^2,

there exists k_0(z)>0 such that, for 0<k<k_0(z), H_k has exactly two negative eigenvalues, counted with multiplicity. It has no nonzero bounded distributional zero-energy solution. Both statements are uniform when z ranges over a fixed compact set, in the sense that k_0 can be chosen for that compact set.

The single-well input is the result proved in [scattering-sign.md](../townes-spectral-structure/scattering-sign.md): -Delta-Q^2 has exactly one negative eigenvalue and has no nonzero bounded zero-energy solution. The proof below is otherwise independent of the two-well eigenvalue expansion.

Consequently the R23 two-level expansion is the full negative spectral sum:

    Tr (H_k)_- - (1/(2M)) int [Q(x)^2+k^2 Q(kx-z)^2]^2 dx
      = -2 pi k^2 q(z)^2 / |log k| + O_z(k^2/|log k|^2) < 0.

Here Tr(H_k)_- denotes the sum of the absolute values of all negative eigenvalues. The full count removes the possible additional near-zero levels explicitly left open in Section 9 of [hierarchical-wells.md](../townes-spectral-structure/hierarchical-wells.md).

## 2. Single-well compressed logarithmic operator

We first record the scalar input in a form used by the proof. Let W>=0 be nonzero and bounded, with exponential decay, write w=sqrt(W), and assume -Delta-W has exactly one negative eigenvalue and has no nonzero bounded distributional zero-energy solution. Set

    m_W = ||w||_2^2,
    e_W = w/sqrt(m_W),
    P_W = I-|e_W><e_W|,
    K_W(x,x') = -(1/(2pi)) w(x) log|x-x'| w(x').

The operator K_W is Hilbert--Schmidt. On w-perp,

    Gamma_W := P_W (I-K_W) P_W >= c_W I > 0.             (2.1)

For completeness, the free two-dimensional resolvent gives, in Hilbert--Schmidt norm as alpha goes to zero,

    w(-Delta+alpha^2)^(-1)w
       = a_alpha |w><w| + K_W + o(1),
    a_alpha = (log(1/alpha)+log 2-EulerGamma)/(2pi).

If Gamma_W had a negative direction, that direction together with w would give two negative directions of the Birman--Schwinger complement for small alpha; this contradicts the assumption of one negative eigenvalue. Thus Gamma_W>=0.

If f in w-perp satisfies Gamma_W f=0, then (I-K_W)f=cw. The function

    psi(x) = c -(1/(2pi)) int log|x-y| w(y)f(y) dy

satisfies w psi=f and (-Delta-W)psi=0. The identity int wf=0 removes logarithmic growth at infinity; exponential decay and local logarithmic integrability make psi bounded. The zero-energy assumption therefore forces f=0. Since Gamma_W is identity minus compact, strict coercivity follows.

The same argument applies to any other well B satisfying these assumptions. No radiality is needed in Sections 2--7.

## 3. Two-channel Birman--Schwinger representation

Consider the general pair

    H_k = -Delta - W(x) - k^2 B(kx),

where both W and B satisfy Section 2. A fixed translated broad potential B(y)=Q(y-z)^2 is included. Write b=sqrt(B), m_B=||b||_2^2. On

    Hcal = L^2(R^2)_x direct-sum L^2(R^2)_y,

define the bounded map

    (A_k psi)_1(x)=w(x)psi(x),
    (A_k psi)_2(y)=b(y)psi(y/k).

Then A_k^*A_k is multiplication by W(x)+k^2B(kx). The positive compact operator

    K_alpha,k = A_k (-Delta+alpha^2)^(-1) A_k^*

has blocks

    K_11(x,x') = w(x) G_alpha(x-x') w(x'),
    K_22(y,y') = b(y) G_alpha((y-y')/k) b(y'),
    K_12(x,y)  = w(x) G_alpha(x-y/k) b(y),

where G_alpha(t)=(1/(2pi)) K_0(alpha|t|). The generalized Birman--Schwinger principle is exact:

    number of eigenvalues of H_k below -alpha^2
       = number of negative eigenvalues of I-K_alpha,k.  (3.1)

This follows either directly from the quadratic-form factorization or by equality of the nonzero spectra of A_k R_0 A_k^* and R_0^(1/2) A_k^*A_k R_0^(1/2). Extra zero directions in the two-channel representation do not change the count.

For each fixed k>0, let alpha go to zero. Put

    ell = log(1/k)/(2pi),   v=(w,b),
    C_k(x,y) = -(1/(2pi)) w(x) log|kx-y| b(y).

The exact scaling of the logarithm gives

    K_alpha,k = a_alpha |v><v| + K^0_k + o_k(1),         (3.2)

in operator norm, where

    K^0_k = [ K_W,                  C_k-ell |w><b| ;
              C_k^*-ell |b><w|,     K_B-ell |b><b| ].   (3.3)

The expansion (3.2) is only taken at fixed k. No uniformity in the simultaneous limit alpha/k -> 0 is assumed or needed. Exponential decay proves its Hilbert--Schmidt remainder by the usual small-argument expansion of K_0, followed by a tail cutoff.

## 4. Norm convergence of the cross kernel

As k goes to zero,

    C_k -> C_0 = |w><c_B| in Hilbert--Schmidt norm,
    c_B(y)=-(1/(2pi)) b(y)log|y|.                        (4.1)

In particular C_k is uniformly bounded. Here is a direct proof covering the logarithmic singularity. Define

    F(a)=int B(y) |log|y-a|-log|y||^2 dy.

The local translation continuity of log|y| in L^2_loc, boundedness of B, and its exponential tail imply F(a)->0 as a->0. Splitting into |y-a|<1 and its complement also gives

    F(a) <= C_B (1+|a|^2).

Indeed, the integral of log^2|y-a| on its unit ball is uniformly finite after using ||B||_infinity, and outside that ball log^2|y-a| is bounded by a constant times 1+|y|^2+|a|^2. Dominated convergence now applies to

    ||C_k-C_0||_HS^2 = (1/(4pi^2)) int W(x)F(kx) dx.

For translated B_z(y)=B_0(y-z), all bounds and convergence are uniform on compact sets of z.

## 5. Exact inertia after removal of the total logarithmic direction

Let P be the orthogonal projection onto v-perp in Hcal. Define

    Gamma_k = P(I-K^0_k)P restricted to v-perp.

Decompose this space orthogonally as

    v-perp = span{e_rel} direct-sum Z,
    Z = w-perp direct-sum b-perp,
    e_rel = (sqrt(m_B)e_W, -sqrt(m_W)e_B)/sqrt(m_W+m_B).

On Z, all explicit ell terms in (3.3) vanish. Equation (4.1) gives

    Gamma_k|_Z = Gamma_W direct-sum Gamma_B + o(1)
                >= (1/2)min(c_W,c_B) I                 (5.1)

for small k. The off-diagonal block between e_rel and Z is uniformly bounded, since the ell terms map entirely inside span{(w,0),(0,b)}. Along the relative direction the exact leading term is

    <e_rel, Gamma_k e_rel>
       = -ell m_W m_B/(m_W+m_B) + O(1).                (5.2)

Taking the Schur complement of the positive block (5.1) only subtracts a bounded nonnegative quantity from (5.2). Therefore Gamma_k is invertible and has exactly one negative eigenvalue for every sufficiently small k. Its remaining spectrum is separated from zero on the positive side; this also follows by the bounded invertible triangular congruence that diagonalizes its two blocks.

Now fix any such k and let alpha go to zero in (3.2). On span{v} direct-sum v-perp, the v-perp block of I-K_alpha,k tends to the invertible Gamma_k. It has exactly one negative eigenvalue for all sufficiently small alpha. Its off-diagonal block remains bounded at this fixed k. The scalar Schur complement along v equals

    -a_alpha ||v||_2^2 + O_k(1),

which is negative. By the inertia identity for a block operator with an invertible lower block, I-K_alpha,k therefore has exactly two negative eigenvalues for all sufficiently small alpha.

Equation (3.1) proves that H_k has exactly two negative eigenvalues in total. This last passage includes arbitrary shallow levels: if a third negative eigenvalue existed, choosing alpha smaller than its square-root absolute energy would contradict the count two. Conversely the count already supplies two negative eigenvalues.

## 6. Zero energy and the Townes spectral sum

For these small k, H_k has no nonzero bounded distributional zero-energy solution. To see this, suppose H_k psi=0 with psi bounded and set f=A_k psi and g=V_k psi. At each fixed k, the source g is bounded and exponentially integrable. Local elliptic regularity allows taking the circular mean a(r)=(1/(2pi))int_0^(2pi) psi(r,theta) dtheta, which satisfies

    r a'(r)=-(1/(2pi)) int_(|x|<r) g(x) dx.

If int g were nonzero, integration in r and exponential decay of g would force a(r)=-(int g)/(2pi) log r+O(1), contradicting boundedness. Thus int g=0. The logarithmic Newton potential

    n(x)=-(1/(2pi)) int log|x-y| g(y) dy

is then bounded and tends to zero at infinity. The difference psi-n is a bounded entire harmonic function, hence constant. The representation gives

    <v,f>=0,    (I-K^0_k)f=c v.

Consequently Gamma_k f=0 and f=0. Then psi is a bounded harmonic constant satisfying V_k psi=0; since V_k is nonzero, psi=0.

For W(x)=Q(x)^2 and B(y)=Q(y-z)^2, the assumptions of Section 2 were proved in R23. The first two eigenvalue expansions established there now exhaust the negative spectrum:

    lambda_1 = -1-k^2Q(z)^2+O_z(k^4),
    lambda_2 = -k^2+2pi k^2 q(z)^2/|log k|
               +O_z(k^2/|log k|^2).

Using int Q^4=2M and the radial first-moment cancellation,

    (1/(2M)) int V_k^2
       =1+k^2+k^2Q(z)^2+O_z(k^4).

This yields the full spectral-sum formula in Section 1. The sign is strict for each fixed z, because q(z)>0.

## 7. Any fixed finite hierarchy

Let W_1,...,W_N be nonzero bounded nonnegative exponentially decaying potentials, each satisfying the one-negative-eigenvalue and bounded-zero-solution assumptions of Section 2. Fix z_1,...,z_N in R^2 and set

    V(x)=sum_{j=1}^N k_j^2 W_j(k_j x-z_j),
    1=k_1>k_2>...>k_N>0.

For sufficiently small max_j(k_{j+1}/k_j), the operator -Delta-V has exactly N negative eigenvalues and no nonzero bounded zero-energy solution. N and the shapes W_j are fixed. The statement does not give estimates uniform in N.

Here is the extension of the preceding proof. Put w_j=sqrt(W_j), m_j=||w_j||_2^2, L_j=-log k_j, and use N channel coordinates y_j=k_j x-z_j. The total divergent zero-energy vector is v=(w_1,...,w_N). The diagonal logarithmic block is

    K_j^0 - (L_j/(2pi)) |w_j><w_j|.

For i<j the off-diagonal block equals

    -(L_j/(2pi)) |w_i><w_j| + C_ij,

where

    C_ij(y_i,y_j)=-(1/(2pi))w_i(y_i)
       log |(k_j/k_i)(y_i+z_i)-(y_j+z_j)| w_j(y_j).

As k_j/k_i goes to zero, C_ij tends in Hilbert--Schmidt norm to a rank-one kernel with w_i as its left factor. The proof is precisely Section 4, with a translated broad variable. All C_ij remain uniformly bounded for fixed N and fixed centers.

On Z=direct-sum_j w_j-perp, the compressed complement therefore tends in norm to direct-sum_j Gamma_j>0. The complementary finite-dimensional subspace inside v-perp consists of vectors f_j=a_j e_j, e_j=w_j/sqrt(m_j), with

    c_j=sqrt(m_j)a_j,       sum_j c_j=0.

For these vectors the logarithmically large part of the quadratic form of the Birman--Schwinger kernel is exactly

    -(1/(2pi)) sum_{i,j} max(L_i,L_j) conjugate(c_i)c_j
      =(1/(2pi)) sum_{j=1}^{N-1} (L_{j+1}-L_j)
                     |sum_{i=1}^j c_i|^2.              (7.1)

One proves (7.1) by writing max(L_i,L_j)=L_1+sum_l (L_{l+1}-L_l)1_{max(i,j)>l}. The total-zero constraint removes the constant term, and the remaining contribution is the square of the partial sum. The map from zero-sum c to its N-1 partial sums is invertible. For fixed m_j and N, the right side is consequently bounded below by

    C_{N,m} min_j(L_{j+1}-L_j) sum_j |a_j|^2.

Thus the complement I-K^0 is strictly negative on this N-1 dimensional mass-relative block once the minimum logarithmic gap is large. Its coupling to Z is bounded, whereas Z is uniformly positive. The Schur complement is negative definite, so the compression to v-perp is invertible with exactly N-1 negative directions. Taking alpha to zero at these fixed scales supplies the last negative direction along v, exactly as in Section 5. Hence the total negative-eigenvalue count is N. Invertibility of the compression also excludes bounded zero-energy solutions as in Section 6.

This finite-hierarchy theorem counts all negative levels without a joint scale-energy limit, and without radial or reflection symmetry of the individual potentials. It does not determine the spectral-sum sign for every N-core family, since that additionally requires sufficiently precise eigenvalue and potential-energy interaction expansions. Only the Townes pair's full sum is evaluated here.

## 8. Spectral-count additivity beyond one bound state per well

The count in Section 7 has a stronger form. Retain boundedness, nonnegativity, nontriviality, exponential decay, fixed finite N, and fixed scaled centers. Replace the one-negative-eigenvalue assumption by

    -Delta-W_j has n_j negative eigenvalues, and has no nonzero
    bounded distributional zero-energy solution,

where 1<=n_j<infinity. Then, for sufficiently separated adjacent scales,

    N_-(-Delta-sum_j k_j^2 W_j(k_j x-z_j)) = sum_j n_j,   (8.1)

and zero has no nonzero bounded distributional solution.

Proof. The kernel argument in Section 2 still proves that Gamma_j is invertible. At each fixed j, the rank-one divergent free Birman--Schwinger expansion and a scalar Schur complement show

    index_-(Gamma_j) = n_j-1.                           (8.2)

Indeed, for all sufficiently small alpha the total Birman--Schwinger complement has one additional negative direction along w_j, while its compression tends to the invertible Gamma_j. Its negative index equals n_j by the usual Birman--Schwinger principle.

For the multiwell operator the Z block now converges in norm to the invertible operator direct-sum_j Gamma_j. It is uniformly invertible and its negative index equals sum_j(n_j-1). The mass-relative finite-dimensional block of I-K^0 tends to minus infinity at the rate min_j log(k_j/k_{j+1}), by (7.1). Its coupling to Z is uniformly bounded. The Schur correction is consequently bounded even though the Z block need not be positive. Thus its Schur complement is negative definite and has dimension N-1. The compressed full zero-energy operator has negative index

    sum_j(n_j-1)+(N-1)=sum_j n_j-1.

It is invertible. Finally the total logarithmic vector contributes one further negative direction as alpha goes to zero at these fixed scales. This proves (8.1), and the representation in Section 6 excludes bounded zero-energy solutions.

For N=1 the statement is the given single-well count; the scale separation condition is empty. The general theorem does not require the potentials to solve a nonlinear equation. The nonlinear Townes structure is used to establish the single-well spectral input and to evaluate the two-well spectral-sum coefficient.

## 9. Two fixed wells separated in space

There is an analogous full-spectrum statement for spatial separation. Let W_1,W_2 be nonzero bounded nonnegative exponentially decaying potentials in R^2. Assume h_j=-Delta-W_j has n_j negative eigenvalues, counted with multiplicity, and has no nonzero bounded distributional zero-energy solution. Then, for all sufficiently large R,

    H_R=-Delta-W_1(x)-W_2(x-R e_1)

has exactly n_1+n_2 negative eigenvalues and no nonzero bounded zero-energy solution. The potentials and their scales are fixed as R tends to infinity.

Use the two-channel map

    (A_R psi)_1(x)=w_1(x)psi(x),
    (A_R psi)_2(y)=w_2(y)psi(y+R e_1),

where w_j=sqrt(W_j). The free zero-energy expansion has divergent vector v=(w_1,w_2), diagonal blocks K_1^0,K_2^0, and off-diagonal block

    C_R(x,y)=-(1/(2pi))w_1(x)log|x-y-R e_1|w_2(y)
            =-ell_R |w_1><w_2|+E_R,
    ell_R=log R/(2pi),
    ||E_R||_HS -> 0.                                  (9.1)

The moving logarithmic singularity in (9.1) is controlled as follows. Its squared norm is a constant times

    int W_1(x)W_2(y) |log(|x-y-R e_1|/R)|^2 dx dy.

On |x|+|y|<=R/2, the ratio inside the logarithm lies in [1/2,3/2], and

    |log(|x-y-R e_1|/R)|<=C(|x|+|y|)/R.

Finite second moments give an O(R^(-2)) contribution. On the complementary set, choose a>0 such that W_1(x)W_2(y)<=C exp[-a(|x|+|y|)]. Factor out exp(-aR/4), leaving exp[-a(|x|+|y|)/2]. For |x-y-R e_1|>=1, the square logarithm is bounded by C[1+|x|^2+|y|^2+R^2+log^2 R], integrable against this remaining weight. For |x-y-R e_1|<1, use u=x-y-R e_1 and retain the integrable exp(-a|y|/2) factor; int_{|u|<1}log^2|u|du is finite. Thus the complementary contribution is at most

    C exp(-aR/4)(1+R^2+log^2 R),

which proves (9.1) directly in Hilbert--Schmidt norm.

The compressed complement on Z=w_1-perp direct-sum w_2-perp converges to the invertible Gamma_1 direct-sum Gamma_2, of negative index n_1+n_2-2. Let m_j=||w_j||_2^2 and e_j=w_j/sqrt(m_j). The remaining relative direction is

    e_rel=(sqrt(m_2)e_1,-sqrt(m_1)e_2)/sqrt(m_1+m_2).

Its quadratic form for the compressed I-K^0 is

    -2ell_R m_1m_2/(m_1+m_2)+O(1).                   (9.2)

The factor 2 differs from the scale-separated calculation because only the two off-diagonal blocks contain log R here. The coupling to Z stays bounded. Its Schur complement is therefore negative for large R, giving compressed negative index n_1+n_2-1 and no kernel. At each such fixed R, taking the spectral parameter alpha to zero supplies one further negative direction along v. This proves the full count n_1+n_2. The zero-energy representation from Section 6 excludes bounded zero-energy solutions.

## 10. Consequences for every fixed two-Townes-well scale ratio

For every fixed 0<k<1, apply Section 9 to

    W_1(x)=Q(x)^2,    W_2(x)=k^2Q(kx)^2.

The single-well spectral property is invariant under this scaling; each well has exactly one negative eigenvalue and no bounded zero-energy solution. Hence the first two negative eigenvalues exhaust the spectrum for large separation R.

The R22 relaxed interaction formula therefore becomes the full trace formula

    Tr(H_{k,R})_- -(1/(2M))int [Q(x)^2+k^2Q(k(x-R e_1))^2]^2 dx
      =epsilon_R^2 A(k)+o_k(epsilon_R^2),
    epsilon_R=A_q sqrt(k) R^(-1/2)exp(-kR),
    q(r)~A_q r^(-1/2)exp(-r).

The all-scale radial comparison and the completed angular enclosure in
[scattering-2cc19db4.md](scattering-2cc19db4.md), [r24_certified_angular.py](../../computations/all-scale-scattering/r24_certified_angular.py), and
[r24_certified_angular.json](../../computations/all-scale-scattering/r24_certified_angular.json) establish A(k)<0 for every 0<k<1. Thus the full trace lies strictly below (1/(2M))int V^2 for all sufficiently large R at every fixed unequal scale ratio. No possible additional negative level near zero is omitted.

At equal scales, Section 9 likewise upgrades the R22 formula in
[fixed-potential.md](../separated-cores/fixed-potential.md) to

    (1/(2M))int [Q(x)^2+Q(x-R e_1)^2]^2 dx - Tr(H_R)_-
      =(8pi A_Q^4/M^2) exp(-2R)(1+o(1))>0,
    Q(r)~A_Q r^(-1/2)exp(-r).

Scale ratios greater than one reduce to ratios less than one by exchanging and dilating the wells. Hence every fixed positive scale ratio is covered for sufficiently large separation. This assertion is not uniform in a joint limit k=k(R) tending to zero or one. It concerns these specified undeformed two-well potentials, while fully relaxing their spectral states; it does not resolve arbitrary overlapping potentials or the global sharp Lieb--Thirring constant.
