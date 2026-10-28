# Exact projector flows and a strict wrong-sign result for ground-state diffusion

Date: 2026-10-16.

This note proves a definite sign on the full localized self-consistent class, rather than proposing another unproved monotonicity principle. Ground-state diffusion without normalization strictly decreases the LT quotient at every occupied rank greater than one; exact Gram normalization makes the same evolution completely stationary. Ordinary normalized heat and density heat through common transport also fail the proposed increasing-quotient property, already from a scalar Townes optimizer. A quotient gradient flow has an elementary positive derivative, but every self-consistent candidate is a fixed point. No unrestricted sharp constant is improved here.

## 1. Setting and the occupied-number derivative

Let H=-Delta on R2. Let phi_1,...,phi_N be orthonormal, smooth, exponentially localized orbitals satisfying

    (H-g rho)phi_j = -e_j phi_j,
    rho = sum_j |phi_j|^2,
    e_1 > e_j > 0 for j>=2,
    phi_1=w>0.                                          (1.1)

The first eigenvalue is simple; degeneracies among the other occupied levels are allowed. Additional unoccupied negative eigenvalues are allowed and do not affect the argument. Set

    T_j = integral |gradient phi_j|^2,
    T = sum_j T_j,
    F = integral rho^2,
    r_j = integral rho |phi_j|^2,
    Q = F/T.

Testing (1.1) with phi_j yields

    T_j - g r_j = -e_j.                                  (1.2)

Mass-preserving planar dilation of the coupled stationary action gives

    T=gF/2,    sum_j e_j = T.                            (1.3)

Thus the hypotheses cover the common-density finite-rank critical states used in the minimal-violator reduction, not only separated or perturbative profiles. The equal component masses are the orthonormal normalization one. The usual cutoff Pohozaev argument is justified by the stated localization.

Now keep the orbitals fixed and vary their occupations:

    gamma_a = sum_j a_j |phi_j><phi_j|,
    T(a)=sum_j a_j T_j,
    F(a)=integral (sum_j a_j |phi_j|^2)^2.

At a=(1,...,1), equations (1.2)-(1.3) give the exact formula

    partial_(a_j) [F(a)/T(a)]
      = [2T r_j-F T_j]/T^2
      = F e_j/T^2 > 0.                                  (1.4)

Consequently every nontrivial infinitesimal decrease of occupied numbers, with fixed orbitals, strictly decreases Q. More precisely, for a_j'(0)<=0 and at least one strict inequality,

    Q'(0) = (F/T^2) sum_j e_j a_j'(0) < 0.               (1.5)

This is a genuine fixed sign on the self-consistent class. It rules out an increasing-Q argument based only on attenuating occupied modes. It does not cover Darboux transformations, which change the remaining orbitals, or nonlinear deformations changing their shapes.

## 2. Ground-state diffusion: wrong sign without normalization, exact stasis with it

Consider the weighted space L2(w^2 dx) and the ground-state diffusion generator

    L_w = -w^(-2) div(w^2 gradient).

Multiplication by w is a unitary map from this weighted space to ordinary L2, and the ground-state transform is

    w L_w f = (H-g rho+e_1)(w f).                        (2.1)

This identity can equivalently define the closed nonnegative form, so no boundedness assumption on phi_j/w is needed. For f_j=phi_j/w,

    integral w^2 conjugate(f_i) f_j = delta_ij,
    L_w f_j = (e_1-e_j) f_j.                             (2.2)

Therefore the exact unnormalized diffusion is

    f_j(t)=exp[-(e_1-e_j)t] f_j,
    gamma(t)=sum_j exp[-2(e_1-e_j)t] |phi_j><phi_j|.       (2.3)

This remains an admissible positive contraction 0<=gamma(t)<=1, and it tends to the rank-one projector onto w. Applying (1.4) gives

    d/dt [F(gamma(t))/T(gamma(t))] at t=0
      = -2F/T^2 sum_j e_j(e_1-e_j) < 0,   N>=2.          (2.4)

Strictness needs only the simple lowest level and positive occupied binding energies. It does not require a lower bound on spectral gaps or absence of further negative spectrum. With p_j=e_j/T and the dimensionless time tau=T t, the slope is

    d/dtau log Q at 0 = -2[p_1-sum_j p_j^2] < 0.         (2.5)

Thus this diffusion starts in the wrong direction for transferring a rank-one upper bound on Q back to the initial projection.

If the diffused family is Gram-normalized instead, its Gram matrix is exactly

    M(t)=diag(exp[-2(e_1-e_j)t]).

Multiplication by M(t)^(-1/2) cancels every decay factor. The normalized projector equals the original P for every finite t. This statement is independent of the chosen occupied basis: the span is invariant under the generator, and its orthogonal projection does not change.

More generally, any frozen spectral filter that is nonzero on every occupied eigenvalue leaves the normalized occupied projection unchanged. The weighted language does not avoid this algebra. Updating the same self-consistent operator in an autonomous normalized flow still leaves a self-consistent initial projector at a fixed point.

**Completed exclusion:** the proposed ground-state diffusion mechanism cannot both reduce occupied rank and preserve the favorable quotient comparison through Gram normalization. Without normalization it has the strict wrong initial sign (2.4); with normalization it does not move the self-consistent projector at all. This result includes a hypothetical minimal violating state and does not assume that such a state exists.

## 3. Ordinary normalized heat: exact formulas and a scalar self-consistent counterexample

For a finite orthonormal frame Phi_0, view Phi_0 as an isometry from C^N into L2. Let

    X(t)=exp(-tH)Phi_0,
    M(t)=X(t)*X(t),
    P(t)=X(t) M(t)^(-1) X(t)*.

The heat semigroup is injective, so M(t)>0 at every finite t. Direct differentiation gives the exact projector evolution

    P_t = -HP-PH+2PHP.                                  (3.1)

One can choose an orthonormal frame gauge satisfying

    Phi_t = -H Phi + Phi K,
    K=Phi* H Phi.                                       (3.2)

The frame obtained from the positive square root M(t)^(-1/2) may differ by a time-dependent unitary; (3.1) is gauge-independent. No approximate Gram estimate is being used.

Put

    A=(I-P)H Phi,
    B=(I-P)(rho Phi),

with the Hilbert–Schmidt real inner product on frames. For smooth frames the exact derivatives are

    T_t = -2 ||A||^2,
    F_t = -4 Re <B,A>,
    Q_t = [2F||A||^2-4T Re<B,A>]/T^2.                   (3.3)

For example, writing tau=sum_j |gradient phi_j|^2 and R=Phi* rho Phi,

    rho_t = Delta rho - 2 tau + 2 Phi* K Phi,
    F_t = -2 integral |gradient rho|^2
          -4 integral rho tau +4 Tr(KR).

The last term is the exact normalization contribution and has no sign that can be dropped. At a self-consistent state (1.1), A=gB and g=2T/F, so Q_t=0 at the initial time. This vanishing is stationarity of the quotient, not evidence for a monotonicity theorem.

There is a strict global counterexample within the scalar self-consistent class. Let phi be a positive L2-normalized Townes optimizer. It is smooth, integrable and exponentially localized, and Q(phi)=C1=2/Mc. The rank-one normalized heat flow is

    phi(t)=exp(t Delta)phi / ||exp(t Delta)phi||_2.

After diffusive spatial rescaling, exp(t Delta)phi converges to its positive integral times the heat kernel. The rescaled normalized profile therefore converges in H1 and L4 to

    psi_G(x)=(2 pi)^(-1/2) exp(-|x|^2/4).

This standard heat asymptotic follows directly by writing the heat convolution as translated copies of the kernel and using dominated convergence; the exponential localization of phi supplies all needed moments. Its quotient is

    T(psi_G)=1/2,    F(psi_G)=1/(4 pi),
    Q(phi(t)) -> 1/(2 pi).                              (3.4)

Strictly C1>1/(2 pi), without numerical Townes data. Indeed the normalized trial sqrt(3/pi)(1+|x|^2)^(-2) gives C1>=15/(28 pi)>1/(2 pi).

Thus normalized heat starting at an exact scalar optimizer eventually has a strictly smaller quotient. It cannot provide an increasing-Q deformation to Townes profiles. The initial derivative is zero, as (3.3) correctly predicts; some later decrease is unavoidable.

## 4. Common transport preserves orthogonality, but density heat has the same obstruction

Let v(t,x) be a smooth real velocity and transport half-densities by

    partial_t phi_j = -v dot gradient phi_j -(div v)phi_j/2. (4.1)

This is the unitary pullback under the coordinate flow. It preserves every pairwise L2 inner product exactly, while

    rho_t + div(rho v)=0.

For the real kinetic stress S_ab=Re sum_j conjugate(partial_a phi_j) partial_b phi_j, integration by parts gives

    F_t = -integral rho^2 div v,
    T_t = -2 integral S_ab partial_a v_b
          +(1/2) integral rho Delta(div v).               (4.2)

In particular an isotropic dilation changes T and F by the same factor; it cannot repair a wrong quotient sign by itself.

Choosing v=-gradient log rho makes rho_t=Delta rho. This is a genuine density diffusion implemented through a common orthogonality-preserving transport, rather than independent smoothing followed by an approximate reorthogonalization. Nevertheless its proposed increasing-Q property is false already at rank one.

For a scalar positive real orbital phi=sqrt(rho), take rho_0=phi_Townes^2, of mass one and finite variance. Let rho(t)=exp(t Delta)rho_0. Then

    F(t)=integral rho(t)^2 ~ 1/(8 pi t).

Let I(t)=integral |gradient rho(t)|^2/rho(t) be its Fisher information. With V0 the centered initial second moment, Cauchy–Schwarz applied to integral (x-mean) dot gradient rho=-2 gives

    I(t) >= 4/(V0+4t).

On the other hand the Gaussian score conditional-expectation identity gives

    I(rho_0*G_t) <= I(G_t)=1/t.

Explicitly, if X has density rho_0 and Z is an independent centered Gaussian of covariance 2t I_2, the score of X+Z is E[-Z/(2t) | X+Z]; Jensen yields the bound. Hence t I(t)->1. Since T(sqrt(rho))=I/4,

    F(t)/T(sqrt(rho(t))) -> 1/(2 pi) < C1.               (4.3)

This proves failure for density heat without using a numerical profile or an unknown stability theorem. For the smooth positive Townes density the transport generator is well-defined; alternatively the rank-one family sqrt(rho(t)) directly realizes the exact continuous normalization. The general orthogonality claim in (4.1) is independent of this scalar counterexample.

## 5. A positive quotient-gradient identity exists, but supplies no critical-state exclusion

For comparison, define g(P)=2T/F and the horizontal frame evolution

    Phi_t = -A+gB
          = -H Phi+g rho Phi+Phi(K-gR),
    R=Phi* rho Phi.                                     (5.1)

Its matrix multiplier is Hermitian, so it preserves orthonormality exactly. Combining the first variations of F and T gives

    Q_t = (2F/T^2) ||A-gB||^2 >= 0.                     (5.2)

Equation (5.2) is simply the Grassmann gradient identity for the quotient. It is valid on any smooth interval of existence; no theorem of global flow existence or convergence is asserted here. It should not be presented as a new sharp functional inequality.

Every self-consistent state (1.1) satisfies A=gB and is an exact fixed point of (5.1). This includes any hypothetical violating optimizer. Consequently monotonicity alone does not establish convergence to separated scalar optimizers or exclude another stationary rank. Any such convergence or exclusion assertion would contain precisely the missing global mathematical content.

## 6. What this settles, and what it does not

The most substantive completed result is the exact occupation derivative (1.4) and its ground-state diffusion consequence (2.4), both on the fully overlapping localized self-consistent class. This is stronger than finding a bad sign on unrelated trial functions. It conclusively eliminates that specific spectral-filtering/Gram-normalization route to a favorable rank reduction.

The remaining calculations distinguish three different evolutions rather than conflating their normalization:

- Linear orbital heat with exact Gram normalization: T decreases, but Q has no universal increasing sign and decreases overall from a Townes state toward its Gaussian heat asymptotic.
- Common half-density transport implementing density heat: orthonormality is exact, but the scalar Townes quotient again tends to the smaller Gaussian value.
- The nonlinear quotient gradient: Q has the exact positive derivative (5.2), but self-consistent states are fixed and no sharp endpoint follows.

No rank-uniform improvement of the d=2, gamma=1 LT constant, no new exclusion of a minimal violating state, and no convergence theorem to separated Townes profiles is claimed.

Primary-source context:

- R. L. Frank, D. Gontier and M. Lewin, *Optimizers for the finite-rank Lieb–Thirring inequality*, https://arxiv.org/abs/2109.05984. The self-consistent finite-rank reduction and its scope are inherited from that work, as detailed in R23/R25. Extra unoccupied negative levels are not excluded here.
- W. Bao and Q. Du, *Computing the ground state solution of Bose–Einstein condensates by a normalized gradient flow*, SIAM J. Sci. Comput. 25 (2004), 1674–1697, https://arxiv.org/abs/cond-mat/0303241 and https://doi.org/10.1137/S1064827503422956. Normalized imaginary-time/gradient methods and their energy dissipation have established precedent. This citation is contextual; it is not used to infer (5.2), global convergence, or any LT theorem.

All decisive formulas above are derived explicitly. Historical priority for this particular wrong-sign formulation has not been established.
