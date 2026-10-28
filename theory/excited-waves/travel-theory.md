# negative-energy traveling waves for pure mass-critical BNLS

Date: 2026-10-07. This note distinguishes exact identities, a conditional counterexample theorem, and unproved candidate mechanisms. No N>=2 negative-energy traveling wave has been proved here.

## 1. Exact identities and signs

Use p=2+8/N and

$$
 E(Q)=\tfrac12\|\Delta Q\|_2^2-\tfrac1p\|Q\|_p^p,
 \quad M(Q)=\|Q\|_2^2,
 \quad P(Q)=\operatorname{Im}\int\overline Q\nabla Q.
$$

The ansatz u(t,x)=exp(i omega t)Q(x-vt) gives

$$
 \Delta^2Q+\omega Q+i v\cdot\nabla Q-|Q|^{p-2}Q=0.\tag{1}
$$

Its action is S_v=E+omega M/2-v dot P/2. In particular, the sign of the momentum term is negative. Mass-preserving isotropic dilation gives

$$
 4E(Q)=\tfrac12v\cdot P(Q),\qquad E(Q)=\tfrac18v\cdot P(Q).\tag{2}
$$

These identities require the usual elliptic Pohozaev justification, for example sufficiently regular exponentially decaying profiles. They also extend through cutoff arguments under the standard integrability assumptions. Stationary profiles have E=0, including excited stationary profiles.

### Full affine identity

Define, with unitary Fourier transform,

$$
 T_{jk}=\int\xi_j\xi_k|\xi|^2|\widehat Q(\xi)|^2d\xi,
 \qquad F=\|Q\|_p^p.
$$

For Q_A(x)=det(A)^(1/2)Q(Ax), differentiation at A=I in entry A_jk gives

$$
 2T_{jk}-\frac4{Np}F\delta_{jk}-\frac12v_kP_j=0.\tag{3}
$$

The transpose version with v_jP_k is equivalent after all index pairs are included. Since T is symmetric, v tensor P is symmetric, hence P is parallel to v whenever v is nonzero. Taking v=v e_1,

$$
 T_{jj}=\frac{2F}{Np}\quad(j\ge2),\qquad
 T_{11}=\frac{2F}{Np}+\frac14vP_1,\qquad T_{jk}=0\ (j\ne k).
$$

Thus negative energy forces T_11<K/N, where K=tr(T)=||Delta Q||_2^2. The profile must have less integrated kinetic weight along propagation than in transverse directions. Positivity of T does not prohibit this; it only bounds how negative vP_1 can be.

### Phase-modulation identity

Vary Q by exp(i a dot x)Q. The nonlinear and mass terms are unchanged, giving

$$
 4\int |\xi|^2\xi |\widehat Q(\xi)|^2d\xi=M(Q)v.\tag{4}
$$

Equation (4) determines a weighted third moment, whereas P is the first moment. Their directions/signs cannot be identified solely from this moment equation. A general spectral distribution may have first and weighted third moments of opposite signs. Therefore (4) is not a proof that v dot P is nonnegative.

## 2. Conditional theorem reducing a genuine N=2 counterexample to one stationary profile and two spectral checks

Set N=2, p=6 and omega=1. Suppose Q is a real, smooth, sufficiently decaying stationary profile satisfying

$$
 \Delta^2Q+Q-Q^5=0,
$$

even in both coordinates. Define

$$
 L_+=\Delta^2+1-5Q^4,\qquad L_-=\Delta^2+1-Q^4.
$$

Assume:

1. L_+ is invertible from H^4 functions even in both coordinates to the corresponding L^2 space.
2. L_- is invertible from H^4 functions odd in x_1 and even in x_2 to the corresponding L^2 space.
3. With z=L_-^{-1}partial_1 Q in that parity sector,
   $$
   I(Q):=\langle\partial_1Q,z\rangle<0.\tag{5}
   $$

Then (1) has a smooth branch Q_v for all sufficiently small real velocities v e_1, and all sufficiently small nonzero v give E(Q_v)<0. Consequently u_v(t,x)=exp(it)Q_v(x-vte_1) is a global H^2 solution with constant H^2 norm and negative energy: a complete counterexample to the universal finite-time claim in dimension two.

**Proof.** Apply the real Banach-space implicit-function theorem to (1) in the symmetry space

$$
 Q_v(-x_1,x_2)=\overline{Q_v(x_1,x_2)},\qquad
 Q_v(x_1,-x_2)=Q_v(x_1,x_2).
$$

At v=0 its derivative is diag(L_+,L_-) on real even-even and imaginary odd-even sectors. Assumptions 1-2 remove all kernels in those sectors. The quintic nonlinearity is smooth from H^4(R^2) to L^2(R^2), so the theorem applies. Differentiating (1),

$$
 Q_v=Q-i v z+O(v^2).
$$

Reflection/conjugation symmetry makes real terms even in v and imaginary terms odd. Integration by parts yields

$$
 P_1(Q_v)=2vI(Q)+O(v^3),\qquad
 E(Q_v)=\frac{v^2}{4}I(Q)+O(v^4).
$$

The second identity follows from (2). If I(Q)<0, energy is strictly negative for small nonzero v. The profile defines an exact all-time solution; its H^2 norm is translation/phase invariant. No stability of the wave is required for a counterexample.

**What remains unproved:** existence of an exact profile Q satisfying all three assumptions. A discretized negative I is an excellent candidate, not the theorem's hypotheses. An interval validation of Q and parity-restricted spectral gaps would suffice; one would not have to validate an entire finite-velocity curve numerically.

## 3. What does and does not protect the inverse sign

If L_- is strictly positive on the odd-even sector, then I>0. Thus ordinary ground-state branches covered by this positivity cannot provide small-velocity negative-energy waves.

### Exact exclusion for every minimizing boosted ground state

There is a stronger variational conclusion that does not require v to be small. Suppose Q is a nonzero optimizer of

$$
 J_v(f)=\frac{\|\Delta f\|_2^2+\omega\|f\|_2^2-v\cdot P(f)}{\|f\|_p^2},
$$

normalized to solve (1), in the positive-symbol regime where this minimization defines a boosted ground state. Complex conjugation preserves the denominator, mass and kinetic terms and reverses momentum. Therefore J_v(Q)<=J_v(bar Q) implies v dot P(Q)>=0, and (2) gives E(Q)>=0.

If v is nonzero and equality holds, bar Q is another optimizer with the identical normalization because both its quadratic functional and its L^p norm equal those of Q. Thus bar Q solves (1). Conjugating the equation for Q also gives the equation for bar Q with v replaced by -v. Subtraction yields v dot grad(bar Q)=0. A nonzero function constant along the v-direction cannot belong to L^2(R^N), contradiction. Hence all nonzero moving minimizing ground states satisfy E(Q)>0. This argument does not apply to excited saddle critical points, which do not minimize J_v.

Excited states may have negative eigenvalues. The facts

$$
 L_+\partial_1Q=0,\quad L_-=L_++(p-2)|Q|^{p-2},\quad
 \langle\partial_1Q,L_-\partial_1Q\rangle
 =(p-2)\int|Q|^{p-2}|\partial_1Q|^2>0
$$

do NOT imply a positive inverse quadratic form. An exact finite-dimensional counterexample to that proposed inference is

$$
 A=\begin{pmatrix}0&0\\0&-1\end{pmatrix},\quad
 D=\begin{pmatrix}1&2\\2&4.5\end{pmatrix}>0,\quad
 B=A+D=\begin{pmatrix}1&2\\2&3.5\end{pmatrix},\quad f=(1,0).
$$

Here Af=0, f^T Bf=1, but f^TB^{-1}f=-7. A new PDE-specific fact would be needed to prove positivity for all excited profiles. No such fact for the mass-critical powers p-2<=4 was established in this search. Conversely, absence of a positivity proof is not proof that negative I occurs in N>=2.

### Frequency scaling cannot change the sign

For a mass-critical stationary branch,

$$
 Q_\omega(x)=\omega^{N/8}Q_1(\omega^{1/4}x),\qquad
 I(Q_\omega)=\omega^{-1/2}I(Q_1).\tag{6}
$$

Therefore varying omega along a scale-equivalent profile family cannot turn a positive I into a negative I. Candidate searches must change the excited profile, geometry, angular sector, or finite dimensionless velocity v/omega^(3/4).

## 4. Radial and vortex reductions

For a radial real profile Q(r), the translation forcing is Q'(r)x_1/r. Write

$$
 A_1=\partial_r^2+\frac{N-1}{r}\partial_r-\frac{N-1}{r^2},\qquad
 L_{-,1}=A_1^2+\omega-|Q(r)|^{8/N}.
$$

Solve L_{-,1}z=Q' in the regular l=1 radial sector. Then

$$
 I=\frac{|S^{N-1}|}{N}\int_0^\infty Q'(r)z(r)r^{N-1}dr.
$$

This is a one-dimensional weighted spectral problem despite the N-dimensional PDE.Importantly, verifying this l=1 inverse alone does not establish all nondegeneracy hypotheses in Section 2; other admissible angular modes of L_+ and L_- must not contain zero eigenvalues.

A separate potential mechanism is a bright vortex Q(r,theta)=exp(i m theta)R(r) in N=2. Translation and velocity perturbations couple angular sectors m-1 and m+1. One must use the full real-linear Hessian; the scalar real-profile L_- formula is inapplicable. No negative-energy vortex construction is claimed here.

## 5. Why naive transverse localization of a one-dimensional wave is not a proof

A one-dimensional wave constant in the transverse coordinates is not in L^2(R^N). Multiplying it by a wide cutoff creates both nonlinearity mismatch and transverse terms in

$$
 \Delta^2(f(x_1)g(x'))=f''''g+2f''\Delta'g+f\Delta'^2g.
$$

The product nonlinearity is |f|^(8/N)f times |g|^(8/N)g, so even the one-dimensional nonlinear exponent differs from the N=1 mass-critical exponent. There is no small-residual H^2 argument obtained merely by making g broad: the cutoff region can carry a macroscopic residual and translation/phase/continuous-spectrum obstructions must be solved. A Lyapunov-Schmidt or spatial-dynamics construction would be needed, including transverse localization. None is supplied by the known one-dimensional multipulse theorem below.

## 6. Focused primary literature checks

1. Ross Parker and Alejandro Aceves, *Multi-pulse solitary waves in a fourth-order nonlinear Schrödinger equation*, Physica D 422 (2021), arXiv:2009.01647v3.
   - https://arxiv.org/pdf/2009.01647 ; web ref .
   - Constructs one-dimensional cubic standing multipulses using oscillatory tails and spatial dynamics. It does not construct our N>=2 mass-critical traveling waves.
   - The paper explicitly introduces L_- inverse applied to the translation mode. Hypothesis 3 assumes L_- nonnegative for the primary pulse; Hypothesis 4 assumes positive inverse pairing. Thus its argument is not a general positivity theorem for excited branches or all exponents.
   - Widely separated finite multipulses plausibly have a leading sum of positive single-pulse contributions to I, with small interaction corrections; turning that heuristic into a bound requires controlling small phase eigenvalues. This explains why simply increasing separations need not improve the negative-I search.

2. Decker, Demirkaya, Alexander, Kevrekidis, *Bright Fractional Single and Multi-Solitons in a Prototypical Nonlinear Schrödinger Paradigm*, arXiv:2602.17175 (2026).
   - https://arxiv.org/abs/2602.17175 ; web ref .
   - Examines one-dimensional fractional-dispersion pulse pairs and their spectral stability, including the biharmonic endpoint. It does not establish a higher-dimensional mass-critical negative-energy traveling wave.

3. *Nodal Multi-peak Standing Waves of Fourth-Order Schrödinger Equations with Mixed Dispersion*, J. Geometric Analysis (2021).
   - https://link.springer.com/article/10.1007/s12220-021-00795-x ; refs , .
   - Its Theorem 1.1 assumes N>=5, a spatially varying potential, and a sufficiently strong second-order dispersion coefficient. Hence it cannot be imported as the required homogeneous multipulse existence theorem.

The new 2026 Helmholtz traveling-wave paper checked in the first note is likewise not an H^2 counterexample source: its profiles need not be L^2. No primary source examined provides the missing sign theorem or an exact N>=2 counterexample.

## 7. Most concrete rigorous next step

Find a stationary N=2 excited profile with I bounded strictly below zero, then validate the exact profile and the two parity-restricted invertibilities. Section 2 would convert those finite proof obligations into an exact global negative-energy traveling wave. If I is only numerically close to zero, resolve domain truncation and near-zero spectral modes before interpreting the sign. Positive values for the tested profiles exclude those local branches only; they do not settle the full negative-energy blowup problem.
