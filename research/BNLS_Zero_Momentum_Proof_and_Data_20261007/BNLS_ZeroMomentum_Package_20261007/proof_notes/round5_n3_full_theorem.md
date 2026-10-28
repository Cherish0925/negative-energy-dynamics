# Three-dimensional nonradial negative-energy global waves

## Theorem

For the mass-critical focusing biharmonic nonlinear Schrödinger equation

\[
 i\partial_tu=\Delta^2u-|u|^{8/3}u\quad\text{on }\mathbb R^3,
\]

there exists an exact real radial standing profile Q and a family of complex profiles U_v, for every real speed

\[
0<|v|\le 10^{-9},
\]

such that

\[
 (\Delta^2+1)U_v-|U_v|^{8/3}U_v+i v\partial_1U_v=0,
 \qquad \|U_v-Q\|_{H^2_Z}\le 1000|v|,
\]

and

\[
 E(U_v)<-180v^2<0.
\]

Here \(\|f\|_{H^2_Z}^2=\|\Delta f\|_2^2+\|f\|_2^2\) and

\[
 E(u)=\frac12\|\Delta u\|_2^2-\frac{3}{14}\int|u|^{14/3},
 \quad P_1(u)=\operatorname{Im}\int\bar u\,\partial_1u.
\]

Consequently \(u_v(t,x)=e^{it}U_v(x-vte_1)\) is a nonradial negative-energy solution defined for every real time, with constant H² norm. In particular negative energy alone does not force finite-time blowup in this three-dimensional equation.

The theorem is supported by the supplied analytic arguments and exact-input interval certificates. It is a research result of this work; external independent review has not yet been performed.

## 1. Exact standing profile

The frozen q is defined by SHA256 `5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b`. The round4 mixed-residual verifier gives

\[
 \|F(q)\|_{Z^*}<1.3\cdot10^{-7},\quad
 \|q\|_Z<136.476,\quad\|q\|_\infty<6.207.
\]

The new radial certificate gives \(\|L_+(q)^{-1}\|_{Z^*\to Z}<25\). The Newton ball has radius \(\rho=4\cdot10^{-6}\). On this ball, \(\|D^2g\|\le211\), for \(g(z)=|z|^{8/3}z\), and the embedding is \(\|h\|_\infty\le\|h\|_Z/4\). Therefore

\[
25(1.3\cdot10^{-7})+\frac{25\cdot211}{8}\rho^2<\rho,
\qquad \frac{25\cdot211}{4}\rho<1.
\]

Banach's theorem gives the exact real radial Q with \(\|Q-q\|_Z<\rho\). In particular \(\|Q\|_Z<137\), \(\|Q\|_\infty<6.300001\).

The proof of the radial inverse is in `round5_n3_radial_proof.md`. It combines an explicit half-line/box Green comparison, rigorous piecewise linear potential approximation and Arb FFT, a positive finite-rank resolvent tail, and an Arb-certified finite-matrix eigensystem. It is a whole-space inverse estimate.

## 2. All symmetry channels

Work over the real Banach space

\[
 X=\{f\in H^2(\mathbb R^3;\mathbb C):f(-x)=\overline{f(x)}\}.
\]

Its real part contains precisely even spherical harmonics, and its imaginary part precisely odd harmonics. The linearization at Q is \(L=L_+(Q)\oplus L_-(Q)\), where

\[
 L_+(Q)=\Delta^2+1-\frac{11}{3}|Q|^{8/3},
 \qquad L_-(Q)=\Delta^2+1-|Q|^{8/3}.
\]

The finite channels are all certified with the following conservative exact-Q lower gaps in the preconditioned energy norm:

| Operator | Degree | Gap greater than |
|---|---:|---:|
| L+ | 0 | 0.0420 |
| L+ | 2 | 0.1045 |
| L+ | 4 | 0.1935 |
| L+ | 6 | 0.0997 |
| L+ | 8 | 0.1509 |
| L+ | 10 | 0.0851 |
| L+ | 12 | 0.2865 |
| L+ | 14 | 0.0643 |
| L− | 1 | 0.0059 |
| L− | 3 | 0.0405 |
| L− | 5 | 0.0752, positive |

For L+ at degree16, the whole-space Birman--Schwinger HS square is below0.701497868. Thus that operator is positive, with exact-Q gap above0.1622.

For completeness, let \(\lambda_\ell=\ell(\ell+1)\). On the natural angular form domain,

\[
\int r^2|\Delta_\ell f|^2
=\int r^2|\Delta_0f|^2
+2\lambda_\ell\int|f'|^2
+\lambda_\ell(\lambda_\ell-2)\int r^{-2}|f|^2.
\]

For degrees \(\ell'\ge\ell\ge1\), the free energy forms are increasing. If \(A_\ell-V\ge\delta A_\ell\), with \(0<\delta\le1\), then

\[
 A_{\ell'}-V\ge\delta A_\ell+(A_{\ell'}-A_\ell)
 \ge\delta A_{\ell'}.
\]

Hence degree5 positivity controls every odd degree at least5, and degree16 positivity every even degree at least16. No angular channels remain unchecked. The direct-sum inverse on X consequently satisfies

\[
 \|L^{-1}\|_{X^*\to X}<200.
\]

The finite-channel certificate uses exact mixed spline trials for generalized Birman--Schwinger eigenvectors. Each trial residual produces a genuine spectral inclusion; the intervals are disjoint. A separately certified whole-space HS norm bounds every omitted eigenvalue after subtracting the known squared eigenvalue lower bounds. No assumed count of finite-difference eigenvalues is used.

## 3. The dipole sign

Let \(z=L_-(Q)^{-1}\partial_1Q\), a real odd function. The response certificate proves

\[
 I=\langle\partial_1Q,z\rangle<-1280,
 \qquad \|z\|_Z<818.
\]

The latter follows from the exact trial norm below808.262, exact-Q response residual below0.046504 and inverse norm below200. The sign is certified using the residual-squared identity

\[
\langle g,L^{-1}g\rangle
=2\langle g,z_0\rangle-\langle Lz_0,z_0\rangle
 +\langle g-Lz_0,L^{-1}(g-Lz_0)\rangle.
\]

Detailed proof and data are in `round5_n3_pairing_proof.md`.

## 4. Quantitative traveling-wave construction

Put \(U_v=Q+w\), and define

\[
 N(w)=g(Q+w)-g(Q)-Dg(Q)w.
\]

On the radius \(R_v=1000|v|\) ball, for \(|v|\le10^{-9}\), the pointwise complex-vector second derivative obeys

\[
\|D^2g(z)\|\le\frac{88}{9}|z|^{5/3}<211.
\]

Indeed the general formula for \(g(z)=|z|^a z\), with \(a=8/3>2\), gives the bound \(a(a+1)|z|^{a-1}\). It applies equally to real and complex perturbations. Thus

\[
 \|N(w)\|_{Z^*}\le\frac{211}{8}\|w\|_Z^2,
\]

and N has Lipschitz constant at most \((211/4)R_v\) in this ball. Also

\[
 \|\partial_1f\|_{Z^*}\le\frac35\|f\|_Z,
 \qquad \|\nabla f\|_2\le\frac1{\sqrt2}\|f\|_Z.
\]

The profile equation is equivalent to the self-map of X

\[
 w=-ivz+L^{-1}N(w)-vL^{-1}(i\partial_1w).
\]

The radius bound is

\[
 \|\mathcal T(w)\|_Z
 \le818|v|+5{,}275{,}120{,}000\,v^2<1000|v|.
\]

The contraction constant is at most

\[
 200\left(\frac{211}{4}\,1000+\frac35\right)|v|
 \le0.01055012<1.
\]

This constructs U_v directly, and in addition

\[
 w=-ivz+r_v,
 \qquad \|r_v\|_Z\le5{,}275{,}120{,}000\,v^2.
\]

The noninteger power causes no loss in this argument: the map is C³ near Q in the energy-space formulation, and only the displayed second-derivative bounds are needed. No smooth H10 manifold or high-regularity multiwave gluing assertion is made here.

## 5. Negative energy and global evolution

Expanding the momentum and integrating the real-Q linear term by parts gives

\[
 P_1(U_v)=2Iv+\mathcal E_v,
\]

where

\[
|\mathcal E_v|
\le\sqrt2\|Q\|_Z\|r_v\|_Z+\frac1{\sqrt2}\|w\|_Z^2
<1.1\cdot10^{12}v^2.
\]

The traveling profile is a stationary point of

\[
 S_v(u)=E(u)+\frac12M(u)-\frac v2P_1(u).
\]

Under the mass-preserving dilation \(u_\lambda(x)=\lambda^{3/2}u(\lambda x)\), energy scales as \(\lambda^4\), momentum as \(\lambda\), and mass is unchanged. The corresponding Pohozaev identity is therefore

\[
 8E(U_v)=vP_1(U_v).
\]

This identity is valid for the H² elliptic profile by the usual cutoff multiplier proof: first use the elliptic equation to gain H4, take a smooth cutoff of the dilation field, and let its radius tend to infinity. All cutoff errors are bounded by H² and L^(14/3) tails. In particular no finite variance assumption is inserted.

The certified estimates give, for every nonzero \(|v|\le10^{-9}\),

\[
 8E(U_v)
 \le-2560v^2+1.1\cdot10^{12}|v|^3
 \le-1460v^2,
\]

so \(E(U_v)<-180v^2\). The strict sign also proves \(P_1(U_v)\ne0\), whereas every radial H² profile has zero momentum. Hence U_v is nonradial. Substitution of the profile equation proves that \(e^{it}U_v(x-vte_1)\) solves the PDE for every real t. Translations and constant phase preserve its H² norm, completing the claimed global negative-energy construction.

## 6. Reproduction and exact inputs

The unified command is

```
python3 round5_n3_theorem.py --verify-all
```

It reruns the round4 mixed residual, new radial inverse, dipole HS/Ritz/response, nine additional finite channels, and degree16 high-channel bound, then verifies all contraction and energy constants. The shorter command without `--verify-all` checks their stored outputs and all final scalar inequalities. The final machine summary is `round5_n3_theorem.json`.

The numerical BVP source generators explain provenance; they are not needed to verify the frozen mixed spline inputs. All exact inputs and verifier outputs have recorded SHA256 identifiers. The radial verifier independently checks its generated IEEE eigensystem using Arb matrix products, so its SciPy call does not supply an unchecked spectral assertion.

## 7. Scaling consequences

The displayed speed restriction is at the normalized temporal frequency one. The exact mass-critical scaling is

\[
u_{\lambda,v}(t,x)=\lambda^{3/2}e^{i\lambda^4t}
 U_v(\lambda x-v\lambda^4te_1),\qquad\lambda>0.
\]

Its physical speed is \(c=\lambda^3v\), while its mass is unchanged and its energy is \(\lambda^4E(U_v)<0\). Thus the construction yields a global negative-energy wave at every prescribed nonzero physical speed by choosing \(\lambda=(|c|/|v|)^{1/3}\) and rotating the propagation direction. It also yields a global wave at every prescribed negative energy, by choosing \(\lambda=(|E_*|/|E(U_v)|)^{1/4}\). These are separate prescriptions; independent simultaneous prescription of speed, energy and mass is not asserted.

In particular the theorem is not confined to a single small negative energy value or a single physical speed. The small parameter is the scale-invariant combination of speed and temporal frequency.
