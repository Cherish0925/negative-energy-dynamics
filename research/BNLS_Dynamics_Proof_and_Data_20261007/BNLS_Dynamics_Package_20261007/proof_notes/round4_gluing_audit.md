# Independent audit of the zero-momentum gluing argument

Date: 7 October 2026. Reviewed files: `round4_zero_momentum_gluing.md`, `round4_stable_manifold.md`, and the analytic deductions in `round4_stability_theory.md`.

## Verdict and scope

The proposed two-wave theorem is a credible conditional theorem under the stated spectral-coercive splitting (SC), interpreted with smooth exponentially localized primal and dual mode functions. I found no fatal derivative-loss or moving-projection error. The proof needs the identities and domain explanations below made explicit; they follow from SC and do not require an extra large-velocity assumption.

The theorem is not yet an unconditional zero-momentum counterexample for the constructed wave. Its substantive additional premise is the existence of an invariant finite-dimensional space containing every failure of coercivity, with localized dual modes and a coercive invariant complement. The known finite Morse count, Hamiltonian trichotomy, and at least 29 unstable directions do not alone supply that premise. A possible remaining nonpositive-energy imaginary spectral component is exactly where further analysis is needed.

## 1. Moving projections: the algebra closes

Write \(A=\mathcal A(t)\), \(Z=Z(t)\), \(W=W(t)\), \(E=\mathcal E_W(t)\), and \(B=B_0\). The constructed analysis and synthesis maps satisfy

\[
WZ=I,\qquad W_t+WA-BW=E.
\]

For \(C=A-ZE\), one has the exact identity

\[
W_t+WC=BW.
\]

Thus a solution of \(w_t=Cw\) with \(W(s)w(s)=0\) stays in \(\ker W(t)\). No term of order \(v\), rather than exponentially small order, has been omitted: translation of the analysis map is canceled by the \(iv\partial_1\) term in the single-wave action Hessian.

The transformed two-wave equations are also genuinely exponentially coupled. If

\[
E_Z=Z_t+ZB-AZ,
\]

then differentiation of \(WZ=I\) gives \(WE_Z+EZ=0\). For \(h=Za+w\), the exact equations are

\[
a'=Ba+EZa+Ew,
\qquad
w'=Cw-E_Za-ZEZa.
\]

The source in the second equation lies in \(\ker W(t)\), since \(W(-E_Z-ZEZ)=0\). This matters for using the projected propagator in the Green operator.

## 2. Coercivity of the localized action

Let \(W_j^{\rm raw}\) be the separately translated dual maps before Gram correction. Since the finite Gram correction is invertible, \(Ww=0\) is equivalent to \(W_j^{\rm raw}w=0\) for both cores.

Take cutoffs \(\chi_j\) equal to one in neighborhoods of their centers of radius comparable to \(vt\), and an exterior cutoff, with the squares summing to one. Exponential localization of the dual modes gives

\[
|W_j^{\rm raw}(\chi_jw)|
=|W_j^{\rm raw}((\chi_j-1)w)|
\le C e^{-\kappa t}\|w\|_{H^2}.
\]

SC extends to the approximate-constraint bound

\[
\langle L_vf,f\rangle
\ge c_1\|f\|_{H^2}^2-C_1|Wf|^2.
\]

Indeed split \(f=(I-ZW)f+ZWf\), use SC on the first summand, and absorb the cross term by Young's inequality. This proves core coercivity after localization. The exterior free form is coercive because \(|b|\le v<1/2\), while all profile potentials there are exponentially small. The fourth-order partition errors are bounded by \(C_v t^{-1}\|w\|_{H^2}^2\) (with sharper powers available). Therefore the stated uniform positive localized action on \(\ker W(t)\) follows.

No orthogonality of the Gram-corrected projection with respect to the energy form is needed for this argument.

## 3. The real-linear conjugation term does not spoil the action identity

The potential contains conjugation, so one must not assume that \(J=-i\) commutes with \(\mathcal L\). Fortunately the claimed identity does not require that. Since \(D_b\) is a real differential operator, it commutes with \(J\). With

\[
H=\mathcal L-JD_b,\qquad A=J\mathcal L,
\]

and real \(L^2\) adjoints, direct multiplication gives

\[
A^*H+HA=D_b\mathcal L-\mathcal L D_b.
\]

This proves the displayed quadratic-action derivative even for the real-linear potential. Also \([D_b,\mathcal V]=b\partial_1\mathcal V\); the divergence correction commutes with multiplication and conjugation. The profile transport cancels the potential time derivative in each core. What remains is an \(O_v(t^{-1})\) quadratic form plus exponentially small errors.

The commutator with \(\Delta^2\) loses no derivatives at the form level. In

\[
-2\operatorname{Re}\langle\Delta h,\Delta D_bh\rangle,
\]

the \(D_b\Delta h\) term vanishes by skew-adjointness, and the remaining terms have at most two derivatives on \(h\) and three on \(b\). Smooth compact approximation justifies this identity on \(H^2\).

For the finite-rank correction \(-ZE\), its range is smooth and \(E\) is exponentially small on \(H^2\); the action derivative contribution is exponentially bounded by \(\|w\|_{H^2}^2\). This yields the forward and backward polynomial estimates.

## 4. The H6 upgrade: two identities should be stated

Put \(\Pi=I-ZW\) and \(D=\Pi A\Pi\), with domain \(H^6\) in \(H^2\). The relevant expansion is

\[
D=A+F,\qquad
F=-ZWA-AZW+ZWAZW.
\]

Here \(WA\), initially defined on the generator domain, extends to a bounded functional on \(H^2\). This follows either from the moving-intertwining identity or by applying the adjoint differential operator to the smooth dual mode functions. Every term in \(F\) therefore is a bounded smoothing finite-rank operator. The same is true of \(C-A\).

There is consequently a uniform elliptic graph norm equivalence

\[
\|w\|_{H^6}\asymp\|w\|_{H^2}+\|Dw\|_{H^2}.
\]

For \(z=Dw\),

\[
z'=Cz+Kw,\qquad K=D_t+[D,C].
\]

The important checks are:

* \(K:H^2\to H^2\) is bounded uniformly in large time. Indeed \(D_t=A_t+F_t\), where \(A_t\) is a smooth bounded multiplication operator, and
  \([D,C]=[A,C-A]+[F,A]+[F,C-A]\) consists of smoothing finite-rank terms. Products involving \(A\) on a dual functional are justified by the adjoint generator acting on its smooth dual mode. Enough regularity for two generators is needed here; the assumption of all exponentially localized derivatives is sufficient.
* The forcing remains in the center bundle. From \(WD=0\) and \(WC=BW-W_t\),
  \[
  W K=W D_t+W[D,C]=-W_tD+W_tD=0.
  \]
  Thus using the center propagator for this inhomogeneous equation is legitimate.

For \(t\ge s\), the two H2 propagator factors in Duhamel multiply as

\[
(t/\tau)^K(\tau/s)^K=(t/s)^K.
\]

The same cancellation holds in the reversed-time case. Therefore one gains only a factor \(1+|t-s|\), and the asserted H6 exponent \(K+1\) is justified. Even a coarser polynomial exponent would suffice for the subsequent exponential-weight fixed point.

The argument should first be performed for smooth data, using the ordinary nonautonomous smooth-potential flow, then extended to H6 and H2 by density and the uniform bounds. This is a proof detail, not an additional spectral assumption.

## 5. Green operator and nonlinear fixed point

The forward integral on stable directions and backward integral on unstable directions are correctly oriented. The exponential weight can be chosen smaller than both the interaction exponent and the least positive hyperbolic rate. Thus arbitrarily small but nonzero relative velocity does not cause a contradiction in the construction: the constants grow and the required starting separation becomes large.

The center and imaginary finite-dimensional blocks have polynomial propagator bounds. Their terminal integrals converge against exponential forcing. The off-diagonal couplings are exponentially small bounded operators on H6 because the modes and dual modes are smooth. A Neumann series and then a cubic H6 contraction are legitimate.

Reflection averaging of a bounded right inverse preserves the right-inverse property on the even subspace, because the full two-wave linear operator commutes with inversion. It is unnecessary for the original spectral coordinates to be chosen equivariantly. The fixed point can therefore be even. Its exact zero momentum follows from symmetry, and its exact negative energy follows from conservation and H2 asymptotic additivity.

## 6. What has and has not been supplied for the particular wave

The following are not interchangeable:

1. A finite-index Hessian with a coercive positive subspace.
2. A Hamiltonian exponential trichotomy with a polynomially bounded center.
3. SC: a finite localized invariant subspace with a coercive invariant complement and localized dual modes.

The established static spectra and Lin–Zeng theorem provide the first two. The localized moving-energy proof uses the third. In particular an upper-triangular center decomposition, or a finite-dimensional embedded neutral component coupled to continuous spectrum, cannot simply be relabeled as the exact invariant splitting in SC.

For the current wave the remaining index difference allows a nonpositive-energy imaginary component. Its spectral location, root structure, localization, and whether it splits off with a coercive invariant complement must be established, or a different gluing proof must handle the coupling explicitly. The conditional theorem is useful because this is now a precise single-wave obligation. It is not the completion of that obligation.

Smooth exponential localization of the profiles is another theorem premise. The earlier H4 and polynomial-moment arguments alone do not literally state it. It can plausibly be proved by a weighted elliptic estimate for the positive free traveling symbol and bootstrap, but that lemma should be supplied rather than replacing polynomial moments by an exponential assertion.

## 7. Secondary check: the single-wave strong stable family

The Lyapunov–Perron construction in `round4_stable_manifold.md` does not require SC. The weaker Hamiltonian trichotomy suffices, because the center propagator is stationary and already polynomially bounded. Its graph-domain upgrade, weighted nonlinear estimates, analytic graph construction, and exact conserved-charge identities are consistent.

The claimed parameter dimension remains dependent on the separate full Morse and Hamiltonian index calculation. Conditional on those inputs, I found no new gap in passing from linear trichotomy to the exact nonstationary, forward-global, negative-energy strong stable family.

Primary source independently checked for the distinction between trichotomy and an invariant coercive decomposition: Lin–Zeng, arXiv:1703.04016v4, Theorems 2.1–2.2 and the graph-norm discussion in Section 7. The two-center and graph-forcing calculations above are independent deductions.

## 8. Closing the profile-localization premise

The missing exponential-profile statement can in fact be proved directly, without new spectral computation.

**Lemma.** Suppose \(U\in H^2(\mathbb R^4)\) solves

\[
PU=|U|^2U,\qquad P=\Delta^2+1+iv\partial_1,
\]

and \(1-3(|v|/4)^{4/3}>0\). Then there is \(a>0\) such that, for every multi-index \(\alpha\),

\[
e^{a\langle x\rangle}\partial^\alpha U\in H^4,
\qquad |\partial^\alpha U(x)|\le C_\alpha e^{-a\langle x\rangle}.
\]

**Proof.** The positive elliptic Fourier symbol gives
\(\|f\|_{H^4}\le C_P\|Pf\|_2\). The existing bootstrap gives \(U\in H^s\) for every finite \(s\), hence \(U\in C_0\) and every derivative is bounded.

Choose smooth bounded radial functions \(\phi_R\) which agree with \(\langle x\rangle\) on expanding balls, obey \(0\le\phi_R\le C\langle x\rangle\), and have uniformly bounded derivatives through every fixed order. They can be obtained as \(R\theta(\langle x\rangle/R)\), where \(\theta(s)=s\) for \(s\le1\) and is constant for \(s\ge3\). Put \(w_R=e^{a\phi_R}\), \(z_R=w_RU\). For each finite \(R\), these are legitimate bounded smooth multipliers of H4.

The commutator \([P,w_R]w_R^{-1}\) has order at most three, with coefficients bounded by \(C a\) independently of \(R\), for \(0<a\le1\). This follows from the derivative bounds for \(\phi_R\) and the formulas for derivatives of an exponential. Therefore

\[
\|z_R\|_{H^4}
\le C_P\||U|^2z_R\|_2+C_P C a\|z_R\|_{H^3}.
\]

Choose \(a\) so the final coefficient is at most \(1/4\). Then choose a fixed ball outside which \(C_P|U|^2\le1/4\). On that ball \(w_R\) is bounded independently of \(R\), while outside it the potential term is absorbed. This gives a uniform H4 bound for \(z_R\). Weak compactness and the local identity \(\phi_R=\langle x\rangle\) for large \(R\) imply \(e^{a\langle x\rangle}U\in H^4\).

For higher derivatives, differentiate the equation. The top-order nonlinear terms are

\[
2|U|^2\partial^\alpha U+U^2\overline{\partial^\alpha U},
\]

and every other product uses derivatives of U of strictly lower order. By induction these lower products have an exponentially weighted L2 bound: put the weight on one differentiated factor, and use the unweighted boundedness of the others. Apply the same truncated-weight estimate to \(\partial^\alpha U\), absorbing the top terms outside a fixed ball where \(3C_P|U|^2\le1/4\). The same small \(a\) works for every fixed order; constants may depend on \(\alpha\). This proves all the weighted H4 bounds. Sobolev embedding H4 into L-infinity then gives the pointwise derivative estimates. \(\square\)

Thus profile localization can be removed from the list of unverified premises for the small-speed branch. Localization and invariant splitting of all relevant *Hamiltonian modes and dual modes* remain part of SC and are not proved by this profile lemma.

## 9. A sharper sufficient condition: the unstable-dimension-31 case

For this particular branch, SC follows if the remaining alternative is resolved as \(\dim_{\mathbb R}E^u=31\). This replaces a functional splitting assumption by one of the two precise spectral possibilities already identified.

**Proposition.** Assume the conclusions of the companion stability proof: \(n(L)=36\), a five-dimensional kernel, exactly five zero Jordan chains of length two with negative-definite generalized-zero form matrix, and Hamiltonian trichotomy. If \(\dim E^u=\dim E^s=31\), then the traveling profile satisfies SC.

**Proof.** Let

\[
\mathcal D=E^u\oplus E^s\oplus E_0,
\qquad \Omega(f,g)=\langle J^{-1}f,g\rangle_{L^2,\mathbb R}.
\]

The form \(L\) is nondegenerate on \(E^u\oplus E^s\), and its negative index there is 31. Since \(A\) is invertible on that space and \(\Omega(Af,g)=\langle Lf,g\rangle\), the restriction of \(\Omega\) is nondegenerate there. On \(E_0=\operatorname{span}\{e_\alpha,\eta_\alpha\}\), its cross matrix is

\[
\Omega(e_\alpha,\eta_\beta)
=\langle q_\alpha,\eta_\beta\rangle=-d''_{\alpha\beta},
\]

which is invertible. The phase-translation vectors pair to zero with one another, so this cross matrix alone proves nondegeneracy of the full zero block. Hyperbolic and zero root spaces are symplectically orthogonal, by the Hamiltonian identity and their disjoint spectra. Therefore \(\Omega|_{\mathcal D}\) is nondegenerate.

Set \(C=\mathcal D^{\perp_\Omega}\). A finite symplectic projection gives a bounded direct sum \(H^2=\mathcal D\oplus C\). Both subspaces are invariant: for \(h\in C\) and \(d\in\mathcal D\),

\[
\Omega(Ah,d)=-\Omega(h,Ad)=0.
\]

The same identity shows \(\langle Lh,d\rangle=0\), initially on the generator domain and then by density. Hence the Hessian form is block diagonal on the decomposition. Its negative index on \(\mathcal D\) is \(31+5=36\), exhausting the full negative index. Its full kernel lies inside \(\mathcal D\). Consequently it is positive on C with no zero direction. The free positive elliptic form plus the compact decaying potential has essential form spectrum bounded away from zero; finite-codimensional compression preserves this fact. Thus positivity on C is uniformly coercive in H2.

It remains to justify localized coordinate maps. Every eigenvalue in the hyperbolic spaces avoids the free imaginary spectrum, and zero lies in the free spectral gap. The corresponding free Fourier matrix resolvents are invertible from L2 to H4. Applying the truncated exponential-weight argument in Section 8 to the eigenvector equation proves exponential localization, with a rate possibly depending on the eigenvalue. For generalized eigenvectors, the previously localized member of the Jordan chain is an additional localized source; induction proves the same claim along every finite chain, reducing the common exponent if needed. Elliptic bootstrap gives all derivatives. This argument applies to the finite collection of modes in \(\mathcal D\).

The coordinate analysis map for the symplectic projection is built from the inverse finite matrix \(\Omega|_{\mathcal D}\) and functionals \(h\mapsto\Omega(h,d_j)\). Since \(J^{-1}=i\), their dual mode functions inherit the exponential localization of \(d_j\). The finite-dimensional restriction of A gives the required matrix B, and invariance gives both intertwining identities in SC. This proves SC. \(\square\)

If instead \(\dim E^u=29\), there are exactly two unaccounted negative directions in the real space. The analogous argument works if the remaining imaginary root space can be included as a finite localized invariant block on which the energy and symplectic restrictions are nondegenerate. Establishing that property, especially in an embedded case, is the remaining substantive issue. The integer alternative alone does not settle it.
