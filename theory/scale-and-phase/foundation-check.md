# R18 independent foundation derivation and exact asymptotic conserved quantities

Date: 2026-10-10. This note gives the proof details of the global finite-variance alternative and derives an exact split of the conserved quantities and sharper two-dimensional trajectory estimates. The occupation inequalities are mathematical inputs: the two-dimensional R16 inequality and the one-dimensional R17 inequality. In particular, the latter's full simple-leading-occupation range still depends on the stated external Read--Schulz theorem. 

## 1. Exact domain and outcome of the derivation

Consider the finite-component common-density mass-critical equation

    i U_t + Delta U + |U|^(4/d) U = 0,

with either:

* d=2, principal Gram eigenvalue Mc, and m_2/Mc <= epsilon_0 from R16;
* d=1, principal Gram eigenvalue Mc, and m_2/Mc < 1, using the R17 quintic variational input.

All masses are finite. The principal eigenvalue is simple. Assume the solution is forward global and U(0) belongs to Sigma. The R17 argument proves the dichotomy it states: either full H1 scattering, or a single principal scalar ground-state core plus H1-scattering secondary fields. In the second case the core width ell(t) is positive and uniformly bounded above; a positive lower bound, width convergence, and a phase law remain unproved. None of these assertions covers an arbitrary two-dimensional occupation spectrum or general initial H1 data without variance.

Here are the essential points independently checked.

1. The exact compactification and inverse, with t=-1/s>0, are

       W(s,y)=t^(d/2) exp(-it|y|^2/4) U(t,-ty),
       U(t,x)=t^(-d/2) exp(i|x|^2/(4t)) W(-1/t,-x/t).

   Direct differentiation gives A(W)=||[x+2it grad]U||_2^2/4 and E(W)=||xU(0)||_2^2/8. The mass-critical nonlinearity transforms with the same power as the Laplacian in both dimensions.

2. If W extends through s=0 in H1, ordinary local Sigma persistence gives weighted convergence there. Its inverse free comparison therefore gives H1 scattering of U. Finite H1 control alone without the weighted step would not prove that last conclusion, but the required weighted step is available.

3. If W blows up at s=0, the R16/R17 concentration result and the individual primary phase inequality give a unique atom Mc delta_(x_*), and the entire primary variance satisfies

       ||(y-x_*)W_1(s)||_2=O(|s|).

   This is an estimate on the full component. The argument does not assume it initially has a finite variance: bounded phase tests, extended quadratic transport, and passage to the terminal atom establish it.

4. The primary approximation has errors ||r_s||_2=O(lambda), ||grad r_s||_2=O(1), and ||(y-x_*)r_s||_2=O(|s|), with lambda<=C|s|. Inverting the transform gives a physical primary error O(t^-1) in the absolute H1 norm. Removing the quadratic phase is also uniform for 0<ell=t lambda<=C: its nonconstant phase carries a factor ell, which cancels the ell^-1 derivative of the core. There is no hidden positive lower bound on ell in this step.

5. Each compactified secondary has bounded H1 norm and a unique strong L2 terminal field w_j. Its individual transport speed is uniformly bounded. Because W belongs to Sigma before the endpoint, these densities are Cauchy in the ordinary finite-second-moment transport space; their second moments converge. Strong complex L2 convergence plus weighted norm convergence gives strong weighted complex L2 convergence. Inverting the conformal map then gives secondary H1 scattering, even though compactified secondary gradients are only weakly convergent.

6. In one dimension the terminal secondary node uses the one-dimensional H1 Holder estimate and exact Gram orthogonality. Its proof does not incorrectly use a global bound on the quintic forcing. Testing the equation away from x_*, density of those tests in L2, and global L2 precompactness suffice for the unique terminal field.

7. H1 convergence of the error does not by itself justify passing energy through a core whose gradient might diverge. The R17 momentum argument avoids this problem by integration by parts. The energy assertions below use conformal identities and bounds on cross nonlinear terms, not an unjustified continuity argument.

No theorem-changing gap was found in these steps under their stated variational inputs. 
## 2. Notation for the non-scattering branch

Work in the constant Gram eigenbasis. Write

    U(t,x)=e_1 exp(i theta(t)+i v.x/2) ell(t)^(-d/2)
                   Q((x-X(t))/ell(t))
             + exp(it Delta)F(x)+R(t,x),
    F_1=0,   X(t)=vt+x_0+o(1),   ||R(t)||_H1 -> 0.

The physical primary error in fact satisfies the sharper paired bounds

    ||R_1(t)||_2 <= C ell(t)/t,
    ||grad R_1(t)||_2 <= C/t.                              (2.1)

For the first inequality retain lambda=ell/t in the compactified primary error. The phase replacement has L2 error bounded by C(ell+ell^2)/t, also O(ell/t) since ell is bounded. No improved full-vector error rate is asserted here.

Use the following quantities, summed over components for a vector:

    B(f)=integral x |f|^2,                    P(f)=Im integral conjugate(f) grad f,
    V(f)=integral |x|^2 |f|^2,               D(f)=Im integral x.conjugate(f)grad f.

In two dimensions write L(f)=Im integral conjugate(f)(x cross grad f). These are well defined for Sigma fields. The terminal secondary vector w belongs to Sigma. Its inverse conformal free datum F also belongs to Sigma, because the transformation interchanges a first moment and one derivative.

## 3. Exact split of mass, momentum, energy, first moment, dilation and angular momentum

The non-scattering branch obeys

    Gamma(U)=Mc e_1 e_1^*+Gamma(F),
    P(U)=Mc v/2+P(F),
    E(U)=Mc |v|^2/8+(1/2)||grad F||_2^2,                  (3.1)
    B(U(0))=Mc x_0+B(F),
    D(U(0))=Mc x_0.v/2+D(F).                             (3.2)

In two dimensions, additionally,

    L(U)=Mc (x_0 cross v)/2+L(F).                         (3.3)

Thus every conserved quantity displayed here splits exactly into the traveling core contribution and the freely propagating secondary contribution. This does not determine the width or phase trajectory. In particular no assertion is made that the variance V(U(0)) splits into the variance of a fixed-width core and V(F).

### Proof by compactified terminal quantities

Let P_* be the terminal compactified primary momentum. R17 gives

    v=-x_*,   x_0=2P_*/Mc.

Direct differentiation of the conformal transform, and the exact virial identities V_U(t)=V_U(0)+4D_U(0)t+8E_U t^2, give

    P(W)=B(U(0))/2,
    lim_(s->0-) V(W(s))=8E(U),
    lim_(s->0-) D(W(s))=-D(U(0)),
    L(W)=L(U)                 (d=2).                    (3.4)

For example P(W)=B(U(t))/2-tP(U), while B(U(t))=B(U(0))+2tP(U). Also D(W)=D(U(t))-V(U(t))/(2t).

The terminal primary limits are

    B(W_1)->Mc x_*,   V(W_1)->Mc |x_*|^2,
    P(W_1)->P_*,
    D(W_1)->x_*.P_*,
    L(W_1)->x_* cross P_*                (d=2).          (3.5)

The variance and first moment follow from ||(y-x_*)W_1||_2=O(|s|). For dilation, the individual primary phase inequality implies

    |Im integral (y-x_*).conjugate(W_1) grad W_1|
       <=sqrt(2 E_scalar(W_1)) ||(y-x_*)W_1||_2
       =O(|s|),

even if its gradient diverges. Angular momentum uses the radial core plus the O(lambda) L2 and O(1) gradient error, as verified in R17. Secondary weighted strong L2 and gradient weak L2 convergence pass B,V,D,L to w; secondary strong H^(1/2) convergence passes P to w.

With the unitary Fourier convention, the exact terminal-to-free relation is

    w(y)=(2i)^(-d/2) Fourier(F)(-y/2),                   (3.6)

up to the consistent constant branch phase, irrelevant to all displayed quadratic quantities. Hence

    P(w)=B(F)/2,   B(w)=-2P(F),   V(w)=4||grad F||_2^2,
    D(w)=-D(F),    L(w)=L(F)                  (d=2).     (3.7)

Combining (3.4)--(3.7) proves energy, first moment, dilation and angular momentum in (3.1)--(3.3). Momentum and Gram splitting are already proved by the R17 error bounds and strong secondary convergence. The energy proof uses the total compactified variance, whose terminal convergence is justified, and never pairs a small H1 error with an uncontrolled core gradient.

### Independent energy proof and a decay estimate

The primary field in the moving frame satisfies

    0 <= E_scalar(exp(-i v.x/2) u_1(t)) <= C/t^2.        (3.8)

Indeed, applying the centered primary conformal identity to the blowup of W at (0,x_*) gives precisely this field, up to reflection, translation and a constant phase. The R17 bounds give C=8E(W) in d=2 and C=4E(W)/a_epsilon in d=1. Its mass remains exactly Mc.

Every physical cross nonlinear energy is t^-2 times its compactified counterpart. In d=2 both integral |W_1|^2 |W_sec|^2 and integral |W_sec|^4 are bounded. In d=1 all three nonnegative terms in

    E(W)=E_scalar(W_1)+A_secondary(W)/2
       -(1/2)integral rho_1^2 rho_sec
       -(1/2)integral rho_1 rho_sec^2
       -(1/6)integral rho_sec^3

are bounded separately by the endpoint energy remainder. Thus all the physical cross terms are O(t^-2). Strong secondary H1 scattering, (3.8), and the primary momentum limit reproduce the energy identity (3.1). Moreover, in either dimension,

    sum_(j>=2)|| (grad-i v/2)u_j(t)||_2^2
       =sum_(j>=2)|| (grad-i v/2)F_j||_2^2+O(t^-2).     (3.9)

Equation (3.9) concerns the squared kinetic norms in the moving frame. It does not imply an O(t^-1) rate for the secondary H1 field difference.

## 4. Quantitative trajectory and momentum in two dimensions

In d=2, the compactified secondary terminal estimate gives, for every eta<1/4,

    ||W_secondary(s)-w||_H^(1/2) = O(|s|^eta).

Continuity of momentum as a quadratic form on H^(1/2) yields

    P(W_1(s))-P_*=O(|s|^eta).                            (4.1)

Let b_W(s)=B(W_1(s))/Mc. Its exact continuity equation gives

    b_W(s)=x_*+(2/Mc)integral_0^s P(W_1(r)) dr
          =x_*+(2P_*/Mc)s+O(|s|^(1+eta)).               (4.2)

The core center differs from b_W by O(s^2), so inversion proves

    X(t)=vt+x_0+O(t^-eta),        every eta<1/4.         (4.3)

The physical primary centroid b_U(t)=-t b_W(-1/t) has the same expansion. More importantly the exact individual conformal momentum identity reads

    P(W_1(-1/t))=Mc b_U(t)/2-t P(u_1(t)).

Substituting (4.1)--(4.2) cancels the constant intercept and gives

    P(u_1(t))=Mc v/2+O(t^(-1-eta)),
    b_U'(t)=v+O(t^(-1-eta)),       every eta<1/4.        (4.4)

The correction to the physical primary centroid velocity is therefore integrable. No differentiability of the profile modulation center X is needed or asserted. The qualitative versions in either dimension are P(u_1)-Mc v/2=o(t^-1) and b_U'=v+o(t^-1), together with the already established centroid limit.

## 5. One-dimensional radiation has a spectral node at the core velocity

In d=1, the R17 terminal background satisfies w_j(x_*)=0. Since F_j belongs to Sigma, Fourier(F_j) belongs to H1 and has a continuous representative. Formula (3.6), with x_*=-v, gives the exact condition

    Fourier(F_j)(v/2)=0,           j>=2.                (5.1)

The free Schrödinger group velocity is 2xi in these conventions. Thus the free radiation amplitude vanishes at the frequency whose velocity equals that of the core. This is a consequence of exact Gram orthogonality and concentration, not an imposed restriction on the initial radiation.

There is also an estimate for the actual secondary field on the instantaneous core scale, not merely its free asymptote. Compactified orthogonality and the one-dimensional H1 Holder inequality give

    |W_j(s,x_c(s)+lambda(s)z)|
       <=C sqrt(lambda(s))(1+|z|^(1/2)).

Inverting, with ell=t lambda and X=-t x_c, proves

    |u_j(t,X(t)+ell(t)z)|
       <=C sqrt(ell(t))/t (1+|z|^(1/2)).                (5.2)

Consequently the secondary density is bounded on each bounded rescaled core region by C ell/t^2. Against a principal quintic core of density O(ell^-1), its leading extra potential is O(t^-2). This supplies a quantitative coupling estimate. It does not by itself prove that ell converges: neutral scaling directions require an additional dynamical argument.

## 6. Boundaries of these deductions

The new exact charge relations and rates do not enlarge the occupation range of the foundational inequality. They do not settle the full two-dimensional rank-two inequality, the all-H1 scattering problem without variance, the original nonradial BNLS question, or the width/phase classification. In the one-component case the energy and momentum identities force zero scalar energy in the moving frame; sharp scalar GN then recovers the exact traveling ground state, consistently with classical scalar classification. For genuinely mixed spectra, the free radiation terms prevent that last scalar rigidity step from being applied without further work.

## Appendix A. Proof details of the R18 rough-background phase theorem

This appendix directly checks Sections 2--6 of [scale-dynamics.md](scale-dynamics.md). Its special scale gauge is essential: the assertion concerns that C1 modulation scale, not any other nearby scale chosen earlier.

### A.1 Anchoring and rescaled coupling

The estimate

    ||w f||_H1 <= C_w (||grad f||_2+|<f,Q>|)

for a fixed exponentially decaying smooth weight is valid in d=1,2. Subtract the mean c of f on a fixed ball. Poincare and telescoping means bound the local L2 norm of f-c on growing balls by a polynomial in the radius times ||grad f||_2. Exponential decay makes the resulting annular series summable. The positive integral of Q bounds c through <f,Q>. The gradient of w is treated in the same manner; w grad f is bounded directly. This avoids a false global homogeneous Sobolev embedding at the two-dimensional endpoint.

For a physical secondary field rescaled at the primary scale lambda, its gradient is O(lambda). Its Q overlap is also O(lambda), by exact Gram orthogonality and the primary normalized L2 error. The anchored estimate therefore gives weighted local H1 size O(lambda). In d=2, weighted local L4 estimates bound a tested S Q term by O(lambda^2) and a tested S epsilon term by O(lambda^2 ||epsilon||_H1). In d=1, weighted local Linfinity control bounds the tested quintic coupling (2|q|^2S+S^2)q by O(lambda^2). The finite secondary mass enters constants; no small bound on its sum is inserted. Thus the tested forcing estimate in the scale note is justified.

### A.2 Modulation identity and the special cancellation

Substitution of u=e^(i theta)lambda^(-d/2)q(t,(x-a)/lambda) gives exactly

    i lambda^2 epsilon_t-L_+ epsilon_R-i L_- epsilon_I
       -A(Q+epsilon)-i B Lambda(Q+epsilon)
       -i C.grad(Q+epsilon)+N+G=0,

with A=lambda^2 theta'-1, B=lambda lambda', C=lambda a'. In particular the signs of all modulation terms in the scale note are correct.

The gauge equations are

    <epsilon_I,Q>=0,
    <epsilon_R,Q^(p+1)>=0,
    <epsilon_R,partial_k Q>=0.

Their finite-dimensional Jacobian at Q is invertible. The scale entry is

    <Lambda Q,Q^(p+1)>
       =(d/2-d/(p+2))integral Q^(p+2)>0.

Projecting the real equation on Q eliminates its time derivative. Moreover L_+Q=-pQ^(p+1), so the scale gauge eliminates its entire linear real-error term. The surviving equation has

    |A| <= C[(|B|+|C|)||epsilon||_H1+lambda^2].

The imaginary projections onto Q^(p+1) and the translation tests have an invertible leading B,C matrix. Their linear L_- terms are O(||epsilon||_H1). Consequently

    |B|+|C| <= C||epsilon||_H1
                   +C||epsilon||_H1(|A|+|B|+|C|)+C lambda^2.

Since ||epsilon||_H1=O(lambda), absorption gives B,C=O(lambda) and A=O(lambda^2). Thus lambda' and a' are bounded, and theta'-lambda^-2 is bounded. Integrating the last bounded difference on the finite interval gives the stated O(T-t) phase-defect tail. This argument does not infer lambda(t)/(T-t) has a limit.

### A.3 Conformal scaling, including mu tending to zero

Let h=1/s and physical core scale lambda=h mu. The physical residual has L2 size O(lambda), gradient O(1), and position norm O(h). Its conformal image consequently has L2 size O(h mu) and gradient O(h). Rescaling the latter by mu gives a normalized H1 residual O(h mu). The conformal core quadratic phase has, in normalized coordinates, nonconstant part

    h mu a.z/2+h mu^2|z|^2/4,

with bounded a and mu. Its weighted H1 effect on Q is also O(h mu). The implicit gauge adjustment therefore preserves ||epsilon||_H1=O(mu/s), uniformly without a positive lower bound on mu.

The conformal secondary gradients need not be globally finite. This does not spoil the forcing estimate. Remove their quadratic phase, which does not change their density. The resulting fields are the original physical secondary fields rescaled at lambda=h mu. Their gradients are O(h mu). Their Q overlaps are O(h mu): exact physical Gram orthogonality applies, and removing the primary's quadratic phase changes its Q approximation by O(h mu) in L2. For that last statement, the change applied to Q is controlled by its exponential moments; the change applied to epsilon is bounded by 2||epsilon||_2. No moment of epsilon is needed.

The anchored estimate now yields tested coupling O((mu/s)^2). The scalar Taylor remainder has the same order. The same cancellation as in A.2 gives

    |mu^2 vartheta'-1| <= C(mu/s)^2,
    |mu mu'|+|mu a'| <= C mu/s.

Division by mu^2 and mu respectively is legitimate for each mu>0 and leaves constants independent of its lower bound. Therefore

    |vartheta'-mu^-2|<=C/s^2,
    |mu'|+|a'|<=C/s.

The s^-2 error is integrable and gives the stated O(1/s) conformal phase-defect tail.

### A.4 Regularity clarification

For physical modulation, the defining pairings are C1 in time because the H1 solution has an H^-1 time derivative and the modulated tests are Schwartz functions. Implicit differentiation is valid even though the H1-valued field need not be C1 into H1.

For conformal modulation when secondary variances are infinite, it is preferable to justify these derivatives directly by pulling each exponentially decaying, quadratically chirped test back to the physical solution. On each compact conformal time interval these are Schwartz tests with C1 parameter dependence, so the physical H^-1 equation differentiates every required pairing. Neither a global conformal secondary H1 bound nor a claim that the complete conformal nonlinear source belongs to H^-1 is needed. The latter claims should not be presumed in this regime.

Verdict: the rough-background phase theorem closes under its displayed R16/R17 inputs, including the special scale gauge and the weighted anchoring argument. The conformal differentiability clarification above makes explicit how the argument survives infinite secondary variance. This audit does not establish a positive limiting width. Section 7's fixed-frequency phase conclusion is a valid conditional implication if its separate stronger amplitude and width hypotheses are proved.
