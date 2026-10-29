# a radial scattering comparison at every scale

15 October 2026. This note proves a strict all-scale bound for the radial
scattering channel and combines it with a completed computer-assisted bound
for the complete angular sum. The calculation uses an outward interval
enclosure of the Townes profile, positive series with explicit remainders,
monotone Riemann sums, and analytic control of both endpoints. Its conclusion
is A(k)<0 for every 0<k<1; a conservative quantitative bound appears below.
The result concerns the specified two-well interaction, not the unrestricted
two-dimensional Lieb--Thirring inequality. Historical priority is unestablished.

Let Q>0 be the positive radial decaying solution of

    -Q''-Q'/r+Q-Q^3=0,

and let h=-Delta-Q^2. The R23 factorization proves that h has exactly the
negative eigenvalue -1 and no zero resonance. For 0<k<1 set

    A(k)=int Q^2 exp(2kx_1)
       +<Q^2 exp(kx_1),(h+k^2)^(-1)Q^2 exp(kx_1)>.

Write the regular radial scattering solutions as

    w_m(r)=I_m(kr)+a_m(k)K_m(kr)+o(K_m(kr)).

Then A(k)=2pi[a_0(k)+2 sum_(m>=1) a_m(k)].

**Computer-assisted theorem.** With these normalizations,

    A(k)<-2pi*0.014/log(1/k)<0,            0<k<1.        (T)

The analytic reductions are in sections 1--2 and 5--6. Section 7 gives the
finite interval computation that completes the proof. It assumes the usual
correct outward rounding of mpmath.iv and IEEE-754 operations enlarged by
nextafter as specified in the supplied programs; no floating-point
approximation of Q is treated as an exact profile.

## 1. A comparison valid for every 0<k<1

The new analytic conclusion in this note is

    a_0(k) < -1/log(1/k),                    0<k<1.       (1)

It is a statement about the radial channel, not yet the sum of all channels.

Put B(r)=K_0(r), q=Q'/Q, b=B'/B and D_Q=partial_r-q,
D_B=partial_r-b. Their positive partner potentials are

    U_Q=1/r^2-Q^2-2q'
       =(r Q(r)^2)^(-1) int_r^infinity [Q(s)^2/s^2+Q(s)^4] ds,

    U_B=1/r^2-2b'
       =(r B(r)^2)^(-1) int_r^infinity B(s)^2/s^2 ds.     (2)

The B formula follows by the same differentiation as the Q formula, using
B''+B'/r=B. Both partner potentials are strictly positive.

The Wronskian identity

    r[Q'B-QB']=int_r^infinity s Q(s)^3 B(s) ds>0         (3)

shows that Q/B is strictly increasing. Thus for s>r,
Q(s)/Q(r)>B(s)/B(r). Comparing the integrands in (2) gives

    W(r):=U_Q(r)-U_B(r)>0.                              (4)

Define a_B(k)=1/log k and

    w_B=I_0(kr)+a_B(k)K_0(kr),
    v_B=D_B w_B,
    v_Q=D_Q w_0.

The intertwining identities give

    [-partial_r^2-r^(-1)partial_r+U_B+k^2]v_B=0,
    [-partial_r^2-r^(-1)partial_r+U_Q+k^2]v_Q=0.         (5)

These are the regular/Friedrichs partner solutions. At the origin, write
L(r)=log(2/r)-EulerGamma. Since B=L+O(r^2 L), the choice
a_B=1/log k cancels the constant term in w_B-a_B B. Direct expansion gives

    v_B=-(1-k^2)a_B r L/2+O(r),

whose leading coefficient is positive. The other solution has v_Q=c r+O(r^3).
Its coefficient c is positive: a negative coefficient would make v_Q negative
and decreasing everywhere, by (r v_Q')'=r(U_Q+k^2)v_Q, contradicting its positive
growing normalization at infinity. Hence v_B,v_Q>0 on (0,infinity).

The origin boundary Wronskian vanishes:

    lim_(r->0) r[v_B v_Q'-v_B'v_Q]=0.                  (6)

At infinity Q/B tends to a positive constant, and (3) gives
q-b=O(exp(-2r)/r). Thus the same transformed free basis can be used for both
partner solutions:

    v_B=D_B I_0(kr)+a_B D_B K_0(kr),
    v_Q=D_B I_0(kr)+a_0 D_B K_0(kr)+o(K_0(kr)).        (7)

The remainders and their derivatives have sufficient decay for the Wronskian
limit because k<1. The transformed Wronskian is exact:

    r W(D_B I_0(kr),D_B K_0(kr))=-(1-k^2).             (8)

For example, this follows from the intertwining equations, since both sides
are constant in r, and the large-r leading factors are 1+k and 1-k.

Subtracting the two equations in (5) gives

    [r(v_B v_Q'-v_B'v_Q)]'=r W v_B v_Q.

Integrating and using (6)--(8) proves the exact identity

    -(1-k^2)[a_0(k)-a_B(k)]
      =int_0^infinity r W(r)v_B(r)v_Q(r) dr >0.        (9)

The integral is finite: near zero its integrand is O(r), up to logarithmic
factors; at infinity W decays exponentially with rate 2 whereas the product
of growing solutions has rate 2k. Equation (1) follows.

No value of Q(0), mass approximation, or numerical scattering coefficient is
used in this proof. The comparison reference is the Bessel seed K_0, whose
partner is regular in its Friedrichs domain even though the seed itself is
logarithmically singular at zero.

## 2. A finite sufficient inequality for the full angular sum

For m>=1 let B_m(k) be the positive radial Birman--Schwinger operator with
kernel

    Q(r) I_m(k min(r,s)) K_m(k max(r,s)) Q(s)

on L^2((0,infinity),r dr). Define the exact zero-energy Hilbert--Schmidt norm

    theta_m^2=||B_m(0)||_HS^2
      =1/(2m^2) int_0^infinity r^(1-2m) Q(r)^2
           [int_0^r s^(2m+1)Q(s)^2 ds] dr.             (10)

The kernel comparison with the zero-energy Green function gives

    ||B_m(k)|| <= theta_m,
    theta_m <= theta_1/m,
    theta_1 <= Tr B_1(0)=M/(4pi)<1.                   (11)

The second inequality uses (min/max)^m<=(min/max) before taking the
Hilbert--Schmidt norm; the first is valid also as a pointwise kernel bound.

Put

    b_m(k)=int_0^infinity r Q(r)^2 I_m(kr)^2 dr,
    B_sum(k)=int_0^infinity r Q(r)^2
                         [I_0(2kr)-I_0(kr)^2] dr
            =2 sum_(m>=1)b_m(k).

The positive-channel resolvent representation then yields

    0<=a_m(k)<=b_m(k)/(1-theta_m).                     (12)

For any fixed integer L>=1, define the completely explicit profile integral

    H_L(k)=2 sum_(m=1)^L b_m(k)/(1-theta_m)
      +[B_sum(k)-2 sum_(m=1)^L b_m(k)]
                       /[1-theta_1/(L+1)].            (13)

The bracketed remainder is nonnegative, and (11) bounds every omitted angular
mode. There is no uncontrolled angular truncation in (13). Equations (1) and
(12)--(13) give the rigorous implication

    log(1/k) H_L(k) <1  ==>  A(k)<0.                  (14)

The exact k-dependent Hilbert--Schmidt norm can replace theta_m in every
retained denominator and only improves the bound:

    theta_m(k)^2 = int int r s Q(r)^2 Q(s)^2
         I_m(k min(r,s))^2 K_m(k max(r,s))^2 dr ds.

Using theta_m(0) is convenient because (13) then involves only a few positive
one-dimensional profile integrals and fixed constants.

## 3. Endpoints and the remaining quantitative task

The sufficient function R_L(k)=log(1/k)H_L(k) tends to zero at BOTH endpoints.
Near zero the Bessel series gives H_L(k)=O(k^2), hence R_L=O(k^2 log(1/k)).
An explicit small-k bound is

    B_sum(k) <= (k^2/2) int r^3 Q(r)^2 I_0(2kr) dr.    (15)

One proof uses circle Poincare on exp(kr cos theta):
I_0(2z)-I_0(z)^2 <= z I_1(2z)/2 <= z^2 I_0(2z)/2.
For k<=k_0 the integral in (15) can be evaluated/bounded once at k_0.

Near one, Q(r)=O(r^(-1/2)exp(-r)) and the Bessel asymptotics give
B_sum(k)=O((1-k)^(-1/2)). Since all denominators in (13) are positive constants,

    R_L(k)=O(sqrt(1-k)) ->0.                          (16)

Thus the inequality in (14) on one explicit compact interval, together with
quantitative versions of (15)--(16), suffices for every 0<k<1. Section 7
records the completed interval calculation. The following earlier
floating-point exploration motivated that calculation; it is not used as
the proof.

The script r24_scattering_bounds.py solves for Q and evaluates (10),(13)
using floating point. It does not solve the scattering equation, and the
omitted angular sum is bounded analytically. The approximate constants are

    theta_1=0.547153604,
    theta_2=0.206363965,
    theta_3=0.114240894,
    theta_4=0.074693838.

Scalar optimization of R_L gave the following candidates, not certified global
maxima:

| L | candidate maximizing k | candidate maximum R_L |
|---|---:|---:|
| 1 | 0.861535078 | 0.950104018 |
| 2 | 0.856048147 | 0.933417122 |
| 4 | 0.853748173 | 0.929714450 |
| 8 | 0.853506559 | 0.929513138 |

The exploratory L=4 bound had a numerical margin about 0.070 below one.
The proof in section 7 instead uses L=1, an explicit theta=0.55, and outward
enclosures for the entire parameter interval. It does not substitute these
exploratory maxima for a uniform bound.

## 4. Why resolvent monotonicity alone does not give the answer

The incoming function f_k=exp(kx_1) also changes with k. Therefore the
coefficient A(k) is not simply a Stieltjes transform of a fixed spectral
measure. An exact dilation identity is

    k A'(k)=-int [2Q^2+x dot grad(Q^2)] w_k^2
           =-2 int Q Lambda Q w_k^2,
    w_k=f_k+(h+k^2)^(-1)(Q^2 f_k).                     (17)

Indeed the potential derivative of A is int w_k^2 delta V, and in two
dimensions A_(lambda^2 V(lambda x))(k)=A_V(k/lambda). Differentiating gives
(17). Since Q Lambda Q changes sign, (17) supplies no monotonicity without
another estimate. The Bessel-partner comparison above avoids this difficulty
for the radial channel.

The present theorem and candidate closure concern the fixed unequal-well
interaction coefficient. They do not prove the arbitrary-potential or
arbitrary-rank two-dimensional Lieb--Thirring inequality. Historical novelty
of this particular Darboux/Bessel comparison has not been established.

## 5. Explicit profile tail and endpoint bounds

Suppose an enclosure supplies Q(R)<=U<1. Define

    a=sqrt(1-U^2),  c=3a+1,
    E=U^2/(2a) [1/c+1/(R c^2)],
    C=[U/K_0(R)] exp(E).                              (18)

Then the following envelope holds on the WHOLE positive axis:

    Q(r)<=C K_0(r),                   r>0.             (19)

Proof: for s>=r>=R, monotonicity Q(s)<=U and comparison for -Delta+a^2 give
Q(s)<=Q(r)exp[-a(s-r)]. The exponential is a supersolution because
(-Delta_rad+a^2)exp[-a(s-r)]=(a/s)exp[-a(s-r)]>0. Also
K_0(s)/K_0(r)<=exp[-(s-r)], since K_1/K_0>1 by their positive integral
representations. Equation (3) therefore implies

    delta(r):=Q'(r)/Q(r)-K_0'(r)/K_0(r)
       <=Q(r)^2 [1/c+1/(r c^2)].

Integrate from R to infinity, using Q(r)<=Uexp[-a(r-R)], to obtain
log(lim(Q/K_0)/(Q(R)/K_0(R)))<=E. Finally Q/K_0 is increasing everywhere, so
the bound for its limiting value is a global envelope, not merely a tail
bound. In particular no derivative enclosure at R is needed.

For an elementary implementation one may use

    exp(-r)sqrt(pi/(2r))[1-1/(8r)] <= K_0(r)
          <= exp(-r)sqrt(pi/(2r)),                     (20)

where the lower bound is useful for r>1/8. Both follow from the integral
representation with factor (1+t/(2r))^(-1/2), bounded above by 1 and below by
1-t/(4r). A directly enclosed K_0(R) gives a tighter value of C in (18).

Let theta_1<=theta<1 be any established bound. Since H_L<=B_sum/(1-theta),
equations (15), (19)--(20), and I_0(z)<=exp(z) imply, for
0<k<=k_0<exp(-1/2),

    R_L(k)<= C^2 pi k_0^2 log(1/k_0)
                    /[16(1-theta)(1-k_0)^3].           (21)

Indeed int_0^infinity r^3 Q^2 I_0(2k_0r)dr is at most
C^2 pi/[8(1-k_0)^3], and k^2 log(1/k) increases on that interval.

For the other endpoint, the elementary circle representation gives

    I_0(z)<=exp(z)sqrt(pi)/(2sqrt(2z)),    z>0.         (22)

Here cos(t)<=1-2t^2/pi^2 for 0<=t<=pi; extend the resulting Gaussian integral
to infinity. Equations (19)--(20), (22), and -log k<=(1-k)/k give, for
k_1<=k<1,

    R_L(k)<= C^2 pi^2 sqrt(1-k_1)
                    /[8sqrt(2)(1-theta)k_1^(3/2)].    (23)

For example, certified values C<=4 and theta<=0.56 would make (21) less than
0.012 at k_0=0.02 and (23) less than 0.318 at k_1=0.9999. Section 7 establishes
the stronger values C<2.82 and theta_1<0.55 and uses the sharper endpoint
estimate (25). Equations (18)--(23) themselves are analytic inequalities.

A sharper endpoint uses the exact integral

    int_0^infinity r K_0(r)^2 I_0(2kr)dr
         =asin(k)/[2k sqrt(1-k^2)].                    (24)

To derive it, insert K_0(r)=(1/2)int_0^infinity t^(-1)
exp[-t-r^2/(4t)]dt twice. The r integral is Gaussian:
int r exp(-A r^2)I_0(2kr)dr=exp(k^2/A)/(2A). The substitution
T=t+u, x=t/T then gives (1/2)int_0^1[1-4k^2x(1-x)]^(-1)dx, which evaluates
to (24). Every integral has nonnegative integrand, so Tonelli applies.

Consequently, for k>=k_1,

    R_L(k)<=C^2/(1-theta) log(1/k) asin(k)
                                /[2k sqrt(1-k^2)]
       <=C^2 pi sqrt(1-k_1)
                  /[4(1-theta)k_1^2 sqrt(1+k_1)].       (25)

For example C<=2.82, theta<=0.56, k_1=0.991 makes the last expression less
than 0.973. This is conditional only on the displayed C,theta enclosures.

## 6. Exact positive series for an elementary envelope integral

These identities are useful for rigorously bounding the tail under
r Q(r)^2<=D exp(-2r), D=C^2 pi/2. Put
c_n=binom(2n,n)/4^n. Then, for 0<k<1,

    int exp(-2r) I_0(2kr)dr =1/[2sqrt(1-k^2)]
       =(1/2)sum_(n>=0)c_n k^(2n),

    int exp(-2r) I_0(kr)^2 dr
       =(1/2)sum_(n>=0)c_n^2 k^(2n),

    int exp(-2r) I_1(kr)^2 dr
       =(1/2)sum_(n>=1)c_n^2 [n/(n+1)] k^(2n).         (26)

All r integrals are over (0,infinity). The square series follow from
Vandermonde's identity:

    I_0(z)^2=sum_(n>=0) [(2n)!/(n!^4)](z/2)^(2n),
    I_1(z)^2=sum_(n>=1)
       [(2n)!/(n!^2(n-1)!(n+1)!)](z/2)^(2n).

Integrating each nonnegative term against exp(-2r), using
int r^(2n)exp(-2r)dr=(2n)!/2^(2n+1), gives (26). In particular, for the
L=1 bound with theta_1<=theta, define

    c0=1/(1-theta/2),
    c1=2/(1-theta)-2/(1-theta/2).

The kernel in H_1 is

    F(k,r)=c0[I_0(2kr)-I_0(kr)^2]+c1 I_1(kr)^2,

whose full exponential integral is the positive series

    int exp(-2r)F(k,r)dr
      =(1/2)sum_(n>=1)
        [c0(c_n-c_n^2)+c1 c_n^2 n/(n+1)] k^(2n).      (27)

This avoids subtracting uncertified large infinite tails. For example a
lower integral enclosure on [0,R] can be subtracted from an upper enclosure
of (27) to give a tail upper bound; both quantities concern the elementary
envelope, so the same subtraction must not be made with the actual Q profile.

## 7. Completed outward interval computation

The validated radial initial-value computation establishes

    2.20620086465074 <= Q(0) <= 2.20620086465075.

The lower endpoint shot turns while remaining positive; the upper endpoint
shot crosses zero. The radial shooting characterization and uniqueness of
the positive decaying Townes solution locate its initial value between these
shots. The same interval Taylor integrator propagates this complete initial
interval to r=8, retaining outward whole-step and nodal enclosures. The
initial power series has an explicit analytic remainder; every subsequent
step uses a strict Picard tube and an interval Taylor remainder of order 19.

The terminal profile upper bound is

    Q(8)<=0.0004111499184074464541714897575666726548.

Equations (18),(20) give C<2.82. The monotone radial integral bound for (10),
including the infinite tail, gives

    theta_1^2<=0.302425353175 < 0.55^2.

Use theta=0.55 in the L=1 angular bound, and C=2.82 in the exponential tail
envelope. The interval [0.02,0.991] is partitioned into 971 cells of width at
most 0.001. Since H_1 is increasing, a cell [a,b] satisfies

    log(1/k)H_1(k)<=log(1/a)H_1(b).

The bound for H_1(b) uses upper radial Riemann sums on the validated profile
mesh; its infinite tail uses (27) minus a lower Riemann sum for the SAME
elementary envelope. Each Bessel series is enclosed with an explicit
geometric remainder. The resulting conservative bounds are

| Parameter interval | Upper bound for log(1/k)H_1(k) |
|---|---:|
| 0<k<=0.02, by (21) | 0.005769 |
| 0.02<=k<=0.991, by the interval computation | 0.985344 |
| 0.991<=k<1, by (25) | 0.950198 |

All are below 0.986. Combining with the strict radial inequality (1) proves
(T). The strictness comes from the positive integral (9); rounding 0.985344
up to 0.986 leaves the stated simple constant 0.014.

The stored results are:

* [r24_validated_shooting_tight.json](../../computations/all-scale-scattering/r24_validated_shooting_tight.json): the two outward endpoint shots;
* [r24_validated_profile_tight.json](../../computations/all-scale-scattering/r24_validated_profile_tight.json): the outward profile enclosure;
* [r24_certified_angular.json](../../computations/all-scale-scattering/r24_certified_angular.json): every parameter cell and all endpoint bounds.

The following commands reproduce the calculation from the project root:

```sh
cd computations/all-scale-scattering  # from the repository root
python3 r24_validated_profile.py --mode shoot \
  --a-low 2.20620086465074 --a-high 2.20620086465075 \
  --step 0.02 --order 18 --dps 70 \
  --output r24_validated_shooting_tight.json
python3 r24_validated_profile.py --mode profile \
  --a-low 2.20620086465074 --a-high 2.20620086465075 \
  --stop 8 --step 0.005 --order 18 --dps 70 \
  --output r24_validated_profile_tight.json
python3 r24_certified_angular.py \
  --profile r24_validated_profile_tight.json \
  --shooting r24_validated_shooting_tight.json \
  --C 2.82 --theta 0.55 --k-start 0.02 --k-end 0.991 --k-step 0.001 \
  --output r24_certified_angular.json
```

The consequence for the separated unequal Townes wells is now unconditional
with respect to the fixed scale ratio: for each fixed 0<k<1, their previously
derived two-level interaction is strictly negative at all sufficiently large
separations. The separation threshold and the asymptotic remainder may depend
on k. This statement does not control arbitrary finite separation, arbitrary
potentials, arbitrary rank, or the nonradial BNLS blow-up problem.
