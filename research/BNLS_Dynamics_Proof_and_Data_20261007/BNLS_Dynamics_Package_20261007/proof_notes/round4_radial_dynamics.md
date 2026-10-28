# Radial Hamiltonian diagnostics and the remaining two unstable dimensions

2026-10-07. **This file reports numerical discovery and a precise certification route. It does not claim an exact radial quartet or an exact unstable dimension 31.** The independent exact Morse/kernel certificate remains separate.

## 1. Findings

For the exact stationary branch let
\[
 f=\partial_\omega Q=\frac12Q+\frac14rQ',\qquad
 z=(L_-|_{Q^\perp})^{-1}f,\qquad \gamma=\langle f,z\rangle.
\]
The radial inverse exists modulo the exact phase kernel by the completed full certificate; critical scaling gives `f⊥Q`. Numerical calculations using the canonical profile consistently give **positive** gamma, approximately
\[
 \gamma\approx981.35577330.
\]
This rules out using a negative-gamma numerical hypothesis to force one radial real eigenpair. It does not prove the sign for exact Q.

A separate radial Hamiltonian eigenvalue computation finds a robust complex quartet. With free decaying Bessel boundary conditions, the first-quadrant candidate is
\[
 \lambda\approx2.92085287365+6.32239174232\,i.
\]
Its real part is comfortably positive. If rigorously certified for the exact Q, the quartet supplies two real unstable dimensions. Combined with the 29 already certified nonradial unstable dimensions, persistence and the full index 31 would then force exactly 31 unstable dimensions for sufficiently small nonzero speed.

## 2. Two independent numerical approaches

### Generalized-zero-chain inverse pairing

A finite-difference saddle solve imposes the orthogonality to Q explicitly and solves the projected equation. For mesh widths `.08,.04,.02,.01`, the computed full pairings are approximately `990.515,983.872,982.040,981.541`. Radii 40 and 50 agree within `10^-8` at the last mesh. The slow mesh convergence comes from the transformed radial origin discretization.

A distinct adaptive radial boundary-value solve uses the untransformed regular radial system and the integral orthogonality constraint. Its results are:

| radius | requested tolerance | gamma | reported maximum RMS residual |
|---:|---:|---:|---:|
| 30 | `1e-7` | 981.3557733990397 | `9.99e-8` |
| 40 | `1e-8` | 981.3557733073701 | `9.98e-9` |
| 50 | `1e-8` | 981.3557733031746 | `9.99e-9` |

The saddle multiplier is about `-3e-12` in the last two solves. These are floating-point consistency checks, not error bounds on the exact continuum inverse pairing.

### The nonzero quartet

On the transformed radial grid, the Hamiltonian matrix is
\[
 \mathcal A_0=\begin{pmatrix}0&L_-\\-L_+&0\end{pmatrix}.
\]
The first-quadrant candidate converges as follows:

| mesh width | radius | candidate |
|---:|---:|---|
| .08 | 30 | `2.95713373665 + 6.39869504050 i` |
| .04 | 40 | `2.93076848857 + 6.34361179924 i` |
| .02 | 40 | `2.92354576444 + 6.32823395191 i` |
| .01 | 40 | `2.92157989529 + 6.32398578406 i` |
| .005 | 40 | `2.92104795211 + 6.32282244001 i` |

The discretized long generalized-zero chain also splits into a spurious small quartet tending toward zero. Those near-zero eigenvalues are explicitly excluded from the claimed discovery evidence.

The nonzero eigenmode decays more slowly than Q. Simple clamped boundary conditions at radius 30 shift the candidate at roughly the `10^-4` level. We therefore replaced them by the exact free decaying boundary relation for the compact canonical potential.

Writing `z=a+ib`, `w=a−ib`, the far-field equations are
\[
 (\Delta^2+1-i\lambda)z=0,\qquad
 (\Delta^2+1+i\lambda)w=0.
\]
For either scalar coefficient `c=1∓iλ`, the decaying radial solutions in four dimensions are
\[
 r^{-1}K_1(\kappa_jr),\qquad \kappa_j^4=-c,\quad\Re\kappa_j>0.
\]
There are two such roots. Their logarithmic derivatives at radius R are
\[
 d_j=-\frac2R-\kappa_j\frac{K_0(\kappa_jR)}{K_1(\kappa_jR)}.
\]
The exact free boundary map for `(F,F',ΔF,(ΔF)')` is
\[
 \binom{\Delta F}{(\Delta F)'}=
 \begin{pmatrix}\kappa_1^2&\kappa_2^2\\
 \kappa_1^2d_1&\kappa_2^2d_2\end{pmatrix}
 \begin{pmatrix}1&1\\d_1&d_2\end{pmatrix}^{-1}
 \binom{F}{F'}.
\]
At R≥36 this is the genuine whole-space boundary condition for the compact canonical q. The final computation uses a real 16-component system with two real eigenvalue parameters, avoiding the convergence failure observed in an earlier complex-variable solver call.

| radius | requested tolerance | first-quadrant candidate | reported max RMS residual |
|---:|---:|---|---:|
| 30 | `1e-7` | `2.920852873840728 + 6.322391742494979 i` | `9.998e-8` |
| 36 | `1e-8` | `2.920852873628844 + 6.322391742340717 i` | `9.980e-9` |
| 40 | `1e-8` | `2.920852873657242 + 6.322391742298660 i` | `9.975e-9` |

The R30 row neglects the tiny nonzero canonical potential between 30 and 36. The R36 and R40 rows have no such potential-tail truncation. Their agreement is numerical evidence, not a substitute for interval enclosures of the differential system and the boundary map.

## 3. A concrete validated route

Let `A=Δ²+1` and `K_Q=A^{-1/2}Q²A^{-1/2}`. For `Re λ>0`, define bounded Fourier multipliers
\[
 R_\mp(\lambda)=A(A\mp i\lambda)^{-1}.
\]
The complex eigenvalue equations are equivalent to the analytic compact operator problem
\[
 \binom{Z}{W}=
 \begin{pmatrix}R_-(\lambda)&0\\0&R_+(\lambda)\end{pmatrix}
 \begin{pmatrix}2K_Q&K_Q\\K_Q&2K_Q\end{pmatrix}
 \binom{Z}{W},
\]
where `Z=A^{1/2}z`, `W=A^{1/2}w`. Thus one may certify a zero of an analytic Fredholm determinant by a finite-rank reduction with a uniform resolvent bound on a contour surrounding the candidate.

The exact profile-transfer estimate is already available:
\[
 \|K_Q-K_q\|\le\delta=312009/64000000.
\]
For `λ=α+iβ`, `α>0`,
\[
 \|R_\pm(\lambda)\|\le\sqrt{1+\beta^2/\alpha^2}.
\]
Consequently the block-operator transfer is bounded by
\[
 3\delta\sqrt{1+\beta^2/\alpha^2}.
\]
This lets a validated contour for the canonical q be transferred to the exact Q, provided the finite-rank inverse estimate dominates that explicit perturbation.

The current two radial Ritz vectors are not by themselves sufficient for this nonselfadjoint contour calculation. Their certified coefficient-one Hilbert--Schmidt remainder is bounded only by
\[
 \sqrt{(38.80-5.395^2-2.999^2)/9}\approx0.279.
\]
After multiplication by the block coefficients and the free resolvent in the candidate region, the crude error is about 2. Such a bound cannot justify ignoring the complement. Additional compact radial modes, or a validated ODE/Evans-function argument with interval Bessel boundary values, are needed. The necessary new proof obligation is now sharply identified: enclose an isolated first-quadrant eigenvalue and transfer it from q to Q.

A small numerical eigenpair residual alone does not complete this step, because the operator is non-self-adjoint and no adequate global inverse estimate has yet been proved on the complement.

## 4. Reproduction

- `round4_radial_dynamics_numeric.py/.json`: projected inverse and finite-difference diagnostics.
- `round4_radial_dynamics_quartet.py/.json`: targeted quartet refinement; the NPZ vector is a numerical initial guess.
- `round4_radial_dynamics_chain.py/.json`: independent adaptive radial inverse pairing; saved radial profiles at radii 30,40,50.
- `round4_radial_dynamics_outgoing_real.py/.json`: final Bessel-boundary quartet solve. It reads the canonical q and the saved clamped initial guess `round4_radial_dynamics_bvp_R30.npz`; the initial guess does not enter any mathematical certification claim.
- `round4_radial_dynamics_outgoing_real_R40.npz`: final numerical candidate profile, useful for an interval residual or Evans-function certificate.

The earlier complex-variable outgoing solver did not converge; its failed output must not be interpreted as a certificate. The final real-system solver succeeded at all three reported radii.
