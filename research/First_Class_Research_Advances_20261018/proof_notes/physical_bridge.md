# Physical-model matching and a mixed-order mass-gap extension

Research continuation, 18 October 2026. This note separates a proved structural extension below from an unproved negative-energy existence problem. Literature priority of the extension is not established by the targeted search.

## 1. Which experimental models actually match?

For pure quartic dispersion in N variables, the mass-critical power is |u|^(8/N)u. Thus:

| Variables | Critical nonlinearity | Cubic Kerr equation |
|---|---|---|
| 1 | |u|^8 u | mass-subcritical |
| 2 | |u|^4 u | mass-subcritical |
| 3 | |u|^(8/3) u | mass-subcritical |
| 4 | |u|^2 u | mass-critical |

In particular, 3D cubic pure BNLS is NOT mass-supercritical. The existing 1D pure-quartic optical soliton experiment cannot be identified with the present critical negative-energy construction.

Primary source: Blanco-Redondo et al., *Pure-quartic solitons*, Nature Communications 7, 10427 (2016), DOI 10.1038/ncomms10427, https://www.nature.com/articles/ncomms10427 . It experimentally studies a temporal envelope with Kerr nonlinearity and dominant fourth-order dispersion. Linear loss, two-photon absorption and free-carrier terms are included in its more realistic model. In that paper optical pulse energy means an L2 integral, not the Hamiltonian sign discussed here.

Iyer–Parker–Stefanov, *Existence and Stability for Traveling Waves of Fourth-Order Semilinear Wave and Schrödinger Equations*, Studies in Applied Mathematics 156 (2026), e70214, DOI 10.1111/sapm.70214, https://onlinelibrary.wiley.com/doi/full/10.1111/sapm.70214 : the NLS application in Section 6 treats real standing profiles in a one-dimensional mixed-dispersion cubic equation. Its beam traveling-wave results must not be mistaken for mass-critical BNLS negative-energy moving profiles.

## 2. A genuine three-variable cubic critical model

Let x in R and y in R², and take

    Aop = -partial_x² + b(D_y),
    a(xi,eta) = xi² + b(eta),

where b is a positive, real-even, elliptic quartic homogeneous polynomial. Examples are b(eta)=|eta|⁴ and b(eta)=eta_1⁴+eta_2⁴. Set

    H = {u in L² : partial_x u in L², D_y² u in L²},
    A(u)=||partial_x u||² + integral b(eta)|uhat|²,
    M(u)=||u||²,
    F(u)=||u||_4⁴,
    E(u)=A(u)/2-F(u)/4.

The equation i u_t=Aop u-|u|²u is cubic and mass-critical under

    u_lambda(t,x,y)=lambda² u(lambda⁴ t,lambda² x,lambda y).

This is a mathematically natural anisotropic dispersion model, not a claim that an experimental implementation of precisely this model has already been demonstrated. Its anisotropic scaling and critical exponent are established themes: see Fibich–Ilan–Schochet, *Critical exponents and collapse of nonlinear Schrödinger equations with anisotropic fourth-order dispersion*, Nonlinearity 16 (2003), 1809–1821, DOI 10.1088/0951-7715/16/5/314, author PDF https://www.math.tau.ac.il/~fibich/Manuscripts/anisotropic_NL.pdf . Komada, Funkcialaj Ekvacioj 65 (2022), 191–214, DOI 10.1619/fesi.65.191, treats blowup for anisotropic fourth-order equations. Those papers' critical scaling should be credited; a mass-gap theorem is a separate claim.

## 3. Exact removal of the apparent anisotropic obstruction

For a traveling profile U with parameters (omega,v_x,v_y), the profile equation is

    [Aop+omega+i v_x partial_x+i v_y dot grad_y]U-|U|²U=0.

Phase modulation in x gives the exact group-velocity relation

    P_x(U)=v_x M(U)/2.

Set U=exp(i v_x x/2) W. Then W solves the same profile equation with

    v_x'=0,  v_y'=v_y,  omega'=omega-v_x²/4,
    P_x(W)=0,
    E(W)=E(U)-v_x² M(U)/8.

Thus negative energy survives the removal of quadratic-axis velocity. This exact partial Galilean symmetry, rather than reflection symmetry of optimizers, is the decisive device.

The anisotropic dilation identity before this removal is

    4E(U)=v_x P_x(U)+(v_y dot P_y(U))/2.

After removal it becomes

    4E(W)=(v_y dot P_y(W))/2.

For W=X+iY and L_W=Aop+omega'-|W|², the imaginary equation gives

    <Y,L_W Y>=(v_y dot P_y(W))/2=4E(W).

Hence precisely the sign identity used in the isotropic mass-gap argument is restored.

For a smooth real standing profile Q, the response matrix also shows this cancellation directly. Since L_-(xQ)=-2 partial_x Q,

    T_xx=<partial_xQ,L_-^{-1}partial_xQ>=M(Q)/4,
    T_xyj=<partial_yj Q,L_-^{-1}partial_xQ>=0.

Consequently the feared indefinite symmetrized product of an arbitrary positive response matrix with anisotropic weights cannot arise through coupling to these quadratic directions. No evenness or uniqueness of Q is required for this fact.

## 4. Uniform traveling-profile mass gap for this mixed model

**Proposition.** Let Mc be defined by the sharp anisotropic inequality

    F(f) <= (2/Mc) M(f) A(f).

There exists delta>0, depending on b but independent of frequency and all velocity components, such that every negative-energy traveling profile of the mixed equation satisfies

    M(U) >= Mc+delta.

The proposition is for weak finite-energy H profiles. The required regularity and cutoff identities can be obtained as follows. H embeds in H¹(R³), so U³ belongs to L², as do the first-derivative drift terms. The profile equation implies Aop U belongs to L² and hence U belongs to D(Aop), in particular to H²(R³). Since H²(R³) is an algebra and the elliptic symbol satisfies 1+a >= c(1+|xi|²+|eta|²), the equation then bootstraps U into every finite isotropic Sobolev space. One can test with compactly supported phase and dilation generators. For phase modulation use x chi(z/R) or y_j chi(z/R); for dilation use the skew generator 2x partial_x+y dot grad_y+2, localized by chi(z/R), with its divergence correction. Integration by parts for the polynomial Aop yields the displayed identities as R tends to infinity. Terms involving derivatives of chi contain bounded annular coefficients and at most the energy derivatives (after integration by parts); higher cutoff derivatives carry additional inverse powers of R. All errors tend to zero by the L² energy tails and the L⁴ nonlinear tail. Thus no spatial-moment assumption is needed. A final manuscript should spell out this short cutoff calculation rather than leave the identities as an extra hypothesis.

### Analytic inputs

1. H embeds in H¹(R³), and hence L⁴. The anisotropic scaling converts the inhomogeneous bound into F<=C MA. Alternatively Hausdorff–Young and integral (1+xi²+b(eta))^(-2) dxi deta<infinity give the same bound.

2. Normalized maximizing sequences for the sharp inequality are compact modulo translations. Indeed, H¹ Lions vanishing would imply L⁴ vanishing, so a translated nonzero weak limit exists. Brezis–Lieb and quadratic decoupling imply, after M=A=1 normalization,

       1 <= ma+(1-m)(1-a) <=1,

   where m,a are the limiting fraction of mass and kinetic energy. Because both are positive for a nonzero L² profile, equality forces m=a=1. This proves optimizer existence and compactness, with no uniqueness assumption.

3. Every complex optimizer has a constant phase, and for a real optimizer Q of mass Mc and A(Q)=1,

       L_-=Aop+1/Mc-Q²

   is nonnegative with form kernel span{Q}. This follows from the existing strictly-convex density-norm lemma with density space L² and exponent kappa=2. The proof uses real/imaginary kinetic splitting, sharp interpolation, equality in Hölder, and strict convexity; it does not need a maximum principle.

4. Q² is form compact relative to Aop+1. Approximate Q² in L² by bounded compactly supported potentials, use H→L⁴ for the error, and local Rellich compactness H¹→L² for the compact part. Therefore L_- is coercive in H on Q-perp.

### Proof of the proposition

Assume profiles U_n have E(U_n)<0 and M(U_n) down to Mc. First remove v_x by the exact boost above, obtaining W_n with E(W_n)<0 and unchanged mass. Apply the anisotropic dilation to make A(W_n)=1. Sharp GN gives

    (1-M(W_n)/Mc)/2 <= E(W_n)<0,

so E(W_n)→0 and F(W_n)→2. Near-optimizer compactness gives, after phases and translations, W_n→Q strongly in H, with Q real, M(Q)=Mc, A(Q)=1.

The y group-velocity identity is

    v_y M(W)=integral grad b(eta)|What|².

Since |grad b|<=C b^(3/4), v_y is bounded when A=1 and mass stays near Mc. The profile-testing and dilation identities give

    omega' M(W)=A(W)+4E(W),

so omega'_n→1/Mc. After extracting v_y,n→v_*, pass to the profile equation. The real optimizer equation and the imaginary part imply v_* dot grad_y Q=0. An L² function invariant along a nonzero Euclidean direction is zero, so v_*=0.

Choose phases so that Y_n=Im W_n is L²-orthogonal to Q. Strong L⁴ convergence gives || |W_n|²-Q² ||_2→0. Thus L_n=Aop+omega'_n-|W_n|² remains coercive on Q-perp for all large n. But

    4E(W_n)=<Y_n,L_nY_n> >=0,

contradicting E(W_n)<0. This proves the uniform positive mass gap.

This conclusion does not establish existence of negative-energy traveling profiles for this mixed model. It is a nonvacuous restriction only once such profiles are found, although the implication itself is unconditional for the specified profile class.

### Positive lower-order dispersion in the quartic directions

The same delta can be chosen uniformly for the family

    Aop_mu=-partial_x²+b(D_y)-mu Delta_y,   mu>=0,

with Mc still defined by the principal anisotropic sharp inequality. After removing v_x and normalizing principal A=1, put B=mu ||grad_y W||². The identities become

    4E(W)=<Y,L_WY>+B,
    omega' M(W)=A-B+4E(W).

If negative-energy profiles approach Mc, sharp GN gives

    E(W)>= B/2 -(M(W)/Mc-1)/2,

so B→0, E→0, and omega'→1/Mc. The normalized profiles again converge strongly in H to Q. Since ||grad_y Q||²>0, strong H convergence implies mu→0 in these normalized units. Thus the nonnegative extra quadratic form causes no loss in the phase-coercivity contradiction. This extends the restriction to the conventional positive quadratic-plus-quartic anisotropic model, with cubic nonlinearity when there are one quadratic and two quartic directions. Positive-semidefinite quadratic matrices in y can be treated similarly: the gradient covariance matrix of a nonzero L² optimizer is positive definite, so vanishing added kinetic energy forces the matrix coefficients to vanish after normalization.

## 5. What genuinely remains for applicability and lower dimensions

The existing N=2 search was not simply omitted. Round-2 source notes report well-decayed radial excited profiles with zero through nine rings, all with positive response. Negative signs from shorter truncated domains were recognized as artifacts. Collinear and square arrays also gave positive responses. Existing one-dimensional 14-pulse candidates have numerically negative response but are not certified real-line solutions; dimension continuation folds before reaching two dimensions.

Therefore a useful low-dimensional existence attack must change the branch or mechanism, rather than repeat the same small-velocity radial search. Two credible direct routes are:

* Continue the FULL complex traveling equation in (velocity,excited-branch parameter), allowing finite-velocity folds and momentum reversal, and certify a found branch. Positive response at v=0 does not exclude E(v)<0 at a finite velocity.
* In the mixed three-variable cubic model, solve the excited standing equation in x and radial y, then compute the quartic-axis response L_-^{-1}partial_y Q. Quadratic-axis response is exactly positive and cannot generate the desired branch. A negative quartic response, accompanied by the symmetry-restricted inverse bounds, would produce a physically better-matched critical counterexample.

For actual apparatus claims the missing result is robustness on an observable propagation interval for the matched physical model, including dimensional coefficients and small loss/odd-dispersion terms. The conservative existence theorem alone cannot establish a robust optical pulse. An unstable branch can still be measurable, but one must quantify its growth rate and preparation tolerance.

## 6. Strongest research payoff

The mixed-order gap is a real extension of the first-class mechanism into a cubic, three-variable setting; the crucial new move is partial Galilean reduction. It preserves the original scientific target rather than relabeling a different problem. The stronger next theorem is existence (or exclusion) of negative-energy moving profiles in this same mixed model, plus a quantitative response/stability prediction. Neither an experimental implementation nor that existence theorem has been established in this note.
