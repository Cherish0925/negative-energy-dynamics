# Round 13: kinetic amplification for general homogeneous dispersion

## Result and scope

Let m>2, s=m/2, N>=1, and let a be real, even, positive elliptic,
m-homogeneous, C^{N+2} away from zero. Consider

    i u_t = a(D)u - |u|^{2m/N}u,
    A(u)=||a(D)^{1/2}u||_2^2, M=||u||_2^2,
    E=A/2-||u||_p^p/p, p=2+2m/N.

Let M_c be the sharp GN mass and d=(M/M_c)^{m/N}-1.
For fixed a,N,m there exist d_0,c,C>0 such that every strongly
approximable conservative maximal H^s flow, with the usual continuation
alternative and

    P=0, E=-e<0, 0<d<d_0,

satisfies

    sup_{0<=t<T+} A(u(t)) >= c e d^{-alpha_m},
    alpha_m = 1 + m/[2(m-1)].                         (1)

For a forward-global uniformly H^s-bounded solution this is equivalently

    e <= C d^{alpha_m} sup_{t>=0} A(u(t)).             (2)

The theorem includes every positive elliptic even homogeneous polynomial
of degree 2k>=4, as well as isotropic fractional symbols |xi|^m for every
real m>2. Convexity of a, radial symmetry, finite moments, uniqueness of
the scalar ground state, and real-sector linearized nondegeneracy are
not assumed. Local well-posedness for every symbol/dimension is not
claimed; the theorem explicitly specifies the conservative flow class.

For every real sharp ground state Q, take

    u_d(0)=(1+d)^{N/(2m)}Q.

Then e=d A(u_d(0))/2, so

    sup A(u_d(t))/A(u_d(0)) >= c d^{-m/[2(m-1)]}.      (3)

Under the stated continuation alternative this forces every fixed finite
amplification factor to be crossed in finite time for all sufficiently
small d. In particular it gives orbital instability of each real sharp
standing wave in the stated solution class. The m=4 case is round 12.

This is NOT a proof of universal finite-time blowup or growup. The right
side is finite for each fixed d>0, and sufficiently large bounded global
motion is still logically compatible with the estimate.

## The essential new point: general negative exterior kinetic term

The old quartic proof used the favorable Hessian form of the biharmonic
virial. That sign is unavailable for a general anisotropic symbol. It is
not needed: factor the localized commutator through a(D)^{1/2}, put all
direction-dependent pieces in a transition annulus, and average disjoint
annuli in time. All nonlocal commutations have vanishing error uniformly
on an H^s ball. The proof below uses elementary Fourier estimates, not
an unsupported application of sharp Garding or pseudolocality.

### Fourier estimates

Write b(xi)=sqrt(a(xi)) and

    B_jk(xi)=partial_j a(xi) xi_k/a(xi), xi!=0.

These are real even bounded degree-zero multipliers, and

    sum_j B_jj(xi)=m.

For every smooth compact cutoff theta and R>=1,

    ||[B_jk(D),theta(x/R)] b(D)u||_2
       <= C R^{-1} ||u||_{H^s},                       (4)
    ||[b(D),theta(x/R)]u||_2
       <= C R^{-1} ||u||_{H^s}.                       (5)

Indeed, with h=xi-zeta, homogeneity and angular C^1 regularity give

    |B_jk(xi)-B_jk(zeta)| b(zeta)
       <= C |h| |zeta|^{s-1}.

For |h|<=|zeta|/2 use the degree-minus-one derivative bound; otherwise
use boundedness and |zeta|<=2|h|. Since s>1, no singular power remains
at zeta=0. Young convolution and
|| |h| theta_R_hat(h)||_1=O(R^{-1}) prove (4).
For (5), use

    |b(xi)-b(zeta)|<=C |h| (|zeta|+|h|)^{s-1}.

This gives O(R^{-1})||u||_{H^{s-1}}+O(R^{-s})||u||_2.

Take h_0 in C_c^infinity(R^N), radial, 0<=h_0<=1, h_0=1 on B_1,
h_0=0 outside B_2. Define

    f_R(x)=x h_0(x/R),
    L_R=f_R dot grad+(div f_R)/2,
    C_R=[a(D),L_R].

For u in H^s, g=b(D)u,

    <u,C_Ru>
       = Re sum_jk <g,(partial_j f_R,k) B_jk(D)g>
         + O(R^{-1}||u||_{H^s}^2).                  (6)

Proof of (6): the Fourier kernel of C_R is

    (i/2)[a(xi)-a(zeta)](xi+zeta)_k f_R,k_hat(h).

The kernel of sum_jk (partial_j f_R,k) q_jk(D), where
q_jk(xi)=partial_j a(xi)xi_k, is

    i h_j f_R,k_hat(h) partial_j a(zeta)zeta_k.

Their difference is bounded by

    C |h|^2 (|zeta|+|h|)^{m-1} |f_R_hat(h)|.

This follows from second-order Taylor expansion of a. Its second
derivatives extend continuously at zero because m>2. After dividing by
<xi>^s<zeta>^s the polynomial factor has at most polynomial growth in h;
Schur's test and f_R_hat(h)=R^{N+1}f_1_hat(Rh) give O(R^{-1}).
Replacing q_jk(D) by the b(D)-sandwich changes its Fourier kernel by

    [b(zeta)-b(xi)]b(zeta)B_jk(zeta)
                     (partial_j f_R,k)_hat(h).

Its absolute value is bounded by
C |h| (|zeta|+|h|)^{m-1}|(partial_j f_R,k)_hat(h)|;
the same weighted Schur test gives O(R^{-1}). Taking real parts proves
(6). This also proves the forms extend from Schwartz functions to H^s.

Now partial_j f_R,k=h_0(x/R)delta_jk+c_jk,R, where c_jk,R is uniformly
bounded and supported on R<|x|<2R. The diagonal identity sum B_jj=m
makes the h_0 term exactly m integral h_0|g|^2. Choose theta_R equal
one on this annulus and supported in R/2<|x|<4R. Since c theta=c,

    <g,c B g>=<theta g,c B(theta g)>+<theta g,c[B,1-theta]g>.

By (4) its magnitude is at most

    C integral_{R/2<|x|<4R}|g|^2 + O(R^{-1}||u||_{H^s}^2).

Therefore

    <u,C_Ru> <= m A(u) - m integral_{|x|>2R}|g|^2
       + C integral_{R/2<|x|<4R}|g|^2
       + O(R^{-1}||u||_{H^s}^2).                    (7)

Translation does not change any constant. There is NO pointwise sign
assertion about partial_x f partial_xi a; the whole anisotropic
transition contribution is displayed in the annulus.

## Complete dynamical argument

### 1. Critical geometry and slow mass transport

The real two-component version of round-11 quantitative polarization
applies to u=(Re u,Im u). The proof uses only sharp GN compactness,
constant-phase equality cases, and phase-sector coercivity. Thus

    inf_theta [M(Im(e^{-i theta}u))/M + A(Im(e^{-i theta}u))/A]
       <= C [1-||u||_p^p/((p/2)(M/M_c)^{m/N} A)].     (8)

The normalized real scalar ground family is compact, making C uniform.
This is not the vacuous one-dimensional complex polarization statement.

Normalize sup_t A(u(t))=1 by the critical scaling. Then

    2e/d <= A(t)<=1,
    ||u||_{H^s}<=C,
    u=e^{i theta(t)}(X+iY), ||Y||_{H^s}<=C sqrt(d).     (9)

Each phase is chosen separately; its time derivative is never used.
For a real cutoff chi_R about any fixed point, the nonlinear contribution
to d/dt integral chi_R |u|^2 vanishes. The linear commutator obeys

    |<v,[a(D),chi_R]w>|<=C R^{-1}||v||_{H^s}||w||_{H^s}. (10)

Indeed |a(xi)-a(zeta)|<=C|h|(|zeta|+|h|)^{m-1}; division by
<xi>^s<zeta>^s and Fourier-Schur gives (10). As a is real even and chi
real, the real-real and imaginary-imaginary terms do not contribute to
the derivative. Equations (9)-(10) yield

    |d/dt integral chi((x-z)/R)|u|^2|<=C sqrt(d)/R.    (11)

Sharp optimizer compactness and the positive lower bound A>=2e/d
give a finite radius R_0 (possibly depending on e/d) about a center at
each time that contains M_c-epsilon_0 mass. Centers at times separated
by at most c R_0/sqrt(d) cannot move more than C R_0, by (11) and the
fact M is close to M_c. Piecewise-linear interpolation produces a(t)
with

    ||a'||_infinity<=L=C sqrt(d),                    (12)

and a fixed-radius ball about a(t) containing M_c-epsilon_0 at every
time. Crucially L is independent of R_0 and e/d.

### 2. Uniform exterior mass

For each eta>0, sufficiently large R_eta gives

    sup_t integral_{|x-a(t)|>R_eta}|u|^2<=M-M_c+eta=:mu. (13)

The proof is the same weak-splitting argument as round 12 and works for
all a: a violation gives a translated weak H^s limit v with
M_c-epsilon_0<=M(v)<=M_c-eta. The remainder mass is also below M_c.
The A quadratic form and L^p interaction split, so negative total energy
would be a sum of two nonnegative subcritical energies. Contradiction.
Local compactness and Brezis-Lieb apply because p=2+2m/N is strictly
below the H^s Sobolev exponent when N>m, and finite otherwise.

### 3. Moving virial with controlled exterior terms

Define J_R=2 Im integral f_R(x-a(t)) dot bar u grad u. Since s>1,
|J_R|<=C R. Fix R>=4 R_eta and put

    K_R=integral_{|x-a|>8R}|g|^2,
    H_R=integral_{R/4<|x-a|<8R}|g|^2.

The integrated localized identity, (7), the local-power nonlinear
commutator, and P=0 give

    J_R' <= -4m e -2m K_R + C H_R + C R^{-1}
       + C integral_{|x-a|>R}|u|^p
       + C L integral_{|x-a|>R}|u||grad u|.           (14)

The motion error is the difference from -2 a' dot P=0. It is supported
outside the radius-R ball because Df_R=I inside that ball.

Choose zeta_R=0 on B_{R/4}, =1 outside B_{R/2}. Equations (5),(13) give

    M(zeta_Ru)<=mu,
    A(zeta_Ru)<=C(K_R+H_R)+C R^{-2}.

Consequently sharp GN and interpolation yield

    integral_outsideR |u|^p <= C mu^{m/N}(K_R+H_R+R^{-2}),
    integral_outsideR |u||grad u|
       <=C mu^{1-1/m}(K_R+H_R+R^{-2})^{1/m}.          (15)

Take d_0 and then eta small enough that the coefficient C mu^{m/N}
is at most a fixed small fraction of 2m. Young's inequality absorbs
the K_R^{1/m} term and leaves

    J_R' <= -4m e + C H_R + C L mu^{1-1/m} H_R^{1/m}
              + C L^{m/(m-1)}mu + o_R(1).           (16)

All remainders tend to zero uniformly in time for the normalized H^s
ball. The constants depend only on a,N,m and fixed scalar sharp data.

### 4. Disjoint-annulus averaging and scaling

For fixed K and R_* take R_j=64^j R_*, 0<=j<K. Their H_R annuli
are disjoint, so sum_j H_Rj(t)<=A(t)<=1. For any time window [0,T]
choose j whose time-average is <=1/K. Integrating (16), using Jensen,
and bounding endpoints by C 64^{K-1}R_* gives

    4m e <= C64^{K-1}R_*/T + C/K
       + C L mu^{1-1/m} K^{-1/m}
       + C L^{m/(m-1)}mu + sup_{R>=R_*}|o_R(1)|.

Let T->infinity first, K->infinity second, R_*->infinity third,
eta->0 last. Thus

    e<=C L^{m/(m-1)}(M-M_c)
      <=C d^{1+m/[2(m-1)]}.

Under u_lambda(t,x)=lambda^{N/2}u(lambda^m t,lambda x), A and E
scale by lambda^m while d is invariant. Taking lambda=B^{-1/m}
undoes sup A=1 and proves (2). The maximal-flow version follows from
the continuation alternative exactly as in round 12.

## Why this does not yet exclude all bounded global negative-energy motion

The only nonvanishing error after averaging is

    L^{m/(m-1)}(M-M_c).

P=0 does not eliminate L: density transport for a general a involves
grad a(D), not D. The small imaginary component provides L=O(sqrt d),
but no known identity makes it vanish or ties it to e at a strength
that closes a contradiction for fixed d. Improving the commutator
cannot by itself resolve that remaining dynamical issue.

## Literature verification status

This note proves the extension directly from the scalar sharp-geometry
inputs already established in the project. A primary-source web search
for higher-order nonradial instability and homogeneous anisotropic
dispersion did not identify a matching quantitative law, but that is
not a priority proof. Inhomogeneous fourth-order nonradial blowup papers
use decay of the coefficient and cannot be cited as solving this
translation-invariant problem. Root literature review remains needed.

## Positive-type homogeneous Hartree extension

The proof extends to nonlocal attraction, with a stronger tail argument
than the earlier one-tail HLS estimate. Assume 2<m<N and

    i u_t=a(D)u-(K*|u|^2)u,
    H_K(u)=intint K(x-y)|u(x)|^2|u(y)|^2 dxdy,
    E=A/2-H_K/4.

Here K is real, even, C^1 away from zero, homogeneous of degree -m,
positive definite as a density quadratic form, and

    |K(x)|+|x||grad K(x)| <= C |x|^{-m}.

Assume the sharp scalar inequality H_K(u)<=2(M/M_c)A(u), with the
optimizer compactness/phase coercivity already proved in round 11.
For this interaction use d=M/M_c-1, rather than the local-power d.
Every strongly approximable conservative solution in the same class obeys

    e <= C d^{1+m/[2(m-1)]} sup A

when global bounded, P=0, E=-e<0, 0<d<d_0. The maximal-flow version
and amplification d^{-m/[2(m-1)]} follow under continuation; amplitude
data are now u_d(0)=sqrt(1+d)Q.

Proof modifications:

1. The real O(2) quantitative phase estimate and near-optimizer compactness
are already available for this positive density form. Its normalized
deficit is 1-H_K/[2(1+d)A]=(d-2e/A)/(1+d)<=d. Thus the slow-center and
uniform exterior-mass proofs apply verbatim. The energy splitting for
Hartree uses local compactness plus decay of the compact-core potential;
it is established explicitly in round11_systems_section.tex.

2. The symmetrized Hartree part of the virial is

    intint rho(x)rho(y)[f_R(x-a)-f_R(y-a)] dot grad K(x-y) dxdy.

Subtract its full-dilation value -m H_K. The defect vanishes when
both points lie in B(a,R), and its absolute integrand is bounded by

    C rho(x)rho(y)|x-y|^{-m}

when at least one point is outside B(a,R). By symmetry take x outside R.
If y is inside R/2, |x-y|>=R/2, so this pair contribution is at most
C R^{-m}M^2. In the complementary case both points lie outside R/2.
Choose zeta_R=1 outside R/2 and zero inside R/4. The remaining integral
is bounded by the absolute-Riesz Hartree form of zeta_Ru. HLS and
elliptic interpolation give

    H_|x|^{-m}(w) <= C ||w||_2^2 A(w).

Therefore the full Hartree virial defect obeys

    |Hartree defect| <= C R^{-m}M^2
       + C mu [K_R+H_R+R^{-2}].                     (H)

Taking d_0,eta small absorbs its K_R term. The current estimate,
Fourier commutator, annulus average, and final exponent are unchanged.

This avoids a nonabsorbable core-tail square-root term: the spatial
separation removes the true core-tail interaction, while the remaining
near-diagonal interaction sees only the small exterior mass.
