# Proof of the finite-hierarchy eigenvalue count

15 October 2026. Checked against [full-spectrum.md](full-spectrum.md), with the Townes
single-well statement checked against [scattering-sign.md](../townes-spectral-structure/scattering-sign.md) and the
two-eigenvalue asymptotics checked against [hierarchical-wells.md](../townes-spectral-structure/hierarchical-wells.md).

## Conclusion

The argument in [full-spectrum.md](full-spectrum.md) proves the stated exact count for any
fixed finite hierarchy of the specified wells. I find no missing sign,
scale factor, compactness assumption, or interchange of the energy and
scale limits in that argument. The proof also excludes nonzero bounded
distributional zero-energy solutions. For the Townes pair this makes the
previous two-level sum the full negative spectral trace.

The hypotheses are material: every separate well is nonzero, nonnegative,
bounded, exponentially decaying, has exactly one negative eigenvalue, and
has no nonzero bounded zero-energy solution. The number of wells, shapes,
and scaled centers are fixed. The required scale separation can depend on
all of them. This is not a statement for comparable scales, arbitrary
scale-dependent centers, infinitely many wells, or the full sharp
Lieb--Thirring optimization problem.

## 1. The compressed single-well operator

Write `w=sqrt(W)`, `e=w/||w||_2`, and

    K(x,y)=-(2 pi)^(-1) w(x) log|x-y| w(y).

The local logarithmic singularity is square integrable in two dimensions.
Boundedness and exponential decay of W therefore make K Hilbert--Schmidt.
Let `P=I-|e><e|`. The free resolvent expansion is

    w(-Delta+alpha^2)^(-1)w
      = a_alpha |w><w| + K + o(1),
    a_alpha=(log(1/alpha)+log 2-EulerGamma)/(2 pi).

If `P(I-K)P` had a negative direction f, the restriction of the complement
of this Birman--Schwinger operator to `span{e,f}` would be negative definite
for small alpha: its first diagonal entry tends to minus infinity, its
second tends to a strictly negative number, and its off-diagonal entries
remain bounded. This would give two negative eigenvalues of `-Delta-W`.

If instead `P(I-K)P f=0`, then `(I-K)f=cw`. The function

    psi(x)=c-(2 pi)^(-1) int log|x-y| w(y)f(y) dy

satisfies `w psi=f`, hence `(-Delta-W)psi=0`. Its logarithmic coefficient
vanishes because `<w,f>=0`. The source `wf` has exponential L1 moments
and exponentially weighted L2 bounds, so the logarithmic potential is
bounded. The assumed absence of bounded zero solutions gives f=0.
An identity-minus-compact nonnegative operator with trivial kernel has a
strict positive lower bound. Thus the asserted coercivity follows.

This step does not assume positivity of K on the entire Hilbert space.
That would be an unwarranted replacement for the preceding argument.

## 2. Channel redundancy and the exact scaling

For the pair, the broad channel is

    (A_2 psi)(y)=b(y)psi(y/k),
    (A_2^*f)(x)=k^2 b(kx)f(kx).

Consequently `A_2^*A_2=k^2 B(kx)`, and its Birman--Schwinger block is
exactly `b(y)G_alpha((y-y')/k)b(y')`, with no additional k or k^2 factor.
The cross block in the note follows from the same adjoint calculation.

The channel representation need not be injective or surjective. The
nonzero spectra of `A R_0 A^*` and `R_0^(1/2)A^*A R_0^(1/2)` agree,
including multiplicities. Additional zero eigenvectors of the former
become eigenvectors with eigenvalue +1 for its complement, so cannot alter
the negative-index calculation.

The resolvent expansion is applied at each fixed collection of scales.
There is no need to estimate its remainder uniformly as a scale tends to
zero together with alpha.

## 3. Cross-kernel convergence, including the moving singularity

The squared Hilbert--Schmidt error is

    (4 pi^2)^(-1) int W(x) F(kx) dx,
    F(a)=int B(y)|log|y-a|-log|y||^2 dy.

Translation continuity in local L2 proves `F(a)->0`. The singular disk
`|y-a|<1` is controlled by `||B||_infinity int_{|t|<1}log^2|t| dt`.
On its complement the logarithm is bounded by a constant times
`1+|y|+|a|`. This gives `F(a)<=C(1+|a|^2)` and a genuine integrable
dominator `C W(x)(1+|x|^2)` for `0<k<=1`. Thus the changing singularity
does not invalidate dominated convergence.

For fixed scaled translations the same proof applies after shifting the
broad variable. Its constants are uniform for translations in a fixed
compact set; it gives no such uniformity for centers escaping to infinity.

## 4. Relative-charge sign and the finite-dimensional identity

For two wells, in the normalized relative vector used in the note, the
two charges are

    c_1= sqrt(m_W m_B/(m_W+m_B)),  c_2=-c_1.

The logarithmically large part of K has quadratic form
`-ell(2 c_1 c_2+c_2^2)=ell m_W m_B/(m_W+m_B)`.
The complement `I-K` therefore has the negative sign and exactly the
coefficient displayed in equation (5.2).

For N wells let `L_j=-log k_j`, `c_j=sqrt(m_j)a_j`, and `sum c_j=0`.
Writing

    max(L_i,L_j)=L_1+sum_l (L_{l+1}-L_l)1_{max(i,j)>l}

gives

    -sum_{i,j} max(L_i,L_j) conjugate(c_i)c_j
       =sum_{l=1}^{N-1}(L_{l+1}-L_l)|sum_{i<=l}c_i|^2.

There is no factor 2 missing. The identity holds for complex charges too.
The partial-sum map is injective on the zero-total-charge space and hence
has a positive smallest singular value there for fixed N and masses.
This proves strict negativity of the complement on the relative block
when every adjacent logarithmic gap is large.

On `Z=direct-sum w_j-perp`, every large logarithmic term vanishes. The
limits of the cross kernels also vanish after compression to Z, since one
factor is w_i. The remaining block is uniformly positive. Its coupling
to the relative block is bounded, so the exact Schur complement subtracts
a bounded nonnegative operator from an already negative definite relative
block. This proves exactly N-1 negative directions and invertibility.

## 5. The total logarithmic direction and arbitrarily shallow levels

At fixed sufficiently separated scales, add back the total charge vector
`v=(w_1,...,w_N)`. The compressed block converges in norm to the invertible
operator just analyzed; its negative index is N-1 for small alpha. The
remaining scalar Schur complement is

    -a_alpha ||v||_2^2+O(1),

and hence negative. The Birman--Schwinger principle gives exactly N
eigenvalues below `-alpha^2` for every sufficiently small positive alpha.
This proves the total negative count: any extra negative eigenvalue,
however close to zero, would be counted by choosing alpha still smaller.

The conclusion therefore does not leave a possible family of exponentially
shallow negative levels uncounted.

## 6. A direct proof of the bounded zero-energy assertion

One explanatory phrase in the source note should be sharpened: for an
exponentially decaying, noncompact potential the solution is not literally
harmonic on an exterior region. A circular-mean argument gives the needed
conclusion without that phrase.

Suppose `(-Delta-V)psi=0` and psi is bounded. Put `g=V psi`; g is bounded
and exponentially integrable. Local elliptic regularity permits taking the
circular mean `a(r)=(2 pi)^(-1)int psi(r,theta)dtheta`. It obeys

    r a'(r)=-(2 pi)^(-1) int_{|x|<r} g(x) dx.

If `G=int g` were nonzero, this identity and exponential decay would give
`a(r)=-(G/(2 pi))log r+O(1)`, contrary to boundedness. Hence G=0. The
logarithmic Newton potential

    n(x)=-(2 pi)^(-1)int log|x-y| g(y)dy

is now bounded and tends to zero at infinity. The difference `psi-n` is
bounded and harmonic on the entire plane, hence constant. Passing to
channel variables gives precisely

    <v,f>=0,  (I-K^0)f=c v.

Invertibility of the compressed operator forces f=0. The remaining psi is
a constant with `V psi=0`, and V is nonzero, so psi=0.

This supplies the stated exclusion of all bounded distributional zero
solutions, including bounded angular zero solutions and L2 zero modes.

## 7. Full trace for the Townes pair

The independent count requires no eigenvalue expansion. Once applied to
the Townes pair it proves that the two eigenvalues expanded in R23 exhaust
the negative spectrum. Their expansions give

    Tr(H_k)_-=1+k^2 Q(z)^2+k^2
       -2 pi k^2 q(z)^2/|log k|
       +O_z(k^2/|log k|^2).

The potential term uses `int Q^4=2M` and

    int Q(x)^2 Q(kx-z)^2 dx = M Q(z)^2+O_z(k^2).

The linear Taylor term vanishes by radiality of Q^2. Thus

    (2M)^(-1)int V_k^2=1+k^2+k^2 Q(z)^2+O_z(k^4),

and subtraction gives the stated strictly negative full-trace defect.
The positivity `q(z)>0` supplies strictness for fixed z, and its positive
minimum on compact sets supplies the compact-center uniformity.

For a hierarchy with more than two wells, the proof establishes the full
negative count and excludes bounded zero solutions. It does not, by itself,
establish a sign for the full Lieb--Thirring defect of that hierarchy.

## 8. Derivation of the general bound-state counts

Section 8 of [full-spectrum.md](full-spectrum.md) was added after the preceding checks.
Its extension to `n_j` negative eigenvalues in each well is valid under
the stated absence of bounded zero-energy solutions.

The kernel construction in Section 1 above never used nonnegativity of
Gamma. Therefore each `Gamma_j` is still injective. Because it is a
selfadjoint identity-minus-compact operator, it is invertible with a
positive distance between its spectrum and zero, and it has finite
negative index. Let that index be `d_j`. For sufficiently small alpha,
the compression of the free Birman--Schwinger complement to `w_j-perp`
has the same index `d_j` and a uniformly bounded inverse. Its coupling to
`w_j` remains bounded. The scalar Schur complement is

    -a_alpha m_j+O(1)<0.

Hence the whole complement has `d_j+1` negative eigenvalues. The ordinary
Birman--Schwinger count equals `n_j` once alpha is below the least absolute
negative energy of the fixed single well. This proves `d_j=n_j-1` without
assuming a positive compressed operator.

For the hierarchy write the compression to total-charge zero in block form

    [ A_scale  B_scale ; B_scale^*  D_scale ],

where `A_scale` acts on the N-1 relative-charge directions and `D_scale`
acts on Z. The estimates in Section 4 above give

    A_scale <= -c min_j log(k_j/k_{j+1}) I + C I,
    ||B_scale||<=C,
    D_scale -> direct-sum_j Gamma_j  in operator norm.

Consequently `||D_scale^(-1)||<=C` and
`index_-(D_scale)=sum_j(n_j-1)`. The Schur correction satisfies

    ||B_scale D_scale^(-1) B_scale^*||<=C,

even when D_scale is indefinite. Its sign is immaterial: the Schur
complement tends to minus infinity uniformly on the finite relative
space. Bounded triangular congruence gives its exact inertia contribution
N-1 and preserves invertibility. Therefore the total-charge-zero
compression has index `sum_j n_j-1`. The final total-charge Schur
complement adds one negative direction at fixed scales as alpha tends to
zero, proving exactly `sum_j n_j` negative eigenvalues in total.

The same invertibility, independently of its index, excludes bounded
zero solutions by Section 6. No additional positivity assumption on the
indefinite Z block is required. No uniform estimate in the number of
wells or in the single-well inverse gaps has been obtained or used.

The circular-mean argument of Section 6 above has also been inserted
directly into Section 6 of the proof file.
