# Proof details of the radial BNLS argument and symmetry extensions

Date: 2026-10-07. Research note; not a solution of the unrestricted nonradial conjecture. Novelty has not been established by an exhaustive literature comparison.

## 1. Source derivation

I read Leonard Dinh's 20-page paper, *Finite-Time Blow-Up of Radial Negative-Energy Solutions for the Mass-Critical Biharmonic Nonlinear Schrödinger Equation*, posted on Meta's research website on October 2, 2026:

https://ai.meta.com/research/publications/finite-time-blow-up-of-radial-negative-energy-solutions-for-the-mass-critical-biharmonic-nonlinear-schrodinger-equation/

The annular interpolation and its infinite-annulus summation check out, including N=2. The Hessian coercivity, lower-order interpolation, and fourth-power ODE closure are consistent. Radial symmetry enters only the nonlinear interpolation. No additional hidden radial step was found. The general-data interpolation proposed in the remark is not valid for arbitrary mass and arbitrary epsilon; a concentrated translated bump obstructs it. This does not refute the PDE conjecture.

For backward time, the correct transformation is conjugate time reversal, u_tilde(t,x)=conjugate(u(-t,x)); PDF text extraction may omit overbars.

## 2. Independently derived planar vortex extension

Consider

$$
i\partial_tu=\Delta^2u-|u|^4u \quad\text{on }\mathbb R^2,
\qquad E(u)=\tfrac12\|\Delta u\|_2^2-\tfrac16\|u\|_6^6.
$$

Fix an integer q. Suppose u_0 in H^2 obeys

$$
u_0(R_\theta x)=e^{iq\theta}u_0(x)
$$

for every planar rotation. Equivalently, away from the origin,
u_0(r,theta)=e^{iq theta}v_0(r). If E(u_0)<0, the maximal solution has finite forward and backward lifespan.

This includes nonradial complex fields whenever q is nonzero. It is still a symmetry-restricted theorem, not the unrestricted problem.

### The needed inequality

Put omega_R(x)=1-exp(-|x|^4/R^4), D_R(u)=integral omega_R |D^2u|_F^2, and m=||u||_2^2. For every epsilon>0,

$$
\int_{\mathbb R^2}\omega_R|u|^6
\le\epsilon D_R(u)+C_\epsilon R^{-4}(m^5+m^3).
\tag{V1}
$$

The constant can be chosen independently of q.

To prove this, let rho>0 and U(s)=rho v(rho s) for s in (1/2,4). Define

$$
\mu=\int_{1/2}^4|U|^2s\,ds,
\qquad Q=\int_{1/2}^4|U''|^2s\,ds.
$$

Since s is bounded above and below, interval interpolation gives
||U'||_2^2 <= C(Q+mu). Choose a smooth cutoff eta supported in (1/2,4), equal to one on [1,2]. The one-dimensional second-order Gagliardo--Nirenberg inequality yields

$$
\int_1^2 |U|^6s\,ds
\le C\|(\eta U)''\|_2\|\eta U\|_2^5
\le C Q^{1/2}\mu^{5/2}+C\mu^3.
\tag{V2}
$$

For the full field,

$$
e_r^TD^2u\,e_r=\partial_r^2u=e^{iq\theta}v''(r),
\qquad |v''(r)|^2\le |D^2u|_F^2.
\tag{V3}
$$

This pointwise inequality avoids trying to use the radial Hessian identity for a vortex, which would be incorrect.

Take rho_j=2^j R, A_j={rho_j<|x|<2rho_j}, A_j^*={rho_j/2<|x|<4rho_j}, d_j=min((rho_j/R)^4,1), alpha_j=d_j rho_j^{-4}. On A_j^*, omega_R is comparable to d_j. Scaling (V2), and using (V3), gives

$$
\int_{A_j}\omega_R|u|^6
\le C\alpha_j^{1/2}D_j^{1/2}\mu_j^{5/2}
 +C\alpha_j\mu_j^3,
$$

where D_j=integral over A_j^* of omega_R|D^2u|_F^2. Young's inequality gives

$$
\int_{A_j}\omega_R|u|^6
\le\delta D_j+C_\delta\alpha_j\mu_j^5+C\alpha_j\mu_j^3.
$$

Now alpha_j<=R^{-4}, the enlarged annuli have bounded overlap, sum_j D_j<=C D_R, and sum_j mu_j<=C m. Summing proves (V1). Smooth equivariant approximation follows by radial mollification and radial cutoff.

### PDE closure

The symmetry is preserved: for each theta, e^{-iq theta}u(t,R_theta x) solves the same Cauchy problem, so uniqueness applies. Negative energy and (V1), combined with the localized commutator identities below, yield finite forward time. Conjugation replaces q by -q; the same argument supplies finite backward time.

For any smooth negative-energy vortex seed, multiplying it by a sufficiently large positive constant produces a negative-energy datum. Thus the class is nonempty for every integer q. For example use (x_1+i x_2)^q exp(-|x|^2) for q>=0 and its conjugate for q<0.

## 3. Explicit commutator ledger, derived for arbitrary u

Set p=2+8/N, h=exp(-|x|^4/R^4), and choose a real phi_R with grad phi_R=xh. Define

$$
M_R=2\operatorname{Im}\int\bar u\,\nabla\phi_R\cdot\nabla u,
\quad
\mathcal H_R=\int \frac{|x|^4}{R^4}h\,|D^2u\,e_r|^2,
\quad
L_R=\int\omega_R|u|^p.
$$

Direct differentiation gives the exact principal contribution

$$
8\sum_{i,j,k}\operatorname{Re}\int
\partial_{jk}\phi_R\,\partial_{ik}\bar u\,\partial_{ij}u
=8\|\Delta u\|_2^2-8D_R-32\mathcal H_R.
\tag{C1}
$$

The nonlinear contribution, after extracting the conserved energy, is

$$
B_R=\frac8{N+4}\int
\left[N\omega_R+4\frac{|x|^4}{R^4}h\right]|u|^p,
\qquad 0\le B_R\le8L_R.
\tag{C2}
$$

The last bound uses s^4 exp(-s^4)<=1-exp(-s^4). Thus the exact identity is

$$
M_R'=16E-8D_R-32\mathcal H_R+B_R+\mathcal E_R,
\tag{C3}
$$

where

$$
\mathcal E_R=-4\operatorname{Re}\int
\partial_{jk}\Delta\phi_R\,\partial_j\bar u\,\partial_ku
-2\int\Delta^2\phi_R|\nabla u|^2
+\int\Delta^3\phi_R|u|^2.
$$

For arbitrary H^2 fields,

$$
|\mathcal E_R|\le\eta D_R+C_{N,\eta}R^{-4}m,
\qquad
|M_R|\le C_Nm+C_NR m^{3/4}D_R^{1/4}.
\tag{C4}
$$

These follow by integration by parts with g=sqrt(omega_R):

$$
\int g|\nabla u|^2
=-\operatorname{Re}\int g\bar u\Delta u
+\frac12\int\Delta g|u|^2
\le\sqrt{NmD_R}+C_NR^{-2}m.
$$

The bounds ||Delta g||_infty<=C_N R^{-2}, |D^2 Delta phi_R|+|Delta^2 phi_R|<=C_NR^{-2}g, and |Delta^3 phi_R|<=C_NR^{-4} are elementary consequences of the exponential formula. Also |grad phi_R|^2<=R^2g.

Any flow-invariant class with L_R<=epsilon D_R+C(epsilon,m)R^{-4} therefore satisfies
M_R'<=16E-cD_R+C(m)R^{-4}. Choose R so that the error is at most -8E. Then -M_R grows at least linearly and, once large, obeys y'>=c R^{-4}m^{-3}y^4. Integrating (y^{-3})'<=-cR^{-4}m^{-3} forces finite-time loss of H^2 regularity.

## 4. Further fully nonradial angular shapes: product rotations

A second extension is available for N=k+l with k,l>=2 and data invariant under O(k) times O(l):

$$
u(x',x'')=v(|x'|,|x''|).
$$

The key geometric fact is that on every fixed annulus either |x'| or |x''| is bounded away from zero. On the first region O(k) invariance reduces the effective local dimension from N to d_1=l+1<N; on the second it reduces it to d_2=k+1<N.

Using a partition of unity, fixed-annulus interpolation produces contributions of the form

$$
C Q^{d_i/N}\mu^{1+(4-d_i)/N}+C\mu^{1+4/N}.
$$

The exponent d_i/N is strictly below one. Dyadic scaling and Young's inequality then yield

$$
L_R\le\epsilon D_R+C_{N,k,\epsilon}R^{-4}
\left(m^{1+4/(k-1)}+m^{1+4/(l-1)}+m^{1+4/N}\right).
\tag{P1}
$$

The local reduction can be checked directly: on |x'|>c, represent the function by F(r,x'') on R^{l+1}; the measure factor r^{k-1} is comparable to a constant on the compact annulus. Its second derivatives in (r,x'') are contractions of the original Euclidean Hessian. Cutoff-generated first derivatives are controlled by the fixed-annulus H^2 interpolation inequality. Apply ordinary dimension-d_1 Gagliardo--Nirenberg, and similarly for the other patch. The exponent of mass after Young is (N+4-d_i)/(N-d_i)=1+4/(k-1) or 1+4/(l-1), respectively.

The symmetry persists by uniqueness. Consequently every such negative-energy solution blows up in finite forward and backward time, with no finite-variance assumption. An example of a genuinely nonradial shape is A exp(-|x'|^2-2|x''|^2) for A sufficiently large.

This covers nonradial subclasses in all dimensions N>=4. It does not cover general data in any dimension, or axisymmetric data with an unrotated one-dimensional axis. Concentration along such an axis is exactly what prevents this annular dimension reduction from being uniform.

## 5. What remains unresolved

Conserved total angular momentum is not enough to obtain these estimates: zero total angular momentum does not exclude concentrated off-center real bumps. A single angular Sobolev norm, if merely finite initially, is also insufficient unless its growth can be bounded along the nonlinear flow. The invariant symmetry classes avoid that propagation problem but do not remove it for general nonradial data.

The unrestricted negative-energy finite-time blowup conjecture remains unproved by these arguments.

## 6. Derivation of the Whitney/local-mass argument

The collaborating local-mass derivation has the following valid form. Define

$$
\mu_\delta(u)=\sup_{x\ne0}\int_{B(x,\delta|x|)}|u(y)|^2\,dy,
\qquad 0<\delta<1/16.
$$

Then, with C_N independent of delta,

$$
L_R(u)\le C_N\mu_\delta(u)^{4/N}
\left[D_R(u)+\delta^{-4}R^{-4}m\right].
\tag{W1}
$$

The covering proof is sound if all local masses and Hessian integrals are taken on B(a_j,4r_j), with r_j=delta|a_j|/16. Use a cutoff supported on B(a_j,2r_j) and interior gradient interpolation from B(a_j,4r_j). This yields

$$
\int_{B(a_j,r_j)}|u|^p
\le C m_j^{4/N}\left[
\int_{B(a_j,4r_j)}|D^2u|^2+r_j^{-4}m_j\right].
$$

The enlarged balls have overlap bounded independently of delta, by the usual disjoint-subball packing argument and the comparability of nearby radii. Each m_j<=mu_delta. The weight is comparable to omega_R(a_j) throughout B(a_j,4r_j), and
omega_R(a_j)r_j^{-4}<=C delta^{-4}R^{-4}. Summation gives (W1).

For a finite cyclic group acting by simultaneous complex rotations on R^{2d}=C^d, K rotated balls of radius delta|x| are pairwise disjoint if delta<sin(pi/K). Field equivariance, u(gx)=chi(g)u(x), supplies equal mass in these balls and hence mu_delta<=m/K. Initial density invariance alone is insufficient for preservation and should not replace field equivariance in the theorem's hypothesis.

Choose K with 8C_N(m/K)^{4/N}<=2. With eta=2 in (C4), the coefficient of D_R in (C3) is at most -4 after using (W1). The remaining R^{-4} term is harmless for a sufficiently large fixed R. This confirms the cyclic-symmetry finite-time theorem, conditional only on its explicitly stated mass-to-orbit-size bound.

## 7. General compact connected symmetry corollary

The local-mass argument gives a cleaner common generalization. Let G be a compact connected subgroup of O(N), assume its common fixed-vector space is {0}, and let chi:G->U(1) be a continuous character. If

$$
u_0(gx)=\chi(g)u_0(x)\quad (g\in G),
\qquad E(u_0)<0,
$$

then the solution has finite forward and backward lifespan.

Here is the missing geometric step. Every nonzero orbit is infinite: an orbit of a connected group is connected, so a finite orbit would be a singleton, contradicting the fixed-vector assumption. For every integer K>=2, define on the unit sphere

$$
s_K(x)=\max_{g_1,\ldots,g_K\in G}\min_{i\ne j}|g_ix-g_jx|.
$$

The compactness of G^K makes this maximum attained and continuous in x. Infinite orbits imply s_K(x)>0 for every x. Compactness of the unit sphere therefore gives s_K^*=min s_K(x)>0. Pick delta<min(1/16,s_K^*/2). Every orbit has K centers whose delta|x|-balls are disjoint. Equivariance gives equal mass, so mu_delta<=m/K for every field in the symmetry class.

The PDE preserves this class by uniqueness and its orthogonal and gauge symmetries. Choosing K large enough for the absorption threshold, (W1) and (C3)--(C4) prove the claim. The constants need not be effective for the qualitative theorem; K and delta are fixed once the initial mass and group are fixed.

Examples are SO(2) vortices, simultaneous U(1) rotations on C^d with fixed charge, and SO(k) times SO(l) block rotations for k,l>=2. This is an extension to nonradial symmetry classes, not a proof for arbitrary nonradial data. Literature novelty remains unverified.
