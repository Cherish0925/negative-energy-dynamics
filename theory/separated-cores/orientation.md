# the rank-two orientation problem

Status: exact reformulations and inequalities, with explicit obstructions to two proposed shortcuts. No proof of the sharp rank-two Lieb–Thirring constant, and no claim of historical priority for the elementary deductions below.

## 1. Exact decomposition, with its domain stated

Let $\phi_1,\phi_2\in H^1(\mathbb R^2;\mathbb R)$ be orthonormal. Write
$$
r=\sqrt{\phi_1^2+\phi_2^2},\qquad \rho=r^2,\qquad
z=(\phi_1+i\phi_2)/r\quad\text{on }\{r>0\}.
$$
Then $|z|=1$, $\int\rho=2$, and orthonormality is exactly
$$
\int\rho z^2=0.
$$
The kinetic energy splits as
$$
T=\sum_{j=1}^2\int|\nabla\phi_j|^2
=A+J,\qquad A=\int|\nabla r|^2,\qquad
J=\int_{\{r>0\}}\rho|\nabla z|^2.
\tag{1}
$$
The identity follows from $\operatorname{Re}(\bar z\nabla z)=0$. For general Sobolev orbitals it is understood on $\{r>0\}$, by approximation or the Sobolev chain rule. One must not assume a global phase lift $z=e^{i\theta}$: zeros and winding can obstruct it. Locally, $J=\int\rho|\nabla\theta|^2$.

For fixed $r$, define
$$
\mathcal J[\rho]=\inf\left\{\int\rho|\nabla z|^2:
 |z|=1,\ \int\rho z^2=0,\ rz\in H^1\right\}.
$$
With $C_1=2/M_c$, the desired rank-two theorem is **equivalent** to
$$
\boxed{\mathcal J[\rho]\ge C_1^{-1}\int\rho^2-\int|\nabla\sqrt\rho|^2}
\tag{2}
$$
for every admissible mass-two density. The right side may be negative. This is not a new theorem: it relocates the unresolved orthogonality cost into a nonlinear weighted circle-map problem. Omitting the pointwise condition $|z|=1$ changes that problem substantially.

## 2. A basis-invariant strengthening of the Haar bound

Set
$$
F=\int\rho^2,\qquad B=\int(\phi_1+i\phi_2)^4
=\int\rho^2z^4.
$$
For every constant rotation $O_\alpha$, the two rotated functions remain normalized and orthogonal. Applying the sharp scalar inequality separately gives
$$
\int(O_\alpha\Phi)_1^4+\int(O_\alpha\Phi)_2^4\le C_1T.
$$
Using $\cos^4 s+\sin^4 s=(3+\cos4s)/4$ and maximizing over $\alpha$ proves
$$
\boxed{3F+|B|\le4C_1T.}\tag{3}
$$
Both $F$ and $|B|$ are invariant under orthogonal changes of the occupied basis (a reflection conjugates $B$). Equivalently,
$$
F\le C_1T+2\min_{O\in O(2)}\int(O\Phi)_1^2(O\Phi)_2^2,
\qquad
\min_O\int(O\Phi)_1^2(O\Phi)_2^2=\frac{F-|B|}{8}.
\tag{4}
$$
Thus the usual $C_2\le4C_1/3$ bound discards a nonnegative, observable fourth angular moment. Separated cores have $|B|/F\to1$, and (3) approaches the conjectured constant there. A putative quotient $F/T=(1+\delta)C_1$ must satisfy
$$
\frac{|B|}{F}\le\frac{1-3\delta}{1+\delta}.
$$
This does **not** improve the uniform factor $4/3$: take a smooth annular radial amplitude $r$ and $z=e^{ik\arg x}$, $k\ne0$, normalized to mass two. Both $\int\rho z^2$ and $B$ vanish. The annulus avoids the origin, so all functions are smooth and there is no vortex regularity issue. Such a family need not be a maximizing spectral subspace; it is enough to rule out a universal positive lower bound on $|B|/F$ from orthogonality alone.

## 3. Ground-state geometry of an actual rank-two optimizer

For a real rank-two optimizer one may choose eigenfunctions of the common scalar Schrödinger operator, with
$$
H=-\Delta-k\rho,\quad H\phi_j=\lambda_j\phi_j,
\quad k=2/C_2,\quad\lambda_1<\lambda_2<0.
$$
The first eigenfunction is strictly positive. Consequently $r>0$ and the specific eigenbasis admits the global phase
$\theta=\arctan(\phi_2/\phi_1)\in(-\pi/2,\pi/2)$.
Let $\omega=\lambda_2-\lambda_1>0$. Resolving the eigenfunction equation along and perpendicular to $(\cos\theta,\sin\theta)$ gives
$$
-\Delta r+r|\nabla\theta|^2-kr^3
=(\lambda_1\cos^2\theta+\lambda_2\sin^2\theta)r,
\tag{5}
$$
$$
-\operatorname{div}(\rho\nabla\theta)
=\omega\rho\sin\theta\cos\theta.
\tag{6}
$$
The ground-state transform with $f=\phi_2/\phi_1=\tan\theta$ yields
$$
\int\phi_1^2|\nabla f|^2=\omega,
\quad\text{hence}\quad
\boxed{\int\rho\sec^2\theta|\nabla\theta|^2=\omega,\qquad J\le\omega.}
\tag{7}
$$
Equation (7) is exact, but is an *upper* bound for the orientation cost; it does not prove (2). A formal multiplication of (6) by an unbounded $\tan\theta$ should be replaced by the ground-state quadratic-form identity or truncation. Positivity of the first eigenfunction justifies a global lift here; it does not justify imposing one on every test family.

## 4. Weighted spectral gaps: valid lower bounds and a counterexample to sufficiency

Let $\lambda_\rho$ denote the spectral gap of the weighted form $\int\rho|\nabla f|^2$ on $L^2(\rho dx)$. The two real components $n=(\operatorname{Re}z,\operatorname{Im}z)$ are orthonormal in that space. The min-max principle, including its constant ground state, gives
$$
J\ge\lambda_\rho.
\tag{8}
$$
Directly: weighted Poincaré and Bessel give
$$
J\ge\lambda_\rho\left(2-\frac{|\int\rho n|^2}{2}\right)
\ge\lambda_\rho,
$$
since $|\int\rho n|^2=\sum_j|\langle r,\phi_j\rangle|^2\le2$.
Using only the mean-zero map $z^2$ would give the weaker bound $J\ge\lambda_\rho/2$.

It is false that the replacement $J\rightsquigarrow\lambda_\rho$ is sufficient in (2). Let $q$ be a smooth compactly supported, normalized scalar near-optimizer. Take two disjointly supported translates/scalings and put
$$
\rho=mq(x)^2+(2-m)\varepsilon^2q(\varepsilon(x-a))^2,
\qquad1<m<2.
$$
For disjoint supports $\lambda_\rho=0$, whereas
$$
A=[m+(2-m)\varepsilon^2]T_q,\quad
F=[m^2+(2-m)^2\varepsilon^2]F_q.
$$
Choose the near-optimizer so $F_q/(C_1T_q)>1/m$, then choose $\varepsilon$ small. This gives $F>C_1(A+\lambda_\rho)$. Smooth positive bridges make the spectral gap arbitrarily small and retain the strict failure. The density itself is admissible for some orientation: on each compact component, a smooth cumulative mass coordinate can wind $z^2$ once around the circle, making its mean zero with finite energy. The low global gap detects the remote weak well; it fails to charge the substantial orientation variation required inside the well of mass $m>1$.

Nor is $J\ge A$ valid: two disjoint normalized real orbitals have $J=0$ and $A>0$. Arbitrarily small positive bridges give the same limiting obstruction. No topological lower bound independent of $\rho$ can repair this, because orientation changes may be placed where the density is tiny.

## 5. The local occupation constraint retains the missing information

For any region $D$, write
$$
m_D=\int_D\rho,\qquad M_D=\int_D\rho nn^T.
$$
Global orthogonality implies $0\le M_D\le I$, not merely $\operatorname{Tr}M_D=m_D$. If $\lambda_{\rho,D}$ is the weighted Neumann gap on $D$, then
$$
\boxed{\int_D\rho|\nabla n|^2\ge
\lambda_{\rho,D}(m_D-1)_+.}\tag{9}
$$
Proof: write $v_D=\int_D\rho n$. Cauchy–Schwarz in the direction $v_D$ yields $|v_D|^2/m_D\le\|M_D\|\le1$. Weighted Poincaré gives the result. Summing over a partition gives a lower bound charging each cell with occupation exceeding one. In the unequal-well counterexample above, the strong core incurs a positive local cost even though the global gap tends to zero.

This is a density-weighted version of the established local exclusion principle, not a new physical principle. It does not produce the sharp Townes constant by itself: one still needs a sharp way to combine local exclusion with the amplitude gradient, without losses from the partition and local interpolation.

## 6. Why two-dimensional conformal invariance does not remove the problem

The unweighted Dirichlet energy is conformally invariant in two dimensions. The relevant energy is weighted. If $x=G(y)$ is conformal with local scale $s$ and the density is transported to preserve mass, then
$$
\widetilde\rho(y)=\rho(G(y))s(y)^2,
\quad\widetilde\theta(y)=\theta(G(y)),
$$
and
$$
\int\widetilde\rho|\nabla_y\widetilde\theta|^2dy
=\int\rho(x)s(G^{-1}x)^2|\nabla_x\theta|^2dx.
$$
It is not invariant. Transport flattening also changes the metric and the amplitude-gradient energy. Therefore neither a conformal change nor a mass-uniformizing transport is an immediate reduction to an unweighted circle-map inequality.

## 7. What this route has and has not achieved

The exact unresolved statement is (2). Formula (3) quantifies the improvement that ordinary scalar projections see; (9) identifies the occupation information needed to avoid the false spectral-gap shortcut. Neither formula establishes a new uniform upper bound for $C_2$, nor proves that a rank-two optimizer is unstable. The self-consistent equations (5)–(7) distinguish spectral optimizers from general orientation fields, but an inequality using them strongly enough to prove (2) is still missing.

Primary references checked:

1. Frank, Gontier, Lewin, *The Nonlinear Schrödinger Equation for Orthonormal Functions II: Application to Lieb–Thirring Inequalities*, Communications in Mathematical Physics (2021), DOI 10.1007/s00220-021-04039-5. Its strict rank-two improvement theorem applies in dimension two to $\gamma>1$, not to the endpoint $\gamma=1$. https://link.springer.com/article/10.1007/s00220-021-04039-5
2. Nam, *A Proof of the Lieb–Thirring Inequality via the Besicovitch Covering Lemma*, Acta Mathematica Vietnamica (2023), DOI 10.1007/s40306-022-00490-1. The local exclusion / uncertainty route and its prior history are explicit there. https://link.springer.com/article/10.1007/s40306-022-00490-1

