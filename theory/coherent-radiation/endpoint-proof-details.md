# Derivation of the Fourier endpoint bounds

18 October 2026. Scope: independent verification of [endpoint.md](endpoint.md), especially its two Fourier sum-of-squares identities and all constants in dimensions three and four, followed by a targeted primary-source comparison. This review does not settle attainment of the traveling-wave mass threshold or literature priority.

## 1. Verification result

The two identities, their equality measures, strictness for Fourier densities, the conversion to profile energy, and every N=3/N=4 constant currently displayed in [endpoint.md](endpoint.md) are correct.

Use probability moments

$$
\mu=\int \xi\,d\nu,\qquad q=\int |\xi|^2\xi\,d\nu,
\qquad a_k=\int|\xi|^k\,d\nu.
$$

For a pure mass-critical BNLS traveling profile, set

$$
d\nu=|\widehat U|^2d\xi/M,\qquad q=v/4,\qquad
h=\mu\cdot q=2E/M,\qquad a_4=A/M.
$$

The first integrand expands exactly to

$$
|\xi|^4+8(\mu\cdot\xi)|\xi|^2
-64|\mu|^2(\mu\cdot\xi)+64|\mu|^4.
$$

Its expectation is therefore $a_4+8h$. Equality requires the two points $(-2\pm2\sqrt3)\mu$. The listed weights are positive, add to one, and give $\mu=e,q=-8e,a_4=64$. Thus $a_4+8h>0$ for every nonzero Fourier density and

$$
A+16E>0.
$$

For the second identity put $e=q/|q|$ and $d=(2|q|)^{1/3}$. Its integrand expands to

$$
|\xi|^4-2d(e\cdot\xi)|\xi|^2+d^3(e\cdot\xi)+d^4/4.
$$

Since $d^3=2|q|$, its expectation is $a_4+2h-3d^4/4$. The stated equality measure on $d(1\pm\sqrt3)e/2$ has moments

$$
\mu=0,\qquad a_2=d^2/2,\qquad q=d^3e/2,
\qquad a_4=3d^4/4.
$$

Consequently

$$
a_4+2h>\frac3{2^{2/3}}|q|^{4/3}
$$

for absolutely continuous probabilities. If $q=0$, the corresponding strict inequality is simply $a_4>0$. Both optimal constants are optimal in the class of probability moments and smooth Fourier densities; optimality within exact nonlinear profiles remains unproved.

## 2. Constants and one direct corollary

From

$$
\omega M=\frac4N A+\left(6-\frac8N\right)E
$$

and $-A/16<E<0$, one obtains:

| Dimension | Kinetic-to-mass interval | Energy interval |
|---|---|---|
| N=3 | $3\omega/4<A/M<8\omega/9$ | $-\omega M/18<E<0$ |
| N=4 | $\omega<A/M<4\omega/3$ | $-\omega M/12<E<0$ |

For N=4, $\omega=a_4+2h$, so every nonzero exact profile, of either energy sign, obeys

$$
\omega>3\,2^{-10/3}|v|^{4/3},\qquad
|v|<4\sqrt2\,3^{-3/4}\omega^{3/4}.
$$

The speed coefficient is 2.4816129576055994.

There is also a direct N=3 negative-energy corollary worth including in the same theorem, rather than treating it as a separate result. Since $h<0$,

$$
\omega=\frac43a_4+\frac53h
=\frac43(a_4+2h)-h
>\frac4{2^{2/3}}|q|^{4/3}
=2^{-4/3}|v|^{4/3}.
$$

Thus

$$
\boxed{|v|<2\omega^{3/4}\quad(N=3,E<0).}
$$

The separate Cauchy–Schwarz estimate in [endpoint.md](endpoint.md) is correct:

$$
|q-a_2\mu|^2\le a_2(a_4-a_2^2),\qquad
\max_{a_2\ge0}a_2(a_4-a_2^2)
=\frac2{3\sqrt3}a_4^{3/2}.
$$

When $h<0$, the left-hand side is strictly larger than $|q|^2$, giving

$$
|v|<4(4/27)^{1/4}(A/M)^{3/4}.
$$

The numerical coefficient again equals 2.4816129576055994, but the scale is A/M, not omega.

## 3. Targeted primary-source comparison

1. **Bugiera–Lenzmann–Schikorra–Sok**, *On symmetry of traveling solitary waves for dispersion generalized NLS*, Nonlinearity 33 (2020), 2797–2819, arXiv:1908.06771. Full primary text: https://arxiv.org/html/1908.06771v1 . Theorem 1 assumes $\omega>-\Sigma_v$, where $\Sigma_v=\inf_\xi(p(\xi)-v\cdot\xi)$, and constructs variational boosted ground states. For $p(\xi)=|\xi|^4$, this gives the familiar sufficient coercivity condition $\omega>3(|v|/4)^{4/3}$. This is stronger numerically than the new N=4 necessary inequality but serves a different logical purpose. The checked paper does not supply the displayed $E>-A/16$ bound or the displayed weaker universal N=4 frequency-speed necessity. Its existence result is credited to Himmelsbach's 2017 thesis, which was not fully retrieved and audited here.

2. **Casteras–Földes**, *Existence of traveling waves for a fourth order Schrödinger equation with mixed dispersion in the Helmholtz regime*, Mathematische Annalen 394, article 41 (2026), DOI 10.1007/s00208-026-03399-4. Full primary text: https://link.springer.com/article/10.1007/s00208-026-03399-4 . Theorem 1.1 constructs solutions in an Lp/resolvent framework for a sign-changing free symbol. Its conclusion is not H2 or L2 localization; the introduction explicitly discusses this distinction. Therefore those waves cannot automatically be treated as finite-mass counterexamples to the moment necessities here. The paper references a 2020 Casteras preprint on normalized fourth-order traveling waves at fixed mass or mass and momentum. The referenced manuscript was not recovered in this targeted search, so it remains a genuine gap in the prior-art audit.

No matching occurrence of these particular two energy/frequency-speed bounds was located in the primary texts checked. This establishes neither first discovery nor absence from the literature. Searches for general fourth-moment inequalities also did not establish priority for the underlying algebraic inequalities. The appropriate manuscript presentation is a proved Fourier-moment lemma and its profile corollaries, with existing variational existence theory cited and priority wording withheld pending a wider bibliography check.

## 4. Remaining scientific limits

- The identities constrain exact profiles but do not produce new profiles, settle the minimum-mass endpoint, or identify the optimal constants over the nonlinear solution set.
- The necessary frequency bound does not make the free symbol positive and supplies no Fredholm spectral gap by itself.
- The new anisotropic/mixed-order uniform mass gap is meaningful as an exclusion theorem, but this work has not proved that its negative intrinsic-energy traveling-profile class is nonempty. The known pure isotropic constructions do not transfer automatically to that model.
- The other independent anisotropic proof now gives a simpler argument uniform over positive-semidefinite lower-order quadratic dispersion; [anisotropic-gap.md](anisotropic-gap.md) should be the main technical source for that extension. The exact partial Galilean reduction and the intrinsic-energy condition, rather than hypothetical optimizer reflection symmetry, are the relevant structural connection.

