# Round 10 focused derivation: opposite-velocity negative-energy multiwaves

## 1. This construction is already in the project record

The manuscript [BNLS-Zero-Momentum-and-Three-Dimensions-20261007.tex](../../manuscripts/biharmonic-certificates/BNLS-Zero-Momentum-and-Three-Dimensions-20261007.tex), Theorem `thm:pair` and its sections on compact finite-rank metrics and moving-center gluing, already states the desired result. Its detailed derivation is in [gluing-general.md](../zero-momentum/gluing-general.md), with existing proof details alongside it.

The stated construction uses the validated four-dimensional cubic BNLS profiles Q_{±v}, at any fixed admissible sufficiently small nonzero v, to produce an inversion-even forward-global solution asymptotic in high Sobolev and weighted norms to

R(t)=exp(it)[Q_v(. - vt e1)+Q_{-v}(. + vt e1)].

Its conserved quantities are P=0, E=2E(Q_v)<0, M=2M(Q_v), with bounded forward Sobolev norms and finite variance at finite times. This is a high-mass example: each negative-energy component is already above the single-profile mass gap. It neither resolves nor contradicts the near-Mc zero-momentum question currently under study.

## 2. Why the naive final-value contraction is insufficient

If one merely bounds the full two-wave linearized propagator by C exp(K|t-s|), while the overlap defect decays like exp(-kappa t) with kappa proportional to |v|, then a backward integral from infinity requires a decay exponent gamma satisfying K<gamma<kappa. Small v need not permit this. Taking a larger initial separation only reduces the defect amplitude; it does not change the rate inequality.

This is a failure of that crude inversion, not a proof that a multiwave cannot exist. Stable and unstable modes must be treated in opposite time directions. The existing project proof does this and controls the remaining center with an arbitrarily small exponential growth rate.

## 3. Focused check of the existing finite-rank metric argument

I checked the project proof against Lin--Zeng's actual Theorem 2.1 and Theorem 2.2 in arXiv:1703.04016, rather than inferring its hypotheses from the abstract. The theorem explicitly supplies all points crucial here:

- the triangular center arrows used in the manuscript;
- bounded off-diagonal maps, including those out of the infinite-dimensional block;
- finite-dimensional blocks contained in every generator graph domain;
- a positive-energy infinite block whose generator is skew for that energy;
- the specified Hessian pairings and center/kernel orthogonality;
- finite-dimensional hyperbolic spaces and polynomial center growth.

Thus no missing smoothness or bounded-coupling assumption was found in this source comparison. For the cubic BNLS traveling linearization, positivity of |xi|^4+1-v xi1 at small v, compactness of the decaying potential, and elliptic regularity supply the required energy-space setting.

The positive metric construction is algebraically sound: leave the infinite positive block unchanged, rescale the finitely many Jordan blocks, then weight the triangular source/target blocks so every off-diagonal coupling has an arbitrarily small norm. Only finitely many coordinates are altered, so the correction is finite rank. The smooth dual coordinates identified through the Hessian pairings permit compact spatial cutoffs with small error in both the form and its generator derivative. This is stronger than merely knowing an abstract polynomial semigroup bound; the localizable form is what can be transported to two moving centers.

The moving-center calculation also passes the focused algebra check. With WZ=I and Wdot+W A=B0 W+E_W, the corrected center generator C=A-Z E_W obeys Wdot+W C=B0 W, so the constraint Ww=0 is preserved. The localized velocity field and compact metric corrections yield a positive energy Q_t with

|Q_t'(w)| <= [2 epsilon+C_epsilon/t+C_epsilon exp(-kappa t)] Q_t(w).

The fourth-order commutator has the energy-form order needed for the H2 bound. The use of the comparison q_+(chi_+ w)+q_-(chi_- w)<=2Q_t(w) keeps a metric condition number from contaminating the tunable epsilon term. This is the essential point permitting epsilon below an arbitrarily small fixed interaction rate.

One then chooses gamma<min(kappa,alpha), where alpha is a hyperbolic spectral gap when hyperbolic directions exist, and epsilon<gamma/2. Center and unstable components are integrated from infinity, stable components forward. Large T makes the remaining coupling and nonlinear terms contractive. A topological shooting argument is not logically required once this bounded Green inverse is actually established.

## 4. Primary-source comparison

1. Lin and Zeng, *Instability, index theorem, and exponential trichotomy for linear Hamiltonian PDEs*, Memoirs AMS 275 (2022), no. 1347. Primary full text checked:
   https://arxiv.org/pdf/1703.04016
   Theorem 2.1 (printed pp. 19--20) and Theorem 2.2 (pp. 21--22).
2. Cote and Le Coz, *High speed excited multi-solitons in nonlinear Schrodinger equations*, J. Math. Pures Appl. 96 (2011), 135--166:
   https://arxiv.org/abs/1007.3034
   This is a second-order NLS result with a high relative-speed hypothesis, not a direct fourth-order small-speed theorem.
3. Le Coz and Tsai's authors' survey gives the distinction explicitly: ground-state multi-solitons can admit arbitrary distinct speeds in the stated setting, while general excited states require a positive speed threshold in the surveyed theorem. It describes the finite-dimensional bad directions and topological versus high-speed arguments:
   https://arxiv.org/html/1409.8379v2
   Section 3.2, Theorem 1 and its following explanation.
4. Parker and Aceves, *Multi-pulse solitary waves in a fourth-order nonlinear Schrodinger equation*:
   https://arxiv.org/abs/2009.01647
   These are fixed multi-pulse solitary profiles, not asymptotically separating opposite-velocity solutions. They cannot be used as a substitute for the present gluing argument.

Targeted searches did not identify an existing published theorem directly covering the exact four-dimensional excited small-speed construction. This limited search is not a priority proof.

## 5. Consequence for the current research target

Do not say that zero momentum, finite variance, and negative energy at arbitrary mass still imply collapse or rule out bounded forward-global solutions; the project already has a claimed construction showing otherwise. The unsolved target remains a uniform near-critical mass window. Any new dynamic rigidity theorem must quantitatively use that window, or some additional compactness/radiation condition, and remain compatible with the older separating two-wave example.
