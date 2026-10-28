# Least-mass traveling endpoints and neutral Hamiltonian modes

Research note, 8 October 2026. This extends the compactification theorem in
[threshold-section.tex](../../manuscripts/thresholds-and-radiation/threshold-section.tex) and the response identities in
[inertia-section.tex](../../manuscripts/thresholds-and-radiation/inertia-section.tex). The conclusions below concern exact profiles
and the linearized evolution. No nonlinear instability conclusion is asserted.

## 1. Setting and a useful Legendre identity

Use the real Hilbert pairing on the complex energy space X=H^{m/2}, m>1.
Let

    F(U,ω,v)=a(D)U+ωU+i v·∇U−|U|^{2m/N}U,
    S_{ω,v}=E+ω M/2−v·P/2,    L=S''_{ω,v}(U).

The dispersion a is real-even, positive elliptic and m-homogeneous. The
energy and charges have the normalization used in round 10. Let Mtr denote
the infimum of masses of all negative-energy exact traveling profiles.
Assume this set is nonempty.

On a C1 family U_{ω,v} of profiles with C2 reduced action
d(ω,v)=S_{ω,v}(U_{ω,v}), put H=d'' and B=D_v P. Stationarity gives

    ∇d=(M/2,−P/2),
    E=d−(ω,v)·∇d,
    ∇E=−H(ω,v),                       (1)
    ∇M=2H e_ω.

This elementary identity is particularly useful at a least-mass endpoint:
mass extremality and energy extremality produce different explicit null
vectors of the same charge Hessian.

If the branch is locally closed under critical scaling, the charges obey

    mω M_ω+(m−1)v·M_v=0,
    mω P_ω+(m−1)Bv=P,
    M_v=−P_ω.                         (2)

The final relation is the Maxwell symmetry of H. Such local scaling
covariance follows from local uniqueness modulo phase and translation.

## 2. A negative-energy attained threshold has degenerate charge response

THEOREM A. Suppose U* is a negative-energy profile with M(U*)=Mtr and lies
on a C1 full parameter family U_{ω,v} with C2 reduced action. Then

    M_ω=0,  M_v=0,  P_ω=0,
    H e_ω=0.                          (3)

If the family has scaling covariance, then also

    (m−1)Bv=P,
    v^T Bv=(v·P)/(m−1)<0.             (4)

In particular the charge Hessian is singular; no invertibility assumption
on B is needed. If B is invertible, the scalar κ of round 10 is exactly zero.

PROOF. Negative energy is an open condition. Every nearby member of the
family therefore has mass at least Mtr, so M has a local minimum at the
parameter of U*. All first derivatives of M vanish. Apply (1), Maxwell
symmetry, and (2). Finally v·P=2mE<0 gives the last strict inequality.

This theorem does NOT prove nonattainment of Mtr. A least-mass profile is
allowed to occur exactly at a degenerate charge response. Assuming that H
is nonsingular and then excluding attainment is only a conditional result.

## 3. Obtaining the family from the profile equation

The supplied-family hypothesis in Theorem A can be replaced by a local
elliptic nondegeneracy hypothesis. Assume the usual local regularity for
the profile map and symmetry action, and suppose L:X→X* is selfadjoint
Fredholm with

    ker L=K:=span_R{iU,∂_1U,...,∂_NU}.                       (5)

The symmetry generators are independent for a nonzero L2 profile. Indeed,
a dependence would impose a constant-coefficient first-order equation and
force the Fourier transform onto a measure-zero affine hyperplane.

Take a fixed slice perpendicular to K. The restriction of L to this slice
and the annihilator of K is an isomorphism. The implicit-function theorem
solves the projected profile equation for all (ω,v) near the original
parameters. The residual belongs to K. The gauge and translation Noether
identities say that the residual pairs to zero with iU_new and ∂_jU_new.
Their Gram matrix with the original K is invertible near U, so the residual
vanishes. This yields a full family, locally unique modulo symmetries.
Regularity of the projected solutions, or a stronger regularity space for
the slice construction, must be included when using the derivative
generators; the argument does not posit differentiability of arbitrary
energy-space translation paths.

A convenient sufficient setting for Fredholmness is

    ω>sup_ξ(v·ξ−a(ξ)),

with compactness of the nonlinear potential perturbation. This gives a
positive free spectral gap. The theorem can simply use (5) and Fredholmness
as its precise hypothesis, without making an unproved decay assertion.

Consequently a negative-energy attained threshold cannot simultaneously
have a regular profile slice and a nonsingular charge response. Failure
can occur through loss of the free spectral gap, additional profile kernel,
or degeneracy of H; the alternatives are not claimed mutually exclusive.

## 4. A length-three neutral Jordan chain

THEOREM B. In the Fredholm setting (5), suppose a C1 full family exists and
H has a nonzero null vector q=(q_ω,q_v). Set

    Z=D_{ω,v}U[q],
    g=q_ω iU−q_v·∇U,
    J=−i.

Then there is W∈X solving

    L W=iZ,
    JL W=Z,    JL Z=g,    JL g=0.                           (6)

The vectors form a genuine length-three chain, because g is nonzero and
Z is not in ker L. If JL generates the linearized evolution on the chosen
phase space, there is the exact polynomial solution

    exp(tJL)W=W+tZ+(t²/2)g.                                (7)

Modulo phase and translation tangent directions its norm grows at least
linearly. This is a secular linearized instability modulo the symmetry
orbit, not a positive-real-part eigenvalue or a nonlinear instability
theorem.

PROOF. Parameter differentiation gives

    L U_ω=−U,       L U_{v_j}=−i∂_jU,

and hence JL Z=g. The equation LW=iZ is solvable iff iZ annihilates K.
For the phase generator its pairing is DM[Z]/2. For each translation
generator its pairing is DP_j[Z]/2, with the signs determined by the
antilinear complex pairing; vanishing is independent of these signs.
The condition Hq=0 is exactly the simultaneous vanishing of these charge
derivatives. Fredholm solvability proves existence of W. Generator
independence gives g≠0 and LZ≠0. Equation (7) follows from the finite chain.
After projection to X/K the linear term is nonzero, since Z∉K.

At a regular negative-energy attained threshold one can take q=e_ω.
Thus minimal traveling mass forces a longer neutral chain even when the
profile Hessian has no extra zero eigenfunction beyond symmetries.

## 5. Splitting at zero energy forces degeneracy of every regular component

THEOREM C. Let V be a zero-energy exact profile with M(V)<Mtr. Suppose it
belongs to a full smooth profile family. Then

    ∇E(V)=0,       H·(ω,v)^T=0.                            (8)

For a scaling-covariant family and ω≠0 this implies

    Bv=−P,    M_v=−P/ω,    M_ω=0.                          (9)

PROOF. By continuity, every member in a sufficiently small neighborhood
still has mass less than Mtr. None can have negative energy by definition
of Mtr. Since V has zero energy, it is a local minimum of energy on the
family. Apply (1). Differentiating E=v·P/(2m) gives Bv=−P; then use (2)
and v·P=0.

For each component of a genuinely split threshold limit from round 10,
M(V_j)<Mtr and ω*=r/Mtr>0. Thus every component with a regular profile slice
has a singular charge Hessian. By Theorem B each such regular component
has a length-three neutral Jordan chain. This strengthens finite splitting:
it cannot consist entirely of ordinary nondegenerate-charge waves.

At an isotropic rotationally equivariant family P=p(c)e, c=|v|>0,
zero energy gives p(c)=0 and (9) gives p'(c)=0. Therefore B=0, and
all entries of H vanish. A nonzero-speed split component is then much more
degenerate than a simple turning point. This conclusion needs rotational
equivariance of the family, not merely isotropy of the equation.

## 6. A nonsingular charge Hessian is impossible at a moving zero endpoint

THEOREM D. Suppose E(U)=0, M(U)≤Mtr, v≠0, and U lies on a smooth full
profile family. Then H is singular.

PROOF. If H were nonsingular, the inverse-function theorem for the charge
map (ω,v)↦(M,P) would allow independent first-order changes of M and P.
Along the profile family stationarity gives the first-law identity

    dE=−(ω/2)dM+(v/2)·dP.                                 (10)

Choose dM<0 and choose dP with a sufficiently negative component along v,
so that dE<0. A small positive perturbation then has negative energy and
mass strictly less than Mtr, a contradiction. This proof requires only
local differentiability and invertibility, not a Hessian of the mass.

There is an important exception to avoid concealing: if v=0, E=0 and
P≠0, this argument fails. A complex stationary wave with nonzero momentum
has not been excluded by the available theory. If v=0 and P=0, critical
scaling gives H(mω,0)=0; at the normalized zero endpoint ω>0, so H is
singular. Thus a single zero-energy endpoint with regular slice either has
degenerate charge response, or is a standing profile with nonzero momentum.
This exceptional possibility must not be silently discarded by assuming
that every stationary profile is real up to constant phase.

## 7. Exact local turning structure in the isotropic attained case

At fixed ω>0 let P=p(c)e and M=M(c), c>0. At an attained negative-energy
mass threshold, Theorem A gives

    p(c*)<0,    p'(c*)=p(c*)/[(m−1)c*]<0.                  (11)

Hence B is negative definite and H has exactly N positive eigenvalues and
one-dimensional kernel. Suppose the family has enough derivatives and
the mass minimum is nondegenerate: M''(c*)>0. With

    κ(c)=p(c)^2/p'(c)−(m−1)c p(c),

the exact branch identity of round 10 yields

    κ(c*)=0,
    κ'(c*)=−mω(m−1)c* M''(c*)<0.                          (12)

To verify (12), differentiate
mω M'=(m−1)c p'−p once and substitute (11) in the derivative of κ.
Thus as speed crosses c*, the positive index of H changes from N+1 to N.
No Hamiltonian eigenvalue bifurcation is inferred here without the spectral
hypotheses needed to relate charge inertia to the spectrum of JL.

## 8. Scope and relation to prior stability theory

The principle linking degenerate conserved-charge slopes to extra neutral
Jordan chains is classical Hamiltonian solitary-wave theory. It must not
be advertised as a newly discovered general mechanism. The present content
is its precise consequence for the least-negative-energy traveling-mass
threshold and its finite-splitting compactification, including the explicit
identities (4), (9), and (12).

Primary sources checked on 8 October 2026:

* Grillakis, Shatah and Strauss, *Stability theory of solitary waves in the
  presence of symmetry, II*, J. Functional Analysis 94 (1990), 308–348,
  DOI 10.1016/0022-1236(90)90016-E.
  https://www.sciencedirect.com/science/article/pii/002212369090016E
* Comech and Pelinovsky, *Purely nonlinear instability of standing waves
  with minimal energy*, Comm. Pure Appl. Math. 56 (2003), 1565–1607,
  DOI 10.1002/cpa.10104. Author page:
  https://dmpeli.math.mcmaster.ca/PaperBank/comech1.html
  The latter paper treats a U(1) setting and a higher zero-eigenvalue
  degeneracy mechanism. Its nonlinear theorem is not imported here: the
  extra symmetries and Morse index assumptions require separate work.

Web source refs: , , .

Unresolved: this note does not determine whether Mtr is attained, compute
Mtr, rule out its zero-energy splitting, or prove nonlinear instability
of every endpoint. It locates attainment/splitting in precise degenerate
spectral structures and produces actual linearized secular solutions when
the Fredholm profile hypotheses hold.
