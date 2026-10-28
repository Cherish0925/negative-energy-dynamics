# Round 11 independent mathematical review

This record is an independent derivation and consistency review. It does not establish literature priority and does not replace the hypotheses of the statements reviewed.

## 1. Round 10 analytic foundations

Reviewed `round10_foundations_section.tex`, `round10_hartree_section.tex`, `round9_foundations.tex`, and the relevant conventions in `round10_inertia_section.tex`.

### Weak local-power profiles

The shifted resolvent argument is consistent for every m>1. If r=m/N<1, the initial nonlinear input exponent is

    2 / ((1-r)(1+2r)) > 1.

The proposed reciprocal exponent iteration therefore starts in the L^p resolvent range. Its fixed point is 1/2, and the actual initial exponent lies strictly below that fixed point, so finite iteration reaches the boundedness range. Low-amplitude nonlinear terms and the frequency correction can be treated separately using interpolation with L^2. Once U is bounded, the nonlinearity is L^2; U belongs to H^m, hence H^1; the C^1 chain rule then gives H^{m+1}. This argument does not need a C^2 nonlinearity at a nodal set.

The general symbol assumptions allow derivatives singular at zero. They nevertheless suffice for Mihlin estimates of the shifted resolvent. They also suffice for the cutoff commutator estimate: for comparable frequencies the factor |xi+eta| compensates the possible |xi|^{-1} derivative, while for noncomparable frequencies |xi+eta| is bounded by a multiple of |xi-eta|. Dividing by the two H^{m/2} weights leaves at most a factor <xi-eta>^{m/2}; the rescaled Fourier kernel has uniformly bounded L^1 norm.

The cutoff Pohozaev signs were checked against the convention P=Im integral(conj(U) grad U) and the profile a(D)U+omega U+i v.grad U-N(U)=0. They give

    v.P = 2mE,
    omega M = (m/N) A + (2m-p)E.

The test is legitimate after the profile bootstrap, and the limit extends by the uniform form bound. No moment assumption has entered.

### Hartree profiles and compactness

For 1<m<N, rho belongs initially to L^{N/(N-m)}. The near kernel lies in L^j for every j<N/m, so its convolution with rho belongs to arbitrarily large finite L^t spaces. Fixing t>N/m yields a strictly positive Sobolev improvement m/N-1/t. The bootstrap to L-infinity and then H^{m+1} closes.

The compactness argument uses q=4N/(2N-m), strictly below the energy Sobolev exponent. Approximating the limiting density by a smooth compactly supported one gives a bounded potential vanishing at spatial infinity; the HLS bound controls the approximation in form norm. This proves both the potential compactness and the nonlocal cross-term disappearance required for splitting. Positive definiteness of the interaction form, rather than positivity of the kernel pointwise, is the correct phase-geometry hypothesis.

The symmetrized cutoff term has coefficient -1/4 and converges to mH/4. The resulting identities and shifted-frequency formula were independently checked:

    v.P = 2mE - D_b,
    omega M = A+B+(2m-4)E-D_b,
    mE = <Y,[a+omega_tilde-K*rho]Y>+B(Y)
         +(1/2-M(Y)/M)D_b.

These signs support the claimed uniform dispersion-cone gap.

### Density convexity and the phase kernel

The first-order density-norm proof is sound. Equality in the supporting-functional inequality for a differentiable strictly convex norm power forces positive proportionality of the two densities. Weighted arithmetic-geometric mean gives equality of their kinetic-to-mass ratios. Polarization through b+Q then removes the possible position-dependent sign. Compactness of the potential upgrades kernel simplicity to energy-space coercivity on the L^2 complement. Optimizer uniqueness, a maximum principle and real-sector nondegeneracy are not used.

## 2. Dimension-independent internal polarization

The following mechanism supplied by the systems agent was independently checked. It addresses the genuine issue that the component count can vary, so fixed-dimensional Rellich compactness alone is insufficient.

Embed all internal spaces into ell^2. Write a bounded sequence U_n in X tensor ell^2, X=H^{m/2}, in a fixed scalar orthonormal basis phi_k. Its internal coefficient vectors are c_{n,k}. Choose an internal unitary W_n that triangularizes the FIRST n coefficient vectors: W_n c_{n,k} lies in span(e_1,...,e_k) for k<=n. Finite-dimensional Gram-Schmidt supplies this, and the transformation extends to a unitary. Triangularizing an infinite family at once is unnecessary and can raise an avoidable complement-dimension issue.

For each fixed k the transformed coefficients lie in a fixed finite-dimensional ball. A diagonal subsequence makes them converge strongly. If K_chi:X->L^2 is multiplication by a compactly supported cutoff followed by the local embedding, K_chi is compact. Its approximation K_chi P_K by finite-rank spatial projections holds in operator norm. After tensoring with the internal identity, the tail estimate retains that same norm; the finite-rank part converges because finitely many internal coefficient vectors converge. This proves strong local L^2 convergence with values in ell^2 after the unitary changes.

Dimension-independent local nonvanishing follows from the Hilbert-valued Sobolev estimates, obtainable by Minkowski applied to the component squares. For local powers, almost-everywhere ell^2 convergence gives the vector Brezis-Lieb splitting through the usual norm-power inequality. For Hartree, the cross density is bounded pointwise by ||U||_{ell^2} ||R_n||_{ell^2}; the scalar HLS and compact-potential argument applies unchanged. Sharp interpolation and mass/kinetic splitting then force full strong energy convergence. A limiting optimizer polarizes to a scalar optimizer times a fixed unit internal vector.

For the gap proof, after this convergence choose a further unitary sending the coefficient vector (<U_{n,j},Q>) to a positive real first coordinate. Every imaginary component is then Q-orthogonal. Scalar phase coercivity can be summed without a factor depending on component count. The shifted energy identity also sums componentwise.

This review supports the dimension-independent theorem for a COMMON scalar principal dispersion, a COMMON scalar admissible dispersion addition, and attraction depending only on total density. A component-dependent or complex matrix dispersion is not automatically covered: conjugating by an internal complex unitary can destroy the real/imaginary splitting on which the phase identity relies.

The completed `round11_density_systems.md` was subsequently reviewed in full. Its stronger nonpositive-energy rigidity theorem is valid: equality in the coercive shifted identity forces E=0, Y=0 and D_b=0; the imaginary equation then forces v=0; positivity of the common frozen real form on Q-perp makes its kernel at most one-dimensional and forces exact internal polarization. For pure homogeneous dispersion, the near-critical small-normalized-energy theorem also permits positive energy: the phase-boost identity gives v->0, the frozen complex form converges to L_Q and is positive on complex Q-perp, so its complex kernel has dimension at most one. This again forces exact polarization. The countably infinite internal dimension causes no further issue after the uniform compactness construction. The paper correctly excludes non-scalar internal frequency generators from these common-frequency statements.

### Final addition: quantitative polarization

The final dimension-independent inequality was independently checked. For M(U)=Mc, A(U)=1, X norm squared A+M, and

    R(U)=inf_{||zeta||=1, q in H^s} ||U-zeta q||_X^2,

the proposed bound R(U)<=C[kappa-F(U)] is valid. The scalar q in this distance is arbitrary; this is transverse polarization stability, not stability of the scalar optimizer manifold.

To check the only delicate remainder, after compactness and alignment write U=(u,Z), with every component of Z complex-L2-orthogonal to a fixed scalar optimizer Q, and u->Q. Put a=|u|^2, b=||Z||^2. For 1<kappa<=2,

    0<=(a+b)^kappa-a^kappa-kappa a^(kappa-1)b<=C b^kappa.

For kappa>2 the remainder is bounded by C(a^(kappa-2)b^2+b^kappa). Dimension-independent Sobolev and Holder estimates bound the integral by O(||Z||_X^(2kappa)) in the first case, and by O(||u||_Lp^(2kappa-4)||Z||_X^4+||Z||_X^(2kappa)) in the second, where p=2kappa. Both are o(||Z||_X^2), uniformly near Q. In the Hartree case the exact remaining term is H(Z)=O(||Z||_X^4).

Applying scalar sharp interpolation to u and expanding its exact mass/kinetic deficits gives

    kappa-F(U)>=kappa[A(Z)+(kappa-1)M(Z)/Mc-<V_Q,||Z||^2>]
                  -o(||Z||_X^2).

The scalar interpolation expansion costs O(||Z||_X^4), and potential-form continuity contributes o(1)||Z||_X^2. Phase coercivity on complex Q-perp thus gives kappa-F(U)>=c||Z||_X^2>=cR(U). If no global constant existed, R(U)<=1+Mc would force the sharp-interpolation defect to zero along a violating sequence, allowing exactly the compactness argument above. This proves a uniform constant with no scalar real-sector nondegeneracy assumption.

## 3. Small-velocity spectral bifurcation

Reviewed the full proof in `round11_spectral_bifurcation.md`.

The exact reduction of J L_v psi=lambda psi with J=-i to the kernel matrix

    D_ij(lambda,v)=<g_i,J (L_c+lambda J_c)^{-1} Jg_j>

is correct. The kernel is symplectically isotropic because phase and translation charges commute. The complementary inverse is uniformly analytic for small lambda under the stated operator assumptions. Away from lambda=0 the finite-dimensional elimination preserves multiplicity.

At lambda=0, D=diag(1,-I) d'' diag(1,-I). In particular its velocity block is -T at v=0. The transpose relation D(-lambda)=D(lambda)^T makes the scalar Schur complement even. Direct real/imaginary block calculation gives the phase lambda^2 term

    <Lambda Q,L_-^{-1}Lambda Q>/m^2

before translation coupling, and subtracts

    c^T T^{-1}c/m^2.

The sign of that subtraction is important. The proposed denominator

    D_Lambda=<Lambda Q,L_-^{-1}Lambda Q>-c^T T^{-1}c

is therefore correct and is invariant under a change of spatial center. It is strictly positive: equality would make Lambda Q a translation derivative, which would require a nonzero L^2 function to be homogeneous of degree -N/2 about one point.

Combining this coefficient with the exact charge scaling formula gives

    lambda(v)^2=(m-2) v^T T v / D_Lambda + o(|v|^2).

The formula has the correct sign: a real pair for m>2 and an imaginary pair for 1<m<2. The frequency rescaling factor omega^{1/m} in the growth rate is also correct. C^1 profile dependence and C^2 reduced action suffice here: the proof uses P=2Tv+o(v), B=2T+o(1) and exact scaling rather than differentiating an uncontrolled remainder.

One minor presentation correction was sent to the author: the scalar function is analytic in z=lambda^2 and continuous in the profile parameter v; joint real analyticity in v is not assumed. Uniform analytic inversion or a continuous-parameter implicit-function argument supplies the unique nearby real root.

The result is a spectral evolution theorem conditional on the specified branch, kernel and complementary inverse assumptions. The review does not turn it into an unconditional nondegeneracy theorem for all homogeneous symbols, nor into a nonlinear orbital-instability theorem without a local-flow argument.

## 4. Concentration energy and endpoint nonlinear dynamics

At the variational-dynamics agent's request, independently reviewed `round11_variational_dynamics.md`, Sections 1--6.

The high-frequency energy lower bound is valid for a bounded real even deficit d with a uniform angular limit. At masses at most the homogeneous critical mass, bounded perturbed energy and divergent kinetic energy force the normalized homogeneous energy defect to zero and the mass to the critical value. Scalar sharp-GN compactness then gives a normalized optimizer. Strong L2 convergence, the bounded deficit, and dominated convergence identify the limiting deficit energy. Thus the barrier is exactly the minimum concentration energy over the full optimizer manifold; its maximum is attained by compactness modulo translations and phase.

The strict-sublevel kinetic bound follows by contradiction, and its sharpness follows by dilating a maximizing optimizer. Conservation plus the explicitly stated continuation property proves the global bounded-flow result. For the q>m interpolation class, the deficit tends to zero, hence all negative-energy data at the upper critical mass are indeed covered. This conclusion concerns all such data, rather than only stationary minimizers.

The concrete H2 local theory for m=4 and N<=3 is sound. The local Lipschitz composition estimate uses H2 into L-infinity and W^{1,4}, together with local Lipschitz continuity of the first two derivatives of F(z)=|z|^{8/N}z. Spectral projection approximations conserve the exact projected Hamiltonian because the projection is selfadjoint and the solution remains in its range. Strong H2 convergence passes energy and mass conservation to the limiting flow. No arbitrary-symbol Strichartz estimate is being assumed.

The orbital stability proof is the classical compact-minimizing-sequence argument. It correctly restricts upper-endpoint perturbations to mass at most the endpoint; nothing in the proof licenses two-sided endpoint stability across higher masses.

The exact dilation-curvature coefficient was differentiated independently:

    (D^2-mD)b=q h z[(m+q)+(m-q)z]/(1+z)^3,
    z=|xi|^q.

The resulting lower-threshold ratio K/|I| -> m(m+q) has the correct constants. Tightness of the normalized correction-energy measures, not unproved higher-moment convergence, is the required input for the asymptotic argument.

A correction was sent concerning the explicitly labeled, unproved spectral-frequency candidate at the end of Section 6: for a non-even optimizer the denominator must remove translation coupling, as in Section 3 of this review. The unprojected <Lambda Q,L_-^{-1}Lambda Q> denominator is justified only if the mixed coefficients c vanish, for example for an even optimizer. This affects no proved energy, flow or stability statement.

## 5. Least-mass endpoint degeneracy

At the threshold-endpoint agent's request, reviewed `round11_threshold_endpoint.md`.

The identities E=d-theta.grad(d), grad(E)=-H theta and grad(M)=2H e_omega are correct. An attained negative-energy mass minimum indeed forces H e_omega=0. Critical scaling then gives (m-1)Bv=P, with v^TBv<0. A zero-energy profile strictly below the negative-energy mass threshold is a local energy minimum on any full nearby profile family and therefore forces H theta=0.

The supplied local profile family follows from a regular Fredholm slice with symmetry-only kernel by the projected implicit-function theorem and the Noether identities, provided the stated symmetry regularity is included. A null vector of H annihilates the mass and momentum derivatives. This gives the Fredholm solvability of LW=iZ and the chain JL W=Z, JL Z=g, JL g=0. Under the stated generator realization, the polynomial solution and its linear growth modulo symmetry tangent directions follow exactly.

The independent-charge perturbation argument excluding a nonsingular H at a moving zero-energy endpoint is valid. The exceptional standing profile with nonzero momentum is appropriately retained. In the rotationally equivariant attained case, direct differentiation verifies

    kappa'(c*)=-m omega (m-1)c* M''(c*).

One notation fix was sent: write H theta=0, not H(omega,v)=0, in the zero-energy theorem, since the latter can be mistaken for the entire matrix vanishing. The stronger entire-matrix conclusion only follows in the subsequently stated nonzero-speed rotationally equivariant case.

## 6. General-symbol transport and moving centers

At the root's request, independently checked `round11_transport_general.md` in full, with particular attention to the nonlocal exact-core argument.

The key cancellation is correct. For z supported inside the core, L_R z=Lz, where L is the exact dilation generator. Symmetry and skew-adjointness give

    <z,[a(D),L_R]z>=2 Re<a(D)z,L_R z>
                        =2 Re<a(D)z,Lz>=mA(z).

This remains true although a(D)z is nonlocal. The statement is only a quadratic-form cancellation; it never requires the defect applied to z to vanish pointwise. Approximation within a slightly larger core extends it to compactly supported H^{m/2} functions.

The Fourier-Schur estimate is also valid. Comparable frequencies yield a bounded quotient after division by the two energy weights; noncomparable ones cost at most <xi-eta>^{m/2}. The remaining Fourier cutoff is Schwartz. Unitary rescaling gives Q_R^2=||D^{m/2}u||_2^2+R^{-m}M. Splitting u into core and exterior pieces therefore leaves an error bounded by C_B(sqrt(T_R)+R^{-m/2}). The proof needs no sign of the angular Hessian of a.

Direct differentiation of J_R=2<u,-iL_Ru> gives the kinetic term 2<u,[a,L_R]u>, the local nonlinear term -2(p-2)/p times the divergence integral, and the Hartree symmetrized term with coefficient one. Their homogeneous limits combine to 4mE. The moving center contributes -2c'.P plus an exterior current term. The H^{1/2} form estimate and interpolation give T_R^{1/m}+R^{-1}; this verifies gamma=min(1/2,1/m), beta=min(m/2,1).

Every term in the integrated identity is continuous on bounded H^{m/2} sets, with the kinetic form controlled by the uniform commutator estimate. The passage from smooth approximations is consequently justified under the note's explicit approximation assumption. A Lipschitz center is sufficient: its time derivative enters only almost everywhere and is bounded.

The sliding-interval estimate correctly holds uniformly in the starting time S and every center with the stated speed bound. Holding R=nu T fixed during each integral, and then applying Jensen to the concave power gamma, gives the asserted positive lower bound on the average exterior kinetic energy. For fixed R, the same two-sided identity gives the exact averaged drift; the order of limits is correct.

The arbitrary-center argument is valid. Negative energy supplies a fixed nonzero L^p or L^q core. The PDE yields a uniform H^{-s} time-Lipschitz bound, and interpolation gives uniform continuity in that same nonlinear spatial norm. Two centers farther apart than the core diameter within a sufficiently short time would contradict that continuity. Piecewise-linear interpolation therefore produces a bounded-speed center at bounded distance. The nested-cutoff product identity transfers homogeneous kinetic localization to this center.

For isotropic fourth-order Hartree, the HLS exponent becomes the H1 Sobolev exponent, so the exterior interaction error is controlled by the exterior gradient energy plus R^{-2}. The favorable-sign biharmonic virial estimate then yields the stronger gradient statement. Its one-sided drift consequence has the correct orientation, limsup P.[c(T)-c(0)]/T<=8E.

No additional dynamical conclusion follows for an orbit with persistently replenished exterior kinetic activity; the note correctly retains this possibility.

The author subsequently added a literal-tail equivalence lemma in `round11_transport_section.tex`; this addition was also checked directly. For s<1, the Fourier Holder bound on |xi|^s gives ||[|D|^s,eta_R]u||_2<=CR^{-s}||u||_2. For s>=1, the mean-value bound gives C(R^{-1}||D^{s-1}u||_2+R^{-s}||u||_2). With delta=min(s,1), the two tails therefore satisfy sqrt(T_R)<=sqrt(D_R)+C_BR^{-delta} and sqrt(D_{2R})<=sqrt(T_R)+C_BR^{-delta}. The final transport theorem may consequently use the literal exterior integral of ||D|^{m/2}u|^2. Substituting into the virial bound gives the correctly stated error exponent 2 delta gamma=min(m/2,2/m). The updated exact-drift and arbitrary-center results at this literal-tail level are valid.

## Overall assessment

No substantive mathematical defect was found in the audited round 10 foundations or the completed conditional spectral calculation. The dimension-independent polarization mechanism is valid and supplies the missing compactness ingredient for the systems extension; the final systems theorem must preserve the common-dispersion and total-density assumptions. The high-frequency strict-sublevel theorem supplies genuine nonlinear global dynamics under its local-flow hypothesis, and unconditionally in the concrete quartic N<=3 realization supplied. The endpoint response/Jordan-chain statements are valid with their stated regularity and Fredholm assumptions. General near-ground nonlinear dynamics of the pure homogeneous equation remains a separate problem.
