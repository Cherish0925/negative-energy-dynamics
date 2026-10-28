# Fixed mass and momentum geometry near a critical ground wave

## Result

Let `a` be a positive, real-even, elliptic homogeneous dispersion of degree `m>2`, set `s=m/2`, `alpha=2m/N`, and

`E(u)=A(u)/2-||u||_(alpha+2)^(alpha+2)/(alpha+2)`,
`M(u)=||u||_2^2`, `P(u)=Im integral conjugate(u) grad u`.

Let `Q` be a real sharp ground profile solving `(a(D)+1)Q-|Q|^alpha Q=0`. Use the already proved phase coercivity: `L_-=a(D)+1-|Q|^alpha` has kernel `RQ` and is coercive from `H^s intersect Q-perp` to its dual. Define

`Z_j=L_-^{-1} partial_j Q`, `T_ij=<partial_i Q,Z_j>`.

Then `T` is strictly positive definite. Suppose exact profiles `U_n` satisfy

`(a(D)+1+i v_n.grad) U_n-|U_n|^alpha U_n=0`,
`v_n ->0`, `v_n !=0`, `U_n ->Q` strongly in `H^s`, after phase and translation.

For every sufficiently large `n`, there exists a continuous `H^s` curve `V_n(lambda)` through `U_n` that preserves **both the mass and every component of momentum exactly**, such that its scalar energy is `C^2` and

`dE(V_n)/dlambda(1)=0`,
`d^2E(V_n)/dlambda^2(1)=(2-m) v_n^T T v_n+o(|v_n|^2)<0`.

Thus every such nonzero-velocity wave is a strict energy maximum along one local curve of fixed mass and momentum. In particular it is not a constrained local energy minimum.

This statement assumes neither a differentiable profile branch, nor real-block nondegeneracy of `L_+`, nor membership of the profile in the domain of the dilation generator. It is a **variational theorem**, not by itself nonlinear orbital instability.

The same construction for `1<m<2` gives positive leading curvature along this particular curve, and gives no stability theorem. At `m=2` its leading coefficient vanishes.

## 1. The imaginary first-order response is forced by the profile equation

Write `U=X+iY`, and choose its phase so `<Y,Q>=0`. Strong `H^s` convergence gives `X->Q`, `Y->0`. The imaginary profile equation is

`L_- Y=-v.grad X+(|U|^alpha-|Q|^alpha)Y`.

The nonlinear potential on the right converges to zero as a quadratic form on `H^s`. Indeed `H^s` embeds into `L^p`, `p=alpha+2`, and Hölder together with continuity of `u -> |u|^alpha` in `L^(p/alpha)` gives the claim. Also `grad:H^s -> H^(-s)` is bounded because `m=2s>1`.

Projecting onto `Q-perp` and using phase coercivity first gives `||Y||_(H^s)=O(|v|)`. Applying the same inverse again gives

`Y=-sum_j v_j Z_j+o(|v|)` in `H^s`.

Only the real convergence `X->Q` is needed. There is no derivative or inverse of the real profile equation in this argument.

Momentum is continuous as a bilinear form on `H^s` for `m>1`, and the real/imaginary decomposition gives `P_j(U)=-2<Y,partial_j X>`. Consequently

`P(U)=2T v+o(|v|)`.

The sharp phase form makes `T` positive definite: a zero quadratic form would require a nonzero directional derivative of a nonzero `L^2` function to vanish.

## 2. Exact finite-dimensional correction of all conserved charges

Fix one profile `U` and define

`W(c)=(1+c_0)U+i sum_j c_j Z_j`, with real `c in R^(N+1)`.

At `c=0`, the Jacobian of `(M(W),P(W))` in these coordinates has blocks

`[[2M(U), O(|v|)], [2P(U), -2T+o(1)]]`.

It is invertible for every sufficiently small speed. The finite-dimensional implicit-function theorem supplies a smooth curve `c(lambda)`, `c(1)=0`, satisfying

`M(W(lambda))=M(U)`, `P(W(lambda))=P(U)/lambda`.

Differentiating at `lambda=1`, and writing `h=W'(1)`, gives

`c_j'(1)=v_j+o(|v|)`, `c_0'(1)=O(|v|^2)`,
`h=i sum_j v_j Z_j+o(|v|)` in `H^s`.

The sharper `O(|v|^2)` amplitude correction follows because `<U,iZ_j>=<Y,Z_j>=O(|v|)`, whereas the other coefficients are `O(|v|)`. An `o(|v|)` amplitude bound would already suffice for the result.

Now let

`V(lambda,x)=lambda^(N/2) W(lambda,lambda x)`.

Critical homogeneity gives

`M(V(lambda))=M(U)`, `P(V(lambda))=P(U)`,
`E(V(lambda))=lambda^m E(W(lambda))`.

The dilation group is strongly continuous in `H^s`, so `V` is a continuous energy-space curve. It is not claimed to be a differentiable `H^s` curve: that would require additional moments. Its **scalar energy** is nevertheless `C^2` by the exact last identity. This avoids an artificial localization or dilation-domain assumption.

## 3. Exact curvature identity

Let `L_U` be the real Hessian of `S=E+M/2-v.P/2` at the exact profile, and write `q_U(h)=<h,L_U h>` in quadratic-form notation. Since `S'(U)=0`,

`E'(W(lambda))|_1=-v.P(U)/2`,
`E''(W(lambda))|_1=q_U(h)+v.P(U)`.

Here `M(W(lambda))` is constant and `P(W(lambda))=P(U)/lambda`, whose first two derivatives are `-P(U)` and `2P(U)`.

The moment-free profile Pohozaev identity is `v.P=2mE`. Differentiating the exact scalar identity `E(V)=lambda^m E(W)` now yields

`E'(V)|_1=mE-v.P/2=0`,
`E''(V)|_1=q_U(h)-(m-1)v.P/2`.

The forms `q_U` converge to the standing form `q_Q` on bounded `H^s` sets. The nonlinearity has a continuous second Fréchet derivative as an energy functional because `p>2`; no differentiability of the profile branch is involved. At `Q`, real and imaginary blocks decouple, and

`q_Q(i sum v_j Z_j)=<sum v_j Z_j,L_- sum v_j Z_j>=v^T T v`.

Therefore

`q_U(h)=v^T T v+o(|v|^2)`,
`E''(V)|_1=(2-m)v^T T v+o(|v|^2)`.

The positive minimum eigenvalue of `T` makes the error uniform in the direction of `v`. For `m>2`, both sides of `lambda=1` contain exact charge-preserving perturbations with strictly smaller energy.

## 4. Why a linear phase boost alone is insufficient

A superficially simpler path is

`V_b(lambda,x)=exp(i(1-lambda) k.x) lambda^(N/2) U(lambda x)`,
`k=P(U)/M(U)`.

It also preserves mass and momentum exactly. Assuming `a` is `C^2` off zero with the expected homogeneous derivative bounds (automatic integrability here for `m>2`), define

`H_U=integral D^2 a(xi) |Uhat(xi)|^2 dxi`.

Its energy curvature is exactly

`E''(V_b)|_1=1/2 [k^T H_U k-(m-1)v.P]`.

To derive it, write the kinetic energy as

`A(V_b(lambda))=integral a(k+lambda(xi-k)) |Uhat(xi)|^2 dxi`.

Euler identities give `D^2a(xi)xi=(m-1)grad a(xi)` and `xi.D^2a(xi)xi=m(m-1)a(xi)`. The boost identity for the exact profile is `integral grad a |Uhat|^2=vM`. Combining these with `v.P=2mE` proves the displayed curvature.

For the quartic isotropic symbol, this becomes

`E''(V_b)|_1=4 integral(k.xi)^2 |Uhat|^2 +2|k|^2 integral |xi|^2 |Uhat|^2 -(3/2)v.P`.

Near `Q`,

`E''(V_b)|_1=(2/M(Q)^2) v^T T H_Q T v -(m-1)v^T T v+o(|v|^2)`.

The phase coercivity `T>0` does not determine this sign. If the moments needed for `x_jQ` are available, the elementary weighted Cauchy inequality gives only

`H_Q >= (M(Q)^2/2) T^{-1}`,

which is a **lower** bound. It cannot imply the needed negative sign. One must not replace this inequality by an upper bound.

The optimal imaginary correction instead minimizes `<psi,L_-psi>` subject to the first-order momentum requirement `-2<partial_jQ,psi>=-P_j`. Its value is

`P^T T^{-1}P/4`, attained by `psi=(1/2) sum_j (T^{-1}P)_j Z_j`.

This is exactly the correction realized to leading order in Sections 2--3. The factor `2-m` results from balancing the least energy cost of momentum compensation against the critical dilation curvature.

## 5. The exact dynamical limitation

Energy saddles need not be dynamically unstable in a Hamiltonian system: gyroscopic effects, additional neutral modes, and negative-energy imaginary modes can matter. A construction of lower-energy data at identical charges is not a proof that the corresponding solution leaves an orbit.

For variational boosted ground waves, the action has Morse index one. Combining that fact with this constrained energy direction is promising, but an unconditional conclusion requires controlling the generalized zero eigenspace or proving the relevant nonlinear argument directly. Real-block nondegeneracy cannot simply be erased from a spectral theorem without replacing its role. No such erasure is claimed here.

The energetic result is new to this round of the project. It is independent of the conditional round 11 spectral reduction: it applies to every converging sequence of exact waves, even if a smooth local profile branch is unavailable. It does not establish a publication-priority claim.

## Independent check

## 6. Uniform consequence for every sufficiently slow action ground wave

This is an existence and compactness corollary, eliminating the supplied-sequence hypothesis for ground waves. Define `K_v=A+M-v.P` and `kappa_v=inf K_v/||u||_p^2`, `p=2+2m/N`. For all sufficiently small speeds, Fourier Hölder gives `|P|<=C A^(1/m)M^(1-1/m)<=C'(A+M)`, so `K_v` is coercive.

A minimizing sequence normalized by `||u||_p=1` is bounded in `H^s`. Nonvanishing and translation yield a nonzero weak limit. Local compactness, Brezis--Lieb, and Hilbert norm splitting imply `kappa_v >= kappa_v[c^(2/p)+(1-c)^(2/p)]` for the limit's `p`-norm mass `c>0`. Since `2/p<1`, this forces `c=1`; coercivity gives strong convergence and attainment. Amplitude-normalize the minimizer to `K_v(U)=||U||_p^p`. Its Euler equation is the frequency-one profile equation, and `K_v(U)=||U||_p^p=kappa_v^(p/(p-2))`. These are precisely action ground waves on the Nehari manifold.

Now `kappa_v -> kappa_0`. Any sequence of such ground waves with `v->0` becomes a minimizing sequence for `K_0/||u||_p^2`, hence is strongly precompact in `H^s` modulo translations and phase. Its limiting frequency-one optimizer is a sharp mass-critical optimizer. To see the latter identification directly, write `r=m/N` and use the sharp inequality `||u||_p^p<=C_* M^r A`. At fixed `A+M`, `M^r A` has its unique maximum at `M=r A`. A sharp critical optimizer can be dilated to attain that ratio, proving equality of the two sharp minimization problems. Conversely any optimizer of `K_0/||u||_p^2` must attain both inequalities. Nehari normalization then forces `M=Mc`; the density rigidity theorem makes it real after a constant phase.

Therefore the sequential theorem above implies: **for m>2, every action ground wave at every sufficiently small nonzero velocity is a strict energy maximum along a local curve of precisely fixed mass and momentum**. If no uniform velocity neighborhood existed, a failing sequence would converge to a real optimizer and contradict the already proved curvature formula. This assertion needs neither ground-state uniqueness, branch existence, nor real-profile nondegeneracy. It remains variational, not a nonlinear instability theorem.
