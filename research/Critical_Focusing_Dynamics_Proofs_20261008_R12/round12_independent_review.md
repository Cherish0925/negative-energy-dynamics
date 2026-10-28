# Round 12 independent mathematical review

This is an internal derivation review of the new results, not external peer review or a determination of priority. Statements are reviewed with their hypotheses, rather than by extending their conclusions to every dispersive equation.

## 1. Inputs from round 11

Reread `round11_spectral_section.tex` and `round11_systems_section.tex` in full. The exact kernel-complement resolvent reduction, the translation-corrected positive denominator, and the resulting small-speed spectral pair remain consistent under the four explicitly stated spectral/profile hypotheses. No scalar real-sector nondegeneracy follows merely from phase coercivity.

The dimension-independent quantitative polarization estimate controls distance to **arbitrary rank-one fields**, not distance to the scalar optimizer manifold. Its transverse expansion and compactness argument do not require real-sector nondegeneracy. The finite-prefix unitary triangularization in infinite internal dimension correctly removes the otherwise missing local compactness.

At the root's request, reread the original optimizer-phase argument in `round9_foundations.tex` and the density argument in `round11_systems_section.tex`. The constant-phase and simple phase-kernel claims hold for every p>2, including noninteger powers and every dimension; they use neither radiality, positivity nor unique continuation. For a complex optimizer f=A+iB, equality in Minkowski for the density L^(p/2) norm forces B²=cA². Reapplying the same equality after a constant π/4 rotation excludes both signs of B/A occurring on positive-measure sets; when c=1 the rotated components instead have disjoint nonzero supports, which also excludes equality. Thus one constant phase makes the optimizer real, regardless of its zero set.

For kernel simplicity the preferable proof uses only first derivatives, avoiding any singular second-order power at zeros. Write κ=1+r, normalize M(Q)=Mc, A(Q)=1 and F(Q)=κ, and suppose a real h is in the nonnegative phase-form kernel. With x=A(h), y=M(h)/Mc, sharp interpolation at Q+i sqrt(t)h first gives nonnegativity and the kernel identity

    x+r y = ∫|Q|^(2r) h².

Hölder, sharp interpolation for h, and weighted arithmetic-geometric mean yield

    x+r y ≤ κ x^(1/κ)y^(r/κ) ≤ x+r y.

All inequalities are equalities. Equality in Hölder gives h²=yQ² on the whole space, including the zero set of Q. The nonnegative form kernel is linear, so applying the same statement to h+Q forces h to be one constant multiple of Q. Potential compactness in the energy-to-dual form norm follows from the strictly subcritical local Sobolev embedding and a small L^p tail. It upgrades kernel simplicity to energy-space coercivity on Q's L² complement. Compactness of the normalized optimizer family gives a uniform constant modulo translations and phase. This is the exact foundational input used in the new real-phase estimate.

## 2. Conserved internal covariance and improved coercivity

Let Γ(U)=∫|U(x)><U(x)| dx. This positive trace-class operator has trace M(U). For every internal unit vector ζ and scalar q,

    M(U−ζq) ≥ M(U)−<ζ,Γ(U)ζ> ≥ M(U)−||Γ(U)||op.

Consequently the normalized polarization distance p(U) in round 11 satisfies p(U)≥χ(U), where χ=1−||Γ||op/M. In fact, if Γ_A is the positive kinetic covariance,

    p(U)=2−||Γ/M+Γ_A/A||op.

This exact formula comes from orthogonally projecting the field onto one internal line in the weighted spatial Hilbert norm; no incompatible choices of the scalar approximant are being made for mass and kinetic energy. Combining p≤C d with p≥χ gives d≥cχ, with a fixed c>0 reduced to at most 1/2 if convenient. Thus

    F(U) ≤ κ (M/Mc)^(κ−1) (1−cχ) A(U).

For a common scalar dispersion and a common real density potential, each complex overlap of two fixed internal components is conserved. The appropriate justification is the Hilbert-triple product rule: the components lie in C(H^s) with time derivative in H^(−s), and both kinetic and common real potential pairings cancel. Each term is a legitimate duality pairing. This avoids assuming that an arbitrary smoothing commutes with the nonlinear potential. Equality of all matrix entries proves exact conservation of Γ also in countably infinite dimension. Its trace-norm continuity follows from

    ||Γ(U)−Γ(V)||_1 ≤ (||U||_2+||V||_2)||U−V||_2.

With an additional common nonnegative dispersion B, the energy satisfies

    2E ≥ [1−(M/Mc)^(κ−1)(1−cχ)] A+B.

Whenever the bracket is positive this bounds the full energy norm, and the stated conservative local-flow continuation hypothesis gives a global bounded solution. At M=Mc it is positive for every χ>0. Therefore any energy-norm-unbounded solution at exactly Mc must have Γ of rank one from the start, and is exactly scalar in a fixed internal line. Rank-one Γ implies this through positivity: the integral of the squared projection onto the orthogonal complement of that line is zero.

This argument supplies a nonexplicit but strictly larger threshold for every nonpolarized internal covariance. It does not identify an optimal threshold as a function of the full covariance spectrum. χ is an operator-norm fraction, not a von Neumann entropy.

## 3. Constrained energy curvature without real-sector nondegeneracy

Reviewed the constraint agent's derivation. Suppose pure homogeneous profiles of order m>2, frequency one, approach a real sharp optimizer Q with nonzero velocity v→0. Choose phase so Im U is Q-orthogonal. Coercivity of the scalar phase form and continuity of the nonlinear potential in form norm give

    Im U = −L_-^(-1)(v·∇Q)+o(|v|) in H^(m/2),
    P(U) = 2Tv+o(|v|).

The first-order spatial derivative maps H^s to H^(−s) because m>1. Thus this step needs neither inversion of L_+ nor differentiability of a preselected profile branch.

Use the finite-dimensional directions U and iL_-^(-1)∂_jQ to construct W(λ) with M(W)=M(U) and P(W)=P(U)/λ. At Q its mass/first-direction block is 2M and its momentum/internal-imaginary block is −2T, hence the charge Jacobian is invertible. This gives W'(1)=iΣv_jL_-^(-1)∂_jQ+o(|v|). For V_λ(x)=λ^(N/2)W(λ)(λx), mass and momentum are both exactly fixed. Direct differentiation of the scalar identity E(V_λ)=λ^m E(W(λ)) gives

    E''(V_λ)|_(λ=1)=q_L(W'(1))−(m−1)v·P(U)/2
                       =(2−m)vᵀTv+o(|v|²)<0.

The factors were independently checked: E(W)'=−v·P/2 and E(W)''=q_L(W')+v·P. The dilated curve need only be continuous in H^s; its scalar energy is C² by the exact homogeneity formula. Calling the whole curve C² in H^s without a scaling-generator domain assumption would be unjustified and is unnecessary. This proves a strict constrained energy saddle, not by itself nonlinear orbital instability.

The added action-ground corollary was also checked. At small velocity the quotient (A+M−v·P)/||u||_p² is coercive, and its exponent p=2+2m/N is strictly energy-subcritical. A normalized minimizing sequence is compact modulo translations: nonvanishing produces a nonzero weak limit, while the strict inequality c^(2/p)+(1−c)^(2/p)>1 excludes splitting. Its Nehari rescaling produces an actual traveling profile. As v→0 these minimizers become minimizers of the zero-velocity quotient. Optimizing M^r A at fixed A+M gives M=rA, which identifies the quotient optimizers with the sharp GN family; the frequency-one Nehari normalization fixes their mass to Mc. Thus the negative-curvature theorem applies to every sufficiently small nonzero-speed action ground wave, without selecting a differentiable branch. This establishes a nonempty, unconditional variational class. The ground-wave existence argument itself is established methodology and is not a priority claim.

## 4. Nonlinear orbital instability and an ancient solution on the exact invariant level

Final-read `round12_nonlinear_flow_section.tex` in full, including its subsequent hypothesis-reduction lemma. For the concrete quartic equation in dimensions N≤3, the remaining substantive assumption is real-block nondegeneracy, ker L_+=span{∂_jQ}. The branch, scaling-domain and complementary-gap hypotheses are proved from it rather than independently assumed.

Here are the checks on that reduction. From Q∈H⁶ one obtains V=|Q|^(8/N)∈W^(2,infinity), with V tending to zero at infinity. For bounded smooth truncations φ_R of a<x>, the exact weighted biharmonic identity controls e^(φ_R)Q uniformly in H²: its error from the unweighted positive form is O(a²) times the H² norm, the exterior potential is small, and the core weighted integral is uniformly bounded. Passing to the limit gives exp(a<x>)Q∈H². The conjugated equation has bounded smooth coefficients in terms of order at most three. Thus global elliptic inversion upgrades the weighted solution successively H²→H³→H⁴→H⁵→H⁶; multiplication by V preserves H². This supplies ΛQ∈H⁴ and its operator identity without an added moment assumption.

The profile map is C² from H⁴ times parameters to L². Its augmented equation on a fixed phase-translation slice has invertible derivative because the real Hessian is Fredholm with exactly the stated kernel. Phase and translation invariance force all augmented multipliers to vanish: their pairing matrix with the moving symmetry vectors stays invertible. The resulting C² branch is unique modulo symmetries. Exact critical scaling and local uniqueness make it scaling-closed; only strong continuity of the spatial dilation action is needed for this argument. Norm-resolvent convergence preserves the dimension N+1 of the isolated zero cluster, which is already filled by the actual symmetry derivatives. This proves the exact kernel and norm-continuous complementary inverse. The real-block nondegeneracy itself remains unproved and is visibly retained in the theorem.

The Nemytskii map F(u)=|u|^(8/N)u is locally C^(1,β) on H², with β=1 in dimensions one and two and β=2/3 in dimension three. Differentiating DF(u)h twice uses derivatives through D³F, L-infinity control of u and h, and L⁴ control of their gradients. D³F is 2/3-Hölder at the three-dimensional nonintegral power, so a remainder of order 1+β is justified. An unjustified quadratic remainder is not used. The Hilbert-vector version needed in the internal-dynamics theorem has the same bounds independently of internal dimension.

The H² local flow follows from its unitary free group and this local Lipschitz property. A selfadjoint Fourier projection regularization is Hamiltonian and commutes with phase and translation; mass, momentum and energy pass to the H² limit. Finite internal dimension is unnecessary. The profile is H⁶ by elliptic inversion from F(U)∈H²; the eigenvalue equation similarly upgrades its L²-domain eigenvectors to H⁶.

The standing Hessian has exactly one negative direction: sharp critical optimality makes it nonnegative on the codimension-one mass tangent space, while its value on Q is strictly negative. At small velocity, bounded potential convergence and the small first-order drift give actual norm-resolvent convergence with a common lower bound and positive essential spectrum. Together with the exact symmetry kernel and complementary gap, these properties preserve the negative index. Merely assuming continuity of the pseudoinverse would not suffice to rule out negative eigenvalues arriving from −∞; the author explicitly supplies the stronger concrete argument.

The real eigenvectors Y_± at ±λ form a nondegenerate hyperbolic plane for the action form. Their cross pairing cannot vanish, because a form of negative index one cannot have a two-dimensional totally isotropic subspace modulo its kernel. The form-orthogonal complement Z is invariant and nonnegative, with null space precisely the symmetry kernel K. Compactness of the decaying potential relative to the positive free form proves energy-space coercivity on Z after L² projection off K. The conserved quadratic form therefore bounds the quotient component, and the projected symmetry coefficients have derivative bounded by that quotient norm. This gives at most linear center growth and the full forward group bound

    ||exp(t J L)||_(H²→H²) ≤ C_v exp(λ_v t),  t≥0.

No unproved spectral-mapping assertion is being used. The kernel-coordinate derivative is legitimate directly in H^(−2)–H² duality; it does not require unnecessary differentiability of the solution in L².

The ancient fixed-point construction uses the full forward group in

    h(t)=ε exp(λt)Y_+ + ∫_(−∞)^t exp((t−s)JL) R(h(s)) ds,  t≤0.

The forcing decays as exp((1+β)λs), so the integral converges and its weighted Lipschitz constant is at most C_v ε^β/(βλ). The fixed point is an ordinary mild solution on every finite subinterval by splitting the integral. Backward H² convergence to U, combined with continuity and conservation, gives exactly the same M, all P, and E as U. No finite-dimensional correction of the energy surface is needed.

The local phase-translation orbit is a C² embedded finite-dimensional manifold because U has the needed translation regularity, its infinitesimal symmetry vectors are independent, and a nonzero L² function has no nontrivial phase-periodic translation. Translations going to infinity cannot approach U. The unstable eigenvector is transverse to the orbit tangent, so the fixed-point trajectory genuinely departs from the entire orbit. Time shifts give the stated first-exit asymptotic λ_v^(−1) log(1/δ)+O_v(1). The escape radius and constants are allowed to depend on v; no uniform two-parameter limit is inferred.

## 5. Quantitative kinetic amplification for actual near-critical trajectories

Reviewed the full `round12_critical_dynamics.md` and independently reproduced the proof. It establishes, for the stated strong conservative quartic solution class and sufficiently small d=(M/Mc)^(4/N)−1>0,

    |E| ≤ C d^(5/3) sup_(t≥0)||Δu(t)||²

for every forward-global uniformly H²-bounded trajectory with P=0 and E<0. The constant is independent of the ratio |E|/(d sup A). This is stronger than the preliminary qualitative sequence statement considered earlier in the round.

Critical scaling first sets sup A=1. The sharp GN deficit of every state is at most d. A real O(2) version of the round-11 quantitative polarization argument therefore selects a constant phase at each time with imaginary part O(sqrt d) in H². This is a genuine real-phase assertion, rather than the vacuous complex one-component rank-one statement. Its proof uses phase coercivity, not real-sector nondegeneracy. The phase need not be differentiated.

The localized mass derivative, after splitting into real and imaginary parts, is bounded by C sqrt d times the sum of the first two cutoff derivative norms. For a radius-R cutoff it is at most C sqrt d/R, R≥1. Near-optimizer compactness and the positive lower kinetic bound 2|E|/d give a finite concentration radius R₀ for the particular trajectory. The radius may depend on |E|/d, but the eventual speed estimate does not: two core centers more than 4R₀ apart force a change of at least Mc−3ε₀ in localized mass, whereas the derivative bound limits this change by C sqrt d |t−s|/R₀. Interpolation on time steps τR₀/sqrt d consequently gives a Lipschitz center with speed at most C sqrt d. This cancellation is the essential uniformity check.

The uniform mass-tail assertion is valid without assumed orbital compactness. If the tail exceeded M−Mc+η at arbitrarily large radii, translating a sequence of times by the chosen center would give a weak core of mass at least Mc−ε₀ but at most Mc−η. The remainder has limiting mass at most M−Mc+ε₀<Mc. Both core and remainder are strictly subcritical. Quadratic and Brezis–Lieb splitting would then make the fixed negative energy nonnegative, a contradiction. Thus the uniform tail mass is at most the surplus M−Mc in the large-radius limit. This statement does not imply kinetic localization.

The refined localized virial inequality retains its negative exterior kinetic term. The radial weight has Hessian at most the identity, agrees with |x|²/2 inside R, and is constant outside 2R. Its principal defect is therefore nonpositive everywhere and equals −8|D²u|² outside 2R. The exterior kinetic density is the full Hessian: replacing it pointwise by |Δu|² would be incorrect, and the source correctly avoids doing so. Their total integrals agree.

For exterior mass μ, the nonlinear tail is bounded by C μ^(4/N)(K_R+H_R+R^(−2)), while the moving-center term is bounded by

    C L μ^(3/4)[(K_R+H_R)^(1/4)+R^(−1/2)].

These follow by applying sharp GN and gradient interpolation to a cutoff product; global H² bounds control its derivative errors. The intermediate R^(−1)μ term is absorbed by the displayed error for μ≤1 and R≥1. Young's inequality absorbs K_R into the negative exterior term and leaves C L^(4/3)μ, plus annular terms.

The transition annuli at radii 8^j R_* are disjoint about the same moving center. Their summed Hessian energy is at most one. Time averaging and Jensen's inequality therefore make their contributions tend to zero as the number of annuli tends to infinity. For any fixed finite set of radii, the boundary term J_R/T vanishes as T→∞. Taking these limits in the specified order, then removing the radius cutoff and η, yields

    |E| ≤ C L^(4/3)(M−Mc) ≤ C d^(5/3)

under the normalization. Undoing the critical scaling proves the stated estimate.

The amplitude-data corollary is also valid: for u₀=sqrt α Q, E=−d A(u₀)/2, so any global bounded solution must have sup A/A(u₀) at least c d^(−2/3). Under the continuation alternative, finite-time breakdown and global unboundedness likewise force crossing of any fixed kinetic level. Hence these arbitrarily small perturbations of Q eventually leave a fixed phase-translation orbital neighborhood. In dimensions one through three the local theory is supplied directly; higher dimensions retain the explicit conservative solution and approximation assumptions.

The amplification bound does not exclude a very large but bounded global orbit. It does not prove finite-time blowup or growup for every global negative-energy solution. No such stronger conclusion follows from the argument.

## Overall assessment

No mathematical defect was found in the completed statements reviewed above. The main actual-flow amplification theorem uses uniform constants and does not assume radial symmetry, a moment bound or localization of the trajectory. The conditional nonlinear instability theorem now controls a genuine trajectory on the exact joint invariant level. The internal-covariance consequence is valid also for infinitely many components. Each conclusion retains its explicit model and local-flow hypotheses; the review does not settle publication priority or the remaining classification of large bounded near-critical motion.

