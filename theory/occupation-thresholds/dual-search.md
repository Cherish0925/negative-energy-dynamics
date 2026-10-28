# Yukawa resolvent excludes the unequal-scale distant Townes mechanism

2026-10-09. This is an analytic continuation of the exact two-bump reduction in [geometric.md](geometric.md). It resolves the sign of that reduction for every fixed scale ratio. Further direct estimates exclude coupled near-equal-scale distant limits and all sufficiently extreme scale ratios at arbitrary separation. Any possible counterexample within this two-Townes family is confined to a bounded comparable-scale, finite-separation parameter region. This does not prove the unrestricted rank-two Lieb–Thirring inequality.

## A uniform weighted inequality for the Townes profile

Let Q be the positive radial solution of

    -Delta Q + Q = Q^3 in R^2,

let Mc = integral Q^2, and for 0 <= eta < 1 set

    A_eta = integral Q exp(eta x_1),
    B_eta = integral Q^2 exp(2 eta x_1),
    D_eta = integral Q^3 exp(eta x_1).

All these integrals are finite. The Townes equation and exponential decay imply

    D_eta = (1 - eta^2) A_eta.                         (1)

The following inequality holds on the full interval:

    Mc B_eta / (A_eta D_eta)
      <= [Mc/(4 pi)] [sqrt(1-eta^2) arcsin(eta)/eta]
      <= Mc/(4 pi) < 1.                              (2)

The bracketed function is assigned its continuous value one at eta=0.

### Proof

Let G(x) = K_0(|x|)/(2 pi) be the positive Green kernel of -Delta+1. The resolvent representation is Q = G * Q^3. Multiplication by exp(eta x_1) gives the exact convolution identity

    Q exp(eta x_1)
       = [G exp(eta x_1)] * [Q^3 exp(eta x_1)].

The L^1-to-L^2 Young inequality therefore yields

    B_eta <= ||G exp(eta x_1)||_2^2 D_eta^2.            (3)

For completeness, compute the kernel norm without a complex-contour argument. The heat-kernel representation is

    G(x) = integral_0^infty (4 pi s)^(-1)
           exp(-s - |x|^2/(4s)) ds.

Tonelli, the ordinary two-dimensional Gaussian integral, and the substitution s+t=tau, s/(s+t)=theta give

    ||G exp(eta x_1)||_2^2
      = (1/(4 pi)) integral_0^1
          [1 - 4 eta^2 theta(1-theta)]^(-1) dtheta
      = arcsin(eta)/(4 pi eta sqrt(1-eta^2)).           (4)

At eta=0 this is 1/(4 pi). Combining (1), (3), and (4) proves the first inequality in (2).

For 0 <= eta < 1,

    arcsin(eta) <= eta/sqrt(1-eta^2),

because the difference of the right side and left side vanishes at zero and has derivative eta^2/(1-eta^2)^(3/2) >= 0. This proves the second inequality in (2).

Finally, the sharp scalar Gagliardo–Nirenberg constant is 2/Mc. The Gaussian exp(-|x|^2/2) has quotient 1/(2 pi), so Mc <= 4 pi. Equality would force that Gaussian to be an optimizer and hence satisfy the cubic Euler–Lagrange equation after rescaling, which it does not. Thus Mc < 4 pi. No numerical value of Mc or computer-assisted profile estimate is needed. QED.

## Consequence for the rank-two construction

The preceding R15 reduction, for f(x)=a q(ax), g(x)=b q(b(x-R e_1)), q=Q/sqrt(Mc), fixed a>b>0, and eta=b/a, gave

    F - C1 K
      = [2 epsilon_R^2 A_eta^2 / Mc^2] H(eta)
          + o(epsilon_R^2),

where C1=2/Mc and

    H(eta)=Mc B_eta/A_eta^2 - (1-eta^2).

Equation (2) now proves the quantitative, entirely analytic estimate

    H(eta)
      <= -(1-eta^2) {1 - [Mc/(4 pi)]
                          sqrt(1-eta^2) arcsin(eta)/eta}
      <= -(1 - Mc/(4 pi))(1-eta^2) < 0.              (5)

Consequently, for each fixed a>b>0 there exists R_0(a,b) such that for all R>R_0(a,b), the exactly orthonormalized two-Townes pair has F/K < C1. This excludes the proposed counterexample mechanism at **every fixed unequal scale ratio**, including the intermediate interval left open in R15.

The coefficient estimate alone supplies no uniform R_0 as eta approaches one; the final section treats that coupled regime directly. Neither argument excludes an overlapping, non-asymptotic Townes pair or a more general self-consistent nonradial structure. Its value is to remove a whole analytic mechanism from the unresolved rank-two endpoint instead of merely failing to find a numerical counterexample.

## Broader kernel statement

The convolution argument itself is not restricted to the cubic profile. If f = (-Delta+a^2)^(-1) h in R^2 with h >= 0, 0 <= b < a, and h exp(b x_1) belongs to L^1, then

    ||f exp(b x_1)||_2^2
      <= arcsin(b/a) / [4 pi b sqrt(a^2-b^2)]
           ||h exp(b x_1)||_1^2,                    (6)

with the b=0 coefficient 1/(4 pi a^2). The norm is exact for the resolvent map from positive L^1 sources to L^2, approached by approximate point sources. Equation (6) is a direct elementary kernel calculation, not claimed here as a historically new operator inequality.

For Townes, the nonlinear equation additionally fixes the weighted source mass through (1); that identity converts (6) into the strict binding-sign exclusion.

## Verification and originality scope

Every step above is analytic. [r16_yukawa_check.py](../../computations/occupation-computations/r16_yukawa_check.py) optionally checks the closed-form kernel integral by numerical quadrature; that check is a reproducibility aid, not an input to the proof. This note claims a derivation within this project, not priority over the published literature. The Green kernel, Young inequality, and Gaussian bound are standard. Historical novelty would require checking the endpoint two-bump analysis in the finite-rank Lieb–Thirring literature.

## The coupled near-equal-scale limit is also excluded

The following direct argument closes the additional asymptotic loophole where b/a approaches one while the centers separate. Unlike the fixed-ratio expansion, it uses estimates uniform in that coupled limit.

By scale invariance set a=1, b=1-delta in [1/2,1], and retain f=q(x), g=b q(b(x-R e_1)) and s,u,w,v from R15. Constants c,C below are positive, independent of b,R, and may change between occurrences. The standard positive Townes tail implies, globally,

    c exp(-r)/sqrt(1+r) <= q(r) <= C exp(-r)/sqrt(1+r).

In particular q(r) <= C exp(-r), and q(r)^2 <= C exp(-2r)/r for r>0.

### Upper bound on v

Put r_1=|x| and r_2=|x-R e_1|. Then

    v <= C integral exp(-2 r_1 - 2 b r_2)/(r_1 r_2) dx.

Elliptic coordinates with these two foci satisfy

    r_1=(R/2)(cosh(mu)+cos(nu)),
    r_2=(R/2)(cosh(mu)-cos(nu)),
    dx=r_1 r_2 dmu dnu,

for mu>0 and 0<nu<2 pi. Consequently

    v <= C K_0((1+b)R) I_0(delta R)
      <= C exp(-2bR)/[sqrt(R) sqrt(1+delta R)].        (7)

The last inequality uses the elementary positive integral bounds for the two modified Bessel functions; they are uniform for (1+b)R>=1 and delta R>=0.

### Lower bound on s u

Let

    L=min(R/4,1/(4 delta)),

where the second entry is infinite for delta=0. Assume L>=2. On the tube

    x_1=t in [1,L],   |x_2|<=sqrt(t),

we have

    r_1<=t+1/2,
    r_2<=R-t+1/6,
    delta t<=1/4.

The lower Townes tail and integration across the tube therefore give

    s >= c L exp(-bR)/sqrt(R).

Integration defining u over the fixed disk |x|<=1 also gives

    u >= c exp(-bR)/sqrt(R).

Because L is comparable to R/(1+delta R), these yield

    s u >= c exp(-2bR)/(1+delta R).                  (8)

Equations (7)-(8) imply the uniform comparison

    v/(s u) <= C sqrt(1/R + delta).                  (9)

Hence v/[s(u+w)] tends to zero in every coupled limit R->infinity, delta->0.

### The fourth-order overlap term is negligible

The triangle inequality and q(r)<=C exp(-r) give

    s <= C integral exp[-b(r_1+r_2)] dx
      <= C exp(-3bR/4) integral exp(-b r_1/4) dx
      <= C exp(-3bR/4).

Combining this with (8),

    s^4/[s(u+w)] <= C (1+delta R) exp(-bR) -> 0.     (10)

The exact numerator from R15 is

    (1-s^2)^2 (F-C1 K)
       = 2v(1+2s^2) - 2s(u+w)(1+s^2)
           + C1(1+b^2)s^4.

Dividing by s(u+w)>0, equations (9)-(10) show that its right side tends to -2 in the coupled limit. Thus F/K<C1 for all sufficiently large indices along **every** sequence R->infinity, b->1 with 1/2<=b<=1. This includes b=1 identically. QED.

### Uniform comparable-scale corollary

For each b_0 in (0,1), there is R_0(b_0) such that every exactly orthonormalized Townes pair with

    a=1,   b in [b_0,1],   R>R_0(b_0)

satisfies F/K<C1.

Indeed, (9) makes the exclusion uniform for b sufficiently close to one and R sufficiently large. On the remaining compact interval [b_0,1-delta_0], the R15 large-separation expansion is uniform: the positive lower scale b_0 and the positive exponential gap delta_0 provide common integrable exponential majorants in the convolution expansions. The strictly negative coefficient in (5) is bounded away from zero on that compact interval. Combining the two regions proves the claim.

This strengthens the initially stated fixed-ratio result. The next section handles scale ratios tending to zero. Intermediate/overlapping comparable-scale separations and general non-Townes rank-two candidates remain unresolved. The result is an exclusion for this construction family, not an upper bound on the unrestricted rank-two constant.

## Extreme scale separation is excluded at every spatial separation

There exists b_*>0 such that the exactly orthonormalized pair generated by

    f(x)=q(x),   g(x)=b q(b(x-R e_1))

has F/K<C1 whenever 0<b<b_* and R>=0. In particular the claim does not require bR, or R, to be large.

### Proof

Smoothness, strict positivity, and the standard differentiated Townes tail show that

    B := sup_x |grad log q(x)| < infinity.

Set g_0=b q(bR)>0. The log-gradient bound yields, for every x and every R>=0,

    exp(-Bb|x|) <= g(x)/g_0 <= exp(Bb|x|).            (11)

The exponential decay of q makes these bounds integrable against q, q^3 and q^2 when b is small. Dominated convergence is uniform in R because the bounds in (11) are independent of R. Consequently, as b decreases to zero,

    s/g_0 -> A := integral q,
    u/g_0 -> B_3 := integral q^3,
    v/g_0^2 -> integral q^2 = 1,                     (12)

uniformly for all R>=0. Since g_0<=b q(0), also s=O(b), uniformly in R, and

    s^4/g_0^2 = (s/g_0)^4 g_0^2 -> 0.               (13)

The exact numerator, after dropping the negative term containing w, is bounded above by

    2v(1+2s^2) - 2s u(1+s^2) + C1(1+b^2)s^4.

Dividing by g_0^2 and using (12)-(13) gives the uniform limiting upper bound

    2(1 - A B_3).

Integration of the profile equation gives A=Mc B_3. Strict Cauchy–Schwarz applied to Q^(1/2) and Q^(3/2) gives

    Mc^2 < (integral Q)(integral Q^3) = (integral Q)^2.

Therefore A^2>Mc and A B_3=A^2/Mc>1. The limiting upper bound is strictly negative. This proves the claim for all sufficiently small b, uniformly in R. QED.

## Combined scope of the exclusion

After common scaling and exchanging the two packets, every two-Townes construction is parameterized by 0<b<=1 and R>=0. The preceding arguments establish numbers b_*>0 and R_*>0 such that any above-scalar pair in this construction family would have to lie in

    b_* <= b <= 1,   0 <= R <= R_*.

The parameter point (b,R)=(1,0) is degenerate (the two generating functions coincide), so limiting tangent pairs at that point must still be treated if one studies compactness of the resulting normalized functions. The statement here only confines possible counterexamples to a bounded parameter region; it does not assert such a counterexample exists, or that a finite mesh can decide the remaining continuum.

Thus the analytic output of R16 is stronger than a numerical failure to find binding: both escape routes of this natural two-packet family — indefinitely separating the packets, and indefinitely separating their length scales — are rigorously excluded. The full rank-two endpoint still involves all orthonormal pairs and remains outside this result.

## Relation to the published two-packet mechanism

Frank, Gontier and Lewin, *The Nonlinear Schrödinger Equation for Orthonormal Functions II: Application to Lieb–Thirring Inequalities*, Communications in Mathematical Physics **384** (2021), 1783–1828, DOI https://doi.org/10.1007/s00220-021-04039-5, Theorem 2 and Sections 3–4, prove strict improvement over rank one for kappa>max(0,2-d/2) using exponentially small interaction between distant scalar optimizers. In d=2 their assumption is strictly kappa>1. Their Theorem 6(iii)/Proposition 11 also explicitly assume p<2, whereas the present endpoint is p=2. The endpoint exclusion derived here is consistent with those statements and helps explain why the same two-packet mechanism cannot simply be carried to the critical endpoint. This comparison is not a comprehensive priority search, and does not justify declaring this project the first to establish an endpoint exclusion.
