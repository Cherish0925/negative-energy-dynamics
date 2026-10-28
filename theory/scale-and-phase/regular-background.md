# Exact threshold collapse with a regular secondary field

Date: 2026-10-10. This is a derived extension of R16–R17, not a classification of every rough-background endpoint. Its basic argument is scalar and applies to a critical mode acted on by a real, time-dependent potential. The vector interpretation below is for the two-dimensional common-density cubic equation.

## 1. Statement

Assume the R16 two-dimensional occupation range and a finite forward singularity at T. Diagonalize the conserved Gram matrix, so that the primary mode u=u_1 has mass M=M_c, its scalar energy E_1 is uniformly bounded, and its density converges to M delta_(x_*). Write

    i u_t+Delta u+|u|^2 u+S(t,x)u=0,
    S=sum_{j>=2}|u_j|^2.

Assume additionally, for some t_0<T,

    sup_{t_0<t<T} ||S(t)||_{W^{2,infinity}(R^2)} < infinity.       (A)

For example, uniform secondary regularity in H^k with k>3 implies (A). This is an actual extra hypothesis; R17's uniform secondary H1 estimate does not imply it. No secondary spatial moment and no time derivative of S are assumed.

Let

    P(t)=Im integral conjugate(u) grad u,
    b(t)=M^{-1} integral x |u|^2,
    e(t)=E_1(t)-|P(t)|^2/(2M),
    I(t)=integral |x-b(t)|^2 |u|^2,
    V_Q=integral |x|^2 Q(x)^2,
    h=T-t.

Then there exist e_*>0 and P_* such that

    e(t)=e_*+O(h^2),
    I(t)=8e_* h^2+O(h^4),
    I'(t)=-16e_* h+O(h^3),
    P(t)=P_*+O(h),
    b(t)=x_*-2P_*h/M+O(h^2).                        (1)

In particular the actual Townes concentration scale, not just the root-mean-square radius, satisfies

    lambda(t)=mu_* (T-t)+O((T-t)^3),
    mu_*=(8e_*/V_Q)^{1/2}>0.                       (2)

Here lambda=sqrt(M)/||grad u||_2, as in R16–R17. Equivalently, the conformal primary

    v(s,y)=h exp(i h|y|^2/4)u(T-h,x_*+h y), s=1/h,

converges in absolute H1 to a fixed translated standing wave:

    ||v(s)-exp(i(s/mu_*^2+theta_*))
          mu_*^{-1}Q((.-y_*)/mu_*)||_{H1}->0,
    y_*=-2P_*/M.                                   (3)

The error in (3) is O(1/s). A smooth local modulation can be chosen with

    mu(s)=mu_*+O(s^{-2}),
    y(s)=y_*+O(s^{-1}),
    theta(s)=s/mu_*^2+theta_*+O(s^{-1}),
    ||v-exp(i theta) Q_{mu,y}||_{H1}=O(s^{-2}).      (4)

Statement (3) is asymptotic classification of the primary mode under (A). It is not uniqueness of the full vector solution for prescribed terminal secondary data. In physical coordinates it yields a precise leading pseudoconformal profile; it does not assert that the unscaled physical H1 error tends to zero.

## 2. Primary energy, force, and centered virial identities

R17 already proves that the whole primary has finite variance and

    integral |x-x_*|^2 |u|^2 <= C h^2.

Cutoff approximation therefore justifies the centered identities below. Under (A), their forcing terms are absolutely integrable. With J=Im(conjugate(u)grad u),

    b'=2P/M,
    P'=integral |u|^2 grad S,
    E_1'=integral grad S . J,
    e'=integral grad S . (J-P|u|^2/M),              (5)
    I''=16e+4 integral (x-b).grad S |u|^2.          (6)

The signs in (5)–(6) correspond to +S u on the left of the equation. A constant force accelerates the centroid and contributes no internal forcing. Because integral (x-b)|u|^2=0, a spatial Hessian bound L gives

    |integral (x-b).grad S |u|^2|<=L I.             (7)

No derivative of S in time occurs in (5). This avoids assuming that the secondary dynamics are time differentiable in a strong norm at T.

## 3. Internal phase positivity and the strictly positive limiting energy

The scalar sharp Gagliardo–Nirenberg inequality at mass M gives nonnegative scalar energy after any phase change. Apply it first to exp(-iP.x/M)u, whose energy is e and current is J-P|u|^2/M. For any admissible real theta,

    |integral grad theta . (J-P|u|^2/M)|^2
       <=2e integral |u|^2 |grad theta|^2.         (8)

Choose theta=S-grad S(t,b).x and use a cutoff approximation. Its gradient has absolute value at most L|x-b|, so

    |e'|<=L sqrt(2e I),
    |(sqrt e)'|<=L sqrt(I/2).                     (9)

The second inequality follows for sqrt(e+eta) first and then eta down to zero; no division by zero is used.

Translate the primary density by its instantaneous centroid. Its continuity equation has current J-P|u|^2/M. The same phase-to-transport argument as R17 consequently gives

    W_2(rho_centered(t),rho_centered(r))
       <=integral_t^r sqrt(8e(tau))d tau.

The measures have mass M, and W_2 denotes the unnormalized quadratic distance. Taking r to T gives

    I(t)<=8 [integral_t^T sqrt(e(r))dr]^2.         (10)

Set f=sqrt e. It is bounded by R16, and (9)–(10) imply

    |f'(t)|<=2L integral_t^T f(r)dr.              (11)

Thus f has a limit f_* and f=f_*+O(h^2). If f_*=0, integrate (11) backwards:

    f(t)<=2L integral_t^T integral_r^T f(q)dq dr.

On a sufficiently short terminal interval, taking the supremum yields

    sup f <= L h_0^2 sup f,

hence f vanishes there. Equation (10) would then give I=0 for an absolutely continuous positive mass, an impossibility. Therefore f_*>0. This proves e_*>0 and e=e_*+O(h^2).

Equations (6)–(7) now give I''=16e_*+O(h^2). The already known bounds I=O(h^2) and I'=O(h) imply terminal values I(T)=I'(T)=0. Twice integrating gives the first three expansions in (1). Bounded grad S gives the last two expansions through (5).

## 4. Conformal energy becomes time integrable after taking its square root

Use coordinates x_*=0 temporarily. Under the conformal change,

    P(v)=hP+(M/2)b,
    E_scalar(v)=h^2 e+(h/8)I'+I/8+|P(v)|^2/(2M). (12)

This follows either directly or by inserting

    integral |x|^2|u|^2=I+M|b|^2

into R17's uncentered conformal identity. In particular the momentum term is a nonnegative square, not a discarded cross term.

Equation (1) gives

    P(v)=O(h^2),
    0<=E_scalar(v)<=C h^4=C s^{-4}.               (13)

Every leading term of order h^2 in (12) cancels. This cancellation supplies information absent from R17's rough-background estimate E_scalar(v)=O(s^{-2}).

The scalar phase-current inequality at mass M now implies

    W_2(|v(s)|^2,|v(r)|^2)
       <=integral_s^r sqrt(8E_scalar(v(tau)))d tau
       <= C/s, r>=s.                             (14)

Thus the conformal primary densities converge in the quadratic transport space to a unique measure eta_*, and

    W_2(|v(s)|^2,eta_*)<=C/s.                     (15)

Both their means and centered second moments converge. The latter equals I(t)/h^2, so its limit is the strictly positive number 8e_*.

## 5. Why concentration of the conformal primary is now impossible

R17 already supplies

    v=exp(i theta)Q_{mu,y}+r,
    ||r||_{H1}<=C/s,
    0<mu<=C, |y|<=C.

The means converge to y_*=-2P_*/M. Along any sequence, pass to a subsequence so mu and y have limits. If mu tends to zero, strong L2 proximity forces the density's weak limit to be M delta_y. But (15) gives convergence also of the centered second moment, whose limit is 8e_*>0. This is impossible. Thus mu stays bounded away from zero.

Every subsequential limit is therefore Q_{mu_*,y_*}^2, and its variance identifies the scale uniquely:

    mu_*^2 V_Q=8e_*.

Uniqueness of eta_* eliminates subsequence choices and proves (2). Since the concentration parameters are bounded above and below, scalar quantitative Gagliardo–Nirenberg stability and (13) improve the profile error to

    ||r||_{H1}<=C sqrt(E_scalar(v))<=C s^{-2}.     (16)

A smooth modulation can be selected for large s by imposing real L2 orthogonality of r to the phase, translation, and scaling tangent vectors at Q_{mu,y}. The tangent Gram matrix is uniformly invertible on this compact parameter set.

## 6. Scale convergence is O(s^{-2}), not just o(1)

A weighted tail estimate supplies the needed distinction. The transport coupling in (15) implies, for large R,

    integral_{|y|>R}|y|^2|v(s,y)|^2dy
       <=4 W_2(|v(s)|^2,eta_*)^2
            +2 integral_{|z|>R/2}|z|^2 d eta_*(z).

Indeed, split the coupling according to |z|<=R/2 and its complement, and use |y|<=2|y-z| in the first region and |y|^2<=2|y-z|^2+2|z|^2 in the second. The limit eta_* has exponential tails. All current Townes profiles also have uniform exponential tails. Split the weighted norm of r at R=C_0 log s, choosing C_0 large enough. Equation (16) gives the inside bound R^2||r||_2^2; the preceding transport estimate gives the outside bound. Hence

    || |y|r||_2<=C/s.                             (17)

The difference between the primary mean and the profile center is O(s^{-2}), since

    integral y(|v|^2-|Q_{mu,y(s)}|^2)
       =2 Re integral y conjugate(Q_{mu,y(s)})r
          +integral y |r|^2.

The first term is O(s^{-2}) by (16), and the second is O(s^{-3}) by (16)–(17). Similarly, in the centered second moment the cross term is O(s^{-2}), using the finite L2 norm of |y|^2 Q_{mu,y(s)}, and the |r|^2 term is O(s^{-2}) by (17). Therefore

    mu(s)^2 V_Q=I(t)/h^2+O(s^{-2})
               =8e_*+O(s^{-2}),

which proves the scale estimate in (4).

## 7. Phase convergence under bounded potential

The transformed primary equation is

    i v_s+Delta v+|v|^2v+B(s,y)v=0,
    B(s,y)=s^{-2} S(T-s^{-1},x_*+y/s).

By (A), ||B(s)||_infinity=O(s^{-2}). Substitute the smoothly modulated decomposition from (16), differentiate the tangent orthogonality conditions, and pair the equation against the finitely many smooth tangent vectors. At a bounded positive scale, the linearized nonlinear operator maps H1 to H^{-1} boundedly; the nonlinear remainder is O(||r||_{H1}^2) in H^{-1}. The tangent parameter matrix is uniformly invertible. Consequently

    |theta'(s)-mu(s)^{-2}|+|mu'(s)|+|y'(s)|
       <=C(||r||_{H1}+||B Q_{mu,y}||_{H^{-1}})
       <=C s^{-2}.                              (18)

To be explicit about the projection: take the real inner product with the tangent vectors after writing the equation in real Hamiltonian form v_s=i(Delta v+|v|^2v+Bv). The unperturbed profile vector field is i mu^{-2}Q_{mu,y}, so the coefficient theta'-mu^{-2} is the phase coefficient. Differentiated orthogonality moves the projected r_s terms to O(||r|| times the parameter derivatives), which is absorbed for large s. All pairings of the linearized operator with tangent vectors are bounded by C||r||_{H1}.

Since mu(s)-mu_*=O(s^{-2}), (18) implies

    theta'(s)-mu_*^{-2}=O(s^{-2}).

Integration proves the phase statement in (4), and (3) follows. These steps establish a phase limit without claiming an exact full-vector solution or uniqueness of the background-coupled evolution.

## 8. Broader curvature growth: exact scale survives below h^{-2}

The rate conclusion (2), without the fixed-phase conclusion (3), needs substantially less than (A). Suppose instead that the background force is regular enough for (5)–(6), and

    ||Hess_x S(t)||_infinity <= K h^{-alpha},
    0<=alpha<2.                                  (19)

Keep the R16–R17 endpoint hypotheses, including bounded e and the already established unique primary atom. The centered argument is insensitive to spatially affine forcing.

Replace L in (11) by L(t). Because h L(t)=O(h^{1-alpha}) is integrable,

    e=e_*+O(h^{2-alpha}), e_*>0,
    I=8e_*h^2+O(h^{4-alpha}),
    I'=-16e_*h+O(h^{3-alpha}).                    (20)

For positivity, the backward Volterra estimate has contraction factor bounded by 2 integral_0^{h_0} r L(T-r)dr, which tends to zero. No power-series expansion of S is needed.

Let e_v denote the scalar energy of v after removing its instantaneous mean momentum. The exact centered identity is

    e_v=h^2 e+(h/8)I'+I/8,
    0<=e_v<=C h^{4-alpha}.                       (21)

Translate the conformal primary density by its instantaneous centroid. Its quadratic transport speed is at most sqrt(8e_v)=O(s^{-2+alpha/2}), which is integrable precisely for alpha<2. Hence the centered conformal densities converge in W2 with error O(s^{-1+alpha/2}). Their variance tends to 8e_*>0. The argument of Section 5 proves convergence to a nonzero fixed Townes scale and again

    lambda(t)/h -> (8e_*/V_Q)^{1/2}>0.             (22)

The scale convergence has a quantitative form. Set c_v to be the conformal primary centroid, p_v=P(v), and remove translation and mean momentum from the conformal field:

    w(s,z)=exp(-i p_v.(z+c_v)/M)v(s,z+c_v).

Its mass is M, its scalar energy is e_v, its centroid and momentum are zero, and its centered variance is I/h^2. After the positive lower scale bound is known, scalar quantitative GN stability gives a modulated Townes approximation with residual

    ||r_w||_{H1}=O(h^{2-alpha/2}).

The centered transport estimate is O(h^{1-alpha/2}). Repeat the coupling-tail argument of Section 6 for w, with R=C_0 log(1/h). It gives

    || |z|r_w||_2^2=O(h^{2-alpha}).

The moment cross term is O(h^{2-alpha/2}), which is no larger than O(h^{2-alpha}) for alpha>=0. Comparing centered variances therefore yields the profile scale

    mu_w(s)=mu_*+O(h^{2-alpha}).                  (23)

For clarity, this modulated scale is not defined to equal R17's physical kinetic scale. Their relation follows directly from the gradient transformation:

    h^2||grad u||_2^2
      =||grad v-i(h/2)y v||_2^2
      =||grad v||_2^2-h integral y.Im(conjugate(v)grad v)
          +(h^2/4)integral |y|^2|v|^2.

R17 bounds P(u), b(u)/h, and the conformal variance, so p_v=hP(u)+M(b(u)-x_*)/2=O(h). The centered conformal current moment is at most sqrt(2 e_v I/h^2)=O(h^{2-alpha/2}) by phase positivity. Hence the last displayed right-hand side is

    ||grad w||_2^2+O(h^2)
       =M/mu_*^2+O(h^{2-alpha}).

Consequently the actual physical kinetic scale satisfies

    lambda(t)=mu_* h+O(h^{3-alpha}).              (24)

For alpha=0, this is the O(h^3) remainder claimed in (2). The argument retains the primary momentum contribution and does not identify modulation and kinetic scales without an estimate.

No limit for the phase is inferred from (19) alone. A large spatially constant potential changes phase without changing curvature; a large affine force changes centroid motion. This is why the bounded-potential phase statement and the curvature-only width statement are explicitly separate.

For the vector equation, P_1(t) already has a limit by R17's secondary H^{1/2} convergence and total momentum conservation. Thus the conformal primary center has the same limiting value y_* as before, even in this broader curvature-growth setting. Its convergence rate need not be O(1/s).

## 9. Regular secondary fields vanish at the collapse point

There is a stronger consequence if the individual secondary fields, not just their total density, remain uniformly regular. Assume

    sup_{t_0<t<T} sum_{j>=2} ||u_j(t)||_{H^k}<infinity,
    k>3.                                         (25)

R17's strong L2 terminal convergence, interpolation, and Sobolev embedding imply strong H1 and C1 convergence to W=(w_j)_{j>=2}. In particular (A) holds. Exact Gram orthogonality and (16) then force

    |u_j(t,x_*)|=O(h),
    w_j(x_*)=0, j>=2.                            (26)

Here is the estimate, including the scale lost under the change of variables. From (16), in physical coordinates,

    u_1(t,x)=h^{-1}exp(i theta(s))
        exp(-i|x-x_*|^2/(4h))Q_{mu(s),y(s)}((x-x_*)/h)
          +r_phys(t,x),
    ||r_phys||_2=O(h^2).

Pair with u_j and use <u_1,u_j>=0. The main term is

    h exp(i theta) integral exp(-ih|y|^2/4)
           Q_{mu,y(s)}(y) conjugate(u_j(t,x_*+hy))dy.

Uniform Lipschitz bounds for u_j, bounded profile parameters, and exponential profile moments reduce this to

    h exp(i theta) [mu(s) integral Q]
                  conjugate(u_j(t,x_*))+O(h^2).

The error pairing with r_phys is O(h^2). Since mu is bounded away from zero, (26) follows. This argument uses the improved O(h^2) primary residual; the R17 O(h) residual alone did not justify the two-dimensional node.

Moreover uniform Lipschitz bounds and (26) give

    S(t,x)<=C(h^2+|x-x_*|^2),
    integral S(t,x)|u_1(t,x)|^2dx=O(h^2).         (27)

Define the secondary subsystem energy

    E_sec(W)=1/2 sum_{j>=2}||grad w_j||_2^2
                   -1/4 integral (sum_{j>=2}|w_j|^2)^2.

Since the physical secondary convergence is now strong H1, total energy conservation and (27) identify the positive internal core energy:

    e_*=E_total-E_sec(W)-|P_*|^2/(2M)>0,
    mu_*^2=(8/V_Q)[E_total-E_sec(W)-|P_*|^2/(2M)]. (28)

Thus the collapse speed is determined by the energy remaining after subtracting the regular secondary energy and the translational kinetic energy of the core. This is an exact identity in the normalized model. It does not assert a terminal secondary H1 limit for arbitrary H1 backgrounds; the stronger conclusion here follows from (25).

## 10. Literature and attribution

The scalar theory of minimal-mass singularities, pseudoconformal profiles, and regular-potential constructions is established literature. This argument does not claim to introduce those subjects or the pseudoconformal blow-up law.

Primary sources checked on 2026-10-10:

- V. Banica, R. Carles, T. Duyckaerts, *Minimal blow-up solutions to the mass-critical inhomogeneous NLS equation*, arXiv:0904.1317. Theorem 1.1 (full PDF, pp. 2–3) constructs pseudoconformal-rate solutions for bounded C2 potentials and sufficiently flat nonlinear coefficients. The discussion on p. 4 explicitly leaves classification outside its scope. https://arxiv.org/pdf/0904.1317
- N. Matsui, *Minimal mass blow-up solutions for nonlinear Schrödinger equations with a potential*, arXiv:2007.15968v4 (2021 revision). The full-text Theorem 1.3 constructs a minimal-mass solution and its profile under weaker static-potential assumptions; it is an existence statement. https://arxiv.org/html/2007.15968v4
- N. Matsui, *Minimal-mass blow-up solutions for inhomogeneous nonlinear Schrödinger equations with growth potentials*, arXiv:2108.06205v2, Arkiv för Matematik 61 (2023), 413–436. The full-text Theorem 1.7 broadens construction assumptions on static potential regularity and growth, prescribing a positive energy. https://arxiv.org/html/2108.06205v2

These inspected theorems do not establish historical priority for the all-endpoint implication proved here. A wider comparison against classification literature remains necessary before any novelty claim. The specific contribution of this note within the present project is the closure of the missing R17 scale implication under a spatial curvature hypothesis: centered force estimates improve conformal energy enough to make quadratic transport converge, preventing a vanishing core scale together with an escaping weighted tail.

The one-dimensional quintic vector equation does not reduce to a scalar quintic with potential S alone: its primary coupling is 2S|u|^2u+S^2u. Therefore the two-dimensional secondary-field theorem must not be transferred to that vector model by substituting the dimension. The scalar external-potential argument is dimension independent at critical power, provided the corresponding sharp-GN stability and concentration inputs are available; the coupled quintic application needs separate control of its mixed nonlinear term.
