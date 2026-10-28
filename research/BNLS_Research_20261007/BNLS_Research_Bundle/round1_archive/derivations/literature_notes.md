# Nonradial mass-critical BNLS: literature check, 2026-10-07

## Exact target

For N >= 2, i u_t = Delta^2 u - |u|^(8/N)u on R^N, arbitrary H^2 initial data, E(u_0)<0. Determine whether both maximal lifespan endpoints are finite. No radiality, finite-variance, bounded-domain, or spatially decaying nonlinear coefficient is part of the target.

## Primary sources checked

1. Thomas Boulenger and Enno Lenzmann, *Blowup for Biharmonic NLS*, arXiv:1503.01741v2 (2015), Ann. Sci. ENS (2017).
   - https://arxiv.org/pdf/1503.01741
   - Web refs: turn4view0, turn20view1. Theorem 3, PDF pp. 4-5: radial H^2, N>=2, negative energy, mu=0 gives finite-time blowup OR global grow-up with ||Delta u(t)||_2 >= C t^2 for sufficiently large t; stronger subsequential growth in N>=5. Mu>0 gives finite-time blowup.
   - Section 1.5, PDF p. 8 explicitly identifies nonradial whole-space blowup as an open problem. Localized virial and Riesz bivariance identities themselves do not require radiality; error estimates do.

2. Leonard Dinh, *Finite-Time Blow-Up of Radial Negative-Energy Solutions for the Mass-Critical Biharmonic Nonlinear Schrödinger Equation*, posted October 2, 2026, Meta AI research page.
   - https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/
   - Landing-page web ref turn1view0; Download the Paper link 18 leads to 20-page PDF, ref turn4view2. Useful opened refs turn8view1, turn8view2, turn12view0, turn20view0.
   - Theorem 1.1, PDF p. 2, states that radial H^2 solutions in every N>=2 with E<0 have T_+,T_- finite. No finite variance assumption.
   - Remark 1.4, PDF p. 5, explicitly retains the nonradial question and locates radiality in Proposition 3.1. It proposes seeking a nonradial weighted interpolation, moving-center localization, or interaction virial method.
   - Weight omega_R(x)=1-exp(-|x|^4/R^4); defect D_R(u)=integral omega_R |D^2u|_F^2. Proposition 3.1 gives arbitrary-epsilon absorption for radial functions with a mass-dependent R^-4 remainder. The virial-defect and Riccati steps are described as symmetry independent.
   - This is a research manuscript reporting a theorem, not evidence of journal acceptance. Our search found no general nonradial theorem or verified counterexample; this is a search result, not proof of absence.

3. Tianxiang Gou, *Blowup of cylindrically symmetric solutions for biharmonic NLS*, arXiv:2205.08167v3 (2024).
   - https://arxiv.org/pdf/2205.08167
   - Web ref turn14view0. Theorem 1.2: N>=4, sigma=4/N, E<0, u_0(y,x_N)=u_0(|y|,x_N), x_N u_0 in L^2. For mu=0 the result still allows finite OR infinite time blowup. Thus it is neither a general nonradial theorem nor a finite-time solution to the target.

4. Renzo Scarpelli and Maicon Hespanha, *Blow-up results for inhomogeneous fourth-order nonlinear Schrödinger equation*, ZAMP 77, 176 (2026).
   - https://link.springer.com/article/10.1007/s00033-026-02768-y
   - Web refs turn14view2, turn20view2. Its nonradial results assume a strictly positive inhomogeneity exponent b and concern the energy-critical regime. The nonlinear coefficient |x|^-b supplies spatial decay absent from our homogeneous target. Do not present this as resolving the problem.

## Independent obstruction to the exact suggested nonradial interpolation

The following is an elementary scaling calculation performed here, not a claim from the above papers.

Fix R>0, x_0 != 0, and nonzero f in C_c^infinity(R^N). Put p=2+8/N and u_lambda(x)=lambda^(N/2) f(lambda(x-x_0)). All u_lambda have identical mass m=||f||_2^2. By change of variables and dominated convergence,

lambda^-4 integral omega_R |u_lambda|^p -> omega_R(x_0)||f||_p^p,

lambda^-4 integral omega_R |D^2 u_lambda|_F^2 -> omega_R(x_0)||D^2 f||_2^2.

If the proposed arbitrary-epsilon bound held for every nonradial u with constant C(epsilon,m), divide it by lambda^4 and let lambda -> infinity. It would require ||f||_p^p <= epsilon ||D^2 f||_2^2 for every epsilon>0, contradiction. The same contradiction survives any fixed weight continuous and strictly positive at some concentration point, and any finite remainder depending only on epsilon, mass, and R.

It can be placed inside the negative-energy class: replace f by A f with A large enough that E(Af)<0. Then E(u_lambda)=lambda^4 E(Af)<0, mass is still fixed, and choose epsilon less than ||Af||_p^p / ||D^2(Af)||_2^2. This does NOT disprove the dynamical blowup conjecture. It disproves only this proposed symmetry-free static inequality, so a proof must exploit additional dynamics, concentration geometry, a different functional, or a restriction on admissible configurations.

## Useful source retrieval for root citations

Root must open relevant webpage refs itself before citing subagent results. Open the Meta landing page and click its paper link for the exact primary PDF; open https://arxiv.org/pdf/1503.01741 for the original theorem and Section 1.5. Stable landing links are preferable to the expiring Facebook CDN PDF URL in bibliography.

## Appendix A. Audited stronger obstruction: arbitrary center, fixed mass and negative energy

**Proposition (static obstruction, independently checked).** Let N>=2, p=2+8/N and fix R>0. Define

\[
 w_R(z)=1-e^{-|z|^4/R^4},\qquad
 F_a(u)=\int w_R(x-a)|u|^p\,dx
 -\varepsilon\int w_R(x-a)|D^2u|_F^2\,dx.
\]

For every fixed 0<epsilon<p/2, there are a number M_*>0 and real-valued U_lambda in C_c^infinity(R^N), lambda tending to infinity, with

\[
 M(U_\lambda)=M_*,\quad E(U_\lambda)=-1,\quad
 P(U_\lambda)=\operatorname{Im}\int\overline{U_\lambda}\nabla U_\lambda=0,
 \qquad \inf_{a\in\mathbb R^N}F_a(U_\lambda)\longrightarrow+\infty.
\]

Consequently no bound F_{a(u)}(u)<=C(epsilon,M(u),E(u)) R^-4 can hold on all negative-energy H^2 data, even if the center a(u) is selected optimally and the constant depends on the conserved mass, energy and momentum. The scale R is fixed: this statement does not exclude a strategy with an adaptively diverging R(u).

**Proof.** For a nonzero real phi in C_c^infinity let K_phi=||Delta phi||_2^2 and A_phi=||phi||_p^p. Set

\[
 c=\left(\frac{pK_\phi}{2A_\phi}\right)^{1/(p-2)},\qquad f=c\phi.
\]

Then E(f)=0. By integration by parts (or Plancherel), ||D^2 f||_2^2=||Delta f||_2^2=:K_f, and A_f:=||f||_p^p=(p/2)K_f. Thus delta:=A_f-epsilon K_f=(p/2-epsilon)K_f>0.

Pick distinct fixed points a_1,a_2, with d=|a_1-a_2|>0. Choose a third real compactly supported function g whose support stays a positive distance from both points and E(g)=-1. Existence is elementary: for any nonzero real compact bump chi supported away from a_1,a_2, E(B chi)=B^2 K_chi/2-B^p A_chi/p tends to minus infinity as B tends to infinity and is continuous, hence equals -1 for some B>0.

Define

\[
 f_{\lambda,j}(x)=\lambda^{N/2}f(\lambda(x-a_j)),\qquad
 U_\lambda=f_{\lambda,1}+f_{\lambda,2}+g.
\]

For all sufficiently large lambda the three supports are pairwise disjoint. Their derivative supports are contained in the corresponding supports. Locality and mass-critical scaling give the exact identities

\[
 M(U_\lambda)=2M(f)+M(g)=M_*,\qquad
 E(U_\lambda)=2\lambda^4E(f)+E(g)=-1.
\]

All functions are real, so P(U_lambda)=0 exactly.

For uniformity in a, the derivative is

\[
 |\nabla w_R(z)|=\frac4R\left(\frac{|z|}{R}\right)^3
 e^{-(|z|/R)^4}\le\frac{C_0}{R},\qquad
 C_0=4(3/4)^{3/4}e^{-3/4}.
\]

Changing variables in each packet therefore gives

\[
 \left|F_a(f_{\lambda,j})-
 \lambda^4w_R(a_j-a)\delta\right|
 \le C_f\lambda^3/R,
\]

where the finite constant

\[
 C_f=C_0\int |y|\bigl(|f(y)|^p+\varepsilon|D^2f(y)|_F^2\bigr)\,dy
\]

is independent of a and lambda. Also F_a(g)>=-epsilon K_g because 0<=w_R<=1. At least one distance |a_j-a| is >=d/2, hence uniformly in a,

\[
 w_R(a_1-a)+w_R(a_2-a)
 \ge c_{R,d}:=1-e^{-(d/(2R))^4}>0.
\]

By disjointness F_a(U_lambda)=F_a(f_lambda,1)+F_a(f_lambda,2)+F_a(g). Consequently

\[
 \inf_a F_a(U_\lambda)
 \ge\delta c_{R,d}\lambda^4-2C_f\lambda^3/R-\varepsilon K_g
 \longrightarrow+\infty.
\]

This proves the assertion. No approximation was used for mass, energy, momentum, or support disjointness. The only asymptotic estimate is the explicit uniform Lipschitz error. This construction is not a BNLS solution family with global lifespans; it refutes the stated instantaneous functional inequality only.

## Appendix B. Brief traveling-wave check

A focused primary-source search did not identify a homogeneous mass-critical H^2 excited traveling wave with rigorously negative energy.

- Iyer, Parker and Stefanov, *Existence and Stability for Traveling Waves of Fourth-Order Semilinear Wave and Schrödinger Equations* (Studies in Applied Mathematics, 2026), https://onlinelibrary.wiley.com/doi/full/10.1111/sapm.70214 (web ref turn39view0): its NLS application is one-dimensional cubic mixed dispersion with a nonzero second-order term, not our homogeneous mass-critical equation.
- Casteras and Foldes, *Existence of traveling waves for a fourth order Schrödinger equation with mixed dispersion in the Helmholtz regime* (Mathematische Annalen, 2026), https://link.springer.com/article/10.1007/s00208-026-03399-4 (refs turn39view1, turn41view3): constructs waves in a sign-changing-symbol regime; the introduction specifically says its profiles are not expected to belong to L^2. Those waves cannot simply be used as H^2 counterexamples.
- The same article points to Casteras's 2020 preprint on prescribed mass and momentum, and to Bugiera-Lenzmann-Schikorra-Sok on boosted ground states. Ground-state results must not be silently extended to arbitrary excited profiles.

Sign convention independently checked: for u(t,x)=e^{i omega t}Q(x-vt), the profile equation is Delta^2 Q+omega Q+i v dot grad Q-|Q|^(p-2)Q=0. With P(Q)=Im integral bar Q grad Q, its action is S=E+omega M/2-v dot P/2. If the profile is sufficiently regular/decaying for the scaling Pohozaev identity, mass-preserving dilation gives 4E(Q)=v dot P(Q)/2, hence E(Q)=v dot P(Q)/8. This identity alone does NOT determine the sign for all excited profiles. For v=0 it does show all such stationary profiles have E=0.
