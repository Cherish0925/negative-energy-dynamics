# Mathematical appendix: axial moments, the cylindrical virial closure, and positive second-order dispersion

Date: 2026-10-07. This appendix does not alter the existing manuscript or its certificates.

## 1. Scope and exact inputs

The conclusions below are conditional on the correctness of the existing computer-assisted construction, including its analytic interpretation. The inputs needed here are precisely:

1. A nonzero real radial solution \(Q\in H^2(\mathbb R^4)\) of
   \[
   \Delta^2Q+Q-Q^3=0.
   \tag{1.1}
   \]
2. On the symmetry space specified below, \(L_+=\Delta^2+1-3Q^2\) is invertible on the real even component and \(L_-=\Delta^2+1-Q^2\) is invertible on the imaginary odd component, as maps \(H^2\to H^{-2}\).
3. For \(g=\partial_sQ\),
   \[
   I=\langle g,L_-^{-1}g\rangle<0.
   \tag{1.2}
   \]

These are the existing manuscript's stationary-profile, spectral-gap, and inverse-pairing conclusions. Its coarse certified bounds \(I<-175\) and \(\|Q\|_Z\le104+3/500<105\), where
\[
\|f\|_Z^2=\|\Delta f\|_2^2+\|f\|_2^2,
\]
are used only for the optional explicit parameter direction in Section 7. No new numerical calculation is required for this appendix.

Write \(x=(s,y)\in\mathbb R\times\mathbb R^3\), and let \(X\subset H^2(\mathbb R^4;\mathbb C)\) be the closed real-linear space
\[
f(s,Oy)=f(s,y)\quad(O\in O(3)),\qquad
f(-s,y)=\overline{f(s,y)}.
\tag{1.3}
\]
Thus the real part is even in \(s\), and the imaginary part is odd in \(s\). Denote the corresponding subspace of \(H^{-2}\) by \(Y\). The excluded translation and phase kernels are dealt with by this symmetry restriction; the stated spectral input excludes any further kernels. No unrestricted inverse is assumed.

The general equation considered in this appendix is
\[
i\partial_tu=\Delta^2u-\mu\Delta u-|u|^2u,
\qquad \mu\ge0,
\tag{1.4}
\]
with
\[
E_\mu(f)=\frac12\|\Delta f\|_2^2
 +\frac\mu2\|\nabla f\|_2^2-\frac14\|f\|_4^4,
\quad M(f)=\|f\|_2^2,
\quad P_s(f)=\operatorname{Im}\int\overline f\,\partial_sf.
\tag{1.5}
\]

## 2. Weighted elliptic lemma: the axial moment is finite

**Lemma 2.1.** Let \(\mu\ge0\), \(\omega>0\), and suppose
\[
c:=\omega-3(|v|/4)^{4/3}>0.
\tag{2.1}
\]
Every \(W\in H^2(\mathbb R^4;\mathbb C)\) solving
\[
A_{\mu,v,\omega}W=|W|^2W,
\qquad A_{\mu,v,\omega}=\Delta^2-\mu\Delta+\omega+iv\partial_s,
\tag{2.2}
\]
satisfies \(W\in H^4\) and \(x_jW\in H^4\) for each coordinate \(j\). In particular, \(sW\in L^2\).

**Proof.** In four dimensions, \(H^2\hookrightarrow L^6\); hence the cubic term is in \(L^2\). The other terms in (2.2), except \(\Delta^2W\), are already in \(L^2\), so \(W\in H^4\). Fourier inversion and Cauchy--Schwarz give \(H^4(\mathbb R^4)\hookrightarrow C_0(\mathbb R^4)\). Consequently \(|W(x)|\to0\) uniformly as \(|x|\to\infty\).

The Fourier symbol of \(A_{\mu,v,\omega}\), with \(\widehat{\partial_sf}=i\xi_s\widehat f\), is
\[
a(\xi)=|\xi|^4+\mu|\xi|^2+\omega-v\xi_s
\ge\omega+|\xi|^4-|v||\xi|\ge c.
\tag{2.3}
\]
The last inequality follows by minimizing \(r^4-|v|r\) over \(r\ge0\). In addition, \(a(\xi)\) is comparable to \(1+|\xi|^4\), with constants depending on the fixed parameters. Thus
\[
\|A^{-1}h\|_2\le c^{-1}\|h\|_2,
\qquad
\|A^{-1}h\|_{H^4}\le C_A\|h\|_2.
\tag{2.4}
\]

Choose a real \(\chi\in C_c^\infty(\mathbb R)\) satisfying \(0\le\chi\le1\), \(\chi=1\) on \([-1,1]\), and \(\chi=0\) outside \([-2,2]\). Fix a coordinate \(j\), set
\[
w_L(x)=x_j\chi(x_j/L),\qquad L\ge1,
\]
and regard primes as derivatives with respect to \(x_j\). For each finite \(L\), \(w_LW\in H^4\). Its commutator equation is
\[
A(w_LW)=|W|^2w_LW+[A,w_L]W.
\tag{2.5}
\]
Direct differentiation gives the full commutator
\[
\begin{aligned}
[A,w_L]W={}&4w_L'\partial_j\Delta W
 +2w_L''\Delta W+4w_L''\partial_j^2W
 +4w_L'''\partial_jW+w_L''''W\\
&-\mu(2w_L'\partial_jW+w_L''W)
 +iv\,\delta_{js}w_L'W.
\end{aligned}
\tag{2.6}
\]
Here \(\|w_L^{(k)}\|_\infty\le C_\chi L^{1-k}\) for \(1\le k\le4\). Therefore
\[
\|[A,w_L]W\|_2
\le C_\chi(1+\mu+|v|)\|W\|_{H^3}=:C_0,
\tag{2.7}
\]
uniformly for \(L\ge1\).

Choose a fixed \(R\) such that \(\sup_{|x|>R}|W(x)|^2\le c/2\). Since \(|w_L(x)|\le|x_j|\), (2.4)--(2.7) imply
\[
\begin{aligned}
c\|w_LW\|_2
&\le\||W|^2w_LW\|_2+C_0\\
&\le\frac c2\|w_LW\|_2
 +R\|W\|_\infty^2\|W\|_2+C_0.
\end{aligned}
\tag{2.8}
\]
This proves a uniform \(L^2\) bound for \(w_LW\). Fatou's lemma already yields \(x_jW\in L^2\). Moreover, the right side of (2.5) is now bounded in \(L^2\), uniformly in \(L\), so (2.4) gives a uniform \(H^4\) bound. A weakly convergent subsequence in \(H^4\) has distributional limit \(x_jW\), because \(w_L=x_j\) eventually on every compact set. Hence \(x_jW\in H^4\), as asserted. \(\square\)

For the original branch, \(\omega=1\), and (2.1) holds after shrinking the small-velocity neighborhood. Thus axial square integrability is proved from the profile equation; it is neither an assumption inserted into the construction nor a missing hypothesis that could avoid the cylindrical theorem. The lemma also supplies all first coordinate moments and more weighted regularity than the present application needs.

## 3. The cylindrical multiplier and the exact unavailable inference

The source being audited is Tianxiang Gou, *Blowup of cylindrically symmetric solutions for biharmonic NLS*, arXiv:2205.08167v3 (4 November 2024), Theorem 1.2; see [G] below. In the mass-critical case its hypotheses include \(d\ge4\), negative energy, and
\[
\Sigma_d=\{u\in H^2(\mathbb R^d):u(y,s)=u(|y|,s),\ su\in L^2\}.
\tag{3.1}
\]
Its parts (i) and (ii) assert finite-time blowup for \(\mu>0\), and finite- or infinite-time blowup for \(\mu=0\), respectively.

On PDF page 3, equation (2.2) defines
\[
\phi_R(y,s)=\psi_R(|y|)+s^2/2,
\qquad
M_{\phi_R}(u)=2\operatorname{Im}\int\overline u\,\nabla\phi_R\cdot\nabla u.
\tag{3.2}
\]
The transverse cutoff has bounded gradient, but
\[
\nabla\phi_R=(\nabla_y\psi_R,s),\qquad
\|\nabla\phi_R\|_\infty=\infty.
\tag{3.3}
\]
The \(\mu=0\) proof ends on PDF pages 8--9 with (2.25) and (2.29), and then invokes the reasoning of [BL, Theorem 3]. The precise problem is the use of the final virial closure, not the mere definition of (3.2). For a bounded-gradient multiplier, the bound underlying [BL, equation (7.15)] is
\[
|M_\phi(u)|
\le2\|\nabla\phi\|_\infty\|u\|_2\|\nabla u\|_2
\le2\|\nabla\phi\|_\infty
 \|u\|_2^{3/2}\|\Delta u\|_2^{1/2}.
\tag{3.4}
\]
Conservation of mass makes its prefactor time independent. A bound \(M_\phi'(t)\le-c_0<0\) can then force growth of \(\|\Delta u(t)\|_2\).

For (3.2), the correct estimate is instead
\[
|M_{\phi_R}(u)|
\le2\|\nabla\psi_R\|_\infty\|u\|_2\|\nabla_yu\|_2
 +2\|su\|_2\|\partial_su\|_2.
\tag{3.5}
\]
The initial condition \(su_0\in L^2\) does not bound \(\|su(t)\|_2\) uniformly in time. The cited proof supplies no such uniform estimate. Thus (3.4) is unavailable, and (2.25)/(2.29), even if accepted, do not by this reasoning force \(H^2\) growup. This is a specific missing inference. It does not, by itself, establish that every estimate earlier in [G] is incorrect, nor does a proof gap alone logically disprove a theorem.

The first sentence of [G]'s proof of Theorem 1.2 also delegates the \(\mu>0\) case to the same BL theorem after its Lemma 2.2. The unbounded-gradient problem remains relevant there. Sections 6--8 below give a separate conditional counterexample construction for that case; it does not rest merely on identifying a gap.

## 4. Exact translation identity and the moment's growth

Let a profile \(W\) satisfy the hypotheses of Lemma 2.1 and put
\[
u(t,y,s)=e^{i\omega t}W(y,s-vt).
\tag{4.1}
\]
The transverse part of (3.2) is invariant under translations in \(s\). In its axial part, the change of variables \(z=s-vt\) gives the exact formula
\[
M_{\phi_R}(u(t))=M_{\phi_R}(W)+2vtP_s(W),
\qquad
\frac{d}{dt}M_{\phi_R}(u(t))=2vP_s(W).
\tag{4.2}
\]
All terms are absolutely integrable: the axial term is controlled by \(\|sW\|_2\|\partial_sW\|_2\). There is no limiting argument in (4.2).

If \(|W(-s,y)|^2=|W(s,y)|^2\), as on our symmetry branch, the axial first moment vanishes. Therefore
\[
\|s\,u(t)\|_2^2=\|sW\|_2^2+v^2t^2M(W).
\tag{4.3}
\]
In particular, (4.1) remains in \(\Sigma_4\) at every finite time, while its axial moment is not uniformly bounded when \(v\ne0\). Its \(H^2\) norm is constant.

For \(\mu=0\), the profile Pohozaev identity is \(E_0(W)=vP_s(W)/8\). Consequently, our negative-energy branch obeys
\[
M_{\phi_R}'(u(t))=16E_0(W)<0,
\qquad \|u(t)\|_{H^2}=\|W\|_{H^2}<\infty.
\tag{4.4}
\]
Thus the negative virial slope is exactly consistent with translation. It cannot alone serve as a contradiction to bounded \(H^2\) dynamics.

## 5. What does Theorem 1.2(ii) mean?

The standard interpretation of infinite-time blowup in this energy-class problem is unbounded \(H^2\) norm along times tending to infinity (possibly with a stronger limit or growth-rate conclusion). Our branch violates every such interpretation because that norm is constant.

For source precision, [G] does not separately define the phrase in Theorem 1.2(ii). Its stated solution space is \(C([0,T),H^2)\), Theorem 1.1 explicitly characterizes finite-time blowup by the Laplacian norm, and the invoked BL argument concerns growth of that norm. No \(\Sigma_d\) norm is defined in [G]. These facts support the energy-space interpretation; they do not justify silently substituting a weighted-norm interpretation.

If one *changes* the conclusion to allow mere divergence of \(\|su(t)\|_2\), (4.3) satisfies that different conclusion. Such a weakening would not give \(H^2\) growup and would not answer the original collapse question. Moreover, this semantic distinction cannot remove the conflict with the finite-time statement for \(\mu>0\), once Sections 6--8 are taken into account.

## 6. Two-parameter continuation: no additional spectral certificate

**Proposition 6.1.** Under the exact inputs in Section 1, there is a real-analytic family \(Q_{\mu,v}\in X\), for \((\mu,v)\) in a neighborhood of \((0,0)\), with \(Q_{0,0}=Q\) and
\[
\Delta^2Q_{\mu,v}-\mu\Delta Q_{\mu,v}+Q_{\mu,v}
 +iv\partial_sQ_{\mu,v}-|Q_{\mu,v}|^2Q_{\mu,v}=0.
\tag{6.1}
\]

**Proof.** Define
\[
\mathcal F(\mu,v,f)=\Delta^2f-\mu\Delta f+f
 +iv\partial_sf-|f|^2f:\mathbb R^2\times X\to Y.
\]
The maps \(\Delta,\partial_s:X\to Y\) are bounded. The cubic is a continuous real polynomial \(H^2\to H^{-2}\), so \(\mathcal F\) is real analytic. At \((0,0,Q)\),
\[
D_f\mathcal F(a+ib)=L_+a+iL_-b.
\]
The Section 1 spectral input makes this a bounded isomorphism \(X\to Y\). The analytic implicit-function theorem applies directly with both parameters. This avoids having to assume a new invertibility statement at a numerically chosen nonzero velocity. Alternatively, invertibility near the base point follows from operator-norm continuity and the Neumann series. \(\square\)

After decreasing the parameter neighborhood, the branch is nonzero, and Lemma 2.1 applies to its members with \(\mu\ge0\), \(\omega=1\). The branch therefore lies in \(\Sigma_4\). Its explicit solutions
\[
u_{\mu,v}(t,x)=e^{it}Q_{\mu,v}(x-vte_s)
\tag{6.2}
\]
exist for all \(t\in\mathbb R\) with constant \(H^2\) norm.

## 7. Negative energy persists for positive \(\mu\)

For any branch member write \(G(W)=\|\nabla W\|_2^2\). The action is
\[
S_{\mu,v,\omega}(f)=E_\mu(f)+\frac\omega2M(f)-\frac v2P_s(f).
\tag{7.1}
\]
The profile equation is its real variational equation. Under the mass-preserving scaling \(f_\lambda(x)=\lambda^2 f(\lambda x)\), the kinetic, quartic, gradient, and momentum terms scale respectively as \(\lambda^4,\lambda^4,\lambda^2,\lambda\). Lemma 2.1 gives enough weighted regularity to differentiate this curve in \(H^2\): indeed \(x_jW\in H^4\) implies \(x\cdot\nabla W\in H^3\). Differentiating the stationary action gives
\[
0=4E_\mu(W)-\mu G(W)-\frac v2P_s(W),
\qquad
E_\mu(W)=\frac\mu4G(W)+\frac v8P_s(W).
\tag{7.2}
\]
The same identity also follows by the existing cutoff Pohozaev proof with the additional gradient term. It is independent of the frequency \(\omega\), because mass is unchanged by this scaling.

Conjugation and uniqueness give
\[
Q_{\mu,-v}=\overline{Q_{\mu,v}}.
\tag{7.3}
\]
At \((\mu,v)=(0,0)\), differentiating in \(v\) yields
\[
\partial_vQ_{0,0}=-iz,
\qquad z=L_-^{-1}\partial_sQ.
\]
Therefore
\[
\left.\partial_vP_s(Q_{\mu,v})\right|_{(0,0)}
=\int(z\partial_sQ-Q\partial_sz)=2I.
\tag{7.4}
\]
Analyticity and the parity (7.3) imply
\[
\begin{aligned}
P_s(Q_{\mu,v})&=2Iv+O(|\mu v|+|v|^3),\\
G(Q_{\mu,v})&=G_0+O(|\mu|+v^2),\qquad G_0=\|\nabla Q\|_2^2>0.
\end{aligned}
\tag{7.5}
\]
Choose any constant
\[
0<\kappa<-I/G_0
\]
and set \(\mu=\kappa v^2\). Equations (7.2)--(7.5) give
\[
E_{\kappa v^2}(Q_{\kappa v^2,v})
=\frac{I+\kappa G_0}{4}v^2+O(v^4)<0
\tag{7.6}
\]
for all sufficiently small nonzero \(v\). In particular, this proves actual positive-\(\mu\) examples, not only the possibility of a continuation.

An explicit admissible direction follows from the existing coarse certificate. Integration by parts and Cauchy--Schwarz give
\[
G_0\le\|Q\|_2\|\Delta Q\|_2
\le\tfrac12\|Q\|_Z^2<\frac{11025}{2}.
\]
Since \(I<-175\), the choice \(\kappa=1/100\) satisfies
\[
\frac{I+\kappa G_0}{4}<-\frac{959}{32}<0.
\tag{7.7}
\]
Thus \(\mu=v^2/100\) is one fixed parameter direction with rigorously negative leading energy coefficient. This appendix does not claim a new numerical lower bound on the permitted nonzero velocity interval; the analytic existence of such an interval suffices.

For these profiles, (4.2) and (7.2) also give
\[
M_{\phi_R}'(u(t))=2vP_s(W)
=16E_\mu(W)-4\mu G(W)<0.
\tag{7.8}
\]
Once again the decrease coexists with constant \(H^2\) norm, now in the \(\mu>0\) case.

## 8. Scaling yields examples for every prescribed \(\mu>0\)

The positive-\(\mu\) result is not confined to a small fixed coefficient if the profile frequency is allowed to vary, as it is in the original Cauchy problem.

Take any one example from Section 7 with coefficient \(\mu_0>0\), profile \(W\), velocity \(v_0\), frequency \(1\), and \(E_{\mu_0}(W)<0\). Given an arbitrary prescribed \(\mu_*>0\), set
\[
\lambda=\sqrt{\mu_*/\mu_0},\qquad
u_*(t,x)=\lambda^2u_0(\lambda^4t,\lambda x).
\tag{8.1}
\]
Direct substitution shows that \(u_*\) solves (1.4) with coefficient \(\mu_*\). It is the traveling wave
\[
u_*(t,x)=e^{i\lambda^4t}W_\lambda(x-\lambda^3v_0te_s),
\qquad W_\lambda(x)=\lambda^2W(\lambda x).
\tag{8.2}
\]
Its energy and axial moment satisfy
\[
E_{\mu_*}(W_\lambda)=\lambda^4E_{\mu_0}(W)<0,
\qquad
\|sW_\lambda\|_2^2=\lambda^{-2}\|sW\|_2^2<\infty.
\tag{8.3}
\]
Cylindrical symmetry is preserved; the solution is global and has constant finite \(H^2\) norm. Its new frequency \(\lambda^4\) is positive. It is not asserted to equal one when \(\mu_*\) is large.

**Conditional consequence.** If the existing Section 1 certificates and their analytic reductions are correct, then in dimension four, for every prescribed \(\mu\ge0\), equation (1.4) has a nonzero cylindrically symmetric traveling solution with initial datum in \(\Sigma_4\), strictly negative \(E_\mu\), and constant finite \(H^2\) norm. For \(\mu=0\), use the original branch; for \(\mu>0\), use Sections 7--8.

This contradicts [G, Theorem 1.2(ii)] under its standard \(H^2\)-growup interpretation, and contradicts the finite-time statement [G, Theorem 1.2(i)] without any ambiguity about infinite-time weighted growth. These are logical consequences of the stated construction inputs. Their justification is the construction and extension above, not the independent observation of a gap in the cited proof.

## 9. What has and has not been established by this audit

The weighted-moment objection is resolved by Lemma 2.1. The specific final virial inference is identified in Section 3 and tested exactly by Section 4. Positive second-order dispersion is handled by a two-parameter implicit-function theorem and mass-critical scaling, using the original inverse certificates. There is no new unresolved spectral assumption in this extension.

The dependency on the existing computer-assisted construction remains explicit: an error in its stationary-state, inverse, or negative-pairing certification would invalidate the conditional examples. Conversely, the existence of a published conflicting theorem is not a mathematical reason to discard a verified construction. The correct review task is to inspect both proof chains. The invalid transfer of a bounded-gradient virial estimate alone would only establish a proof gap; the exact conditional construction establishes the stronger incompatibility stated above.

This appendix makes no claim about the supercritical Theorem 1.1, other dimensions, alternative hypotheses that might repair a cylindrical blowup theorem, or priority among all unpublished work. It also does not establish orbital stability of the traveling waves. None of those assertions is needed to refute the universal negative-energy blowup implication under the inputs of Section 1.

## Sources and reproducibility pointers

- **[G]** Tianxiang Gou, *Blowup of cylindrically symmetric solutions for biharmonic NLS*, [arXiv:2205.08167v3](https://arxiv.org/pdf/2205.08167v3), especially PDF pp. 2--3 and 8--9, Theorem 1.2, equation (2.2), equations (2.25), (2.29), and the subsequent closing sentence. Published in *Proceedings of the Edinburgh Mathematical Society* 67 (2024), 1085--1098, [DOI:10.1017/S001309152400066X](https://doi.org/10.1017/S001309152400066X).
- **[BL]** Thomas Boulenger and Enno Lenzmann, *Blowup for biharmonic NLS*, [arXiv:1503.01741](https://arxiv.org/pdf/1503.01741), Theorem 3 and equation (7.15).
- Existing construction: `research/BNLS_Research_Bundle/BNLS_Nonradial_Research_20261007.tex`, especially its stationary-profile validation, spectral transfer, negative inverse pairing, and analytic branch sections.
- Existing exact arithmetic implication: `research/BNLS_Research_Bundle/round2_certificate/round2_final_rational_implication.json` and its accompanying Python script. Their premise dependency is retained in Section 1; a displayed program `PASS` is not a substitute for verifying those premises.
- Locally inspected primary source: `sources/gou2205v3.pdf` and its extracted `sources/gou2205v3.txt`.
