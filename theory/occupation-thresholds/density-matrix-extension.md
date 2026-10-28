# Countably many occupations: extension of the near-rank-one inequality

Date: 2026-10-09. This note is conditional only on the finite-rank theorem
proved elsewhere in this research round, with one rank-independent constant
tau_0>0. It does not independently re-prove that finite-rank theorem.

## Precise statement

Assume that every finite orthonormal H^1 family (phi_j) satisfies

    integral (sum n_j |phi_j|^2)^2
       <= (2/M_c) n_1 sum n_j ||grad phi_j||_2^2

whenever n_1=max n_j>0 and sum_(j>=2) n_j <= tau_0 n_1.

Then the same inequality holds for every positive trace-class operator
gamma on L^2(R^2) with finite kinetic energy and

    Tr gamma - ||gamma||_op <= tau_0 ||gamma||_op.

In operator notation, the conclusion is

    integral rho_gamma^2
      <= (2/M_c) ||gamma||_op Tr(-Delta gamma).

No upper bound on the rank is required. All function spaces and constants
are those of R^2; this is not an assertion in arbitrary spatial dimensions.

## Proof by spectral truncation

The case gamma=0 is immediate. A nonzero positive trace-class operator
is compact, so alpha=||gamma||_op>0 is an attained eigenvalue. Order its
positive eigenvalues n_1=alpha>=n_2>=...>0, repeated with multiplicity,
and choose orthonormal eigenfunctions phi_j. Define kinetic energy by

    T(gamma)=Tr((−Delta)^(1/2) gamma (−Delta)^(1/2))
            =sum n_j ||grad phi_j||_2^2 < infinity.

The sum identity can be obtained by monotone bounded spectral
approximations of -Delta. It implies phi_j in H^1 for every n_j>0.

Put gamma_N=sum_(j<=N) n_j |phi_j><phi_j|. Then
||gamma_N||_op=alpha, and

    Tr gamma_N-alpha <= Tr gamma-alpha <= tau_0 alpha.

The finite-rank theorem therefore applies to every N. The nonnegative
densities rho_N=sum_(j<=N)n_j|phi_j|^2 increase almost everywhere to
rho_gamma. Their integrals increase to Tr gamma, which is finite, and
T(gamma_N) increases to T(gamma). Hence monotone convergence gives

    integral rho_gamma^2 =lim_N integral rho_N^2
       <=(2/M_c) alpha lim_N T(gamma_N).

This also proves rho_gamma belongs to L^2. There is no exchange of
uncontrolled nonlinear limits. QED.

## Sharpness for each prescribed countable spectrum

Let (n_j) be any summable nonnegative sequence with n_1=alpha>0 and
sum_(j>=2)n_j<=tau_0 alpha. The coefficient (2/M_c) alpha cannot be
decreased even if the complete spectrum is fixed.

For each epsilon>0 choose a normalized compactly supported smooth
first orbital phi_1 whose scalar GN quotient is within epsilon of 2/M_c.
This is possible by approximation of the normalized Townes state.
For all j>=2 choose normalized smooth functions phi_j supported on
mutually disjoint balls, all disjoint from supp phi_1. A dilation of any
fixed bump makes its gradient norm arbitrarily small, while translations
allow the corresponding balls to remain disjoint. Choose these dilations
so that

    sum_(j>=2) n_j ||grad phi_j||_2^2 < epsilon.

The functions are exactly orthonormal and the positive trace-class
operator they define has exactly the prescribed spectrum. The kinetic
energy tends to alpha ||grad phi_1||_2^2, and disjoint supports imply

    integral rho_gamma^2 >= alpha^2 integral |phi_1|^4.

Thus its density-to-kinetic quotient approaches alpha(2/M_c), after
letting epsilon tend to zero and improving the first-orbital approximation.
The already proved inequality gives the matching upper bound. This
argument establishes a supremum, not attainment by a mixed state.

## Consequence and precise limitation for dynamics

At the formal energy level for common-density cubic NLS,

    E(gamma)=1/2 T(gamma)-1/4 integral rho_gamma^2
       >=1/2 (1-alpha/M_c) T(gamma).

Therefore alpha<M_c yields a uniform kinetic bound for any solution for
which the occupation spectrum and energy are conserved. A theorem for
countably many time-dependent components additionally needs the
Hilbert-valued H^1 local well-posedness and conservation argument.
Those are separate analytic obligations; this static extension alone
should not be described as an infinite-rank blow-up theorem.

In particular, arbitrary trace-class occupation sequences do not even
admit an H^1 finite-variance realization. Let

    H_osc=-Delta+|x|^2

on R^2 and let its eigenvalues be e_j in nondecreasing order. Since
e_j is comparable to sqrt(j), the rearrangement/min--max principle gives

    sum_j n_j (||grad phi_j||_2^2+||x phi_j||_2^2)
       >=sum_j n_j e_j.

Thus simultaneous finite kinetic energy and finite variance requires
sum_j n_j sqrt(j)<infinity. Conversely this condition is sufficient for
some such realization, by choosing harmonic-oscillator eigenfunctions.
The assertion is about existence of a finite-variance realization;
constructing a negative-energy one with the same spectrum is a further
question. For the main report it is cleanest to retain the blow-up
construction at finite rank and present the countable-rank theorem as
the sharp kinetic inequality.

## Focused prior-art comparison

Search and primary-source checks on 2026-10-09 did not locate a theorem
asserting the exact near-pure plateau above in d=2 at the kinetic
exponent 2. This is a search result, not a proof of novelty. The strongest
relevant overlaps found were:

1. Dolbeault, Felmer, Loss, Paturel, *Lieb--Thirring type inequalities
   and Gagliardo--Nirenberg inequalities for systems*, JFA 238 (2006),
   193--220, DOI 10.1016/j.jfa.2005.11.008.
   https://www.sciencedirect.com/science/article/pii/S0022123605004179
   Occupation-number inequalities, mixed states, and the LT/GN connection
   are explicitly present there. These ideas cannot be claimed as new.
   The retrieved primary abstract does not assert an exact rank-one
   constant for trace/operator-norm ratio just above one.

2. Carlen, Frank, Lieb, *Stability estimates for the lowest eigenvalue
   of a Schrodinger operator*, GAFA 24 (2014), 63--84.
   https://arxiv.org/pdf/1301.5032
   Theorems 2.2 and 2.6 give quantitative stability for the scalar
   optimal-potential and GN problems. These are directly relevant
   ingredients. They concern the lowest eigenvalue/scalar optimizer,
   not the displayed fixed-occupation density-matrix theorem.

3. Gontier, Lewin, Nazar, *The nonlinear Schrodinger equation for
   orthonormal functions: I. Existence of ground states*, ARMA 240
   (2021), 1203--1254.
   https://arxiv.org/pdf/2002.04963
   The paper develops mixed-occupation variational problems, including
   noninteger particle number and states with one partially filled
   orbital. Its standing regime is 1<p<1+2/d (PDF p.3), excluding our
   d=2,p=2 endpoint. Its binding conjecture and theorems additionally
   use p<2. Proposition 16 concerns this strictly subcritical regime.

4. Frank, Gontier, Lewin, *The nonlinear Schrodinger equation for
   orthonormal functions II: Application to Lieb--Thirring inequalities*,
   CMP 384 (2021), 1783--1828.
   https://link.springer.com/article/10.1007/s00220-021-04039-5
   Theorem 2 proves strict failure of one-bound-state optimality for
   kappa>max(0,2-d/2), hence kappa>1 in d=2. The kinetic endpoint is
   included in the general variational formalism and duality, but the
   strict-improvement theorem does not cover d=2,kappa=1. No exact
   near-rank-one occupation plateau was found in the full text.

5. Frank, Gontier, Lewin, *Optimizers for the finite-rank Lieb--Thirring
   inequality*, AJM 147 (2025) (arXiv full text used here).
   https://arxiv.org/html/2109.05984v2
   This concerns unweighted sums of the first N eigenvalues, existence
   of optimizing potentials, compactness, and binding for stated
   exponent ranges. It does not state the trace/operator-norm condition
   above. Its concentration-compactness and threshold spectral methods
   are relevant predecessors, not identical conclusions.

The finite-rank proof and spectral certificate give a sharp
near-rank-one fixed-occupation theorem at a specific two-dimensional
critical endpoint, with rank-independent scope. It is not a solution
of the full unweighted rank-two Lieb--Thirring conjecture, and neither
the LT/GN duality nor the use of occupation numbers is newly introduced.
