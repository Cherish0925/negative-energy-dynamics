# Round 9: closest primary literature and scope comparison

Audit date: 2026-10-08. Internal research note for the main manuscript. This is a targeted comparison, not an exhaustive priority certification.

## Result of the comparison

Among the primary sources checked, I did not find the proposed theorem asserting a **uniform strict mass gap above the sharp homogeneous critical mass for every negative-energy traveling profile**, simultaneously allowing a nonnegative dispersion perturbation and a lower-order defocusing nonlinear energy. The closest combined-nonlinearity result found concerns normalized **stationary** solutions and the ordinary threshold, not a strict interval above it.

The distinction to preserve is:

- Classical sharp Gagliardo–Nirenberg coercivity already excludes negative energy at or below the critical mass.
- The proposed profile theorem would exclude negative-energy traveling profiles in an additional open mass interval above that critical mass, uniformly over the specified perturbations.
- That result does not by itself exclude arbitrary global, bounded, nonradial solutions, prove a soliton-resolution theorem, or settle the original finite-time blowup question.

The proposed scope supplied by the parent is

\[
i u_t=(a_m(D)+b(D))u-|u|^{2m/N}u+2G'(|u|^2)u,
\]

where \(m>1\), \(a_m\) is positive elliptic, real, even and homogeneous of degree \(m\),
\(b\ge0\), \(\xi\cdot\nabla b\le mb\), and
\(G\ge0\), \(0\le\rho G'\le(1+m/N)G\).
There is no lower bound on \(\xi\cdot\nabla b\), and no assumption \(G\le\rho G'\).
This note audits related literature; it does not independently certify the emerging proof or its regularity assumptions.

## Closest combined-nonlinearity theorem

**Wenjing Chen and Zexi Wang**, *Normalized solutions to the biharmonic nonlinear Schrödinger equation with combined nonlinearities*, arXiv:2305.16565v1 (2023).

Primary PDF: <https://arxiv.org/pdf/2305.16565>. Retrieved refs: `turn280view0`, `turn283view1`.

They study \(\Delta^2u=\lambda u+\mu|u|^{q-2}u+|u|^{p-2}u\), \(\|u\|_2=a\), \(N\ge2\). In Theorem 1.4, \(p=2+8/N\), \(2<q<p\), and \(\mu<0\): no normalized stationary solution exists for \(a\le\bar a=\|Q\|_2\); the constrained energy infimum equals zero there. For \(a>\bar a\), the infimum is minus infinity. Theorem 1.6 concerns a mass-supercritical leading power and defocusing lower power, with an explicit smallness condition, and yields a radial ground state of positive energy. These results neither quantify a forbidden interval above the critical mass for negative-energy travelers nor address arbitrary positive dispersion perturbations. Their mass parameter is an L² norm, whereas our \(M\) is its square.

**Zhouji Ma, Xiaojun Chang and Zhaosheng Feng**, *Normalized ground state of a mixed dispersion nonlinear Schrödinger equation with combined power-type nonlinearities*, EJDE 2024, no. 29, 1–20, DOI 10.58997/ejde.2024.29.

Primary author-institution record: <https://scholarworks.utrgv.edu/mss_fac/538/>. Retrieved ref: `turn283view0`.

The abstract establishes normalized ground states through constrained minimization, local minima, and the Nehari–Pohozaev manifold. I verified the bibliographic record and abstract, but the linked PDF fetch failed. Consequently this item supports only the nearby existence-literature comparison; it is not evidence for a precise nonexistence theorem or an exhaustive absence claim.

**Jacopo Bellazzini and Luigi Forcella**, *Mass-subcritical Half-Wave equation with mixed nonlinearities: Existence and non-existence of ground states and traveling waves*, DCDS 53 (2026), 131–145, DOI 10.3934/dcds.2025131; online August 2025.

Primary publisher page: <https://www.aimsciences.org/article/doi/10.3934/dcds.2025131>. Retrieved ref: `turn282view1`.

This work proves a critical-mass existence/nonexistence alternative for constrained minimizers and traveling waves with a mass-subcritical focusing power and a mass-subcritical defocusing perturbation; it also proves one-dimensional orbital stability. The operator has order one and the focusing power is subcritical, so neither the dispersion-order assumption nor the critical nonlinearity matches the proposed theorem.

## General-symbol traveling waves: established foundations

**Bugiera–Lenzmann–Schikorra–Sok**, arXiv:1908.06771, *On symmetry of traveling solitary waves for dispersion generalized NLS*.

Primary: <https://arxiv.org/abs/1908.06771>, <https://arxiv.org/pdf/1908.06771>. Retrieved refs: `turn270view1`, `turn267view2`; PDF additionally read locally.

Theorem 1 treats real continuous elliptic symbols of order \(2s\), \(s\ge1/2\), suitable energy-subcritical powers, and frequencies above the bottom of the boosted symbol. Boosted Weinstein minimization yields traveling profiles and compactness modulo translations. When \(s>1/2\), velocity is arbitrary; the order-one endpoint has a velocity restriction. Symmetry results require additional structural hypotheses. This is a substantial general-dispersion existence predecessor, but it does not assert the proposed all-profile negative-energy mass gap with arbitrary defocusing \(G\).

**Naumkin–Raphaël**, arXiv:1712.04484, on small traveling waves for mass-critical fractional NLS.

Primary PDF: <https://arxiv.org/pdf/1712.04484>. Retrieved ref: `turn278view0`.

For one-dimensional fractional dispersion of order \(1<s<2\), mass-critical traveling waves exist below the standing-wave critical mass. Their variational functional is the boosted energy, involving momentum. The sharp inequality makes the unmodified energy positive below that mass. Thus a theorem excluding **all** subthreshold travelers would be false; the proposed negative-unmodified-energy qualification is essential and consistent with this work.

The manuscript already correctly identifies phase-rigidity, phase-kernel coercivity, Gagliardo–Nirenberg compactness and Pohozaev identities as established methods. Related references include Fernández–Jeanjean–Mandel–Mariș (arXiv:2010.01448, Proposition 3.8) and Iyer–Parker–Stefanov (arXiv:2512.12390, Section 3.3.2). Their use should not be marketed as an invention of these underlying principles.

## Fresh October 5 nonradial scattering theorem: exact scope

**Takahisa Inui, Koichi Komada and Kuranosuke Nishimura**, arXiv:2610.05802v1, submitted 2026-10-05, *Scattering of non-radial solutions for the fourth-order Schrödinger equation with H-dot-one-half-critical and supercritical nonlinearity*.

Primary: <https://arxiv.org/abs/2610.05802>, <https://arxiv.org/html/2610.05802v1>. Retrieved refs: `turn273view0`, `turn283view2`, `turn284view1`, `turn284view2`.

Theorem 1.1 assumes \(d\ge2\), \(\mu\ge0\),

\[
1+\frac8{d-1}\le p<1+\frac8{(d-4)_+},
\quad S_\omega(u_0)<S_\omega(Q_\omega),\quad K(u_0)\ge0.
\]

The upper endpoint is infinite for \(d\le4\). It concludes global H² scattering in both time directions. Remark 1.2 explicitly leaves open the nonradial below-ground-state scattering problem for \(d=1\) or \(1+8/d<p<1+8/(d-1)\). Our mass-critical exponent \(p=1+8/d\) is outside the theorem. The transverse virial method requires the higher exponent. Its equation (1.10) already records the compact-orbit averaged identity balancing \(2K\) against center displacement paired with momentum. This identity, also anticipated in older work, is not new here.

## Blowup and near-threshold dynamics

**Bonheure–Castéras–Gou–Jeanjean**, arXiv:1703.07977, *Strong instability of ground states for the biharmonic nonlinear Schrödinger equation*.

Primary PDF: <https://arxiv.org/pdf/1703.07977>. Retrieved refs: `turn261view2`, `turn262view3`–`turn262view5`.

For \(N\ge2\), radial ground states are strongly unstable by finite-time blowup in the specified mass-supercritical range, and also at mass criticality when the second-order dispersion coefficient is positive. For zero second-order coefficient at mass criticality, their Theorem 1.2 gives finite- or infinite-time blowup instability. These are existence-of-nearby-blowup statements around radial ground states, not classifications of every nonradial datum slightly above critical mass. Their stationary Pohozaev relation gives critical stationary energy \(\mu\|\nabla Q\|_2^2/4\ge0\).

**Van Duong Dinh**, arXiv:1706.09304, *On the focusing mass-critical nonlinear fourth-order Schrödinger equation below the energy space*.

Primary PDF: <https://arxiv.org/pdf/1706.09304>. Retrieved ref: `turn264view1`.

The paper supplies concentration and limiting-profile conclusions conditional on finite-time blowup, and global existence below the ground-state mass for suitable rough-data regularity. Its stated minimal-mass profile convergence theorem includes a uniqueness assumption for ground states. It does not prove that arbitrary nonradial negative-energy near-threshold data must blow up, or that all globally bounded negative-energy solutions have a strict mass gap. A uniform finite rescaled-lifespan bound diverging as mass approaches threshold is naturally a consequence of sharp compactness and continuous dependence, not evidence of a separate major innovation.

**Bai–Majdoub–Saanouni**, arXiv:2312.07002v2, on nonradial blowup for the mass-critical fourth-order inhomogeneous equation.

Primary: <https://arxiv.org/html/2312.07002v2>. Retrieved refs: `turn262view2`, `turn269view2`.

The nonradial negative-energy theorem requires a spatial weight \(|x|^{-b}\) with \(0<b<\min(N/2,4)\), and exponent \((8-2b)/N\). Positive second-order dispersion yields finite-time blowup; the pure fourth-order case gives finite- or infinite-time blowup and a growup lower bound. The proof explicitly depends on \(b>0\); setting \(b=0\) is not a permitted deduction. Thus its title cannot be cited as resolving the homogeneous target.

**Meta/Dinh radial result**, public primary research page dated 2026-10-02:

<https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/>. Retrieved ref: `turn266search5`.

The announced theorem assumes radial H² negative-energy data in \(N\ge2\) and proves finite-time blowup in both time directions, using exponential localization and radial interpolation. Its symmetry hypothesis separates it from the original unrestricted nonradial question.

## Higher-order positive perturbations: an established converse mechanism

The proposed gap hypothesis \(\xi\cdot\nabla b\le mb\) has a substantive boundary. For \(b(\xi)=\varepsilon|\xi|^k\), \(k>m\), the parent and independent analyst obtain

\[
I_\varepsilon(M)=\inf_{\|u\|_2^2=M}
\left[\frac12\||D|^{m/2}u\|_2^2+
\frac\varepsilon2\||D|^{k/2}u\|_2^2-
\frac1{2+2m/N}\|u\|_{2+2m/N}^{2+2m/N}\right].
\]

For fixed \(\varepsilon>0\), the claimed sharp alternative is zero and unattained for \(0<M\le M_{c,m}\), and negative and attained for every \(M>M_{c,m}\). The minimizers are standing profiles; their energy identity is
\(E=-(k-m)\varepsilon\||D|^{k/2}Q\|_2^2/(2m)<0\).
Consequently no strict mass gap above the lower-order critical mass survives this higher-order perturbation. This explains a boundary of the proposed robust gap theorem. The mechanism and important exact cases have prior theorems:

**Bonheure–Casteras–Moreira dos Santos–Nascimento**, *Orbitally stable standing waves of a mixed dispersion nonlinear Schrödinger equation*, SIAM J. Math. Anal. **50** (2018), 5027–5071, DOI 10.1137/17M1154138, arXiv:1710.09775v2.

Primary: <https://arxiv.org/html/1710.09775v2>. Retrieved refs: `turn294view0`, `turn295view3`, `turn296view0`.

Theorem 1.1 covers \(\gamma\Delta^2-\beta\Delta\), \(\gamma>0\), \(\beta\ge0\). At \(\sigma=2/N\), it proves normalized minimizers at every mass above a threshold; Proposition 2.8 treats this endpoint. Thus \(m=2,k=4\), with nonlinearity power \(2\sigma=4/N\), is a direct predecessor. The paper's variational arguments use coercivity, negativity and strict subadditivity. Its discussion leaves attainment at the critical threshold unresolved. Sharp lower-order GN coercivity identifies the exact endpoint and excludes attainment there; this is a routine endpoint deduction, not a new stabilization mechanism.

**Tingjian Luo and Hichem Hajaiej**, *Normalized solutions for a class of scalar field equations involving mixed fractional Laplacians*, Advanced Nonlinear Studies **22** (2022), 228–247, DOI 10.1515/ans-2022-0013.

Primary: <https://doi.org/10.1515/ans-2022-0013>, <https://www.degruyterbrill.com/document/doi/10.1515/ans-2022-0013/html>. Retrieved ref: `turn297search0` (indexed publisher full text; direct open failed). Reproducible query: `"ans-2022-0013" "Theorem"`.

For \(0<s_1<s_2<1\), dimension \(d\ge1\), and nonlinearity \(|u|^pu\) with \(p=4s_1/d\), Theorem 1.1 and Remark 1.1 give zero infimum at \(c\le c_0=\|Q_{s_1}\|_2\) and negative infimum above it. Theorem 1.2(3) gives attainment if and only if \(c>c_0\). Theorem 1.3 gives the stationary equation with positive frequency. Remark 1.7 extends their conclusions to \(s_2=1\). With \(m=2s_1,k=2s_2\), this directly overlaps \(1<m<k\le2\); their parameter \(c\) is an L² norm. Arbitrary positive higher-order coefficient follows by mass-preserving spatial scaling. The sharp converse dichotomy is therefore already established in this fractional range.

**Haijun Luo and Zhitao Zhang**, *Existence and stability of normalized solutions to the mixed dispersion nonlinear Schrödinger equations*, Electronic Research Archive **30** (2022), 2871–2898, DOI 10.3934/era.2022146.

Primary: <https://www.aimspress.com/article/doi/10.3934/era.2022146>. Retrieved ref: `turn292view0`.

Their general-nonlinearity theorem for \(\gamma\Delta^2-\beta\Delta\) gives an orbital-stability/existence threshold for \(\beta\ge0\), under mass-subcritical assumptions relative to the fourth-order dispersion. This is useful broader context. For the sharp lower-critical converse, the preceding two references are more direct and should be preferred.

Thus the all-order converse should be presented as a general-order formulation and sharpness companion to the new exclusion theorem, with explicit credit for the known classical and fractional cases. It should not be advertised as discovering that positive higher-order dispersion creates normalized negative-energy standing waves.

## Same-order relative-smallness boundary

The stronger example supplied by the parent is

\[
b_\varepsilon(\xi)=\varepsilon|\xi|^m
\frac{|\xi|^q}{1+|\xi|^q},\qquad q>0.
\]

It satisfies \(0\le b_\varepsilon\le\varepsilon |\xi|^m\), but

\[
mb_\varepsilon-\xi\cdot\nabla b_\varepsilon
=-\varepsilon q\frac{|\xi|^{m+q}}{(1+|\xi|^q)^2}<0
\quad(\xi\ne0).
\]

The parent and independent reviewer obtain normalized negative-energy stationary minimizers for every
\(M\in(M_{c,m},(1+\varepsilon)^{N/m}M_{c,m})\): the low-frequency homogeneous threshold makes the infimum negative, while the larger high-frequency coefficient gives coercivity. Strict binding excludes dichotomy. Consequently mere smallness in the relative quadratic-form norm does not replace the Euler inequality, even when the differential order is unchanged. This does not contradict the earlier homogeneous angular-perturbation theorem, because this perturbation is not homogeneous.

A targeted search found no exact previously published instance of this rational-symbol example or this precise mass window. It did find substantial related normalized-minimizer theory, so the construction should be presented with its explicit calculation and existing variational ancestry, without an exhaustive novelty claim. In particular, Fernández–Jeanjean–Mandel–Mariș (arXiv:2010.01448v3), Proposition 3.1 and Theorem 3.4, analyze nonhomogeneous fourth-order dispersion with quadratic symbol \(|\xi|^4-2|\xi|^2\), including highest-order mass criticality; strict energy below the linear mass floor yields compact minimizing sequences and minimizers. Their symbol is different and is not a nonnegative small perturbation of \(|\xi|^m\). Primary PDF retrieved as `turn300view0`: <https://arxiv.org/pdf/2010.01448>.

The relevant contrast is therefore **Euler-sign control versus relative form smallness**, not simply lower order versus higher order. The rational-symbol construction is the more informative sharpness example for the clean manuscript; the mixed-power construction supplies transparent classical and fractional precedent.

## Bibliography recommendations for the clean manuscript

Retain the existing general-symbol, phase-rigidity and compactness predecessors, and add these entries where the corresponding comparison is actually used:

```tex
\bibitem{CW}
W. Chen and Z. Wang,
\emph{Normalized solutions to the biharmonic nonlinear Schr\"odinger equation with combined nonlinearities},
arXiv:2305.16565 (2023), Theorem 1.4.

\bibitem{BCMN}
D. Bonheure, J.-B. Casteras, E. Moreira dos Santos and R. Nascimento,
\emph{Orbitally stable standing waves of a mixed dispersion nonlinear Schr\"odinger equation},
SIAM J. Math. Anal. \textbf{50} (2018), 5027--5071,
doi:10.1137/17M1154138; arXiv:1710.09775.

\bibitem{LH}
T. Luo and H. Hajaiej,
\emph{Normalized solutions for a class of scalar field equations involving mixed fractional Laplacians},
Adv. Nonlinear Stud. \textbf{22} (2022), 228--247,
doi:10.1515/ans-2022-0013.

\bibitem{IKN}
T. Inui, K. Komada and K. Nishimura,
\emph{Scattering of non-radial solutions for the fourth-order Schr\"odinger equation with
$\dot H^{1/2}$-critical and supercritical nonlinearity},
arXiv:2610.05802 (2026), Theorem 1.1 and Remark 1.2.

\bibitem{FJMM}
A. J. Fern\'andez, L. Jeanjean, R. Mandel and M. Mari\c{s},
\emph{Non-homogeneous Gagliardo--Nirenberg inequalities in $\mathbb R^N$ and application to a biharmonic non-linear Schr\"odinger equation},
J. Differential Equations \textbf{330} (2022), 1--65,
arXiv:2010.01448, Proposition 3.8.
```

## Assessment suitable for the main manuscript

A defensible contribution claim, conditional on the completed proof, is:

> We establish a uniform strict exclusion interval above the homogeneous sharp mass threshold for negative-energy traveling profiles, robust under the stated nonnegative dispersion and defocusing nonlinear perturbations. This goes beyond the standard threshold coercivity and the stationary existence/nonexistence results compared here.

Do not infer from this audit that the result is the first in all literature. Do not call it a solution of the full nonradial finite-time blowup problem. Do not treat existence of positive-energy subthreshold travelers as a contradiction. No checked theorem provides the missing implication from arbitrary globally bounded dynamics to a finite family of traveling profiles.

The useful comparison with prior work is therefore structural: sharp critical compactness and established phase rigidity can support a new uniform exclusion theorem; the new statement must be distinguished from the standard tools used to prove it and from dynamical questions it does not yet close.
