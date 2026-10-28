# Proof details: round 10 inertia geometry

## 1. Arbitrary-speed full-Hessian index at least three: verified

Use the real action S(U)=E(U)+ωM(U)/2−v·P(U)/2 and assume a real-even elliptic homogeneous symbol of degree m>1. For an exact profile, define the complex-selfadjoint frozen operator
$$
 K=a(D)+\omega+i v\cdot\nabla-|U|^\alpha,
 \quad KU=0,
 \quad\alpha=2m/N.
$$
Complex conjugation gives K bar U=2i v·∇bar U, and self-adjointness gives
$$
 \langle U,K\bar U\rangle=0,\qquad
 \langle\bar U,K\bar U\rangle=2v\cdot P(U).
$$
If E<0, the exact homogeneous profile identity yields v·P=2mE<0. Then U and bar U are complex linearly independent, since dependence would imply constant phase and P=0. Hence
$$
 V=\{tU+z\bar U:t\in\mathbb R,z\in\mathbb C\}
$$
is a three-dimensional real subspace. The full real Hessian L=S''(U) obeys
$$
 Q_L(\eta)=\operatorname{Re}\langle\eta,K\eta\rangle
 -\alpha\int |U|^{\alpha-2}[\operatorname{Re}(\bar U\eta)]^2.
$$
For η=tU+z bar U, its first term is exactly 2(v·P)|z|². If z≠0 this is strictly negative. If z=0 and t≠0, the second term equals −αt²||U||_{α+2}^{α+2}<0. Thus Q_L is strictly negative on V\{0}, proving n_-(L)≥3.

The quadratic expression remains meaningful for α<2: set its integrand to zero where U=0, and use [Re(bar Uη)]²≤|U|²|η|². No derivative singularity is introduced.

**Scope caveat:** without ω>sup_ξ(v·ξ−a(ξ)), the essential spectrum may intersect the negative axis. The variational Morse index conclusion remains correct (and the index may be infinite), but one must not automatically describe the result as the existence of three discrete negative eigenvalues.

## 2. A stronger standing-wave index from the number of negative inertia directions

Let Q be a nonzero real standing profile, L_-=a(D)+ω−|Q|^α, and assume the projected inverse defining
$$
 T_{ij}=\langle\partial_iQ,L_-^{-1}\partial_jQ\rangle
$$
exists. If this symmetric inertia matrix has k negative eigenvalues, let V_- be the k-dimensional span of responses L_-^{-1}(ζ·∇Q) for ζ in its negative eigenspace. Its restricted L_- quadratic form is exactly ζ^T Tζ<0. The response map is injective on that space. Thus n_-(L_-)≥k.

For L_+=L_-−α|Q|^α, adjoining Q gives a (k+1)-dimensional negative subspace. Indeed Q∈ker L_-, Q is independent from V_-, and
$$
 \langle tQ+b,L_+(tQ+b)\rangle
 =\langle b,L_-b\rangle
 -\alpha\int |Q|^\alpha(tQ+b)^2<0
$$
for every nonzero tQ+b with b∈V_-. The first term is strictly negative when b≠0, and the second term is strictly negative when b=0,t≠0. Therefore
$$
 n_-(S''(Q))=n_-(L_+)+n_-(L_-)\ge2k+1.
$$
These finite-dimensional negative subspaces persist under sufficiently small form-continuous perturbations of the profile and parameters. For an isotropic radial profile with T=I Id and I<0, this yields n_-(S''(Q))≥2N+1, and the same lower bound holds on continuous sufficiently small-speed branches. This strengthens the universal index-three statement in this branch regime.

## 3. Scaling-Hessian identities independently derived

For a differentiable mass-critical profile branch with on-shell action d(ω,v), the natural scaling is
$$
 d(\lambda^m\omega,\lambda^{m-1}v)=\lambda^m d(\omega,v).
$$
Consequently
$$
 \omega d_\omega+\frac{m-1}{m}v\cdot d_v=d,
 \quad d_\omega=M/2,\quad d_v=-P/2.
$$
Put q=(ω,(m−1)v/m). Differentiation gives
$$
 d''q=(0,-P/(2m)),\qquad
 q^T d''q=-\frac{m-1}{m}E.
$$
Thus negative-energy profiles supply a positive direction of the charge/action Hessian, whenever a differentiable on-shell branch exists. This is a branch conclusion, not an assertion that every profile lies on a smooth multiparameter branch.

For an isotropic branch near v=0 with inverse-phase scalar I, write b=(2−m)/m. The action expansion is
$$
 d(\omega,v)=d_0\omega-\frac I2\omega^b|v|^2+o(|v|^2)
$$
with the derivative control needed to differentiate the remainder. The leading velocity block is −Iω^b Id, and the ω-Schur complement is
$$
 \frac{I(2-m)}{m^2}\omega^{b-2}|v|^2+o(|v|^2).
$$
Hence for I<0 and m>2, the charge Hessian is positive definite for sufficiently small nonzero v, provided the expansion is genuinely C² to the indicated order. For 1<m<2 the leading Schur complement is negative; for m=2 this leading term vanishes and higher order information is required.

Regularity warning: a scalar o(|v|²) expansion alone does not justify taking two parameter derivatives. The manuscript must obtain a differentiable expansion from its implicit-function argument or state the corresponding derivative remainder assumptions.

## 4. derivation of the complete submitted inertia section

Read research/round10_inertia_section.tex after its creation. The exact bordered formula is correct with D=(mω,(m−1)v):
$$
 H D=(0,-P/2)^T,\quad
 R^T H R=-\tfrac12\begin{pmatrix}(m-1)vP&P^T\\P&B\end{pmatrix},
 \quad R=\begin{pmatrix}mω&0\$m-1)v&I\end{pmatrix}.
$$
For ω≠0 and invertible B, its frequency Schur complement is indeed κ/(2m²ω²), with κ=P^TB^{-1}P−(m−1)vP. Thus p(H)=n_-(B)+1_{κ>0}. No sign correction needed.

The response-refined estimate n_-(L)≥3+n_-(B|P⊥) is also valid. Differentiating the profile equation gives Lwζ=−iζ·∇U and q_L(wζ)=ζ^TBζ/2. Pairings with bar U and i bar U vanish because ∫U∂jU=0; the pairing with U is ζ·P, so it vanishes on P⊥. The negative response subspace is form-orthogonal to the explicit three-dimensional negative subspace and has zero intersection with it. For a rotational family with P=p(c)v/c and p(c)<0, the transverse block has N−1 negative directions, yielding n_-(L)≥N+2. Its constrained-minimizer exclusion follows by intersecting with the mass/momentum tangent space of codimension N+1.

The manuscript's C¹ profile/charge assumptions give P=2Tv+o(v) and B=2T+o(1) directly. Consequently its κ expansion is justified without differentiating an uncontrolled scalar remainder. Its mass expansion coefficient (m−2)/m and energy coefficient 1/m are both correct.

One typographic error was reported: `\overline U^{,2}` in the three-plane formula should have a spacing command rather than a literal comma. No substantive mathematical error was found in the checked statements. The Hamiltonian spectral-index application remains conditional on the explicitly listed operator and nondegeneracy assumptions; this audit does not replace verification of those assumptions on any particular numerical branch.
