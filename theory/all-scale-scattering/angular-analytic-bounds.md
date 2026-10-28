# Analytic angular bounds and the information missing from Pohozaev

Date: 2026-10-15. Companion to r24_scattering.md. This note does not prove the
complete scattering sign. It records exact analytic estimates and why the
mass and unweighted Pohozaev identities do not close the exponential weights.

## 1. A monotonic-potential Hilbert--Schmidt estimate

Let V be nonnegative radial decreasing on R2, with
A=int_0^infinity r V(r) dr. For angular momentum m>=1, the zero-energy
Birman--Schwinger kernel is

    sqrt(V(r)V(s))/(2m) * (min(r,s)/max(r,s))^m.

Its trace is A/(2m). Then

    ||B_m(0)||_HS <= A/[2m sqrt(m+1)].             (1)

Proof. The probability measure r V(r) dr/A is a mixture of uniform radial
disk measures 2r/R^2 1_(r<R) dr. For a differentiable V, the mixing measure
is -R^2 V'(R)dR/(2A); general decreasing V follows by Stieltjes integration.
For two such disk radii R<=S, put t=R/S. Direct integration gives

    E[(min(r,s)/max(r,s))^(2m)]
      =t^2(log(1/t)+1/2),                         m=1,
      =(m t^2-t^(2m))/(m^2-1),                    m>1.

Both expressions increase on 0<t<=1 and equal 1/(m+1) at t=1. Average over
the mixing radii, and multiply by the squared trace, to obtain (1).

For V=Q^2, A=M/(2pi), so theta_m<=M/[4pi m sqrt(m+1)]. This uses monotonicity
in addition to the trace estimate, and requires no numerical profile.

A floating-point test against the actual Townes Born integrals gave
log(1/k)H approximately 1.194 at k=.85 when this bound is used for all
denominators. Therefore this estimate, even using the actual mass rather than
only M<4pi, does not numerically close the sufficient bound of
r24_scattering.md. No rigorous lower enclosure for that numerical value is
asserted; it is not a proof that the complete scattering coefficient is
positive, and it is not used as such.

## 2. What weighted Pohozaev actually says about the moments

Set

    A_n=int_0^infinity r^(2n+1)Q^2,
    B_n=int_0^infinity r^(2n+1)Q'^2,
    C_n=int_0^infinity r^(2n+1)Q^4.

Multiplying the Townes equation by r^(2n+1)Q and by r^(2n+2)Q', respectively,
and integrating gives

    B_n+A_n-C_n=2n^2 A_(n-1),
    n B_n-(n+1)A_n+(n+1)C_n/2=0.

Hence, for n>=1,

    2(2n+1)A_n=(3n+1)C_n+4n^3 A_(n-1).          (2)

All boundary terms vanish by regularity at zero and exponential decay. For
n=0 the identities give B_0=A_0 and C_0=2A_0.

The Bessel-square power series in the positive angular Born terms has
nonnegative coefficients. To bound it from above using moments, one needs
upper bounds on A_n. Equation (2) with C_n>=0 gives a LOWER bound on A_n.
Thus positivity of the nonlinear term goes in the wrong direction for that
proposed use of Pohozaev. An upper bound such as C_n<=K A_(n-1) would need
additional pointwise information r^2 Q(r)^2<=K.

## 3. A precise insufficiency of unweighted integral data

Radial monotonicity, M<4pi, and the two identities T=M, F=2M do not bound
any positive exponential moment uniformly. Here T=int|grad g|^2, M=int g^2,
F=int g^4.

Choose a smooth decreasing cutoff chi, equal to one on [0,1] and zero on
[2,infinity), and first form the radial decreasing H1 function

    f_R(r)=max(Q(r),R^(-2)chi(r/R)).

One may smooth the maximum and the radial joins while preserving monotonicity,
the estimates below, and a plateau comparable to R^(-2) on [R/2,R]. The tail
added in L2 has squared norm O(R^(-2)); its derivative and L4 contributions
also vanish. Thus f_R converges to Q in H1 and L4.

Write M0=||f_R||_2^2, T0=||grad f_R||_2^2, F0=||f_R||_4^4, and set

    a_R^2=2M0/F0,      b_R^2=M0/T0,
    g_R(x)=a_R f_R(b_R x).

Then T(g_R)=M(g_R), F(g_R)=2M(g_R) exactly, while

    M(g_R)=2M0 T0/F0 -> M_c<4pi,
    a_R,b_R ->1.

For every fixed k>0, the plateau on a growing annulus gives

    int exp(2k x_1)g_R(x)^2 dx -> infinity.

For example restrict to a fixed angular sector about the positive x1 axis
and radii comparable to R/b_R: its polynomially small mass is multiplied by
an exponential in R. Consequently the same divergence occurs in the relevant
Bessel exponential moments. These g_R are NOT solutions of the Townes ODE.
The example proves only that the listed integral and monotonicity facts do
not provide the desired upper bounds; quantitative ODE information must enter.

## 4. A conditional explicit potential comparison

The positive function

    z_m(r)=r^m/(R^2+r^2)^m

satisfies

    [-partial_r^2-r^(-1)partial_r+m^2/r^2]z_m
      =[4m(m+1)R^2/(R^2+r^2)^2]z_m.

Its ground-state transform gives the corresponding quadratic-form inequality.
Thus a pointwise bound

    Q(r)^2 <= 8 theta R^2/(R^2+r^2)^2

would imply, simultaneously for all m>=1,

    ||B_m(0)|| <= 2 theta/[m(m+1)].                (3)

Numerical optimization of this envelope suggests R approximately .894 and
theta approximately .570186. Used with the actual Born integrals, (3) gives
log(1/k)H approximately .968 at k=.85. Neither the envelope nor the uniform
Born integrals have been bounded analytically here, so (3) is a conditional
alternative, not a completed sign proof. Its m^(-2) decay explains why it can
outperform a smaller first-mode Hilbert--Schmidt constant coupled with weaker
higher-mode estimates.
