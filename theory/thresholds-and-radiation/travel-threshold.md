# Compactification of the negative-energy traveling-wave mass threshold

This is a new derivation in the preliminary calculations. It does not determine the numerical threshold and does not establish its strict negative-energy attainment. It identifies every possible failure of compactness at that threshold. Its proof uses standard translation profile decomposition and exact profile identities; no novelty is claimed for those ingredients.

## 1. Model and threshold

Let N>=1, m>1, s=m/2, r=m/N, p=2+2r. Let a be a real even positive elliptic m-homogeneous Fourier symbol, C^{N+2} away from the origin. Write

- M(U)=||U||_2^2;
- A(U)=integral a(xi)|Uhat(xi)|^2 dxi;
- E(U)=A(U)/2-||U||_p^p/p;
- P(U)=integral xi |Uhat(xi)|^2 dxi.

The sharp critical mass Mc is characterized by

||f||_p^p <= (p/2)(M(f)/Mc)^r A(f).

A traveling profile is a nonzero U in H^s satisfying

[a(D)+omega+i v.grad]U-|U|^{p-2}U=0

weakly. The existing regularity and cutoff Pohozaev arguments give

v.P(U)=2m E(U),

omega M(U)=r A(U)+(2m-p)E(U).

Assume that at least one negative-energy traveling profile exists. Define

Mtr=inf{M(U): U is an exact traveling profile, E(U)<0}.

Then Mc<=Mtr<infinity. The previously established phase-coercivity argument supplies the stronger strict gap Mtr>Mc. The theorem below itself only needs the sharp GN inequality, not that stronger gap or any ground-state uniqueness/nondegeneracy.

## 2. A velocity identity without a spatial moment

**Lemma.** Every H^s traveling profile satisfies

v M(U)=integral grad a(xi)|Uhat(xi)|^2 dxi.

Consequently, with

Ca=sup_{xi !=0} |grad a(xi)| / a(xi)^((m-1)/m),

one has

|v| <= Ca [A(U)/M(U)]^((m-1)/m).

For a(xi)=|xi|^4, Ca=4.

**Proof.** The action is S=E+omega M/2-v.P/2. Choose a real chi in C_c^infinity equal to x_j near zero and put chi_R(x)=R chi(x/R). The curve theta -> exp(i theta chi_R)U is differentiable in H^s for fixed R, and S'(U)=0 implies

2 Re <a(D)U, i chi_R U> = integral (v.grad chi_R)|U|^2.

The right side tends to v_j M by dominated convergence. The left side is the quadratic form of the commutator of a(D) with chi_R. Its Fourier kernel, apart from the harmless Fourier convention constant and factor i, is

(a(xi)-a(eta)) R^{N+1} chihat(R(xi-eta)).

The mean-value estimate for a gives

|a(xi)-a(eta)| <= C |xi-eta| (|xi|+|eta|)^{m-1}.

After dividing by <xi>^s<eta>^s, splitting the region where |xi| and |eta| are comparable from its complement gives the upper bound

C |xi-eta| <xi-eta>^s.

The resulting convolution kernel has uniformly bounded L^1 norm for R>=1, since after q=R(xi-eta) the linear factor cancels the extra R. Thus these commutators have uniformly bounded forms on H^s. For Schwartz U the limit is obtained by chi_R U -> x_j U in L^2 and the Fourier differentiation identity; it equals integral partial_j a |Uhat|^2. Density and the uniform form bound extend the limit to all H^s. This proves the identity. Hölder's inequality then gives

|v|M <= Ca A^((m-1)/m) M^(1/m).

This argument does not differentiate exp(i eta.x)U directly in H^s; that would incorrectly require an unassumed spatial moment.

## 3. Main compactification theorem

**Theorem.** Let U_n be any sequence of negative-energy exact traveling profiles such that M(U_n)->Mtr. Apply the mass-preserving scaling to normalize A(U_n)=1, and scale their parameters accordingly. After a subsequence exactly one of the following alternatives holds.

**A. A negative-energy endpoint.** There are translations x_n and a nonzero exact traveling profile U_* such that

U_n(.+x_n)->U_* strongly in H^s,

M(U_*)=Mtr, A(U_*)=1, E(U_*)<0.

The frequencies and velocities converge to those of U_*.

**B. A zero-energy endpoint configuration.** E(U_n)->0. There are an integer J with

1<=J<=floor(Mtr/Mc),

nonzero exact traveling profiles V_1,...,V_J, and translations x_n^j with |x_n^j-x_n^k|->infinity for j!=k, such that

U_n - sum_{j=1}^J V_j(. - x_n^j) ->0 strongly in H^s.

All V_j solve the same profile equation with the same limiting frequency omega_* and velocity v_*, and

E(V_j)=0, M(V_j)>=Mc,

sum_j M(V_j)=Mtr, sum_j A(V_j)=1,

omega_*=r/Mtr>0,

v_*.P(V_j)=0, omega_* M(V_j)=r A(V_j).

In particular there is no diffuse L^2 component and no high-frequency kinetic remainder at the endpoint. Constant phase factors are absorbed in the fixed profiles; subsequences of phase factors can always be taken when needed.

**Proof.**

### Step 1: parameter compactness

The normalization is U_lambda(x)=lambda^{N/2}U(lambda x) with lambda=A(U)^(-1/m). Then omega_lambda=lambda^m omega, v_lambda=lambda^{m-1}v and E_lambda=lambda^m E. Thus A=1 and the mass is unchanged.

Sharp GN and E_n<0 imply

-[ (M_n/Mc)^r-1 ]/2 <= E_n <0.

The masses are bounded and bounded away from zero. The velocity lemma gives a uniform bound on v_n; the scalar Pohozaev identity gives a uniform bound on omega_n. Pass to a subsequence with E_n->e<=0, v_n->v_*, omega_n->omega_*. The identity gives

omega_* Mtr=r+(2m-p)e.

### Step 2: translation profiles and inheritance of the exact equation

Use the standard translation profile decomposition for a bounded H^s sequence, with p strictly between 2 and the Sobolev endpoint. It produces profiles V_j and separating translations, quadratic norm decoupling, Brézis--Lieb decoupling, and a remainder tending to zero in L^p after taking the number of profiles to infinity. Precisely,

sum M(V_j)<=Mtr, sum A(V_j)<=1,

lim ||U_n||_p^p=sum ||V_j||_p^p.

The last equality follows in the iterated decomposition limit. The local compactness H^s_loc -> L^p_loc and convergence of the parameters imply that each nonzero V_j solves the same exact profile equation with (omega_*,v_*). No coercivity of a(xi)+omega_*-v_*.xi is assumed.

The decomposition only requires translations: concentration to arbitrarily small scales is negligible in this L^p norm because the exponent is H^s-subcritical, while spreading and modulation escape are also L^p-negligible under the H^s bound. The standard proof can equivalently be given by iterative nonzero translated weak limits and the local-vanishing lemma.

### Step 3: any negative-energy profile forces complete compactness

If E(V_j)<0 for any j, then by the definition of Mtr, M(V_j)>=Mtr. Quadratic mass decoupling forces equality and strong L^2 convergence of U_n(.+x_n^j) to V_j.

For the difference w_n, the H^s norm remains bounded. Sharp GN gives ||w_n||_p^p<=C M(w_n)^r A(w_n)->0. Also

|P(w_n)|<=C M(w_n)^(1-1/m) A(w_n)^(1/m)->0.

Polarization (or interpolation to H^{1/2}) therefore gives P(U_n)->P(V_j). The exact Pohozaev identity yields E_n->E(V_j), and the convergence of the nonlinear norms yields A(U_n)->A(V_j). Weak H^s convergence together with norm convergence is strong. This is Alternative A.

If e<0 then at least one such negative-energy profile must exist: otherwise every E(V_j)>=0, and the nonlinear and kinetic decoupling gives

e = sum_j E(V_j) + [1-sum_j A(V_j)]/2 >=0,

a contradiction. The series is convergent since both nonnegative quadratic and nonlinear norm series converge.

### Step 4: the only remaining endpoint is a finite zero-energy configuration

If Alternative A fails, then no V_j has negative energy and e=0. The same energy identity gives

0=sum_j E(V_j)+[1-sum_j A(V_j)]/2.

Every term is nonnegative. Hence every nonzero V_j has E(V_j)=0 and sum_j A(V_j)=1. Sharp GN implies M(V_j)>=Mc. There can consequently be only finitely many profiles, J<=floor(Mtr/Mc), and at least one because their kinetic energies sum to one.

The limit frequency satisfies omega_*=r/Mtr>0. Applying the second Pohozaev identity individually to each zero-energy V_j yields omega_* M(V_j)=r A(V_j). Summing it gives

omega_* sum_j M(V_j)=r=omega_* Mtr.

The strict positivity of omega_* therefore forces sum_j M(V_j)=Mtr. Both the mass and the kinetic remainder vanish, proving strong H^s convergence to the separated finite sum. The other identities follow directly from the profile equations. QED.

## 4. Consequences that do not overstate the theorem

1. If a minimizing sequence has -E(U_n)/A(U_n)>=eta>0, then Mtr is attained by a negative-energy traveling profile. Thus a failure of negative-energy attainment necessarily approaches zero normalized energy.
2. If Mtr<2Mc, every normalized minimizing sequence has a strongly convergent translated subsequence to one profile of mass Mtr and energy <=0. The theorem does not decide whether its energy is strictly negative or zero.
3. More generally, all lack of compactness at this threshold consists of finitely many zero-energy profiles with a common (omega,v); unconstrained radiation is not an additional endpoint mechanism.
4. If the limiting velocity is zero, Alternative B is a finite collection of standing profiles at a common positive frequency. If it is nonzero, every endpoint profile is a zero-energy traveler with momentum orthogonal to that common velocity.
5. This is a static compactification theorem. It proves neither soliton resolution for time-dependent solutions nor exclusion of a global bounded negative-energy orbit.
6. It applies to any fixed symbol in the above homogeneous class for which the negative-energy traveler set is nonempty. For the pure four-dimensional BNLS, the previous validated construction is the source of nonemptiness; the compactification proof is otherwise independent of that construction.

## 5. Classical ingredients / priority notes

The translation profile decomposition and concentration-compactness method are classical. An explicitly relevant biharmonic predecessor is the primary article "Biharmonic nonlinear Schrodinger equation and the profile decomposition", Nonlinear Analysis 74 (2011), 6244--6255, DOI 10.1016/j.na.2011.06.004. Its accessible abstract explicitly establishes decomposition of bounded H^2 sequences and sharp GN inequalities. The above finite zero-energy endpoint alternative is a derivation for this particular negative-energy mass threshold; a comprehensive novelty determination has not been completed.

Primary source:
https://www.sciencedirect.com/science/article/abs/pii/S0362546X11004123

The velocity identity is a standard Noether / group-velocity relation; the important use here is that it prevents escape of the normalized parameters even without assuming positivity of the full traveling linear symbol.

## 6. Exact branch identity: negative inertia lowers mass for order m>2

Suppose a C^2 branch z -> U_z of exact profiles exists at fixed frequency omega>0 and velocity v=z e, where e is a fixed unit vector. Suppose U_0=Q is real. Define the axial momentum Pi(z)=e.P(U_z), and let kappa=Pi'(0). Then, exactly along the branch,

omega dM(U_z)/dz = [(m-1)z Pi'(z)-Pi(z)]/m.

Indeed S_z(U_z)=E(U_z)+omega M(U_z)/2-z Pi(z)/2 has derivative -Pi(z)/2 because U_z is critical for S_z. Substituting the exact Pohozaev relation E(U_z)=z Pi(z)/(2m) proves the identity. Since Q is real, Pi(0)=0. Integration gives

E(U_z)=kappa z^2/(2m)+o(z^2),

M(U_z)=M(Q)+(m-2)kappa z^2/(2m omega)+o(z^2).

Thus if m>2 and kappa<0, every sufficiently small nonzero z has both negative energy and mass strictly below that of its standing parent. In particular Mtr<M(Q), not merely Mtr<=M(Q), for every such negative-inertia seed. The four-dimensional cubic BNLS construction has m=4, omega=1 and Pi(z)=2Iz+O(z^3), with the validated I<0, so

E(U_z)=I z^2/4+O(z^4),

M(U_z)=M(Q)+I z^2/2+O(z^4),

M(U_z)-M(Q)=2E(U_z)+O(z^4).

The O(z^4) statements use the analytic even/odd branch symmetry available for that construction; the general C^2 branch conclusion only uses o(z^2). This relates the phase spectral response directly to the direction of movement of the mass threshold. The bifurcation construction itself and its validated inertia sign remain inputs, not conclusions of this identity.
