# Proof details: exact-Gram vector Bourgain–Wang construction

Date: 2026-10-09. Derived against [endpoint-construction.md](endpoint-construction.md) and the
original Bourgain–Wang (1997) Proposition 2.8, printed p.202:
https://www.numdam.org/item/ASNSP_1997_4_25_1-2_197_0.pdf

## Verdict and scope

The displayed construction closes as an H1, finite-variance existence theorem
for any prescribed finite list of secondary masses. Its nonlinear estimates
do not require these masses to be small. Small relative occupation enters
only when identifying the constructed mass with a separately proved exact
threshold. The final integration uses [occupation-gap.md](occupation-gap.md): if occupations
are ordered, the condition is p2/p1<=epsilon0, with no restriction on the
total secondary occupation. This replaces the narrower R15 range.
The proof uses a classical scalar linearized-flow theorem; it does not prove
the rank-two Lieb–Thirring equality or classify all threshold dynamics.

Two corrections were communicated to the construction author: multiplication
by i belongs INSIDE the real-linear propagator, and smoothness after inverse
pseudoconformal transformation needs higher spatial moments, not merely H3.
The first correction is essential algebraically but changes no estimates.
The second is a statement/regularity issue with a standard explicit repair
given below. Replace differentiated weights exp(-c|y|) by the smooth weight
exp(-c sqrt(1+|y|^2)), or put the exponential outside each derivative.

## 1. Exact linearization

For F(a)=|a|^2 a, q=Q e1, and v1=0,

    DF(q)w = Q^2 w + 2 Q^2 Re(w1)e1.

Thus the first block is the real-linear scalar Townes operator, and every
transverse block is the selfadjoint operator L_-=-Delta+1-Q^2. Selfadjointness
and elliptic graph-norm equivalence bound its flow in every finite Sobolev
order. Commuting y through this flow gives linear first-moment growth.
The constants for the direct sum do not grow with the number of components
when Euclidean vector norms are used.

The scalar flow has an invariant secular subspace with at most cubic time
growth and exponentially localized dual coordinates. Its complementary flow
is bounded in Sobolev norm and grows at most linearly in first moment. These
are the precise published inputs used here; no dispersive decay or numerical
spectral assertion is substituted for them.

## 2. The apparently dangerous linear perturbation is controlled

Write q+v+w and subtract the exact equations for q and v. The forcing is

    N = F(q+v+w)-F(q)-F(v)-DF(q)w.

The w-independent part is exactly Q|v|^2 e1+Q^2 v. Since v is
superpolynomially small near the exponentially localized Q, this part is
superpolynomial in all finite Sobolev and moment norms.

The linear-in-w terms split into globally supported v^2 w terms and Qv w
terms. The former are only O(s^-2) as global multiplication operators, but
are superpolynomially small when paired with an exponentially localized
secular dual. The latter are superpolynomially small already as localized
multiplication operators. The remaining terms are bounded by
O((Q+|v|)|w|^2+|w|^3).

Consequently, if H=||w||_H3<=1 and Y=||yw||_2,

    ||N||_H3 <= C_N s^-N + C s^-2 H + C H^2,
    ell(N) <= C_N s^-N (1+H) + C H^2,
    ||yN||_2 <= C_N s^-N + C s^-2 Y + C H Y,

where ell is exponentially weighted L1. The same statements hold in
polarized form for differences. In particular it would be WRONG to apply
the cubic secular growth to only the crude global bound s^-2 H; that loses
two powers. The localized estimate is what closes the construction.

## 3. Explicit integral check

In the norm sup(s^A H+s^(A-1)Y), the unit ball gives the source bounds

    global H3: s^-N+s^(-A-2)+s^(-2A),
    localized L1: s^-N+s^(-2A),
    moment: s^-N+s^(-A-1)+s^(-2A+1).

The complementary propagator yields output

    H3: s^(-N+1)+s^(-A-1)+s^(-2A+1),
    moment: s^(-N+2)+s^(-A)+s^(-2A+2).

The secular propagator yields, in BOTH output norms,

    s^(-N+4)+s^(-2A+4).

These follow directly from integrals of (1+r-s)^j r^-b, j=0,1,3.
With A>4 and N>A+4, multiplication by the defining time weights makes every
coefficient tend to zero as the initial conformal time S tends to infinity.
Polarization gives the same small factor in the Lipschitz estimate. Thus
there is a genuine contraction; no compactness or unproved stability step
is hidden at this point.

The exact terminal equation is

    w(s)=-integral_s^infinity G_vec(s-r)[ i N(r,w(r)) ] dr.

The scalar block is only REAL-linear. Writing -i outside the propagator
would not solve the stated equation. All bounds apply to iN without change.

## 4. Pseudoconformal signs and the exact Gram matrix

Use

    v(s,y)=e^(-is) s^-1 e^(i|y|^2/(4s)) Z(-1/s,-y/s).

This includes a spatial reflection, which is itself a symmetry. For t<0,
s=-1/t, the inverse is

    U(t,x)=s e^(-is|x|^2/4) e^(is) [q(-sx)+v(s,-sx)+w(s,-sx)].

Substitution gives the regular tail Z(t,x) exactly, with no residual spatial
reflection or complex conjugation. The core is

    S(t,x)=|t|^-1 Q(x/t) exp(i|x|^2/(4t)-i/t).

For r equal to the inverse transform of w,

    ||r||_2=||w||_2,
    ||grad r||_2 <= s||grad w||_2 + (1/2)||yw||_2,
    ||xr||_2=s^-1||yw||_2.

Thus A=6 gives r=O(|t|^5) in H1, and finite variance. The core has

    ||grad S||_2^2 = M_c/t^2 + (1/4)||yQ||_2^2.

Choose the regular secondary final data Phi_j with disjoint compact supports
away from the origin and ||Phi_j||_2^2=m_j, Phi_1=0. The regular vector flow
preserves their Gram matrix. The full solution also preserves its Gram
matrix, because all components evolve under the same real scalar potential.
At t→0, ||r||_2→0 and

    |<S,Z_j>| <= ||S||_1 ||Z_j||_infinity
                <= |t| ||Q||_1 sup||Z_j||_infinity →0.

Hence the full conserved Gram matrix is EXACTLY diag(M_c,m_2,...,m_k).
No approximate orthogonality, mass adjustment, or nonlinear Gram–Schmidt
operation is being used.

This constructs a blow-up at M=M_c/p_max for every finite occupation spectrum
p. It establishes sharp-threshold blow-up where the matching lower bound
has separately been proved. The current R16 range is p2/p1<=epsilon0 and
allows arbitrary total secondary occupation and arbitrary finite rank.

## 5. Higher regularity repair

H3 plus one moment is enough for the physical H1 statement, but does not by
itself imply smoothness after multiplication by a quadratic phase. For a
desired physical order m, include moments ||y^j w||_2, 1<=j<=m, with weights
s^(A-j), and take a sufficiently high Sobolev order h>=m. The published scalar
moment bound has growth (1+|s-r|^j); the selfadjoint transverse blocks have the
same polynomial moment bound, obtained by commutator induction and weighted
Sobolev interpolation. The source estimate is

    ||y^j N||_2 <= C_N s^-N + (C s^-2+C H)||y^j w||_2.

The complementary moment integral then gains one inverse power relative to
s^(j-A). The secular term is unchanged apart from a finite basis constant.
Taking A>max(4,m+1), N sufficiently large closes this finite-order space.
Weighted interpolation supplies the mixed derivatives needed to differentiate
the inverse quadratic phase m times.

If a single C-infinity solution is asserted, one also uses uniqueness in the
base terminal contraction space to identify these higher-order constructions
on common late-time intervals, and persistence of regularity to propagate
back along the base solution. Alternatively one can state arbitrarily high
prescribed finite regularity, which requires only the finite-order argument.

## 6. Forward global counterpart: independently checked

The conformal-time solution

    V(s)=exp(is)[Qe1+v(s)+w(s)],  s>=S,

is itself an exact original-NLS solution. The pseudoconformal map preserves
the Gram matrix at each time, so its Gram matrix is the same exact diagonal
matrix as the finite-time blow-up solution. Its primary component approaches
exp(is)Q strongly in H1 since v1=0 and w→0 in H1.

For the transverse components let Z_lin(t)=exp(it Delta)Phi. Smooth local
theory for the Schwartz initial data, or the Duhamel formula with one moment,
gives

    ||Z(t)-Z_lin(t)||_H1 + ||x(Z(t)-Z_lin(t))||_2 = O(|t|).

The reflected pseudoconformal image of Z_lin is an exact free solution
exp(is Delta)f. If D=Z-Z_lin, direct differentiation gives

    ||C_ref D(s)||_2 = ||D(-1/s)||_2,
    ||grad C_ref D(s)||_2
       <= s^-1 ||grad D(-1/s)||_2 + (1/2)||xD(-1/s)||_2.

Thus the difference is O(s^-1) in H1. Adding the decaying correction w proves
V_j(s)-exp(is Delta)f_j→0 in H1 for every j>=2. Uniform forward H1 boundedness
also follows from this expression. The free states f_j belong to H1 because
Phi is Schwartz. No general scattering or soliton-resolution theorem is being
assumed here.

Consequently both a forward-global soliton-plus-radiation solution and a
finite-time blow-up solution exist with every prescribed finite exact Gram
matrix diag(Mc,m2,...,mk). In the separately proved p2/p1<=epsilon0 range,
these two kinds of solution lie at precisely the same sharp occupation
boundary. This is an existence statement, not a classification or stability
claim.

## 7. Independent scientific assessment

The argument provides an exact-Gram vector extension and an application to
the occupation boundary. It inherits the blow-up mechanism from the classical
Bourgain–Wang construction. Its historical novelty has not been established
by this audit. It is neither a solution of all threshold dynamics nor a proof
that the equal two-mode threshold cannot lie below 2 M_c.
