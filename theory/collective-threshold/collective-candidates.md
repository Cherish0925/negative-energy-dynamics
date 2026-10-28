# collective occupation candidates at the two-dimensional LT endpoint

2026-10-11. This note concerns the equal-occupation kinetic quotient

$$
 R(\phi)=\frac{\int(\sum_j|\phi_j|^2)^2}
                 {\sum_j\int|\nabla\phi_j|^2},\qquad
 \langle\phi_i,\phi_j\rangle=\delta_{ij}.
$$

The target is to decide whether any finite rank exceeds
`C1 = 2/Mc ≈ 0.17092707344864`. Equivalently, the potential quotient is
`L1 = 1/(2 Mc) ≈ 0.04273176836216`.
No above-target candidate or general proof was obtained in this branch.
There is one exact family-wide obstruction and two numerical periodic searches.
The obstruction is a short consequence of classical one-dimensional theory;
no historical novelty is asserted.

## 1. Complete Cartesian-product occupation cannot exceed 1/6

Let `f_1,...,f_m` and `g_1,...,g_n` be arbitrary orthonormal H1 families on R.
Occupy the **entire** Cartesian product

$$
 \phi_{ij}(x,y)=f_i(x)g_j(y),\quad 1\le i\le m,\quad1\le j\le n.
$$

No Gaussian assumption, common scale, positivity, or weak secondary
occupation enters. Define

$$
 A_f=\sum_i\|f_i'\|_2^2,\quad
 B_f=\int(\sum_i|f_i|^2)^2,
$$

and similarly for g. The sharp one-dimensional LT inequality at exponent
3/2 gives

$$
 B_f^2\le m A_f/3.                                      \tag{1}
$$

For completeness, take `V=alpha rho_f`, use the variational principle,
Hölder on the first m negative eigenvalues, and
`Tr(-d²/dx²-V)_-^(3/2) <= (3/16) integral V²`. This yields

$$
 A_f\ge\alpha B_f-(3/16)^{2/3}\alpha^{4/3}B_f^{2/3}m^{1/3}.
$$

Maximizing the right side over alpha gives `A_f >= 3 B_f²/m` exactly.
The product density and kinetic trace are

$$
 F=B_fB_g,\qquad T=nA_f+mA_g.
$$

Therefore

$$
 \boxed{R\le\frac{\sqrt{mnA_fA_g}/3}{nA_f+mA_g}
                \le\frac16 < \frac2{M_c}.}             \tag{2}
$$

The constant 1/6 is sharp in this class: for m=n=1, normalized sech profiles
with matched kinetic scales attain it. For fixed higher m,n, take widely
separated equal-width one-dimensional sech profiles, orthonormalize their
vanishing overlaps, and match the two directional kinetic traces. The
quotient tends to 1/6. Spatial rotations preserve the assertion.

**Limit:** This does not cover a nonrectangular selection of product orbitals,
or arbitrary entangled/nonseparable orbitals. In particular, a Fermi-energy
cutoff in a separable Hamiltonian selects `e_i+e_j<mu`, usually a triangular
or curved subset rather than the full Cartesian product. Thus (2) does not
exclude the next periodic search.

The primary historical input is the classical sharp one-dimensional LT
inequality. A modern primary source discussing its relation to orthonormal
cubic NLS and nonattainment is Frank--Gontier--Lewin, *The nonlinear
Schrödinger equation for orthonormal functions II*, CMP 384 (2021),
https://arxiv.org/abs/2002.04964 and
https://doi.org/10.1007/s00220-021-04039-5.

## 2. Periodic candidates and their relevance

For a potential periodic with square cell `[0,2pi]^2`, let `P(V)` be the
negative spectral trace per unit area of `-Delta-V`. The periodic ratio is

$$
 L_{\rm per}(V)=P(V)/\langle V_+^2\rangle.
$$

A ratio strictly above L1, with a certified margin, would contradict the
whole-space inequality: cutoff over increasingly many cells and use the
vanishing boundary/volume ratio (or the standard equality of periodic and
whole-space LT constants). We do not make that conclusion from discretized
values below L1.

If V has a negative part, using the spectrum of V but charging only
`integral V_+²` gives a **lower bound** on the true ratio for the nonnegative
potential V_+, because replacing V by V_+ only lowers the Schrödinger
operator. Thus our positive-part-cost experiment can certify a counterexample
if high enough, but its failure does not exclude the actual clipped potential.

For reference, a uniform potential has

$$
 L_{\rm cl}=1/(8\pi)=0.03978873577297,
$$

about 6.89% below L1 when divided by L1.

### 2a. Separable trigonometric potential

We computed all negative combinations of the one-dimensional Bloch bands for

$$
 V=c+a(\cos x+\cos y)+b(\cos2x+\cos2y).
$$

For each Bloch momentum `k in [-1/2,1/2)`, the one-dimensional plane-wave
matrix has diagonal `(ell+k)^2` and off-diagonals `-a/2,-b/2`. The negative
two-dimensional levels are `e_i(kx)+e_j(ky)-c`. The trace is divided by cell
area `(2pi)^2`; the momentum integral uses the full Brillouin zone.

Differential-evolution and Nelder--Mead searches, including negative c and
positive-part denominator, returned near-semiclassical configurations.
One recorded point is

`(c,a,b)=(2.00054357,0.7283338,0.08201107)`.

Bloch meshes 40,80,160 give approximately

`0.0397893913, 0.0397884915, 0.0397886411`.

The sign-changing quadrature drift is important: coarse momentum meshes can
create a false apparent improvement over the semiclassical constant. These
values are far below L1. There is no proof excluding this potential family.

### 2b. Nonseparable square lattice of Gaussian wells

We then used a genuinely nonseparable potential,

$$
 V(x,y)=A\sum_{z\in\mathbb Z^2}
       e^{-| (x,y)-2\pi z|^2/(2\sigma^2)}+c.
$$

Its Fourier coefficients are

$$
 \widehat V_m=\frac{A\sigma^2}{2\pi}e^{-\sigma^2|m|^2/2}
                     +c\,\mathbf1_{m=0}.
$$

The Bloch matrix on plane waves `ell in [-ncut,ncut]^2` is consequently exact
within that finite basis. We varied well depth, well width and background,
including `c<0`; positive-part cost was used. A two-stage numerical search
produced

`A=2.9414883, sigma=0.73521703, c/A=0.01513357`.

Here V is positive, so no clipping issue arises. At a 12-by-12 positive-quadrant
Bloch mesh, plane-wave cutoffs 8,12,16 give

| Plane-wave cutoff | Periodic ratio |
|---|---:|
| 8 | 0.04256185612410 |
| 12 | 0.04256185612635 |
| 16 | 0.04256185612635 |

The associated quotient is approximately **0.398% below the scalar target**.
This is above the uniform gas value, but below the value needed to refute the
conjecture. A final 24-by-24 momentum check is recorded in the JSON.

At the sampled high-symmetry points, the first band ranges from approximately
-0.7033 to -0.6321; the second band is positive (0.1210 at `(1/2,0)`). This
supports interpreting the candidate as a band formed from one localized
bound state per cell, not a demonstrated many-band collective enhancement.
The high-symmetry samples alone do not certify a full band gap.

## 3. Numerical versus continuum statements

The Cartesian-product bound (2) is a continuum analytic statement. In the
periodic calculations, finite plane-wave Ritz truncation underestimates the
negative spectral trace at each fixed momentum. However, the numerical Bloch
quadrature and potential quadrature are not interval-enclosed. Their observed
convergence is not a rigorous upper bound or a proof of global optimality.
No conclusion excluding periodic organization, nonrectangular product shells,
or general high-rank concentration follows from these negative searches.

The reproducible code is [r20_collective_candidates.py](../../computations/collective-threshold/r20_collective_candidates.py); default mode
rechecks the recorded candidates and writes
[r20_collective_candidates_results.json](../../computations/collective-threshold/r20_collective_candidates_results.json). `--search` repeats the
Gaussian-lattice parameter optimization. Run with

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/r20_collective_candidates.py
```

The meaningful distinction exposed here is between complete separable
occupation (rigorously bounded by 1/6) and genuinely two-dimensional collective
organization. The latter is the unresolved issue; numerical absence of an
above-threshold state is not its solution.
