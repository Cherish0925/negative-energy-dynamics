# Proof details of round8_compact_dynamics.md

## Verdict

No substantive flaw was found in the deductions of Theorems A and B, conditional on the round-5 interaction-virial estimate with the explicitly restored general-momentum term

$$
I_R'\le16ME-8P\cdot W+B R^{-2}h^{1/2}+Chd_R^\theta.
$$

This audit checked the new argument, not an independent rederivation of every term in that previously proved fourth-order interaction identity. Bibliographic priority statements require their separate source audit.

## Detailed checks

1. **Sign.** Integrating the displayed upper bound gives
   $8\int P\cdot W\le16ME(t-s)+\text{errors}-[I_R(t)-I_R(s)]$.
   Hence the claimed upper bound on mean counter-momentum drift has the correct direction. For a traveling wave it is consistent with $v\cdot P=8E$.

2. **Short-window budgets.** The first-average hypothesis for all windows of length at least $T_0$ implies $\int_Jh\le H(|J|+T_0)$ for every subinterval $J$, by extending a short interval. No pointwise kinetic bound is silently used.

3. **Coarse center transport.** A scalar cutoff centered at $c(s)$ initially contains at least $7M/8$. Taking its radius proportional to $\int_s^t h$ limits mass loss to $M/8$. The resulting support must intersect the $7M/8$-mass ball at $c(t)$. This proves the coarse bound on $|c(t)-c(s)|$ for completely discontinuous choices of centers. Jumps between admissible centers are bounded and do not affect long-time velocities.

4. **Mass-only tail interpolation.** Applying $\|\nabla f\|_2^2\le\|f\|_2\|\Delta f\|_2$ to a cutoff of $u$ outside a mass-concentration ball yields the stated exterior gradient estimate. Cauchy--Schwarz then bounds $\int_{\rm exterior}|\Delta u||\nabla u|$ by a mass-tail quarter power times $h^{3/4}$. Curvature tails themselves need not be small. The scalar cutoff's second derivative contributes $O(R^{-1}h^{1/2})$.

5. **Localized centroid without a first moment.** With $R=LT$, the coarse transport estimate keeps all relevant centers within $R/4$. The endpoint error is $Mr+CR\mu(r)$. Dividing by $T$, taking $T\to\infty$ first and then $r\to\infty$, gives an error tending to zero. Constants are uniform in the starting time under Theorem A. No physical first moment is assumed or constructed.

6. **Theorem A low-kinetic endpoints.** Selecting one point from each endpoint interval of fixed length $T_0$ with $h\le2H$ is valid. The discarded pieces have uniformly bounded $\int|W|$, by Hölder and their first kinetic budgets. Their contribution divided by $T$ vanishes. Passing $T\to\infty$ for fixed $R$, and then $R\to\infty$, is the correct order.

7. **Theorem B subsequence.** From a hypothetical sequence $\int_0^{T_n}h\le HT_n$, selecting $t_n\in[T_n/2,T_n]$ with $h(t_n)\le4H$ gives $\int_0^{t_n}h\le2Ht_n$. Thus the sequence-only center/current result applies with constant $2H$, independently of pointwise behavior before $t_n$. The initial endpoint $h(0)$ is finite for a strong $H^2$ solution. The contradiction rules out every bounded-average subsequence, proving actual divergence of the averages.

## Scope

The one-sided drift law is the appropriate conclusion for mass tightness alone. Equality cannot be claimed from an upper virial estimate which discards a favorable kinetic deficit. The result permits instantaneous kinetic peaks and arbitrary noncompact curvature tails, but still assumes uniform mass tightness modulo a single center. It does not prove the unrestricted dynamical mass gap.

## Scalar nonnegative second-order dispersion extension

For $i u_t=(\Delta^2-\mu\Delta)u-|u|^{8/N}u$, $\mu\ge0$, let $G^2=\|\nabla u\|_2^2$ and $E_\mu=E+\mu G^2/2$. The appended factors were independently recomputed:

$$
J'=16E_\mu-4\mu G^2,\qquad X'=4W+2\mu P,
$$

where $J=2\operatorname{Im}\int x\bar u\nabla u$ and $X=\int x|u|^2$ are used only to identify the uncut algebra; the actual proof is localized. Since $I=MJ-2X\cdot P$,

$$
I'=16ME_\mu-4\mu M G^2-8P\cdot W-4\mu|P|^2.
$$

Combining the localized upper inequality with the localized center/current law gives precisely

$$
\limsup_{T\to\infty}\sup_{S\ge0}
\left[\frac{P\cdot(c(S+T)-c(S))}{T}
+\frac{2\mu}{T}\int_S^{S+T}\|\nabla u(t)\|_2^2dt\right]
\le8E_\mu.
$$

The extra second-order Hessian defect has the favorable sign for $\mu\ge0$. Its lower-order cutoff flux errors are controlled by the same mass-tightness interpolation and first kinetic average. The factors and sign are correct. This does not justify an arbitrary matrix lower-order term by the same formula without a separate anisotropic computation.
