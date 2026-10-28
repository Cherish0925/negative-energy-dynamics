# Round 10 Proof details and a nonlocal extension

## 1. derivation of the round 9 core

I independently checked [foundations.tex](../../manuscripts/dilation-structure/foundations.tex), [cone-section.tex](../../manuscripts/dilation-structure/cone-section.tex), [bounded-boundary-section.tex](../../manuscripts/dilation-structure/bounded-boundary-section.tex), and [relative-section.tex](../../manuscripts/dilation-structure/relative-section.tex). No fatal mathematical gap was found in the statements as written.

* Constant phase of optimizers does not use a modulus inequality for the higher-order kinetic form. Real-evenness gives kinetic splitting, and the sharp inequality plus strict triangle equality forces a constant phase. This is valid.
* The phase-kernel argument correctly handles powers below two in its second remainder. The zero-set convention is essential. The final use of the linearity of the form kernel, applying the squared-modulus conclusion also to `b+Q`, genuinely removes spatially varying signs.
* The full dispersion cone permits an unbounded dilation defect `D_b` along a sequence. The shifted-frequency identity retains its coefficient `1/2-M(Y)/M`, so there is no hidden uniform-derivative assumption. Estimating the actual frequency before shifting would have been incorrect, but the final proof does not do that.
* The small bounded-order perturbation counterexample uses coercivity only below `(1+epsilon)^(N/m) M_c`. Its strict binding proof handles submasses below `M_c` by their zero infimum. The real-minimizer argument uses convexity, not a nonexistent higher-order diamagnetic inequality. The stated threshold and exact negative-energy identity are consistent.
* The residual inertia estimate genuinely allows arbitrary frequency and velocity: the large-residual regime absorbs both via the parameter-injectivity bound. Its moving-center periodic consequence is an integrated kinematic restriction, not a Lyapunov estimate. The manuscript correctly does not infer general blowup from it.

Two scope boundaries are mathematically essential:

1. Real-evenness is what makes the imaginary equation a coercive scalar phase equation. A general real but non-even dispersion need not share that structure; a mere small odd perturbation is not covered by the same argument.
2. Positive residual speed cannot by itself rule out a bounded Hamiltonian orbit. A circular orbit is the finite-dimensional illustration. Any claimed general dynamical closure needs a further spacetime monotonicity or compact-rigidity statement.

## 2. A substantive extension: nonlocal density interactions

The phase-coercivity argument is not limited to a local power. For a mass-critical Hartree interaction the replacement is a positive-definite Hilbert geometry of the density. This supplies a clean generalization to nonlocal attraction without assuming positivity of the ground state or nondegeneracy of its real-part linearization.

### Setting

Let `1<m<N`, `s=m/2`, and let `a` have the same real-even, positive elliptic, homogeneous order-`m` hypotheses as in round 9. Let

`K(x)=|x|^{-m}`,

or more generally let `K` be real, even, `C^1` away from zero, homogeneous of degree `-m`, with

`|K(x)|+|x||grad K(x)| <= C |x|^{-m}`,

and with a strictly positive Fourier density almost everywhere. The latter means that the form

`D(f,g)=integral integral K(x-y) f(x) g(y) dx dy`

is a positive-definite real inner product on its finite-energy domain of real densities. A concrete anisotropic class is positive sums of `|B_j x|^{-m}` with invertible real matrices `B_j`.

Define

`H(u)=D(|u|^2,|u|^2)`, `A(u)=integral a |uhat|^2`, `M(u)=||u||_2^2`,

`E(u)=A(u)/2-H(u)/4`.

Hardy--Littlewood--Sobolev and interpolation yield `H(u)<=C M(u) A(u)`. Write its sharp constant as `2/M_c`:

`H(u) <= (2/M_c) M(u) A(u)`.

The relevant equation is

`i u_t = a(D)u - (K*|u|^2)u`,

and the profile equation is

`a(D)U + omega U + i v.grad U - (K*|U|^2)U=0`.

### Theorem H (pure Hartree profile gap)

There exists `delta>0`, depending only on the fixed `N,m,a,K`, such that every nonzero weak `H^s` traveling profile with `E(U)<0` has

`M(U) >= M_c + delta`.

No radial symmetry, spatial moment, uniqueness, positivity, or real-sector nondegeneracy of a ground state is assumed.

### H.1. Compactness of sharp maximizers

Put `q=4N/(2N-m)`, which lies strictly between `2` and the `H^s` Sobolev exponent `2N/(N-m)`. HLS gives

`|D(f,g)| <= C ||f||_{q/2} ||g||_{q/2}`.

Normalize a maximizing sequence by `M(u_n)=M_c`, `A(u_n)=1`, so `H(u_n)->2`. Local vanishing in mass would force `||u_n||_q->0` by the standard bounded-overlap localization argument, contradicting the Hartree norm. After translations obtain a nonzero weak limit `Q` in `H^s` and local strong convergence in `L^q`. Set `r_n=u_n-Q`.

The product `Q r_n` tends to zero in `L^{q/2}`: use local strong convergence and then the small `L^q` tail of `Q`. Hence the squared densities split up to an error tending to zero in `L^{q/2}`. In addition,

`D(|Q|^2,|r_n|^2)->0`.

To prove the last claim first approximate `Q` in `L^q` by a bounded compactly supported function. For that approximation the potential is bounded, tends to zero at infinity, and multiplication by it is compact as a form `H^s -> H^{-s}`. HLS controls the approximation error. Consequently

`H(u_n)=H(Q)+H(r_n)+o(1)`.

With `M(Q)=M_1>0`, `A(Q)=A_1`, and residual limiting mass and kinetic energy `M_2,A_2`, sharp GN gives

`M_c <= M_1 A_1 + M_2 A_2`, `A_1+A_2=1`, `M_1+M_2=M_c`.

This is impossible when both masses are positive. Thus `M_1=M_c`, `A_1=1`, and convergence is strong. The argument also proves attainment and compactness of normalized optimizers modulo translation and phase.

### H.2. Constant phase from density geometry

For `u=X+iY`, real-evenness gives `M(u)=M(X)+M(Y)` and `A(u)=A(X)+A(Y)`. The positive-definite density form gives

`sqrt H(u)=||X^2+Y^2||_D <= sqrt H(X)+sqrt H(Y)`.

Using the sharp inequality on both real components and then two-term Cauchy--Schwarz,

`sqrt H(u) <= sqrt(2/M_c)[sqrt(M(X)A(X))+sqrt(M(Y)A(Y))] <= sqrt((2/M_c)M(u)A(u))`.

An optimizer has equality everywhere. Equality in the first triangle inequality, combined with strict positive definiteness, gives `Y^2=c X^2`. Apply the same conclusion after multiplication by `exp(i pi/4)`. Exactly as for the local-power proof, both relative signs cannot occur on sets of positive measure. Every optimizer has constant complex phase and can be taken real.

A real normalized optimizer satisfies

`a(D)Q + omega_* Q - (K*Q^2)Q=0`, `omega_*=1/M_c`.

### H.3. Strict phase coercivity without a maximum principle

Take a real optimizer with `M=M(Q)=M_c`, allowing arbitrary kinetic normalization `A=A(Q)>0`, and let `C_*=2/M_c`. Then `H(Q)=C_* M A` and `omega_*=A/M` in the corresponding normalization. Define

`L_-=a(D)+A/M-K*Q^2`.

For real `b`, let `B=M(b)` and `C=A(b)`. Applying the sharp inequality to `Q+i sqrt(t)b` gives the exact polynomial comparison

`H(Q)+2t D(Q^2,b^2)+t^2 H(b) <= C_* (M+tB)(A+tC)`.

The derivative at zero proves `L_->=0`. If `b` belongs to the form kernel, then

`2 D(Q^2,b^2)=C_* (MC+AB)`.

Cauchy--Schwarz in the density Hilbert space and the sharp inequality for `b` now give

`[C_* (MC+AB)/2]^2 <= H(Q) H(b) <= C_*^2 M A B C`.

Therefore `(MC-AB)^2<=0`, forcing equality throughout. Strict positive definiteness of `D` gives

`b^2=(B/M)Q^2`.

The kernel is a real linear space containing `Q`. Applying this result to `b+Q` shows that `b` is a constant real multiple of `Q`. Thus

`ker_R L_-=span_R{Q}`.

Multiplication by `K*Q^2` is a compact form by the approximation argument in H.1. The coercive free part `a(D)+A/M` then yields

`<b,L_- b> >= c_Q ||b||_{H^s}^2` when `<b,Q>=0`.

The normalized optimizer compactness gives a uniform coercivity constant over that entire set.

This proof is the decisive extension: the phase kernel comes from equality in a density interaction Cauchy--Schwarz inequality. It does not import a positivity-preserving resolvent that fails for higher-order dispersion.

### H.4. Regularity and virial identities for weak profiles

A fixed-profile shifted resolvent `(a(D)+i v.grad+Lambda)^{-1}` maps `L^p` to `H^{m,p}` by the same Mihlin argument as round 9. Weak `H^s` gives `U` in `L^{2N/(N-m)}` and `L^2`.

Split `K=K_near+K_far`, with the near part supported on a bounded ball. Then `K_far*|U|^2` is bounded because `K_far` is bounded and `U` is in `L^2`. The near kernel belongs to every `L^j`, `1<=j<N/m`. Since `|U|^2` belongs to `L^{N/(N-m)}`, Young's inequality shows that the near potential belongs to arbitrarily large finite `L^t` spaces. Choose a fixed `t>N/m` sufficiently large. If `U` belongs to `L^q`, the product of the near potential and `U` belongs to `L^p`, where `1/p=1/t+1/q`; the resolvent and Sobolev embedding improve the reciprocal exponent by `m/N-1/t>0`. Starting at the energy Sobolev exponent, finitely many iterations yield `U` bounded; endpoint exponents may be weakened slightly. Linear and bounded-potential terms improve at least as strongly.

Now `K*|U|^2` is bounded, since the near kernel is integrable and `U` bounded; the equation gives `U` in `H^m`, hence in `H^1`. Also `grad |U|^2` lies in `L^1` and `L^2`. Convolving this derivative with the near/far decomposition shows `grad(K*|U|^2)` belongs to `L^2+L^infty`. Thus `(K*|U|^2)U` belongs to `H^1`, and a final resolvent step gives `U` in `H^{m+1}`.

For the cutoff dilation `L_R=f_R.grad+(div f_R)/2`, the Hartree pairing is

`Re integral (K*rho)U overline(L_R U) = -1/4 integral integral rho(x)rho(y) [f_R(x)-f_R(y)].grad K(x-y)`.

The functions `f_R(x)=x chi(x/R)` have a uniform Lipschitz constant. The integrand is therefore dominated by `C rho(x)rho(y)|x-y|^{-m}`, which is integrable by HLS. Homogeneity gives the limiting pairing `m H(U)/4`. Combined with the already proved kinetic/drift commutator limits, this proves

`v.P(U)=2mE(U)`.

Testing the profile against `U` gives the frequency identity

`omega M(U)=A(U)+(2m-4)E(U)`.

Finally, writing `U=X+iY`, the imaginary equation and momentum formula give

`mE(U)=<Y,[a(D)+omega-K*|U|^2]Y>`.

### H.5. Proof of the mass gap

Suppose negative-energy profiles have masses tending to `M_c`. Normalize by mass-preserving dilation so `A(U_n)=1`. The sharp inequality forces `H(U_n)->2` and `E(U_n)->0`. By H.1--H.2, translation and phase give `U_n->Q` strongly in `H^s`, with `Q` real. A further phase makes `Y_n=Im U_n` orthogonal to `Q`. The frequency identity gives `omega_n->1/M_c`.

HLS implies convergence of `K*|U_n|^2` to `K*Q^2` in form norm. Strict phase coercivity now makes

`<Y_n,[a(D)+omega_n-K*|U_n|^2]Y_n> >= c ||Y_n||_{H^s}^2 >=0`.

This contradicts the exact identity `m E(U_n)` with `E(U_n)<0`. The theorem follows.

## 3. Further consequences and limits of this extension

* The quantitative residual-inertia theorem extends to this Hartree problem with the same proof: the map `u -> (K*|u|^2)u` is locally Lipschitz `H^s -> H^{-s}` by HLS, and all uses of the nonlinearity in the round 9 proof were form continuity, that Lipschitz estimate, and phase coercivity. The scale factor remains `A^{2/m-1}`.
* The same theorem also accommodates all admissible nonnegative subhomogeneous dispersion additions `b` from round 9, with one gap independent of `b`. Here `omega_tilde M=A+B+(2m-4)E` after shifting by `D_b/M`, and the exact phase identity becomes

  `mE=<Y,[a+omega_tilde-K*|U|^2]Y>+B_b(Y)+D_b(1/2-M(Y)/M)`.

  Near threshold, the last two terms are nonnegative and the first is coercive. The regularity argument uses the shifted resolvent for `a+b+i v.grad` and is unchanged. This is a proved corollary of the displayed argument, not merely an analogy.
* No assertion has been derived here for arbitrary non-even symbols, matrix-valued dispersions, or unrestricted coupled systems. In those cases the scalar real/imaginary decomposition or the one-dimensional phase kernel can fail.
* This is a new derivation in the current research record, not a certified literature-priority claim. It does not close the general bounded-trajectory problem for pure BNLS.

## 4. Primary-literature checks

Retrieved primary papers and their relevant scopes:

1. Cho--Hwang--Kwon--Lee, *On finite time blowup for mass-critical Hartree equations*, arXiv:1208.2302, version 3 (2014): https://arxiv.org/abs/1208.2302 . The full text was checked at https://arxiv.org/html/1208.2302v3 . Theorem 1.1 assumes radial data, high regularity and weighted derivatives for 1<=alpha<2, n>=4. Theorem 1.2 assumes the same kind of radial/weighted hypotheses for 2<alpha<1+n/2. In particular the high-order theorem does not cover all 1<m<N, anisotropic symbols, or general nonradial profiles. This is a dynamical radial blowup theorem, not the proposed uniform nonradial profile gap.
2. Lenzmann, *Uniqueness of Ground States for Pseudo-Relativistic Hartree Equations*, arXiv:0801.3976; https://msp.org/apde/2009/2-1/apde-v2-n1-p01-p.pdf . This is a central predecessor for Hartree ground-state nondegeneracy, but the quoted uniqueness is for a specific pseudorelativistic setting; it is not the above arbitrary real-even higher-order phase-kernel argument.
3. *Nondegeneracy of positive solutions for a biharmonic Hartree equation and its applications*, arXiv:2310.11056; published JDE 2025, https://www.sciencedirect.com/science/article/pii/S0022039625001433 . Its displayed exponent `(2N-alpha)/(N-4)` and absence of a positive frequency identify the energy-critical elliptic equation. Do not conflate that result with the frequency-bearing mass-critical Hartree optimizer studied here.
4. Gao--Wang, *Minimal mass non-scattering solutions of the focusing L2-critical Hartree equations with radial data*, DCDS 37 (2017), 1979--2007, https://www.aimsciences.org/article/doi/10.3934/dcds.2017084 . This proves a radial second-order minimal-mass classification in dimensions 3 and 4, showing the known connection between spectral information and dynamical rigidity but not supplying the general higher-order nonradial bridge.

The search did not establish priority for Theorem H. Any publication claim requires full comparison with the related Hartree variational and traveling-wave literature.

## 5. A cleaner common principle: convex density norms force a simple phase kernel

The second-order remainder proof in round 9 is valid, but it is not needed. Both the local-power and Hartree cases follow from a first-order equality argument, which avoids singular second derivatives at nodal sets.

### Abstract lemma

Let `A(u)` be a positive real-even quadratic form, with `A(X+iY)=A(X)+A(Y)`, and let `M(u)=||u||_2^2`. Let `B` be a strictly convex real normed space of densities for which `|u|^2` is admissible, and put

`F(u)=|| |u|^2 ||_B^kappa`, `kappa>1`.

Assume the sharp inequality

`F(u) <= kappa (M(u)/M_c)^(kappa-1) A(u)`

holds, has an optimizer `Q` with `M(Q)=M_c`, and the density functional `f(rho)=||rho||_B^kappa` is Gateaux differentiable at `rho=Q^2`. Its derivative is assumed representable by the phase potential:

`Df(Q^2)[h]=kappa <V_Q,h>`.

The same conclusion holds with the derivative understood as a bounded density functional, if a multiplication potential is not needed.

Then every optimizer is a constant phase times a real function. For a real optimizer define

`L_-=A_operator+(kappa-1)A(Q)/M_c-V_Q`.

Its real quadratic form is nonnegative, and its form kernel equals `span_R{Q}`.

### Proof

For `u=X+iY`, the density triangle inequality gives

`F(u)^(1/kappa) <= F(X)^(1/kappa)+F(Y)^(1/kappa)`.

Applying sharp GN on both components and then two-term Holder proves the same sharp upper bound in terms of `A(u),M(u)`. At an optimizer, equality in the strictly convex density norm forces `Y^2=cX^2`; rotating by `exp(i pi/4)` removes variable relative signs. This proves constant phase.

Now take a real optimizer `Q`, with `M=M_c` and `A=A(Q)`. Since `F(Q)=kappa A`, sharp GN applied to `Q+i sqrt(t)b` yields

`f(Q^2+t b^2) <= kappa (1+t B/M)^(kappa-1)(A+t C)`,

where `B=M(b)`, `C=A(b)`. Differentiating at zero shows

`<V_Q,b^2> <= C+(kappa-1)AB/M`.

Thus `L_->=0`, and the optimizer Euler--Lagrange equation puts `Q` in its form kernel.

If `b` is also in the form kernel, equality holds in that derivative bound. The supporting-functional inequality for a differentiable norm power gives

`Df(Q^2)[b^2] <= kappa f(Q^2)^((kappa-1)/kappa) f(b^2)^(1/kappa)`.

Use `f(Q^2)=kappa A` and sharp GN for `b`. On setting `x=C/A`, `y=B/M`, the kernel identity becomes

`x+(kappa-1)y <= kappa x^(1/kappa)y^((kappa-1)/kappa)`.

Weighted arithmetic--geometric mean gives the reverse inequality. Hence equality holds and `x=y`. Equality in the norm supporting-functional inequality, by strict convexity of `B`, implies

`b^2=y Q^2`.

Since the form kernel is linear and contains `Q`, apply this conclusion also to `b+Q`; subtraction gives `b=cQ` with one constant real `c`. This proves the lemma.

### What is actually unified

* Local critical power: `B=L^kappa`, `kappa=1+m/N`, and `F(u)=||u||_(2kappa)^(2kappa)`.
* Critical Hartree: `B` is the completion in the positive-definite interaction norm `||rho||_B^2=D(rho,rho)`, `kappa=2`.
* These are not identified by matching exponents. Their attraction depends on the same density variable through different strictly convex geometries. The phase-kernel simplicity is a consequence of sharp critical interpolation and equality in those geometries.

To turn the abstract phase lemma into a full traveling-wave gap theorem, additional analytic hypotheses are still required: compactness of normalized near-optimizers, continuity/compactness of the phase potential form, profile regularity, and a dilation identity at the critical spatial scaling. Those were proved above for the stated Hartree class and in round 9 for the local-power class. The abstract lemma alone does not supply these PDE facts.

## 6. Proof details of the round 10 dynamical core

Read [dynamic-core.md](dynamic-core.md) through its ballistic exterior-gradient section. The argument checks under the stated standard strong-H2 solution framework and integrated localized virial identity.

* The homogeneous interpolation exponents in all dimensions are correct. They turn gradient-tail control, full mass boundedness, and a global H2 bound into nonlinear-tail control without assuming an L2 tail.
* Negative energy and the same interpolation give a positive uniform gradient norm. H^{-2} Lipschitz time control interpolated against the uniform H2 bound yields H1 time Holder exponent 1/4. This suffices to regularize an arbitrary gradient-localizing center to a bounded-speed one at bounded displacement.
* The moving-center error uses the full mass only: Cauchy--Schwarz bounds it by the square root of the gradient tail times sqrt(M). No hidden mass tightness is used.
* The drift inequality sign is correct: integrating J_R'<=16E-2a'.P+errors gives P.(a(T)-a(0))/T<=8E+o(1).
* The averaged error power kappa=min(1/2,8/N) is correct. The lower bound on averaged D_R follows from concavity (Jensen) with the correct direction.
* In the ballistic extension, R=nu T is a fixed radius for each observation interval, not a radius varying inside the differentiated functional. Consequently no R' term is missing. The endpoint bound divided by T is O(nu), while the cutoff error tends to zero. Uniformity in the start time S follows from the global bounds.
* The stated exclusion of localization in a sublinear radius is valid about bounded-speed centers. It should not silently be enlarged to arbitrary centers under only growing-radius localization; the fixed-radius center-regularization proof does not directly give that enlargement.

This is a rigorous necessary escape alternative. It does not make the missing estimate on replenishment of exterior gradient energy, and therefore does not prove the general near-critical dynamical gap.
