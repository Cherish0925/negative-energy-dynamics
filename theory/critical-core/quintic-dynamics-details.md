# Proof details: quintic endpoint and global finite-variance dynamics

Date: 2026-10-09.
Companion source: [quintic-dynamics.md](quintic-dynamics.md), Sections 2--8, including the final
global Sigma alternative. The companion variational input was checked
separately in [variational-extension-details.md](variational-extension-details.md).

The deductions use the stated
finite-component H1 solution theory, scalar stability lemma and inherited
Read--Schulz sharp one-dimensional inequality. No further small occupation
assumption or finite primary variance is introduced into Sections 2--6.
Section 7 explicitly requires finite secondary variances, and Section 8
explicitly requires full initial Sigma data. 

## 1. Individual phase variation and the unique principal atom

At exactly critical principal mass, scalar GN makes
E_scalar(exp(ib theta)u_1)>=0 for every real b. Expanding its quadratic
polynomial gives

    |integral J_1 theta'|^2
        <=2E_1 integral |u_1|^2 |theta'|^2.

This needs no preservation of the vector Gram matrix under the auxiliary
phase change: only scalar critical mass is used. E_1 is bounded, not
assumed conserved. The continuity equation is
partial_t|u_1|^2+2partial_x J_1=0, so the transport speed constant is
sqrt(8E_1). The bounded-test Hamilton--Jacobi argument cited in the
companion transport notes applies also to extended quadratic distance when
individual second moments are infinite.

As an independent one-dimensional consistency check, the exact amplitude
decomposition gives

    E_scalar(u_1)=E_scalar(|u_1|)
                    +(1/2)integral |J_1|^2/|u_1|^2,

with the usual zero-density convention. Scalar GN thus bounds the physical
continuity velocity action by8E_1, agreeing with the phase argument.

Finite transport cost to one fixed-time measure gives uniform tightness,
without presupposing second moments. Bounded-Lipschitz Cauchy convergence
then supplies a unique terminal measure retaining the whole mass. Full-time
scalar concentration identifies that measure as Mc delta_(x_*). This is
not based on an assumed secondary terminal field.

## 2. Automatic variance and rate

Passing to the terminal atom through tight couplings and lower
semicontinuity gives exactly

    integral |x-x_*|^2|u_1(t)|^2
        <=[integral_t^T sqrt(8E_1(r))dr]^2.

The only transport plan to an atom has the displayed moment as its cost;
this is what upgrades an initially possibly infinite variance to a finite
one. Combining I_1||u_1'||^2>=Mc^2/4 with I_1<=8E_bar(T-t)^2 yields the
gradient and scale constants in equation (7). Time reversal gives the
two-sided global existence assertion for infinite-variance primary data.
No uniform long-time H1 bound follows or is claimed there.

The conformal scalar energy expands as

    E_1(v)=h^2 E_1(u)+(h/8)I_1'+I_1/8,

and the phase bound gives |I_1'|<=4sqrt(2E_1 I_1). Thus the constant4 in
E_1(v)<=4E_bar/s^2 is correct.

## 3. Secondary limits without a global quintic forcing estimate

The primary remainder has L2 norm O(lambda) and bounded derivative.
One-dimensional Sobolev interpolation therefore gives its uniform norm
O(sqrt(lambda)). The principal field is consequently uniformly bounded
and tends to zero on each compact set avoiding x_*. The secondary fields
are uniformly H1 and hence uniformly bounded everywhere.

For a compactly supported smooth test avoiding x_*, both the linear term
and rho^2u_j in the tested equation are uniformly bounded. Thus every such
pairing has a terminal limit. These tests are dense in L2 because removing
one point does not affect L2 density. Uniform mass bounds then give a unique
full-trajectory weak L2 limit.

The individual secondary continuity equation with bounded kinetic energy
gives relative quadratic transport cost at most C|t-s|. Its tightness
consequence combined with local Rellich compactness gives global L2
precompactness. Weak-limit uniqueness upgrades this to full strong L2
convergence, then to strong H^sigma for sigma<1 and uniform convergence by
one-dimensional interpolation. No estimate of the singular forcing in a
global negative Sobolev norm is required.

Exact principal-secondary Gram orthogonality, after division by the core
factor sqrt(lambda), gives a Q-weighted average of u_j of size O(sqrt(lambda)).
The uniform H1 Holder estimate controls its difference from the value at
the core center by the same order. Hence u_j(t,x(t))=O(sqrt(lambda)) and the
continuous terminal background satisfies w_j(x_*)=0. The complete secondary
Gram matrix is preserved by strong L2 convergence.

## 4. Weighted convergence and conformal radiation

If the secondary variances are finite at one time, the transport estimate
places their densities in the complete finite-mass P2 space up to T.
The identified terminal density and P2 convergence imply convergence of
weighted norms. The weighted fields converge weakly, first against compact
tests and then globally by boundedness. Weak convergence plus convergence
of norms yields strong weighted L2 convergence; this step does not infer
phase convergence from density convergence alone.

Subtracting free evolution of the terminal field gives an error tending to
zero in L2 and weighted L2, with bounded derivative. Under the conformal
map its derivative is bounded by h times that derivative plus half the
weighted error. This proves H1 free scattering of each conformal secondary
field. Differentiating the exact free transform gives
||f_j'||^2=||x W_j||^2/4 and preserves all Gram entries.

The physical energy decomposition has three nonnegative secondary or
interaction integrals. Their sum is uniformly bounded by bounded primary
energy and secondary kinetic energy. Their conformal images acquire the
factor h^2. They therefore vanish, leaving the conserved conformal energy
equal to one half of the free secondary kinetic energy, as stated in (17).

## 5. Global Sigma alternative and its quantitative core error

For the transformation in (19), direct differentiation gives

    A(W)=||J(t)U||^2/4,    F(W)=t^2F(U).

The virial law V''=16E and
||JU||^2=V-tV'+4t^2A give
||JU||^2-(4/3)t^2F=V_0, so E(W)=V_0/8. Both the factor4/3 and the factor1/8
are correct for the one-dimensional quintic normalization.

There are exactly two H1 continuation possibilities at the finite conformal
endpoint0. If it extends, local Sigma persistence and comparison with the
free solution at that endpoint yield H1 scattering after the inverse map.
If it blows up, the previous endpoint theorem applies. Its scale is
lambda(s)<=C|s|, giving a physical core width ell(t)<=C. The principal
remainder's derivative remains bounded, its mass is O(lambda), and its
position norm relative to x_* is O(|s|). The inverse map consequently gives
a physical primary H1 error O(1/t), even if ell(t) tends to zero.

Secondary H^(1/2) convergence implies momentum convergence. Conservation
of total conformal momentum supplies the principal momentum limit P_*.
The principal centroid identity then gives
b_1(s)=x_*+(2P_*/Mc)s+o(|s|). The profile-center discrepancy is
O(lambda^2+|s|lambda)=O(s^2), proving
X(t)=-x_*t+2P_*/Mc+o(1).

Replacing the quadratic phase by the carrier exp(ivx/2) costs O(1/t) in
H1 uniformly for bounded ell. In the derivative of the profile, its
potential ell^(-1) factor is canceled by the factor ell in the phase
difference. Thus no unproved lower bound on ell is used.

The physical momentum formula remains valid for arbitrarily small ell:
integration by parts places the linear cross-term derivative on the
O(1/t) H1 error, giving a momentum discrepancy O(1/t), independent of the
possibly large core gradient. Secondary free scattering preserves their
limiting momenta and Gram matrix.

Finally the alternatives are disjoint. A bounded-width Townes core retains
positive mass in a uniformly bounded-radius moving interval, whereas a
free L2 Schrodinger solution has uniformly vanishing mass in every such
interval. The latter follows by L1-intersect-L2 approximation and the free
dispersive estimate. The theorem leaves the scale limit and phase law
unclassified, exactly as its statement says.

No correction was needed in the audited Sections 2--8.
