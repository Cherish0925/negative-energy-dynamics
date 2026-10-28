# A certified radial Hamiltonian quartet for the exact N4 profile

2026-10-07. This note proves a continuum eigenvalue existence statement. The
finite matrix, whole-space residual, exact-profile transfer and positive
infinite-dimensional complement are all used. No eigenvalue conclusion is
inferred from a residual alone.

## 1. Exact conclusion and inputs

Let Q be the exact stationary profile singled out by the frozen N4 certificate,

\[
(\Delta^2+1)Q-Q^3=0,\qquad
L_+=\Delta^2+1-3Q^2,\quad L_-=\Delta^2+1-Q^2,
\]

and restrict the real Hamiltonian generator

\[
\mathcal A_Q=\begin{pmatrix}0&L_-\\-L_+&0\end{pmatrix}
\]

to radial functions. There is exactly one eigenvalue, counted with algebraic
multiplicity, in

\[
\boxed{\ 1.5<\Re\lambda<4.5,\qquad4.5<\Im\lambda<7.5\ }.
\]

Consequently it is algebraically simple in the radial sector. The real
Hamiltonian symmetries give the simple radial quartet
\(\lambda,\bar\lambda,-\lambda,-\bar\lambda\). This contributes two real
unstable dimensions.

The numerical value \(2.9208528736+6.3223917423i\) was used to choose trial
functions and a contour. The certified location is the rectangle above, not
an error bar around those numerical digits.

The required exact inputs are:

* the unchanged rational q with SHA256
  `c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627`;
* \(\|Q-q\|_Z\le3\cdot10^{-7}\), proved by the new mixed-residual refinement
  of the **same** exact Q, and \(\|q\|_Z<104\), \(\|q\|_\infty<6.73\);
* \(\|\Delta^2q+q-q^3\|_2<0.000242\);
* the full radial Morse certificate: three negative Hessian directions in
  total, one phase kernel, and nonzero preconditioned spectral gap \(>1/29\).

Here \(\|u\|_Z^2=\|\Delta u\|_2^2+\|u\|_2^2\). Omitting the common spherical
area \(2\pi^2\) gives an equivalent radial Hilbert norm; the finite-block
calculations consistently use \(r^3dr\). Global profile errors are divided by
\(\sqrt{2\pi^2}\) when passed into those radial norms.

## 2. Why a seven-dimensional block suffices

Work in the Z-Hilbert quotient by the exact phase vector \(e=(0,Q)\), represented
by its Z-orthogonal complement. Let \(\Pi\) be the exact orthogonal projection.
The induced generator and energy operator are

\[
 A=\Pi\mathcal A_Q,\qquad H=(\Delta^2+1)^{-1}\operatorname{diag}(L_+,L_-).
\]

On this quotient H is bounded, self-adjoint, invertible, has exactly three
negative directions, and has a positive essential part. The frozen spectral
bound gives \(\|H^{-1}\|<29\); the Hilbert--Schmidt bounds and profile transfer
give \(\|H\|<6\). Indeed the radial coefficient-three Birman–Schwinger norm is at most \(\sqrt{38.80}+3\delta<7\), where \(\delta=(2\cdot104\rho+\rho^2)/256\); hence \(\|I-K_{3,Q}\|<6\), and the coefficient-one bound is smaller.

The phase quotient is an actual group quotient: \(\mathcal A_Qe=0\), so the
linearized group preserves the removed one-dimensional space. Its energy
identity is \(H A+A^*H=0\).

The trial block contains four real directions of a candidate quartet, together
with three approximate zero-chain directions. If \(a,b\) are complex radial
candidate components, take

\[
 V_0=(\Re a,\Re b),\quad V_1=(\Im a,\Im b),\quad
 V_2=(\Re a,-\Re b),\quad V_3=(\Im a,-\Im b),
\]
\[
 V_4=(f,0),\qquad V_5=(0,z),\qquad V_6=(h,0).
\]

The approximate chain equations are
\(L_+f=-q\), \(L_-z=f\), \(L_+h=z\). The actual trial functions are compact,
C5 piecewise polynomials of degree 11, with rational coefficients specified
by exact dyadic endpoint jets. Their odd origin jets of orders 1,3,5 vanish.
Their derivatives through order 5 vanish at the compact endpoint. They
therefore belong to the whole-space radial H6 domain of the generator.

The fixed dyadic matrix C defines W=\(\Pi VC\). The explicit reference matrix is
\(B_0=C^{-1}B_{\rm raw}C\), where

\[
 B_{\rm raw}=\operatorname{diag}\left(
 \begin{pmatrix}\alpha&\beta\\-\beta&\alpha\end{pmatrix},
 \begin{pmatrix}-\alpha&-\beta\\\beta&-\alpha\end{pmatrix},
 \begin{pmatrix}0&1&0\\0&0&-1\\0&0&0\end{pmatrix}\right).
\]

The parameters alpha,beta are the exact dyadic numbers saved as hexadecimal
strings. This block has exactly one algebraically simple eigenvalue in the
chosen first-quadrant rectangle.

## 3. Positive complement and the quantitative Schur argument

The complete theorem, including the generator-domain and quotient argument,
is in Section 7 of `round5_radial_analytic.md`. Its form used here is recorded
for clarity.

Suppose \(G=W^*HW\) is invertible and has all three negative directions. Then

\[
 P_E=WG^{-1}W^*H,\qquad P_C=I-P_E
\]

are the energy-orthogonal projections onto the finite block and its complement.
The complement is positive and coercive. For

\[
 g\ge\|G^{-1}\|,\quad w\ge\|W\|,\quad M\ge\|H\|,\quad
 q_c=1+w^2gM,
\]

one has \(\|P_C\|\le q_c\). The compressed complement generator is
skew-adjoint in its positive energy norm and has resolvent at most
\(1/\Re\lambda\) there. Bounded off-diagonal blocks follow from the finite
trial vectors lying in D(A) and the energy identity; removing these bounded
blocks preserves the group generator property.

Let \(\|AW-WB_0\|\le\epsilon\), and let B be the exact compressed finite
matrix. Suppose

\[
 \|B-B_0\|\le\delta_B,
 \quad \sup_{\lambda\in\Gamma}\|(B_0-\lambda)^{-1}\|\le k,
 \quad\inf_{\lambda\in\Gamma}\Re\lambda\ge\alpha_\Gamma>0.
\]

The off-diagonal Schur correction is bounded by
\(gM q_c^2\epsilon^2/\alpha_\Gamma\). Thus

\[
\boxed{\quad k\left(\delta_B+
\frac{gM q_c^2\epsilon^2}{\alpha_\Gamma}\right)<1\quad}
\]

transfers the algebraic eigenvalue count from B0 to the full quotient generator.
The determinant involved is only seven dimensional; the infinite-dimensional
complement is controlled by its positive conserved energy. Homotopy of the
bounded off-diagonal blocks, followed by the finite matrix homotopy, gives the
count through the analytic Schur determinant throughout the right half-plane.

Using the directly integrated compressed matrix is essential here. Estimating
\(B-B_0\) merely by the H2 residual would discard useful cancellation and give
a much weaker bound.

## 4. What is integrated rigorously

The verifier reconstructs every Hermite polynomial from its exact endpoint
jets at 384-bit Arb precision. It refines at the union of the frozen q knots
and trial-function knots. All quadratic forms and residual norms are integrals
over this whole compact support. No sampled residual, finite-difference
spectral approximation or unbounded-domain truncation enters the certificate.

For radial functions in four dimensions,

\[
\Delta u=u''+3u'/r,
\]
\[
\Delta^2u=u^{(4)}+6u'''/r+3u''/r^2-3u'/r^3,
\]
\[
\Delta^3u=u^{(6)}+9u^{(5)}/r+9u^{(4)}/r^2
 -12u'''/r^3+9u''/r^4-9u'/r^5.
\]

At the origin these are evaluated coefficientwise using the exact even low
jets, so no division by zero is used. Away from the origin the residual and
its Laplacian are represented by the polynomial numerators \(r^3R\) and
\(r^5\Delta R\). Their squared integrals have weights \(r^{-3}\) and
\(r^{-7}\). Replacing those positive weights by their left-endpoint upper
bounds gives rigorous H2 residual upper bounds.

The energy Gram matrix uses exact polynomial integrals. The skew matrix uses

\[
 K_{ij}=\langle L V_i,J L V_j\rangle_{L^2},\qquad B_q=G_q^{-1}K_q.
\]

To evaluate the signed integrals in K, expand \(r^{-3}\) about a cell midpoint m:

\[
 r^{-3}=m^{-3}\sum_{n=0}^{39}(-1)^n {n+2\choose2}
 [h(t-1/2)/m]^n+\mathcal E.
\]

On every cell away from zero, \(\eta=h/(2m)\le1/3\), and

\[
 |\mathcal E|\le m^{-3}{42\choose2}\eta^{40}
 (1-43\eta/41)^{-1}.
\]

The polynomial coefficient sum bounds the other factor in the remainder
integral. Therefore the result is an interval enclosure of the signed integral,
not a quadrature guess. Bernstein convex-hull estimates bound the pointwise
norms of U, U', Delta U, 2qU and its corresponding derivatives.

The finite block certificate gives

\[
 n_-(G_q)=3,\quad \|G_q^{-1}\|<5.858013,
\]
\[
 \|W_q^*W_q-I\|<3.8\cdot10^{-6},\quad
 \|R_q C\|<0.002949489,
\]
\[
 \|B_q-B_0\|<9.706\cdot10^{-9}.
\]

The small diagonal LDL pivots of the candidate quartet Gram are not used as
perturbation margins. Inertia is transferred through the **full inverse norm**
and a nonsingular straight-line homotopy of the Gram matrix.

## 5. Transfer to the exact stationary profile

Put \(v=Q-q\), \(\rho=3\cdot10^{-7}\), and \(X=\|(\Delta^2+1)v\|_2\).
Fourier Cauchy--Schwarz and interpolation give

\[
 \|v\|_\infty\le(24\sqrt3\pi)^{-1/2}\sqrt{\rho X}
 <0.088\sqrt{\rho X}.
\]

The stationary equation and the frozen L2 residual imply

\[
 X\le3(6.73)^2\rho+3(6.73)(0.088)\rho^{3/2}\sqrt X
 +(0.088)^2\rho^2X+0.000242.
\]

The positive root of this quadratic inequality in \(\sqrt X\) is below
\(\sqrt{0.0003}\). Hence

\[
 X<0.0003,\qquad \|v\|_\infty<8.4\cdot10^{-7}.
\]

This is an inequality for the already existing H4 difference, so no bootstrap
assumption of a small H4 norm is made.

For each scalar normalized trial U, write

\[
 (Q^2-q^2)U=(2qU)v+Uv^2.
\]

The certified suprema of \(g=2qU\), g', Delta g imply

\[
 \|gv\|_{Z,rad}\le\rho_{rad}
 \sqrt{\|g\|_\infty^2+
 (\|g\|_\infty+\sqrt2\|g'\|_\infty+\|\Delta g\|_\infty)^2}.
\]

The quadratic term follows by differentiating Uv2. The frozen embedding
\(\|f\|_4\le\|f\|_Z/4\), applied to the components of grad v, gives
\(\|\nabla v\|_4^2\le\rho X/16\); this controls its \(|\nabla v|^2\) term.
The explicit formulas are in `round5_radial_quartet_certificate.py`.

In the phase quotient the remaining approximate phase term is
\(\Pi(0,q)=\Pi(0,q-Q)\). The energy projection is a contraction, so this term
costs at most \(\rho_{rad}\) times the appropriate frozen row norm of C.
Combining the two errors gives

\[
 \epsilon_Q<0.002991362.
\]

The energy perturbation uses the frozen product constant 1/256:

\[
 \|H_Q-H_q\|\le
 \frac{3(2\cdot104\rho+\rho^2)}{256}.
\]

Because \(H_Q(0,Q)=0\), the exact Gram equals the unprojected trial Gram.
The exact compressed skew matrix also equals
\(\langle L_QVC,J L_QVC\rangle\), without numerical knowledge of the phase
projection. The verifier transfers both G and K and then the inverse product.
It obtains

\[
 g<5.858206,\quad w<1.000001876,\quad
 \delta_B<0.000877055,\quad q_c<36.149366.
\]

## 6. Final contour and result

Each of the four sides of the stated rectangle is divided into 160 closed
segments. An acb interval matrix inverse encloses \((B_0-\lambda)^{-1}\) for
every lambda on each entire segment. The Frobenius norm bounds the operator
norm and yields

\[
 k<1.330629,\qquad \alpha_\Gamma=1.5.
\]

The final interval computation proves

\[
 k\left(\delta_B+\frac{g\,6\,q_c^2\epsilon_Q^2}{1.5}\right)
 <\boxed{0.365771}<1.
\]

This closes the exact radial quartet certificate.

The 29 previously established nonradial unstable dimensions persist together
with these two radial dimensions under sufficiently small nonzero traveling
speed. The already proved moving-wave Hamiltonian index is 31. Therefore the
small nonzero-speed branch has exactly 31 real unstable dimensions, and the
same number of stable dimensions. The statement uses sufficiently small speed;
this computation does not supply an explicit velocity threshold.

## 7. A qualitative consequence: the exact zero-chain sign

The formerly numerical sign
\[
\gamma=\langle f,(L_-|_{Q^\perp})^{-1}f\rangle>0,
\qquad f=\tfrac12Q+\tfrac14rQ',
\]
now follows from the certified quartet and the Morse index, without an additional
inverse-pairing computation. The orthogonality \(\langle f,Q\rangle=0\) follows
from mass-critical scaling. Write \(z=(L_-|_{Q^\perp})^{-1}f\) and
\(h=L_+^{-1}z\). The exact radial kernel statements make both inverses legitimate.

The real four-dimensional quartet spectral space is H-nondegenerate and has
signature (2,2). Indeed, the energy-skew identity pairs a spectral space only
with its reflected space across the imaginary axis. The paired spectral space
is nondegenerate because H is invertible; its two-dimensional stable and unstable
subspaces are individually isotropic, giving exactly two positive and two
negative directions. Hence its energy-orthogonal complement in the phase
quotient is nondegenerate with negative index one.

In that complement the projected zero-chain vectors
\[
e_1=(f,0),\qquad e_2=(0,z),\qquad e_3=(-h,0)
\]
have energy Gram matrix
\[
\begin{pmatrix}
0&0&-\gamma\\
0&\gamma&0\\
-\gamma&0&*\end{pmatrix}.
\]
Projection away from the phase does not change these pairings. Orthogonality of
the zero chain to the nonzero quartet follows recursively from the energy-skew
identity. If gamma were negative, the displayed chain would contain two
negative directions, contradicting the remaining index one. If gamma were zero,
e1 and e2 would be independent and span a two-dimensional totally isotropic
space. A nondegenerate Pontryagin space of negative index one has no such
subspace: projection onto its one-dimensional negative part is injective on a
totally isotropic subspace. Thus gamma is strictly positive.

The original radial zero chain therefore has exactly length four, including the
phase vector. A further preimage would require
\[
\langle L_+^{-1}z,Q\rangle=-\langle z,f\rangle=-\gamma=0,
\]
which is impossible. The radial geometric kernel is one dimensional, so there
are no additional zero chains. Zero lies in the free essential spectral gap;
the relatively compact localized potential leaves it an isolated spectral
point, as required for this Jordan-chain statement.

This argument proves the sign, not a numerical enclosure of gamma's magnitude.

## 8. Reproduction and exact inputs

Python 3 with python-flint 0.9.0 suffices for the new verifiers. The optional
candidate-generation scripts use SciPy, but are not used in any proof check.
With the files in one directory, run:

```
python3 round5_n4_mixed_residual.py
python3 round5_n4_refinement_certificate.py
python3 round5_radial_verify_block.py 2
python3 round5_radial_contour.py
python3 round5_radial_quartet_certificate.py
```

The quartet portion takes roughly 15 seconds on the current environment.
Its frozen trial inputs are:

* `round5_radial_block_exact_h2.json` (the compact rational C5 profiles);
* `round5_radial_block_whitening.json` (the fixed dyadic 7 by 7 change of basis);
* `round2_radial_H4_exact_h1_16.json` (the unchanged canonical q);
* `round2_verify_frozen_ritz.py` (pure exact Hermite helper functions).

The previously delivered base/Morse certificates and the analytic finite-block
theorem remain mathematical dependencies. No NPZ file, BVP solve, finite-
difference eigenpair, floating quadrature or numerical library eigensolver is
read by these proof-checking commands.
