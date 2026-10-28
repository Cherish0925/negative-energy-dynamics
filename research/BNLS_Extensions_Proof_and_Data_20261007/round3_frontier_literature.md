# Beyond the four-dimensional traveling counterexample: source audit and next theorems

Research notes, 2026-10-07. These notes distinguish consequences of the existing certified construction from extensions which still require a new proof. They do not assert that any named paper exhausts the literature.

## 1. Immediate conclusions of the search

1. No directly applicable published multi-soliton theorem was located for the pure fourth-order, four-dimensional cubic equation with the small-speed excited waves constructed in the current project. There are nearby results, but their model, dimension, or speed hypotheses differ materially.
2. An exact outgoing pair of opposite-speed waves would give an exact zero-momentum, negative-energy, forward-global bounded solution. Establishing that exact pair is a substantial remaining theorem; separated approximate sums do not suffice.
3. The homogeneous biharmonic negative-energy blowup theorems of Boulenger--Lenzmann and the Dinh papers checked below are radial. Several apparently relevant “nonradial fourth-order” titles concern an inhomogeneous spatial weight. They do not prohibit continuation of the present nonradial waves to powers slightly above cubic in dimension four.
4. There is a genuine conflict with the literal energy-space conclusion of Gou's cylindrical mass-critical theorem. Its assumptions include the present symmetry, once finite axial moments are established. The separate file `round3_gou_audit.md` proves those moments and identifies the unavailable bounded-gradient virial closure. One should report the conflict and its precise mathematical audit, not silently omit it or infer a false conclusion merely from a title.
5. Negative effective inertia alone is not a stability theorem. The existing certificates suggest a feasible Hamiltonian-index instability proof, but a full-kernel/Morse-index certificate and the functional-analytic hypotheses must still be completed.

## 2. Exact zero-momentum implication from a hypothetical two-soliton

Use the current convention

\[
iu_t=\Delta^2u-|u|^2u,\quad
P(f)=\operatorname{Im}\int\bar f\nabla f,\quad
E(f)=\tfrac12\|\Delta f\|_2^2-\tfrac14\|f\|_4^4.
\]

Fix one of the small nonzero speeds for which the certified branch has
\(E(Q_v)<0\), \(Q_{-v}=\overline{Q_v}\), and
\(P(Q_{-v})=-P(Q_v)\). Define

\[
R_\pm(t,x)=e^{it}Q_{\pm v}(x\mp vt e_1).
\]

**Conditional gluing implication.** Suppose there is an exact solution on
\([T,\infty)\) satisfying
\[
\|u(t)-R_+(t)-R_-(t)\|_{H^2}\longrightarrow0.
\]
Then, by conservation and separation,
\[
M(u)=2M(Q_v),\qquad P(u)=0,\qquad E(u)=2E(Q_v)<0,
\]
and \(\sup_{t\ge T}\|u(t)\|_{H^2}<\infty\).

Here are all steps in the last statement. Translated fixed \(H^2\) functions become orthogonal in the mass, gradient, and Laplacian pairings as their relative displacement tends to infinity; this follows first for compactly supported smooth functions, then by density. The mixed quartic integrals vanish by the same approximation and \(H^2(\mathbb R^4)\hookrightarrow L^4\). Thus the sum's mass, momentum, and energy approach the sum of the constituents' quantities. Each functional is continuous on bounded \(H^2\) sets. Their conservation makes the limiting identities exact at every finite time. The asymptotic bound controls all sufficiently large times, while continuity controls the remaining compact interval. Translating time gives a forward-global initial-value solution on \([0,\infty)\). This argument does not prove backward global existence.

The pair can be arranged to be even under ordinary spatial reflection:
\[
R_+(t,-s,y)+R_-(t,-s,y)=R_+(t,s,y)+R_-(t,s,y),
\]
using \(Q_v(-s,y)=\overline{Q_v(s,y)}=Q_{-v}(s,y)\). Ordinary reflection and transverse \(O(3)\) symmetry are invariant under the forward PDE and force all components of momentum to vanish. In contrast, reflection combined with conjugation is a useful *profile* symmetry but involves time reversal for the evolutionary equation. A gluing proof must use the correct invariant symmetry.

The main missing ingredients are control of the full linearized flow, its unstable finite-dimensional directions, neutral phase/translation directions, and the dispersive continuous component for two separating centers. A crude backward Duhamel contraction may require the interaction-decay exponent to dominate a linear growth exponent. That is not automatic when \(v\) is small. A spectral trichotomy with unstable-mode shooting is a plausible route, but has not been proved here.

Common scaling does not remove this issue. The frequency family is
\[
Q_{\omega,v}(x)=\omega^{1/2}Q_{1,v\omega^{-3/4}}(\omega^{1/4}x).
\]
At fixed dimensionless speed, the spatial decay scale is \(\omega^{1/4}\), physical speed is proportional to \(\omega^{3/4}\), and temporal spectral rates are proportional to \(\omega\). Interaction rates and linear growth rates therefore scale together. Merely rescaling both waves does not establish a required large *dimensionless* relative speed.

## 3. Closest multi-wave sources and their actual scope

### 3.1 Wang: a different fourth-order equation in one dimension

Zhong Wang, *Multi solitary waves for a fourth order nonlinear Schrödinger type equation*, Nonlinear Analysis: Real World Applications 37 (2017), 287--308.

- Publisher: <https://www.sciencedirect.com/science/article/abs/pii/S146812181730038X>
- Author's primary exposition: <https://nowaves.sciencesconf.org/data/pages/NoWaves_Wang.pdf>, especially the displayed equation on slide 3 and Theorem 2.1 around slide 14.

This is a one-dimensional Hasimoto/vortex-filament equation containing second and fourth spatial derivatives, derivative nonlinearities, and cubic/quintic terms. It is not the pure BNLS equation. The theorem assumes negative fourth-order coefficient, sufficiently large carrier parameters, positive frequency parameters, and distinct speeds of a special solitary-wave family. It constructs an exponentially accurate outgoing sum in \(H^2\) for sufficiently large times. It does not cover arbitrary excited four-dimensional profiles or the present small-speed branch.

### 3.2 Côte--Le Coz: arbitrary bound states but second-order NLS and large relative speeds

Raphaël Côte and Stefan Le Coz, *High-speed excited multi-solitons in nonlinear Schrödinger equations*, arXiv:1007.3034.

- <https://arxiv.org/abs/1007.3034>
- <https://arxiv.org/html/1007.3034v2>
- Author manuscript: <https://hal.science/hal-00503279v1/file/cote-lecoz.pdf>

Theorem 1 permits general \(H^1\) stationary bound states, including excited states, for a second-order NLS with a sufficiently regular focusing energy-subcritical nonlinearity. Its profiles are Galilean boosts of those stationary states. A lower bound on all relative velocities, depending on the profiles, is required; the result gives an exact outgoing multi-soliton with exponential convergence for large time. Its unstable-mode constructions are relevant methodological precedents. It cannot be inserted unchanged here: BNLS has no corresponding Galilean boost symmetry, and our available waves have small dimensionless speeds.

### 3.3 Parker--Aceves: spatial multi-pulses are not outgoing multi-solitons

Ross Parker and Alejandro Aceves, *Multi-pulse solitary waves in a fourth-order nonlinear Schrödinger equation*, arXiv:2009.01647.

- <https://arxiv.org/abs/2009.01647>
- <https://arxiv.org/html/2009.01647v3>

The setting is a one-dimensional cubic equation with second/fourth dispersion. The construction concerns localized standing profiles composed of spatially separated pulses, based on an associated fourth-order ODE and nondegeneracy/transversality hypotheses. The separations within a bound profile do not grow linearly in time. Thus a multi-pulse existence theorem of this type is not an exact opposite-velocity two-soliton theorem for the four-dimensional equation.

## 4. Blowup sources: what does and does not obstruct further continuation

### 4.1 Homogeneous radial results

Boulenger--Lenzmann, *Blowup for biharmonic NLS*:

- <https://arxiv.org/abs/1503.01741>
- Journal version: <https://numdam.org/item/10.24033/asens.2326.pdf>

The general negative-energy theorems relevant here impose radial symmetry. They do not supply an all-nonradial obstruction to the present traveling branch.

Van Duong Dinh, *Dynamics of radial solutions for the focusing fourth-order nonlinear Schrödinger equations*:

- <https://arxiv.org/pdf/2001.03022>

The equation is homogeneous with \(N\ge2\), \(\mu\ge0\), and power \(\alpha>8/N\), below the energy-critical exponent when \(N\ge5\). The scattering and blowup conclusions in question concern radial initial data. A traveling nonradial wave in dimension four is outside that hypothesis.

Dinh, *On blowup solutions to the focusing intercritical nonlinear fourth-order Schrödinger equation*:

- <https://arxiv.org/pdf/1801.08866>

Proposition 4.3 treats radial \(H^2\) data with \(d\ge2\), \(8/d<\alpha<\alpha^*\), \(\alpha\le8\), and threshold conditions. Proposition 4.5 also assumes radial data and, additionally, \(d\ge5\), \(\alpha<4\), negative energy, and bounded critical norm. Neither is an unrestricted nonradial theorem in dimension four.

A search hit entitled *Blow-up criteria for fractional nonlinear Schrödinger equation*, arXiv:1808.07368, really does concern nonradial data, but its fractional exponent is \(s\in(1/2,1)\). It is not a result for the biharmonic exponent \(s=2\): <https://arxiv.org/abs/1808.07368>.

### 4.2 Gou's actual cylindrical theorem, and the exact conflict

Tianxiang Gou, *Blowup of cylindrically symmetric solutions for biharmonic NLS*, arXiv:2205.08167v3; published in Proceedings of the Edinburgh Mathematical Society 67 (2024), 1085--1098, DOI 10.1017/S001309152400066X.

- <https://arxiv.org/pdf/2205.08167>
- <https://doi.org/10.1017/S001309152400066X>

Theorem 1.1 requires \(d\ge5\), \(0<s_c<2\), and \(0<\sigma\le1\), so it does **not** cover the proposed dimension-four continuation to \(p=2\sigma+1>3\). Theorem 1.2 assumes \(d\ge4\), \(s_c=0\), \(\mu\ge0\), negative energy, and cylindrical data with finite axial variance. It states finite blowup for \(\mu>0\), and finite or infinite-time blowup for \(\mu=0\). The proof invokes the Boulenger--Lenzmann closure after using a multiplier with axial quadratic growth. The latter has unbounded gradient. Source details and a complete mathematical audit are in `round3_gou_audit.md`.

The following diagnosis is our calculation, not a claim drawn from another source. For
\(\phi_R(y,s)=\psi_R(|y|)+s^2/2\), a translated wave obeys exactly
\[
M_{\phi_R}(e^{it}W(y,s-vt))=M_{\phi_R}(W)+2vtP_s(W).
\]
Its \(H^2\) norm is constant. Thus an estimate bounding this virial solely by conserved mass and a power of the \(H^2\) norm cannot hold uniformly along axial translations when \(P_s(W)\ne0\). A valid estimate contains \(\|s u(t)\|_2\), which can grow linearly. This identifies the missing inference. The companion audit establishes finite axial moment for our profile by a cutoff-commutator argument, so failure to verify that hypothesis is not a resolution of the conflict. A proof gap alone does not disprove a theorem; the existing certified construction and its extensions are the distinct mathematical evidence to be checked against the assertion.

### 4.3 Low dimensions and inhomogeneous false friends

Leonard Dinh, *Finite-Time Blow-Up of Radial Negative-Energy Solutions for the Mass-Critical Biharmonic Nonlinear Schrödinger Equation*, posted 2026-10-02:

- <https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/>

The stated new conclusion covers radial \(H^2\) data in \(N\ge2\), using exponential localization. It does not remove the symmetry assumption in dimensions two or three.

Bai--Majdoub--Saanouni, *Non-radial Blow-up for a mass-critical fourth-order inhomogeneous nonlinear Schrödinger equation*, arXiv:2312.07002v2:

- <https://arxiv.org/pdf/2312.07002>

Theorem 1.2 assumes the weight \(|x|^{-b}\) with strictly positive \(0<b<\min(N/2,4)\), power \((8-2b)/N\), and nonnegative second-order coefficient. Its negative-energy result is finite blowup for positive second-order coefficient and finite/growup alternatives when that coefficient vanishes. The strict spatial weight is essential to the argument; setting \(b=0\) does not yield the homogeneous theorem sought here.

Dinh, *Non-radial finite time blow-up for the fourth-order nonlinear Schrödinger equations*, Applied Mathematics Letters 132 (2022), 108084:

- <https://doi.org/10.1016/j.aml.2022.108084>

Despite the broad title, the focusing nonlinearity is spatially inhomogeneous, \(-|x|^{-2}|u|^{4/n}u\). This is another result that cannot be used as a homogeneous BNLS obstruction.

Within the primary-source searches completed on 2026-10-07, no theorem was located settling all nonradial negative-energy homogeneous mass-critical data in \(N=2,3\). This is a bounded literature-search conclusion, not a proof of worldwide novelty or nonexistence of an overlooked paper.

## 5. Stability: precise distinction and a feasible additional certificate

For the certified real radial profile set
\[
L_+=\Delta^2+1-3Q^2,\quad L_-=\Delta^2+1-Q^2,\quad
I=\langle\partial_1Q,L_-^{-1}\partial_1Q\rangle<0.
\]
This \(I\) is a translation-response pairing. It is not the Vakhitov--Kolokolov frequency pairing, and its sign alone is not a universal instability criterion.

Iyer--Parker--Stefanov, *Existence and stability for traveling waves of fourth order semilinear wave and Schrödinger equations*, arXiv:2512.12390:

- <https://arxiv.org/html/2512.12390v1>

Its NLS stability result in Section 6 concerns one-dimensional standing waves of a mixed-dispersion cubic equation. The relevant variational branch has nonnegative \(L_-\), a single negative direction for \(L_+\), and an additional nondegeneracy requirement for the sharp slope criterion. Those are not the spectral properties of our excited four-dimensional profile. Its beam-equation traveling-wave results must not be re-labelled as NLS traveling-wave results.

The appropriate broader references are Grillakis--Shatah--Strauss II and Hamiltonian--Krein index theory:

- GSS II: <https://doi.org/10.1016/0022-1236(90)90016-E>.
- Kapitula--Kevrekidis--Sandstede (2004): <https://doi.org/10.1016/j.physd.2004.03.018>.
- Their 2005 addendum: <https://doi.org/10.1016/j.physd.2004.11.015>.

These connect the Hessian's negative directions, symmetry constraints, and unstable spectrum. Applying the odd-index instability mechanism requires checking the full kernel, finite negative index, positive essential part, the constraint/action Hessian, and the relevant evolution and regularity hypotheses. Nonlinear orbital instability requires the corresponding nonlinear-flow assumptions in addition to a spectral calculation.

The following is our new analytic reduction. Let
\[
d(\omega,\mathbf v)=\left(E+\tfrac\omega2M-\tfrac12\mathbf v\cdot P\right)(Q_{\omega,\mathbf v}).
\]
Critical scaling and rotation symmetry give
\[
d(\omega,\mathbf v)=\omega d(1,\mathbf v\omega^{-3/4})
=\omega d_0-\tfrac I2|\mathbf v|^2\omega^{-1/2}
+O(|\mathbf v|^4\omega^{-2}).
\]
The three transverse velocity eigenvalues of its Hessian are positive for small nonzero \(\mathbf v\), because their leading value is \(-I\omega^{-1/2}\). The longitudinal-frequency block has
\[
d_{\omega\omega}=-\tfrac{3I}{8}|\mathbf v|^2\omega^{-5/2}+O(|\mathbf v|^4),\quad
d_{\omega v}=\tfrac I2v\omega^{-3/2}+O(v^3),\quad
d_{vv}=-I\omega^{-1/2}+O(v^2),
\]
and determinant \(I^2v^2\omega^{-3}/8+O(v^4)>0\). Hence this five-parameter action Hessian is positive definite for sufficiently small nonzero speeds. At zero speed the frequency direction is degenerate, so applying a nondegenerate scalar slope rule there would be invalid.

For a radial function in dimension four, the degree-\(\ell\) spherical harmonics have multiplicity \((\ell+1)^2\). Existing certificates yield two negative radial \(L_+\) eigenvalues, one negative \(\ell=2\) eigenvalue per channel, and positivity in \(\ell\ge4\). The full \(L_-\) index is five: one radial and four degree-one negative directions, with only the phase kernel. The existing degree-one Hilbert--Schmidt output also encloses \(\operatorname{tr}(K_{1,1}^2)<1.24\); together with its top eigenvalue lower bound and the exact translation eigenvalue \(1/3\), this controls the degree-one \(L_+\) channel.

The remaining useful small certificate is a lower bound above one for the top eigenvalue of \(K_{3,3}\). The numerical value is approximately \(1.333846\), but this number is **not** a rigorous lower bound. An exact Rayleigh lower bound, combined with the already certified squared Hilbert--Schmidt bound \(\|K_{3,3}\|_{HS}^2<1.98\), would exclude extra eigenvalues at one and fix the entire Morse count. The expected count is
\[
n(L_+)=2+4+9+16=31,\quad n(L_-)=5,\quad n(L)=36.
\]
The only kernels would then be phase plus four translations. After continuity to a small nonzero velocity and verification of the index theorem's hypotheses, \(n(L)-p(d'')=36-5=31\) is odd and would give an instability result. The present note does not claim that this final application has already been completed.

## 6. Recommended next targets, separated by logical status

**Direct analytic extensions from existing exact inputs:** smooth parameter continuation in frequency, small second-order dispersion, and powers near cubic; correct momentum/energy identities for each; weighted profile regularity; the counterexample's conflict with a cylindrical virial closure. The corresponding parameter domain must come from an IFT argument, not from a numerically guessed fixed velocity.

**One short additional spectral certification plus an analytic application:** full Morse index and instability of the small-speed branch. This is the closest extension of the existing proof machinery.

**A substantive new PDE theorem:** exact opposite-speed outgoing two-soliton gluing, which would settle the zero-total-momentum variant negatively in dimension four. No claim of that conclusion is justified until the gluing is exact.

**Separate dimensional projects:** existence and validated negative inverse pairing for suitable two- or three-dimensional profiles. Continuous numerical continuation in dimension is a discovery device, not a proof for a new integer dimension; nonlinear mapping regularity and all spectral obligations must be re-established there.

## Source retrieval record for the parent report

Useful currently retrieved source IDs: Gou `turn110academia23` / `turn102view0`; Dinh radial `turn110academia24` / `turn103view1`; Dinh intercritical `turn111academia20` / `turn103view0`; fractional false friend `turn111search6`; inhomogeneous Dinh `turn110search1`; Bai et al. `turn110academia26` / `turn101view0`; Meta radial update `turn110search5`; Wang slides `turn97view1`; Côte--Le Coz `turn97view2` / `turn108view0`; Parker--Aceves `turn97view4`; Iyer et al. `turn95view0`; GSS II `turn112search14`; Hamiltonian--Krein paper/addendum `turn112search0` and `turn112search2`. Parent should open sources itself before using browser citations in a final user-facing answer.
