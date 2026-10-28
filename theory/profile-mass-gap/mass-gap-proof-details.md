# Proof details: a uniform mass gap for negative-energy traveling waves

Date: 7 October 2026. These proof details establish the proposed analytic theorem independently of the earlier interval computations. The argument is valid in every dimension N≥1 once the elementary optimizer and phase-kernel lemmas below are included. It does not require uniqueness of the optimizer, nondegeneracy of L+, radiality of the traveling profile, finite variance, or a bounded frequency/speed parameter range.

## 1. Precise conclusion and quantifiers

Let α=8/N, p=α+2, and

$$
 E(u)=\tfrac12\|\Delta u\|_2^2-\tfrac1p\|u\|_p^p,
 \qquad M(u)=\|u\|_2^2.
$$

Let Mc be the sharp GN threshold, defined by

$$
 \|u\|_p^p\le\frac p2(M(u)/M_c)^{\alpha/2}\|\Delta u\|_2^2.
$$

Then there exists δN>0 such that every nonzero weak H² profile satisfying

$$
 \Delta^2U+\omega U+i v\cdot\nabla U-|U|^\alpha U=0,
 \quad \omega\in\mathbb R,
 \quad v\in\mathbb R^N,
 \quad E(U)<0,
$$

has M(U)≥Mc+δN. This is a non-effective positive gap. It is a theorem about traveling profiles, not a claim about all global solutions. If no such negative-energy profile exists in a particular dimension, the universal statement remains valid; the theorem itself is not an existence construction.

## 2. Weak H² profiles gain H4 in every dimension

This point needs an explicit argument in N>8, since the initial nonlinearity need not lie in L².

Set R=(Δ²+1)⁻¹. The equation reads

$$
 U=(1-\omega)RU-i v\cdot R\nabla U+R(|U|^\alpha U).
$$

For 1<r<∞, R maps Lr to W^{4,r}; for 1<q<∞, R∂j maps Lq to W^{3,q}. The latter directly acts on U, so it does not presuppose ∂jU∈Lq. These are standard bounded elliptic Fourier multipliers.

For N>4, begin with q0=2N/(N−4) and a0=1/q0=1/2−2/N. Notice

$$
 q_0/(1+8/N)>1
$$

because N²−4N+32>0. If U∈Lq, a=1/q≤a0, the reciprocal exponents supplied by the nonlinear, drift and zero-order terms are respectively

$$
 (1+8/N)a-4/N,\qquad a-3/N,\qquad a-4/N.
$$

The nonlinear improvement is at least16/N², while the drift improvement is3/N. Choosing a fixed loss smaller than half min(16/N²,3/N) avoids all critical Sobolev endpoints. A finite number of steps therefore reaches exponents where every term embeds into L∞. At a zero reciprocal endpoint, one first takes an arbitrary finite larger exponent and continues. All nonlinear source exponents remain greater than one because q only increases.

For N≤4, H² already embeds into all required finite Lq spaces, and one such step gives L∞. Hence, in every dimension, U∈L∞∩L². Then |U|^αU∈L²; using ∇U∈L² in the original equation gives Δ²U∈L² and therefore U∈H4.

Arbitrarily large fixed |ω| or |v| affect constants, not this regularity conclusion.

## 3. Traveling identities need no spatial moments

The current identity

$$
 W(U):=\operatorname{Im}\int\Delta U\nabla\bar U
       =\frac14M(U)v
$$

is valid already at H². In the stationary action, test the legal compactly weighted phase direction iφRU, with φR=xjχ(x/R). The main terms converge by dominated convergence because ΔU∇U∈L¹ and ∇φR is uniformly bounded. The term with ΔφR is O(1/R) times ||ΔU||₂||U||₂. No xU integrability is used.

After the H4 gain, the cutoff dilation direction

$$
 \chi(x/R)\,[NU/2+x\cdot\nabla U]
$$

belongs to H² for every finite R. Integration by parts yields the mass-critical identity

$$
 8E(U)=v\cdot P(U).
$$

The leading x-weighted terms cancel into divergence terms. Remaining errors are bounded by tails of |U|², |∇U|², |D²U|² and |U|p, with the appropriate nonpositive powers of R. Thus the cutoff limit does not require finite variance. The scalar profile pairing is

$$
 \|\Delta U\|_2^2+\omega M(U)-\|U\|_p^p-v\cdot P(U)=0.
$$

## 4. Every complex GN optimizer has constant phase: elementary proof

Write an optimizer u=a+ib with real a,b. Minkowski in L^{p/2}, the real GN inequality and Hölder for the two scalar pairs give

$$
 \|u\|_p^2
 \le\|a\|_p^2+\|b\|_p^2
 \le C\,[M(a)^{1-2/p}K(a)^{2/p}
          +M(b)^{1-2/p}K(b)^{2/p}]
 \le C M(u)^{1-2/p}K(u)^{2/p},
$$

where K=||Δ·||₂². Equality at the two ends forces equality in Minkowski. If both components are nonzero, a² and b² are proportional almost everywhere. Apply the same fact to e^{iπ/4}u: (a+b)² and (a−b)² are also proportional. These two relations imply that a², b² and ab are fixed multiples of a²+b². Therefore the real two-vector (a(x),b(x)) lies on a fixed real line for almost every x. This proves u=e^{iθ}Q with Q real. Cases where a component, or a rotated component, vanishes already have this form.

This argument permits sign changes and does not use unique continuation or Fourier positivity. Existing Fourier-rearrangement symmetry results also imply the conclusion for even p, but the present elementary reasoning removes that restriction.

## 5. Phase-kernel simplicity in all dimensions

Normalize a real optimizer Q so K(Q)=1 and M(Q)=Mc=M. Put a=α/2=4/N. Then

$$
 \|Q\|_p^p=a+1,\qquad
 \omega_Q=a/M,
 \qquad L_-=\Delta^2+\omega_Q-|Q|^{2a}.
$$

The sharp inequality applied to Q+i√s h, s≥0, first shows L−≥0. Indeed the first right derivative of

$$
 \int(Q^2+s h^2)^{a+1}
 \le(a+1)(1+s\|h\|_2^2/M)^a(1+s\|\Delta h\|_2^2)
$$

at zero is precisely the corresponding quadratic-form inequality.

Now let h be a real element of ker L−. Write k=||Δh||₂² and y=||h||₂²/M. The first derivatives of both sides coincide. The pointwise second-order remainder on the left is nonnegative by convexity, so Fatou gives

$$
 J:=\int |Q|^{2a-2}h^4
 \le(a-1)y^2+2ky.
$$

Cauchy–Schwarz and the kernel equation give

$$
 J\ge\frac{(\int |Q|^{2a}h^2)^2}{\int|Q|^{2a+2}}
      =\frac{(k+ay)^2}{a+1}.
$$

Combining the bounds yields (k−y)²≤0. Equality in Cauchy consequently implies h²=yQ² where Q≠0. On {Q=0}, when a<1 the second-order Fatou limit forces h=0; when a=1 Cauchy equality gives the same result. When a>1, the identity on {Q≠0} already accounts for the whole mass ||h||₂²=yM, so h=0 on the remaining set. Thus h²=yQ² almost everywhere in all cases.

Since h+Q is also a kernel vector, applying this conclusion to h+Q forces h/Q to be constant, not merely constant in modulus. Therefore

$$
 \ker L_- =\operatorname{span}\{Q\}.
$$

The potential is compact relative to the H² form. For N>4, |Q|^{8/N}∈L^{N/4}, and bounded compactly supported functions approximate it in that norm; critical Sobolev and local Rellich give the claim. For N≤4, use an exponent strictly above N/4 and the relevant finite Sobolev embedding. It follows that L− is coercive in H² on the L²-orthogonal complement of Q. No L+ assertion is involved.

## 6. Compactness and the contradiction

If the claimed gap failed, choose negative-energy profiles with masses tending to Mc. Critical scaling makes K(U_n)=1 without changing mass or energy sign, while allowing arbitrary rescaled frequencies and velocities. The sharp inequality squeezes ||U_n||p^p to p/2.

GN maximizing-sequence compactness gives strong H² convergence, after translations and a subsequence, to an optimizer Q. This compactness does not need optimizer uniqueness. A direct concentration-compactness proof uses nonvanishing, Brezis–Lieb splitting and

$$
 M_1^{a}K_1+M_2^{a}K_2 < M_c^a(K_1+K_2)
$$

whenever both mass pieces are nonzero. The remaining norm equalities force strong H² convergence.

Make Q real using Section4. Continuity of W in H² and W(Q)=0 give v_n→0 by the current identity. The scalar profile pairing then gives ω_n→a/Mc. Choose the remaining small constant phase so U_n=a_n+ib_n with b_n⊥Q exactly.

The real form

$$
 A_n=\Delta^2+\omega_n-|U_n|^{8/N}
$$

converges to L− in H²→H⁻² operator norm. For N>4 this follows from strong L² convergence and the L^{N/4} potential estimate; for N≤4 use strong convergence in a suitable finite Lq. Therefore A_n is uniformly positive on Q⊥ for all sufficiently large n.

The imaginary equation and momentum integration by parts give the exact identities

$$
 A_n b_n=-v_n\cdot\nabla a_n,
 \qquad v_n\cdot P(U_n)=2\langle b_n,A_n b_n\rangle.
$$

Hence

$$
 E(U_n)=\tfrac14\langle b_n,A_n b_n\rangle\ge0,
$$

contradicting negative energy. This proves a uniform gap over all frequencies and speeds. The coercivity constant need only be positive for the one limiting optimizer; uniform nondegeneracy of the entire optimizer family is not assumed.

## 7. Independent algebra check of the fixed-mass, fixed-momentum curve

Set a=P(U)/M(U), m=M(U)|a|⁴, and

$$
 B=\int(|\xi|^2|a|^2+2(\xi\cdot a)^2)|\widehat U(\xi)|^2d\xi.
$$

For Uλ=e^{i(1−λ)a·x}λ^{N/2}U(λx), both mass and momentum are fixed. Let A=a·W=2E. Direct quartic expansion gives

$$
 E(U_\lambda)=\lambda^4E+4\lambda^3(1-\lambda)E
 +\lambda^2(1-\lambda)^2B
 +2\lambda(1-\lambda)^3m+\tfrac12(1-\lambda)^4m.
$$

Thus

$$
 E(U_\lambda)-E(U)
 =(\lambda-1)^2\big[(B-\tfrac32m-3E)\lambda^2
 +(m-2E)\lambda+(\tfrac12m-E)\big].
$$

Jensen gives B≥3m. If E<0, every displayed coefficient is strictly positive, proving a strict global minimum at λ=1 along this particular curve for λ>0. This calculation is valid in all dimensions and does not imply stability on the whole fixed-mass/momentum manifold.

## 8. Sources and priority

Primary-source checking confirmed Lenzmann–Sok, arXiv:1805.06294v4, Theorem2, which treats all GN optimizers for even integer p and proves their reality and radial symmetry up to phase and translation. Their remarks also mention alternative arguments for reality at non-even p. Bugiera–Lenzmann–Schikorra–Sok, arXiv:1908.06771, treats symmetries of variational traveling ground states for generalized dispersion. Neither source, as checked, states the uniform negative-energy traveling-wave mass gap proved above. This limited search does not establish novelty priority. The reality lemma itself should not be advertised as newly discovered.
