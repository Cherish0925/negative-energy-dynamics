# Round 13: momentum-adapted modulation and quadratic center drift

## Scope

This note stays with the pure mass-critical biharmonic equation

    i u_t = Δ²u − |u|^(8/N)u,      N∈{1,2,3}.

Write p=2+8/N, M=||u||₂², A=||Δu||₂²,
E=A/2−||u||_p^p/p, and P=Im∫bar(u)∇u. Let Q be a real sharp ground
wave normalized by

    Δ²Q+Q−|Q|^(p−2)Q=0,       M(Q)=M_c.

This note makes one substantial additional spectral assumption beyond
round 12:

    ker L_+ = span{∂₁Q,...,∂_N Q},
    L_+=Δ²+1−(p−1)|Q|^(p−2).

As in the preceding work, L_-=Δ²+1−|Q|^(p−2) is nonnegative,
ker L_-=span Q, and its inverse on Q-perp is coercive. Weighted
regularity of Q and its dual modes is proved below for this concrete
equation; it is not an additional assumption. The conclusions remain
conditional on the real-sector nondegeneracy hypothesis on Q. They do
not prove that hypothesis for all pure biharmonic ground waves.

## Result

There are a normalized neighborhood U_Q of the phase/translation orbit
of Q and constants d_Q,C_Q>0 with the following property. Let u be a
conservative H² solution, with the usual strong approximation and
continuation property, such that

    0<d=(M/M_c)^(4/N)−1<d_Q,    E=−e<0,    P=0.

Suppose the datum, after amplitude normalization to mass M_c and spatial
normalization to kinetic energy A(Q), belongs to U_Q. Then every
forward-global such solution satisfies

    liminf_(T→∞) (1/T)∫₀ᵀ A(u(t))dt ≥ c_Q e d^(−7/3).      (1a)

In particular, if B=sup_{t≥0}A(u(t))<∞,

    e ≤ C_Q d^(7/3) B.                                      (1)

For the initial data u_d(0)=(1+d)^(N/8)Q, the full continuation
alternative consequently gives

    sup_{0≤t<T_+} A(u_d(t))/A(u_d(0)) ≥ c_Q d^(−4/3).         (2)

More precisely, every factor strictly below the right side is reached
at some finite time, and at arbitrarily late times if the solution is
global. In that case the lower actual-time average of A/A(0) is at
least c_Q d^(−4/3). The result doubles the exponent 2/3 in the
unconditional round-12 amplification to 4/3, under the stated
nondegeneracy assumption. It does not exclude
all global bounded motion and is not a finite-time blowup theorem.

## 1. A center intrinsic to the phase operator

### Weighted regularity of the dual modes follows from the equation

The round-12 elliptic argument gives Q∈H⁶ and, for some a>0,
e^(a<x>)Q∈H⁶. Briefly, V=|Q|^(8/N) belongs to W^(2,∞) and tends to
zero; testing (Δ²+1−V)Q=0 against e^(2φ_R)Q for smooth bounded
truncations φ_R of a<x> gives a uniform weighted H² bound. The exact
identity for w_R=e^(φ_R)Q is

    Re<Δ²Q,e^(2φ_R)Q>
      = ||Δw_R+|∇φ_R|²w_R||₂²
        −||2∇φ_R·∇w_R+(Δφ_R)w_R||₂².

Its error relative to ||Δw_R||₂² is at most Ca²||w_R||_H²².
The exterior potential is small and the interior weighted integral is
uniformly bounded, so the error and exterior potential are absorbed.
Conjugating the elliptic equation and bootstrapping gives weighted H⁶.

Now let L_-Z=f, where Z∈Q-perp and f is either ∂_jQ or ΛQ. For
0<a'<a small enough, e^(a'<x>)f∈H². Use the same bounded truncations,
now with φ_R≤a'<x>, and test the inhomogeneous equation. Its extra
source term satisfies

    |<e^(φ_R)f,e^(φ_R)Z>|
      ≤(1/4)||e^(φ_R)Z||₂²+C||e^(a'<x>)f||₂².

The previous absorption argument gives a uniform weighted H² bound
for e^(φ_R)Z. The interior potential term is bounded by the unweighted
L² norm of the fixed function Z on a fixed ball. After R→∞, the
conjugated equation has bounded smooth coefficients in differential
terms of order at most three, with right side e^(a'<x>)f+Vw.
Successive elliptic gains H²→H³→H⁴→H⁵→H⁶ therefore give

    e^(a'<x>)Z∈H⁶.

Thus ΛQ∈H⁴, all dual modes are sufficiently regular, and in particular
∇Z_j,ΛZ_j,∇W,ΛW∈L². This proof uses no real-sector nondegeneracy.

Let Λ=N/2+x·∇, Z_j=L_-^{-1}∂_jQ, and set

    T_ij=<∂_iQ,Z_j>,       c_j=<ΛQ,Z_j>.

Phase coercivity makes T positive definite. Replacing Q(x) by Q(x+b)
replaces c by c−Tb. Choose b=T^{-1}c once and for all. Thus

    <ΛQ,Z_j>=0.

Now define W=L_-^{-1}ΛQ. Since <ΛQ,Q>=0, this inverse is legitimate.
Selfadjointness gives

    <∂_jQ,W>=0,       D=<ΛQ,W>>0.                           (3)

The strict inequality follows because ΛQ≠0 and ΛQ is Q-perpendicular.
A nonzero L² function cannot be homogeneous of degree −N/2.

## 2. Constrained coercivity and isolation

The sharp mass-critical inequality gives E(f)≥0 for M(f)=M_c,
with E(Q)=0. Its second variation along the mass sphere is therefore

    <L_+h,h>≥0 for <h,Q>=0.

If its constrained quadratic form vanishes, positivity on Q-perp
implies L_+h∈span Q. Differentiate the critical scaling identity:

    L_+ΛQ=−4Q.

The assumed kernel description consequently gives the constrained null
space span{ΛQ,∂₁Q,...,∂_N Q}. Compactness of the decaying potential
relative to Δ²+1 upgrades strict positivity off this finite-dimensional
space to an H² coercive bound. In particular, (3) and T>0 imply

    <L_+h,h> ≥ c||h||_H²² − C<h,Q>²

whenever <h,W>=<h,Z_j>=0. Together with phase coercivity this yields

    <L_+h,h>+<L_-k,k>
      ≥ c(||h||_H²²+||k||_H²²) − C<h,Q>²                  (4)

under the three sets of gauges <h,W>=<h,Z_j>=<k,Q>=0.

The normalized sharp-optimizer orbit of Q is isolated. One way to see
this is a local translation-slice implicit function argument for the
stationary equation, using the invertibility of L_+ off its translation
kernel, and the already established constant-phase property. An
equivalent direct argument applies (4) and the exact mass/energy
constraints to a nearby optimizer: the perturbation norm is bounded by
its own higher-order remainder and hence must vanish.

## 3. The small-deficit trajectory remains in the same component

For each nonzero state f define its continuous amplitude/spatial
normalization to mass M_c and kinetic energy A(Q). For negative energy
and mass parameter d, its normalized sharp-GN deficit is at most d.
The sharp-GN compactness theorem therefore says its distance in H² to
the set G of normalized sharp optimizers tends uniformly to zero as
d→0, modulo translations and phase.

Choose ρ>0 so the quotient ball of radius 2ρ around Q's orbit contains
no other normalized optimizer orbit. If a normalized trajectory reaches
distance ρ from Q's orbit, its distance from that orbit is ρ and its
distance from every other optimizer orbit is at least ρ, by the triangle
inequality. This contradicts uniform distance less than ρ/4 from G once
d is small enough. A trajectory starting at distance less than ρ/2
therefore remains inside distance ρ. Choose ρ initially small enough to
lie in the modulation tube. This applies on the maximal existence
interval; it does not assume a priori that one fixed ground wave
describes the trajectory.

## 4. Exact modulation equations

In that tube write

    u(t,x)=λ(t)^(N/2)e^(iθ(t)) w(s,y),
    w=Q+h+ik,  y=λ(t)(x−a(t)),  ds/dt=λ(t)^4,

with real h,k and gauges

    <h,Z_j>=0,       <h,W>=0,       <k,Q>=0.                (5)

The modulation Jacobian at Q is block diagonal with invertible blocks
T,D,M_c. The proved weighted dual regularity allows differentiation of these
pairings in the energy solution class; unbounded Λh is always paired
by integration by parts against ΛZ or ΛW. Parameters are locally
absolutely continuous, and the following equations hold almost
everywhere. Put

    b=λ_s/λ,       v=λ a_s,       α=θ_s−1,
    F(z)=|z|^(p−2)z,
    R=F(Q+h+ik)−F(Q)−(p−1)|Q|^(p−2)h−i|Q|^(p−2)k.

Then exactly

    h_s=L_-k−Im R+α k−bΛ(Q+h)+v·∇(Q+h),
    k_s=−L_+h+Re R−α(Q+h)−bΛk+v·∇k.                     (6)

In N≤3, H² embeds in L∞ and is an algebra, while p>4. Thus, for
small ε=(||h||_H²²+||k||_H²²)^(1/2),

    ||R||₂ ≤ C_Q ε².                                     (7)

The momentum is invariant under phase and obeys P(u)=λP(w). The exact
zero-momentum condition is

    <k,∂_jQ>=−<k,∂_j h>.                                  (8)

Differentiate (5) using (6). With T_h,jl=<∂_l h,Z_j>, the translation
equation becomes

    [(T+T_h)v]_j
      = <k,∂_j h>+<Im R,Z_j>−α<k,Z_j>+b<Λh,Z_j>.          (9)

The scale equation is

    b[D+<Λh,W>]−v·<∇h,W>
      = <k,ΛQ>−<Im R,W>+α<k,W>.                          (10)

The phase equation is

    α[M_c+<h,Q>]+b<Λk,Q>−v·<∇k,Q>
      = −<h,L_+Q>+<Re R,Q>.                              (11)

For ε small the coefficient matrix of (9)–(11) is a small perturbation
of diag(T,D,M_c), and hence

    |v|+|b|+|α| ≤ C_Q ε.

Substitute this once more in (9). Every term on its right is quadratic:

    |v| ≤ C_Q ε².                                        (12)

This is the crucial cancellation. Momentum does not identify the
ordinary fourth-order density velocity, but it annihilates the linear
translation term in the dual modulation coordinate. The scale and
phase terms have not been discarded: (10) and (11) are precisely what
show that their contribution to translation is also quadratic.

## 5. Energy controls ε² by the mass surplus

Set δM=M(u)−M_c=O(d). Critical scaling preserves mass and gives
E(w)=λ^(-4)E(u)<0. The mass identity says

    2<h,Q> = δM−||h||₂²−||k||₂².

For S=E+M/2, S'(Q)=0. Taylor expansion and (4) yield

    S(w)−S(Q)
      ≥ c_Q ε²−C_Q δM²−o(ε²).

On the other hand S(w)−S(Q)=E(w)+δM/2≤δM/2. Shrinking the fixed
modulation tube and d_Q if necessary therefore gives

    ε² ≤ C_Q d.                                          (13)

Combining (12) and (13), then returning to physical time, gives

    |a_t|=λ³|v|≤C_Q d λ³.                                (14)

The equality a_t=λ³v follows from ds/dt=λ⁴ and v=λa_s;
this scaling factor is essential.

## 6. Kinetic amplification

Assume the forward solution is global. The modulation closeness gives
A(w)≈A(Q), so A(u)=λ⁴A(w) and (14) imply, without any upper bound on A,

    |a_t|≤C_Q d A(t)^(3/4).                                (15)

A ball of radius C_Q A(t)^(-1/4) about a(t) contains more than
M_c−ε₀ mass, with a fixed small ε₀. Also A(t)≥2e/d>0.

Uniform exterior mass is still at most the mass surplus. Indeed if
times t_k and radii R_k→∞ violated the bound, rescale each u(t_k)
about a(t_k) to kinetic energy one. The normalized ball containing
M_c−ε₀ has a fixed radius, and the bad tail radius tends to infinity
because A(t_k)≥2e/d. A weak H² limit g is therefore nonzero but has
M(g)≤M_c−η. The remainder is also strictly subcritical. Energy
splitting would then give a strictly positive limiting energy, whereas
the normalized total energies equal −e/A(t_k)≤0. This contradiction
proves, for every η>0,

    sup_t ∫_{|x−a(t)|>R_η}|u(t,x)|²≤M−M_c+η.               (16)

Apply the actual-time annulus argument in round13_virial_closure.md
with speed coefficient C_Q d rather than C sqrt(d). For clarity, its
precise localized estimate, with μ=M−M_c+η, is

    J_R'≤−16e+C H_R+C_Q μ d^(4/3)A(t)
                     +C[R^(−2)A(t)^(1/2)+R^(−4)],          (17)

where H_R is the kinetic mass in the transition annulus. The factor
d^(4/3) comes from absorbing the exterior current into the negative
exterior full-Hessian energy. It uses |a_t|^(4/3)≤C_Qd^(4/3)A.

Let L=liminf T^(-1)∫₀ᵀA. If L is infinite there is nothing to prove.
Otherwise select endpoint times t_k with averages converging to L and
A(t_k)^(1/4)/t_k→0, as in the actual-time proof. The endpoint estimate
|J_R(t)|≤CRA(t)^(1/4) then vanishes after division by t_k.
For K disjoint geometrically spaced annuli, choose one whose averaged
H_R is at most L/K in the limit. Integrate (17), then send time to
infinity, K to infinity, the base radius to infinity, and η to zero.
The result is

    e≤C_Q(M−M_c)d^(4/3)L≤C_Qd^(7/3)L.

This proves (1a), and the supremum bound (1) follows immediately.

For u_d(0)=(1+d)^(N/8)Q, E=−dA(u_d(0))/2 and P=0. Formula (2)
follows, with the stated average and arbitrarily late crossings in the
global case. If the maximal lifetime is finite, the H² continuation
alternative makes A unbounded; if the solution is global unbounded,
the same is true along a sequence; if global bounded, (1) applies.
Continuity then provides every strictly smaller finite crossing.

## 7. Removing the zero-momentum restriction near a nondegenerate ground

There is a second conclusion under the same sole structural hypothesis
ker L_+=span translations and the same normalized initial neighborhood,
but now **with arbitrary conserved momentum**. Every forward-global
negative-energy nearcritical trajectory in that component satisfies

    liminf_(T→∞) (1/T)∫₀ᵀ A(t)dt ≥ c_Q |E| d^(−2).        (18)

Thus the zero-momentum restriction can be removed in this conditional
near-ground regime. At P=0, (1a) retains the sharper exponent 7/3.

The component trapping, constrained coercivity, and bound ε²≤Cd above
do not use P=0. For general P, the exact momentum identity is

    <k,∂_jQ>=−P_j/(2λ)−<k,∂_j h>.

Accordingly, the right side of (9) acquires P_j/(2λ). Since the
momentum of Q vanishes, |P|/λ≤C_Q ε. Solving the coupled system
first at linear order and substituting back gives

    v=(1/2)T^(-1)(P/λ)+r,       |r|≤C_Q ε²≤C_Q d,
    a_t=(λ²/2)T^(-1)P+ρ,       |ρ|≤C_Q d λ³.              (19)

Do not bound the full momentum term in virial by its absolute value.
Its leading sign is favorable:

    −2a_t·P ≤ −c_Q λ²|P|²+C_Q d²λ⁴.                      (20)

The same uniform exterior mass proof holds for the modulation center.
Before setting P=0, the localized virial inequality is

    J_R'≤−16e−8K_R−2a_t·P+C nonlinear_tail+Cq_R
                                      +C|a_t| current_tail.

Absorbing exterior kinetic energy as before bounds the current term by
Cμ|a_t|^(4/3), plus C H_R+Cq_R. From (19),

    μ|a_t|^(4/3)
      ≤ C_Q μ λ^(8/3)|P|^(4/3)+C_Q μ d^(4/3)λ⁴
      ≤ ε₁ λ²|P|²+C_(Q,ε₁)[μ³+μd^(4/3)]λ⁴.             (21)

Here ε₁ is any fixed sufficiently small number, chosen to absorb its
term into (20). The second Young inequality uses
μλ^(8/3)|P|^(4/3)=μ(λ²|P|²)^(2/3)λ^(4/3), so its residual power is
exactly μ³λ⁴. Since λ⁴≈A,

    J_R'≤−16e+C H_R+C_Q[d²+μ³+μd^(4/3)]A+Cq_R.           (22)

Apply the same endpoint selection and disjoint-annulus averaging,
then send η→0 so μ→M−M_c=O(d). For d<1 the coefficient is at most
C_Q d², proving (18). No Galilean invariance is used or claimed.

## What remains

The stronger exponent follows from a precise use of conserved momentum,
but real-sector nondegeneracy remains an explicit additional assumption.
Weighted regularity has been established from the concrete equation.
Without real-sector nondegeneracy, the round-12 d^(−2/3) amplification
remains the unconditional result.

Even under these assumptions, (1) permits bounded motion on a much
higher kinetic scale. Repeating it at a later time does not change d
or E and therefore does not force an iteration to infinity. A further
step would need either a genuinely monotone scale law or a sign-definite
relation between center drift and the momentum carried by the outer
field. The exact equations (9)–(11) expose the residual quadratic terms
that such a step would have to handle.
