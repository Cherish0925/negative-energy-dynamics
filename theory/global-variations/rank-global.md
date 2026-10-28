# Rank-changing variations and the unresolved global-rank step

Date: 2026-10-16. This investigation produces no new universal rank bound and does not exclude a violating optimizer. Its definite conclusions are the exact addition formula below and the failure of the proposed generic two-dimensional counting shortcut. The finite-rank reduction itself is already in R26.

## 1. Precisely when spectral completeness follows

Use the R26 normalization

$$
 C_N=\sup_{\operatorname{rank}P\le N}\frac{F(P)}{T(P)},\qquad
 F(P)=\int\rho_P^2,
 \quad H=-\Delta-\frac{2\rho_P}{C_N}.
$$

Let a rank-$N$ projection $P$ attain $C=C_N$. For any unit $\chi\in H^1\cap\operatorname{Ran}(P)^\perp$, set $P_+=P+|\chi\rangle\langle\chi|$. Direct expansion, without a perturbation approximation, gives

$$
 \boxed{CT(P_+)-F(P_+)
 =C\langle\chi,H\chi\rangle-\int|\chi|^4.}
 \tag{1}
$$

In particular, if $H\chi=-e\chi$, $e\ge0$, then

$$
 \frac{F(P_+)}{T(P_+)}-C
 =\frac{Ce+\|\chi\|_4^4}{T(P)+\|\nabla\chi\|_2^2}>0.
 \tag{2}
$$

The case $e=0$ here requires an actual $L^2$ eigenfunction in $H^1$; (2) makes no assertion about a bounded zero-energy resonance.

Consequently, **if $C_{N+1}=C_N$**, every such rank-$N$ optimizer occupies its complete negative spectrum and has no unoccupied zero eigenfunction. In particular this holds for a finite-rank optimizer of $C_\infty$, if one exists. The stronger complement inequality is then

$$
 C\langle\chi,H\chi\rangle\ge\|\chi\|_4^4
 \qquad(\|\chi\|_2=1,\ \chi\perp\operatorname{Ran}P).
 \tag{3}
$$

For a first violating rank, the hypothesis $C_{N+1}=C_N$ is unavailable. An unused negative state implies $C_{N+1}>C_N$, entirely consistently with first-rank minimality. Passing to the full negative projection and optimizing again can increase the rank repeatedly. Finiteness of the negative spectrum at each individual step supplies no bound on the number of steps. Neither (1) nor scalar Townes sharpness makes that iteration terminate.

## 2. Why exponential decay and a mass bound cannot replace the missing step

There is no function of the potential mass alone bounding the number of negative eigenvalues in two dimensions, even among nonnegative smooth compactly supported potentials. Here is a direct proof pertinent to the proposed rank count.

Fix $m>0$ and an arbitrary integer $K$. Choose $w\ge0$ smooth, supported in the unit disk, with $\int w=m/K$. Let $\eta_R$ equal one in that disk, equal $\log(R/|x|)/\log R$ for $1<|x|<R$, and zero outside. Then

$$
 \int|\nabla\eta_R|^2=\frac{2\pi}{\log R},\qquad
 \int w\eta_R^2=\frac mK.
$$

Choose $\log R>2\pi K/m$ and translate $K$ copies of both $w$ and $\eta_R$ so that the trial supports are disjoint. The resulting potential has mass $m$; its quadratic form is strictly negative on the $K$-dimensional span of the trials. Thus it has at least $K$ negative eigenvalues. It is smooth and compactly supported, hence exponentially decaying. The trials belong to $H^1$; their corner points cause no difficulty for the quadratic-form min–max principle.

Two-dimensional scaling $V_\lambda(x)=\lambda^2V(\lambda x)$ preserves $\int V$ and the eigenvalue count, while $\int V_\lambda^2=\lambda^2\int V^2$. One can therefore additionally impose $\int V^2=1$. This proves that qualitative exponential decay, potential mass, and this normalization still give no uniform count. The construction is not self-consistent and does not disprove a count restricted to actual optimizers; it pinpoints where their nonlinear structure would have to enter.

For an optimizer, $V=a\rho$ gives $\int V=aN$, with $a=2/C_N$. A semiclassical replacement $N_-(H)\lesssim\int V/(4\pi)$ with a uniform sublinear error cannot simply be assumed. R24 already supplies another obstruction to this shortcut through separated Townes wells. Qualitative compactness at each fixed first-violating rank does not become uniform as that rank varies and its excess over $C_1$ tends to zero.

## 3. The recent finite-rank theorem does not supply the endpoint estimate

The exact relevant hypotheses in Duong–Le–Nam–Nguyen, arXiv:2510.24148, Theorem 2.1, are

$$
 0<s\le1,\qquad s<d/2,\qquad
 q\in\left(1+\frac{2s}{d},\frac{d}{d-2s}\right).
$$

Its Lemma 3.6 proves a uniform rank bound using the CLR estimate and interpolation with an exponent strictly smaller than one. Our $(d,s,q)=(2,1,2)$ violates both strict endpoint restrictions. Substitution into its interpolation calculation gives

$$
 \frac{\frac d{2s}(q-1)-\alpha}{1-\alpha}=1
 \qquad(0<\alpha<1),
$$

which is not in the required density-exponent interval above $2$. Independently, the two-dimensional mass-only CLR estimate is false by Section 2. Thus this is an actual failure of the proof mechanism, not a parameter omitted from the theorem's statement.

FGL's finite-cutoff optimizer theorem does apply here. Its strict-doubling/nonattainment theorem instead requires $\gamma>\max(0,2-d/2)$, hence $\gamma>1$ when $d=2$. It provides no strict-doubling or global nonattainment statement at $\gamma=1$.

Primary sources checked:

- Frank–Gontier–Lewin, *Optimizers for the finite-rank Lieb–Thirring inequality*, Theorem 3 and Theorem 4, condition (17): https://arxiv.org/html/2109.05984v2 .
- Duong–Le–Nam–Nguyen, *Finite-Rank Optimizers for the mass–supercritical Lieb–Thirring and Hardy–Lieb–Thirring Inequalities*, Theorem 2.1 (printed p. 4), Lemma 3.6 (printed p. 12): https://arxiv.org/pdf/2510.24148 .

## 4. Outcome

No global-rank advance is established here. A complete negative spectral projection follows from a one-rank plateau or finite-rank global attainment, neither of which follows from first violating rank. A uniform rank bound would require a genuinely optimizer-specific estimate controlling the iteration or preventing fragmentation and increasingly weak occupied levels uniformly in rank. Scalar Townes sharpness, the existing deletion identities, and qualitative exponential decay do not provide that estimate. The unresolved step is retained explicitly; it is not replaced by an assumption of spectral completeness.
