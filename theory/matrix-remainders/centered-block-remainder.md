# proved centered Gaussian block remainder

This is an proof note. It does not claim a quadratic commutator remainder or a planar constant improvement.

## Finite-matrix statement

Fix `0 < alpha < pi`, numbers `theta_i in [-alpha/4, alpha/4]`, and a positive semidefinite matrix `Gamma`. Set

    C_ij = Gamma_ij / cos(theta_i + theta_j),
    g(s,t) = cos(s+t) [sin(s-t)/(s-t) - cos(s-t)],
    G_alpha = alpha^2 sum_ij g(theta_i,theta_j)
                                Re((C^2)_ij C_ji).

The Stein argument in Read–Schulz, Section 2.2, gives `C >= 0`. Put

    I = (-pi/4, pi/4),
    D(s) = 2 sqrt(cos(2s))/sqrt(3),
    c = 1 - pi/4,
    P_s = 1_{Theta <= s},
    R_t = 1_{Theta > t},
    M_st = P_s C R_t + R_t C P_s,    s < t.

Then the following dimension-independent estimate holds:

    G_alpha >= (2 alpha^2 c^2 / 3)
                  integral_{s<t in I} D(s)D(t) Tr(C M_st^2) ds dt.   (1)

Every integrand on the right is nonnegative. More explicitly, with `L = ran P_s` and `R = ran R_t`,

    Tr(C M_st^2)
      = Tr(C_LL C_LR C_RL) + Tr(C_RR C_RL C_LR) >= 0.               (2)

Indices between the cuts do not occur in (2).

## Gaussian normalization and proof

Read–Schulz Lemma 6 constructs the bilinear form

    B(f,f) >= c integral_I D(s) f(s)^2 ds,

and vectors `v_i = chi_i/sqrt(2)`, where `chi_i` is the indicator of the interval from the smallest `theta_i` to `theta_i`. Its normalization is

    ||v_i-v_j||_B^2 = sqrt(g(theta_i,theta_j)).

For a centered Gaussian process `Z(f)` with covariance `B(f,h)`, define

    sigma_i = Z(chi_i)/sqrt(2),
    K_ij = (sigma_i-sigma_j)^2 C_ij.

The Gaussian fourth-moment identity and the Read–Schulz trace identity give

    G_alpha = (2 alpha^2/3) E Tr(C K^2).                            (3)

Only the finite span of the indicators is needed.

Centered quadratic Gaussian variance is monotone under covariance enlargement. Indeed, if covariance matrices satisfy `Sigma = c Sigma_0 + E`, with `E >= 0`, then for every real symmetric quadratic-form matrix `H`,

    Var(z^T H z) = 2 Tr(Sigma H Sigma H)
                  >= 2 c^2 Tr(Sigma_0 H Sigma_0 H).

The mixed trace is nonnegative because

    Tr(Sigma_0 H E H) = ||Sigma_0^(1/2) H E^(1/2)||_HS^2.

The same result holds for a vector-valued quadratic form with any positive semidefinite output inner product, by decomposing that inner product into scalar squared norms. Apply it to the Hermitian-matrix-valued `K` with squared norm `Tr(C K^2)`. Complex entries cause no change: regard Hermitian matrices as a real vector space.

Since `E Tr(C K^2) >= E Tr(C (K-EK)^2)`, (3) is bounded below by `c^2` times the centered variance for the diagonal covariance

    B_0(f,h) = integral_I D(s) f(s)h(s) ds.

Under this covariance, Wick's formula gives exactly

    E_0 Tr(C (K-E_0 K)^2)
      = (1/2) integral_{I x I} D(s)D(t) Tr(C M_st^2) ds dt
      = integral_{s<t in I} D(s)D(t) Tr(C M_st^2) ds dt.             (4)

Here the symmetric kernel before integration has entries

    M_st,ij = (chi_i-chi_j)(s)(chi_i-chi_j)(t) C_ij.

For `s<t`, the product of indicator differences is one exactly when one index lies below `s` and the other above `t`; otherwise it is zero. This yields the block expression stated above. The factor `1/2` in the first line of (4) is the Wick factor `2` times the square of the `1/2` from `sigma = Z(chi)/sqrt(2)`. Equations (3) and (4) prove (1).

This argument uses monotonicity only of the centered second-chaos norm. It does not assert monotonicity of the full quartic Gaussian expectation.

## Integrated version and endpoint scope

For finitely many orthonormal Hilbert-valued rows `W in H^1`, put `Gamma=WW*`, `A(x)=integral_{-infinity}^x Gamma`, and `Theta_alpha=(alpha/2)(A-I/2)`. The Read–Schulz identity therefore implies

    T_x - (alpha^2/4) integral Tr(Gamma^3)
      >= [alpha^2 (4-pi)^2 / 96]
            integral_x integral_{s<t in I}
                D(s)D(t) Tr(C_alpha(x) M_st(x)^2) ds dt dx.        (5)

This statement is established for every fixed `alpha < pi`. All matrices are finite and the integrals are finite; for example the Stein series gives `||C_alpha||_S3 <= sec(alpha/2) ||Gamma||_S3`. No endpoint formula involving `C_pi` is asserted. The endpoint normalization need not be integrable: on a scalar sharp sech channel, `C_pi=lambda/pi` is constant, so `integral Tr(C_pi^3)` diverges. Passing to `alpha=pi` therefore requires a separate argument that is not supplied here.

## Unresolved comparison

For a separate constant-weight Brownian model `D=1`, let `Theta=diag(theta_i)`,

    E = Tr(C^2 [Theta,[Theta,C]]),
    Y_ij = |theta_i-theta_j| C_ij.

Its centered variance is exactly

    J = (3/8) E - (1/4) Tr(C Y^2).                                (6)

The potentially useful comparison `Tr(C Y^2) <= E` has not been proved here. Nor has a comparison of (1) with a quadratic commutator involving the bounded Stein defect `Q=C-XCX`. Neither comparison is a consequence of covariance monotonicity alone.

Source checked: Larry Read and Marvin Schulz, *The sharp one-dimensional Lieb–Thirring inequality for the sum of eigenvalues*, arXiv:2609.10478, Section 2.2, especially equations (2.12)–(2.15) and Lemma 6; https://arxiv.org/html/2609.10478.
