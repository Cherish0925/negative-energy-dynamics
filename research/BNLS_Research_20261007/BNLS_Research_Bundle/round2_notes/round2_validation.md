# Rigorous Birman–Schwinger scalar certificates for the canonical profile

This note records an executed interval-arithmetic proof for the compact, exact rational approximate profile used in the four-dimensional cubic BNLS computation. It does not identify a floating-point collocation output with an exact stationary solution. The passage from the approximate profile to an exact solution, and the traveling-wave implicit-function argument, are separate certificates.

## Fixed input and reproducibility

The sole profile input is `round2_radial_H4_exact_h1_16.json`, SHA256

`c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627`.

Its rational nodes and hexadecimal binary64 jets specify a unique piecewise degree-seven Hermite polynomial q, matching q,q',q'',q''' at every knot. Each hexadecimal number is interpreted as an exact rational number, not as a numerical enclosure. The profile is C3, has q'(0)=q'''(0)=0, and vanishes identically for r>=36. Exact rational Bernstein coefficients yield

    ||q||_infinity <= 6.72169038577537580891885227174498140811920166015625.

The verifier is `round2_certified_birman_hs.py`; frozen SHA256 after adding all assertion/metadata requirements is

`96cc5d8633361c7cd23861af1e18a7c2500d7c2fa5fc967c87f2def8e61757f4`.

Run `python round2_certified_birman_hs.py ELL 16` separately for ELL=0,1,2,3,4, with Python 3.12.14 and python-flint 0.9.0 (other compatible versions can be independently checked). It uses 192-bit Arb/acb arithmetic and 9380 cells per channel. It asserts the input SHA and the channel's required inequality. It never regenerates the profile. Each JSON output records the source hashes, software versions, precision, quadrature subdivision count, and full upper-endpoint enclosure strings. All five inequalities below have been executed successfully. The final metadata-hardened verifier was independently rerun for all five channels from clean staging; every required inequality passed in the aggregate verification run.

## Free resolvent and exact kernel formula

On L2((0,infinity),r^3 dr), let

    H_ell = -d_r^2 - 3 r^(-1)d_r + ell(ell+2)r^(-2),
    R_ell = (H_ell^2+1)^(-1),
    B_(ell,beta) = beta q R_ell q.

These are the Friedrichs radial realizations of the free Laplacian/angular channels. The coefficient beta is 3 for real even channels ell=0,2,4 and 1 for imaginary odd channels ell=1,3. B is positive, compact, and trace class for this q, even though q may change sign.

Write nu=ell+1, kappa=exp(i*pi/4). The Green kernel of H_ell+i in the radial measure is

    (rs)^(-1) I_nu(kappa min(r,s)) K_nu(kappa max(r,s)).

Since (H^2+1)^(-1)=-Im(H+i)^(-1), the kernel of B after unitary conjugation from r^3dr to dr is

    B(r,s) = -beta sqrt(rs) q(r)q(s)
             Im[I_nu(kappa min(r,s)) K_nu(kappa max(r,s))].

Consequently

    tr B = -beta integral_0^36 r q(r)^2 Im[I_nu(kappa r)K_nu(kappa r)] dr.

For epsilon=1/100000 put a(r)=r q(r)^2. Denote the real and imaginary parts of the two Bessel functions by I_R,I_I,K_R,K_I. Define

    J1(s)=integral_epsilon^s a I_R^2,
    J2(s)=integral_epsilon^s a I_R I_I,
    J3(s)=integral_epsilon^s a I_I^2.

The Hilbert–Schmidt square on [epsilon,36]^2 is exactly

    2 beta^2 integral_epsilon^36 a(s)
       [K_I(s)^2 J1(s)+2 K_R(s)K_I(s)J2(s)+K_R(s)^2J3(s)] ds.

This formula avoids an expensive two-dimensional quadrature without dropping its cross term or factor two.

## Validated Bessel neighborhoods

Arb evaluates I_nu, K_nu and their derivatives at the exact midpoint of each rational cell. These special-function evaluations are rigorous complex balls, not ordinary floating-point calls. First derivatives follow from

    I'(r)=kappa I_(nu-1)(kappa r)-nu I_nu(kappa r)/r,
    K'(r)=-kappa K_(nu-1)(kappa r)-nu K_nu(kappa r)/r.

To enclose the functions on the whole cell [a,b], use the Bessel equation

    f'' + f'/r - (i+nu^2/r^2) f=0.

For Y=(f,r f'),

    Y' = [[0,1/r],[nu^2/r+i r,0]] Y.

With m=(a+b)/2, d=(b-a)/2, L=nu^2/a+b+1/a and M=|f(m)|+m|f'(m)|, Gronwall gives ||Y(r)||_infinity <= exp(Ld)M throughout the cell. Therefore

    |f(r)-f(m)| <= (d/a) exp(Ld) M,
    |r f'(r)-m f'(m)| <= d(nu^2/a+b) exp(Ld) M.

The code adds these absolute bounds to both real and imaginary components, divides the second state component by the positive interval [a,b], and obtains f'' from the differential equation. This deliberately conservative enclosure eliminates dependency inflation from evaluating K directly at a wide complex ball. It is valid for both I and K, and in both directions from the midpoint.

## Certified quadrature and cumulative integrals

Every cell lies within a single exact Hermite polynomial piece. Derivatives q,q',q'' are enclosed by polynomial interval evaluation. Product rules then give interval enclosures through second order for the cumulative-integral densities F_j and outer coefficients b_j:

    F=(a I_R^2, a I_R I_I, a I_I^2),
    b=(a K_I^2, 2 a K_R K_I, a K_R^2).

For a cell of width h and midpoint m, the full-cell midpoint rule has the rigorous error bound h^3 sup|f''|/24. For cumulative integrals at the midpoint, Taylor expansion about m gives

    integral_left^m f = (h/2) f(m) - (h^2/8) f'(m)
                       + [-h^3 sup|f''|/48, h^3 sup|f''|/48].

If J_left is the already certified cumulative integral at the cell's left endpoint, a whole-cell enclosure is J_left+[0,h]F(cell). For the outer integrand G=sum_j b_j J_j,

    G''=sum_j [b_j'' J_j+2 b_j' F_j+b_j F_j'].

This yields a rigorous midpoint error for the Hilbert–Schmidt integral while preserving accumulated uncertainty. The trace integrand is treated with the same second-derivative midpoint bound. All arithmetic is outward-rounded Arb arithmetic, including exponentials and special functions; exact Fraction arithmetic is used to construct the profile and its simple moments.

The origin mesh begins at epsilon and grows by at most the factor 21/20, with a maximum physical cell width 1/256. All later cells have width at most 1/256. The four-unit polynomial tail is subdivided as well. The exact subdivision choices affect efficiency only: each individual cell carries its own proved remainder bound.

## Origin and tail bounds

The excluded region touching zero is handled analytically, without a Bessel evaluation at the singular endpoint. For positive H,

    (H^2+1)^(-1) <= (2H)^(-1).

The Green kernel of H_ell^(-1), in the radial measure, has diagonal 1/(2 nu r^2). It follows that

    tr(1_[0,epsilon] B 1_[0,epsilon])
        <= beta ||q||_infinity^2 epsilon^2/(8 nu) = T0,

and

    tr B <= beta/(4 nu) integral_0^36 r q(r)^2 dr = Tcoarse.

The latter integral and the supremum bound are computed exactly using rational polynomials. Positivity implies |B(r,s)|^2<=B(r,r)B(s,s). Hence the Hilbert–Schmidt contribution of the union of the two omitted strips is at most 2 T0 Tcoarse. This is added as the interval [0,2 T0 Tcoarse]. The trace origin contribution is added as [0,T0]. Nothing is omitted beyond r=36 because q is exactly zero there.

For ell=0 these origin errors are respectively <1.695e-9 and <8.705e-8. They are included in the reported final endpoints.

## Executed results and spectral consequences

The required output files are `round2_certified_birman_l0_sub16.json` through `round2_certified_birman_l4_sub16.json`. The asserted results are:

| ell | beta | Certified scalar bound |
|---:|---:|:---|
| 0 | 3 | ||B||_HS^2 < 38.80 |
| 1 | 1 | tr B < 1.70 |
| 2 | 3 | ||B||_HS^2 < 4.80 |
| 3 | 1 | ||B||_HS^2 < 0.22 |
| 4 | 3 | ||B||_HS^2 < 0.73 |

The ell=0 upper endpoint is enclosed by

    38.7956907754366969439250339728973902162169912315927291824
      +/- 3.30e-56.

A short decimal display of a ball may look less sharp than the internal interval. The explicit Arb comparisons, the required-pass assertions, and the separately exported full endpoint enclosures determine the certified inequalities.

Combining these bounds with the separate exact rational Rayleigh–Ritz certificates in `round2_ritz_exact_results.json` gives the following. Here mu_j are decreasing eigenvalues of B:

* ell=0,beta=3: mu1>=5.395, mu2>=2.999, and mu3^2<38.80-5.395^2-2.999^2=0.699974; thus the preconditioned distance from 1 exceeds 0.16.
* ell=2,beta=3: mu1>=2.11, and mu2^2<4.80-2.11^2=0.3479; thus the distance exceeds 0.4.
* ell=4,beta=3: mu1^2<0.73; thus the distance exceeds 0.14.
* ell=1,beta=1: mu1>=1.04 and mu2<1.70-1.04=0.66; thus the distance is at least 0.04.
* ell=3,beta=1: mu1^2<0.22; thus the distance exceeds 0.53.

The statements about distance from 1 use the nonnegative spectrum of B. The nonzero spectrum agrees with that of the symmetrically preconditioned potential (H_ell^2+1)^(-1/2) beta q^2 (H_ell^2+1)^(-1/2). The complementary high angular channels are covered by the separate exact polynomial quadratic-form certificate `round2_radial_highangular_certificate.json`, with gap at least 0.1. These are spectral bounds for the explicitly specified approximate q; the exact-profile perturbation must still be applied in the full existence proof.

No asymptotic mesh-convergence extrapolation, unproved numerical eigenvalue count, or non-rigorous floating-point Bessel value is used in these scalar certificates.
