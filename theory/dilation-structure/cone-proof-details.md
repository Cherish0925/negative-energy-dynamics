# Independent mathematical derivation: Round 9 cone theorem

## Verdict

The uniform negative-energy traveling-profile mass gap is supported by the argument, including the simultaneous nonlinear extension. I found no fatal mathematical flaw in the stated energy-space proof. The audit additionally removes every lower bound on the radial derivative of the added dispersion. The decisive refinement is to shift the profile frequency algebraically rather than to estimate the dilation defect.

It concerns traveling profiles and does not establish a decomposition or classification of arbitrary global solutions.

## Strongest checked statement

Fix N>=1, m>1, a real even positive elliptic m-homogeneous principal symbol a, individually C^{N+2} away from zero. Put r=m/N, p=2+2r. Let M_c be the principal sharp GN mass.

The added dispersion b is real even, individually C^{N+2} away from zero, and satisfies

    b>=0,   xi.dot.grad b <= m b,
    |partial^beta b(xi)| <= C_{b,beta}|xi|^{-|beta|}(1+|xi|^m).

No lower bound on xi.dot.grad b/b and no uniform derivative constants across b are needed.

The added local energy G is nonnegative, C^1 on [0,infinity), G(0)=0, and

    0 <= rho G'(rho) <= (1+r) G(rho).

Assume z -> 2G'(|z|^2)z is locally C^1. This last regularity is an actual hypothesis; it does not follow from the cone inequality.

For every weak H^{m/2} profile

    (a(D)+b(D))U + omega U + i v.grad U - |U|^{2r}U
        + 2G'(|U|^2)U = 0,

whose conserved energy

    E = (A+B)/2 - C/p + F

is negative, the proof gives M(U)>=M_c+epsilon, with epsilon depending only on the fixed principal model. The constants of b and G, frequency and velocity are arbitrary. The same local principal-symbol robustness argument remains applicable.

## Independently checked exact algebra

Use

    A = integral a |Uhat|^2,
    B = integral b |Uhat|^2,
    C = integral |U|^p,
    F = integral G(rho), rho=|U|^2,
    H = integral xi.grad b |Uhat|^2,
    D_b = m B-H,
    K_G = N integral (rho G'-G),
    D_G = m F-K_G,
    g = 2G'.

The assumptions imply D_b>=0 and D_G>=0. Each quantity is finite for each profile. No uniform bound on D_b is assumed or needed.

Cutoff dilation gives

    v.P = 2m E-D_b-2D_G.                     (1)

Pairing with U gives

    omega M = r(A+B)+(2m-p)E
                -D_b-2(1-1/N)D_G.          (2)

The nonlinear coefficient follows from

    J=integral g(rho)rho=2F+(2/N)K_G,
    pF-J=(2/N)D_G.

In particular the D_G term in (2) cancels exactly when N=1. Taking G(rho)=c rho also reproduces the expected frequency shift by -2c, independently checking its sign and coefficient.

Write U=X+iY. The imaginary profile equation and P=-2 integral Y grad X give

    m E = <Y,[a(D)+b(D)+omega-|U|^{2r}+g(rho)]Y>
             +D_b/2+D_G.                   (3)

## Shifted-frequency refinement: no radial lower bound

Define

    omega_tilde = omega+[D_b+2(1-1/N)D_G]/M,
    q = M(Y)/M.

Equations (2)-(3) become

    omega_tilde M = r(A+B)+(2m-p)E,

    m E = <Y,[a(D)+omega_tilde-|U|^{2r}]Y>
          + B_b(Y) + integral g(rho)Y^2
          + D_b(1/2-q)
          + D_G[1-2(1-1/N)q].              (4)

This identity is the key improvement. It retains an arbitrarily large dilation defect with a positive coefficient rather than trying to show that the defect vanishes.

Suppose masses of negative-energy profiles tend to M_c. Scale A=1 within the admissible operator/nonlinearity class. The sharp GN inequality gives, with delta=(M/M_c)^r-1,

    0<=B+2F<delta,   -delta/2<=E<0.

Thus B,F,E tend to zero. Principal near-optimizer compactness yields, after translation and constant phase, U_n->Q strongly in H^{m/2}, with Q real. Arrange Y_n perpendicular to Q. Then q_n->0 and omega_tilde_n->r/M_c. Principal phase coercivity implies that the first term in (4) is at least c_Q ||Y_n||_{H^{m/2}}^2/2 for all sufficiently large n. All remaining terms are nonnegative: b>=0, g>=0, and q_n<1/2 eventually. For N>=1,

    1-2(1-1/N)q_n > 0

under the same bound. Therefore E_n>=0, a contradiction.

The proof does not require convergence of omega_n itself, b_n, G_n, or either defect. This closes the uniform theorem over the full one-sided dispersion cone.

For example b(xi)=mu exp(-|xi|^2) is allowed, for arbitrary mu>=0. Its logarithmic radial slope tends to minus infinity, so it is genuinely outside every fixed two-sided radial-slope class while remaining inside the theorem.

## Analytic details checked

1. Individual elliptic bootstrap. Since m>1, the velocity symbol is lower order. A sufficiently large positive shift yields a denominator comparable with 1+|xi|^m. The derivative hypotheses imply the Mihlin bounds for the resolvent into H^{m,q}. Nonlinearity growth is at most |U|+|U|^{1+2r}. Sobolev iteration reaches L^infinity in finitely many steps; then H^m subset H^1 and the explicitly assumed local C^1 chain rule give H^{m+1}. No uniform regularity constants are used in the compactness argument.

2. Growth of G. On [0,1], bounded G' gives G<=C rho and bounded g. On [1,infinity), the upper logarithmic-slope inequality gives G<=G(1)rho^{1+r}, with zero case handled by differential Gronwall; then g<=2(1+r)G/rho. The removed lower condition G<=rho G' is not needed.

3. Nonlocal cutoff commutator. B2 implies

    |b(xi)-b(eta)| |xi+eta|
        <= C_b |xi-eta| [1+(|xi|+|eta|)^m].

For separated frequencies use the zeroth-order bound; for close frequencies the segment stays away from zero and use the first derivative. After dividing by H^{m/2} weights, the kernel is dominated by |k|<k>^{m/2}|fhat_R(k)|, uniformly integrable in R. This proves H^{m/2}->H^{-m/2} form boundedness. Schwartz approximation gives the Euler-multiplier limit. The sphere of radius delta in Fourier integration by parts has boundary flux O(delta^N), since b is bounded near zero; angular discontinuity at the single origin is harmless.

4. Dilation closure. For U_lambda(x)=lambda^{N/2}U(lambda x), the transformed additions are

    b_lambda(xi)=lambda^m b(xi/lambda),
    G_lambda(rho)=lambda^{m+N}G(lambda^{-N}rho).

All sign and upper-dilation conditions are preserved, and energy scales by lambda^m. Individual derivative constants may change; the theorem does not bound them.

5. Variational foundation. I rechecked the round-8 constant-phase optimizer argument, normalized near-optimizer compactness, and the phase-kernel second-variation calculation. In particular the second-order comparison produces (C_1-A B/M)^2<=0, and polarization identifies the entire phase kernel. Compactness of the nonlinear multiplication form then gives coercivity off the constant-phase direction. No positivity or uniqueness of a real optimizer is implicitly required.

## Corrections and limits

Several missing plus signs in the evolving note's phase-energy displays were identified and reported to its author; the equations above state the intended exact sums. No substantive sign error was found.

The lower radial bound on b is superseded by the shifted-frequency argument. The lower nonlinear bound G<=rho G' is also unnecessary, but positivity of g is used in this version. A negative g would require a separate proof and is not silently included.

The theorem does not give a numerical epsilon, prove profile existence for every operator, prove dynamical stability, or settle unrestricted global-solution behavior.
