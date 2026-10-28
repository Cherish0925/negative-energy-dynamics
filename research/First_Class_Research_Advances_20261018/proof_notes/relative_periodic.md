# Relative-periodic negative-energy motion: exact identities and the missing dynamical estimate

Research intermediate note, 2026-10-18. Scope: first-class negative-energy coherent structures only. The uniform mass gap for traveling waves is an existing project theorem; a mass gap for all relative-periodic solutions is **not proved** here.

## 1. Setting and normalization

Consider

\[
 i u_t=a(D)u-|u|^p u,\qquad p=2m/N,\quad m>2,
\]

where the symbol is real, even, positive elliptic, and homogeneous of degree m. Use

\[
 M=\int |u|^2,\quad P=\operatorname{Im}\int\bar u\nabla u,
 \quad E=\frac12\langle u,a(D)u\rangle-\frac1{p+2}\int|u|^{p+2}.
\]

For the calculations below take a sufficiently smooth, decaying solution, or explicitly assume that the displayed unlocalized virial and first-moment identities are justified by approximation. Finite variance together with H^{m/2} makes the dilation integral finite, but propagation and differentiation of the weighted regularity are separate hypotheses for general symbols.

Suppose

\[
 u(t+T,x)=e^{i\theta}u(t,x-y),\qquad v=y/T.
\]

Then the translating-frame orbit over a period is compact in every topology in which the solution is continuous. The unweighted formulation may also be obtained by uniform localized identities where their commutator hypotheses hold; it is not silently inferred for arbitrary rough strong solutions.

## 2. Exact relative-periodic virial and current relations

Set

\[
 J_v(t)=2\operatorname{Im}\int(x-vt)\cdot\bar u\nabla u.
\]

The homogeneous mass-critical dilation identity gives

\[
 J_v'(t)=4mE-2v\cdot P.
\]

The relative-periodic boundary condition makes J_v(T)=J_v(0). Hence

\[
 \boxed{v\cdot P=2mE.}\tag{2.1}
\]

If the first moment identity is justified, the same boundary condition and Fourier commutator give

\[
 \boxed{Mv=\frac1T\int_0^T\int\nabla a(\xi)|\widehat u(t,\xi)|^2\,d\xi\,dt.}\tag{2.2}
\]

In particular E<0 demands a strictly negative inner product between the mean translation velocity and the conserved momentum. P=0, v=0, or merely v·P=0 forces E=0. This rules out fixed-center negative-energy breathers, but is an immediate virial consequence and must not be sold as a major new result.

For a=|xi|^4, the compact-orbit antecedent is Pausader–Shao, *The mass-critical fourth-order Schrödinger equation in high dimensions*, arXiv:0906.1547v2, Section 6, Proposition 6.1. That proposition is stated for n>=1 with H^{2+1/(n+5)} regularity and fixed-scale precompactness, despite the high-dimensional scope of the paper's main scattering theorem. It gives the asymptotic version of (2.1), with the authors' different time/momentum conventions. Proposition 6.2 relates the average fourth-order mass current to E and P. Primary PDF read this turn: https://arxiv.org/pdf/0906.1547, pp. 42–44 in PDF counting (printed pp. 42–44); browser references turn220view0, turn222view0, turn222view1. A root answer must reopen the source before citing this agent's refs.

## 3. The precise extra term absent for traveling waves

Choose any differentiable phase gamma with gamma(T)-gamma(0)=theta modulo 2pi and set

\[
 w(t,z)=e^{-i\gamma(t)}u(t,z+vt)=X(t,z)+iY(t,z).
\]

Then w is T-periodic and

\[
 iw_t=(a(D)+\gamma'-|w|^p)w+i v\cdot\nabla w.
\]

Writing L_gamma=a(D)+gamma'-|w|^p, its imaginary component is

\[
 X_t=L_\gamma Y+v\cdot\nabla X.
\]

Since P=-2 integral Y grad X, pairing this equation with Y gives, at every time,

\[
 \langle Y,L_\gamma Y\rangle-\langle Y,X_t\rangle
 =\frac12v\cdot P=mE.
\]

Consequently the exact extension of the traveling-wave phase identity is

\[
 \boxed{mE=\frac1T\int_0^T\langle Y,L_\gamma Y\rangle dt
       -\frac1T\int_0^T\langle Y,X_t\rangle dt.}\tag{3.1}
\]

For a genuine traveling wave choose gamma(t)=omega t and w independent of t; the last term vanishes, recovering the project identity. For a breather it is a signed symplectic area:

\[
 \int_0^T\langle Y,X_t\rangle dt
 =\frac12\int_0^T
 (\langle Y,X_t\rangle-\langle X,Y_t\rangle)dt.
\]

Periodicity only removes the *sum* of these two terms (the derivative of <X,Y>); it does not remove their difference. Integrating by parts and discarding this area would be a mathematical error.

The individual quadratic term and area depend on the time-dependent phase gauge; their difference in (3.1) is invariant. Therefore any proposed area estimate must specify a modulation gauge and prove its phase-speed control. Choosing a pointwise best constant phase and differentiating as though that phase were constant is invalid.

## 4. A rigorous conditional consequence: negative energy requires sustained internal motion

Suppose an identified periodic gauge and a real Hilbert norm H satisfy the actual orbitwise coercivity

\[
 \langle Y(t),L_\gamma(t)Y(t)\rangle\ge c\|Y(t)\|_H^2,
 \qquad c>0.
\]

This is an **additional hypothesis**, not automatic from M near Mc: the phase kernel, gamma', scale motion and potential perturbation must all be treated.

Define

\[
 B=\frac1T\int_0^T\|Y\|_H^2dt,
 \qquad D=\frac1T\int_0^T\|X_t\|_{H^*}^2dt.
\]

For E=-e<0, (3.1) and Cauchy–Schwarz imply

\[
 cB+me\le\frac1T\int_0^T\langle Y,X_t\rangle dt
 \le\sqrt{BD}.
\]

Thus B>0 and

\[
 \boxed{D\ge c^2B+2cme+\frac{m^2e^2}{B}.}\tag{4.1}
\]

In particular D>c^2 B. A negative-energy relative-periodic orbit cannot remain quasi-static in this specified positive phase sector. If D<=c^2B were independently proved for a class of trajectories, all such negative-energy orbits would be excluded.

Equation (4.1) is a short proved conditional lemma, not a proof of a universal breather mass gap. The challenge is precisely to extract a usable coercivity and temporal-area bound from the nonlinear flow without assuming the desired conclusion.

## 5. Why instantaneous near-ground estimates plus periodicity cannot supply that bound

Take real localized Q and f with <Q,f>=0 and consider the kinematic loop

\[
 w(t)=Q+\varepsilon e^{-i\Omega t}f,\qquad T=2\pi/\Omega.
\]

It is T-periodic, remains O(epsilon) close to Q, has exactly constant mass M(Q)+epsilon^2 M(f), and Y perpendicular to Q. Nevertheless

\[
 \frac1T\int_0^T\langle Y,X_t\rangle dt
 =\frac12\Omega\varepsilon^2\|f\|_2^2.
\]

Every fixed spatial quadratic form of Y has period average O(epsilon^2), independent of Omega. Hence no estimate bounding the temporal area by a fixed fraction of the phase quadratic form follows just from smallness, orthogonality and periodicity. This loop is **not asserted to solve the PDE**, conserve its energy, or furnish a counterexample to the desired theorem. It identifies the indispensable dynamical information.

Even linearized Hamiltonian oscillations make the issue sharper: at zero translation, h_t=L_-k implies <k,h_t>=<k,L_-k>, so the symplectic area and positive phase form balance at leading order. A blanket strict inequality between them cannot be derived by citing phase positivity alone; it must use a nonlinear scale/energy mechanism or exclude internal modes.

## 6. Consequence for the strongest next target

The meaningful strengthening is:

> Is there a delta>0, independent of period T and drift v, such that every negative-energy relative-periodic localized solution has M>=Mc+delta?

This is already strictly beyond the traveling-wave theorem because the profile may change shape. A broader target replaces relative periodicity with uniformly compact motion modulo translations. Neither target is established by (2.1), (2.2), the existing static phase gap, or R13's time-averaged kinetic lower bounds.

The missing object is now explicit: control of the closed-orbit symplectic area in (3.1), after quotienting phase/translation and controlling the critical scale. Two substantive routes are nonlinear modulation/one-pass analysis around the mass-critical optimizer, or Floquet/resonance analysis proving absence of the required periodic internal excitation. A simple replacement of a stationary profile by its temporal average loses this area and cannot close the theorem.

For the first class this is a central next problem: it decides whether the existing mass gap is a structural restriction on persistent coherent motion or a property special to exact traveling profiles.
