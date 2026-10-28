# Literature comparison for the proposed quadratic quintic collapse

Date: 2026-10-11.This note compares the candidate mechanism with actual published or preprint theorems. It does not establish existence of the proposed vector solution or certify priority.

## 1. The candidate being compared

The equation is the **local**, one-dimensional, common-density quintic system

$$
 i\partial_tu_j+\partial_x^2u_j+\rho^2u_j=0,
 \qquad \rho=\sum_j|u_j|^2.
$$

The proposed branch has an even principal component of conserved mass
$M_c=\|Q\|_2^2$, odd secondary components with a smooth terminal background
$W$, and $A=\sum_{j\ge2}|W'_j(0)|^2>0$. Its total mass is **larger** than
$M_c$. The zero-energy transverse scattering problem is

$$
 H=-\partial_y^2-Q^4=-\partial_y^2-3\operatorname{sech}^2(2y),
 \quad HF=0,
 \quad F(y)=y+c\operatorname{sgn}y+o(1),
 \quad c=\frac\pi4+\log2-1.
$$

The accompanying notes derive a matched energy correction $-cA\lambda$.
If the residual core energy tends to zero and the required asymptotic remainder
is smaller than this correction, the formal balance

$$
 \frac{V_Q}{8}\dot\lambda^2-cA\lambda=o(\lambda),
 \qquad V_Q=\int y^2Q^2,
$$

suggests

$$
 \lambda(t)\sim \frac{2cA}{V_Q}(T-t)^2.
$$

Those italicized dynamical requirements are not consequences of the static
scattering calculation. The candidate has not been constructed as an exact PDE
solution. The literature conclusions below retain that distinction.

## 2. Exact physical model overlap

Jing Li, Boris A. Malomed, Wenliang Li, Xi Chen, E. Ya. Sherman,
*Coupled density-spin Bose-Einstein condensates dynamics and collapse in systems
with quintic nonlinearity*, arXiv:1910.05023 (2019).

Primary text: <https://arxiv.org/html/1910.05023v1>, equations (3), (8), (14)–(15).

Their two-component Gross–Pitaevskii model has same-spin and cross-spin
three-body couplings $g_1,g_2$, together with spin-orbit and Zeeman terms.
Setting spin-orbit and Zeeman coefficients to zero and $g_1=g_2=g>0$ gives

$$
 iu_t+\tfrac12u_{xx}+g(|u|^2+|v|^2)^2u=0,
 \quad iv_t+\tfrac12v_{xx}+g(|u|^2+|v|^2)^2v=0.
$$

Constant space/amplitude rescalings give exactly our two-component PDE.
The paper identifies this equality of couplings as the spin-isotropic case.
Its investigation uses variational approximations and simulations; it does not
prove the principal-mass/odd-background branch above. Thus the physical model
itself is established, while the proposed asymptotic theorem remains a separate
mathematical task. The HTML-rendered date is not the original publication date;
the arXiv header identifies October 2019.

## 3. Double-power minimal-mass collapse: altered rates are established, but not this exponent

Stefan Le Coz, Yvan Martel, Pierre Raphaël,
*Minimal mass blow up solutions for a double power nonlinear Schrödinger equation*,
Revista Matemática Iberoamericana 32 (2016), 795–833.

Primary PDF: <https://arxiv.org/pdf/1406.6002>, Theorem 1, Lemma 1.
Publisher: <https://ems.press/journals/rmi/articles/14122>.

For $d=1,2,3$ and $1<p<1+4/d$, they construct scalar minimal-total-mass
solutions of

$$
 iu_t+\Delta u+|u|^{4/d}u+|u|^{p-1}u=0
$$

with any prescribed energy and

$$
 \lambda(t)\sim C_p(T-t)^\sigma,
 \qquad \sigma=\frac4{4+d(p-1)}\in(1/2,1).
$$

These collapse **more slowly** than the pseudoconformal width $T-t$, whereas
our candidate width is smaller. In their model the attractive perturbation
energy grows like $-\lambda^{-d(p-1)/2}$; our proposed matched correction
vanishes like $-cA\lambda$. The principle that a lower-order perturbation can
select a different critical collapse rate is therefore not new. The particular
self-consistent vector interaction is not covered by their theorem. Their
defocusing lower-power perturbation gives global bounded critical-mass solutions
(Lemma 1), again a different sign and equation.

## 4. Faster-than-pseudoconformal scalar NLS is known for interacting multiple bubbles

Yvan Martel, Pierre Raphaël,
*Strongly interacting blow up bubbles for the mass critical NLS*,
Annales scientifiques de l’École Normale Supérieure 51 (2018), 701–737.

Primary PDF: <https://arxiv.org/pdf/1512.00900>, Theorem 1 and Corollary 2.
Publisher: <https://www.numdam.org/articles/10.24033/asens.2364/>.

For the two-dimensional scalar cubic equation they construct configurations of
$K\ge2$ interacting ground-state bubbles. Pseudoconformal transformation of
their infinite-time concentrating solutions gives finite-time blowup with

$$
 \|\nabla u(t)\|_2\sim
 \sqrt K\|\nabla Q\|_2\frac{|\log(T-t)|}{T-t}.
$$

The bubble widths are of order $(T-t)/|\log(T-t)|$, and $K M_c$ concentrates
at the final point. This is neither the proposed exponent nor a single
principal critical-mass core with a nonconcentrating odd component. It rules out
any broad claim that faster-than-pseudoconformal behavior itself would be new
to critical NLS.

## 5. The exponent two already occurs in a different mass-critical dispersive equation

Uihyeon Jeong, Kihyun Kim, Taegyu Kim, Soonsik Kwon,
*Classification of single-bubble blow-up solutions for Calogero–Moser derivative
nonlinear Schrödinger equation*, arXiv:2601.07410 (January 2026).

Primary PDF: <https://arxiv.org/pdf/2601.07410>, Assumption 1.2, Theorem 1.3,
Remarks 1.7–1.12.

Their **nonlocal derivative** equation is
$iu_t+u_{xx}+2D_+(|u|^2)u=0$, $D_+=(-i\partial_x)\Pi_+$.
Under a single-soliton-plus-$L^2$-radiation decomposition and
$u_0\in H^{2L+1}$, they prove either
$\lambda\sim\ell(T-t)^{2k}$, $1\le k\le L$, or
$\lambda\lesssim(T-t)^{2L+3/2}$. The quantized branch has convergent phase.
Their Remark 1.11 anticipates radiation
$q|x-x_*|^{2k-2}(x-x_*)$ near the singularity, but explicitly leaves that
refined expansion unproved. In particular, its $k=1$ odd-slope analogy must
not be promoted to an established radiation-selection theorem.

This comparison gives a useful structural precedent, not a transferable proof:
CM-DNLS has integrability, algebraic soliton tails, and a different linearized
operator; our quintic candidate has an exponentially decaying core and rapid
phase $\theta'\sim\lambda^{-2}$. Their Remark 1.12 also records the unresolved
scalar near-soliton question whether the fast alternative $\lambda\lesssim T-t$
must actually be pseudoconformal.

Earlier **construction**, independently of that classification:

* Kihyun Kim, Taegyu Kim, Soonsik Kwon,
  *Construction of smooth chiral finite-time blow-up solutions to Calogero–Moser
  derivative nonlinear Schrödinger equation*,
  <https://arxiv.org/pdf/2404.09603>.
* Uihyeon Jeong, Taegyu Kim,
  *Quantized blow-up dynamics for Calogero–Moser derivative nonlinear Schrödinger
  equation*, <https://arxiv.org/pdf/2412.12518>, v2 April 2026.
  This constructs the sequence of smooth quantized blowup solutions using
  modulation and the conservation-law hierarchy, without claiming that every
  allowable exotic rate is realized.

Consequently neither “the first quadratic width” nor “the first radiation-driven
nonpseudoconformal collapse” is a defensible description of the present work.

## 6. Inhomogeneous scalar constructions do not settle the zero-energy branch

Naoki Matsui, *Minimal-mass blow-up solutions for inhomogeneous nonlinear
Schrödinger equations with growth potentials*, arXiv:2108.06205;
Arkiv för Matematik 61 (2023).

Primary text: <https://arxiv.org/html/2108.06205v2>, Theorem 1.7.

For a scalar critical NLS with a spatial coefficient and an allowed static
potential, the theorem constructs minimal-mass solutions with **prescribed
positive** energy $E_0>0$ and

$$
 \lambda(t)=\sqrt{8E_0/\|yQ\|_2^2}\,|t|(1+o(1)).
$$

It is a construction theorem with explicit coefficient/potential hypotheses,
not a classification of arbitrary time-dependent self-consistent potentials.
It does not conclude anything about the degenerate $E_0=0$ mechanism proposed
here. No inspected primary theorem establishes our exact vector branch through
this route. Failure to find one is not proof of novelty.

## 7. The 2026 “universal bound” does not forbid fast quadratic collapse

Beomjong Kwak, Soonsik Kwon,
*A universal bound on the blow-up rate for the focusing mass-critical nonlinear
Schrödinger equation*, arXiv:2602.21968 (February 2026).

Primary text: <https://arxiv.org/html/2602.21968v1>, Theorems 1.1, 1.2, 1.5,
Corollary 1.4.

The equation is scalar $iu_t+\Delta u+|u|^{4/d}u=0$. Theorem 1.1 says that,
for every $\epsilon>0$, at least $M_c$ concentrates along a sequence in
windows of radius $\epsilon\sqrt{T-t}$. Theorem 1.2 gives a log-log-improved
**upper bound for a concentration radius in an integrated sense** for radial
solutions in $d\ge2$. These improve the slowest permitted concentration;
they do not give a lower bound $\lambda\gtrsim T-t$. A hypothetical width
$\lambda\sim(T-t)^2$ is compatible with their concentration conclusions.
Moreover, the theorems as stated are not vector one-dimensional results.

## 8. Known vector classification is at a different mass and for different coupling

Xing Cheng, Zuyu Ma, Jiqiang Zheng,
*Classification of the minimal-mass blowup solutions to the two dimensional
focusing cubic nonlinear Schrödinger system*, arXiv:2504.01674v2 (April 2025).

Primary PDF: <https://arxiv.org/pdf/2504.01674>, equation (1.1), introduction,
main classification.

Their nonlinearity is
$F_j=2(\sum_k|u_k|^2)u_j-|u_j|^2u_j$, and their threshold is the **total**
vector scattering mass of its ground state. Finite-component minimal-total-mass
solutions are classified as solitons or pseudoconformal transforms. The
coefficient of cross-coupling differs even from the two-dimensional
common-density system, and it is not the one-dimensional quintic equation.
Most importantly, fixing a largest Gram occupation at $M_c$ with nonzero
remaining occupations does not put a solution at a scalar or vector
minimal-total-mass threshold. This classification cannot be applied by replacing
its mass assumption with our occupation assumption.

## 9. Direct checks against the internal R18 regular-background result

These checks are deductions from the current candidate and the stated R18
hypotheses, not claims imported from the cited literature.

In the cubic system the principal component sees the secondary density as a
linear potential. In the quintic system, with $S=\sum_{j\ge2}|u_j|^2$,

$$
 \rho^2u_1=|u_1|^4u_1+
 \underbrace{(2S|u_1|^2+S^2)}_{V_{\rm eff}(t,x)}u_1.
$$

At $x=\lambda y$, the candidate gives
$|u_1|^2\sim\lambda^{-1}Q^2$ and
$S\sim A\lambda^2F^2$. Hence

$$
 V_{\rm eff}\sim 2A\lambda Q^2F^2,
 \qquad \partial_x^2 V_{\rm eff}=O(A/\lambda).
$$

For $\lambda\sim h^2$, that is the borderline $h^{-2}$, outside the R18
assumption $\|\nabla^2V\|_\infty\lesssim h^{-\alpha}$, $\alpha<2$.
“Smooth terminal secondary background” therefore does not imply the relevant
effective-potential regularity. The boundary layer makes that distinction
essential.

The principal chirp energy is of order $\dot\lambda^2\sim h^2$, so a
transport estimate based on its time integral allows variance of order $h^4$.
The companion outer-matching calculation shows how secondary radiation at
distance $\sqrt h$ contributes the same variance order. A variance argument
that discards it cannot rule out the proposed branch.

## 10. What can and cannot presently be concluded

The source comparison has not located a theorem that proves or forbids the
specified local-vector, principal-critical-mass quadratic branch. The scalar
minimal-total-mass classification, double-power theorems, known multi-bubble
construction, and universal concentration bounds each have identifiable
hypotheses preventing such a conclusion.

The candidate is mathematically specific: orthogonality removes the transverse
bound state; zero-energy scattering supplies a linear-in-width energy
correction; the zero residual-core-energy branch then predicts a quadratic
width. The solvable potential, modulation method, altered critical rates, and
quadratic widths in other PDEs all have prior precedents. Any eventual novelty
would have to reside in proving this coupled PDE mechanism, its actual rate
and coefficient, and the class of initial data realizing it.

What remains indispensable is an exact nonlinear construction or exclusion:
a sufficiently accurate smooth inner/outer composite, control of the singular
time-dependent linearized flow and primary unstable modes, exact mass/Gram
constraints, and an error estimate small enough to justify the proposed
$O(\lambda)$ energy balance. The literature comparison cannot substitute for
those steps.
