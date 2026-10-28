# Derivation of the angular enclosure

15 October 2026. This note checks the mathematics and interval-operation directions of [r24_certified_angular.py](../../computations/all-scale-scattering/r24_certified_angular.py), including its updated within-cell Hilbert--Schmidt estimate. It assumes that the named profile and shooting inputs are the outputs of the separately checked interval ODE computation. It does not substitute a floating-point Townes profile for that input.

## 1. Complete angular tail, with no mode truncation

For the positive angular channels, the zero-energy radial kernel is

    Q(r)Q(s)(min(r,s)/max(r,s))^m/(2m).

Its Hilbert--Schmidt norm theta_m obeys theta_m<=theta_1/m. This follows pointwise by comparing (min/max)^m with min/max before squaring and integrating. Hence theta_1<=theta<1 gives

    2 sum_{m>=1} a_m(k)
       <= 2 b_1(k)/(1-theta)
          +(B_sum(k)-2b_1(k))/(1-theta/2).

The Bessel identity B_sum=2 sum_{m>=1}b_m rewrites this as int rQ(r)^2 F(kr)dr, where

    F(z)=c0[I_0(2z)-I_0(z)^2]+c1 I_1(z)^2,
    c0=1/(1-theta/2),
    c1=2/(1-theta)-2/(1-theta/2)>0.

The identity I_0(2z)-I_0(z)^2=2 sum_{m>=1}I_m(z)^2 proves that F is nonnegative and increasing on z>=0. This justifies both radial endpoint Riemann bounds and the right-k-endpoint bound on each k cell.

## 2. Hilbert--Schmidt enclosure

Put A(r)=int_0^r s^3Q(s)^2 ds. The exact quantity is

    theta_1^2=(1/2)int_0^infinity Q(r)^2 A(r) dr/r.

Let Q(r)<=q_a on a cell [a,b]. The updated code uses

    A(r)<=A_a+q_a^2(r^4-a^4)/4,

where A_a bounds A(a). Integration gives the cell upper bound

    q_a^2/2 * [A_a log(b/a)
       +q_a^2/4 *((b^4-a^4)/4-a^4 log(b/a))].

The cumulative bound is updated only after this calculation, exactly as required. The expression in the inner parentheses is nonnegative, since it is int_a^b (r^4-a^4)dr/r. Its interval lower endpoint may therefore safely be replaced by zero. On the first [0,b] cell, Q(0)^4b^4/32 is the correct bound.

The envelope rQ(r)^2<=D exp(-2r) gives

    A(infinity)<=A(R)+D exp(-2R)(R^2/2+R/2+1/4),
    theta_tail^2<=D A(infinity) exp(-2R)/(4R^2).

Both constants match the implementation. Positivity of the outer integrands makes all substitutions upper bounds.

## 3. Core and tail integrals

On each [a,b], monotonicity of the true Townes profile gives Q(r)<=Q(a)<=q_a. Consequently

    int_a^b rQ(r)^2 F(kr)dr
        <=q_a^2 (b^2-a^2)F(kb)/2.

For the elementary envelope integral,

    int_a^b exp(-2r)F(kr)dr
        >=(b-a) exp(-2b)F(ka).

The code subtracts this lower core integral from the upper enclosure of the full elementary Laplace integral, then multiplies by D. It does not subtract an actual-Q integral from an envelope integral. This is the correct subtraction for an upper bound on the remaining tail.

The input records inspected were contiguous from r=1/100 to R=8, and the first cell is [0,1/100]. Both the loose and tight input files cover the full interval [0,8].

## 4. Positive series and their remainder bounds

For I_m(z), m=0,1, consecutive positive terms have ratio

    (z^2/4)/[n(n+m)].

After the term n=N, the omitted first term is n=N+1 and all following ratios are bounded by (z^2/4)/[(N+2)(N+2+m)]. The code uses precisely this geometric tail. Its denominator is explicitly checked positive.

With c_n=binom(2n,n)/4^n, integration of the positive Bessel square series gives

    int_0^infinity exp(-2r)F(kr)dr
      =(1/2)sum_{n>=1}[c0(c_n-c_n^2)
                      +c1 c_n^2 n/(n+1)]k^(2n).

The coefficient recurrence c_n=c_{n-1}(2n-1)/(2n) is exact. Each coefficient is nonnegative and at most (c0+c1)/2. Therefore the remainder bound after n=N used by the code,

    (c0+c1) k^(2N+2)/[2(1-k^2)],

is valid. This estimate includes every positive series term; it is not a quadrature or angular-truncation approximation.

## 5. Endpoints and k-cell coverage

The exact integral

    int_0^infinity r K_0(r)^2 I_0(2kr)dr
       =asin(k)/(2k sqrt(1-k^2))

was checked independently by the positive double heat-integral representation of K_0 and the Gaussian I_0 integral. The transformed integral is

    (1/2)int_0^1 [1-4k^2x(1-x)]^(-1)dx.

With Q<=C K_0, log(1/k)<=(1-k)/k and asin(k)<=pi/2, this yields

    log(1/k)H_1(k)
       <=C^2 pi sqrt(1-k)/[4(1-theta)k^2sqrt(1+k)].

The right side is decreasing. Thus evaluating it at k_end bounds every k>=k_end. The small-k estimate used in the script follows from

    I_0(2z)-I_0(z)^2<=z^2 I_0(2z)/2,

the global exponential envelope, and monotonicity of k^2 log(1/k) for k<exp(-1/2). Its factor 16 in the denominator is correct.

On a compact cell [k_left,k_right], H_1(k) is increasing while log(1/k) is decreasing. The valid upper bound is therefore H_1(k_right) log(1/k_left). The script uses exact rational cell endpoints, enclosing the right endpoint in binary64 intervals and evaluating the left logarithm by interval arithmetic. The cells are adjacent and include both compact-interval endpoints.

## 6. Arithmetic and actual issues identified

Each binary64 addition, subtraction, multiplication and division is followed by nextafter toward the required exterior direction. Integer coefficients in these computations are within the exact binary64 integer range. Decimal/rational input conversion first rounds the exact Fraction, then extends by one ulp. mpmath.iv endpoints are similarly extended by one ulp after conversion. The statements are conditional on the stated ordinary IEEE-754 operation behavior and the correctness of mpmath.iv's elementary interval functions.

All places that clamp a lower bound to zero concern quantities independently known to be nonnegative: positive products, Bessel variance, c_n-c_n^2, the within-cell HS correction, or an actual positive tail. Thus those clamps are justified.

The initial loose profile gave C_bound=2.81359286579935883976..., so `--C 2.81` with that file fails the assertion. This was reported immediately. The tight profile has a smaller tail enclosure; alternatively C=2.82 works with the loose profile. The final result must name the actual input files and parameters used. No theorem can be based on silently mixing these inputs.

A reporting-only rounding issue was also reported: `float(Cbound.b)`, `float(small.b)`, `float(large.b)` and the displayed square root of theta_squared can round downward. Their printed `_upper` values should be enlarged by nextafter toward +infinity. The actual closure tests already use outward endpoints, so this issue does not change the proof decisions.

The reporting issue has been corrected in the final JSON by enlargement toward +infinity. The completed successful output [r24_certified_angular.json](../../computations/all-scale-scattering/r24_certified_angular.json) names [r24_validated_profile_tight.json](../../computations/all-scale-scattering/r24_validated_profile_tight.json) and [r24_validated_shooting_tight.json](../../computations/all-scale-scattering/r24_validated_shooting_tight.json), with C=2.82 and theta=0.55. Its stated enclosures are

    theta_1^2 <= 0.30242535317434427,
    compact-cell maximum <= 0.985343659554888,
    small endpoint bound <= 0.005768976332261827,
    large endpoint bound <= 0.9501975361507016.

There are 971 adjacent k cells covering [0.02,0.991]; the maximizing cell is [108/125,173/200]=[0.864,0.865]. Each displayed bound is strictly below the required threshold. Together with the radial comparison, the completed enclosure therefore establishes A(k)<0 for every 0<k<1, subject to the explicitly stated arithmetic assumptions and the independently established profile/shooting enclosure. No invalid mathematical upper bound or missing Bessel/angular remainder was found in the inspected updated computation.
