# relaxed spectral interaction of unequal Townes wells

Date: 2026-10-12. The expansion below is an analytical result **under the stated one-well spectral ordering**. Its coefficient need not have the same sign as the coefficient for projection onto undeformed Townes functions. 

## 1. Exact setting and coefficient

Let

$$
-\Delta Q+Q-Q^3=0,\quad M=\int Q^2,\quad q=Q/\sqrt M,
\quad q(r)\sim A r^{-1/2}e^{-r}.
$$

Fix $0<k<1$. Put

$$
V=Q^2,\quad U_R(x)=k^2Q^2(k(x-Re_1)),\quad
H_R=-\Delta-V-U_R,\quad h=-\Delta-V,
$$

$$
a_R(x)=kq(k(x-Re_1)),\quad
\varepsilon_R=A\sqrt k\,R^{-1/2}e^{-kR},\quad f(x)=e^{kx_1}.
$$

Assume explicitly that the second min-max level of $h$ obeys

$$
\lambda_2(h)>-k^2.
\tag{A}
$$

The ground level of $h$ is $-1$, simple with eigenfunction $q$. Assumption (A) both makes $h+k^2$ invertible and ensures that the two lowest limiting levels of $H_R$ are $-1,-k^2$. It is automatically satisfied for all $k$ sufficiently close to 1, by simplicity and the ground-state spectral gap. It is **not** assumed established here for every $0<k<1$.

Let

$$
g=Vf\in L^2,\qquad \eta=(h+k^2)^{-1}g,
$$

and define the finite scalar

$$
\boxed{\mathcal A(k)=\int V f^2+
\langle Vf,(h+k^2)^{-1}Vf\rangle.}
\tag{1}
$$

The resolvent in (1) includes the negative ground-state direction; dropping it changes the coefficient and is incorrect. With
$S_2(W)=|\lambda_1(-\Delta-W)|+|\lambda_2(-\Delta-W)|$
and $L_1=1/(2M)$, the expansion is

$$
\boxed{
S_2(V+U_R)-L_1\int(V+U_R)^2
=\varepsilon_R^2\mathcal A(k)+o(\varepsilon_R^2).}
\tag{2}
$$

Thus a rigorously positive value of $\mathcal A(k)$, together with (A), would give a strict two-level counterexample for all sufficiently large separations. A negative value gives repulsion for this fixed-potential construction at that ratio. A finite set of negative samples would not settle the full conjecture.

If the tail coefficient is instead defined for unnormalized $Q$, write $A_Q=\sqrt M A$ and $\varepsilon_Q=A_Q\sqrt k R^{-1/2}e^{-kR}$. Then the right side of (2) is $\varepsilon_Q^2\mathcal A(k)/M+o(\varepsilon_Q^2)$. These are the same normalization.

## 2. Proof through quasimodes, including the spectral error

Separated-well spectral convergence implies that, under (A), for large $R$ there are simple eigenvalues near $-1$ and $-k^2$, separated from the other spectrum by a constant independent of $R$. This familiar conclusion can be proved by an IMS partition into neighborhoods of the two centers and their complement, followed by the min-max principle. Only a fixed negative-energy window is needed; the continuum starts at 0.

The profile tail gives

$$
a_R/\varepsilon_R\longrightarrow f
\quad\text{in }L^2(V^2dx),
\tag{3}
$$

and also the analogous weighted convergence needed below with $Vdx$. A global majorant follows from
$q(r)\le C(1+r)^{-1/2}e^{-r}$; the factor $V$ decays exponentially faster than the possible growth $e^{k|x|}$ since $k<1$.

For the broad level take

$$
\psi_R=a_R+\varepsilon_R\eta.
$$

Since $(h+k^2)\eta=Vf$ and
$(-\Delta+k^2)a_R=U_Ra_R$,

$$
(H_R+k^2)\psi_R
=-V(a_R-\varepsilon_Rf)-\varepsilon_RU_R\eta.
\tag{4}
$$

The first term is $o(\varepsilon_R)$ in $L^2$ by (3). The second is also $o(\varepsilon_R)$, because $\eta\in L^2$, $U_R$ is uniformly bounded and translates to infinity. Also $\|\psi_R\|_2\to1$.

To calculate the Rayleigh quotient to greater precision than the norm of (4), use

$$
\begin{aligned}
\langle\psi_R,(H_R+k^2)\psi_R\rangle
&=-\varepsilon_R\langle a_R,U_R\eta\rangle
+o(\varepsilon_R^2)\\
&=-\varepsilon_R\langle a_R,V(f+\eta)\rangle
+o(\varepsilon_R^2)\\
&=-\varepsilon_R^2\mathcal A(k)+o(\varepsilon_R^2).
\end{aligned}
\tag{5}
$$

The middle equality is exact before the remainder: integrate
$(-\Delta+k^2)a_R=U_Ra_R$
against $\eta$, and use
$(-\Delta+k^2)\eta=V(f+\eta)$.
The discarded term involving $V(a_R-\varepsilon_Rf)$ is $o(\varepsilon_R^2)$, since both $a_R$ and $\varepsilon_R\eta$ have weighted norm $O(\varepsilon_R)$. The term $\varepsilon_R^2\langle\eta,U_R\eta\rangle$ is $o(\varepsilon_R^2)$.

The residual has norm $o(\varepsilon_R)$. For an isolated simple eigenvalue with a fixed spectral gap, the difference between its eigenvalue and the Rayleigh quotient is bounded by a constant times the squared residual norm. This follows immediately by decomposing the normalized trial vector into its spectral projection onto that eigenvalue and the orthogonal complement. Therefore (5) proves the actual broad-level expansion

$$
\lambda_b(H_R)=-k^2-\varepsilon_R^2\mathcal A(k)+o(\varepsilon_R^2).
\tag{6}
$$

For the narrow level use $q$ itself. Its Rayleigh quotient is

$$
-1-\int U_Rq^2
=-1-\varepsilon_R^2\int Vf^2+o(\varepsilon_R^2).
$$

The residual norm is at most a constant times $\|U_Rq\|_2$, which is $o(\varepsilon_R)$. Indeed its square is an exponentially decaying convolution with rate $\min(4k,2)>2k$, up to polynomial factors. The same gap estimate then gives

$$
\lambda_n(H_R)=-1-\varepsilon_R^2\int Vf^2+o(\varepsilon_R^2).
\tag{7}
$$

Finally,

$$
\int V^2=2M,\quad \int U_R^2=2Mk^2,\quad
\int VU_R=M\varepsilon_R^2\int Vf^2+o(\varepsilon_R^2).
$$

Hence

$$
L_1\int(V+U_R)^2
=1+k^2+\varepsilon_R^2\int Vf^2+o(\varepsilon_R^2).
$$

The cross term **exactly cancels the leading shift of the narrow level**. Combining this with (6)–(7) proves (2).

## 3. Why the undeformed-projector calculation is insufficient

Set

$$
I_1=\int qf,\qquad I_2=\int q^2f^2,
\quad G(k)=\frac{1-k^2}{M}I_1^2-I_2,
\quad\Pi=1-|q\rangle\langle q|.
$$

The equation for $q$ implies

$$
\langle Vf,q\rangle=(1-k^2)I_1.
$$

Separating the ground state in the full resolvent yields the exact identity

$$
\boxed{
\mathcal A(k)=-MG(k)
+\langle\Pi Vf,[\Pi(h+k^2)\Pi]^{-1}\Pi Vf\rangle.}
\tag{8}
$$

Under (A), the final term is nonnegative. It is of the same asymptotic order as the raw interaction; it cannot be dismissed as an error. Physically, it describes deformation of the slowly decaying mode by the narrow well. This term is the unresolved sign competition in the unequal-scale construction.

## 4. A convergent partial-wave formula

Expand

$$
f(r,\theta)=I_0(kr)+2\sum_{m\ge1}I_m(kr)\cos(m\theta).
$$

Let $w_m$ be regular at the origin and solve

$$
-w_m''-\frac1r w_m'+\left(\frac{m^2}{r^2}+k^2-Q(r)^2\right)w_m=0,
$$

normalized at infinity by

$$
w_m(r)=I_m(kr)+a_m(k)K_m(kr)+o(K_m(kr)).
$$

For fixed $k<1$, the corrections caused by the exponentially decaying potential are smaller than $K_m(kr)$: variation of parameters gives decay rate $2-k>k$ for those corrections. The integral definition below also fixes the coefficient directly.

Then

$$
\boxed{\mathcal A(k)=2\pi\left(a_0(k)+2\sum_{m\ge1}a_m(k)\right).}
\tag{9}
$$

To compute without subtracting two exponentially large growing solutions, integrate any regular solution $y_m$, along with

$$
J_m(r)=\int_0^r tQ(t)^2 I_m(kt)y_m(t)dt.
$$

The coefficients are

$$
c_{I,m}=\lim_{r\to\infty}r\bigl[y_m'(r)K_m(kr)-k y_m(r)K_m'(kr)\bigr],
\qquad a_m=J_m(\infty)/c_{I,m}.
\tag{10}
$$

Here primes on Bessel functions denote derivatives of their argument. The Wronskian sign is fixed by
$I_m(z)K_m'(z)-I_m'(z)K_m(z)=-1/z$.
Writing $y_m=r^m z_m$ gives the nonsingular initial-value formulation

$$
z_m''+\frac{2m+1}{r}z_m'+(Q^2-k^2)z_m=0,
\quad z_m(0)=1,\quad z_m'(0)=0,
$$

with $z_m'(r)=-(Q(0)^2-k^2)r/(2m+2)+O(r^3)$.

## 5. Control of omitted angular channels

For $m\ge1$, the free radial resolvent kernel is
$I_m(kr_<)K_m(kr_>)$, on $L^2((0,\infty),rdr)$. Its Birman–Schwinger operator $B_m$ is positive and satisfies

$$
\|B_m\|\le\operatorname{Tr}B_m
\le\frac1{2m}\int_0^\infty rQ(r)^2dr
=\frac{M}{4\pi m}<1.
\tag{11}
$$

The bound $I_m(z)K_m(z)\le1/(2m)$ follows by comparison to the zero-energy radial Green function. The strict inequality $M<4\pi$ follows from the Gaussian trial in the scalar sharp Gagliardo–Nirenberg inequality and the fact that a Gaussian does not satisfy its Euler–Lagrange equation. Thus these angular channels have no negative eigenvalues.

With the first Born coefficient

$$
a_m^{(0)}=\int_0^\infty rQ(r)^2I_m(kr)^2dr,
$$

the resolvent representation gives

$$
0\le a_m\le\frac{a_m^{(0)}}{1-M/(4\pi m)},\qquad m\ge1.
\tag{12}
$$

In particular the omitted tail above $m=L$ obeys

$$
\sum_{m>L}a_m\le\frac1{1-M/[4\pi(L+1)]}
\int_0^\infty rQ(r)^2\sum_{m>L}I_m(kr)^2dr.
\tag{13}
$$

The full sum can be evaluated using
$\sum_{m\ge1}I_m(z)^2=[I_0(2z)-I_0(z)^2]/2$.
It is integrable for fixed $k<1$, establishing absolute convergence of the positive angular tail in (9). The radial channel $m=0$ contains the negative ground-state contribution and must be treated with its sign intact.

## 6. Relation to prior work

The asymptotic interaction method belongs to established separated-well spectral analysis; Frank–Gontier–Lewin, arXiv:2002.04964, already employ exponentially small interactions to resolve adjacent exponent ranges. No historical originality claim is made for the present coefficient formula. Its relevance here is that it identifies an actual leading-order response omitted by the raw two-profile projection and gives a concrete, convergent calculation for it.

Equation (2), subject to (A), and the partial-wave formulas have been analytically derived. A global sign theorem for $\mathcal A(k)$, a positive certified value, or a resolution of the full endpoint problem has not been obtained in this note.

The floating-point computation (files [r22_scattering_check.py](../../computations/separated-cores/r22_scattering_check.py) and [r22_scattering_check.json](../../computations/separated-cores/r22_scattering_check.json)) gave the following values using angular channels through $m=40$:

| k | A(k), approximate |
|---:|---:|
| 0.10 | -2.8723616721 |
| 0.30 | -5.1109586391 |
| 0.50 | -8.4706010788 |
| 0.70 | -17.1605054973 |
| 0.85 | -43.3566559336 |
| 0.90 | -73.0791275967 |

The radial channel was negative and the higher angular channels positive. This targeted calculation found no positive coefficient. Agreement between finite angular cutoffs is numerical evidence, not interval certification or an all-$k$ sign theorem.
