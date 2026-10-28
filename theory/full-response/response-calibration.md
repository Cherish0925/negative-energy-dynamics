# A targeted calibration of the quadratic potential-response family

18 October 2026. Numerical calibration, not a proof about an exact solution
and not an interval-certified inequality. Input: the previously computed
R24 three-mode shell. No new branch search is performed.

## Question and outcome

For the known stationary shell, does the five-dimensional potential family

$$
 W=\Phi^T A\Phi,\qquad A=A^T,\quad\operatorname{Tr}A=0
$$

detect its previously identified relative-scale saddle? **Numerically it
does not.** The largest response ratio in this entire family is approximately
0.954703, below the instability threshold 1. A derivative-dependent
potential constructed from the known unstable direction gives approximately
1.101766, above 1. Thus the full projected-resolvent response detects this
saddle, while the proposed quadratic restriction misses it.

The shell has modal mass beta approximately 12.80583924, above
M_c approximately 11.7008965. It is not a counterexample to the main
conjecture, and this experiment says nothing universal about subcritical
self-consistent optimizers.

## Definitions and exact angular reduction

Write the unnormalized shell as

$$
 U=(f(r),g(r)\cos\theta,g(r)\sin\theta),\quad
 \rho_U=f^2+g^2,\quad H=-\Delta-\rho_U.
$$

The normalized frame is Phi=U/sqrt(beta). Its self-consistent coupling is
beta, and its occupied energies are -1,-e,-e, with
e=0.06222748425517942. Define P to project on these three occupied states.
For a real multiplication potential W, the response is

$$
 \mathcal R(W)=\sum_{i=0}^2
 \langle Q(W\phi_i),[Q(H+e_i)Q]^{-1}Q(W\phi_i)\rangle,
 \qquad Q=I-P.
$$

The instability ratio is 2 beta R(W)/||W||_2^2.

On the radial space L2((0,infinity),r dr), set

$$
 H_m=-\partial_r^2-r^{-1}\partial_r+m^2/r^2-f^2-g^2,
 \quad
 I_{m,\epsilon}(s)=
 \langle Q_m s,[Q_m(H_m+\epsilon)Q_m]^{-1}Q_m s\rangle.
$$

Q_0 removes f, Q_1 removes g, and Q_m=I for m>=2. These removals apply for
*every* resolvent energy. In particular, H_0+e has a negative occupied
ground-state direction, which must be removed; removing only zero modes
would give the wrong calculation.

Rotational symmetry splits the trace-free potential family into sectors
ell=0,1,2 of dimensions 1,2,2. The radial profiles, up to irrelevant scalar
factors, are

$$
 w_0=g^2-2f^2,\qquad w_1=fg,\qquad w_2=g^2.
$$

For ell>0 take W=w_ell cos(ell theta); the sine partner has the same ratio.
Let J=int w_ell^2 r dr. Exact angular integration gives

$$
 q_0=\frac{2}{J}\{I_{0,1}(w_0f)+I_{1,e}(w_0g)\},
$$
$$
 q_1=\frac{2}{J}\{I_{1,1}(w_1f)
       +\tfrac12 I_{0,e}(w_1g)+\tfrac12 I_{2,e}(w_1g)\},
$$
$$
 q_2=\frac{2}{J}\{I_{2,1}(w_2f)
       +\tfrac12 I_{1,e}(w_2g)+\tfrac12 I_{3,e}(w_2g)\}.
$$

Different sectors are orthogonal for both the response form and the L2
denominator, so the largest of these three numbers is the maximum over the
full five-dimensional trace-free family.

The trace-free restriction is not the cause of the missed instability.
Adding the trace direction enlarges only the radial block, to
span{f^2,g^2}. At R=65,h=0.005 its two generalized response eigenvalues are
approximately 0.67727832 and 0.92160629. The largest eigenvalue over the
entire six-dimensional real symmetric quadratic family is still the
ell=1 value 0.95470765. The script also computes this enlarged radial block
at each grid resolution.

## Resolvent discretization and controls

The script uses conservative radial finite volumes on cell centers
r_j=(j+1/2)h, conjugated by sqrt(r) to obtain a symmetric matrix. It imposes
zero flux at the origin and a distant Dirichlet boundary. For m=0,1, the
occupied-state orthogonality is imposed by a saddle-point linear system,
not by deleting a numerically selected eigenvector. Solving the resolvent
includes all unoccupied bound states and the large-box representation of
the continuum.

At R=65,h=0.005, the lowest radial eigenvalues are approximately:

| m | First four eigenvalues of H_m |
|---|---|
| 0 | -1.00000555, -0.02213158, 0.00310083, 0.01263419 |
| 1 | -0.06222761, 0.00364045, 0.01248481, 0.02656527 |
| 2 | 0.00622434, 0.01658967, 0.03119799, 0.04974954 |
| 3 | 0.00963273, 0.02253253, 0.04000242, 0.06200444 |

The additional unoccupied m=0 bound state is retained. The occupied shell
is the lowest three-dimensional space in this discretization, so all the
restricted denominators used above are positive.

Two controls use the same resolvent:

1. Common dilation: W=2 rho_U+r rho_U'. For an exact stationary critical
   profile its ratio is exactly 1. This follows by differentiating the
   spatially scaled equation and projecting out the occupied states.
2. Core relative dilation: W=f(f+r f'). This is the density response of the
   already identified negative direction h=(f+r f',0,0). Positivity of the
   projected linear operator and Cauchy--Schwarz imply that a negative
   constrained Hessian in that direction forces the response ratio above 1.

The controls test the normalization, occupied-state projection and the
ability to detect the specific known saddle.

## Numerical values

| R | h | q_0 | q_1 | q_2 | Common dilation | Core relative dilation |
|---|---|---|---|---|---|---|
| 45 | .04 | .9207395772 | .9549776367 | .6716584787 | 1.0007343207 | 1.1028475962 |
| 45 | .02 | .9203116873 | .9547719071 | .6716341270 | 1.0001833780 | 1.1020363313 |
| 45 | .01 | .9202048211 | .9547204970 | .6716280379 | 1.0000458170 | 1.1018337746 |
| 45 | .005 | .9201781111 | .9547076458 | .6716265154 | 1.0000114376 | 1.1017831515 |
| 65 | .01 | .9202048217 | .9547204973 | .6716282077 | 1.0000458382 | 1.1018337804 |
| 65 | .005 | .9201781118 | .9547076462 | .6716266855 | 1.0000114588 | 1.1017831574 |
| 65 | .0025 | .9201714347 | .9547044335 | .6716263049 | 1.0000028646 | 1.1017705027 |

The leading mesh errors exhibit second-order convergence. A simple
second-order extrapolation of the last two rows gives
(q_0,q_1,q_2) approximately
(0.9201692090,0.9547033626,0.6716261780), and the core-dilation control
approximately 1.1017662844. These are numerical estimates, not rigorous
error enclosures. The conclusion of this calibration is insensitive to
the observed mesh and radius differences.

Files: r31_response_calibration.py (reproduction),
r31_response_calibration.json (raw results), this note (formulas and scope).

## Optimizing the two derivative potentials

The targeted extension uses the two-dimensional radial space

$$
 W_f=f(f+r f'),\qquad W_g=g(g+r g').
$$

Their common sum is one half of the exact dilation potential. Let
J_ij=int W_i W_j r dr, and define S by

$$
 c^TSc=2\{I_{0,1}((c_fW_f+c_gW_g)f)
                +I_{1,e}((c_fW_f+c_gW_g)g)\}.
$$

The extremal response ratios are the generalized eigenvalues of (S,J).
This also permits a direct comparison with the original independent
orbital dilations. Restricting the orbital response to
(a_f Lambda f, a_g Lambda g cos(theta), a_g Lambda g sin(theta)) gives
the response matrix

$$
 S_{\rm dil}=2B\,\operatorname{diag}(k_f^{-1},k_g^{-1})B^T,
$$

where k_f=<Q_0 Lambda f,(H_0+1)Q_0 Lambda f>,
k_g=<Q_1 Lambda g,(H_1+e)Q_1 Lambda g>, and
B_ij=<W_i,u_j Q_j Lambda u_j> in radial measure. For an exact continuum
profile, B=J and k_i=2 sum_j J_ij. The code evaluates the projected
discrete quadratic costs and couplings directly, so both full and
restricted responses use the same operator and orthogonality convention.

The variational formula for a positive inverse gives S-S_dil>=0: allowing
all unoccupied states can only increase the response. The numerical values
are:

| R | h | Full derivative response eigenvalues | Dilation-restricted response eigenvalues |
|---|---|---|---|
| 65 | .005 | 1.0000114586, 1.3643745430 | 1.0000114577, 1.2124317939 |
| 65 | .0025 | 1.0000028646, 1.3643683090 | 1.0000028630, 1.2124252901 |

The first eigenvalue approaches the exact common-dilation value 1.
Second-order extrapolation of the nontrivial eigenvalues gives
approximately 1.36436623 for the full response and 1.21242312 for the
dilation-restricted response. The full spectral relaxation increases this
calibrated instability ratio by approximately 0.151943.

At the finest mesh, the optimal potential is proportional to

$$
 \boxed{W_g-0.3196391683\,W_f.}
$$

Its radial L2-normalized coefficient vector is
(-0.4037965911,1.2632888302). The computed matrices are

$$
 J=\begin{pmatrix}
 1.2883069357&-0.0630422429\\
 -0.0630422429&0.4546793733
 \end{pmatrix},\qquad
 S=\begin{pmatrix}
 1.4194185801&-0.1941488706\\
 -0.1941488706&0.5857856163
 \end{pmatrix}.
$$

This supplies an explicit potential witness with a substantially stronger
response than the independent-dilation restriction on this shell. It does
not establish a sign for an arbitrary self-consistent solution or a
subcritical optimizer. The occupied shell, its relative-scale instability,
and the exact response variational principle are existing inputs; this
extension is their targeted numerical evaluation, not a new general
instability theorem.

## Consequence for the current route

Retain the full projected spectral response as a possible analytical
mechanism, including derivative-dependent and nonlocal potential
directions. Do not assume that trace-free quadratic functions of the
occupied orbitals supply a universal instability witness. This finite
family misses an actual computed saddle even though the same response
operator detects its derivative-dependent direction. A universal
subcritical instability theorem remains unproved.
