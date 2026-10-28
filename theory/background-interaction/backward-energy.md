# Polynomial backward estimates for the quadratic quintic candidate

Date: 2026-10-11. This note proves a linear energy estimate for a precisely defined parity-preserving, projected linearized equation around the matched family in [quintic-closure.md](quintic-closure.md). It does not construct a nonlinear blow-up solution or assume the existence of arbitrarily accurate approximate solutions.

## 1. What is proved

Let T be fixed, h=T-t, and lambda(t)=kappa h^2 for a fixed kappa>0. Let k=lambda_t=-2kappa h. Use the smooth odd matched secondary family W_lambda and its exact-Gram correction from [quintic-closure.md](quintic-closure.md). Define the phase-rotated reference field

    A_1(t,x)=lambda^(-1/2)Q(x/lambda) exp(i k x^2/(4lambda)),
    A_sec(t,x)=W_lambda(x),
    omega(t)=lambda^(-2).

The fast scalar phase exp(i theta), theta_t=omega, has already been removed from the primary coordinate. This diagonal phase rotation is an exact operation on the linearized equation: the common-density system is invariant under independent constant phases of each component.

Set rho_A=|A|^2. Regard complex fields as a real Hilbert space with pairing

    (z,w)_R=Re sum_j integral conjugate(z_j)w_j.

The real self-adjoint action Hessian is

    H(t)z=-z_xx-rho_A^2 z
          -4 rho_A A Re(sum_j conjugate(A_j)z_j)
          +omega P_1 z,                             (1)

where P_1 selects the primary component. It is the Hessian of the conserved energy plus omega times half the primary mass. Write Jz=-iz. The rotating-frame unprojected linearized equation has generator JH(t), not a generator estimated by its operator norm lambda^(-2).

Let Q_lambda=lambda^(-1/2)Q(x/lambda), and write (Lambda Q)_lambda for the same scaling of Lambda Q=(1/2+y partial_y)Q. Work in the parity class in which z_1 is even and each secondary component is odd. Define the moving real-linear constraint space X(t) by

    (z_1,Q_lambda)_R=0,
    (z_1,iQ_lambda)_R=0,
    (z_1,(Lambda Q)_lambda)_R=0.                    (2)

For a forcing f in this parity class, consider the **projected linear equation**

    z_t=JH(t)z+f+R(t),                              (3)

where R is in the primary span of Q_lambda, iQ_lambda and (Lambda Q)_lambda and is uniquely chosen so that the derivatives of all constraints (2) vanish. This is a definition of the linear problem; it does not assert that an arbitrary nonlinear error satisfies (3) without the usual modulation-coordinate calculation.

For t sufficiently close to T, there is a fixed M_0>0 such that

    E_lin(t,z)=(H(t)z,z)_R+M_0||z_sec||_2^2,

is uniformly equivalent on X(t) to

    N_lambda(z)^2=||z_1'||_2^2+lambda^(-2)||z_1||_2^2
                    +||z_sec'||_2^2+||z_sec||_2^2. (4)

For smooth solutions of (3),

    |d E_lin/dt|
       <=(C/h) E_lin+C sqrt(E_lin) N_lambda(f).    (5)

By density the corresponding integrated energy estimate extends to energy-class solutions with an integrable right side. Constants depend on kappa, the fixed matched family, its finite number of occupied modes, and the cutoff. They are independent of the terminal time t_1<T used in a backward construction.

In particular, for z(t_1)=0,

    N_lambda(t)(z(t))
       <=C integral_t^(t_1) (h(t)/h(s))^C
                                   N_lambda(s)(f(s)) ds. (6)

The exponent C is finite but is not claimed to be small. This estimate has polynomial loss in h, rather than exponential loss exp(C h^(-3)). It therefore supplies a real linear building block. It does not establish that the available matched family has a sufficiently small forcing in the norm (4).

## 2. The odd transverse estimate by itself

The principal transverse operator is

    H_Q,lambda=-partial_x^2-lambda^(-2)Q(x/lambda)^4.

For every odd complex f in H1(R),

    (H_Q,lambda f,f)_R >= (5/8)||f'||_2^2.          (7)

Here is a direct proof, stronger in the odd sector than the general Q-orthogonal bound used previously. Scale lambda to one and set z=tanh(2x), f(x)=g(z). Then

    integral |f'|^2=2 integral_(−1)^1 (1-z^2)|g'|^2 dz,
    integral Q^4|f|^2=(3/2)integral_(−1)^1|g|^2 dz.

Oddness gives zero mean. The first nonzero Legendre eigenvalue is 2, so

    integral (1-z^2)|g'|^2 >=2 integral |g|^2.

This inequality also follows by the usual completion of squares for the Legendre operator and approximation at its endpoints. Hence the potential term is at most (3/8) of the derivative term, proving (7). The homogeneous constant is sharp, as cutoffs of tanh(2x) approach equality.

For odd f there is also the elementary bound

    |f(x)|<=|x|^(1/2)||f'||_2.

Consequently every fixed exponentially decaying weight V with integral |y||V(y)| finite obeys

    integral lambda^(-2)|V(x/lambda)||f(x)|^2 dx
       <=C_V||f'||_2^2.                            (8)

Differentiating the transverse quadratic form with respect to lambda replaces Q^4 by a fixed combination of Q^4 and y(Q^4)'. Equations (7)–(8) therefore prove for the exact transverse equation i z_t=H_Q,lambda z

    |d/dt (H_Q,lambda z,z)_R|
       <=C |lambda_t/lambda| (H_Q,lambda z,z)_R.

There is no lambda^(-2) growth factor. The term containing the generator cancels by self-adjointness. This is an unprojected transverse propagator statement.

## 3. The primary constrained form

Let L_+=-partial_y^2+1-5Q^4 and L_-=-partial_y^2+1-Q^4. In the even sector,

    (L_+a,a)+(L_-b,b)
       >=c(||a||_H1^2+||b||_H1^2)                 (9)

when a is orthogonal to Q and Lambda Q and b is orthogonal to Q.

For clarity, nonnegativity of the L_+ form on the mass tangent a perpendicular to Q follows by taking the second variation of the scalar sharp mass-critical inequality E(u)>=0 at mass Mc. Its only constrained zero direction in the even sector is Lambda Q. Indeed L_+Lambda Q=-2Q, and the only kernel of L_+ itself is the odd translation mode Q'. The latter fact follows directly from the elementary Poschl–Teller operators after y is replaced by 2y: L_+ has bound-state eigenvalues -8 and 0, with the zero mode odd; L_- has only its zero eigenfunction Q below the essential spectrum [1,infinity). Their factorization is generated by partial_z+nu tanh z, with nu=3/2 and 1/2 respectively. Compactness below the essential spectrum then gives (9) after removal of Lambda Q and Q. This supplies the standard coercivity used here; it is not a new spectral theorem.

After scaling, the primary norm in (9) is precisely the first two terms of (4). The useful identities are

    H_0(t)(iQ_lambda)=0,
    H_0(t)(Lambda Q)_lambda=-2omega Q_lambda,       (10)

where H_0 has primary blocks L_+,lambda and L_-,lambda and secondary block H_Q,lambda. These identities make the fast phase and scale projections neutral for the main energy on X(t).

## 4. Sizes of the matched perturbation

Write K(t)=H(t)-H_0(t). The secondary matching has the following elementary consequences:

    |W_lambda(x)|<=C|x|+C lambda,
    |W_lambda(lambda y)|<=C lambda(1+|y|),
    ||W_lambda||_infinity+||W_lambda'||_infinity<=C.

The constant primary chirp in scaled coordinates has size

    beta=k lambda=O(lambda^(3/2)),
    A_1=Q_lambda exp(i beta y^2/4).

The off-diagonal Hessian coefficient in (1), localized to the principal core, has size

    rho_A |A_1||W_lambda|
       <=C lambda^(-1/2) V(x/lambda)

with an exponentially decaying V, plus smaller terms. In particular, for any z in the parity class,

    |cross-form(z)|<=C lambda^(3/2) N_lambda(z)^2. (11)

To verify the power, the primary L2 norm is at most lambda N_lambda(z). By oddness,

    ||V(x/lambda)z_sec||_2<=C lambda||z_sec'||_2.

Multiplying these two bounds by lambda^(-1/2) gives lambda^(3/2). The chirp perturbation of the primary potential has the same relative form size: |exp(i beta y^2/2)-1|<=C|beta|y^2 on fixed weighted tests. The scalar secondary background contributes a bounded physical potential to the secondary block; its negative part is absorbed by M_0||z_sec||_2^2. On the primary block its bounded part is O(lambda^2) relative to (4), and its core-density part is still smaller by the node of W_lambda.

Combining (7), (9) and (11), and choosing M_0 sufficiently large, proves the norm equivalence in (4) for small lambda.

A more specific estimate is needed for the projection terms. For each fixed primary test

    Phi_lambda in {Q_lambda,iQ_lambda,(Lambda Q)_lambda},

one has

    |(K(t)z,Phi_lambda)_R|
       <=C lambda^(1/2)N_lambda(z).                (12)

For the chirp part this follows from lambda^(3/2) times the energy norm of Phi_lambda, which is O(lambda^(-1)). For the off-diagonal part it follows directly from the weighted odd bound: the product of the physical coefficient lambda^(-1/2) and Phi_lambda has amplitude lambda^(-1), whose pairing with z_sec(lambda y) gains lambda^(1/2). Bounded outer secondary potentials do not act on a primary test. The remaining primary-background terms are smaller.

The explicit matched family also obeys the time-derivative form bound

    |(H_t(t)z,z)_R| <= (C/h) N_lambda(z)^2.        (13)

For H_0 this follows from (8), omega_t/omega=4/h, and |lambda_t|/lambda=2/h. For the matched perturbation, differentiate its displayed cutoff formula. The quantities g=F-y and y g' are bounded, so lambda partial_lambda r_lambda is O(lambda), supported in |x|<=2sqrt(lambda). The logarithmic derivative of the Gram correction satisfies lambda partial_lambda B_lambda=O(lambda^2), so partial_t B_lambda=O(lambda |lambda_t|): this follows by differentiating the same integrals used for its O(lambda^2) size, or directly from the smooth matrix inverse square root on the fixed positive definite Gram neighborhood. Weighted core bounds survive these derivatives with a factor C|lambda_t|/lambda. The chirp coefficient satisfies |beta_t|<=C|beta|/h. These facts prove (13). No uniform bound on the second derivative of each secondary field is required.

## 5. All fast projection terms are accounted for

Write R=alpha Q_lambda+beta_0 iQ_lambda+gamma_0(Lambda Q)_lambda. The real constraint Gram matrix is a fixed invertible diagonal matrix. From the differentiated constraints and (10)–(12),

    |alpha|<=C lambda^(1/2)N_lambda(z)+C||f_1||_2,

    |beta_0|+|gamma_0|
       <=C lambda^(-1)N_lambda(z)
          +C(lambda/h)N_lambda(z)+C||f_1||_2.      (14)

There is no large moving-basis contribution to alpha: partial_t Q_lambda=-(lambda_t/lambda)(Lambda Q)_lambda, which pairs to zero by (2). The moving-basis contributions to the other coefficients have the explicitly displayed size lambda N_lambda(z)/h.

Let L=H+M_0P_sec be the energy operator. Its pairings with primary modes equal those of H. On X(t), (10) yields

    |(Lz,Q_lambda)_R|<=C lambda^(-1)N_lambda(z),
    |(Lz,iQ_lambda)_R|
       +|(Lz,(Lambda Q)_lambda)_R|
          <=C lambda^(1/2)N_lambda(z).             (15)

Multiplying (14) and (15), using ||f_1||_2<=lambda N_lambda(f), gives

    |(Lz,R)_R|
       <=C lambda^(-1/2)N_lambda(z)^2
           +C N_lambda(z)N_lambda(f).

Since lambda^(-1/2)=kappa^(-1/2)/h, this is the claimed C/h growth. The potentially fast lambda^(-2) phase/scale dynamics has not been omitted: its coefficients are present in (14), and its contribution to the main energy cancels exactly in (15). Only the matched perturbation survives, at the favorable size lambda^(3/2).

## 6. Energy differentiation and backward integration

Differentiate E_lin along (3). The principal Hamiltonian contribution vanishes:

    (Hz,JHz)_R=0.

The added secondary mass produces

    M_0(P_sec z,JHz)_R.

Its complex-linear self-adjoint secondary terms have zero real pairing. The remaining antilinear secondary term is bounded by a constant times

    integral rho_A |W_lambda|^2 |z_sec|^2,

and its coefficient is uniformly bounded: Q_lambda^2|W_lambda|^2 is O(lambda) on the core, and the outer |W_lambda|^4 is bounded. The primary-secondary term is bounded by (11). Hence the entire added-mass contribution is at most C N_lambda(z)^2.

The forcing has the form bound |(Lz,f)_R|<=C N_lambda(z)N_lambda(f), by polarization and the same bounded-form estimates as in Section 4. Combining this with (13) and (15) proves (5).

Applying the square-root energy inequality backward from t_1 gives (6). In particular, if N_lambda(f(t))<=C_f h(t)^m and m>C-1, then the zero-terminal solutions satisfy

    N_lambda(z(t))<=C C_f h(t)^(m+1)/(m-C+1),

uniformly as t_1 tends to T. The same polynomial factor multiplies a nonzero terminal error. Such an estimate is suitable for a terminal-sequence argument only after its actual residual and nonlinear terms have been bounded at the required order.

## 7. What still prevents a trajectory theorem

The reference family used here is fully specified and its linear energy estimate is proved. Nevertheless:

1. A fixed outer W does not solve the outer evolution. Its residual is not automatically small. One must construct the correct evolving outer field and its overlap with the shrinking layer.
2. The leading primary acceleration and coupling require a profile correction and modulation solvability conditions. The negative matched energy coefficient alone does not prove those conditions are all compatible.
3. The true exact-mass perturbation satisfies a nonlinear mass constraint, whose Q component is quadratic in the error; replacing it by the tangent space (2) requires a verified nonlinear coordinate calculation.
4. Higher-order profile corrections must preserve the coercivity, derivative-form, and mode estimates (11)–(13). Their existence and sufficiently small residual have not been established here.
5. Closing the nonlinear error equation requires explicit bounds in the energy norm (4), not just an L2 residual or a formal asymptotic expansion.

Thus the h^(-4) linear oscillation is not by itself an obstruction: the Hamiltonian and constrained spectral structure reduce it to polynomial backward growth. The unresolved task is the construction and control of an actual matched approximate evolution, followed by a nonlinear terminal limit. This note supplies that construction with a precise linear estimate, without assuming the rest of the argument.
