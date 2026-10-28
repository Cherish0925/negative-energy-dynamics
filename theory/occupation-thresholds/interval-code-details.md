# Proof details of the R15 validated Townes shooting program

Date: 2026-10-09. Companion source: [r15_validated_townes.py](../../computations/occupation-computations/r15_validated_townes.py).
SHA-256 of the reviewed final file:
`d5bd62d276b0decd65eadca0c198610289fdb06f8ca33aad7606178edfc25b34`.

## Outcome and scope

The fixed `--certificate` calculation uses the interval arithmetic and derivative recurrences detailed below. The analytic shooting characterization of the unique positive radial ground state and the tail maximum principle remain mathematical inputs; the program is not a replacement for those arguments.

Reproduction uses ordinary CPython, without `-O` (the program's assertions must be enabled):

    python research/r15_validated_townes.py --certificate

The output is saved in [r15_townes_certificate_audit_rerun.json](../../computations/occupation-computations/r15_townes_certificate_audit_rerun.json).

## Arithmetic and conversions

Each scalar addition, product and reciprocal is evaluated in binary64 and then widened with `math.nextafter` in the required directions. Under correctly rounded IEEE-754 elementary operations this encloses the exact operation on the binary64 inputs. Product extrema use all four endpoint products; division excludes denominators containing zero and reverses reciprocal endpoints correctly, including negative denominators. Negation is exact. The source uses small integers and finite binary64 constants; no unrounded conversion of a non-dyadic exact bound is silently used as an enclosure.

The stated decimal shooting endpoints are explicitly interpreted as exact binary64 dyadics, which is sufficient: they need not equal the decimal rationals. Their exact integer ratios are emitted. The tiny Cauchy error radii `1e-39` and `1e-35` are also binary64 values. The rational tail bounds are approximately 3.54456e-42 and 1.47470e-38; I additionally checked using exact Fractions that they are strictly smaller than the actual binary64 radii, not merely the corresponding decimal numbers.

There are no transcendental evaluations in the differential enclosure. `log2` chooses the step only; correctness does not rely on a certified logarithm. The dyadic-grid assertions ensure exact additions and a positive step on the certificate's run.

## Origin enclosure

Writing q(r)=sum c_n r^(2n), the coded recurrence

    4(n+1)^2 c_(n+1) = c_n - sum_(i+j+k=n) c_i c_j c_k

is correct for q''+q'/r=q-q^3. The computed derivative polynomial also has the correct factors 2(n+1).

The analytic Volterra map on the complex disk |r|<=1/10, with |q-a|<=1/10, maps that ball into itself and contracts: the source verifies the corresponding rational inequalities with |q|<=231/100. Cauchy's bound applies to the even analytic solution. At r=1/128, the actual ratio to the complex disk radius is 5/64, below the deliberately coarse 101/1000. Both omitted series tails are correctly bounded.

The mesh starts at 1/128, so the interval loop alone does not cover the origin. The separately checked inequality

    (231/100)^2 (1+1/16384)^2 < 6

covers the full interval [0,1/128]. Positivity there follows from q>=a-1/10>1. This also gives q'<0 for 0<r<=1/128 by integrating (r q')'=r(q-q^3)<0, as required by the shooting classifications.

The function's optional parameter K should not be interpreted as supporting arbitrary orders with the same hard-coded remainder: the certified path uses exactly K=20, which is valid.

## Taylor propagation

The inverse-radius coefficients are (-1)^n/r^(n+1), the correct normalized Taylor coefficients. The recurrences for q and p=q' use normalized derivatives and convolution coefficients correctly. There is no missing factorial.

For each step, the Picard tube checks the self-map inclusion y+[0,h] f([r,r+h],Y) subset Y. Together with local smoothness away from zero this supplies existence and containment on the entire step. The construction of an initial tube need not itself be a validated bound: only the final checked inclusion is used.

The endpoint polynomial has degrees 0 through N-1. The separate interval `jets` evaluation over the whole time-and-state tube bounds the Nth normalized derivative, so adding that coefficient times h^N is the valid componentwise Lagrange remainder. Thus the endpoint and the whole-step tube have distinct, correct roles.

The envelope is evaluated on each full Picard tube, not just at mesh points. Contiguous dyadic steps therefore cover [1/128,6] without gaps.

## Shooting classification and returned values

The lower shot reaches r=11.3125 with q>2.6934e-5 and p>3.6965e-7. Every preceding Picard tube has q>0. It is therefore a genuine undershooting shot, not a later return after an earlier zero.

The upper shot reaches r=11.1875 with q<-3.0660e-7. Every preceding Picard tube has p<0. It therefore crosses zero while still descending, rather than being mistaken for an oscillating excited solution.

These strengthened history checks are present in the reviewed final code. The connected shooting alternative plus uniqueness of the positive decaying radial solution then brackets Q(0) between the exact dyadic endpoints. That argument must remain in the mathematical write-up.

The whole-bracket propagation reaches exactly r=6, with

    0.0027004838668358466 <= Q(6) <= 0.0042832814841662929,
    max certified Q(r)^2 (1+r^2)^2 <= 5.024646047563436 < 6.

The textual endpoint representation uses 17 significant decimal digits, so parsing it back recovers the identical binary64 endpoint; the subsequent Fraction comparison against 1/200 is sound.

## Infinite tail

The code verifies the numerical input Q(6)<1/200. Positivity, radial monotonicity and decay of the identified ground state give Q(r)<=1/200 for r>=6. Set W=(1/200) exp(-(r-6)/2). Then

    (-Delta+1/4)Q=(Q^2-3/4)Q<=0,
    (-Delta+1/4)W=W/(2r)>0.

The exterior maximum principle gives Q<=W. Moreover W(r)(1+r^2) strictly decreases for r>=6, since its logarithmic derivative is -1/2+2r/(1+r^2)<0. At r=6 its square is (37/200)^2<6, an exact rational inequality checked by the program. This closes the rational envelope over [6,infinity).

## Conclusion

For the fixed certificate inputs, the reviewed program plus the stated analytic origin, shooting and tail arguments establishes Q(r)^2<6/(1+r^2)^2 on the full half-line. This conclusion does not prove the rank-two Lieb-Thirring conjecture or establish the novelty of the resulting one-bound-state statement; those are separate questions.
