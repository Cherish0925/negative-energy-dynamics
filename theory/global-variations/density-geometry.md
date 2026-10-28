# Density geometry: exact counterexamples and the tensor-product boundary

Date: 2026-10-16.

This note does not improve the unrestricted two-dimensional Lieb–Thirring constant and does not exclude a minimal violating optimizer. Its completed results are explicit counterexamples to several proposed geometric shortcuts, together with an elementary sharp bound for complete tensor-product projections. The latter is a direct consequence of the classical one-dimensional gamma=3/2 inequality, not a claimed innovation. All constructions and estimates below are analytic; no numerical experiment is used as a premise.

The setting and normalization are those of R23–R25. For a finite orthonormal family Phi=(phi_1,...,phi_N) in H1(R2;C), let

    rho = |Phi|^2,    F = integral rho^2,
    T = sum_j integral |gradient phi_j|^2,
    C1 = 2/Mc,       K1 = 1/C1 = Mc/2.

The desired unrestricted inequality is T >= K1 F. The established one-dimensional lifting bound used in R25 is T >= K0 F, K0=sqrt(3) pi. Numerically K0 approximately 5.441398 and K1 approximately 5.850448; these numerical values are not used in the counterexample proofs.

## 1. The exact complex geometric decomposition, and what it cannot do

Set r=sqrt(rho), n=Phi/r on {rho>0}, and

    a_mu = Im <n,partial_mu n>,
    D_mu n = partial_mu n - i a_mu n,
    j_mu = Im sum_j conjugate(phi_j) partial_mu phi_j = rho a_mu.

Here <z,w>=sum conjugate(z_j)w_j. Since |n|=1, the amplitude, common-phase and projective terms split exactly:

    T = A + J + Gcp,
    A   = integral |gradient sqrt(rho)|^2,
    J   = integral |j|^2/rho,
    Gcp = integral rho sum_mu |D_mu n|^2.                 (1.1)

The orthonormality condition is

    integral rho n n* = I_N.                             (1.2)

The full sphere-direction cost is G=T-A=J+Gcp. For a real family, a=j=0 and G=Gcp. Formula (1.1) is a standard amplitude/phase decomposition, not a new inequality.

There is an immediate restriction on topological approaches at a real finite-rank optimizer. The occupied eigenfunctions can be taken real. The lowest occupied eigenfunction of the scalar attractive Schrödinger operator is strictly positive; choose it as phi_1. Then n_1>0 everywhere. Consequently the direction map lies in an open real hemisphere, and the projective map lies in a single affine chart. It is null-homotopic on its domain. In addition, its Berry connection and curvature vanish identically, because n is real. Thus a putative optimal violating projector need not carry any nonzero CP topological charge or curvature. This does not make its Dirichlet energy vanish; it specifically rules out deriving a positive cost from a forced topological class.

The desired estimate in these variables is G >= K1 F-A. Restating that estimate does not prove it. In particular the right side changes sign, and the counterexamples below distinguish positive standalone lower bounds for G from this signed target.

## 2. One connected annulus: complete intensity overlap, zero current, isotropic kinetic tensor, and Gcp/F -> 0

Fix N>=2. Choose a smooth even nonnegative g supported in (-1,1), positive there, with integral g^2=1. Write

    a = integral |g'|^2 > 0,    b = integral g^4 > 0.

Choose distinct integer angular modes symmetric under k -> -k:

    N=2m+1: k=-m,...,m;
    N=2m:   k=-m,...,-1,1,...,m.

Their sum is zero. Put K_N=sum_k k^2; explicitly

    K_N=N(N^2-1)/12             if N is odd,
    K_N=N(N+1)(N+2)/12          if N is even.

For R>2 define, in polar coordinates,

    phi_k(r,theta) = (2 pi R)^(-1/2) g(r-R) exp(i k theta).  (2.1)

These are smooth compactly supported functions on R2: their support stays away from the origin. Angular integration proves exact orthogonality, and evenness of g gives exact normalization:

    integral |phi_k|^2 = (1/R) integral_(R-1)^(R+1) r g(r-R)^2 dr = 1.

All orbital intensities are identical. On the single connected annulus where the density is positive,

    rho_R = N g(r-R)^2/(2 pi R),
    F_R = N^2 b/(2 pi R),
    A_R = N a,
    G_R = Gcp_R = (K_N/R) integral_(-1)^1 g(s)^2/(R+s) ds,
    J_R = 0.                                               (2.2)

The last assertion follows from sum_k k=0. The normalized direction depends only on theta, so the pullback Berry curvature is identically zero on the positive-density set. Direct angular integration of the real kinetic tensor gives

    T_x=T_y=T/2,    Re sum_k integral partial_x phi_k conjugate(partial_y phi_k)=0.

Thus the family is kinetically isotropic; rotating coordinates or balancing T_x and T_y cannot remove this example.

Since

    1/[R(R+1)] <= (1/R) integral g(s)^2/(R+s) ds <= 1/[R(R-1)],

we obtain the explicit estimate

    0 < Gcp_R/F_R <= 2 pi K_N/[N^2 b (R-1)] -> 0.          (2.3)

If desired, apply the mass-preserving planar dilation phi(x)->lambda phi(lambda x), with lambda^2=F0/F_R. Then F=F0 exactly, Gcp->0, and A->infinity. Every pair of orbital intensities still has normalized overlap exactly one.

**Precisely falsified:** for any fixed N>=2, no positive constant c_N can make

    Gcp >= c_N F

hold merely from orthonormality, complete intensity overlap, zero total/local current, and an isotropic kinetic tensor. The example has a connected positive-density region and is not a pair of separated wells. It also shows that a nonzero two-dimensional projective area is not forced by orthogonality.

**Not falsified:** G >= K1 F-A. In this family A/F grows like R. The amplitude term already makes that signed lower bound nonpositive for large R.

## 3. Fixed N, F and A: no positive weighted spectral gap from these scalars, even with strictly positive density

The preceding annulus changes A/F. A separate construction fixes both quantities and makes the limitation of a weighted-Poincare strategy exact.

### Proposition

For every N>=2, F0>0 and A0>K1 F0, there is a sequence of smooth complex orthonormal families with

    rho_epsilon > 0 everywhere,
    F_epsilon = F0,
    A_epsilon = A0,
    j_epsilon = 0,
    G_epsilon = Gcp_epsilon -> 0.                         (3.1)

For every pair i,j, their intensity overlap satisfies

    integral |phi_i|^2 |phi_j|^2 /
      sqrt[(integral |phi_i|^4)(integral |phi_j|^4)] -> 1.  (3.2)

The projective maps are null-homotopic and constant outside a compact set. The first N-1 positive eigenvalues of the corresponding density-weighted Laplacian tend to zero.

### Construction and proof

Choose a real, nonnegative, radial, smooth compactly supported q with integral q^2=1. Put

    t=integral |gradient q|^2,    b=integral q^4.

Choose q so that t/b<A0/F0. This is possible by compactly supported radial approximation to a normalized scalar sharp optimizer, since A0/F0>K1. Let q_1,...,q_N be disjoint translates of q, and let g_0(x)>0 be a fixed Gaussian. Define the real vector

    f_epsilon=(q_1+epsilon g_0,...,q_N+epsilon g_0)^T,
    M_epsilon=integral f_epsilon f_epsilon^T,
    h_epsilon=M_epsilon^(-1/2)f_epsilon,
    Phi_epsilon=U h_epsilon,                              (3.3)

where U is the unitary discrete Fourier matrix, whose entries all have modulus N^(-1/2). For small epsilon the Gram matrix is positive definite and tends to I. Thus (3.3) is exactly orthonormal and tends strongly in H1 to U(q_1,...,q_N)^T.

The density is strictly positive: f_epsilon is everywhere nonzero and M_epsilon^(-1/2) is invertible. A constant unitary preserves the density and kinetic energy, so

    F_epsilon -> N b,    T_epsilon -> N t.

At epsilon=0 the supports are disjoint and sqrt(rho_0)=sum q_k, hence A_0limit=N t. Lower semicontinuity of the amplitude kinetic energy and the pointwise bound A_epsilon<=T_epsilon give

    A_epsilon -> N t,    G_epsilon=T_epsilon-A_epsilon -> 0.

The same argument in each coordinate gives A_x,e -> Nt/2 and A_y,e -> Nt/2. In the limit, each component of U(q_1,...,q_N) has intensity rho_0/N. Strong H1 and therefore L4 convergence establishes (3.2).

Because h_epsilon is real, j=Im<h_epsilon,gradient h_epsilon>=0, even after the constant unitary. Outside the compact union of the q_k supports, h_epsilon is a positive scalar Gaussian times the fixed vector M_epsilon^(-1/2)(1,...,1)^T. The direction is therefore constant there. Moreover, with v_epsilon=M_epsilon^(1/2)(1,...,1)^T,

    v_epsilon dot h_epsilon = sum_k f_k,epsilon > 0.

The real direction lies in an open hemisphere, proving null-homotopy; after U it remains in a unitarily rotated real locus, with zero Berry curvature.

It remains to fix F and A exactly. First use an isotropic mass-preserving dilation with

    lambda_epsilon^2=F0/F_epsilon.

Then use the area-preserving pullback (x,y)->(s x,y/s). It leaves F unchanged and sends the amplitude energy to

    lambda_epsilon^2 [s^2 A_x,e + s^(-2) A_y,e].           (3.4)

The minimum over s>0 tends to F0 t/b<A0. Hence for all sufficiently small epsilon one can choose s_epsilon, bounded above and away from zero, so that (3.4)=A0. These bounded dilations retain G_epsilon->0, the current condition and all the overlap/topology properties.

For completeness, let

    L_rho = -rho^(-1) div(rho gradient)

on L2(rho dx), with its nonnegative closed quadratic form. For the densities in this construction the Gaussian tail makes its ground-state transform a confining Schrödinger operator, so its spectrum is discrete. Its lowest eigenvalue is lambda_0=0 and is simple. The N functions n_j=phi_j/sqrt(rho) are orthonormal in L2(rho dx); the min-max principle gives

    sum_(k=0)^(N-1) lambda_k(L_rho)
       <= sum_j integral rho |gradient n_j|^2 = G_epsilon. (3.5)

All terms are nonnegative, so lambda_1,...,lambda_(N-1)->0.

**Consequences and scope.** There is no strictly positive universal lower bound for G or for these weighted eigenvalues from N,F,A alone throughout A>K1 F, even if rho is everywhere positive and all displayed orbital intensities nearly coincide. Strong orbital overlap is basis-dependent and does not remove a density bottleneck. The construction is a strengthened version of the separated-packet/unitary-rotation obstruction already present in R23; it should not be counted as a new mechanism or as a strongly bound self-consistent state. It does not address A<K1 F, precisely where the sought LT estimate would demand positive G.

The inequality opposite to (3.5), G >= sum lambda_k, is only the usual min-max principle. Naming it a geometric coercivity theorem would not overcome the degenerating spectra exhibited here.

## 4. Complete tensor-product projections have the sharp coefficient 6

Let A and B be arbitrary nonzero finite-rank orthogonal projections on L2(R), of ranks n and m, with finite kinetic energy. Put

    f_A=integral rho_A^2,    t_A=Tr(-partial_x^2 A),

and similarly for B. No separation or pointwise nonoverlap is imposed on either family.

The classical one-dimensional gamma=3/2 sharp Lieb–Thirring inequality has constant 3/16. Its weighted kinetic dual is

    t(G) >= 3 (integral rho_G^2)^2 / Tr(G^3).              (4.1)

One direct derivation, for V>=0, is

    integral V rho_G - t(G)
      <= Tr(G H_-)
      <= [Tr G^3]^(1/3) [Tr H_-^(3/2)]^(2/3)
      <= [Tr G^3]^(1/3) (3/16)^(2/3) (integral V^2)^(2/3),

where H=-partial_x^2-V. Set V=c rho_G and maximize over c>0; the maximum lower bound is exactly (4.1). Since Tr A^3=n and Tr B^3=m,

    t_A >= 3 f_A^2/n,    t_B >= 3 f_B^2/m.

For P=A tensor B the exact tensor identities give

    rho_P(x,y)=rho_A(x)rho_B(y),
    F(P)=f_A f_B,
    T(P)=m t_A+n t_B.

Consequently

    T(P) >= 3(m/n)f_A^2+3(n/m)f_B^2 >= 6 F(P).            (4.2)

This holds at every finite rank n m and permits arbitrarily strong overlap inside each one-dimensional family. The constant 6 is optimal for each fixed pair n,m. Indeed

    q_a(x)=sqrt(a/2) sech(a x),
    integral q_a^4=a/3,    integral |q_a'|^2=a^2/3.

The rank-one product q_a(x)q_a(y) attains equality. For arbitrary fixed n,m, take compactly supported smooth approximations to q_a and disjoint translates within each one-dimensional factor; their exact projection tensor products approach equality in (4.2).

The coefficient 6 is strictly larger than the scalar planar optimum K1. This strict inequality can be demonstrated without using a numerical Townes mass. The normalized radial trial

    psi(x,y)=sqrt(3/pi) (1+x^2+y^2)^(-2)

has

    integral |psi|^2=1,
    T(psi)=12/5,
    F(psi)=9/(7 pi),
    T/F=28 pi/15 < 6.                                   (4.3)

Therefore K1<=28 pi/15<6. Any projection with T/F<6 cannot be a complete tensor product in any rotated Cartesian coordinate system.

Equations (4.2)–(4.3) also disprove the proposed shortcut that all two-coordinate coupling can be collected into an additional nonnegative term relative to the coefficient-6 tensor bound. Two-dimensional nonseparability can already lower the quotient for a single orbital. This is distinct from increasing the occupied rank.

The scope of (4.2) must not be enlarged silently. It concerns P=A tensor B. It has not been proved here for arbitrary sums of different product projections, for every projector admitting some product orbitals, or for general slice matrices R_x. It is a direct tensorization of a known sharp one-dimensional theorem, not a new unrestricted LT bound.

## 5. Relation to the exact lifting deficits from R25

For arbitrary P, R25 gives, with S=integral Tr(R_x^3),

    T-K0 F = D_x+D_y+[(pi/2)sqrt(S)-sqrt(3)F/sqrt(S)]^2,
    D_x=T_x-(pi^2/4)S >= 0,
    D_y=T_y-3F^2/S >= 0.                                (5.1)

For complete tensor products, (4.2) supplies the genuine quantitative consequence

    D_x+D_y+square >= (6-sqrt(3)pi)F.                     (5.2)

The coefficient in (5.2) is approximately 0.558602. This is a proved joint deficit in that restricted class, including arbitrary factor ranks. It is not a bound for an arbitrary two-dimensional projection.

For a single product orbital the incompatibility of equality conditions in the two one-dimensional steps is already visible. However, mere nonattainment of equality in (5.1), even supplemented by a classification of exact one-dimensional equality cases, does not establish a uniform c>0 over all ranks. This note has not proved the compactness or quantitative estimate needed for that passage. In particular, it does not claim

    D_x+D_y+square >= cF   for every finite-rank P

with any new c>0. The CP counterexamples in Sections 2–3 cannot supply such c either: they target standalone directional costs, whereas (5.1) contains coupled amplitude, slice-spectrum and Cauchy losses.

## 6. Proven output and source attribution

The completed deductions are:

1. The annular family (2.1) explicitly disproves a positive standalone projective-energy bound based on rank, complete orbital intensity overlap, zero current and isotropic kinetic energy.
2. The fixed-(N,F,A) family proves collapse of all first N-1 positive weighted spectral gaps despite strict positivity of rho and almost complete intensity overlap. Its exact limitation A>K1 F is essential.
3. Real scalar-potential optimizers have zero Berry curvature and a hemisphere-valued direction map; a nontrivial CP topological class cannot be assumed at a minimal violator.
4. Complete tensor-product projections obey the known-one-dimensional-theorem consequence T>=6F, with sharp constant. The explicit rational radial trial shows why general two-dimensional coupling cannot be treated as a nonnegative correction to that bound.

None excludes the fully overlapping, nonseparable, self-consistent minimal violating state of R23/R25, and none improves the best unrestricted coefficient used there.

Primary sources checked for attribution:

- A. Laptev and T. Weidl, *Sharp Lieb–Thirring inequalities in high dimensions*, arXiv:math-ph/9903007v2, https://arxiv.org/abs/math-ph/9903007. This supplies the standard sharp gamma>=3/2 theorem; (4.1) is its elementary dual consequence.
- J. E. Harriman, *Orthonormal orbitals for the representation of an arbitrary density*, Physical Review A 24 (1981), 680–682, DOI https://doi.org/10.1103/PhysRevA.24.680. The primary abstract explicitly records arbitrary-density orthonormal constructions and a kinetic decomposition containing the Weizsaecker term. Thus density representation by orthonormal phases and amplitude/directional splitting are not new ideas; the explicit counterexamples above are derived here without invoking uninspected details of that paper.
- R25 records the inspected 2026 sharp one-dimensional matrix results and the finite-rank optimizer theorem. No new theorem about their stability or equality classes is assumed in this note.

Historical priority for the specific counterexample formulations has not been established.
