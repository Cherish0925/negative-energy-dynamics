# the small-speed spectral pair at a mass-critical ground wave

## Scope

This note proves a conditional spectral bifurcation theorem. The additional hypotheses are ordinary profile nondegeneracy and closed-operator continuity hypotheses, stated explicitly below. It does not prove that every homogeneous dispersion has a nondegenerate ground wave. The result is new to this project; a literature-priority claim is not made.

The main extra information beyond the round 10 Hamiltonian index count is the exact leading growth rate and the translation-coupled denominator. A direct Lyapunov--Schmidt argument proves the pair without invoking an instability index theorem.

## Setting and hypotheses

Let a(D) have a positive elliptic real-even homogeneous symbol of degree m>1. Set alpha=2m/N and

    i u_t = a(D)u - |u|^alpha u.

Let Q be a real ground wave solving (a(D)+1)Q-|Q|^alpha Q=0. Work in the real Hilbert space H=L^2(R^N;C), with J=-i. Assume:

1. Q and its derivatives have sufficient regularity and decay that partial_j Q and Lambda Q belong to the operator domains needed below, where Lambda Q=NQ/2+x·grad Q. In particular critical scaling can be differentiated in L^2 and the profile equation, giving L_+ Lambda Q=-mQ.
2. L_-=a(D)+1-|Q|^alpha is nonnegative, has kernel RQ, and has a bounded inverse on Q-perp. L_+=a(D)+1-(alpha+1)|Q|^alpha has kernel exactly span{partial_j Q}; zero is isolated, and its inverse on the kernel complement is bounded. The index-one property of L_+ holds for a sharp ground wave, but the local pair calculation itself does not need it.
3. There is a C^1 local branch U_(omega,v), with U_(1,0)=Q, solving a(D)U+omega U+i v·grad U-|U|^alpha U=0, and closed under critical scaling up to phase and translation. Its reduced action d(omega,v)=E(U)+omega M(U)/2-v·P(U)/2 is C^2, with d_omega=M/2 and d_v=-P/2. At zero velocity, after translation gauge, D_v U=-i L_-^{-1} grad Q. These assumptions yield the round 10 expansions P=2Tv+o(|v|), B=D_vP=2T+o(1), not an unjustified differentiated o(|v|^2) remainder.
4. The real action Hessian L_v at U_(1,v) is selfadjoint on a common dense domain; its kernel is exactly K_v=span_R{iU_v,partial_1 U_v,...,partial_N U_v}. The kernel bases vary continuously, and the inverse of L_v on K_v-perp, extended by zero on K_v, is norm-continuous as a bounded operator on H. The kernel dimension and the complementary gap persist for small v. A sufficient concrete realization is common domain H^m, operator-norm continuity H^m to L^2, bounded decaying coefficients, and the stated gap/kernel assumptions.

Assumption 4 can also be formulated through norm-resolvent continuity, the isolated zero spectral projection, and a common local inverse. It is the exact input needed to make the finite-dimensional spectral reduction uniform in v.

Define

    T_ij = <partial_i Q,L_-^{-1}partial_j Q>,
    c_j = <Lambda Q,L_-^{-1}partial_j Q>,
    D_Lambda = <Lambda Q,L_-^{-1}Lambda Q> - c^T T^{-1} c.

All quantities are real. L_-^{-1} is taken on Q-perp; <Q,Lambda Q>=<Q,partial_jQ>=0.

## The theorem

Under hypotheses 1--4, T is positive definite and D_Lambda>0. For all sufficiently small nonzero v, when m is not 2, the nonzero spectrum of A_v=J L_v in a fixed neighborhood of zero consists of precisely one simple pair, with

    lambda(v)^2 = (m-2) v^T T v / D_Lambda + o(|v|^2).

For m>2 the pair is real and

    lambda_+(v) = sqrt((m-2) v^T T v / D_Lambda) + o(|v|),
    lambda_-(v) = -lambda_+(v).

Thus these waves are spectrally unstable, with an instability time scale proportional to |v|^{-1}. This time scale refers to linear growth, not a proved nonlinear escape-time estimate.

For 1<m<2 the pair is purely imaginary and

    lambda_+(v) = i sqrt((2-m) v^T T v / D_Lambda) + o(|v|),
    lambda_-(v) = -lambda_+(v).

This local calculation alone does not exclude unstable spectrum away from zero. Under the round 10 index hypotheses and n_-(L_v)=1, that exclusion follows from the established Hamiltonian index formula. No asymptotic stability claim follows.

At m=2 the coefficient vanishes; the theorem gives no nonzero leading term. For general degree-two homogeneous symbols one cannot replace that statement by Galilean invariance.

If Q is even under x -> -x, then c=0 and the denominator simplifies. Evenness is not otherwise required.

## Proof

### Positivity and independence of the center

The inverse of L_- is strictly positive on Q-perp, so T>0 because no nonzero directional derivative of a nonzero L^2 function can vanish. Let

    Lambda_perp Q = Lambda Q - sum_j (T^{-1}c)_j partial_j Q.

Then

    D_Lambda = <Lambda_perp Q,L_-^{-1}Lambda_perp Q>.

This is positive: equality would imply Lambda Q=zeta·grad Q, hence (x-zeta)·grad Q+NQ/2=0. The associated mass-preserving dilation group would fix Q; a nonzero L^2 function cannot be homogeneous of degree -N/2 about a point. Integration in polar coordinates, or the unitary dilation group, gives the contradiction.

Changing the spatial center adds a linear combination of partial_j Q to Lambda Q. The Schur expression D_Lambda is invariant under that change. It is therefore a geometric quantity of the orbit, not a choice of origin.

### Exact finite-dimensional reduction

Write g_0=iU_v and g_j=partial_j U_v (j=1,...,N). Their span K_v is isotropic for J:

    <g_i,Jg_j>=0.

For phase-translation pairings this is integration of a mass derivative. For two translations it is commutation of the translation charges; equivalently, in Fourier variables the relevant pairing is purely imaginary before taking the real part.

Let Pi_v be orthogonal projection onto K_v and Pi_c=I-Pi_v. Put

    L_c = L_v restricted to K_v-perp,
    J_c = Pi_c J Pi_c,
    R_v(lambda) = (L_c+lambda J_c)^{-1} on K_v-perp,

extended by zero on K_v. The inverse exists and is analytic for |lambda|<rho, with rho>0 independent of sufficiently small v, by a Neumann series and the uniform bounded inverse assumption. The spectrum is considered on the complexification of the real Hilbert space; real pairings below extend complex bilinearly.

The eigenvalue equation J L_v psi=lambda psi is equivalent to

    (L_v+lambda J)psi=0.

Write psi=k+w, k in K_v and w in K_v-perp. For lambda nonzero,

    w=-lambda R_v(lambda) Jk,

and the remaining kernel equation is exactly

    D(lambda,v) z=0,
    D_ij(lambda,v)=<g_i,J R_v(lambda) Jg_j>,
    k=sum_j z_j g_j.

The omitted common scalar factor is -lambda^2. Thus for lambda nonzero in the uniform disk, the kernel of D is naturally isomorphic to the eigenspace. The same analytic block elimination preserves algebraic multiplicities away from lambda=0.

Selfadjointness of L_c and skew-adjointness of J imply

    D(-lambda,v)=D(lambda,v)^T.

At lambda=0, profile differentiation gives

    L_v partial_omega U=-U,
    L_v partial_vj U=-i partial_j U=Jg_j.

Kernel components of the parameter derivatives have no effect, by isotropy. Consequently

    D(0,v)=C d''(1,v) C,  C=diag(1,-I_N).

In particular D_vv(0,v)=-B(1,v)/2. Since B=2T+o(1), this N by N block stays invertible for small lambda,v.

Take its scalar Schur complement f(lambda,v). The transpose identity gives

    f(-lambda,v)=f(lambda,v).

Hence f is analytic in z=lambda^2, with a uniform radius and coefficients continuous in v. At lambda=0 its value is the charge-Hessian Schur complement calculated exactly in round 10:

    f(0,v)= [P^T B^{-1}P-(m-1)v·P]/(2m^2)
          = (2-m)v^TTv/m^2+o(|v|^2).

No second velocity derivative of U is required here: the last equality uses only P=2Tv+o(|v|), B=2T+o(1), and the exact scaling identity.

### The coefficient of lambda^2, including translation coupling

Let R=Lambda Q/m. For the following block calculation first replace R by R_0, its L^2-orthogonal projection off span{partial_jQ}; this is the unique complement representative of the frequency derivative. Put Z_j=L_-^{-1}partial_jQ and W_0=L_-^{-1}R_0. At v=0,

    L_0=diag(L_+,L_-), J(h,b)=(b,-h),
    L_c^{-1}Jg_0=(-R_0,0),
    L_c^{-1}Jg_j=(0,-Z_j).

Expand the exact resolvent in lambda. Denoting b_j=<R_0,Z_j>, the relevant entries are

    D_00(lambda,0)=lambda^2 <R_0,L_-^{-1}R_0>+O(lambda^4),
    D_0v(lambda,0)=lambda b^T+O(lambda^2),
    D_v0(lambda,0)=-lambda b+O(lambda^2),
    D_vv(lambda,0)=-T+O(lambda).

In fact additional parity in real/imaginary blocks sharpens some remainders, but is unnecessary. The scalar Schur complement is even, so its coefficient is

    partial_z f(0,0)
      =<R_0,L_-^{-1}R_0>-b^TT^{-1}b
      =D_Lambda/m^2 >0.

The last equality is invariance of the Schur expression under adding translations to R. Thus

    f(lambda,v)
      =(2-m)v^TTv/m^2+o(|v|^2)
       +lambda^2 (D_Lambda/m^2+o(1)) + O(lambda^4),

with the lambda remainder uniform for small v. This is an operator-resolvent expansion, not a formal expansion of the nonlinear profile to fourth order.

### Existence, uniqueness, sign, and simplicity of the pair

Set z=lambda^2. The real analytic scalar equation f(z,v)=0 has partial_z f(0,0)=D_Lambda/m^2>0. The implicit-function theorem (or uniform monotonicity plus analytic inversion) produces one real root z(v) near zero, satisfying

    z(v)=(m-2)v^TTv/D_Lambda+o(|v|^2).

The root is unique in a fixed sufficiently small complex z disk. For m not 2 and nonzero small v it is nonzero, because T>0. Its sign is the sign of m-2, and each of its two square roots is simple: partial_lambda f=2lambda partial_z f is nonzero. The block elimination above gives exactly the asserted eigenpair and excludes additional nonzero eigenvalues near zero. This completes the spectral proof.

## Frequency scaling

If the branch is chosen with exact scaling covariance, write w=v omega^{-(m-1)/m}. Linearized eigenvalues scale as

    lambda(omega,v)=omega lambda(1,w).

Thus for fixed omega>0 and v->0,

    lambda_+(omega,v)
      =omega^{1/m} sqrt((m-2)v^TTv/D_Lambda)+o(|v|)

when m>2. T and D_Lambda in this display are evaluated at the omega=1 ground wave. The factor omega^{1/m} is fixed by dimensions; changing frequency normalization without it would be incorrect.

## Nonlinear implication: what must additionally be supplied

A growing eigenpair is already a time-evolution result. Nonlinear orbital instability requires a local-flow argument. It follows under the usual semilinear instability hypotheses: a well-defined sufficiently differentiable local flow in a specified Banach phase space, a nonlinear remainder of order 1+rho, rho>0, and the linear evolution bounds / unstable-manifold construction needed to compare nonlinear trajectories with the unstable eigenmode. These hypotheses should be checked for an actual operator/nonlinearity and phase space, not asserted for every real-even homogeneous symbol.

For polynomial nonlinearities, H^s with s>N/2 and s sufficiently large gives a convenient semilinear realization: the nonlinearity is smooth on H^s, the dispersive group is unitary, and a bounded profile potential gives a bounded perturbation of its generator. One can then use the isolated real eigenvalue and a Hamiltonian exponential-trichotomy theorem to construct a local unstable manifold. Membership of the eigenfunction, spectral decomposition bounds, and the free phase/translation orbit must still be recorded. This note does not claim a general unconditional nonlinear theorem from the spectral result alone.

The previously obtained index count establishes only that one positive real eigenvalue exists, when all its assumptions hold. The new calculation determines that this eigenvalue emerges from the mass-critical scaling chain and measures its rate directly.

## Primary literature checked

* Z. Lin and C. Zeng, Instability, index theorem, and exponential trichotomy for Linear Hamiltonian PDEs, arXiv:1703.04016, v4 (2021). Primary source: https://arxiv.org/abs/1703.04016 . Supplies established Hamiltonian index / exponential-trichotomy background, not the present explicit coefficient.
* A. Comech, On the meaning of the Vakhitov--Kolokolov stability criterion for the nonlinear Dirac equation, arXiv:1107.1763 (2011). Primary source: https://arxiv.org/abs/1107.1763 . Establishes generic emergence of a real eigenpair at a charge-slope degeneracy in another Hamiltonian field model. The principle of a pair leaving the origin is established theory.
* V. Iyer, R. Parker, A. G. Stefanov, Existence and stability for traveling waves of fourth order semilinear wave and Schrodinger equations, arXiv:2512.12390. Full primary HTML https://arxiv.org/html/2512.12390v1 inspected. Its fourth-order NLS application is a one-dimensional mixed-dispersion cubic equation (equation 1.6), and its beam-wave result uses a real fourth-order profile with c^2 partial_xx. It does not directly prove the present mass-critical pure homogeneous small-velocity coefficient.
* I. Naumkin and P. Raphael, On small travelling waves to the mass critical fractional NLS, arXiv:1712.04484. Primary source: https://arxiv.org/abs/1712.04484 . Constructs sub-ground-mass traveling waves and studies the small-mass limit; that limit differs from the zero-velocity perturbation of a mass-critical standing ground wave considered here.

Search was not sufficient to certify novelty priority. This result should be described as a derived theorem in this project, with its relationship to established slope/index bifurcation theory made explicit.

## Closing targeted primary comparison

1. Bugiera--Lenzmann--Schikorra--Sok, On symmetry of traveling solitary waves for dispersion generalized NLS, Nonlinearity 33 (2020), primary full text https://arxiv.org/html/1908.06771v1 . Their Theorem 1 uses a real continuous symbol with A|xi|^(2s)+c <= p(xi) <= B|xi|^(2s), s>=1/2, energy-subcritical 0<sigma<sigma_*(s,N), and omega>−inf_xi[p(xi)−v·xi]. It gives compact minimizing sequences and boosted ground-wave existence. Consequently its equation class genuinely includes homogeneous m>2 at mass criticality sigma=m/N. Additional integer-power and symbol hypotheses yield cylindrical/conjugation symmetry. The article does not provide real-profile nondegeneracy, a differentiable local branch through a specified Q, or the present small-speed spectral coefficient. Its Theorem 1 attributes the existence argument to Himmelsbach's thesis.

2. Himmelsbach, Blowup, solitary waves and scattering for the fractional nonlinear Schroedinger equation (2017), primary university record https://edoc.unibas.ch/entities/publication/f9e6d037-f942-4e48-84ce-6888d3b3a221 . The inspected abstract describes boosted-profile existence, symmetry and spatial decay; the thesis PDF was not accessible through the rendered record. Do not claim a full-text novelty exclusion based on this abstract.

3. Bonheure--Casteras--Gou--Jeanjean, Strong instability of ground states to a fourth order Schroedinger equation, primary https://arxiv.org/pdf/1703.07977 . Theorem 1.2 includes pure quartic dispersion, mass criticality sigma*N=4, N>=2, and radial standing ground waves. It proves nonlinear instability through perturbations blowing up in finite or infinite time. This is a genuine earlier instability theorem in a matched standing model. It neither gives a nonzero-velocity spectral pair nor its small-speed coefficient. Our conditional spectral theorem is not uniformly stronger than that nonlinear theorem and should not be described as superseding it.

4. Iyer--Parker--Stefanov, primary https://arxiv.org/html/2512.12390v1 , equation 1.6 is a one-dimensional mixed-dispersion cubic NLS. Its quartic principal-order mass-critical power would be alpha=8, whereas its cubic alpha=2 is mass-subcritical. The beam-wave profile has c^2 partial_xx, not the complex i v partial_x term of the pure Schrödinger traveler. Hence neither criticality nor the profile family matches the present theorem directly.

The targeted search did not locate the explicit formula (m−2)v^T T v / D_Lambda in these sources. This supports precise differentiation of hypotheses and conclusions, not a definitive first-in-literature claim.
