# Full Morse index and kernel of the certified four-dimensional BNLS wave

2026-10-07. This note closes the previously missing degree-three certificate. All statements concern the exact stationary profile selected by the existing frozen existence certificate, not an approximate numerical profile. The only imported existence input is the base proof's real radial solution

\[
(\Delta^2+1)Q-Q^3=0,\qquad \|Q-q\|_Z\le 0.006,\quad \|q\|_Z<104,
\qquad \|f\|_Z^2=\|\Delta f\|_2^2+\|f\|_2^2.
\]

The canonical rational trial has SHA256 `c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627`. No frozen base file was changed.

## 1. Exact conclusion

Let
\[
L_+=\Delta^2+1-3Q^2,\qquad L_-=\Delta^2+1-Q^2.
\]
On the full real scalar spaces, with no angular symmetry restriction,
\[
 n(L_+)=31,\qquad n(L_-)=5,
\]
\[
 \ker L_+=\operatorname{span}_{\mathbb R}\{\partial_1Q,\ldots,\partial_4Q\},
 \qquad \ker L_-=\operatorname{span}_{\mathbb R}\{Q\}.
\]
Thus the real-complex Hessian has 36 negative directions and exactly five zero directions. For the form-preconditioned self-adjoint operators
\[
 T_\pm=A^{-1/2}L_\pm A^{-1/2},\qquad A=\Delta^2+1,
\]
all nonzero spectrum has distance strictly greater than `1/29` from zero.

This gap is a spectral separation of the preconditioned operator. It is **not** an assertion that the absolute value of an indefinite quadratic form bounds the norm on the whole kernel complement; such an assertion would be false because positive and negative directions can cancel. On the respective positive and negative spectral subspaces, the quadratic forms have the corresponding signed coercivity.

## 2. The new degree-three Rayleigh certificate

The frozen file `round2_ritz_exact_data.json` already supplies a reduced radial trial `f` for degree two. Reuse that same exact compact rational Hermite function in the new harmonic
\[
 h(x)=r^3f(r)Y_3(\theta).
\]
No new numerical eigenproblem is needed. For this degree-three harmonic the effective radial dimension is 10, so its Rayleigh quotient is
\[
 \mathcal R=\frac{3\int_0^{36}q(r)^2 f(r)^2r^9\,dr}
 {\int_0^{36}\left[(f''+9f'/r)^2+f^2\right]r^9\,dr}.
\]
Every integrand becomes a polynomial on each Hermite cell. The apparently singular kinetic expression is evaluated as
\[
 \int_0^{36}(rf''+9f')^2r^7\,dr.
\]
The compact endpoint has all four jets zero; the reduced radial function has vanishing odd origin jets. The trial is therefore an admissible nonzero `H²` harmonic.

`round4_ell3_rayleigh.py` recomputes both forms with exact `Fraction` arithmetic. Its exact rational comparison proves
\[
 \mathcal R>\frac{13}{10}.
\]
The decimal `1.308995988054891` is only a readable approximation to the quotient; the decision uses the exact rational numerator and denominator saved in `round4_ell3_rayleigh_results.json`.

The existing rigorous Hilbert--Schmidt bound is
\[
 \|K_{1,q,3}\|_{HS}^2<0.22,
 \quad K_{c,q,\ell}=c A_\ell^{-1/2}q^2A_\ell^{-1/2}.
\]
Therefore `||K_{3,q,3}||²_HS<1.98`. Its top eigenvalue exceeds 1.30, while all subsequent eigenvalues obey
\[
 \mu_2^2\le\sum_{j\ge2}\mu_j^2<1.98-1.30^2=0.29<0.54^2.
\]
This gives exactly one negative direction and no zero direction after transfer to the exact profile.

## 3. Transfer from the rational profile to Q

The base product estimate is
\[
 \|fgh\|_{Z^*}\le\frac1{256}\|f\|_Z\|g\|_Z\|h\|_Z.
\]
Thus
\[
 \|A^{-1/2}(Q^2-q^2)A^{-1/2}\|
 \le\frac{2(104)(0.006)+(0.006)^2}{256}
 =\delta:=\frac{312009}{64000000}.
\]
The coefficient-three transfer is `3δ=936027/64000000`. The same bound holds after restriction to every angular channel. Min--max perturbation therefore gives
\[
 |\mu_j(K_{c,Q,\ell})-\mu_j(K_{c,q,\ell})|\le c\delta.
\]
No Hilbert--Schmidt continuity from `q` to `Q` is assumed or needed.

## 4. Full angular accounting

The real degree-`ell` spherical harmonics on `S³` have dimension `(ell+1)²`. The complete count is

| degree | multiplicity | negative `L+`, per channel | zero `L+`, per channel | negative `L−`, per channel | zero `L−`, per channel |
|---|---:|---:|---:|---:|---:|
| 0 | 1 | 2 | 0 | 1 | 1 |
| 1 | 4 | 1 | 1 | 1 | 0 |
| 2 | 9 | 1 | 0 | 0 | 0 |
| 3 | 16 | 1 | 0 | 0 | 0 |
| every degree >=4 | `(ell+1)²` | 0 | 0 | 0 | 0 |

The details below also exclude all additional zero eigenvalues.

### Radial degree zero

The frozen certificates give, for coefficient three,
\[
 \mu_1\ge5.395,\quad \mu_2>2.999,\quad \sum\mu_j^2<38.80<39.
\]
As
\[
39-5.395^2-2.999^2<0.95^2,
\]
all later eigenvalues are below 0.95. Hence `L+` has exactly two negative directions and a preconditioned gap at least `0.05−3δ>1/29`.

The exact identity `L−Q=0` gives an exact coefficient-one eigenvalue 1, or coefficient-three eigenvalue 3. The first coefficient-three eigenvalue of `Q` remains above 5, and every eigenvalue from the third onward is below `0.95+3δ<1`. Thus the exact eigenvalue 3 must be the second one and is simple. Dividing the coefficient-three spectrum by three proves one radial negative `L−` direction and only the phase kernel.

### Degree one: the formerly hidden extra-kernel issue

For coefficient one, the exact trial and interval certificates give
\[
 \mu_1(K_{1,q,1})>1.04,\quad \operatorname{tr}K_{1,q,1}<1.70,
 \quad \|K_{1,q,1}\|_{HS}^2<1.24.
\]
The first two bounds already prove one negative direction and no kernel for `L−`, with nonzero gap exceeding `0.04−δ>1/29`.

Differentiating the exact stationary equation gives
\[
 L_+\partial_jQ=0.
\]
Consequently `K_{1,Q,1}` has the exact eigenvalue `1/3`. Its top eigenvalue exceeds `1.04−δ>1`. Hence its second eigenvalue is at least `1/3`, and perturbation yields
\[
 \mu_2(K_{1,q,1})\ge\frac13-\delta.
\]
Using the squared Hilbert--Schmidt bound now proves
\[
 \mu_3(K_{1,q,1})^2
 <1.24-1.04^2-\left(\frac13-\delta\right)^2<0.23^2.
\]
Thus
\[
 \mu_3(K_{1,Q,1})<0.23+\delta<\frac13.
\]
The exact `1/3` eigenvalue is therefore the simple second eigenvalue. After multiplication by three, each degree-one `L+` channel has one negative eigenvalue, one translation kernel, and a positive spectral remainder separated from zero by more than `1/29`.

### Degree two

For coefficient three, `μ1>2.11` and `HS²<4.80`. Thus `μ2²<4.80−2.11²<0.6²`. Transfer gives exactly one negative `L+` eigenvalue with gap at least `0.4−3δ>1/29`. For coefficient one,
\[
 \|K_{1,Q,2}\|\le\sqrt{4.80}/3+\delta<0.75,
\]
so `L−` is positive.

### Degree three and every higher degree

Section 2 gives exactly one degree-three negative `L+` eigenvalue. Its two separating margins are `0.30−3δ` and `0.46−3δ`, both larger than `1/29`.

For degree four, `HS²(K_{3,q,4})<0.73<0.9²`; thus `L+` is positive with gap `0.1−3δ>1/29`. The exact angular identity
\[
 \|D_\ell f\|_{L^2(r^3dr)}^2=
 \|D_0f\|_{L^2(r^3dr)}^2
 +2\ell(\ell+2)\int r|f'|^2dr
 +\ell^2(\ell+2)^2\int r^{-1}|f|^2dr
\]
shows the common angular forms increase for every `ell>=1`. The largest Birman--Schwinger eigenvalue is therefore nonincreasing in `ell`. The degree-four `L+` bound covers **every** higher degree, including odd degrees. The degree-two `L−` bound likewise covers every higher degree.

Summing multiplicities gives `n(L+)=2+4+9+16=31`, `n(L−)=1+4=5`, and exactly five real kernel vectors.

## 5. Functional setting and exact symmetry vectors

The base solution is `H⁴`. Since `H⁴(R⁴)` is an algebra and `A^{-1}` gains four derivatives, `AQ=Q³` bootstraps to `Q∈H^s` for every finite `s`. In particular, differentiating the equation is justified and the translations belong to the operator domain.

Also `Q∈C_0`, so multiplication by `Q²` is form-compact relative to `A`; this follows by approximating the potential by compactly supported bounded functions and using local Rellich compactness. The essential spectrum of each unpreconditioned operator is `[1,∞)`. The compact preconditioned analysis controls all negative and zero spectrum, not merely eigenvalues seen on a truncated domain.

## 6. Quantitative persistence for the exact traveling branch

For the pure four-dimensional cubic branch at frequency one, let
\[
 A U_v+i\mathbf v\cdot\nabla U_v-|U_v|^2U_v=0,
 \qquad 0<|\mathbf v|\le10^{-6},\quad\|U_v-Q\|_Z\le200|\mathbf v|.
\]
Its real Hessian on the full complex energy space is
\[
 \mathcal L_v w=A w+i\mathbf v\cdot\nabla w
 -2|U_v|^2w-U_v^2\overline w.
\]
Writing `s=|v|`, the product estimate and first-derivative bound give
\[
 \|A^{-1/2}(\mathcal L_v-\mathcal L_0)A^{-1/2}\|
 \le\left[\frac3{256}(210+200s)200+\frac35\right]s
 =492.7875s+468.75s^2<0.000493.
\]
For `s<=10^{-6}` this is less than one third of the stationary `1/29` gap. The spectral cluster near zero therefore remains five-dimensional, and the negative spectral rank remains 36.

The exact symmetries give five kernel vectors `iU_v,∂1U_v,...,∂4U_v`. They are linearly independent for **every** nonzero localized `H¹` function: an identity `aiU+b·∇U=0` with real coefficients would force the Fourier transform to be supported on a hyperplane when `b≠0`, impossible for a nonzero `L²` function; when `b=0` it forces `a=0`. Consequently the entire five-dimensional near-zero cluster is exactly the symmetry kernel. No extra near-zero eigenvalue is allowed to split away.

Thus, throughout the explicit speed interval,
\[
 n(\mathcal L_v)=36,\qquad
 \ker\mathcal L_v=\operatorname{span}_{\mathbb R}\{iU_v,\partial_1U_v,\ldots,\partial_4U_v\},
\]
with nonzero preconditioned spectral gap greater than `1/30`. The conclusion is a Hessian statement; instability follows only after the separate Hamiltonian-index hypotheses and action-Hessian signature are established.

## 7. Reproduction and scope

New files:

- `round4_ell3_rayleigh.py` and `round4_ell3_rayleigh_results.json`: exact new Rayleigh certificate.
- `round4_verify_morse.py`, `round4_morse_results.json`, `round4_morse_verification.log`: exact scalar separation and full angular accounting.
- `round4_morse_work/`: isolated rerun of all five Arb Hilbert--Schmidt channels, with canonical input, copied verifier and logs. The original files were not overwritten.

The copied interval verifier was rerun at 192 bits and subdivision 16 for degrees 0 through 4. The full accounting script checks its rigorous upper-endpoint enclosures against the rational thresholds, checks every perturbation and gap inequality using exact fractions, and checks the exact degree-three Rayleigh ratio. All checks passed. This completes the missing full-space spectral certificate; it is not a replacement for the already separate stationary existence certificate or for an independent external review of the combined proof.
