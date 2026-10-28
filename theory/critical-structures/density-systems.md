# polarization rigidity and dimension-independent critical gaps

Status: complete analytic arguments below, with the compactness and symmetry steps independently checked by `/root/r11_independent_challenge`. These are single-common-frequency profile theorems, not a classification of arbitrary vector dynamics or matrix-frequency relative equilibria. Priority of the new combination is not established by the limited literature search.

## 1. Precise setting and results

Let H be any nonzero separable complex Hilbert space, including C^d for arbitrary finite d or ell^2. Let N>=1, m>1, s=m/2, and let a be a real-even positive elliptic m-homogeneous Fourier symbol with the smoothness assumptions of round 10. Set

    M(U) = integral ||U(x)||_H^2 dx,
    A(U) = integral a(xi) ||Uhat(xi)||_H^2 dxi,
    rho_U = ||U||_H^2.

We cover either of two attractions:

* Local critical power: kappa=1+m/N, F(U)=integral rho_U^kappa, V_rho=rho^(kappa-1).
* Critical positive-type Hartree: 1<m<N, kappa=2, F(U)=D(rho_U,rho_U), V_rho=K*rho. K is the even homogeneous degree -m kernel of round 10: |K|+|x||grad K|<=C|x|^-m, and its interaction norm is positive definite. Pointwise positivity is not required.

The scalar sharp constant defines Mc by

    F(u) <= kappa (M(u)/Mc)^(kappa-1) A(u).

Let b be any scalar real-even nonnegative symbol satisfying the round 10 order-m derivative bounds and xi.grad b <= m b. The same scalar a+b acts on every internal component. Write

    E_b(U) = (A(U)+B_b(U))/2 - F(U)/(2 kappa).

A common-frequency traveling profile is a nonzero U in H^s(R^N;H) satisfying

    [a(D)+b(D)+omega+i v.grad] U - V_{rho_U} U = 0.       (1)

### Theorem A: all dimensions have the same critical optimizer

The vector inequality has the same sharp Mc, for every H. Every optimizer is completely polarized:

    U(x) = zeta Q(x),       ||zeta||_H=1,

where Q is a scalar optimizer, real after a constant scalar phase. Moreover, for any varying internal dimensions H_n, every sequence with M(U_n)->Mc, A(U_n)->1 and F(U_n)->kappa is strongly compact in H^s after spatial translations and internal unitary transformations (embed H_n isometrically in ell^2). Every limit is zeta Q.

### Theorem B: dimension-independent nonpositive-energy rigidity

There is delta>0 depending only on N,m,a and the scalar attraction, independent of H, b, omega and v, such that a profile (1) with

    M(U) < Mc+delta,       E_b(U) <= 0

must satisfy

    E_b(U)=0,   v=0,   D_b(U)=0,   U=zeta q,

where D_b(U)=integral [m b-xi.grad b]||Uhat||^2 and q is a real scalar stationary profile for the same a+b and omega. Necessarily M(U)>=Mc. In particular every negative-energy profile, in any finite or countably infinite internal dimension, has mass at least Mc+delta.

If m b-xi.grad b is strictly positive almost everywhere away from zero, there are no nonzero nonpositive-energy profiles in this mass window.

### Theorem C: exact polarization of nearly critical traveling waves

For b=0, there exists eta>0, independent of H, such that every profile (1) satisfying

    |M(U)/Mc-1| + |E_0(U)|/A(U) < eta

is exactly polarized U=zeta q, with q a scalar traveling profile. The energy can be positive here. Thus genuinely different spatial profiles in different internal components cannot bifurcate into this normalized near-critical common-frequency sector.

These assertions do not require scalar optimizer uniqueness, positivity, radial symmetry, or nondegeneracy of the scalar real-sector linearization.

## 2. Lifting the sharp inequality and identifying equality

For any orthonormal internal basis write U=(u_j). The density norm triangle inequality followed by scalar sharp interpolation and sequence Holder gives

    F(U)^(1/kappa)
      <= sum_j F(u_j)^(1/kappa)
      <= kappa^(1/kappa) Mc^(-(kappa-1)/kappa)
         sum_j A(u_j)^(1/kappa) M(u_j)^((kappa-1)/kappa)
      <= kappa^(1/kappa) Mc^(-(kappa-1)/kappa)
         A(U)^(1/kappa) M(U)^((kappa-1)/kappa).

For infinitely many components, apply this first to finite partial sums. The tails converge in the density norm because the same bound for the tail tends to zero. A one-component scalar optimizer proves sharpness.

For equality, split each u_j into its real and imaginary scalar components f_l. Every nonzero component is a scalar optimizer; strict convexity forces all f_l^2 to be proportional; Holder forces the kinetic-to-mass ratios to agree. It remains to rule out spatially changing signs between components. Apply a real orthogonal rotation to any pair f_i,f_j. The rotated vector is also an optimizer, so its two rotated squared components must again be proportional. If f_j/f_i took both signs of one nonzero constant on sets of positive measure, the squared sum and difference would fail proportionality (and when the magnitude is one, their nonzero supports are disjoint). Therefore f_j is a single constant multiple of f_i. This proves U=zeta Q. Zero components are harmless, and the pairwise argument covers countably many components.

## 3. A compactness lemma removing internal dimension

The important point is that ordinary local Rellich compactness fails directly for Hilbert-valued functions: a fixed spatial profile may move through mutually orthogonal internal directions. A single internal unitary removes precisely this failure.

**Lemma.** Let X=H^s(R^N;C), s>0. Every bounded sequence U_n in X tensor ell^2 has a subsequence and internal unitaries W_n on ell^2 for which W_n U_n converges weakly in X tensor ell^2 and strongly in L^2_loc(R^N;ell^2).

**Proof.** Fix an orthonormal basis (phi_k) of the scalar Hilbert space X, and write c_nk=<phi_k,U_n>_X in ell^2. For each n, Gram-Schmidt the first n vectors c_n1,...,c_nn and extend the finite orthonormal list to an orthonormal basis of ell^2. Choose W_n such that

    W_n c_nk in span{e_1,...,e_k},      k<=n.

Finite truncation to the first n coefficient vectors makes extension to a genuine unitary automatic. For each fixed k the transformed coefficient sequence is bounded in a fixed finite-dimensional space; diagonal extraction makes every coefficient converge strongly in ell^2. The transformed U_n also have a weakly convergent subsequence in X tensor ell^2, with those coefficient limits.

For a compactly supported smooth chi, the scalar map K_chi:X->L^2, f->chi f, is compact. If P_L is scalar projection onto phi_1,...,phi_L, then

    ||K_chi(I-P_L)||_{X->L^2} -> 0.

The norm is unchanged by tensoring with the identity on ell^2. The transformed P_L U_n converge strongly since there are only L convergent internal coefficients. Their tails after K_chi are uniformly small. Therefore chi W_n U_n converges strongly in L^2(ell^2). Exhaust spatial compact sets. QED.

The construction applies to varying finite-dimensional H_n by isometric inclusion in ell^2; all physical quadratic forms and total densities are preserved by the embedding and W_n.

## 4. Near-optimizer compactness

First rule out local vanishing of mass by the usual localized Sobolev estimate, with dimension-independent constants. These estimates hold for Hilbert-valued functions: Bessel-potential convolution followed by the norm triangle inequality proves Sobolev embedding, and scalar spatial localization followed by summing internal quadratic norms proves the localized version. For any 2<p<2_s^* (with 2_s^*=infinity when 2s>=N), boundedness in H^s and

    sup_y integral_{B_1(y)} ||U_n||^2 -> 0

imply ||U_n||_{L^p(H)}->0. This contradicts F(U_n)->kappa: use p=2kappa in the local case, and p=4N/(2N-m) plus HLS in the Hartree case. Both exponents are strictly inside the Sobolev range.

Translate to make local mass nonzero, and apply the internal-unitary compactness lemma. Write U_n -> U weakly in H^s and strongly locally in L^2(H), with U nonzero; interpolation gives local strong convergence in the attraction exponent. Put R_n=U_n-U. Hilbert quadratic splitting gives M_n=M(U)+M(R_n)+o(1), A_n=A(U)+A(R_n)+o(1).

For the local power, the ordinary Brezis-Lieb proof applies to the Hilbert norm after a.e. strong internal convergence:

    integral ||U_n||^(2kappa)
      = integral ||U||^(2kappa)+integral ||R_n||^(2kappa)+o(1).

For Hartree, rho_{U_n}=rho_U+rho_{R_n}+2 Re<U,R_n>. The last term tends to zero in L^{q/2}, q=4N/(2N-m), by local convergence and the small L^q tail of U. Also D(rho_U,rho_{R_n})->0: approximate rho_U by the squared norm of a compactly supported smooth finite-dimensional vector field in L^{q/2}; its potential is bounded and decays at infinity, while R_n tends to zero locally in L^2(H). HLS controls the approximation error. Hence F splits in this case too.

Let M_1>0,M_2 and A_1,A_2 be the limiting mass and kinetic contributions. Sharp vector interpolation gives

    kappa <= kappa Mc^(-(kappa-1))
               [M_1^(kappa-1) A_1 + M_2^(kappa-1) A_2],

where M_1+M_2=Mc and A_1+A_2=1. If both masses were positive, the right side would be strictly less than kappa. Therefore M_2=0, and the equality then forces A_2=0. This proves strong H^s convergence to an optimizer, which Section 2 identifies as zeta Q. The argument is uniform in the internal dimension.

## 5. The exact internal kernel

Normalize scalar Q by M(Q)=Mc, A(Q)=1. The scalar phase operator

    L_Q = a(D)+(kappa-1)/Mc - V_{Q^2}

is nonnegative, has real kernel R Q and is coercive on the real L^2-orthogonal complement of Q, by the round 10 density-convexity lemma and compactness of the potential. The same coercivity holds on complex Q-perp by summing real and imaginary parts, with a constant independent of the internal dimension.

At U=Q e_1, write a perturbation as H=(h+ik)e_1+Z with Z perpendicular to e_1 pointwise. The second variation of E+omega_*M/2 is

    <h,L_+h> + <k,L_Q k>
      + sum_{j>=2} [<Re Z_j,L_Q Re Z_j>+<Im Z_j,L_Q Im Z_j>].

Consequently its kernel in the phase and internal transverse sector is exactly

    { Q eta : eta in H, Re<eta,e_1>=0 }.

For finite dimension d, this has real dimension 2d-1 and is exactly the tangent space to the unitary orbit of Q e_1. Any additional kernel of the full Hessian is entirely in the scalar real sector L_+, which is not assumed nondegenerate. There is no false assertion that the full vector phase kernel is one-dimensional.

## 6. Weak profile identities

Weak profiles admit the same regularity bootstrap as round 10, now with Hilbert norms and common scalar Fourier multipliers: U belongs to L^infinity(R^N;H) intersect H^{m+1}(R^N;H). The multiplier estimates on Hilbert-valued L^p follow from the vector-valued Mihlin theorem (Hilbert spaces are UMD); constants in the needed common-symbol estimates do not depend on finite internal dimension. Alternatively all cutoff identities can be obtained by finite internal projection and passage to the limit, after scalar-potential bootstrap. No spatial moment is assumed.

All energies and fluxes are sums over internal components. Let

    P(U)= integral xi ||Uhat(xi)||^2,
    D=D_b(U)= integral [mb-xi.grad b]||Uhat||^2 >= 0.

Cutoff dilation and testing by U give

    v.P = 2m E - D,
    omega M = (kappa-1)(A+B)+(2m-2kappa)E-D.       (2)

Choose an internal orthonormal basis and write U=X+iY with real coefficient functions. Since the common a+b is real and V_rho is real, the imaginary equation yields

    <Y,[a+b+omega-V_rho]Y> = v.P/2.

With omega_tilde=omega+D/M this is

    m E = <Y,[a+omega_tilde-V_rho]Y> + B(Y)
             + D[1/2-M(Y)/M],                       (3)

and

    omega_tilde M=(kappa-1)(A+B)+(2m-2kappa)E.       (4)

These formulas are basis-independent as complete identities, although individual X,Y depend on the chosen internal unitary.

## 7. Proof of Theorem B

Suppose a sequence of counterexamples to the rigidity conclusion exists with M_n->Mc from above or at Mc. The critical scaling preserves the b cone, so normalize A_n=1. Sharp GN and E_n<=0 imply

    0<=B_n <= (M_n/Mc)^(kappa-1)-1 -> 0,
    E_n -> 0,       F(U_n)->kappa.

Apply Sections 3-4: after translations and internal unitaries, U_n->Q e_1 strongly in H^s. Align the internal coefficient vector

    z_n = integral Q(x) U_n(x) dx

with the positive real first internal coordinate. This can be done without losing convergence to Qe_1, since z_n->Mc e_1. Now every imaginary component Y_nj is orthogonal to Q, and ||Y_n||_{H^s}->0.

By (4), omega_tilde_n->(kappa-1)/Mc, independent of how large D_n may be. The local or Hartree potentials converge in form norm by Sobolev/Holder or HLS, respectively. Scalar phase coercivity, summed over all internal coordinates, gives

    <Y_n,[a+omega_tilde_n-V_{rho_n}]Y_n>
        >= c ||Y_n||_{H^s(H)}^2.

For large n, M(Y_n)/M_n<1/4. Every term on the right of (3) is nonnegative, and therefore E_n<=0 forces

    E_n=0,      Y_n=0,      D_n=0.

The imaginary equation then gives v_n.grad X_n=0. A nonzero L^2 function cannot be constant in a nonzero spatial direction (equivalently its Fourier support cannot lie in a measure-zero hyperplane), so v_n=0.

The real components satisfy

    T_n X_nj=0,       T_n=a+b_n+omega_n-V_{rho_n}.

Since D_n=0, omega_n=omega_tilde_n. The form T_n is strictly positive on Q-perp: its a+omega-V part is close to L_Q and b_n>=0. Its real kernel has dimension at most one; otherwise a nontrivial linear combination of two kernel vectors would be orthogonal to Q. Thus all X_nj are real constant multiples of one scalar q_n. This is the asserted polarization, contradicting that these were counterexamples. The sequential argument proves a uniform delta.

## 8. Proof of Theorem C

If the asserted eta failed, normalize a sequence of unpolarized profiles with A_n=1, M_n->Mc and E_n->0. Then F_n=kappa(A_n-2E_n)->kappa, so vector optimizer compactness yields U_n->Qe_1.

For pure homogeneous dispersion, the phase-boost identity is

    v_n M_n = integral grad a(xi) ||Uhat_n(xi)||^2 dxi.    (5)

It follows by testing the profile equation against i x_j chi(x/R) U and passing through the cutoff commutator; round 10 supplies the scalar argument and the component sum converges absolutely because grad a has order m-1<m. It does not require xU in L^2.

Strong H^s convergence makes the right side converge. Its limit is zero, because Q is real, |Qhat|^2 is even, and grad a is odd. Hence v_n->0. By (2) with b=0,

    omega_n M_n=(kappa-1)+(2m-2kappa)E_n,

so omega_n->omega_*=(kappa-1)/Mc. The complex self-adjoint frozen profile form

    T_n = a(D)+omega_n+i v_n.grad - V_{rho_n}

converges in H^s-to-H^-s form norm to L_Q. The order-one drift is form-small since m>1. Thus T_n is strictly positive on the complex codimension-one space Q-perp. Its complex kernel has dimension at most one. Every internal component of U_n lies in this kernel, so all are complex constant multiples of one scalar profile. This contradicts lack of polarization and proves the theorem.

## 9. What changes if internal symmetry is broken

The assumptions 'common scalar dispersion' and 'attraction depends only on total density' are structural. An arbitrary matrix-valued symbol is not automatically covered. A unitary used to remove internal phase modes can turn a real matrix symbol into a complex one, reintroducing mixed real-imaginary terms in (3). Positivity of the full matrix symbol alone does not prove the componentwise positivity used above.

Likewise, the U(H)-invariant evolution permits relative equilibria

    u(t,x)=exp(i t Omega) U(x-vt)

with a non-scalar Hermitian internal generator Omega. Then distinct components may occupy distinct spectral values of the same frozen spatial operator. The common-frequency argument proving one-dimensional range no longer applies. Theorems A-C do not settle these internally rotating states. This distinction is a concrete next mathematical problem, not a claim that every possible system has been unified.

## 10. Relation to prior work and scientific content

Sharp vector-valued Gagliardo-Nirenberg inequalities and coupled-system ground states are established subjects. Li Ma and Lin Zhao, 'Uniqueness of ground states of some coupled nonlinear Schrodinger systems and their application', arXiv:0708.0284, published JDE 245 (2008), 2551-2565, already derive sharp vector inequalities from coupled ground states. We do not claim vector sharp interpolation itself as new.

Cheng, Guo, Hwang and Yoon, arXiv:2202.10757, published JDE 433 (2025), treat finite and infinite coupled cubic focusing systems and scattering below their sharp threshold. Their coupling contains the component-dependent quartic correction 2(integral rho^2)-integral sum_j |u_j|^4; its infinite-component optimization can fail to have an optimizer. That model lacks the full internal unitary invariance used here and is not contradicted by complete polarization in Theorem A.

The concrete additional conclusions developed here are: (i) an elementary internal-unitary compactness argument that survives unbounded component number, (ii) exact common-frequency polarization rigidity near criticality for the general higher-order homogeneous and positive-type Hartree classes, and (iii) a negative-energy mass gap and zero-energy rigidity uniform simultaneously in internal dimension and the full scalar dispersion cone. A comprehensive novelty survey remains separate.

Primary sources:
- https://arxiv.org/abs/0708.0284 (tool ref )
- https://arxiv.org/abs/2202.10757 (tool ref ; abstract supports coupled/infinite-system scope)
- https://www.sciencedirect.com/science/article/abs/pii/S002203962500227X (tool ref ; indexed publisher text displays the non-U(d)-invariant energy and nonattainment distinction)

## 11. Additional theorem: quantitative polarization for arbitrary fields

Independently reviewed by r11_independent_challenge after the initial A-C review.
For every nonzero U and every internal dimension define

    d(U)=1-F(U)/[kappa (M(U)/Mc)^(kappa-1) A(U)],
    p(U)=inf_{||zeta||=1,q in H^s} { M(U-zeta q)/M(U)+A(U-zeta q)/A(U) }.

There is a uniform constant C, depending only on the fixed scalar dispersion and interaction, such that

    p(U) <= C d(U).

The scalar q is arbitrary, not asserted to be an optimizer. Thus this controls loss of internal polarization without requiring scalar uniqueness or real-sector nondegeneracy. It holds for fields at every time whenever they lie in the energy space, without any stationary equation.

Proof: normalize M=Mc,A=1. If no C existed, p<=2 implies a sequence with d->0 and d/p->0. Compactness after translations/internal unitaries gives U_n=(u_n,Z_n)->(Q,0). Align integral Q U_n to the positive first coordinate so each transverse component Z_nj is complex Q-orthogonal. Let ||Z||_X^2=M(Z)/Mc+A(Z). The common-density expansion is

    F(u,Z)=F(u)+kappa <V_|u|²,||Z||²>+o(||Z||_X²).

For local powers use (a+b)^kappa-a^kappa-kappa a^(kappa-1)b <= C b^kappa for 1<kappa<=2, and <=C(a^(kappa-2)b²+b^kappa) for kappa>2. Here a=|u|²,b=||Z||². Holder and vector Sobolev bound remainders by O(||Z||_X^(2kappa)) or O(||Z||_X^4+||Z||_X^(2kappa)), both little-o of ||Z||_X². Hartree's remainder is exactly F(Z)=O(||Z||_X^4).

Scalar GN on u gives F(u)<=kappa (1-M(Z)/Mc)^(kappa-1)(1-A(Z)). Expanding this and using potential form continuity yields

    kappa-F(U) >= kappa sum_j <Z_j,L_Q Z_j>-o(||Z||_X²)
                >= c ||Z||_X² >= c p(U).

This contradicts d/p->0. The two-parameter amplitude/spatial normalization preserves d and p, proving the global scale-invariant statement. The complete theorem and proof have been inserted in round11_systems_section.tex, label thm:r11-quantitativepolarization.
