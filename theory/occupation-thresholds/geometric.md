# Rank-two geometry and unequal-scale Townes pairs

This note records exact identities and one asymptotic exclusion result. It does **not** prove the two-dimensional rank-two Lieb–Thirring conjecture. The equal-scale two-bump obstruction is a prior-round baseline; the unequal-scale coefficient and its endpoint signs are the continuation developed here.

## Normalization

Let Q be the positive radial Townes ground state

    -ΔQ + Q = Q³  on R²,

and let Mc = ∫Q². The Pohozaev identities give ∫|∇Q|² = Mc and ∫Q⁴ = 2Mc. Put q = Q/sqrt(Mc), so ∫q² = ∫|∇q|² = 1 and ∫q⁴ = C1 = 2/Mc. The proposed rank-two inequality is

    ∫(|φ1|²+|φ2|²)² ≤ C1 (∫|∇φ1|²+∫|∇φ2|²)

for L²-orthonormal pairs.

## Geometric identities and a failed universal bound

For a complex spinor Φ=(φ1,φ2), write Φ=Rχ wherever R=|Φ|>0 and χ*χ=1. Then

    Σ|∇φj|² = |∇R|² + R²|∇χ|².

Let ρ=R², n=χ*σχ in S², and a=-iχ*∇χ. Pointwise,

    |∇χ|² = (1/4)|∇n|² + |a|².

Orthonormality is exactly

    ∫ρ=2,   ∫ρ n=0.

The desired inequality is therefore

    ∫ρ² ≤ (2/Mc) [∫|∇sqrt(ρ)|² +(1/4)∫ρ|∇n|²+∫ρ|a|²].

A putative general bound “orientation energy ≥ amplitude energy” is false: take two disjointly supported, normalized smooth functions, with χ constant and equal to a different coordinate vector on each support. Orientation energy is zero but amplitude energy is positive. The inequality is nevertheless true for such disjoint pairs by applying scalar GN separately. Thus a successful geometric argument must couple the local mass decomposition to the orientation cost; it cannot bound the latter by amplitude energy alone.

For real-valued pairs, Φ=R(cos θ,sin θ), so the equivalent identities are

    A = ∫|∇R|²+∫R²|∇θ|²,
    ∫R²=2,  ∫R² e^(2iθ)=0.

These are local coordinate identities; one should not assume a globally smooth phase across zeros. The sharp constant can be reduced to real pairs by spectral duality with a real scalar potential, whose eigenfunctions admit a real orthonormal basis. This reduction is standard and not an original theorem.

## Exact unequal-scale two-bump formula

Fix a>b>0 and R>0. Let

    f(x)=a q(ax),   g(x)=b q(b(x-Re1)).

Both have L² norm one. Define

    s=∫fg,  u=∫f³g,  w=∫fg³,  v=∫f²g²,  t=∫∇f·∇g.

For R large, 0<s<1. Exact orthonormalization is

    φ+=(f+g)/sqrt(2(1+s)),  φ−=(f−g)/sqrt(2(1−s)).

Its density and kinetic energy are

    ρ=(f²+g²−2sfg)/(1−s²),
    A=(a²+b²−2st)/(1−s²).

Since each scaled q solves -Δf+a²f=Mc f³,

    t=−a²s+Mc u=−b²s+Mc w.

Direct expansion, with no omitted errors, gives

    (1−s²)² [∫ρ²−C1 A]
      =2v(1+2s²)−2s(u+w)(1+s²)+C1(a²+b²)s⁴.             (1)

The cancellation of the ordinary s² term is specific to the critical two-dimensional cubic scaling.

## Large-separation reduction to one explicit function

Write η=b/a in (0,1). Standard radial ODE asymptotics give

    q(r) ~ cq r^(−1/2)e^(−r),   cq>0.

Set εR=cq sqrt(b) R^(−1/2)e^(−bR). For each fixed a>b, exponential decay and dominated convergence give

    s=εR ∫f e^(bx1)+o(εR),
    u=εR ∫f³e^(bx1)+o(εR),
    w=o(εR),
    v=εR² ∫f²e^(2bx1)+o(εR²).

The strict a>b assumption is essential to these dominated-convergence steps and the estimates are not asserted uniform as η approaches 1.

Define finite integrals for 0≤η<1:

    Aη=∫Q e^(ηx1),   Bη=∫Q²e^(2ηx1),   Dη=∫Q³e^(ηx1).

Multiplying the Townes equation by e^(ηx1) and integrating gives the exact identity

    Dη=(1−η²)Aη.                                      (2)

Equation (1) consequently gives

    ∫ρ²−C1 A
       = [2 εR²/Mc²] [Mc Bη−Aη Dη]+o(εR²)
       = [2 εR² Aη²/Mc²] H(η)+o(εR²),                (3)

where

    H(η)=Mc Bη/Aη²−(1−η²).

This is a precise, potentially useful reduction: H(η)>0 at one fixed η would produce a genuine rank-two counterexample for all sufficiently large R. H(η)<0 rules out this entire large-separation family at that ratio.

## Proved endpoint signs

At η=0, equation (2) says ∫Q=∫Q³. Strict Cauchy–Schwarz gives

    (∫Q²)² < (∫Q)(∫Q³) = (∫Q)².

Thus H(0)=Mc²/(∫Q)²−1<0. By continuity, H is negative on an interval [0,η0]. This excludes all sufficiently disparate fixed scales in the large-separation limit.

As η approaches 1 from below, Dη tends to the finite positive D1=∫Q³e^(x1). Equation (2) implies Aη~D1/[2(1−η)]. Meanwhile the radial tail and the large-argument estimate for I0 give

    Bη=2π∫r Q(r)² I0(2ηr)dr = O((1−η)^(−1/2)).

Consequently

    H(η)=−2(1−η)+O((1−η)^(3/2))<0

for η sufficiently close to 1. This also excludes all sufficiently close but distinct fixed scales followed by large separation.

These two endpoint exclusions are rigorous. They leave a compact intermediate interval of ratios, as well as coupled limits in which η varies with R.

## Exploratory numerical evidence; not a certificate

A radial scipy.solve_bvp calculation with residual tolerance 2e−10, 3,933 adaptive nodes, decaying K0 boundary condition at r=30, and tail matching at r=16 produced Q(0)=2.20620086465 and Mc=11.70089652456. Adaptive radial quadrature used the Bessel representations of Aη and Bη. The following numbers are exploratory rather than interval-certified.

| η | H(η) | Mc Bη / [Aη²(1−η²)] |
|---:|---:|---:|
| 0 | −0.400307891 | 0.599692109 |
| 0.2 | −0.387014642 | 0.596859748 |
| 0.4 | −0.347156128 | 0.586718895 |
| 0.6 | −0.280111348 | 0.562326019 |
| 0.8 | −0.180548510 | 0.498476362 |
| 0.9 | −0.110540749 | 0.418206583 |
| 0.95 | −0.064794213 | 0.335443971 |
| 0.99 | −0.016345328 | 0.178626746 |
| 0.995 | −0.008660461 | 0.131783376 |

The calculations give no evidence for a counterexample within this family. They do not prove H≤0 on the remaining continuum of ratios, and even such a proof would not establish the unrestricted rank-two conjecture.

## What this changes

The new calculation rules out two substantial limiting regimes of the unequal-scale two-Townes ansatz and gives its exact remaining sign problem. It does not improve the presently available universal Lieb–Thirring bound. It suggests that merely separating and resizing scalar optimizers is unlikely to yield the sought breakthrough; a successful counterexample would need an intermediate, genuinely interacting structure, or a proof would need a mechanism controlling such structures.
