# Independent check: linear growth of the excited-wave center group

2026-10-18. This note checks the linear input needed to glue a negative-energy traveling wave to an outgoing small radiation packet. It does not by itself construct the nonlinear solution.

## Inputs actually read

`first_class_push/old_dynamics_reference.json`, the complete `BNLS_Dynamics_20261007.pdf`, Sections 2–5, gives for sufficiently small fixed nonzero velocity:

- The self-adjoint real Hessian L_v has negative index 36 and kernel dimension 5, consisting exactly of phase and translations. The explicit preconditioned separation is >1/30 on nonzero spectrum for |v|<=10^-6.
- The 5 by 5 parameter Hessian d''(omega,v) is positive definite for sufficiently small nonzero v; the radius of this last conclusion is not numerically quantified.
- With A_v=J L_v, J=-i, the generalized zero eigenspace consists of five chains of length exactly two. The Hessian on the five generalized vectors is -d'', hence has negative index 5.
- That particular PDF proves only dim_R E^u in {29,31}, and explicitly identifies the remaining radial complex quartet as then unverified.

Therefore the subsequent exact quartet certificate is a necessary separate input if the new proof uses the stronger center bound below. Merely citing this older PDF or its arbitrary polynomial trichotomy is insufficient.

That later input has now also been independently read: `mainline_review/early_bnls/BNLS_Zero_Momentum_and_Three_Dimensions_20261007.txt`, Section 6 (text lines 467 onward). It certifies exactly one simple radial eigenvalue in 1.5<Re lambda<4.5, 4.5<Im lambda<7.5 by finite/infinite Schur reduction and interval contour inversion. The full certified inequality is <0.365771<1. Its quartet contributes two real unstable dimensions; persistence for sufficiently small traveling speed plus the previous 29 and upper bound 31 gives the exact count 31. The velocity threshold remains existential. Thus the linear proposition's needed inputs are present in the existing project proof chain; these certificates were read, not numerically rerun in this check.

## Conditional proposition with all required inputs

Assume the later certificate establishes dim_R E^u=dim_R E^s=31. For the fixed small nonzero wave, let P_c be the spectral/trichotomy projection complementary to its stable and unstable generalized root spaces. Then

\[
 \|e^{tA_v}P_c\|_{H^{10}\to H^{10}}
 \le C_v(1+|t|),\qquad t\in\mathbb R.
\]

More precisely, after removing the generalized zero eigenspace, the remaining center group is uniformly bounded in H^{10}.

### Proof

1. **Hyperbolic signature.** Hamiltonian symmetry and nondegeneracy of the L pairing between stable and unstable root spaces make the Hessian on E^s direct-sum E^u nondegenerate of signature (31,31). This follows also from the finite-dimensional Hamiltonian decomposition underlying the index theorem. It accounts for 31 negative directions. Possible Jordan blocks in the hyperbolic spectrum do not change the inertia statement.

2. **Zero block.** The generalized zero block E^0 has dimension 10, with five true kernel vectors e_alpha and five generalized vectors zeta_alpha satisfying A zeta_alpha=e_alpha and A e_alpha=0. The matrix <L zeta_alpha,zeta_beta>=-d'' is negative definite. The block is symplectically nondegenerate because d'' is invertible. The flow on it is I+tA and hence has at most linear growth in every Sobolev norm of its smooth basis.

3. **Positive invariant complement.** Take the symplectic complement of E^s direct-sum E^u direct-sum E^0, denoted X_+. The Hamiltonian decomposition makes it closed and A-invariant, with all cross L pairings zero. The 31+5 negative directions already exhaust n(L)=36. Thus the quadratic form on X_+ is nonnegative. Its null space is zero: if q in X_+ has <Lq,q>=0, nonnegativity polarizes to <Lq,h>=0 for every h in X_+; the already established cross-pairings then give Lq=0 on the whole space. But X_+ intersects the full generalized zero space trivially.

4. **Uniform energy-space coercivity.** The free Hessian has Fourier eigenvalues |xi|^4+1 plus or minus v·xi. For sufficiently small fixed v their infimum is positive, and their growth is equivalent to 1+|xi|^4. The profile-dependent coefficients decay, so the potential perturbation is form-compact from H^2 to H^-2. Positivity on the finite-codimensional complement, no null vector, and this positive essential gap imply

\[
 c_v\|q\|_{H^2}^2\le\langle Lq,q\rangle
 \le C_v\|q\|_{H^2}^2,\qquad q\in X_+.
\]

The standard contradiction proof normalizes the H^2 norm, extracts a weak limit, uses compactness of the negative potential, and obtains a nonzero null vector if the lower bound fails. Since L energy is conserved by e^{tJL}, the group on X_+ is uniformly bounded on H^2 for both signs of t.

5. **H^{10} lifting without a dispersive estimate.** The real operator A is elliptic of order four with constant leading part J Delta^2 and smooth bounded lower-order coefficients. Its square is elliptic of order eight, with leading part -Delta^4. Elliptic graph-norm equivalence gives

\[
 \|q\|_{H^{10}}\asymp_v
 \|q\|_{H^2}+\|A^2q\|_{H^2}.
\]

The invariant projections commute with A and preserve its graph domains; their finite-dimensional complements have smooth eigenvectors and dual eigenvectors. A^2 commutes with the group. Applying the H^2 bound to q and A^2q gives a uniform H^{10} bound on X_+. Adding the zero block yields the displayed linear bound. No absence of positive-energy embedded eigenvalues or threshold resonances is required for this energy estimate.

All constants may deteriorate as v tends to zero. The proposition fixes a nonzero v first and makes no uniform-in-v claim.

## Why the exact growth degree matters

A center Green kernel bounded by C(1+|t-s|)^K maps a forcing O(t^-q) to O(t^{K+1-q}) when q>K+1. A freely dispersing four-dimensional packet with nondegenerate frequency support has |z|=O(t^-2). Its coefficient |z|^2 h is O(t^-4 h), so this term improves the weighted norm only when K<3. Increasing the order of an approximate-radiation residual does not repair K>=3 for this linear-in-h term. Thus establishing K=1 (or projecting out the zero block and controlling its modulation separately) is a substantive necessary step, and the argument above supplies it once the 31-dimensional instability certificate is explicitly present.

## Independent WKB and nonlinear check of wave_radiation.md

The complete draft `first_class_push/wave_radiation.md` was then read and recomputed. No consequential gap was found in the following finite-regularity construction.

1. For r=t^-2 exp(i t Phi(x/t)) A(t,x/t), with grad_y Phi=xi and y=4|xi|^2xi, conjugating -Delta_x gives B0+t^-1 B1+t^-2 B2 with exactly the draft's B_j. Squaring correctly gives the four operators displayed there. The transport identity B0B1+B1B0=-i(y·grad_y+2) follows from div_y y=4 and cancels the t^-2-prefactor and x/t transport in i partial_t.

2. The resulting amplitude equation is i A_t-t^-2 L2 A-t^-3 L3 A-t^-4 L4 A+t^-4|A|^2A=0. At power t^-n-1 the coefficient indices are n-1, n-2, n-3, and the cubic index sum n-3. Thus each A_n is determined algebraically by division by -in, with no integration in y and no spreading of compact support.

3. After including A_0 through A_J the first unremoved amplitude term is t^-J-2. Physical t^-2 amplitude and the four-dimensional L^2 volume factor t^2 cancel. Bounded phase frequencies and smooth compact amplitudes give the same residual decay in every fixed Sobolev order. The N=4 stationary-phase factor is exp(-i pi N/4)=-1, so the stated A_0 has the correct sign and normalization for a unitary Fourier transform.

4. The velocity support remains in |x|<vt/2 for the approximate radiation; only this approximate field is assigned compact velocity support. The exponentially localized core is vt away, so core/radiation mixed terms decay exponentially in any fixed Sobolev norm. No unsupported nonlinear Fourier-support invariance is used.

5. In H^10, radiation-squared times h has coefficient O(t^-4) in W^{10,infinity}; quadratic and cubic h remainders obey the stated algebra estimates. The center Green operator loses two temporal powers, so the residual t^-J-2 gives h=O(t^-J). On the weighted ball, the radiation-linear term gains T^-2 and the core-quadratic term gains T^{2-J}. J>=3 and sufficiently large T close the contraction even if the constants depend badly on v.

6. The mild correction satisfies the exact semilinear equation, and H^10 local uniqueness/continuation gives a strong forward-global H^10 solution. Strong asymptotic additivity in H^2 determines M, P and E exactly; no finite-time invariant tuning is needed.

Two presentational fixes were sent to the author: state H^10 rather than automatically claiming smoothness, and account for phase/position shifts when replacing t>=T by t>=0. An explicit normalization is u_tilde(t,x)=exp(-iT)u(t+T,x+vT), with the corresponding radiative scattering state exp(-iT)[exp(-iT Delta^2)r_+](x+vT). This preserves all three conserved quantities and the Fourier support.
