# Unequal distant Townes wells: the scattering coefficient

Derivation, 12 October 2026. This extends the equal-scale fixed-potential calculation to a fixed unequal scale ratio. It does not optimize over potential shapes.

## Setup and spectral restriction

Let $-\Delta Q+Q-Q^3=0$, $m=\int Q^2$, $Q(r)\sim ar^{-1/2}e^{-r}$, and $h=-\Delta-Q^2$. Its simple ground eigenvalue is $-1$. Let $\lambda_2(h)\le0$ mean the second min-max level, zero if there is no second negative eigenvalue. Fix

$$
\sqrt{\max(0,-\lambda_2(h))}<k<1.
$$

Thus $-k^2$ lies strictly between the narrow-well ground and its remaining spectrum. Set

$$
p_R(x)=kQ(k(x-Re_1)),\quad
V_R=Q^2+p_R^2,\quad H_R=-\Delta-V_R,
\quad\varepsilon_R=a\sqrt{k}\,R^{-1/2}e^{-kR}.
$$

Both isolated ground functions have mass $m$, with eigenvalues $-1$ and $-k^2$. The scale ratio $k$ is fixed before $R\to\infty$.

Define

$$
f_k(x)=e^{kx_1},\qquad g_k=Q^2f_k,\qquad
I(k)=\int Q^2f_k^2,
$$
$$
\boxed{\mathcal C(k)=I(k)+
\langle g_k,(h+k^2)^{-1}g_k\rangle.}
$$

The resolvent here includes the negative ground direction. Omitting that direction reverses the crucial competition.

## Leading eigenvalue shifts

For fixed $k$ in the stated interval,

$$
\lambda_1(H_R)=-1-\frac{\varepsilon_R^2}{m}I(k)
+o(\varepsilon_R^2),
$$
$$
\lambda_2(H_R)=-k^2-\frac{\varepsilon_R^2}{m}\mathcal C(k)
+o(\varepsilon_R^2).
$$

Also

$$
\frac1{2m}\int V_R^2
=1+k^2+\frac{\varepsilon_R^2}{m}I(k)
+o(\varepsilon_R^2).
$$

Consequently the deficit is

$$
\boxed{\frac1{2m}\int V_R^2-S_2(H_R)
=-\frac{\varepsilon_R^2}{m}\mathcal C(k)
+o(\varepsilon_R^2).}
$$

Positive $\mathcal C(k)$ would provide distant unequal-well counterexamples; negative $\mathcal C(k)$ gives nonbinding for this family.

## Derivation by the scalar Schur complement

The broad tail obeys $p_R/\varepsilon_R\to f_k$ locally. Exponential bounds imply

$$
\int Q^2p_R^2=\varepsilon_R^2I(k)+o(\varepsilon_R^2),
\qquad Q^2p_R/\varepsilon_R\to g_k\quad\text{in }L^2.
$$

The first limit uses $k<1$; the second only needs $k<2$. One can split space into a fixed neighborhood of the narrow core and its complement, using any slightly larger exponential weight still below the corresponding integrability endpoint.

For the narrow eigenvalue, project onto $Q/\sqrt m$. Its off-diagonal residual is controlled by $\|p_R^2Q\|_2$, and

$$
\|p_R^2Q\|_2^2=o(\varepsilon_R^2)
$$

for every fixed $0<k<1$. Indeed the exponential costs in the integral $\int p_R^4Q^2$ are at least $\min(4k,2)R$, strictly larger than $2kR$, up to harmless polynomial factors. The complementary resolvent near $-1$ is uniformly bounded, since both the translated broad ground $-k^2$ and all other isolated-well levels remain separated from $-1$. The scalar Schur complement therefore gives the first shift.

For the broad eigenvalue, put $u_R=p_R/\sqrt m$, $P_R=|u_R\rangle\langle u_R|$, $\Pi_R=1-P_R$. Its diagonal entry is

$$
\langle u_R,H_Ru_R\rangle=-k^2-
\frac1m\int Q^2p_R^2.
$$

Its off-diagonal vector is $-\Pi_RQ^2p_R/\sqrt m$. The spectral restriction on $k$, together with the scalar ground gaps of both wells and IMS localization, implies a uniform inverse for

$$
\Pi_R(H_R+k^2)\Pi_R
$$

on $\operatorname{Ran}\Pi_R$. There is one complementary negative level near $-1+k^2$, bounded away from zero, while all remaining complementary levels are bounded above zero by a fixed positive number. The latter claim follows by first removing the two approximate ground directions and applying the single-well gaps; the Gram corrections tend to zero.

For sources localized near the narrow core, these inverses converge strongly to $(h+k^2)^{-1}$. This can be checked first on compactly supported sources using local convergence of the coefficients and $P_R\to0$ strongly; the uniform inverse bound then extends convergence to the fixed source $g_k$. Equivalently one may cut off $(h+k^2)^{-1}g_k$ far from the broad core, project away $u_R$, and use the uniform inverse bound on its vanishing residual.

The scalar Schur complement at the eigenvalue near $-k^2$ now gives

$$
\lambda_2=-k^2-\frac1m\int Q^2p_R^2
-\frac1m\left\langle\Pi_RQ^2p_R,
[\Pi_R(H_R-\lambda_2)\Pi_R]^{-1}
\Pi_RQ^2p_R\right\rangle.
$$

First the uniform inverse gives $\lambda_2+k^2=O(\varepsilon_R^2)$; the resolvent identity permits replacement of $\lambda_2$ by $-k^2$ at higher order. The stated strong convergence gives the coefficient $\mathcal C(k)$.

## Orthogonality and the ground contribution

The local broad-state shape is

$$
\chi_k=f_k+(h+k^2)^{-1}(Q^2f_k),
\qquad (h+k^2)\chi_k=0.
$$

The identity

$$
\int Q^3f_k=(1-k^2)\int Qf_k
$$

follows by integrating the equation for $Q$ against $f_k$. It gives $\int Q\chi_k=0$. Thus the negative ground component of the resolvent is exactly what enforces orthogonality to the narrow state; it is not a dispensable correction.

## A rigorous sign near equal scales

With $\Pi=1-|Q\rangle\langle Q|/m$, spectral decomposition gives

$$
\mathcal C(k)=I(k)
-\frac{\left(\int Q^3e^{kx_1}\right)^2}{m(1-k^2)}
+\left\langle\Pi g_k,(h+k^2)^{-1}\Pi g_k\right\rangle.
$$

The last term stays bounded as $k\uparrow1$, because of the single-well ground gap and uniform $L^2$ bounds on $g_k$. The tail representation gives

$$
\int Q^3e^{x_1}=\sqrt{8\pi}\,a,
\qquad
I(k)\sim\frac{\pi a^2}{\sqrt{2(1-k)}}.
$$

Therefore

$$
\boxed{\mathcal C(k)=
-\frac{8\pi a^2}{m(1-k^2)}
+O((1-k)^{-1/2})<0}
$$

for all fixed $k<1$ sufficiently close to one. This proves nonbinding for those unequal-scale fixed-potential families, in addition to the exact equal-scale case. No sign has been established here for all admissible scale ratios.

The limits $R\to\infty$ and $k\uparrow1$ are nonuniform: the above coefficient diverges, whereas the equal-scale result has a finite $e^{-2R}$ coefficient. A joint limit with $(1-k)R=O(1)$ needs a separate uniform analysis; the formulas must not be interchanged across that regime.
