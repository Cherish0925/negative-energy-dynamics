# Exact negative-spectrum count for finitely many distant two-dimensional wells

2026-10-15. This note proves the count at the spectral threshold, including
arbitrarily shallow eigenvalues. The proof uses the standard
Birman--Schwinger principle and the two-dimensional logarithmic resolvent
expansion. Historical priority for this particular formulation has not been
investigated; no novelty claim is made.

## 1. Statement

Let `W_j`, `1<=j<=N`, be fixed nonzero, nonnegative, bounded potentials on
`R^2`, with

$$
 0\le W_j(x)\le C_j e^{-\sigma_j|x|},\qquad \sigma_j>0.
$$

Assume each operator `-Delta-W_j` has exactly one negative eigenvalue,
counted with multiplicity, and no nonzero bounded distributional solution
at zero energy. Fix pairwise distinct vectors `a_1,...,a_N` in `R^2` and
put

$$
 V_R(X)=\sum_{j=1}^N W_j(X-Ra_j),\qquad H_R=-\Delta-V_R.
$$

**Theorem.** There exists `R_0<infinity` such that for every `R>=R_0`,
`H_R` has exactly `N` negative eigenvalues, counted with multiplicity,
and no nonzero bounded distributional zero-energy solution.

The shapes may have different fixed widths and strengths, and need not be
radial. The number of wells and the vectors `a_j` are fixed. The proof does
not assert uniformity as a width or a single-well spectral parameter
varies simultaneously with `R`.

More generally, if the j-th well has `n_j` negative eigenvalues and remains
regular at zero in the same bounded-solution sense, the total negative
count is exactly `sum_j n_j` for sufficiently large `R`.

## 2. Single-well compression at zero energy

Write

$$
 w_j=\sqrt{W_j},\quad m_j=\|w_j\|_2^2>0,
 \quad e_j=w_j/\sqrt{m_j},
 \quad P_j=I-|e_j\rangle\langle e_j|.
$$

The logarithmic operator

$$
 K_j(x,y)=-\frac1{2\pi}w_j(x)\log|x-y|w_j(y)
$$

is Hilbert--Schmidt, since the local logarithmic singularity is square
integrable and the multiplication weights decay exponentially. The free
resolvent expansion is, in operator norm,

$$
 w_j(-\Delta+\alpha^2)^{-1}w_j
   =a_\alpha|w_j\rangle\langle w_j|+K_j+o(1),
 \quad
 a_\alpha=\frac{\log(1/\alpha)+\log2-\gamma_E}{2\pi}.
 \tag{2.1}
$$

On `w_j^perp`, set

$$
 \Gamma_j=P_j(I-K_j)P_j.
$$

For a one-bound-state well,

$$
 \Gamma_j\ge c_j I>0. \tag{2.2}
$$

Indeed a strictly negative direction of `Gamma_j`, together with `w_j`,
would give two negative directions of the complement in (2.1) for small
`alpha`, contrary to the Birman--Schwinger count. If instead
`Gamma_j f=0`, `f perpendicular to w_j`, then `(I-K_j)f=cw_j`. The
function

$$
 \psi(x)=c-\frac1{2\pi}\int\log|x-y|w_j(y)f(y)\,dy
$$

satisfies `w_j psi=f` and `(-Delta-W_j)psi=0`. Its logarithmic coefficient
vanishes because `int w_j f=0`; the exponential weights make it bounded.
The assumed absence of bounded zero solutions forces `f=0`. As an
identity minus compact operator, a nonnegative injective `Gamma_j` has
the strict lower bound (2.2).

For the more general single-well count `n_j`, the same kernel argument
proves invertibility of `Gamma_j`, without requiring positivity. Taking a
Schur complement in (2.1) then shows

$$
 \operatorname{ind}_{-}\Gamma_j=n_j-1. \tag{2.3}
$$

## 3. Exact channel representation

On `Hcal=direct-sum_j L^2(R^2)`, define

$$
 (A_R\psi)_j(x)=w_j(x)\psi(x+Ra_j).
$$

Then `A_R^*A_R` is multiplication by `V_R`. Consequently the positive
compact Birman--Schwinger operator

$$
 \mathcal K_{\alpha,R}=A_R(-\Delta+\alpha^2)^{-1}A_R^*
$$

has block kernel

$$
 (\mathcal K_{\alpha,R})_{ij}(x,y)
  =w_i(x)G_\alpha(R(a_i-a_j)+x-y)w_j(y),
$$

where `G_alpha(z)=(2*pi)^(-1)K_0(alpha|z|)`. The exact count is

$$
 N(H_R<-\alpha^2)
   =\operatorname{ind}_{-}(I-\mathcal K_{\alpha,R}).
 \tag{3.1}
$$

The representation may contain redundant channel vectors. They add
eigenvalues zero to the Birman--Schwinger operator, hence positive
eigenvalues one to its complement; they do not affect (3.1).

For each **fixed** `R`, take `alpha` to zero. With
`v=(w_1,...,w_N)`, one obtains

$$
 \mathcal K_{\alpha,R}
   =a_\alpha|v\rangle\langle v|+\mathcal K_R^0+o_R(1),
 \tag{3.2}
$$

where the diagonal blocks of `K_R^0` equal `K_j`, and the off-diagonal
blocks are

$$
 (\mathcal K_R^0)_{ij}(x,y)
 =-\frac1{2\pi}w_i(x)
       \log|R(a_i-a_j)+x-y|w_j(y). \tag{3.3}
$$

No simultaneous uniform limit in `alpha` and `R` is used.

## 4. Cross-well convergence, including the moving singularity

For fixed nonzero `d=a_i-a_j`, let

$$
 \ell_R=\frac{\log R}{2\pi},\qquad
 c_{ij}=\frac{\log|a_i-a_j|}{2\pi}.
$$

The required norm expansion is

$$
 (\mathcal K_R^0)_{ij}
  =-(\ell_R+c_{ij})|w_i\rangle\langle w_j|
       +E_{ij,R},\qquad
 \|E_{ij,R}\|_{\rm HS}=O(R^{-1}). \tag{4.1}
$$

Here is a proof that explicitly controls the logarithmic singularity
moving to `x-y=-Rd`. The squared Hilbert--Schmidt norm, apart from
`(2*pi)^(-2)`, is

$$
 \int_{\mathbb R^2}D_{ij}(s)
   \left|\log|Rd+s|-\log(R|d|)\right|^2ds,
$$

where

$$
 D_{ij}(s)=\int W_i(x)W_j(x-s)\,dx.
$$

Exponential decay and `|x|+|x-s|>=|s|` imply
`D_ij(s)<=C exp(-c|s|)` after reducing the exponential rate. On
`|s|<=R|d|/2`, the mean value theorem gives

$$
 \left|\log|Rd+s|-\log(R|d|)\right|
     \le\frac{2|s|}{R|d|}.
$$

Its weighted squared integral is therefore `O(R^(-2))`.

On the complementary tail, split off the unit disk `|Rd+s|<1`. There,
`D_ij(s)<=C exp(-c(R|d|-1))`, and after changing variables `t=Rd+s`,

$$
 \int_{|t|<1}\left|\log|t|-\log(R|d|)\right|^2dt
     \le C(1+\log^2 R).
$$

Outside that disk, both logarithms are bounded by a polynomial in
`R+|s|`, so their weighted tail integral is exponentially small in `R`.
This proves (4.1). In particular it is not necessary to pretend that the
Taylor expansion of the logarithm holds near its moving singularity.

For any fixed finite configuration the estimates are uniform over its
finitely many pairs. They are also uniform for `a_j` in a bounded family
with a positive lower bound on all pair separations.

## 5. Relative charges and bounded coupling to the neutral subspace

Let `P` be the orthogonal projection onto `v^perp` and define

$$
 \Gamma_R=P(I-\mathcal K_R^0)P\big|_{v^\perp}.
$$

Decompose this Hilbert space orthogonally as

$$
 v^\perp=\mathcal E\oplus\mathcal Z,
 \qquad \mathcal Z=\bigoplus_{j=1}^N w_j^\perp,
$$

where

$$
 \mathcal E=\left\{f_j=b_je_j:\quad
      \sum_j\sqrt{m_j}\,b_j=0\right\},
 \qquad \dim\mathcal E=N-1.
$$

Set `c_j=sqrt(m_j)b_j`. The logarithmically large off-diagonal
part of `K_R^0` has quadratic form

$$
 -\ell_R\sum_{i\ne j}\overline{c_i}c_j
 =\ell_R\sum_j|c_j|^2,
       \qquad \sum_j c_j=0. \tag{5.1}
$$

Hence its complement on `E` is strictly negative with size proportional
to `log R`:

$$
 (\Gamma_R)_{\mathcal EE}
       \le-\ell_R\min_j(m_j)I+C I. \tag{5.2}
$$

All explicit rank-one cross terms in (4.1) vanish after compression to
`Z`, so

$$
 (\Gamma_R)_{\mathcal ZZ}
       =\bigoplus_j\Gamma_j+O(R^{-1}). \tag{5.3}
$$

The large logarithmic terms also give **zero** coupling between `E` and
`Z`: every left and right factor is one of the `w_j`. The diagonal
operators `K_j` have fixed bounded norm, the constants `c_ij` are fixed,
and the remainders tend to zero. Thus

$$
 \|(\Gamma_R)_{\mathcal EZ}\|\le C. \tag{5.4}
$$

In the one-bound-state case, (5.3) is uniformly positive. Taking its
Schur complement subtracts a bounded nonnegative operator from the
negative finite block (5.2). For large `R` the Schur complement is
negative definite. By the exact block inertia identity, `Gamma_R` is
invertible and has exactly `N-1` negative eigenvalues.

For general `n_j`, (5.3) is uniformly invertible, with negative index
`sum_j(n_j-1)`. The Schur correction is bounded even if its sign is
indefinite, and (5.2) still dominates it. Hence

$$
 \operatorname{ind}_{-}\Gamma_R
    =\sum_j(n_j-1)+(N-1)=\sum_jn_j-1, \tag{5.5}
$$

and `Gamma_R` is invertible. The argument uses a bounded invertible
triangular congruence, so it gives the exact inertia, not only an upper
or lower estimate for the count.

## 6. Adding the total charge counts every negative level

Fix any sufficiently large `R`. By (3.2), the compression of
`I-K_alpha,R` to `v^perp` converges in norm to the invertible `Gamma_R`.
It therefore has the same negative index for all sufficiently small
`alpha`. Its coupling to the remaining scalar direction `span{v}` is
bounded at this fixed `R`. The last scalar Schur complement is

$$
 -a_\alpha\|v\|_2^2+O_R(1)<0.
$$

It supplies exactly one additional negative direction. Equation (3.1)
therefore gives

$$
 N(H_R<-\alpha^2)=\sum_j n_j
$$

for every sufficiently small positive `alpha` at this `R`. This proves
the total negative count. Any additional negative eigenvalue, however
close to zero, would be counted by choosing `alpha` below its square-root
absolute energy. In particular the proof leaves no uncounted
exponentially shallow level.

## 7. Absence of bounded zero-energy solutions

Suppose `H_R psi=0` and `psi` is bounded. At fixed `R`,
`g=V_R psi` is bounded and exponentially integrable. For its circular mean
`a(r)=(2*pi)^(-1)int psi(r,theta)dtheta`, the equation gives

$$
 r a'(r)=-\frac1{2\pi}\int_{|X|<r}g(X)\,dX.
$$

Boundedness therefore forces `int g=0`; otherwise the circular mean has
a nonzero logarithmic growth coefficient. The Newton potential

$$
 n(X)=-\frac1{2\pi}\int\log|X-Y|g(Y)\,dY
$$

is now bounded and tends to zero at infinity. The difference `psi-n` is
a bounded harmonic function on the whole plane and is constant. With
`f=A_R psi`, this representation becomes

$$
 \langle v,f\rangle=0,
 \qquad (I-\mathcal K_R^0)f=c v.
$$

Consequently `Gamma_R f=0`. Its invertibility forces `f=0`. Then `psi`
is a constant satisfying `V_R psi=0`; because the potential is nonzero,
`psi=0`. This handles zero eigenfunctions as well as bounded threshold
resonances.

## 8. Consequence for the R22 Townes interaction

The analytic single-well result established in R23 applies to

$$
 W_1(x)=Q(x)^2,\qquad W_2(x)=k^2Q(kx)^2
$$

for every **fixed** `0<k<1`. Scaling preserves the one-negative-level
count and absence of bounded zero solutions. For

$$
 H_{R,k}=-\Delta-Q(x)^2-k^2Q(k(x-Re_1))^2,
$$

the theorem proves that the two levels used in R22 exhaust the negative
spectrum whenever `R` is sufficiently large, with the required distance
allowed to depend on `k`. Therefore the R22 expansion upgrades exactly
to the full negative spectral trace:

$$
 \boxed{
 \operatorname{Tr}(H_{R,k})_-
  -\frac1{2M}\int\left[Q(x)^2+k^2Q(k(x-Re_1))^2\right]^2dx
  =\epsilon_R^2\mathcal A(k)+o_k(\epsilon_R^2).
 }
$$

Here `epsilon_R` and `A(k)` have precisely the normalization in
[relaxed-unequal-wells.md](../separated-cores/relaxed-unequal-wells.md), and `Tr(H)_-` denotes the sum of absolute
values of all negative eigenvalues. No eigenvalue or eigenfunction
expansion was needed for the count itself.

Thus, once `A(k)<0` is established for a fixed `k`, a hidden shallow
level cannot reverse the negative sign of the full trace defect in this
distant-well family. A proof for every fixed ratio still does not give a
uniform theorem for `k=k(R)` approaching zero or one, strongly
overlapping self-consistent wells, or the arbitrary-potential sharp
Lieb--Thirring inequality.

## 9. Relation to the previous scale-hierarchy count

The logical organization agrees with [full-spectrum.md](full-spectrum.md) and its
independent verification. The new technical input required for distance
separation is (4.1), including the moving logarithmic singularity. The
finite-dimensional charge form is (5.1), rather than the partial-sum
form arising from an ordered scale hierarchy. Both arguments take the
threshold limit only after fixing the geometric parameters.

This is a proved consequence of the displayed estimates and standard
spectral tools. Its historical originality has not been established.
