# Counterexample derivation for mass-critical pure BNLS

Working equation: i u_t = Delta^2 u - |u|^(8/N) u on R^N.
Energy E = (1/2)||Delta u||_2^2 - (1/(p+2))||u||_(p+2)^(p+2), p=8/N.
Momentum P = Im integral conjugate(u) grad(u); mass M=||u||_2^2.

Status: No rigorous counterexample or complete proof for the requested N>=2 problem was obtained. An independently cross-checked **numerical candidate for a negative-energy traveling wave in N=1** was found. This does not solve the N>=2 problem and is not yet a certified real-line solution. Details and reproducible scripts follow.

## 1. Exact analytical exclusions and identities

### Standing waves

For u(t,x)=exp(i omega t)Q(x), the profile equation is
Delta^2 Q + omega Q - |Q|^p Q = 0.
For sufficiently decaying finite-energy critical points, apply the mass-preserving dilation Q_lambda(x)=lambda^(N/2)Q(lambda x) to the action S=E+omega M/2. Since E(Q_lambda)=lambda^4 E(Q), stationarity gives 4E(Q)=0. Thus every such standing wave, including excited states, has E=0. It is not a negative-energy counterexample.

This argument also applies to stationary rotating profiles: the angular-momentum term is invariant under this dilation, so E=0.

### Traveling waves

For u(t,x)=exp(i omega t)Q(x-vt), the equation is
Delta^2 Q + omega Q + i v dot grad Q - |Q|^p Q = 0.
Its action is S_v=E+omega M/2-v dot P/2. Dilation yields

**E(Q) = (v dot P(Q))/8.**

Therefore a counterexample could arise from a traveling wave whose momentum points against its velocity. The identity is not a positivity theorem.

A phase-modulation variation Q -> exp(i a dot x)Q gives
v M = 4 integral xi |xi|^2 |Qhat(xi)|^2 dxi.
This fixes a third Fourier moment, not the first moment P. The implication v dot P>=0 does not follow for arbitrary profiles.

For quotient-minimizing traveling ground states, positivity does follow by reflection/conjugation: the quotient numerator is ||Delta Q||^2+omega M-v dot P, and Qbar has the same nonlinear denominator and the opposite P. A minimizer cannot have v dot P<0 because conjugation would lower its quotient. Hence the elementary counterexample search must leave the ground-state branch.

### Small-velocity excited-state test

Let Q be a real stationary profile, L_- = Delta^2 + omega - |Q|^p, and assume the symmetry-restricted inverse and local traveling branch exist. For v in the x_1 direction,
Q_v = Q - i v W + O(v^2),  L_- W = partial_1 Q.
Then
P_1(Q_v) = 2v <L_-^{-1} partial_1 Q, partial_1 Q> + O(v^3),
E(Q_v) = (v^2/4) <L_-^{-1} partial_1 Q, partial_1 Q> + O(v^4).

Thus a rigorously negative quadratic form, nondegeneracy, and a certified implicit-function construction would give a counterexample. These hypotheses must not be silently assumed. Ground states have a nonnegative imaginary Hessian, whereas excited profiles can have negative directions.

### Ordinary boosts do not generate solutions

Pure BNLS is not Galilean invariant. Multiplying an arbitrary standing profile by exp(i k dot x) and translating it does not preserve the equation, because fourth-order differentiation generates third- and second-order terms that cannot be canceled by only velocity/frequency changes. Therefore a formal NLS boost is not a counterexample construction.

### Time reversal

For this convention, u_rev(t,x)=conjugate(u(-t,x)) solves the same equation and has the same energy. u(-t,x) without conjugation does not solve the same signed equation. Any proved forward negative-energy theorem would transfer to backward time by conjugate time reversal.

### Other invalid counterexamples

Nonzero constant waves/plane waves on R^N are not L^2. A 1D localized wave extended constantly in transverse dimensions is not L^2(R^N). Negative-energy stable states for mixed-dispersion models do not answer the pure Delta^2 problem. Translating a radial solution only produces a solution radial about another center, not a genuinely general nonradial construction.

## 2. Numerical 1D candidate, not a proof

We solved Q''''+Q-Q^9=0 for real even multipulse standing profiles. Seed bumps came from the mass-critical 1D ground state (mass approximately 2.9867929783). The same-sign pulse train has equilibrium separation about 4.75. We independently solved the odd linear equation W''''+(1-Q^8)W=Q'.

Approximate form I = integral W Q' over the real line:

| Main pulses | Approximate mass | I |
|---:|---:|---:|
| 2 | 6.29055631 | 0.56986737 |
| 3 | 9.59514930 | 0.52181709 |
| 4 | 12.89974411 | 0.47288353 |
| 5 | 16.20433894 | 0.42398146 |
| 8 | 26.11812340 | 0.27727182 |
| 10 | 32.72731304 | 0.17946547 |
| 12 | 39.33650268 | 0.08165922 |
| 14 | 45.94569233 | -0.01614685 |

The n=14 negative value was checked with an independent linear BVP on [0,80], even standing-wave and odd W symmetry. Tolerance 1e-10 gave I=-0.01614724388746. The standing solution used 36,400 adaptive mesh nodes; the linear solve used 51,501 nodes. FFT/GMRES and BVP signs agree.

We then directly solved the full complex traveling profile, Q=a+ib,
a''''=( (a^2+b^2)^4 -1 )a + v b',
b''''=( (a^2+b^2)^4 -1 )b - v a',
with a even and b odd. The initial guess was Q - i v W, but the converged profile satisfies the full nonlinear equation on the numerical interval.

| v | P | E, direct quadrature | v P/8 | E-vP/8 |
|---:|---:|---:|---:|---:|
| 0.005 | -0.0001646156769 | -1.0288492902e-7 | -1.0288479803e-7 | -1.31e-13 |
| 0.010 | -0.0003480934486 | -4.3511699488e-7 | -4.3511681079e-7 | -1.84e-13 |
| 0.020 | -0.0008471637507 | -2.1179095757e-6 | -2.1179093767e-6 | -1.99e-13 |

All three complex BVP solves converged at relative residual tolerance 2e-10, approximately 36,000 adaptive nodes. The negative energy is therefore not merely inferred from a possibly ill-conditioned linear solve; it also occurs in a nonlinear profile with the exact critical Pohozaev relation matching numerically.

**Limits:** Floating-point BVP residuals are not rigorous error enclosures. Conditions at r=80 set profile and first derivative to zero rather than certify the exact infinite-domain stable manifold. The finite-interval solution is not automatically an exact H^2(R) solution. A rigorous real-line existence certificate and strict energy enclosure are still required. The requested N>=2 theorem is not falsified by this N=1 computation.

Reproducible scripts:
- travel_probe.py: first spectral ground/profile exploration (many failed roots are retained as failed runs).
- travel_bvp_probe.py: 3-5 pulse BVP exploration.
- travel_many_probe2.py: 8-14 pulse continuation seeds with corrected spacing.
- travel_negative_verify.py: independent high-accuracy real/linear/complex BVP checks.
- negative_travel_results.json: high-accuracy candidate measurements.
- negative_travel_1d_0.005.npz, negative_travel_1d_0.01.npz, negative_travel_1d_0.02.npz: sampled profiles.

## 3. Tests in N=2

For radial Q, we used variables (Q,Q',Z,Z') with Z=Delta_N Q. The singular BVP formulation is
Y'=[Q',Z,Z',|Q|^p Q-Q] + S Y/r,
S_11=S_33=-(N-1), p=8/N,
with Q'(0)=Z'(0)=0 and Q(R)=Q'(R)=0.

For the l=1 response write W(r,theta)=r V(r) cos(theta). The identity Delta_l=1(r V)=r Delta_(N+2)V reduces the inverse problem to
Delta_(N+2)^2 V+(1-|Q|^p)V=Q'/r,
and the sign of the Cartesian response is the sign of integral Q' V r^N dr.

The N=2 radial ground profile had mass approximately 13.14308374 and positive I approximately 2.28510671. Direct radial ring/train seeds did not converge to excited profiles. Dimension continuation from the 1D 14-pulse profile stalled around d=1.055 despite reducing steps; this may be a fold or a numerical obstruction and does not establish nonexistence. It did not reach N=2.

Separately, Fourier Newton solves for genuine nonradial N=2 collinear multipulse standing profiles, p=4, gave:

| Bumps | Approximate mass | I in the train direction |
|---:|---:|---:|
| 2 | 26.88814641 | 2.62204514 |
| 3 | 40.62919467 | 2.98723503 |
| 4 | 54.37028081 | 3.35217843 |

These signs are positive. Discrete nonlinear residuals ranged from 4.4e-11 to 2.2e-9; they are exploratory finite-box calculations, not existence certificates. Hence the 1D mechanism has not transferred to this tested N=2 family. Scripts: radial_travel_probe.py, radial_dimension_continue.py, travel2d_probe.py.

## 4. Localization obstruction worth keeping explicit

No radial tail inequality of the form
integral_|x|>R |u|^(p+2) <= C R^(-alpha) F(||u||_2,||Delta u||_2), alpha>0,
can hold uniformly for all nonradial H^2 functions with translation-invariant F: translate a fixed compactly supported nonzero bump beyond R while keeping both norms unchanged. Optimizing a single center removes this one-bump example, but two separated bumps show why a one-center estimate still requires genuine concentration information. This is an obstruction to an argument, not a counterexample to the evolution conjecture.

## 5. Primary sources checked

- Bugiera, Lenzmann, Schikorra, Sok, "On symmetry of traveling solitary waves for dispersion generalized NLS", Nonlinearity 33 (2020), 2797-2819, arXiv:1908.06771. https://arxiv.org/abs/1908.06771 . Source establishes that traveling-wave symmetry questions genuinely include biharmonic dispersion; the identities and calculations above were independently derived.
- Meta research page, Leonard Dinh, "Finite-Time Blow-Up of Radial Negative-Energy Solutions for the Mass-Critical Biharmonic Nonlinear Schrödinger Equation", dated October 2, 2026. https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/ . Its stated theorem covers N>=2 radial data and explicitly both time directions.
- Iyer, Parker, Stefanov, "Existence and Stability for Traveling Waves of Fourth-Order Semilinear Wave and Schrödinger Equations", Studies in Applied Mathematics 156 (2026), e70214, arXiv:2512.12390. https://arxiv.org/abs/2512.12390 . Checked to avoid false relevance: its Schrödinger application concerns mixed-dispersion standing profiles and a cubic example, not a mass-critical pure-BNLS negative-energy counterexample.
- Van Duong Dinh, "Non-radial finite time blow-up for the fourth-order nonlinear Schrödinger equations", Applied Mathematics Letters 132 (2022), 108084. DOI 10.1016/j.aml.2022.108084. Its nonlinearity is inhomogeneous |x|^-2 |u|^(4/N)u, so it cannot be substituted for the homogeneous target.

These notes contain verified algebra, failed/successful numerical searches, and explicit remaining proof obligations. They do not assert that the main problem has been solved or that the numerical candidate is original.

## 6. Final bounded-search update and discretization details

The square-array N=2 search finished. A 2x2 array converged with mass 55.31840873 and positive I=5.76374029; a 3x3 array converged with mass 126.92214806 and positive I=9.95284499. Their preconditioned nonlinear residual suprema were 6.79e-12 and 1.61e-9. A 4x4 seed did not converge. No negative N=2 quadratic form was found in this bounded search.

1D high-accuracy BVP: half-domain [0,80], real standing even boundary conditions Q'(0)=Q'''(0)=0, Q(80)=Q'(80)=0; linear odd boundary conditions W(0)=W''(0)=0, W(80)=W'(80)=0. The complex traveling conditions impose a'(0)=a'''(0)=b(0)=b''(0)=0 and a(80)=a'(80)=b(80)=b'(80)=0. Final quadrature/profile storage uses 16001 equally spaced points on [0,80]; the adaptive collocation mesh is denser where needed.

2D collinear FFT exploration: periodic rectangle 48x32, grid 256x128, nonlinear preconditioned residual tolerance 2e-8, linear GMRES relative tolerance 1e-7. Square-array exploration: periodic square 48x48, grid 256x256, same solver tolerances. These grids are exploratory and not claimed as convergence studies. [travel2d_results.json](../../computations/excited-waves/round1_archive/numerical/travel2d_results.json) additionally records unpreconditioned elliptic residuals and standing energy; nonzero finite-box energy is a discretization diagnostic, not a PDE counterexample.

All started computational processes completed. Search is frozen at the reported results; no background research process remains.
