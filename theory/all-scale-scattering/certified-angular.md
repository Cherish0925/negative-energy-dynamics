# A completed enclosure of the full angular scattering sum

15 October 2026. This note records the executed computer-assisted part of the
all-scale theorem in [scattering-2cc19db4.md](scattering-2cc19db4.md). It proves the required inequality
for every real parameter in the open interval, including all angular modes.
The mathematical argument and source code are supplied together.

## 1. Exact statement and reduction

Let Q be the positive decaying radial solution of

    -Delta Q + Q - Q^3 = 0  on R^2,

and h=-Delta-Q^2. For 0<k<1 define

    A(k) = int Q^2 exp(2kx_1)
         + <Q^2 exp(kx_1),(h+k^2)^(-1)Q^2 exp(kx_1)>.

The inverse exists by the one-well result in R23. The analytic Darboux/Bessel
comparison, independently checked in [radial-scattering-verification.md](radial-scattering-verification.md),
gives a_0(k)<-1/log(1/k). The remaining channels obey

    0 <= a_m(k) <= b_m(k)/(1-theta_m),
    b_m(k)=int_0^infinity r Q(r)^2 I_m(kr)^2 dr,
    theta_m <= theta_1/m.

Here theta_m is the zero-energy Hilbert--Schmidt norm defined in
[scattering-2cc19db4.md](scattering-2cc19db4.md), and A/(2pi)=a_0+2 sum_(m>=1)a_m.

The computation below proves theta_1<0.55. Fix the EXACT rational theta=11/20
and put

    c0=1/(1-theta/2),
    c1=2/(1-theta)-2/(1-theta/2)>0,
    G(z)=c0[I_0(2z)-I_0(z)^2]+c1 I_1(z)^2,
    H(k)=int_0^infinity r Q(r)^2 G(kr) dr.

The Bessel addition identity bounds the entire omitted angular tail, giving
2 sum_(m>=1)a_m(k)<=H(k). All coefficients of G's even power series are
nonnegative, so G and H are increasing. The executed result is

    log(1/k) H(k) < 0.986,        every 0<k<1.

Consequently the completed theorem is

    A(k) < -2 pi * 0.014 / log(1/k) < 0,    every 0<k<1.       (1)

The constants 0.986 and 0.014 are deliberately rounded outward from the
strict interval bounds below. They are not sharp constants.

## 2. A certified profile and a global tail envelope

The separate ODE proof in [validated-profile.md](validated-profile.md) identifies Q by two
interval-enclosed shooting solutions, connectedness and the classical
uniqueness theorem for the positive decaying radial ground state. It proves

    2.20620086465074 < Q(0) < 2.20620086465075,

and encloses the whole family of solutions between these amplitudes to r=8
using outward interval Taylor arithmetic and validated Picard tubes.

The input files used in this computation are EXACTLY

- [r24_validated_shooting_tight.json](../../computations/all-scale-scattering/r24_validated_shooting_tight.json), with bracket_success=true and the
  lower shot positive over every complete integration step;
- [r24_validated_profile_tight.json](../../computations/all-scale-scattering/r24_validated_profile_tight.json), with 1619 propagation segments.

No ordinary BVP output enters the enclosure. On a mesh cell [a,b], monotonicity
of Q bounds it above by the enclosed upper endpoint value at a. The initial
cell [0,.01] uses the enclosed amplitude. Thus the angular calculation uses
1620 contiguous cells through r=8.

For R=8 and the enclosed upper value U of Q(R), set

    alpha=sqrt(1-U^2), c=3alpha+1,
    Cstar=(U/K_0(R)) exp{U^2/(2alpha)[1/c+1/(R c^2)]}.

The Wronskian/comparison proof in [scattering-2cc19db4.md](scattering-2cc19db4.md) establishes Q(r)<=Cstar
K_0(r) for ALL r>0. For the computation we bound K_0(R) below by

    exp(-R) sqrt(pi/(2R)) (1-1/(8R)).

This elementary bound follows, for example, from the positive Laplace
representation after the substitution t=cosh(s)-1 and
(1+x)^(-1/2)>=1-x/2. The same representation gives
K_0(r)<=exp(-r)sqrt(pi/(2r)). Interval evaluation yields Cstar<2.809834.
We use the larger rational value C=2.82, so

    Q(r)<=C K_0(r),
    r Q(r)^2 <= D exp(-2r),   D=C^2 pi/2.                    (2)

## 3. The angular operator bound, including its infinite radial tail

Write A(r)=int_0^r s^3 Q(s)^2 ds. Exactly,

    theta_1^2=(1/2) int_0^infinity Q(r)^2 A(r)/r dr.

Suppose q_a bounds Q on [a,b], and A_a bounds A(a). For a>0,

    A(r)<=A_a+q_a^2(r^4-a^4)/4,

so the cell's contribution is at most

    q_a^2/2 { A_a log(b/a)
       +q_a^2/4[(b^4-a^4)/4-a^4 log(b/a)] }.              (3)

The first cell contributes at most Q(0)^4 b^4/32. Update A_a by
q_a^2(b^4-a^4)/4 after each cell. For the tail use (2):

    A_infinity <= A(R)+D exp(-2R)(R^2/2+R/2+1/4),
    theta_1^2 tail <= D A_infinity exp(-2R)/(4R^2).

The executed outward upper bound is

    theta_1^2 <= 0.30242535317434427 < 0.3025 = (0.55)^2.

This establishes the operator bound used in Section 1; it is not a sampled
eigenvalue calculation or a truncation of angular momentum.

## 4. Positive-series integration and control of every k

For c_n=binom(2n,n)/4^n, positive-term integration gives

    int_0^infinity exp(-2r) I_0(2kr) dr = (1/2) sum c_n k^(2n),
    int_0^infinity exp(-2r) I_0(kr)^2 dr = (1/2) sum c_n^2 k^(2n),
    int_0^infinity exp(-2r) I_1(kr)^2 dr
       = (1/2) sum c_n^2 n/(n+1) k^(2n).

The n=0 term in the last expression is zero. Vandermonde's identity proves
the product coefficients, and nonnegative terms justify integration. Hence

    L(k):=int_0^infinity exp(-2r)G(kr)dr
       =sum_(n>=1) d_n k^(2n),
    d_n=(1/2)[c0(c_n-c_n^2)+c1 c_n^2 n/(n+1)]>=0.

Every d_n<=(c0+c1)/2. After 4000 terms the remaining positive tail is at most

    [(c0+c1)/2] k^8002/(1-k^2).

At radial cell [a,b], the core H contribution is bounded above by

    q_a^2 (b^2-a^2) G(kb)/2.

The exact same elementary envelope gives the remaining tail bound

    int_R^infinity r Q^2 G(kr) dr
       <=D { L(k)-sum_cells exp(-2b)G(ka)(b-a) }.          (4)

The sum subtracted in (4) is a LOWER Riemann bound on the integral of
exp(-2r)G(kr) over [0,R]. Therefore subtraction cannot omit a positive tail.
The explicit I_0 and I_1 series retain 72 terms; the ratio of successive
positive terms gives a geometric bound on all omitted terms. No asymptotic
Bessel expansion is used in the compact-interval calculation.

The exact rational k intervals partition [.02,.991] into 971 cells of length
.001. On each cell [a,b], monotonicity gives

    log(1/k) H(k) <= log(1/a) H(b).

Outward evaluation of the preceding bounds on ALL these cells gives

    log(1/k)H(k) <= 0.985343659554888 < 0.985344.

The largest enclosed value is on [.864,.865]. The proof uses monotonicity on
whole cells; no maximization routine or interpolation between samples is
assumed.

## 5. The two infinite parameter tails

For 0<k<=k0=.02, circle Poincare gives

    I_0(2z)-I_0(z)^2 <= (z^2/2) I_0(2z).

Since H<=B_sum/(1-theta), (2) and I_0(2z)<=exp(2z) imply

    log(1/k)H(k)
       <= C^2 pi k0^2 log(1/k0)/[16(1-theta)(1-k0)^3]
       < 0.005769.

For the other endpoint the positive integral representation of K_0 gives
the EXACT identity

    int_0^infinity r K_0(r)^2 I_0(2kr) dr
       = asin(k)/(2k sqrt(1-k^2)).

Drop the nonnegative subtractand in B_sum, use -log(k)<=(1-k)/k and
asin(k)<=pi/2, and then monotonicity of the resulting elementary majorant.
For k>=k1=.991 this yields

    log(1/k)H(k)
       <= C^2 pi sqrt(1-k1)/[4(1-theta) k1^2 sqrt(1+k1)]
       < 0.950198.

Together with Section 4, these bounds prove (1) throughout the open interval.

## 6. Arithmetic, independent checks and reproduction

The profile code uses mpmath.iv at 70 decimal digits; its proof is described
separately. The angular code uses mpmath.iv for exp, log, square roots and pi.
For the large arrays of positive series terms it uses IEEE-754 binary64
addition, subtraction, multiplication and division, with `numpy.nextafter`
enlarging EVERY result toward each endpoint. No ordinary floating sum or
quadrature estimate is treated as an enclosure. Correct IEEE-754 rounding
of these basic operations, and the stated interval-library operations, are
the arithmetic assumptions of this computer-assisted proof.

The JSON's transcendental display values are also enlarged upward by one
ulp. The logical comparisons use interval endpoints before display.

Run the two profile commands in [validated-profile.md](validated-profile.md), followed by

```bash
python3 research/r24_certified_angular.py --profile research/r24_validated_profile_tight.json --shooting research/r24_validated_shooting_tight.json --C 2.82 --output research/r24_certified_angular.json
```

Dependencies: Python 3, NumPy and mpmath. The proof does not require SciPy.
The completed output has `all_k_bound_closes: true`. Independent checks
covered the radial comparison, all cell and tail formulas, geometric
remainders, parameter coverage and outward arithmetic directions.

This proves the specified scattering coefficient inequality. It does not
prove the sharp Lieb--Thirring inequality for arbitrary potentials. The
classical Darboux transform, Bessel identities, Birman--Schwinger theory and
ground-state uniqueness are inputs; historical priority for their particular
combination here has not been established.
