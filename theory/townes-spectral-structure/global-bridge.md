# Global restrictions and the limit of scalar averaging

Date: 2026-10-15. This is a self-contained derivation for the two-dimensional, exponent-one Lieb–Thirring problem. It does not prove the conjectured sharp constant. No historical originality is asserted for the elementary consequences below.

## 1. Setting

For a finite-rank orthogonal projection P with real orthonormal H1 orbitals, write

    rho_P = sum_i phi_i^2,
    T(P) = sum_i ||grad phi_i||_2^2,
    F(P) = int rho_P^2,
    C_N = sup_(0<rank P<=N) F(P)/T(P),
    C_1 = 2/M_c,  L_N = C_N/4.

The scalar inequality is int f^4 <= C_1 ||f||_2^2 ||grad f||_2^2. Suppose N is the smallest violating rank and C_N=(1+delta)C_1, delta>0. Existing finite-rank optimizer theory supplies a real rank-N optimizer P with

    V=2 rho_P/C_N,
    (-Delta-V)phi_i=-e_i phi_i,
    e_1>=...>=e_N>0.

The e_i are the magnitudes of the N lowest occupied eigenvalues. There may be further unoccupied negative eigenvalues. Set S=sum_i e_i. Summing the eigenvalue equations and using F(P)=C_N T(P) gives

    S = (2/C_N)F(P)-T(P) = T(P),
    L_N int V^2 = S.

Minimality of N means C_k=C_1 and L_k=L_1 for every 1<=k<N. The previously derived real Haar estimate gives delta<=1/(N+1).

## 2. A global occupied spectral interval

Apply the rank-one spectral inequality to this same V:

    e_1 <= L_1 int V^2 = S/(1+delta).

Apply the rank-(N-1) inequality, again to the same V:

    S-e_N <= L_1 int V^2 = S/(1+delta).

Therefore

    delta S/(1+delta) <= e_N <= e_i <= e_1 <= S/(1+delta),
    e_N/e_1 >= delta.                                      (1)

This is nonperturbative and does not assume separated, radial or comparable-shape cores. In terms of the exponential length scales ell_i=e_i^(-1/2),

    max_i ell_i / min_i ell_i <= delta^(-1/2).                (2)

Together with N<=delta^(-1)-1, this says that a counterexample with a prescribed positive fractional improvement has both a bounded first rank and bounded occupied spectral scale ratios. It does not supply a bound uniform as delta tends to zero. Nor does it prove control of spatial diameter or of orbital shapes.

These inequalities follow from already-known lower-rank inequalities plus self-consistency. They must not be presented as a new general Lieb–Thirring theorem.

## 3. Every occupied-space split must carry definite overlap

Take any orthogonal decomposition P=A+B with 1<=rank A,rank B<N. Define scalar-constant deficits

    d(A)=C_1 T(A)-F(A)>=0,
    d(B)=C_1 T(B)-F(B)>=0.

Since rho_P=rho_A+rho_B and kinetic energy is additive,

    2 int rho_A rho_B
       = F(P)-F(A)-F(B)
       = delta C_1 T(P)+d(A)+d(B).                          (3)

Consequently every such split obeys

    int rho_A rho_B >= (delta C_1/2)T(P)
                       = delta F(P)/(2(1+delta)).            (4)

The statement applies to arbitrary rotations of the occupied space, not only the eigenbasis or a particular graph of orbital overlaps. A proposed violating optimizer cannot contain a nearly detached occupied subspace unless its relative improvement is correspondingly small.

Equation (3) is also exact accounting of the obstacle: lower-rank deficits must be paid for by inter-subspace attraction. Knowing that both deficits are nonnegative does not bound the attraction from above. Thus (3) alone cannot exclude collective binding.

## 4. Why small projector deficit does not imply small orbital deficits

Let q_m be compactly supported, real, L2-normalized approximations to a normalized Townes optimizer, chosen so that

    t_m=||grad q_m||_2^2 -> t>0,
    b_m=int q_m^4 -> C_1 t.

Translate two copies q_(1,m),q_(2,m) to have disjoint supports, and form the orthonormal orbitals

    phi_(+,m)=(q_(1,m)+q_(2,m))/sqrt(2),
    phi_(-,m)=(q_(1,m)-q_(2,m))/sqrt(2).

Their projector is unchanged by this occupied-space rotation. Exactly,

    T(P_m)=2t_m,  F(P_m)=2b_m,
    F(P_m)/T(P_m) -> C_1.

Yet each displayed orbital satisfies

    ||grad phi_(+,m)||_2^2=||grad phi_(-,m)||_2^2=t_m,
    int phi_(+,m)^4=int phi_(-,m)^4=b_m/2,
    d(phi_(+,m))=d(phi_(-,m))=C_1 t_m-b_m/2 -> C_1 t/2>0.

Thus projector near-saturation can coexist with order-one scalar deficits in an orthonormal basis. For every rank-one projector R, one also has

    ||P_m-R||_HS^2 = 3-2 Tr(P_m R) >= 1.

Projector near-saturation does not even force the rank-two projector close to a rank-one projector in Hilbert–Schmidt distance. There is a good localized basis in this example, but finding a good basis or a cluster decomposition is an additional theorem, not a consequence of the small numerical deficit.

This example is below the conjectured threshold; it is not a counterexample to the main conjecture, and it does not exclude a stronger theorem using strict improvement and exact optimizing self-consistency. It disproves precisely the inference from small deficit alone to small component deficits or rank-one closeness.

## 5. An optimal limitation of universal positive scalar averaging

Consider proofs that apply scalar GN to constant linear combinations

    f_a(x)=a dot Phi(x),  Phi=(phi_1,...,phi_N),

then average with a nonnegative measure. Nonzero coefficient vectors can be normalized to |a|=1 by absorbing |a|^4 into the measure. Let K_ij=<grad phi_i,grad phi_j>. The averaged scalar bound is

    int [int (a dot Phi(x))^4 dnu(a)] dx
       <= C_1 Tr(K M),
    M=int aa^T dnu(a).

Suppose this averaging is to yield a universal algebraic estimate by imposing

    int (a dot v)^4 dnu(a) >= |v|^4 for every v in R^N,
    M <= b I.

Then necessarily

    b >= (N+2)/3.                                          (5)

Proof: averaging the first condition over uniform v on S^(N-1), and using E_v(a dot v)^4=3/[N(N+2)], gives

    nu(S^(N-1)) >= N(N+2)/3.

On the other hand, Tr M=nu(S^(N-1))<=bN. Combine these statements. Equality is attained by Haar measure of total mass N(N+2)/3, for which M=((N+2)/3)I and the quartic majorization is equality. Thus the loss is exactly optimal within this class, rather than an accident of choosing uniform random coefficients.

For complex constant combinations the corresponding argument gives the optimal loss (N+1)/2, using E|<a,v>|^4=2/[N(N+1)]. The real representation of an optimizing potential is therefore useful, but it does not make scalar averaging sharp at rank greater than one.

Scope: (5) does not rule out measures depending on the spatial range of Phi, or proofs using information beyond the displayed quartic majorization and kinetic matrix control. For disjoint cores, coordinate averaging is sharp because Phi(x) lies on the union of coordinate axes. Spatial geometry matters.

There is nevertheless an explicit smooth rank-two family for which even adapting the measure to the orbitals cannot remove this loss while retaining pointwise quartic domination:

    phi_1(x,y)=sqrt(2/pi) x exp(-(x^2+y^2)/2),
    phi_2(x,y)=sqrt(2/pi) y exp(-(x^2+y^2)/2).

These orbitals are orthonormal, K=2I, and Phi(x,y)/|Phi(x,y)| runs through every unit direction as the polar angle varies. Pointwise quartic domination therefore requires the universal angular condition. Any such scalar averaging has loss at least 4/3. This is a failure of that proof mechanism, not of the desired inequality: directly F(P)=1/pi, T(P)=4, so F/T=1/(4pi)<C_1.

## 6. Exact amplitude–orientation formulation of the remaining global problem

For a real family set r=sqrt(rho), n=Phi/r on {r>0}. Almost everywhere,

    |n|=1,
    int r^2 n n^T = I_N,
    T(P)=int |grad r|^2 + int r^2 |grad n|^2.                 (6)

The second term is the kinetic cost of changing the occupied direction in space. The target inequality is exactly

    int r^2 |grad n|^2
       >= (1/C_1)int r^4 - int |grad r|^2                   (7)

under the global matrix normalization in (6). Scalar GN applied to r only gives int r^4<=C_1 N int|grad r|^2; it loses the directional term that must resolve the collective problem. Constant-coefficient random averaging similarly cannot recover it sharply, as Section 5 proves.

Equation (7) is an exact variational reformulation, not a proved additional inequality. It states the global mathematical work still needed: quantify the unavoidable spatial variation of an orthogonal family at the same sharp constant as a single scalar core, allowing both overlap and fragmentation. Simply naming (7) a universal principle would leave the original problem untouched.

## 7. Source and scope

The optimizer existence, self-consistent equation and occupied spectral ordering used here are inherited from:

R. L. Frank, D. Gontier and M. Lewin, *Optimizers for the finite-rank Lieb–Thirring inequality*, American Journal of Mathematics 147 (2025), 503–560; arXiv:2109.05984. Publisher-hosted manuscript: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-frank-gontier-lewin-FINAL.pdf

Equations (1)–(4), the counterexample in Section 4 and the averaging optimization in Section 5 are derived explicitly above. They have not undergone a historical-priority determination. They neither establish an arbitrary-rank improvement to the best known Lieb–Thirring constant nor settle the two-dimensional exponent-one conjecture.
