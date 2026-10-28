# Rough-background virial identities and an independent Dini-curvature derivation

Date: 2026-10-11. This note studies the two-dimensional common-density cubic system. It does not prove exact collapse scale under the original secondary H1 assumptions. It proves the cancellation identities, identifies a concrete concentration term not controlled by those assumptions, and independently verifies the Dini-curvature extension developed in [sharpness.md](sharpness.md).

## 1. Exact energy and force cancellation

Write the principal mode as u, the secondary vector as W=(u_j)_{j>=2}, and

    rho=|u|^2, S=sum_{j>=2}|u_j|^2,
    J=Im(conj(u) grad u), K=Im sum_{j>=2}conj(u_j) grad u_j,
    E1=1/2 int|grad u|^2-1/4 int rho^2,
    Es=1/2 sum int|grad u_j|^2-1/4 int S^2,
    C=int rho S.

The equations are i u_t+Delta u+(rho+S)u=0 and the same common real potential for every component. For smooth fields, with sufficient decay to justify each displayed integral,

    rho_t=-2 div J,       S_t=-2 div K,
    E1'=int grad S . J,
    Es'=int grad rho . K,
    C'=2 int grad S . J+2 int grad rho . K.

Thus

    E=E1+Es-C/2

is conserved. The signs agree with the focusing convention in the existing files.

Let V1=int |x|^2 rho and Vs=int |x|^2 S. Then

    V1''=16E1+4 int x.grad S rho,
    Vs''=16Es+4 int x.grad rho S.

Adding uses int x.grad(rho S)=-2 C and gives exactly

    (V1+Vs)''=16(E1+Es-C/2)=16E.

The cancellation is exact, but it does not supply a sign or an integrable bound for either component's tidal force separately. Adding the energies gives the same conserved identity and does not close the missing component equation.

Under H1 alone, the individual energy derivatives and the full unbounded-weight force integrals need not be defined as absolutely integrable functions. They must not be used without a justification. The safe version is the localized virial identity, for a fixed smooth real weight phi with bounded derivatives through order four:

    d^2/dt^2 int phi rho
      =4 sum_{k,l}int phi_kl Re(partial_k u conjugate(partial_l u))
       -int Delta^2 phi rho-int Delta phi rho^2
       +2 int grad phi . grad S rho.

Each term is well defined for every fixed H1 state in dimension two. For the force term, grad W is in L2 and W,u are in every finite Lp; bounded grad phi and Holder suffice. Summing principal and secondary identities converts the cross term to -2 int Delta phi rho S, exactly the cross part of the full density's quartic term. The usual H1 approximation establishes the distributional identity.

## 2. A static concentration example that retains all conserved spectral data

A uniform H1 bound on the secondary modes, strong terminal Hsigma convergence for every sigma<1, and even an exactly fixed energy do not force the principal tidal integral to vanish. This statement is about estimates on states, not a counterexample solution of the PDE.

Let Q be the radial Townes profile, M=||Q||2^2, and set u_lambda(x)=lambda^-1 Q(x/lambda). Choose r0>0 so small that

    H(r)=2Q(r)^2+r (Q(r)^2)' >0,  0<=r<=r0.

This is possible because Q(0)>0 and Q is smooth radial. Choose a nonzero smooth real function

    phi(y)=y_1 chi(|y|),  support(phi) subset B(0,r0).

It is odd in y_1, hence orthogonal to Q. Choose a smooth real g, odd in x_1, supported in 2<|x|<3, normalized by ||g||2=1. For a fixed secondary occupation 0<m<=epsilon0 M and a small positive a, define

    w_lambda(x)=a phi(x/lambda)+c_lambda g(x),
    c_lambda=(m-a^2 lambda^2||phi||2^2)^(1/2).

For small lambda the supports are disjoint, and exactly

    ||u_lambda||2^2=M, ||w_lambda||2^2=m,
    <u_lambda,w_lambda>=0.

The Gram matrix is diag(M,m). The secondary H1 norm is uniformly bounded, and

    w_lambda -> sqrt(m)g strongly in Hsigma, 0<=sigma<1,
    ||grad(w_lambda-sqrt(m)g)||2^2 -> a^2||grad phi||2^2>0.

The high-frequency portion has vanishing mass but nonzero kinetic energy. In particular, no uniform local absolute continuity of secondary kinetic energy follows from the existing conclusions.

The principal tidal integral has a nonzero limit:

    F_lambda=int x.grad(|w_lambda|^2)|u_lambda|^2
       -> a^2 int y.grad(|phi|^2)Q^2
        =-a^2 int [2Q^2+y.grad Q^2]|phi|^2 <0.

The far-field contribution tends to zero exponentially. On the concentrating support the secondary density Hessian is of order lambda^-2. This demonstrates precisely the missing control: bounded secondary H1 and all sub-H1 strong limits still allow order-one tidal forcing at the core scale.

Energy can also be fixed exactly. Let E_lambda(a) be the total vector energy of (u_lambda,w_lambda). Since the scalar energy of u_lambda is zero and the supports are disjoint,

    E_lambda(a) -> E_secondary(sqrt(m)g)
                    +(a^2/2)<phi,(-Delta-Q^2)phi>.

The R16 homogeneous spectral gap on Q-perpendicular functions makes the second coefficient strictly positive. The convergence and its a-derivative are uniform near any fixed a0>0: the errors are O(lambda^2), plus exponentially small terms. The ordinary implicit function theorem therefore produces a_lambda=a0+O(lambda^2) with E_lambda(a_lambda) exactly equal to the displayed limiting energy at a0. All the preceding properties and the nonzero tidal limit remain valid. The H1 convergence failure and tidal forcing are not artifacts of varying Gram or energy.

This example does not obey the time-dependent system when lambda is prescribed arbitrarily. It proves only that a proof removing the curvature assumption must use additional dynamics; applying the already available fixed-time estimates cannot suffice.

## 3. A global moment identity when secondary variance is finite

Translate the singularity to x_*=0. Assume the R17 secondary weighted convergence, which follows if the initial secondary modes have finite variance. Write W_* for their terminal vector and D(W_*)=Im sum int x.conjugate(w_j) grad w_j.

The secondary weighted L2 convergence and weak H1 convergence imply

    Im sum int x.conjugate(u_j(t)) grad u_j(t) -> D(W_*).

The primary current moment tends to zero: the scalar phase inequality and its O((T-t)^2) variance bound give an O(T-t) bound. Thus the total variance's terminal value and derivative are V(W_*) and 4D(W_*). The full system virial identity integrates exactly to

    V1(t)+Vs(t)=V(W_*)-4D(W_*)(T-t)+8E(T-t)^2.

Consequently

    Vs(t)=V(W_*)-4D(W_*)(T-t)+8E(T-t)^2-V1(t).

This provides exact second-order bookkeeping but does not determine V1/(T-t)^2. The undetermined principal variance is precisely the term that survives the total-force cancellation. No claim of strong physical H1 convergence of W(t) is used here.

## 4. Proof details: moving to a centered accelerating frame

The following calculation applies to a scalar critical NLS acted on by a real potential V(t,x), with the R17 mass, energy, variance, and concentration inputs. Spatial derivatives of V are assumed locally regular enough to justify the identities. No time derivative of V is needed.

Let b be the principal centroid, P its momentum, p=P/M, and

    z=x-b(t), w(t,z)=exp(-i p(t).z)u(t,b(t)+z).

Since b'=2p, direct substitution gives

    i w_t+Delta w+|w|^(4/d)w+W(t,z)w=0,
    W(t,z)=V(t,b+z)-p'(t).z+|p(t)|^2.

The constant |p|^2 can equivalently be removed by a scalar phase. The negative sign on p'.z is essential. The transformed field has exactly zero mean position and zero momentum, and obeys the ordinary continuity equation. Its scalar energy is

    e=E1-|P|^2/(2M)>=0.

Writing I=int |z|^2|w|^2 and L(t)=||Hess_x V(t)||infinity,

    I''=16e+4 int z.grad W |w|^2,
    |int z.grad W |w|^2|<=L I,
    |(sqrt(e))'|<=L sqrt(I/2),
    I(t)<=8 (int_t^T sqrt(e(r))dr)^2.

The final two statements use scalar sharp-GN positivity under phase changes, first with the phase W-grad W(t,0).z, then with the transport duality. Since integral z|w|^2=0 and P(w)=0, the affine inertial force has no effect in these estimates.

If

    D(h0):=int_0^h0 r L(T-r)dr <infinity,

then sqrt(e) has a terminal limit. Indeed, e is uniformly bounded by the existing energy estimate and |(sqrt(e))'|<=C h L. If that limit were zero, the integral inequality above would imply

    sup_(T-h<t<T) sqrt(e(t))
      <=2 D(h) sup_(T-h<t<T) sqrt(e(t)).

For small h, 2D(h)<1, forcing e=0 and then I=0 on a nonempty time interval, impossible for a positive absolutely continuous mass. Thus e_*>0. Moreover e-e_*=O(D(h)). Integrating the centered virial with I(T)=I'(T)=0 proves

    I/h^2 ->8e_*>0.

## 5. Proof details: conformal cancellation gives the correct Dini condition

Set h=T-t, s=1/h, and

    v(s,y)=h^(d/2) exp(i h|y|^2/4) w(T-h,h y).

Direct substitution gives

    i v_s+Delta v+|v|^(4/d)v+B(s,y)v=0,
    B(s,y)=h^2 W(T-h,h y),
    ||Hess_y B||infinity=h^4 L(T-h).

The field v still has zero position mean and zero momentum. Its variance is I/h^2, uniformly bounded. Its scalar energy is exactly

    Ev=h^2 e+(h/8)I'+I/8.

The already established rough bounds e=O(1), I=O(h^2), I'=O(h) imply 0<=Ev=O(h^2), hence Ev tends to zero. This terminal zero is available before proving a positive conformal width.

The scalar energy derivative is

    Ev'=int J_v.grad B.

Subtract grad B(s,0) using P(v)=0. Apply the scalar phase inequality to B-grad B(s,0).y. The resulting estimate is

    |(sqrt(Ev))'| <=sqrt((I/h^2)/2) h^4 L(T-h)
                  <=C s^-4 L(T-1/s).

A regularization sqrt(Ev+eta), followed by eta down to zero, handles possible zeros of Ev. The phase may grow quadratically, but its gradient multiplied by v belongs to L2 because the centered variance is finite; cutoff approximation is legitimate. Time-dependent or spatially affine terms do not require a V_t bound.

Integrating from s to infinity, using Ev(infinity)=0, gives

    sqrt(Ev(s))<=C A(h),
    A(h)=int_0^h r^2 L(T-r)dr.

The conformal centered density transport speed is at most sqrt(8Ev). Therefore its remaining transport length is bounded by

    C int_s^infinity A(1/tau)d tau
      =C int_0^h (r-r^2/h)L(T-r)dr
      <=C D(h) ->0.

The equality follows by Tonelli's theorem, so no unjustified exchange of signed integrals occurs. This is the decisive improvement over merely estimating Ev from separate terms in its algebraic identity: taking its exact energy derivative first retains the affine cancellation and uses the known terminal zero.

The densities converge in W2, with their centered second moments converging to 8e_*>0. The existing Townes approximation has bounded conformal scale. If that scale approached zero along a sequence, its density limit would be a point mass, contradicting W2 convergence and the positive limiting centered variance. Thus the scale stays away from zero, and the variance determines its unique positive limit. This independently verifies the Dini-curvature scale conclusion in the companion note.

## 6. Scope

The Dini improvement is an actual weakening of R18's power hypothesis: L(h)=h^-2/log(1/h)^p is admitted for p>1. It is still an additional spatial regularity condition on the effective secondary potential. The static family in Section 2 shows why it does not follow from the current H1 control. Removing that assumption requires a dynamical exclusion of concentrating secondary kinetic energy, or an alternative argument that accommodates it. The total virial cancellation alone does not accomplish either step.

## 7. Additional Proof details of the profile-free scalar theorem

After the companion [sharpness.md](sharpness.md) was written, Sections 2, 3, and 7 were independently checked. Their qualitative argument does not require an already known Townes profile or a quantitative scalar-GN stability constant.

For mass M and normalized gradient A_Q, the sharp-GN maximizing sequence cannot split its mass into m and M-m with 0<m<M: its nonlinear norm is bounded by C_GN[m^(2/d)a+(M-m)^(2/d)(A_Q-a)], strictly below C_GN M^(2/d)A_Q. Nonvanishing supplies a nonzero profile; the contradiction forces full mass in that profile. Strong L2 convergence and bounded H1 imply convergence in the critical nonlinear norm, which is Sobolev-subcritical. Sharpness then forces convergence of gradient norms. This proves strong H1 compactness modulo translations and phases.

At the physical blowup times, gradient normalization makes the bounded scalar energy tend to zero, so the compactness lemma applies. The phase-current estimate gives tightness and a unique terminal measure. Hence the concentrating centers stay bounded and the terminal measure is one full-mass atom. Extended quadratic transport then proves finite whole-field variance at every prior time, without an initial moment assumption.

At the conformal endpoint, if gradients were unbounded along a sequence, the same compactness lemma would force an atom. This contradicts the already obtained W2 limit with positive centered variance. Once conformal gradients are bounded above, the uncertainty inequality gives a positive lower bound. The same lemma at bounded scales, together with the unique W2 density limit, fixes both the center and scale and proves full-time H1 convergence modulo phase.

The kinetic identity in the companion note was also checked directly:

    ||grad v||2^2=h^2(||grad u||2^2-|P|^2/M)+I/4+hI'/4.

Thus the limiting width is the actual kinetic width, not merely a second-moment radius. This audit supports the companion note's qualitative scalar theorem in every finite dimension, under its explicit solution and identity-justification hypotheses. It does not assert a quantitative rate without the additional stability estimate, nor historical novelty.

## 8. Proof details of the projected backward-energy estimate

The complete [backward-energy.md](backward-energy.md) and [structural-synthesis.md](structural-synthesis.md) were read independently after their creation. The mathematical cross-model boundaries in the synthesis are consistent: the arbitrary-dimensional scalar forced theorem is not promoted to an arbitrary-dimensional occupation theorem, the quintic static energy family is not identified with an actual trajectory, and its effective curvature scales like lambda^-1, hence h^-2 on the proposed quadratic branch.

For the backward-energy calculation, the following points were explicitly checked:

- Rotating only the primary constant phase produces the action Hessian E''(A)+omega P1. The fast phase does not reappear in the Hessian coefficients, because the energy is invariant under independent constant component phases. The localized quadratic chirp stays in A; no global quadratic phase change of the error is used.
- The odd transverse form has the stated 5/8 homogeneous coercivity. Its time derivative costs |lambda_t|/lambda by the odd pointwise bound and exponential localization. The fast transverse generator cancels exactly by self-adjointness.
- The primary even-sector coercivity holds on the three displayed real constraints. The spectral values and the identities L_-Q=0 and L_+Lambda Q=-2Q have the correct normalizations.
- The core cross Hessian has amplitude lambda^-1/2 but relative form size lambda^(3/2), because each odd transverse field gains one lambda in its weighted L2 norm and the primary mass part of the energy gives another lambda. Pairing this perturbation with a normalized primary mode has size lambda^(1/2)N_lambda.
- The projection coefficient in the Q direction has no H0 contribution, since H0(iQ_lambda)=0, and no moving-Q contribution, since the error is perpendicular to Lambda Q. The phase and scale projection coefficients can indeed be as large as lambda^-1N_lambda. Their fast contribution to the main energy vanishes; their remaining perturbation pairing is lambda^(1/2)N_lambda. Multiplication gives lambda^-1/2N_lambda^2, precisely O(h^-1) for lambda=kappa h^2.
- The added secondary mass does not introduce an unaccounted fast term. Its complex-linear self-adjoint terms have zero real Hamiltonian pairing; the remaining secondary coefficient is bounded, and the primary-secondary term obeys the preceding form bound.

One wording clarification was sent to the author: the Gram correction satisfies lambda partial_lambda B_lambda=O(lambda^2), not an O(lambda^2) bound on its ordinary lambda or time derivative. The derivative-form estimate uses the logarithmic derivative and is unchanged.

The independently checked conclusion is the stated polynomial backward estimate for that explicitly defined projected linear equation around the smooth static matched family. It is not a nonlinear error estimate for the actual coupled singular evolution. The latter still requires a verified modulation-coordinate reduction, a sufficiently accurate evolving reference field, and nonlinear residual control. No omitted h^-4 energy-growth term was found within the defined projected linear problem.
