# Derivation of the moment-free bordered reduction

Reviewed: the latest version of [robust-gap.md](robust-gap.md), headed “Robust profile gap from a moment-free bordered reduction”, on 2026-10-18. This review addresses the proof itself, not priority relative to R9 or external literature.

**Conclusion.** Subject to the explicitly stated, previously established normalized-optimizer compactness and phase-coercivity foundations, the proof of

$$
 |E(U)|\le C\|a(D)U+\omega U+i v\cdot\nabla U-|U|^{p-2}U\|_{H^{-s}}
$$

for normalized nearcritical negative-energy states is closed by the bordered construction. I found no circular use of dilation differentiability. No extra real-sector nondegeneracy or weighted regularity is required. The functional-analytic details below make the two implicit claims explicit.

## Nonlinearity is C1 for the complete stated exponent range

Let $s=m/2>0$, $p=2+2m/N>2$. If $m<N$,

$$
 p=2+2m/N<\frac{2N}{N-m}.
$$

If $m=N$, every finite p is admissible; if $m>N$, Hs embeds into L-infinity and hence into every finite Lp above 2. Thus in every stated case Hs embeds continuously into Lp, locally compactly into Lp on bounded spatial sets.

The real Nemytskii map

$$
 u\mapsto |u|^{p-2}u:L^p(\mathbb R^N;\mathbb C)\longrightarrow L^{p'}(\mathbb R^N;\mathbb C)
$$

is C1 for every p>2. Its real derivative is

$$
 DN(u)h=|u|^{p-2}h+(p-2)|u|^{p-4}u\,\operatorname{Re}(\overline u h),
$$

with value zero at u=0, and pointwise norm at most $(p-1)|u|^{p-2}|h|$. Hölder gives the Lp-to-Lp' derivative bound and continuity. Dual Sobolev embedding supplies Lp' into H^-s. Consequently F is C1 from Hs times the finite-dimensional parameter space to H^-s, even when p is nonintegral or lies between 2 and 3.

The velocity term is bounded Hs to H^-s because $2s=m>1$: its Fourier multiplier has order one strictly below m. No derivative of U beyond Hs is used here.

## Relative compactness and finite-dimensional kernel

The real scalar potentials are multiples of $W=|Q|^{p-2}$, with

$$
 W\in L^{p/(p-2)}.
$$

Hölder gives

$$
 |\langle f,Wg\rangle|\le\|W\|_{p/(p-2)}\|f\|_p\|g\|_p
 \le C\|W\|_{p/(p-2)}\|f\|_{H^s}\|g\|_{H^s}.
$$

Approximate W in that Lebesgue norm by bounded compactly supported functions. Each resulting multiplication operator is compact Hs to H^-s: a weakly convergent bounded Hs sequence converges strongly in L2 on the compact support, and L2 embeds continuously in H^-s. The norm estimate passes compactness to W. Thus the real two-block L is a compact perturbation of the positive isomorphism a(D)+omega_c and is Fredholm of index zero.

Real selfadjointness identifies its range with the annihilator of K=ker L in H^-s. K is finite-dimensional. The border built from smooth compactly supported chi_j with an invertible pairing matrix on K is therefore an isomorphism exactly as claimed. One does not need a smooth or decaying basis of K.

## Why the scaling argument is not circular

At the regularized representative V, F(V)=-sum c_j chi_j. Critical homogeneity gives the exact distributional identity

$$
 F(T_\lambda V;\lambda^m\omega,\lambda^{m-1}v)
 =-\lambda^m\sum c_jT_\lambda\chi_j.
$$

For each lambda near one, (T_lambda V,c) therefore solves the bordered equations with the stated parameters. Initially T_lambda V is only strongly continuous in Hs, a standard property of the dilation group. This suffices to ensure that it remains in the local uniqueness neighborhood for lambda sufficiently close to one; a common interval over all V is not needed to compute the derivative at lambda=1.

The border parameter

$$
 z_j(\lambda)=\langle V,T_\lambda^{-1}\chi_j\rangle-\langle Q,\chi_j\rangle
$$

is C1 because $T_\lambda^{-1}\chi_j$ is C1 in L2. Its derivative is bounded by a constant times $\|V\|_2$. The source parameter

$$
 g(\lambda)=\sum c_j(\chi_j-\lambda^mT_\lambda\chi_j)
$$

is C1 in H^-s, with derivative bounded by a constant times |c|. The frequency and velocity parameters are ordinary differentiable scalar functions.

The IFT solution map is C1 in all these parameters. Its unique solution must equal (T_lambda V,c). Thus the latter curve is C1 into Hs, proving Lambda V belongs to Hs. In a sufficiently small chart the derivative of the IFT solution map is uniformly bounded, so

$$
 \|\Lambda V\|_{H^s}\le C(\|V\|_2+|c|+|\omega|+|v|).
$$

The right side is uniformly bounded by the already established parameter control. This establishes the required uniform estimate without any prior moment of V or U.

## Checks on the remaining steps

- The parameter map (alpha,b) -> alpha Q+i b.grad Q is injective in H^-s. A nonzero L2 function cannot be constant along a nonzero spatial direction. The h-dependent terms containing unbounded omega or v are absorbed by the small chart radius before any boundedness of those parameters is assumed.
- The finite chart cover is taken after removing phase and translation, which preserve the residual norm. It does not require a common kernel dimension for different optimizers: each chart uses its own finite border.
- A small constant phase rotation of V makes Im V orthogonal to Q. Although its residual no longer lies in the original span of the chi_j, only its norm and the already established dilation bound are used after this point; both survive phase rotation.
- The identities $\langle Y,B_VY\rangle=v\cdot P/2+\langle Y,f_I\rangle$ and $mE-v\cdot P/2=\operatorname{Re}\langle f,\Lambda V\rangle$ have the signs and factors consistent with the stated action and momentum convention.
- Young's inequality gives an error O(rho+rho^2), which is O(rho) in the small-residual regime. Local Lipschitz continuity of E then transfers the inequality from V to U.
- The rescaled residual norm in equation (9) has the correct power: the normalized residual H^-s norm equals $A^{-1}\big[\int|\widehat R|^2/(1+a/A)\big]^{1/2}$, while the normalized energy is E/A.
- The amplitude perturbation used for optimality of the linear exponent does have both negative energy and residual of first order in epsilon after kinetic normalization.

## Interpretation

This is a robust functional obstruction to nearcritical negative-energy pseudoprofiles, not a lifetime estimate. The proof does not settle recurrence, finite-time blowup, arbitrary bounded trajectories, or the minimum traveling-wave mass endpoint. The separate comparison with R9 has now been completed in [robust-gap.md](robust-gap.md): the new estimate removes its dilation-defect hypothesis, with a linear energy exponent instead of the stronger square-root exponent on R9's narrower class.
