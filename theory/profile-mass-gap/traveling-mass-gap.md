# A uniform ground-mass gap for negative-energy traveling waves

Research note, 7 October 2026. This note proves a qualitative mass gap for every finite-energy negative-energy traveling profile of the pure mass-critical biharmonic NLS in every dimension $N\ge1$. The four-dimensional cubic equation is one application. The proof uses an elementary real/complex Gagliardo--Nirenberg argument and a second-order equality calculation for the phase kernel. It does not require Fourier rearrangement, uniqueness of ground states, nondegeneracy of the real linearized operator $L_+$, radial symmetry of the traveling profile, or a bound on its speed. No claim of worldwide priority is made.

## 1. The statement and the precise threshold

Fix an integer $N\ge1$, and put
$$
 \alpha=8/N>0,\qquad r=4/N=\alpha/2,\qquad p=\alpha+2=2r+2.
$$
For $f\in H^2(\mathbb R^N;\mathbb C)$, write
$$
 M(f)=\|f\|_2^2,\quad A(f)=\|\Delta f\|_2^2,\quad
 B(f)=\|f\|_p^p,\quad E(f)=\tfrac12A(f)-\tfrac1pB(f).
$$
Let $M_c>0$ be the sharp mass in
$$
 B(f)\le\frac p2\left(\frac{M(f)}{M_c}\right)^{\alpha/2}A(f).
                                                               \tag{1.1}
$$
The ordinary Gagliardo--Nirenberg inequality makes its sharp constant finite. Sharp optimizers exist by the normalized compactness argument in Section 3. Section 4 proves their constant complex phase directly, including noninteger powers.

**Theorem 1.1.** There exists $\varepsilon_N>0$ such that every nonzero distributional $H^2$ solution of
$$
 \Delta^2U+\omega U+i v\cdot\nabla U-|U|^\alpha U=0,
 \qquad \omega\in\mathbb R,\ v\in\mathbb R^N,
                                                               \tag{1.2}
$$
with $E(U)<0$, satisfies
$$
 \boxed{M(U)\ge M_c+\varepsilon_N.}                              \tag{1.3}
$$
Thus the infimum of masses of negative-energy traveling waves is strictly above the ground mass. The positive gap is qualitative; no numerical lower value for $\varepsilon_N$ is supplied. If that profile class is empty the statement holds vacuously.

This is a theorem about traveling profiles. It does **not** establish the same strict gap for arbitrary globally bounded negative-energy evolutions, whose asymptotic form has not been classified.

## 2. Identities for arbitrary $H^2$ weak profiles

Every profile in (1.2) belongs to $H^4$, including when $\alpha$ is noninteger. If $N\le8$, the Sobolev embedding gives $U\in L^{2(1+\alpha)}$ (using any finite exponent when $N=4$, and $L^\infty$ when $N<4$). Thus $|U|^\alpha U\in L^2$, and (1.2) immediately gives $\Delta^2U\in L^2$.

For $N>8$, here are the explicit bootstrap details. Choose $\mu>0$ large enough that
$$
 A_\mu=\Delta^2+i v\cdot\nabla+\mu
$$
has symbol bounded below by $c(1+|\xi|^4)$. Its constant-coefficient elliptic inverse maps $L^s$ continuously into $W^{4,s}$ for every $1<s<\infty$, by the Fourier multiplier theorem. Rewrite the distributional equation as
$$
 U=A_\mu^{-1}(|U|^\alpha U)+(\mu-\omega)A_\mu^{-1}U.
$$
The second term is in $H^4$, hence in every $L^q$ between two and $q_{\rm lin}=2N/(N-8)$. Initially $U\in L^{q_0}$, $q_0=2N/(N-4)$. If $U\in L^q$, the nonlinear term is in $L^{q/(1+\alpha)}$, where this exponent is greater than one, initially and at every subsequent step. Elliptic Sobolev improvement gives the reciprocal-exponent recurrence
$$
 a_{j+1}=(1+8/N)a_j-4/N,\qquad
 a_0=\tfrac12-2/N,
$$
and hence $a_j=\tfrac12-(2/N)(1+8/N)^j$, until the desired exponent is reached. If a step crosses a Sobolev endpoint, choose an intermediate exponent instead. After finitely many steps one reaches
$$
 U\in L^{q_{\rm target}},\qquad q_{\rm target}=2(1+\alpha).
$$
The linear term never obstructs this finite iteration because $q_{\rm target}<q_{\rm lin}$ for $N>8$. Thus the nonlinear term is now in $L^2$, and the original equation gives $U\in H^4$. Only this regularity, not any false claim of a smooth noninteger Nemytskii map, is needed below. No weighted moment is assumed.

The real pairing of (1.2) with $U$ gives
$$
 A(U)+\omega M(U)-v\cdot P(U)-B(U)=0,
 \quad P(U)=\operatorname{Im}\int\bar U\nabla U.                 \tag{2.1}
$$

The cutoff dilation identity gives
$$
 \boxed{v\cdot P(U)=8E(U).}                                    \tag{2.2}
$$
Here is an energy-space justification of (2.2). Let $\phi_R=R^2\phi(x/R)$, with $\phi(x)=|x|^2/2$ on the unit ball and constant outside a larger ball, and uniformly bounded derivatives of order one through six after the indicated scaling. Let
$$
 \mathcal V_R(t)=2\operatorname{Im}\int\nabla\phi_R\cdot\bar u\nabla u,
 \quad u(t,x)=e^{i\omega t}U(x-vt).
$$
This is a strong solution, by the regularity just established. Translation of the profile gives at $t=0$
$$
 \mathcal V_R'(0)=2\int D^2\phi_R(x)[v,j_U(x)]\,dx
 \longrightarrow2v\cdot P(U),
 \quad j_U=\operatorname{Im}(\bar U\nabla U)\in L^1.
$$
On the other hand, the localized fourth-order virial identity has leading terms
$$
 8\operatorname{Re}\int\partial_{jk}\phi_R\,
          \partial_{ij}\bar U\,\partial_{ik}U
 -\frac{2\alpha}{p}\int\Delta\phi_R|U|^p,
$$
and all other terms are bounded in absolute value by
$C(R^{-2}\|\nabla U\|_2^2+R^{-4}\|U\|_2^2)$.
Dominated convergence sends the leading terms to $8A-(2N\alpha/p)B=8A-(16/p)B=16E$. Thus $2v\cdot P=16E$, proving (2.2) without a moment assumption.

Combining (2.1)--(2.2) with $B=pA/2-pE$ gives
$$
 \boxed{\omega M=\frac4N A+(8-p)E
                 =\frac4N A+(6-8/N)E.}                        \tag{2.3}
$$

For completeness, a second identity, not needed in the core contradiction, is
$$
 W(U):=\operatorname{Im}\int\Delta U\nabla\bar U
       =\frac14M(U)v.                                         \tag{2.4}
$$
To justify it at $H^2$, differentiate the stationary action
$S=E+\omega M/2-v\cdot P/2$ in the legitimate direction $i f_R U$, where $f_R(x)=x_j\chi(x/R)$. The derivative is
$$
 2\int\nabla f_R\cdot\operatorname{Im}(\Delta U\nabla\bar U)
 +\operatorname{Im}\int(\Delta f_R)\bar U\Delta U
 -\frac12v\cdot\int|U|^2\nabla f_R=0.
$$
The middle term vanishes as $R\to\infty$, since $\|\Delta f_R\|_\infty=O(R^{-1})$. The other two converge by $L^1$ domination and $\nabla f_R\to e_j$. Hence (2.4).

## 3. Near-optimizer compactness with the normalization fixed

**Lemma 3.1.** If a sequence $f_n\in H^2$ satisfies
$$
 M(f_n)\to M_c,\quad A(f_n)=1,\quad B(f_n)\to p/2,
                                                               \tag{3.1}
$$
then some subsequence, after translations, converges strongly in $H^2$ to a sharp optimizer $Q$, with
$$
 M(Q)=M_c,\quad A(Q)=1,\quad B(Q)=p/2.
$$

**Proof.** The sequence is bounded in $H^2$ and does not vanish locally in mass. To see the latter explicitly, a partition into unit cubes and cutoffs with bounded overlap, followed by the ordinary mass-critical Gagliardo--Nirenberg inequality on each cutoff, gives
$$
 \|f\|_p^p\le C\left(\sup_y\int_{B(y,R_0)}|f|^2\right)^{\alpha/2}
                 \|f\|_{H^2}^2
$$
for a fixed $R_0$. Thus a suitable translated subsequence has a nonzero weak $H^2$ limit $Q$. Local Rellich compactness also gives almost-everywhere convergence after a subsequence. Let $r_n=f_n-Q$. Weak orthogonality in $L^2$ and $\dot H^2$, and Brezis--Lieb for $L^p$, give the three corresponding norm splittings.

Set $m=M(Q)/M_c\in(0,1]$, $a=A(Q)\in[0,1]$. Apply (1.1) to $Q$ and to $r_n$, and pass to the limit. Then
$$
 1\le m^{\alpha/2}a+(1-m)^{\alpha/2}(1-a).                      \tag{3.2}
$$
If $0<m<1$, both powers are strictly less than one, so their convex combination in (3.2) is strictly less than one: a contradiction. Therefore $m=1$, after which (3.2) forces $a=1$. The remainder tends to zero in $L^2$ and $\dot H^2$, hence also in $H^2$ by interpolation. All limiting equalities follow. $\square$

Only translation noncompactness remains after the two normalizations in (3.1). No uniqueness or quantitative stability theorem for optimizers is used.

## 4. Constant phase and a one-dimensional phase kernel in every dimension

### 4.1 The real and complex sharp constants agree; every optimizer has constant phase

Let $C_{\mathbb R}$ be the sharp constant in $B(f)\le C M(f)^r A(f)$ over real-valued functions. For $u=a+i b$, the triangle inequality in $L^{p/2}$, followed by the real GN inequality and the two-term Hölder inequality, gives
$$
 \begin{split}
 \|u\|_p^2
 &=\|a^2+b^2\|_{p/2}
 \le\|a\|_p^2+\|b\|_p^2\\
 &\le C_{\mathbb R}^{2/p}
       [M(a)^{2r/p}A(a)^{2/p}+M(b)^{2r/p}A(b)^{2/p}]\\
 &\le C_{\mathbb R}^{2/p}
        [M(a)+M(b)]^{2r/p}[A(a)+A(b)]^{2/p}.
 \end{split}                                                   \tag{4.1}
$$
Here $2r/p+2/p=1$. The opposite comparison follows because real functions are a subset of complex functions. Therefore the two sharp constants agree.

If $u$ is a complex optimizer, all inequalities in (4.1) are equalities. Strict convexity in the first triangle inequality says $a^2$ and $b^2$ are proportional almost everywhere. If either is zero, the optimizer already has constant phase. Otherwise
$$
 a^2=\tau|u|^2,\qquad b^2=(1-\tau)|u|^2,
 \qquad0<\tau<1.
$$
Apply the same equality argument to $e^{i\pi/4}u$, which is another optimizer. Its real and imaginary squares are also proportional, so $ab=c|u|^2$ for a fixed real constant $c$. These identities imply a fixed real ratio $b/a=c/\tau$ wherever $u\ne0$. Hence
$$
 \boxed{u=e^{i\vartheta}q\quad\hbox{for some real }q\in H^2.}     \tag{4.2}
$$
The real function may change sign; no positivity or radial symmetry has been inferred. This avoids the even-integer restriction of the Fourier-rearrangement route.

The constant-phase argument is known: a public Minkowski-plus-rotation proof appears in the last paragraph of Proposition 3.8 of Fernandez--Jeanjean--Mandel--Maris, arXiv:2010.01448v3. Lenzmann--Sok also explicitly distinguishes real-valuedness at arbitrary powers from their even-power spatial rearrangement theorem. We have supplied the short homogeneous-GN adaptation to keep the dependencies precise.

### 4.2 Nonnegativity of the phase Hessian

Take the limiting optimizer $Q$ in Lemma 3.1 real by (4.2). Its Euler--Lagrange equation with the fixed normalization is
$$
 \Delta^2Q+\omega_Q Q-|Q|^{2r}Q=0,
 \qquad\omega_Q=\frac r{M_c}=\frac4{NM_c}>0.                    \tag{4.3}
$$
For example, differentiate $B(f)/(M(f)^rA(f))$, and use $A(Q)=1$, $B(Q)=r+1$, to obtain precisely these coefficients. Define
$$
 L_-=\Delta^2+\omega_Q-|Q|^{2r}.
$$
It is a continuous quadratic form on $H^2$, since $Q,h\in L^p$ and $p=2r+2$. It is nonnegative. Indeed, for real $h\in H^2$ the curve
$$
 g_\varepsilon=
 \left(\frac{M_c}{M_c+\varepsilon^2\|h\|_2^2}\right)^{1/2}
 (Q+i\varepsilon h)
$$
has mass $M_c$, hence $E(g_\varepsilon)\ge0=E(Q)$. Its quadratic coefficient is $\frac12\langle h,L_-h\rangle$. This calculation uses only the twice differentiable energy functional with power $p>2$.

### 4.3 Simplicity of the phase kernel without Fourier positivity

We give the argument with general normalization $A=\|\Delta Q\|_2^2>0$, $M=M_c$, so $\omega_Q=rA/M$ and $\int|Q|^{2r+2}=(r+1)A$. Suppose $b\in H^2$ is real and $L_-b=0$ as a form equation. Set
$$
 B=\|b\|_2^2,\qquad C=\|\Delta b\|_2^2.
$$
Pairing the kernel equation with $b$ gives
$$
 \int|Q|^{2r}b^2=C+\frac{rAB}{M}.                              \tag{4.4}
$$
Sharp GN applied to $Q+i\sqrt{s}\,b$, $s\ge0$, gives
$$
 N(s):=\int(Q^2+s b^2)^{r+1}
 \le R(s):=(r+1)(1+sB/M)^r(A+sC).                              \tag{4.5}
$$
At zero both values and first derivatives agree, by (4.4). Subtract the common tangent, divide by $s^2$, and let $s\downarrow0$. The integrand of the Taylor remainder is nonnegative by convexity. Fatou's lemma therefore gives
$$
 D:=\int |Q|^{2r-2}b^4
 \le (r-1)\frac{AB^2}{M^2}+2\frac{BC}{M}.                      \tag{4.6}
$$
For $r<1$, the integrand is interpreted as infinity where $Q=0$ and $b\ne0$, and as zero where both vanish. The same Taylor-remainder limit proves that this infinity cannot occur on a positive-measure set; the resulting $D$ is finite. For $r=1$, the weight is one. For $r>1$, the weight is zero on the zero set of $Q$. Thus (4.6) does not assume an unjustified fourth derivative of the nonlinearity at its zeros.

Cauchy--Schwarz gives the reverse estimate
$$
 D\ge\frac{(C+rAB/M)^2}{(r+1)A}.                              \tag{4.7}
$$
Combining (4.6)--(4.7) and multiplying by $(r+1)A$ yields exactly
$$
 0\le-(C-AB/M)^2.
$$
Hence $C=AB/M$, and equality holds in Cauchy--Schwarz. It follows that
$$
 b^2=(B/M)Q^2
$$
on the nonzero set of $Q$. This already accounts for the full integral $B$, so $b=0$ almost everywhere on the zero set too, including the case $r>1$.

The form kernel is a linear space and contains $Q$, so the same argument applies to $b+Q$: for another constant $k'$, $(b+Q)^2=k'Q^2$. Subtracting $b^2=(B/M)Q^2$ gives $2bQ=(k'-B/M-1)Q^2$. Thus $b$ is a constant multiple of $Q$ on its nonzero set and, by the preceding mass argument, on its zero set as well. We have proved
$$
 \boxed{\ker L_-={\rm span}\{Q\}.}                              \tag{4.8}
$$

### 4.4 Coercivity on the complement

The potential form is compact relative to $\Delta^2+\omega_Q$. To check this without a bounded-potential assumption, note that $|Q|^{2r}\in L^{p/(2r)}$. On a bounded region, weakly convergent bounded $H^2$ sequences converge strongly in $L^p$ after restriction because the mass-critical exponent is strictly energy-subcritical. On the complement of a large ball, Hölder bounds the potential form by
$$
 \||Q|^{2r}\mathbf1_{|x|>R}\|_{p/(2r)}\|h\|_p^2,
$$
which tends uniformly to zero on bounded $H^2$ sets. Thus the conjugated operator
$$
 (\Delta^2+\omega_Q)^{-1/2}|Q|^{2r}(\Delta^2+\omega_Q)^{-1/2}
$$
is compact. Nonnegativity and the simple kernel (4.8) then give, for some $c_Q>0$,
$$
 \boxed{\langle h,L_-h\rangle\ge c_Q\|h\|_{H^2}^2
       \quad\hbox{if }h\in H^2(\mathbb R^N;\mathbb R),\
       \langle h,Q\rangle_{L^2}=0.}                           \tag{4.9}
$$
For clarity, this is physical $L^2$ orthogonality. After conjugation, decompose along the single kernel vector and its orthogonal complement. If unit $H^2$-norm vectors had energy tending to zero, the compact spectral gap forces the complementary component to zero; physical orthogonality then forces the kernel coefficient to vanish as well, a contradiction.

No information about $L_+=\Delta^2+\omega_Q-(2r+1)|Q|^{2r}$ has entered.

## 5. The contradiction for negative-energy traveling waves

Suppose Theorem 1.1 were false. By (1.1), every negative-energy profile has mass strictly greater than $M_c$; hence there would be profiles $U_n$ with
$$
 M(U_n)\downarrow M_c,\qquad E(U_n)<0.
$$
Apply the mass-critical scaling $U\mapsto U_\lambda=\lambda^{N/2}U(\lambda x)$, choosing $\lambda$ so $A(U_n)=1$. The scaled profile still solves (1.2), with frequency $\lambda^4\omega$ and velocity $\lambda^3v$, and energy $\lambda^4E<0$. Thus arbitrary original speeds and frequencies are included.

Sharp GN gives
$$
 0>E(U_n)\ge\frac12\left[1-
             (M(U_n)/M_c)^{\alpha/2}\right]\longrightarrow0,
$$
so $B(U_n)=p/2-pE(U_n)\to p/2$. Lemma 3.1 and the elementary constant-phase theorem (4.2) give, after translations and phase rotations,
$$
 U_n\longrightarrow Q\quad\hbox{strongly in }H^2,
$$
where $Q$ is one of the real optimizers just analyzed. A further phase rotation tending to zero can be chosen so that, writing $U_n=a_n+i b_n$,
$$
 \langle b_n,Q\rangle=0,
 \quad a_n\to Q,\quad b_n\to0\quad\hbox{in }H^2.               \tag{5.1}
$$
Indeed, rotate the complex scalar $\int U_nQ$, which converges to $M_c>0$, to be positive real.

Identity (2.3) now yields
$$
 \omega_nM(U_n)=4/N+(8-p)E(U_n)\longrightarrow4/N,
 \quad\omega_n\longrightarrow\omega_Q.                        \tag{5.2}
$$
Although (2.4) also implies $v_n\to0$, no control of $v_n$ is required for the next step.

Set
$$
 \mathcal A_n=\Delta^2+\omega_n-|U_n|^\alpha.
$$
Its quadratic form converges to that of $L_-$ in operator norm from $H^2$ to $H^{-2}$. Indeed, strong $H^2$ convergence implies strong $L^p$ convergence and therefore
$$
 \||U_n|^\alpha-|Q|^\alpha\|_{p/\alpha}\longrightarrow0
$$
for every $\alpha>0$. Hölder then gives
$$
 \left|\int (|U_n|^\alpha-|Q|^\alpha)h^2\right|
 \le\||U_n|^\alpha-|Q|^\alpha\|_{p/\alpha}\|h\|_p^2
 =o(1)\|h\|_{H^2}^2.
$$
Together with (5.2), this proves the claimed form convergence. Therefore, by (4.9) and (5.1), for all sufficiently large $n$,
$$
 \langle b_n,\mathcal A_n b_n\rangle
       \ge\tfrac12c_Q\|b_n\|_{H^2}^2\ge0.                    \tag{5.3}
$$

The imaginary part of the traveling-wave equation is
$$
 \mathcal A_n b_n=-v_n\cdot\nabla a_n.
$$
Since
$$
 P(U_n)=\int(a_n\nabla b_n-b_n\nabla a_n)
        =-2\int b_n\nabla a_n,
$$
pairing that equation with $b_n$ gives the exact identity
$$
 \langle b_n,\mathcal A_n b_n\rangle
       =\tfrac12v_n\cdot P(U_n)=4E(U_n).
$$
Thus
$$
 \boxed{E(U_n)=\tfrac14\langle b_n,\mathcal A_n b_n\rangle\ge0,}
$$
contradicting $E(U_n)<0$. This proves Theorem 1.1. $\square$

Only the coercivity of the particular subsequential limit $Q$ was needed. One does not need to prove uniqueness of optimizers, or establish a uniform phase gap over their entire set in advance.

## 6. What the theorem says about the main dynamical problem

The obstruction to negative-energy traveling waves close to the ground mass is a positive phase Hessian. Farther away, an excited profile can have a negative phase direction and negative velocity--momentum response; that is consistent with the project construction.

The gap theorem rules out one specific putative mechanism for a dynamical threshold equal to $M_c$: a sequence of negative-energy traveling waves with masses tending to $M_c$. It does not rule out other globally bounded nonlinear behavior near that mass, so it does not prove $m_{\rm ng}>M_c$. Bridging that gap requires a genuine dynamical rigidity theorem, not another profile estimate.

The theorem includes dimension three and all other positive integer dimensions. No spatial radiality assertion is needed for ground optimizers. The elementary phase-kernel argument replaces the earlier even-integer Fourier-positivity proof and removes that limitation.

## 7. Nonperturbative quartic anisotropy

Let $a(\xi)$ be any real homogeneous polynomial of degree four satisfying
$$
 0<c|\xi|^4\le a(\xi)\le C|\xi|^4\quad(\xi\ne0),
$$
and let $a(D)$ be its Fourier multiplier. Its fourth degree makes it even, so it preserves real functions. Define
$$
 A_a(f)=\int a(\xi)|\widehat f(\xi)|^2\,d\xi,
 \qquad E_a(f)=\tfrac12 A_a(f)-\tfrac1p\|f\|_p^p,
$$
and let $M_{c,a}$ be the sharp mass for
$$
 \|f\|_p^p\le\frac p2\left(\frac{M(f)}{M_{c,a}}\right)^{4/N}A_a(f).
$$

**Corollary 7.1.** There is $\varepsilon_{N,a}>0$ such that every nonzero $H^2$ profile
$$
 a(D)U+\omega U+i v\cdot\nabla U-|U|^{8/N}U=0,
 \quad E_a(U)<0,
$$
satisfies $M(U)\ge M_{c,a}+\varepsilon_{N,a}$. No smallness of the anisotropy is assumed.

**Justification.** The form $A_a+M$ is equivalent to the $H^2$ norm; it is real and splits as $A_a(a_1+i a_2)=A_a(a_1)+A_a(a_2)$. All of the GN compactness, constant-phase, second-order kernel, and perturbation arguments therefore remain unchanged. Fourth-order homogeneity gives the same dilation identity $v\cdot P=8E_a$ and the same frequency identity (2.3). To justify dilation at $H^2$, first use the same elliptic bootstrap with the coercive multiplier $a(D)+iv\cdot\nabla+\mu$, which gives $H^4$. Then test stationarity against a compactly supported dilation generator. Integration by parts in the local fourth-order operator produces the homogeneous principal term $4A_a$; terms whose cutoff derivatives do not vanish are supported in the exterior annulus and tend to zero by the $H^2$ tail, or contain an additional negative power of the cutoff radius. The nonlinear term is legitimate since $H^4\subset W^{1,p}$ at the mass-critical power, so $|U|^p\in W^{1,1}$. The imaginary part again gives $E_a(U)=\frac14\langle\operatorname{Im}U,[a(D)+\omega-|U|^{8/N}]\operatorname{Im}U\rangle$. This is exactly the contradiction in Section 5. $\square$

This corollary concerns arbitrary positive quartic dispersion, not an assertion about added lower-order terms or nonlocal symbols. Both homogeneity and the real quadratic form have explicit roles in the proof.

**Historical proof note.** The first version of this argument used Fourier positivity and was therefore formulated only for $N=1,2,4$, where the mass-critical power is an even integer. Sections 4.1--4.4 now replace that route entirely. The former dimension restriction is not a hypothesis of Theorem 1.1 or Corollary 7.1.

## Sources and assumptions

- The sharp Gagliardo--Nirenberg framework and normalized concentration compactness are classical. Their exact uses, including the needed compactness proof, are supplied above.
- A. J. Fernandez, L. Jeanjean, R. Mandel and M. Maris, *Non-homogeneous Gagliardo--Nirenberg inequalities in R^N and application to a biharmonic non-linear Schrödinger equation*, arXiv:2010.01448v3; J. Differential Equations 330 (2022), 1--65. The last paragraph of Proposition 3.8 contains the constant-phase Minkowski-and-rotation argument used in Section 4.1. Primary PDF: https://arxiv.org/pdf/2010.01448.
- E. Lenzmann and J. Sok, *A sharp rearrangement principle in Fourier space and symmetry results for PDEs with arbitrary order*, arXiv:1805.06294v4, Theorem 2, provides a related stronger spatial-symmetry result for even exponents. The present all-dimensional proof does not depend on Fourier rearrangement or claim their radial-symmetry conclusion at noninteger exponents. Primary PDF: https://arxiv.org/pdf/1805.06294.
- The localized fourth-order virial identity used in Section 2 is the standard commutator identity in Boulenger--Lenzmann, *Blowup for biharmonic NLS*, arXiv:1503.01741, and was reproduced in the preceding analytic notes.

The proof is analytic and has no numerical input. The normalized compactness, cutoff identities, and phase-kernel calculation have been independently checked within the present research session. They remain subject to external mathematical review. Novelty of this precise uniform mass-gap statement has not been exhaustively established.
