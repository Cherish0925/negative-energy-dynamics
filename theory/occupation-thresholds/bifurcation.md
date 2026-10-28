# Rank-two endpoint: exact angular exclusion and the remaining radial test

Date: 2026-10-09. Intermediate mathematical note for the root calculation.
All statements explicitly labelled numerical below are exploratory, not certified.

## 1. Normalization

Let Q be the positive radial solution of

    -Delta Q + Q - Q^3 = 0  on R^2,

and M_c = integral Q^2. The Pohozaev identities give

    integral |grad Q|^2 = M_c,  integral Q^4 = 2 M_c.

Write q = Q / sqrt(M_c), C_1 = 2/M_c, and H = -Delta - Q^2.
Thus ||q||_2 = ||grad q||_2 = 1 and H Q = -Q.

The scalar sharp Gagliardo--Nirenberg inequality is

    integral |f|^4 <= C_1 ||f||_2^2 ||grad f||_2^2.

For f(x)=exp(-|x|^2/2), its quotient is 1/(2*pi). Therefore
M_c <= 4*pi. This inequality is strict: equality would make this Gaussian
a scalar optimizer, but the Gaussian does not satisfy the optimizer
Euler equation -a Delta f + b f = c f^3 for any positive a,b,c.
Consequently M_c < 4*pi. No numerical evaluation of Q is used here.

## 2. A complete angular coercivity lemma

**Lemma.** If psi in H^1(R^2) has zero angular average at almost every
radius, then

    integral Q^2 |psi|^2 <= (M_c/(4*pi)) integral |grad psi|^2.

In particular,

    <psi,H psi> >= [1-M_c/(4*pi)] ||grad psi||_2^2 > 0

for nonzero psi. Hence H has no negative eigenfunction in a nonzero
angular-momentum sector. Its possible extra negative spectrum is purely radial.

**Proof.** For integer ell >= 1, the free radial kinetic operator

    A_ell = -d^2/dr^2 -(1/r)d/dr + ell^2/r^2

on L^2((0,infinity),r dr) has zero-energy Green kernel

    G_ell(r,s) = (1/(2 ell)) (min(r,s)/max(r,s))^ell.

For a nonnegative radial potential V with integral r V finite, the positive
Birman--Schwinger operator sqrt(V) A_ell^{-1} sqrt(V) has trace

    (1/(2 ell)) integral_0^infinity r V(r) dr.

Its norm is at most this trace. Equivalently, by the quadratic-form
Birman--Schwinger principle,

    integral V |f|^2 r dr
      <= [1/(2 ell) integral r V dr]
         integral (|f'|^2 + ell^2 |f|^2/r^2) r dr.

With V=Q^2, the coefficient is M_c/(4*pi*ell). Decomposing psi in angular
Fourier modes and using |ell|>=1 proves the claimed inequality. The trace
formula can first be applied on annuli and extended by form closure, so
the use of a zero-energy Green kernel is legitimate despite the lack of
a bounded inverse on the entire L^2 space. QED.

This is a direct rigorous local structural result. No claim of historical
novelty is made; the underlying trace estimate is the classical radial
Birman--Schwinger/Bargmann mechanism.

## 3. What the first occupation variation actually tests

Fix normalized orthogonal q,psi. Introduce an unnormalized second
occupation t>=0 and let

    R(t) = integral (q^2+t|psi|^2)^2 / (1+t||grad psi||_2^2).

Then R(0)=C_1 and direct differentiation gives the exact formula

    R'(0) = -C_1 <psi,H psi>.

Thus a negative direction of H on Q-perp would immediately improve the
rank-one constant at first order. Conversely the lemma proves a strict
negative first variation for every nonzero angular-mean-zero secondary
mode:

    R'(0) <= -C_1 [1-M_c/(4*pi)] ||grad psi||_2^2.

The sign is independent of trial-profile fitting. In particular an
infinitesimal dipole/vortex occupation around an undeformed Townes core
cannot disprove the rank-two endpoint.

For occupations summing to one, p=(1-epsilon,epsilon), the corresponding
comparison is with (1-epsilon)C_1, and

    d/depsilon [C_trial(p)-(1-epsilon)C_1] at epsilon=0
       = -C_1 <psi,H psi>.

This identity is not a conclusion about the global optimizer: both modes
may deform, and a nonperturbative maximizing pair is not ruled out.

## 4. A finite-amplitude consequence for an exact Townes core

Let psi_1,...,psi_k be orthonormal H^1 functions with zero angular average,
and let t_j>=0, tau=sum t_j. Put

    eta=sum t_j |psi_j|^2, B=sum t_j ||grad psi_j||_2^2,
    kappa_ang=1-M_c/(4*pi)>0.

The angular lemma gives

    2 integral q^2 eta <= C_1(1-kappa_ang)B.

Applying scalar GN to sqrt(eta), using the pointwise Cauchy--Schwarz
estimate |grad sqrt(eta)|^2 <= sum t_j |grad psi_j|^2, gives

    integral eta^2 <= C_1 tau B.

Consequently, if tau<=kappa_ang,

    integral (q^2+eta)^2 <= C_1(1+B).

Thus an entire finite-amplitude family, not only its first variation,
cannot improve C_1. For any fixed list of secondary occupations, the
upper constant C_1 is a supremum in this restricted family: place
orthonormal angular waves at arbitrarily large scales, so their kinetic
energy and interaction with q tend to zero. This restriction retains the
exact Townes first mode; it is not the unrestricted weighted rank-two theorem.

The analogous finite-amplitude argument was independently derived by
the imbalanced-threshold subagent.

## 5. A sharper radial zero-energy test

The following statement holds for any sufficiently decaying nonnegative
radial V, not merely Q^2. Define

    m=integral_0^infinity r V(r) dr,
    T(V)=(1/(2m)) double-integral rV(r)sV(s)|log(r/s)| dr ds.

Assume m>0 and finite logarithmic moments so the displayed operators
and trace exist. If T(V)<1, -Delta_rad-V has at most one negative
eigenvalue.

**Proof.** On L^2(r dr), let chi=sqrt(V) and
P=I-|chi><chi|/m. For kappa>0 the Birman--Schwinger operator has kernel

    K_kappa(r,s)=sqrt(V(r)) I_0(kappa min(r,s))
                         K_0(kappa max(r,s)) sqrt(V(s)).

As kappa decreases to zero, the divergent term is a scalar multiple of
|chi><chi|. Compression by P removes it. The compressed positive
operators increase in quadratic-form order to a positive operator
K_bar with kernel, before compression,

    -sqrt(V(r)) log(max(r,s)) sqrt(V(s)).

The trace after compression is

    -integral rV(r)log r dr
      +(1/m) double-integral rV(r)sV(s)log(max(r,s)) dr ds
    =T(V).

By the codimension-one min--max inequality,

    lambda_2(K_kappa) <= ||P K_kappa P|| <= Tr K_bar=T(V)<1.

Therefore K_kappa has at most one eigenvalue above one for every kappa,
which proves the negative-eigenvalue count. QED.

The same constant can be written as a single integral. If
F(r)=integral_0^r sV(s) ds, then

    T(V)=integral_0^infinity F(r)(m-F(r))/(m r) dr.

This is convenient for rigorous enclosure: all integrands are
nonnegative, and the origin and infinity tails can be bounded separately.
Extra care is required to translate this compressed estimate into an
assertion about all threshold resonances; the eigenvalue-count statement
above is the result proved here. The stronger threshold statement requires a separate argument.

## 6. Numerical reconnaissance (not a proof)

The reproducible script r15_townes_spectrum.py computes a radial BVP
approximation and then zero-energy Sturm solutions plus radial finite
differences. Approximate output:

    Q(0) = 2.206200874387411
    M_c  = 11.700896524634562
    T(Q^2) = 0.7401523551841571

The simple optimized log-Bargmann estimate integral rQ^2|log(r/R)| dr
has minimum about 1.0351329 and does not suffice. Compressing the divergent
rank-one part gives substantial apparent slack (1-T approximately 0.260).

The radial zero-energy solution regular at the origin has one observed
node and large-radius form a+b log r with a approximately 0.25518718,
b approximately -0.79528507. The ell=1 regular solution has zero
observed nodes and positive growing coefficient approximately 0.31354495.
Finite differences at mesh widths 0.025 and 0.0125 likewise show only
the known radial eigenvalue near -1.

The BVP solver exhausted its requested mesh budget at tolerance 2e-10;
although the Pohozaev residuals were about 1e-10, neither they nor mesh
agreement constitute an interval certificate. The Townes profile and the
integral T<1 remain uncertified in this note. Data are in
research/r15_townes_profile.npz. No numerical output is used in Sections
1--4 or the conditional theorem of Section 5.

## 7. Consequence for the attack

The unrestricted equality L^(2)_(1,2)=L^(1)_(1,2) is not proved here.
The exact angular lemma rules out a natural infinitesimal branch and a
finite-amplitude subclass. The radial trace estimate isolates one
plausibly certifiable missing local spectral input. Even complete local
coercivity would still leave the global, nonperturbative rank-two
optimization problem; it must not be reported as the full endpoint.
