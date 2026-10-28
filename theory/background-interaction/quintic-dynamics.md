# The first dynamical corrections to the transverse layer

Date: 2026-10-11. This note continues [transverse-dispersion.md](transverse-dispersion.md) and is to be read with the independently derived matched-energy and outer-response notes. It proves exact inhomogeneous-profile identities and checks their matching. Their use in a nonlinear asymptotic expansion is explicitly formal: this note does not provide a contraction argument or a complete trajectory with quadratic collapse.

## 1. Notation and the leading balance

Use

    H=-partial_y^2-Q^4,
    Q=3^(1/4)sqrt(sech(2y)),
    L_+=-partial_y^2+1-5Q^4,
    L_-=-partial_y^2+1-Q^4,
    V_Q=integral y^2Q^2=sqrt(3)pi^3/32.

The exact odd zero-energy profile F from the preceding note satisfies

    HF=0,
    F(y)=y+c sign(y)+exponentially small terms,
    c=pi/4+log(2)-1>0.

Let lambda>0, k=lambda', a_j(t) be the total effective outer slopes (including the boundary-induced radiation), and A=sum|a_j|^2. They must not be identified with the slopes of the unforced secondary subsystem alone; the feedback is recorded in Section 6. The principal real shape correction P is the unique even localized solution

    L_+P=2Q^3F^2-(c/V_Q)y^2Q,
    <P,Q>=0.                                               (1.1)

The last equality is a consequence of the equation, as proved in the preceding note. At leading order the mass constraint forces

    lambda''=4cA/V_Q.                                      (1.2)

Write gamma=4cA/V_Q. For constant A and zero terminal speed, k^2=2gamma lambda and lambda=(gamma/2)(T-t)^2.

## 2. The first imaginary transverse correction is solvable

The leading secondary approximation a_j lambda F(x/lambda) has nonzero time derivative. For constant a_j,

    i partial_t[a_j lambda F(y)]=i a_j k Z(y),
    Z(y)=F(y)-yF'(y).

To cancel it at the leading spatial order, introduce

    v_j=a_j lambda F+i a_j lambda^2 k G,
    HG=Z.                                                  (2.1)

There exists a unique odd smooth G with no linear term in its asymptotic expansion. It satisfies

    G(y)=-(c/2)y|y|+K sign(y)+O(poly(|y|)e^(-4|y|)),
    K=(3/2)integral_0^infinity [F(r)^2-(r+c)^2]dr.           (2.2)

In particular, the first dynamical correction contains no logarithmic spatial tail.

### Exact proof

On y>0 put G=F u. The equation becomes

    (F^2 u')'=-F Z.

Regularity at zero selects

    u'(y)=-F(y)^(-2) I(y),
    I(y)=integral_0^y F(r)[F(r)-rF'(r)]dr
        =(3/2)integral_0^y F(r)^2dr-(1/2)yF(y)^2.            (2.3)

The odd zero-energy solution F has no positive zero. This follows from the explicit degree-one-half Pöschl–Teller operator: it has one negative eigenvalue in the even sector and none in the odd sector, so its regular odd zero-energy solution has no positive node. Alternatively this can be checked directly from the Legendre formula. Thus division by F in (2.3) is valid for y>0. At zero, F=d y+O(y^3) with d nonzero and I/F^2=O(y^3), so the resulting G extends smoothly and oddly through zero.

At infinity, (2.3) and the exponential asymptotics of F give

    I(y)=(c/2)y^2+c^2y+K+exponentially small terms,

and hence

    I/F^2=c/2+(K-c^3/2)/(y+c)^2
                      +exponentially small terms.         (2.4)

There is no 1/y term. Integrating (2.4), multiplying by F, and adding an appropriate multiple of the homogeneous solution F removes the linear asymptotic term. The remaining constant is exactly K, proving (2.2). This absence of a logarithm follows from the special scaling source F-yF'; it is not an assumption on the solution.

Existence can also be seen without division by F: solve the smooth odd inhomogeneous ODE with any initial derivative, obtain its quadratic-plus-linear-plus-constant asymptotic by exponentially decaying coefficients, and subtract a multiple of F to cancel its linear term. The identity above determines its remaining constant. The same observation proves uniqueness under the no-linear-tail normalization.

## 3. Varying outer slopes have a compatible correction too

If a_j depends on t, the remaining term i a_j' lambda F can be canceled by

    i a_j' lambda^3 K_F,
    H K_F=F.

One does not need a second ODE construction: the exact identity

    K_F=(2/3)G-(1/6)y^2F                               (3.1)

works because H(y^2F)=-2F-4yF'. Its asymptotic is

    K_F(y)=-(1/6)y^3-(c/2)y|y|+(2K/3)sign(y)
                                  +exponentially small terms.

The corrected transverse expansion is therefore

    v_j=a_j lambda F+i a_j lambda^2 kG
                         +i a_j' lambda^3 K_F+... .          (3.2)

In the overlap region its displayed terms are

    a_j x-i a_j' x^3/6
      +c a_j lambda sign(x)
      -(ic/2)(a_j k+a_j' lambda)x|x|
      +iK a_j lambda^2 k sign(x)
      +(2iK/3)a_j' lambda^3 sign(x)+... .                    (3.3)

The smooth outer quintic subsystem at an odd node has Taylor expansion a_jx-i a_j'x^3/6+..., since the equation at linear order in x is i a_j'+6b_j=0. Thus the first two terms agree with the outer evolution. If g_j=c a_j lambda denotes the leading offset, the nonsmooth quadratic term in (3.3) is exactly -i g_j' x|x|/2. This is the coefficient required by the free equation on each half-line:

    i partial_t[g_j sign(x)]
      +partial_x^2[-i g_j' x|x|/2]=0,  x!=0.

The inner profile is smooth at the origin; the sign and absolute-value expressions describe only its large-|y| expansion. No discontinuous full PDE field is being proposed.

## 4. The leading acceleration is not changed by G

For fixed complex a_j, the profiles F and G are real. Consequently

    |a_j lambda F+i a_j lambda^2 kG|^2
       =|a_j|^2(lambda^2F^2+lambda^4 k^2G^2).

There is no density cross term linear in G. Under k=O(sqrt(lambda)), the contribution of its square to the rescaled secondary density is O(lambda^6), whereas the leading term is A lambda^3F^2. The a_j' term may have a nonzero density cross term, but it enters at rescaled order lambda^5 when a_j' is bounded. Both are strictly above the lambda^3 balance determining (1.2).

This order statement holds on each fixed rescaled compact set. Extending it uniformly over a growing overlap region needs the explicit matching estimates supplied by a future construction.

The first remaining real transverse source can also be recorded. Freeze a_j and A, take k^2=2gamma lambda, and retain the real primary correction (1.1). The uncanceled source at physical order a_j lambda^2 is

    -gamma(5G-2yG')+A(4Q^3PF+2Q^2F^3).

Thus a real secondary term a_j A lambda^4 R cancels it if

    HR=-(4c/V_Q)(5G-2yG')+4Q^3PF+2Q^2F^3.                  (4.1)

This odd inhomogeneous ODE has a smooth odd solution, unique after removal of its linear asymptotic term. Its leading asymptotic on y>0 is

    R(y)=-(4c/V_Q)(c/24)y^4
             +(4c/V_Q)(5K/2)y^2+constant
             +exponentially small terms.                   (4.2)

The quartic term in physical variables is -c a_j lambda'' x|x|^3/24. It equals the next half-line coefficient -g_j'' x|x|^3/24 when a_j is frozen. The quadratic term agrees with differentiating the smaller imaginary boundary offset iK a_j lambda^2k. Thus the first real transverse correction is also compatible with the outer equation. Equation (4.1) has not been estimated in a global nonlinear norm here.

## 5. The next principal imaginary correction has no kernel obstruction

Use the chirped core coordinates in which

    u_1=lambda^(-1/2)exp(i theta+i kx^2/(4lambda))q(t,y),
    theta'=lambda^(-2).

Put eta(t)=A(t)lambda(t)^3 and begin with q=Q+eta P. The first time-dependent imaginary source in the rescaled equation is i lambda^2 eta' P. Because <P,Q>=0, the equation

    L_- S=P,
    <S,Q>=0                                               (5.1)

has a unique even exponentially decaying solution. The operator L_- has kernel span{Q}, and is invertible on its orthogonal complement. Therefore

    q=Q+eta P+i lambda^2 eta' S+...                         (5.2)

cancels this imaginary source. For constant A this is the term 3i A lambda^4 k S, of order lambda^(9/2) on the quadratic branch. No extra mass constraint is needed: the mass compatibility that fixed lambda'' in the real equation supplies exactly the orthogonality required to invert the next imaginary operator.

This is a useful structural consistency: the real core solvability, imaginary core solvability, and the matched transverse energy all give the same leading coefficient. They do not constitute nonlinear stability of the expansion.

## 6. Relation with the exact linear outer response

The companion outer-matching note constructs, for a boundary offset b h^2 with h=T-t, an exact half-line backward-free response

    R_out(h,x)=b h^2 Psi(x/sqrt(h)), x>0,

where

    Psi(z)=e^(i pi/4) z/(2sqrt(pi))
          integral_0^1 tau^(-3/2)e^(-i z^2/(4tau))(1-tau)^2d tau.

The oscillatory integral is understood by an Abel limit where necessary. Its small-z expansion begins

    Psi(z)=1+d z+i z^2+(i d/4)z^3-z^4/12+...,
    d=-8e^(i pi/4)/(3sqrt(pi)).

For lambda=L h^2 and b=c a_j L, these quadratic and quartic coefficients agree exactly with (3.3) and (4.2). The linear term changes the outer slope by O(h^(3/2)), below the order of the constant leading slope; the associated cubic term is its required time-dependent outer Taylor coefficient.

Although this correction does not alter the leading acceleration coefficient, it cannot be discarded from a residual estimate. The shrinking potential amplifies a slope mismatch of size h^(3/2) to a physical core equation error of size h^(-1/2). One must use the corrected slope in the entire profile a_j lambda F. In the linear half-line model, if a_Z is the unforced smooth outer slope, the Dirichlet-to-Neumann relation gives the implicit equation

    a_eff(h)=a_Z(h)-e^(i pi/4) D_h^(1/2)[c lambda(h) a_eff(h)],

with the zero-terminal Riemann--Liouville half derivative. Accordingly, all occurrences of a_j and its time derivative in Sections 3--5 refer to a slope that has been matched in this manner (or by an equivalent full outer construction). This note does not solve the nonlinear slope equation or bound the complete matching residual.

The physical overlap may be chosen with

    lambda << delta << sqrt(h),

for example delta=h when lambda is proportional to h^2. This is equivalent to lambda<<delta<<lambda^(1/4), up to fixed scale constants. On that overlap the first imaginary quadratic tail is small relative to the real offset, because |k| delta^2/lambda tends to zero. The outer response has spatial width sqrt(h), distinct from the much smaller core width lambda.

This supplies a consistent core scale, intermediate region, and actual linear radiative field. To promote it to a solution of the nonlinear vector equation still requires a uniform global residual estimate, control of the unstable core modes and terminal radiation, and an existence argument with exact conserved Gram matrix. None of these remaining steps is replaced by the local cancellations above.
