# a uniform strict bound for the complete positive angular contribution

15 October 2026.

## Result and scope

Let Q be the unique positive decreasing radial solution of

$$
-Q''-r^{-1}Q'+Q-Q^3=0,\qquad Q'(0)=0,\qquad Q(\infty)=0.
$$

Use exactly the definitions of $\theta_m,b_m,B_{\rm sum},H_4$ in
[scattering-2cc19db4.md](scattering-2cc19db4.md). A validated computation, with analytic control of both
endpoints and of the infinite radial/angular/series tails, gives

$$
\boxed{\sup_{0<k<1}\log(1/k)H_4(k)<\frac{24}{25}<1.}
$$

Together with the radial comparison proved in R24,
$a_0(k)<-1/\log(1/k)$, this proves

$$
\boxed{\mathcal A(k)<-\frac{2\pi}{25\log(1/k)}<0
\quad(0<k<1).}
$$

The computer-assisted part is an interval enclosure of Q and positive profile
integrals. There is no sampled-sign inference. In particular, the finite
partition in k covers entire intervals by monotonicity. The theorem concerns
the unequal-well interaction coefficient defined in R22--R24. It does not
prove the arbitrary-potential Lieb--Thirring conjecture.

## Reproduction

The independent files are:

- [r25_interval_shoot.py](../../computations/all-scale-scattering/r25_interval_shoot.py): validated origin series and interval Taylor ODE solver;
- [r25_shoot_bracket.json](../../computations/all-scale-scattering/r25_shoot_bracket.json): overshoot/undershoot endpoints, including exact binary interval endpoints;
- [r25_shoot_2_2062008646507_2_2062008646508.json](../../computations/all-scale-scattering/r25_shoot_2_2062008646507_2_2062008646508.json): the Q enclosure to radius 8;
- [r25_uniform_certificate.py](../../computations/all-scale-scattering/r25_uniform_certificate.py): positive integral and complete-k verification;
- [r25_uniform_certificate.json](../../computations/all-scale-scattering/r25_uniform_certificate.json): numerical bounds from that verification.

Run, in order, from the workspace root:

```bash
cd computations/all-scale-scattering  # from the repository root
python r25_interval_shoot.py
python r25_interval_shoot.py 2.2062008646507,2.2062008646508 8 --enclose
python r25_uniform_certificate.py
```

The arithmetic is `mpmath.iv` at 60 decimal digits. The raw `_mpi_` tuples in
the shooting files preserve exact binary endpoints; the human-readable decimal
strings are descriptive only. The proof relies on the standard existence,
uniqueness, strict radial decrease, and shooting characterization of the
Townes solution, plus outward interval arithmetic and the identities below.

## 1. Validated initial value and the entire finite-radius profile

The two rational initial values are

$$
\alpha_-=2.2062008646507,\qquad
\alpha_+=2.2062008646508.
$$

The interval integration establishes an undershoot for $\alpha_-$: while
$0<Q<1$, the derivative becomes strictly positive at radius approximately
17.0258067798. It establishes an overshoot for $\alpha_+$: Q is strictly
negative at radius approximately 16.9158067798. The lower-parameter computation additionally checks Q>0 on every complete
Picard step tube, including the terminal step; the origin disk bound handles
[0,r0]. Thus no earlier zero can have been missed between output points.

Here is a self-contained shooting bracket argument. Call P the initial
parameters whose positive trajectory first turns upward, and N those whose
trajectory reaches zero. At a first upward turn, 0<Q<1 and
$E=Q'^2/2-Q^2/2+Q^4/4<0$. Since $E'=-Q'^2/r\le0$, a P-trajectory
can never subsequently reach zero, where E would be nonnegative. P and N
are disjoint open sets. The two computed endpoint parameters belong to
different sets, so connectedness gives an intervening parameter in neither.
Its trajectory stays positive and decreasing. Its limiting value must be 0
or 1. The latter is impossible: setting y=Q-1 and v=sqrt(r)y gives
$v''+[Q(Q+1)+1/(4r^2)]v=0$, which is oscillatory for sufficiently
large r and cannot remain positive. Hence this trajectory decays to zero,
and uniqueness identifies it with Q. No numerical central value is treated
as exact data.

### Origin error

Put $t=r^2$, $Q(r)=F(t)$. The regular equation is

$$
4(tF''+F')=F-F^3,
\qquad
c_{n+1}=\frac{c_n-(F^3)_n}{4(n+1)^2}.
$$

On the complex disk $|t|\le1/100$, the Volterra operator for F maps
$|F-\alpha|\le1/10$ strictly into itself, because $|\alpha|<2.21$ and

$$
\frac{1}{400}(2.31+2.31^3)<0.1,
\qquad
\frac{1}{400}(1+3\,2.31^2)<1.
$$

Its fixed point is analytic and bounded by 2.31. Cauchy's estimate consequently
bounds the coefficient tail. At $r_0=1/20$,
$z=r_0^2/(1/100)=1/4$. After coefficients $0,\ldots,N-1$, with N=70,

$$
|R_Q|\le\frac{2.31z^N}{1-z},
\qquad
|R_{Q'}|\le\frac{2r_0\,2.31}{1/100}
\left(\frac{Nz^{N-1}}{1-z}+\frac{z^N}{(1-z)^2}\right).
$$

Both are added as interval remainders, not estimated empirically.

### ODE steps

Write $q'=p$, $p'=q-q^3-p/r$. At each step, the code first finds a
rectangular tube on the whole time interval whose Picard image is contained
in itself. This validates existence and bounds every intermediate value.
The Taylor coefficients through order 19 are evaluated from the initial
interval. The coefficient of order 20 is evaluated over the whole validated
tube and time interval; multiplying it by $h^{20}$ gives the Lagrange
remainder enclosure. The recurrences are the exact polynomial recurrences
for $q-q^3-p/r$. Step sizes are at most .01, and at most r/20 near zero.

The same solver propagates the full initial interval
$[\alpha_-,\alpha_+]$ to R=8, producing 810 subintervals after including
$[0,r_0]$. Since the true Q decreases, its value at the left endpoint gives
an upper bound throughout each subinterval. The final enclosure is contained
in

$$
0.00041111268<Q(8)<0.00041117604.
$$

## 2. A global tail envelope preserving the exact exponential rate

The interval computation establishes the convenient global bound

$$
\boxed{Q(r)\le A K_0(r)\quad(r>0),\qquad A=2.82.}
$$

Here is the complete justification. Let $q_R$ be the certified upper bound
for Q(8), and take $\beta=0.9999999$. The checked inequality
$q_R^2<1-\beta^2$, radial decrease, and the exterior maximum principle give

$$
Q(r)\le q_R e^{-\beta(r-R)},\qquad r\ge R=8.
$$

Indeed Q is a subsolution for $-\Delta+\beta^2$, and the right side is a
supersolution with the correct boundary value.

Put $B=K_0$. The Wronskian identity gives

$$
(Q/B)'(r)=\frac{1}{rB(r)^2}\int_r^\infty sB(s)Q(s)^3\,ds>0.
$$

Since $(I_0/B)'=1/(rB^2)$, integration and the preceding rough exponential
bound yield

$$
A_\infty:=\lim_{r\to\infty}\frac{Q(r)}{B(r)}
\le\frac{q_R}{B(R)}+
q_R^3 e^R\left(\frac{R}{3\beta-1}+
\frac{1}{(3\beta-1)^2}\right).
$$

The bound used $I_0(s)\le e^s$ and discarded a nonnegative subtraction.
The Bessel integral representation, together with
$(1+x)^{-1/2}\ge1-x/2$, gives

$$
K_0(R)\ge\sqrt{\frac\pi{2R}}e^{-R}
\left(1-\frac1{8R}\right).
$$

Substitution with interval arithmetic bounds $A_\infty$ by
2.810012602, which is below 2.82. Since Q/B increases, this controls all
r, including the interior. Also
$K_0(r)\le\sqrt{\pi/(2r)}e^{-r}$, so

$$
Q(r)^2\le\frac{A^2\pi}{2r}e^{-2r}.
$$

## 3. Positive moments and exact finite-radius integration

Let $V_i$ be the squared upper bound for Q at the left endpoint of a profile
interval $[r_i,r_{i+1}]$. Define the upper moments

$$
\widehat\mu_n=
\sum_i V_i\frac{r_{i+1}^{2n+2}-r_i^{2n+2}}{2n+2}
+\frac{A^2\pi}{2}\int_8^\infty r^{2n}e^{-2r}\,dr.
$$

Every term is evaluated by intervals. These bound
$\mu_n=\int_0^\infty r^{2n+1}Q(r)^2dr$ from above. The integer incomplete
Gamma tail is evaluated by exact integration-by-parts recurrence. In scaled
form $t_n=\int_8^\infty r^{2n}e^{-2r}dr/(n!)^2$,

$$
t_0=\tfrac12e^{-16},\qquad
t_n=e^{-16}\left(\frac{8^n}{n!}\right)^2
\left(\frac12+\frac{n}{16}\right)
+\frac{2n-1}{2n}t_{n-1}.
$$

The zero-energy Hilbert--Schmidt constants are also bounded directly using
this upper profile. On one interval, with
$J_i=\int_0^{r_i}s^{2m+1}V(s)ds$, the inner integral is exactly

$$
J_i+V_i\frac{r^{2m+2}-r_i^{2m+2}}{2m+2}.
$$

Substituting it into the defining triangular double integral leaves only
powers and, for m=1, a logarithm. For the outer tail r>=8 use

$$
\int_8^\infty r^{1-2m}Q^2
\left(\int_0^r s^{2m+1}Q^2ds\right)dr
\le\widehat\mu_m\frac{A^2\pi e^{-16}}{4\,8^{2m}}.
$$

The resulting certified upper bounds are

| m | upper bound for $\theta_m$ |
|---|---:|
| 1 | 0.552721078 |
| 2 | 0.208489925 |
| 3 | 0.115422629 |
| 4 | 0.075467839 |

They are slightly larger than the floating-point values, as expected from
a piecewise constant upper envelope. The complete omitted angular sum still
uses the analytic bound $\theta_m\le\theta_1/m$, so there is no angular
cutoff error.

## 4. Entire Bessel series and its infinite tail

For n>=m,

$$
I_m(z)^2=\sum_{n=m}^\infty
\frac{(2n)!}{4^n(n!)^2(n-m)!(n+m)!}\,z^{2n}.
$$

Write $c_n=\binom{2n}{n}/4^n$,
$r_{nm}=(n!)^2/((n-m)!(n+m)!)$,
$d_m=1-\overline\theta_m$, and
$d_T=1-\overline\theta_1/5$. Write the true series as $H_4(k)=\sum_{n\ge1}h_n^{\rm true}k^{2n}$.
For each retained coefficient n<=512, an interval upper bound is

$$
h_n=\frac{\widehat\mu_n}{(n!)^2}
\left[\frac{1-c_n}{d_T}
+2c_n\sum_{m=1}^{\min(4,n)}r_{nm}
\left(\frac1{d_m}-\frac1{d_T}\right)\right].
$$

Although the displayed regrouping may have negative individual corrections,
the full bracket is positive: it is the sum of the positive angular
coefficients with their positive denominators. The program also checks its
interval lower endpoint is positive for every retained n. Each denominator
uses a certified upper norm, and the moment coefficients are positive;
therefore the bounds propagate in the required direction.

Keep n<=512. The global envelope from section 2 gives

$$
\frac{\mu_n}{(n!)^2}\le\frac{A^2\pi}{4}c_n
\le\frac{A^2\pi}{4}.
$$

Every true angular denominator is at least $1-\overline\theta_1$, so the
complete omitted tail of the **true H4 series** has the simple bound

$$
\sum_{n\ge513}h_n^{\rm true}k^{2n}
\le C\frac{k^{1026}}{1-k^2},\qquad
C=\frac{A^2\pi}{4(1-\overline\theta_1)}.
$$

The global bound in this last step applies directly to the true moments
$\mu_n$; it is not asserted for the piecewise-envelope moments
$\widehat\mu_n$. Only the first 512 coefficient bounds use those envelope
moments. No large-r truncation, truncated Bessel evaluation, or inferred floating
quadrature accuracy is used.

## 5. All k, including both endpoints

### Small k

Circle Poincare gives

$$
B_{\rm sum}(k)\le\frac{k^2}{2}
\int_0^\infty r^3Q(r)^2I_0(2kr)dr.
$$

The global envelope and $I_0(z)\le e^z$ imply

$$
H_4(k)\le\frac{A^2\pi k^2}
{16(1-\overline\theta_1)(1-k)^3}.
$$

For 0<k<=.01, the functions $k^2\log(1/k)$ and $(1-k)^{-3}$ increase.
The resulting uniform bound is less than 0.001657.

### Large k

The elementary angular Gaussian bound is

$$
I_0(z)\le\frac{\sqrt\pi}{2\sqrt{2z}}e^z.
$$

It follows by inserting $\cos\theta\le1-2\theta^2/\pi^2$ into the integral
representation and extending a Gaussian integral to infinity. Consequently

$$
H_4(k)\le
\frac{A^2\pi^2}{8(1-\overline\theta_1)\sqrt{2k(1-k)}}.
$$

Since $\log(1/k)\le(1-k)/k$, the log-weighted bound decreases with k.
For .997<=k<1 it is less than 0.853361.

### Compact interval: coverage, not sampling

H4 is increasing in k because every angular integral has positive power-series
coefficients. Partition [.01,.997] into the 987 exact intervals
$[j/1000,(j+1)/1000]$, j=10,...,996. If a<=k<=b, then

$$
\log(1/k)H_4(k)\le\log(1/a)H_4(b)
\le\log(1/a)\left(\sum_{n=1}^{512}\overline h_n b^{2n}
+C\frac{b^{1026}}{1-b^2}\right).
$$

Every right-hand side is evaluated as an interval and its upper endpoint is
checked strictly below the rational number 24/25. The largest upper endpoint is

$$
0.9593178247384492449276873154329\ldots,
$$

on the interval [.856,.857]. Combining the three regions proves the boxed
uniform strict bound.

## What this resolves

R24 left a single quantitative hypothesis before its angular sum argument
could determine the complete sign of the fixed unequal-scale interaction.
The present certificate supplies that hypothesis for every 0<k<1. The result
therefore rules out positive interaction by this coefficient at every fixed
unequal scale ratio, rather than at finitely many sampled ratios or only near
the two endpoints. Joint limits in which scale ratio and separation vary
together still require the corresponding uniform interaction expansion; the
arbitrary-rank and strong-overlap optimization problems are distinct.
