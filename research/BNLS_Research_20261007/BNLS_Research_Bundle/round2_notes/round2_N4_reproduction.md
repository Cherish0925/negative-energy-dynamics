# Four-dimensional negative-energy traveling-wave candidate: exact reduction and reproducibility

**Status:** independently reproduced, strongly resolved numerical candidate for the actual N>=2 problem. These computations are not an interval-certified existence proof on R^4. In particular, the periodic computational box is not silently identified with R^4.

## 1. Target, signs, and what an exact profile would imply

We use

\[
i\partial_tu=\Delta^2u-|u|^2u\quad\text{on }\mathbb R^4,
\qquad E(u)=\frac12\int|\Delta u|^2-\frac14\int|u|^4.
\]

The exponent 2 is exactly 8/N for N=4. A traveling profile at frequency omega=1 and velocity v e_1 obeys

\[
\Delta^2 Q+Q+i v\partial_1Q-|Q|^2Q=0.\tag{1}
\]

If an exact H^2(R^4) profile Q with E(Q)<0 is certified, then

\[
u(t,x)=e^{it}Q(x-vt e_1)
\]

is an explicit global solution for every real t. Substitution gives i u_t=e^{it}(-Q-i v Q_1), exactly matching the right-hand side by (1). Translation and constant phase multiplication are unitary on H^2, so its H^2 norm is constant for all time. It therefore never has finite- or infinite-time growth in this norm. Such a profile would disprove the universal nonradial negative-energy blow-up assertion, not merely provide a slower blow-up example.

This is conditional on exact real-space profile existence, which remains to be certified.

## 2. Exact axial reduction, not a dimensional approximation

Write x=(s,z), s=x_1 in R, z in R^3, r=|z|. Restrict only to O(3) symmetry in z, allowing arbitrary dependence on s. Let

\[
W(s,r)=r Q(s,r).
\]

Because the transverse dimension is exactly three,

\[
\Delta_{\mathbb R^4}Q
=\left(\partial_s^2+\partial_r^2+\frac2r\partial_r\right)Q
=\frac{(\partial_s^2+\partial_r^2)W}{r}.
\]

Applying the same identity twice gives

\[
\Delta_{\mathbb R^4}^2Q=\frac{(\partial_s^2+\partial_r^2)^2W}{r}.
\]

Thus (1) is exactly equivalent, for r>0, to

\[
(\partial_s^2+\partial_r^2)^2W+W+i v W_s
-\frac{|W|^2W}{r^2}=0.\tag{2}
\]

Extend W oddly in the signed r variable. A smooth odd W has W=r a(s,r^2) near r=0, so Q=W/r extends smoothly and evenly there. Equation (2) also extends smoothly: |W|^2W/r^2 vanishes at r=0. No physical boundary or external potential has been introduced by this exact algebraic transformation. The computational truncation described below does introduce a finite-box approximation.

We impose the additional exact symmetry

\[
W(-s,r)=\overline{W(s,r)},\qquad W(s,-r)=-W(s,r).
\]

Its real part is even in s; its imaginary part is odd in s. These conditions preserve the traveling profile equation and remove the phase and longitudinal translation kernel directions at the real radial seed.

## 3. Correct integration constants

The area of the transverse unit sphere S^2 is 4 pi. After doubling the radial half-line, for a decaying smooth W,

\[
M(Q)=2\pi\int_{\mathbb R^2}|W|^2\,ds\,dr,
\]

\[
P_1(Q)=2\pi\int_{\mathbb R^2}\operatorname{Im}(\overline W W_s)\,ds\,dr,
\]

\[
E(Q)=2\pi\int_{\mathbb R^2}
\left(\frac12|\Delta_2W|^2-\frac14\frac{|W|^4}{r^2}\right)ds\,dr.
\]

Likewise ||Delta_4 Q||_2^2=2 pi integral |Delta_2 W|^2. Integration by parts gives ||grad_4 Q||_2^2=2 pi integral (|W_s|^2+|W_r|^2). These are the constants used in the code; all reported energies are the original four-dimensional energy.

At the axis, the nonlinear energy integrand |W|^4/r^2 has limit zero, so the discrete axis contribution is set to zero. When displaying Q itself at the axis, its correct value is W_r(s,0), not zero.

## 4. Seed and independent response check

The seed was supplied by the radial excited-state continuation in `round2_radial_mode1_dim4.npz`, containing r, y=(q,q',Delta q,(Delta q)'), and V for the l=1 response. Its visible structure is a positive core q(0) approximately 6.7216903857 and a negative annular peak near radius 3.375 of height approximately -1.559. There are small oscillatory decaying tails. Its approximate mass is 5317.79224.

The l=1 response is

\[
L_-^{-1}\partial_1q=x_1 V(|x|),\qquad L_-=\Delta^2+1-q^2.
\]

In axial variables, the initial response is chi(s,r)=rs V(sqrt(s^2+r^2)). Independently of the radial BVP inverse, the Fourier implementation solves

\[
(\Delta_2^2+1-q^2)\chi=W_{0,s}
\]

in the real subspace odd in both s and r. Its response form is

\[
I=2\pi\int\chi W_{0,s}.
\]

On the 256^2, side-length 56 grid, this independent inverse gave I=-273.473861912114, matching the separately discretized radial result. The expected small-velocity expansion is

\[
P_1(Q_v)=2vI+O(v^3),\qquad E(Q_v)=\frac{v^2}{4}I+O(v^4).
\]

The initial complex guess is W_0-i v chi. It is only an initial guess: every reported traveling result solves the full complex nonlinear equation (2).

## 5. Exact candidate recipe and numerical solver

Primary script: `round2_N4_axial.py`. Dependencies: NumPy and SciPy.

Run from the folder containing this script and the radial seed:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python round2_N4_axial.py 256 56
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python round2_N4_axial.py 384 56
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python round2_N4_axial.py 384 72
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python round2_N4_axial.py 512 64
```

For N grid points and side length L, s_j=r_j=-L/2+jL/N. Fourier multipliers are

\[
K_v(k_s,k_r)=1+(k_s^2+k_r^2)^2-v k_s.
\]

For the velocities tested, this is strictly positive. The nonlinear root function is

\[
F(W)=W-\Pi K_v^{-1}\left(\frac{|\Pi W|^2\Pi W}{r^2}\right),
\]

where Pi is the odd-r and conjugate-reflection-in-s projection. The identity on components outside this symmetry subspace avoids spurious null directions. SciPy's Krylov nonlinear root solver uses absolute tolerance 2e-11 on this preconditioned residual. The independent scalar response uses GMRES with relative tolerance 2e-10. The radial seed is evaluated using CubicHermiteSpline with supplied values and first derivatives; piecewise linear interpolation is not used.

### Computational boundary assumptions

FFT differentiation uses a periodic square [-L/2,L/2)^2. Oddness forces W=0 on the radial axis and on the signed-r periodic boundary, but it does not enforce an exact infinite-domain stable manifold. The actual profile is extremely small near the boundary. Enlarging L tests this truncation empirically; it is not a proof of an exponentially small domain error. The target remains the decaying R^4 problem, not a torus or a ball problem.

### Residual definitions

- `preconditioned_residual`: maximum absolute component of the stacked real/imaginary F(W).
- `elliptic_residual`: maximum pointwise modulus of Delta_2^2 W+W+i v W_s-|W|^2W/r^2, using spectral derivatives.
- `pohozaev`: direct quadrature E-vP_1/8. The exact identity follows from mass-preserving dilation of the traveling action E+M/2-vP/2.
- All integrals use the periodic trapezoidal rule, multiplied by 2 pi h^2.
- These are floating-point diagnostics, not directed-rounding enclosures.

## 6. Direct nonlinear measurements

At N=256, L=56:

| v | Momentum P_1 | Direct energy E | E-vP_1/8 |
|---:|---:|---:|---:|
| 0.002 | -1.09377281906 | -0.000273443188655 | 1.61e-11 |
| 0.005 | -2.73282322955 | -0.00170801449693 | 2.15e-11 |
| 0.010 | -5.45417351246 | -0.00681771703382 | -1.43e-10 |
| 0.020 | -10.81713905658 | -0.02704284762443 | 1.70e-11 |

At fixed v=0.02, refining both resolution and domain:

| Grid | Side L | Direct E | E-vP/8 | Elliptic residual sup |
|---:|---:|---:|---:|---:|
| 256^2 | 56 | -0.02704284762443 | 1.70e-11 | 1.54e-10 |
| 384^2 | 56 | -0.02704284762616 | 1.53e-11 | 1.48e-9 |
| 384^2 | 72 | -0.02704284764252 | -1.07e-12 | 5.41e-10 |
| 512^2 | 64 | -0.02704284764087 | 5.73e-13 | 3.64e-9 |

The standing v=0 profile has energy approximately zero (2.24e-11 on the first grid), rather than a spurious negative offset of the magnitude seen above.

For N=384, L=72, v=0.02, separate norm quadratures give

- mass approximately 5317.7387640176;
- ||grad Q||_2^2 approximately 3361.3213907466;
- ||Delta Q||_2^2 approximately 5317.8469354081;
- ||Q||_4^4 approximately 10635.8020422069;
- standard Bessel H^2 norm squared approximately 17358.2284809188.

These norms would remain constant along the exact linearly drifting solution if the profile is certified.

## 7. A Galilean-boost artifact is excluded

BNLS is not Galilean invariant. More strongly, a nonzero real localized standing profile q cannot be turned into an exact traveling profile merely by Q=e^{iks}q, even if its frequency is adjusted. Expanding the fourth-order derivative gives the imaginary profile residual

\[
\partial_s\left[4k\Delta q+(v-4k^3)q\right].
\]

If it vanished, decay in s forces the bracket to vanish. For k nonzero this makes q an L^2 eigenfunction of the Laplacian on R^4, which does not exist. For k=0 and v nonzero, it requires q_s=0, again incompatible with a nonzero localized L^2 profile. This is an analytical exclusion, independent of numerical residuals.

We also fitted the best single linear-phase boost of the standing profile at v=0.02, optimizing both k and the frequency to minimize its transformed L^2 residual. Its best residual was approximately 0.3654434, whereas the actual full complex solution had residual approximately 3.56e-9. The optimized boost had positive energy approximately 0.0182716 and positive momentum approximately 10.1246, opposite to the observed negative-energy branch.

The exact independent phase-modulation identity is

\[
vM=4\int\xi_1|\xi|^2|\widehat Q(\xi)|^2d\xi.
\]

In the axial representation its third moment is 2 pi integral Im(conjugate(W_s) Delta_2 W). At v=0.02 the check vM-4J_3 was approximately 7.7e-13, even though P_1 is negative. Thus the sign is consistent with fourth-order dispersion; group transport and the first Fourier moment need not point in the same direction.

Control script: `round2_N4_boost_control.py`; output: `round2_N4_boost_controls.json`.

## 8. Numerical invertibility diagnostics for the remaining proof

In the PT/O(3) space, write K=Delta_2^2+1. We computed the compact positive operators C_-=K^-1/2 q^2 K^-1/2 on real odd-s/odd-r functions and C_+=3K^-1/2 q^2 K^-1/2 on real even-s/odd-r functions. The Hessians are congruent to I-C_±.

For C_-, the largest eigenvalues were approximately
1.04260968448, 0.44461530981, 1/3, 0.17416572595, ... .
Thus the nearest preconditioned Hessian eigenvalue to zero is approximately -0.04260968448.

For C_+, the largest eigenvalues were approximately
5.39609155223, 3, 2.11809783400, 0.81487521981, 0.74050751316, ... .
The nearest Hessian eigenvalue to zero is approximately +0.18512478019.

The relevant candidate is therefore not numerically close to a zero mode after removing symmetries. However, these numerical spectra do not prove that all omitted modes are controlled.

For angular l modes in R^4, the exact Rellich lower bound is

\[
\int|\Delta_l f|^2r^3dr\ge[l(l+2)]^2\int|f|^2r^{-1}dr.
\]

Sampled values of sup r^4(cq^2-1)_+ were approximately 239.49209 for c=1 and 1183.78043 for c=3. If these were enclosed rigorously, high angular modes l>=4 (minus) and l>=5 (plus) would be positive. With the PT parity, only L_- modes l=1,3 and L_+ modes l=0,2,4 would then require individual certified spectral estimates.

Remaining rigorous work: certify a decaying standing profile, enclose the relevant inverse/spectral bounds and the negative response form, then apply a quantitative symmetry-restricted implicit-function theorem; or certify a finite-v profile directly with an infinite-domain Newton enclosure and a strictly negative energy interval. No such enclosure is claimed in these files.

## 9. Data map

- `round2_N4_axial.py`: independent exact-reduction solver and response inversion.
- `round2_N4_axial_results.jsonl`: all nonlinear grid/domain/velocity measurements.
- `round2_N4_axial_linear.jsonl`: independent response forms.
- `round2_N4_axial_N*_L*_v*.npz`: coordinate vectors and complex W snapshots; Q=W/r with axis value W_r.
- `round2_N4_spectrum.py`, `round2_N4_spectrum_results.json`: compact spectrum diagnostics and angular bounds.
- `round2_N4_boost_control.py`, `round2_N4_boost_controls.json`: explicit phase-boost controls and third-moment identity.
- `round2_N4_norms.json`, `round2_N4_tail_samples.json`: direct norm and tail samples.
- `round2_N4_profile.png`: real/imaginary profile image, explicitly labeled numerical candidate.

No novelty claim is made. The strength of these computations is independent dimensional reduction, actual nonlinear traveling profiles, multiple velocities, grid/domain agreement, two independent identities, and explicit elimination of a simple boost artifact. Their remaining limit is mathematical certification on R^4.
