# The full second variation and a rank bound for the first collective improvement

Date: 2026-10-12. This note concerns the two-dimensional, exponent-one Lieb–Thirring problem. It derives exact necessary stability conditions and a quantitative restriction on the **smallest violating rank**. It does not settle the sharp constant. Standard spectral perturbation, finite-rank optimizer existence, and the optimizer spectral gap are inherited mathematical tools; no historical priority is claimed for the consequences below.

## 1. Normalizations and real orbitals

For an orthogonal projection P of finite rank in H1(R2), set

    rho_P = sum_i |phi_i|^2,  T(P) = sum_i ||grad phi_i||_2^2,
    F(P) = int rho_P^2,
    C_N = sup_(0 < rank(P) <= N) F(P)/T(P).

The corresponding finite-rank spectral constant is L_N=C_N/4:

    S_N(V) := sum_(i=1)^N (-lambda_i(-Delta-V))_+
           <= L_N int V^2.

The rank-one constants are C_1=2/M_c and L_1=1/(2M_c), where -Delta Q+Q-Q^3=0 and M_c=||Q||_2^2.

Finite-rank optimizer existence and its Euler–Lagrange equation are available from Frank–Gontier–Lewin (FGL). An optimizer can be taken to be a projection onto R<=N negative eigenfunctions of a real scalar potential. Consequently its range admits a real orthonormal basis. At a rank-R optimizer write C=C_N, L=C/4, rho=rho_P and

    V = 2 rho/C = rho/(2L),
    H = -Delta-V,
    H phi_i = lambda_i phi_i,  lambda_i<0,  i=1,...,R.

The occupied eigenvalues are the first R eigenvalues. The orbitals are smooth and decay exponentially. For the smallest rank N with C_N>C_1, the optimizer has R=N; otherwise it would violate minimality.

The real-basis reduction is important: the sharper real Haar moments below cannot be applied to an arbitrary complex family without this reduction.

## 2. Haar compression of the occupied space

Let P have rank R and a real orthonormal basis, and choose a Haar-uniform k-dimensional real subspace of Ran(P), 1<=k<=R. Denote its orthogonal projection by P_A. For the vector Phi(x)=(phi_1(x),...,phi_R(x)) in R^R,

    rho_(P_A)(x) = Phi(x)^T A Phi(x),

where A is a uniformly rotated rank-k orthogonal matrix projection. Rotational invariance and the beta distribution of the squared length of a projected unit vector give exactly

    E rho_(P_A)(x) = (k/R) rho_P(x),
    E rho_(P_A)(x)^2 = [k(k+2)/(R(R+2))] rho_P(x)^2,
    E T(P_A) = (k/R) T(P).

For completeness, the second identity follows by writing a uniform sphere vector X as Z/|Z| with independent standard real Gaussian coordinates. Then sum_(j<=k) X_j^2 has Beta(k/2,(R-k)/2) distribution and second moment k(k+2)/(R(R+2)); k=R follows directly.

Apply the rank-k inequality F(P_A)<=C_k T(P_A) before averaging. The exact conclusion is

    F(P)/T(P) <= [(R+2)/(k+2)] C_k.                    (1)

Using a real optimizer for C_N with rank R<=N gives, for all 1<=k<=N,

    C_N <= [(N+2)/(k+2)] C_k.                         (2)

If R<k, monotonicity directly gives C_N=C_R<=C_k, so that case is also covered. Thus C_N/(N+2) is non-increasing, while C_N itself is non-decreasing. The bound (2) is an elementary consequence of real finite-rank optimization and Haar compression; it is not the conjectured rank-independent bound.

Suppose N>=2 is the **first violating rank**, so C_(N-1)=C_1 and C_N=(1+delta) C_1 with delta>0. Taking k=N-1 yields

    C_1 < C_N <= [(N+2)/(N+1)] C_1,
    0 < delta <= 1/(N+1),
    N <= 1/delta - 1.                                 (3)

The common component mass beta=2/C_N of its self-consistent NLS profile therefore satisfies

    [(N+1)/(N+2)] M_c <= beta < M_c.                  (4)

This relates the first possible collective violation to the size of the threshold reduction. It gives **no uniform upper bound on N**, since delta may tend to zero. It must not be paraphrased as a bound on arbitrary large-rank counterexamples: a smaller-rank counterexample can be supplemented with diffuse, distant orbitals.

Examples of (4): a first rank-two violation must have beta>=3M_c/4; a first rank-three violation must have beta>=4M_c/5. These lower bounds leave a substantial unresolved interval and are not existence or nonexistence results.

## 3. Exact orbital Hessian under all orthogonality constraints

Let Pi=1-P. We can quotient out constant rotations of the occupied basis and represent any remaining tangent vector by real functions psi_i in Ran(Pi). Let Psi be the operator whose columns are psi_i, and Phi the operator whose columns are phi_i. The curve

    Phi(t) = (Phi+t Psi) (I+t^2 Psi^*Psi)^(-1/2)

is exactly orthonormal. Its second derivative at zero is

    phi_i''(0) = -sum_j phi_j <psi_j,psi_i>.

Set B Psi=sum_i phi_i psi_i and A_i=Pi(H-lambda_i)Pi. Direct differentiation gives

    [C T(P(t))-F(P(t))]''_(t=0)
       = 2C sum_i <psi_i,(H-lambda_i)psi_i>
         -8 int (sum_i phi_i psi_i)^2.                 (5)

Indeed rho'=2 B Psi, while rho'' has both the term 2 sum_i psi_i^2 and the occupied-space correction -2 sum_ij phi_i phi_j <psi_i,psi_j>. The correction is essential: together with the kinetic correction it produces the -lambda_i terms in (5).

At a global optimizer C T-F>=0 and equals zero at t=0, hence

    sum_i <psi_i,A_i psi_i> >= (1/L) ||B Psi||_2^2
             for every psi_i perpendicular to Ran(P). (6)

For complex tangent vectors the right side becomes ||Re sum_i conjugate(phi_i)psi_i||_2^2. Pure imaginary perturbations have no first density variation; replacing this real part by an absolute value would give an incorrect stronger statement.

Internal orthogonal rotations of the occupied basis change neither P, rho nor T. They are exact gauge zero directions, not additional collective instabilities.

## 4. The spectral gap and the potential Hessian

One needs lambda_R<lambda_(R+1), not merely negativity of lambda_R, to invert all A_i. This spectral gap is proved in FGL, *Optimizers for the finite-rank Lieb–Thirring inequality*, Theorem 3 and Section 5, Step 2.

At exponent one the orbital Hessian also gives a short verification. If an occupied real phi_i and an unoccupied real eigenfunction f have the same eigenvalue, replace phi_i by cos(t)phi_i+sin(t)f. Formula (5) becomes

    [C T-F]''(0) = -8 int phi_i^2 f^2 <0,

contradicting optimality. The integral is nonzero by unique continuation (the nonzero set of either smooth eigenfunction is open and dense). Thus an occupied spectral shell cannot be only partly filled.

For real W, spectral perturbation of H-tW gives

    S_N'(V)[W] = int rho W,
    S_N''(V)[W,W]
       = 2 sum_i <Pi(W phi_i), A_i^(-1) Pi(W phi_i)>.
                                                               (7)

All occupied–occupied terms cancel in the trace. This formula includes unoccupied bound states and the continuous spectral subspace. It remains valid with degeneracies inside the occupied cluster; only the gap across its boundary is needed.

Define the self-adjoint positive quadratic-form operator

    R W = sum_i phi_i A_i^(-1) Pi(W phi_i).

Multiplication by phi_i is understood with the projection Pi in the adjoint pairing. Then (6) is equivalent by the Hilbert-space operator norm identity to

    <W,RW> <= L ||W||_2^2  for every real W,
    equivalently R <= L I.                             (8)

The same condition follows from the global maximum of S_N(V)-L||V||_2^2, whose Hessian is 2(R-LI). Begin with bounded compactly supported W; bounded orbitals and the spectral gap extend the form and inequality to L2.

## 5. Exact symmetry modes and a false positivity shortcut

Translations V(x)->V(x+a) and mass-critical spatial dilations V(x)->s^2 V(sx) preserve optimality with the same L. Differentiating rho=2LV along these curves gives

    R(partial_a V) = L partial_a V,
    R(2V+x dot grad V) = L(2V+x dot grad V).             (9)

A nonzero rotational tangent (x_1 partial_2-x_2 partial_1)V likewise has eigenvalue L. Its presence must not be silently discarded by assuming radiality.

Therefore any optimizer saturates (8) in at least the translation and scaling symmetry directions. The reduced resolvents A_i^(-1) are positive as quadratic forms, but their kernels need not preserve pointwise positivity. A Perron–Frobenius argument based on a positive response kernel would already contradict the sign-changing translation modes of the rank-one optimizer. That shortcut is invalid.

Symmetry directions cannot on their own produce a strict violation of (8). Nor does negativity of an excited orbital's unconstrained scalar Hessian suffice: the missing occupied-space projections are exactly the orthogonality constraints that can remove such directions.

## 6. A scalar spectral consequence and why a universal reverse bound fails

In (6), set only the i-th variation equal to a given real chi perpendicular to Ran(P), set all other columns to zero, and sum these N separate inequalities. With S=-sum_i lambda_i one obtains

    <chi,[-Delta-(1+2/N)V]chi> >= -(S/N)||chi||_2^2
                 for every chi perpendicular to Ran(P).

Consequently, by min-max,

    lambda_(N+1)(-Delta-(1+2/N)V) >= -S/N.             (10)

This scalar consequence is necessary for an optimizer, but weaker than the full response bound. A universal reverse inequality based only on the number of wells or eigenvalues is false.

To see the obstruction concretely, let V_R be the sum of N Townes potentials Q(x-a_j)^2, with all pairwise separations tending to infinity. For each individual original well, the first eigenvalue of -Delta-Q^2 is -1. At the factor a=1+2/N<3 (N>=2),

    lambda_1(-Delta-a Q^2)<-1,
    lambda_2(-Delta-a Q^2)>-1.

The second statement follows without an assumed radial spectral classification. The rank-one constrained Hessian gives lambda_2(-Delta-3Q^2)>=-1 by min-max, while the two translation functions partial_j Q give eigenvalue -1, so equality holds at a=3. Strict monotonicity of discrete eigenvalues under the strictly positive change (3-a)Q^2 gives the strict bound for a<3; if the second level is the essential-spectrum threshold zero, the bound is immediate.

Decoupling of separated wells then implies that the first N levels of the original V_R tend to -1, while the (N+1)-st level of a V_R tends to lambda_2(-Delta-aQ^2)>-1 (or to zero if there is no such bound state). Therefore, for all sufficiently separated wells,

    lambda_(N+1)(-Delta-a V_R) > -S_N(V_R)/N.

Here decoupling follows from translated single-well trial states for the upper bounds and IMS localization, with cutoffs on increasing separated balls, for the lower bounds. This example is **not** an exact self-consistent violating optimizer. Its role is to show precisely that an opposite spectral estimate cannot hold for general multiple-well potentials. The unexploited hypothesis in a successful contradiction must include the strict improvement C>C_1 and exact self-consistency, rather than merely N>=2.

## 7. The precise remaining second-variation problem

A proof by instability would need the following genuinely new statement:

> For every real self-consistent finite-rank optimizing candidate with C>C_1 and smallest violating rank N, there exists a real W such that <W,RW> > (C/4)||W||_2^2.

Equivalently, there must be an admissible external orbital variation violating (6). Such a result would contradict the existence of the finite-rank optimizer and settle the conjecture. The first-variation equation, Pohozaev identity, orthogonality, and the symmetry modes do not supply this strict inequality.

Conversely, (8) is only a necessary local condition. Verifying it for a numerical stationary profile does not prove the profile globally optimal or yield a counterexample; its quotient still has to exceed C_1. This note establishes no universal instability theorem.

The useful exact restrictions presently obtained are (3)–(4), the fully constrained Hessian (5)–(8), and the symmetry identities (9). They identify a nonperturbative spectral obstacle without replacing it by a radial or small-secondary-mode assumption.

## 8. Sources and scope of attribution

1. R. L. Frank, D. Gontier, M. Lewin, *The nonlinear Schrödinger equation for orthonormal functions II. Application to Lieb–Thirring inequalities*, arXiv:2002.04964v3, Theorem 6 and Section 3. https://arxiv.org/html/2002.04964v3
2. R. L. Frank, D. Gontier, M. Lewin, *Optimizers for the finite-rank Lieb–Thirring inequality*, arXiv:2109.05984v2, Theorem 3 and Section 5. The spectral gap and optimizer regularity are explicitly part of this existing work. https://arxiv.org/html/2109.05984v2

The rank-compression calculation is proved directly here. A targeted literature search did not locate this exact presentation, but this is not a novelty determination. The Hessian is standard second-order perturbation theory, checked here with all signs, coefficients, and constraints needed for this problem. None of these statements is presented as a resolution of the two-dimensional endpoint conjecture.
