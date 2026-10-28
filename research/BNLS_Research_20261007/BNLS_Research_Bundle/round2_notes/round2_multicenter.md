# Round 2: moving centers, envelope localization, and explicit transport obstructions

7 October 2026. This is a direct attempt at the unrestricted nonradial problem. It obtains exact dynamic identities and two explicit obstructions. It does **not** establish finite-time blowup for arbitrary negative-energy data.

Throughout, (N\ge2\), (p=2+8/N\),
\[
i u_t=\Delta^2u-|u|^{p-2}u,\quad
E(u)=\tfrac12\|\Delta u\|_2^2-\tfrac1p\|u\|_p^p,
\]
and (F_R(z)=z e^{-|z|^4/R^4}\),
\[
V_{R,c}(u)=2\Im\int\bar u F_R(x-c)\cdot\nabla u\,dx.
\]

## 1. Exactly what a moving center adds

For a differentiable path (c(t)\), direct differentiation gives
\[
\frac{d}{dt}V_{R,c(t)}(u(t))
=\mathcal V_{R,c(t)}(u(t))
-2\dot c(t)\cdot\Im\int\bar u\,D^2\phi_{R,c(t)}\nabla u\,dx. \tag{1.1}
\]
Here \(\nabla\phi_{R,c}=F_R(x-c)\), and \(\mathcal V_{R,c}\) is the full frozen-center biharmonic virial expression, including every signed term. The extra integral is a localized, Hessian-weighted first-order momentum. It is not determined by total momentum.

There is an exact way to cancel this transport term: if (c(t)\) is a differentiable critical point of the function (c\mapsto V_{R,c}(u(t))\), then
\[
\nabla_c V_{R,c}(u)=-2\Im\int\bar u D^2\phi_{R,c}\nabla u=0,
\]
so the transport term vanishes. Thus the envelope idea is mathematically meaningful. Section 3 shows that this cancellation does not imply the needed sign or a Riccati inequality.

## 2. Barycentric tracking produces an indefinite fourth-order correction

For a sufficiently localized smooth component (v\), define
\[
m=\int|v|^2,\quad X=\int x|v|^2,\quad
P=\Im\int\bar v\nabla v,\quad
Q=\int \xi|\xi|^2|\widehat v(\xi)|^2\,d\xi.
\]
Use a unitary Fourier transform; thus (Q=\langle v,(-i\nabla)(-\Delta)v\rangle\).
The continuity equation gives
\[
X'=4Q,\qquad P'=0.
\]
For the barycenter (c=X/m\), the untruncated centered virial is
\[
V_c(v)=2\Im\int\bar v(x-c)\cdot\nabla v.
\]
Its exact derivative is
\[
\boxed{\quad V_c'=16E(v)-\frac8m P\cdot Q.\quad} \tag{2.1}
\]

Unlike second-order dispersion, the velocity moment (Q\) is not proportional to (P\). In fact (P\cdot Q\) can be strictly negative.

### An explicit compactly supported example with \(P\cdot Q<0\)

Choose real radial (q\in C_c^\infty(\mathbb R^N)\) with \(\|q\|_2=1\), and put (a=\|\nabla q\|_2^2/N\). For a modulated translate,
\[
P(e^{ik\cdot x}q(x-b))=k,\qquad
Q(e^{ik\cdot x}q(x-b))=igl[(N+2)a+|k|^2\bigr]k.
\]
The formula follows by shifting the radial Fourier density; all odd centered moments vanish and \(\int\xi_i\xi_j|\widehat q|^2=a\delta_{ij}\).

Take two disjoint translates of (q\), a unit vector (e\), and
\[
f_0(x)=\sqrt{9/10}\,e^{i\kappa e\cdot x}q(x-b_1)
+\sqrt{1/10}\,e^{-3i\kappa e\cdot x}q(x-b_2).
\]
Then (M(f_0)=1\), and locality of the differential momentum operators gives
\[
P(f_0)=\frac35\kappa e,
\quad
Q(f_0)=\frac35\kappa\bigl[(N+2)a-3\kappa^2\bigr]e.
\]
For \(\kappa^2>(N+2)a/3\), their scalar product is negative. Choose (A>0\) so that (f=Af_0\) has zero energy:
\[
A^{p-2}=\frac{p\|\Delta f_0\|_2^2}{2\|f_0\|_p^p}.
\]
The sign (P(f)\cdot Q(f)<0\) is unchanged. Therefore the centered virial of this zero-energy component has **strictly positive** derivative.

### Fixed total mass, negative energy, and zero total momentum

Let \(f_{\lambda,a}(x)=\lambda^{N/2}f(\lambda(x-a))\). Choose two distinct centers and a disjoint real (b\in C_c^\infty\) with (E(b)=-1\), and set
\[
U_\lambda=f_{\lambda,a_1}+\overline f_{\lambda,a_2}+b.
\]
For all large \(\lambda\), the components have disjoint support and
\[
M(U_\lambda)=2M(f)+M(b),\quad E(U_\lambda)=-1,\quad P(U_\lambda)=0.
\]
Choose fixed smooth spatial cutoffs equal to one near each component and with disjoint supports. Define the component barycenters using the corresponding localized masses and first moments. At the initial time all cutoff flux errors vanish because the data vanish in the transition regions. Thus (2.1) holds for each local component at that time, and their sum satisfies
\[
\left.\frac{d}{dt}\sum_{j=1}^3V_{c_j(t)}(u_j(t))\right|_{t=0}
=-16-16\lambda^4\frac{P(f)\cdot Q(f)}{M(f)}
\longrightarrow+\infty. \tag{2.2}
\]
The notation (u_j\) here denotes the localized component of the actual full solution, not a claim that the components evolve independently. Their initial derivative identities are exact by locality and disjoint support.

**Consequence.** Tracking the concentration centers by their local mass barycenters cannot give a universally negative multi-virial derivative from negative total energy, even with fixed mass and zero total momentum. Discarding \(-8P_j\cdot Q_j/m_j\), or treating it as nonpositive, would be an error.

## 3. Optimizing the center cancels transport but still admits a positive-derivative obstruction

Fix (R>0\) and consider
\[
V_*(u)=\inf_{c\in\mathbb R^N}V_{R,c}(u).
\]
At a unique nondegenerate minimizing center, the ordinary envelope derivative equals the frozen-center derivative. We now construct smooth data with fixed mass, fixed energy (-1\), fixed momentum, a fixed strictly negative (V_*\), but derivative (V_*'\to+\infty\).

### Step 1: a background that selects one center

Let (q_\varepsilon(x)=\varepsilon^{-N/2}q(x/\varepsilon)\), where (q\) is real radial, compactly supported, and has unit mass. For (k>0\), put
\[
b=Ae^{ikx_1}q_\varepsilon(x),
\]
with (A\) chosen so (E(b)=-1\). Such an (A\) exists because (E(Ae^{ikx_1}q_\varepsilon)\) is positive for sufficiently small (A\) and tends to (-\infty\) as (A\to\infty\).

Its current is (k|b|^2e_1\), so
\[
V_{R,c}(b)=2kA^2\int q_\varepsilon(x)^2 F_{R,1}(x-c)\,dx.
\]
After dividing by (2kA^2\), this converges uniformly in (C^2\), as \(\varepsilon\downarrow0\), to (F_{R,1}(-c)\). The latter has a unique global negative minimum at
\[
c=\frac{R}{\sqrt2}e_1.
\]
The minimum is nondegenerate: the Hessian is positive definite there. Its value is separated by a positive gap from points outside any fixed sufficiently small neighborhood, including infinity, where the function tends to zero. Uniform (C^2\) convergence therefore implies that, for sufficiently small fixed \(\varepsilon\), (c\mapsto V_{R,c}(b)\) has a unique nondegenerate global minimizer (c_0\) nearby. Choose such a fixed background once and for all.

### Step 2: a current-free packet with anisotropic Hessian energy

Choose real (g\in C_c^\infty\) so that, writing
\[
K=\|D^2g\|_2^2,\qquad
T_{11}=\sum_i\|\partial_i\partial_1g\|_2^2,
\]
one has (T_{11}<K/N\). An explicit construction is a tensor product bump squeezed strongly in direction (e_2\):
\[
g_L(x)=L^{1/2}\psi(Lx_2)\prod_{j\ne2}\psi(x_j),\qquad
\psi\in C_c^\infty(\mathbb R)\setminus\{0\}.
\]
Then (K\) grows as a positive constant times (L^4\), whereas (T_{11}=O(L^2)\). Hence the inequality holds for large fixed (L\). Amplitude-normalize this real function to zero energy; the ratio (T_{11}/K\) is unaffected. Continue to call the normalized function (g\). Its nonlinear integral is
\[
\|g\|_p^p=(p/2)K=(N+4)K/N.
\]

Choose (a=c_0+de_1\), (d>0\), outside the background support, and set
\[
U_\lambda=b+g_{\lambda,a}.
\]
For all sufficiently large \(\lambda\), supports are disjoint. Therefore
\[
M(U_\lambda)=M(b)+M(g),\quad
E(U_\lambda)=-1,\quad P(U_\lambda)=P(b),
\]
exactly and independently of \(\lambda\).

Because (g_{\lambda,a}\) is real, its current vanishes **pointwise**. Disjoint supports therefore imply
\[
V_{R,c}(U_\lambda)=V_{R,c}(b)
\quad\text{for every }c\text{ and every sufficiently large }\lambda. \tag{3.1}
\]
Thus the entire objective function, its unique minimizing center (c_0\), and its strictly negative minimum are unchanged.

### Step 3: its frozen-center derivative is positive of order \(\lambda^4\)

Let (s=d/R\), (h=e^{-s^4}\). At the packet center,
\[
D^2\phi_{R,c_0}(a)=hI-4s^4h e_1\otimes e_1,
\qquad \Delta\phi_{R,c_0}(a)=h(N-4s^4).
\]
The leading principal-minus-nonlinear contribution of the packet is exactly
\[
\begin{aligned}
&8\lambda^4[hK-4s^4hT_{11}]
-\frac8{N+4}\lambda^4h(N-4s^4)\|g\|_p^p\\
&\hspace{15mm}=32s^4h\left(\frac KN-T_{11}\right)\lambda^4>0.
\end{aligned} \tag{3.2}
\]
The Taylor error in the leading coefficients is (O_R(\lambda^3)\); lower-order virial terms are (O_R(\lambda^2+1)\). The background contributes a fixed finite number. Hence
\[
\mathcal V_{R,c_0}(U_\lambda)
=32s^4h(K/N-T_{11})\lambda^4+O_R(\lambda^3)
\longrightarrow+\infty. \tag{3.3}
\]

For each \(\lambda\), consider the actual solution starting from (U_\lambda\). Uniform continuity of (V_{R,c}(u(t))\) in (c\) near the initial time follows from its (H^1\) bound; the virial derivatives are uniformly continuous in (c\) as (H^2\) quadratic and nonlinear forms with uniformly bounded multiplier derivatives. The isolated unique minimum persists locally, or equivalently the envelope theorem applies at (t=0\). Therefore
\[
\left.\frac{d}{dt}V_*(u(t))\right|_{t=0}
=\mathcal V_{R,c_0}(U_\lambda)\to+\infty. \tag{3.4}
\]
This also directly realizes the critical-center cancellation in (1.1); no uncontrolled center velocity was used to obtain the positive derivative.

The fixed negative minimum can be made large compared with total mass by taking (kR\) large in the background construction. Indeed the minimum divided by (M(b)\) is approximately (-\sqrt2 e^{-1/4}kR\). The packet (g\) is fixed; the background amplitude needed for negative energy can grow, so the same ratio relative to (M(b)+M(g)\) remains arbitrarily large.

**Consequence.** At fixed (R\), center minimization does not yield an unconditional instantaneous inequality of the form
\[
V_*'\le -c_0-c_1(-V_*)^4
\]
or even a uniform upper bound on (V_*'\) depending only on the fixed (M,E,P,R\). In terms of (y=-V_*\), the derivative can be arbitrarily negative while (y\) is a fixed positive number. This is an actual-envelope obstruction, not merely the earlier fixed-center counterexample.

This does not rule out a radius chosen after seeing the concentrating datum, a time-integrated argument, or a functional using multiple centers and density-dependent partitions. Those require new estimates.

## 4. What a genuine multi-center partition must control

Take a real smooth quadratic partition of unity \(\sum_j\chi_j^2=1\). Set (u_j=\chi_j u\), (S=\sum_j|\nabla\chi_j|^2\). Expansion and integration by parts give the exact fourth-order IMS identity
\[
\boxed{
\sum_j\|\Delta(\chi_j u)\|_2^2
=\|\Delta u\|_2^2
+4\sum_j\int|\nabla\chi_j\cdot\nabla u|^2
+2\int S|\nabla u|^2
+\int\left(\sum_j\chi_j\Delta^2\chi_j\right)|u|^2.
} \tag{4.1}
\]
For example, the one-dimensional partition (\chi_1=\cos(kx)\), (\chi_2=\sin(kx)\) gives exactly the expected correction (6k^2\|u'\|_2^2+k^4\|u\|_2^2\), checking the coefficients.

The nonlinear part introduces an additional localization cost:
\[
\begin{aligned}
\sum_jE(\chi_j u)-E(u)
={}&2\sum_j\int|\nabla\chi_j\cdot\nabla u|^2
+\int S|\nabla u|^2\\
&+\frac12\int\left(\sum_j\chi_j\Delta^2\chi_j\right)|u|^2
+\frac1p\int\left(1-\sum_j|\chi_j|^p\right)|u|^p.
\end{aligned} \tag{4.2}
\]
The last term is nonnegative because (p>2\) and \(\sum\chi_j^2=1\). It may be very large when a concentration sits in a transition region. Thus negative global energy does not automatically imply negative sum of localized energies for an arbitrary partition.

For time-dependent cutoffs and centers, one legitimate scalar multiplier is
\[
\Phi(t,x)=\sum_j\chi_j(t,x)^2\phi_R(x-c_j(t)).
\]
Then
\[
V_\Phi'=\mathcal V_\Phi+2\Im\int\bar u\nabla(\partial_t\Phi)\cdot\nabla u,
\quad
\partial_t\Phi=\sum_j\bigl[2\chi_j\partial_t\chi_j\phi_j
-\chi_j^2\dot c_j\cdot\nabla\phi_j\bigr]. \tag{4.3}
\]
Expanding the gradient produces the center terms from (1.1), cutoff-transport terms, and terms involving both center velocities and cutoff gradients. The spatial virial \(\mathcal V_\Phi\) additionally contains derivatives of the partition up to order six. None is removed merely by choosing the centers to be barycenters.

One could try to place transitions only in regions of sufficiently small local mass and absorb (4.2) using the proved local-mass estimate. This is a valid instant-by-instant goal. To turn it into a full proof, however, one needs a time-dependent choice with controlled \(\partial_t\chi_j\), controlled transport in (4.3), and compatibility when concentrations merge, split, or change relative scale. The explicit sign obstruction (2.2) shows that barycentric transport is not automatically favorable; (3.4) shows that minimizing a single-center virial does not repair the problem.

## 5. Outcome of this attempt

The moving-center calculation and envelope optimization were carried through rather than left as suggestions. Barycentric multi-center virials have an indefinite correction (-8P_j\cdot Q_j/m_j\), and the sign failure occurs for explicit compactly supported fixed-invariant data. Optimizing a single center exactly cancels the transport derivative but still admits an arbitrarily positive envelope derivative, caused by a current-free anisotropic zero-energy packet.

The remaining possible multi-center route must incorporate both density and higher-order dispersive stress, and must control partition transport; it cannot be justified from first-order current, barycenter motion, or envelope stationarity alone. No complete dynamic estimate resolving those requirements has been proved in this round. The unrestricted negative-energy finite-time blowup conjecture remains unresolved by this work.
