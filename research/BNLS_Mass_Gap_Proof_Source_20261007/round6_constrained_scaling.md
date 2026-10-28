# Conserved-momentum dilation of negative-energy mass-critical traveling waves

Research note, 7 October 2026. The identities below apply to every nonzero weak H2 traveling profile of the mass-critical biharmonic NLS. They do not depend on a particular numerical profile or its Morse index. No claim of worldwide novelty is made.

## 1. Definitions and two exact identities

Let
\[
 iu_t=\Delta^2u-|u|^{8/N}u,\qquad
 u(t,x)=e^{i\omega t}U(x-vt),
\]
so
\[
 \Delta^2U+\omega U+i v\cdot\nabla U-|U|^{8/N}U=0.
\]
Use
\[
 M=\int|U|^2,\quad P=\operatorname{Im}\int\bar U\nabla U,
 \quad E=\frac12\int|\Delta U|^2-
       \frac1{2+8/N}\int|U|^{2+8/N}.
\]
No weighted moment is required. The cutoff identities established for arbitrary weak H2 profiles in `round6_traveling_mass_gap.md`, Section 2, justify the variations below: energy-subcritical elliptic bootstrapping first gives H4, and cutoff dilation and phase tests then give the identities by dominated convergence. Fourier transforms are unitary, and
\[
 W=\int |\xi|^2\xi|\widehat U(\xi)|^2d\xi
   =\operatorname{Im}\int\Delta U\nabla\bar U.
\]
The profile is a critical point of
\[
 S_{\omega,v}(U)=E(U)+\frac\omega2M(U)-\frac12v\cdot P(U).
\]
Under the mass-preserving scaling \(U_{\lambda,0}(x)=\lambda^{N/2}U(\lambda x)\), energy and momentum are \(\lambda^4E\) and \(\lambda P\). Differentiation gives
\[
 4E-\frac12v\cdot P=0,\qquad v\cdot P=8E.                 \tag{1.1}
\]
Under modulation \(U_{1,k}=e^{ik\cdot x}U\), the energy derivative at zero is \(2W\), and the momentum derivative is \(M\) times the identity. Hence
\[
 2W-\frac M2v=0,\qquad W=\frac M4v.                       \tag{1.2}
\]
These are stationarity identities; a phase modulation is not being asserted to be a symmetry of the evolution.

## 2. Full Fourier expansion

Define
\[
 U_{\lambda,k}(x)=e^{ik\cdot x}\lambda^{N/2}U(\lambda x),
 \quad G=\int|\xi|^2|\widehat U|^2,\quad
 T_{jk}=\int\xi_j\xi_k|\widehat U|^2.
\]
Then \(M(U_{\lambda,k})=M\), \(P(U_{\lambda,k})=\lambda P+Mk\), and
\[
 \begin{split}
 E(U_{\lambda,k})={}&\lambda^4E+2\lambda^3 k\cdot W
   +\lambda^2(|k|^2G+2k^TTk)\\
   &+2\lambda|k|^2k\cdot P+\frac M2|k|^4.                 \tag{2.1}
 \end{split}
\]
Indeed, the Fourier density is shifted from \(\xi\) to \(\lambda\xi+k\), so expand \(|\lambda\xi+k|^4/2\) and use that the mass-critical nonlinear energy scales as \(\lambda^4\). This checks every coefficient without appealing to a formal Hessian convention.

Set
\[
 \mu=P/M,\quad U_\lambda=U_{\lambda,(1-\lambda)\mu},\quad
 m=M|\mu|^4,\quad B=|\mu|^2G+2\mu^TT\mu.
\]
Thus \(M(U_\lambda)=M\) and \(P(U_\lambda)=P\) for every \(\lambda>0\). Jensen or Cauchy--Schwarz gives
\[
 G\ge M|\mu|^2,\quad \mu^TT\mu\ge M|\mu|^4,
 \quad B\ge3m.                                            \tag{2.2}
\]
The two stationarity identities imply \(\mu\cdot W=2E\).

## 3. Exact positive factorization on the whole constrained dilation curve

Substitution into (2.1), with \(\delta=\lambda-1\), gives
\[
 E(U_\lambda)-E
 =\delta^2[(B-6E)+(2B-8E-2m)\delta
                    +(B-3E-3m/2)\delta^2].                \tag{3.1}
\]
Equivalently,
\[
 \boxed{
 E(U_\lambda)-E
 =(\lambda-1)^2\left[
   (B-3m/2-3E)\lambda^2+(m-2E)\lambda+(m/2-E)
 \right].}                                                \tag{3.2}
\]

**Theorem.** If \(E(U)<0\), then \(\lambda=1\) is the strict global minimizer of energy on this entire mass-and-momentum-preserving dilation curve. More quantitatively,
\[
 E(U_\lambda)-E(U)
 \ge (|E(U)|+m/2)(\lambda-1)^2,\qquad\lambda>0.             \tag{3.3}
\]
Every coefficient in the bracket in (3.2) is positive: the first is at least \(3m/2+3|E|\), by (2.2); the other two are immediate. Dropping the terms containing positive powers of \(\lambda\) proves (3.3).

The local curvature is the special case
\[
 \left.\frac{d^2}{d\lambda^2}E(U_\lambda)\right|_{\lambda=1}
 =-12E+2B>0.                                               \tag{3.4}
\]
In contrast, ordinary mass-preserving dilation, which changes momentum, has energy \(\lambda^4E\) and curvature \(12E<0\) at one.

There is a second useful consequence. Directly neutralizing momentum by a linear phase changes the energy to
\[
 \boxed{E(e^{-i\mu\cdot x}U)=B-3m/2-3E
           \ge3m/2+3|E|>0.}                               \tag{3.5}
\]
Thus a negative-energy traveling wave cannot be converted into a zero-momentum negative-energy datum by simply applying the momentum-neutralizing phase. This is an exact obstruction to that construction, not a claim that all possible zero-momentum constructions are impossible.

The profile need not be stable: a minimum along this one curve is not a minimum on the complete constraint surface, and does not make the full Hessian positive. The existing excited waves possess many unrelated unstable directions. The identities explain precisely why the familiar negative-energy shrinking direction changes when momentum conservation is imposed.

## 4. The least mass of globally bounded negative-energy zero-momentum motion

In a fixed dimension define
\[
 m_{\rm ng}=\inf\{M(u_0):E(u_0)<0,\ P(u_0)=0,
   \ u\text{ is forward global and }\sup_{t\ge0}\|u(t)\|_{H^2}<\infty\}.
\]
The infimum of an empty set is \(+\infty\). Let \(M_c\) be the mass in the sharp mass-critical Gagliardo--Nirenberg inequality,
\[
 \frac1{2+8/N}\|f\|_{2+8/N}^{2+8/N}
 \le\frac12\left(\frac{M(f)}{M_c}\right)^{4/N}\|\Delta f\|_2^2.
\]
Then every admissible datum has \(M(u_0)>M_c\), and hence
\[
 M_c\le m_{\rm ng}.                                       \tag{4.1}
\]
The strict pointwise inequality does not imply a strict inequality for the infimum.

Whenever a rigorously constructed exact opposite-velocity pair converges in \(H^2\) to two separated copies of \(U_v\), conservation and decoupling give exactly
\[
 M(u)=2M(U_v),\quad P(u)=0,\quad E(u)=2E(U_v)<0.
\]
Consequently the family of such verified pair constructions gives
\[
 m_{\rm ng}\le\inf_{v\text{ admitted by the construction}}2M(U_v).
                                                                  \tag{4.2}
\]
For a small-speed excited branch tending to \(Q_{\rm exc}\), this is at most \(2M(Q_{\rm exc})\). This upper bound relies on the exact pair construction, not a linear superposition of two waves.

The intrinsic-spreading theorem already rules out a uniformly mass-tight global bounded zero-momentum negative-energy orbit. Thus an object attaining \(m_{\rm ng}\), if it exists, cannot be a single compact orbit modulo translations. It must remain spatially noncompact. This does not rule out attainment by a separating multiwave or wave-plus-radiation solution. Determining whether \(m_{\rm ng}>M_c\), and identifying the least-mass escape mechanism, are new research questions posed here; they are not being attributed to a named established conjecture.

## 5. The sharp radiation budget, and what it does not prove

Suppose an exact asymptotic state consists of one negative-energy traveling wave and asymptotically free radiation \(e^{-it\Delta^2}f\), with the mass, momentum and energy cross terms vanishing. These are hypotheses of this paragraph, not a proved wave-operator construction. If total momentum is zero, the radiation carries \(P(f)=-P(U)\). Its asymptotic energy is
\[
 E_{\rm rad}=\frac12\|\Delta f\|_2^2\ge0.
\]
For \(m_r=\|f\|_2^2>0\), Jensen applied to the probability measure \(|\widehat f|^2/m_r\) gives
\[
 \boxed{E_{\rm rad}\ge\frac{|P(f)|^4}{2m_r^3}.}             \tag{5.1}
\]
The constant is sharp as an infimum: increasingly broad wave packets with Fourier mass concentrated near one carrier frequency approach equality. A nonzero \(L^2\) Fourier function cannot be a point mass, so no nonzero finite-width packet attains equality.

Strict negativity of the total energy requires \(E_{\rm rad}<|E(U)|\), whence the necessary budget
\[
 \boxed{m_r^3>\frac{|P(U)|^4}{2|E(U)|}.}                    \tag{5.2}
\]
This is a necessary condition, not by itself sufficient for an exact nonlinear asymptotic solution.

On the small-speed negative-inertia branch, \(|P(U_v)|\asymp|v|\) and \(-E(U_v)\asymp v^2\). The minimum radiation mass allowed by (5.2) is therefore of order \(v^{2/3}\), tending to zero. Thus a future spatially separated soliton-plus-radiation wave-operator theorem could improve the pair upper bound towards \(M(Q_{\rm exc})\). It would be incorrect to conclude \(m_{\rm ng}\ge2M_c\) simply by demanding two nonlinear cores: radiation is another possible carrier of compensating momentum.

