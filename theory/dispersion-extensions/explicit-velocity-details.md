# Proof details of the explicit traveling-wave extension

Date: 2026-10-07. This note audits the new implication from the previously certified profile, inverse, and response estimates. It does not replace or recertify those estimates. I independently recomputed the constants using Python `Fraction`, without importing the proposed verification script, and inspected [verify_explicit_extension.py](../../computations/dispersion-extensions/verify_explicit_extension.py). No sign, norm, contraction, or scaling failure was found under the inputs stated below.

## 1. Precise scope and inputs

The dimension is **four**. Write

$$
 \|f\|_Z^2=\|\Delta f\|_2^2+\|f\|_2^2,
 \qquad \mathcal X=\{f\in H^2(\mathbb R^4;\mathbb C):f(-x)=\overline{f(x)}\}.
$$

Thus the real part is even and the imaginary part odd under **full inversion**. This is not a restriction to axisymmetric functions. The inputs are an exact real radial solution

$$
 (\Delta^2+1)Q-Q^3=0,
$$

and certified estimates

$$
 \|Q\|_Z\le105=:m,\quad
 \|\mathcal L^{-1}\|_{\mathcal X^*\to\mathcal X}\le29=:C,\quad
 z=L_-^{-1}\partial_1Q,\quad \|z\|_Z\le151,
 \quad I=\langle\partial_1Q,z\rangle<-175,
$$

where $\mathcal L(a+ib)=L_+a+iL_-b$, $L_+=\Delta^2+1-3Q^2$, and $L_-=\Delta^2+1-Q^2$. The input inverse estimate must hold on the whole space $\mathcal X$. The supplied sector bounds do give this implication if, as stated in the parent proof, they cover real even spherical degrees $0,2,4,\ldots$ and imaginary odd degrees $1,3,5,\ldots$, including the high-degree bounds. Angular multiplicity does not enlarge the norm of their orthogonal direct sum.

Use the safe constants

$$
 \alpha=1/256,\qquad G=3/5,\qquad H=1/2.
$$

They mean $\|f\|_4\le\|f\|_Z/4$, $\|\partial_1\|_{Z\to Z^*}\le G$, and $\|\Delta\|_{Z\to Z^*}\le H$. Indeed the exact derivative multiplier supremum is $3^{3/4}/4<3/5$, and $\sup_{r\ge0}r^2/(1+r^4)=1/2$.

## 2. Matrices and quartic principal symbols

Let $B$ be any real symmetric $4\times4$ matrix. More generally let $a(\xi)$ be a **real homogeneous quartic polynomial**, and set

$$
 \delta_a=\sup_{|\xi|=1}|a(\xi)-|\xi|^4|.
$$

Such a polynomial is even. In the small neighborhood used below it is positive and uniformly elliptic. For $a(D)$ defined by its Fourier multiplier, consider

$$
 iu_t=a(D)u-B:D^2u-|u|^2u.
$$

The perturbation $\mathcal T=a(D)-\Delta^2-B:D^2$ satisfies

$$
 \|\mathcal T\|_{Z\to Z^*}
 \le \delta_a+\tfrac12\|B\|_{\rm op}.
$$

This follows directly from $|a(\xi)-|\xi|^4|\le\delta_a|\xi|^4$ and $|\xi^TB\xi|\le\|B\|_{\rm op}|\xi|^2$. Cross derivatives cause no additional factor. Every real even constant-coefficient term preserves $\mathcal X$. The term $iv\partial_1$ also preserves it: it exchanges real-even and imaginary-odd components. The nonlinear term preserves it pointwise. Arbitrary $B$ need not preserve axial symmetry, which is why the full PT-space inverse is essential.

Fix

$$
 0<t=|v|\le10^{-6},\qquad
 2\delta_a+\|B\|_{\rm op}\le t^2/1000.
$$

Then $\|\mathcal T\|\le t^2/2000=H\kappa t^2$, with $\kappa=1/1000$. The scalar case is $a=|\xi|^4$, $B=\mu I$.

## 3. Fixed point and complex cubic derivative

The traveling ansatz is

$$
 u(t,x)=e^{it}U(x-vte_1).
$$

The phase is $e^{it}$, consistent with the stated sign of the BNLS equation. The profile equation is

$$
 a(D)U-B:D^2U+U+iv\partial_1U-|U|^2U=0.
$$

For $U=Q+h$, the nonlinear remainder after the real-linear derivative is exactly

$$
 N_2(h)=Qh^2+2Q|h|^2+|h|^2h.
$$

In particular the derivative is $3Q^2$ on the real component and $Q^2$ on the imaginary component. Hölder and the embedding above give

$$
 \|N_2(h)\|_{Z^*}\le\alpha(3m\|h\|_Z^2+\|h\|_Z^3),
$$

and Lipschitz constant at most $\alpha(6mr+3r^2)$ on the ball of radius $r$. The fixed point is

$$
 h=-ivz-\mathcal L^{-1}\mathcal TQ
       -\mathcal L^{-1}(iv\partial_1h+\mathcal Th)
       +\mathcal L^{-1}N_2(h).
$$

For the scalar case this gives the stated positive terms $+\mu\mathcal L^{-1}\Delta Q$ and $+\mu\mathcal L^{-1}\Delta h$. On $\|h\|_Z\le Rt$, $R=200$, put $D=1500000$. Direct estimates yield

$$
 \|h+ivz\|_Z\le D_0t^2\le Dt^2,
$$

where

$$
 D_0=C\{\kappa Hm+GR+\kappa HR\,10^{-6}
              +\alpha(3mR^2+R^3\,10^{-6})\}
     =1430826.1787529<D.
$$

Consequently $151+D10^{-6}=152.5<200$, so the ball maps strictly inside itself. The contraction constant is at most

$$
 C\{G10^{-6}+H\kappa10^{-12}
       +\alpha(6mR10^{-6}+3R^2 10^{-12})\}
 =0.0142908510937645<0.015.
$$

These estimates prove a unique fixed point in this ball at every stated parameter, rather than merely an unspecified sufficiently small speed. Existence is real Banach-space contraction; complex holomorphy is neither asserted nor required.

## 4. Momentum and energy signs

Use the convention

$$
 P_1(U)=\operatorname{Im}\int\overline U\,\partial_1U.
$$

If $h=-ivz+e$, integration by parts gives

$$
 P_1(Q+h)=2Iv-2\operatorname{Im}\langle\partial_1Q,e\rangle+P_1(h).
$$

Thus

$$
 |P_1(Q+h)-2Iv|
 \le 2GmDt^2+GR^2t^2=189024000t^2.
$$

This formula confirms both the sign of the response $-ivz$ and the factor two in the momentum expansion. Multiplying the error by $|v|=t$, and using $I<-175$, gives

$$
 \frac{vP_1(U)}8
 <\frac{-350+189024000\cdot10^{-6}}8\,t^2
 =-20.122t^2.
$$

Define

$$
 K_B(U)=\int\nabla\overline U\cdot B\nabla U,
 \qquad
 E_{a,B}(U)=\tfrac12\langle U,a(D)U\rangle
                 +\tfrac12K_B(U)-\tfrac14\|U\|_4^4.
$$

The stationary equation is the real Euler equation for
$E_{a,B}+\frac12\|U\|_2^2-\frac v2P_1$.
Under the mass-preserving variation $U_\lambda(x)=\lambda^2U(\lambda x)$, the quartic energy and quartic nonlinearity scale as $\lambda^4$, the matrix term as $\lambda^2$, and momentum as $\lambda$. The resulting Pohozaev identity is

$$
 E_{a,B}(U)=\tfrac14K_B(U)+\tfrac18vP_1(U).
$$

It remains valid for indefinite $B$; the proof does not use positivity of $K_B$. For a real elliptic quartic polynomial, the $H^2$ solution bootstraps to $H^4$ and the identity can be justified with spatial cutoffs; an arbitrary nonlocal, merely positively homogeneous symbol would need an additional Pohozaev justification and is not included in this audit.

The upper bound

$$
 K_B(U)\le\|B\|_{\rm op}\|\nabla U\|_2^2,
 \qquad
 \|\nabla U\|_2^2\le\tfrac12(105+200\cdot10^{-6})^2
 =5512.52100002
$$

now gives

$$
 E_{a,B}(U)<
 \left(\frac{5512.52100002}{4000}-20.122\right)t^2
 =-18.743869749995t^2<-18t^2.
$$

For $B=\mu I$ this reduces exactly to
$E_\mu=\mu\|\nabla U\|_2^2/4+vP_1/8$.
For the original equation $a=|\xi|^4,B=0$, the simpler identity $E=vP_1/8$ applies. Nonzero momentum also ensures that $U$ cannot be radial about any center.

## 5. Arbitrary fixed matrices by scaling

The mass-critical transformation

$$
 u_\lambda(t,x)=\lambda^2u(\lambda^4t,\lambda x)
$$

leaves the homogeneous quartic symbol $a$ unchanged and sends

$$
 B_0\mapsto B'=\lambda^2B_0,\qquad
 \omega\mapsto\lambda^4\omega,\qquad
 v\mapsto\lambda^3v,\qquad
 E_{a,B_0}\mapsto\lambda^4E_{a,B_0}.
$$

For $a=|\xi|^4$, every fixed real symmetric matrix $B\ne0$ is reached by taking $v_0=10^{-6}$, $B_0=10^{-15}B/\|B\|_{\rm op}$, and $\lambda^2=10^{15}\|B\|_{\rm op}$. The case $B=0$ uses the unscaled profile. This includes every fixed positive, zero, or negative scalar $\mu$.

The simultaneous quartic extension is also correct. Fix a real quartic form satisfying

$$
 \delta_a\le\frac1{4\cdot10^{15}},
$$

and any real symmetric $B$. Choose

$$
 v_0=10^{-6},\qquad
 \lambda^2=\max\{1,2\cdot10^{15}\|B\|_{\rm op}\},
 \qquad B_0=B/\lambda^2.
$$

Then $2\delta_a+\|B_0\|_{\rm op}\le10^{-15}=v_0^2/1000$. The explicit contraction produces a negative-energy profile for $(a,B_0)$, and the stated scaling produces one for $(a,B)$.

The frequency after scaling is generally not one. Accordingly, the arbitrary-matrix conclusion requires **frequency to be free**. It does not assert existence at every matrix with frequency held fixed.

## 6. derivation verdict and boundaries

The explicit-speed implication, the real symmetric matrix generalization, and the small real quartic-form generalization follow from the displayed rational bounds. The solutions are global explicit translating waves with constant $H^2$ norm and negative energy.

The essential boundaries are: dimension four; real even quartic symbol as specified; the full PT inverse and negative-response bounds are imported certified premises; and frequency is free after scaling. A proof of these new implications does not itself verify the source spectral certificates. The positive-scalar conclusion has a direct conflict with the cited cylindrical blowup statement in Gou, which is addressed separately in [gou-details.md](gou-details.md); this note does not claim that conflict disappears.

