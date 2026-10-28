# Independent audit of the traveling-wave threshold compactification

Audited source: `round10_travel_threshold.md`, including its branch identity, on 2026-10-08. This audit treats the sharp critical GN inequality and the previously proved weak-profile cutoff Pohozaev identities as established inputs. It does not audit the separate computer-assisted construction used to make the negative-energy traveler set nonempty.

## Verdict

The compactification theorem and the fixed-frequency branch mass identity are mathematically sound under the stated assumptions. I found no missing coercivity assumption on the full traveling symbol. In particular, diffuse mass at a possible linear resonance when the limiting frequency is nonpositive does **not** invalidate the proof: the negative-energy case eliminates all other mass before using momentum continuity, while the zero-energy case has strictly positive limiting frequency and eliminates diffuse mass by summing exact profile identities.

The result is a static necessary compactification statement. It neither proves strict-negative-energy attainment of the threshold nor asserts that every listed zero-energy configuration is realizable by a sequence of exact traveling waves. No unrestricted dynamical blowup or soliton-resolution consequence follows from it.

## 1. Moment-free velocity identity

For the action

\[
S_{\omega,v}(U)=E(U)+\frac\omega2M(U)-\frac12v\cdot P(U),
\]

the bounded cutoff phase variation \(e^{i\theta\chi_R}U\), with \(\chi_R(x)=R\chi(x/R)\) and \(\chi=x_j\) near zero, is differentiable in \(H^s\) for each fixed \(R\). Every nonlinear and frequency term has zero real pairing with \(i\chi_RU\). The exact identity is

\[
2\operatorname{Re}\langle a(D)U,i\chi_RU\rangle
=\int (v\cdot\nabla\chi_R)|U|^2.
\]

The factor of two is correct: the action contains \(A/2\) and \(-v\cdot P/2\).

For the commutator, set \(\delta=\xi-\eta\). Homogeneity with \(m>1\) gives

\[
|a(\xi)-a(\eta)|\le C|\delta|(|\xi|+|\eta|)^{m-1}.
\]

After division by \(\langle\xi\rangle^s\langle\eta\rangle^s\), the source's upper bound \(C|\delta|\langle\delta\rangle^s\) is valid. In the comparable-frequency region the ratio is bounded, since \(m-1-2s=-1\); in the noncomparable region the large frequency is controlled by \(|\delta|\), and \(m-1-s=s-1\le s\). The resulting Schur/Young kernel has uniformly bounded \(L^1\) norm because

\[
\int R^{N+1}|\widehat\chi(R\delta)|\,|\delta|\langle\delta\rangle^s\,d\delta
=\int |\widehat\chi(q)|\,|q|\langle q/R\rangle^s\,dq\le C.
\]

For Schwartz data, \(\chi_RU\to x_jU\) in \(L^2\) and the Fourier differentiation calculation gives the limit \(\int\partial_j a\,|\widehat U|^2\). Density plus the uniform form bound extends the limit to every \(H^s\) profile. The limiting quadratic form is continuous on \(H^s\), since \(|\partial_ja(\xi)|\lesssim |\xi|^{m-1}\lesssim1+a(\xi)\). Thus

\[
vM(U)=\int\nabla a(\xi)|\widehat U(\xi)|^2\,d\xi
\]

holds without a spatial moment, and the stated velocity bound follows by Hölder. Direct differentiation of the unbounded phase \(e^{i\theta x_j}U\) would be unjustified for general \(H^s\) data, but the source explicitly avoids that error.

## 2. Parameter compactness and profiles

The scaling laws are correct:

\[
U_\lambda=\lambda^{N/2}U(\lambda x),\qquad
(\omega_\lambda,v_\lambda)=(\lambda^m\omega,\lambda^{m-1}v).
\]

At \(A(U_n)=1\), bounded positive mass and the preceding velocity identity bound \(v_n\); GN bounds \(E_n\); and

\[
\omega_nM_n=r+(2m-p)E_n
\]

bounds \(\omega_n\). There is no division by \(\omega_n\), hence no hidden sign assumption in this step.

The required translation-only profile decomposition is available because

\[
2<p=2+2m/N<2N/(N-m)\quad(N>m),
\]

and \(p\) is finite when \(N\le m\). This is strictly subcritical for the \(H^{m/2}\) embedding. The decomposition should be stated with the iterated remainder property

\[
\lim_{J\to\infty}\limsup_{n\to\infty}\|R_n^J\|_p=0.
\]

It does not claim the remainder is small in \(H^s\) at this stage. High-frequency or dilute mass can be present in that remainder and is removed later by exact identities.

Every extracted translated weak limit is an exact profile at \((\omega_*,v_*)\): weak global \(H^s\) convergence handles the nonlocal linear operator, local strong \(L^p\) convergence handles \(|U|^{p-2}U\), and the first-order drift is bounded from \(H^s\) to \(H^{-s}\) because \(m>1\). No positivity of \(a(\xi)+\omega_*-v_*\cdot\xi\) is required.

## 3. Why a negative profile removes resonant radiation

If one extracted profile \(V\) has negative energy, its mass is at least \(M_{\mathrm{tr}}\) by the definition of the threshold. Since the total limiting mass is exactly \(M_{\mathrm{tr}}\), this consumes all mass and yields strong translated \(L^2\) convergence.

The remaining kinetic energy need not vanish from this fact alone. The essential additional step in the source is valid:

\[
\|w_n\|_p^p\le C M(w_n)^r A(w_n)\to0,
\quad
|P(w_n)|\le C M(w_n)^{1-1/m}A(w_n)^{1/m}\to0.
\]

Equivalently, strong \(L^2\) convergence and bounded \(H^s\) norm imply strong \(H^{1/2}\) convergence because \(s>1/2\); momentum is continuous there. Thus \(P(U_n)\to P(V)\), and the exact identity \(v\cdot P=2mE\) forces \(E_n\to E(V)\). Nonlinear norm convergence then forces \(A(V)=1\), removing the kinetic remainder and giving strong \(H^s\) convergence.

This argument works even if \(\omega_*\le0\) or the limiting traveling symbol has real zeros. A separate spectral coercivity assumption would be unnecessary and would weaken the theorem.

The infinite-series energy decomposition is legitimate: both \(\sum_jA(V_j)\) and \(\sum_j\|V_j\|_p^p\) converge, hence \(\sum_j|E(V_j)|<\infty\). If \(e<0\), at least one profile has negative energy.

## 4. Zero-energy endpoint and absence of diffuse mass

If no extracted profile has negative energy, then

\[
0=e=\sum_jE(V_j)+\frac12\Bigl(1-\sum_jA(V_j)\Bigr)
\]

forces every nonzero profile to have zero energy and \(\sum_jA(V_j)=1\). GN implies \(M(V_j)\ge M_c\), so only finitely many profiles occur and \(J\le\lfloor M_{\mathrm{tr}}/M_c\rfloor\).

The limiting scalar identity gives \(\omega_*=r/M_{\mathrm{tr}}>0\). Applying the exact scalar Pohozaev identity to each zero-energy profile gives \(\omega_*M(V_j)=rA(V_j)\). Summation then gives

\[
\omega_*\sum_jM(V_j)=r=\omega_*M_{\mathrm{tr}},
\]

which removes all diffuse mass. Together with the kinetic equality this proves the advertised strong \(H^s\) decomposition. This is stronger than a generic bounded-sequence profile decomposition and is the substantive closure in the argument.

## 5. Branch identity

At fixed \(\omega>0\), write \(\Pi(z)=e\cdot P(U_z)\). Criticality of the action gives

\[
E'(z)+\frac\omega2M'(z)-\frac z2\Pi'(z)=0.
\]

Substitution of \(E(z)=z\Pi(z)/(2m)\) yields exactly

\[
\omega M'(z)=\frac{(m-1)z\Pi'(z)-\Pi(z)}m.
\]

For a \(C^2\) branch through real \(Q\), \(\Pi(0)=0\), and with \(\kappa=\Pi'(0)\),

\[
E(U_z)=\frac\kappa{2m}z^2+o(z^2),\qquad
M(U_z)=M(Q)+\frac{(m-2)\kappa}{2m\omega}z^2+o(z^2).
\]

The claimed quartic-order remainders require the separately stated analytic/parity branch symmetry; they do not follow from \(C^2\) alone. The source makes this distinction correctly. Negative inertia for \(m>2\) strictly lowers the mass along the branch, hence gives \(M_{\mathrm{tr}}<M(Q)\).

## Recommended strongest accurate statement

For every fixed real-even positive elliptic homogeneous symbol of order \(m>1\), assuming the negative-energy exact traveler class is nonempty and the stated weak-profile identities, every sequence approaching its least mass is compact after kinetic normalization and translation, **except possibly for a finite collection of separated zero-energy exact profiles at common limiting parameters**. Such a configuration exhausts both mass and kinetic energy. In particular, normalized energy bounded away from zero implies negative-energy attainment; mass below \(2M_c\) implies single-profile compactness but does not decide whether the limiting energy is negative or zero.

Suggested editorial clarifications only: state the iterated profile-remainder limit explicitly; call the zero-energy alternative a necessary endpoint configuration, not an existence construction; and keep the nonemptiness input separate from this proof. No mathematical repair to the main argument is required.

## Additional independent audit: lower-threshold selection and Gamma limit

I also audited Sections 4–5 of `round10_symbol_thresholds.md`. The constants, normalization, scale bounds, liminf argument, and recovery sequence are correct. No uniform higher Fourier moment of the varying minimizers is needed.

The essential order of proof is sound: GN compactness gives normalized \(V_M\to Q\) in \(H^s\); positivity of the correction and one fixed Fourier annulus force \(\lambda_M\to0\); annular convergence then gives

\[
\liminf D_{\lambda_M}(V_M)\ge C_*(Q)\ge C_{\min}>0.
\]

Negativity gives \(\lambda_M^qD_{\lambda_M}(V_M)<d\), hence the upper scale bound. A fixed finite-moment selected optimizer supplies the negative trial energy, and \(I(M)\ge-\alpha d\lambda_M^m/2\) supplies the lower scale bound. Only after both scale bounds are obtained does one infer boundedness of the scalar rescaled correction. Thus there is no circular use of a higher-moment bound.

The annular argument remains valid if \(C_*(Q)=\infty\): exhausting annuli then forces an infinite liminf. Along actual minimizers this is excluded by the scalar correction bound. Recovery uses a *fixed* finite-moment optimizer and the valid global majorant \(b(\lambda\xi)/\lambda^{m+q}\le C|\xi|^{m+q}\).

The strong-topology Gamma limit also handles the mass constraint: if a strong \(H^s\) limit has mass different from \(M_0\), there is no subsequence of finite-energy admissible terms. On mass \(M_0\), \(E_0\ge0\), so the discarded \(E_0/d\) term cannot spoil the liminf. Equicoercivity is deliberately not asserted and is not needed for the separate minimizer compactness argument.

One wording should be made explicit: the minimizers of the Gamma-limit functional are the *optimally dilated* selected optimizers,

\[
\operatorname*{argmin}F_0
=\{\beta_*^{N/2}Q(\beta_*\,\cdot): Q\in\mathcal G_{\mathrm{select}}\},
\]

including translations and constant phases. The normalized profiles \(V_M\) converge to \(\mathcal G_{\mathrm{select}}\), whereas the profiles on the fixed \(d^{1/q}\) scale converge to this dilated set. The final sentence of Section 5 should not be read as identifying \(\mathcal G_{\mathrm{select}}\) itself with \(\arg\min F_0\) unless \(\beta_*=1\).

The next normalized frequency coefficient also checks algebraically: \(r m/(m+q)+p q/[2(m+q)]=r+q/(m+q)\). No additional dispersion expansion is silently used for that coefficient.
