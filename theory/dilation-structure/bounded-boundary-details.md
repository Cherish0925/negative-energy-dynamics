# Proof details of the saturated same-order boundary

Date: 2026-10-08. Reviewed source: [bounded-boundary-section.tex](../../manuscripts/dilation-structure/bounded-boundary-section.tex) in full.

## Verdict

The stated theorem and its proof close for every dimension $N\ge1$, every principal real-even positive elliptic homogeneous symbol $a$ of order $m>1$ and stated individual smoothness, and every fixed $\varepsilon,q>0$. No change to the theorem is required. 
The added symbol is

$$
b(\xi)=\varepsilon a(\xi)\frac{|\xi|^q}{1+|\xi|^q}.
$$

It obeys the original order-$m$ growth and derivative requirements and $0\le b\le\varepsilon a$, but

$$
mb-\xi\cdot\nabla b
=-\varepsilon q a(\xi)\frac{|\xi|^q}{(1+|\xi|^q)^2}<0
\quad(\xi\ne0).
$$

Therefore this construction, unlike a positive polynomial higher-order term, isolates the upper Euler/dilation sign within the original operator-order class.

## Main checks

1. **Coercivity in the claimed interval.** For $d=(M/M_c)^{m/N}-1\in(0,\varepsilon)$, choose $\eta=(\varepsilon-d)/2$. The bound $b\ge(\varepsilon-\eta)a-C_\eta$ yields

$$
E(f)\ge\frac{\varepsilon-d}{4}A(f)-\frac{C_\eta M}{2}.
$$

Thus minimizing sequences have uniformly bounded $H^{m/2}$ norms at each fixed mass in the open interval. For a general anisotropic symbol, $a(\xi)$ is still bounded on every bounded ball, so the same scalar lower bound applies.

2. **Negative energy.** A principal-negative real smooth trial function exists at every $M>M_c$. Under low-frequency dilation, its principal energy has order $\lambda^m$, whereas its added energy is bounded by $C_f\varepsilon\lambda^{m+q}$. This proves negative infimum throughout the claimed interval and does not presume extra regularity of a principal optimizer.

3. **Strict binding.** The two exact amplitude formulas supply monotonicity of $I(M)/M$ and strictness when the smaller infimum is negative. Every mass split at a mass below the upper endpoint remains within the finite-infimum range. Splits with both pieces below $M_c$ have right-hand energy zero and are also excluded. No continuity theorem for $I$ is missing: normalization of bounded remainder sequences suffices at each positive limiting remainder mass.

4. **Strong same-order compactness.** Local mass vanishing makes the critical nonlinear norm vanish by localized GN. After extraction, Hilbert splitting applies to the $b$ form because $B\le\varepsilon A$. Once binding forces full mass into the weak limit, the residual nonlinear term tends to zero by

$$
\|w_n\|_p^p\le C M(w_n)^{m/N}A(w_n)\longrightarrow0.
$$

Thus criticality of the nonlinearity relative to the highest operator order does not leave a kinetic defect. Energy splitting forces strong $H^{m/2}$ convergence.

5. **Real minimizers.** The component-rescaling convexity proof is correct. It uses real-evenness to split the kinetic form and convexity of $z^{p/2}$ to compare nonlinear terms. It does not use a generally false higher-order inequality for $|f|$.

6. **Frequency and regularity.** The manuscript's identity

$$
\omega M=(1-2/p)\|Q\|_p^p-2E(Q)>0
$$

follows directly from the weak equation and negative energy. The positive resolvent therefore has the required ellipticity and Mihlin estimates. The bootstrap gives $L^\infty$, then $H^m$, then $H^{m+1}$, exactly as claimed, without positivity of the profile or a maximum principle.

7. **Dilation identity.** Scalar differentiation of the constrained energy is justified by the pointwise bound $|\xi\cdot\nabla b|\le(m+q)b\le C a$. With

$$
H(Q)=\varepsilon q\int a(\xi)
\frac{|\xi|^q}{(1+|\xi|^q)^2}|\widehat Q(\xi)|^2\,d\xi>0,
$$

it gives

$$
E(Q)=-\frac{H(Q)}{2m},
\qquad
\omega M=\frac mN(A(Q)+B(Q))
+\frac{1+m/N}{m}H(Q)>0.
$$

The strict sign is valid because a nonzero $L^2$ Fourier transform cannot be supported at the single frequency zero. There is no missing finite-variance or energy-space-generator assumption.

## The unchanged sharp threshold is intrinsic to the modified kinetic form

The constant $M_c$ is also the exact sharp GN critical mass when the denominator uses $A+B$, not merely an arbitrary reference to the principal symbol.

Indeed, define

$$
\mathcal C_b=\sup_{f\ne0}
\frac{\|f\|_p^p}{M(f)^{m/N}[A(f)+B(f)]},
\qquad
\mathcal C_a=\frac p2 M_c^{-m/N}.
$$

Since $B\ge0$, $\mathcal C_b\le\mathcal C_a$. Let $Q$ be a principal sharp optimizer and $Q_\lambda(x)=\lambda^{N/2}Q(\lambda x)$. Dominated convergence gives

$$
\lambda^{-m}B(Q_\lambda)
=\varepsilon\int a(\xi)
\frac{\lambda^q|\xi|^q}{1+\lambda^q|\xi|^q}
|\widehat Q(\xi)|^2\,d\xi\longrightarrow0
$$

as $\lambda\downarrow0$; the domination is simply $\varepsilon a|\widehat Q|^2\in L^1$. The full quotient therefore tends to $\mathcal C_a$, proving equality of the sharp constants. The full inequality is not attained: every nonzero $f$ has $B(f)>0$, so its full quotient is strictly below the corresponding principal quotient, hence strictly below $\mathcal C_a$.

Accordingly the new standing waves approach the genuine sharp critical mass of their own modified energy, even though that full nonhomogeneous sharp inequality has no optimizer.

## Optional upper-threshold fact, with no claim at the endpoint

Let $M_h=(1+\varepsilon)^{N/m}M_c$. For every $M>M_h$, one also has $I(M)=-\infty$. Pick a smooth mass-$M$ trial function with

$$
\frac{1+\varepsilon}{2}A(f)-\frac1p\|f\|_p^p<0,
$$

which exists by the principal sharp GN inequality and smooth approximation. Under high-frequency dilation,

$$
\lambda^{-m}B(f_\lambda)\longrightarrow\varepsilon A(f)
\qquad(\lambda\to\infty)
$$

by dominated convergence. Hence $\lambda^{-m}E(f_\lambda)$ tends to a strictly negative number, and the energy tends to $-\infty$.

Nothing here determines $I(M_h)$, attainment at $M_h$, or finite-time blowup above $M_h$. The main theorem deliberately uses an open upper interval. Within the interval, conservation and the displayed coercivity imply a bounded energy norm for any strong flow having the usual continuation criterion; this is a conditional flow consequence, separate from the explicitly global stationary solutions.
