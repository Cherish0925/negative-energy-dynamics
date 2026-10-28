# Proof details of R18's Hilbert-valued extension

Date: 2026-10-10. The infinite-component passage uses the finite-rank static inequalities and scalar endpoint inputs in [hilbert-extension.md](hilbert-extension.md). 
## 1. Outcome

No failure was found in the infinite-component argument. In particular, the proof does not confuse Hilbert-valued Sobolev boundedness with Rellich compactness and does not assume uniform smallness or conservation of high-index kinetic tails. Its countable-rank conclusions follow from two genuinely different controls: exact trace-class component mass tails, and spatial tightness from the aggregate continuity equation.

Two wording clarifications were sent to the author while the audit was performed:

* The two-dimensional subthreshold range must explicitly retain m_2/m_1<=epsilon_0. If m_1 is changed below Mc, the endpoint-looking condition m_2/Mc<=epsilon_0 alone is not the same condition. The derivation and Section 10 already use the correct ratio.
* A local H1 extension time uniform on an H1 ball should be justified using smallness of the **undifferentiated** critical free norm and boundedness of the derivative norm. Absolute continuity of each individual derivative Strichartz norm is not uniform on an H1 ball. The needed uniform argument is supplied below.

Neither issue changes the mathematical conclusion when stated as above.

## 2. Dimension-independent Strichartz and local H1 theory

For q,r>=2, successive Minkowski inequalities give

    ||(sum_j |f_j|^2)^(1/2)||_(L_t^q L_x^r)
       <= (sum_j ||f_j||_(L_t^q L_x^r)^2)^(1/2).

For q',r'<=2 the corresponding comparison is reversed. The author uses these directions correctly. Applying scalar homogeneous Strichartz coordinatewise, then the first inequality, gives the H-valued homogeneous estimate. For the retarded inhomogeneous operator, apply the same output inequality, the scalar retarded estimate, then the dual reverse inequality. Thus the vector estimate has the scalar constant and is independent of the number of components. Finite-coordinate truncation converges by completeness. This works for the required pairs (4,4) in dimension two and (6,6) in dimension one, with (infinity,2) for energy norms.

The polynomial maps ||z||^2 z and ||z||^4 z on a complex Hilbert space, treated as a real Banach space, have exactly the pointwise and differentiated Lipschitz estimates asserted in the note. Their constants depend on the degree, not on dim H. The Hilbert norm satisfies the diamagnetic inequality, so the scalar H1 Sobolev constants apply.

Here is the requested uniform continuation detail. Let q=r=p+1, in the notation of the Hilbert note. In both models H1(R^d;H) embeds into L^r(R^d;H). Consequently

    ||exp(it Delta)f||_(L_t^q(I;L_x^r(H)))
       <= C |I|^(1/q) ||f||_H1.

The derivative Strichartz norm is bounded by C||f||_H1 and need not be uniformly small. In the derivative nonlinear estimate, its coefficient is the (p-1)st power of the small undifferentiated critical norm. Choosing |I| depending only on an H1 bound makes this coefficient small; the standard contraction/stability estimates then propagate a bounded derivative Strichartz norm. This proves a lifespan uniform on each H1 ball. It justifies the stronger blowup alternative ||U(t)||_H1 tending to infinity at every finite maximal endpoint, rather than only an unbounded limsup.

Projection approximants P_N U_0 converge in H1. Their solutions remain in ran P_N because the nonlinearity is a scalar multiple of U. The vector local stability estimates give convergence on each compact interval in the true lifespan. It is legitimate to pass mass, energy, momentum and Gram conservation along this sequence. These approximant solutions need not equal P_N U(t); the note correctly uses local solution stability rather than asserting that identity.

## 3. Trace conservation and static constants

The rank-one identity in (3.1) gives

    ||Gamma(U)-Gamma(V)||_S1
       <= (||U||_2+||V||_2)||U-V||_2.

This is valid in an arbitrary Hilbert space: the trace norm of |a><b| is ||a||||b||, and the Bochner integral is finite. Thus the fixed Gram operator is conserved in trace norm. Its spectral projections yield the exact tail identity

    ||(I-P_N)U(t)||_2^2=sum_(j>N)m_j,

uniformly in t. The note never makes the analogous unsupported statement for gradient tails.

For static truncations P_N U at a fixed time, both A(P_N U) and the nonlinear density integral increase to their respective finite limits. Therefore their difference E(P_N U) converges as well, even though the energies themselves need not be monotone. Passing the finite-rank inequalities gives exactly the stated a,b remainder constants. They are independent of rank; trace finiteness is still needed to define the H1 state and the nonlinear estimates.

Below threshold, the constants are correct:

    E >= (1/2)(1-m_1/Mc)A,       d=2,
    E >= (1/2)(1-(m_1/Mc)^2)A,   d=1.

The first formula assumes m_2/m_1<=epsilon_0. The second follows from the external one-dimensional all-occupation inequality and does not require a strict leading gap. A strict gap is still used for the one-dimensional endpoint kinetic remainder and subsequent endpoint classification. No finite-rank restriction remains in these coercivity statements.

## 4. Terminal strong convergence and the two tails

In dimension two, the direct Bochner L1 source estimate is valid:

    integral |u_1|^2 ||V|| <= sqrt(Mc) sqrt(integral |u_1|^2||V||^2).

The energy remainder bounds the second factor, and the secondary cubic term is also bounded in L1(H). The Hilbert-valued embedding H^s into Linfinity for s>1 follows directly from Fourier Cauchy--Schwarz. Therefore V_t is bounded in H^-s(H), with a constant independent of rank. Interpolation with the uniform H1 bound gives a joint Cauchy estimate in every H^sigma, sigma<1. There is no hidden infinite-dimensional compact embedding in this argument.

In dimension one, the weak-limit uniqueness argument is valid because the principal field is bounded on compact sets away from x_*. Pairings against scalar compact tests times finitely many component vectors have bounded derivatives and form a dense test class in L2(R;H). Uniform boundedness supplies a unique weak limit.

For strong convergence, both tail estimates are necessary and are supplied:

1. Aggregate secondary transport gives uniform spatial L2 tightness.
2. Trace conservation gives uniform component L2 tail smallness.

After removing both tails, only finitely many scalar components on a bounded spatial interval remain, so ordinary scalar Rellich applies. The two tails upgrade this finite-dimensional compactness to global L2(R;H) compactness. Weak-limit uniqueness then gives convergence of the entire trajectory. Bounded H1 and interpolation yield joint H^sigma convergence. This is the correct repair of the failure of unrestricted Hilbert-valued Rellich compactness.

The Hilbert-valued one-dimensional Sobolev estimate and the fundamental theorem of calculus give the uniform field convergence and the node W(x_*)=0 exactly as stated. The Bochner orthogonality identity controls all secondary coordinates together, using their finite total mass rather than summing uncontrolled coordinatewise constants.

## 5. Aggregate transport and strong weighted convergence

The total secondary current obeys

    |Im<V,grad V>|^2/||V||^2 <= ||grad V||^2

pointwise, with zero assigned on the zero set. Thus its aggregate density has uniformly bounded quadratic transport speed. If the **total** secondary second moment is finite at one time, the measures are Cauchy in the fixed-finite-mass P2 space and converge with their second moments.

Joint strong L2 convergence identifies that measure limit as ||W||^2 dx. It also gives weak convergence of xV to xW against compactly supported H-valued L2 tests. Uniform weighted norm boundedness extends the weak convergence to all such tests. Since the total weighted norms converge, Hilbert-space norm convergence gives strong convergence of xV to xW.

This argument is sufficient for the entire field and does not require a separate estimate of high-index weighted tails. Conversely, merely assuming that every coordinate has finite variance would be insufficient. The note explicitly retains the stronger total-moment condition.

Joint conformal H1 radiation follows from

    ||grad C_h(error)||_2
       <= h||grad error||_2+(1/2)||x error||_2.

The first term tends to zero by the uniform full secondary gradient bound, not by smallness of individual kinetic tails. The second tends to zero by the aggregate weighted result. Thus the claimed strong H1 convergence is justified even though physical terminal convergence is only sub-H1.

## 6. Global alternative and subthreshold Sigma scattering

Momentum is a continuous quadratic form on H^(1/2)(R^d;H), as seen from its multiplier xi. Joint H^(1/2) terminal convergence therefore suffices for the exact core velocity. The center expansion uses only scalar principal estimates and the joint momentum limit; no additional compactness step is hidden there.

The Hilbert-valued pseudoconformal conservation coefficient is correct:

    ||JU||_2^2-[8/(p+1)]t^2||U||_(p+1)^(p+1)=V0.

At a regular compactified endpoint, finite-time Sigma persistence supplies both derivative and weighted convergence. To make the Sigma scattering assertion explicit, write the inverse compactification as

    U(t,x)=t^(-d/2)exp(i|x|^2/(4t))Z(-1/t,-x/t).

For a difference from the compactified free comparison, differentiation gives ordinary gradient convergence from t^-1||grad error|| and (1/2)||y error||. Applying J=x+2it grad instead gives exactly twice the norm of the compactified derivative error. Since x exp(-it Delta)=exp(-it Delta)J, the latter is the position norm of the interaction-picture error. Thus H1 and weighted convergence of the compactified field give scattering in Sigma, with all norms joint in H.

In the singular compactified case, the preceding terminal and weighted arguments supply precisely the joint ingredients needed for the finite-dimensional inversion proof. No exchange of an infinite sum with independently selected scattering limits is used. The principal component separates the two alternatives, so their disjointness remains scalar and valid.

Finally, the harmonic-oscillator trace condition in Section 10 is consistent: finite weighted kinetic-plus-variance trace requires sum m_j e_j<infinity by the weighted min--max principle, and e_j is comparable to j^(1/d). Taking oscillator eigenfunctions proves sufficiency for some Sigma realization. This observation appropriately limits which trace-class spectra admit the global-Sigma hypothesis; it does not claim infinite-rank endpoint blowup construction.

## 7. Scope of this derivation

The new infinite-component steps pass the checks above. The review does not independently re-prove the R16 occupation plateau, the R17 strict-gap remainder, their scalar stability input, or the external Read--Schulz theorem. Those dependencies remain explicit. The justified enlargement is from finite rank to arbitrary trace-class rank for the stated dynamics and norms; it is not an enlargement of the two-dimensional occupation range, removal of total variance, or a proof of physical strong H1 terminal convergence.

## Addendum: final clarifications and spatial coherence operator

The author subsequently made both requested clarifications explicitly. I also read the added spatial-coherence subsection directly. Its trace-norm consequence is correct. If T_U is the Hilbert--Schmidt factor associated with the component functions, gamma_U=T_U T_U^*, and

    gamma_U-gamma_B=(T_U-T_B)T_U^*+T_B(T_U-T_B)^*.

The Schatten inequality ||AB^*||_S1<=||A||_S2||B||_S2 gives the asserted Lipschitz bound. The nonzero spectra of the spatial and component Gram operators agree. For B=cS+V and V pointwise perpendicular to c, the spatial kernel cross terms vanish exactly. Free propagation conjugates gamma_F by the free Schrödinger group. Thus both the finite-time and infinite-time trace-norm decompositions follow from the already proved joint L2 field limits. The caution about the concentrating rank-one operator having no asserted trace-norm limit, and the absence of any weighted kinetic trace-norm claim, is necessary and correctly retained.
