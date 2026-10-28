# R17 Proof details: automatic primary variance at a critical collapse

Date: 2026-10-09. This note establishes the principal-mode transport argument proposed by the `critical_rate` branch. Its mathematical inputs are the R16 occupation-gap theorem and [threshold-rigidity.md](../occupation-thresholds/threshold-rigidity.md). No R16 file is modified.

## 1. Assumptions and conclusion

Consider a finite-component H1 solution in two space dimensions,

    i partial_t u_j = -Delta u_j-rho u_j,
    rho=sum_j |u_j|^2,
    E=1/2 sum_j ||grad u_j||_2^2-1/4 integral rho^2.

Work in the fixed Gram eigenbasis at the R16 endpoint: the principal mode has mass Mc=||Q||_2^2, its Gram eigenvalue is simple, and each secondary occupation divided by the principal occupation is at most the R16 epsilon_0. The R16 global deficit gives, throughout the lifespan,

    0<=E_1(t):=1/2||grad u_1(t)||_2^2-1/4||u_1(t)||_4^4<=2E.

If T is a finite forward H1 blowup time, R16 also gives the full-trajectory weak measure limit

    |u_1(t,x)|^2 dx -> Mc delta_(x_*),   t -> T.

Under these inputs, the following stronger conclusion is valid for every t<T in the lifespan, without an assumed initial second moment:

    I_1(t):=integral |x-x_*|^2 |u_1(t,x)|^2 dx
        <= [integral_t^T sqrt(8E_1(r)) dr]^2
        <=16E(T-t)^2.                                      (1)

In particular, finite-time endpoint blowup forces the principal mode to have finite variance at every earlier lifespan time. If the principal mode has infinite variance at even one lifespan time, the solution instead exists globally in both time directions. Uniform-in-time H1 boundedness and scattering are not asserted by this conclusion.

## 2. Why a phase on one mode is admissible here

Scalar sharp Gagliardo--Nirenberg at mass Mc gives E_scalar(f)>=0 for every f in H1 with ||f||_2^2=Mc. For bounded smooth real theta with bounded gradient and every real a,

    0<=E_scalar(exp(ia theta)u_1)
      =E_1+a integral J_1.grad theta
          +(a^2/2) integral rho_1 |grad theta|^2,

where rho_1=|u_1|^2 and J_1=Im(conjugate(u_1) grad u_1). The discriminant is nonpositive, hence

    |integral J_1.grad theta|^2
        <=2E_1 integral rho_1 |grad theta|^2.                 (2)

This argument uses scalar energy positivity, not positivity of the full-system energy after changing only one phase. It therefore does not require that the phase change preserve off-diagonal Gram entries. The warning in Section 4 of the R16 dynamics note is correct for the full energy argument but does not prohibit (2).

The common nonlinear potential rho is real. It follows directly from the equation that the individual density satisfies

    partial_t rho_1+2 div J_1=0.                             (3)

Conservation of E_1 is neither true in general nor needed. Its continuity in time follows from H1 continuity and the two-dimensional H1-to-L4 embedding.

## 3. Transport with no second-moment assumption

Use the extended unnormalized quadratic transport distance

    W(mu,nu)^2=inf_(pi with marginals mu,nu)
                         integral |x-y|^2 d pi.

The marginals have mass Mc. This quantity is initially allowed to be infinite. The bounded-Lipschitz Hopf--Lax duality proved in Section 6 of the R16 dynamics note applies to arbitrary equal-mass finite measures, not just finite-second-moment measures.

From (2), Young's inequality gives

    2 integral J_1.grad theta
       <=1/2 integral rho_1 |grad theta|^2+4E_1(t).

Testing (3) against Hamilton--Jacobi subsolutions and applying that duality yields, on any compact lifespan segment [a,b],

    W(rho_1(a)dx,rho_1(b)dx)^2
        <=8(b-a) integral_a^b E_1(r) dr.                     (4)

Thus every such pair has finite relative transport cost, even if neither individual marginal has finite second moment. Gluing couplings proves the usual triangle inequality for this extended distance on its finite-distance classes. Subdivide [a,b], apply (4) on each subinterval, and let the mesh tend to zero. Since E_1 is continuous and nonnegative, the resulting sums converge to give

    W(rho_1(a)dx,rho_1(b)dx)
        <=integral_a^b sqrt(8E_1(r)) dr.                     (5)

The weaker uniform bound W<=4sqrt(E)|b-a| follows directly from (4) and E_1<=2E and needs no subdivision.

Fix t<T and take times b_n increasing to T. Approximate optimal plans from rho_1(t)dx to rho_1(b_n)dx are tight: the first marginal is fixed and the second marginals converge weakly to Mc delta_(x_*), with no loss of their common mass. Any weakly convergent subsequence of plans has marginals rho_1(t)dx and Mc delta_(x_*). Lower semicontinuity of the nonnegative quadratic cost, followed by (5), gives

    W(rho_1(t)dx,Mc delta_(x_*))^2
        <=[integral_t^T sqrt(8E_1(r)) dr]^2.

There is exactly one coupling with the second marginal Mc delta_(x_*): all mass at x is sent to x_*. Its cost is I_1(t), including when that cost is initially infinite. The displayed finite upper bound proves (1), rather than presupposing finite variance.

## 4. Infinite variance excludes both finite lifespan endpoints

Finite mass makes infinite variance independent of the chosen finite center: |x-a|^2<=2|x-b|^2+2|a-b|^2. Therefore infinite variance about one point implies infinite variance about every point.

If the principal initial mode has infinite variance and the forward lifespan endpoint were finite, the R16 finite-time concentration theorem and Sections 2--3 would imply (1) at the initial time, a contradiction. The same argument with time reversed excludes a finite backward endpoint. Equivalently, time reversal followed by complex conjugation preserves the mass, the occupation spectrum, and the energy hypotheses. Standard H1 local well-posedness and its blowup alternative then imply two-sided global existence.

This is a sufficient global-existence condition at the exact fixed-spectrum threshold. It does not classify all global states, and finite variance alone does not imply blowup.

## 5. Conformal normalization and exact constants

Write h=T-t>0, s=1/h, and center at x_*. Define only the principal conformal field

    v_1(s,y)=h exp(i h |y|^2/4)u_1(T-h,x_*+h y).

Its mass is Mc. Equation (1) gives

    ||y v_1(s)||_2^2=I_1(T-h)/h^2<=16E.                    (6)

Since I_1 is now known finite, the phase is admissible in H1 and v_1 belongs to H1. Set

    V_J(t)=integral (x-x_*).J_1(t,x) dx.

The integral is finite by Cauchy--Schwarz. Approximate theta(x)=|x-x_*|^2/2 by bounded smooth radial cutoffs with gradients bounded by C|x-x_*|. Dominated convergence in (2) yields

    |V_J(t)|^2<=2E_1(t) I_1(t).                            (7)

Direct differentiation and the change of variables x=x_*+h y give the exact conformal energy expansion

    E_scalar(v_1(s))
        =h^2 E_1(t)+(h/2)V_J(t)+I_1(t)/8.                 (8)

In particular, the sign of the phase in the definition of v_1 is consistent with the positive middle term in (8). The lower bound follows once more from scalar GN at mass Mc. Equations (7)--(8) give

    0<=E_scalar(v_1(s))
       <=[h sqrt(E_1(t))+sqrt(I_1(t)/8)]^2
       <=8E h^2=8E/s^2.                                  (9)

No claim is made that the whole conformally transformed vector is in H1: secondary components may have infinite physical variance. Equations (6)--(9) concern the principal mode, whose variance has just been proved finite.

## 6. Explicit lower rate and degenerate energy

The two-dimensional uncertainty inequality for the principal mode is

    I_1(t)||grad u_1(t)||_2^2>=Mc^2.

Combining it with (1), for E>0,

    ||grad u_1(t)||_2>=Mc/[4sqrt(E)(T-t)],
    lambda(t)=sqrt(Mc)/||grad u_1(t)||_2
        <=4sqrt(E/Mc)(T-t).                               (10)

This makes the previous qualitative R16 lower rate quantitative. If E=0, (1) would force the nonzero absolutely continuous density rho_1(t)dx to be a point mass at every earlier time, an impossibility. Thus no finite-time blowup can occur in that degenerate case. For a genuinely non-pure spectrum R16 already gives E>0.

## 7. derivation verdict and scope

The proposed principal-mode variance argument, its two-sided global-existence consequence for infinite-variance principal data, and the conformal constants 16E and 8E are correct under the stated R16 hypotheses. The crucial logical distinction is scalar phase positivity at the critical principal mass, which does not require the Gram matrix to be preserved by that individual phase. The extended transport argument establishes the second moment before any quadratic phase or virial expression is used.

The proof does not establish exact asymptotic equality lambda(t)~c(T-t), a classification of every endpoint solution, or uniform H1 bounds for the infinite-variance global solutions.
