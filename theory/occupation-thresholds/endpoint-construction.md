# Exact-occupation blow-up at the mixed threshold

Date: 2026-10-09. This note gives a vector extension of the Bourgain--Wang
construction, with every extra linearized block explicitly controlled, and its
application to the occupation threshold proved in R15 and substantially
extended in [occupation-gap.md](occupation-gap.md). The construction is not
claimed to be a new blow-up mechanism or an established historical first.

## 1. Statement

Consider, for a finite number k of complex components,

    i U_t + Delta U + |U|^2 U = 0   on R^2,

where |U| is the Euclidean norm in C^k. Let Q>0 solve

    -Delta Q + Q - Q^3 = 0,   Mc = ||Q||_2^2.

**Existence theorem.** Given any nonnegative numbers m_2,...,m_k, there is
epsilon>0 and a solution U on (-epsilon,0), smooth and of finite variance at
each negative time, with conserved Gram matrix exactly

    Gamma(U) = diag(Mc,m_2,...,m_k),

which blows up at 0 and obeys

    U(t) = S(t)e_1 + Z(t) + r(t),
    ||r(t)||_{H^1} = O(|t|^5),

where S is a standard pseudoconformal Townes blow-up and Z is a smooth regular
solution through t=0 with Z_1 identically zero. In particular,

    ||grad U(t)||_2 ~ sqrt(Mc)/|t|.

The remainder exponent 5 can be replaced by any prescribed positive integer
by imposing enough flatness on the regular tail; our compactly supported
tail data vanish identically near the blow-up point and supply all orders.

Consequently, for every finite sorted occupation spectrum p satisfying

    p_2/p_1 <= epsilon_0,

where epsilon_0>0 is the rank-independent constant in
[occupation-gap.md](occupation-gap.md), choose

    m_j = Mc p_j/p_max,   M = Mc/p_max.

Then the **equality boundary is attained by an actual finite-time blow-up
solution**, even though the associated sharp kinetic inequality has no
mixed-mode optimizer. The two assertions are compatible: the solution has
a concentrating Townes core and a regular nonzero tail, not a mixed stationary
optimizer. This is an existence result, not a classification of all threshold
solutions.

This conclusion no longer requires small total secondary occupation. The
ratio condition permits arbitrarily many weak secondary modes and arbitrary
finite total secondary mass relative to the main mode. A small-total-secondary
range of the R15 form follows by taking tau_0<=epsilon_0; no numerical
comparison between previously unspecified choices of constants is assumed.

## 2. Classical linear input and its exact vector extension

The sole non-elementary evolution input is Proposition 2.8, equations
(2.9)--(2.12), of Bourgain--Wang (1997), printed p.202. Its hypotheses are
exactly the 2D cubic scalar Townes linearization, with no external potential.

For the real-linear first-component equation

    i w_s = -Delta w+w-2Q^2 w-Q^2 conjugate(w),

let G(s) denote its real-linear flow. There is an invariant decomposition
into a finite-dimensional secular space S and a complement M, with bounded
projections P_S,P_M, such that, for every integer h>=1,

    ||G(a)P_M f||_{H^h} <= C_h ||f||_{H^h},             (2.1)
    ||G(a)P_S f||_{H^h}
       <= C_h(1+|a|^3) integral exp(-c|y|)|f(y)| dy,   (2.2)
    || |y|G(a)P_M f||_2
       <= C || |y|f||_2+C(1+|a|)||f||_{H^1},          (2.3)
    || |y|G(a)P_S f||_2
       <= C(1+|a|^3) integral exp(-c|y|)|f(y)| dy.     (2.4)

The projections need not be interpreted as commuting complex-orthogonal
projections: this is the real-linear invariant decomposition provided by the
published proposition. All bounds are used only in the forms displayed.

For a vector perturbation of Q e_1 in the rotating frame, every component
j>=2 instead satisfies

    i w_{j,s} = L_- w_j,   L_-=-Delta+1-Q^2.

These blocks are selfadjoint. Their H^h flow is uniformly bounded: choose a
large constant c_0 with L_-+c_0>=1, use conservation of its integer graph
norms, elliptic equivalence with H^{2a}, and interpolation. Q and all its
derivatives are bounded. Their first moments obey

    ||y exp(-ia L_-)f||_2
       <= ||yf||_2+C|a|||f||_{H^1},                   (2.5)

by commuting y with L_- and using L2 unitarity. No dispersive estimate, absence
of threshold resonance, or R15 spectral certificate is needed for these
transverse blocks. This fully verifies the additional linear input required
when passing from scalar Bourgain--Wang to the present vector equation.

Let P be the scalar secular projection acting only on component 1, and let
P^c be its complement plus all transverse components. Then (2.1)--(2.5)
hold for the vector linearized flow G_vec, with P/P^c in place of P_S/P_M.

## 3. A regular tail with the exact desired Gram matrix

For each j>=2 choose Phi_j in C_c^infinity(R^2), supported away from 0,
with disjoint supports and ||Phi_j||_2^2=m_j. Set Phi_1=0. Zero masses can
simply be omitted. Let Z solve the vector NLS locally near time 0 with

    Z(0)=Phi.

Classical smooth local well-posedness and weighted persistence give, for
each finite order used below, bounded smooth weighted Sobolev norms on a
sufficiently short interval. Component Z_1 remains identically zero.
The tail Gram matrix is diag(0,m_2,...,m_k), since all components evolve by
the same real potential -|Z|^2 and Gram is conserved.

Every mixed space-time derivative of Z at (0,0) vanishes. Indeed the spatial
jets of Phi vanish there and repeated time differentiation of the polynomial
PDE expresses time jets by spatial jets. Taylor's theorem therefore gives
arbitrarily high space-time vanishing at (0,0).

For s>0 large, put

    v(s,y) = exp(-is) s^(-1) exp(i|y|^2/(4s))
                 Z(-1/s,-y/s).

This is the pseudoconformal image of Z, followed by the rotating-frame
change. It solves

    i v_s = -Delta v + v - |v|^2 v,

and v_1=0. Pseudoconformal symmetry is componentwise and preserves all
spatial inner products.

Fix h>=3. Weighted smoothness and the chain rule imply

    ||v(s)||_{W^{h,infinity}} <= C/s.                 (3.1)

For every N and c>0 the flatness just established, together with the
exponential weight away from the origin, implies

    ||exp(-c<y>)v(s)||_{W^{h,infinity}} <= C_N s^(-N), (3.2)

where <y>=(1+|y|^2)^(1/2). This smooth weight is used when differentiating
the weighted product; it is equivalent to exp(-c|y|) for all undifferentiated
weighted integrals below.

For clarity, split |y|<=delta s and its complement. On the first region,
Taylor vanishing gives bounds by s^(-N)(1+|y|)^N after all fixed derivatives;
the exponential weight absorbs this polynomial. On the second region,
exp(-c|y|)<=exp(-c delta s), and the global weighted bounds on Z suffice.

## 4. Nonlinear estimates, including the secular projection

Let F(a)=|a|^2 a and write the unknown in the rotating frame as

    W(s)=Q e_1+v(s)+w(s).

After subtracting the exact equations for Q e_1 and v,

    i w_s = L_vec w - N(s,w),

where L_vec is the block linearization in Section 2 and

    N(s,w)=F(Qe_1+v+w)-F(Qe_1)-F(v)-DF(Qe_1)w.

The sign in the Duhamel integral has no bearing on estimates. Because
v_1=0, the forcing term at w=0 is particularly simple:

    N(s,0)=Q |v|^2 e_1+Q^2 v.

It and its moments decay faster than any fixed power of s by (3.2).

Set H=||w||_{H^h}, Y=|| |y|w||_2, and
ell(f)=integral exp(-c|y|)|f(y)|dy, with a sufficiently small c>0.
The cubic polynomial expansion, Sobolev multiplication for h>=3 in 2D,
and (3.1)--(3.2) give, whenever H<=1,

    ||N(s,w)||_{H^h} <= C_N s^(-N)+C s^(-2) H+C H^2, (4.1)
    ell(N(s,w)) <= C_N s^(-N)(1+H)+C H^2,            (4.2)
    || |y|N(s,w)||_2
       <= C_N s^(-N)+C s^(-2)Y+C H Y.               (4.3)

In (4.1), the terms linear in w containing Qv are rapidly small locally,
whereas the global linear coefficients contain two v factors and are
O(s^-2) in W^{h,infinity}. In (4.2), those same global coefficients become
rapidly small after the exponential weight: one cannot use only the cruder
s^-2 bound on the secular projection. Terms quadratic in w are O(H^2);
terms cubic in w are absorbed using H<=1. For (4.3), multiplying any
w-dependent term by |y| puts the moment on one w factor. Terms without w
remain rapidly small. These statements follow term by term from the cubic
polynomial and hold for differences with the corresponding polarized bounds.

## 5. Contraction at infinite conformal time

Fix A=6 and h=3. Define the Banach norm on [S,infinity) by

    ||w||_X = sup_{s>=S}
        [s^A ||w(s)||_{H^h}+s^(A-1)|| |y|w(s)||_2].

Solve the terminal integral equation

    w(s) = - integral_s^infinity G_vec(s-r)[i N(r,w(r))] dr.

Multiplication by i stays inside the real-linear propagator; moving it
outside would be incorrect for the first-component linearization. The
same estimates apply to iN, since its H^h, moment and weighted L1 norms
equal those of N. In the unit ball of X,
equations (4.1)--(4.3) give

    ||N||_{H^h}=O(r^-N+r^(-A-2)+r^(-2A)),
    ell(N)=O(r^-N+r^(-2A)),
    || |y|N||_2=O(r^-N+r^(-A-1)+r^(-2A+1)).

For the P^c part, (2.1),(2.3),(2.5) yield

    ||P^c w(s)||_{H^h}
       <= C[s^(-N+1)+s^(-A-1)+s^(-2A+1)],
    || |y|P^c w(s)||_2
       <= C[s^(-N+2)+s^(-A)+s^(-2A+2)].

For the P part, (2.2),(2.4) yield, for both H^h and first moment,

    <= C[s^(-N+4)+s^(-2A+4)].

Choose N>A+4. After multiplication by the weights defining X, all
coefficients tend to zero as S tends to infinity; A>4 is sufficient.
The polarized estimates for differences give a Lipschitz constant tending
to zero by exactly the same integrals. Hence for S large the Duhamel map is
a strict contraction of the closed unit ball of X into itself.

This proves an exact solution for s>=S with

    ||w(s)||_{H^3}=O(s^-6),   || |y|w(s)||_2=O(s^-5).

No approximation of the desired occupation masses occurs here. Arbitrarily
large smooth tails merely increase the required S and shorten the physical
existence interval.

### Higher moments and smoothness in physical coordinates

Higher conformal Sobolev regularity alone does not prove smoothness after
inverting the quadratic phase. One must control moments too. For an integer
m>=1, use h>=max(3,m) and A>=max(6,m+4), with the enlarged norm

    sup_s [s^A ||w||_{H^h}+s^(A-m)|| |y|^m w||_2].

When matching to the base contraction below, take A>6 (or a smaller fixed
point ball if A=6), so interpolation constants cause no overlap issue.

Intermediate moments follow by Holder interpolation with L2. The scalar
complement bound is exactly BW (2.11), with alpha=m:

    || |y|^m G(a)P_M f||_2
       <= C|| |y|^m f||_2+C(1+|a|^m)||f||_{H^m}.

The secular bound BW (2.12) still grows only cubically. The transverse
selfadjoint flow satisfies the same m-th-moment complement bound. Indeed
the derivative of its m-th-moment norm Y_m is bounded by
C|| |y|^(m-1)grad u||_2; weighted Sobolev interpolation (or repeated
integration by parts followed by Young's inequality) bounds this by
C(Y_m+||u||_{H^m})^(1-1/m)||u||_{H^m}^(1/m). Uniform H^m control and
integration give Y_m(a)<=C[Y_m(0)+(1+|a|^m)||u(0)||_{H^m}]. The real
potential contributes zero to the moment derivative.

Estimate (4.3) holds with |y|^m and Y_m in place of |y| and Y. Thus the
complement m-th moment of the Duhamel map is bounded by

    C[s^(-N+m+1)+s^(-A+m-1)+s^(-2A+m+1)],

and its secular moment by C[s^(-N+4)+s^(-2A+4)]. These bounds and their
differences close the same contraction after choosing N>A+m+4. The space
H^h intersect {|y|^h w in L2}, taking m=h, controls all mixed derivatives
and moments of total order at most h by weighted interpolation. Its
pseudoconformal image consequently belongs to physical H^h at every
nonzero time.

Every such higher-order construction belongs, for sufficiently large s,
to the original H^3/first-moment contraction ball (enlarge S and use A>=6).
Uniqueness identifies it with w on that interval. Persistence of higher
regularity then propagates it backward along the fixed physical H^1
solution on compact subintervals of (-1/S,0). This proves smoothness of one
and the same physical solution at every negative time. Larger A similarly
gives stronger remainder rates for that solution, since the tail is flat
to every order.

## 6. Returning to physical time and exact conservation

The standard pseudoconformal map is

    (Cf)(s,y)=s^-1 exp(i|y|^2/(4s)) f(-1/s,y/s),

for s>0, with spatial reflection as needed when composing the inverse.
It preserves the focusing cubic vector equation. The definition of v in
Section 3 deliberately uses the reflected version, so that inversion gives
precisely the regular solution Z(t,x), not its spatial reflection.
Equivalently use the inverse explicitly, for t<0 and s=-1/t:

    U(t,x)=s exp(-i s |x|^2/4)
           exp(is)[Q(-s x)e_1+v(s,-s x)+w(s,-s x)].

Substitution of Section 3 shows that the v term in this formula equals
Z(t,x). The Q term is the radial pseudoconformal Townes solution

    S(t,x)=|t|^-1 Q(x/t)
               exp(i|x|^2/(4t)-i/t).

The w term, denoted r(t), satisfies

    ||r(t)||_2=||w(s)||_2=O(s^-6),
    ||grad r(t)||_2
       <= s||grad w(s)||_2+(1/2)|| |y|w(s)||_2
       =O(s^-5).

The first-moment norm of r is s^-1|| |y|w||_2, so U has finite variance at
each t<0. Direct differentiation gives

    ||grad S(t)||_2^2
       = Mc/t^2+(1/4)|| |y|Q||_2^2.

Since Z is bounded in H^1 and r tends to zero there, this proves blow-up
and the stated rate.

For completeness, the exact Gram computation can be made in physical time.
The regular tail has constant Gram diag(0,m_2,...,m_k), and

    |<S(t),Z_j(t)>|
       <= ||Z_j(t)||_infinity ||S(t)||_1
       <= C |t| ||Q||_1 -> 0.

All terms involving r tend to zero by its L2 norm. Thus

    lim_{t up to 0} Gamma(U(t))=diag(Mc,m_2,...,m_k).

The exact Gram matrix is conserved for each t<0 because U_j all solve
the same selfadjoint scalar Hamiltonian -Delta-|U|^2. It therefore equals
this limit at every time, proving the claimed exact masses and all
off-diagonal orthogonality relations. No a posteriori Gram--Schmidt change
to a nonlinear solution is made.

### Global solutions on the same occupation boundary

The conformal-time solution itself also has a useful physical interpretation.
Set

    V(s)=exp(is)[Qe_1+v(s)+w(s)],   s>=S.

It solves the original NLS, has the same exact Gram matrix, and is globally
bounded in H1 forward in s. Its first component converges strongly in H1
to exp(is)Q. Its other components scatter to free waves: there exist
f_j in H1, j>=2, such that

    ||V_j(s)-exp(is Delta)f_j||_{H1} -> 0.

To verify the scattering assertion directly, compare Z(t) with the linear
solution Z_lin(t)=exp(it Delta)Phi. Smooth local theory gives
||Z(t)-Z_lin(t)||_{H1}+||x[Z(t)-Z_lin(t)]||_2=O(|t|).
The pseudoconformal image of Z_lin is an exact free solution for s>0;
write it as exp(is Delta)f. The difference of their images has L2 norm
O(s^-1), and its gradient norm is bounded by

    s^-1 ||grad[Z-Z_lin](-1/s)||_2
       +(1/2)||x[Z-Z_lin](-1/s)||_2 = O(s^-1).

The correction exp(is)w also tends to zero in H1. This proves the asserted
soliton-plus-free-radiation asymptotic without invoking any general
asymptotic-stability or soliton-resolution theorem.

Thus, at each fixed mixed spectrum covered by the R16 condition
p_2/p_1<=epsilon_0 and exact mass Mc/p_max,
both forward global solutions and finite-time blow-up solutions exist.
The equality boundary does not force one universal fate.

## 7. What is and is not settled

Together with [occupation-gap.md](occupation-gap.md), this closes **existence of blow-up on
the exact equality boundary** for every finite mixed occupation spectrum
with p_2/p_1<=epsilon_0, with no restriction on the total secondary mass.
It also shows why positive energy and nonattainment of the stationary
variational problem do not imply global existence at that boundary.

The construction itself works with arbitrary finite tail masses. Outside
the known occupation-ratio range, Mc/p_max remains the mass of this explicit class of
constructed blow-ups; the exact fixed-spectrum threshold could be lower.
No conclusion about the full rank-two Lieb--Thirring equality is inferred.
No stability, genericity, complete classification, or engineering-scale
robustness of these special blow-ups is asserted.

## 8. Primary source checked directly

J. Bourgain and W. Wang, *Construction of blowup solutions for the nonlinear
Schrodinger equation with critical nonlinearity*, Annali della Scuola
Normale Superiore di Pisa, Classe di Scienze, Serie IV, 25 (1997), 197--215.
Original scanned PDF:
https://www.numdam.org/item/ASNSP_1997_4_25_1-2_197_0.pdf

The source theorem is scalar. Its Theorem 1' motivates the construction;
the input actually used verbatim here is Proposition 2.8. The passage to
vector equations is proved above by verifying the additional selfadjoint
linear blocks and all nonlinear/moment estimates. The source is not being
represented as already stating an occupation-spectrum theorem.
