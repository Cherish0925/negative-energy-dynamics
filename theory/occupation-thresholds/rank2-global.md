# R16 rank-two endpoint: global structural calculations

Date: 2026-10-09. This branch did not prove or disprove the unrestricted
equal-occupation rank-two endpoint. Its decisive contribution this round was
the proof of the stronger occupation theorem and endpoint
dynamics, recorded separately. This note preserves the global endpoint
calculations without presenting them as a solution.

Let `C1=2/Mc`. For an orthonormal real pair u,v set
`rho=u^2+v^2`, `A=integral(|grad u|^2+|grad v|^2)`, and
`F=integral rho^2`. The unresolved inequality is `F<=C1 A`.

## 1. Exact scalar-deficit identity

Define `delta_u=C1||grad u||_2^2-integral u^4` and similarly delta_v.
Then

```
F-C1 A = 2 integral u^2v^2-delta_u-delta_v.
```

Scalar GN alone supplies nonnegativity of the two deficits; it does not
control the positive overlap by their sum. Orthogonality cannot be discarded
at this step. The R16 occupation theorem resolves the corresponding overlap
problem when the second occupation is sufficiently small, but equal weights
do not satisfy that hypothesis.

For `w_theta=u cos(theta)+v sin(theta)`, norm one follows from orthogonality.
Writing `delta(theta)=C1||grad w_theta||_2^2-integral w_theta^4`, direct
angular averaging gives

```
average_theta delta(theta) = C1 A/2 - 3F/8.
```

Thus the rank-two endpoint is equivalently the strengthened averaged-deficit
bound `average delta>=C1 A/8`. Mere nonnegativity only gives
`F<=(4/3)C1 A`, which is insufficient. This calculation isolates the exact
missing quantitative content of an approach based on all rotated scalar
projections.

## 2. What a genuine optimizing counterexample must satisfy

The finite-rank optimizer and shell-gap theory of Frank--Gontier--Lewin,
combined with spectral duality, allows one to study a real potential and real
eigenfunctions. If the optimal rank-two constant C2 is strictly larger than
C1, the two occupied eigenfunctions can be chosen u>0 and v real, with

```
V=(2/C2)(u^2+v^2),
(-Delta-V)u=-e1 u,
(-Delta-V)v=-e2 v,
e1>e2>0.
```

The occupied spectral cutoff cannot split a degenerate eigenvalue. The exact
ground-state transform for `f=v/u` is

```
-div(u^2 grad f)=(e1-e2)u^2 f,
integral u^2 f=0,   integral u^2 f^2=1,
integral u^2 |grad f|^2=e1-e2.
```

It preserves the sign-changing information absent from absolute-value Young
estimates. No inequality closing this weighted eigenfunction problem under
the nonlinear relation for V was obtained here.

If V is radial and the second eigenvalue is simple, the second occupied
eigenfunction must be radial: every nonzero angular harmonic has the usual
twofold real angular degeneracy. Consequently a radial optimizing
counterexample would require a radial excited second state. A radial
ground-plus-one-vortex candidate cannot be the full rank-two spectral
optimizer because it leaves a degenerate shell incomplete. This does not
exclude radial ground-plus-radial-excited configurations or nonradial ones.

Source checked directly: Frank--Gontier--Lewin, *Optimizers for the finite-rank
Lieb--Thirring inequality*, arXiv:2109.05984v2, existence/bubble decomposition
and Euler--Lagrange/shell-gap results. The structural framework is theirs,
not a claimed invention of this project.

## 3. A fully global exclusion of nonzero-angular-momentum radial-density pairs

There is a useful exact exclusion class independent of any Townes ansatz.
For a nonnegative radial potential V and angular harmonic m!=0, the radial
zero-energy Green kernel of
`A_m=-partial_rr-r^(-1)partial_r+m^2/r^2` is

```
G_m(r,s)=(1/(2|m|))(min(r,s)/max(r,s))^|m|.
```

The trace bound for the corresponding positive Birman--Schwinger operator
gives

```
integral V|psi|^2
 <= [(1/(2|m|)) integral_0^infinity r V(r)dr]
       integral |grad psi|^2.
```

Let a finite common-density field have radial rho and have every component in
an angular sector with `|m_j|>=m0>=1`. Its total mass is M. Substituting
V=rho and summing gives

```
integral rho^2 <= (M/(4pi)) sum_j ||grad u_j||_2^2/|m_j|
              <= (M/(4pi m0)) A.
```

For a normalized orthonormal pair M=2 this proves

```
F/A <=1/(2pi m0)<=1/(2pi)<2/Mc=C1.
```

Thus all such pairs, including counter-rotating vortex pairs with arbitrary
radial amplitudes, are separated strictly from the disputed scalar constant.
This is a global estimate on that class, not a small-amplitude calculation.
It does not cover an m=0 component, which is unavoidable for the ground
eigenfunction of an optimizing positive potential.

The same classical angular estimate gives global H1 control in this invariant
symmetry class whenever `M<8pi m0`, by

```
E >= (1/2)(1-M/(8pi m0)) A.
```

The symmetry class is preserved when each component initially has a single
angular harmonic and radial amplitude: the common density stays radial and
the common potential preserves each angular sector. This is a model-level
sufficient bound; neither sharpness nor historical novelty is asserted.

## 4. Relationship to the other R16 branches

The separate Yukawa-resolvent branch closes the sign for every fixed unequal
scale ratio in the far-separated two-Townes construction. Together with the
global angular exclusion above, this limits several explicit counterexample
mechanisms. It is not an exclusion of all possible configurations.

The completed R16 advance is instead the sharp theorem under a separated
largest occupation, now independent of the number and total occupation of
secondary modes, plus its spectral remainder and dynamical consequences.
Its proof is in the accompanying files.

