# Classification literature and a spectral route to transverse radiation

Date: 2026-10-11. Scope: primary-source comparison for the project's two-dimensional common-density cubic fixed-Gram threshold, and a precise consequence of its homogeneous transverse coercivity. This note does not establish historical priority or a nonlinear rough-background classification.

## 1. What the closest classification actually proves

**Pierre Raphaël and Jérémie Szeftel**, *Existence and uniqueness of minimal blow up solutions to an inhomogeneous mass critical NLS*, JAMS 24 (2011), 471–546. Full primary PDF checked: <https://arxiv.org/pdf/1001.1627> (Theorem 1.3 and discussion, PDF pp. 4–6).

Their equation is `i u_t + Δu + k(x)|u|²u = 0` in two dimensions. The standing assumptions are `k in C5 ∩ W1,infinity`, `0<k1≤k≤1`, with the maximum attained. At a nondegenerate maximum `k(x0)=1`, `Hess k(x0)<0`, Theorem 1.3 classifies every critical-mass finite-time H1 blowup at x0: for each admissible energy there is a unique solution up to constant phase. The allowed energy has an explicit Hessian correction. Their physical H1 asymptotic profile has the pseudoconformal rate. The proof directly derives modulation dynamics and improves the remainder, without assuming the pseudoconformal symmetry survives.

**Comparison:** this is a genuine all-solution classification, not just a construction. It shows that rate, phase, and uniqueness in an inhomogeneous equation are established objectives and techniques. It is not a theorem for a real time-dependent linear potential `S(t,x)u`, and its conserved scalar energy and fixed spatial Taylor expansion do not apply to the project's self-consistent H1 density. In particular, R18 does not solve their stated uniqueness conjecture for degenerate nonlinear coefficients.

## 2. Bourgain–Wang uniqueness has strong asymptotic hypotheses

**Michael Röckner, Yiming Su, Deng Zhang**, *Multi-bubble Bourgain-Wang solutions to nonlinear Schrödinger equation*, arXiv:2110.04107; journal version Transactions AMS 377 (2024). Primary PDF checked: <https://arxiv.org/pdf/2110.04107>; journal metadata: <https://www.ams.org/journals/tran/2024-377-01/S0002-9947-2023-09025-0/>.

Their scalar equation in dimensions one and two includes lower-order coefficients

`a1=2i sum_l ∇φ_l(x) h_l(t)`,

`a0=−|sum_l ∇φ_l(x)h_l(t)|²+i sum_l Δφ_l(x)h_l(t)`.

Here φ_l are smooth bounded spatial functions, h_l continuous. Spatial coefficient flatness at each blowup point is imposed. The terminal regular residue is small, very smooth, weighted, and flat to high order. The paper constructs multiple pseudoconformal bubbles plus a regular residue and proves conditional uniqueness when the prescribed asymptotic H1 error is `O((T−t)^(4+ζ))`, ζ>0. Its pseudoconformal corollary constructs non-pure multi-solitons.

**Comparison:** “rough” here concerns time dependence obtained from stochastic/rough-path transformations; it is not arbitrary H1 spatial roughness in S. Our O(h) or O(h²) L2 primary errors do not meet their full-solution H1 uniqueness hypothesis. The paper is a close predecessor for singular-core-plus-regular-radiation constructions; it does not automatically classify all fixed-Gram threshold trajectories.

## 3. Low-rate uniqueness for pure bubbles does not include arbitrary radiation

**Daomin Cao, Yiming Su, Deng Zhang**, *On uniqueness of multi-bubble blow-up solutions and multi-solitons to L2-critical nonlinear Schrödinger equations*, arXiv:2105.14554; ARMA (2023). Full primary PDF checked: <https://arxiv.org/pdf/2105.14554>, introduction and theorem setup.

For canonical scalar NLS in dimensions one and two, their uniqueness class contains solutions converging to a prescribed sum of pure pseudoconformal bubbles with physical H1 error `O(h^ζ)`, any positive ζ, under their frequency-closeness or spatial-separation alternatives. A weaker scaled convergence condition is also treated with an extra averaged condition. Modified localized energy/virial functionals upgrade polynomial convergence to exponential convergence. The pure multi-soliton result assumes H1 convergence faster than t^-2, with a weaker-rate version in Σ.

**Comparison:** these are prescribed pure-bubble/pure-soliton classes; their terminal residue is zero. The project's critical principal mode is pure at its own mass, but the vector has nonzero transverse mass which continually feeds a real potential. Applying their bootstrap requires deriving and controlling these extra forcing terms. It cannot be justified by subtracting the background informally.

## 4. Moving-potential technology is relevant, but its stated theorem does not cover unlimited collapse

**Marius Beceanu and Avy Soffer**, *The Schrödinger Equation with a Potential in Rough Motion*, CPDE 37 (2012). Primary PDF checked: <https://arxiv.org/pdf/1103.0521>, Proposition 1.1, pp. 3–4.

They prove endpoint Strichartz estimates in three dimensions for a translated, boosted, dilated fixed real potential. The static operator must have no embedded eigenvalues or threshold resonances. The dilation parameter β has a half-derivative/continuity or bounded-variation type control; the proposition also requires sufficiently small oscillation on the final time tail. The proof explicitly treats transfer between bound and continuous states through modulation equations.

**Comparison:** in our physical coordinates β=log λ tends to minus infinity, so the small-tail-oscillation hypothesis fails, even if λ_t is bounded. In core time `dτ/dt=λ^-2`, R18 gives `|d(log λ)/dτ|=|λλ_t|=O(λ)→0`, but small instantaneous speed does not imply finite cumulative motion. The theorem therefore supplies an approach, not a directly applicable estimate.

## 5. A concrete spectral consequence of the project's existing gap

Assume the R16 homogeneous estimate for the two-dimensional Townes potential:

    H = −Δ−Q²,   HQ=−Q,
    h(f)=<f,Hf> ≥ κ ||∇f||²,  whenever <f,Q>=0,
    κ>0.

This already implies that Q spans the negative spectral subspace: any second negative eigenfunction can be chosen orthogonal to Q and violates the displayed inequality. The following threshold consequence needs no new numerical computation.

**Lemma.** A bounded distributional solution ψ of `Hψ=0` on R² is identically zero.

**Proof.** Smooth bounded potential and elliptic regularity make ψ locally H2, with uniform local regularity because ψ is bounded. Testing against exponentially decaying Q by compact cutoff approximation gives

    0=<Hψ,Q>=<ψ,HQ>=−<ψ,Q>.

Choose logarithmic cutoffs χ_R equal to one on B_R and zero outside B_(R²), with `||∇χ_R||²≤C/log R`. The weak equation and the IMS identity give

    h(χ_Rψ)=integral |∇χ_R|² |ψ|² ≤ C ||ψ||∞²/log R.

Put `a_R=<χ_Rψ,Q>/Mc` and `g_R=χ_Rψ−a_R Q`. Exact orthogonality and the exponential tail of Q imply `a_R→0` exponentially, while `HQ=−Q` yields

    h(g_R)=h(χ_Rψ)+Mc |a_R|².

Coercivity therefore forces `||∇g_R||²→0`. On each fixed ball g_R tends locally in H1 to ψ, so ∇ψ=0. A constant solution of `−Δψ−Q²ψ=0` must vanish. This proves the lemma.

For exponentially decaying real potentials in two dimensions, all threshold resonance/eigenfunction obstructions have bounded distributional representatives. Thus zero is a regular spectral point here. This last identification is standard threshold spectral theory, not a claim of a new definition.

**Wilhelm Schlag**, *Dispersive estimates for Schrödinger operators in dimension two*, CMP 257 (2005), 87–117. Full primary Theorem 1 checked: <https://arxiv.org/pdf/math/0405437>. For real `|V(x)|≤C(1+|x|)^(-β)`, β>3, and regular zero, it proves

    ||exp(−itH) P_ac(H)||_(L1→Linfinity) ≤ C |t|^-1.

The potential `V=−Q²` meets the decay assumption. Its positive spectrum is absolutely continuous and Q is its sole negative mode, so `P_ac=I−|Q><Q|/Mc`. Combining this classical theorem with the lemma gives the stated dispersive estimate for the exact transverse Townes operator. This is a deduction from the existing project gap and an established theorem, not a new general dispersive result.

## 6. Static radiation cannot remain locally trapped

A further elementary consequence is useful for the nonlinear target. For every `f in H1`, `f⊥Q`, and every fixed R,

    ||exp(−itH) f||_(H1(B_R)) → 0,  |t|→infinity.

Indeed, first take `f=P_ac g` with smooth compactly supported g. Then f is in L1∩H2, and Schlag's estimate gives local L2 decay; conservation of the H graph norm gives a uniform H2 bound. Local integration by parts/interpolation implies local gradient decay. Approximate an arbitrary H1 vector in Q⊥ by such data. The propagator is uniformly H1 bounded (by its quadratic form plus mass), so approximation transfers the limit. No uniform decay rate for all H1 data is asserted.

For a countable family with finite summed H1 norm, the same local squared-norm convergence follows by finite-mode approximation and the uniform H1 propagator bound.

This closes the *autonomous linear* radiation statement. It does not yet establish local decay for the actual shrinking, translating, coupled core. That problem has nonintegrable cumulative dilation, perturbations of the exact projection onto Q, and nonlinear secondary interactions.

## 7. Why a static orthogonality estimate alone cannot finish the dynamics

The nonconcentration of secondary L2 mass is not equivalent to nonconcentration of its energy. For any nonzero smooth compactly supported f with `<f,Q>=0`, the family

    z_λ(x)=f(x/λ),  d=2,

has `||z_λ||²=λ²||f||²→0` and bounded nonzero gradient norm, while

    integral [λ^-2 Q²(x/λ)] |z_λ(x)|² dx
       = integral Q²(y)|f(y)|²dy >0.

It is exactly orthogonal to the pure principal profile `λ^-1 Q(x/λ)`. This is an instantaneous function family, not an actual vector solution. It shows why strong L2 terminal convergence plus uniform H1 and Gram orthogonality do not by themselves make the core–secondary interaction vanish. The missing ingredient must use evolution.

A promising precise next target is a continuous-spectrum local-energy estimate uniform along the core-time path. R18's bounded physical modulation speed makes the well adiabatically slow in core time; the new static spectral consequence supplies the absence of hidden bound or zero-threshold channels. One still needs an estimate that survives indefinitely accumulated dilation and controls the nonlinear feedback at the energy level. Neither the checked classification papers nor the checked moving-potential theorem supplies this conclusion under the current H1 hypotheses.

## 8. Scope of the comparison

No checked primary theorem duplicates the full fixed-Gram hypothesis/conclusion package or settles the original H1-background width classification. This limited search does not prove novelty. The precise predecessors above should replace any claim that pseudoconformal-rate classification, radiation decomposition, or the use of modulation around Q began in this project. The newly written static spectral lemma and its consequences are complete conditional deductions from the R16 coercivity input; they do not resolve the full nonlinear endpoint.
