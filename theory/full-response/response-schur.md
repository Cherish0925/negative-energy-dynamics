# Full-response correction to component dilation and translation tests

Let real orthonormal orbitals satisfy

$$
 H\phi_i=-e_i\phi_i,\quad H=-\Delta-a\rho,\quad
 \rho=\sum_i\phi_i^2,
$$

and occupy the lowest N levels with a gap. Let P be their projection,
Pi=I-P, $A_i=\Pi(H+e_i)\Pi>0$, and let $A=\operatorname{diag}(A_i)$
on the direct sum of the horizontal orbital spaces. Set

$$
 B Y=\sum_i\phi_iY_i,\qquad
 B^*W=(\Pi(W\phi_i))_i,\qquad
 \mathcal Q=A-2aB^*B,\quad R=BA^{-1}B^*.
$$

The constrained orbital quadratic form is $q(Y)=\langle Y,\mathcal
QY\rangle$, and the potential response is $\mathcal R(W)=\langle
W,RW\rangle$. All inverse operators include the complete unoccupied
spectrum. The following identities do not assume stability or the sharp
conjecture. The full inequalities $\mathcal Q\ge0$ and
$R\le(2a)^{-1}I$ are equivalent: both assert that
$\sqrt{2a}\,BA^{-1/2}$ has operator norm at most one. Thus the
improvement below is only relative to a restricted orbital trial family;
the full potential Hessian is not logically stronger than the full orbital
Hessian.

## 1. Exact improvement obtained by optimizing the full response

For any sufficiently regular horizontal vector Y, put

$$
 W=2BY,\qquad Z=\mathcal QY=AY-aB^*W.
$$

Then

$$
 \boxed{
 \frac{1}{2a}\|W\|_2^2-\mathcal R(W)
 =\frac1{a^2}\left[q(Y)-\langle Z,A^{-1}Z\rangle\right].}
 \tag{1}
$$

Indeed $A^{-1}B^*W=a^{-1}(Y-A^{-1}Z)$, hence
$RW=W/(2a)-a^{-1}BA^{-1}Z$. Pairing with W and substituting
$aB^*W=AY-Z$ gives (1). By approximation the same identity holds
whenever the displayed forms are finite.

Thus optimizing the spectral response subtracts a nonnegative residual
Gram form from a restricted orbital test. It can detect an instability
even when that particular orbital test has positive q. Equation (1) alone
does not establish that the subtraction dominates q at every candidate.

## 2. Dilation, including all occupied projection terms

Let $D=1+x\cdot\nabla$, which is skew-adjoint on real L2 in dimension
two. Put

$$
 d_{ji}=\langle\phi_j,D\phi_i\rangle=-d_{ij},\qquad
 y_i=\Pi D\phi_i=D\phi_i-\sum_jd_{ji}\phi_j,
 \quad b_i=\phi_i y_i,\quad b=\sum_i b_i.
$$

Skew symmetry gives

$$
 b=\rho+\tfrac12x\cdot\nabla\rho.                     \tag{2}
$$

The commutator calculation is exact:

$$
 (H+e_i)D\phi_i
 =a(2\rho+x\cdot\nabla\rho)\phi_i-2e_i\phi_i,
 \qquad A_i y_i=2a\Pi(b\phi_i).                       \tag{3}
$$

In particular this does not require equal e_i or vanishing overlaps
$d_{ji}$. Taking the unprojected identity against $\phi_j$ gives

$$
 a\int(2\rho+x\cdot\nabla\rho)\phi_i\phi_j
 =(e_i-e_j)d_{ji}+2e_i\delta_{ij}.                    \tag{4}
$$

Consequently the occupied-energy correction in projecting Dphi_i is
exactly $\sum_j(e_i-e_j)d_{ji}^2$. It is already contained in (3)
through b_i and must not be subtracted a second time. The projection P is
fixed at the candidate when computing the horizontal Hessian; differentiating
P is neither required nor an omitted term.

For real coefficients c_i take $Y(c)_i=c_i y_i$. Equations (2)-(3) give

$$
 q(Y(c))=2a\sum_{i<j}\langle b_i,b_j\rangle(c_i-c_j)^2,
 \tag{5}
$$

$$
 W(c)=2\sum_i c_i b_i,\qquad
 Z(c)_i=2a\Pi\left\{\phi_i\left[c_i b-\sum_jc_jb_j\right]\right\}.
 \tag{6}
$$

Combining (1), (5), and (6) gives the complete response matrix on this
corrected component-dilation space. Its quadratic form is the matrix in
(5), minus $Z^*A^{-1}Z$, divided by a squared. Both matrices annihilate
the constant coefficient vector. This is the exact scale Ward identity.

The raw potentials $(2+x\cdot\nabla)\phi_i^2$ differ from the corrected
ones by

$$
 2b_i=(2+x\cdot\nabla)\phi_i^2-2\sum_jd_{ji}\phi_i\phi_j. \tag{7}
$$

Their sums agree, but individual raw and corrected tests must not be
identified when the off-diagonal overlaps are nonzero.

## 3. Translation version and an exact rank-two reduction

For any fixed direction v in R2, replace D above by $D_v=v\cdot\nabla$.
It is again skew-adjoint, and now

$$
 b=\tfrac12D_v\rho,\qquad
 (H+e_i)D_v\phi_i=a(D_v\rho)\phi_i.
$$

Therefore (3), (5), (6), and (1) hold unchanged with these new b_i. This
argument applies to one fixed spatial direction at a time; no unsupported
pairwise matrix symmetry between different directions is assumed.

For N=2 write u=phi_1, v=phi_2 (the letter v here denotes the orbital),
and use any one of these skew generators D. Let

$$
 d=\langle u,Dv\rangle,
 \quad y_1=Du+d v,\quad y_2=Dv-d u,\quad
 b_1=u y_1,\quad b_2=v y_2,\quad I=\int b_1b_2.
$$

For the single corrected potential W=2b_1, define

$$
 S=\langle\Pi(u b_2),A_1^{-1}\Pi(u b_2)\rangle
  +\langle\Pi(v b_1),A_2^{-1}\Pi(v b_1)\rangle.
$$

The full response deficit is exactly

$$
 \boxed{\frac1{2a}\|2b_1\|_2^2-\mathcal R(2b_1)
       =\frac{2I}{a}-4S.}                            \tag{8}
$$

The corrected second potential has the same deficit; their sum is the
symmetry mode. In particular a negative I already gives instability, while
the optimized test can also succeed for I>=0 precisely if S>I/(2a).

In two dimensions there is always a nonzero translation direction with
d=0: choose a direction perpendicular to the vector $\langle
u,\nabla v\rangle$; if that vector vanishes, any direction works. In
this direction no Gram correction is present, and
$b_1=uD u$, $b_2=vD v$. Thus (8) supplies a two-resolvent test with
no occupied overlap coefficients for every rank-two candidate, with no
radial or parity assumption.

Ground-state positivity u>0 does not itself establish the sign of I,
which contains derivatives of the two densities. Nor has a universal
lower bound S>I/(2a) been established here from subcritical a<M_c and
minimal-rank optimality. These are exact reductions and response identities,
not a new theorem excluding all rank-two candidates.
