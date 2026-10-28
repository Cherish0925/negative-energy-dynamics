# Independent verification and response certificate for the four-dimensional candidate

7 October 2026. This note establishes the branch sign and angular reduction, and supplies **executed exact rational scalar certificates** for the canonical approximate profile and an approximate response. It does not, by itself, certify the existence of an exact stationary profile or a traveling branch; the remaining spectral/Newton assumptions are identified explicitly.

## 1. Sign of the traveling branch

In (N=4$, the equation is cubic. Let a real radial exact profile solve
$$
\Delta^2Q+Q-Q^3=0.
$$
A traveling profile of velocity (v e_1$, with temporal frequency one, must solve
$$
\Delta^2Q_v+Q_v+i v\partial_1Q_v-|Q_v|^2Q_v=0. \tag{1.1}
$$
Write (L_-=\Delta^2+1-Q^2$ and (f=\partial_1Q$. If a smooth branch exists and the relevant imaginary linearized operator is invertible, its first variation is
$$
Q_v=Q-i v\psi+O(v^2),\qquad L_-\psi=f.
$$
Indeed, the order-(v$ imaginary equation is (-L_-\psi+f=0$. Define
$$
I=\langle f,L_-^{-1}f\rangle=\langle f,\psi\rangle.
$$
With momentum (P_1(u)=\Im\int\bar u\partial_1u$, integration by parts gives
$$
P_1(Q_v)=2vI+O(v^3).
$$
The exact traveling-profile scaling identity is (E(Q_v)=vP_1(Q_v)/8$. Consequently
$$
\boxed{E(Q_v)=\tfrac14 I v^2+O(v^4).} \tag{1.2}
$$
The parity of the remainders follows if the local branch is unique in a symmetry-fixed slice, because (Q_{-v}=\overline{Q_v}$. The weaker differentiability statement (E(Q_v)=Iv^2/4+o(v^2)$ already suffices for the sign conclusion. Thus a strictly negative (I$, together with a validated local branch, would produce an exact global negative-energy traveling solution.

## 2. The dimension-shifted response equation is correct

Write $\psi(x)=Y_1(x/r)W(r)=x_1V(r)$, with (Y_1=x_1/r$ and (W=rV$. For the angular-momentum-one radial Laplacian,
$$
D_{N,1}W=W''+\frac{N-1}{r}W'-\frac{N-1}{r^2}W,
$$
direct differentiation gives
$$
D_{N,1}(rV)=r\left(V''+\frac{N+1}{r}V'\right)=rD_{N+2}V.
$$
Applying it twice yields (D_{N,1}^2(rV)=rD_{N+2}^2V$. Therefore, in (N=4$,
$$
\left(D_6^2+1-Q^2\right)V=\frac{Q'}r,
\qquad D_6=\partial_r^2+\frac5r\partial_r. \tag{2.1}
$$
At the origin (Q'/r\to Q''(0)=Z(0)/4$ when (Z=D_4Q$. This verifies both the dimension shift and the origin value in `round2_radial_integerdims.py`.

The physical angular factor is
$$
\int_{S^3}\theta_1^2\,d\theta=\frac{|S^3|}{4}=\frac{\pi^2}{2}=:a_4,
$$
so
$$
I=a_4\int_0^\infty Q'V r^4\,dr
=a_4\int_0^\infty\left[(D_6V)^2+(1-Q^2)V^2\right]r^5\,dr. \tag{2.2}
$$
The original saved response independently gave the two values (-273.4738679603$ and (-273.4738672277$; refined data agree near (-273.473861887$. These floating-point cross-checks preceded the exact certificates below.

## 3. Why this would not contradict the earlier radial or symmetry theorem

The stationary radial profile has energy zero. A traveling branch selects the velocity axis and is generally nonradial. Its continuous spatial symmetry is the group rotating the three transverse coordinates; this group fixes every point of the velocity axis, and therefore fails the earlier theorem's infinite-orbit hypothesis.

A fixed-width profile translating to infinity also violates the earlier uniform relative-ball mass hypothesis: for any fixed center and fixed relative radius, a ball centered on the moving profile eventually contains almost all its mass. Likewise its angular (H^2$ mass typically grows as (t^4$, so its integrated angular mass has precisely the (T^5$ order required by the previously derived necessary condition. None of those partial results excludes this candidate.

## 4. A residual identity giving the correct one-sided sign certificate

Let (A=L_-$ restricted to the (\ell=1$ sector, and let (z$ be any domain trial response. Put (r=f-Az$. If (A$ is self-adjoint and invertible,
$$
\boxed{
\langle f,A^{-1}f\rangle
=2\langle f,z\rangle-\langle z,Az\rangle
+\langle r,A^{-1}r\rangle.} \tag{4.1}
$$
If every positive spectral value of (A$ is at least $\gamma>0$, then
$$
A^{-1}\le\gamma^{-1}I
$$
as a quadratic-form upper bound. Negative eigenvalues need not be bounded away from zero quantitatively for this *upper* bound: their inverse contributions are negative. Hence
$$
I\le J(z)+\gamma^{-1}\|r\|_2^2,
\quad J(z)=2\langle f,z\rangle-\langle z,Az\rangle. \tag{4.2}
$$
Invertibility still must be established, and a full implicit-function proof may need stronger inverse estimates.

A negative Rayleigh quotient by itself is **not** a certificate that (I<0$. For example, (A=\operatorname{diag}(-1,1)$ has a negative direction, but (f=(0,1)$ gives (I=1$. The residual and the one-sided spectral estimate are essential.

## 5. Executed exact rational certificates against the frozen canonical profile

The canonical approximate stationary profile is exactly defined by

[round2_radial_H4_exact_h1_16.json](../../computations/excited-waves/axial-profiles/round2_radial_H4_exact_h1_16.json).

Its nodes are rational, its endpoint jets are exact binary-rational numbers encoded as hexadecimal floats, and each interval is the unique degree-seven Hermite polynomial with the prescribed derivatives of orders zero through three. The function is identically zero after radius 36. The independent trial (V$ is similarly defined by the exact `vjets` in

[round2_certificate_exact_rational_data.json](../../computations/excited-waves/round2_certificate/round2_certificate_exact_rational_data.json).

It uses nodes (j/5$, is zero after radius 40, and has common derivatives through order three at every interface. Vanishing odd derivatives at zero and vanishing jets at the outer endpoint make the radial profile and (\psi=x_1V$ legitimate compactly supported (H^4$ functions.

[round2_certificate_canonical.py](../../computations/excited-waves/round2_certificate/round2_certificate_canonical.py) forms the union of the two sets of knots (680 intervals), restricts the polynomials by exact rational affine transformations, and performs all scalar polynomial integrals with Python `Fraction`. It encloses $\pi$ by the alternating-series bounds for Machin's formula. Every proposed loose bound is checked by an exact rational comparison.

For the response residual, multiplying by (r^3$ gives the polynomial
$$
H=r^2\widetilde Q'-r^3V''''-10r^2V'''-15rV''+15V'
-r^3V+r^3\widetilde Q^2V.
$$
Then $\|f_{\widetilde Q}-A_{\widetilde Q}\psi\|_2^2=a_4\int H^2/r\,dr$. The first interval is integrated exactly using the exact cancellation (H=O(r^3)$. On each other interval ([a,b]$, the program uses (1/r\le1/a$, leaving an exact polynomial integral. Thus this is a genuine conservative integral bound, not a sampled residual.

The exact tests establish

| Quantity | Certified convenient bound |
|---|---:|
| $\|\widetilde Q\|_Z$, (\|u\|_Z^2=\|u\|_2^2+\|\Delta u\|_2^2$ | $\le104$ |
| $\|\psi\|_Z$ | $\le132$ |
| $J_{\widetilde Q}(\psi)$ | $\le-273$ |
| $\langle\psi,A_{\widetilde Q}\psi\rangle$ | $\le-273$ |
| Response residual $\eta$ | $<0.000645<0.000662$ |
| $\|\psi\|_2$ | $\le104$ |
| $\|\psi\|_4$ | $\le18$ |
| $\|\widetilde Q\psi\|_4$ | $\le26$ |
| $\|\widetilde Q\psi\|_2$ | $\le133$ |
| $\|\psi\|_\infty$ | $\le6$ |
| $\|\widetilde Q\|_2$ | $\le73$ |
| $\langle\psi,(\Delta^2+1/2)\psi\rangle$ | $\le11950$ |
| $\int\widetilde Q^2\psi^2$ | $\ge17540$ |

More informative decimal summaries of the exact enclosures are
$$
\eta^2\le4.147919638281\times10^{-7},\quad
J\le-273.4738618768,\quad
\|\widetilde Q\|_Z^2\le10635.584484,\quad
\|\psi\|_Z^2\le17273.995931.
$$
The machine-readable results are [round2_certificate_canonical_results.json](../../computations/excited-waves/round2_certificate/round2_certificate_canonical_results.json); exact integral values are retained in [round2_certificate_canonical_integrals.json](../../computations/excited-waves/round2_certificate/round2_certificate_canonical_integrals.json). The exact checks, rather than rounded printed decimals, are the certificate.

The canonical stationary-profile residual was independently audited in `round2_radial_canonical_residual.py`: its exact Hermite/Bernstein calculation with outward-rounded positive arithmetic proves
$$
\|\Delta^2\widetilde Q+\widetilde Q-\widetilde Q^3\|_2<0.000242.
$$
This residual bound alone is not an existence theorem for a nearby exact (Q$.

## 6. Error tolerance for an exact radial profile in an H2 ball

Suppose an exact radial stationary (Q$ has been validated with
$$
\rho=\|Q-\widetilde Q\|_Z.
$$
No (L^\infty$ error bound for the true profile is necessary. The sharp four-dimensional Sobolev inequality and interpolation give
$$
\|h\|_4\le\rho/4,\qquad
\|\partial_1h\|_2\le3\rho/8,
\quad h=Q-\widetilde Q.
$$
Here the second estimate uses radiality of (h$. For the first, the sharp homogeneous (H^1\to L^4$ constant has square $\sqrt6/(8\pi)<1/8$, while $\|\nabla h\|_2^2\le\rho^2/2$.

Using the exact trial bounds above,
$$
\left|\int(Q^2-\widetilde Q^2)\psi^2\right|
\le1197\rho+\frac{81}{4}\rho^2=:b(\rho), \tag{6.1}
$$
because $\|\widetilde Q\psi^2\|_{4/3}\le\|\widetilde Q\psi\|_2\|\psi\|_4\le133\cdot18$. Also
$$
\|\partial_1Q-A_Q\psi\|_2
\le0.001+\frac{107}{8}\rho+\frac38\rho^2=:e(\rho). \tag{6.2}
$$
Consequently
$$
J_Q(\psi)\le-273+1275\rho+\frac{81}{4}\rho^2. \tag{6.3}
$$
If a positive (L^2$ spectral gap $\gamma=1/2$ has additionally been proved, (4.2) gives the explicit certificate
$$
\boxed{
I\le-273+1275\rho+\frac{81}{4}\rho^2
+2\left(0.001+\frac{107}{8}\rho+\frac38\rho^2\right)^2.} \tag{6.4}
$$
For example, the right side is below (-141$ at $\rho=0.1$. Thus the scalar sign is tolerant of a much larger profile error than the numerical approximations suggest. The spectral premise must not be replaced by a floating-point eigenvalue plot.

## 7. A scalar trace route to that one-sided spectral gap

In the effective radial six-dimensional space put (B_0=-D_6$, and choose $\gamma=1/2$. The Birman–Schwinger operator
$$
\mathcal B_Q=Q(B_0^2+1/2)^{-1}Q
$$
is positive and trace class. Its nonzero eigenvalues agree with those of
$(B_0^2+1/2)^{-1/2}Q^2(B_0^2+1/2)^{-1/2}$.

Let $z=2^{-1/4}e^{i\pi/4}$. The radial Green kernel for $(B_0+z^2)^{-1}$, relative to measure (r^5dr$, is
$$
G_z(r,s)=(rs)^{-2}I_2(z\min\{r,s\})K_2(z\max\{r,s\}).
$$
Factoring (B_0^2+1/2$ therefore yields the exact trace formula
$$
\operatorname{tr}\mathcal B_Q
=-\sqrt2\int_0^\infty r Q(r)^2\Im[I_2(zr)K_2(zr)]\,dr. \tag{7.1}
$$
The small-argument expansion (I_2(w)K_2(w)=1/4-w^2/24+\cdots$, together with the operator monotonic bound $(B_0^2+1/2)^{-1}\le B_0^{-2}$, gives for the nonnegative trace weight
$$
0\le\tau(r):=-\sqrt2r\Im[I_2(zr)K_2(zr)]\le r^3/24.
$$
Thus the trace error for an (L^2(\mathbb R^4)$ profile perturbation obeys
$$
|\operatorname{tr}\mathcal B_Q-\operatorname{tr}\mathcal B_{\widetilde Q}|
\le\frac{\rho(146+\rho)}{24|S^3|}
<\frac{\rho(146+\rho)}{432}. \tag{7.2}
$$

The response supplies a lower bound on the first Birman–Schwinger eigenvalue:
$$
\lambda_1(\mathcal B_Q)
\ge\frac{17540-b(\rho)}{11950}. \tag{7.3}
$$
Therefore the two scalar conditions
$$
\operatorname{tr}\mathcal B_{\widetilde Q}\le2.354,
\qquad
2.354+\frac{\rho(146+\rho)}{432}
-\frac{17540-b(\rho)}{11950}<1 \tag{7.4}
$$
would imply $\lambda_2(\mathcal B_Q)<1$. The negative trial form, preserved whenever (b(\rho)<273$, then proves that (A_Q$ has exactly one eigenvalue below (1/2$, and that eigenvalue is negative. In particular zero is excluded and the positive spectral gap is at least (1/2$.

For $\rho=0.1$, the left side bounding $\lambda_2$ is below (0.931$. Independent floating-point Bessel quadrature gives the nominal trace (2.352733013272$, and finite-difference Birman–Schwinger eigenvalues at this shift begin near (1.62324,0.37884,0.20046$. These numbers support the chosen margin but are not, in this note, a rigorous enclosure of the Bessel integral. The polynomial trial numerator, denominator, and all perturbation estimates are certified; (7.1)'s nominal trace enclosure is a separate remaining scalar verification unless supplied elsewhere in the project.

## 8. Completion requirements

The sign and dimension shift are correct, the scalar trial/residual bounds have been executed in exact rational arithmetic, and the prior radial/symmetry theorems do not contradict the candidate. To obtain an actual counterexample to the unrestricted blowup assertion, the remaining proof must still supply:

1. Existence of an exact radial stationary (Q$ in a certified neighborhood of the canonical approximate profile.
2. The required linearized invertibility on the full symmetry-fixed traveling-wave space, not only the $\ell=1$ response sector.
3. A local traveling branch obtained by a valid implicit-function or Lyapunov–Schmidt argument.

Once those are established, a certified (I<0$ and (1.2) give negative energy for sufficiently small nonzero speed, and the traveling solution is global. None of these final existence steps is supplied merely by a small sampled residual or a successful nonlinear solver.
