# a quantitative action reduction for one-dimensional near-extremizers

This is an proof note. It does **not** prove a uniform approximation by sech channels, improve the unrestricted two-dimensional constant, or solve the planar Lieb–Thirring conjecture.

The new steps below are: a coercive consequence of an existing resolvent identity; retention of that consequence in the existing action construction; a variational choice of the spectral matrix; and a transverse-energy/density transfer. The final missing step is stated explicitly at the end.

## 1. Inputs and notation

The external input is OpenAI, *Sharp one-dimensional Lieb–Thirring inequalities for matrix potentials*, October 5, 2026:

https://www.emergentmind.com/openai-math-explorer/papers/526.pdf?v=adc7f12

The formulas used are its (3.10)–(3.12), (3.24), (3.26), Proposition 4.3, Proposition 5.1, and the compact-penalty argument of Section 6. We work at its parameter sigma = 1/2, so q = 3 and c_sigma = 1/2. The action endpoint is (pi/2) Tr K^2. Its theorem is an input; the refinements proved here are not asserted to appear in that paper.

The already established sharp one-dimensional inequality for orthonormal Hilbert-valued rows is also used:

$$
T_x(U)\ge k_0 S(U),\qquad k_0=\pi^2/4,
\quad S(U)=\int\operatorname{Tr}(UU^*)^3dx.
$$

Initially let Omega be a bounded interval and let U have n orthonormal real rows in H^1_0(Omega;R^d). All matrix coefficients below are constant in x. A second nonnegative quadratic form T_y on the rows can be included; for the planar application it is the y-derivative form. Write

$$
\Gamma=UU^*,\quad \mathsf T_x=\int U'U'^*dx,
\quad \mathsf T_y=\int (\partial_yU)(\partial_yU)^*dx,
\quad M=\int\Gamma^3dx.
$$

Thus T_x=Tr mathsf T_x, T_y=Tr mathsf T_y, T=T_x+T_y, S=Tr M, and D=T_x-k_0 S>=0. The physical operator on the internal Hilbert space is gamma_U(x)=U(x)^*U(x), whereas Gamma is the finite row Gram matrix. They must not be confused.

## 2. A coercive matrix trace comparison

Let B,V be Hermitian, suppose (sI-B)^2+V is uniformly positive for real s, and define

$$
R(t)=\pi^{-1}\int_\mathbb R((sI-B)^2+V+tI)^{-1}ds,
\quad N=\frac12\int_0^\infty(t^{-1/2}I-R(t))dt\ge0.
$$

Put L=R^{-1}. The cited resolvent construction supplies Hermitian Z with

$$
V+tI=L^2+Z^2+i[B,Z],\qquad LZ+ZL=-i[B,L].
$$

For F=(tI+N^2)^{1/2}, let J(t)=||R^{-1/2}-R^{1/2}F||_HS^2 and H(t)=Tr(RZ^2). Its exact positive identity is

$$
\Delta:=\operatorname{Tr}(NV)-\operatorname{Tr}N^3
=\frac12\int_0^\infty(H(t)+3J(t))dt.\tag{2.1}
$$

Assume ||B||_op<=kappa, ||V||_op<=kappa^2, and ||N||_op<=kappa, with kappa>0. Then

$$
\Delta\ge\frac{\|V-N^2\|_{\rm HS}^2}{128\kappa},\qquad
\Delta\ge\frac{\|[B,N^2]\|_{\rm HS}^2}{2048\kappa^3}.\tag{2.2}
$$

Proof: normalize kappa=1 and restrict t to [2,3]. Comparing V with plus/minus I and integrating the resolvents gives (1/2)I<=R<=I; hence I<=L<=2I and ||F||<=2. The Sylvester integral for Z gives ||Z||<=||[B,L]||/(2 lambda_min(L))<=2. Put a=||L-F||_HS and z=||Z||_HS. Then J>=a^2/2 and H>=z^2/2. Also

$$
\|V-N^2\|_{\rm HS}
\le(\|L\|+\|F\|)a+(\|Z\|+2\|B\|)z\le4a+4z.
$$

Its square is at most 64(J+H). Integrating (2.1) over an interval of length one proves the first estimate. For the second,

$$
\|[B,F]\|_{\rm HS}^2\le64H+16J,
\quad \|[B,N^2]\|_{\rm HS}^2=\|[B,F^2]\|_{\rm HS}^2
\le1024H+256J.
$$

Again use (2.1), then restore scale. In particular, splitting the two estimates gives

$$
\Delta\ge\frac{\|V-N^2\|_{\rm HS}^2}{256\kappa}
+\frac{\|[B,N^2]\|_{\rm HS}^2}{4096\kappa^3}.\tag{2.3}
$$

There is no rank factor. There is a largest-scale parameter kappa; this becomes a genuine issue later.

## 3. Retaining this information in the action theorem

For a positive diagonal K, kappa=||K||_op, define

$$
E_K(A)=\int\big(\|A'\|_{\rm HS}^2+\operatorname{Tr}K^2AA^*
-\operatorname{Tr}(AA^*)^3\big)dx.
$$

For rho=AA^* set

$$
\mathcal R_K(A)=\int\min_{B=B^*,\ \|B\|\le\kappa}
\left\{\|A'-BA\|_{\rm HS}^2
+\frac{\|K^2-B^2-\rho^2\|_{\rm HS}^2}{256\kappa}
+\frac{\|[B,\rho^2]\|_{\rm HS}^2}{4096\kappa^3}\right\}dx.\tag{3.1}
$$

There exists a constant lower-triangular C, with A=CU, such that

$$
E_K(A)\ge\frac\pi2\operatorname{Tr}K^2+\mathcal R_K(A).\tag{3.2}
$$

Here is the passage from the cited action proof, including the limiting issue. Denote its regularization by h>0 and its path penalty by tau>0. Its constructed path satisfies tau B'=M_h(B)-AA^*, B(left)=K, B(right)=-K, and ||B||<=kappa. Before discarding a square, its action identity is exactly

$$
E_K(A)-[J_h(-K)-J_h(K)]
=\int\left\{\|A'-BA\|^2+operatorname{Tr}\rho(K^2-B^2)
-\operatorname{Tr}\rho^3+\tau^{-1}\|M_h(B)-\rho\|^2\right\}dx.\tag{3.3}
$$

On the exact constraint rho=M_h(B)>=0, put V=K^2-B^2+hI and N=rho+sqrt(h)I. The source gives 0<=rho<=kappa I. Thus (2.3) applies with kappa replaced by kappa+sqrt(h). Direct expansion gives

$$
\operatorname{Tr}\rho(K^2-B^2)-\operatorname{Tr}\rho^3
\ge\Delta-n\kappa^2\sqrt h.
$$

In (2.3), the two errors become K^2-B^2-rho^2-2sqrt(h)rho and [B,rho^2+2sqrt(h)rho]. They converge uniformly on the fixed finite-dimensional compact set to those in (3.1).

For fixed h, repeat the source's compact-penalty argument with these continuous nonnegative terms retained. The residual penalty makes the exact-constraint lower bound valid up to an error tending to zero as tau tends to zero, uniformly on the compact set. No bound on B' is needed: after retaining the squares one takes the pointwise minimum over B in (3.1). The matrices C have a subsequence converging for fixed h.

The subsequent C_h are also uniformly bounded as h decreases. Indeed their actions have a lower bound bounded below independently of small h, while the positive part of E_K(CU) is quadratic in C and its negative part is coercive of degree six. On a bounded interval an explicit bound is

$$
\int\operatorname{Tr}(CUU^*C^*)^3dx
\ge\frac{\|C\|_{\rm HS}^6}{n^2|\Omega|^2}.
$$

Consequently a further subsequence C_h converges. The pointwise minimum in (3.1) is continuous in A,A' and has an integrable dominating bound on this subsequence. The endpoint tends to (pi/2)Tr K^2. This proves (3.2).

Semidefinite K is allowed by K_nu^2=K^2+nu I and the same finite-dimensional coercivity argument. If K=0 identically choose C=0 and interpret the remainder as zero for that choice.

## 4. Choosing K without a positivity assumption on the original frame

Fix 0<epsilon<1 and mu>0, and set

$$
\eta=\frac{\mu(1-\epsilon)}{1+\mu},\qquad
c=\frac\pi2\sqrt{\frac{1+\mu}{1-\epsilon}}.
$$

Minimize over 0<=R<=I the continuous concave functional

$$
G(R)=(1-\epsilon)\operatorname{Tr}(R\mathsf T_x)
+\eta\operatorname{Tr}(R\mathsf T_y)
-k_0\int\operatorname{Tr}(\Gamma^{1/2}R\Gamma^{1/2})^3dx.
$$

A minimizing projection P exists because the extreme points of this matrix interval are projections. Let U_P be an orthonormal row basis of the retained subspace, with subscript P denoting its quantities. The sharp one-dimensional inequality gives D_P>=0. Comparing G(P) and G(I) yields

$$
T_x-T_{x,P}\le\frac{D+\eta T_y}{\epsilon},\tag{4.1}
$$

and, more precisely,

$$
D_P+\mu T_P\le D+\mu T
-(\epsilon+\mu)(T_x-T_{x,P})
-(\mu-\eta)(T_y-T_{y,P})\le D+\mu T.\tag{4.2}
$$

For a unit vector v in Ran P, vary R=P-t vv*. The one-sided derivative at zero is nonnegative. Therefore, on this retained space,

$$
(1-\epsilon)\mathsf T_{x,P}+\eta\mathsf T_{y,P}\le3k_0 M_P.
$$

It follows that

$$
K^2:=3c^2M_P-(1+\mu)\mathsf T_{x,P}-\mu\mathsf T_{y,P}\ge0.\tag{4.3}
$$

Diagonalize K in decreasing order and apply (3.2) to this row basis. The resulting C is constant and lower triangular.

## 5. The exact upper comparison and its Bregman term

Put R=C^*C and A=CU_P. Since k_i>=k_j for i<=j,

$$
\mathrm{Tri}(C):=\operatorname{Tr}K^2(C^*C-CC^*)
=\sum_{i>j}(k_j^2-k_i^2)|C_{ij}|^2\ge0.\tag{5.1}
$$

Let f(R)=integral Tr(Gamma_P^{1/2} R Gamma_P^{1/2})^3. Its cubic Bregman difference at cI is

$$
\mathrm{Breg}(R)=f(R)-c^3S_P-3c^2\operatorname{Tr}M_P(R-cI).
$$

For Q=Gamma_P^{1/2} R Gamma_P^{1/2}, Q0=c Gamma_P, H=Q-Q0, the integrand is exactly Tr H^2(Q+2Q0). It is at least Tr|H|^3: diagonalize H, and use Q_ii+(Q0)_ii>=|H_ii|. Hence

$$
\mathrm{Breg}(R)\ge\int\|\gamma_A(x)-c\gamma_{U_P}(x)\|_{\mathfrak S^3}^3dx.\tag{5.2}
$$

The equality of the row and physical Schatten expressions follows from the polar decomposition of U_P, and holds for the difference as well.

Equation (4.3), not an unjustified commutation, now gives the exact upper comparison

$$
E_K(A)=2c^3S_P-\mu T(A)-\mathrm{Breg}(R)-\mathrm{Tri}(C).
$$

Combining it with (3.2) yields

$$
\mathcal R_K(A)+\mathrm{Breg}(R)+\mathrm{Tri}(C)+\mu T(A)
\le\frac\pi2\{D_P+r(c)S_P+\mu T_P\},\tag{5.3}
$$

where r(c)=k0-3c^2+4c^3/pi. In particular, because c>=pi/2,

$$
T(A/\sqrt c)\le T+\frac{D+r(c)S_P}{\mu}.\tag{5.4}
$$

This controls total kinetic energy of the transformed frame. It does **not** assert small x-derivative distance between that frame and U. Such a distance does not follow from (5.2).

## 6. Explicit rank-independent near-extremizer bounds

Suppose 0<delta=D/T_x<=1/16. Choose epsilon=sqrt(delta), mu=delta^(3/4), and eta,c as above. Then

$$
T_x-T_{x,P}\le\sqrt\delta\,T_x+\delta^{1/4}T_y,
\quad T(A/\sqrt c)\le T+9\delta^{1/4}T_x,\tag{6.1}
$$

$$
\mathcal R_K(A)+\mathrm{Breg}(R)+\mathrm{Tri}(C)
\le10(\pi/2)\delta^{3/4}T,\tag{6.2}
$$

$$
\int\|\gamma_{A/\sqrt c}-\gamma_{U_P}\|_{\mathfrak S^3}^3dx
\le\frac{40}{\pi^2}\delta^{3/4}T.\tag{6.3}
$$

To check the constants, put z=c/(pi/2). Then r=k0(z-1)^2(2z+1)<=8k0 delta, and S_P<=T_x/k0. All displayed bounds are independent of the retained rank. This is a variational projection, not a cutoff at a fixed mode number or at a fixed individual kinetic energy.

## 7. Turning the Schatten error into physical density error

For positive finite-rank operators G,H on L^2(R_y), put X=sqrt G, Y=sqrt H, D0=X-Y, S0=X+Y and M0=G-H. The identity M0=(S0 D0+D0 S0)/2 gives an elementary square-root estimate. Take K0=sgn(D0)|D0|^4. In an eigenbasis of D0, positivity of S0 plus/minus D0 gives (S0)_ii>=|d_i|. Thus

$$
\operatorname{Tr}M_0K_0=\operatorname{Tr}S_0|D_0|^5
\ge\operatorname{Tr}|D_0|^6.
$$

Schatten Holder then proves ||sqrt G-sqrt H||_6^2<=||G-H||_3. No extra spectral-gap hypothesis is used.

Apply this separately at every x. Write E=integral ||G-H||_3^3 dx and T_y^sum=T_y(G)+T_y(H). The weighted one-dimensional density inequality

$$
\int\rho_\gamma(y)^2dy\le\frac1{\sqrt3}
(\operatorname{Tr}\gamma^3)^{1/2}
(\operatorname{Tr}(-\partial_y^2)\gamma)^{1/2}
$$

applied to gamma=D0^2, together with ||partial_y D0||_HS^2<=2(T_y(G)+T_y(H)), yields

$$
|F(G)^{1/4}-F(H)^{1/4}|
\le(2/3)^{1/8}(E\,T_y^{sum})^{1/8}.\tag{7.1}
$$

The pointwise ingredient is |sqrt(rho_G)-sqrt(rho_H)|<=sqrt(rho_{D0^2}); then use the L^4 reverse triangle inequality. This argument does not claim a false kinetic bound on |G-H|.

Use (7.1) with G=gamma_{A/sqrt c} and H=gamma_{U_P}. Equations (6.1) and (6.3) make this physical density error tend to zero at fixed total kinetic energy. The discarded projection is also harmless at the density level: rho_U-rho_{U_P}=rho_{U_(I-P)}>=0, and the established planar bound K_base=sqrt(3)pi, after anisotropic rescaling, gives

$$
\|\rho_U-\rho_{U_P}\|_2^2
\le\frac2{K_{base}}\sqrt{(T_x-T_{x,P})(T_y-T_{y,P})}.
$$

## 8. Extensions and precise limitations

The initial action argument is for a bounded interval, finite internal dimension, and real rows. For a fixed finite number of rows it extends to H^1(R;H) with a separable real Hilbert space H by finite-dimensional internal approximation, cutoff, and Gram renormalization. In the planar application choose the internal approximations converging in both L^2_y and the y-form norm. These approximations need not contract y-energy, but their energies converge. For fixed U, sextic coercivity is uniform along the approximations: the continuous positive sextic form on the finite-dimensional coefficient sphere has a strictly positive minimum, and convergence preserves it. Therefore the C subsequences remain bounded even while interval length and internal dimension increase. This fixed-row-count passage is separate from, and does not supply, compactness uniform in the number of rows.

The min_B integrand in (3.1) is continuous; an integrable majorant follows by taking B=K and using H^1(R;H) boundedness in x. Thus the action lower bound and the displayed estimates pass to the limit. The same arguments handle semidefinite K as described in Section 3. An empty retained projection is allowed and gives A=0. General complex frames require a separate complex action/realification formulation; none is silently assumed here. Real finite-rank optimizers suffice for the previously established minimal-violating-rank reduction of the planar question.

At exact zero of the strengthened remainder, A'=BA, K^2=B^2+rho^2, and [B,rho^2]=0. On regular occupied components this is the commuting first-order system leading to sech profiles. This observation alone is **not** a quantitative, uniform extraction theorem.

The unresolved issue is to produce approximately commuting sech blocks from small remainder, uniformly in rank and in all energy scales, with the density and energy bounds needed for the planar improvement. The global factor kappa=||K|| can be dominated by a higher-energy spectator while many lower-energy channels carry substantial total energy. Replacing it by each local spectral scale is not justified. The full positive resolvent integral naturally retains such scale information, but turning it into a usable spectral-block estimate remains unproved. Also Gamma<=K, when available from the unregularized field, does not imply Gamma^2<=K^2.

Consequently this note establishes a quantitative action reduction with physical density transfer and no asymptotic excess of total kinetic energy. It does not yet establish proximity to the exact-channel class, the constant K_sat in a neighborhood of that class, or any new unrestricted planar constant.

## 9. A further exact local-scale constraint from the unregularized field

It has not yet closed the block-extraction step.

Assume K>0 and Q_s=s^2 I-2sB+K^2>=0 for every real s, and that the unregularized matrix field is

$$
N=\frac1{2\pi}\int_\mathbb R[\log Q_s-\log(s^2)I]ds\ge0.
$$

Start with strict positive pencils and then take any limit for which this matrix logarithm integral converges. Put A_s=s^2 I+K^2 and X_s=2sB. Symmetrization gives

$$
K-N=\frac1{2\pi}\int_\mathbb R
\left[\log A_s-\frac{\log(A_s+X_s)+\log(A_s-X_s)}2\right]ds.
$$

The resolvent representation of the logarithm and the even resolvent expansion imply the operator inequality

$$
K-N\ge\frac1{2\pi}\int_\mathbb R\int_0^\infty
(A_s+t)^{-1}X_s(A_s+t)^{-1}X_s(A_s+t)^{-1}\,dt\,ds\ge0.\tag{9.1}
$$

Indeed, after conjugating by (A_s+t)^(-1/2), the even difference is Y^2(I-Y^2)^(-1)>=Y^2, where Y=(A_s+t)^(-1/2)X_s(A_s+t)^(-1/2) has norm less than one.

In the K eigenbasis, the diagonal entry of (9.1) can be integrated exactly:

$$
(K-N)_{ii}\ge\sum_j |B_{ij}|^2
\frac{2(k_i+2k_j)}{3(k_i+k_j)^2}
\ge\frac23\sum_j\frac{|B_{ij}|^2}{k_i+k_j}.\tag{9.2}
$$

For verification, the s integral is pi/[2a(a+b)^2] with a=sqrt(k_i^2+t), b=sqrt(k_j^2+t), after its prefactor is extracted. The remaining integral is

$$
\int_0^\infty\frac{dt}{\sqrt{k_i^2+t}(\sqrt{k_i^2+t}+\sqrt{k_j^2+t})^2}
=\frac{2(k_i+2k_j)}{3(k_i+k_j)^2}.
$$

Since N>=0, this proves sum_j |B_ij|^2/(k_i+k_j)<=3k_i/2. It constrains mixing of different spectral scales without replacing K by its largest eigenvalue. It does not by itself imply B^2<=K^2, a weighted eikonal-defect estimate, or uniform sech-block extraction.
