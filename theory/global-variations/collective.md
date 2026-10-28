# Finite collective rotations: fixed-scale calculation

This calculation did not exclude a minimal-rank counterexample. It determines the sign of the proposed distant-copy variation and closes its endpoint-angle error. No further separation or scale classification is claimed.

Let (P) be a real optimizer at the first violating rank (N), with

$$
 C=C_N=(1+\delta)C_1,\quad d=C-C_1>0,\quad
 T=T(P),\quad F=\|\rho_P\|_2^2=CT.
$$

Write (E(\Gamma)=CT(\Gamma)-\|\rho_\Gamma\|_2^2), (H=-\Delta-2\rho_P/C), and let (e_N>0) be the smallest occupied binding energy. Lower-rank projections satisfy (F(A)\le C_1T(A)).

## Weighted occupied-space estimate

For a contraction (0\le\Gamma\le P), put (P_t=\mathbf1_{\Gamma>t}). The exact identity

$$
 E(\Gamma)=\int_0^1E(P_t)\,dt+
 \frac12\int_0^1\int_0^1
 \|\rho_{P_t}-\rho_{P_u}\|_2^2\,dt\,du
\tag{1}
$$

retains both the proper-rank deficit and the density variance. Let (\kappa>0) be the smallest eigenvalue of the kinetic matrix (P(-\Delta)P). Consider two contractions in (P) with eigenvalues (w_i) and (1-w_i), allowing independent eigenbases. Put (a=\min w_i), (b=\max w_i). For almost every (a<t<b), their layer projections at (t) and (1-t) have ranks adding to (N). Their kinetic traces therefore add to at least (N\kappa). In each variance term, the two rectangles with one parameter below the smallest occupation and the other above the largest contribute (a(1-b)F). Hence

$$
 E(\Gamma_w)+E(\widetilde\Gamma_{1-w})
 \ge dN\kappa(b-a)+2a(1-b)F.
\tag{2}
$$

This bound is strictly positive except when every (w_i=0) or every (w_i=1). For matching eigenbases, the stronger estimate is

$$
 E(\Gamma_w)+E(P-\Gamma_w)
 =2\int\rho_w(\rho-\rho_w)
 \ge dT(b-a)+2a(1-b)F.
\tag{3}
$$

Indeed (w_i+w_j-2w_iw_j\ge|w_i-w_j|+2a(1-b)), and integration over weight level sets reduces the first term to proper occupied splits, for which (2\int\rho_A\rho_{A^c}\ge dT).

The kinetic constant is quantitative:

$$
 \kappa\ge \frac{T}{1+\delta}(1-\sqrt{1-\delta})^2.
\tag{4}
$$

To check it, the rank-((N-1)) spectral inequality gives (e_N\ge\delta T/(1+\delta)). For any unit (\psi\in P), with (t=\|\nabla\psi\|_2^2) and (e=-\langle\psi,H\psi\rangle\ge e_N), self-consistency, Cauchy–Schwarz and scalar GN give

$$
 t+e=\frac2C\int\rho\psi^2
 \le2\sqrt{Tt/(1+\delta)}.
$$

Solving this quadratic inequality in (\sqrt t) proves (4).

## Exact cosine-sine path to a distant copy

Fix (s>0). Let (Q_R) be the projection onto (s\phi_i(s(x-Re_1))). Choose real principal frames

$$
 \langle e_i,q_j\rangle=\delta_{ij}\cos\alpha_i,
 \qquad e_i\in P,\quad q_i\in Q_R,
$$

and put (f_i=(q_i-\cos\alpha_i e_i)/\sin\alpha_i). For large (R), (\alpha_i\to\pi/2), the (f_i) are orthonormal in (P^\perp), and (f_i-q_i\to0) in (H^1). Define (P_{R,\theta}) by the orthonormal columns

$$
 p_i=\cos\theta_i e_i+\sin\theta_i f_i,
 \qquad 0\le\theta_i\le\alpha_i.
\tag{5}
$$

For (w_i=\cos^2\theta_i), spatial separation gives

$$
 E(P_{R,\theta})
 =E(\Gamma_w^U)+s^2E(\Gamma_{1-w}^V)+o(1)
$$

uniformly in angles and the independently rotated principal frames. Each contraction deficit is nonnegative by (1). Thus

$$
 E(P_{R,\theta})\ge
 \min(1,s^2)[dN\kappa(b-a)+2a(1-b)F]+o(1).
\tag{6}
$$

Uniformity follows from finite-dimensional bounded frame rotations, vanishing translated gradient pairings, and (\|e_iq_j\|_2\to0); the latter follows by compact-support approximation in (L^4). This proves positivity away from the two endpoint vectors. An absolute (o(1)) alone does not cover angles approaching those endpoints.

To close that gap, put (z=\sum_i\sin^2\theta_i). Since (H) preserves (P), the exact finite identity is

$$
 E(P_{R,\theta})=
 C\sum_i\sin^2\theta_i
 [\langle f_i,Hf_i\rangle-\langle e_i,He_i\rangle]
 -\|\rho_{P_{R,\theta}}-\rho_P\|_2^2.
\tag{7}
$$

Here (\langle f_i,Hf_i\rangle\ge-o(1)), (\langle e_i,He_i\rangle\le-e_N), and direct expansion of the density gives

$$
 \|\rho_{P_{R,\theta}}-\rho_P\|_2^2
 \le\varepsilon_Rz+Kz^2,
 \qquad\varepsilon_R\to0.
$$

The linear-in-(\sqrt z) density term contains (e_if_i\to0) in (L^2); the remaining density term is (O(z)) in (L^2). Consequently (E\ge Ce_Nz/2>0) in a fixed small neighborhood of (P), for large (R).

At the **exact** second endpoint (Q_R), use (g_i=\sin\alpha_i e_i-\cos\alpha_i f_i\in Q_R^\perp), (g_i-e_i\to0), and

$$
 p_i=\cos(\alpha_i-\theta_i)q_i+
 \sin(\alpha_i-\theta_i)g_i.
$$

The same argument with (H_{Q_R}=-\Delta-2\rho_{Q_R}/C) gives (E\ge Cs^2e_Nz'/2>0), where (z'=\sum_i\sin^2(\alpha_i-\theta_i)). The remaining angles form a compact set on which the leading bracket of (6) has a positive minimum.

Therefore, for every fixed (s>0) and sufficiently large (R),

$$
 E(P_{R,\theta})>0
 \quad\text{throughout the cube (5), except at }P,Q_R.
\tag{8}
$$

This includes independently rotated bases and angles depending on (R). The proposed finite collective rotation has the wrong sign for excluding the original optimizer. The calculation provides no inequality excluding compact, strongly overlapping competitors; the full sharp LT question remains open here.

The established inputs are the finite-rank optimizer reduction and the earlier lower-rank bounds (R21/R23/R26). The finite-rotation calculations are derived above. 
