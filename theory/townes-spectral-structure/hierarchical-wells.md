# Two unequal Townes wells in the joint scale limit

**Status.** The argument below proves the stated expansion for Townes wells.
The scalar input is that `h = -Delta - Q^2` has exactly one negative eigenvalue,
`-1`, and has no nonzero bounded distributional solution at zero energy. Those
facts are established analytically in the companion notes
[scattering-sign.md](scattering-sign.md) and [partner-details.md](partner-details.md); no numerical eigenvalue
count is substituted for them here. This result is about the first two
eigenvalues of this specific potential family, not the entire Lieb--Thirring
optimization problem. No historical priority claim is made.

## 1. Statement

Let `Q` be the positive radial solution of

$$
-\Delta Q+Q-Q^3=0\quad\hbox{in }\mathbb R^2,
\qquad M=\int Q^2,\quad q=Q/\sqrt M.
$$

For fixed `z in R^2`, put

$$
V_k(x)=Q(x)^2+k^2Q(kx-z)^2,\quad
H_k=-\Delta-V_k,\quad L=|\log k|,
\qquad k\downarrow0.
$$

Order its negative eigenvalues increasingly. Under the scalar spectral input
above, the first two eigenvalues exist and obey

$$
\lambda_1(H_k)=-1-k^2Q(z)^2+O_z(k^4),
\tag{1}
$$

$$
\boxed{\lambda_2(H_k)
=-k^2+\frac{2\pi k^2 q(z)^2}{L}
+O_z\!\left(\frac{k^2}{L^2}\right).}
\tag{2}
$$

Consequently, with `S_2 = -lambda_1-lambda_2`,

$$
\boxed{S_2(H_k)-\frac1{2M}\int V_k^2
=-\frac{2\pi k^2q(z)^2}{L}
+O_z\!\left(\frac{k^2}{L^2}\right)<0}
\tag{3}
$$

for all sufficiently small `k`. The result includes the concentric case `z=0`.
The error estimates are uniform when `z` belongs to a fixed compact set. They
are not asserted uniformly for `z=z(k)` tending to infinity.

The leading coefficient `2 pi` comes from the local logarithmic singularity
of the two-dimensional Green function. After its deep ground state has been
occupied, the shrinking well raises the broad state's energy to leading order.

## 2. The zero-energy compressed operator

Set

$$
e=Q/\sqrt M,\quad \Pi=I-|e\rangle\langle e|,
\quad K_0(x,y)=-\frac1{2\pi}Q(x)\log|x-y|Q(y),
\quad \Gamma=\Pi(I-K_0)\Pi\big|_{e^\perp}.
\tag{4}
$$

`K_0` is Hilbert--Schmidt: the diagonal logarithmic singularity is locally
square integrable, and `Q` decays exponentially. The scalar spectral input
implies

$$
\Gamma\ge c I\quad\hbox{on }e^\perp
\tag{5}
$$

for some `c>0`.

Here is a proof, including the role of both assumptions. The free
Birman--Schwinger operator has the norm expansion

$$
Q(-\Delta+\alpha^2)^{-1}Q
=\left(\frac{|\log\alpha|}{2\pi}+c_0\right)
 |Q\rangle\langle Q|+K_0+o(1),
\quad c_0=\frac{\log2-\gamma_{\rm E}}{2\pi}.
\tag{6}
$$

For `0<alpha<1`, exactly one of its eigenvalues exceeds `1`. If `Gamma` had a
negative direction, that direction together with `e` would give two such
eigenvalues for small `alpha`, by the two-dimensional min--max principle.
Thus `Gamma >= 0`.

If `phi in e-perp` lay in its kernel, then

$$
(I-K_0)\phi=cQ
$$

for a constant `c`. Let

$$
\psi(x)=c-\frac1{2\pi}\int\log|x-y|Q(y)\phi(y)\,dy.
$$

Since `int Q phi=0`, exponential decay of `Q` and Cauchy--Schwarz imply that
this logarithmic potential is bounded and approaches `c` at infinity.
Locally, it belongs to `H^2`, so is bounded there too. Also `Q psi=phi` and
`(-Delta-Q^2)psi=0`. The zero-energy assumption forces `psi=phi=0`.
Finally, `Gamma` is identity minus a compact operator, so nonnegativity and
trivial kernel imply the strict uniform lower bound (5).

## 3. A regular Green function expansion, with the broad pole removed

Define the broad operator in scaled variables by

$$
h_z=-\Delta_y-Q(y-z)^2,\qquad q_z(y)=q(y-z).
$$

For `delta in [-1/2,1]`, define its reduced resolvent

$$
R_z^{\rm reg}(\delta)
=(h_z+1+\delta)^{-1}
-\frac{|q_z\rangle\langle q_z|}{\delta},
\tag{7}
$$

interpreting the right side by analytic continuation at `delta=0`.
Because the remainder of the spectrum is nonnegative, this is a bounded
analytic family throughout a neighborhood of the stated interval.

Its Green kernel has the local form

$$
R_z^{\rm reg}(\delta;y,y')
=-\frac1{2\pi}\log|y-y'|+g_z(\delta;y,y'),
\tag{8}
$$

where `g_z` and its first `delta` derivative are jointly continuous near
`(y,y')=(0,0)`, uniformly on that interval. Write
`gamma_z(delta)=g_z(delta;0,0)`. The assertions follow from the local
fundamental solution for a smooth bounded Schrödinger potential; subtracting
the isolated eigenprojection removes the only pole in this energy interval.
They can also be obtained by the free-resolvent identity: its logarithmic
kernel is explicit, and convolution of two local logarithmic kernels has a
continuous diagonal value. Resolvent differentiation gives the same property
for the first parameter derivative.

In the original `x` variables introduce the bounded compact operator

$$
K_k^{\rm reg}(\delta)(x,y)
=Q(x)R_z^{\rm reg}(\delta;kx,ky)Q(y).
$$

Equations (8) and exponential decay imply, in operator norm and also after one
`delta` derivative,

$$
K_k^{\rm reg}(\delta)
=\left(\frac{L}{2\pi}+\gamma_z(\delta)\right)
 |Q\rangle\langle Q|+K_0+E_k(\delta),
\qquad\|E_k\|+\|\partial_\delta E_k\|=o(1).
\tag{9}
$$

For clarity, a global uniformity argument is available without assuming that
the local kernel expansion holds at large `x`. Split both multiplication
operators `Q` at `|x|=k^{-1/4}`. In the interior, `|kx|<=k^{3/4}`, so continuity
of `g_z` gives an `o(1)` Hilbert--Schmidt remainder. In the exterior, the
unscaled reduced resolvent and its `delta` derivative have operator norm
`O(k^{-2})`; multiplying by the exponentially small tail of `Q` gives
`O(k^{-2} exp(-c k^{-1/4}))`. The tails of `K_0` and of the rank-one terms are
also negligible. This proves the norm statements in (9).

## 4. Exact pole reduction and the shallow eigenvalue

Set

$$
A_k(\delta)=I-K_k^{\rm reg}(\delta),\qquad
v_k(x)=Q(x)q(kx-z).
\tag{10}
$$

The `e-perp` block of `A_k` is `Gamma+o(1)`, hence uniformly invertible by
(5). Its Schur complement along `e` is

$$
s_k(\delta)=-\frac{M L}{2\pi}+O_z(1),
\tag{11}
$$

uniformly in `delta`. Thus `A_k` is invertible, has exactly one negative
direction, and

$$
\langle Q,A_k(\delta)^{-1}Q\rangle
=\frac{M}{s_k(\delta)}
=-\frac{2\pi}{L}+O_z(L^{-2}),
\quad \|A_k^{-1}Q\|=O_z(L^{-1}),
\quad\|A_k^{-1}\|=O_z(1).
\tag{12}
$$

Since `v_k=q(z)Q+O_z(k)` in `L^2`,

$$
b_k(\delta):=\langle v_k,A_k(\delta)^{-1}v_k\rangle
=-\frac{2\pi q(z)^2}{L}+O_z(L^{-2}).
\tag{13}
$$

In addition, differentiating the inverse and using (9) gives

$$
|b_k'(\delta)|\le C_z(L^{-1}+k)^2=O_z(L^{-2}).
\tag{14}
$$

In fact `b_k'(delta)<=0` exactly: the reduced resolvent derivative is
`-R_z^reg(delta)^2`, a nonpositive operator, and
`b_k'=<A_k^{-1}v_k,(K_k^reg)'A_k^{-1}v_k>`. Thus the left side of
`delta-b_k(delta)=0` is strictly increasing even before its asymptotic size is
estimated.

The eigenvalue equation for `H_k` at `lambda=-k^2(1+delta)` is **exactly**

$$
\delta=b_k(\delta).
\tag{15}
$$

This reduction is also valid at `delta=0`; one need not divide by a pole.
Indeed, write the broad normalized ground state in original variables as
`phi_k(x)=k q(kx-z)`, let `a=<phi_k,psi>`, and set `w=Q psi`.
Projecting the equation onto its broad ground state and orthogonal complement
gives

$$
A_k(\delta)w=akv_k,
\qquad k^2\delta a=k\langle v_k,w\rangle.
$$

If `a=0`, invertibility of `A_k` forces `w=psi=0`. Otherwise these two
identities yield (15). Conversely a nonzero solution of (15) reconstructs an
eigenfunction from the same equations. This also proves that no eigenvalue is
hidden by the broad resolvent pole.

Equations (13)--(14) show that (15) has exactly one root in
`delta in [-1/2,1]` for small `k`, and

$$
\delta_k=-\frac{2\pi q(z)^2}{L}+O_z(L^{-2}).
\tag{16}
$$

## 5. Why this root is the second eigenvalue

The broad operator plus `2k^2` is strictly positive. Therefore the ordinary
positive Birman--Schwinger counting principle applies at energy `-2k^2`.
Its kernel is

$$
K_k^{\rm reg}(1)+|v_k\rangle\langle v_k|.
$$

The `e-perp` block of its complement is `Gamma+o(1)` and positive. Its
one-dimensional Schur complement along `e` is `-ML/(2pi)+O(1)`. Hence this
complement has exactly one negative eigenvalue. It follows that **exactly one**
eigenvalue of `H_k` lies below `-2k^2`.

The exact reduction (15) gives exactly one eigenvalue between `-2k^2` and
`-k^2/2`. It is therefore `lambda_2`, and (16) proves (2). No assertion about
the possible spectrum between `-k^2/2` and zero is needed for this conclusion.

## 6. First eigenvalue and cancellation in the two-level spectral sum

The perturbation `-k^2 Q(kx-z)^2` has operator norm `O(k^2)`. The isolated
simple eigenvalue `-1` of `h` consequently satisfies

$$
\lambda_1=-1-k^2\int q(x)^2Q(kx-z)^2\,dx+O_z(k^4).
$$

The first moment of the radial density `q^2` vanishes. Taylor expansion and
its finite second moment therefore give (1). Similarly,

$$
\int Q(x)^2Q(kx-z)^2\,dx=M Q(z)^2+O_z(k^2).
$$

The Pohozaev identity `int Q^4=2M` yields

$$
\frac1{2M}\int V_k^2
=1+k^2+k^2Q(z)^2+O_z(k^4).
$$

Combining this identity with (1)--(2) proves (3). The cancellation of the
`k^2 Q(z)^2` term is essential; using only the first-order attraction to the
narrow core misses the logarithmic cost in the second occupied level.

## 7. Generality and boundaries of the conclusion

The pole-reduction argument is not specific to Townes profiles. Suppose both
`W` and `B` are real nonnegative smooth potentials that, together with their
derivatives, decay exponentially. Assume the narrow operator `-Delta-W` has
exactly one negative eigenvalue and no bounded zero-energy solution. Assume the
broad operator `-Delta-B` has exactly one negative eigenvalue `-b^2`, simple
with normalized positive state `phi` and separated from the remaining spectrum
by the gap `b^2>0`. Then the analogous second eigenvalue of

$$
-\Delta-W(x)-k^2B(kx-z)
$$

obeys

$$
\lambda_2=-k^2b^2+
\frac{2\pi k^2|\phi(-z)|^2}{|\log k|}
+O_z\!\left(\frac{k^2}{|\log k|^2}\right).
$$

One takes a compact negative-energy interval around `-b^2` separated from zero
and repeats Sections 2--5 with `sqrt(W)` in place of `Q`. The leading `2pi`
is independent of the narrow well; its detailed scattering data first affect
the next inverse-logarithmic term. This is an expression of the standard
two-dimensional threshold-resolvent mechanism, not a new general theory of
point interactions.

The Townes conclusion rules out improvement of the two-level sharp constant
along this *fixed-z hierarchical family*. It does not settle arbitrary
overlapping potentials, growing displacement `z(k)`, all ranks, or stability
under unrestricted perturbations of `V_k`.

## 8. Literature placement

The operator organization belongs to established two-dimensional threshold
resolvent theory. A primary reference is A. Jensen and G. Nenciu,
*A unified approach to resolvent expansions at thresholds*, Reviews in
Mathematical Physics 13 (2001), 717--754; erratum 16 (2004), 675--677.
An accessible author preprint is
<https://webdoc.sub.gwdg.de/ebook/serien/e/reports_Aalborg_Univ/R-00-2015.pdf>.
Its general factorization and threshold decomposition should be distinguished
from the concrete two-well spectral-sum calculation above. The present
derivation supplies its own compressed-block and eigenvalue-ordering argument;
an exhaustive search for this exact special-case expansion has not been done.

## 9. A separate threshold question, not used above

To replace `S_2` by the sum over *all* negative eigenvalues, one would need to
exclude further eigenvalues in `(-k^2/2,0)`. A natural next lemma is uniformity
of the scaled logarithmic Birman--Schwinger expansion all the way to scaled
energy zero, using the broad operator's zero regularity. A weighted
threshold-resolvent expansion suggests this should be possible, but the
uniform kernel remainder and eigenvalue count in that additional joint limit
are not proved in this note. Therefore no full negative-spectrum claim is
included in (3).
