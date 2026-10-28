# A sharp obstruction to the Townes-calibrated gradient correction

The proposed universal inequality

$$
T+\eta W\ge (1+\eta)K_1F,\qquad
W=\int |\nabla\sqrt\rho|^2,\quad K_1=M_c/2,
\tag{1}
$$

is false for **every fixed $\eta>0$**, already for two real orthonormal
orbitals. In particular, choosing $\eta=2\pi/K_1-1$ does not provide a
route from a semiclassical coefficient $2\pi$ to the sharp planar
conjecture. This does not disprove the planar conjecture itself.

The proof is analytic and uses two separated Townes profiles, followed by
exact orthonormalization. It does not require a numerical Townes profile,
the numerical value of $M_c$, or an unproved sharp inequality at rank two.

## 1. Exact orthonormal family and identities

Let $q=Q/\sqrt{M_c}$, where the positive radial decreasing Townes solution
satisfies

$$
-\Delta q+q=M_cq^3,\qquad
\int q^2=\int |\nabla q|^2=1,\qquad
\int q^4=2/M_c.
$$

For $R>0$, set

$$
u(x)=q(x-Re_1/2),\qquad v(x)=q(x+Re_1/2),
$$

$$
s=\int uv,\qquad J=\int u^3v=\int uv^3,\qquad
I=\int u^2v^2.
$$

The equality defining $J$ follows from reflection symmetry. Since
$0<s<1$, the two functions

$$
\psi_+=\frac{u+v}{\sqrt{2(1+s)}},\qquad
\psi_-=\frac{u-v}{\sqrt{2(1-s)}}
\tag{2}
$$

are exactly orthonormal. Their density is positive everywhere:

$$
\rho=\frac{u^2+v^2-2suv}{1-s^2}.
\tag{3}
$$

Integration by parts in the equation for $u$ gives
$\int\nabla u\cdot\nabla v=M_cJ-s$. Consequently,

$$
T=\frac{2(1+s^2-M_csJ)}{1-s^2},
$$

$$
F=\frac{4/M_c+2I-8sJ+4s^2I}{(1-s^2)^2}.
$$

Thus the exact sharp-constant deficit is

$$
D:=T-K_1F
=\frac{M_c\{2sJ(1+s^2)-I(1+2s^2)\}-2s^4}
 {(1-s^2)^2}.
\tag{4}
$$

For any real two-component vector $(f,g)$, the elementary amplitude
identity is

$$
|\nabla f|^2+|\nabla g|^2
-|\nabla\sqrt{f^2+g^2}|^2
=\frac{|f\nabla g-g\nabla f|^2}{f^2+g^2}.
$$

The determinant of the linear change $(u,v)\mapsto(\psi_+,\psi_-)$
has squared modulus $(1-s^2)^{-1}$. Hence

$$
G:=T-W
=\int\frac{|u\nabla v-v\nabla u|^2}
 {u^2+v^2-2suv}.
\tag{5}
$$

Equations (4) and (5) are exact; in particular no near-orthogonality
approximation is being substituted for the constraint.

## 2. The two different interaction scales

The standard exterior comparison argument gives, for every $0<\sigma<1$,

$$
q(r)\le C_\sigma e^{-\sigma r},\qquad
q(r)\ge c r^{-1/2}e^{-r}\quad(r\ge r_0).
\tag{6}
$$

For completeness, compare with the decaying radial solutions
$K_0(\sigma r)$ and $K_0(r)$, where $K_0$ is the modified Bessel
function. Outside a sufficiently large disk,
$( -\Delta+\sigma^2)q=(M_cq^2-1+\sigma^2)q\le0$, while
$( -\Delta+1)q=M_cq^3\ge0$. Boundary comparison and decay at infinity
give the upper and lower bounds, using
$K_0(r)\asymp r^{-1/2}e^{-r}$. The upper bound can be enlarged to all
$r\ge0$.

Take $\sigma=7/8$ and $\tau=3/4$. If $r_u,r_v$ denote distances
to the two centers, then $r_u+r_v\ge R$, and

$$
e^{-\sigma(r_u+r_v)}
\le e^{-\tau R}e^{-(\sigma-\tau)r_u}.
$$

After integration this proves

$$
s\le Ce^{-3R/4},\qquad J\le Ce^{-3R/4}.
$$

Here the second estimate also follows directly from
$J\le\|q\|_\infty^2s$. For sufficiently large $R$, discard the
nonpositive terms in (4) to obtain the one-sided bound

$$
D\le Ce^{-3R/2}.
\tag{7}
$$

No assumption $D\ge0$ is used or needed.

In contrast, (5) has a larger contribution from the middle of the gap
between the profiles. On the fixed rectangle
$\Omega=\{|x_1|\le1,\ |x_2|\le1\}$, both radii equal $R/2+O(1)$.
By (6),

$$
\min(u^2,v^2)\ge cR^{-1}e^{-R}\quad\hbox{on }\Omega.
\tag{8}
$$

Also $-q'(r)/q(r)\ge1/\sqrt2$ for all sufficiently large $r$.
Indeed $M_cq^2\le1/2$ there, radial monotonicity yields
$q''=q-M_cq^3-q'/r\ge q/2$, and multiplication by $q'<0$, followed
by integration to infinity, gives $q'(r)^2\ge q(r)^2/2$.
The two radial directions have opposite horizontal components on
$\Omega$, bounded away from zero as $R\to\infty$. Therefore

$$
|\partial_1\log u-\partial_1\log v|\ge c>0
\quad\hbox{on }\Omega.
$$

Since $s,u,v\ge0$, equation (5) implies

$$
G\ge c\int_\Omega\frac{u^2v^2}{u^2+v^2}
\ge c'R^{-1}e^{-R}.
\tag{9}
$$

Only a fixed rectangle was used; a wider transverse strip would give a
stronger lower bound, which is unnecessary here.

## 3. Contradiction and its exact scope

The deficit in (1) is

$$
T+\eta W-(1+\eta)K_1F=(1+\eta)D-\eta G.
$$

Combining (7) and (9), for each fixed $\eta>0$,

$$
T+\eta W-(1+\eta)K_1F
\le C(1+\eta)e^{-3R/2}-c\eta R^{-1}e^{-R}<0
$$

for all sufficiently large $R$. This proves the assertion.

One consequence is more general than the single proposed coefficient:
if a universal bound $T+\eta W\ge AF$, with $\eta>0$, were to
recover the sharp conjecture solely by $W\le T$, it would require
$A\ge(1+\eta)K_1$. The counterexample excludes every such choice.
Allowing a larger $\eta$ with $A=2\pi$ may give a true nonsharp
inequality, but the resulting coefficient $A/(1+\eta)$ is then
strictly below $K_1$.

The mechanism is specific and relevant: the Fisher information of the
combined density loses an order-$e^{-R}$ contribution in the region
where two exponentially small tails mix. The orthonormal projection's
sharp kinetic deficit changes only at a smaller scale. Consequently,
even a two-variable bound calibrated to a single Townes profile must
also respect this separated-profile boundary.

There is a quantitative restriction on possible nonlinear replacements.
The same upper-bound argument gives $D\le C_\tau e^{-2\tau R}$ for every
$\tau<1$, whereas $G\ge cR^{-1}e^{-R}$, and $T\to2$.
For any $0<p<2$, choose $p/2<\tau<1$. It follows that

$$
\limsup_{R\to\infty}\frac{D\,T^{p-1}}{G^p}\le0.
\tag{10}
$$

Thus no universal positive remainder
$T-K_1F\ge c(T-W)^p/T^{p-1}$ can hold for any $p<2$. A quadratic
remainder is not excluded by this construction, but is not proved here.
Equivalently, a differentiable universal envelope
$F/T\le f(W/T)$, calibrated by $f(1)=1/K_1$, cannot have
$f'(1)>0$: on this family the approach of $F/T$ to $1/K_1$ is
of smaller order than the approach of $W/T$ to one.

These orbitals have not been shown to form a self-consistent optimizing
state. Thus the calculation does **not** exclude an inequality restricted
to actual minimal violating optimizers. Proving such a restricted
statement would have to use their common scalar potential, stationarity,
or second variation; the unrestricted $(T,F,W)$ route above does not
provide it.

The complete two-dimensional sharp orthonormal inequality remains
unproved by this note. No historical priority is claimed for this
counterexample formulation.

## 4. Precise equal-scale comparison with the existing binding expansion

Write $q(r)\sim A r^{-1/2}e^{-r}$. The exact kinetic deficit was already
calculated in [two-core.md](../separated-cores/two-core.md), Sections 1–2. In that note the deficit
was normalized as $K_1^{-1}T-F$; converting its formula gives

$$
D=T-K_1F\sim8\pi A^4e^{-2R}>0.
\tag{11}
$$

In particular this pair does not violate the sharp planar inequality:
its eventually positive deficit is too small to support the proposed
linear gradient correction. We now calculate the corresponding
directional energy, which was not needed for the R22 binding result:

$$
\boxed{G=T-W\sim\sqrt2\,\pi^{3/2}A^2R^{-1/2}e^{-R}.}
\tag{12}
$$

Here is a global dominated-convergence proof, including the regions
outside the middle of the two cores. Put $x_1=t$, $x_2=\sqrt R\,z$,
with centers at $\pm Re_1/2$. At every fixed $(t,z)$,

$$
u^2\sim\frac{2A^2}{R}e^{-R}e^{2t-2z^2},\qquad
v^2\sim\frac{2A^2}{R}e^{-R}e^{-2t-2z^2}.
$$

Moreover $q'/q\to-1$, so
$|\nabla\log u-\nabla\log v|^2\to4$. This derivative limit follows
also directly by integrating the radial equation:
$-rq'(r)=\int_r^\infty s(q-M_cq^3)\,ds$, then using the displayed
tail of $q$. The logarithmic derivative is bounded on the whole
half-line, by positivity, smoothness, and its limit at infinity.
Since $s\to0$, the integrand $g_R$ in (5) satisfies

$$
R e^R g_R(t,\sqrt Rz)
\longrightarrow4A^2e^{-2z^2}\operatorname{sech}(2t).
\tag{13}
$$

For domination, the bounded logarithmic derivative and $s\le1/2$
give $g_R\le C\min(u^2,v^2)$. The global estimate
$q(r)^2\le C(1+r)^{-1}e^{-2r}$ therefore yields

$$
R e^R g_R(t,\sqrt Rz)
\le C\exp\!\left[R-2\sqrt{(R/2+|t|)^2+Rz^2}\right].
$$

The negative of this exponent is at least both $2|t|$ and
$\sqrt{R^2+4Rz^2}-R$. For $R\ge1$, the latter is at least
$\sqrt{1+4z^2}-1$. Averaging the two bounds gives the integrable
majorant

$$
C e^{-|t|}\exp[-(\sqrt{1+4z^2}-1)/2].
$$

Thus (13) can be integrated over all $(t,z)$. Since the Jacobian is
$\sqrt R$,

$$
\lim_{R\to\infty}\sqrt R\,e^R G
=4A^2\left(\int_{\mathbb R}\operatorname{sech}(2t)dt\right)
\left(\int_{\mathbb R}e^{-2z^2}dz\right)
=\sqrt2\pi^{3/2}A^2,
$$

proving (12). Combining with the already established (11),

$$
\boxed{\frac{D}{G^2}\sim\frac{4R}{\pi^2},\qquad
\frac{DT}{G^2}\sim\frac{8R}{\pi^2}.}
\tag{14}
$$

The first ratio uses the fixed inverse width of the profiles; the second
is invariant under common planar dilation, with $R$ interpreted as
separation in units of that width. This identifies the precise
distinction: orthogonalization produces a positive binding-scale
deficit of order $e^{-2R}$, while mixing the density tails changes
its Fisher information at order $R^{-1/2}e^{-R}$. A quadratic
correction is consistent with this particular family, but any positive
correction of smaller power is inconsistent with it. No universal
quadratic estimate follows from (14).
