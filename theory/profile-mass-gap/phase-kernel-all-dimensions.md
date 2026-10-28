# Sharp-GN phase rigidity and the phase kernel in every dimension

Internal proof note, 7 October 2026. This note is independent of radial symmetry,
Fourier rearrangement, positivity of a ground state, and unique continuation.
It does not assert nondegeneracy of the real linearized operator.

## 1. Constant phase of complex sharp-GN optimizers

Let $N\ge1$, $r=4/N$, and $p=2r+2$. Write

$$A(u)=\|\Delta u\|_2^2,\qquad M(u)=\|u\|_2^2.$$

The real and complex sharp constants in

$$\|u\|_p^p\le C_{\rm GN}A(u)M(u)^r$$

are equal. Every nonzero complex optimizer has the form $e^{i\theta}Q$
for a real optimizer $Q$ and a constant $\theta$.

Proof. Put $u=a+ib$, with $a,b$ real, and $\vartheta=2/p\in(0,1)$.
Minkowski in $L^{p/2}$, the real sharp inequality, and two-term Holder give

$$\begin{aligned}
\|u\|_p^2
&=\|a^2+b^2\|_{p/2}\le\|a\|_p^2+\|b\|_p^2\\
&\le C_{\rm real}^{2/p}
\left(A(a)^\vartheta M(a)^{1-\vartheta}
      +A(b)^\vartheta M(b)^{1-\vartheta}\right)\\
&\le C_{\rm real}^{2/p}
\left(A(a)+A(b)\right)^\vartheta
\left(M(a)+M(b)\right)^{1-\vartheta}.
\end{aligned}$$

Here $2r/p=1-2/p$. This proves equality of the constants, since real
functions form a subset of complex functions. If $u$ is an optimizer,
every inequality in this chain is an equality. Unless one component is
zero, strict convexity of $L^{p/2}$ implies $b^2=k^2a^2$ a.e. for $k>0$.
It remains to rule out both signs in $b=\pm ka$.

The rotated function $e^{i\pi/4}u$ is also an optimizer. Its real and
imaginary parts are $(a-b)/\sqrt2$ and $(a+b)/\sqrt2$, whose squares must
again be proportional. If $k\ne1$, their squared ratios on the sets
$b=ka$ and $b=-ka$ are reciprocal and distinct; thus both sets cannot
have positive measure on $\{a\ne0\}$. If $k=1$, the two rotated
components have disjoint supports, which is incompatible with equality
in Minkowski unless one component vanishes. Consequently $b=ka$ a.e.
or $b=-ka$ a.e., proving the assertion.

The constant-phase argument is known. A fully public version of the
Minkowski-plus-rotation proof appears in the last paragraph of Proposition
3.8, pp. 26–27, in A. J. Fernandez, L. Jeanjean, R. Mandel and M. Maris,
*Non-homogeneous Gagliardo-Nirenberg inequalities in R^N and application
to a biharmonic non-linear Schrodinger equation*, arXiv:2010.01448v3,
J. Differential Equations 330 (2022), 1–65,
https://arxiv.org/pdf/2010.01448. Their setting is a positive quadratic
norm and an $L^p$ constraint; the additional Holder step above gives the
homogeneous GN formulation directly. Lenzmann–Sok, arXiv:1805.06294,
Remark 1 following Theorem 2, also states that real-valuedness modulo
phase holds for non-even $p$, separately from the even-$p$ restriction on
their Fourier rearrangement theorem.

## 2. Positivity and exact phase kernel

Let $Q$ be any nonzero real sharp-GN optimizer, normalized in amplitude
so that

$$\|Q\|_p^p=(r+1)A,\quad A=A(Q),\quad M=M(Q),\quad
\omega=\frac{rA}{M},\quad C_{\rm GN}=\frac{r+1}{M^r}.$$

The Euler equation is

$$(\Delta^2+\omega)Q-|Q|^{2r}Q=0.$$

On real $H^2(\mathbb R^N)$ define the continuous quadratic form

$$\mathfrak l_-(b)=\|\Delta b\|_2^2+\omega\|b\|_2^2
 -\int |Q|^{2r}b^2.$$

Then

$$\mathfrak l_-\ge0,\qquad
\ker\mathfrak l_-=\operatorname{span}_{\mathbb R}\{Q\}.$$

The kernel means the form nullspace, equivalently the weak kernel of
$L_-=\Delta^2+\omega-|Q|^{2r}:H^2\to H^{-2}$. Positivity makes these
notions equivalent by the Cauchy–Schwarz inequality for nonnegative
forms.

Proof. For real $b\in H^2$, put $B=\|b\|_2^2$, $C=\|\Delta b\|_2^2$,
and $t=B/M$. Apply the complex sharp inequality to $Q+i\sqrt{s}\,b$:

$$N(s):=\int(Q^2+s b^2)^{r+1}
 \le (r+1)(1+st)^r(A+sC),\qquad s\ge0.\tag{1}$$

The two sides agree at $s=0$. Their one-sided first derivatives exist:
Holder controls $\int |Q|^{2r}b^2$, and the integrand derivatives for
$0\le s\le1$ are bounded by a constant times
$|Q|^{2r}b^2+|b|^{2r+2}$. Comparing derivatives gives

$$\int |Q|^{2r}b^2\le C+\omega B,$$

which proves positivity. If $b$ belongs to the form kernel, equality
holds here, so the two first derivatives in (1) also agree.

For $s>0$ the pointwise convex remainder

$$R_s(x)=\frac{(Q^2+s b^2)^{r+1}-|Q|^{2r+2}
 -(r+1)s|Q|^{2r}b^2}{s^2}$$

is nonnegative. Fatou's lemma and the ordinary scalar expansion of the
right-hand side of (1) imply

$$D:=\int |Q|^{2r-2}b^4
 \le (r-1)A t^2+2Ct.\tag{2}$$

To specify the integrand at zeros of $Q$: if $r<1$, take it to be $+\infty$
where $b\ne0$, and zero where $b=0$; if $r=1$, it is $b^4$; if $r>1$,
it is zero. These are exactly the limits of $2R_s/[r(r+1)]$. In
particular (2) forces $b=0$ a.e. on $\{Q=0\}$ when $r<1$. This argument
requires no classical second differentiability of the integral $N$.

Cauchy–Schwarz, applied to $|Q|^{r+1}$ and $|Q|^{r-1}b^2$, gives

$$\left(C+rAt\right)^2
 =\left(\int |Q|^{2r}b^2\right)^2
 \le(r+1)A D.\tag{3}$$

Combining (2) and (3) yields

$$0\le(r+1)A\big((r-1)At^2+2Ct\big)-(C+rAt)^2
 =-(C-At)^2.$$

Thus $C=At$ and equality holds in (3). Its equality condition gives
$b^2=tQ^2$ a.e. on $\{Q\ne0\}$. Integrating this identity over that set
already accounts for the entire mass $B=tM$, so $b=0$ a.e. on $\{Q=0\}$
also when $r\ge1$. Consequently

$$b^2=tQ^2\text{ a.e.},\qquad C=tA.$$

The Euler equation puts $Q$ in the form kernel. Since that kernel is a
linear space, $b+Q$ belongs to it as well. Apply the same conclusion to
$b+Q$: there is $t'\ge0$ with $(b+Q)^2=t'Q^2$ a.e. Subtracting
$b^2=tQ^2$ gives $2bQ=(t'-t-1)Q^2$, hence
$b=\tfrac12(t'-t-1)Q$ on $\{Q\ne0\}$ and also on its complement.
This proves simplicity without needing the constant-phase result from
Section 1 in the final step. This short polarization observation was
independently supplied by the N3 calculation.

Alternatively, the identities $b^2=tQ^2$ and $C=tA$ show that equality
holds in the sharp GN inequality for $Q+ib$ (indeed for every
$Q+i\sqrt{s}\,b$): its mass and kinetic energy are multiplied by $1+t$,
and its $p$-th power norm by $(1+t)^{r+1}$. Section 1 then also gives
$b\in\operatorname{span}\{Q\}$.

## 3. The resulting coercive gap

For each fixed such $Q$, there is $c_Q>0$ such that

$$\mathfrak l_-(b)\ge c_Q\|b\|_{H^2}^2
\quad\text{whenever } b\in H^2(\mathbb R^N;\mathbb R),\quad
\langle b,Q\rangle_{L^2}=0.$$

Indeed, multiplication by $V=|Q|^{8/N}$ is a compact form perturbation
of $\Delta^2+\omega$ on $H^2$:

* If $N>4$, then $V\in L^{N/4}$ because $Q\in L^2$; approximate $V$
  in that norm by bounded, compactly supported functions and use
  $H^2\hookrightarrow L^{2N/(N-4)}$ and local Rellich compactness.
* If $N=4$, use $V=Q^2\in L^2$ and $H^2\hookrightarrow L^4$ instead.
* If $N<4$, use $Q\in C_0\cap L^\infty$ from the strict Sobolev
  embedding, and approximate $V$ uniformly by compactly supported
  bounded functions.

The free form $\|\Delta b\|_2^2+\omega\|b\|_2^2$ is equivalent to the
$H^2$ norm. A compact perturbation has a positive gap away from its
kernel once it is nonnegative and the kernel is exactly one-dimensional.
More explicitly, a normalized sequence in $Q^\perp$ with form tending
to zero has a weakly convergent subsequence; compactness of the potential
form makes its weak limit a nonzero form-kernel vector, contradicting
orthogonality. This proves the claimed gap.

No dimension-independent numerical lower bound on $c_Q$, no uniformity
over an unnormalized family of optimizers, and no claim about $L_+$ are
included. Uniformity over a compact normalized optimizer family can be
obtained separately by the same contradiction argument.
