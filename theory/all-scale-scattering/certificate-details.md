# Proof of the R25 interval certificate

2026-10-15. This note records the mathematical and implementation checks
actually made on [r25_interval_shoot.py](../../computations/all-scale-scattering/r25_interval_shoot.py), the shooting JSON outputs,
[r25_uniform_certificate.py](../../computations/all-scale-scattering/r25_uniform_certificate.py), and the final statement
[main-theorem.md](main-theorem.md). It does not replace the proofs in
[uniform-bound.md](uniform-bound.md) or the raw certificate.

## Conclusion

The validated shooting enclosure and the positive-integral certificate
support

$$
 \log(1/k)H_4(k)<24/25\quad\hbox{for every }0<k<1.
$$

Combined with the independently checked analytic radial comparison, this
gives

$$
 \mathcal A(k)<-\frac{2\pi}{25\log(1/k)}<0,
       \qquad 0<k<1.
$$

The complete certificate was independently executed. The 987 compact
parameter intervals, both analytic endpoint bounds, and every asserted
norm and coefficient inequality passed. The largest compact interval
bound is less than `0.959318`, below the exact rational `24/25=0.96`.
The final shooting outputs identify a genuinely positive undershoot
trajectory at the lower initial parameter and an overshoot at the upper
parameter. The issue identified during this review, concerning a possible
missed node between output radii, was repaired and the two shooting runs
were repeated.

## 1. Origin series and Taylor integration

The origin change of variable `t=r^2` gives
`4(tF''+F')=F-F^3`. Its coefficient recursion has denominator
`4(n+1)^2`, as implemented. On the complex disk `|t|<=0.01`, the
Volterra map preserves `|F-alpha|<=0.1` and is a contraction with the
displayed bounds using `|F|<=2.31`. Thus the Cauchy coefficient bound is
valid for all initial values in the stated interval, not only for a
floating central approximation.

The remainder for `Q'` is the derivative of the full majorant geometric
tail: the terms `N*z^(N-1)/(1-z)` and `z^N/(1-z)^2` are both present.
The radius `r0=1/20` gives `z=1/4` as required. The analytic origin
enclosure also proves positivity on `[0,r0]` because
`alpha-0.1>0`.

The `jet` function generates Taylor coefficients divided by the relevant
factorials. Its convolution for `Q^3` and the geometric expansion of
`1/r` agree exactly with

$$
 q'=p,\qquad p'=q-q^3-p/r.
$$

At each step, the Picard image is explicitly tested for inclusion in the
whole step tube. The coefficient of order 20 is evaluated on this entire
tube and the whole radius interval, so it bounds the Lagrange remainder.
The initial guesses for the tube need not themselves be valid derivative
bounds: the subsequent Picard inclusion test supplies the required
enclosure. Reducing the guessed tube size does not weaken the proof.

The accumulated radius intervals and the last step `target-r` enclose
the exact underlying mesh and the final radius eight. No calculation
assumes that a rounded floating radius is exact.

## 2. Exact endpoints and the shooting classification repair

The current `hull(a,b)` passes the binary endpoints directly into
`iv.mpf([a,b])`. The saved `_mpi_` tuples preserve the sign, integer
mantissa, binary exponent, and precision of both endpoints. The
certificate reconstructs those tuples with `iv.make_mpf`. The
human-readable `nstr` decimal fields are not inputs to any bound.
Converting those printed decimal fields back into purported intervals
would not be justified; the checked implementation avoids that issue.
The endpoint representation was already in this corrected form when this
Proof details began.

The original undershoot test only inspected a final endpoint satisfying
`0<q<1` and `p>0`. By itself, that test does not exclude a trajectory
which crossed zero between earlier output radii. This review requested
a whole-step positivity check. The corrected solver accumulates
`positive_on_all_step_tubes` and asserts it before accepting an
undershoot. The lower-parameter rerun reports that flag as `true`.
Its endpoint satisfies `q>7.098849e-8` and `p>5.9371734e-10`; every
earlier entire step tube also has `q>0`. The upper-parameter trajectory
has a strictly negative endpoint, which already proves an overshoot.

The accompanying shooting argument now identifies the actual Townes
initial value: positive upward-turn trajectories and zero-crossing
trajectories form disjoint open classes. At the first upward turn the
radial energy is negative, and

$$
 E'=-(Q')^2/r\le0
$$

prevents any later zero. A parameter on the boundary between the classes
stays positive and decreasing and tends to zero. It cannot tend to one:
if it stayed above one, `(rQ')'=r(Q-Q^3)<0` would imply
`Q'<=-c/r` after any fixed positive radius, contradicting convergence.
Uniqueness of the positive decaying radial solution then gives the
claimed initial-value bracket.

## 3. The global Bessel envelope

The checked inequality `Q(8)^2<1-beta^2`, with `beta=0.9999999`, makes
`Q(8)exp(-beta(r-8))` an exterior supersolution. This gives the rough
tail required to integrate the exact Wronskian identity. In the resulting
bound on `lim Q/K_0`, the contribution

$$
 q_R^3e^R\left[\frac{R}{3\beta-1}
              +\frac1{(3\beta-1)^2}\right]
$$

has the correct exponential factor and coefficients. The lower bound
for `K_0(R)` follows directly from
`(1+x)^(-1/2)>=1-x/2` in its positive integral representation. The
verified tail coefficient is below `2.810013`, so the rational choice
`A=2.82` is valid. Since `Q/K_0` is increasing, this is a global bound,
not merely an exterior estimate.

## 4. Moment, angular, and series-tail normalizations

The stored moments are normalized by `(n!)^2`. The compact panel
recurrence and the two-step integration-by-parts recurrence for the
exponential tail preserve that normalization. In particular the tail
coefficient multiplying the previous scaled moment is
`(2n-1)/(2n)`, as implemented.

The Hilbert--Schmidt integral is over a triangle and has prefactor
`1/(2m^2)`. Its same-panel contribution and the outer-tail bound in the
code agree with direct integration. The four certified norm bounds are
strictly below one. The largest is the `m=1` bound, also explicitly
checked in the final code, so it controls the common denominator used
in the series tail and both endpoint bounds.

The Bessel-square coefficient used by the program is

$$
 \frac{(2n)!}{4^n(n!)^2(n-m)!(n+m)!},\qquad n\ge m.
$$

The regrouping of its positive angular weights includes some negative
individual corrections, but the total coefficient is positive. The
interval lower bound of that total is tested before multiplying by an
upper moment. Thus no multiplication by a negative unknown coefficient
reverses an inequality.

For `n<=512`, the code uses finite-panel upper moments. For the omitted
coefficients it independently uses the global true-profile moment bound
from `Q<=A K_0`. These are two separate estimates: it is not necessary,
and was not proved, that every coefficient of the infinite piecewise
constant upper profile obeys the latter global bound. This distinction
was identified during review and clarified in the written derivation;
the code already used the correct finite-sum-plus-true-tail procedure.

The omitted true series is bounded by

$$
 \frac{A^2\pi}{4(1-\overline\theta_1)}
        \frac{k^{1026}}{1-k^2}.
$$

The radial tail, series tail, and angular tail are all included; none
is inferred from floating quadrature convergence.

## 5. Coverage of the entire k interval and the final quantifiers

The small-k estimate has denominator `16(1-theta_1)(1-k)^3` and
the large-k estimate has denominator
`8(1-theta_1)sqrt(2k(1-k))`; both constants were checked from their
elementary positive integrals. After multiplication by `log(1/k)`, they
give upper bounds below `0.001657` on `(0,0.01]` and below `0.853361`
on `[0.997,1)`.

The 987 compact intervals have exact rational endpoints `j/1000`.
Positivity of the coefficient series proves monotonicity of `H_4`, so
`log(1/a)H_4(b)` bounds every interior point of `[a,b]`. The independent
execution reproduced the maximum bound below `0.959318` on
`[0.856,0.857]`. This is interval coverage, not a sign inference from
sampled parameter values.

The final theorem's quantifiers are correct: the coefficient result
holds for every `0<k<1`; the full negative-trace inequality holds for
every fixed such `k` and all `R>R_0(k)`. The separate analytic
distant-well count proves there are exactly two negative levels there.
No uniform statement in a simultaneous limit `k=k(R)` is implied.
