# a local-scale bound for the logarithmic matrix field

This is a proved auxiliary estimate. It does not assert a weighted eikonal-defect bound or solve the planar conjecture.

Let K be a strictly positive finite-dimensional Hermitian matrix, let B be Hermitian, and assume

$$
Q_s=s^2I-2sB+K^2\ge bI\qquad(s\in\mathbb R)
$$

for some b>0. Define the symmetric improper matrix integral

$$
N=\frac1{2\pi}\int_\mathbb R[\log Q_s-\log(s^2)I]ds,
$$

and suppose N>=0. The field is the sigma=1/2, zero-regularization version of the field in Sections 3–4 of OpenAI, *Sharp one-dimensional Lieb–Thirring inequalities for matrix potentials* (October 5, 2026), https://www.emergentmind.com/openai-math-explorer/papers/526.pdf?v=adc7f12 . The estimate below is a derivation from its logarithmic representation, not a theorem attributed to that paper.

In an eigenbasis K=diag(k_i),

$$
\boxed{\quad
(K-N)_{ii}\ge\sum_j|B_{ij}|^2
\frac{2(k_i+2k_j)}{3(k_i+k_j)^2},\qquad
\sum_j\frac{|B_{ij}|^2}{k_i+k_j}\le\frac32 k_i.
\quad}\tag{1}
$$

The proof also gives K-N>=0 as an operator. The strict pencil assumption may be weakened by passage to a convergent limit; such a passage must preserve the stated matrix logarithm integral and N>=0.

**Proof.** Put A_s=s^2I+K^2 and X_s=2sB. Symmetrizing in s and using the scalar logarithmic integral on each eigenspace of K gives

$$
K-N=\frac1{2\pi}\int_\mathbb R
\left[\log A_s-\frac{\log(A_s+X_s)+\log(A_s-X_s)}2\right]ds.
$$

For positive A plus/minus X, the resolvent formula for log and the substitution Y=(A+t)^(-1/2)X(A+t)^(-1/2) give

$$
\begin{aligned}
\log A-\tfrac12\log(A+X)-\tfrac12\log(A-X)
&=\int_0^\infty(A+t)^{-1/2}Y^2(I-Y^2)^{-1}(A+t)^{-1/2}dt\\
&\ge\int_0^\infty(A+t)^{-1}X(A+t)^{-1}X(A+t)^{-1}dt.
\end{aligned}
$$

Here ||Y||<1, and Y^2 commutes with (I-Y^2)^(-1), so the displayed inequality is an operator inequality. Its integrand is positive semidefinite. Tonelli can therefore be applied to each quadratic form. The i-th diagonal entry yields

$$
(K-N)_{ii}\ge\sum_j|B_{ij}|^2\frac2\pi
\int_0^\infty\int_\mathbb R
\frac{s^2\,ds\,dt}{(s^2+k_i^2+t)^2(s^2+k_j^2+t)}.
$$

For a,b>0,

$$
\int_\mathbb R\frac{s^2\,ds}{(s^2+a^2)^2(s^2+b^2)}
=\frac\pi{2a(a+b)^2}.
$$

Consequently the coefficient is

$$
\int_0^\infty\frac{dt}{\sqrt{k_i^2+t}(\sqrt{k_i^2+t}+\sqrt{k_j^2+t})^2}
=\frac{2(k_i+2k_j)}{3(k_i+k_j)^2}.
$$

For the last equality set u=sqrt(k_i^2+t)+sqrt(k_j^2+t). The integrand times dt becomes [u^(-2)-(k_i^2-k_j^2)u^(-4)]du, with lower endpoint k_i+k_j. This verifies the constant also when the eigenvalues coincide.

Finally N>=0 implies (K-N)_ii<=k_i. The coefficient is at least 2/[3(k_i+k_j)], proving the second inequality in (1).

The bound controls weighted row sums of B. It does not imply B^2<=K^2. It also does not alone control the weighted error sum_ij |(K^2-B^2-N^2)_ij|^2/(k_i+k_j); that stronger assertion remains a separate question.
