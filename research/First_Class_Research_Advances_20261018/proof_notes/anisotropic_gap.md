# Uniform negative-energy traveling-wave mass gap for quadratic–quartic dispersion

Research derivation, 2026-10-18. This extends the existing isotropically homogeneous phase-gap mechanism to a genuinely anisotropic, mixed differential-order model. The main concrete case is a cubic equation in three physical variables. No existence of negative-energy waves for that new model is asserted here.

## 1. Statement and conventions

Let \(x\in\mathbb R^{n_2}\), \(y\in\mathbb R^{n_4}\), with \(n_2,n_4\ge1\), and put
\[
 D=2n_2+n_4,\qquad r=4/D,\qquad p=2+2r.
\]
Let \(b(\eta)\) be a real, even, positive elliptic quartic polynomial: \(c|\eta|^4\le b(\eta)\le C|\eta|^4\). Define
\[
 \mathcal A=-\Delta_x+b(D_y),\quad
 A(u)=\|\nabla_xu\|_2^2+\int b(\eta)|\widehat u(\xi,\eta)|^2\,d\xi d\eta,
 \quad M(u)=\|u\|_2^2,
\]
\[
 H_a=\{u\in L^2:A(u)<\infty\},\quad
 E(u)=\tfrac12A(u)-\tfrac1p\|u\|_p^p,
 \quad P(u)=\operatorname{Im}\int\overline u\nabla u.
\]
The sharp mass \(M_c>0\) is defined by
\[
 \|u\|_p^p\le\frac p2\left(\frac{M(u)}{M_c}\right)^r A(u). \tag{GN}
\]

**Theorem.** There is \(\delta>0\), depending only on \(n_2,n_4,b\), such that every nonzero weak \(H_a\) solution of
\[
 [\mathcal A+\omega+i v_x\cdot\nabla_x+i v_y\cdot\nabla_y]U-|U|^{p-2}U=0 \tag{TW}
\]
with \(\omega\in\mathbb R\), \((v_x,v_y)\in\mathbb R^{n_2+n_4}\), and \(E(U)<0\), satisfies
\[
 M(U)\ge M_c+\delta. \tag{GAP}
\]
The constant is independent of both velocity components and frequency. No radiality, spatial moment, optimizer uniqueness, real-sector nondegeneracy, or previously constructed traveling branch is needed. The proof works for the noninteger exponent \(p-2=8/D\).

In particular, \(n_2=1,n_4=2,b(\eta)=|\eta|^4\) gives the genuinely three-variable cubic equation
\[
 iu_t=-\partial_x^2u+\Delta_y^2u-|u|^2u,
 \quad (x,y)\in\mathbb R\times\mathbb R^2.
\]
Its critical scaling is \(u_\lambda(x,y)=\lambda^2u(\lambda^2x,\lambda y)\); it is not an isotropic fourth-order model in three dimensions.

## 2. Anisotropic embedding and sharp compactness

The dilation \(u_\lambda=\lambda^{D/2}u(\lambda^2x,\lambda y)\) preserves \(M\), and multiplies \(A,E,\|u\|_p^p\) by \(\lambda^4\). The homogeneous frequency volume satisfies
\[
 |\{(\xi,\eta):|\xi|^2+b(\eta)\le R^4\}|=C_bR^D.
\]
Consequently Hausdorff–Young and weighted Cauchy–Schwarz give \(H_a\hookrightarrow L^q\) for every
\[
 2\le q<\frac{2D}{D-4}\quad(D>4),
 \qquad 2\le q<\infty\quad(D\le4).
\]
Indeed the weight integral is finite precisely when \(q/(q-2)>D/4\). Optimizing the inhomogeneous embedding under the above dilation yields
\[
 \|u\|_p^p\le C M(u)^rA(u),
\]
because \(p=2+8/D\). Thus the optimal constant is finite and positive.

The energy space continuously embeds into ordinary \(H^1(\mathbb R^{n_2+n_4})\). Local Rellich compactness in \(L^2\), followed by interpolation with an anisotropically admissible \(L^q\), \(q>p\), gives local compactness in \(L^p\). The same \(H^1\) local-mass vanishing lemma gives global \(L^{2+4/(n_2+n_4)}\) vanishing; interpolation with an admissible \(L^q\), \(q>p\), gives \(L^p\) vanishing. Here \(2+4/(n_2+n_4)\le p\), and a suitable \(q>p\) exists since \(p\) is strictly below the anisotropic Sobolev endpoint.

Normalize a GN maximizing sequence by \(M(u_j)\to M_c\), \(A(u_j)=1\), \(\|u_j\|_p^p\to p/2\). Vanishing is impossible, so translations yield a nonzero weak limit \(Q\). Local compactness gives almost-everywhere convergence. If
\[
 M_1=M(Q)>0,\quad A_1=A(Q)>0,\quad
 M_2=M_c-M_1,\quad A_2=1-A_1,
\]
quadratic splitting, Brezis–Lieb and GN imply
\[
 M_c^r\le M_1^r A_1+M_2^rA_2.
\]
If both masses are positive, the right side is strictly less than
\(M_c^r(A_1+A_2)=M_c^r\), a contradiction. Thus \(M_2=0\); GN then forces \(A_2=0\). The convergence is strong in \(H_a\). This also proves compactness modulo translations of the normalized optimizer family and of every normalized near-optimizer sequence.

## 3. Constant phase without a positivity-preserving fourth-order operator

Write \(k=p/2=1+r>1\). Starting with the real sharp constant, \(u=X+iY\) satisfies
\[
 \|X^2+Y^2\|_k
 \le\|X^2\|_k+\|Y^2\|_k
 \le C^{1/k}\left(M(X)^{r/k}A(X)^{1/k}+M(Y)^{r/k}A(Y)^{1/k}\right)
\]
\[
 \le C^{1/k}(M(X)+M(Y))^{r/k}(A(X)+A(Y))^{1/k}.
\]
The real and complex sharp constants are therefore equal. For a complex optimizer equality holds throughout. Strict convexity of \(L^k\) makes \(X^2,Y^2\) proportional. Apply the same conclusion after a constant rotation of the real pair, in particular \((X+Y,X-Y)/\sqrt2\). The two proportionality relations force \(X,Y\) to be real-linearly dependent: if both signs of \(X/Y\) occurred on sets of positive measure, the rotated squared ratio would take two different values (or one component would vanish on one set and not the other). Hence every complex optimizer has constant phase. No assertion that its real representative has one sign is used.

For a normalized real optimizer \(Q\),
\[
 M(Q)=M_c,\quad A(Q)=1,\quad \|Q\|_p^p=k,
\]
the Euler–Lagrange equation is
\[
 (\mathcal A+\omega_*)Q-|Q|^{2r}Q=0,
 \qquad \omega_*=r/M_c>0. \tag{EL}
\]

## 4. Phase-kernel simplicity and coercivity

Set \(L_Q=\mathcal A+\omega_*-|Q|^{2r}\). Expanding GN at \(Q+ith\), \(h\) real, proves \(\langle h,L_Qh\rangle\ge0\). This second-order variation exists for every \(p>2\); its coefficient is \(k\int|Q|^{p-2}h^2\).

If \(h\in\ker L_Q\), put \(x=A(h)\) and \(y=M(h)/M_c\). Hölder, sharp GN, and weighted arithmetic–geometric mean give
\[
 x+ry=\int|Q|^{2r}h^2
 \le\|Q\|_p^{2r}\|h\|_p^2
 \le kx^{1/k}y^{r/k}
 \le x+ry.
\]
Equality forces \(x=y\) and \(h^2=yQ^2\). The kernel of a nonnegative form is linear, so \(h+Q\) also belongs to it and \((h+Q)^2=zQ^2\) for a constant \(z\). Subtracting gives \(h=cQ\), including on the zero set of \(Q\). Thus
\[
 \ker L_Q=\mathbb RQ. \tag{K}
\]

The multiplication form \(|Q|^{p-2}\) is compact relative to \(H_a\): approximate it in \(L^{p/(p-2)}\) by bounded compactly supported functions, use \(H_a\hookrightarrow L^p\), and use local \(L^2\) compactness for the approximants. Since \(\omega_*>0\), compactness and (K) imply
\[
 \langle h,L_Qh\rangle\ge c_Q\bigl(M(h)+A(h)\bigr),
 \qquad \langle h,Q\rangle_2=0. \tag{C}
\]
For completeness, if this failed, normalized \(h_j\perp Q\) with form tending to zero would have a weak limit \(h\); compactness of the potential term plus positivity of \(\mathcal A+\omega_*\) implies that this limit is nonzero and lies in \(\ker L_Q\cap Q^\perp\), a contradiction.

## 5. Weak-profile identities and their legitimacy

The weak energy-space profile has sufficient regularity for cutoff phase and dilation tests. Shift the symbol by a large constant:
\[
 |\xi|^2+b(\eta)-v_x\cdot\xi-v_y\cdot\eta+\Lambda\asymp1+|\xi|^2+|\eta|^4.
\]
The inverse is an anisotropic elliptic multiplier of degree \(-4\). Its local Sobolev improvement uses homogeneous dimension \(D\). Starting below the Sobolev endpoint, bootstrapping the equation improves reciprocal integrability according to
\[
 \beta_{j+1}=(1+8/D)\beta_j-4/D.
\]
For \(D>4\), the starting value can be chosen arbitrarily close to \(\beta_0=(D-4)/(2D)\), strictly below the fixed point \(1/2\); the iterates eventually cross zero. For \(D\le4\), start with any sufficiently large finite integrability exponent. This proves boundedness. The nonlinearity is then in \(L^2\), so \(\mathcal AU\in L^2\). These claims use the usual dyadic anisotropic elliptic multiplier estimate. For the concrete cubic \(D=4\) case the bootstrap is unnecessary: \(U\in L^6\) gives \(U^3\in L^2\), and \((1+\mathcal A)^{-1}:L^2\to L^\infty\) follows from \(\int(1+a)^{-2}<\infty\).

For quartic polynomial \(b\), the remaining identities follow by local integration by parts. Use cutoffs \(\chi(x/R^2,y/R)\), with the symmetrized anisotropic dilation vector field \(2x\cdot\nabla_x+y\cdot\nabla_y+D/2\). All differentiated cutoff coefficients have the matching anisotropic weights; the error terms are bounded by kinetic and mass tails plus \(\|U\|_{L^p(\mathrm{outside})}^p\), and tend to zero. No moment \(\int |(x,y)|^2|U|^2\) is used. Testing (TW) by \(U\) and by this cutoff generator yields
\[
 A+\omega M-v_x\cdot P_x-v_y\cdot P_y-\|U\|_p^p=0, \tag{N}
\]
\[
 4E=v_x\cdot P_x+\tfrac12v_y\cdot P_y. \tag{P}
\]
Cutoff modulation \(e^{i\theta\chi_R(x)}U\) gives the exact quadratic-direction momentum identity
\[
 2P_x=v_xM. \tag{Gx}
\]
The quartic operator commutes with the \(x\)-cutoff. Similarly cutoff \(y\)-modulation gives
\[
 v_yM=\int\nabla b(\eta)|\widehat U(\xi,\eta)|^2\,d\xi d\eta. \tag{Gy}
\]
The latter can alternatively be obtained by the bounded commutator argument in \(L_x^2H_y^2\). It implies
\[
 |v_y|\le C_b\left(A(U)/M(U)\right)^{3/4}.
\]

## 6. Remove all quadratic-direction motion exactly

Put \(U=e^{iv_x\cdot x/2}V\). Substitution in (TW) gives
\[
 [\mathcal A+\widetilde\omega+i v_y\cdot\nabla_y]V-|V|^{p-2}V=0,
 \qquad \widetilde\omega=\omega-|v_x|^2/4.
\]
By (Gx), \(P_x(V)=0\), and direct expansion gives
\[
 M(U)=M(V),\qquad E(U)=E(V)+\frac{|v_x|^2}{8}M(V).
\]
In particular \(E(U)<0\Rightarrow E(V)<0\). It suffices to prove the gap for profiles with \(v_x=0\). Their identities reduce to
\[
 4E(V)=\tfrac12v_y\cdot P_y(V),\qquad
 \widetilde\omega M(V)=rA(V)+(8-p)E(V). \tag{R}
\]
The anisotropic scaling preserves this reduced profile class, with
\[
 \widetilde\omega_\lambda=\lambda^4\widetilde\omega,
 \quad (v_y)_\lambda=\lambda^3v_y,
 \quad E(V_\lambda)=\lambda^4E(V).
\]

## 7. Contradiction proof of the uniform gap

Suppose reduced negative-energy profiles \(V_j\) have \(M(V_j)\downarrow M_c\). Normalize \(A(V_j)=1\). GN gives
\[
 -\frac12\left[\left(\frac{M(V_j)}{M_c}\right)^r-1\right]
 \le E(V_j)<0.
\]
Hence \(E(V_j)\to0\), \(\|V_j\|_p^p\to k\), and normalized near-optimizer compactness gives, after translation and constant phase,
\[
 V_j\to Q\quad\text{strongly in }H_a,
\]
where \(Q\) is a real normalized optimizer. Choose the remaining constant phase so that \(Y_j=\operatorname{Im}V_j\) satisfies \(\langle Y_j,Q\rangle=0\). Equation (R) gives
\[
 \widetilde\omega_j\to r/M_c=\omega_*.
\]
In fact (Gy) bounds the normalized quartic velocities, but no velocity convergence is needed for the contradiction.

Write \(V_j=X_j+iY_j\) and \(L_j=\mathcal A+\widetilde\omega_j-|V_j|^{p-2}\). The imaginary equation, paired with \(Y_j\), gives the exact identity
\[
 \langle Y_j,L_jY_j\rangle
 =-\int Y_jv_{y,j}\cdot\nabla_yX_j
 =\tfrac12v_{y,j}\cdot P_y(V_j)=4E(V_j)<0. \tag{I}
\]
But strong \(L^p\) convergence implies
\[
 |V_j|^{p-2}\to |Q|^{p-2}
 \quad\text{in }L^{p/(p-2)},
\]
including when \(0<p-2<1\). Hölder and the energy-space embedding therefore imply
\[
 |\langle h,(L_j-L_Q)h\rangle|=o(1)\|h\|_{H_a}^2
\]
uniformly in \(h\). Coercivity (C), applied to \(Y_j\perp Q\), makes the left side of (I) nonnegative for all sufficiently large \(j\), contradiction. This proves (GAP).

The proof does not assume positivity or a spectral gap for the full moving symbol \(\mathcal A+\widetilde\omega-v_y\cdot D_y\). Only the nonmoving optimizer phase form is used.

## 8. Additional exact consequences

* If \(v_y=0\), every traveling profile has \(E(V)=0\) in its quadratic rest frame and hence \(E(U)=|v_x|^2M/8\ge0\). Negative energy requires genuine motion in the quartic directions; ordinary quadratic Galilean motion cannot produce it.
* Define the quadratic-frame-invariant energy
  \[
  E_{\mathrm{int}}(U)=E(U)-\frac{|P_x(U)|^2}{2M(U)}.
  \]
  For a traveling profile it equals \(E(V)\). The proof establishes the stronger statement
  \[
  E_{\mathrm{int}}(U)<0\Longrightarrow M(U)\ge M_c+\delta,
  \]
  even if laboratory-frame \(E(U)\ge0\). It also yields
  \[
  4E_{\mathrm{int}}(U)=\tfrac12v_y\cdot P_y(U).
  \]
* Any positive quadratic form \(\xi^{\mathsf T}B\xi\) can replace \(|\xi|^2\) after an invertible linear coordinate change; direct expansion gives the frame energy \(E-\frac1{2M}P_x^{\mathsf T}BP_x\).
* The gap concerns exact traveling profiles, not all time-dependent bounded trajectories. Its optimal numerical size and nonemptiness of the negative-internal-energy profile class remain separate questions.

## 9. Scope beyond polynomial quartic symbols

The compactness, constant-phase, phase-kernel and contradiction arguments above depend only on ellipticity, reality, evenness and anisotropic homogeneity. They extend directly to sufficiently smooth positive quartic-homogeneous \(b\), once the Fourier commutator versions of (P), (Gy) and anisotropic elliptic bootstrap are supplied. The fully local proof above already covers \(b=|\eta|^4\), \(\sum\eta_j^4\), and every positive even quartic polynomial. Keeping that explicit class avoids hiding nonlocal commutator regularity assumptions in the theorem statement.

## 10. Preliminary primary-literature comparison

The anisotropic equation and its critical scaling are established subjects; neither is claimed new. Relevant primary results located on 2026-10-18:

* G. Fibich, B. Ilan and S. Schochet, *Critical exponents and collapse of nonlinear Schrödinger equations with anisotropic fourth-order dispersion* (2003): anisotropic GN and critical exponents/collapse. Publisher/institution record: https://cris.tau.ac.il/en/publications/critical-exponents-and-collapse-of-nonlinear-schr%C3%B6dinger-equation/
* K. Komada, *Existence of Blow-up Solutions to Nonlinear Schrödinger Equations with Anisotropic Fourth-Order Dispersion*, Funkcialaj Ekvacioj 65 (2022), 191–214, DOI 10.1619/fesi.65.191. Primary abstract: https://www.jstage.jst.go.jp/article/fesi/65/2/65_191/_article/-char/en . It concerns masscritical/supercritical blowup; full comparison is still required.
* A. Esfahani, H. Hajaiej, A. Pomponio, *New Insights into the Solutions of a Class of Anisotropic Nonlinear Schrödinger Equations on the Plane*, arXiv:2405.11199, Milan J. Math. 93 (2025), 349–393. Their displayed model has quadratic \(x\)-dispersion and \(D_y^{2s}\) with \(0<s<1\), rather than quartic \(s=2\). It includes normalized solutions and boosted waves, so generic anisotropic traveling-wave existence is not a novelty claim here. https://arxiv.org/abs/2405.11199

The specific candidate extension derived here is the velocity- and frequency-uniform gap above the anisotropic critical mass, equivalently for negative quadratic-frame-invariant energy. The targeted search did not establish a prior identical theorem, but this is not a completed priority survey.

## 11. Fully explicit three-variable cubic cutoff calculation, including positive lower-order dispersion

This section supplies a direct local proof of the analytic identities in the concrete model
\[
 {\cal A}_\mu=-\partial_x^2+\Delta_y^2-\mu\Delta_y,\quad
 x\in\mathbb R,\ y\in\mathbb R^2,\quad \mu\ge0.
\]
Write \(A=\|\partial_xU\|_2^2+\|\Delta_yU\|_2^2\),
\(B=\mu\|\nabla_yU\|_2^2\), \(F=\|U\|_4^4\), and
\(E_\mu=(A+B)/2-F/4\).

### Regularity from the energy space

The energy space embeds into \(H^1(\mathbb R^3)\), hence \(U\in L^6\). Thus \(U^3\in L^2\), all first-order drift terms are in \(L^2\), and \(\mu\Delta_yU\in L^2\). The equation implies \((-\partial_x^2+\Delta_y^2)U\in L^2\). Its elliptic symbol controls \(1+|\xi|^2+|\eta|^2\), so \(U\in H^2(\mathbb R^3)\). Since \(H^2(\mathbb R^3)\) is an algebra, the equation can be bootstrapped: \(U\in H^k\), \(k\ge2\), implies \(U^3\in H^k\), the drifts lie in \(H^{k-1}\), and the order-two or order-four elliptic operator gains at least two ordinary derivatives. This gives \(U\in H^{k+1}\). Equivalently absorb the whole \({\cal A}_\mu\) into its elliptic resolvent at every step. Hence \(U\in H^k\) for every finite \(k\), without any spatial-moment assumption.

### A skew cutoff generator

Let \(z=(x,y)\), \(F_0(z)=(2x,y)\), \(\chi\in C_c^\infty(\mathbb R^3)\) be real, equal to one on the unit ball, and zero outside the radius-two ball. Set
\[
 F_R(z)=\chi(z/R)F_0(z),\quad d_R=\operatorname{div}F_R,\quad
 K_R=F_R\cdot\nabla+\tfrac12d_R.
\]
The operator \(K_R\) is skew-adjoint in \(L^2\), so
\(\operatorname{Re}\langle f,K_Rf\rangle=0\).
For each \(R\), \(K_RU\) is an admissible energy-space test function by the regularity just established. Moreover
\[
 \|\partial^\alpha F_R\|_\infty\le C_\alpha R^{1-|\alpha|}
 \quad(|\alpha|\ge1).
\]
Inside the ball of radius \(R\), \(d_R=4\) and the derivative matrix of \(F_R\) is \(\operatorname{diag}(2,1,1)\).

For the \(x\)-kinetic term, differentiate explicitly:
\[
 \partial_x(K_RU)=K_R\partial_xU+
    \sum_j(\partial_xF_{R,j})\partial_jU+
    \tfrac12(\partial_xd_R)U .
\]
The skew term has zero real pairing with \(\partial_xU\), and the other terms converge to \(2\|\partial_xU\|_2^2\). The difference is bounded by a constant times
\(\|U\|_{H^1(|z|>R)}^2\), plus terms with an additional \(R^{-1}\).

For the quartic term,
\[
 \Delta_y(K_RU)=K_R\Delta_yU
 +2\sum_{\alpha\in y,j}(\partial_\alpha F_{R,j})
                 \partial_\alpha\partial_jU
 +(\Delta_yF_R)\cdot\nabla U
 +(\nabla_yd_R)\cdot\nabla_yU
 +\tfrac12(\Delta_yd_R)U .
\]
Pair this with \(\Delta_yU\). The first term again has zero real part. Inside the ball the second term is exactly \(2\Delta_yU\), and all remaining terms vanish there. The annular error is bounded by
\[
 C\|U\|_{H^2(|z|>R)}^2
 +C R^{-1}\|\Delta_yU\|_{L^2(|z|>R)}
                       \|U\|_{H^1(|z|>R)}
 +C R^{-2}\|\Delta_yU\|_2\|U\|_2,
\]
which tends to zero. This is why no unbounded factor \(xU\) or \(yU\) remains in the limiting argument. Therefore the quartic contribution tends to \(2\|\Delta_yU\|_2^2\). The same first-order calculation in the \(y\) variables gives the lower-order contribution \(B\).

The frequency term is zero exactly. For the cubic term,
\[
 \operatorname{Re}\int |U|^2\overline U K_RU
 =\int \tfrac14d_R|U|^4\longrightarrow F.
\]
Let \(B_v=i v\cdot\nabla\). Since \(B_v\) is self-adjoint and \(K_R\) skew-adjoint,
\[
 \operatorname{Re}\langle B_vU,K_RU\rangle
 =\tfrac12\operatorname{Re}\langle U,[B_v,K_R]U\rangle
 =-\tfrac12\int\sum_{\ell,j}v_\ell
           (\partial_\ell F_{R,j})\operatorname{Im}(\overline U\partial_jU).
\]
Dominated convergence applies to the current, since \(U,\nabla U\in L^2\). The limit is
\(-v_xP_x-\tfrac12v_y\cdot P_y\).
Putting the terms together gives the precise Pohozaev identity
\[
 2A+B-F=v_xP_x+\tfrac12v_y\cdot P_y,
 \qquad
 4E_\mu=B+v_xP_x+\tfrac12v_y\cdot P_y. \tag{Pmu}
\]
The Nehari test is simply
\[
 A+B+\omega M-v_xP_x-v_y\cdot P_y-F=0. \tag{Nmu}
\]

For the quadratic momentum identity use
\(\phi_R(x)=x\chi_1(x/R)\), with \(\chi_1=1\) near zero. Testing by
\(i\phi_RU\), or differentiating the corresponding compactly generated phase variation, gives
\[
 \int \phi_R'(x)\left(2\operatorname{Im}(\overline U\partial_xU)
                      -v_x|U|^2\right)=0.
\]
All \(y\)-operators commute with \(\phi_R\). Since \(\phi_R'\) is uniformly bounded and tends to one, \(2P_x=v_xM\).

### Uniformity for every \(\mu\ge0\)

Remove \(v_x\) by the exact boost. The reduced identities are
\[
 4E_\mu=B+\tfrac12v_y\cdot P_y
       =B+\langle Y,({\cal A}_\mu+\omega'-|W|^2)Y\rangle,
 \qquad
 \omega'M=A-B+4E_\mu. \tag{Rmu}
\]
Under the anisotropic normalization \(A(W_\lambda)=1\), the coefficient changes to \(\mu_\lambda=\lambda^2\mu\). Since the theorem is for all nonnegative coefficients, this preserves its class.

Suppose a sequence of reduced profiles has \(M\downarrow M_c\), \(A=1\), \(E_\mu<0\), allowing arbitrary \(\mu_j\ge0\). Principal sharp GN gives
\[
 E_{\mu_j}(W_j)\ge
 \tfrac12B_j-\tfrac12(M(W_j)/M_c-1).
\]
Thus \(B_j\to0\), \(E_{\mu_j}(W_j)\to0\), \(F(W_j)\to2\).
Near-optimizer compactness gives \(W_j\to Q\) strongly in the principal energy space, and (Rmu) gives \(\omega'_j\to1/M_c\).

Choose phases with \(Y_j\perp Q\). The form
\[
 -\partial_x^2+\Delta_y^2+\omega'_j-|W_j|^2
\]
is uniformly coercive on \(Q^\perp\) for large \(j\). Adding the nonnegative form \(-\mu_j\Delta_y\) preserves coercivity. Therefore (Rmu) implies \(4E_{\mu_j}(W_j)\ge0\), contradiction.

**Consequently one and the same positive \(\delta\) works for every
\(\mu\ge0\), every frequency and every velocity.** It is unnecessary to prove \(\mu_j\to0\) after normalization. The stronger invariant formulation is
\[
 E_\mu(U)-\frac{P_x(U)^2}{2M(U)}<0
 \quad\Longrightarrow\quad M(U)\ge M_c+\delta.
\]
The same argument covers any positive-semidefinite quadratic form in the \(y\) variables: its contribution \(B\) is nonnegative, has anisotropic degree two, satisfies the same identities, and is retained as a positive form in the final coercivity step.
