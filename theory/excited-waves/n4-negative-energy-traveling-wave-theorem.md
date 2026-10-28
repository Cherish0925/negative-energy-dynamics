# A precise four-dimensional route from a negative inverse pairing to a global negative-energy wave

Date: 2026-10-07. This is a proved conditional theorem and explicit sufficient certification framework. The supplied numerical candidate is not promoted to an exact solution by this note.

## 1. Equation and normalizations

Consider

$$
 i\partial_tu=\Delta^2u-|u|^2u,\qquad (t,x)\in\mathbb R\times\mathbb R^4.
$$

Set

$$
 M(u)=\|u\|_2^2,\quad K(u)=\|\Delta u\|_2^2,\quad
 E(u)=\frac12K(u)-\frac14\|u\|_4^4,\quad
 P(u)=\operatorname{Im}\int\overline u\nabla u.
$$

The nonlinearity is cubic, and this is exactly the mass-critical exponent 8/N=2 in N=4. A profile Q_v moving with velocity v e_1 and frequency 1 solves

$$
 \mathcal F(v,Q_v):=\Delta^2Q_v+Q_v+i v\partial_1Q_v-|Q_v|^2Q_v=0.\tag{1}
$$

It generates the exact solution

$$
 u_v(t,x)=e^{it}Q_v(x-vte_1).\tag{2}
$$

The relevant profile action is

$$
 S_v(f)=E(f)+\frac12M(f)-\frac v2P_1(f).
$$

The mass-preserving Pohozaev identity for (1) is

$$
 E(Q_v)=\frac v8P_1(Q_v).\tag{3}
$$

It follows by testing the stationary equation against cutoff versions of 2Q_v+x dot grad Q_v and passing to infinity. Kinetic, quartic, and momentum contributions tend respectively to 2K, -||Q_v||_4^4, and -vP_1/2; the mass contribution tends to zero. H^4 regularity and integrability of these densities make the cutoff remainders vanish. This avoids assuming a finite spatial moment merely to justify dilation differentiation.

At v=0, multiplication by Q and (3) give the useful exact diagnostics

$$
 K(Q)=M(Q),\qquad \|Q\|_4^4=2M(Q),\qquad E(Q)=0.\tag{4}
$$

## 2. Symmetry space and theorem

Write x=(s,y) in R times R^3. Define a closed real-linear subspace X of H^4(R^4;C) by

$$
 f(s,Ay)=f(s,y)\quad(A\in O(3)),\qquad
 f(-s,y)=\overline{f(s,y)}.\tag{5}
$$

Thus the real part is axially symmetric and even in s, and the imaginary part is axially symmetric and odd in s. Let Y be the corresponding closed subspace of L^2. Equation (1) preserves these symmetries.

**Theorem.** Let Q be a real nonzero radial H^4(R^4) solution of

$$
 \Delta^2Q+Q-Q^3=0.
$$

Define self-adjoint operators on their natural H^4 domains,

$$
 L_+=\Delta^2+1-3Q^2,\qquad L_-=\Delta^2+1-Q^2.
$$

Assume:

1. L_+ is invertible on real O(3)-invariant functions even in s.
2. L_- is invertible on real O(3)-invariant functions odd in s.
3. With g=partial_1 Q and z=L_-^{-1}g in the odd sector,
   $$
   I=\langle g,z\rangle_{L^2(\mathbb R^4)}<0.\tag{6}
   $$

Then there is epsilon>0 and a real-analytic branch v mapsto Q_v in X for |v|<epsilon satisfying (1), Q_0=Q, and

$$
 Q_v=Q-i v z+O_{H^4}(v^2),\qquad
 P_1(Q_v)=2Iv+O(v^3),\qquad
 E(Q_v)=\frac I4v^2+O(v^4).\tag{7}
$$

In particular, every sufficiently small nonzero v gives E(Q_v)<0. The solution (2) exists for all positive and negative times and has a constant finite H^2 norm. It is therefore a counterexample to the assertion that every negative-energy nonradial H^2 solution must blow up in finite time, in dimension four.

**Proof.** H^4(R^4) embeds into L-infinity and is a Banach algebra. Consequently the polynomial map f mapsto |f|^2f is real analytic from H^4 to L^2. The map F:R times X to Y is real analytic. At (0,Q), its derivative in the profile variable is block diagonal: L_+ acts on the real even component and L_- on the imaginary odd component. Assumptions 1-2 make this derivative an isomorphism, so the Banach-space implicit-function theorem gives the unique local analytic branch.

Differentiating F(v,Q_v)=0 at zero gives L_- Im(Q'_0)=-partial_1Q, while the real derivative is zero. Hence Q'_0=-i z. Direct differentiation of momentum, followed by integration by parts, gives

$$
 \left.\frac d{dv}P_1(Q_v)\right|_{v=0}
 =\int(z\partial_1Q-Q\partial_1z)=2\langle\partial_1Q,z\rangle.
$$

Conjugation maps the equation with v to the equation with -v and preserves X; local uniqueness therefore gives Q_{-v}=bar Q_v. Momentum is odd in v and energy is even. This proves the first two expansions in (7), and (3) yields the energy expansion. Translation and multiplication by a constant phase preserve H^2 norm, proving the final claim. No orbital or spectral stability assumption is needed.

## 3. Why the symmetry restriction removes the unavoidable kernels

For a radial stationary Q, the phase kernel of L_- is Q, which is even in s and is excluded from the imaginary odd sector. The longitudinal translation kernel partial_1Q of L_+ is odd in s and is excluded from the real even sector. Transverse translations partial_{y_j}Q are not O(3)-invariant. Rotating a radial function gives the zero variation, so there are no additional rotational kernel vectors generated from Q.

This removes the symmetry-generated kernels only. Additional accidental zero eigenvalues for an excited state still have to be ruled out. Assuming nondegeneracy solely because the numerical BVP solver converged would leave a genuine gap.

## 4. Angular reduction makes the remaining spectral obligations finite

For a radial potential in R^4, separate into spherical harmonic degree ell. The angular eigenvalue is

$$
 \lambda_\ell=\ell(\ell+2),\qquad
 A_\ell=\partial_r^2+\frac3r\partial_r-\frac{\lambda_\ell}{r^2}.
$$

In the O(3)-invariant subspace there is one zonal harmonic for each ell, with parity (-1)^ell under s mapsto -s. The radial operators are

$$
 L_{c,\ell}=A_\ell^2+1-cQ(r)^2,
 \qquad c=3\ \text{for }L_+,\quad c=1\ \text{for }L_-.
$$

Thus check only:

- L_{3,ell} for even ell=0,2,4,...;
- L_{1,ell} for odd ell=1,3,5,... .

The source g=Q'(r)s/r lies entirely in ell=1. If z(x)=Z(r)s/r, then

$$
 (A_1^2+1-Q^2)Z=Q',\qquad
 I=\frac{|S^3|}{4}\int_0^\infty Q'(r)Z(r)r^3dr
 =\frac{\pi^2}{2}\int_0^\infty Q'Zr^3dr.\tag{8}
$$

Normalization matters: the one-dimensional radial integral alone differs from the full Cartesian inner product by pi^2/2.

### Explicit high-angular-momentum exclusion

For ell>=1 and regular radial coefficient f, integration by parts gives

$$
 \int_0^\infty r^3|A_\ell f|^2dr
 =\int r^3|A_0 f|^2dr
 +2\lambda_\ell\int r|f'|^2dr
 +\lambda_\ell^2\int r^{-1}|f|^2dr
 \ge\lambda_\ell^2\int r^{-1}|f|^2dr.\tag{9}
$$

The boundary term vanishes because a smooth ell>=1 mode has f(0)=0; the identity extends by density to the form domain. If B=sup_{r>0} r^4Q(r)^2 is finite, then

$$
 \lambda_\ell^2\ge cB\quad\Longrightarrow\quad L_{c,\ell}\ge1.\tag{10}
$$

Only finitely many low ell remain. Their negative eigenvalues are allowed; only zero must be excluded. It is enough to bound the distance of their spectra from zero strictly below, with rigorous control of the infinite radial domain.

One can avoid an independently weighted error estimate for the exact profile. If a validated approximation q satisfies ||Q-q||_infinity<=delta and B_q=sup r^4 q^2 is known, then Q^2<=2q^2+2delta^2. Therefore

$$
 \lambda_\ell^2\ge2cB_q\quad\Longrightarrow\quad
 L_{c,\ell}\ge1-2c\delta^2.\tag{11}
$$

For delta^2<1/(2c), this still proves positivity for all sufficiently large ell. A compactly supported smooth q makes B_q elementary to enclose.

## 5. Explicit sufficient validation bounds

These are sufficient, not claimed optimal. They are included to make the proof obligations concrete.

Use the equivalent H^4 norm

$$
 \|h\|_X=\|(\Delta^2+1)h\|_2.
$$

With the unitary Fourier transform on R^4,

$$
 \|h\|_\infty\le S\|h\|_X,\qquad
 S=\frac1{4\sqrt2\pi},\qquad
 \|\partial_1h\|_2\le G\|h\|_X,\quad
 G=\frac{3^{3/4}}4.\tag{12}
$$

The first constant follows from
$\int_{\mathbb R^4}(1+|\xi|^4)^{-2}d\xi=\pi^2/2$.
The second follows from maximizing r/(1+r^4). Also ||h||_2<=||h||_X.

### Exact stationary profile near a numerical q

Let q be a real smooth radial approximation, eta=||Delta^2q+q-q^3||_2, and m=||q||_infinity. Suppose L_q=Delta^2+1-3q^2 is invertible on the radial sector with

$$
 \|L_q^{-1}\|_{L^2\to X}\le C.
$$

If rho>0 satisfies

$$
 C\eta+C(3mS\rho^2+S^2\rho^3)\le\rho,
 \qquad C(6mS\rho+3S^2\rho^2)<1,\tag{13}
$$

then contraction mapping gives an exact radial Q with ||Q-q||_X<=rho. Indeed the correction h solves

$$
 h=-L_q^{-1}(\Delta^2q+q-q^3)+L_q^{-1}(3qh^2+h^3).
$$

If a radial L^2 spectral gap dist(0,spec L_q)>=gamma_0 is known, a valid conversion is

$$
 C\le1+\frac{3m^2}{\gamma_0},\tag{14}
$$

since (Delta^2+1)h=L_q h+3q^2h.

### Transfer the finite angular spectral gaps

Set delta=S rho. Then for c=1 or3,

$$
 \|c(Q^2-q^2)\|_\infty\le d_c:=c\delta(2m+\delta).\tag{15}
$$

If the corresponding approximate low-mode operator A_ell^2+1-cq^2 has spectral distance from zero at least gamma_{c,ell}>d_c, its exact-Q counterpart has distance at least gamma_{c,ell}-d_c. Together with (11), this proves the full two sector invertibilities in the theorem.

### Certify the negative inverse pairing

Let g_0=partial_1q, let z_0 be an approximate solution in the ell=1 sector, and set

$$
 \eta_z=\|(\Delta^2+1-q^2)z_0-g_0\|_2,\quad
 \delta_g=G\rho,\quad I_0=\langle g_0,z_0\rangle.
$$

Let gamma>0 be a certified exact-Q ell=1 L_- spectral distance from zero. Then

$$
 |I-I_0|\le\delta_g\|z_0\|_2
 +\frac{\|g_0\|_2+\delta_g}{\gamma}
 \bigl(\eta_z+d_1\|z_0\|_2+\delta_g\bigr).\tag{16}
$$

This follows by writing the exact residual of z_0, using the inverse norm gamma^-1, and splitting the two inner-product errors. An upper enclosure for I_0 plus the right-hand side strictly below zero validates assumption 3.

All radial norms in these formulas must include their full R^4 angular factors, or all constants must be rescaled consistently. A small BVP collocation residual at mesh nodes is not eta in (13): eta requires an actual L^2 residual enclosure, including interpolation and the unbounded tail.

## 6. Analytic existence versus the particular excited candidate

The action J(q)=1/2(||Delta q||_2^2+||q||_2^2)-1/4||q||_4^4 on H^2_rad(R^4) is even and superquadratic. The radial embedding into L^4 is compact. Its Palais-Smale condition follows from

$$
 J(q)-\tfrac14J'(q)[q]=\tfrac14\|q\|_{H}^2,
 \quad \|q\|_H^2=\|\Delta q\|_2^2+\|q\|_2^2,
$$

followed by compact L^4 convergence. The usual symmetric mountain-pass/fountain argument therefore produces infinitely many radial stationary critical points with unbounded action. Elliptic bootstrap gives H^4 regularity; symmetric criticality gives the full PDE. This supplies an analytic abundance of stationary radial states. It does not identify a particular numerically computed profile, prove its nondegeneracy, or determine the sign of I.

A focused primary-source search did not produce a general nondegeneracy theorem for excited radial solutions of Delta^2Q+Q-Q^3=0 in dimension four. Pimenta's *Radial sign-changing solutions to biharmonic nonlinear Schrödinger equations* (Boundary Value Problems 2015, DOI 10.1186/s13661-015-0282-z; https://link.springer.com/article/10.1186/s13661-015-0282-z, web ref ) states its main setting in N>=5 and does not provide the needed excited-state spectral nondegeneracy. It cannot replace the checks above.

## 7. Status of the reported candidate

The radial audit reports a dimension-four cubic excited candidate with numerical I approximately -273.47 and mass approximately 5317.79, stored as round2_radial_mode1_dim4.npz. Those floating-point values are not interval certificates. If profile, spectral, and sign enclosures (13)-(16) are completed, the theorem yields an exact counterexample to the original universal claim. Until then, the result is a substantial numerical candidate together with a complete conditional analytic conversion, not a proved disproof.

## 8. Improved energy-space validation: modest residuals are sufficient

This addendum gives a substantially better certification route than the H4 estimates of Section 5. The numerical values below are **sufficient target inequalities**, not an assertion that all their hypotheses have already been certified. In particular, Birman–Schwinger integral/eigenvalue enclosures remain indispensable.

### 8.1 Norms and explicit constants

Put A=Delta^2+1 and

$$
 \|h\|_Z=\|A^{1/2}h\|_2=(\|\Delta h\|_2^2+\|h\|_2^2)^{1/2},
 \qquad \|f\|_{Z^*}=\|A^{-1/2}f\|_2.
$$

The following dimension-four inequalities hold:

$$
 \|h\|_4\le C_4\|h\|_Z,\qquad
 C_4^2=\frac{\sqrt6}{16\pi},\qquad
 \alpha:=C_4^4=\frac3{128\pi^2},
$$

$$
 \|\partial_1h\|_{Z^*}\le G\|h\|_Z,
 \qquad G=\frac{3^{3/4}}4.
$$

For the first inequality use the sharp R4 Sobolev inequality
$\|h\|_4^2\le\sqrt6\,\|\nabla h\|_2^2/(8\pi)$
and $2\|\nabla h\|_2^2\le\|\Delta h\|_2^2+\|h\|_2^2$.
For the second maximize $r/(1+r^4)$ in Fourier space. Consequently,

$$
 \|fgh\|_{Z^*}\le\alpha\|f\|_Z\|g\|_Z\|h\|_Z.\tag{17}
$$

A weak stationary solution Q in Z is automatically in H4: H2(R4) embeds continuously into L6, so Q^3 belongs to L2 and AQ=Q^3 implies H4. Hence obtaining Q by an H2 contraction suffices for the H4 implicit-function theorem in Section 2.

### 8.2 Birman–Schwinger inverse and exact stationary profile

For the compactly supported bounded real approximation q, set

$$
 K_{c,q}=A^{-1/2}(c q^2)A^{-1/2},\qquad B_{c,q}=I-K_{c,q}.
$$

Restrict to any indicated angular sector. K is positive and compact. Its nonzero eigenvalues agree, including multiplicity, with those of $cM_qA^{-1}M_q$; replacing q by |q| gives a unitarily equivalent nonzero spectrum. If

$$
 \operatorname{dist}(1,\operatorname{spec}K_{c,q})\ge\gamma>0,
$$

then $L_{c,q}=A-cq^2$ has inverse $Z^*\to Z$ of norm at most $\gamma^{-1}$. This is the factorization $L=A^{1/2}BA^{1/2}$. There is no multiplication by the large factor $\|q\|_\infty^2$.

Let $m\ge\|q\|_Z$, $\eta\ge\|Aq-q^3\|_{Z^*}$, and let $\gamma_R$ be a certified c=3 radial-sector BS gap. An L2 residual upper bound is also a valid eta. For a proposed radius rho, the two conditions

$$
 \frac{\eta+\alpha(3m\rho^2+\rho^3)}{\gamma_R}\le\rho,
 \qquad
 \frac{\alpha(6m\rho+3\rho^2)}{\gamma_R}<1 \tag{18}
$$

prove existence and uniqueness in that correction ball of a real radial exact Q with $\|Q-q\|_Z\le\rho$. This follows from the same correction equation as Section 5, using (17).

For every angular sector, the exact-Q BS perturbation is bounded by

$$
 \|K_{c,Q}-K_{c,q}\|\le d_c:=c\alpha(2m\rho+\rho^2).\tag{19}
$$

Indeed, for unit Z test vectors h,k, apply Holder to
$\int c(Q-q)(Q+q)hk$. Thus any q-sector gap exceeding d_c persists for Q. This form estimate avoids an H2-to-L-infinity claim, which would be false in dimension four.

### 8.3 Five sector certificates suffice

Let $\mu_1\ge\mu_2\ge\cdots\ge0$ be the BS eigenvalues, and H an upper bound on its Hilbert–Schmidt norm squared. If Ritz/minmax certificates give $\mu_j\ge a_j>1$ for j=1,...,k, then

$$
 \mu_{k+1}^2\le H-\sum_{j=1}^k a_j^2.
$$

If the right side is less than 1, this isolates all eigenvalues above 1 and gives gap
$\min\{a_k-1,1-\sqrt{H-\sum a_j^2}\}$.
A trace upper bound T may instead be used to give
$\mu_{k+1}\le T-\sum a_j$.
Numerical quadrature or floating eigenvalues alone are not such certificates.

The following deliberately loose bounds suffice:

| Sector | Required certified q-BS bounds | Implied gap from 1 |
|---|---|---|
| c=3, ell=0 | mu1 >= 5.395, mu2 >= 2.999, HS squared <= 39 | > 0.0513304; use 0.05 |
| c=3, ell=2 | mu1 >= 2.11, HS squared <= 4.8 | > 0.410 |
| c=3, ell=4 | HS squared <= 0.73 | > 0.145 |
| c=1, ell=1 | mu1 >= 1.04, trace <= 1.70 | >= 0.04 |
| c=1, ell=3 | HS squared <= 0.22 | > 0.530 |

For ell0, the remainder is exactly at most
$39-5.395^2-2.999^2=0.899974$, yielding the stated gap. For ell2 it is at most 0.3479. For ell1 the remaining trace is at most 0.66.

The ell4 and ell3 bounds cover all higher relevant angular degrees. Identity (9) proves monotonicity of the kinetic forms as lambda_ell increases, on their common form core for ell>=1 and then by closure. Therefore the largest BS eigenvalue for a fixed potential cannot increase with ell, by its variational quotient
$c\int q^2|f|^2/\langle f,A_\ell f\rangle$, where here A_ell denotes the positive fourth-order kinetic-plus-one operator. This avoids confusing that positive operator with the second-order radial Laplacian denoted A_ell earlier in the note. First transfer (19) at ell4 and ell3 to Q; their positivity then holds for every higher relevant ell by the same monotonicity.

These five certificates plus (18)-(19) prove both full symmetry-sector invertibilities required in Section 2. Since Q is H4 and bounded, the Z inverse also gives the bounded H4-to-L2 operator inverse needed by the analytic implicit-function theorem: if Lh=f in L2 and h in Z, then Ah=f+cQ^2h belongs to L2.

### 8.4 Negative inverse pairing via a quadratic residual identity

Let psi be any real trial response in the ell1 sector and write

$$
 g_q=\partial_1q,\quad
 J_q=2\langle g_q,\psi\rangle-\langle\psi,(A-q^2)\psi\rangle,
 \quad
 \eta_\psi\ge\|(A-q^2)\psi-g_q\|_{Z^*}.
$$

For exact Q set $g=\partial_1Q$, $L=A-Q^2$, and $r=g-L\psi$. A direct expansion gives the exact identity

$$
 I=\langle g,L^{-1}g\rangle
 =J_Q+\langle r,L^{-1}r\rangle.\tag{20}
$$

This holds even though L is indefinite. If $b\ge\|\psi\|_Z$, and the q ell1 BS gap is $\gamma_-$, then (19) yields the upper bound

$$
 I\le J_q+2G\rho b+d_1b^2
 +\frac{(\eta_\psi+d_1b+G\rho)^2}{\gamma_--d_1},
 \qquad d_1<\gamma_-.\tag{21}
$$

All full-space angular factors must be included. The terms respectively bound the source perturbation in J, potential perturbation in J, and quadratic residual correction. One may improve (21) by a one-sided spectral bound on the positive part of L inverse, but that additional bound is not assumed here.

### 8.5 Concrete conservative certificate with the refined canonical q

Suppose all quantities below are rigorously enclosed for the **same** exact rational compact approximation q and trial psi:

$$
 \|q\|_Z\le104,\quad \|\psi\|_Z\le132,
 \quad\|Aq-q^3\|_2\le0.000242,
$$
$$
 \|(A-q^2)\psi-\partial_1q\|_2\le0.000662,
 \qquad J_q\le-273,
$$

and the five BS bounds in the preceding table hold. Take rho=0.006. Using only gamma_R=0.05 and gamma_-=0.04, outward-rounded sufficient estimates are

$$
 \text{Newton radius bound}<0.005373467<0.006,
 \qquad\text{contraction constant}<0.177823807<1,
$$
$$
 d_1<0.002963731,\quad d_3<0.008891191,
 \quad\gamma_--d_1>0.037036269.
$$

The other sector gaps also survive their respective perturbations. Finally (21) gives

$$
 J_Q-J_q<52.542719,\qquad
 \|r\|_{Z^*}<0.395293636,
 \qquad
 \langle r,L^{-1}r\rangle<4.219029,
$$
$$
 I<-273+52.542719+4.219029=-216.238252<0.\tag{22}
$$

Thus **these concrete finite certifications would close the conditional theorem and disprove the universal negative-energy claim in dimension four**. The margins are ample, so there is no need to chase machine precision. The logical obstacle is proving the BS trace/HS and Ritz enclosures for the canonical exact q, including integration and tail errors, not improving the plotted profile.

For comparison, the earlier coarser q with eta<=0.002846 also works at rho=0.02 if its radial BS gap is certified >=0.17; the same b, eta_psi, and J bounds give I<-40.33. However a radial HS bound of 39 only implies gap>=0.05, so those two versions must not be mixed. The refined q and loose BS certificate above are the recommended coherent version.

## 9. Direct H2 implicit-function theorem and moment-free Pohozaev derivation

No separately quantified H4 inverse estimate or exponential spatial decay is needed in the proof above. Let X_Z be the symmetry space (5) with H2 regularity and let Y_Z be its H^{-2} counterpart, viewed as a real Banach space. Equation (17) shows that the cubic is a continuous polynomial X_Z to Y_Z. The operator partial_1 is bounded between these spaces. Therefore F(v,Q) is real analytic X_Z to Y_Z. The two sector BS inverse certificates give its derivative an isomorphism directly in these spaces. Apply the analytic implicit-function theorem here to obtain an H2-analytic branch. Momentum is a continuous quadratic form on H2 and energy a continuous polynomial there, so all parity and derivative arguments establishing (7) remain valid.

Each such profile automatically belongs to H4, because

$$
 A Q_v=|Q_v|^2Q_v-i v\partial_1Q_v\in L^2,
$$

using H2(R4) contained in L6. This is qualitative elliptic regularity, not an extra numerical certificate. Further bootstrap gives any regularity required to interpret the traveling-wave solution classically; H4 already suffices for the cutoff computation below.

To justify Pohozaev without a finite spatial moment, choose a real compact smooth cutoff chi equal to 1 near the origin. Define

$$
 F_R(x)=x\chi(x/R),\qquad
 D_R=F_R\cdot\nabla+\tfrac12\operatorname{div}F_R.
$$

D_R is skew-adjoint on L2. Pair the stationary equation with D_R Q_v and take real parts. The mass term is exactly zero. For the kinetic term, use

$$
 \Delta(D_RQ)=D_R\Delta Q
 +2\sum_{j,k}(\partial_kF_{R,j})\partial_{kj}Q
 +(\Delta F_R+\nabla\operatorname{div}F_R)\cdot\nabla Q
 +\tfrac12\Delta\operatorname{div}F_R\,Q.
$$

The real pairing of Delta Q with D_R Delta Q vanishes. Since partial_k F_{R,j} tends to delta_kj, the principal remaining term tends to 2||Delta Q||2 squared. Every error is bounded by a constant times an annular integral of

$$
 |\Delta Q|\,|D^2Q|
 +R^{-1}|\Delta Q|\,|\nabla Q|
 +R^{-2}|\Delta Q|\,|Q|.
$$

These vanish as R tends to infinity by Cauchy–Schwarz and H2 tails. The cubic pairing is exactly

$$
 \operatorname{Re}\int |Q|^2Q\overline{D_RQ}
 =\tfrac14\int\operatorname{div}F_R\,|Q|^4
 \longrightarrow\|Q\|_4^4.
$$

For momentum density $p_j=\operatorname{Im}(\overline Q\partial_jQ)$, elementary integration by parts gives

$$
 \operatorname{Re}\int i v\partial_1Q\overline{D_RQ}
 =-\tfrac v2\int\sum_j(\partial_1F_{R,j})p_j
 \longrightarrow-\tfrac v2P_1(Q).
$$

The density p is L1 by Q in H1. Derivatives of F_R are uniformly bounded, so dominated convergence applies. Taking the limit gives

$$
 2\|\Delta Q_v\|_2^2-\|Q_v\|_4^4-\frac v2P_1(Q_v)=0,
 \qquad E(Q_v)=\frac v8P_1(Q_v).
$$

All integrations can first be performed for smooth approximations on the fixed compact support of F_R and passed to the limit. H4 regularity makes the displayed products and integrations legitimate. No xQ, x grad Q, or weighted tail estimate enters the argument.

## 10. Exact arithmetic certificates

The following rational bounds hold for the frozen compact rational q in [round2_radial_H4_exact_h1_16.json](../../computations/excited-waves/axial-profiles/round2_radial_H4_exact_h1_16.json) and the canonical response psi. Reproducible rational integration code and results are in [round2_certificate_canonical.py](../../computations/excited-waves/round2_certificate/round2_certificate_canonical.py), [round2_certificate_canonical_integrals.json](../../computations/excited-waves/round2_certificate/round2_certificate_canonical_integrals.json), and [round2_certificate_canonical_results.json](../../computations/excited-waves/round2_certificate/round2_certificate_canonical_results.json):

- ||q||Z squared <= 10635.58448399505 < 104 squared;
- ||psi||Z squared <= 17273.995930603982 < 132 squared;
- Jq <= -273.4738618768856 < -273;
- response L2 residual squared <= 4.14791963828076e-7, hence residual < 0.000645 < 0.000662.

The parent also reports exact rational Ritz/minmax checks for all the lower eigenvalue bounds in the table, with results in `round2_ritz_exact_results.json`. These reports do not by themselves certify the BS upper trace/HS bounds; those remain separate required enclosures at the time of this update. The use of one canonical q throughout, or a rigorously budgeted operator-norm transfer from another q, is essential.

## 11. Final rational arithmetic version of the implication

For maximal simplicity, replace the sharp constants by

$$
 C_4\le\tfrac14,\qquad\alpha=\tfrac1{256},\qquad G=\tfrac35.
$$

The first follows from the displayed sharp Sobolev constant and pi>3>sqrt(6). The second derivative bound follows by raising to the fourth power: (3^(3/4)/4)^4=27/256 < (3/5)^4. All subsequent certificate arithmetic is then rational.

With m=104, b=132, eta_q=121/500000, eta_psi=331/500000, rho=3/500, gamma_R=1/20, gamma_-=1/25, and Jq<=-273, the exact arithmetic implications are:

$$
 \text{Newton radius bound}=\frac{9148027}{1600000000}<\frac3{500},
 \qquad
 \text{contraction bound}=\frac{936027}{3200000}<1,
$$
$$
 d_1=\frac{312009}{64000000},\qquad
 d_3=\frac{936027}{64000000},\qquad
 \gamma_--d_1=\frac{2247991}{64000000}>0,
$$
$$
 J_Q-J_q\le\frac{343579401}{4000000},\qquad
 \|r\|_{Z^*}\le\frac{10364489}{16000000},
$$
$$
 I\le-\frac{24609689664617}{140499437500}<-175<0.
$$

The pure-Python standard-library script [round2_final_rational_implication.py](../../computations/excited-waves/round2_certificate/round2_final_rational_implication.py) verifies these and all needed spectral-gap reductions using `fractions.Fraction`; no floating-point comparison occurs. Its output is [round2_final_rational_implication.json](../../computations/excited-waves/round2_certificate/round2_final_rational_implication.json), and all checks pass. Decimal strings in the output are display only. This script verifies the analytic implication from the declared premises; it deliberately does not claim to verify the independent BS integral bounds. For all high angular sectors, a preconditioned gap of 1/10 is sufficient. Such a gap may be obtained from the table's HS bounds, or directly from a certified pointwise inequality implying c q(r)^2 <= (9/10)(1+lambda_ell^2/r^4) and (9).
