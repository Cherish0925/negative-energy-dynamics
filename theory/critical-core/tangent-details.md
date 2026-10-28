# Proof details of the R17 coincident two-Townes certificate

Date: 2026-10-09.

**Conclusion: PASS for the tangent-family theorem and the stated local exclusion.** The computation proves a strict gap for every real scale/translation tangent direction, and continuity then excludes a full neighborhood of coinciding Townes packets. It does not prove the general rank-two inequality or its remaining compact two-Townes region.

Files examined:

- [rank2-endpoint.md](rank2-endpoint.md)
- [r17_tangent_certificate.py](../../computations/occupation-computations/r17_tangent_certificate.py)
- [r17_tangent_certificate.json](../../computations/occupation-computations/r17_tangent_certificate.json)
- inherited interval implementation [r15_validated_townes.py](../../computations/occupation-computations/r15_validated_townes.py)
- [quantitative-gap.md](../occupation-thresholds/quantitative-gap.md) for inherited profile conventions

The R17 certificate was independently executed in this branch and returned `certificate_passed: true` in 408 validated steps. Its output matched the stored seven integral intervals and all three coefficient intervals. The inherited R15 `--certificate` was also rerun successfully: lower shot undershoot with positivity, upper shot overshoot with negative derivative, and the whole initial bracket enclosed through r=6. 

## 1. Independent coefficient derivation

Let H=ΛQ, D=∂1Q, f=αH+βD and N=||f||². Rotational invariance reduces every spatial translation direction to D. Orthogonality to Q follows from the critical scaling identity and parity, respectively; radial and angular sectors are mutually orthogonal for both their L² and gradient inner products.

With the note’s radial integrals, N=2πh α²+πm β² and Mc=2πm. Differentiation of the elliptic equation yields L+H=−2Q and L+D=0, where L+=−Δ+1−3Q². Therefore

    hQ[H]=2π(2j−h),       hQ[D]=π(2k−m).

For the orthonormal pair (Q/√Mc,f/√N), direct expansion gives

    N²(F−C1 A)=∫f⁴−(2N/Mc)hQ[f].

The fourth-power angular integrals are ∫1 dθ=2π, ∫cos²θ dθ=π, ∫cos⁴θ dθ=3π/4. Odd terms vanish. The resulting coefficients are exactly

    c40=a4−(2h/m)(2j−h),
    c04=3b4/4−(2k−m),
    c22=6d4−4hk/m−4j+4h,

and their factors are 2π, π, π. In particular, the mixed coefficient and the normalization by N² are correct. The calculation is a full polynomial identity in the parameters, not a directional sample or a Taylor truncation in α,β.

## 2. Origin and tail enclosures

At the origin, the inherited positive monotone ground state obeys 0<Q≤221/100. From (rQ′)′=r(Q−Q³) and Q′(0)=0 one obtains |Q′(r)|≤7r: the deliberately loose bound follows because |x−x³|<14 on 0≤x≤221/100. Hence |H|≤221/100+7r². Replacing each nonnegative integrand factor by its maximum on [0,1/128] and integrating r dr gives the exact type of upper bounds in the script; zero is a valid lower bound.

At r=6 the outward enclosure has Q(6)<1/200. For c=99/100 and certified a6≥Q(6), the function a6 exp[−c(r−6)] is a supersolution of the true linear operator −Δ+(1−Q²): its image divided by itself is 1−Q²−c²+c/r>0. The exterior maximum principle, together with decay at infinity and boundary domination at r=6, proves the Q tail bound. The script explicitly checks the stronger sufficient numerical condition c²+a6²<1 by intervals.

Integration of the radial ODE then gives

    |Q′(r)|≤a6 e^{−c(r−6)}(1/c+1/(c²r)).

The limit rQ′(r)→0 used in this integration follows from the decaying ground-state asymptotics, or directly from the now-integrable ODE right side and Q(r)→0. Because r≥6,

    |H(r)|≤a6 e^{−c(r−6)}(r+2)/c².

Indeed c²+rc+1≤r+2 when 0<c≤1. Thus with s=r−6 the script’s factors (s+6)(s+8)^n are correct. Each `tail_moment` expands a nonnegative polynomial and integrates its monomials using n!/rate^(n+1); there is no sampled tail or numerical exponential evaluation. All seven tail expressions have the correct powers of a6, c and the derivative bound.

## 3. Interval implementation

The interval class widens every elementary sum, product and reciprocal with `math.nextafter`. It interprets finite floating endpoints as exact dyadic reals. The new `nonnegative_square` safely handles a sign-changing interval by lower bound zero and the outward maximum of endpoint squares. For intervals of one sign, ordinary interval multiplication followed by clamping the lower endpoint to zero remains enclosing.

Each radial integrand is evaluated on the complete Picard tube and complete radius interval. Multiplication by the dyadic step therefore encloses its entire integral on that step. The step selector’s `log2` only chooses a mesh; it does not evaluate any function entering a mathematical inequality. Endpoint arithmetic is checked to satisfy end−r=h. All denominators used for the final coefficients are positive because m.lo>9/5.

The inherited implementation obtains endpoint Taylor enclosures from interval jets over the full tube and uses a separately bounded analytic series at the coordinate singularity. Those are the already established R15 dependencies. As usual for this implementation, the numerical conclusion assumes ordinary IEEE-754 binary64 behavior of Python’s basic arithmetic; this is not an exact-rational integration package.

## 4. Uniform numerical gap

The interval output proves

    9/5<m<77/40, 1<h<6/5, j<7/4, k<8/3,
    c40<−1/2, c04<−3/4, c22<−3/2.

Write X=2πh α², Y=πm β². The three exact rational checks using π<22/7 imply respectively

    2πc40 α⁴≤−X²/20,
    πc04 β⁴≤−Y²/20,
    πc22 α²β²≤−XY/10.

Summing proves F−C1 A≤−1/20, including the pure translation and pure dilation directions. The kinetic identities give

    ||∇H||²/||H||²=3j/h−1<17/4,
    ||∇D||²/||D||²=3k/m−1<31/9<17/4.

The gradient quotient for any normalized combination is their weighted average. Thus A≤21/4 and F/A≤C1−1/105. No missing direction dependence remains in these bounds.

## 5. Passage from tangents to a whole punctured neighborhood

The map g(b,z)=bq(b(·−z)) is C² into H¹ near (1,0), by smoothness and exponential decay of the Townes profile and its weighted derivatives. Its differential is (b−1)Λq−z·∇q. This differential is injective and perpendicular to q, and its L² norm is uniformly comparable to the Euclidean parameter distance d. Consequently normalized Gram–Schmidt remainders converge in H¹, uniformly over parameter directions, to the normalized tangent family, with error O(d).

The density quartic functional is continuous on bounded H¹ sets in two dimensions, the kinetic trace is continuous, and A≥1. Compactness of the unit parameter sphere therefore transfers the explicit 1/105 tangent quotient gap to a 1/210 gap throughout some common punctured neighborhood. An explicit numerical radius is not produced and is not required for this existence statement.

Constant complex phases on the two original packets merely change the generating basis of their complex span; density and kinetic trace of an orthonormal basis remain unchanged. This does not extend the theorem to independently Galilean-modulated packets or arbitrary orthonormal functions. The final compact-parameter implication in the endpoint note additionally inherits the separate R16 exclusions at distant and extreme-scale boundaries; those older global exclusions were not re-proved in this audit.

No mathematical correction to the tangent reduction, analytic enclosures, or uniform-neighborhood argument was needed.
