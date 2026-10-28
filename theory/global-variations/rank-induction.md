# rank induction — no new exclusion obtained

16 October 2026. This branch does not prove a new rank exclusion or improve
the sharp constant. The distinctions below prevent existing restrictions or
algebraic restatements from being counted as new results.

## What was checked against previous work

The starting materials were `r25_global_variation.md`,
[global-route.md](../all-scale-scattering/global-route.md), and [r24_deletion_symbolic.py](../../computations/all-scale-scattering/r24_deletion_symbolic.py). The proposed
minimal-rank consequences were then checked against
[global-bridge.md](../townes-spectral-structure/global-bridge.md) and [collective-hessian.md](../collective-threshold/collective-hessian.md).

For a first violating rank, lower-rank scalar-constant inequalities imply
that every proper occupied-space split has a definite density overlap and
that every occupied binding energy is bounded below by a positive fraction
of the sum of occupied energies. These statements, including arbitrary
occupied-space rotations and the resulting bound on spectral scale ratios,
are already proved in R23, Sections 2–3. The real Haar compression loss
and its dependence on the first violating rank are already in R21. They
are not R26 results.

The deletion deficit for every real unit vector a can be written as a
nonnegative quartic polynomial in a. Averaging that polynomial against
matrix-valued Haar moments generates further necessary matrix conditions,
but no contradiction, improved rank exclusion, or uniform scalar constant
was obtained. This calculation is therefore not promoted to a result.

## The radial deletion attempt

Use the notation of [global-route.md](../all-scale-scattering/global-route.md): the original common-density
state has positive first radial orbital w, strictly ordered binding energies,
and transformed orbitals v_j for j>=2. Set

    S = sum_(j>=2) v_j²,   Tv = sum_(j>=2) int |grad v_j|²,
    Fv = int S²,           WS = int W S,
    Er = sum_(j>=2) e_j M_j.

All integrals use planar measure. The exact transformed equations give

    Tv + WS - Fv = -Er.

The radial scaling identity gives

    I := int r W' S = 2 Tv - Fv.

Consequently

    I = Fv - 2 WS - 2 Er.

This last equality is recorded only to identify the direction of the
missing bound. It is not an additional estimate. In particular, W>0 does
not compare Fv with 2(WS+Er). The original radial component identity
T(u_j)=e_j M_j identifies Er with the original remaining kinetic energy,
but does not compare that quantity with Tv or Fv in the required direction.

Substituting the two density derivative identities from R24 and integrating
by parts returns the same scaling equality. No additional nonnegative
remainder was obtained. Pointwise W'<=0 and rho>=S cannot be inserted: the
R24 stationary computations already rule out those shortcuts.

## Conclusion

The implication

    [int r W' S <= 0 for every exact radial deleted family]
    + [the lower-rank sharp inequality]
    => [no equal-mass radial self-consistent state with beta < Mc]

remains a conditional induction step established in R24. This branch has
neither proved its missing premise nor constructed an exact radial family
that falsifies it. No claim about its sign follows from the checked
identities alone.

The general nonradial deletion is additionally obstructed by the issues
proved in R25: its transformed objects are constrained differential forms,
and discarding either their form constraint or the subtractive partner
spectrum loses the scalar sharp constant. Those are established obstructions,
not new R26 discoveries.

There is therefore no R26 rank-induction theorem to add to the mainline
results. The preceding overlap, energy, and Haar statements must remain
attributed to R21/R23; the unresolved radial integrated sign remains at
R24's previously stated status.
