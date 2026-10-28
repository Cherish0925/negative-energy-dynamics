# Proof details of the hierarchical two-well expansion

The Townes statement in [hierarchical-wells.md](hierarchical-wells.md), Sections 1–6, passes the independent algebraic, scaling, spectral-ordering, and error audit below. This is not a claim about historical novelty or about the global Lieb–Thirring optimization problem.

## Compressed zero-energy operator

The implication from one negative eigenvalue to $\Gamma\ge0$ is valid. A strictly negative compressed direction, together with the $Q$ direction whose negative quadratic form diverges like $-|\log\alpha|$, would produce two negative directions of the Birman–Schwinger complement for small $\alpha$. Bounded off-diagonal matrix entries cannot prevent this.

If $\Gamma\phi=0$, $\phi\perp Q$, then $(I-K_0)\phi=cQ$. The logarithmic potential

$$
\psi=c-\frac1{2\pi}\log|\cdot|*(Q\phi)
$$

indeed satisfies $Q\psi=\phi$ and $(-\Delta-Q^2)\psi=0$. The cancellation $\int Q\phi=0$, together with exponential weighted integrability of $Q\phi$, makes $\psi$ bounded at infinity; elliptic regularity gives local boundedness. Thus absence of a bounded zero solution excludes the kernel. Since the compression is identity minus a compact self-adjoint operator, strict coercivity follows. No positivity of the logarithmic kernel itself is assumed.

## Dilation and the broad pole

With $U_k f(x)=k f(kx)$, the broad operator is $k^2U_kh_zU_k^*$. Its resolvent has operator prefactor $k^{-2}$, but the integral-kernel dilation contributes $k^2$. Therefore its kernel in original variables is exactly $R_z(\delta;kx,ky)$, with no remaining power of $k$.

The normalized broad ground state is $\phi_k=kq(kx-z)$; the Birman–Schwinger pole is consequently $\delta^{-1}|v_k\rangle\langle v_k|$, where $v_k=Qq(kx-z)$. The projected equations

$$
A_kw=akv_k,\qquad k^2\delta a=k\langle v_k,w\rangle
$$

give exactly $\delta=\langle v_k,A_k^{-1}v_k\rangle$. They remain valid at $\delta=0$, so the proof does not discard a possible eigenfunction by dividing by the resolvent pole. Invertibility of $A_k$ excludes solutions with $a=0$.

## Green-kernel and inverse estimates

The local logarithmic singularity has coefficient $-1/(2\pi)$. After subtracting the broad eigenprojection, the remaining resolvent is uniformly bounded on the orthogonal complement for $-1/2\le\delta\le1$. Standard local resolvent regularity gives a continuous diagonal remainder and the corresponding first parameter derivative.

The cutoff argument in the source note is consistent in operator norm. In the interior, continuity of the remainder gives a weighted Hilbert–Schmidt error $o(1)$. In the exterior, the original-variable regular resolvent and its parameter derivative have norm $O(k^{-2})$, which is overwhelmed by the multiplication tail $O(e^{-c k^{-1/4}})$.

The Schur complement is $s=-ML/(2\pi)+O(1)$; its complementary block remains uniformly positive. Hence $A^{-1}Q=O(L^{-1})$, $\|A^{-1}\|=O(1)$, and

$$
b(\delta)=-\frac{2\pi q(z)^2}{L}+O(L^{-2}),
\qquad b'(\delta)=O(L^{-2}).
$$

The $O(k)$ error in $v_k=q(z)Q+O(k)$ contributes only $O(k/L+k^2)$, which is smaller than $L^{-2}$. An $o(1)$ operator remainder is therefore sufficient; no unproved inverse-logarithmic rate for that remainder is needed.

## Which eigenvalue is found

At energy $-2k^2$, the broad operator plus $2k^2$ is strictly positive. Its Birman–Schwinger complement is $A_k(1)-|v_k\rangle\langle v_k|$. The $Q^\perp$ block is $\Gamma+o(1)$, because $\Pi v_k=O(k)$, and the scalar Schur complement is negative of order $L$. Thus exactly one eigenvalue lies below $-2k^2$, with no eigenvalue at that threshold.

The exact pole reduction has precisely one root on $[-1/2,1]$, since $1-b'(\delta)>0$ and the endpoint signs differ. It identifies exactly one eigenvalue in $(-2k^2,-k^2/2)$. This is therefore $\lambda_2$. Possible additional levels closer to zero do not affect this identification or the two-level sum.

## Final cancellation and scope

The isolated deep eigenvalue has perturbation error $O(k^4)$. The linear Taylor contribution to its first-order expectation vanishes because the narrow ground-state density is radial. The same cancellation occurs in the potential cross integral. The resulting two-level deficit is

$$
-\frac{2\pi k^2q(z)^2}{|\log k|}
+O\!\left(\frac{k^2}{|\log k|^2}\right).
$$

For fixed finite $z$, $q(z)>0$; on compact sets the lower bound stays uniform. No conclusion uniform in diverging $z(k)$ follows.

The initial wording of Section 7 had one gap outside the Townes theorem: a merely “smooth broad potential” with a “unique simple negative eigenvalue” need not have the spectral isolation and decay assumptions used by the proof. This has been corrected in the packaged source note: both potentials and their derivatives decay exponentially, and the broad operator has exactly one simple negative eigenvalue with the stated gap. The Townes model already satisfied these conditions. No additional unresolved gap was identified in this audit of Sections 1–6.
