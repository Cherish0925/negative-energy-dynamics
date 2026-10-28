# Arbitrarily slow outgoing BNLS multiwaves via a finite-rank almost-conserved metric

Research continuation, 7 October 2026. This note removes the extra spectral-coercive splitting (SC) hypothesis from the preceding conditional two-wave argument. It uses the full triangular decomposition in Lin–Zeng Theorem 2.1, not merely its polynomial group estimate. In particular, it does not require certification of the unresolved radial Hamiltonian quartet.

## 1. Statement and precise input

Consider the four-dimensional cubic equation

\[
 i u_t=\Delta^2u-|u|^2u.
\]

Let \(0<v<1/2\), and let \(Q_v\) be a smooth exponentially localized profile satisfying

\[
 (\Delta^2+1)Q_v+iv\partial_1Q_v-|Q_v|^2Q_v=0.
\]

Write \(J=-i\), \(A_v=JL_v\), where

\[
 L_v=\Delta^2+1+iv\partial_1-\mathcal V_v,
 \qquad \mathcal V_vh=2|Q_v|^2h+Q_v^2\bar h.
\]

All spaces and forms are real. Use \(X=H^2(\mathbb R^4;\mathbb C)\), with the equivalent norm \(\|h\|_X^2=\|h\|_2^2+\|\Delta h\|_2^2\). The Lin–Zeng hypotheses (H1)–(H3), finite-dimensional kernel, and the graph-domain identities

\[
 D(A_v^k:X\to X)=H^{2+4k},\quad k\ge1,
\]

hold automatically here. Indeed the free form \(L_{v,\infty}=\Delta^2+1+iv\partial_1\) has symbol \(|\xi|^4+1-v\xi_1\), with minimum \(1-3(v/4)^{4/3}>0\). It is a positive isomorphism \(H^2\to H^{-2}\). The decaying smooth potential is a compact map \(H^2\to H^{-2}\): on a fixed ball this follows from Rellich compactness into \(L^2\), and outside the ball its multiplication norm tends to zero. Preconditioning by the positive free form therefore produces identity minus a compact self-adjoint operator. Its negative index and kernel are finite, and its positive spectral subspace has a strictly positive lower bound. Multiplication by \(-i\), with dense domain \(H^2\subset H^{-2}\), is anti-self-dual. The remaining domain condition (H3) follows from the finite kernel by Lin–Zeng Remark 2.3. Finally smooth bounded coefficients and elliptic regularity give the stated graph domains and norm equivalences.

Thus the theorem does not require the exact Morse count, action-Hessian nondegeneracy, or knowledge of whether \(\dim E^u=29\) or \(31\). The sharper existing certificates only give additional information, such as an explicit upper bound on the correction rank.

**Theorem.** For any such profile, put \(Q_{-v}(x)=Q_v(-x)\). There exist \(T<\infty\), \(\gamma>0\), and an inversion-even exact solution \(u\in C([T,\infty);H^6)\) such that

\[
 \left\|u(t)-e^{it}\{Q_v(\cdot-vte_1)+Q_{-v}(\cdot+vte_1)\}\right\|_{H^6}
 \le C e^{-\gamma t}.
\]

In particular, if \(E(Q_v)<0\), then

\[
 P(u)=0,\qquad E(u)=2E(Q_v)<0,
 \qquad \sup_{t\ge T}\|u(t)\|_{H^6}<\infty.
\]

Time translation makes the initial time zero. Constants and starting separation may deteriorate arbitrarily as \(v\downarrow0\); the theorem imposes no positive minimum speed. The proof below establishes the necessary linear estimate with an arbitrarily small exponential rate, which is sufficient for an exponentially decaying interaction error.

## 2. The finite-rank almost-conservation lemma

### 2.1 The triangular decomposition, including the continuous block

Lin–Zeng Theorem 2.1 supplies closed subspaces \(X_j\), \(0\le j\le6\), with \(X_0=\ker L_v\), and

\[
 X=\bigoplus_{j=0}^6X_j.
\]

Every block except \(X_3\) is finite-dimensional in this application. More importantly, their theorem explicitly states

\[
 X_j\subset\bigcap_{k\ge1}D(A_v^k),\qquad j\ne3.
\]

Thus all their finite-dimensional basis functions lie in every Sobolev space; this includes finite complementary directions which need not themselves be eigenfunctions.

The hyperbolic spaces are \(X_5=E^u\) and \(X_6=E^s\), both invariant. The center \(E^c=\bigoplus_{j=0}^4X_j\) is invariant and its equations have the triangular form

\[
\begin{aligned}
 x_0'&=A_{01}x_1+A_{02}x_2+A_{03}x_3+A_{04}x_4,\\
 x_1'&=A_1x_1+A_{12}x_2+A_{13}x_3+A_{14}x_4,\\
 x_2'&=A_2x_2+A_{24}x_4,\\
 x_3'&=A_3x_3+A_{34}x_4,\\
 x_4'&=A_4x_4.
\end{aligned}
\]

All displayed off-diagonal blocks are bounded on the energy space, including the maps from the continuous block. The operators \(A_2,A_3\) are skew-adjoint for the positive metrics \(-L_2,L_3\), respectively. The finite matrices \(A_1,A_4\) have imaginary spectrum and may have Jordan blocks. The Hessian form is

\[
 L_v[h,h]=L_2[x_2,x_2]+L_3[x_3,x_3]
       +2B_{14}[x_1,x_4]+2B_{56}[x_5,x_6],
\]

with \(-L_2,L_3\) coercive and \(B_{14},B_{56}\) nondegenerate pairings. Within the center, the kernel is orthogonal to blocks 1 through 4 in the chosen underlying \(H^2\) inner product. It need not be orthogonal to the hyperbolic blocks.

### 2.2 Arbitrarily small growth in a positive metric

Fix any \(\delta>0\). A finite real matrix with purely imaginary spectrum admits a positive inner product in which its symmetric part has absolute form bound at most \(\delta/10\) times that inner product. One way to see this is to use real Jordan form, retain the skew rotation blocks, and rescale successive generalized vectors so that all nilpotent entries are arbitrarily small. Choose such metrics \(G_1,G_4\) for \(A_1,A_4\).

Define on the center

\[
 q_\delta(h)=a_0\|x_0\|^2+a_1G_1[x_1,x_1]
              -L_2[x_2,x_2]+L_3[x_3,x_3]+a_4G_4[x_4,x_4].
\]

Choose \(a_4\) large, then \(a_1\) small, then \(a_0\) still smaller. More explicitly, in the coordinates scaled by the square roots of these weights, the coupling from block \(j\) to block \(i\) has norm equal to its fixed norm times \(\sqrt{a_i/a_j}\), with weights of blocks 2 and 3 fixed at one. The triangular arrows are only

\[
 4\longrightarrow\{2,3,1,0\},\quad
 \{2,3\}\longrightarrow\{1,0\},\quad 1\longrightarrow0.
\]

Therefore every off-diagonal norm can be made less than \(\delta/(10N)\), where \(N\) is their finite number. Cauchy–Schwarz gives

\[
 \left|\frac{d}{dt}q_\delta(e^{tA_v}h)\right|
 \le\delta q_\delta(e^{tA_v}h),\qquad h\in E^c\cap D(A_v).
\]

There is no attempt to scale away the continuous operator \(A_3\): its metric remains exactly \(L_3\), in which it is skew-adjoint.

Extend \(q_\delta\) to a positive form on all \(X\) by adding arbitrary positive metrics on \(X_5\) and \(X_6\), with no cross terms. The resulting form is coercive and bounded on \(X\). Since its infinite-dimensional part is exactly \(L_3\), it has the form

\[
 q_\delta(h)=\langle(L_v+K_\delta)h,h\rangle,
 \qquad K_\delta\text{ self-adjoint and finite rank}.
\]

The small symmetric-generator bound is asserted only on \(E^c\); the finite hyperbolic dynamics will be separated rather than suppressed. The rank needed for the correction is at most \(\dim\ker L_v+2n^-(L_v)\), hence at most 77 for the present wave, because all coordinate functionals appearing in the correction factor through the finite blocks.

### 2.3 Why the finite-rank kernels are smooth

The preceding finite rank assertion alone would not justify a spatial truncation. We check its dual regularity.

Let \(P_j\) denote the projections associated with the decomposition. For \(j=1\), coordinates of \(P_1h\) are recovered from the pairings \(\langle L_vh,e_{4,k}\rangle\), since \(B_{14}\) is nondegenerate and all other Hessian blocks pairing against \(X_4\) vanish. Thus their dual functions are finite linear combinations of \(L_ve_{4,k}\). Similarly:

* coordinates of \(P_4\) use \(L_vX_1\);
* coordinates of \(P_2\) use \(L_vX_2\);
* coordinates of \(P_5,P_6\) use \(L_vX_6,L_vX_5\), respectively;
* on the center, coordinates of \(P_0\) use \((1+\Delta^2)X_0\), by \(H^2\) orthogonality; on the whole space use \(P_0h=\operatorname{Orth}_{X_0}^{H^2}(h-P_5h-P_6h)\). The already smooth hyperbolic coordinate functionals preserve the claimed dual regularity.

All these dual functions lie in \(H^m\) for every finite \(m\). Expanding the difference between the displayed Hessian matrix and the new metric therefore writes

\[
 K_\delta[h,h]=\sum_{j,k=1}^{m_\delta}c_{jk}
       \langle f_j,h\rangle\langle f_k,h\rangle,
 \qquad f_j\in\bigcap_{m\ge0}H^m,
\]

with a real symmetric matrix \(c\). No exponential decay or isolated imaginary eigenvalue assumption has entered this argument.

### 2.4 Compactly supported approximation, including the generator

Choose a smooth spatial cutoff \(\chi_R\) and replace each \(f_j\) by \(f_{j,R}=\chi_Rf_j\). These functions are smooth and compactly supported, and converge to \(f_j\) in every fixed Sobolev norm. Let \(K_{\delta,R}\) be the corresponding self-adjoint finite-rank form.

The estimates needed below are

\[
 \|K_{\delta,R}-K_\delta\|_{X\to X^*}\to0,
\]

\[
 \|A_v^*(K_{\delta,R}-K_\delta)
       +(K_{\delta,R}-K_\delta)A_v\|_{X\to X^*}\to0,
\]

where the second expression is interpreted as a quadratic form, initially on \(D(A_v)\). To verify the second estimate, move \(A_v\) from \(h\) to the smooth dual functions in each rank-one term. Since \(A_v^*:H^2\to H^{-2}\) is bounded, convergence of the dual functions in \(H^2\) is already enough. Choosing convergence in \(H^{10}\) additionally gives more than the regularity needed for all graph-domain calculations later; no uniform-in-\(R\) exponential localization is claimed.

First fix \(\delta\) and the positive metric. Then take \(R\) large relative to its coercivity constant. Relabeling the initially prescribed small rate, we obtain the following precise lemma.

**Compact metric lemma.** For every \(\varepsilon>0\), there exists a self-adjoint finite-rank \(K_\varepsilon\) with smooth compactly supported kernels such that

\[
 c_\varepsilon\|h\|_X^2\le
 q_\varepsilon(h):=\langle(L_v+K_\varepsilon)h,h\rangle
 \le C_\varepsilon\|h\|_X^2\quad(h\in X),
\]

and

\[
 |\langle(K_\varepsilon A_v+A_v^*K_\varepsilon)h,h\rangle|
 \le\varepsilon q_\varepsilon(h)
 \quad(h\in E^c\cap D(A_v)).
\]

The form extends to all \(h\in E^c\). The constants and support radius can be very large. Their size does not matter because the starting separation remains free.

## 3. Only the hyperbolic modes need to be transported exactly

Let \(D_h=E^u\oplus E^s\). Its dimension is finite and its form is nondegenerate. The basis and dual basis of its invariant projection are smooth and exponentially localized. Here this stronger localization is available because every eigenvalue in \(D_h\) lies off the imaginary axis, hence off the free essential spectrum. Weighted elliptic resolvent estimates for the fourth-order system imply exponential decay of eigenvectors; induction along finite Jordan chains does the same for generalized eigenvectors. The duals can equivalently be recovered through the nondegenerate \(L_v\) pairing on \(D_h\).

For completeness, the weighted argument uses the invertibility of the free matrix symbol \(A_{v,\infty}-\lambda\) when \(\Re\lambda\ne0\). Conjugating by \(e^{a\langle x\rangle}\) introduces an arbitrarily small relative graph perturbation for sufficiently small \(a>0\). After cutting off to the far field, the decaying profile potential is absorbed in the free resolvent estimate. Cutoff commutators are compactly supported. Truncated weights and passage to the limit yield an exponential \(H^2\) bound, and elliptic bootstrap gives every required derivative. For a generalized root vector the right side is the already localized preceding vector. No claim about embedded imaginary modes is needed.

Choose synthesis and analysis maps \(Z,W\) for this hyperbolic subspace with \(WZ=I\), \(A_vZ=ZB\), \(WA_v=BW\), and \(\ker W=E^c\). Transport two reflected copies to \(\pm vt e_1\) and correct their exponentially small off-diagonal Gram matrix. Denote the resulting maps by \(Z(t),W(t)\), and the direct sum of their constant generators by \(B_0\).

Writing

\[
 S(t,x)=Q_v(x-vte_1)+Q_{-v}(x+vte_1),
 \quad \mathcal A(t)=J\{\Delta^2+1-\mathcal V(t)\},
\]

where \(\mathcal Vh=2|S|^2h+S^2\bar h\), gives

\[
 \dot Z+ZB_0-\mathcal A Z=E_Z(t),\qquad
 \dot W+W\mathcal A-B_0W=E_W(t),
\]

with \(E_Z,E_W\) exponentially small in all fixed operator and graph norms used below. Let

\[
 \Pi=I-ZW,
 \quad \mathcal C=\mathcal A-ZE_W.
\]

Then \(Ww=0\) is preserved by \(w_t=\mathcal Cw\), and \(\mathcal C-\mathcal A\) is exponentially small and finite rank with smooth range and dual range.

## 4. The two-center near-conserved coercive form

Choose a real velocity field \(b(t,x_1)\) equal to \(+v\) on the right core and \(-v\) on the left core, with transition scale comparable to \(vt\). Its derivatives satisfy

\[
 |b|\le v,\quad \|\partial_x^j b\|_\infty\le C_vt^{-j},\quad
 \|b_t\|_\infty\le C_v/t.
\]

Let \(D_b=b\partial_1+\tfrac12\partial_1b\), and translate the compact metric corrections to the two cores, denoting them \(K_\varepsilon^\pm(t)\). Set

\[
 \mathcal H_\varepsilon(t)
 =\Delta^2+1-\mathcal V(t)+iD_b
      +K_\varepsilon^+(t)+K_\varepsilon^-(t),
 \qquad Q_t(w)=\langle\mathcal H_\varepsilon(t)w,w\rangle.
\]

### 4.1 Coercivity and the constant in the small growth estimate

Take a smooth partition \(\chi_+^2+\chi_-^2+\chi_0^2=1\). The core cutoffs have radius comparable to \(vt\), equal one on the supports of their compact metric corrections, and are supported where \(b=\pm v\). They exclude the other core. Their derivatives are \(O_v(t^{-j})\). Fourth-order IMS expansion, the first-order momentum identity, and exponential potential tails give

\[
 Q_t(w)=q_\varepsilon^+(\chi_+w)+q_\varepsilon^-(\chi_-w)
       +\langle(\Delta^2+1+iD_b)\chi_0w,\chi_0w\rangle
       +O_\varepsilon(t^{-1}+e^{-\kappa t})\|w\|_X^2.
\]

The compact terms localize exactly because their dual functions are supported where the core cutoff is one. The free exterior form is uniformly positive for \(v<1/2\). Hence, for sufficiently large \(T_\varepsilon\),

\[
 c'_{\varepsilon}\|w\|_X^2\le Q_t(w)\le C'_{\varepsilon}\|w\|_X^2,
\]

and, simultaneously,

\[
 q_\varepsilon^+(\chi_+w)+q_\varepsilon^-(\chi_-w)\le2Q_t(w).
\]

This second inequality matters: one must not replace local energies by the norm and lose an uncontrolled condition-number factor multiplying \(\varepsilon\). The exact IMS decomposition allows the factor 2, independently of the condition number, after taking the starting time sufficiently large.

### 4.2 Form derivative with no loss of derivatives

For the uncorrected moving action \(\mathcal H_0=\Delta^2+1-\mathcal V+iD_b\), direct differentiation along \(h_t=\mathcal Ah\) gives the form operator

\[
 \dot{\mathcal H}_0+\mathcal H_0\mathcal A+\mathcal A^*\mathcal H_0
 =iD_{b_t}+[D_b,\Delta^2]-\{\mathcal V_t+b\partial_1\mathcal V\}.
\]

The last term is exponentially small: transport cancels in each core and the transition region is in profile tails. The commutator is a bounded quadratic form on \(H^2\), with estimate

\[
 |\langle[D_b,\Delta^2]w,w\rangle|
 \le C\{\|b'\|_\infty\|w\|_{H^2}^2
   +\|b''\|_\infty\|w\|_{H^1}\|w\|_{H^2}
   +\|b'''\|_\infty\|w\|_2\|w\|_{H^2}\}.
\]

This follows by writing the form as \(-2\Re\langle\Delta w,\Delta D_bw\rangle\) and canceling the skew-adjoint \(D_b\Delta w\) term. Thus fourth spatial derivatives do not act on an uncontrolled solution factor.

For a transported compact correction, its translation derivative cancels the local transport term exactly:

\[
 \dot K_\varepsilon^\pm+K_\varepsilon^\pm\mathcal A
       +\mathcal A^*K_\varepsilon^\pm
 =T_{\pm vt}(K_\varepsilon A_{\pm v}
                   +A_{\pm v}^*K_\varepsilon)T_{\pm vt}^{-1}
       +O_\varepsilon(e^{-\kappa t}).
\]

The error comes from the distant wave potential on a fixed compact support. The principal form on the right has compact kernels, since a differential operator applied to a smooth compact kernel remains compactly supported. It therefore acts only on \(\chi_\pm w\).

Although \(\chi_\pm w\) need not lie exactly in the corresponding single-wave center, its hyperbolic coordinates are exponentially small when \(W(t)w=0\). Indeed, the exact moving constraint differs from the raw single-core one only exponentially, and the hyperbolic dual tails outside the core cutoff are exponential. Projecting away these small coordinates and applying the compact metric lemma, initially with rate \(\varepsilon/4\) and then relabeling the metric by \(\varepsilon\), yields

\[
 |\langle(\dot K_\varepsilon^\pm+K_\varepsilon^\pm\mathcal A
       +\mathcal A^*K_\varepsilon^\pm)w,w\rangle|
 \le\varepsilon q_\varepsilon^\pm(\chi_\pm w)
      +C_\varepsilon e^{-\kappa t}\|w\|_X^2.
\]

Finally, replacing \(\mathcal A\) by \(\mathcal C\) introduces an exponentially small finite-rank form. Combining all estimates gives, for center solutions,

\[
 |Q_t'(w)|\le\{2\varepsilon+C_\varepsilon/t
                         +C_\varepsilon e^{-\kappa t}\}Q_t(w).
\]

Consequently the center evolution obeys

\[
 \|U_C(t,s)\|_{H^2\to H^2}
 \le C_\varepsilon e^{\varepsilon|t-s|}
        \max(t/s,s/t)^{K_\varepsilon},\qquad t,s\ge T_\varepsilon.
\]

Since \(\varepsilon\) was arbitrary, this is precisely an arbitrarily small exponential bound. Neither polynomial growth for the full nonautonomous two-center system nor exponential localization of imaginary modes is asserted or needed.

## 5. Upgrade to H6 without an unbounded commutator

Define \(\mathcal D(t)=\Pi(t)\mathcal A(t)\Pi(t)\). Since the projection has a smooth finite-dimensional range and smooth duals, \(\mathcal D-\mathcal A\) is a bounded finite-rank smoothing operator. Uniform elliptic graph estimates give, on \(\ker W(t)\),

\[
 \|w\|_{H^6}\asymp\|w\|_{H^2}+\|\mathcal D(t)w\|_{H^2}.
\]

If \(z=\mathcal Dw\) and \(w_t=\mathcal Cw\), then

\[
 z_t=\mathcal Cz+\mathcal F(t)w,
 \qquad \mathcal F=\dot{\mathcal D}+[\mathcal D,\mathcal C].
\]

The operator \(\mathcal F:H^2\to H^2\) is uniformly bounded. To see this, write \(\mathcal D=\mathcal A+F_1\) and \(\mathcal C=\mathcal A+F_2\), with \(F_j\) finite rank and smooth. Then

\[
 \mathcal F=\mathcal A_t+(F_1)_t+[\mathcal A,F_2-F_1]+[F_1,F_2].
\]

The time derivative \(\mathcal A_t\) is multiplication by smooth bounded coefficients. In each commutator with a finite-rank map, \(\mathcal A\) either acts on a smooth range vector or is transferred to its smooth dual vector; this gives a bounded finite-rank map on \(H^2\). No commutator of a spatial cutoff with the free generator occurs in this graph argument.

Furthermore \(\mathcal Fw\) lies in the moving center whenever \(w\) does. This follows by differentiating \(Wz=0\) and using \(\dot W+W\mathcal C=B_0W\). Thus Duhamel can use the center propagator. Keeping the multiplicative ratio bound along the time integral gives

\[
 \|U_C(t,s)\|_{H^6\to H^6}
 \le C_\varepsilon(1+|t-s|)
       e^{\varepsilon|t-s|}\max(t/s,s/t)^{K_\varepsilon}.
\]

For \(t,s\ge T\ge1\), the ratio is at most \(1+|t-s|\). This leaves a polynomial factor times the same small exponential rate.

## 6. Exponentially weighted right inverse and nonlinear completion

The interaction defect of the approximate sum is \(O(e^{-\kappa t})\) in \(H^6\) for some \(\kappa>0\), because all mixed cubic terms contain tails from distinct exponentially localized cores. Let \(\alpha>0\) be smaller than the absolute real parts of the finitely many nonzero hyperbolic eigenvalues, after allowing for Jordan polynomial factors. If there are none, omit the corresponding integrals.

Choose constants in this order:

\[
 0<\gamma<\min(\kappa,\alpha),\qquad 0<\varepsilon<\gamma/2,
\]

then construct the compact metric for this \(\varepsilon\), and finally take \(T\) sufficiently large. The center integral backward from infinity is bounded in

\[
 \|h\|_{X_\gamma}=\sup_{t\ge T}e^{\gamma(t-T)}\|h(t)\|_{H^6},
\]

because

\[
 \int_0^\infty (1+r)^{K_\varepsilon+1}
             e^{-(\gamma-\varepsilon)r}\,dr<\infty.
\]

Hyperbolic stable directions are integrated forward from \(T\), and unstable directions backward from infinity; their integrals are bounded by the usual \((\alpha-\gamma)^{-1}\) and \((\alpha+\gamma)^{-1}\) factors. The remaining coupling of the finite hyperbolic system with the center is exponentially small in \(T\), so a Neumann series supplies a right inverse for the full linearized equation. Very large metric or Green constants are absorbed by taking the initial separation larger.

Since \(H^6(\mathbb R^4)\) is an algebra, the nonlinear remainder is locally quadratic and Lipschitz there. Its fixed-point map on \(X_\gamma\) is a contraction in a ball of radius \(C e^{-\kappa T}\) for sufficiently large \(T\). This gives an exact solution exponentially asymptotic to the two waves.

Choose the left metric, transported mode bases, and cutoffs by reflection of the right ones. The equation, defect, center/hyperbolic splittings, and Green construction then preserve inversion-even functions. Equivalently one can symmetrize the right inverse by reflection. The fixed point is even, so its total momentum vanishes exactly. Conservation and asymptotic separation give the exact energy and mass identities

\[
 E(u)=2E(Q_v),\qquad M(u)=2M(Q_v),\qquad P(u)=0.
\]

The momentum identity also follows directly from oddness of its density under inversion.

## 7. Consequences and scope

1. Applied to the already constructed four-dimensional negative-energy branch, the theorem produces bounded forward-global zero-momentum negative-energy solutions. The missing radial quartet certificate is no longer a prerequisite for this construction.
2. The proof explains the geometric alternative in the preceding intrinsic-spreading theorem: this pair separates linearly, so the negative-energy zero-momentum solution escapes every single expanding ball whose speed is smaller than the two-core separation speed.
3. The mechanism is more general than the symmetric pair. Finitely many smooth localized profiles with distinct velocities and a common admissible frequency can be treated with separate compact corrections and a partition into moving cores and exterior. This extension needs the same finite-index hypotheses for each profile; no negative-energy conclusion follows unless the sum of their energies is negative.
4. No claim is made that every negative-energy zero-momentum solution is global, that an open set of such data remains bounded, or that the underlying four-dimensional profile certificates have received external independent verification.

## 8. Source and mathematical provenance

The external structural input is Z. Lin and C. Zeng, *Instability, index theorem, and exponential trichotomy for linear Hamiltonian PDEs*, Memoirs of the AMS 275 (2022), no. 1347, arXiv:1703.04016v4. The precise input is Theorem 2.1, including finite-block smoothness, bounded triangular couplings, and the positive skew-adjoint continuous block; Theorem 2.2 alone would not justify the localizable metric construction.

The compact finite-rank near-conserved metric, its moving-core patching, the arbitrarily small center growth rate, and their application to the present BNLS pair are deductions in this note. Literature priority for this gluing mechanism has not yet been determined. The statement is a proof-level continuation of the existing four-dimensional certified construction, not a numerical conclusion about the unresolved radial eigenvalues.

## 9. Finite spatial moments and inherited compact symmetries

The same construction can be carried out in

\[
 Y=\{h\in H^{10}: x_jh\in H^6,\ 1\le j\le4\},
 \quad \|h\|_Y=\|h\|_{H^{10}}+\sum_j\|x_jh\|_{H^6}.
\]

This strengthens the initial-data conclusion to finite variance. The details below avoid assuming that the center projection commutes with multiplication by position.

### 9.1 Arbitrary fixed unweighted graph regularity

The Section 5 argument iterates. With \(\mathcal F=\dot{\mathcal D}+[\mathcal D,\mathcal C]\),

\[
 (\mathcal D^k)_t+[\mathcal D^k,\mathcal C]
 =\sum_{j=0}^{k-1}\mathcal D^j\mathcal F\mathcal D^{k-1-j}.
\]

Here \(\mathcal F\) is an order-zero smooth multiplier plus smooth finite-rank operators, bounded on every fixed Sobolev space. The sum maps \(H^{2+4(k-1)}\) boundedly to \(H^2\). Each \(\mathcal D^k\) preserves the moving center. Induction and elliptic graph norm equivalence therefore give the small exponential center bound, with an enlarged polynomial factor, in every fixed \(H^{2+4k}\). In particular it holds in \(H^{10}\).

### 9.2 A projected position equation

For a center solution \(w\), set \(z_j=\Pi x_jw\). Put

\[
 B=\dot\Pi+\Pi\mathcal C-\mathcal C\Pi.
\]

The fact that \(\mathcal C\) preserves the moving center says \(B\Pi=0\). Hence

\[
 (z_j)_t-\mathcal Cz_j=B(I-\Pi)x_jw+\Pi[x_j,\mathcal C]w.
\]

Both terms lie jointly in the center, since the left side does, and their \(H^6\) norm is bounded by \(C\|w\|_{H^{10}}\), uniformly for large \(t\). The first term is finite rank. Indeed each raw hyperbolic coordinate of \(w\) is zero, so in that coordinate

\[
 \langle\psi(\cdot-c_k(t)),x_jw\rangle
 =\langle(x_j-c_{k,j}(t))\psi(\cdot-c_k(t)),w\rangle.
\]

The right dual functions have uniformly bounded Sobolev norms by exponential localization. The finite Gram correction does not change this cancellation, because all raw constraints vanish individually. Thus \(Wx_jw\), and therefore \((I-\Pi)x_jw\), are bounded in \(H^6\) by \(C\|w\|_{H^2}\). All coefficients of \(B\) are uniformly smooth finite-rank coefficients.

For the second term, \([x_j,J\Delta^2]\) has order three, so it maps \(H^{10}\to H^6\). Multiplication potentials commute with \(x_j\). The remaining finite-rank commutators are uniformly smoothing: within a single transported block, the common center cancels between range and dual; cross-core terms contain only polynomial center differences multiplying exponentially small Gram or coupling coefficients. Thus they are uniformly bounded in every required graph norm.

Duhamel and the unweighted \(H^{10}\) estimate yield

\[
 \|U_C(t,s)\|_{Y\cap\ker W(s)\to Y\cap\ker W(t)}
 \le C_\varepsilon(1+|t-s|)^{m_\varepsilon}
                         e^{\varepsilon|t-s|}.
\]

To recover the full position norm from \(z_j\), use
\(x_jw=z_j+ZWx_jw\) and the uniformly bounded centered-dual estimate just proved. The argument is first performed on smooth weighted data and extended by the resulting a priori bounds.

### 9.3 Hyperbolic transport and the weighted right inverse

The center projections are uniformly bounded on \(Y\). One can verify this by \(x_j\Pi h=\Pi x_jh+[x_j,\Pi]h\); the commutator is uniformly smoothing by the same centered range/dual cancellation. For the finite hyperbolic component, use the time-dependent coordinate norm \((1+t)|a|\), which is equivalent to the \(Y\) norm of \(Z(t)a\) for large \(t\). Equivalence follows from separated localized cores at \(\pm vte_1\), finite-dimensional norm equivalence, and fixed \(v>0\). The ratio

\[
 \frac{1+t}{1+s}\le1+|t-s|,\qquad t,s\ge0,
\]

costs only an additional polynomial factor in the finite-dimensional stable and unstable Green integrals. The exponentially small linear couplings remain small in these weighted norms; factors polynomial in \(t\) can be absorbed by slightly reducing their exponential rate.

The defect obeys \(\|\mathrm{defect}(t)\|_Y\le Ce^{-\kappa' t}\) for some \(\kappa'>0\), since its unweighted and position-weighted mixed products are exponentially small, with at most a polynomial factor from moving centers. Finally the quadratic and cubic nonlinear remainder is locally quadratic and Lipschitz on \(Y\): a position factor is always assigned to one correction factor, and \(H^6\) is an algebra. For example,

\[
 \|x_j(S|h|^2)\|_{H^6}
 \le C\|S\|_{H^6}\|h\|_{H^{10}}\|x_jh\|_{H^6}.
\]

Therefore the same weighted fixed point gives

\[
 \|u(t)-R(t)\|_{H^{10}}+
 \sum_j\|x_j(u(t)-R(t))\|_{H^6}\le Ce^{-\gamma t}.
\]

In particular the initial datum is in \(H^{10}\cap\{xu\in L^2\}\), and the exact solution has finite variance at every finite time. Its variance may grow quadratically under the outgoing separation; no uniform bound on variance is claimed.

### 9.4 Compact-group symmetry

Suppose the approximate pair is invariant under a compact group of spatial orthogonal transformations, in addition to full inversion. The physical linearized operator and all its single-wave hyperbolic Riesz projections commute with that group. Translations along the common fixed axis and the corrected Gram construction preserve this property. Alternatively, average any bounded linear right inverse over the compact group using Haar measure; equivariance of the differential equation shows that it remains a right inverse with the same norm bound. This averaging is applied to the Green operator, not to a finite-rank certificate, so there is no false claim that averaging finite-rank operators preserves rank.

The fixed point can consequently be taken invariant under the group. In particular, for the project's axisymmetric branch one may choose the exact zero-momentum pair to be both inversion-even and invariant under transverse \(O(3)\). The weighted conclusion then also supplies the finite axial moment. These deductions strengthen the geometric comparison with the cylindrical setting; their validity rests on the full gluing proof above, rather than on a formal superposition alone.

## 10. Families and the leading variance asymptotic

The stable finite-dimensional initial coordinate at time \(T\) need not be fixed to zero. Specify a sufficiently small stable coordinate \(a_s(T)=\eta\), add its homogeneous forward-decaying contribution to the Green formula, and perform the same contraction on a ball controlled by \(|\eta|+e^{-\kappa T}\). Every correction produced by the zero-stable-data right inverse has stable coordinate zero at \(T\), so the prescribed coordinate is exact and the resulting parameterization is injective. Reflection-even pairs of stable coordinates have the same dimension as the stable space of one wave.

For the already established sufficiently small-velocity branch, this gives at least 29 real parameters of distinct exact forward-global zero-momentum negative-energy pairs, all with the same asymptotic profiles and hence identical mass, energy and momentum. This is a finite-dimensional family and does not assert an open set of bounded solutions. The weighted version uses the identical argument in \(Y\); its neighborhood may depend on \(T\).

For the project's inversion-conjugation profile, \(|Q_v(x)|^2\) is even and its intrinsic centroid vanishes. The weighted convergence in Section 9 therefore gives, after possibly decreasing the convergence rate,

\[
 \int_{\mathbb R^4}|x|^2|u(t,x)|^2\,dx
 =2M(Q_v)v^2t^2+2\int_{\mathbb R^4}|x|^2|Q_v(x)|^2\,dx
       +O(t e^{-\gamma t}).
\]

The omitted cross term between separated profiles is exponentially small, and the exact-solution correction contributes at most \(C\|xR(t)\|_2\|x(u-R)(t)\|_2+C\|x(u-R)(t)\|_2^2\). The spatial centroid stays zero by inversion symmetry. Thus zero total momentum and strictly negative energy coexist with quantitatively ballistic internal separation and quadratic variance growth.
