# time-dependent outer matching for the quadratic quintic branch

Date: 2026-10-11. The linear half-line response and its moments below are exact. Their matching to the first inner correction is also explicit. They do not establish existence of a singular solution of the coupled nonlinear system.

## 1. Choose a nonlinear outer evolution

Let the terminal secondary vector $W$ be smooth, odd, and rapidly decaying. Let $Z(t)$ be its local backward solution of the secondary-only common-density quintic system,

$$
 iZ_{j,t}+Z_{j,xx}+\Big(\sum_{k\ge2}|Z_k|^2\Big)^2 Z_j=0,
 \qquad Z(T)=W.
$$

Smooth local theory and parity give, on a short terminal interval,

$$
 Z(t,0)=0,\quad a_j(t)=\partial_xZ_j(t,0)=a_{j,*}+O(h),
 \quad h=T-t.
$$

All these statements hold in any sufficiently high fixed Sobolev norm allowed by the terminal data. The full secondary Gram matrix and $E(Z(t))=E(W)$ are exactly conserved. This choice matters: freely evolving the same background need not conserve its nonlinear energy, and an artificial $O(h)$ energy drift would dominate the candidate interaction energy $O(\lambda)=O(h^2)$.

For $\lambda=\kappa h^2$, replacing the terminal slope $a_*$ by $a(t)$ changes the matched term $-c|a|^2\lambda$ only by $O(h^3)$. Thus this ordinary outer time evolution leaves its leading $h^2$ coefficient unchanged.

## 2. Exact half-line boundary radiation

Consider on $x>0,h>0$

$$
 i\partial_hR=\partial_x^2R,\qquad R(0,x)=0,
 \qquad R(h,0)=b h^2.
$$

The causal, spatially decaying solution is

$$
 R(h,x)=b h^2B(x/\sqrt h),
$$

where $B(0)=1$ and

$$
 B''+\frac{i\eta}{2}B'-2iB=0.
$$

One precise definition, which fixes the branch, is the Laplace transform

$$
 \widehat R(p,x)=\frac{2b}{p^3}
                   \exp[-e^{i\pi/4}\sqrt p\,x],
 \qquad \Re p>0.
$$

Equivalently, for $\eta>0$,

$$
 B(\eta)=\frac{e^{i\pi/4}\eta}{2\sqrt\pi}
       \int_1^\infty u^{-1/2}(1-u^{-1})^2
                       e^{-i\eta^2u/4}\,du.
$$

The last integral is an oscillatory improper integral. Integration by parts at the lower endpoint, where the prefactor vanishes to second order, gives

$$
 B(\eta)=O(\eta^{-5}),\qquad B'(\eta)=O(\eta^{-4})
 \quad(\eta\to\infty).
$$

These estimates also justify the moments used below. The Dirichlet-to-Neumann map obtained by differentiating the Laplace transform is

$$
 \partial_xR(h,0)
    =-e^{i\pi/4}D_h^{1/2}(b h^2)
    =-\frac{8e^{i\pi/4}}{3\sqrt\pi}\,b h^{3/2}.
$$

Here $D^{1/2}$ is the Riemann--Liouville half derivative of a function vanishing at zero. Thus

$$
 d:=B'(0)=-\frac{8e^{i\pi/4}}{3\sqrt\pi},\qquad
 B(\eta)=1+d\eta+i\eta^2+O(\eta^3).
$$

The response has the exact norm scalings

$$
 \|R(h)\|_2=|b|h^{9/4}\|B\|_2,
 \|R_x(h)\|_2=|b|h^{7/4}\|B'\|_2,
 \|xR(h)\|_2=|b|h^{11/4}\|\eta B\|_2.
$$

These norms are on the positive half-line. An odd extension changes them by $\sqrt2$, but has a jump at the origin. Only the eventual composite with the inner offset removed is globally continuous; the discontinuous odd extension must not itself be presented as an $H^1(\mathbb R)$ solution.

## 3. Matching to the exact transverse scatterer

Let $c=\pi/4+\log2-1$, and let $F$ be the odd zero-energy profile from the companion notes. Its outer behavior is

$$
 a\lambda F(x/\lambda)
       =ax+ca\lambda\operatorname{sgn}x+\text{exponentially small terms}.
$$

For $\lambda=\kappa h^2$, the necessary leading boundary value is therefore $b=ca\kappa$. The half-line response contributes near the origin

$$
 R(h,x)=ca\kappa h^2
       +dca\kappa h^{3/2}x
       +ica\kappa h x^2+O(h^{1/2}x^3),\qquad x>0.
$$

The negative side is obtained by odd reflection. In particular:

* The radiation extends to distance $\sqrt h=\lambda^{1/4}/\kappa^{1/4}$, much farther than the core scale $\lambda$.
* Its correction to the outer slope at zero is $O(h^{3/2})$, and therefore does not change the leading coefficient $|a_*|^2$.
* Its quadratic term is $ica\kappa h\,x|x|$.

The inner imaginary correction computed independently in [transverse-dispersion.md](transverse-dispersion.md) has the form

$$
 ia\lambda^2\dot\lambda\,G(x/\lambda),\qquad
 HG=F-yF',\qquad G(y)\sim-\frac c2 y|y|+K\operatorname{sgn}y.
$$

Since $\dot\lambda=-2\kappa h$, its quadratic outer term is exactly

$$
 -\frac{iac}{2}\dot\lambda\,x|x|
      =ica\kappa h\,x|x|.
$$

Thus the inner time-derivative correction and the causal outer radiation match in both sign and magnitude. A fixed cutoff joining the stationary scatterer directly to $Z$ would omit this term.

Ordinary evolution of the terminal slope contributes integer powers of $h$; the half derivative of the boundary value contributes half-integer powers. Consequently a systematic expansion naturally involves powers of $h^{1/2}$, not just integer powers of the core scale $\lambda$.

## 4. Exact moments and the total virial cancellation

Set $M_n(h)=\int_0^\infty x^nR(h,x)\,dx$. The decay established above makes $M_1$ and $M_3$ absolutely convergent. Integration by parts in the exact half-line equation gives

$$
 iM_1'=b h^2,\qquad iM_3'=6M_1,
$$

with zero terminal moments. Hence

$$
 M_1(h)=-\frac{i b}{3}h^3,\qquad
 M_3(h)=-\frac b2 h^4.
$$

Equivalently,

$$
 \int_0^\infty\eta B(\eta)\,d\eta=-\frac i3,
 \qquad
 \boxed{\int_0^\infty\eta^3B(\eta)\,d\eta=-\frac12.}
$$

Take the odd vector extension with $b_j=c\kappa a_{j,*}$, and put $A=\sum|a_{j,*}|^2$. Since the smooth odd outer field satisfies $|Z(t,x)|\le C|x|$, dominated convergence, with dominating function $C\eta^3|B(\eta)|$, gives

$$
 2\operatorname{Re}\sum_j\int_{\mathbb R}
        x^2\overline{Z_j(t,x)}R_j(h,x)\,dx
       =-2c\kappa A h^4+o(h^4).
$$

The quadratic radiation term in the variance is $O(h^{11/2})=o(h^4)$. Therefore its leading variance change is the negative quantity above. The primary variance is

$$
 I_1=V_Q\lambda^2=V_Q\kappa^2h^4.
$$

These cancel precisely when

$$
 \boxed{\kappa=\frac{2cA}{V_Q}.}
$$

This is the same coefficient obtained independently from the matched static energy and the primary mass solvability condition. It resolves the apparent global virial conflict of a patch confined to $|x|\sim h$: such a patch misses radiation at $|x|\sim\sqrt h$, whose mass is small but whose cross variance is of the required order $h^4$.

The cancellation is a consistency calculation for the candidate composite. It does not prove that the exact nonlinear evolution has these asymptotics.

## 5. Reinsert the boundary derivative into the inner profile

The $O(h^{3/2})$ slope feedback is lower order in amplitude, but cannot be left as an uncancelled inner term. If $\delta a=O(h^{3/2})$ is left multiplying $x$ instead of $\lambda F(x/\lambda)$, the concentrated primary potential produces

$$
 \lambda^{-2}Q(x/\lambda)^4\,\delta a\,x
     =\frac{\delta a}{\lambda}yQ(y)^4.
$$

For $\lambda\asymp h^2$, this has pointwise inner size $O(h^{-1/2})$, $L^2$ size $O(h^{1/2})$, and a derivative of $L^2$ size $O(h^{-3/2})$. Thus it is larger than the first inner time-derivative forcing in the norms relevant to a direct $H^1$ construction.

For the free half-line boundary response, the effective slope should instead satisfy

$$
 a_{\rm eff}(h)=a_Z(h)-e^{i\pi/4}
                D_h^{1/2}\big(c\lambda(h)a_{\rm eff}(h)\big),
 \qquad g(h)=c\lambda(h)a_{\rm eff}(h).
$$

The inner layer must then use $a_{\rm eff}\lambda F$. This is the leading Dirichlet-to-Neumann relation for the corresponding time-dependent Robin outer condition. In a full nonlinear outer problem, the derivative of the nonlinear volume response must also be included at its proper order.

The displayed fractional equation is not being asserted to have been solved by a Banach contraction. A half derivative loses regularity, and the most obvious Neumann series generally diverges. This can be seen exactly when $\lambda=\kappa h^2$ and $a_Z=a_0$ is constant. Its finite-order recursion is

$$
 a^{[N]}(h)=\sum_{n=0}^N c_nh^{3n/2},\qquad c_0=a_0,
$$

$$
 c_{n+1}=-e^{i\pi/4}c\kappa
    \frac{\Gamma(3n/2+3)}{\Gamma(3n/2+5/2)}c_n.
$$

Every truncation satisfies the exact residual identity

$$
 a^{[N]}+e^{i\pi/4}D_h^{1/2}(c\kappa h^2a^{[N]})-a_0
       =-c_{N+1}h^{3(N+1)/2}.
$$

Gamma-ratio asymptotics give coefficient growth comparable, up to exponential and polynomial factors, to $\sqrt{n!}$. Therefore this is a controlled finite-order asymptotic recursion, not a convergent power series for nonzero $h$. General half-integer expansions of $\lambda$ and $a_Z$ likewise give a triangular recursion: the leading factor $h^2$ and subsequent half derivative advance the order by $3/2$, so each new coefficient depends only on earlier ones.

## 6. The remaining analytic step

An actual nonlinear construction still needs a smooth composite in which the odd jumps and the successive polynomial tails cancel; an outer correction obeying the time-dependent boundary relation to sufficient order; the primary unstable directions and exact conservation constraints; and a remainder estimate for the singular time-dependent linearized flow. In particular, one cannot simply invoke the scalar Bourgain--Wang theorem with the present profiles substituted into it: its hypotheses and propagator estimates must be re-established for this coupled, faster-scale regime.

What is proved here is the exact half-line response, its spatial scale, its derivative feedback, and its moment identities. They show that ordinary time evolution of the background does not destroy the leading slope coefficient, and that the first dynamical outer correction repairs both the inner matching and the global virial balance. They do not yet provide a residual estimate sufficient to close a terminal fixed-point construction.
