# Rank-independent regularity and scale bounds for a selfconsistent optimizer

These estimates apply to an actual finite-rank selfconsistent optimizer. They do not prove the planar Lieb–Thirring conjecture, a uniform joint-deficit gap, or a soliton-channel approximation theorem. The amplitude constant below is explicit but extremely large.

## Assumptions and notation

Let the real or complex orbitals $\phi_1,\ldots,\phi_N$ be orthonormal in $L^2(\mathbb R^2)$, and suppose

$$
H\phi_i=-e_i\phi_i,\qquad H=-\Delta-a\rho,
\qquad \rho=\sum_i|\phi_i|^2,
$$

where $a>0$, $e_1\ge\cdots\ge e_N>0$, and the occupied ground state is the ground state of $H$. In particular $\inf\sigma(H)=-e_1$; additional unoccupied negative eigenvalues are permitted. Put

$$
T=\sum_i\|\nabla\phi_i\|_2^2,\qquad F=\int\rho^2,
\qquad aF=2T,\qquad \sum_i e_i=T.
$$

The finite-rank optimizer is smooth and exponentially decaying. All estimates below are independent of $N$. Write $\Phi=(\phi_1,\ldots,\phi_N)^T$, $E=\operatorname{diag}(e_i)$, and $r=|\Phi|=\sqrt\rho$.

## 1. Density and second-derivative bounds

The sharp planar BV Sobolev inequality and the diamagnetic inequality give

$$
\|r^3\|_2\le\frac1{2\sqrt\pi}\|\nabla(r^3)\|_1
\le\frac3{2\sqrt\pi}F^{1/2}T^{1/2}.
$$

There is no circular use of $H^2$ regularity: $r\in L^2\cap L^4$ and $\nabla r\in L^2$ imply $r^3\in W^{1,1}$, and BV Sobolev supplies $r^3\in L^2$. Consequently

$$
\boxed{\int\rho^3\le\frac9{4\pi}FT.} \tag{1}
$$

The equation then gives $\Delta\phi_i\in L^2$, and

$$
\begin{aligned}
\sum_i\|\Delta\phi_i\|_2^2
&=a^2\int\rho^3-2a\int\rho\sum_i e_i|\phi_i|^2+\sum_i e_i^2\\
&\le a^2\int\rho^3+T^2
\le\left(1+\frac{9a}{2\pi}\right)T^2.
\end{aligned}
$$

Thus

$$
\boxed{\sum_i\|\Delta\phi_i\|_2^2\le
\left(1+\frac{9a}{2\pi}\right)T^2.} \tag{2}
$$

The vector Kato inequality gives $-\Delta r\le ar^3$. Testing with $r^3$, using smooth cutoffs and truncation if necessary, yields

$$
3\int r^2|\nabla r|^2\le a\int r^6.
$$

The cutoff error is bounded by a constant times $R^{-2}\int r^4$ and vanishes. Since $|\nabla\rho|^2=4r^2|\nabla r|^2$, (1) implies

$$
\boxed{\|\nabla\rho\|_2^2\le\frac6\pi T^2.} \tag{3}
$$

In particular the generic construction that keeps a nonvanishing transverse kinetic tail at arbitrarily high frequency, with no uniform second-derivative bound, cannot occur within this normalized optimizer class. Low-frequency spreading and separation into many scales are not excluded by (1)–(3).

## 2. Amplitude controlled by the lowest eigenvalue

Let $M=\|\rho\|_\infty$ and $h=aM+e_1$. The equation gives

$$
\|\Delta\Phi\|_{L^\infty(\ell^2)}\le h\sqrt M.
$$

For any unit spatial direction $\nu$, the heat identity and the exact norm
$\|\partial_\nu e^{t\Delta}\|_{L^\infty\to L^\infty}=1/\sqrt{\pi t}$
give

$$
\|\partial_\nu\Phi\|_\infty
\le\frac{\sqrt M}{\sqrt{\pi t}}
+2\sqrt{\frac t\pi}\,h\sqrt M.
$$

These estimates hold for Hilbert-valued functions with the same constants. Taking $t=(2h)^{-1}$ shows that $\Phi$ is Lipschitz with constant

$$
L=2\sqrt{\frac2\pi}\sqrt{Mh}.
$$

At a point $x_0$ attaining $|\Phi(x_0)|=\sqrt M$, it follows that

$$
\rho(x)\ge M/4\qquad\text{if}\qquad
|x-x_0|\le b,\qquad b^2=\frac\pi{32h}.
$$

If $aM<e_1$, the desired amplitude estimate is already immediate. Otherwise $h\le2aM$, so the rescaled potential obeys

$$
b^2a\rho(x_0+bz)\ge\alpha_0\mathbf1_{\{|z|\le1\}},
\qquad \alpha_0=\frac\pi{256}.
$$

For completeness, this weak disk potential has an explicit strictly negative Rayleigh quotient. Set $\log R=4/\alpha_0$, and take

$$
f_R(z)=
\begin{cases}
1,&|z|\le1,\\
\log(R/|z|)/\log R,&1<|z|<R,\\
0,&|z|\ge R.
\end{cases}
$$

Then

$$
\int|\nabla f_R|^2=\frac{2\pi}{\log R}=\frac{\pi\alpha_0}{2},
\quad
\alpha_0\int_{|z|\le1}f_R^2=\pi\alpha_0,
\quad
\|f_R\|_2^2\le\pi R^2.
$$

Therefore

$$
\inf\sigma(-\Delta-\alpha_0\mathbf1_{|z|\le1})
\le-\lambda_0,
\qquad
\lambda_0=\frac{\alpha_0}{2}e^{-8/\alpha_0}
=\frac\pi{512}e^{-2048/\pi}.
$$

The variational principle and scaling give

$$
e_1\ge\frac{\lambda_0}{b^2}
=\frac{32\lambda_0}{\pi}(aM+e_1)
\ge\frac{32\lambda_0}{\pi}aM.
$$

Combining the two cases proves

$$
\boxed{a\|\rho\|_\infty\le C_* e_1,
\qquad C_*=16e^{2048/\pi}.} \tag{4}
$$

The exponentially small weak-well eigenvalue is retained explicitly. No threshold-strength assertion for a two-dimensional disk well is used.

## 3. Occupied kinetic matrix and slice Gram bounds

For every unit coefficient vector $w\in\mathbb C^N$, the occupied linear combination $f=\sum_iw_i\phi_i$ satisfies

$$
\|\nabla f\|_2^2
=a\int\rho|f|^2-\sum_i e_i|w_i|^2
\le aM.
$$

Hence the occupied kinetic matrix obeys the Loewner bound

$$
\boxed{\left(\langle\nabla\phi_i,\nabla\phi_j\rangle\right)_{ij}
\le C_*e_1 I_N.} \tag{5}
$$

For any slicing direction, let
$\Gamma(x)_{ij}=\langle\phi_i(x,\cdot),\phi_j(x,\cdot)\rangle_{L^2_y}$.
The sharp elementary one-dimensional Hilbert-valued estimate
$\|f\|_{L^\infty_x(L^2_y)}^2\le\|f\|_2\|\partial_xf\|_2$
applied to each occupied linear combination gives

$$
\boxed{\sup_x\|\Gamma(x)\|_{\mathrm{op}}^2\le aM\le C_*e_1.} \tag{6}
$$

## 4. Conditional consequence for the R30 pruning multiplier

In the separately derived constant-occupation pruning construction, suppose the positive multiplier has the audited form

$$
K^2=3c^2M_P-(1+\mu)T_{x,P}-\mu T_{y,P},
\qquad M_P=\int\Gamma_P(x)^3\,dx,
$$

where $\mu\ge0$, $\int\Gamma_P=I$, and
$\|\Gamma_P(x)\|_{\mathrm{op}}\le\|\Gamma(x)\|_{\mathrm{op}}$.
Dropping the positive kinetic matrices and using (6) gives

$$
\kappa^2:=\|K\|_{\mathrm{op}}^2\le3c^2 C_*e_1.
$$

If the original optimizer is a minimal-rank violation with
$e_N\ge\delta_v e_1$, $0<\delta_v\le1$, then

$$
\boxed{N\kappa^2\le\frac{3c^2C_*}{\delta_v}T.} \tag{7}
$$

However, the previously established minimal-rank inequality
$\delta_v\le1/(N+1)$ already implies $N\le1/\delta_v-1$.
The elementary bound $\sup_x\|\Gamma(x)\|_{\mathrm{op}}^2\le T_x$
therefore gives the stronger estimate

$$
N\kappa^2\le\frac{3c^2}{\delta_v}T_x.
$$

Thus (7) must not be advertised as newly removing rank dependence at fixed violation size. The amplitude estimate supplies physical spectral-scale control, but fixed-violation rank control was already available. Neither estimate by itself justifies compressing the nonlinear matrix action to spectral blocks of $K$: mixed blocks and the residual still require estimates.

## 5. Why these estimates do not close the planar conjecture

The violation size $\delta_v$ and a small one-dimensional lifting deficit are different parameters. Write $K_1=M_c/2$, $K_0=\sqrt3\pi$, and suppose $T/F=K_1/(1+\delta_v)$. Then

$$
T-K_0F=T\left[1-\frac{K_0}{K_1}(1+\delta_v)\right].
$$

As $\delta_v\downarrow0$, this tends to the positive fraction
$1-K_0/K_1$ of $T$, approximately $0.06992T$. In particular, approaching a hypothetical arbitrarily small violation of the Townes constant does not force the one-dimensional lifting deficit to zero. Also (7) deteriorates like $1/\delta_v$.

A proof valid only in the asymptotic small-lifting-deficit regime would therefore still not reach the Townes coefficient. A quantitative block theorem at the required finite deficit, or a different argument, remains necessary.

The estimates (1)–(6), including all constants and the weak-well argument, were independently audited in R30. Formula (7) additionally uses the separately audited pruning Euler identity.
