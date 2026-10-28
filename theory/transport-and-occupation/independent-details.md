# Round 13 independent mathematical derivation

## 1. Scope of the completed initial derivation

Read in full: round12_critical_dynamics.md, round12_critical_dynamics_section.tex, and round11_systems_section.tex. Re-derived the fragile parts of the round-12 kinetic-amplification theorem rather than accepting the earlier review conclusions.

Current conclusion: no substantive gap found in the round-12 theorem as stated for conservative strongly approximable H² solutions. Its conclusion is mandatory kinetic amplification, not finite-time blowup or exclusion of every bounded global orbit.

## 2. Quantitative constant-phase estimate

The real two-component argument is essential; the complex one-component rank-one assertion would be vacuous. The real version is valid.

For normalized M(Q)=Mc and A(Q)=1, omega=(p/2-1)/Mc, the phase form L_-=Delta²+omega-|Q|^(p-2) is nonnegative by imaginary variation of sharp GN. If h lies in its kernel, put x=A(h), y=M(h)/Mc. Holder followed by sharp GN gives

    x+(kappa-1)y = int |Q|^(2kappa-2)h²
                     <= kappa x^(1/kappa)y^((kappa-1)/kappa)
                     <= x+(kappa-1)y.

Equality gives x=y and h²=y Q². Since the kernel is a linear space, apply the same equality to h+Q. The two possible signs of h/Q cannot both occur, because (1+sqrt(y))² and (1-sqrt(y))² are distinct when y>0. Thus h=cQ. This does not assume positivity of Q, positivity preservation of the biharmonic resolvent, unique continuation, uniqueness of the optimizer, or L_+ nondegeneracy.

Compactness of the potential form and the positive essential spectral threshold imply H² coercivity on Q-perp. Normalized optimizer compactness gives uniform constants modulo translation. The transverse Taylor remainder is o(||Y||H²²), including p<4, by the L^p remainder bound. These facts close the contradiction proof of the global constant-phase deficit estimate.

## 3. Slow center and uniform mass surplus

Writing u=e^(itheta)(X+iY), the exact localized density derivative consists of bilinear X,Y terms. The bound is C sqrt(d)(||grad phi||infinity+||Delta phi||infinity); no phase time derivative is taken. For a radius-R cutoff this is C sqrt(d)/R when R>=1.

Near-optimizer compactness gives a fixed normalized core radius. The positive lower kinetic scale 2e/d for the particular orbit turns it into a finite physical radius R0. Center locations at a time gap proportional to R0/sqrt(d) cannot differ by more than 4R0, because the two near-Mc mass cores would be disjoint. Linear interpolation therefore has speed C sqrt(d), with constants independent of e/d; the radius R0 cancels.

For the uniform tail claim, suppose mass outside radii Rk tends above M-Mc+eta. Recenter at the already selected Lipschitz center. Weak H² compactness and local strong L² convergence give a core v satisfying Mc-epsilon0 <= M(v) <= Mc-eta. The remainder mass is at most M-Mc+epsilon0<Mc. Brezis-Lieb and quadratic splitting give -e=E(v)+E(remainder)+o(1), impossible because both pieces have subcritical mass. This proof is sound; it does not require kinetic tightness.

## 4. Localized virial and annulus averaging

For the truncated quadratic radial weight with D²phi<=I, the leading kinetic density is

    8 Re int phi_jk partial_ij(bar u) partial_ik(u).

Its defect relative to 8A is nonpositive as a quadratic form, and equals -8|D²u|² outside the cutoff. This uses the full Hessian density, not an incorrect pointwise identification with |Delta u|². Higher derivatives of the weight give O(R^-2) under the normalized H² bound. The nonlinear coefficient is -16/(Np), consistent with the global derivative 16E.

The moving-center contribution is -2a' dot P plus an exterior current. At P=0 the latter is bounded by C L mu^(3/4)(K+H+small)^(1/4), where mu is the exterior mass. Young's inequality produces C L^(4/3)mu after absorption into the negative exterior Hessian term. The nonlinear tail is C mu^(4/N)(K+H+small), which is absorbable at small mass surplus.

The disjoint annuli have total time-integrated kinetic mass at most T. One can select an annulus with time-averaged kinetic mass <=1/K. Its finite radius, though potentially enormous, remains fixed during the integration. The limits T->infinity, K->infinity, Rbase->infinity and eta->0 are legitimate in the stated order. No unproved differentiation of a growing cutoff enters. This yields e<=C L^(4/3)(M-Mc), and hence e<=C d^(5/3)B.

## 5. Flow and conclusion scope

The theorem explicitly assumes strong energy-space approximation. In N<=3, the local nonlinearity is locally Lipschitz in the H² algebra. For N=3, its exponent is 8/3; enough composition regularity holds for the local flow, though stronger smooth-remainder claims must retain the stated Holder exponent. Conservation and the integrated identities can be obtained using regularized nonlinearities and strong H² convergence; one should not assume unlimited classical regularity of the unsmoothed fractional-power nonlinearity at its zeros.

The continuation alternative extends the bound to the full maximal lifespan: finite breakdown or unbounded global evolution trivially has infinite kinetic supremum; only bounded global trajectories require the main proof. For amplified real sharp optimizers, E=-d A0/2, so the mandatory factor is c d^(-2/3). This does imply orbital instability in H² modulo phase and translation, with a finite time crossing of each prescribed factor for sufficiently small d. It does not identify the eventual fate of that solution.

## 6. Direct nonzero-momentum extension

Before using P=0, retain the term -2a' dot P and bound its absolute value. The same proof yields, with B=sup A,

    |E| <= C [d^(5/3) B + sqrt(d) |P| B^(3/4)].

All powers agree with critical scaling. The phase deficit only gives |P|<=C sqrt(d) B^(1/4), which reduces the extra term to order dB. Thus this elementary extension cannot by itself remove the zero-momentum hypothesis while preserving the stronger amplification power.

## 7. Round-13 incoming results

Pending full drafts. The proposed improved center-speed argument is being independently checked; its present form must retain real-sector nondegeneracy and optimizer-component trapping. A negative energy curvature by itself does not imply dynamical instability.

## 8. General homogeneous dispersion: completed full derivation

Read round13_general_dispersion.md in full and independently reconstructed every Fourier-kernel estimate. Verdict: the stated extension for real even positive elliptic m-homogeneous a, m>2, passes this internal mathematical review in its explicit strongly approximable conservative H^(m/2) flow class.

Set s=m/2, b=sqrt(a), g=b(D)u, and B_jk=(partial_j a)xi_k/a. The important facts are bounded degree-zero B_jk and sum_j B_jj=m. For h=xi-zeta,

    |B(xi)-B(zeta)| b(zeta) <= C |h| |zeta|^(s-1).

When |h|<|zeta|/2 this follows from the degree-minus-one derivative; in the complementary region it follows from boundedness of B and |zeta|<=2|h|. Since s>1 there is no low-frequency singularity. This proves the cutoff commutator [B,theta_R]b=O(R^-1):H^s->L².

For f_R=x h0(x/R), the exact Fourier kernel of [a(D),L_R] is

    (i/2)(a(xi)-a(zeta))(xi+zeta)_k fhat_R,k(xi-zeta).

Subtract the first Taylor term i h_j fhat_R,k partial_j a(zeta)zeta_k. The remainder is bounded by |h|²(|zeta|+|h|)^(m-1)|fhat_R|. Dividing by the two H^s weights leaves at most polynomial growth in h, so Schur and fhat_R=R^(N+1) fhat_1(Rh) give O(R^-1). The b-sandwich replacement has kernel difference (b(xi)-b(zeta))b(zeta)B(zeta)(partial_j f_R,k)^hat, again giving O(R^-1). These are ordinary Fourier estimates, not an appeal to an unproved positive pseudodifferential symbol.

The h0 I part of Df_R gives exactly m int h0|g|². Every angular/anisotropic term is confined to an annulus coefficient c_jk. If theta is one on that coefficient's support,

    <g,c B g> = <theta g,c B(theta g)> + <theta g,c[B,1-theta]g>.

The first term is bounded by annular L² mass of g and the second is O(R^-1). Therefore the claimed negative exterior |g|² contribution is valid without convexity of a. The nonlocal kinetic density g is legitimate because [b,cutoff]u=O(R^-1) in L², which also validates the exterior GN and current estimates.

The general vector field f_R need not be a gradient: the exact virial identity uses its divergence in the nonlinear term, and its full derivative in the moving-center term. For f=x on the core this gives 4mE. The statement in the draft that Df=I “there” should explicitly mean inside the core ball; the resulting motion defect is outside it.

The remaining density transport, weak-core splitting, and fixed-radius annulus limits are the R12 arguments with kinetic current exponent 1/m. They give

    |E| <= C d^[1+m/(2(m-1))] sup A,

and the amplitude perturbation amplification exponent m/[2(m-1)]. This is an actual extension of the proved dynamical implication, not merely a formal scaling extrapolation. It does not constitute an established priority claim or a universal local-well-posedness theorem for all symbols and dimensions.

## 9. Momentum-adapted modulation: completed full derivation

Read round13_center_momentum.md in full. Verdict: the stronger quartic estimate satisfies the stated hypotheses under BOTH stated additional inputs: ker L_+=span translations and the explicitly required weighted regularity of Q,Z_j,W. Neither input is silently supplied by R12.

The phase inverse duals Z_j=L_-^-1 partial_j Q yield the positive matrix T. Translating the origin changes c_j=<Lambda Q,Z_j> by minus T times the translation, so one may set c=0. Then W=L_-^-1 Lambda Q satisfies <partial_jQ,W>=0 and D=<Lambda Q,W>>0. These identities remove linear translation-scale cross-coupling without radial symmetry.

Sharp mass-sphere minimization gives nonnegativity of L_+ on Q-perp. Its constrained nullspace is exactly span{Lambda Q,partial_jQ}: a zero constrained form implies L_+h lies in span Q; L_+Lambda Q=-4Q and the assumed kernel then identify h. The W and Z gauges remove these null directions. Compact potential perturbation gives coercivity in H². Q itself is perpendicular to all Z_j and W, so the extension to h not exactly Q-perpendicular with error C<h,Q>² is legitimate.

Nondegeneracy isolates Q in the set of optimizers normalized to the same mass and kinetic energy. A continuous trajectory with uniformly small deficit cannot leave that component: choose rho so the distance-2rho neighborhood of Q's phase/translation orbit contains no other normalized optimizer. A state on the distance-rho boundary cannot be within rho/4 of any normalized optimizer. Near-optimizer compactness rules out such a boundary crossing for sufficiently small d. This justifies the single ground-wave chart for the entire trajectory.

I substituted u=lambda^(N/2)e^(itheta)(Q+h+ik)(lambda(x-a)) into the PDE and checked the exact real/imaginary equations and all three differentiated gauges. Their signs and factors agree with (6)–(11) of the note. In particular,

    P=0  =>  <k,partial_jQ>=-<k,partial_jh>,

so the translation equation has no linear right-hand side after the T/D centering. The scale and phase parameters are O(epsilon), hence their contributions back into translation are quadratic; v=O(epsilon²). The physical speed is a_t=lambda³v, not lambda v or lambda⁴v.

The mass identity and S=E+M/2 expansion give epsilon²<=Cd because E(w)<0 and M(w)-Mc=O(d). With B=1, lambda is uniformly bounded above, hence the center speed is O(d). The same weak-core argument and annulus virial then yield

    |E| <= C_Q d^(7/3) B,
    sup A/A0 >= c_Q d^(-4/3)

for amplified Q data. This doubles the quartic amplitude-excursion exponent relative to R12, conditionally. Reapplying this fixed-d estimate at a later time does not produce unbounded iteration: d and E are conserved, so no all-bounded-orbit exclusion follows.

## 10. Gaussian occupation theorem and explicit polarization: completed derivation

Read round13_invariant_threshold.md in full. All displayed Gaussian and covariance formulas pass independent verification.

In the eigenbasis of the mass covariance, a finite complex Gaussian projection has random mass S=sum lambda_j|Z_j|². Pointwise Gaussian integration gives E F(f_Z)=Gamma(r+2)F(U). Phase averaging kills all off-diagonal kinetic Gram entries even after multiplication by S^r. The exchange-of-two-coordinates proof orders b_j=E[|Z_j|²S^r] exactly as the occupations. Holder and convex Jensen at exponent r+1 give b_1<=Gamma(r+2)M^r, with strictness at every rank greater than one. This holds for all r>0.

There is no infinite-dimensional identity-covariance Gaussian in the proof. Finite internal projections converge in the energy norm, while their mass moments increase monotonically and remain bounded by M^r. Thus the infinite-rank passage is valid.

For r>=1, convex Jensen at exponent r gives the stated trace-alignment coefficient. The exact projection distance is p(U)=2-lambda_max(X+Y), since a scalar kinetic multiplier commutes with fixed internal projections. The spectral estimate lambda_max(X+Y)>=Tr((X+Y)²)/2>=2Tr(XY) gives the constants 2(r+1)/r in the complex case and (2r+1)/r in the real case. The latter legitimately treats one complex scalar field as two REAL components; its real covariance is not asserted to be dynamically conserved.

Checked formulas B1=(M+mu)/2, B2=(M²+TrGamma²+2Mmu+2mu²)/6, B4 via complete homogeneous polynomials, and the equal-occupation gamma ratio. For two equal occupations at quartic N=2, B2=M²/2, hence the explicit sufficient interval M<sqrt(2)Mc is correct. It is not a computation of the optimal fixed-spectrum threshold.

The evolution consequence follows from conservation of the complex internal covariance and energy. At M=Mc, any unbounded energy norm forces rank-one covariance because every higher rank has strict B_r<Mc^r; rank-one covariance gives a fixed internal direction for the full solution, not merely for a blowup subsequence.

I independently opened Frank--Gontier--Lewin arXiv:2002.04964v3. Theorem 2 states strict finite-rank spectral improvement L^(2)>L^(1) for gamma>max(0,2-N/2). At gamma=1 this applies in N>=3. Finite-rank gamma=1 duality supplies K2<K1 for two orthonormal kinetic-density modes. The note's smooth compactly supported orthonormal approximation preserves that strict inequality, and choosing each occupation mu below Mc but above (kappa K2)^(N/2) gives negative-energy finite-variance second-order vector NLS data. The standard 16E variance identity then proves finite-time blowup. This correctly refutes the proposed maximum-occupation-only principle in that model class; it is a consequence of established strict binding, not a new resolution of Lieb--Thirring and not a quartic counterexample.

## 11. Actual-time lower average without a kinetic upper bound

Read round13_virial_closure.md in full and rederived its new steps. The unconditional quartic strengthening

    liminf_(T->infinity) T^-1 int_0^T A(t)dt >= c |E| d^(-5/3)

satisfies the stated hypotheses for the stated forward-global conservative strong flow.

The instantaneous phase decomposition yields cutoff transport sqrt(d)[R^-1 A^(3/4)+R^-2 A^(1/2)]. Since A>=2e/d, choose R above a fixed orbit-dependent scale. Interpolating concentration centers in intrinsic time int A^(3/4) gives a locally absolutely continuous physical center with |a'|<=C sqrt(d) A^(3/4), and a uniformly bounded physical difference from the sharp normalized concentration center.

The new mass-tail argument correctly handles A(tk)->infinity: normalize each bad sequence by A(tk)^(-1/4) ABOUT ITS SHARPLY LOCALIZED CENTER, not about a center whose normalized displacement might diverge. The rescaled fields have kinetic energy one and a nonzero fixed-radius mass core. The alleged exterior surplus forces the weak core mass below Mc. Its energy is then strictly positive, whereas the subcritical remainder has nonnegative energy and total rescaled energy has a nonpositive limit. This is a contradiction. Thus uniform physical mass tails bounded by M-Mc+eta do not require a uniform kinetic bound.

The moving-center Young term is C mu |a'|^(4/3)<=C mu d^(2/3) A. The remaining cutoff error is q_R=R^-2 sqrt(A)+R^-4, and the endpoint virial is bounded by CR A^(1/4). Given finite lower average L, choose Tn approaching it, then tn in the last sqrt(Tn) interval with A(tn)<=C(L+1)sqrt(Tn). Their time averages still tend to L and A(tn)^(1/4)/tn->0. This supplies the endpoint control missing from a direct uniform-bound argument. Disjoint-annulus averaging followed by the time, annulus-count, radius and eta limits gives the stated lower average.

The positive lower density of high-kinetic times requires the separately stated finite B=sup A. Without finite B, a positive average can still be supported by sparse high peaks; the theorem does not claim otherwise.

The constructed zero-momentum data (1+a epsilon²)Q+i epsilon h were checked: momentum vanishes exactly, d is order epsilon², large fixed a makes E negative, and the cubic Fourier current is exactly 8epsilon(1+a epsilon²)<h,partial_j Delta Q>. Such h exists because an L² Fourier transform cannot be supported on the zero set of the resulting nonzero polynomial. This proves the ordinary instantaneous density current need not be order d even at P=0.

## 12. Removal of weighted-dual assumptions; conditional stronger average

Subsequently read the added weighted elliptic lemma in round13_center_momentum.md. It is valid in N<=3. For w=e^phi Q, direct expansion gives the exact identity

    Re<Delta²Q,e^(2phi)Q>
      = ||Delta w+|grad phi|²w||²
          -||2 grad phi dot grad w+(Delta phi)w||².

Smooth bounded truncations of a<x> have errors O(a²)||w||H²². The potential tends to zero at infinity, while the weighted contribution on a fixed interior ball is uniformly bounded. Absorption proves exponential weighted H². Since Q lies in H6 and V=|Q|^(8/N) is in W^(2,infinity), conjugating and bootstrapping the order-at-most-three perturbation gives weighted H6. The same proof with source f=partial_jQ or Lambda Q applies to Z and W: weighted f is in H² at a slightly smaller exponential rate, and its pairing is absorbed by one quarter of the L² term. Thus the earlier separate weighted-dual assumption is now proved from the concrete equation; only real-sector nondegeneracy remains additional.

The modulation center has a core ball of radius C A^(-1/4), and speed |a'|<=C_Q d A^(3/4). Applying the previous actual-time argument to this center gives

    liminf T^-1 int A >= c_Q |E| d^(-7/3),

without a global kinetic upper bound. All earlier modulation trapping and epsilon²<=Cd estimates were themselves independent of such an upper bound. This conditional strengthening is therefore valid.

## 13. Positive-type homogeneous Hartree tail

Read and verified the Hartree addition to round13_general_dispersion.md. For 2<m<N and real even homogeneous K with |K|+|x||grad K|<=C|x|^-m, the virial defect after subtracting full dilation vanishes when both points are inside the core ball. Its absolute value is controlled by the Riesz pair density because f_R-id has a uniform Lipschitz constant.

If one point is outside R and the other inside R/2, separation gives CR^-m M². Otherwise both points are outside R/2, so their contribution is bounded by the Riesz Hartree form of an exterior cutoff field. HLS and energy interpolation give that form <=C M(cutoff u) A(cutoff u), yielding C mu(K_R+H_R+small). This is absorbable at small mass surplus and avoids a nonabsorbable one-tail square-root estimate. Pointwise positivity of K is not needed for this absolute bound; positive definiteness remains needed for the inherited sharp density geometry. No Hartree Gaussian-moment extension is asserted.

## 14. General homogeneous local/Hartree actual-time theorem

Read round13_persistent_general_section.tex in full. The unified result with alpha_m=1+m/[2(m-1)] and no global kinetic bound satisfies the stated hypotheses.

Instantaneously scaling to A=1 changes the cutoff radius to R A^(1/m). The normalized Fourier virial error therefore becomes R^-1 A^(1-1/m), and the normalized cutoff-kinetic error becomes R^-2 A^(1-2/m). Both powers lie strictly between zero and one for m>2, so their time averages are bounded by the corresponding powers of the average of A. The intrinsic-time center has speed C sqrt(d) A^((m-1)/m), and the current Young remainder is exactly C mu d^[m/(2(m-1))] A. The endpoint bound CR A^(1/m) vanishes on the previously selected endpoint sequence.

The Hartree weak splitting is also valid: with density exponent q=2N/(2N-m)>1, bounded H^(m/2) and local compactness imply |w_k|² weakly tends to zero in L^q. The cross density v conjugate(w_k) tends strongly to zero in L^q by compact-core approximation and uniform L^(2q) control. Absolute-Riesz HLS places K*|v|² in L^(q/(q-1)); thus its pairing against |w_k|² vanishes. This removes every mixed Hartree term, with no assumption of pointwise positive K. Consequently the rescaled weak-core positive-energy contradiction used for uniform physical mass tails applies unchanged.

The final corollary is recurrent kinetic amplification at arbitrarily late times for global amplitude-perturbed sharp standing waves. Its logical alternatives remain finite-time breakdown versus global motion with the stated large lower time average; it does not force global motion to be unbounded.

## 15. Removing the momentum restriction under real nondegeneracy

The additional nonzero-momentum calculation proposed by r13_center_momentum was independently verified. The exact normalized momentum is

    P/λ = -2<k,grad(Q+h)>.

Therefore the translation equation has leading term +P/(2λ), and the existing smallness estimates give

    v = (1/2)T^-1(P/λ)+O(d),
    a_t = (λ²/2)T^-1P+O(dλ³).

The preliminary modulation estimate remains valid without P=0 because |P|/λ=|P(w)|<=C epsilon. The signed center contribution now helps:

    -2a_t dot P <= -c λ²|P|²+C d²λ4.

For the exterior current remainder, splitting a_t and writing X=λ²|P|² gives

    mu λ^(8/3)|P|^(4/3)
      = (mu λ^(4/3)) X^(2/3)
      <= epsilon X+C_epsilon mu³λ4.

The other part is C mu d^(4/3)λ4. After eta->0, mu=O(d), and d² dominates d³ and d^(7/3) at small d. Since λ4 is comparable to A throughout the trapped Q component, the identical actual-time argument yields

    liminf T^-1 int A >= c_Q |E| d^-2

with NO momentum restriction, under the explicitly retained L_+ nondegeneracy of Q. At P=0 the separate stronger exponent 7/3 remains available. This extension preserves the same equation and negative-energy nearcritical class; it does not solve the general nonradial finite-time collapse question.

## 16. Final theorem-level derivation during assembly

The final integer-order common Hilbert-valued local flow in prop:r13g-local-flow was independently checked. For m=2k, integer k>=2 and N<=3, alpha=4k/N>k guarantees F(Z)=||Z||^alpha Z is real Frechet C^(k+1), with operator derivative bounds independent of internal dimension. Integer Sobolev products and H^k embedding therefore give local Lipschitz continuity H^k(H)->H^k(H). The common Fourier group is unitary in that space even with real measurable 0<=b<=C(1+|xi|^(2k)).

The self-adjoint band projection creates a legitimate projected Hamiltonian evolution: restricted energy, mass and momentum are conserved; the approximation converges strongly in C_tH^k on compact lifespan intervals. Energy and momentum are continuous in H^k, so conservation passes to the limit. For b=0 the localized-virial projection error vanishes because Pi_nF(U_n)->F(U) in H^k and the fixed-radius first-order virial operator sends H^k to L². No nonhomogeneous dilation identity is silently asserted when b is present.

The same approximation proves correlation-operator conservation rigorously: on Ran Pi_n all components share the self-adjoint operator (a+b)(D)-Pi_n V_n Pi_n. Their pairwise inner products are conserved. Strong L² convergence gives trace-norm convergence of covariances by

    ||Gamma(U)-Gamma(V)||_1
       <= (||U||_2+||V||_2)||U-V||_2.

Final scope qualifications checked: the general real-phase input covers all local r>0 through transverse remainder o(||Y||Hs²), and covers Hartree through its exact density quadratic expansion. The explicit Gaussian coefficient only substitutes for it in local r>=1. Hartree must retain a STRICTLY positive-definite density form, not merely semidefinite positivity, because its phase-kernel argument uses a strictly convex density norm. The real Gaussian / scalar constant-phase deduction also retains real-even a; the complex occupation theorem alone does not need that parity, but scalar real/imaginary kinetic splitting does. These are assumptions already intended by the manuscript's model class; the authors have been asked to keep them explicit.

The final general-average theorem's physical-time subsequence, no-upper-bound mass-tail argument, and Hartree density-space splitting were rechecked without new concerns. The final nonzero-momentum modulation TeX preserves the correct signs, powers of lambda, and the stated nondegeneracy condition. No theorem-level gap was found in this final audit.

## 17. Final assembled manuscript

Read Critical_Focusing_Dynamics_20261008_R13.tex and its newly assembled round13_scalar_foundation.tex and round13_polarization_foundation.tex, including the explicit real-Hilbert appendix. The new appendix correctly proves the real analogue needed for every local r>0 and for the strictly positive-definite Hartree form, rather than treating the complex one-component assertion as useful phase control.

The center section now imports the proved general Fourier exterior estimate instead of the earlier exact quartic Hessian formula. Its additional R^-1 A^(3/4) error is harmless: Jensen controls its actual-time average by R^-1 L^(3/4), which vanishes at the prescribed final radius limit. The 7/3 and arbitrary-momentum 2 exponents are unchanged.

The abstract and scope paragraph retain the correct qualifications: explicit solution class for general symbols, concrete local flow for integer orders in N<=3, real-sector nondegeneracy only for the stronger modulation result, local-only Gaussian projection, no optimal higher-rank coefficient claim, no established originality priority, and no universal nonradial finite-time blowup assertion. No additional substantive proof gap was identified in the assembled manuscript.
