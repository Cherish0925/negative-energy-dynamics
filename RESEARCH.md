# Research narrative

## 1. The organizing question

Critical focusing couples two competing effects: dispersion penalizes concentration, while nonlinear attraction rewards it. At the critical exponent they have the same scaling. The sharp inequality therefore determines a mass scale, but it does not, by itself, determine every trajectory above that scale. Momentum, phase, and internal occupations decide which mechanisms are available.

This distinction connects the three developments in the repository. Negative-energy excited waves show that coherent motion can persist globally. Optimizer coercivity excludes that particular mechanism near the critical mass. For common-density systems, a conserved occupation spectrum changes the threshold and identifies the component that can concentrate. The remaining collective-binding question is a sharp orthogonal-function inequality.

## 2. Equations and conventions

For a positive homogeneous symbol $a(\xi)$ of order $m$, use

$$
i\partial_tu=a(D)u-|u|^{2m/d}u,
\quad M=\|u\|_2^2,
\quad A=\langle u,a(D)u\rangle,
\quad E=\tfrac12A-\tfrac1p\|u\|_p^p,
\quad p=2+2m/d.
$$

The sharp scalar inequality defines $M_c$ by

$$
\|u\|_p^p\le\frac p2\left(\frac{M(u)}{M_c}\right)^{m/d}A(u).
$$

The biharmonic equation has $a(\xi)=|\xi|^4$, so the mass-critical power is cubic in four dimensions and $|u|^{8/3}u$ in three. A traveling profile solves

$$
a(D)U+\omega U+i v\cdot\nabla U-|U|^{2m/d}U=0,
\qquad u(t,x)=e^{i\omega t}U(x-vt).
$$

The common-density second-order systems instead take the form

$$
i\partial_tu_j+\Delta u_j+\rho^{2/d}u_j=0,
\qquad \rho=\sum_j|u_j|^2.
$$

Their internal Gram operator $\Gamma=\int UU^*$ is conserved. Write its ordered eigenvalues as $m_j=Mp_j$, with $\sum p_j=1$. These are spatial inner-product occupations, not merely polarization labels. In two dimensions the nonlinearity is cubic; in one dimension it is quintic.

## 3. Excited-state response creates global negative energy

An excited standing wave need not have the phase positivity of a sharp optimizer. For the certified four-dimensional seed,

$$
I=\langle\partial_1Q,L_-^{-1}\partial_1Q\rangle
\le-\frac{24609689664617}{140499437500}<-175.
$$

Continuation gives

$$
P_1(U_v)=2Iv+O(v^3),\qquad E(U_v)=\frac I4v^2+O(v^4)<0.
$$

Translation and phase rotation preserve its Sobolev norm for all real times. The three-dimensional construction supplies a separate certified seed and explicit small-speed range. This gives a negative answer to an unconditional extension of negative-energy blowup/growup to all nonradial data; it leaves the published radial results intact.

The negative response belongs to an excited state. Positivity of the ground-state phase operator, used later, concerns a different variational class and is fully compatible with this construction.

## 4. Zero total momentum and the cost of radiation

A pair of opposite-speed waves cancels momentum while retaining negative energy. The four-dimensional nonlinear construction produces an exact forward-global, uniformly H¹⁰-bounded trajectory, with finite variance at each finite time. Separation makes the variance grow without requiring growth of the Sobolev norm.

A second construction uses one moving core and free radiation. For a prescribed core with speed $v>0$ and momentum $-q e_1$, the exact infimum radiation mass compatible with zero total momentum and negative total energy is

$$
\mu_{\rm crit}=q(4/v)^{1/3}.
$$

Every strictly larger radiation mass is realizable in the specified asymptotic class. This improves the small-speed limiting total mass from two excited cores to one excited core. It does not move that limit down to the scalar ground-state mass.

For general homogeneous dispersion, the corresponding free-radiation energy infimum at mass $\mu$ and momentum $\pi$ is $a^{**}(\pi)/(2\mu^{m-1})$, where $a^{**}$ is the convex envelope. The nonlinear core-plus-radiation construction is a further step beyond this variational formula.

## 5. Phase coercivity creates a strict profile gap

Near the sharp scalar mass, negative-energy normalized profiles must approach the optimizer set. Constant-phase rigidity and positivity of $L_-$ transverse to the phase direction contradict the negative phase contribution required by a traveling profile. This gives

$$
E(U)<0\quad\Longrightarrow\quad M(U)\ge M_c+\delta,
$$

uniformly in frequency and velocity, for the specified real-even positive elliptic homogeneous symbols. No optimizer uniqueness, radial symmetry, spatial variance, or real-sector ground-state nondegeneracy is used.

The quantitative extension, at $A(U)=1$, is

$$
\inf_{\omega,v}\|R_{\omega,v}(U)\|_{H^{-m/2}}
\ge c|E(U)|
$$

in the near-critical negative-energy class. The normalization and the residual norm matter. This estimate controls proximity to coherent profiles; it does not exclude every recurrent or deforming bounded orbit.

Dispersion changes must also be stated precisely. A nonnegative perturbation that is arbitrarily small relative to the principal symbol can destroy the profile gap when the dilation condition fails. The same work determines static concentration boundaries and two-threshold geometry for specific interpolating symbols. These variational concentration scales are not temporal blowup rates.

## 6. Instability and transport constrain coherent motion

The excited four-dimensional seed has Morse counts $n_-(L_+)=31$ and $n_-(L_-)=5$. The certified radial quartet completes the sufficiently small nonzero-speed stable and unstable dimensions at 31. Strong-stable families give nonstationary global trajectories converging to the wave; they do not give an open stable basin.

For slow ground waves of order $m>2$, the leading constrained curvature is $(2-m)v^TTv<0$. The variational conclusion is broader than the spectral and nonlinear instability theorem, whose real-sector and spectral assumptions remain explicit.

Localized transport provides a separate statement about general evolution. Negative-energy, zero-momentum trajectories with bounded kinetic averages must separate mass; confinement forces kinetic amplification. For $E=-e$, near-critical excess $d_*=(M/M_c)^{\kappa-1}-1$, and order $m>2$, the general average estimate has exponent

$$
\liminf_{T\to\infty}\frac1T\int_0^T A(t)\,dt
\ge ce\,d_*^{-\alpha},\qquad
\alpha=1+\frac{m}{2(m-1)}.
$$

The quartic refinements require additional nondegeneracy. An averaged lower bound still permits a sufficiently large bounded kinetic level.

## 7. Conserved occupations determine a different threshold

For every finite occupation vector, the two-dimensional strict-side threshold is $M_*(p)=2/C(p)=1/(2L(p))$, where $C(p)$ is the weighted orthonormal kinetic constant and $L(p)$ its spectral dual. Majorization gives $p\succ q\Rightarrow M_*(p)\le M_*(q)$: distributing occupation more evenly cannot lower this threshold. The one-dimensional quintic value for every finite spectrum follows from the external sharp inequality.

For the two-dimensional cubic common-density system, there is a rank-independent $\varepsilon_0>0$ such that

$$
p_2/p_1\le\varepsilon_0
\quad\Longrightarrow\quad M_*(p)=M_c/p_1.
$$

Below this threshold every H¹ solution with that spectrum is global and bounded in the energy norm. At the threshold there are both blowup and forward-global examples with the exact spectrum. Above it there are smooth compactly supported negative-energy blowup data. The assertion concerns the threshold for uniform protection against collapse; it does not prescribe the outcome of every superthreshold datum.

The decisive improvement over a near-pure-state statement is that the total secondary occupation need not be small. Only each secondary occupation relative to the largest one is bounded. A global deficit estimate controls the entire secondary kinetic energy at criticality:

$$
E(U)\ge\tfrac12E_1(u_1)+\tfrac1{64}A_{\rm sec}.
$$

The same variational estimate is dual to a weighted spectral inequality controlling all excited bound states by the deficit in the optimal one-state estimate. The full two-dimensional Lieb–Thirring constant would require coefficient one, which is not obtained here.

## 8. A coherent critical core and its background

In the stated occupation regimes, finite-time critical concentration has one principal coherent core and a unique regular background carrying the residual Gram spectrum. The principal density acquires finite variance automatically. Its center and momentum have an explicit first-order relation, while the residual occupations remain in the background.

For forward-global, finite-total-variance critical solutions, the corresponding conformal argument gives a dichotomy between full scattering and a scaled moving ground core plus free radiation, with strong H¹ error tending to zero. In general the core width need not yet be known to converge to a positive number.

The one-dimensional quintic extension uses the sharp one-dimensional Lieb–Thirring inequality of Read–Schulz as an external input. Its additional positive-deficit argument applies to every strictly simple maximal occupation, $p_2<p_1$. It is not a new proof of their inequality. A Hilbert-valued extension uses conserved trace tails to pass from finite components to countably many modes.

## 9. Collapse scale is selected by the first nonzero interaction

For a scalar mass-critical NLS with a real time-dependent potential, bounded scalar energy and

$$
\int_0^{h_0}h\|\nabla_x^2V(T-h)\|_\infty\,dh<\infty
$$

give a conditional scale theorem for finite-time blowup at mass $M_c$:

$$
\lambda_{\rm kin}(t)/(T-t)\longrightarrow\mu_*>0.
$$

This is a conclusion about the actual gradient-normalized scale. It uses the written regularity assumptions for the transport and virial identities. The earlier power-law curvature condition is a sufficient special case.

In the one-dimensional quintic vector system, a different matched family has

$$
E(U_{\lambda,k})=E(W)+\frac{V_Q}{8}k^2-cA\lambda+o(\lambda),
\qquad c=\pi/4+\log2-1>0.
$$

Exact Gram preservation and the negative linear scale term are established for the matched initial-data family. They motivate $\lambda\sim(2cA/V_Q)(T-t)^2$; the singular solution with this law has not been constructed. The effective potential lies at the borderline of the preceding curvature condition, so the two statements do not conflict.

## 10. Orthogonality and collective binding

For finite orthonormal families on $\mathbb R^2$, the remaining sharp question is

$$
\int\left(\sum_j|\phi_j|^2\right)^2
\stackrel{?}{\le}\frac2{M_c}\sum_j\|\nabla\phi_j\|_2^2.
$$

Its dual is $L_{1,2}=1/(2M_c)$. This is exactly where an unrestricted occupation threshold would require information beyond the small-secondary-occupation theorem.

The completed restricted results include positive separated-core deficits, transverse coercivity on a specified modulation slice, all-scale negativity of the Townes two-well scattering coefficient, and control of the full negative spectrum for finite separated well families. Fixed-rank or fixed-scale qualifiers are part of these results.

The later calculations derive arbitrary-rank matrix remainder estimates, transfer them to physical density control, and compare restricted variations with the full unoccupied spectral response. They also show why proposed universal density-gradient corrections and certain merger or diffusion routes cannot establish the target. Hermite and periodic-potential searches retain full data and resolution comparisons; neither produced a certified violation or a proof of the unrestricted inequality.

## 11. Optical interpretation

In a two-dimensional common-density optical model with diffraction coefficient $D$ and cubic coupling $g$, the normalized occupation threshold corresponds to physical power $P_*(p)=(D/g)M_*(p)$. Thus the spectral question determines whether two equally occupied orthogonal modes double the smallest power admitting collapse. This interpretation requires the specified common coupling; the general effect of coherence on collapse has established optical antecedents.

The mixed model

$$
i u_z=(-\partial_\tau^2+\Delta_y^2-\nabla_y\cdot K\nabla_y)u-|u|^2u,
\qquad y\in\mathbb R^2,\quad K\succeq0,
$$

has one quadratic and two quartic directions. The partial Galilean transform removes the quadratic-direction momentum and gives intrinsic energy $E_{\rm int}=E-P_\tau^2/(2M)$. The proof yields a uniform negative-intrinsic-energy traveling-wave mass gap and its residual version. A negative-energy traveling wave in this specific model has not yet been constructed.

Continuation runs approaching the mixed model are retained, including the refinement that reversed a coarse-grid negative response. They are numerical exploration, not an experimental realization. The initial linear-optical Bell-measurement reproduction is also preserved as a separate preliminary calculation and is not counted as a new focusing result.

## 12. What makes this one research development

The common language is critical scaling together with the quantities that survive evolution. The central proof mechanisms are optimizer compactness, phase coercivity, spectral response, exact momentum or Gram constraints, and localized transport. They connect constructions to exclusions and static variational structure to actual dynamics. The equations and hypotheses determine which connection is valid; sharing a technique does not turn distinct model conclusions into a universal theorem.
