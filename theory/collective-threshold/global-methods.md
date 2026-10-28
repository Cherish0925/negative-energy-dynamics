# global structure at the two-dimensional Lieb–Thirring endpoint

Date: 2026-10-12. This note records exact deductions and the points at which the attempted global arguments stop. It does not resolve the endpoint conjecture or claim priority for the deductions.

## 1. Normalization and primary-source status

For a finite orthonormal family of scalar functions on R², set

    P = sum_j |phi_j><phi_j|,
    rho = sum_j |phi_j|²,
    T = sum_j integral |gradient phi_j|²,
    F = integral rho².

Let C_N be the supremum of F/T over projections of rank at most N. The scalar sharp constant is C_1 = 2/M_c, where -Delta Q + Q - Q³ = 0 and M_c = integral Q². The full endpoint asks whether C_N = C_1 for every finite N. The dual spectral normalization is L_{1,2}^{(N)} = C_N/4.

The following sources were directly inspected:

* Frank–Gontier–Lewin, *The nonlinear Schrödinger equation for orthonormal functions II. Application to Lieb–Thirring inequalities*, arXiv:2002.04964v3, https://arxiv.org/html/2002.04964v3 . Its strict improvement over the one-state constant in dimension two requires gamma > 1. Its finite-rank optimizer theorem includes the gamma = 1 problem and gives a real self-consistent occupied eigenbasis. It does not prove the endpoint.
* Read–Schulz, *The sharp one-dimensional Lieb–Thirring inequality for the sum of eigenvalues*, arXiv:2609.10478v2, September 14, 2026, https://arxiv.org/html/2609.10478v2 . Theorem 1 states the sharp one-dimensional result; Theorem 2 states L_{1,d} <= (2/sqrt(3)) L_{1,d}^{cl}. In dimension two this is L_{1,2} <= 1/(4 sqrt(3) pi), or C <= 1/(sqrt(3) pi). This note has inspected the theorem statements and mechanism, not independently verified that preprint's entire proof.
* Carvalho Corso–Ried, *On a Variational Problem Related to the Cwikel–Lieb–Rozenblum and Lieb–Thirring Inequalities*, CMP 406 (2025), article 50, https://doi.org/10.1007/s00220-024-05216-y . Corollary 1.7 gives the earlier 1.44655 ratio in the one-dimensional physical case; dimension lifting gives a dimension-independent upper ratio. This optimizes an auxiliary method, not the conjectural sharp constant.

Numerically, using M_c approximately 11.7008965 only for illustration,

    1/(4 sqrt(3) pi) = 0.04594407462,
    1/(2 M_c)       = 0.04273176846.

The stated 2026 upper bound is therefore about 7.52% above the one-state target in d = 2. It does not close our endpoint. No inspected newer primary source supplies that closure. This is not an exhaustive assertion about every possible recent manuscript.

## 2. Random deletion inside the occupied space

Here is a global necessary condition on a smallest-rank counterexample. No spatial symmetry or closeness to Q is imposed.

Suppose N is the smallest rank with C_N > C_1. The finite-rank optimizer theorem supplies an optimizer of rank exactly N, and its orbitals can be chosen real because its self-consistent potential is real. Write Phi(x) = (phi_1(x),...,phi_N(x)). For a uniformly random unit vector a in the real sphere S^{N-1}, define

    u_a(x) = a dot Phi(x),
    P_a = P - |u_a><u_a|.

Then P_a is a rank-(N-1) orthogonal projection. Spherical moments give

    E |u_a|² = rho/N,
    E |u_a|⁴ = 3 rho²/[N(N+2)],
    E T(P_a) = (N-1) T/N.

Consequently

    E F(P_a) = (N²-1) F/[N(N+2)].

Minimality of N says F(P_a) <= C_1 T(P_a) for every a. Averaging gives

    C_N = F/T <= [(N+2)/(N+1)] C_1.                 (2.1)

Equivalently, if g = 2/C_N is the common modal mass of the rescaled stationary optimizer, then

    M_c (N+1)/(N+2) <= g < M_c.                    (2.2)

Thus a first failure at very large rank would have a very small relative improvement over the scalar constant:

    C_N/C_1 - 1 <= 1/(N+1).

This is not an upper bound on the unknown first violating rank. Arbitrarily small violations remain compatible with arbitrarily large N. Nor does g close to M_c imply that each orbital is close to a Townes profile: no individual scalar GN deficit has been shown small.

More generally, a uniformly random real k-dimensional subspace of the occupied space gives

    E rho_k² = k(k+2) rho²/[N(N+2)],
    E T_k = kT/N,

and hence C_N <= [(N+2)/(k+2)] C_k whenever the argument is applied to a real N-rank optimizing family. For a complex spherical average the analogous factor is (N+1)/(k+1); the real basis is why (2.1) is slightly stronger.

## 3. Full external-mode second variation

Let the optimizing real orthonormal orbitals solve

    H phi_j = -e_j phi_j,
    H = -Delta - V,
    V = g rho,
    g = 2/C_N,
    e_j > 0.

The mass-preserving spatial Pohozaev identity and the summed eigenvalue identities give

    T = (g/2)F = sum_j e_j =: S.                   (3.1)

The functional J(P) = T(P) - (g/2) F(P) is nonnegative on all rank-at-most-N projections and vanishes at this optimizer.

Choose a real normalized f perpendicular to all occupied orbitals and replace phi_j by cos(t) phi_j + sin(t) f, keeping the other orbitals fixed. This remains an orthonormal family. Direct expansion of J yields

    J(P_t) = t² [ <f,Hf> + e_j
                       - 2g integral phi_j² f² ] + O(t³).

Therefore every occupied-to-unoccupied variation obeys

    <f,Hf> + e_j >= 2g integral phi_j² f².         (3.2)

In fact one may rotate any normalized u_a = a dot Phi out of the occupied space. The resulting stronger matrix statement is

    E + <f,Hf> I_N - 2g integral f² Phi Phi^T >= 0,
    E = diag(e_1,...,e_N).                          (3.3)

Taking the trace gives

    <f, [-Delta - (1+2/N)V + S/N] f> >= 0
                       for every f perpendicular to Ran(P).

By the min–max principle,

    lambda_{N+1}(-Delta-(1+2/N)V) >= -S/N.         (3.4)

Missing discrete eigenvalues are interpreted through the min–max levels, so the essential-spectrum threshold 0 causes no ambiguity. This is a necessary condition for a genuine optimizing stationary state; an arbitrary stationary solution need not satisfy it.

For N = 1 and the Townes optimizer, V = Q², e_1 = 1. The translations satisfy

    (-Delta-3Q²) partial_k Q = -partial_k Q.

The known scalar second variation gives lambda_2(-Delta-3Q²) = -1. Thus the coefficient 1+2/N and the shift S/N in (3.4) have the expected sharp one-state normalization. This is not evidence that the same relation is contradictory at N > 1.

## 4. What commutator estimates add, and what remains missing

The standard coordinate-commutator/Yang inequality in d = 2, applied to H and a level mu between its Nth and (N+1)st levels, has the form

    sum_j (mu+e_j)² <= 2 sum_j (mu+e_j) T_j,
    T_j = integral |gradient phi_j|².

At mu = lambda_{N+1}(H) <= 0, including mu = 0 when there is no next bound state, equation (3.1) cancels the linear terms and gives

    N mu² + sum_j e_j² <= 2 sum_j e_j T_j.         (4.1)

This contains an uncontrolled frequency–kinetic correlation, sum e_j T_j. Stationarity gives sum T_j = sum e_j, not T_j = e_j for each component. Replacing the individual T_j by e_j would be an unjustified scalar-to-vector inference. In addition, (4.1) concerns H, whereas (3.4) concerns the more attractive potential (1+2/N)V. It does not provide the opposite bound needed to contradict (3.4).

There is also an exact first-order trace comparison for K = -Delta-(1+2/N)V. The occupied space is an admissible trial space, and

    -Tr(PK) = S + (2/N) integral V rho = S(1+4/N).

Hence the sum of the magnitudes of the first N negative levels of K is at least S(1+4/N). However,

    integral [(1+2/N)V]² = (1+4/N+4/N²) integral V².

The guaranteed spectral quotient is the old one multiplied by

    (1+4/N)/(1+4/N+4/N²) < 1.                     (4.2)

Thus simply amplifying the potential does not turn an optimizer into a better counterexample. Any successful use of (3.4) requires genuinely additional spectral information beyond these trace and coordinate-commutator identities.

## 5. Ground-state transformation: exact content and its limit

Choose the first stationary mode psi_1 = w > 0 after rescaling psi_j = sqrt(g) phi_j, and put f_j = psi_j/w. The common-density stationary equations give

    -div(w² gradient f_j) = (e_1-e_j) w² f_j,
    integral w² f_i f_j = g delta_ij.              (5.1)

The ground-state representation also gives

    integral w² |gradient f_j|² = g(e_1-e_j).      (5.2)

This exposes orthogonality as a weighted spectral problem rather than an arbitrary cancellation of phases. It does not produce a universal sharp lower bound on the weighted gap: the weight w² is unknown and may have widely separated concentration regions. Families of separated scalar profiles make such weighted gaps small. A proof that silently substitutes the Townes spectral gap would reintroduce the small-perturbation assumption the global problem must avoid.

An elementary use of the scalar Keller bound on each nodal domain of a real stationary psi_j yields only

    g >= M_c n_j e_j/(sum_i e_i),                  (5.3)

where n_j is its number of nodal domains. To see this, each nodal restriction is a Dirichlet eigenfunction with eigenvalue -e_j in potential V, and the scalar bound gives e_j <= (1/(2M_c)) integral_{domain} V². Summing over its disjoint nodal domains and using integral V² = 2g sum_i e_i gives (5.3). There is no established inequality max_j n_j e_j >= sum_i e_i, so this does not give g >= M_c.

Dirichlet cutting of space also has the wrong direct bracketing direction for an upper bound on the original negative spectral sum: it raises eigenvalues and decreases that sum. Neumann cutting reverses the comparison but admits constant modes, so the same scalar whole-space sharp bound is unavailable without boundary terms. These are concrete points of failure, not a proof that all partition methods must fail.

## 6. Conformal and cumulative-mass mechanisms

The special feature in the 2026 one-dimensional proof is a matrix cumulative mass A(x) with 0 <= A <= I and A'(x) = U(x)U(x)^T. The rank-one derivative closes products of matrix moments. In two dimensions the rectangular cumulative matrix satisfies a mixed derivative identity, A_xy = U U^T, whereas A_x and A_y involve integrals along different slices. The one-dimensional first-derivative closure is therefore absent. Treating A_x or A_y as U U^T is incorrect.

Two-dimensional conformal invariance of the unweighted Dirichlet integral does not remove this problem. A conformal change preserves that integral for an unchanged scalar function, but transforms its L² Gram matrix and quartic density integral by spatially varying Jacobian weights. Rescaling the orbitals to preserve their Gram matrix introduces derivatives of that Jacobian into the energy. A general flattening transport has additional anisotropic metric terms. No sign or sharp cancellation for those terms has been obtained here.

## 7. Research consequence

The global target remains the exclusion or construction of a compact, equal-occupation optimizing state with g < M_c. The material above adds two exact requirements to such a state: the minimal-rank mass window (2.2) and external-mode stability (3.3)–(3.4). The latter can reject stationary numerical candidates that solve the Euler equations but are saddles of the full projection problem. Neither requirement is sufficient to solve the endpoint. The missing step is a global relation between the self-consistent density, occupied spectrum, and unoccupied modes that is stronger than the trace and commutator identities above.

## 8. Historical comparison for numerical splitting

Antoine Levitt, *Best constants in Lieb–Thirring inequalities: a numerical investigation*, Journal of Spectral Theory 4 (2014), 153–175, DOI 10.4171/JST/65, primary PDF https://ems.press/content/serial-article-files/33509 , already reports two-dimensional splitting in Section 4.2, pp. 167–169. Figure 4 shows separating peaks at gamma = 1.2. Figure 6 shows an eight-bound-state radial potential splitting into eight peaks after a nonradial perturbation at gamma = 1.1. The computed radial branches in Figure 5 lie below the one-state value below approximately gamma = 1.16; the stated explored interval includes gamma = 1.

Accordingly, observing splitting into rank-one peaks in the present gamma = 1 orbital optimization is a reproduction of an already documented type of numerical behavior, not a newly discovered mechanism. Levitt's displayed nonradial examples use gamma = 1.1 and 1.2, so this comparison should not be misreported as an identical published gamma = 1 experiment. Numerical splitting is also not proof of global optimality: FGL later established strict improvement for gamma > 1, including parameter values where finite numerical searches had missed the improvement.
