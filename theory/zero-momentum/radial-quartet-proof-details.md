# Independent analytic and arithmetic derivation of the N4 radial quartet certificate

## Outcome

No blocking error was found in the finite-block theorem, exact-profile transfer, or final numerical inequalities. The three final verifier commands were copied with their exact inputs into `round5_quartet_independent_review/` and rerun there, without using the original output files. They all passed and reproduced

$$
 k\left(\delta_B+gM q_c^2\epsilon^2/\alpha\right)
 <0.365770416<1.
$$

The certified conclusion is one algebraically simple radial eigenvalue in the rectangle $(1.5,4.5)+i(4.5,7.5)$, and hence its Hamiltonian quartet. The many displayed approximate eigenvalue digits are not certified by this rectangle computation.

The existing exact-Q existence/refinement and radial Morse results are mathematical inputs to this review; their full source verifiers were not independently rerun here. Their recorded profile hash and the refinement's same-Q assertion are checked by the final certificate. 

## 1. Infinite-dimensional positive complement

The quotient by the exact phase vector is legitimate: this vector belongs to the generator domain and is killed by the generator. The group therefore descends to the quotient, represented by the Z-orthogonal complement. The bounded energy form remains self-adjoint and is invertible there. Its negative index is three.

For the verified finite block W, the Gram matrix G is nonsingular and has three negative eigenvalues. Consequently the H-orthogonal complement C of Ran W is nonnegative. Nonnegative alone is not sufficient to justify the later resolvent bound, but Section7 provides the missing coercivity argument. If PC is the bounded H-orthogonal projection, a continuous functional f on C extends as f PC; the vector

$$
 u=H^{-1}P_C^*f
$$

lies in C and solves its compressed form equation. This proves a bounded inverse for the positive compressed form, hence coercivity. Thus no hidden finite-dimensional truncation of the positive complement is being used.

The compressed generator's group property is also justified. Since the finitely many columns of W lie in D(A), APE is bounded, while the Hamiltonian identity implies

$$
 W^*HA=-(AW)^*H,
$$

so PEA extends boundedly. Removing the bounded off-diagonal blocks from the known group generator preserves generation. Its C block conserves the coercive positive form, making its group unitary in that energy norm. Therefore the resolvent estimate $1/\Re\lambda$ holds on the entire right half-plane.

## 2. Gram inertia and exact-Q transfer

The radial block integrator reconstructs C5 compact splines with exact dyadic jets. The final code explicitly checks the odd origin jets of orders1,3,5 and all six zero endpoint jets; this puts the whole-space trial vectors in H6. The origin formulas for the first three radial Laplacians and the non-origin polynomial numerator formulas were checked algebraically and match dimension4.

The LDL computation is an interval Schur elimination of the symmetric Gram matrix. Every pivot excludes zero; three are negative. It is not a count inferred from approximate eigenvalues. The subsequent exact-Q inertia transfer uses the full inverse norm and $\|G_q^{-1}\|\|G_Q-G_q\|<1$, so even small individual LDL pivots are not being treated as perturbation margins.

The exact Gram is independent of phase projection because $H_Q(0,Q)=0$. Thus comparison of the unprojected q and Q forms is valid. The product estimate gives

$$
 \|H_Q-H_q\|\le 3(2\|q\|_Z\rho+\rho^2)/256,
$$

and multiplication by the raw trial Frobenius norm squared correctly bounds the finite Gram perturbation. Dividing the global profile error by $\sqrt{2\pi^2}$ when using radial trial norms is consistent throughout the other error estimates.

The ambient bound $\|H_Q\|<6$ follows directly from positivity of the Birman--Schwinger operator and the frozen radial bound $\|K_{+,q}\|_{HS}^2<38.8$:

$$
 \|I-K_{+,q}\|\le\max(1,\sqrt{38.8}-1)<5.23,
$$

with a negligible q-to-Q perturbation. The minus block has the smaller coefficient and also satisfies this bound.

## 3. H2 residual transfer

Write $v=Q-q$ and $A_0=\Delta^2+1$. The quadratic inequality for $X=\|A_0v\|_2$ has positive leading coefficient and one positive root. Evaluating its right side at0.0003 proves that root is smaller, so the H4 bound is not an assumed bootstrap hypothesis.

The L-infinity interpolation bound used there is conservative. A direct independent proof gives the stronger estimate

$$
 \|v\|_\infty\le\frac1{4\pi}
 \|A_0^{3/4}v\|_2
 \le\frac1{4\pi}\sqrt{\|v\|_Z\|A_0v\|_2},
$$

because $\int_{\mathbb R^4}(1+|\xi|^4)^{-3/2}d\xi=\pi^2$. In particular the certificate's coefficient0.088 is valid.

For every scalar normalized trial U, the decomposition

$$
 (Q^2-q^2)U=(2qU)v+Uv^2
$$

has the stated H2 estimates. In the linear term, $\|\nabla v\|_2\le\rho/\sqrt2$ accounts for the factor $\sqrt2\|g'\|_\infty$. In the quadratic term,

$$
 \Delta(Uv^2)=(\Delta U)v^2+4v\nabla U\cdot\nabla v
 +2Uv\Delta v+2U|\nabla v|^2.
$$

These are exactly the four contributions in the code. Also

$$
 \|\nabla v\|_4^2\le\frac1{16}\sum_j\|\partial_jv\|_Z^2
 \le\rho X/16,
$$

so the final quadratic gradient term has the correct bound and surface-area factor.

After projection onto the exact phase quotient, the residual phase vector is $\Pi_Q(0,q-Q)$, not an uncontrolled multiple of q. Its contribution is the radial profile error times the appropriate row norm of the fixed change-of-basis matrix C. This matches the final certificate.

## 4. Direct compressed matrix and contour argument

The signed matrix entries $K_{ij}=\langle L V_i,J L V_j\rangle$ were checked against the chosen sign convention $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. Their polynomial numerator weights are $r^{-3}$. The inverse-weight Taylor remainder is a valid geometric majorant, and the final code explicitly verifies the required ratio bound.

The transfer identity for the compressed matrix is

$$
 B_Q-B_q=G_Q^{-1}\big[(K_Q-K_q)-(G_Q-G_q)B_q\big].
$$

The certificate's estimate $\delta_B$ is precisely the norm bound obtained from this identity plus the integrated reference error. The smaller direct compressed-matrix error is therefore justified; it is not replacing the continuum residual by an unrelated small number.

In the H-orthogonal coordinates, the two off-diagonal norms in energy units multiply to at most $gM q_c^2\epsilon^2$. Combining them with the complement resolvent gives the stated quadratic Schur correction, with no omitted factor of w or g. The finite-dimensional reference inverse is enclosed over every full boundary segment using complex-ball matrix inversion. The segments cover the rectangle boundary and remain in the strict right half-plane.

The analytic Schur determinant is seven dimensional, while the complement is holomorphically invertible throughout the rectangle. The strict boundary inequality gives a nonvanishing homotopy to the explicit reference determinant. Analytic Schur factorization preserves algebraic multiplicity, establishing the continuum eigenvalue count rather than only a matrix eigenvalue count.

## 5. Additional analytic consequence: the critical chain coefficient is positive

The quartet's four-dimensional real invariant space is nondegenerate for H and has two positive and two negative directions. Its H-orthogonal complement in the radial phase quotient consequently has negative index one.

Let $L_+f=-Q$, $L_-z=f$, and $\gamma=\langle f,z\rangle$. The mass-critical identity gives $\langle Q,f\rangle=0$, allowing the second equation. In the quotient the zero-chain vectors are

$$
 e_1=(f,0),\quad e_2=(0,z),\quad
 e_3=(-L_+^{-1}z,0).
$$

They are H-orthogonal to the quartet by the Hamiltonian identity, applied successively along the generalized zero chain. Their Gram matrix has the form

$$
 \begin{pmatrix}0&0&-\gamma\\0&\gamma&0\\-\gamma&0&*\end{pmatrix}.
$$

If $\gamma<0$, this matrix has two negative directions, contradicting the complement's index one. If $\gamma=0$, the independent vectors e1,e2 span a two-dimensional totally isotropic subspace, also impossible in a nondegenerate Pontryagin space of negative index one. Thus $\gamma>0$.

The next preimage would require the solvability condition $\langle Q,-L_+^{-1}z\rangle=\gamma=0$, which now fails. Since the radial kernel of the original generator is one dimensional, the original phase Jordan chain has exactly length four. Zero lies in the free essential spectral gap, so this is a discrete Jordan-chain statement. This consequence uses the certified quartet and Morse count and does not need a separate numerical enclosure of gamma.
