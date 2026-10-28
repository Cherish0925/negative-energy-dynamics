# Quantitative intrinsic spreading for bounded negative-energy BNLS dynamics

Research note, 2026-10-07. This note contains an analytic result independent of every numerical profile, inverse bound, and computer-assisted traveling-wave certificate in the project. The interaction functional itself is established technology: compare Komada, arXiv:2609.33381v1, Section 5, Proposition 5.2. The contribution developed here is a one-sided estimate in terms of pairwise **mass** tails, without compactness of the orbit, followed by a quantitative ballistic spreading consequence.

## 1. Statement

Let N >= 1 and let u be a standard strong H2 solution on [0,infinity) of

    i u_t = Delta^2 u - |u|^beta u,

where beta = 8/N. Set

    M = integral |u|^2 > 0,
    E = (1/2) integral |Delta u|^2 - (1/(beta+2)) integral |u|^(beta+2),
    P = Im integral conjugate(u) grad u.

Assume E < 0, P = 0, and

    K = sup_{t >= 0} ||Delta u(t)||_2 < infinity.

No radial symmetry, moment condition, orbit precompactness, or smooth concentration-center trajectory is assumed. For R > 0 define

    D_R(t) = double integral_{|x-y| > R} |u(t,x)|^2 |u(t,y)|^2 dx dy,
    d_R(t) = D_R(t) / M^2 in [0,1].

**Theorem 1 (pairwise escape inequality).** There are finite constants A,B,C > 0, depending only on N,M,K and fixed universal cutoff choices, such that, for every S >= 0, T > 0, and R >= 1,

    16 M |E| <= A R/T + B/R^2
                   + (C/T) integral_S^(S+T) d_R(t)^theta dt,

where

    theta = min(4/N, 1/4).

**Theorem 2 (intrinsic ballistic spreading).** There are c,delta,eta,T0 > 0, depending only on N,M,K,|E|, such that for every S >= 0 and T >= T0,

    measure { t in [S,S+T] : D_(cT)(t) >= delta M^2 } >= eta T.

Consequently, at each of the times in that same set,

    inf_{a in R^N} integral_{|x-a| > cT/2} |u(t,x)|^2 dx
        >= (delta/2) M.

Thus every possible center fails to contain a fixed positive mass fraction in a ball of radius cT/2 at a positive proportion of times in each long interval. This is intrinsic separation, not escape caused merely by translating a single compact profile.

The theorem does not assert that such zero-momentum global bounded solutions exist, nor does it prove their finite-time blowup. It supplies a necessary behavior for any such solution. Two oppositely traveling coherent structures would be compatible with this conclusion if an exact multiwave solution were constructed.

## 2. Fixed cutoffs and elementary estimates

Choose a smooth real radial phi on R^N satisfying

    phi(x) = |x|^2/2 for |x| <= 4,
    grad phi(x) = 0 for |x| >= 8,
    D^2 phi(x) <= Identity in the sense of quadratic forms,
    ||D^j phi||_infinity < infinity, 1 <= j <= 6.

Such a cutoff is obtained by smoothly turning its radial derivative from r to zero, keeping phi'' <= 1 and phi'/r <= 1. Nonnegativity of the Hessian is neither required nor claimed. Put phi_R(x)=R^2 phi(x/R). Then

    ||D^j phi_R||_infinity <= C_j R^(2-j),
    D^2 phi_R - Identity = 0 on |x| <= 4R,
    Delta phi_R - N = 0 on |x| <= 4R.

Choose eta_R(x)=eta(x/R), where eta is smooth, zero on |x|<=1, one on |x|>=2, and takes values in [0,1]. For a fixed center a define m_r(a)=integral_{|x-a|>r}|u(x)|^2. With

    G = M^(1/4) K^(1/2),
    H_R = K + C_eta G/R + C_eta sqrt(M)/R^2,

the interpolation inequality ||grad u||_2^2 <= ||u||_2 ||Delta u||_2 gives ||grad u||_2 <= G. The product rule gives

    ||Delta(eta_R(.-a)u)||_2 <= H_R,
    ||eta_R(.-a)u||_2^2 <= m_R(a).

The mass-critical Gagliardo--Nirenberg inequality implies

    integral_{|x-a| > 2R} |u|^(2+8/N)
      <= C_N m_R(a)^(4/N) H_R^2.                         (2.1)

The corresponding localized gradient bound is

    integral_{|x-a| > 2R} |grad u|^2
      <= ||grad(eta_R(.-a)u)||_2^2
      <= sqrt(m_R(a)) H_R.                              (2.2)

These estimates need only a mass tail, not a Delta-u tail. For R >= 1, H_R is bounded above by a constant depending on M,K and the cutoff.

## 3. One-particle virial upper bound without radiality

Write rho=|u|^2 and j=Im(conjugate(u) grad u). For a fixed y let

    M_R^y(u) = 2 integral grad phi_R(x-y) dot j(x) dx.

The standard fourth-order commutator identity, with repeated indices summed, is

    d/dt M_R^y(u)
      = 8 Re integral (partial_jk phi_R)(partial_ij conjugate(u))(partial_ik u)
        -4 Re integral (partial_jk Delta phi_R)(partial_j conjugate(u))(partial_k u)
        -2 integral (Delta^2 phi_R)|grad u|^2
        + integral (Delta^3 phi_R)rho
        -(2 beta/(beta+2)) integral (Delta phi_R)|u|^(beta+2).       (3.1)

All cutoff functions in (3.1) are evaluated at x-y. The leading Hessian form is bounded above by 8||D^2u||_2^2=8||Delta u||_2^2 because D^2 phi_R <= Identity. This argument is valid for arbitrary complex, nonradial u. The remaining derivative-of-cutoff terms are at most C(R^-2 G^2+R^-4 M). Therefore

    d/dt M_R^y(u)
      <= 16 E + C(R^-2 G^2+R^-4 M)
           + C integral_{|x-y|>4R} |u(x)|^(2+8/N) dx.       (3.2)

The inequality, rather than a two-sided approximation, is the useful point: there is no uncontrolled positive Delta-u tail.

For standard H2 solutions, (3.1) is understood in integrated form, obtained first for regularized solutions and then by strong H2 approximation. Every term on its right has a continuous H2 realization. This is the same energy-space justification used for localized fourth-order virial identities; no spatial moments are introduced.

## 4. Interaction identity and the momentum-flux term

Define the interaction virial

    I_R(t) = integral rho(t,y) M_R^y(u(t)) dy
           = 2 double integral rho(t,y) grad phi_R(x-y) dot j(t,x) dx dy.

It is finite, and

    |I_R(t)| <= 2 ||grad phi||_infinity R M^(3/2) G.          (4.1)

Define also

    w(t,x) = Im(Delta u(t,x) grad conjugate(u(t,x))),
    W(t) = integral w(t,x) dx,

so |W(t)| <= K G. The mass equation, tested against any suitable real f, is

    integral f rho_t
      = 2 Im integral (Delta f) conjugate(u) Delta u
        +4 Im integral grad f dot (Delta u grad conjugate(u)).    (4.2)

When differentiating I_R, the part in which rho(t,y) is differentiated equals exactly

    Y_R(t)
      = 4 double integral D^2 Delta phi_R(x-y)[j(t,x),j(t,y)] dx dy
        -8 double integral D^2 phi_R(x-y)[j(t,x),w(t,y)] dx dy.    (4.3)

To verify the first term, initially (4.2) gives

    4 double integral j_j(x) (partial_j Delta phi_R)(x-y)
                         Im(conjugate(u(y)) Delta u(y)) dxdy.

Use Im(conjugate(u)Delta u)=div j and integrate once in y. This yields the first term of (4.3), with the displayed positive sign. Thus its absolute value is at most

    C R^-2 ||j||_1^2 <= C R^-2 M G^2.                    (4.4)

Splitting the second term using D^2 phi_R=Identity+(D^2 phi_R-Identity) gives

    Y_R(t) = -8 P dot W(t) + O(R^-2 M G^2) + Tail_R(t),

where

    |Tail_R(t)| <= C double integral_{|x-y|>4R}
                   |u(x)| |grad u(x)| |Delta u(y)| |grad u(y)| dxdy.  (4.5)

No phase-space moment beyond H2 appears. In particular, W is well-defined even when the center of mass is not.

## 5. Controlling interaction errors by pairwise mass alone

Apply Cauchy--Schwarz on R^N_x times R^N_y to (4.5):

    |Tail_R(t)| <= C G K sqrt(B_R(t)),

where

    B_R(t) = double integral_{|x-y|>4R} rho(t,x)|grad u(t,y)|^2 dxdy.

Using (2.2) at scale 2R with center x yields

    B_R(t)
      <= H_(2R) integral rho(t,x) sqrt(m_(2R)(x)) dx
      <= H_(2R) sqrt(M D_(2R)(t))
      <= H_(2R) sqrt(M D_R(t)).                            (5.1)

The middle inequality is Cauchy--Schwarz, because integral rho(x)m_(2R)(x) dx = D_(2R). Consequently

    |Tail_R(t)| <= C G K H_(2R)^(1/2) (M D_R(t))^(1/4)
                <= C(N,M,K) d_R(t)^(1/4), R>=1.            (5.2)

For the nonlinear remainder in (3.2), (2.1) at scale 2R gives

    integral rho(y) integral_{|x-y|>4R} |u(x)|^(2+8/N) dxdy
      <= C H_(2R)^2 integral rho(y)m_(2R)(y)^q dy,

where q=4/N. Let alpha=min(q,1). Jensen if q<=1, or m^(q)<=M^(q-1)m if q>=1, gives

    integral rho(y)m_(2R)(y)^q dy
      <= M^(q+1) d_(2R)^alpha
      <= M^(q+1) d_R^alpha.                               (5.3)

Combining (3.2), (4.3), (5.2), and (5.3), and using 0<=d_R<=1, proves the pointwise-in-time upper bound

    I_R'(t) <= 16 M E - 8 P dot W(t)
                         + B/R^2 + C d_R(t)^theta,         (5.4)

with theta=min(4/N,1/4). The R^-4 term is absorbed into R^-2 for R>=1.

This is the central estimate. It remains valid for arbitrary P, independently of precompactness.

## 6. Integration and ballistic spreading

Integrate (5.4) over [S,S+T] and use (4.1). For general P this gives

    -16 M E + (8/T) P dot integral_S^(S+T) W(t) dt
       <= A R/T + B/R^2 + (C/T) integral_S^(S+T) d_R(t)^theta dt.   (6.1)

For P=0, this is Theorem 1. Put e=|E|, increase C if necessary so C>=16Me, and choose c>0 small enough that Ac<=4Me. Choose T0 so cT>=1 and B/(cT)^2<=4Me for all T>=T0. Then R=cT gives

    (1/T) integral_S^(S+T) d_(cT)(t)^theta dt >= epsilon,
    epsilon = 8Me/C in (0,1/2].                            (6.2)

Set delta=(epsilon/2)^(1/theta), eta=epsilon/2. Since 0<=d^theta<=1, the contribution from times with d<delta is at most epsilon/2, and the contribution from the other times is at most their relative measure. Hence

    measure {t in [S,S+T]:d_(cT)(t)>=delta} >= eta T.

Finally, for every a and r>0, a pair with |x-y|>2r has at least one of x,y outside B(a,r). Therefore

    D_(2r)(t) <= 2M integral_{|x-a|>r} rho(t,x) dx.

Taking r=cT/2 proves the all-centers assertion in Theorem 2.

## 7. Consequences and consistency checks

### 7.1. No mass-tight bounded orbit at zero momentum

If a globally H2-bounded solution has P=0 and is uniformly mass-tight modulo arbitrary translations, namely

    lim_(R->infinity) sup_(t>=0) inf_a integral_{|x-a|>R}|u(t,x)|^2 dx = 0,

then E cannot be negative. Indeed, uniform mass tightness forces sup_t d_R(t)->0, contradicting Theorem 1 by first taking T->infinity and then R->infinity. No H2 orbit precompactness and no regularity of a chosen center are required.

This is an exclusion theorem for negative energy, not a classification at E=0.

### 7.2. A genuine increase in intrinsic diameter

At the times in Theorem 2, no ball of radius cT/2 contains more than (1-delta/2)M of the mass. In particular, an arbitrary choice of moving coordinate frame cannot remove the conclusion. A single traveling wave has time-independent D_R and is therefore ruled out at negative energy if its momentum is zero.

### 7.3. Translation-only consistency test

For an exact mass-critical traveling wave u(t,x)=exp(i omega t)Q(x-vt) with sufficient decay, conservation of local mass gives

    W = Mv/4.

The profile virial relation is E=v dot P/8. Consequently the left side of (6.1) is

    -16ME + 8P dot(Mv/4)=0.

Thus the general defect inequality does not incorrectly rule out the negative-energy nonzero-momentum traveling waves sought in the main project. The P=0 hypothesis has a specific mathematical role.

### 7.4. Finite-variance corollary

Whenever the moments exist,

    double integral |x-y|^2 rho(x)rho(y) dxdy
      = 2M inf_a integral |x-a|^2 rho(x) dx.

Theorem 2 implies a lower bound of order T^3 on the integral over [S,S+T] of this optimal-center variance. This is a time-average statement; it does not assert a pointwise variance lower bound at every time.

### 7.5. Nonzero momentum with a positive energy-flux defect

The assumption P=0 can be replaced by any uniform positive lower bound on the left side of (6.1). In particular, |W(t)|<=KG implies that intrinsic ballistic spreading still follows if

    16M|E| - 8|P|KG > 0,

or, equivalently,

    |E| > |P| K^(3/2) / (2 M^(3/4)).

A global bounded negative-energy orbit that remains uniformly mass-tight modulo translations must therefore satisfy the opposite necessary inequality. More precisely, (6.1), followed first by T->infinity and then R->infinity, yields

    limsup_(T->infinity) P dot [(1/T) integral_0^T W(t)dt] <= 2ME < 0.

Thus a tight negative-energy coherent motion requires an averaged third-order dispersive flux opposed to the conserved momentum. For a traveling wave this becomes v dot P = 8E exactly. The inequality alone does not establish equality for arbitrary mass-tight dynamics.

## 8. Extension to every mass-supercritical, energy-subcritical power

The same result holds for every beta satisfying

    beta >= 8/N,
    beta < 8/(N-4) if N>=5,
    beta < infinity if N<=4.

Use the energy E_beta with power beta+2. The one-particle virial main term is

    2N beta E_beta - (N beta-8)||Delta u||_2^2
        <= 2N beta E_beta.

The localized Gagliardo--Nirenberg estimate is

    integral_{|x-a|>2R}|u|^(beta+2)
      <= C m_R(a)^gamma H_R^(N beta/4),
    gamma = 1 - beta(N-4)/8 > 0.

Consequently (5.4) becomes

    I_R' <= 2N beta M E_beta -8P dot W + B/R^2 + C d_R^theta,
    theta = min(gamma,1/4)>0.

For P=0,E_beta<0, all conclusions follow with 16 replaced by 2N beta. The energy-critical endpoint is not included, because gamma=0 there and a mass tail alone does not control the nonlinear tail. No claim is made about that endpoint.

## 9. Position relative to prior work

1. Boulenger--Lenzmann, *Blowup for biharmonic NLS*, arXiv:1503.01741v2 / Anal. Sci. ENS 50 (2017): the fourth-order commutator behind (3.1), and its favorable leading sign, are standard ingredients of their localized virial proof. Their radial nonlinear-tail estimate is replaced here by a mass-tail Gagliardo--Nirenberg bound under a global H2 bound.
2. Koichi Komada, *Scattering of group-invariant solutions below the ground state for the fourth-order NLS*, arXiv:2609.33381v1, 27 September 2026, Section 5, Proposition 5.2: the interaction functional used here and the momentum-flux term are already present. That proposition obtains a time-averaged identity for H2-precompact orbits. The present note does not claim to invent the interaction virial. Its distinct analytic content is the quantitative one-sided estimate (5.4), using pairwise mass tails alone, and the positive-density ballistic consequence for general bounded negative-energy dynamics.

The novelty of the precise quantitative theorem still requires a full literature check. Its proof is supplied explicitly so its mathematical validity is not contingent on a novelty claim.

Primary sources inspected in this turn:

- https://arxiv.org/pdf/1503.01741 (commutator equations (3.7)--(3.9), nonlinear term in Lemma 3.1).
- https://arxiv.org/html/2609.33381v1 (Proposition 5.2 and equations (5.9)--(5.14)).
