# Primary variance, global threshold data, and conformal radiation

Date: 2026-10-09. This note continues [threshold-rigidity.md](../occupation-thresholds/threshold-rigidity.md). The new statements are consequences of the R16 all-state energy remainder and endpoint concentration theorem. It does not claim a complete classification of critical blow-up speeds. All components are finite in number.

## 1. Assumptions and conclusions

Consider on R2

    i u_{j,t} = -Delta u_j-rho u_j,
    rho=sum_j |u_j|^2,
    E= (1/2)sum_j ||grad u_j||_2^2-(1/4)integral rho^2.

Diagonalize the conserved Gram matrix once. Assume

    ||u_1||_2^2=Mc=||Q||_2^2,
    <u_i,u_j>=0 for i!=j,
    max_{j>=2}||u_j||_2^2/Mc<=epsilon0,

with epsilon0 exactly as in R16, and -Delta Q+Q-Q^3=0. The total secondary mass is unrestricted, but finite. R16 proves throughout the maximal H1 lifespan

    0<=E1(t):=E_scalar(u_1(t))<=2E,
    A_sec(t):=sum_{j>=2}||grad u_j(t)||_2^2<=64E.       (1)

Suppose T is a finite forward blow-up time. R16 also proves, along the full trajectory,

    |u_1(t)|^2 dx -> Mc delta_(x_*),
    u_j(t)->w_j strongly in H^sigma, every sigma<1, j>=2,

where w_j belong to H1. The primary terminal atom is unique.

The new conclusions are:

**A. Automatic finite variance of the entire primary mode.** Without assuming any spatial moment of the initial data, at every t<T,

    I1(t):=integral |x-x_*|^2 |u_1(t,x)|^2 dx
       <= [integral_t^T sqrt(8 E1(r)) dr]^2
       <=16 E (T-t)^2.                              (2)

This controls the full primary mode, not just the mass inside a ball comparable to its Townes scale. In particular, any finite-time threshold blow-up has a principal Gram eigenmode in Sigma=H1 cap {|x|u in L2} at every earlier time.

**B. A directly specified global class on the exact threshold.** If, at one time t0,

    integral |x|^2 |u_1(t0,x)|^2 dx=infinity,         (3)

then the H1 solution exists for all positive and negative times. No uniform-in-time H1 bound is asserted. This statement applies to the actual principal Gram eigenmode, which is well defined up to constant phase because the largest eigenvalue is simple. Infinite variance is independent of the choice of a fixed spatial center.

**C. Strong weighted convergence of each finite-variance secondary mode.** If |x|u_j(t0) belongs to L2 for some secondary j and one t0<T, then |x|w_j belongs to L2 and

    || |x-x_*| (u_j(t)-w_j)||_2 ->0.                 (4)

This is in addition to the H^sigma convergence in R16. It does not imply strong physical H1 convergence.

**D. Every finite-variance threshold blow-up has freely scattering conformal secondary modes.** If all secondary modes have finite variance at one time, apply the pseudoconformal transformation about (T,x_*), with h=T-t, s=1/h:

    v_j(s,y)=h exp(i h|y|^2/4)u_j(T-h,x_*+h y).

The transformed vector is an H1 solution for all sufficiently large s. There exist f_j in H1, j>=2, with

    ||v_j(s)-exp(is Delta)f_j||_{H1}->0.             (5)

These scattering states are determined by the terminal background w_j. For the primary mode, without even requiring secondary finite variance,

    || |y|v_1(s)||_2^2<=16E,
    0<=E_scalar(v_1(s))<=8E/s^2.                    (6)

Thus any faster-than-pseudoconformal primary blow-up becomes kinetic grow-up in conformal time, while its variance remains bounded and its scalar energy tends to zero. Excluding this remaining behavior requires a further dynamical argument.

In fact there are parameters vartheta(s), y_c(s), and mu(s)>0 such that

    ||v_1(s)-exp(i vartheta(s))mu(s)^(-1)
                    Q((.-y_c(s))/mu(s))||_{H1}<=C/s,
    0<mu(s)<=C,  |y_c(s)|<=C.                       (6a)

The error here tends to zero in the absolute H1 norm, not merely after normalizing by the primary kinetic energy. This argument by itself does not give a positive lower bound for mu(s) or convergence of the parameters.

The companion momentum argument, independently recorded in [momentum-details.md](momentum-details.md), further proves convergence of the center:

    y_c(s)->-2P_*/Mc,
    P_*:=P_total-sum_{j>=2}P(w_j),

in coordinates centered at x_*. Thus it is the scale and phase trajectory, not the center limit, that remains unclassified after combining the two notes.

## 2. The primary density has its own transport bound

Write rho1=|u_1|^2 and J1=Im(conjugate(u_1) grad u_1). The real common potential rho implies the separate continuity equation

    partial_t rho1+2 div J1=0.

For any real bounded smooth theta with bounded gradient, scalar sharp GN at mass Mc gives

    E_scalar(exp(ia theta)u_1)
       =E1+a integral J1.grad theta
          +(a^2/2)integral rho1 |grad theta|^2 >=0

for every real a. Therefore

    |integral J1.grad theta|^2
       <=2 E1 integral rho1 |grad theta|^2.         (7)

No preservation of the vector Gram matrix under this individual phase change is needed: the nonnegativity used here is scalar and uses only the exactly critical primary mass. This is why the argument gives information not supplied by applying a common phase only to the total vector.

For finite measures of equal mass, let W denote the extended unnormalized quadratic transport distance. It is allowed to be infinite for arbitrary pairs, and neither marginal is initially required to have finite second moment. The bounded-test Hamilton--Jacobi/Kantorovich argument proved in Section 6 of the R16 note applies to (7), giving, first on a compact interval [a,b],

    W(rho1(a)dx,rho1(b)dx)
       <=sqrt(8 sup_[a,b] E1) (b-a).

The triangle inequality remains valid for the extended distance: glue two finite-cost couplings and use Minkowski in L2. Partition [a,b] and use continuity of E1 on compact H1 lifespan intervals. The result is

    W(rho1(a)dx,rho1(b)dx)
       <=integral_a^b sqrt(8E1(r)) dr
       <=4 sqrt(E)(b-a).                           (8)

This argument uses bounded Lipschitz endpoint tests and truncated quadratic cost, exactly as in R16. It does not presuppose membership in the usual finite-second-moment space P2.

Let b tend to T. Almost optimal transport plans are tight since their marginals are tight. Lower semicontinuity of the quadratic cost and the primary terminal atom give

    W(rho1(t)dx,Mc delta_(x_*))
       <=integral_t^T sqrt(8E1(r)) dr.

There is only one possible target coordinate in a coupling with a point mass. Consequently

    W(rho1(t)dx,Mc delta_(x_*))^2=I1(t),

including the possibility that the left side would initially have been infinite. The finite upper bound proves (2).

### Finite variance is invariant along finite portions of the lifespan

For any coupling pi between primary densities at times a,b,

    [integral |y|^2 rho1(b,y)dy]^(1/2)
       <=[integral |x|^2 rho1(a,x)dx]^(1/2)
          +[integral |x-y|^2 d pi]^(1/2).

A finite-cost coupling from (8) shows that finite variance at one time implies finite variance at the other. Reversing times proves the equivalence. If a finite maximal H1 endpoint existed for data satisfying (3), (2) would contradict (3). Time reversal and conjugation give the same argument at a finite backward endpoint. Standard H1 continuation therefore proves conclusion B.

This is a global-existence statement for a nonempty and directly defined class at the exact threshold. It does not classify all finite-variance data: R16 constructs finite-variance examples with distinct forward fates.

An explicit family shows that this class is nonempty for every permitted finite occupation spectrum. Choose

    u_1(t0,x)=sqrt(Mc/(2pi)) (1+|x|^2)^(-3/4).

The integral of (1+|x|^2)^(-3/2) over R2 is 2pi, so the primary mass is exactly Mc. This smooth function belongs to H1 but has infinite second moment. For every secondary mode choose a smooth function on its own disjoint annulus with angular factor exp(i theta), and normalize its mass to Mc t_j. Every secondary is exactly orthogonal to the radial primary and to the other secondaries. The resulting vector has precisely the prescribed Gram spectrum, finite energy, and a two-sided global H1 evolution by conclusion B.

## 3. Quantitative primary consequences

After (2) is known, the usual first- and second-moment identities are justified by cutoff approximation. In particular

    I1'(t)=4 integral (x-x_*).J1(t,x) dx,
    |I1'(t)|<=4 sqrt(2 E1(t) I1(t))<=32E(T-t).       (9)

For the unbounded quadratic test in (7), approximate |x-x_*|^2/2 by smooth cutoffs with gradient bounded by C|x-x_*| and pass to the limit. The Cauchy--Schwarz integrability follows from finite I1 and H1 regularity. This proves the middle inequality in (9).

The primary centroid a1(t)=Mc^(-1)integral x rho1(t,x)dx is now defined and satisfies

    |a1(t)-x_*|<=4 sqrt(E/Mc)(T-t).

The Heisenberg inequality in dimension two gives

    Mc^2<=I1(t)||grad u_1(t)||_2^2,
    ||grad u_1(t)||_2>=Mc/[4sqrt(E)(T-t)].           (10)

For E=0 a finite-time blow-up is impossible, since (2) would make a positive absolutely continuous mass supported at one point.

The primary momentum is not generally conserved; the common potential transfers momentum between components. No identification of x_* with the initial primary centroid is made.

## 4. Secondary transport and strong weighted field convergence

For an individual secondary component, set rho_j=|u_j|^2 and J_j=Im(conjugate(u_j)grad u_j). Pointwise,

    |J_j|^2/rho_j<=|grad u_j|^2

with value zero where rho_j=0. Thus for every admissible theta,

    2|integral J_j.grad theta|
       <=2||grad u_j||_2 (integral rho_j |grad theta|^2)^(1/2).

The same extended-cost argument, or its usual dynamic formulation after finite variance is established, gives

    W(rho_j(t)dx,rho_j(s)dx)
       <=2 integral_t^s ||grad u_j(r)||_2 dr
       <=16sqrt(E)|s-t|.                           (11)

If rho_j has finite second moment at one time, (11) preserves that property through every finite time interval. As t tends to T these measures are Cauchy in the ordinary finite-mass P2 space. Their already known weak limit is |w_j|^2 dx. Hence

    W(rho_j(t)dx,|w_j|^2dx)<=16sqrt(E)(T-t),
    integral |x-x_*|^2 |u_j(t,x)|^2 dx
       ->integral |x-x_*|^2 |w_j(x)|^2 dx.          (12)

The last implication can also be seen directly from near-optimal couplings and Minkowski applied to the position norm; no density regularity is needed for it.

R16 proves u_j(t)->w_j strongly in L2. The weighted fields (x-x_*)u_j(t) are bounded in L2 by (12), and converge weakly to (x-x_*)w_j, because this is true against compactly supported tests and those are dense in L2. Their norms converge by (12). The Hilbert-space norm identity upgrades weak convergence to strong convergence, proving (4). This handles the complex phase of the field, not just its density.

## 5. The conformal primary: precise identities and the remaining rate issue

Translate x_* to zero and T to zero for the calculation; write t=-h<0 and s=1/h. The transformation

    v_1(s,y)=h exp(i h|y|^2/4)u_1(-h,h y)

preserves L2 mass. Direct differentiation and change of variables give

    || |y|v_1||_2^2=h^(-2)I1(-h),
    E_scalar(v_1)
       =h^2 E1(-h)+(h/2)integral x.J1(-h,x)dx+I1(-h)/8
       =h^2 E1(-h)+(h/8)I1'(-h)+I1(-h)/8.          (13)

The sign in front of I1' is positive. An exact pseudoconformal Townes wave has I1=8E1 h^2 and I1'=-16E1 h, so its transformed scalar energy is indeed zero.

Since its mass is Mc, E_scalar(v_1)>=0 by sharp GN. Using (1), (2), and (9) in (13),

    E_scalar(v_1)<=2E h^2+4E h^2+2E h^2=8E h^2.

This proves (6). Moreover

    | ||grad v_1(s)||_2-h||grad u_1(-h)||_2 |
       <=(1/2)sqrt(I1(-h))<=2sqrt(E)h.             (14)

If lambda(t)=sqrt(Mc)/||grad u_1(t)||_2, then lambda(t)/h->0 if and only if ||grad v_1(s)||_2->infinity. The same equivalence holds along sequences. Thus a universal two-sided pseudoconformal rate requires ruling out primary kinetic grow-up in this bounded-variance, vanishing-energy conformal regime. Estimates (6) alone do not rule it out.

### Absolute H1 approach to the one-Townes manifold

R16 supplies a primary decomposition, in the centered coordinates,

    u_1(-h,x)=exp(i theta_h)lambda_h^(-1)
                    Q((x-x_h)/lambda_h)+r_h(x),
    ||r_h||_2<=C lambda_h,  ||grad r_h||_2<=C,
    lambda_h<=C h,  |x_h|<=C h.

The moment estimate (2) and the explicit moment of the Townes core imply

    ||x r_h||_2<=||x u_1(-h)||_2
                      +||x lambda_h^(-1)Q((.-x_h)/lambda_h)||_2
                  <=C h.

Thus the conformal residual obeys

    ||C r_h||_2=||r_h||_2<=C h,
    ||grad C r_h||_2<=h||grad r_h||_2+(1/2)||x r_h||_2<=C h.  (14a)

Set mu=lambda_h/h and y_c=x_h/h, which are uniformly bounded. The conformal image of the Townes core is

    exp(i theta_h) exp(i h|y|^2/4)mu^(-1)Q((y-y_c)/mu).

Absorb the constant phase h|y_c|^2/4 into vartheta. With z=(y-y_c)/mu, the remaining phase is

    phi=h[mu y_c.z/2+mu^2 |z|^2/4].

Since |exp(i phi)-1|<=|phi| and Q and its derivatives have exponential decay, its L2 contribution is bounded by C h(mu|y_c|+mu^2). When differentiating the profile, the factor mu^(-1) in the L2 derivative norm cancels the smallest factor mu in phi, giving the bound C h(|y_c|+mu). Differentiating the phase itself contributes at most

    (h/2)||y mu^(-1)Q((y-y_c)/mu)||_2
       <=C h(|y_c|+mu).

Thus replacing the transformed core by its constant-phase Townes profile costs at most C h in H1, uniformly even when mu tends to zero. Combining with (14a) proves (6a).

Under the finite-secondary-variance assumption of Section 6, the full vector therefore has an absolute-H1 decomposition

    V(s)=exp(i vartheta(s))mu(s)^(-1)
                 Q((.-y_c(s))/mu(s)) e_1
             +(0,exp(is Delta)f_2,...,exp(is Delta)f_k)+o_{H1}(1).

Its unclassified feature is the trajectory of the Townes parameters, especially the possibility mu(s)->0 along a sequence. This formula must not be presented as a proof of convergence to a fixed-scale standing wave.

For completeness, the companion first-order primary centroid expansion also gives an exact cancellation of conformal momentum. Direct transformation yields

    P(v_1(s))=h P(u_1(t))+(Mc/2)(b_1(t)-x_*).

Since P(u_1(t))->P_* and b_1(t)-x_*=-2P_*h/Mc+o(h),

    P(v_1(s))=o(1/s).

This statement does not control the conformal kinetic energy, which can still be large for a real narrow Townes profile.

### Why energy and transport alone do not fix an exact speed

There is a concrete test of this missing implication. For any alpha>1, put lambda(t)=(-t)^alpha, t<0, and define the scalar curve

    a(t,x)=lambda^(-1)Q(x/lambda)
           exp(i theta(t)+i lambda'(t)|x|^2/(4lambda(t))),
    theta'(t)=lambda(t)^(-2).

This curve has mass Mc and satisfies the scalar continuity equation exactly. Direct calculation gives, with VQ=integral |y|^2 Q(y)^2dy,

    I_a(t)=VQ lambda(t)^2,
    E_scalar(a(t))=VQ lambda'(t)^2/8.

Consequently it obeys the sharp primary variance/energy-length inequality with equality, while its scale shrinks faster than |t|. It is NOT a solution of the unforced cubic NLS. Its exact residual is

    i a_t+Delta a+|a|^2 a
       =-[lambda''(t)/(4lambda(t))]|x|^2 a.        (15)

To make this ansatz an exact scalar equation with an added real potential in the convention +V a on the left would require V=lambda''|x|^2/(4lambda), which is not an admissible common-density secondary field globally. Formula (15) identifies the missing dynamical information: control of the actual coupled force is required. It is neither a counterexample to the vector theorem nor evidence that such an accelerated vector blow-up exists.

## 6. Free scattering of all conformal secondary components

Assume now every secondary component has finite variance at one time. Part A gives the same property for the primary. The complete conformal vector V is therefore an H1 solution for all sufficiently large s, by the standard pseudoconformal symmetry of the common-density cubic equation.

Let W_j(x)=w_j(x+x_*) in centered coordinates and define the free physical-time solution

    z_j(t)=exp(it Delta)W_j,

so z_j(0)=W_j. Because W_j belongs to Sigma, the free group is continuous at t=0 in Sigma. For completeness, its position identity is

    x exp(it Delta)W_j
       =exp(it Delta)(x W_j-2it grad W_j),

which gives the required weighted continuity. Parts C and R16 consequently imply

    ||u_j(T-h,x_*+.)-z_j(-h)||_2->0,
    ||x[u_j(T-h,x_*+.)-z_j(-h)]||_2->0.            (16)

The physical gradients of the difference are uniformly bounded, because both u_j and z_j are uniformly H1 bounded.

The conformal image

    z_j^C(s,y)=h exp(i h|y|^2/4)z_j(-h,h y)

is an exact free solution for s>0. Its H1 norm is finite, so z_j^C(s)=exp(is Delta)f_j for some f_j in H1.

With the unitary two-dimensional Fourier convention

    hat W(xi)=(2pi)^(-1)integral exp(-ix.xi)W(x)dx,

the scattering state is explicitly

    f_j(z)=(i/2)hat W_j(-z/2).                      (16a)

This follows by substituting z=-2xi in the free Schrödinger kernel. The equality is first checked for Schwartz data and extends to Sigma by the unitarity of the Fourier and free Schrödinger transforms. In particular the radiation profile is fixed by the terminal secondary field; it is not selected by a subsequence. Conformal differentiation and (16) give

    ||v_j-z_j^C||_2=||u_j-z_j||_2 ->0,
    ||grad(v_j-z_j^C)||_2
       <=h||grad(u_j-z_j)||_2+(1/2)||x(u_j-z_j)||_2 ->0.

This proves (5). The proof requires no general scattering theorem and no strong physical H1 terminal convergence.

The scattering Gram matrix is exactly

    <f_i,f_j>=<w_i,w_j>=Mc t_i delta_ij, i,j>=2,

because the free conformal map is unitary in L2 and R16 already identifies the limiting Gram matrix. The asymptotic radiation kinetic energy is also determined:

    ||grad f_j||_2^2=(1/4)||x W_j||_2^2.           (17)

Indeed, the gradient formula for z_j^C has an h grad z_j term tending to zero and a position term tending in norm to xW_j/2.

Finally, total conformal energy is conserved. Using (6), R16's bounds F_sec<=384epsilon E and I_cross<=66E, and their h^2 scaling under the conformal map, all nonlinear secondary and cross energies tend to zero. Equations (5)--(6) yield the exact value

    E(V)= (1/2)sum_{j>=2}||grad f_j||_2^2
         =(1/8)sum_{j>=2}|| |x-x_*|w_j||_2^2.      (18)

The entire conformal conserved energy is thus carried asymptotically by the secondary free radiation. The primary scalar energy tends to zero, but its scale need not yet have been classified.

## 7. Scope and dependencies

The proof inputs are the R16 quantitative occupation theorem, its fixed-spectrum endpoint concentration, standard H1 local theory and conservation, scalar sharp GN, and the extended quadratic-transport duality explicitly proved in the R16 dynamics note. The phase-current idea has classical antecedents in scalar critical NLS; the novelty claim here is limited to the derived fixed-spectrum vector statements until a full literature comparison is completed.

This note proves a global class of exact-threshold data specified by infinite variance of the principal eigenmode, automatic primary variance for every finite-time threshold singularity, weighted secondary convergence, and H1 scattering of every finite-variance conformal secondary field. It does not prove universal exact pseudoconformal speed, strong physical H1 background convergence, complete conformal soliton resolution, or any assertion about the equal-occupation rank-two endpoint.
