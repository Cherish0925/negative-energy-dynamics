# Global occupation reduction, self-consistent states, and collective collapse

Date: 2026-10-11. This note treats the two-dimensional common-density cubic NLS. It derives exact global reductions of the proposed sharp inequality, checks an associated exact-collapse implication, and identifies where amplitude–direction arguments lose the required information. It does not prove or disprove the sharp inequality. The finite-rank optimizer input is explicitly inherited from Frank–Gontier–Lewin (FGL), not claimed as a new result.

## 1. Precise target and an exact occupation-layer identity

Let Q solve -Delta Q+Q-Q^3=0, M_c=||Q||2^2, and C_1=2/M_c. For a finite-rank orthogonal projection P with H1 range, write

    rho_P(x)=sum_j |phi_j(x)|^2,
    T(P)=Tr(-Delta P),
    D(P)=C_1 T(P)-||rho_P||2^2.

The central conjectural statement is D(P)>=0 for every such P, with arbitrary finite rank. It is exactly the sharp orthonormal kinetic inequality corresponding to the two-dimensional gamma=1 Lieb–Thirring problem.

There is no need to solve different fractional occupation spectra separately. In this note Gamma denotes the spatial density operator sum_j |u_j><u_j| on L2; its nonzero eigenvalues equal those of the component Gram matrix (int u_i conjugate(u_j)), so its operator norm is the largest conserved occupation. Let Gamma>=0 have finite trace and finite kinetic energy, and let m=||Gamma||op>0. Put P_t=1_(Gamma>t), 0<t<m. The spectral layer-cake representation gives

    Gamma=int_0^m P_t dt,
    rho_Gamma=int_0^m rho_(P_t) dt,
    T(Gamma)=int_0^m T(P_t)dt.

Every P_t has finite rank for t>0. The Hilbert-space variance identity yields exactly

    C_1 m T(Gamma)-||rho_Gamma||2^2
      =m int_0^m D(P_t)dt
        +1/2 int_0^m int_0^m
                   ||rho_(P_s)-rho_(P_t)||2^2 ds dt.       (1)

Proof: expand the last squared norm and integrate. Its value is
m int||rho_(P_t)||2^2dt-||int rho_(P_t)dt||2^2, which cancels the corresponding term from m intD(P_t). For finite rank this is ordinary finite algebra. The trace-class version follows by monotone spectral truncation; a standard nonsharp Lieb–Thirring bound ensures the relevant density integrals are finite, and the nonnegative difference term admits the same limit.

Consequences, all global and nonperturbative:

- Positivity for every finite-rank projection proves the sharp inequality for every finite-trace occupation spectrum.
- A negative deficit for any occupation operator forces D(P_t)<0 for at least one of its nested spectral projections. Therefore a counterexample can always be chosen with equal occupied eigenvalues.
- The additional double integral is nonnegative. Unequal occupation values introduce an exact density-variance contribution; they cannot conceal a counterexample that does not already occur at a projection level.

For example, Gamma=P1+eta P2 with orthogonal rank-one P1,P2 and 0<eta<1 gives

    D(Gamma)=(1-eta)D(P1)+eta D(P1+P2)
               +eta(1-eta)||rho_(P2)||2^2.

This identity does not supply positivity of the unresolved equal-occupation projection term.

## 2. Finite-rank optimizers reduce failure to a self-consistent stationary state

Define

    C_N=sup { ||rho_Gamma||2^2/[||Gamma||op T(Gamma)] :
              0<rank(Gamma)<=N }.

At d=2,p=2, FGL Theorem 6(i)–(ii) establishes existence of a finite-rank optimizer, with equal nonzero occupation numbers after its stated normalization. The optimizer occupies the first R negative eigenfunctions of its self-consistent Schrödinger operator, for some R<=N. Dividing by its common occupation reduces it to a rank-R projection maximizing the same quotient. Thus C_N also equals the supremum over projections of rank at most N.

If the conjecture fails, choose the smallest N with C_N>C_1. Its optimizer must have rank exactly N; otherwise it contradicts minimality. Let phi_1,...,phi_N be an orthonormal basis diagonalizing the stationary multipliers, rho=sum|phi_j|^2, and C=C_N. Direct differentiation of F/T gives

    (-Delta-g rho)phi_j=-e_j phi_j,
    g=2/C, e_j>0.                                        (2)

The coefficient is 2/C because the quartic density functional has derivative 4rho phi_j and kinetic energy has derivative 2(-Delta phi_j). Set

    psi_j=sqrt(g) phi_j, rho_psi=sum|psi_j|^2.

Then

    -Delta psi_j-rho_psi psi_j=-e_j psi_j,
    <psi_i,psi_j>=g delta_ij,
    g=2/C<M_c.                                           (3)

The self-consistent profile is regular and exponentially decaying. The finite-rank eigenfunctions first bootstrap to bounded continuous functions; their density tends to zero at infinity, and e_j>0 gives the usual negative-eigenvalue exponential decay. In particular, the profiles have finite second moments.

The two-dimensional Pohozaev identity gives

    E(psi)=1/2 sum||grad psi_j||2^2-1/4 int rho_psi^2=0.   (4)

One short derivation differentiates the stationary action under the common mass-preserving spatial dilation psi_j(x)->s psi_j(sx). Every individual mass is unchanged while E scales by s^2. Therefore stationarity forces E=0.

Conversely, any nonzero orthogonal common-density stationary family of the form (3), with equal mass g<M_c and sufficient decay for Pohozaev, immediately violates the target inequality. Indeed, P=sum |psi_j/sqrt(g)><psi_j/sqrt(g)| is a projection, and (4) gives

    ||rho_P||2^2/T(P)=2/g>2/M_c.                         (5)

Thus, using the known finite-rank optimizer theorem, the target inequality is equivalent to the following nonlinear statement:

> Every localized orthogonal stationary family for the two-dimensional common-density cubic system, with equal component mass g, has g>=M_c; equivalently its total mass is at least N M_c.

It would suffice to prove this for the self-consistent finite-rank optimizing families selected by FGL. Demanding it for all stationary states is a stronger-looking formulation but is equivalent here because violation of either statement supplies a violating projection and a projection violation supplies a stationary optimizer.

This is an exact reduction, not a proof of the stationary mass bound. The ordinary scalar/vector GN inequality only gives total mass >=M_c, which is weaker by the factor N. Orthogonality has to supply the missing information.

## 3. A counterexample would produce an exact collective collapse

The reduction has a direct dynamical consequence stronger than merely constructing negative-energy initial data. Suppose (3) exists with g<M_c. Let h=T-t>0, and define

    U_j(t,x)=h^-1 exp(-i|x|^2/(4h)+i e_j/h) psi_j(x/h).  (6)

This is an exact solution of

    i U_j,t+Delta U_j+rho_U U_j=0.

To check signs, the stationary evolution v_j(s,y)=exp(i e_j s)psi_j(y) solves the same system. Substituting u=h^-1 exp(-i|x|^2/(4h))v(1/h,x/h) cancels the dilation and quadratic-phase terms, leaving h^-3 exp(-i|x|^2/(4h)) times i v_s+Delta v+rho_v v. No complex conjugation is required in this convention.

Orthogonality makes the different frequency phases harmless for the Gram matrix:

    int U_i conjugate(U_j)=g delta_ij.

Every component concentrates its full mass g at the same point, and the total concentrated mass is N g. The limiting localized Gram matrix is g I_N, not rank one. This is therefore a genuinely collective core in the precise occupation sense.

For every stationary component, the current is divergence free. Exponential decay gives int x.Im(conjugate(psi_j)grad psi_j)=0. Consequently

    sum||grad U_j||2^2=h^-2 sum||grad psi_j||2^2
                        +1/4 sum||x psi_j||2^2,
    E(U)=1/8 sum||x psi_j||2^2>0.

The solution has finite variance and finite-time H1 blowup, even though its largest occupied mass is g<M_c.

Conversely, if the sharp inequality is true, energy conservation implies for every solution with ||Gamma||op=m<M_c,

    E(U)>=1/2(1-m/M_c) sum||grad U_j||2^2.

This bounds the H1 norm and excludes finite-time blowup. Hence, with the FGL optimizer input, deciding the sharp inequality is also equivalent to deciding whether such sub-M_c-maximal-occupation collective collapse can occur. Failure of the inequality necessarily has an exact pseudoconformal representative (6).

All ingredients in this implication—finite-rank optimizer existence, its Euler–Lagrange equation, Pohozaev, and pseudoconformal symmetry—are existing mathematical structures. Their combination precisely identifies the physical alternative but does not settle which alternative holds.

## 4. What the amplitude–direction decomposition does and does not prove

For a projection P, collect its orbitals into U(x) in C^N. Put R=|U|=sqrt(rho_P), v=U/R where R>0. Then

    |v|=1,
    T(P)=int |grad R|^2+int R^2|grad v|^2,               (7)
    int R^2 vv*=I_N,
    int R^2=N.                                         (8)

The cross term in (7) vanishes because Re(v*partial_k v)=0. The formulas are interpreted almost everywhere and extended across zeros by the usual Sobolev approximation.

Applying scalar GN to R alone loses a factor N:

    int R^4<=C_1 N int|grad R|^2.

One cannot repair this by asserting intR^2|grad v|^2 >=(N-1)int|grad R|^2. That assertion is false: take N disjointly supported normalized scalar functions. On each support v is a constant coordinate vector, so the direction energy is zero, while the amplitude energy is positive. The desired sharp bound in this case instead follows by applying scalar GN separately on the disjoint components.

A pointwise unitary rotation can send v(x) to one fixed coordinate vector and remove the direction variation, but it changes the Gram matrix from I_N to a rank-one matrix. Such a rotation is not an admissible operation on the variational problem. Constant unitary rotations preserve the Gram matrix and energy, but do not remove the spatial variation of v.

For a real stationary basis, local rotations yield the exact Wronskian identity

    div(psi_b grad psi_a-psi_a grad psi_b)
       =(e_a-e_b)psi_a psi_b.                            (9)

This follows directly from (3). It expresses the constrained orbital stationarity but has no fixed sign. The local rotation mechanism therefore does not by itself eliminate multimode optimizers.

The point where a nonperturbative proof is needed is visible in (7)–(8): spatial fragmentation may avoid direction energy, whereas overlap forces directional variation. A successful estimate has to treat both mechanisms together while retaining the individual occupation constraint. Neither scalar GN on the total amplitude nor pointwise alignment retains that information.

## 5. Averaging scalar inequalities has an exact but insufficient constant

For every unit a in C^N, the scalar combination f_a=a*U has mass one. Scalar GN gives int|f_a|^4<=C_1 int|grad f_a|^2. Averaging a uniformly on the complex unit sphere uses

    E_a |a*U|^4=2|U|^4/[N(N+1)],
    E_a |a*grad U|^2=|grad U|^2/N.

The result is only

    ||rho_P||2^2<=C_1 (N+1)/2 T(P).                     (10)

This loss is exact for that averaging calculation; it is not an omitted choice of phase or normalization. Recovering the factor one would require a global lower bound on the average scalar GN deficit over all directions, which is another substantive geometric inequality rather than a free consequence of the scalar theorem.

## 6. Derivation of a genuinely global separable-family exclusion

There is a nonperturbative family for which an even stronger constant follows from known one-dimensional sharp theory. For a one-dimensional positive finite-rank operator A, define M_A=Tr A, K_A=Tr(-partial_x^2 A), B_A=int rho_A^2. Sharp one-dimensional Lieb–Thirring at exponent 3/2 has constant 3/16. Schatten Holder gives, for V=a rho_A,

    a B_A-K_A
      <=[Tr(A^3)]^(1/3) (3/16)^(2/3)
                          a^(4/3) B_A^(2/3).

Optimizing a>0 yields

    B_A^2<=[Tr(A^3)] K_A/3.                             (11)

The Schatten moment is Tr(A^3), not Tr(A^2); scaling A by a constant also confirms the required homogeneity.

For contractions 0<=A,B<=1, Tr(A^3)<=M_A and Tr(B^3)<=M_B. For the Cartesian tensor product Gamma=A tensor B,

    ||rho_Gamma||2^2=B_A B_B
       <=(1/3)sqrt(M_A M_B K_A K_B)
       <=(K_A M_B+M_A K_B)/6
        =T(Gamma)/6.                                   (12)

Convexity of the squared density norm extends (12) to finite convex combinations of these tensor-product contractions. This includes full rectangular Cartesian orbital families. It does not include arbitrary irregular subsets of a product orbital basis.

The constant 1/6 is strictly below C_1, with an elementary explicit witness and no numerical Townes input. Put ell=log(2) and

    q(x)=sech(|x|)/sqrt(2pi ell), x in R2.

Then ||q||2=1. The radial integrals int_0^infinity r sech^2(r)dr=ell and int_0^infinity r sech^4(r)dr=(4ell-1)/6 give

    T(q)=(2ell+1)/(6ell),
    int|q|^4=(4ell-1)/(12pi ell^2),
    int|q|^4/T(q)=(4ell-1)/[2pi ell(2ell+1)].

The elementary bounds .69<ell<.70 and pi<22/7 imply that this ratio is strictly greater than 1.76/10.56=1/6. For completeness, the series ell=2 sum_(k>=0) 1/[(2k+1)3^(2k+1)] gives the sharper lower and upper bounds 56/81<ell<25/36. Thus C_1>1/6, equivalently M_c<12, without computing Q. The product of identical normalized one-dimensional sech optimizers attains 1/6 in the separable family itself.

This excludes that complete global separable family from producing a counterexample. It does not exclude general correlated orbitals or nonrectangular occupation patterns and is not a proof of the full conjecture.

## 7. Attribution and unresolved step

Primary source:

Rupert L. Frank, David Gontier, Mathieu Lewin, *The nonlinear Schrödinger equation for orthonormal functions II. Application to Lieb–Thirring inequalities*, arXiv:2002.04964v3. Theorem 6(i)–(ii), with d=2,p=2, gives the finite-rank optimizer and self-consistent equal-occupation structure used in Section 2. The restrictions in Theorems 1 and 2 do not settle the d=2,gamma=1 endpoint. https://arxiv.org/html/2002.04964v3

The new work in this note is the explicit checking and organization of the global reductions, their exact collapse implication, and the success/failure boundaries of the proposed mechanisms. No historical priority is claimed for these algebraic consequences. The unresolved mathematical statement remains D(P)>=0 for every finite-rank projection, equivalently the stationary equal-mass bound in Section 2. None of Sections 1–6 proves that statement.
