# Conserved internal correlations and critical focusing dynamics

## Scope and notation

This note connects the dimension-independent quantitative polarization theorem of round 11 to actual time evolution. It uses the same common scalar dispersion and total-density interactions, and does not introduce noncommuting internal couplings or component-dependent frequencies.

Let H be a nonzero separable complex Hilbert space, N>=1, m>1, s=m/2. Let a be a positive elliptic real-even m-homogeneous Fourier symbol. The Fourier transform is unitary, with factor (2 pi)^(-N/2). Write

    rho_U(x)=||U(x)||_H^2,
    M(U)=integral rho_U,
    A(U)=integral a(xi)||Uhat(xi)||_H^2 dxi.

The interaction is either local, F(U)=integral rho_U^kappa with kappa=1+m/N, or the positive-definite Hartree interaction F(U)=D(rho_U,rho_U), kappa=2, under the assumptions of round11_systems_section.tex. Put r=kappa-1. Let b>=0 be a common real scalar multiplier, of order at most m, and B(U)=integral b||Uhat||^2. No dilation inequality on b is needed here. The equation and energy are

    i U_t=(a+b)(D)U - V_{rho_U}U,
    E(U)=(A(U)+B(U))/2 - F(U)/(2 kappa).

The general dynamical conclusions below assume a conservative local energy-space flow with the continuation property: a finite endpoint of its maximal interval requires the energy-space norm to become unbounded. This assumption is verified without dispersive estimates for the concrete quartic local models in N=1,2,3 discussed below.

The sharp scalar critical mass Mc is normalized by

    F(u) <= kappa (M(u)/Mc)^r A(u).

Round 11 proves the same sharp inequality for all internal dimensions, and a dimension-independent constant C such that p(U)<=C d(U), where

    d(U)=1-F(U)/[kappa (M(U)/Mc)^r A(U)],
    p(U)=inf_{||zeta||=1,q} [M(U-zeta q)/M(U)+A(U-zeta q)/A(U)].

No scalar optimizer uniqueness or real-sector nondegeneracy is needed for that theorem.

## 1. The full internal correlation operator is conserved

Define the positive trace-class operator on H

    Gamma(U)=integral |U(x)><U(x)| dx.

It satisfies Tr Gamma=M. Its largest eigenvalue mu=||Gamma||op exists for every nonzero U, including when H is infinite-dimensional. Define the conserved fraction

    chi=1-mu/M,     0<=chi<1.

Proposition. Along the common scalar flow, Gamma(U(t))=Gamma(U(0)) as trace-class operators.

Proof. For fixed internal h,k, set u_h=<h,U> and u_k=<k,U>. These scalar components solve the same time-dependent spatial equation i u_t=H(t)u, where H(t)=(a+b)(D)-V_{rho_U} is self-adjoint as an energy-space form. The Hilbert-triple product rule gives

    d/dt integral u_h conjugate(u_k)
      = -i <H(t)u_h,u_k> + i <u_h,H(t)u_k> = 0.

The pairings are well-defined: for local powers use Holder in L^{2 kappa}, and for Hartree use HLS and the density-space Cauchy inequality. The kinetic form is continuous on H^s. Solutions lie in C H^s with time derivative in C H^{-s}, which suffices for the product rule. Equality for a countable dense set of h,k, followed by continuity, proves operator equality. In addition,

    ||Gamma(U)-Gamma(W)||_1
       <= (||U||_2+||W||_2)||U-W||_2,

so no topology ambiguity remains at energy-space limits. This proves the proposition.

The eigenvalues are conserved populations of orthogonal spatial modes. Dividing one identical spatial profile among many internal components does not lower mu: such a field still has rank-one Gamma and mu=M.

## 2. A strict mass-threshold improvement determined by the initial state

Theorem. There exists c>0, depending only on the scalar dispersion and interaction and not on internal dimension, such that

    F(U) <= kappa (M/Mc)^r (1-c chi) A(U).                 (2.1)

One can take c=min(C^{-1},1/2), where C is the quantitative polarization constant of round 11.

Proof. For any unit internal vector zeta, the best scalar q in the L2 approximation is q(x)=<zeta,U(x)>. Its squared error is

    inf_q M(U-zeta q)=M-<zeta,Gamma zeta>.

Taking the infimum over zeta gives M-mu=M chi. The kinetic term in p is nonnegative, so p(U)>=chi. Consequently d(U)>=chi/C and (2.1) follows. This argument is exact and does not need a profile decomposition at individual times.

For reference, if Gamma_A=integral a(xi)|Uhat(xi)><Uhat(xi)| dxi, the full distance has the exact formula

    p(U)=2-lambda_max(Gamma/M+Gamma_A/A).

Indeed the same pointwise scalar projection minimizes the combined Hilbert norm. Since Gamma_A/A is positive with trace one, this also gives p>=chi. Gamma_A is not assumed to be conserved.

Corollary (global bounded flow above the scalar critical mass). Let

    eta=1-(M/Mc)^r(1-c chi).

If eta>0 at the initial time, then eta is constant and

    E(U(t)) >= eta A(U(t))/2+B(U(t))/2,
    sup_t [A(U(t))+B(U(t))] <= 2 E(U(0))/min(eta,1).

Thus the conservative local flow is global in both time directions and uniformly bounded in its energy space. In particular every state with chi>0 has a nonempty globally controlled mass interval

    M < Mc (1-c chi)^(-1/r),

which extends strictly above Mc. The endpoint equality eta=0 is not included.

For example take two L2-orthonormal spatial functions f,g and U0=sqrt(M/2)(f,g). Then chi=1/2. Every such initial field is globally bounded if M<Mc(1-c/2)^(-1/r), regardless of the shape of f and g, subject only to finite initial energy.

Corollary (exact scalar reduction of critical-mass unbounded evolution). If M=Mc and A(U(t_n))+B(U(t_n)) becomes unbounded along any sequence in a conservative orbit, then chi=0. Therefore Gamma has rank one. Its range is a fixed complex line spanned by zeta, and

    U(t,x)=zeta u(t,x)

for every time in the maximal interval. The scalar field u solves the original scalar equation and M(u)=Mc. This conclusion concerns the initial data and the entire orbit, not just a rescaled limiting core.

Proof of the rank statement. If Gamma=M|zeta><zeta|, then for every h perpendicular to zeta, integral |<h,U>|^2=<h,Gamma h>=0. A countable orthonormal basis of zeta-perp gives U(x) in span(zeta) almost everywhere. Conservation of Gamma fixes this line for all times. If chi>0, the preceding energy bound contradicts unboundedness, proving the result.

More generally, unbounded evolution at a fixed finite mass must satisfy

    chi <= c^{-1}[1-(Mc/M)^r].                            (2.2)

For M=Mc(1+epsilon), this gives chi <= (r/c)epsilon+O(epsilon^2). Thus any near-minimal-mass singular or grow-up orbit must already have almost all of its internal mass in one fixed mode. No claim of existence of such scalar orbits is made here.

## 3. Complementary control at arbitrarily large total mass

This section is an elementary homogeneous-symbol version of the established Lieb--Thirring/Rumin kinetic-energy argument. It is included to identify what the conserved operator norm controls, not to claim priority for the method or the conservation law.

Set t=m/N and

    V_a=(2 pi)^(-N) measure{xi:a(xi)<1}.

Theorem (explicit kinetic-density estimate). For every Hilbert-valued U in H^{m/2},

    integral rho_U^{1+t}
       <= (1+t)(1+2t) V_a^t mu^t A(U).                  (3.1)

Here mu=||Gamma(U)||op. No finite-dimensional restriction or orthogonality hypothesis in a preselected internal basis is required.

Proof. Define the positive spatial density matrix gamma=sum_j |u_j><u_j| on L2. It and Gamma have the same nonzero eigenvalues, since they are the two products of the Hilbert--Schmidt map associated with U and its adjoint (up to conjugating one coordinate convention). Thus 0<=gamma<=mu I.

Let P_E=1_{a(D)<=E}. Its constant diagonal is V_a E^{1/t}. Consequently

    ||P_E U(x)||_H^2 <= mu V_a E^{1/t}.

The reverse triangle inequality yields

    ||(1-P_E)U(x)||_H^2
       >= (sqrt(rho_U(x))-sqrt(mu V_a) E^{1/(2t)})_+^2.

Layer-cake in the spectral variable gives

    A(U)=integral_0^infinity ||(1-P_E)U||_2^2 dE.

Integrating the preceding pointwise inequality in E, then in x, gives

    A(U)>= (mu V_a)^(-t) integral rho_U^{1+t}
                    * integral_0^1 (1-y^{1/(2t)})^2 dy.

The last integral equals [(1+t)(1+2t)]^{-1}, proving (3.1). Finite-rank approximation and Tonelli extend the argument to arbitrary separable H.

For the local critical nonlinearity kappa=1+t, energy therefore satisfies

    E(U)>=1/2 [1-(1+2t)V_a^t mu^t] A(U)+B(U)/2.         (3.2)

Thus all finite-energy initial data satisfying

    mu < V_a^{-1}(1+2t)^(-1/t)                          (3.3)

produce global bounded conservative flow, with no upper bound on total mass M. For any prescribed finite M one can choose enough mutually L2-orthogonal modes, each with squared L2 norm below (3.3), to meet the condition. The required number of modes can grow with M; this is not a scalar large-mass global theorem.

The sharp near-Mc estimate (2.1) and the explicit occupation estimate (3.1) complement each other. A unified local energy coefficient is

    Theta=min{(M/Mc)^t(1-c chi), (1+2t)V_a^t mu^t}.

Whenever Theta<1, energy controls the kinetic norm. The first term retains the exact scalar Mc and improves it for every nonzero chi; the second remains effective at arbitrarily large total mass.

For the Hartree interaction, put 0<t=m/N<1 and let H_K be any HLS constant such that

    |D(rho,rho)| <= H_K ||rho||_{2/(2-t)}^2.

Interpolation between L1 and L^{1+t}, followed by (3.1), gives

    F(U)<=H_K (1+t)(1+2t)V_a^t M^{1-t}mu^t A(U).

The corresponding complementary Hartree coefficient is

    Theta_H=min{(M/Mc)(1-c chi),
        (H_K/2)(1+t)(1+2t)V_a^t M^{1-t}mu^t}.

The same energy conclusion holds if Theta_H<1. No assertion that these explicit occupation constants are sharp is made.

## 4. Concrete unconditional quartic realization

Take N=1,2,3, m=4, a a real positive elliptic homogeneous quartic symbol (a(xi)=|xi|^4 is the basic case), and a real b>=0 satisfying b(xi)<=C(1+|xi|^4). Consider

    i U_t=(a+b)(D)U-||U||_H^{8/N}U,
    U0 in H2(R^N;H).

The linear group is unitary on H2. Since H2 embeds into Linfinity in these dimensions, the map z -> ||z||^{8/N}z is locally Lipschitz on H2(H), with constants independent of internal dimension. The elementary chain rule uses derivatives up to order three of this Hilbert-space radial map; 8/N>2 makes them bounded on bounded balls. Hence the Duhamel contraction gives a unique maximal C H2 solution with the H2 continuation property. Symmetric Fourier Galerkin approximations preserve mass and energy, and converge in C H2 on the local existence interval; continuity of the energy then yields conservation. The operator Gamma is conserved by the product-rule argument above.

Therefore all conclusions of Sections 1--3 are unconditional for these concrete quartic equations, including countably many internal components. They do not require curvature-based Strichartz estimates, radial symmetry, a moment assumption, or proximity to a coherent wave.

For a(xi)=|xi|^4, V_a=|B_N|/(2 pi)^N, and (3.3) reads

    mu < (2 pi)^N/|B_N| * (1+8/N)^(-N/4).

## 5. Relation to prior work and precise novelty scope

Hong--Kwon--Yoon, "Global existence versus finite time blowup dichotomy for the system of nonlinear Schrödinger equations", arXiv:1712.06811 (2017; later journal publication), explicitly preserve all pairwise component overlaps, formulate the density-matrix evolution and conserved operator norm, and prove a global/blowup result for the orthogonal three-dimensional cubic system. Their Section 1, Theorem 1.1, and Proposition 7.3 give the relevant existing framework; Theorem 1.2 on kinetic-energy optimizers excludes its exponent endpoints. The same paper attributes the direct kinetic-energy argument to Rumin and the broader inequality to Lieb--Thirring.

Primary source checked in this round: https://arxiv.org/pdf/1712.06811 .

Thus conservation of Gamma, the largest-occupation viewpoint, and the layer-cake kinetic bound are established ideas, not independent priority claims. The project-derived addition is the fixed-state strict improvement (2.1), with the sharp scalar critical mass retained and a dimension-independent linear correction in 1-mu/M, obtained from round 11 quantitative polarization. Its dynamical consequences include an explicit open mass range above Mc for every genuinely nonpolarized internal state and exact scalar reduction of all critical-mass unbounded orbits. These follow directly once the round 11 theorem and the conservative flow assumptions are in place. Exhaustive priority verification of this precise quantitative formulation has not been completed.
