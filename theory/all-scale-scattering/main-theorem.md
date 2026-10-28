# Distant Townes wells at the two-dimensional Lieb–Thirring endpoint

15 October 2026. The result below combines an analytic scattering comparison,
a reproducible interval computation, and an exact negative-spectrum count.
Its scope is the stated two-well family. Historical priority has not been
established. The arbitrary-potential sharp Lieb–Thirring problem remains open
in this work.

## Statement

Let Q be the positive radial solution of

    -Delta Q + Q - Q^3 = 0 on R^2,
    M = integral Q^2,
    h = -Delta-Q^2.

For every 0<k<1 define

    A(k)=integral Q^2 exp(2kx_1)
         +<Q^2 exp(kx_1),(h+k^2)^(-1)Q^2 exp(kx_1)>.

The inverse exists: h has exactly one negative eigenvalue, -1, and zero is
regular in the bounded-solution sense. The proof of this fact is included
in r23_partner_audit.md.

**Computer-assisted conclusion.** The complete scattering coefficient obeys

    A(k) < -2 pi/[25 log(1/k)] < 0, for every 0<k<1.       (1)

All angular modes are included. The coefficient 1/25 is a rounded-down
analytic margin, rather than the last digits of a floating-point maximum.

For fixed k, put

    V_(k,R)(x)=Q(x)^2+k^2 Q(k(x-R e_1))^2.

There is R_0(k)<infinity such that, for all R>R_0(k),

    Tr(-Delta-V_(k,R))_- < (1/(2M)) integral V_(k,R)^2.   (2)

The trace denotes the sum of the absolute values of ALL negative eigenvalues.
For large R there are exactly two, and no bounded zero-energy solution.
No extra shallow eigenvalues have been discarded. R_0 is not asserted
uniform in k. In particular this does not cover k=k(R) tending to zero or
one without further estimates, nor comparable separations or arbitrary
self-consistent multimode potentials.

## Analytic reduction of (1)

The angular expansion gives

    A(k)=2 pi [a_0(k)+2 sum_(m>=1) a_m(k)].

The Darboux comparison with the K_0 seed proves, for all 0<k<1,

    a_0(k)<-1/log(1/k).

The full proof, including both origin conditions and the transformed
Wronskian, is supplied in r24_scattering.md and independently checked in
r24_radial_scattering_verification.md. This is an analytic statement;
the interval calculation is used for the positive angular contribution.

For m>=1 let theta_m be the zero-energy Hilbert–Schmidt norm

    theta_m^2 = 1/(2m^2) integral r^(1-2m) Q(r)^2
                         [integral_0^r s^(2m+1)Q(s)^2 ds] dr.

Let b_m(k)=integral rQ^2 I_m(kr)^2 dr, and

    B(k)=integral rQ^2 [I_0(2kr)-I_0(kr)^2] dr.

Birman–Schwinger bounds give a_m<=b_m/(1-theta_m), and
theta_m<=theta_1/m. The uncomputed angular modes are therefore controlled by

    2 sum_(m>=1) a_m(k) <= H_4(k),
    H_4=2 sum_(m=1)^4 b_m/(1-theta_m)
         +[B-2 sum_(m=1)^4 b_m]/[1-theta_1/5].

Using upper bounds for the theta values gives a larger valid H_4. Its
power-series coefficients are positive, so interval endpoint values bound
the whole parameter interval, not merely the sampled points.

The interval certificate proves

    log(1/k) H_4(k) < 24/25, for every 0<k<1.

Combining this with the radial comparison yields (1).

## Numerical part and all omitted terms

The shooting calculation encloses the actual Townes initial value between
2.2062008646507 and 2.2062008646508. It uses an analytic origin series with
a Cauchy remainder, Picard tube inclusion, and interval Taylor integration.
Binary interval endpoints are saved exactly, not reconstructed from printed
decimals. The finite-interval enclosure and monotonicity of Q give 810
radial panels through r=8. A separate analytic comparison proves

    Q(r) <= 2.82 K_0(r), for every r>0.

The certified Hilbert–Schmidt upper bounds are smaller than

    theta_1<0.552722, theta_2<0.208490,
    theta_3<0.115423, theta_4<0.075468.

The positive Bessel series is retained through degree k^1024. The infinite
series remainder is bounded using the global K_0 envelope; the radial
integral beyond r=8 and the infinite angular sum have their own upper bounds.

On [.01,.997], 987 adjacent rational intervals are covered by

    log(1/k) H_4(k) <= log(1/a) H_4(b), k in [a,b].

Their largest interval upper bound is below 0.959318. Analytic bounds on
(0,.01] and [.997,1) are below 0.001657 and 0.853361 respectively. These
three bounds imply the rational bound 24/25 on the whole open interval.

The complete derivation of the numerical bounds is in r25_uniform_bound.md;
r25_interval_shoot.py and r25_uniform_certificate.py execute the certificate.
The certificate includes the moment normalizations, Hilbert–Schmidt factors, positive series and endpoint bounds.

## Why (2) follows for the full trace

Writing q=Q/sqrt(M) and q(r)~c r^(-1/2)exp(-r), the fixed-k asymptotic
calculation gives, with epsilon_R=c sqrt(k) R^(-1/2) exp(-kR),

    S_2(V_(k,R))-(1/(2M)) integral V_(k,R)^2
       = epsilon_R^2 A(k)+o_k(epsilon_R^2).

This calculation retains the entire resolvent response of the broad mode,
including its negative ground-state direction. It is supplied in
r22_relaxed_unequal_wells.md; its original single-well ordering hypothesis
is now supplied by the Townes spectral result.

r25_separated_count.md proves that finitely many fixed exponentially decaying
wells regular at zero have the sum of their individual negative eigenvalue
counts when their centers are sufficiently far apart. It controls the
logarithmic kernel at the moving inter-well singularities and takes the
zero-energy limit after fixing the separation. Applying it here identifies
S_2 with the full negative trace. Equation (1) then determines the sign for
all sufficiently large separations at each fixed k.

## Relation to the principal research question

The principal question asks whether every finite orthonormal family obeys
integral (sum |phi_j|^2)^2 <= (2/M) sum integral |grad phi_j|^2.
This result closes the previously unresolved fixed unequal-scale distant
two-Townes-well construction. It supplies neither an upper bound for all
potentials nor a theorem excluding every compact subcritical optimizer.
It is also not a proof about the originally proposed nonradial BNLS problem.

The attempted global independent-scaling and state-deletion arguments have
not produced the required sign. Those failures are recorded separately;
they are not included among the proved conclusions (1)–(2).

## External mathematical input

The identification of the shooting solution uses M. K. Kwong,
*Uniqueness of positive solutions of Delta u-u+u^p=0 in R^n*,
Archive for Rational Mechanics and Analysis 105 (1989), 243–266,
https://doi.org/10.1007/BF00251502 .
The Birman–Schwinger principle, radial Bessel functions and basic spectral
perturbation are standard inputs; their specialized uses and constants are
derived in the included notes. These inputs are not claimed as new results.

## Reproducing the calculation

The included executable certificate requires Python 3 and mpmath 1.3.0.
From the root of this extracted archive, run the three commands in
research/r25_uniform_bound.md. They regenerate the shooting bracket, the
finite-radius interval profile and the complete parameter certificate, in
that order. The final executable asserts the rational bound 24/25 directly.
The accompanying SHA256 manifest identifies the source and data snapshot.
