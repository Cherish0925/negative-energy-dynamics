# all coincident two-Townes tangent directions have a strict rank-two deficit

Date: 2026-10-09. This note resolves the degenerate corner left in the R16
two-Townes analysis. It does not prove the unrestricted rank-two
Lieb--Thirring inequality. The result is a complete, validated exclusion of
every scale/translation tangent direction, not a sampled parameter search.

Let Q be the positive radial Townes solution of

    -Delta Q + Q - Q^3 = 0 in R^2,
    Mc = integral Q^2, q=Q/sqrt(Mc), C1=2/Mc.

Then ||q||_2=||grad q||_2=1 and integral q^4=C1. Write

    Lambda Q=Q+x.grad Q.

The Q and all derivatives used below are the same profile as in the saved
R15 shooting certificate. No new floating-point approximation is substituted
for it.

## 1. Complete tangent-family theorem

For every real a and b in R^2, not simultaneously zero, set

    f=a Lambda Q+b.grad Q,   w=f/||f||_2.

Then (q,w) is an orthonormal pair. For

    A=||grad q||_2^2+||grad w||_2^2,
    F=integral(q^2+w^2)^2,

one has the explicit uniform bounds

    F-C1 A <= -1/20,                                (1)
    F/A <= C1-1/105.                                (2)

All constants in (1)--(2) are rational and independent of the tangent
direction. The overall spatial scale is fixed by ||grad q||_2=1; after a
common spatial dilation, (2) remains unchanged whereas (1) scales by the
square of that dilation.

### Exact reduction to three coefficients

By rotation, b.grad Q can be written beta Q'(r)cos(theta). Put

    H(r)=Q(r)+r Q'(r), P(r)=Q'(r),
    f=alpha H+beta P cos(theta).

The mass-preserving scaling identity gives <Q,Lambda Q>=0, and parity gives
<Q,partial_j Q>=0. Moreover the two tangent sectors are mutually
orthogonal. They are nonzero, so f cannot vanish unless alpha=beta=0.

Introduce seven radial integrals, all over (0,infinity) with measure r dr:

    m=integral Q^2 r dr,
    h=integral H^2 r dr,
    j=integral Q^2 H^2 r dr,
    k=integral Q^2 P^2 r dr,
    a4=integral H^4 r dr,
    b4=integral P^4 r dr,
    d4=integral H^2 P^2 r dr.

Thus Mc=2pi m, ||H||_2^2=2pi h and
||partial_1 Q||_2^2=pi m. The last identity follows from radial symmetry and
the Townes Pohozaev identity ||grad Q||_2^2=Mc.

Differentiating the profile equation gives, for L+=-Delta+1-3Q^2,

    L+ Lambda Q=-2Q,   L+ partial_1 Q=0.

Since <Lambda Q,Q>=0, integration by parts yields

    h_Q[H]=2pi(2j-h),
    h_Q[partial_1 Q]=pi(2k-m),

where h_Q[v]=integral(|grad v|^2-Q^2|v|^2). Mixed radial/angular terms vanish.
Set N=||f||_2^2=2pi h alpha^2+pi m beta^2. Using the exact equality for q,

    N^2(F-C1 A)=integral f^4-(2/Mc)N h_Q[f].        (3)

Angular integration of cos^2 and cos^4 now gives the exact biquadratic
polynomial

    N^2(F-C1 A)=2pi c40 alpha^4
                    +pi c04 beta^4+pi c22 alpha^2 beta^2, (4)

where

    c40=a4-(2h/m)(2j-h),
    c04=(3/4)b4-(2k-m),
    c22=6d4-4hk/m-4j+4h.                            (5)

There is no truncation of the tangent direction in (4); its dependence on
all directions is exactly polynomial.

## 2. Validated coefficient enclosures

The accompanying standard-library Python program
[r17_tangent_certificate.py](../../computations/occupation-computations/r17_tangent_certificate.py) uses the interval arithmetic and validated ODE
steps from [r15_validated_townes.py](../../computations/occupation-computations/r15_validated_townes.py). The R15 certificate brackets Q(0) between
the exact dyadic numbers represented by 2.20620086 and 2.20620087. This
bracket is propagated as one interval initial condition, so the true Townes
solution remains enclosed throughout.

The new calculation integrates the seven radial integrands using whole
Picard tubes on 408 dyadic intervals up to r=6. Each elementary arithmetic
operation is rounded outward. No ordinary numerical quadrature, sampled
integrand maximum or floating-point eigensolver enters the proof.

The saved [r17_tangent_certificate.json](../../computations/occupation-computations/r17_tangent_certificate.json) gives the complete enclosures. To
avoid treating decimal renderings as exact proof constants, only the
following coarser rational consequences are used:

    9/5 < m < 77/40,       1 < h < 6/5,
    j < 7/4,              k < 8/3,
    c40 < -1/2,           c04 < -3/4,
    c22 < -3/2.                                    (6)

For reference, the directed coefficient intervals are approximately

    c40 in [-2.285341,-0.651739],
    c04 in [-1.802676,-0.999418],
    c22 in [-6.450114,-1.696796].

These displayed rounded intervals are only a readable summary; the JSON
records round-trip binary64 endpoints and the program checks (6) with exact
`Fraction` conversions.

### Origin and infinite-tail enclosures

On 0<=r<=1/128, monotonicity gives Q<=221/100. The integral form of the
profile equation gives |Q'|<=7r. Consequently |H|<=221/100+7r^2. Integrating
these nonnegative upper bounds and using zero as a lower bound encloses
the entire origin interval, including the coordinate singularity.

The propagated endpoint obeys Q(6)<1/200. Let c=99/100 and a6 be its
certified upper bound. For r>=6,

    Q(r)<=a6 exp[-c(r-6)].                          (7)

Indeed W=a6 exp[-c(r-6)] is a supersolution of
[-Delta+(1-Q^2)]W>=0 because
1-Q^2-c^2+c/r>0. The radial exterior maximum principle proves (7), using
Q,W->0 at infinity. Integrating
(rQ')'=r(Q-Q^3) from r to infinity gives

    |Q'(r)|<=a6 exp[-c(r-6)](1/c+1/(c^2 r)),
    |H(r)|<=a6 exp[-c(r-6)](r+2)/c^2.               (8)

The tail contributions are therefore bounded by integrals of nonnegative
polynomials times exp[-2c(r-6)] or exp[-4c(r-6)]. They are evaluated
exactly up to outward interval arithmetic from

    integral_0^infinity s^n exp(-lambda s) ds=n!/lambda^(n+1).

Thus no numerical exponential evaluation or unproved tail cutoff is used.

### Deriving the stated uniform constants

Let X=2pi h alpha^2 and Y=pi m beta^2, so N=X+Y. Equations (4)--(6), together
with pi<22/7, give separately

    2pi c40 alpha^4 <= -X^2/20,
    pi c04 beta^4 <= -Y^2/20,
    pi c22 alpha^2 beta^2 <= -XY/10.

Their sum and (3) prove (1).

The same differentiated profile equations give

    ||grad H||_2^2/||H||_2^2=3j/h-1<17/4,
    ||grad partial_1 Q||_2^2/||partial_1 Q||_2^2
        =3k/m-1<31/9<17/4.

The kinetic energy of the normalized combination w is a weighted average
of these two ratios. Hence A<=1+17/4=21/4. Dividing (1) by A proves (2).

## 3. A whole neighborhood of coinciding Townes packets is excluded

Consider the normalized generating functions

    f0(x)=q(x),   g_{b,z}(x)=b q(b(x-z)),
    b>0, z in R^2, (b,z)!=(1,0).

Let s=<f0,g_{b,z}> and orthonormalize by

    phi_1=q,   phi_2=(g_{b,z}-s q)/sqrt(1-s^2).

This basis and every other orthonormal basis of the same two-dimensional
complex span have the same density and kinetic trace. Multiplying either
generating packet by a constant phase therefore does not change the result.

The map (b,z)->g_{b,z} is twice continuously differentiable into H1 near
(1,0), because Q is smooth and all needed weighted derivatives decay
exponentially. Its Taylor expansion is

    g_{b,z}=q+(b-1)Lambda q-z.grad q+O_H1(d^2),
    d=sqrt((b-1)^2+|z|^2).

The first-order term is perpendicular to q, and its L2 norm is bounded
above and below by positive constants times d. Thus uniformly over the
compact sphere of parameter directions,

    phi_2=[(b-1)Lambda q-z.grad q]
             /||(b-1)Lambda q-z.grad q||_2+O_H1(d).

The functional F/A is continuous on these H1-bounded normalized pairs,
and A>=1. The strict uniform gap (2) therefore proves the existence of a
single eta>0 such that

    0<sqrt((b-1)^2+|z|^2)<eta
      implies F/A<=C1-1/210.                       (9)

The neighborhood radius eta is not assigned a numerical value here. Its
existence follows from an explicit uniform tangent gap and ordinary H1
Taylor continuity; it is not an assertion based on a finite parameter mesh.

## 4. What this adds to the global endpoint problem

R16 excluded distant two-Townes pairs, arbitrary simultaneous near-equal
scale/distant limits, and extreme scale separation at every spatial
separation. The only degenerate point remaining when those parameters were
bounded was (b,z)=(1,0). Equation (9) excludes that point and an entire
neighborhood. Consequently any above-scalar pair within this particular
two-Townes family must lie in a genuine compact parameter set that is
separated from every degenerating boundary. The quotient is continuous on
that compact set and therefore attains its maximum there.

This does not establish that its remaining maximum is at most C1. Nor does
exclusion of the entire two-Townes family, if later completed, control
arbitrary orthonormal pairs. A general self-consistent nonradial optimizer
could have a different shape.

The original equal-occupation target remains

    integral(|phi_1|^2+|phi_2|^2)^2
        <=(2/Mc)(||grad phi_1||_2^2+||grad phi_2||_2^2)

for every orthonormal pair. This note proves a strict exclusion theorem for
one previously unresolved limiting mechanism, not that target.

## 5. Reproduction and inherited inputs

Run from the project root:

    python3 research/r15_validated_townes.py --certificate
    python3 research/r17_tangent_certificate.py

The first validates the profile bracket used by the second. The R15 saved
certificate is [r15_townes_certificate.json](../../computations/occupation-computations/r15_townes_certificate.json); the R17 output is
[r17_tangent_certificate.json](../../computations/occupation-computations/r17_tangent_certificate.json). All integration arithmetic is standard
Python binary64 with `math.nextafter` outward enlargement; rational final
checks use `fractions.Fraction`.

The profile equation, Pohozaev identities, differentiated zero modes,
Gram--Schmidt orthogonalization and interval arithmetic are established
tools. The contribution recorded here is the exact all-direction
biquadratic reduction together with its validated strict sign and the
resulting complete exclusion of the coincident-packet mechanism. Historical
first priority is not asserted.

The relation to the literature is consistent with Frank--Gontier--Lewin,
*The Nonlinear Schrödinger Equation for Orthonormal Functions II:
Application to Lieb--Thirring Inequalities*, Communications in Mathematical
Physics 384 (2021), 1783--1828,
https://doi.org/10.1007/s00220-021-04039-5. Their distant-packet strict-binding
theorem assumes kappa>max(0,2-d/2), strictly kappa>1 when d=2. It does not
settle the kappa=1 endpoint considered here. This primary source was
checked directly during this branch.
