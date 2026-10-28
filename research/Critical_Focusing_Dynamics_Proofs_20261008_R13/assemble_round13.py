from pathlib import Path

root = Path(__file__).resolve().parent
foundation = (root / 'round10_foundations_section.tex').read_text()
foundation = foundation[:foundation.index(r'\begin{lemma}[Weak-profile regularity')]
foundation = foundation.replace(r'\section{Analytic foundations and conventions}',
                                r'\section{Scalar compactness and critical normalization}')
(root / 'round13_scalar_foundation.tex').write_text(foundation)

phase = (root / 'round12_polarization_foundation.tex').read_text()
phase = phase.replace('A scalar optimizer placed\nin one component proves sharpness.',
                      'A scalar maximizing sequence\nin one component proves sharpness.')
phase += r'''
\subsection{The real version and scalar constant phase}
\label{subsec:r13-real-phase}
All preceding density inequalities, compactness, and quantitative
polarization statements hold over a separable real internal Hilbert
space, with orthogonal maps replacing unitaries and real scalar $q$
in the definition of $\mathfrak p$. Here are the points that matter
for the scalar evolution theorem. The real scalar sharp constant
equals the complex one: apply the density triangle inequality and
sequence H\"older to $(\operatorname{Re}u,\operatorname{Im}u)$,
starting with the real scalar constant, while the reverse comparison
is immediate. Equality forces a constant real internal direction
by the pair-rotation argument above. The internal compactness proof
uses real Gram--Schmidt without any other change. Finally rotate
$\int QU_n$ into the first real direction. Every transverse real
component is orthogonal to $Q$, so exactly the displayed $L_Q$
coercivity and transverse expansion apply. This proves the real
quantitative assertion, not just its complex analogue.

In particular, for a scalar complex $u$ and either allowed interaction,
there exists a phase $\theta$ such that $u=e^{i\theta}(X+iY)$,
with $X,Y$ real, and
\[
 \frac{M(Y)}{M(u)}+\frac{A(Y)}{A(u)}\le C\mathfrak d(u).
\]
This holds for every local exponent $r>0$, and for the strictly
positive-definite Hartree density form. For negative energy and
$d=(M/M_c)^{\kappa-1}-1>0$, one has
$0\le\mathfrak d(u)<d/(1+d)$, providing exactly the input used
in Theorem~\ref{thm:r13-general-average}. No phase is differentiated
in time. In the local range $r\ge1$,
Theorem~\ref{thm:r13-explicitpolarization} gives an explicit constant
in place of this compactness argument.
'''
(root / 'round13_polarization_foundation.tex').write_text(phase)

old = (root / 'round13_virial_closure_section.tex').read_text()
obstruction = old[old.index(r'\subsection{The instantaneous translation'):]
obstruction = obstruction[:obstruction.index('The proof of Theorem')]
obstruction = obstruction.replace(r'\subsection{The instantaneous translation term cannot be removed by momentum alone}',
    r'\section{Zero momentum and instantaneous quartic transport}')
obstruction += r'''
The improved center in Section~\ref{sec:r13-center} is a modulation
coordinate chosen by dual orthogonality, not the ordinary first-moment
center. Its quadratic drift is therefore consistent with the example.
The example rules out the proposed instantaneous current improvement;
it does not rule out further cancellation along the nonlinear evolution.
'''
(root / 'round13_current_obstruction.tex').write_text(obstruction)

main = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=23mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,microtype,amsmath,amssymb,amsthm,mathtools,enumitem,xcolor,booktabs}
\usepackage[colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\setlength{\parskip}{3pt}
\setlist{nosep}
\allowdisplaybreaks[1]
\title{Thresholds, coherent structures, and dynamics\\of critical focusing dispersive systems\\[5pt]
\large Persistent kinetic amplification, conserved occupations,\\and momentum-adapted motion}
\author{Research manuscript, version 13}
\date{8 October 2026}
\begin{document}
\maketitle
\begin{abstract}
We connect sharp critical concentration geometry to nonlinear evolution
through three results. For real-even positive elliptic homogeneous
dispersion of order $m>2$, global zero-momentum negative-energy
solutions near critical mass satisfy a lower physical-time mean kinetic
bound $\liminf_{T\to\infty}T^{-1}\int_0^T A(t)\,dt
\ge c|E|d^{-1-m/[2(m-1)]}$. The result covers critical local powers
and a class of strictly positive-definite homogeneous Hartree
interactions, without radiality, a spatial moment, a global kinetic
bound, or symbol convexity. Fourier factorization preserves an exterior
negative kinetic term, while intrinsic-time center construction and
weak energy splitting control the small mass tail.
For local multicomponent systems, Gaussian projection of the scalar
sharp inequality gives an explicit coefficient depending on the entire
conserved occupation spectrum. This yields all-time energy bounds for
specified above-critical masses, including $M<\sqrt2M_c$ for two equal
orthogonal occupations in the two-dimensional quartic system, and an
exact scalar reduction for every unbounded critical-mass evolution.
Finally, near a quartic ground wave with nondegenerate real linearization,
momentum-adapted modulation improves the mean bound to
$c_Q|E|d^{-7/3}$ at zero momentum and to $c_Q|E|d^{-2}$ at arbitrary
momentum. Complete supporting proofs and the remaining dynamical
obstruction are included.
\end{abstract}

\noindent\textbf{Status and scope.}
This manuscript contains analytic derivations with independent internal
review; it has not undergone external peer review or formal verification.
Originality priority and optimality of the exponents or higher-rank
coefficients are not established. The stronger modulation results
retain the explicit assumption $\ker L_+=\operatorname{span}\{\partial_jQ\}$.
The general mean-bound theorem states its conservative strong solution
class; a concrete local-flow proof is supplied for local powers of
order $m=2k\ge4$ in dimensions one through three. None of the results
proves that all nonradial negative-energy solutions blow up in finite time.

\section*{The mathematical connection}
The main question is how critical threshold geometry restricts a
time-dependent solution. Write $M=\|u\|_2^2$ and
$A=\|a(D)^{1/2}u\|_2^2$. Sharp interpolation at critical mass $M_c$
gives only $A(t)\ge2|E|/d$ when $E<0$. We show that nonlinear evolution
forces a substantially higher \emph{long-time average}. The mass surplus
leaves at most $O(d)$ mass outside a persistent core. Quantitative phase
control bounds the motion of that core, and the favorable exterior
kinetic contribution absorbs the tail current. This produces
\[
 \liminf_{T\to\infty}\frac1T\int_0^T A(t)\,dt
 \ge c|E|d^{-\alpha_m},\qquad
 \alpha_m=1+\frac{m}{2(m-1)}.
\]
For amplitude perturbations $u_d(0)=(1+d)^{1/[2(\kappa-1)]}Q$,
where $M(Q)=M_c$ and $\kappa=1+m/N$ locally or $\kappa=2$ for
Hartree, this forces mean amplification at least
$cd^{-m/[2(m-1)]}$. Every prescribed finite factor is crossed at
arbitrarily late times by a global solution for sufficiently small $d$.

The multicomponent result uses the same threshold geometry in a
different dynamical direction. The internal correlation operator
$\Gamma=\int|U(x)\rangle\langle U(x)|\,dx$ is conserved.
An explicit occupation-sensitive sharp-scalar inequality turns that
conservation law into a uniform bound for all times. It also makes
the assertion of scalar behavior at threshold exact for the entire
evolution, not just for a concentrating subsequence.

For a nondegenerate quartic ground component, the inverse phase
operator defines dual translation coordinates in which conserved
momentum determines the leading drift. At zero momentum the drift
becomes quadratic in the perturbation, improving the exponent. At
nonzero momentum the signed main term in moving virial is favorable,
so a weaker improvement survives without imposing $P=0$.

\paragraph{Reading guide.}
Section~\ref{sec:r13-occupations} gives explicit conserved-spectrum
bounds. Section~\ref{sec:r13-dispersion-structure} establishes the
Fourier and interaction estimates and the concrete local flow.
Section~\ref{sec:r13-persistent-general} proves the general mean
bound, and Section~\ref{sec:r13-center} proves the conditional
momentum refinement. The appendices supply scalar compactness,
phase coercivity, quantitative polarization, and an exact obstruction
to a stronger instantaneous current bound.

\input{round13_invariant_threshold_section.tex}
\input{round13_dispersion_structure_section.tex}
\input{round13_persistent_general_section.tex}
\input{round13_center_momentum_section.tex}

\section{Relation to existing work and the remaining evolution problem}
For the pure quartic equation, Boulenger--Lenzmann~\cite{BL} prove
radial negative-energy finite- or infinite-time blowup, and
Bonheure--Cast\'eras--Gou--Jeanjean~\cite{BCGJ} deduce ground-wave
instability under their stated radial hypotheses. The recent
Dinh--Muse manuscript~\cite{DM}, Theorem 1.1 and Remark 1.4, states
radial finite-time blowup and leaves the unrestricted nonradial
question open. Instability in the full perturbation space is already
implied by instability using radial perturbations of the same wave.
Thus orbital instability alone should not be presented as resolving
the nonradial blowup problem. The distinctive conclusion studied here
is a quantitative physical-time average for general near-threshold
trajectories, with the precise momentum and spectral assumptions
stated in each theorem.

Pausader--Shao~\cite{PS}, Section 6, already relate center motion,
momentum, and energy for fixed-scale precompact quartic trajectories
with the additional regularity in their proposition. Their rigidity
argument rules out the corresponding negative-energy zero-momentum
compact trajectory. Our tail argument permits small mass radiation
and does not assume kinetic compactness. The remaining moving-tail
term is exactly what prevents the present theorem from giving full
compact-trajectory rigidity for every bounded solution.

Inui--Komada--Nishimura~\cite{IKN} prove nonradial subground scattering
in a range starting at nonlinearity power $1+8/(N-1)$, using a
virial transverse to momentum. The mass-critical power $1+8/N$ is
outside that range: its transverse scaling exponent is below four.
Their argument therefore does not directly settle the critical
problem addressed here.

Occupation-sensitive interpolation has a substantial history,
including Dolbeault--Felmer--Loss--Paturel~\cite{DFLP}. Hong--Kwon--Yoon
\cite{HKY} give fractional operator kinetic estimates and conservation
of pairwise component inner products. We do not claim either idea as
new. The Gaussian coefficient $\mathcal B_r$ above is an explicit
refinement retaining the scalar endpoint and the full occupation
spectrum; its optimality at fixed higher rank is not asserted.
Indeed, for $k$ equal occupations the Gaussian ratio tends to
$1/\mathrm G(r+2)$ as $k\to\infty$, whereas operator-norm kinetic
inequalities can yield mass intervals growing with rank. Neither
bound uniformly replaces the other for every purpose.

Frank--Gontier--Lewin~\cite{FGL} prove strict finite-rank binding for
the ordinary second-order kinetic problem in their specified range.
For eigenvalue moment one and dimension at least three, rank two
strictly improves on the rank-one spectral constant. Consequently
one cannot simply replace total mass by largest occupation while
retaining the scalar optimal kinetic constant. This is an established
obstruction from their work; we neither solve a Lieb--Thirring
conjecture nor transfer that strict-binding theorem to quartic
dispersion without proof.

\paragraph{What remains mathematically open in this manuscript.}
The mean bounds permit bounded global motion at a sufficiently large
kinetic level. They also permit sparse high peaks when no kinetic
upper bound is assumed. Applying the same estimate at a later time
does not amplify it again, because $d$ and $E$ are conserved.
To exclude every bounded negative-energy trajectory one needs a new
long-time statement controlling scale evolution or the accumulated
motion of the small mass tail. Only after that step could one
separate finite-time collapse from infinite-time growth. The
modulation identities locate these terms explicitly; they do not
remove them. Independently, proving real-sector nondegeneracy in
the full ground-wave class would remove the remaining hypothesis
from the stronger center theorem. Determining the optimal
fixed-occupation constant is another substantive variational problem.

\appendix
\input{round13_scalar_foundation.tex}
\input{round13_polarization_foundation.tex}
\input{round13_current_obstruction.tex}

\clearpage
\begin{thebibliography}{9}
\raggedright
\bibitem{BL} T. Boulenger and E. Lenzmann,
\emph{Blowup for biharmonic NLS}, Ann. Sci. ENS 50 (2017).
\href{https://arxiv.org/abs/1503.01741}{arXiv:1503.01741}.
\bibitem{BCGJ} D. Bonheure, J.-B. Cast\'eras, T. Gou and L. Jeanjean,
\emph{Strong instability of ground states to a fourth order Schr\"odinger equation},
IMRN 2019, 5299--5315.
\href{https://arxiv.org/abs/1703.07977}{arXiv:1703.07977}.
\bibitem{DM} L. Dinh, with Muse Spark,
\emph{Finite-Time Blow-Up of Radial Negative-Energy Solutions for the
Mass-Critical Biharmonic Nonlinear Schr\"odinger Equation}, manuscript,
2 October 2026.
\href{https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/}{Official manuscript and PDF}.
\bibitem{PS} B. Pausader and S. Shao,
\emph{The mass-critical fourth-order Schr\"odinger equation in high dimensions},
J. Hyperbolic Differ. Equ. 7 (2010), 651--705.
\href{https://arxiv.org/abs/0906.1547}{arXiv:0906.1547}.
\bibitem{IKN} T. Inui, K. Komada and K. Nishimura,
\emph{Scattering of non-radial solutions for the fourth-order
Schr\"odinger equation with $\dot H^{1/2}$-critical and supercritical nonlinearity},
2026 preprint.
\href{https://arxiv.org/abs/2610.05802}{arXiv:2610.05802v1}.
\bibitem{DFLP} J. Dolbeault, P. Felmer, M. Loss and E. Paturel,
\emph{Lieb--Thirring type inequalities and Gagliardo--Nirenberg
inequalities for systems}, J. Funct. Anal. 238 (2006), 193--220.
\href{https://arxiv.org/abs/math-ph/0506052}{arXiv:math-ph/0506052}.
\bibitem{HKY} Y. Hong, S. Kwon and H. Yoon,
\emph{Global existence versus finite time blowup dichotomy for the system
of nonlinear Schr\"odinger equations}.
\href{https://arxiv.org/abs/1712.06811}{arXiv:1712.06811}.
\bibitem{FGL} R. L. Frank, D. Gontier and M. Lewin,
\emph{The Nonlinear Schr\"odinger Equation for Orthonormal Functions II:
Application to Lieb--Thirring Inequalities},
Commun. Math. Phys. 384 (2021), 1783--1828.
\href{https://arxiv.org/abs/2002.04964}{arXiv:2002.04964}.
\end{thebibliography}
\end{document}
'''
(root / 'Critical_Focusing_Dynamics_20261008_R13.tex').write_text(main)
print('Assembled R13 manuscript and three supporting appendices.')
