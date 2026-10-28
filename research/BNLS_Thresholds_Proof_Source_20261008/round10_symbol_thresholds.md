# Round 10: two dispersion thresholds and selection at the lower threshold

This note proves a variational theorem for a general, possibly anisotropic,
nonhomogeneous symbol. It also gives the complete constrained-energy phase
diagram for the rational interpolation considered in round 9, and a sharp
lower-threshold asymptotic that selects a subset of homogeneous GN optimizers.
The variational methods themselves are standard. No historical priority claim
is made here. None of these statements is a general dynamical blowup theorem.

## 1. Assumptions and notation

Fix N>=1, m>1, s=m/2, r=m/N, and p=2+2r. Fourier transform is unitary.
Let a_0 and a_infty be real, even, positive elliptic m-homogeneous symbols,
continuous on the sphere and C^{N+2} off the origin. Write

    A_j(f) = integral a_j(xi)|fhat(xi)|^2 dxi,
    M(f) = ||f||_2^2,   C_p(f) = ||f||_p^p,
    E_j(f) = A_j(f)/2-C_p(f)/p.

Let M_j denote the sharp GN mass:

    C_p(f)/p <= (1/2)(M(f)/M_j)^r A_j(f),  j=0,infty.

Assume a_infty-a_0 is positive elliptic of degree m. In particular
M_infty>M_0: if a_infty >= (1+eta)a_0, then
M_infty >= (1+eta)^{1/r}M_0.

The full symbol is k=a_0+b, where b is real and even, continuous off zero,
and for some q>0 and positive constants c,C satisfies

    c min(|xi|^{m+q},|xi|^m) <= b(xi) <= C min(|xi|^{m+q},|xi|^m).       (H1)

At high frequencies suppose, uniformly in theta on the sphere,

    R^{-m} k(R theta) -> a_infty(theta),   R->infty.                    (H2)

At low frequencies suppose, uniformly in theta,

    R^{-(m+q)} b(R theta) -> c_*(theta),   R->0,                        (H3)

where c_*(xi) is positive elliptic homogeneous of degree m+q. We use
`C_*(f)=integral c_*(xi)|fhat(xi)|^2` for its quadratic form. It may be
infinite on H^s. Assumptions (H1)--(H3) imply k is comparable to |xi|^m.
For profile regularity also assume the individual order-m symbol bounds

    |partial^beta k(xi)| <= C_beta |xi|^{m-|beta|},  |beta|<=N+2.

They are not needed for the variational infimum or compactness statements.

Define

    E_k(f) = (A_0(f)+B(f))/2-C_p(f)/p,
    I(M) = inf { E_k(f): f in H^s, M(f)=M },
    B(f) = integral b(xi)|fhat(xi)|^2 dxi.

The normalized equality set of the principal sharp GN inequality is

    G_0 = {Q: M(Q)=M_0, A_0(Q)=1, C_p(Q)=p/2}.

It is compact in H^s modulo spatial translation and constant phase. This is
the normalized sharp-GN compactness lemma proved in rounds 8--9. Every
complex optimizer has constant phase. No uniqueness or nondegeneracy of its
real linearized operator is assumed.

For the sharp asymptotic below require

    G_0 contains at least one Q with C_*(Q)<infty.                     (H4)

This is automatic for 0<q<=m+2 under the stated regularity of a_0: every
normalized optimizer solves a_0(D)Q+(r/M_0)Q-|Q|^{2r}Q=0 and the previously
proved individual bootstrap gives Q in H^{m+1}. The condition is stated
explicitly when q>m+2; no unproved unlimited smoothness is used.

## 2. Two thresholds for the full variational problem

**Theorem 1.** Under (H1)--(H2):

1. The sharp GN constant with full kinetic form A_k=A_0+B is the same as
   with A_0. Its critical mass is M_0, and no nonzero optimizer attains the
   full-symbol inequality.
2. For 0<M<=M_0, I(M)=0 without attainment.
3. For M_0<M<M_infty, -infty<I(M)<0 and every minimizing sequence is
   precompact in H^s modulo translation and subsequence. In particular it
   has a minimizer. A real minimizer can be chosen.
4. For M>M_infty, I(M)=-infty.

Thus the two sharp homogeneous GN masses, rather than a pointwise
coefficient comparison, are the exact lower and upper thresholds away
from the upper endpoint. The symbols a_0 and a_infty can have different
anisotropy.

**Proof.** Since A_k>=A_0, the sharp constant for k is no larger than that
for a_0. For Q in G_0 and Q_lambda(x)=lambda^{N/2}Q(lambda x), dominated
convergence using b(xi)<=C|xi|^m and (H1) gives

    lambda^{-m}B(Q_lambda)
       = integral lambda^{-m}b(lambda xi)|Qhat(xi)|^2 ->0.

Hence the constant is also no smaller. Since B(f)>0 for every nonzero f,
equality for the full symbol is impossible. The same strict positivity
shows E_k(f)>0 at masses M<=M_0; low-frequency dilation of any smooth
mass-M trial function gives I(M)=0.

For fixed M<M_infty, (H2) implies for every eta>0

    k(xi) >= (1-eta)a_infty(xi)-C_eta.

The homogeneous inequality therefore yields

    E_k(f) >= (1/2)[1-eta-(M/M_infty)^r] A_infty(f)-C_eta M/2.          (2.1)

Choose eta so the square bracket is positive. This proves a finite lower
bound and boundedness of minimizing sequences. When M>M_0 a smooth
principal negative-energy trial exists by sharpness of the principal GN
inequality and amplitude scaling. For a fixed such trial f, (H1) gives

    E_k(f_lambda)=lambda^m E_0(f)+O(lambda^{m+q})<0

at sufficiently small lambda. Thus I(M)<0.

For clarity the compactness step is recorded fully. For theta>1,

    E_k(sqrt(theta)f)
      =theta^{p/2} E_k(f)
         +(theta-theta^{p/2}) A_k(f)/2.

For masses below M_infty this gives I(theta L)<=theta I(L), and the
stronger I(theta L)<=theta^{p/2} I(L)<theta I(L) if I(L)<0. Thus I(M)/M
is strictly smaller than I(L)/L for every 0<L<M when I(M)<0: if L<=M_0
the latter ratio is zero; if L>M_0 use the strict inequality. Consequently

    I(M)<I(L)+I(M-L),  0<L<M.                                       (2.2)

A bounded minimizing sequence cannot vanish locally in mass, because
the localized GN inequality gives C_p(f_n)->0 under local vanishing,
contradicting I(M)<0. Translate to extract a nonzero weak H^s limit Q and
almost-everywhere convergence. Quadratic forms split by weak Hilbert
convergence, and C_p splits by Brezis--Lieb. If 0<M(Q)<M, normalize the
remainder to its limiting positive mass; boundedness of all energy terms
shows this changes its energy by o(1). The splitting contradicts (2.2).
Thus M(Q)=M. The remainder w_n has M(w_n)->0 and bounded A_k(w_n), so
C_p(w_n)<=C M(w_n)^r A_0(w_n)->0. Energy splitting now forces
A_k(w_n)->0, giving strong H^s convergence.

To obtain a real minimizer, write f=X+iY and let theta=M(X)/M(f). When
both components are nonzero, set g=X/sqrt(theta) and
h=Y/sqrt(1-theta). They have the same mass as f. Evenness of k splits
its quadratic form over real and imaginary parts, while convexity yields

    |f|^p <=theta|g|^p+(1-theta)|h|^p.

Hence E_k(f)>=theta E_k(g)+(1-theta)E_k(h). A real minimizing sequence
exists and its strong limit is real.

Finally, if M>M_infty choose smooth f of mass M with E_infty(f)<0.
Uniform high-frequency convergence and k<=C|xi|^m give

    lambda^{-m}E_k(f_lambda)->E_infty(f)<0,   lambda->infty,

by dominated convergence. Therefore I(M)=-infty. QED.

Every minimizer U in the open window has a Lagrange multiplier omega>0:

    k(D)U+omega U-|U|^{2r}U=0,
    omega M=r A_k(U)-p I(M)>0.                                     (2.3)

Under the individual symbol derivative bounds, U is in L^infty cap
H^{m+1} by the same elliptic bootstrap used in round 9. Real minimizers
have zero momentum and produce global standing waves directly.

## 3. Full upper-endpoint classification for rational interpolation

First allow anisotropy and set

    h=a_infty-a_0,
    k_q(xi)=a_0(xi)+h(xi)|xi|^q/(1+|xi|^q)
           =a_infty(xi)-d_q(xi),
    d_q(xi)=h(xi)/(1+|xi|^q).

At M=M_infty,

    E_k(f)=E_infty(f)-D_q(f)/2,   E_infty(f)>=0.                    (3.1)

**Theorem 2.** For this interpolation:

* If 0<q<m, I(M_infty)=-infty, including anisotropic h.
* If q>m, -infty<I(M_infty)<0 and every minimizing sequence is
  precompact modulo translations; a real minimizer exists, including
  anisotropic h.
* If q=m, a_0(xi)=|xi|^m and a_infty(xi)=(1+epsilon)|xi|^m, then

      I(M_infty)=-epsilon M_infty/2,

  and the infimum is not attained.

**Proof for q<m.** Take an a_infty optimizer Q of mass M_infty, so
E_infty(Q)=0. Then

    lambda^{-(m-q)}D_q(Q_lambda)
      = integral h(xi)/(lambda^{-q}+|xi|^q)|Qhat(xi)|^2
      -> integral h(xi)|xi|^{-q}|Qhat(xi)|^2 >0.

The limiting integral is finite, since 0<m-q<m and Q in H^s; the
integrands are bounded by C |xi|^{m-q}|Qhat|^2. Therefore D_q grows
like a positive multiple of lambda^{m-q}, and (3.1) gives I=-infty.

**Proof for q>m.** The multiplier d_q is bounded and tends to zero as
|xi|->infty. Formula (3.1) gives I>=-||d_q||_infty M_infty/2. Negativity
follows from the low-frequency principal trial because M_infty>M_0.
It remains to prove that minimizing sequences are bounded: the
coercivity inequality (2.1) degenerates at this endpoint.

Suppose instead f_n minimizes and A_infty(f_n)=t_n^m->infty. Put
f_n(x)=t_n^{N/2}V_n(t_n x), so M(V_n)=M_infty and A_infty(V_n)=1.
Since D_q(f_n) is bounded and E_k(f_n)->I, one has

    E_infty(V_n)=t_n^{-m}[E_k(f_n)+D_q(f_n)/2]->0.

The normalized sharp-GN compactness lemma gives, after translations,
V_n->Q strongly in H^s, with Q an a_infty optimizer. Translation does
not affect D_q, and

    D_q(f_n)= integral d_q(t_n xi)|Vhat_n(xi)|^2 ->0.

Indeed replacement of V_n by Q changes this by o(1), using the uniform
L^infty bound on d_q and strong L^2 convergence; the expression for Q
tends to zero by dominated convergence, since d_q(t_n xi)->0 almost
everywhere. Formula (3.1) then gives liminf E_k(f_n)>=0, contradicting
I<0. Thus minimizing sequences are bounded.

For every split 0<L<M_infty, both submasses are strictly below the upper
endpoint. Amplitude scaling gives the same strict binding (2.2), now
with endpoint mass M_infty. The preceding weak-limit and Brezis--Lieb
argument yields full strong compactness and attainment. Realness and
the positive multiplier follow as before.

**Proof for isotropic q=m.** Here

    0<d_m(xi)=epsilon |xi|^m/(1+|xi|^m)<epsilon

for every finite nonzero xi. Thus (3.1) implies
E_k(f)>-epsilon M_infty/2 for every nonzero admissible f. Conversely,
take an a_infty optimizer Q of mass M_infty and dilate to infinity.
Its homogeneous energy remains zero and dominated convergence gives
D_m(Q_lambda)->epsilon M_infty. This proves the exact infimum and
nonattainment. QED.

For the anisotropic borderline q=m one must not replace h(theta) by a
constant. The simple isotropic formula is generally unavailable. A
high-frequency escaping minimizing sequence would have limiting energy
at least

    J_escape=-1/2 sup_{Q in G_infty}
                    integral h(xi/|xi|)|Qhat(xi)|^2,

where G_infty is normalized by mass M_infty and A_infty=1. The same
compactness argument proves attainment if I(M_infty)<J_escape. We do
not assert a complete classification of equality in this anisotropic
borderline case.

For any rational interpolation and any of its minimizers, differentiation
of the mass-preserving scaling energy gives the exact identity

    E_k(U)=-(q/(2m)) integral h(xi)|xi|^q/(1+|xi|^q)^2 |Uhat|^2<0.    (3.2)

It holds at the attained upper endpoint q>m as well. The derivative is
dominated by C|xi|^m, so no spatial moment or differentiability of the
dilation curve as an H^s-valued map is required.

## 4. Sharp lower-threshold scale and shape selection

Set

    C_min = inf_{Q in G_0} C_*(Q),
    beta_* = [m/((m+q)C_min)]^{1/q},
    K_* = [q/(2(m+q))] beta_*^m.

Under (H4), C_min is finite, strictly positive, and attained. Finiteness
is immediate. For positivity use c_*(xi)>=c|xi|^{m+q} and Jensen on the
probability measure |Qhat|^2/M_0:

    integral |xi|^{m+q}|Qhat|^2
      >= M_0^{-q/m}(integral |xi|^m|Qhat|^2)^{1+q/m},

where the last m-moment is bounded below since A_0(Q)=1. For attainment,
take a minimizing sequence in G_0, translate for strong H^s convergence
to Q in G_0, and use lower semicontinuity of the nonnegative c_* form.

Write G_select={Q in G_0:C_*(Q)=C_min}. This set is nonempty and compact
in H^s modulo translations and phase.

**Theorem 3.** Assume (H1)--(H4). Let M decrease to M_0 from above and
let U_M be any constrained minimizer. Define

    alpha=M/M_0,
    d=alpha^r-1,
    lambda_M=[A_0(U_M)/alpha]^{1/m},
    U_M(x)=sqrt(alpha) lambda_M^{N/2} V_M(lambda_M x).

Thus M(V_M)=M_0 and A_0(V_M)=1. Then

    I(M) = -alpha K_* d^{1+m/q}(1+o(1)),                            (4.1)
    lambda_M/d^{1/q} -> beta_*,                                   (4.2)
    dist_{H^s}(V_M, G_select modulo translations and phase)->0,     (4.3)
    1-(2/p)||V_M||_p^p = o(d),                                   (4.4)
    B(U_M)/A_0(U_M) = [m/(m+q)]d+o(d),                            (4.5)
    omega_M = (r/M_0) beta_*^m d^{m/q}(1+o(1)).                   (4.6)

The distance statement means that every sequence M_n->M_0 has a
subsequence and translations/phases on which V_{M_n} converges strongly
in H^s to an element of G_select. There is no uniqueness assumption on
the homogeneous ground states, and no spectral nondegeneracy assumption.

**Proof.** Put

    H(V)=1-(2/p)C_p(V)>=0

on the normalization M=M_0,A_0=1. The exact energy formula is

    E_k(U_M)=alpha lambda_M^m/2 [-d+(1+d)H(V_M)]
                  +alpha/2 integral b(lambda_M xi)|Vhat_M|^2.      (4.7)

Negativity and b>=0 imply 0<=H(V_M)<d/(1+d), so the normalized
sharp-GN compactness lemma applies: modulo translations/phases every
sequence has a subsequence V_M->Q in G_0 strongly in H^s.

We first prove lambda_M->0, with no moment assumption on the minimizers.
If a subsequence has lambda_M>=ell>0, (H1) gives

    B(U_M)/A_0(U_M)
      >= c integral min(lambda_M^q|xi|^{m+q},|xi|^m)|Vhat_M|^2.

Choose an annulus on which the limiting Q has a positive Fourier
L^2-mass. The right side is then bounded below by a fixed positive
constant, whereas (4.7) implies B/A_0<d->0. Contradiction.

For lambda>0 define the normalized rescaled correction

    D_lambda(V)=integral b(lambda xi)/lambda^{m+q}|Vhat(xi)|^2.

If lambda_n->0 and V_n->Q strongly in H^s, then

    liminf D_{lambda_n}(V_n)>=C_*(Q)>=C_min.                        (4.8)

To see this, restrict the integral to an arbitrary compact annulus;
(H3) gives uniform convergence of its multiplier and strong Fourier
L^2 convergence gives convergence of the restricted integral. Discard
the complement using nonnegativity, then exhaust all frequencies.
No uniform (m+q)-moment bound on V_n has been assumed.

For any fixed Q in G_select, (H1) bounds
b(lambda xi)/lambda^{m+q} by C|xi|^{m+q}; thus (H3), (H4), and dominated
convergence give D_lambda(Q)->C_min. Test with
sqrt(alpha)(beta_* d^{1/q})^{N/2}Q(beta_*d^{1/q} x). Formula (4.7)
with H(Q)=0 proves

    limsup I(M)/(alpha d^{1+m/q}) <= -K_*<0.                       (4.9)

Equations (4.7)--(4.8) and negativity show, along every subsequence,

    lambda_M^q D_{lambda_M}(V_M)<d,

so lambda_M^q<=2d/C_min for sufficiently small d. Conversely (4.7)
implies I(M)>=-alpha d lambda_M^m/2; combining this with (4.9) gives
lambda_M^m>=K_* d^{m/q} for sufficiently small d. Consequently

    0<c<=beta_M:=lambda_M/d^{1/q}<=C<infty.                         (4.10)

The same inequality also bounds D_{lambda_M}(V_M), and (4.7) bounds
H(V_M)/d. Extract a subsequence with beta_M->beta in (0,infty),
V_M->Q in G_0 strongly H^s after translations/phases, and convergent
scalar quantities D and H/d. Dividing (4.7) by alpha d^{1+m/q} gives

    I(M)/(alpha d^{1+m/q})
      =1/2 [-beta_M^m +(1+d) beta_M^m H(V_M)/d
                           +beta_M^{m+q} D_{lambda_M}(V_M)].       (4.11)

Using (4.8) and H>=0, its liminf is at least

    F(beta,C_*(Q)):=1/2[-beta^m+C_*(Q)beta^{m+q}]
      >= min_{t>0}1/2[-t^m+C_min t^{m+q}]
      =-K_*.

The one-variable minimizer is unique, beta=beta_*. Moreover strict
monotonicity of the minimum in C_*(Q) forces C_*(Q)=C_min. Equality
with the upper bound (4.9) also forces H(V_M)/d->0 and
D_{lambda_M}(V_M)->C_min. This proves (4.1)--(4.4). Every subsequential
limit has these properties, so the assertions hold for the full family
in the stated distance sense.

Finally

    B(U_M)/A_0(U_M)=lambda_M^q D_{lambda_M}(V_M)
      =d beta_*^q C_min+o(d)=m d/(m+q)+o(d),

which is (4.5). The exact multiplier formula (2.3), with
A_0(U_M)=alpha lambda_M^m, B/A_0=O(d), and I/A_0=O(d), gives
omega_M/lambda_M^m->r/M_0, proving (4.6). QED.

One can also read off the next normalized frequency coefficient without
requiring a higher-order dispersion expansion:

    omega_M/lambda_M^m
      = r/M_0 + [r+q/(m+q)]d/M_0+o(d).

This follows directly from (2.3), (4.1), (4.2), and (4.5), and is not an
expansion of lambda_M itself beyond its leading order.

## 5. Precise variational limiting principle

The preceding theorem has an actual Gamma-limit interpretation, not
just a formal balance. For d>0 let alpha_d=(1+d)^{1/r}, ell=d^{1/q},
and define on H^s, with the strong H^s topology,

    F_d(W)= E_k(sqrt(alpha_d) ell^{N/2}W(ell x))
                   /(alpha_d d^{1+m/q}),  if M(W)=M_0,
    F_d(W)=+infty otherwise.

The exact expression is

    F_d(W)=E_0(W)/d-C_p(W)/p
       +(1/2) integral b(ell xi)/ell^{m+q}|What(xi)|^2.              (5.1)

The Gamma-limit is

    F_0(W)=[C_*(W)-A_0(W)]/2,
       if M(W)=M_0 and E_0(W)=0;
    F_0(W)=+infty otherwise.                                      (5.2)

For a strong H^s-convergent sequence, E_0 and C_p are continuous.
If E_0(W)>0, the first term in (5.1) diverges to infinity, while the
third is nonnegative and the second stays bounded. If E_0(W)=0,
the first term is nonnegative on the mass constraint, and the annular
lower-semicontinuity argument proves the liminf bound. For finite
F_0(W), the constant sequence W is a recovery sequence by dominated
convergence from b<=C|xi|^{m+q}. This proves the Gamma-limit.

Translation invariance prevents literal global equicoercivity; it is
not asserted. Theorem 3 separately proves compactness of minimizers
modulo translation after the indicated rescaling. The minimizers of
(5.2) are precisely beta_*^{N/2}Q(beta_* x) for Q in G_select, including
translations and phases. The normalized V_M instead approach Q itself;
the rescaled W_M in (5.1) approach its beta_* dilation. This distinguishes
a rigorous selection statement from an unsupported formal modulation
calculation.

## 6. Concrete quartic consequence and scope

For a_0=|xi|^4 and b=epsilon |xi|^6/(1+|xi|^2), take m=4,q=2. Let

    S_6=min_{Q in G_0} integral |xi|^6|Qhat|^2,
    C_min=epsilon S_6,
    d=(M/M_c)^{4/N}-1.

Then beta_*^2=2/(3 epsilon S_6), and

    I(M) ~ -(M/M_c) [2/(27 epsilon^2 S_6^2)] d^3,
    lambda_M^2 ~ [2/(3 epsilon S_6)] d,
    omega_M ~ [4/(N M_c)] [4/(9 epsilon^2 S_6^2)] d^2.

The physical width grows like d^{-1/2}, its kinetic energy vanishes
like d^2, and its negative energy vanishes like d^3. The shape selected
is a principal critical GN optimizer minimizing the sixth Fourier
moment, a well-defined selection rule even without uniqueness.

For this q=2<m=4 example the upper endpoint already satisfies
I(M_infty)=-infty. The complete isotropic diagram for general q is:

    M<=M_0:                  I=0, not attained;
    M_0<M<M_infty:           finite negative, attained;
    M>M_infty:               I=-infty;
    M=M_infty,q<m:           I=-infty;
    M=M_infty,q=m:           I=-epsilon M_infty/2, not attained;
    M=M_infty,q>m:           finite negative, attained.

This is a complete constrained variational classification within the
specified isotropic interpolation family, plus a sharp lower-threshold
selection law (unconditional in the stated regularity class for q<=m+2).
It says nothing by itself about the fate of arbitrary solutions of the
pure homogeneous BNLS. Orbital stability would require a suitable
well-posed conservative flow and the usual variational stability
argument; it is not silently included.

## 7. Literature check and attribution limits

Targeted web searches on October 8, 2026 found the following relevant
primary-source background, which should be checked directly before
final bibliography/priority statements:

* Bonheure et al., *Normalized solutions to the mixed dispersion
  nonlinear Schrodinger equation in the mass critical and supercritical
  regime*, arXiv:1802.09217. It studies a fourth-plus-second-order symbol,
  not the same-order low/high interpolation analyzed here.
* Liu, Romani, Su, *Mixed-dispersion Schrodinger equations and
  Gagliardo--Nirenberg inequalities: equivalence between ground states
  and optimizers*, arXiv:2603.26493. The abstract concerns the regime
  mass-supercritical for the Laplacian and mass-subcritical for the
  bilaplacian; it explicitly builds on a known critical-mass existence
  threshold from Bonheure et al. (2018).
* Carles, *On Schrodinger equations with modified dispersion*,
  arXiv:1105.4954, treats well/ill-posedness for homogeneous or bounded
  Fourier multipliers, not this constrained minimum classification.

The present search does not establish novelty. The strong mathematical
content to assess against the literature is the full same-order
two-threshold endpoint classification and the optimizer-manifold
selection law, rather than the familiar concentration-compactness
existence mechanism.

## 8. Joint weak-perturbation and mass-excess limit

This further result requires no finite higher-moment assumption. Fix
an elliptic homogeneous symbol a and put

    b_0(xi)=a(xi)|xi|^q/(1+|xi|^q),   k_epsilon=a+epsilon b_0,
    M_c=M_{c,a}, r=m/N, p=2+2r.

Fix 0<tau<1, set alpha_epsilon=(1+epsilon tau)^{1/r} and
M_epsilon=alpha_epsilon M_c. Denote the k_epsilon constrained infimum
by I_epsilon. These masses lie strictly in its existence window.
Let the entire homogeneous equality manifold be

    H={Q: M(Q)=M_c, E_a(Q)=0},

with no A_a normalization. Define

    J(tau)=min_{Q in H} [B_0(Q)-tau A_a(Q)]/2,
    S_tau=argmin_{Q in H} [B_0(Q)-tau A_a(Q)]/2.

**Theorem 4.** J(tau) is finite, negative, attained, and S_tau is compact
in H^s modulo translations and constant phase. For every constrained
minimizer U_epsilon of I_epsilon(M_epsilon),

    I_epsilon(M_epsilon)/(alpha_epsilon epsilon) -> J(tau),
    dist_{H^s}(U_epsilon/sqrt(alpha_epsilon), S_tau)->0.

The statement also holds along tau_epsilon->tau in (0,1), with J(tau)
as the limit, and the compactness estimates are uniform when tau stays
in a compact subinterval of (0,1). No spatial rescaling is used: the
weak perturbation selects an actual scale from the scale-invariant
critical equality manifold.

**Proof.** Since b_0/a tends to one at infinity,

    B_0(f)>=(1-eta)A_a(f)-C_eta M(f).

On H the objective is therefore coercive in A_a for eta<1-tau.
It is negative for a sufficiently low-frequency dilation of any
homogeneous optimizer. A minimizing sequence has A_a bounded above
and bounded away from zero, since its objective is >=-tau A_a/2.
Normalize A_a to one and use sharp-GN compactness. The normalizing
scales stay in a compact subset of (0,infty), giving strong H^s
convergence modulo translation. Continuity of the bounded order-m
form B_0 gives attainment and compactness of S_tau.

For f of mass M_c, the identity alpha_epsilon^r=1+epsilon tau yields

    F_epsilon(f):=E_{k_epsilon}(sqrt(alpha_epsilon) f)
                     /(alpha_epsilon epsilon)
      = E_a(f)/epsilon + B_0(f)/2 - tau ||f||_p^p/p.                (8.1)

This strongly-H^s Gamma-converges to (B_0-tau A_a)/2 on H and +infty
off H. The liminf follows from E_a>=0 and continuity of the other two
terms; a constant equality profile is a recovery sequence.

The required compactness of minimizers is proved separately. Sharp GN
at mass alpha_epsilon M_c gives

    E_{k_epsilon}(U)
      >=epsilon[(1-eta-tau)A_a(U)-C_eta M(U)]/2.

Testing (8.1) with a selected profile gives the exact upper bound
I_epsilon/(alpha_epsilon epsilon)<=J(tau)<0. Hence A_a(U_epsilon) is
uniformly bounded. The lower bound E>=-epsilon tau A_a/2 also forces
A_a(U_epsilon) bounded away from zero. For
f_epsilon=U_epsilon/sqrt(alpha_epsilon), (8.1) shows
E_a(f_epsilon)=O(epsilon). Normalize its kinetic form and apply sharp-GN
compactness, obtaining a strong H^s limit Q in H after translations.
The Gamma liminf is at least J(tau), whereas the trial upper bound is
at most J(tau). Equality follows and Q belongs to S_tau. This proves
both assertions. Uniformity for tau in compact subintervals and limits
tau_epsilon->tau follow from the same estimates. QED.

The Lagrange multipliers obey, along each convergent subsequence,

    omega_epsilon -> r A_a(Q)/M_c,  Q in S_tau.

Thus arbitrarily weak perturbations can select finite-frequency,
finite-width critical ground profiles when the mass excess is of the
same order as the perturbation. This complements Theorem 3, where the
mass excess is much smaller and the selected spatial scale diverges.

J(tau) is concave as an infimum of affine functions of tau and is strictly
decreasing: if 0<tau_1<tau_2<1 and Q_1 is a minimizer at tau_1, then

    J(tau_2)<=J(tau_1)-(tau_2-tau_1) A_a(Q_1)/2<J(tau_1).

When the finite (m+q)-moment assumption of Theorem 3 holds, the same
one-variable minimization and annular liminf argument, now entirely on
H, give as tau->0

    J(tau)~-K_0 tau^{1+m/q},

where K_0 is defined by minimizing integral a(xi)|xi|^q|Qhat|^2 over
the normalized A_a=1 equality set. This recovers the lower-threshold
law as the small-tau limit of the full perturbation-selection functional.
