# Proof details: higher-order converse and bounded-order boundary

Date: 2026-10-08.

## Higher-order manuscript verdict

I independently checked `round9_superorder_converse.md` and found no mathematical error in the stated theorem. For fixed k>m>1 and epsilon>0, all of the following are established by the supplied argument:

- The constrained infimum is zero and unattained for 0<M<=M_c,m.
- It is finite, negative and attained for every M>M_c,m.
- Every minimizing sequence is strongly precompact in H^{k/2} modulo translations and subsequences.
- A minimizer can be chosen real; no false higher-order modulus inequality is used.
- The weak minimizer is L^infinity and H^{k+1}, has positive frequency, and generates a global negative-energy zero-momentum standing wave.
- The exact energy formula and the quantitative low-frequency bounds, including the improved factor m/k, are correct.
- Lower-order-normalized minimizers converge subsequentially modulo translations and phase to the lower-order GN optimizer set in H^{m/2}.

The optional matching energy upper bound correctly retains the extra hypothesis that a lower-order optimizer belongs to H^{k/2}; it must not be removed for arbitrarily large k.

The concentration-compactness details are sufficient: strict binding covers splits involving subthreshold pieces, and vanishing residual mass annihilates the nonlinear term by the GN mass factor. The real-minimizer proof normalizes real and imaginary components to the same mass and uses convexity, so it works for higher-order kinetic operators without a maximum principle.

## Important scope qualification

The higher-order example epsilon|xi|^k violates both the upper dilation inequality and the original order-m growth assumption. Alone it does not establish sharp necessity of the dilation inequality while all other original operator-class assumptions are retained.

A stronger same-order construction is given in [bounded-boundary-section.tex](../../manuscripts/dilation-structure/bounded-boundary-section.tex).

For every real-even positive elliptic m-homogeneous principal symbol a, let

    b(xi)=epsilon a(xi)|xi|^q/(1+|xi|^q), q>0.

Then 0<=b<=epsilon a, all order-m symbol derivative bounds hold, but

    m b-xi.dot.grad b
       =-epsilon q a(xi)|xi|^q/(1+|xi|^q)^2<0.

For each mass

    M_c,a < M < (1+epsilon)^(N/m) M_c,a,

the constrained energy is coercive, negative and attained by a real minimizer. Coercivity uses b>=(epsilon-eta)a-C_eta and eta<epsilon-d, where d=(M/M_c,a)^(m/N)-1. Strict negativity follows by low-frequency dilation of a smooth negative-principal-energy trial function. The same amplitude binding and Hilbert/Brezis-Lieb splitting give strong H^{m/2} compactness. In the final residual step, the critical nonlinearity still vanishes because

    ||w_n||_p^p <= C M(w_n)^(m/N) A(w_n) -> 0.

The energy of the resulting stationary profile is exactly

    -epsilon q/(2m) integral a(xi)|xi|^q/(1+|xi|^q)^2 |Qhat(xi)|^2.

Thus the upper dilation condition cannot simply be dropped even among arbitrarily small, same-order quadratic-form perturbations. This does not assert that every individual violation destroys the gap.

## Prior-work positioning

A concrete earlier primary-source match is:

D. Bonheure, J.-B. Casteras, E. Moreira dos Santos, R. Nascimento,
"Orbitally stable standing waves of a mixed dispersion nonlinear Schrodinger equation,"
arXiv:1710.09775v2 (2018),
https://arxiv.org/html/1710.09775v2

Theorem 1.1(ii) already gives constrained minimizers above the critical mass for the lower-order critical exponent sigma=2/N in the m=2,k=4 prototype. Lemma 2.6 states the corresponding threshold for zero versus negative constrained infimum. This confirms that higher-order variational stabilization is inherited mathematics, not a first discovery in this work.

The general-symbol same-order saturating construction is valuable here as an exact boundary/counterexample to unrestricted robustness. The proof itself uses standard constrained minimization. I did not establish an exhaustive literature priority claim for that construction.
