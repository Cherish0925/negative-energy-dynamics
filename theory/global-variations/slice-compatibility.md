# A quantitative remainder in the one-dimensional matrix estimate

This calculation retains a nonnegative term in Read–Schulz's proof and establishes a uniform strict improvement over the lifted coefficient on the explicit class that saturates the one-dimensional Hilbert-valued inequality. It does not improve the unrestricted two-dimensional constant: a quantitative extension to near-saturating families is still missing.

## Source and notation

Primary text: Larry Read and Marvin R. Schulz, *The sharp one-dimensional Lieb–Thirring inequality for the sum of eigenvalues*, arXiv:2609.10478v2, https://arxiv.org/pdf/2609.10478, §§2.1–2.2, equations (2.10), (2.12), (2.13), and Lemma 6. The following notation agrees with that proof.

Let the orthonormal rows psi_i(x) belong to a Hilbert space H. Set W:H→C^N by (Wf)_i=<psi_i,f>, Q=WW*, A(x)=integral_{-infinity}^x Q(t)dt, and S=integral Tr Q^3. Then A'=Q and A(-infinity)=0, A(infinity)=I. For 0<alpha<pi put

    q_alpha(s)=-alpha tan(alpha(s-1/2)).

In an orthonormal eigenbasis of A, with eigenvalues lambda_i, define

    B_ij=q_alpha((lambda_i+lambda_j)/2) Q_ij,
    theta_i=alpha(lambda_i-1/2)/2,
    C_ij=Q_ij/cos(theta_i+theta_j),
    h(t)=sin(t)/t-cos(t),
    g_ik=cos(theta_i+theta_k) h(theta_i-theta_k).

The matrix C is nonnegative. Read–Schulz prove that g_ik=|v_i-v_k|^4 for vectors v_i in a finite-dimensional real Hilbert space. Their exact integrated identity is

    T_x-alpha^2 S/4
      = integral ||W'-B W/2||_HS^2 + (1/4) integral G_alpha,

    G_alpha=alpha^2 sum_ik Re((C^2)_ik C_ki) g_ik >=0.       (1)

The cubic summands need not be nonnegative separately. Consequently a pointwise scalar lower bound for g cannot simply be substituted into this sum.

## A dimension-independent algebraic lower bound

At any fixed x let z be a standard Gaussian vector in the auxiliary space containing the v_i, sigma_i=z·v_i, and

    (K_z)_ik=(sigma_i-sigma_k)^2 C_ik.

The identity (2.13) in the source and the Gaussian fourth moment give

    G_alpha=(2 alpha^2/3) E_z Tr(C K_z^2).

For C>=0 and Hermitian K, weighted Cauchy–Schwarz gives

    Tr(C K^2) >= (Tr(CK))^2/Tr C,

with the zero-matrix case interpreted separately. Furthermore

    Tr(C K_z)=sum_ik |C_ik|^2 (z·(v_i-v_k))^2.

Write M=sum_ik |C_ik|^2 (v_i-v_k)(v_i-v_k)^T. Then

    E(Tr(C K_z))^2=(Tr M)^2+2 Tr(M^2) >=(Tr M)^2,
    Tr M=sum_ik |C_ik|^2 sqrt(g_ik).

Therefore

    G_alpha >= [2 alpha^2/(3 Tr C)]
                 [sum_ik |C_ik|^2 sqrt(g_ik)]^2.            (2)

There is no factor N in (2). Its normalization, however, involves Tr C and the cumulative eigenvalue-dependent weights; (2) is not yet a rank-uniform stability theorem in a standard kinetic or density norm. In particular g_ik vanishes when lambda_i=lambda_k, and the cosines degenerate near the endpoints as alpha tends to pi.

Equation (2) implies the pointwise exact classification

    G_alpha=0 iff [A,Q]=0.                                 (3)

Indeed sqrt(g_ik)>0 when lambda_i differs from lambda_k, so zero G forces C_ik=Q_ik=0 across distinct eigenspaces. Conversely commuting A and Q makes all contributing g_ik zero. This concerns G, not the complete deficit in (1).

## A uniform gap on the exact one-dimensional saturation class

Let b_1,...,b_N be an arbitrary orthonormal family in H1(R). For nonnegative weights c_i, set rho_c=sum_i c_i|b_i|^2, rho_1=sum_i|b_i|^2 and T_b=sum_i||b_i'||_2^2. Pointwise Holder and then integral Cauchy–Schwarz give

    rho_c <= rho_(c^4)^(1/4) rho_1^(3/4),
    integral rho_c^2 <= [(sum_i c_i^4) integral rho_1^3]^(1/2).

Applying the sharp scalar orthonormal one-dimensional inequality of Read–Schulz to rho_1 proves

    integral rho_c^2 <= (2/pi) [(sum_i c_i^4) T_b]^(1/2).   (4)

This is a direct consequence of the theorem proved in the cited preprint, with arbitrary rank and arbitrary weights. The coefficient 2/pi is sufficient below; it is not asserted to be sharp for (4).

Now fix arbitrary positive lambda_i, arbitrary centers x_i, and define

    a_i(x)^2=(lambda_i/pi) sech(lambda_i(x-x_i)),
    phi_i(x,y)=a_i(x)b_i(y).

The phi_i are orthonormal, regardless of the overlaps between the a_i. Direct integration gives

    integral a_i^2=1,  integral |a_i'|^2=lambda_i^2/8,
    integral a_i^4=2lambda_i/pi^2,
    integral a_i^6=lambda_i^2/(2pi^2).

At each x, the slice operator has mutually orthogonal eigenvectors b_i and eigenvalues a_i(x)^2. Thus these families exactly satisfy D_x=0. They include independent scales and centers, and are not restricted to complete tensor-product projections.

Cauchy–Schwarz in x implies

    integral a_i^2 a_j^2 <= 2sqrt(lambda_i lambda_j)/pi^2.

Since every transverse overlap integral |b_i|^2|b_j|^2 is nonnegative, put c_i=sqrt(lambda_i) and use (4):

    F <= (2/pi^2) integral (sum_i sqrt(lambda_i)|b_i|^2)^2
      <= (4/pi^3) [(sum_i lambda_i^2) T_b]^(1/2).

The exact kinetic identities are T_x=(sum_i lambda_i^2)/8 and T_y=T_b. Consequently

    F <= (8sqrt(2)/pi^3) sqrt(T_x T_y)
      <= (4sqrt(2)/pi^3)(T_x+T_y),

or equivalently

    T >= [pi^3/(4sqrt(2))] F.                            (5)

The coefficient pi^3/(4sqrt(2)) is strictly larger than sqrt(3) pi because pi^2>4sqrt(6). Thus on this entire explicit saturation class,

    D_y+[(pi/2)sqrt(S)-sqrt(3)F/sqrt(S)]^2
       >= [pi^3/(4sqrt(2))-sqrt(3)pi] F.                  (6)

The positive coefficient in (6) is independent of rank, centers and all scale ratios. This is a bound for the class just defined; a proof that it encompasses every equality case requires the separate rigidity argument and its regularity hypotheses. No such classification is assumed in proving (5).

## Why this does not yet improve the unrestricted planar constant

For H=L2(R_y), the exact planar decomposition of R25 remains

    T-sqrt(3) pi F
       =D_x+D_y+[(pi/2)sqrt(S)-sqrt(3) F/sqrt(S)]^2.

Let R_alpha denote the right side of (2). At fixed alpha, the exact statement is

    D_x >= (1/4) integral R_alpha - (pi^2-alpha^2)S/4.

Consequently D_x >= (1/4) limsup_{alpha up to pi} integral R_alpha. It would be incorrect to insert the fixed-alpha remainder directly in D_x while omitting the negative correction. A positive lower bound for the limiting expression by cF has not been established. Such a bound would require coupling it with the square residual in (1), the transverse gamma=3/2 deficit, and the integrated Cauchy–Schwarz deficit. Neither (2) nor equality classification (3) supplies that coupling.

Equation (6) proves a uniform gap on the explicit exact-saturation class, not merely nonattainment of the lifting constant there. Extending it to near-saturation of the full planar bound requires a quantitative joint estimate involving all three deficits, or a weaker one-sided approximation that preserves density while allowing kinetic energy to be discarded. Small D_x alone does not imply approximation by exact channels in the full homogeneous H1 norm: the rank-one counterexample below rules out that proposed intermediate theorem. Rank, translations, dilations and separation of distinct channels also prevent an inference from continuity around individual finite-rank families to a uniform neighborhood.

No proof of the two-dimensional sharp conjecture, no unrestricted improvement over sqrt(3) pi, and no counterexample is claimed in this note.

## Near-equality hypothesis must be joint

The following exact construction excludes a D_x-only full homogeneous H1 stability statement, even at rank one. Let a>0 be a normalized quintic soliton as above. Choose real normalized smooth compactly supported b_0,b with b_0 supported in (-2,-1) and b supported in (-1/2,1/2). Set

    b_k(y)=sqrt(k) b(k(y-2)),  epsilon=1/k,
    t_0=||b_0'||_2^2>0,  t_b=||b'||_2^2>0.

Then b_0 and b_k, and their derivatives, have disjoint supports, and ||b_k'||_2^2=k^2 t_b. For a bounded real smooth f with bounded derivative and nonzero variance under the probability measure a^2 dx, define

    phi_epsilon(x,y)
      =a(x)[sqrt(1-epsilon^2 f(x)^2)b_0(y)
                   +epsilon f(x)b_k(y)].

Take epsilon ||f||_infinity<1. The transverse vector in brackets has norm one at every x, so ||phi_epsilon||_2=1 and S=integral a^6 exactly. Put m_j=integral a^2 f^j. Differentiating the unit vector gives the exact formulas

    D_x=epsilon^2 integral a^2 f'^2/(1-epsilon^2 f^2)
          =O(epsilon^2),
    T_y=t_0(1-epsilon^2 m_2)+t_b m_2.

Nevertheless the y-gradient stays a positive distance from that of every single product A(x)B(y), without any soliton restriction on A. Indeed e_0=b_0'/sqrt(t_0) and e_k=b_k'/(k sqrt(t_b)) are orthonormal in L2(R_y), and

    partial_y phi_epsilon
       =[sqrt(t_0) a sqrt(1-epsilon^2 f^2)] e_0
                       +[sqrt(t_b) a f] e_k.

The Gram matrix of the two displayed x-dependent coefficients converges to

    G = [[t_0,                  sqrt(t_0 t_b) m_1],
         [sqrt(t_0 t_b) m_1,     t_b m_2            ]],
    det G=t_0 t_b(m_2-m_1^2)>0.

Every partial_y(A B)=A B' is a rank-one tensor in L2(R_x) tensor L2(R_y). The elementary best rank-one approximation formula therefore yields

    liminf_(epsilon->0) inf_(A,B)
       ||partial_y(phi_epsilon-A B)||_2^2
          >=lambda_min(G)>0.

Equivalently, project onto span{e_0,e_k} and apply the two-column singular-value formula; projection cannot increase the approximation error. This proves the claimed obstruction with a lower bound independent of epsilon.

This is a failure of the proposed strong approximation norm, not a counterexample to the planar bound. In fact F(phi_epsilon) tends to (integral a^4)(integral b_0^4), while the positive transverse energy t_b m_2 survives. Joint smallness of D_x, D_y and the balancing square, or an approximation permitting loss of excess kinetic energy, is therefore the relevant unproved target. No implication from those joint hypotheses is asserted here.
