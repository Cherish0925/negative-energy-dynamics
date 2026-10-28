# Transverse zero-energy scattering and the quadratic-scale branch

Date: 2026-10-11. This note derives an exact one-dimensional transverse scattering profile and verifies, independently of the matched-energy calculation in the companion quintic note, the leading core equation that it produces. The scattering identities and the elliptic correction below are proved. A nonlinear solution realizing the proposed quadratic collapse scale has not been constructed here.

## 1. Why orthogonality alone does not complete the rough-background argument

Consider either the two-dimensional cubic or the one-dimensional quintic common-density system. The full principal field and each secondary field solve the same linear equation with the self-consistent real potential:

    i u_{j,t}=H(t)u_j,  H(t)=-Delta-rho(t)^(2/d).

If P(t)=|u_1(t)><u_1(t)|/Mc, then, in the weak sense justified by the H1 flow,

    i P_t=[H(t),P(t)].

Thus exact orthogonality to the actual principal solution is dynamically preserved. This exact moving projection is different from the instantaneous spectral projection onto the scaled ground-state profile Q_lambda. The R17/R18 estimates only give

    |<u_j,Q_lambda>|=O(lambda).

A packet with L2 size O(lambda) at spatial scale lambda can have order-one kinetic energy. Consequently that estimate alone cannot establish a strong H1 secondary terminal limit.

In the primary rotating frame the frozen transverse operator is

    L_-=-Delta+1-Q^(4/d).

The shift by 1 separates its Q mode from its continuous spectrum. However, the feedback into the principal equation is quadratic in secondary fields. A normal form for such feedback contains spectral differences omega-omega', so the common spectral shift and the primary phase cancel. The diagonal continuous-spectrum interaction omega=omega' remains. This is the precise reason that R18's linear phase cancellation does not automatically make the density force time integrable. Actual local decay or a matched inner/outer analysis is needed.

The latter approach yields a concrete mechanism in one dimension.

## 2. Exact odd zero-energy transverse profile

For the one-dimensional quintic ground state,

    Q(y)=3^(1/4) sqrt(sech(2y)),
    H=-d_y^2-Q^4=-d_y^2-3 sech(2y)^2.

There is a unique odd real solution F of HF=0 having slope 1 at positive infinity. It is

    F(y)=(pi/4)[P_(1/2)(tanh(2y))-P_(1/2)(-tanh(2y))],

where P_nu is the Legendre function on (-1,1). Its asymptotics are

    F(y)=y+c_* sign(y)+O((1+|y|)e^(-4|y|)),
    F'(y)=1+O((1+|y|)e^(-4|y|)),
    c_*=pi/4+log(2)-1>0.                         (2.1)

To verify the formula, set z=tanh(2y). The equation HF=0 becomes

    (1-z^2)F_zz-2z F_z+(3/4)F=0,

the Legendre equation of degree 1/2. The odd combination is forced by the parity condition. The connection identity on (-1,1) gives

    P_(1/2)(-z)=-(2/pi) Q_(1/2)(z).

As z tends to 1,

    Q_nu(z)=(1/2)log(2/(1-z))-gamma-psi(nu+1)+o(1).

Here log(2/(1-tanh(2y)))/2=2y+o(1), and

    psi(3/2)=-gamma-2log(2)+2.

These identities give exactly (2.1), including its coefficient and sign. Exponential error estimates also follow directly from F''=-3 sech(2y)^2 F after the leading linear asymptotic is known. Uniqueness follows because the odd solution space is one-dimensional and its nonzero asymptotic slope is fixed by this explicit formula.

The ordinary one-dimensional scattering-length convention F~y-a_s gives a_s=-c_*. The sign convention must be recorded when comparing literature.

## 3. Two exact scattering identities

All integrals in the following identities converge absolutely:

    integral_R [(F'-1)^2-Q^4 F^2]dy=-2c_*,                (3.1)

    J:=integral_R (Lambda Q) Q^3 F^2 dy=-c_*/2,
    Lambda Q=(1/2)Q+yQ'.                                  (3.2)

For (3.1), first integrate over [-R,R]. Since F''=-Q^4F,

    integral_(−R)^R (F'^2-Q^4F^2)dy=2F(R)F'(R).

Consequently

    integral_(−R)^R [(F'-1)^2-Q^4F^2]dy
       =2F(R)F'(R)-4F(R)+2R -> -2c_*.

For (3.2), put V=Q^4. Since Q^3 Lambda Q=V/2+yV'/4,

    J=(1/4)integral V F^2-(1/2)integral y V F F'.

The boundary terms from the first integration by parts vanish exponentially. On the symmetric interval, use F''=-VF to write the last expression as

    (R/2)F'(R)^2-(1/2)F(R)F'(R).

Its limit is -c_*/2. This derivation is independent of any matched energy argument.

It is useful to distinguish (3.1) from the raw slope-prescribed inner energy:

    integral_(−R)^R [F'^2-Q^4F^2-1]dy -> 2c_*.

The signs differ because a fixed exterior field requires matching away the offset c_* lambda sign(x). Keeping only the raw inner boundary form would produce the wrong effective energy.

## 4. The physical transverse layer

Translate the putative concentration point to zero. Suppose a smooth odd terminal secondary field has expansion

    w_j(x)=a_j x+O(x^3),
    A=sum_(j>=2)|a_j|^2.

At the inner scale x=lambda y, the static leading transverse equation is HF=0. Therefore its compatible leading field is

    u_j(t,lambda y) approximately a_j lambda F(y),         (4.1)

not a_j lambda y. The latter has nonzero order-lambda^(-1) residual in the transverse equation. Equation (4.1) is the natural boundary layer enforced by the shrinking primary potential.

Since the principal amplitude is lambda^(-1/2)Q, the rescaled secondary density is

    lambda sum_(j>=2)|u_j(t,lambda y)|^2
       approximately A lambda^3 F(y)^2.                    (4.2)

Thus the leading additional term in the rescaled principal quintic equation is

    2A lambda^3 Q^3 F^2.                                  (4.3)

The companion quintic calculation matches (4.1) to the fixed exterior fields. Identity (3.1) gives the first energy correction -c_* A lambda. It is essential to include the transverse kinetic correction: retaining only the mixed nonlinear term produces an incorrect coefficient.

## 5. Independent primary solvability calculation

Take a centered chirped core with phase theta'=lambda^(-2):

    u_1=lambda^(-1/2) exp(i theta+i lambda' x^2/(4lambda))
                       [Q(y)+A lambda^3 P(y)],
    y=x/lambda.

For the pure Q core, direct differentiation gives

    i u_{1,t}+u_{1,xx}+|u_1|^4u_1
       =-lambda'' x^2 u_1/(4lambda).

Multiplication by the rescaling factor lambda^2 makes this the term

    -(lambda^3 lambda''/4)y^2 Q.

At the common leading order A lambda^3, inclusion of (4.3) therefore asks for

    L_+ P=2Q^3 F^2-(lambda''/(4A))y^2Q,
    L_+=-d_y^2+1-5Q^4.                                    (5.1)

The critical principal mass imposes the tangent condition <Q,P>=0. The exact mass-critical identity

    L_+ Lambda Q=-2Q

shows that (5.1) is compatible with this condition precisely when

    0=2J-(lambda''/(4A))<Lambda Q,y^2Q>.

The second moment V_Q and its scaling pairing are

    V_Q=integral y^2 Q^2dy=sqrt(3) pi^3/32,
    <Lambda Q,y^2Q>=-V_Q.

Using (3.2) gives

    lambda''=4c_* A/V_Q.                                 (5.2)

In particular the elliptic correction

    L_+P=2Q^3F^2-(c_*/V_Q)y^2Q                           (5.3)

has a unique even exponentially decaying solution, and that solution satisfies <Q,P>=0. Existence uses the standard scalar nondegeneracy ker L_+=span{Q'}, whose kernel is odd; equivalently, it follows directly from the Pöschl–Teller operator -d_y^2+1-15 sech(2y)^2. The exponentially localized even right side is consequently in the range on the even subspace. The pairing computation proves the mass tangent condition, rather than adding it as an incompatible second constraint.

A frequency correction theta'=lambda^(-2)+nu A lambda adds a multiple of Q to the right side of (5.1). It does not alter (5.2), because <Lambda Q,Q>=0. Thus the acceleration coefficient is independent of that phase gauge at this order.

Equation (5.2), with vanishing endpoint radius and vanishing endpoint speed, predicts

    lambda(t)=(2c_* A/V_Q)(T-t)^2.                         (5.4)

The same coefficient follows independently from the matched energy

    E_total-E_background
       =(V_Q/8)(lambda')^2-c_* A lambda+lower terms.

At zero effective core energy this gives (5.4); positive effective core energy instead gives the usual leading scale proportional to T-t. The agreement of energy and mass-constrained equation solvability is a substantive consistency check. Neither route alone constructs a solution.

## 6. What remains before (5.4) can be a dynamical theorem

The profile F grows linearly and its offset changes with lambda. It must be matched to an actual evolving outer secondary solution. The term i partial_t[a_j lambda F(x/lambda)] is not zero. For a quadratic radius, it is of order lambda^(1/2) on the core, whereas its stationary spatial operator cancels exactly. A subsequent imaginary transverse correction and an intermediate matching region are therefore required. Dropping this time derivative would be an invalid existence proof.

Likewise the primary expansion must control the unstable scalar directions, the secular parameters, exact Gram conservation, and all spatially global remainders. The elliptic correction (5.3) removes one leading compatibility obstruction; it does not provide those estimates.

The exact identities proved here explain why replacing the rough-background question by a blanket assertion of pseudoconformal scale is potentially too restrictive. They give a specific competing law and the precise scattering coefficient that a construction must use. They do not establish a counterexample to R18's regular-background theorem: that theorem is for the two-dimensional cubic coupling, whereas (5.4) concerns the one-dimensional quintic mixed term.

## 7. Literature check for the generic transverse approach

Primary-source search found Beceanu–Soffer, *The Schrödinger Equation with Potential in Rough Motion*, arXiv:1103.0521, and Beceanu, *Variable potentials and dispersive equations*, arXiv:1410.3521. Their returned abstracts concern time-dependent-potential dispersive estimates; the former explicitly works in R3. No theorem from either source has been imported into this note, and their hypotheses have not been verified for a potential concentrating at an unknown rate in d=1 or 2. The exact calculations in Sections 2–5 are self-contained except for the standard scalar nondegeneracy indicated there.

The historical novelty of this boundary-layer mechanism has not been established. It should be compared against minimal-mass singularities with lower-order perturbations and vector boundary-layer constructions before a priority claim.
