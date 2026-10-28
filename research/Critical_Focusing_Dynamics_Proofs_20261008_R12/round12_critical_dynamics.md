# Round 12: forced kinetic amplification near critical mass

## Main theorem (new actual-flow conclusion)

Fix N>=1 and the pure focusing mass-critical biharmonic equation

    i u_t = Δ²u - |u|^(8/N)u.

Let M_c be its sharp mass, A(u)=||Δu||_2², E=A/2-||u||_p^p/p,
p=2+8/N, and P=Im∫bar(u)∇u. There exist constants d_0,C_N>0
(depending on the sharp scalar problem and N) such that every forward-global
strong conservative H² solution with

    P=0, E=-e<0, d=(M/M_c)^(4/N)-1 ∈(0,d_0),
    B=sup_{t>=0} A(u(t))<∞

satisfies

    e <= C_N d^(5/3) B.                                      (T)

The solution class is the usual one for which localized mass and virial
identities pass by strong energy-space approximation. The statement does
not assert a local theory in dimensions requiring an independently chosen
solution class.

Therefore every such solution has

    sup_t ||Δu(t)||² >= c_N |E| d^(-5/3).

This strengthens the instantaneous sharp-GN bound A(t)>=2e/d by the
additional factor d^(-2/3). The conclusion concerns real trajectories,
without radial symmetry, finite variance, or an assumed localization
property. It does not rule out arbitrarily large bounded motion, and it
does not prove finite-time blowup.

### Immediate family of examples

Let Q be any real sharp optimizer and α>1, u(0)=sqrt(α) Q, so
M=α M_c, d=α^(4/N)-1, E=-d A(u(0))/2 and P=0.
If the solution is global bounded, then

    sup_t A(u(t))/A(u(0)) >= c_N d^(-2/3).

If a standard continuation theory is available, the full alternative is
finite-time breakdown with divergent H² norm, global unbounded norm, or
a bounded global solution making this mandatory large kinetic excursion.

## Proof

Critical scaling reduces B to one. Then M stays in a fixed compact interval
around M_c, ||u(t)||_H² is uniformly bounded, and sharp GN implies

    2e/d <= A(t) <= 1.

We prove the estimate with constants independent of e/d; this point is
essential.

### 1. Quantitative distance from a constant phase times a real field

For every scalar complex f≠0, put

    D(f)=1- ||f||_p^p / [(p/2)(M(f)/M_c)^(4/N) A(f)].

There is a constant C such that a constant phase θ can be chosen with

    M(Im(e^(-iθ)f))/M(f) + A(Im(e^(-iθ)f))/A(f) <= C D(f).      (1)

This is a real O(2) statement, not the complex one-component polarization
statement (which would be vacuous). Here is a direct proof.

Normalize M=M_c,A=1 by amplitude and spatial scaling. If (1) failed, a
sequence with D→0 would, by sharp-GN compactness modulo translations and
phases, converge strongly in H² to a real optimizer Q. Choose phase so
f=X+iY and ∫QY=0. Let y=M(Y), a=A(Y), r=4/N, κ=p/2=1+r.
Taylor expansion in Y, with uniform Sobolev control, gives

    ||X+iY||_p^p = ||X||_p^p + κ∫|X|^(p-2)Y² + o(||Y||_H²²).

Sharp GN on X gives

    ||X||_p^p <= κ (1-y/M_c)^r (1-a).

Consequently

    κ-||f||_p^p
      >= κ [a+(r/M_c)y-∫|Q|^(p-2)Y²] - o(||Y||_H²²)
      = κ <Y,L_-Y> - o(||Y||_H²²).

The phase operator L_-=Δ²+r/M_c-|Q|^(p-2) is coercive on Q^⊥.
Its kernel is exactly span Q by the sharp interpolation/density strict
convexity argument from rounds 9–11; no L_+ nondegeneracy is used.
Thus D>=c||Y||_H²², contradiction. Compactness of normalized optimizers
makes the constant uniform. When D is bounded away from zero, the left
side is at most 2, giving the global statement.

For a negative-energy state on our trajectory,

    D(u(t)) = [d-2e/A(t)]/(1+d) <= d.

Hence, separately at every time, there is a phase with

    ||Y(t)||_H² <= C sqrt(d),  ||X(t)||_H² <= C.               (2)

No derivative of that phase is taken.

### 2. Density transport is slow, at a scale-independent speed

For a real smooth bounded cutoff φ, the mass identity is

    d/dt ∫φ|u|²
      = 2 Im ∫[2∇φ·∇bar(u)+(Δφ)bar(u)] Δu.

The nonlinear term cancels identically. Substitution u=e^(iθ)(X+iY)
and (2) gives

    |d/dt ∫φ|u|²| <= C sqrt(d)(||∇φ||_∞+||Δφ||_∞).           (3)

This is an integrated identity, so time-dependent phase choices cause no
problem. In particular, for φ(x)=χ((x-b)/R), R>=1,

    |d/dt ∫χ((x-b)/R)|u|²| <= C sqrt(d)/R.                  (4)

The cancellation of R in the center construction below is important:
the concentration radius may depend on e/d, but its resulting speed does not.

### 3. Obtain a center; localization is not an extra hypothesis

Choose ε_0=M_c/32 and d_0 sufficiently small. Sharp-GN near-optimizer
compactness gives a fixed normalized radius capturing M_c-ε_0 of mass.
Since for this particular trajectory A(t)∈[2e/d,1], there exists a finite
R_0>=1, possibly large and depending on e/d, such that at every t there
is c(t) with

    ∫_{|x-c(t)|<=R_0}|u(t)|² >= M_c-ε_0.                    (5)

Let χ equal one on B_1, zero outside B_2. If
|c(t)-c(s)|>4R_0, (5) makes the integral with cutoff centered at c(s)
change by at least M_c-3ε_0, provided M-M_c<=ε_0. By (4) this is
impossible when

    |t-s| <= τ R_0/sqrt(d),

where τ>0 is universal for the fixed scalar problem. Linearly interpolate
c at these times. The resulting center a(t) satisfies

    ||a'||_∞ <= L=C sqrt(d),
    |a(t)-c(t)| <= 8R_0.                                  (6)

In particular a fixed ball about a(t) always contains M_c-ε_0 mass.
Neither scalar ground-state uniqueness nor differentiable modulation is
needed.

### 4. Uniform tail mass equals at most the mass surplus

For each η>0, there is R_η<∞ such that

    sup_t ∫_{|x-a(t)|>R_η}|u(t,x)|² <= M-M_c+η.              (7)

Proof by contradiction: otherwise choose t_k and R_k→∞ so the exterior
mass exceeds M-M_c+η. Translate by a(t_k), extract a weak H² limit v and
strong local L² convergence. From (5)–(6), M(v)>=M_c-ε_0, while the
assumed tail gives M(v)<=M_c-η. The remainder w_k has limiting mass
M-M(v)<=M-M_c+ε_0< M_c. Thus both v and w_k are strictly subcritical.
The quadratic splitting and Brezis–Lieb splitting give

    -e=E(v)+E(w_k)+o(1).

Sharp GN makes both energies nonnegative for all sufficiently large k,
a contradiction. This establishes (7). It allows a genuinely noncompact
mass tail of size M-M_c, and does not assert kinetic tightness.

### 5. Retain the negative exterior kinetic contribution in virial

Choose a real radial φ_R with φ_R=|x|²/2 for |x|<=R, φ_R constant for
|x|>=2R, D²φ_R<=I, and derivative bounds |D^jφ_R|<=C_j R^(2-j).
For example set the radial derivative φ_R'(r)=r h(r/R) with h smooth,
nonincreasing, h=1 on [0,1], h=0 on [2,∞). Define

    J_R=2 Im∫∇φ_R(x-a(t))·bar(u)∇u,
    K_R(t)=∫_{|x-a(t)|>2R}|D²u|²,
    H_R(t)=∫_{R/2<|x-a(t)|<2R}|D²u|².

The tails use the full Hessian. One must not replace |D²u|² by |Δu|²
pointwise on the exterior. Their total integrals agree.

The exact quartic localized identity from round 10 and P=0 give

    J_R' <= -16e -8 K_R + C∫outsideR |u|^p
              + C R^(-2) + C L∫outsideR |u||∇u|.           (8)

Indeed the principal kinetic term is
8 Re∫(∂jkφ_R)∂ij bar(u)∂ik u. Relative to 8A its defect is
nonpositive everywhere and equals -8|D²u|² outside 2R. All other
cutoff terms are O(R^(-2)) under the normalized H² bound. The nonlinear
defect is supported outside R. Motion contributes -2a'·P plus the last
term in (8), and the total momentum is zero. Also |J_R|<=C R.

Fix η>0 and put μ=M-M_c+η. For R>=2R_η choose a cutoff ζ_R zero on
B_{R/2}, one outside B_R. By (7), M(ζ_Ru)<=μ and

    A(ζ_Ru) <= C[K_R+H_R+R^(-2)].

Sharp GN and elementary interpolation therefore give

    ∫outsideR |u|^p <= C μ^(4/N)[K_R+H_R+R^(-2)],
    ∫outsideR |u||∇u|
       <= C μ^(3/4)[(K_R+H_R)^(1/4)+R^(-1/2)].             (9)

Take d_0 and η small enough that C μ^(4/N)<=1. Young's inequality
absorbs both terms containing K_R into its negative coefficient:

    J_R' <= -16e + C μ^(4/N) H_R
            + C L μ^(3/4) H_R^(1/4)
            + C L^(4/3) μ + o_R(1),                       (10)

where o_R→0 uniformly in t. No sign or coercivity in the transition
annulus is assumed.

### 6. Average disjoint annuli; then remove the cutoff

Fix K<∞ and R_*>=2R_η. Let R_j=8^j R_*, j=0,...,K-1. Their transition
annuli (R_j/2,2R_j) are disjoint about the same moving center. Since
A(t)<=1,

    Σ_j H_{R_j}(t)<=1.

For every T choose a j(T) whose time-averaged H_{R_j} is <=1/K. Integrate
(10) and apply Jensen to the fourth root. Since each R_j<=8^(K-1)R_*,

    16e <= 2C 8^(K-1)R_*/T + C μ^(4/N)/K
           + C L μ^(3/4) K^(-1/4)
           + C L^(4/3) μ + sup_{R>=R_*}|o_R(1)|.

Take T→∞ for fixed K,R_*, then K→∞, then R_*→∞, and finally η→0.
All limits are justified in this order; no growing-in-time cutoff is
being differentiated. The result is

    e <= C L^(4/3)(M-M_c).                                (11)

Finally (6) gives L<=C sqrt(d), while M-M_c<=C d. Therefore

    e <= C d^(5/3)

under B=1. Undo critical scaling to obtain (T).

## Scope and remaining issue

The argument proves a quantitative dynamic amplification law. It does not
bound the total kinetic norm from above; a putative global bounded orbit
can satisfy it by reaching a sufficiently high scale. Thus it is not a
proof that every near-threshold negative-energy zero-momentum solution
blows up, nor a proof of growup for all global solutions. Its significance
is that the instantaneous GN scale e/d is dynamically insufficient by a
factor d^(-2/3), without any radial, moment, or localization hypothesis.

Potential further improvement would require a sharper relation between
center motion and conserved momentum, or control of repeated changes of
scale. The fourth-order density velocity depends on a cubic Fourier
moment rather than P, so P=0 alone does not set the physical center speed
to zero. The proof uses precisely the extra small phase component supplied
by critical near-optimizer geometry.

## Finite-time amplification and orbital instability

Assume a maximal H² flow with the usual continuation alternative: a finite
maximal forward lifespan entails ||u(t)||_H²→∞ in the relevant limsup
sense. Then every negative-energy zero-momentum datum in the above mass
window satisfies

    sup_{0<=t<T_+} A(u(t)) >= c_N e d^(-5/3),

because the only case needing proof is the global bounded one. For
u_d(0)=(1+d)^(N/8)Q one has

    A(u_d(0))=(1+d)^(N/4)A(Q),
    e=d A(u_d(0))/2.

Thus, for every prescribed K>1, all sufficiently small d>0 have a finite
forward time t_d<T_+(d) with A(u_d(t_d))>K A(u_d(0)). This includes all
three possible fates: finite blowup, global growup, and bounded global
motion. It is a compulsory finite-time excursion, not just a conditional
statement about a bounded orbit.

Since u_d(0)→Q in H² and P(u_d(0))=0, the standing wave associated with
any real sharp optimizer Q is orbitally unstable in H² modulo phase and
translations. For example choose K=4; the distance from every phase and
translate of Q is bounded below by

    ||Δu_d(t_d)||_2-||ΔQ||_2 >= ||ΔQ||_2

(up to a harmless strictness choice). No radial or L_+ nondegeneracy
hypothesis is involved. The existence and instability statement is
unconditional in N=1,2,3, where the H² local flow and continuation follow
from the standard H² algebra/composition estimates; for larger N it uses
the appropriate established strong H² local theory. Priority versus
existing standing-wave instability results must be checked separately;
the quantitative d^(-2/3) kinetic amplification is the primary new
statement of this argument.
