# General homogeneous transport and kinetic localization

## Scope

This note gives a complete extension of the round-10 transport argument to arbitrary positive elliptic homogeneous dispersion, including anisotropic symbols, and to mass-critical Hartree interactions. It uses an absolute kinetic-tail estimate, not a favorable sign of the localized principal commutator. No claim of first priority is made. The underlying localized-virial and compactness methods are classical; the precise all-degree anisotropic statement and its weak kinetic-localization formulation require a further targeted literature comparison.

The proof first measures the homogeneous energy of a spatially cut-off exterior wave. An elementary cutoff-commutator equivalence, added below, gives the theorem for the literal exterior integral of | |D|^{m/2}u|^2. It does **not** assert the stronger exterior-gradient conclusion proved for the isotropic quartic local equation in round 10. A quartic Hartree version of that stronger conclusion is recorded separately below. The complete LaTeX version with this improvement is [transport-section.tex](../../manuscripts/critical-structures/transport-section.tex).

## 1. Equations and assumptions

Fix N>=1 and m>1, and put s=m/2. Let a be real, even, positive elliptic, homogeneous of degree m, and smooth away from zero (the C^{N+2} class used in previous sections suffices):

    c |xi|^m <= a(xi) <= C |xi|^m.

Write A(u)=int a(xi)|uhat(xi)|^2, M(u)=||u||_2^2, and

    P(u)=int xi |uhat(xi)|^2.

The momentum is finite because m>1. Consider either:

(L) iu_t=a(D)u-|u|^{p-2}u, p=2+2m/N,

    E(u)=A(u)/2-||u||_p^p/p;

or, when 1<m<N,

(H) iu_t=a(D)u-(K*|u|^2)u,

    E(u)=A(u)/2-H(u)/4,
    H(u)=int int K(x-y)|u(x)|^2|u(y)|^2 dx dy.

For (H), K is real, even, C^1 off zero, homogeneous of degree -m, and

    |K(x)|+|x| |grad K(x)| <= C_K |x|^{-m}.

Positive type or pointwise positivity is NOT needed for the transport theorem. The absolute Riesz interaction supplies all estimates; the conserved energy is that of the actual kernel K. Positivity was needed in the preceding phase-kernel and ground-state arguments, not here.

Let u be a forward-global strong energy solution, approximable on compact time intervals by sufficiently smooth solutions so that the integrated localized virial identity follows by continuity. Assume conservation of M,P,E and

    sup_{t>=0} ||u(t)||_{H^s} <= B < infinity.

This is a statement about such solutions, and does not supply local well-posedness for every anisotropic symbol.

Choose real smooth chi with 0<=chi<=1, chi=1 on |x|<=1, and chi=0 on |x|>=2. Put eta=1-chi and, for a center c,

    T_R^c(t)=|| |D|^s [eta((x-c(t))/R)u(t)] ||_2^2.

One can equivalently use A on the cut-off function, since a is elliptic. This is exterior localized kinetic energy. For noninteger s it is not the literal pointwise tail of |D|^s u, and must not be relabeled as that quantity. Uniformly in R>=1, t and c,

    0 <= T_R^c(t) <= C B^2.

The usual smooth-cutoff product estimate proves this bound:

    || |D|^s(chi_R w)||_2 <= C(|| |D|^s w||_2+R^{-s}||w||_2).

### Literal kinetic tail equivalence

Define D_R^c=int_{|x-c|>R}| |D|^s u|^2 and delta=min(s,1). Then

    sqrt(T_R^c) <= sqrt(D_R^c)+C_B R^{-delta},
    sqrt(D_{2R}^c) <= sqrt(T_R^c)+C_B R^{-delta}.

Indeed Fourier convolution and Young give

    ||[|D|^s,eta_R]u||_2 <= C R^{-s}||u||_2, 0<s<1,

using ||xi|^s-|zeta|^s|<=|xi-zeta|^s. For s>=1, the inequality

    ||xi|^s-|zeta|^s| <= C|xi-zeta|(|zeta|^{s-1}+|xi-zeta|^{s-1})

gives the bound C(R^{-1}||u||_{dot H^{s-1}}+R^{-s}||u||_2). The constant part of eta commutes. Since eta_R vanishes inside R and equals one outside 2R, the two assertions follow. Thus every result below can instead be stated using D_R, with the virial decay exponent changed to beta_literal=min(m/2,2/m); gamma is unchanged. In particular the ballistic statement is a positive average of actual exterior homogeneous kinetic density. Uniform localization about centers differing by a bounded amount then transfers simply by inclusion of balls.

## 2. The key commutator fact: exactness on the core

Choose a real smooth compactly supported vector field f, equal to x on |x|<=4, and set f_R(x)=R f(x/R). Define

    L_R=f_R.grad+(div f_R)/2,
    B_R=-i L_R,
    C_R=[a(D),L_R].

The operator L_R is skew-adjoint, B_R and C_R are symmetric forms, and C_R is an order-m form. Let

    Q_R(w)^2=|| |D|^s w||_2^2+R^{-m}||w||_2^2.

There is a constant C independent of R such that

    |<z,C_R w>|+|<z,m a(D)w>| <= C Q_R(z) Q_R(w).       (2.1)

Here and below sesquilinear forms are understood in energy duality. To check the assertion, first take R=1. In Fourier variables C_1 has kernel, up to fixed normalization and a harmless factor i,

    (a(xi)-a(zeta)) (xi+zeta).fhat(xi-zeta)/2.

Since m>1 and a is homogeneous with a bounded angular gradient,

    |a(xi)-a(zeta)| |xi+zeta|
      <= C |xi-zeta| (|xi|+|zeta|)^m.

Dividing by <xi>^s <zeta>^s bounds the polynomial factor by
C |xi-zeta| <xi-zeta>^s. This is integrable against the Schwartz function fhat. Schur's test gives the H^s-to-H^{-s} bound at scale one. Under the unitary rescaling v(y)=R^{N/2}w(Ry), C_R is R^{-m}C_1, which proves (2.1). No sign of the Hessian of a, or of a localized principal symbol, enters.

Define the kinetic defect

    D_R=C_R-m a(D).

If z is supported in |x|<=2R, then

    <z,D_R z>=0.                                        (2.2)

Indeed L_R z equals the exact dilation generator Lz=(x.grad+N/2)z. For smooth compactly supported z, homogeneity gives

    2 Re<a(D)z,Lz>=m A(z).

The same identity holds for L_R in this pairing, establishing (2.2). Approximation by compactly supported smooth functions, with (2.1), extends the result to every such H^s function. This is a quadratic-form statement; it does not claim that D_R z vanishes as a function.

Now split u=z+w, where z=chi_R u and w=eta_R u. By (2.2),

    <u,D_Ru>=<w,D_Rw>+2 Re<z,D_Rw>.

The product estimate and (2.1) imply, on the bounded energy ball,

    |<u,C_Ru>-m A(u)|
       <= C_B ( T_R^{1/2}+R^{-s} ).                    (2.3)

This exact-core argument is the step that makes the theorem valid for arbitrary anisotropy. The inequality D^2 phi<=I is not sufficient for that purpose in a general symbol.

## 3. Nonlinear and moving-center errors

For a Lipschitz center c with ||c'||_infinity<=L, define

    J_R(t)=2 <u(t),B_R^{c(t)}u(t)>
          =2 Im int f_R(x-c(t)).ubar grad u.

For s<1, the integral is the symmetric H^{1/2} quadratic form, defined by density. The scale-one first-order form bound and rescaling give

    |J_R(t)| <= C(R ||u||_{dot H^{1/2}}^2+M)
              <= C_0 R,                              (3.1)

for R>=1; m>1 ensures H^s embeds continuously into H^{1/2}.

### Local power

The local nonlinear contribution is exactly

    -2(p-2)/p int div f_R(x-c) |u|^p.

The difference from its unlocalized value -4m||u||_p^p/p is bounded in absolute value by C int_{|x-c|>4R}|u|^p. Since eta_R=1 there, critical Gagliardo-Nirenberg interpolation gives

    int_{|x-c|>4R}|u|^p
       <= ||eta_R u||_p^p
       <= C M^{m/N} T_R.                              (3.2)

No sharp constant or near-threshold assumption is used.

### Hartree interaction

Symmetrization gives exactly the nonlinear contribution

    int int rho(x)rho(y)[f_R(x-c)-f_R(y-c)].grad K(x-y) dx dy,

where rho=|u|^2. Its unlocalized value is -mH(u). The difference vanishes when both x and y lie in B(c,4R). Global Lipschitz continuity of f_R and the bound on grad K dominate its absolute value by

    C int int_{at least one of |x-c|,|y-c|>4R}
                 rho(x)rho(y)|x-y|^{-m} dx dy.

Let q=4N/(2N-m). HLS and the critical interpolation

    ||w||_q^2 <= C ||w||_2 || |D|^s w||_2

therefore yield

    |Hartree localized term +mH(u)|
      <= C ||eta_Ru||_q^2 ||u||_q^2
      <= C_{M,B} T_R^{1/2}.                           (3.3)

The singularity at the diagonal is harmless after the symmetrization: the vector-field difference supplies one power of |x-y|. Approximation and HLS justify the formula at the energy level.

### Motion of the center

The center derivative contributes

    -2 c'(t). int Df_R(x-c) Im(ubar grad u).

Its principal part is -2c'.P. The error involves g_R=Df_R-I, which vanishes on B(c,4R). Since eta_R=1 on the support of g_R, its current form on u equals its current form on w=eta_Ru. For smooth functions this follows directly; the extra derivative of eta has real product with |u|^2 and no imaginary part. Density gives the same identity in H^{1/2}.

For each component, the rescaled bounded-coefficient first-order form satisfies

    |Im int g_R wbar grad w|
       <= C(||w||_{dot H^{1/2}}^2+R^{-1}||w||_2^2)
       <= C_M T_R^{1/m}+C_M R^{-1}.                  (3.4)

The last step is Fourier interpolation between derivative orders 0 and m/2. The coefficient g_R is a constant matrix plus a rescaled compactly supported smooth matrix; its first-order form bound follows from the same Fourier-Schur calculation used for B_R, with the constant piece treated directly.

Combining (2.3)--(3.4), put

    gamma=min(1/2,1/m), beta=min(m/2,1).

Then both equations satisfy the **two-sided** integrated bound

    |J_R' - 4m E + 2c'(t).P|
       <= C_1 [ (T_R^c(t))^gamma + R^{-beta} ].       (3.5)

All constants are uniform over centers of speed at most L. Smooth-solution identities extend to the stated energy solution by convergence on each compact time interval: every term on the right is continuous on bounded H^s sets, and (2.1) controls the kinetic form. There is no spatial-moment assumption.

## 4. Persistent transport on the linear distance scale

**Theorem.** Assume E=-e<0 and P=0. For every speed bound L there are nu,d>0, depending only on the equation, M,B,e,L and the fixed cutoffs, such that every center of speed <=L satisfies

    liminf_{T->infinity} inf_{S>=0}
      (1/T) int_S^{S+T} T_{nu T}^{c}(t) dt >= d.       (4.1)

Proof. Integrate the upper half of (3.5) over [S,S+T] and use (3.1):

    C_1 average[(T_R^c)^gamma]
       >= 4m e-C_1 R^{-beta}-2C_0 R/T.

Choose nu>0 with 2C_0 nu<=m e and set R=nu T, held fixed in this time integral. For all sufficiently large T the right side is at least 2m e. Since 0<gamma<=1, Jensen gives

    average[T_R^c] >= (2m e/C_1)^{1/gamma}.

This is uniform in S and c, proving (4.1).

Because T_R is uniformly bounded, a positive proportion of the times in every sufficiently long interval must carry a fixed exterior kinetic amount. This is not a finite propagation-speed assertion, nor a finite radiation-budget bound. The result does not exclude indefinitely replenished exterior activity.

## 5. Exact averaged drift from kinetic localization

**Theorem.** Assume, for a Lipschitz center c,

    lim_{R->infinity} limsup_{T->infinity}
      (1/T) int_0^T T_R^c(t) dt =0.                   (5.1)

Then the limit exists and

    lim_{T->infinity} P.[c(T)-c(0)]/T = 2m E.         (5.2)

Proof. Integrate the two-sided bound (3.5), divide by T, and use (3.1) and Jensen. For fixed R, the discrepancy from (5.2) has limiting absolute value at most

    C [R^{-beta}+(limsup_T average[T_R^c])^gamma].

Let R tend to infinity. This proves the assertion. It holds at every energy sign; negative energy is used only for its exclusion consequence and the center regularization below.

In particular, E<0 and P=0 rule out (5.1). Negative energy also rules out a localized bounded global orbit whose center is sublinear in the momentum direction. For a traveling profile c(t)=vt, (5.2) reduces to the exact identity v.P=2mE derived independently from the profile equation.

## 6. Uniform kinetic localization needs no assumed center regularity

**Theorem.** Suppose E<0 and an arbitrary map b:[0,infinity)->R^N obeys

    sup_{t>=0} T_R^b(t) ->0 as R->infinity.            (6.1)

Then b stays within a bounded distance of a Lipschitz center c; localization (6.1) also holds about c. Therefore

    P.[b(T)-b(0)]/T ->2mE.

In particular, such a solution is impossible if P=0.

Proof details follow. In case (L), use z=p. Negative energy gives

    ||u(t)||_p^p >= p e.

In case (H), use z=q=4N/(2N-m). Since H(u)=2A(u)+4e>=4e and |H(u)|<=C||u||_q^4,

    ||u(t)||_q >= c(e)>0.

In both cases (6.1), the estimates in Section 3, and eta_R=1 outside 2R imply that the L^z norm outside B(b(t),2R) tends to zero uniformly in time. Thus each such ball contains a fixed positive L^z amount for large enough R.

The equation gives ||u_t||_{H^{-s}}<=C_B: for the local power use Holder with H^s->L^p; for Hartree use HLS in the form

    |int (K*|u|^2)u hbar| <= C||u||_q^3||h||_q.

Choose a derivative index sigma strictly between N(1/2-1/z) and s. Interpolation between H^{-s} time continuity and the H^s bound gives

    ||u(t)-u(t')||_{L^z}
      <=C||u(t)-u(t')||_{H^sigma}
      <=C |t-t'|^{(s-sigma)/(2s)}.                   (6.2)

Choose R_0 and then tau>0 so that the outside L^z norm is much smaller than the fixed core norm, while (6.2) is smaller still for |t-t'|<=tau. If the centers b(t),b(t') were more than 4R_0 apart, their radius-2R_0 balls would be disjoint. Restriction to the old core ball would contradict (6.2). Hence

    |b(t)-b(t')|<=4R_0 whenever |t-t'|<=tau.

Piecewise-linear interpolation through b(n tau) gives a center c with speed <=4R_0/tau and |c-b|<=8R_0.

To transfer the homogeneous kinetic localization to c, take R much larger than this fixed displacement. The function eta((x-c)/R) is supported where eta((x-b)/(R/4))=1. Hence

    eta((x-c)/R)u
       =eta((x-c)/R)[eta((x-b)/(R/4))u].

The cutoff product estimate bounds its dot H^s norm by the smaller-radius tail norm plus O(R^{-s})sqrt M, uniformly in time. This proves localization about c. Apply (5.2) and use the bounded displacement to replace c by b.

The condition is weaker than precompactness of the orbit in H^s modulo translations: a fixed localized core may coexist in a bounded family with a fixed-mass packet spreading to infinity whose dot H^s norm tends to zero. Such a diffuse mass tail is allowed by (6.1). No compactness of the frequency distribution is needed.

## 7. Stronger quartic Hartree consequence

When a(xi)=|xi|^4, N>4 and K is homogeneous of degree -4 with the bounds above, define

    G_R^c(t)=int_{|x-c(t)|>R}|grad u(t,x)|^2 dx.

For the usual radial cutoff f_R=grad phi_R with D^2 phi_R<=I, the biharmonic kinetic contribution is at most 8||Delta u||_2^2+O_B(R^{-2}), exactly as in round 10. The Hartree nonlinear error is estimated using q=2N/(N-2) and Sobolev:

    |nonlinear error|
       <= C||eta_Ru||_q^2 ||u||_q^2
       <= C_B ||grad(eta_Ru)||_2^2
       <= C_B (G_R^c+R^{-2}).

The center-current error is <=C sqrt M L (G_R^c)^{1/2}. Thus

    J_R' <=16E-2c'.P+C[(G_R^c)^{1/2}+R^{-2}].

The round-10 integration now yields persistent averaged exterior gradient at radius nu T for every bounded-speed center when E<0,P=0. Uniform gradient tightness with an arbitrary center is likewise impossible (the L^q core and temporal continuity argument regularizes the center). For P nonzero, this favorable-sign estimate supplies the upper drift bound limsup P.[c(T)-c(0)]/T<=8E, rather than the exact drift equality at the stronger kinetic-localization level.

This Hartree extension uses nonlocal pair symmetrization in an essential way, but no sign of K is needed. It does not give the same gradient-level result for a general anisotropic quartic symbol.

## 8. Literature and novelty boundary

Primary sources checked during this round:

1. T. Boulenger, D. Himmelsbach and E. Lenzmann, *Blowup for fractional NLS*, arXiv:1509.08845; J. Funct. Anal. 271 (2016), 2569--2603. https://arxiv.org/abs/1509.08845 . The fractional localized-virial approach and its bounded-observable strategy are prior work.
2. V. D. Dinh, *Blow-up criteria for fractional nonlinear Schrodinger equation*, arXiv:1808.07368. https://arxiv.org/html/1808.07368v1 . Proposition 1.5 is stronger than the present conditional exclusion for isotropic 1<m<2: it already gives finite-time blowup or unbounded kinetic norm along a sequence for nonradial negative-energy mass-critical solutions, without a localization hypothesis. Thus the isotropic fractional specialization is not a new resolution; the scope of interest here is the common anisotropic/all-degree structure and quantitative transport identity.
3. *On finite time blowup for mass-critical Hartree equations*, arXiv:1208.2302. https://arxiv.org/abs/1208.2302 . Negative-energy Hartree blowup via a virial mechanism is prior work; this note must not be presented as its first discovery.

The new claim relative to our previous manuscript is the common anisotropic all-m exterior-kinetic theorem, the exact averaged drift law, the absence of a need for regularity of a uniformly localizing center, and the nonlocal quartic exterior-gradient extension. Establishing whether these precise combined statements are new to the literature needs comparison with the full hypotheses of the preceding works and additional papers. It is safe to describe them as completed extensions within this project, not as resolution of the unrestricted global dynamics problem.

## 9. A tempting phase-space idea not used in the theorem

The symbol p_R(x,xi)=R|xi|h((x.xi)/(R|xi|)), with h'=1 near zero and h'<=1, has

    grad a(xi).grad_x p_R=m a(xi)h'<=m a(xi)

for every positive homogeneous a. This supplies a favorable *principal kinetic symbol* without isotropy. However, turning it into a useful energy-space nonlinear virial requires control of a pseudodifferential nonlinear commutator and low-frequency errors. That argument has not been supplied here. It must not be substituted for the fully proved exact-core localization method above, or used to claim a lower-derivative anisotropic transport theorem.
