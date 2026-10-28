# persistent kinetic amplification in actual time

This note strengthens the round-12 supremum bound to a lower bound on the lower long-time average, without assuming a globally bounded kinetic energy. It stays with the pure mass-critical quartic equation and zero total momentum. It does not prove finite-time blowup or rule out all bounded global motion.

## Theorem

Let

    i u_t = Δ²u - |u|^(8/N) u,
    M = ||u||₂², A(t) = ||Δu(t)||₂²,
    E = A/2 - ||u||_p^p/p = -e < 0,
    p = 2+8/N, P = Im ∫ conjugate(u) ∇u = 0,
    d = (M/Mc)^(4/N)-1.

There are constants d0,c>0, depending only on the scalar sharp problem and N, such that every forward-global conservative strong H² solution in the approximation class of the mass and virial identities, with 0<d<d0, satisfies

    liminf_(T→∞) (1/T) ∫₀ᵀ A(t) dt >= c e d^(-5/3).        (1)

No uniform upper bound on A is assumed. The flow hypotheses are those already made in round 12; for N=1,2,3 the concrete H² local theory is supplied there.

Thus high kinetic energy cannot consist only of an early, isolated excursion followed by a permanently much lower regime. For every fixed starting time, the same lower long-time average holds. In particular, A(t) exceeds every strict lower value than the right side of (1) at arbitrarily late times.

If B=sup A(t)<∞ and L*=c e d^(-5/3) is the right side, then

    liminf_(T→∞) |{t∈[0,T]: A(t)>=L*/2}|/T >= L*/(2B).    (2)

This last estimate is a direct consequence of (1), not a separate dynamical assumption.

## Proof

Write r=4/N and δ=M-Mc. All constants below are independent of e and of the particular orbit, unless a radius is explicitly chosen for that orbit. Sharp GN gives

    A(t) >= a_* := 2e/d > 0.                              (3)

The proof does not normalize sup A. Its intrinsic transport time is

    s(t)=∫₀ᵗ A(τ)^(3/4) dτ.

Since A is continuous and bounded on every compact time interval, s is locally absolutely continuous and strictly increasing; (3) also gives s(t)→∞.

### 1. Scale-sensitive density transport

The real O(2) polarization estimate from round 12 gives, at each separate time, a constant phase with u=e^(iθ)(X+iY), X,Y real, and

    M(Y) <= C d M,  A(Y) <= C d A(t).

No time derivative of θ is taken. Apply this to the exact localized mass identity. With M in its fixed nearcritical interval,

    |d/dt ∫φ|u|²|
    <= C sqrt(d) [||∇φ||∞ A(t)^(3/4)
                    + ||Δφ||∞ A(t)^(1/2)].                (4)

For χ((x-b)/R) with R>=a_*^(-1/4),

    |d/dt ∫χ((x-b)/R)|u|²|
       <= C sqrt(d) A(t)^(3/4)/R.                         (5)

The second term is absorbed because A(t)^(-1/4)/R<=1.

### 2. A moving center with variable speed

Fix ε0=Mc/32 and d0 small. Sharp near-optimizer compactness, after kinetic normalization, supplies a universal radius Rbar and at each time a center c(t) such that

    ∫_(|x-c(t)|<=Rbar A(t)^(-1/4)) |u|² >= Mc-ε0.          (6)

Choose R0>=max(1,Rbar,a_*^(-1/4),Rbar a_*^(-1/4)), increasing constants if necessary. In particular the same mass lies in B(c(t),R0).

Use (5) to compare centers at two times. If |c(t)-c(t')|>4R0, the cutoff centered at c(t') changes by at least Mc-3ε0. This is impossible if

    |s(t)-s(t')| <= τ R0/sqrt(d),

with fixed sufficiently small τ>0. Sample c at equally spaced intrinsic times and interpolate linearly in s. The resulting a(t) satisfies

    |a(t)-c(t)| <= 8R0,
    |a'(t)| <= C sqrt(d) A(t)^(3/4)  for a.e. t.           (7)

It is locally absolutely continuous. Notice that R0 may depend on e/d, whereas the speed constant in (7) does not.

### 3. Uniform tail mass without a uniform kinetic bound

For each η>0 there is Rη<∞ such that

    sup_(t>=0) ∫_(|x-a(t)|>Rη) |u(t,x)|² <= δ+η.           (8)

Here is the extra compactness step needed beyond round 12. Suppose instead that times tk and radii Rk→∞ violate (8). Since |a(tk)-c(tk)|<=8R0, the same lower tail bound holds outside B(c(tk),Rk-8R0). Put Ak=A(tk), λk=Ak^(-1/4), and

    gk(y)=λk^(N/2) u(tk,c(tk)+λk y).

Then A(gk)=1, M(gk)=M, and E(gk)=-e/Ak∈[-d/2,0). By (6), B(0,Rbar) contains at least Mc-ε0 mass of every gk. After a subsequence, gk⇀g in H² and converges strongly locally in L². Thus M(g)>=Mc-ε0>0. The assumed tail is outside the normalized radius

    (Rk-8R0)/λk >= (Rk-8R0) a_*^(1/4) →∞,

so M(g)<=Mc-η. Let wk=gk-g. Quadratic and Brezis–Lieb splitting yield

    E(gk)=E(g)+E(wk)+o(1),
    M(wk)=M-M(g)+o(1)<=δ+ε0+o(1)<Mc.

The sharp inequality gives E(wk)>=0 for all sufficiently large k. Because g is nonzero and strictly subcritical, E(g)>0. Taking a subsequence of E(gk), whose limit is nonpositive, gives a contradiction. This proves (8), including sequences where Ak→∞. It is essential to normalize about c(tk), the center in (6): the normalized difference between a and c need not be bounded, although their physical difference is bounded.

### 4. Localized virial with only integrable kinetic bounds

For the cutoff φR of round 12, centered at a(t), put

    JR=2 Im ∫∇φR(x-a(t))·conjugate(u)∇u,
    KR=∫_(|x-a(t)|>2R) |D²u|²,
    HR=∫_(R/2<|x-a(t)|<2R) |D²u|².

The full Hessian is used in these tails. Its total squared norm equals A, but it must not be identified with the pointwise squared Laplacian on an exterior set. Define

    qR(t)=R^(-2) A(t)^(1/2)+R^(-4).

The exact quartic identity, D²φR<=I, P=0 and conservation give

    JR' <= -16e -8KR + C∫_(outside R)|u|^p
                         + C qR
                         + C |a'| ∫_(outside R)|u||∇u|.    (9)

Its endpoint bound is

    |JR(t)| <= C R A(t)^(1/4).                            (10)

Fix η small, let μ=δ+η, and take R>=2Rη. A smooth exterior cutoff ζR gives

    M(ζR u)<=μ,
    A(ζR u)<=C(KR+HR+qR).

Therefore

    ∫_(outside R)|u|^p <= C μ^r (KR+HR+qR),
    ∫_(outside R)|u||∇u|
       <= C μ^(3/4) (KR+HR+qR)^(1/4).                    (11)

Choose d0 and η so that C μ^r is small. Young's inequality absorbs the KR part into its negative coefficient; apply the same inequality to HR and qR, allowing a fixed multiple of these terms. Equations (7), (9) and (11) imply

    JR' <= -16e + C HR + C μ d^(2/3) A(t) + C qR(t).       (12)

This form is deliberately simple: no uniform bound on A, no pointwise smallness of the transition annulus, and no smooth modulation parameters are needed.

### 5. Endpoint selection and averaging disjoint annuli

Let

    L=liminf_(T→∞) (1/T)∫₀ᵀ A(t)dt.

If L=∞, (1) is immediate. Suppose L<∞, and select Tn→∞ with the averages tending to L. There is tn∈[Tn-sqrt(Tn),Tn] with

    A(tn) <= C(L+1) sqrt(Tn),

since otherwise the integral over that last interval would already exceed the total integral. Consequently tn/Tn→1, the average through tn tends to L (upper bound from Tn; lower bound from the definition of liminf), and

    A(tn)^(1/4)/tn → 0.                                   (13)

Fix an integer K and Rbase>=2Rη, and take Rj=8^j Rbase for 0<=j<K. The transition annuli are disjoint, so Σj HRj(t)<=A(t). For each n choose j(n) whose time average through tn is at most K^(-1) times the time average of A. Integrate (12) at that radius. All chosen radii are bounded by 8^(K-1)Rbase, so (10) and (13) make both endpoint terms divided by tn vanish. Cauchy–Schwarz controls the average of A^(1/2). Letting n→∞ gives

    16e <= C L/K + C μ d^(2/3) L
                   + C Rbase^(-2) sqrt(L)+C Rbase^(-4).

Now let K→∞, Rbase→∞, and finally η→0. Radius-dependent terms cause no issue: the time limit was taken first for each finite choice. Since δ=Mc[(1+d)^(N/4)-1]<=C d,

    e <= C d^(5/3) L.

This proves (1). For (2), use

    (1/T)∫₀ᵀ A <= L*/2 + B |{A>=L*/2}∩[0,T]|/T.

## Amplitude perturbations of a sharp standing wave

For u_d(0)=(1+d)^(N/8)Q, the exact initial identities give e=d A(0)/2. Every global solution therefore satisfies

    liminf_(T→∞) (1/T)∫₀ᵀ A(t)/A(0) dt >= c d^(-2/3).

For each prescribed K>0, all sufficiently small d force A(t)>K A(0) at arbitrarily late times if the solution is global. Finite-time breakdown remains the other continuation alternative. This is stronger than the round-12 finite crossing result, while still not classifying the global orbit as bounded or unbounded.

## Why zero momentum does not improve instantaneous transport

The need for new long-time information is not an artifact of the density estimate. Let Q be a real sharp standing wave with enough elliptic regularity for the following pairings, and let h be real with

    <h,Q>=0,  <h,∂k Q>=0 for every k,
    <h,∂j ΔQ> != 0 for some j.

Such h exists: if ∂jΔQ belonged to span{Q,∂1Q,...,∂NQ}, pairing with Q would remove its Q component, and Fourier transformation would put the nonzero L² function Qhat on the zero set of a nonzero polynomial. That is impossible. The argument can equivalently use smooth compactly supported tests and distributional pairings.

Set uε=(1+a ε²)Q+i εh. Its momentum is exactly zero. Its mass defect is

    dε = (4/N)(2a+M(h)/Mc) ε² + O(ε⁴).

If Q solves Δ²Q+ωQ-|Q|^(8/N)Q=0, then

    E(uε)=ε²[(A(h)-∫|Q|^(8/N)h²)/2-a ωMc]+o(ε²).

A fixed sufficiently large a makes E(uε)<0. Nevertheless its quartic mass current is

    4∫ ξj|ξ|² |uεhat(ξ)|²dξ
      =8ε(1+aε²)<h,∂jΔQ>,

which has size comparable to sqrt(dε). When the first spatial moment is finite this is exactly its instantaneous derivative; in general it is the finite H² Fourier current appearing in localized transport. Thus the implication P=0 ⇒ instantaneous density speed O(d) is false even in the nearcritical negative-energy class. Any stronger transport conclusion must exploit evolution over time.

The Young exponent is also exact for the estimates used here:

    sup_(k>=0) [b μ^(3/4) k^(1/4)-c k]
       = C_c b^(4/3) μ.

Consequently repeating the same tail interpolation cannot eliminate the positive center-motion term. A further closure requires a dynamical correlation between translation and the exterior momentum/energy, or a different monotone quantity. No such closure is asserted in this note.
