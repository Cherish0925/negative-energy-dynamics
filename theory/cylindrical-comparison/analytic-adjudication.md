# Independent analytic adjudication of the cylindrical blowup conflict

Date: 2026-10-07.

This note establishes the analytic implication from the validated stationary-profile certificate to counterexamples to Theorem 1.2 of T. Gou, *Blowup of cylindrically symmetric solutions for biharmonic NLS*, arXiv:2205.08167v3 (4 November 2024). It does not replace the numerical certificate. The parent audit reports a fresh 9/9 certificate rerun and a strict inverse-pairing upper bound `I_upper = -175.1586348`; the proof below only needs the qualitative inequality I < 0 and the stated inverses.

## 1. Exact inputs and conventions

Work on R^4, write x=(y,s), y in R^3, and use

    i u_t = Delta^2 u - mu Delta u - |u|^2 u,       mu >= 0.

For f in H^2(R^4;C), define

    M(f) = integral |f|^2,
    P(f) = Im integral conjugate(f) partial_s f,
    G(f) = integral |gradient f|^2,
    E_mu(f) = (1/2) integral |Delta f|^2 + (mu/2) G(f)
              - (1/4) integral |f|^4.

The real Hilbert pairing is Re integral conjugate(f) g. The Fourier convention is partial_s -> i xi_s.

The certificate inputs are:

1. A nonzero real radial Q in H^2(R^4) solving Delta^2 Q + Q - Q^3 = 0.
2. The real operators L_+ = Delta^2 + 1 - 3Q^2 and L_- = Delta^2 + 1 - Q^2 are boundedly invertible H^{-2} -> H^2 on the following respective symmetry components: O(3)-invariant and even in s for L_+; O(3)-invariant and odd in s for L_-.
3. With z = L_-^{-1} partial_s Q, the real duality pairing

       I = <partial_s Q, z>

   is strictly negative.

There is no inverse claim on a space containing the phase or translation kernel. These symmetry components exclude those kernels; the certificate must exclude any additional kernels.

## 2. Two-parameter continuation and the signs

Let X be the closed real-linear subspace of H^2 consisting of f satisfying

    f(Oy,s)=f(y,s) for every O in O(3),
    f(y,-s)=conjugate(f(y,s)).

Let Y be the corresponding symmetry subspace of H^{-2}. The map

    F(mu,v,f) = Delta^2 f - mu Delta f + f + i v partial_s f - |f|^2 f

is real analytic R^2 x X -> Y. Indeed the lower-order operators are bounded H^2 -> H^{-2}, and H^2(R^4) embeds into L^4, which makes the cubic a continuous polynomial to H^{-2}. At (0,0,Q), the derivative is L_+ on the real component and i L_- on the imaginary component. Input 2 and the analytic implicit-function theorem therefore give a real-analytic family U_{mu,v} in X for (mu,v) sufficiently close to (0,0), satisfying

    Delta^2 U - mu Delta U + U + i v partial_s U - |U|^2 U = 0.    (2.1)

The function u(t,x)=exp(i t) U_{mu,v}(x-v t e_s) is consequently an exact solution whenever the regularity needed for substitution is established below. This sign follows directly from i u_t = exp(i t)(-U - i v partial_s U).

The real gradient of P is -2 i partial_s f. Thus (2.1) is the Euler-Lagrange equation of

    S_{mu,v}(f) = E_mu(f) + M(f)/2 - v P(f)/2.

At mu=0, differentiating (2.1) in v at zero gives

    partial_v U_{0,0} = -i z,
    U_{0,v} = Q - i v z + O_{H^2}(v^2).

Direct expansion of momentum gives

    P(Q - i v z) = v integral (z partial_s Q - Q partial_s z)
                  = 2v <partial_s Q,z> = 2Iv.

Conjugation maps the equation with v to the equation with -v. Local uniqueness implies U_{mu,-v}=conjugate(U_{mu,v}); hence P(U_{mu,v}) is odd in v. Analyticity then gives

    P(U_{mu,v}) = 2Iv + O(|mu v| + |v|^3).                       (2.2)

All signs in these formulas are fixed by the equation and the stated definition of P, not by convention switching.

## 3. Complete weighted elliptic argument

### Lemma

Suppose mu>=0, omega>0, and W in H^2(R^4;C) solves

    A W = |W|^2 W,
    A = Delta^2 - mu Delta + omega + i v partial_s,

and suppose

    c = omega - 3(|v|/4)^(4/3) > 0.                            (3.1)

Then W belongs to H^4, tends uniformly to zero at spatial infinity, and x_j W belongs to H^4 for every coordinate j. In particular sW belongs to L^2.

### Proof

In four dimensions H^2 embeds into L^6. Thus |W|^2 W belongs to L^2, while Delta W and partial_s W also belong to L^2. The equation implies Delta^2 W belongs to L^2, hence W belongs to H^4. Furthermore its Fourier transform is integrable: by Cauchy-Schwarz, the integral of |W_hat| is at most ||W||_{H^4} times the square root of the finite integral of (1+|xi|^2)^(-4) over R^4. Fourier inversion and the Riemann-Lebesgue lemma therefore give W in C_0(R^4).

The Fourier symbol is

    a(xi) = |xi|^4 + mu |xi|^2 + omega - v xi_s.

Since mu>=0,

    a(xi) >= omega + |xi|^4 - |v| |xi|
           >= omega - 3(|v|/4)^(4/3) = c.

For these fixed parameters, a(xi) is also comparable to 1+|xi|^4: at large |xi| its leading term is |xi|^4, and on a fixed compact set the positive lower bound c applies. Consequently

    ||A^{-1}h||_2 <= c^{-1}||h||_2,
    ||A^{-1}h||_{H^4} <= C_A ||h||_2.                           (3.2)

Fix a coordinate j. Choose a real smooth cutoff chi on R with 0<=chi<=1, chi=1 on [-1,1], and chi=0 outside [-2,2]. For L>=1 let

    w_L(x) = x_j chi(x_j/L).

For each finite L the product w_L W is in H^4. The kth derivative of w_L with respect to x_j obeys ||w_L^(k)||_infinity <= C_k L^(1-k), for 1<=k<=4. The full commutator is

    [A,w_L]W = 4 w_L' partial_j Delta W
                + 2 w_L'' Delta W + 4 w_L'' partial_j^2 W
                + 4 w_L''' partial_j W + w_L'''' W
                - mu(2 w_L' partial_j W + w_L'' W)
                + i v delta_{j,s} w_L' W.                     (3.3)

Thus, uniformly for L>=1,

    ||[A,w_L]W||_2 <= C_chi (1+mu+|v|) ||W||_{H^3} =: C_0.

Multiplying the profile equation by w_L gives

    A(w_L W) = |W|^2 w_L W + [A,w_L]W.                        (3.4)

Choose a fixed R_0 so large that |W(x)|^2 <= c/2 whenever |x|>R_0. On the ball |x|<=R_0, one has |w_L(x)|<=|x_j|<=R_0 for every L. Apply the first bound in (3.2) to (3.4):

    c ||w_L W||_2
      <= || |W|^2 w_L W ||_2 + C_0
      <= (c/2)||w_L W||_2 + R_0||W||_infinity^2||W||_2 + C_0.

After absorption, ||w_L W||_2 is bounded uniformly in L. The right side of (3.4) is consequently bounded in L^2 uniformly in L; the second bound in (3.2) makes ||w_L W||_{H^4} uniformly bounded as well. A subsequence converges weakly in H^4. On every compact set w_L=x_j for all sufficiently large L, so the distributional limit is x_j W. Therefore x_j W belongs to H^4. This proves the lemma.

No weighted bound on W was assumed in this argument. Its inputs are H^2 regularity, the equation, and the positive free-symbol gap (3.1).

For the IFT branch omega=1, condition (3.1) holds for every sufficiently small v, uniformly for mu>=0. Consequently U_{mu,v} belongs to Gou's initial-data class

    Sigma_4 = {f in H^2: f(y,s)=f(|y|,s), sf in L^2}.

The H^4 regularity makes the exact solution substitution valid in L^2. Every finite-time translated profile remains in Sigma_4. Its H^2 norm is constant for all real t.

## 4. Pohozaev identity, including positive second-order dispersion

For a branch member U, use the mass-preserving curve U_lambda(x)=lambda^2 U(lambda x). The weighted lemma ensures this curve is differentiable at lambda=1 in H^2: x_j U in H^4 implies x dot gradient U in H^3. Its mass, fourth-order kinetic energy, gradient energy, quartic term, and momentum scale respectively as lambda^0, lambda^4, lambda^2, lambda^4, and lambda.

Stationarity of S_{mu,v} yields

    0 = 4 E_mu(U) - mu G(U) - (v/2) P(U).

Therefore

    E_mu(U) = v P(U)/8 + mu G(U)/4.                           (4.1)

In particular E_0(U_{0,v})=Iv^2/4+O(v^4)<0 for all sufficiently small nonzero v.

To obtain positive mu, let G_0=G(Q)>0 and choose a fixed

    0 < eta < -I/G_0.

Set mu=eta v^2. Along this curve (2.2) gives P(U_{eta v^2,v})=2Iv+O(v^3). The same analyticity and conjugation symmetry imply G(U_{eta v^2,v})=G_0+O(v^2). Hence (4.1) gives

    E_{eta v^2}(U_{eta v^2,v})
      = (I/4 + eta G_0/4) v^2 + O(v^4) < 0                  (4.2)

for every sufficiently small nonzero v. For example eta=-I/(2G_0) gives the leading coefficient I/8<0. The sign of the mu contribution is positive; the negative inertia contribution dominates it by the explicit choice of eta.

Thus the same three certificate inputs provide exact global constant-H^2 negative-energy solutions both at mu=0 and at some strictly positive mu. No new stationary-profile or spectral certificate is needed for this positive-mu continuation.

## 5. Scaling to every prescribed positive mu

Fix one counterexample at mu'=eta v^2>0 and any desired coefficient mu_*>0. Let

    lambda = sqrt(mu_*/mu'),
    Phi(x) = lambda^2 U_{mu',v}(lambda x),
    omega_* = lambda^4,
    v_* = lambda^3 v.

Then

    u_*(t,x) = exp(i omega_* t) Phi(x-v_* t e_s)

solves the equation with coefficient mu_*. This follows either by direct substitution or by applying the spacetime scaling lambda^2 u(lambda^4 t,lambda x); the transformed coefficient is precisely lambda^2 mu'. Moreover

    M(Phi)=M(U),
    P(Phi)=lambda P(U),
    G(Phi)=lambda^2 G(U),
    E_{mu_*}(Phi)=lambda^4 E_{mu'}(U)<0.

Scaling preserves cylindrical symmetry and finiteness of the axial L^2 moment. The transformed solution is global for every real t with constant finite H^2 norm. Thus the logical consequence of Inputs 1--3 is a counterexample to the finite-time assertion for every fixed mu_*>0, with frequency and velocity allowed to vary. Gou's theorem has no fixed-frequency or fixed-velocity restriction.

## 6. Exact diagnosis of the virial closure

Gou's equation (2.2) uses

    phi_R(y,s)=psi_R(|y|)+s^2/2,
    M_phi(f)=2 Im integral conjugate(f) gradient(phi_R) dot gradient(f).

Its transverse gradient is bounded, but its axial gradient equals s and is unbounded. The valid estimate is

    |M_phi(f)|
      <= 2||gradient psi_R||_infinity ||f||_2 ||gradient_y f||_2
          + 2||s f||_2 ||partial_s f||_2.                    (6.1)

The initial condition s u_0 in L^2 gives no time-uniform bound on ||s u(t)||_2. Therefore the bounded-gradient estimate used in the radial localized-virial argument cannot be imported without an additional argument controlling that factor.

For our exact traveling solution a change of variables, without approximation or asymptotic error, gives

    M_phi(u(t)) = M_phi(U)+2vt P(U).                         (6.2)

The modulus of a PT-symmetric branch member is even in s. Its axial first moment therefore vanishes, and

    ||s u(t)||_2^2 = ||s U||_2^2 + v^2 t^2 M(U).            (6.3)

At mu=0, (4.1) and (6.2) imply

    d M_phi(u(t))/dt = 2vP(U)=16E_0(U)<0,

while ||u(t)||_{H^2} is exactly constant. Negative virial slope and absence of H^2 growth coexist because the moment in (6.1) grows. Thus the missing estimate is not a harmless omission that the initial finite moment automatically repairs.

At positive mu one likewise has

    d M_phi(u(t))/dt = 2vP(U)=16E_mu(U)-4mu G(U)<0.

This is also consistent with the leading virial expression in Gou's argument and with the exact global wave; the problem is the subsequent inference from virial decrease to H^2 blowup.

## 7. Precise adjudication and scope

Gou's public v3 Theorem 1.2 assumes d>=4, mu>=0, mass criticality, u_0 in Sigma_d, and E_mu(u_0)<0. In d=4 the constructed initial profiles satisfy every one of these assumptions, including the finite axial moment established from the profile equation above. The exact solutions exist for all real times and have constant finite H^2 norm.

Therefore, once Inputs 1--3 are accepted on the independent certificate audit, the original statement of Theorem 1.2(ii) at mu=0 is false under its energy-space blowup meaning; and Theorem 1.2(i) is false at every fixed mu>0 by Sections 4--5. The positive-mu case removes any possible ambiguity about interpreting infinite-time blowup as mere growth of an axial weighted moment.

The conclusion concerns the stated theorem and its proof, not every result in Gou's article. No claim about Theorem 1.1 is established here. Nor does this contradict the Boulenger--Lenzmann or Dinh radial theorems: the traveling profiles are cylindrically symmetric but not fully radial for nonzero v.

Primary source: https://arxiv.org/html/2205.08167v3 ; Theorem 1.2, definition of Sigma_d, equation (2.2), and the proof of Theorem 1.2.
