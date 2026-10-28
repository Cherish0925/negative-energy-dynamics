# gradient-localization rigidity and the unresolved threshold limit

## 1. Actual conclusion

For the pure mass-critical BNLS
$$
 i u_t=\Delta^2u-|u|^{8/N}u,\qquad N\ge1,
$$
a forward-global strong H² solution with negative conserved energy, zero conserved momentum, and uniformly bounded H² norm cannot have its **gradient** uniformly localized modulo translations. This replaces mass localization by a weaker condition: arbitrary noncompact L² mass is allowed, provided its gradient vanishes in the tail. A Cesàro version also holds if a bounded-speed center is supplied.

This does not prove that all near-critical negative-energy zero-momentum solutions blow up or grow up. Persistent exterior gradient energy is still allowed. The result follows from the established localized virial identity plus a new choice of localization assumptions; its novelty relative to the literature has not been established.

## 2. Definitions

Let
$$
 p=2+8/N,\quad M=\|u\|_2^2,\quad P=\Im\int\bar u\nabla u,
 \quad E=\frac12\|\Delta u\|_2^2-\frac1p\|u\|_p^p.
$$
Assume a standard strong solution with conservation laws and
$$
 \sup_{t\ge0}\|u(t)\|_{H^2}\le B<\infty.
$$
For a center c define
$$
 D_R(t)=\int_{|x-c(t)|>R}|\nabla u(t,x)|^2\,dx.
$$
No finite variance or first spatial moment is used.

## 3. Theorem: arbitrary centers and uniform gradient localization

**Theorem.** Suppose E<0 and there is a map c:[0,∞)→R^N, with no assumed regularity, such that
$$
 \lim_{R\to\infty}\sup_{t\ge0}D_R(t)=0.
$$
Then c differs by a uniformly bounded amount from a Lipschitz map, and
$$
 \limsup_{T\to\infty}\frac{P\cdot[c(T)-c(0)]}{T}\le 8E.
$$
In particular P cannot vanish. There is no mass restriction, radial hypothesis, or curvature-tail localization hypothesis.

### Proof, step A: gradient localization forces nonlinear localization

For f∈H² the following homogeneous interpolation inequalities hold:
$$
 \|f\|_p^p\le
 \begin{cases}
 C_N\|f\|_2^{2(4-N)/N}\|\nabla f\|_2^4,&N\le4,\\
 C_N\|\nabla f\|_2^{16/N}\|\Delta f\|_2^{2-8/N},&N>4.
 \end{cases}
$$
Indeed Sobolev at derivative order σ=2N/(N+4) maps homogeneous H^σ into L^p. Interpolate σ between 0 and 1 when N≤4, and between 1 and 2 when N>4. The endpoint N=4 is the usual homogeneous H¹→L⁴ embedding.

Apply this to f=η((x-c(t))/R)u(t), where η=0 in the unit ball and η=1 outside the ball of radius 2. Uniformly in time,
$$
 \|f\|_2\le\sqrt M,\quad
 \|\nabla f\|_2\le D_R(t)^{1/2}+C\sqrt M/R,
 \quad\|\Delta f\|_2\le C_B.
$$
Writing q_N=min(4,16/N), one obtains
$$
 \int_{|x-c(t)|>2R}|u|^p
 \le C_{N,M,B}\bigl(D_R(t)^{1/2}+R^{-1}\bigr)^{q_N}.
$$
Thus the nonlinear density is uniformly localized whenever the gradient is.

### Proof, step B: regularize the center without assuming its velocity

Since E<0,
$$
 \|u(t)\|_p^p=\frac p2\|\Delta u(t)\|_2^2+p|E|\ge p|E|.
$$
The global versions of the inequalities in step A, together with B<∞, imply
$$
 \inf_{t\ge0}\|\nabla u(t)\|_2\ge g_*>0.
$$
The equation and H²→L^p give a uniform bound on u_t in H^{-2}. Therefore
$$
 \|u(t)-u(s)\|_{H^{-2}}\le C_B|t-s|,
 \qquad\|u(t)-u(s)\|_{H^1}\le C_B|t-s|^{1/4},
$$
where the second estimate interpolates H^{-2} and the uniform H² bound. Choose τ>0 so that the H¹ difference is at most g_*/4 whenever |t−s|≤τ. Choose R₀ with
$$
 \sup_t D_{R_0}(t)\le g_*^2/16.
$$
If |c(t)−c(s)|>2R₀ for |t−s|≤τ, the balls around the two centers are disjoint. On B(c(s),R₀), the gradient of u(s) has norm at least sqrt(15)g_*/4, while the gradient of u(t) has norm at most g_*/4. This contradicts the H¹ time-continuity estimate. Hence
$$
 |c(t)-c(s)|\le2R_0\quad (|t-s|\le\tau).
$$
Piecewise linear interpolation through c(nτ) gives a Lipschitz center a with
$$
 \|a'\|_\infty\le2R_0/\tau,\qquad
 \sup_{t\ge0}|a(t)-c(t)|\le4R_0.
$$
Uniform gradient and nonlinear localization persist about a.

### Proof, step C: moving-center localized virial

Take the same smooth radial cutoff φ_R used in rounds 8 and 9: φ_R=|x|²/2 for |x|≤4R, constant for |x|≥8R, D²φ_R≤I, with the standard scaled derivative bounds. Set
$$
 J_R(t)=2\Im\int\nabla\phi_R(x-a(t))\cdot\bar u\nabla u.
$$
Then |J_R(t)|≤C_BR. The fixed-center identity and the favorable top-order Hessian bound give
$$
 J_R'\le16E-2a'(t)\cdot P
 +C_BR^{-2}+C\int_{|x-a(t)|>4R}|u|^p
 +C|a'(t)|\sqrt M
    \left(\int_{|x-a(t)|>4R}|\nabla u|^2\right)^{1/2}.
$$
The last term is exactly the error from replacing D²φ_R by I in
$-2a'\cdot\int D²φ_R\,\Im(\bar u\nabla u)$.
All displayed errors tend uniformly to zero as R→∞. The differentiated identity holds in integrated energy-space form, as in round 8; a Lipschitz a is sufficient, or follows by smoothing a and passing to the integrated limit.

Integrate to T, divide by T, let T→∞ at fixed R, and then R→∞:
$$
 \limsup_{T\to\infty}\frac{P\cdot[a(T)-a(0)]}{T}\le8E.
$$
The bounded difference a−c gives the same statement for c. If P=0, this implies 0≤8E<0, a contradiction. QED.

## 4. Cesàro relaxation and a quantitative exterior-gradient requirement

**Theorem.** Let u be a forward-global uniformly H²-bounded strong solution with E<0. Suppose a is Lipschitz and
$$
 \lim_{R\to\infty}\limsup_{T\to\infty}
 \frac1T\int_0^T\int_{|x-a(t)|>R}|\nabla u|^2\,dx\,dt=0.
$$
Then the same averaged drift inequality holds:
$$
 \limsup_{T\to\infty}\frac{P\cdot[a(T)-a(0)]}{T}\le8E.
$$
In particular such averaged localization is impossible when P=0.

**Proof.** Put κ=min(1/2,8/N), so 0<κ≤1/2. Boundedness of D_R and step A imply that the total moving-virial error is bounded by
$$
 C_{N,M,B,\|a'\|_\infty}\bigl(R^{-\min(2,q_N)}+D_R(t)^\kappa\bigr).
$$
Jensen's inequality bounds its time average by a vanishing R-term plus C times the κ-th power of the time average of D_R. The integrated argument in step C now applies. QED.

More quantitatively, when P=0, choose R_* so that the R-error is at most 4|E|. For every R≥R_* and every interval [S,S+T],
$$
 C\frac1T\int_S^{S+T}D_R(t)^\kappa\,dt
 \ge 12|E|-C_B R/T.
$$
Consequently
$$
 \inf_{R\ge R_*}\liminf_{T\to\infty}\inf_{S\ge0}
 \frac1T\int_S^{S+T}D_R(t)\,dt
 \ge (12|E|/C)^{1/\kappa}>0,
$$
where the harmless numerical constant can be reduced if desired. The constants depend on the model, mass, H² bound, energy, and the chosen center speed bound. This says that any hypothetical global bounded zero-momentum negative-energy state must sustain nonzero averaged exterior gradient energy outside every fixed radius about every bounded-speed center. It is not merely allowed to carry a diffuse zero-gradient mass tail.

## 5. Why this still does not close the near-critical problem

Let δ_M=(M/M_c)^{4/N}−1. The sharp GN inequality gives
$$
 -\frac{\delta_M}{2}A(u)\le E(u)<0,
 \qquad A(u)=\|\Delta u\|_2^2.
$$
For fixed negative E this forces A≥2|E|/δ_M. Normalizing A=1 along a hypothetical sequence M↓M_c forces E→0; normalized data converge to an allowed zero-energy optimizer. Normalizing E=−1 instead makes the kinetic norm diverge. Neither normalization preserves both negative energy and a compact kinetic scale at the limiting mass.

Even with a uniform kinetic upper bound on one trajectory, near-optimizer compactness gives a small but nonzero tail bound. The ratio |E|/A may be arbitrarily smaller than that bound. The exterior-gradient lower bound in section 4 can therefore be compatible with the near-optimizer tail upper bound. No contradiction follows without an additional relation tying the escaping gradient budget to the signed negative energy, or a genuine time-integrated radiation mechanism.

The residual-inertia inequality similarly gives a nonzero lower bound on shape motion, but a Hamiltonian bounded orbit can continue moving forever. A finite total shape-motion budget has not been proved.

Thus the remaining substantive target is: prove that the exterior gradient forced by section 4 cannot be repeatedly replenished in a near-critical zero-momentum negative-energy state, or construct such an orbit. A static virial absorption estimate cannot do this, as round 9's explicit separated-packet construction demonstrates.

## 6. A sharper unconditional alternative: ballistic exterior-gradient escape

The same estimates give a stronger spatial statement than failure of tightness. Assume P=0 and E=−e<0, and fix any Lipschitz center a with speed bound L. Let C₀ be the endpoint constant |J_R|≤C₀R, and let C₁ bound the tail-error coefficient. Choose a small **fixed** speed ν>0 satisfying 2C₀ν≤4e. In the integrated moving-virial estimate take R=νT rather than first fixing R. The cutoff error tends to zero as T→∞, whereas the endpoint contribution is at most 2C₀ν. Therefore
$$
 \liminf_{T\to\infty}\inf_{S\ge0}
 \frac1T\int_S^{S+T}
 \left(\int_{|x-a(t)|>\nu T}|\nabla u(t,x)|^2\,dx\right)^\kappa dt
 \ge\frac{8e}{C_1}>0,
$$
where reducing the harmless numerical coefficient covers all sufficiently large T. Jensen gives
$$
 \liminf_{T\to\infty}\inf_{S\ge0}
 \frac1T\int_S^{S+T}\int_{|x-a(t)|>\nu T}|\nabla u|^2\,dx\,dt
 \ge\left(\frac{8e}{C_1}\right)^{1/\kappa}>0.
$$
Thus a hypothetical global uniformly H²-bounded zero-momentum negative-energy state must exhibit persistent gradient energy at distance comparable to the observation-window length, about every bounded-speed center. This excludes localization inside any sublinearly growing radius, even if uniform localization inside fixed radii fails. It is a quantitative necessary alternative, not a construction of such a global state and not a claim of physical dissipation. The constants depend on the actual H² bound, energy, mass, and center speed; no uniform positive speed is asserted as E→0.
