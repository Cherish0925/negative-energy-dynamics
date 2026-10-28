Completion note: the radial quartet discussed historically below is now certified; see round5_radial_quartet.md and its proof details. The gluing proof remains independent of this certification.

# A finite-rank almost-conserved energy: independent analytic derivation

7 October 2026. This note changes the role of the unresolved radial quartet. The quartet is still relevant to the exact unstable dimension, but it need not be a prerequisite for the zero-momentum two-wave construction. The result below follows from the complete triangular decomposition in Lin–Zeng, Theorem 2.1; it does not require the stronger spectral-coercive splitting (SC) used in round 4.

## 1. Abstract lemma

Let X be a real Hilbert energy space and A=JL a Hamiltonian generator satisfying the hypotheses of Lin–Zeng, Theorems 2.1–2.2. Suppose ker L is finite dimensional. Write the invariant trichotomy as

    X = E^u ⊕ E^c ⊕ E^s.

For every ε>0 there is a bounded symmetric quadratic form Hε with the following properties:

1. Hε is strictly positive and coercive on all of X.
2. Hε−L has finite rank at most dim ker L+2 n⁻(L).
3. For x in E^c∩D(A),

       |Hε(Ax,x)+Hε(x,Ax)| ≤ ε Hε(x,x).

4. If the finite-coordinate functionals of the Lin–Zeng decomposition have smooth representing functions, Hε−L can be approximated by a finite-rank form whose representing functions are smooth and compactly supported, while preserving positivity and replacing ε by 2ε.

The constants of coercivity and equivalence may depend strongly on ε. No uniformity as ε tends to zero is asserted or needed.

### Proof of the metric statement

Use the precise decomposition X=⊕_{j=0}^6 X_j of Lin–Zeng Theorem 2.1, where X0=ker L, X5,6 are the hyperbolic spaces, and X0,1,2,4,5,6 are finite dimensional. The center generator has the upper triangular block form

    x0' = A01 x1+A02 x2+A03 x3+A04 x4,
    x1' = A1 x1+A12 x2+A13 x3+A14 x4,
    x2' = A2 x2+A24 x4,
    x3' = A3 x3+A34 x4,
    x4' = A4 x4.

Every off-diagonal block is bounded. L has center blocks L2<0, L3>0 and the nondegenerate pairing B14 between X1 and X4. In particular A2 is skew-adjoint for the norm −L2, and A3 is skew-adjoint for L3. The spectra of A1 and A4 lie on the imaginary axis.

For a finite-dimensional real matrix F with imaginary spectrum and any θ>0, there is a positive inner product G satisfying

    |G(Fa,a)+G(a,Fa)| ≤ θ G(a,a).

To see this directly, put F into real Jordan form. Its diagonal blocks are zero scalars or rotation blocks, and hence skew for Euclidean inner products. A diagonal rescaling of each Jordan chain makes the nilpotent off-diagonal entries arbitrarily small. Transport the resulting inner product back. This proof also handles non-semisimple imaginary eigenvalues.

Choose such inner products G1,G4 with θ≪ε, and set

    Hc(x,x)=w0 |x0|²+w1 G1(x1,x1)
             −L2(x2,x2)+L3(x3,x3)+w4 G4(x4,x4).

Choose the weights in the order w4≫1, then w1≪1, then w0≪w1. Indeed an off-diagonal arrow j→i contributes, in weighted coordinates, a norm bounded by a fixed constant times sqrt(wi/wj), taking w2=w3=1. The arrows are precisely

    4→3, 4→2, 4→1, 4→0,
    3→1, 3→0,
    2→1, 2→0,
    1→0.

Every ratio can be made as small as desired by the indicated choices. There are finitely many arrows, so the sum of their quadratic cross terms is at most ε Hc after reserving part of ε for the diagonal blocks. This proves the absolute differential estimate.

Complete Hc by any positive inner products on X5 and X6. The result is coercive on X because the direct-sum projections are bounded and L3 is coercive on X3. The coefficient of L3 has remained exactly one. Therefore Hε−L involves only finite-coordinate forms, so is finite rank. If d_j=dim X_j,

    rank(Hε−L) ≤ d0+2d1+d2+2d5
                 = d0+2n⁻(L)−d2
                 ≤ d0+2n⁻(L).

No assertion of exact invariance of the finite center blocks, their spectral isolation, or their exponential spatial localization was used. In particular the upper-triangular couplings A03 and A13 have not been discarded.

## 2. Why the finite-coordinate functionals are smooth for the BNLS operator

Here X=H²(R⁴), with Z-inner product induced by A0=Δ²+1, and

    A=J L,   L=Δ²+1+i v·∇−2|Uv|²−Uv² conjugation.

All profile derivatives are bounded and the profile is smooth. Elliptic regularity gives D(A^k)=H^{4k+2}. Theorem 2.1 explicitly places each finite block X_j, j≠3, in the intersection of these graph domains. Its basis vectors are therefore in every H^s.

The finite-coordinate maps are also represented by smooth functions. For X1 and X4, use pairings of Lh with the basis vectors of the other block and the inverse of B14. For X2 use the inverse finite Gram matrix of L2, and for the hyperbolic blocks use B56. Each representing function is L applied to a smooth vector, hence is smooth and square-integrable with all derivatives. The X0 coordinate is recovered by the exact formula P0 h=Orth_{ker L}^Z(h−P5 h−P6 h). The other center blocks are Z-orthogonal to ker L by item 8 of Theorem 2.1; that item does not assert the same orthogonality for X5 and X6. A Z-inner-product functional with a smooth kernel vector has L² representative A0 times that vector, which is again smooth.

Consequently K=Hε−L can be written as

    K(h,h)=Σ_{a,b=1}^m k_ab <f_a,h>_{L²,R}<f_b,h>_{L²,R},

where k_ab is a real symmetric matrix and every f_a lies in all H^s. No spatial exponential decay of the finite center vectors is required.

## 3. Compact localization controls the commutator, not just the norm

Let χ_R be a standard smooth spatial cutoff and f_{a,R}=χ_R f_a. Define K_R using the same matrix k_ab. Then f_{a,R}→f_a in H², hence also in H⁻². The differential operator A* is continuous from H² to H⁻². Thus

    A* f_{a,R} → A* f_a  in H⁻².

For h in the generator domain,

    2 K_R(Ah,h)
       =2 Σ k_ab <A* f_{a,R},h><f_{b,R},h>.

It follows that K_R→K and A*K_R+K_RA→A*K+KA as bounded quadratic forms on H². This is the relevant graph-dual approximation. Mere L² convergence of the mode functions would not by itself justify the commutator conclusion.

Choose R after ε and the coercivity constant of Hε are fixed. Make both errors sufficiently small compared with ε times that coercivity constant. Then Hε,R=L+K_R stays coercive and has an arbitrarily small relative symmetric derivative on E^c. The harmless factor two in the lemma can instead be absorbed by starting with ε/2.

This proves the compactly supported finite-rank version needed for moving waves. The support radius may be very large but is finite.

## 4. Extension away from the exact center constraints

Let P_h be the finite-dimensional hyperbolic projection and P_c=I−P_h. The derivative estimate is initially on P_cX. For x=P_cx+P_hx, boundedness of the finite-rank derivative form and Young's inequality imply

    |(Hε,R A+A* Hε,R)(x,x)|
       ≤ C ε Hε,R(x,x)+Cε |P_h x|²,

where C is an absolute harmless factor and Cε is allowed to depend on the chosen metric. One can, for example, reserve one additional ε for the cross term. The coordinate term is squared; no uncontrolled linear error in the full energy norm is needed.

This extension is essential in a partition-of-unity argument, since cutting off a center vector makes its hyperbolic coordinates only approximately zero.

## 5. Derivation of the two-core localization step

For two outgoing cores at ±vt, translate compact corrections K_± together with their cores. For t sufficiently large, choose a smooth partition

    χ_+²+χ_-²+χ_0²=1

such that χ_± equals one on the full support of the corresponding correction kernel and vanishes near the other core. The localization identity for each correction is then exact:

    K_±(χ_±h,χ_±h)=K_±(h,h).

The sum of the two single-core corrected actions and the exterior free action therefore differs from the patched corrected action only by the usual fourth-order IMS error and exponentially small other-core potentials. After coercivity,

    Σ local corrected energies ≤ (1+Cε/t) patched energy.

The leading coefficient is one. Thus a possibly poor condition number of Hε does not multiply the small exponential rate ε by a fixed large constant. It appears only in Cε/t, which produces a polynomial prefactor in the propagator bound.

Only the hyperbolic modes are projected out in the moving construction. They lie off the free imaginary spectrum and have exponentially localized primal and dual functions. For a vector satisfying both raw hyperbolic constraints, the hyperbolic coordinates of χ_±h are exponentially small, since the relevant cutoffs are one near their cores. The constraint-error term in Section 4 is therefore exponentially bounded and can be absorbed in the action inequality.

Translations of K_± cancel the velocity term when differentiating, so each correction is paired with its own co-moving single-wave generator. Terms involving the other core are exponentially small because the correction has compact support. This confirms that the patched inequality has the form

    |Q'(t)| ≤ (c ε+Cε/t) Q(t)

for the projected center flow, after the already established exponentially small finite-rank intertwining correction is included.

Hence both forward and backward center propagators satisfy

    ||S_c(t,s)||_{H²→H²}
       ≤ Cε exp(cε |t−s|) max(t/s,s/t)^{Cε}.

The H6 graph-norm argument from round4_gluing_audit.md adds only a polynomial in |t−s|. It does not force a new fixed positive exponential rate, because the exponential factors multiply exactly along the Duhamel interval.

## 6. Consequence for the missing radial quartet

The center Green integral against an interaction forcing O(e^{-κt}) converges whenever its chosen terminal weight η satisfies

    cε < η < min(κ, α),

where α is the least positive hyperbolic rate. Since ε is arbitrary, such a choice is possible for every fixed nonzero relative velocity and hence every κ>0. Large constants only enlarge the starting time/separation.

Thus the radial quartet is not logically required to obtain the slow-velocity two-wave construction if the rest of the projected fixed-point proof is carried out with this modified energy. In particular neither a localized invariant finite-dimensional center block nor exact exhaustion of the negative index by hyperbolic modes is required.

This note establishes and checks the replacement lemma and its localization mechanism. The actual two-wave theorem must still combine these statements with the moving-projection identities, graph-domain estimates, nonlinear contraction, and symmetry argument; these are treated in the companion gluing note. The statement here is not an independent claim that the old SC hypothesis was already automatic.

## 7. A quantitative finite-dimensional quartet certification theorem

This is a separate route to determining whether the unstable dimension is 29 or 31. It remains useful even if that distinction is no longer needed for gluing.

Quotient the radial phase kernel using its Z-orthogonal projection. The induced generator Ahat is skew with respect to the nondegenerate Hessian form H=Lhat, whose negative index is three. Let

    ||H||≤M,     ||H⁻¹||≤1/m.

Here H denotes the bounded form operator in the quotient Z inner product. Choose an injective map W:R^d→D(Ahat) and a real matrix B0, and rigorously verify

    G=W* H W is invertible,   n⁻(G)=3,
    ||W||≤w,   ||G⁻¹||≤g,
    ||Ahat W−W B0||≤ε.

All finite-dimensional norms below are Euclidean operator norms and infinite-dimensional norms are Z norms, unless energy is explicitly specified. Put

    q=1+w² g M.

Let Γ be a simple closed contour contained in Re λ>0 and set

    α=inf_{λ∈Γ} Re λ>0,
    k=sup_{λ∈Γ}||(B0−λ)⁻¹||.

If

    k [g w M ε + g M q² ε²/α] < 1,                 (7.1)

then Ahat and B0 have the same total algebraic eigenvalue count inside Γ. Thus a contour around a simple first-quadrant eigenvalue of B0 gives an actual nonreal unstable eigenvalue of the full continuum operator. Real coefficients give its conjugate and hence two real unstable dimensions.

### Complete proof

Let F=Ran W and C=F^{⊥_H}. The H-orthogonal projection onto F is

    PE=W G⁻¹ W* H,

so ||PC||=||I−PE||≤q. The Hessian form is block diagonal on F⊕C. Since F exhausts all three negative directions, H is nonnegative on C. It has no compressed kernel: if h∈C pairs to zero under H with every vector of C, it also pairs to zero with F by definition, so Hh=0 and h=0.

In fact its coercivity is explicitly

    H(h,h)≥(m/q)||h||²,     h∈C.                 (7.2)

For a bounded functional f on C, extend it to X by f PC and set u=H⁻¹ PC* f. Then u∈C because Hu vanishes on F. It solves the compressed equation and satisfies ||u||≤(q/m)||f||. The positive compressed operator therefore has inverse norm at most q/m, proving (7.2).

Write R=Ahat W−W B0. In the coordinates W a+h, h∈C, the generator is

    Ahat = [[B, Cfc],[Dcf, Ac]],
    B=G⁻¹ W* H Ahat W,
    Dcf=PC Ahat W=PC R.

The exact compressed B satisfies

    ||B−B0||≤g w M ε.

The H-skew identity gives

    G Cfc=−Dcf* Hc.

Consequently, with the energy norm ||h||c²=H(h,h),

    ||Dcf||_{Euclidean→energy}≤sqrt(M) q ε,
    ||Cfc||_{energy→Euclidean}≤g sqrt(M) q ε.

The compressed Ac generates a unitary group in this energy norm. Here the generator assertion is not an additional premise. The off-diagonal operators are bounded in the Z topology: PE Ahat extends boundedly because

    W* H Ahat=−(Ahat W)* H,

and Ahat PE is bounded since the columns of W lie in D(Ahat). Therefore the block-diagonal operator B⊕Ac is a bounded perturbation of the known group generator Ahat. Its invariant C block generates a group; conservation of the positive Hc form makes that group unitary. It follows that

    ||(Ac−λ)⁻¹||_{energy}≤1/Re λ.

The exact Schur complement is

    B−λ−Cfc(Ac−λ)⁻¹ Dcf.

Its difference from B0−λ is bounded on Γ by the bracket in (7.1). Thus the product with (B0−λ)⁻¹ has norm strictly below one. The finite-dimensional analytic Rouché homotopy from this Schur complement to B0−λ stays invertible on Γ. The complementary Ac block has no right-half-plane spectrum. The Schur factorization therefore identifies algebraic multiplicities with those of the full operator and proves the count claim.

If the exact compressed matrix B itself is enclosed and used as the finite reference, the first, linear term in (7.1) disappears: only the quadratic residual term remains. No approximation of the infinite positive complement is required.

### Kernel quotient and the critical chain

The quotient does not require prior certification of γ. If e=(0,Q) spans the phase kernel, Π is its Z-orthogonal projection complement, and A e=0, then A induces Ahat=Π A|Ran Π. The Hessian form is unchanged by adding e and is nondegenerate on the quotient. The original group descends to the quotient, so Ahat is a group generator. A residual identity

    A V−V B0=e c+R

becomes

    Ahat(ΠV)−(ΠV)B0=ΠR.

The phase component is removed exactly and does not enter ε. This is useful for the length-four critical zero chain: after quotienting it is a length-three chain, to be included together with the four real quartet directions.

The numerical seven-dimensional candidate has relative Hessian Gram eigenvalues

    −1.0060976, −0.3696425, −0.2699810,
     0.3427584,  0.8604296,  0.8713405, 0.9489307.

These values are diagnostic only. They suggest a well-conditioned finite block for the precise inequality (7.1), rather than serving as any exact inertia or continuum eigenvalue certificate.

## Sources and attribution

The structural input is Lin–Zeng, *Instability, index theorem, and exponential trichotomy for linear Hamiltonian PDEs*, Memoirs AMS 275 (2022), no. 1347; arXiv:1703.04016v4, Theorem 2.1 and Theorem 2.2. The finite-rank metric is a direct constructive deduction from its exact triangular form. No novelty-priority claim for this abstract deduction is made here. Its application to the moving two-core BNLS problem is the present research step.
