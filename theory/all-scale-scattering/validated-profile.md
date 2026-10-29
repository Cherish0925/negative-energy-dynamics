# An interval enclosure of the two-dimensional Townes profile

15 October 2026. This note documents the executed interval computation in
[r24_validated_profile.py](../../computations/all-scale-scattering/r24_validated_profile.py), [r24_validated_shooting_tight.json](../../computations/all-scale-scattering/r24_validated_shooting_tight.json), and
[r24_validated_profile_tight.json](../../computations/all-scale-scattering/r24_validated_profile_tight.json). The computation uses neither an
unvalidated boundary-value solution nor a floating-point estimate of Q(0)
as a mathematical input.

The ODE is

    Q'=P,  P'=Q-Q^3-P/r,  Q(0)=a,  P(0)=0.

The executed shooting integrations prove

    2.20620086465074 < Q(0) < 2.20620086465075.

Propagation of this entire interval gives

    0.0004111388055274108280656224668505271924
       <= Q(8) <=
    0.0004111499184074464541714897575666726548,

and

    -0.0004361284606355364358011495589238432792
       <= Q'(8) <=
    -0.0004361165775975341182419672884786729326.

The profile file also encloses Q and Q' at every node of a mesh of maximum
length 0.005, as well as on every complete mesh segment. It includes separate
nodes at 0, 0.005, and 0.01 before the ordinary ODE propagation starts.

## 1. Arithmetic and serialization

All operations determining a mathematical bound use `mpmath.iv` version
1.3.0 with interval decimal precision 70. Only integer powers and rational
arithmetic are required by the enclosure algorithm. Grid endpoints use
Python `Fraction`; no binary floating-point grid coordinate enters an
enclosure. Ordinary floats are used only in progress messages and elapsed
times.

Each interval endpoint is read as its exact dyadic representation
`(-1)^sign * mantissa * 2^exponent`. Serialization takes the exact floor of
the lower endpoint times 10^40 and the exact ceiling of the upper endpoint
times 10^40. Thus the decimal endpoints in the JSON files are outward
enclosures, not rounded-to-nearest displays.

The script checks every inclusion and contraction described below. A failed
step is retried with half its length; failure at a step below 10^-8 raises
an error rather than producing a result.

## 2. Analytic enclosure at the radial singularity

For complex r the regular solution satisfies

    Q(r)=a+int_0^r [1/t int_0^t s(Q(s)-Q(s)^3) ds] dt.

On the disk `|r|<=R=0.1`, work in the ball `||Q-a||_infinity<=eta=0.1`.
Writing `B=|a|+eta`, the integral map has image radius at most

    (R^2/4)(B+B^3) < eta

and Lipschitz constant at most

    (R^2/4)(1+3B^2) < 1.

Both strict inequalities are evaluated with outward intervals and stored
in the output. This proves the existence of a unique analytic solution
in the ball. Reflection and uniqueness make it even. Write

    Q(r)=sum_{j>=0} c_j r^(2j),  c_0=a.

Its exact recurrence is

    c_(j+1)=[c_j-sum_(i+l+m=j)c_i c_l c_m]/[4(j+1)^2].

Cauchy's estimate applied to Q-a gives `|c_j|<=eta/R^(2j)` for j>=1.
At `r=0.01`, after retaining j=0,...,16, let `z=(r/R)^2`. The remaining
terms are enclosed by the symmetric intervals of radii

    E_Q=eta z^17/(1-z),
    E_P=(2eta/r) z^17(17-16z)/(1-z)^2.

The same formula evaluates the extra node at 0.005. This construction
handles the r=0 singularity analytically, with explicit tails.

## 3. Validated Taylor steps

Let the current enclosure be `(q_0,p_0)` at an exact rational radius r_0.
On `[r_0,r_0+h]`, the code finds rectangles `(Q_t,P_t)` satisfying the
strict Picard inclusions

    q_0+[0,h]P_t interior-subset Q_t,
    p_0+[0,h](Q_t-Q_t^3-P_t/[r_0,r_0+h]) interior-subset P_t.

It also checks the sup-norm contraction estimate

    h max{1, 1+3 sup|Q_t|^2+1/r_0} < 1.

Consequently the entire exact solution starting anywhere in the input
rectangle stays inside the tube. The contraction also gives uniqueness.

For normalized derivative coefficients q_j and p_j, define
`d_j=(-1)^j/r_0^(j+1)`. The recurrence is

    q_(j+1)=p_j/(j+1),
    p_(j+1)=[q_j-sum_(a+b+c=j)q_a q_b q_c
                       -sum_(a+b=j)p_a d_b]/(j+1).

First evaluate these coefficients at the input interval and point radius
through degree 18. Then evaluate the same recurrence through degree 19,
with initial values allowed throughout `(Q_t,P_t)` and the radius
throughout `[r_0,r_0+h]`. The last result encloses every normalized 19th
derivative along the step. Taylor's theorem therefore gives

    y(r_0+h) in sum_(j=0)^18 y_j h^j + Y_19 h^19.

Replacing h by the interval `[0,h]` gives an enclosure of the whole step.
Both endpoint and whole-step enclosures are recorded. Interval dependency
can enlarge the result but cannot invalidate the inclusion.

Near r=0 the step is at most r_0/16. The maximum step is 0.02 for shooting
and 0.005 for the final profile. These choices make the derivative
remainder small without assuming its sign.

## 4. The two endpoint shots identify the ground-state amplitude

The lower initial value `a_-=2.20620086465074` has been enclosed up to
`r approximately 18.03657235839541`, where

    Q >= 0.0000000250402050271144300225210637802628 > 0,
    Q' >= 0.0000000001826535408371183540908402742954 > 0.

Every whole-step Taylor range before this point is strictly positive in Q;
the analytic disk bound handles the initial interval. The lower shot
therefore turns while still positive.

The upper initial value `a_+=2.20620086465075` has been enclosed up to
`r approximately 18.23657235839541`, where

    Q <= -0.0000000003324566939727182860559055309624 < 0,
    Q' <= -0.0000000199909715031332650132068469255364 < 0.

Thus it crosses zero. A prior positive turn is impossible: at such a first
turn Q lies in (0,1), and the radial energy

    E=(Q')^2/2-Q^2/2+Q^4/4,  E'=-(Q')^2/r,

is then strictly negative and can never subsequently reach Q=0, where
the energy would be nonnegative.

Here is the shooting argument connecting these two finite computations
to the ground state. Initial values in the bracket exceed 1. While the
solution remains positive and decreasing it is bounded and can be
continued. The events of first crossing zero and first turning while
positive are disjoint open sets of initial values: at a zero the derivative
is nonzero by uniqueness; at a positive first turn the second derivative is
strictly positive, because Q is then in (0,1). Since the two bracket
endpoints belong to different open sets, some intermediate initial value
has neither event. Its solution stays positive and strictly decreasing
for all r.

For such a solution the limit is 0 or 1. Indeed, the energy bound controls
Q', and its derivative is bounded away from the origin; since the integral
of |Q'| is finite, Q' tends to zero. The ODE then forces the limiting value
ell to satisfy `ell-ell^3=0`. Limit 1 is impossible: then v=Q-1 is positive
and obeys

    v''+r^(-1)v'+Q(Q+1)v=0,

whose coefficient is at least 2. Setting `w=sqrt(r)v` gives a linear
equation `w''+[Q(Q+1)+1/(4r^2)]w=0`; Sturm comparison forbids a solution
remaining positive on the whole half-line. The limit is therefore zero.
The equation and exterior comparison with a decaying modified Bessel
function give exponential decay.

Uniqueness of the positive decaying radial solution identifies this
intermediate shot with the Townes profile. The uniqueness theorem used
here is the established result of M. K. Kwong, *Uniqueness of positive
solutions of Delta u-u+u^p=0 in R^n*, Archive for Rational Mechanics and
Analysis 105, 243--266 (1989), DOI 10.1007/BF00251502. The publisher's
abstract explicitly includes the whole-space, positive radial, decaying
case: https://link.springer.com/article/10.1007/BF00251502 .

No monotonic ordering of all shoots with respect to their initial value
is assumed. The connectedness argument and uniqueness suffice.

## 5. Reproduction and use of the profile table

Run the two commands from the project root:

```bash
cd computations/all-scale-scattering  # from the repository root
python3 r24_validated_profile.py --mode shoot --a-low 2.20620086465074 --a-high 2.20620086465075 --stop 24 --output r24_validated_shooting_tight.json
python3 r24_validated_profile.py --mode profile --a-low 2.20620086465074 --a-high 2.20620086465075 --step 0.005 --output r24_validated_profile_tight.json
```

The shooting file must have `bracket_success: true`; the lower shot must
also have `positive_entire_history: true`. The profile table has 1619
propagation segments. Each `r0` and `r1` is an exact rational string;
`q0`, `p0`, `q1`, `p1`, `q_range`, and `p_range` contain outward lower and
upper decimal bounds. `q_tube` and `p_tube` are the larger Picard tubes,
not the sharper whole-step Taylor ranges. `origin_nodes` supplies the
first three nodes.

For a monotone-profile quadrature, the upper Q bound at a cell's left node
bounds Q on that cell, and the lower bound at its right node is a lower
bound there. The monotonicity follows from the shooting argument above.

A separate ordinary SciPy boundary-value calculation on [0,25] gives
Q(8) approximately 0.000411144362 and agrees with the interval. That
calculation was used only as a comparison and is not an input to any
enclosure or shooting conclusion.
