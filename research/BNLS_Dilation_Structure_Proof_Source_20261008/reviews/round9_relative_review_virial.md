# Independent review of round9_relative_dynamics.md

Reviewer: virial_absorption agent. Date: 2026-10-08.

Reviewed the full note and independently checked the decisive arguments. No substantive mathematical gap was found under its stated hypotheses.

1. **Uniform optimizer estimates.** The normalized real optimizer set is compact modulo translation. Uniform phase coercivity follows from form continuity and removal of the small projection onto a limiting optimizer. The gradient-direction bound follows from the fact that a nonzero L² Fourier transform cannot be supported on a hyperplane. The frequency/velocity map has uniform injectivity because real and imaginary functions are orthogonal in the real-even dual multiplier norm. Differentiation H^s→H^(s−1)→H^(−s) is bounded precisely because m=2s>1.

2. **Arbitrary parameter and residual control.** The perturbation of the parameter map costs only C||U−Q||X(|ω|+|v|), which can be absorbed uniformly. Subtracting the optimizer equation correctly gives |ω−ω*|+|v|≤C[ρ+ε(1+ρ)]. In the small-residual case, this is sufficient to transfer phase coercivity. The identity v·P/2=〈b,L_Ub〉−〈Im F,b〉 and the lower bound on ||v·∇Q||dual give v·P≥c|v|²−Cρ². In the large-residual case, the parameter bound and bounded normalized momentum absorb both the quadratic velocity term and the linear momentum pairing into Cρ². Thus the statement really does allow arbitrary ω and v.

3. **Critical scaling.** With λ=A(U)^(−1/m), the residual satisfies Fλ(x)=λ^(N/2+m)F(λx). Therefore

   ||Fλ||X*² = λ^(2m) ∫ |Fhat(ξ)|²/[1+λ^m a(ξ)] dξ
                = A(U)^(−1) ∫ |Fhat(ξ)|²/[A(U)+a(ξ)] dξ.

   Multiplying the normalized inequality by A(U) gives exactly the velocity factor A(U)^(2/m−1). The sign and constants in the dilation-defect consequence are consistent.

4. **Effective inertia.** The response formula follows by solving the imaginary equation on Q⊥ and using ||b||X≤C(|v|+ρ). A useful explicit sentence is that the L² projection onto Q⊥ is uniformly bounded on X (and its dual), so the coercive form inverse can be estimated in the full dual norm restricted to the annihilator of Q. This is implicit in the note, not a defect in the proof.

5. **Periodic cutoff identity.** With J_R=Im∫Vbar L_RV and iV_t=H(V), skew-adjointness of L_R gives J_R'=2Re〈H(V),L_RV〉. Consequently its limit is 2mE−v·P, with the stated sign. The assumed Cper H^(m+1)∩C1per H^s regularity makes J_R a differentiable quadratic form; the round-8 commutator estimates justify dominated convergence over one period. Periodicity then implies v·P=2mE. Frequency adjustment ω→ω+ν changes the residual to i(V_t−iνV), giving the claimed phase-independent shape-speed lower bound.

6. **Scope.** The result is an approximate-profile residual certificate and a restriction on sufficiently regular relative-periodic solutions. It neither excludes all breathers nor proves the unrestricted bounded-global dynamical mass gap. It is consistent with the independent static interaction-virial obstruction: for those constructed packets, the profile residual may be much larger than the square root of the very small negative energy.
