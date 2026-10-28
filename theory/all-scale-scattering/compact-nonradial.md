# A finite nodal competitor and explicit ratio tests for compact rank two

Date: 2026-10-15. This note derives two tests directly from the stationary
equations. Neither excludes every compact nonradial rank-two optimizer. No
historical priority is asserted.

Let real smooth exponentially decaying profiles satisfy

    H=-Delta-rho, rho=u^2+v^2,
    Hu=-e1 u, Hv=-e2 v, e1>e2>0,
    u>0, int u^2=int v^2=beta, int uv=0.

Write delta=e1-e2 and

    E(u,v)=int(|grad u|^2+|grad v|^2)-(1/2)int rho^2.

An optimizing self-consistent pair has E=0 by the two-dimensional Pohozaev
identity. At the equal component mass beta=2/C2 it minimizes E over orthogonal
pairs of that mass, with minimum zero. The formulas below also hold for other
stationary pairs, but energy nonnegativity of competitors uses minimization.

## 1. Exact finite folding of the second nodal orbital

Set

    a=beta^(-1) int u|v|,       0<a<1,
    w=(|v|-a u)/sqrt(1-a^2).

The pair (u,w) has the same Gram matrix beta I. Strict a<1 follows from
Cauchy--Schwarz: equality would make |v| proportional to u, impossible for a
continuous sign-changing v and positive u. The map is admissible in H1, since
|v| is H1 and has the same kinetic energy as v.

Its density change is exactly

    d_rho=u^2+w^2-rho
         =a(a rho-2u|v|)/(1-a^2).

For any competing pair U_new, direct expansion around the self-consistent
potential gives

    E(U_new)-E(U)
      =sum_i <u_new,i,H u_new,i>-sum_i <u_i,H u_i>
       -(1/2)||rho_new-rho||_2^2.

Since <|v|,H|v|>=-e2 beta and <u,H|v|>=-e1 a beta,

    E(u,w)-E(u,v)
      =beta delta a^2/(1-a^2)
       -a^2/[2(1-a^2)^2] int(a rho-2u|v|)^2.          (1)

Consequently a minimizing pair must satisfy the finite, non-infinitesimal
inequality

    int(a rho-2u|v|)^2 <= 2 beta delta(1-a^2).        (2)

The left side is the squared density change before the normalization factor;
the positive term in (1) is the exact cost of removing the ground-state
component of |v|. Dropping this term reverses the conclusion.

There is also a nodal flux identity. In distributions, away from singular
points of the nodal set and then by the standard weak formulation,

    H|v|=-e2|v|-2 |grad v| delta_{v=0}.

Pairing with u gives

    beta delta a = 2 int_{v=0} u|grad v| dS.         (3)

Thus (2) compares a quartic density change with a nodal flux. Identity (3)
does not by itself provide a lower bound for the left side of (2).

### Analytic test: folding raises the energy at weak overlap

Let F=int rho^2 and B=int u^2v^2. The elementary bound

    int(a rho-2u|v|)^2 <= 2a^2 F+8B

combined with (1) yields

    E(u,w)-E(u,v)
      >= a^2/(1-a^2) [beta delta-(a^2 F+4B)/(1-a^2)]. (4)

Hence whenever a^2 F+4B < beta delta(1-a^2), folding strictly increases the
energy. In particular a weak-overlap family with a,B -> 0, bounded F and beta,
and beta delta bounded below cannot be destabilized by this competitor.
This is an actual obstruction to the proposed universal folding descent.
It leaves strongly overlapping pairs with comparable binding frequencies.

The scalar moment constraints cannot alone reverse (2). For 0<alpha<1, put
f=alpha with probability 1/(1+alpha^2), and f=-1/alpha with probability
alpha^2/(1+alpha^2). Then E f=0, E f^2=1, a=E|f|=2alpha/(1+alpha^2), while
a(1+f^2)-2|f| vanishes at both values. These moments are realized by rotating
two normalized functions with disjoint supports:

    u=sqrt(beta)(cos(theta)g1+sin(theta)g2),
    v=sqrt(beta)(sin(theta)g1-cos(theta)g2), alpha=tan(theta).

Here the folding sends v to -v and leaves the projector unchanged. This pair
is not a compact positive-ground-state solution of the coupled PDE. It shows
precisely why moment conditions without differential self-consistency cannot
prove the required positive lower bound.

## 2. Explicit polynomial variations of the ground-state ratio

Put f=v/u and dmu=u^2 dx/beta. Then

    int dmu=1, int f dmu=0, int f^2 dmu=1,
    -div(u^2 grad f)=delta u^2 f.                   (5)

Assume mu4=int f^4 dmu<infinity. Set mu3=int f^3 dmu and

    p(f)=f^2-mu3 f-1,        h=u p(f).

Then h is orthogonal to both u and v. Truncation in (5), followed by the
finite fourth-moment limit, gives

    int u^2 |grad f|^2 = beta delta,
    int u^2 f|grad f|^2 = (beta delta/2)mu3,
    int u^2 f^2|grad f|^2 = (beta delta/3)mu4.

Thus the ground-state transform computes, without unknown derivative terms,

    ||h||_2^2 = beta(mu4-1-mu3^2),
    <h,(H+e1)h> = beta delta(4mu4/3-mu3^2),
    <h,(H+e2)h> = beta delta(1+mu4/3).              (6)

These formulas can first be proved for smooth bounded truncations and then
passed to the weighted form domain. Boundedness of v ensures the nonlinear
integrals below are finite once mu4 is finite. For exponentially decaying
bound states, e2>e1/4 is a sufficient condition for mu4<infinity, using their
standard exponential upper bounds and the positive ground-state lower bound.

For every real a0,b0, the variation (a0 h,b0 h) respects all Gram constraints
to first order. The full constrained quadratic form is

    Q(a0 h,b0 h)
      = beta delta[(4mu4/3-mu3^2)a0^2+(1+mu4/3)b0^2]
        -2 int u^4(a0+b0 f)^2 p(f)^2.              (7)

Accordingly, define I_j=int u^4 f^j p(f)^2, j=0,1,2. A minimizing pair must
make the following explicit 2 by 2 matrix positive semidefinite:

    [ beta delta(4mu4/3-mu3^2)-2I0,   -2I1
      -2I1,   beta delta(1+mu4/3)-2I2 ].            (8)

In particular,

    2 I0 <= beta delta(4mu4/3-mu3^2),
    2 I2 <= beta delta(1+mu4/3).                    (9)

The cancellation of mu3 in the second diagonal entry was checked by exact
polynomial integration rules int f^k dmu=mu_k, with mu0=mu2=1 and mu1=0.
Equations (5)-(6) provide the mathematical derivation.

This test forces the ratio f, in the u^4-weighted region, toward roots of
f^2-mu3 f-1 when delta is small and mu4 stays bounded. It does not establish
such moment control uniformly for an unknown optimizer. In particular,
e2<=e1/4 need not allow this unbounded polynomial variation; bounded variations
remain legitimate but do not satisfy the same moment formula.

## 3. Outcome of this branch

No compact nonradial optimizer has been excluded and no counterexample has
been constructed. Equations (1) and (4) show why nodal folding cannot serve as
a universal descent. Equations (8)-(9) provide a specific finite-dimensional
test of the full Hessian, with all coefficients computed from the ratio and
binding-frequency gap. To prove nonexistence with these tests one still needs
a lower bound on I0 or I2 that beats their displayed right sides for every
self-consistent pair of mass beta<M_c. No such lower bound is proved here.
