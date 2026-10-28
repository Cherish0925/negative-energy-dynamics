# Analytic excerpt from R24 scattering notes

This archive retains only analytic sections 1–2 of the R24 working note. The complete radial argument is independently derived in [radial-scattering-verification.md](radial-scattering-verification.md). The computational proof used in R25 is supplied in [uniform-bound.md](uniform-bound.md) and the accompanying R25 scripts; no alternate R24 computation is required.

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

