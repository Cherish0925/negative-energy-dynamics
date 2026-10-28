# Proof details of the R16 endpoint dynamics argument

Date: 2026-10-09. File audited: [threshold-rigidity.md](threshold-rigidity.md), including the
extended transport-cost argument, full background-field limit, final
separated-top-occupation hypothesis, and all-time global deficit update.

## Conclusion

The argument proves necessary structure and a lower blowup-rate bound for any
finite-time H1 blowup at the stated fixed-spectrum threshold. The audited
dynamics note does not itself construct that blowup; a separate R16 branch
handles existence. The phase-current
estimate, terminal measure, coherent atom, strong regular-background limit,
and rate `||grad u_1(t)||_2 >= c/(T-t)` all pass the audit.

The conclusion does not require a finite variance. The truncated-cost
Kantorovich argument supplied in the note is sufficient for measures of finite
mass whose individual second moments may be infinite.

## 1. Energy normalization and entry into the scalar stability neighborhood

In the diagonal Gram basis write `u_j=sqrt(Mc t_j) phi_j`, `t_1=1`, with
orthonormal phi_j. Let `a=||grad phi_1||_2^2` and
`B_raw=sum_{j>=2}t_j||grad phi_j||_2^2`. Then exactly

```
C1(a+B_raw)-integral (|phi_1|^2+sum t_j|phi_j|^2)^2 = 4E/Mc^2.
```

The total kinetic energy tends to infinity at a finite maximal H1 endpoint:
a bounded subsequence would provide uniform local continuation intervals and
extend the solution past the endpoint. The crude inequality in the note shows
`B_raw<=C(E+a)`, hence `a->infinity` and `lambda=a^(-1/2)->0`.
The normalized tuples are therefore optimizing sequences. Applying the
all-optimizing-sequences theorem along an arbitrary sequence of late times
justifies eventual entry into the stability neighborhood for the whole
trajectory, rather than only one subsequence.

With the old R15 margin, the exact deficit gives

```
delta <= 8E lambda^2/Mc^2,
A_sec <= 16E/kappa,
0 <= E_scalar(u_1) <= 2E.
```

The coefficient in the intensity estimate also checks:

```
|| |u_1|^2 - lambda^(-2)Q^2((.-x(t))/lambda) ||_1
   <= 2sqrt(Mc) sqrt(8KE/Mc) lambda
   = sqrt(32KE) lambda.
```

## 2. Unique terminal atom and regular density

The secondary kinetic bound and its conserved finite mass give a uniform H1
bound for `sqrt(rho_sec)` and a uniform L2 bound for `rho_sec`. Thus secondary
mass in every ball of radius r is at most `C r`, uniformly in the center and in
late time. No secondary atom can occur.

The common-phase estimate below makes the total density measures Cauchy in
the bounded-Lipschitz metric. Spatial cutoffs with gradient `O(1/R)` give
uniform tightness. The terminal measure has the same total mass. The primary
Townes approximation forces each subsequential center limit a to give an atom
`Mc delta_a`. Every remaining part has an L2 density. Uniqueness of the atomic
part forces the same point a for all subsequences, hence `x(t)->x_*`.

The local strong-density argument is sound: bounded H1 norm of the square
root, Rellich compactness into every finite local Lp in two dimensions, and
uniqueness of the measure limit give strong local L2 convergence of rho_sec.
Tightness upgrades it to global L1 convergence. Weak lower semicontinuity gives
`sqrt(f)` in H1. In fact this already yields global strong L2 convergence:

```
||sqrt(rho_sec)-sqrt(f)||_2^2 <= ||rho_sec-f||_1 ->0,
```

and interpolation with the bounded H1 norm gives strong L4 convergence of the
square roots. The subsequent full field-limit argument yields every finite Lp
for the density.

Primary-secondary products vanish in global L1 by splitting into a shrinking
ball with radius much larger than lambda and its complement. Cauchy--Schwarz
uses the uniformly vanishing secondary mass inside and vanishing primary mass
outside. This validates the rank-one singular part of the local occupation
matrix, including after a fixed unitary change back to the original basis.

## 3. The full secondary field limit

The added argument strengthens subsequential compactness to full convergence.
Set `I=integral |u_1|^2 rho_sec` and `F_sec=integral rho_sec^2`. Energy gives

```
I = 2E_scalar(u_1)+A_sec-F_sec/2-2E <= 2E+A_sec.
```

For every secondary component,

```
integral |u_1|^2 |u_j| <= sqrt(Mc I),
integral rho_sec |u_j| <= ||rho_sec||_2 ||u_j||_2.
```

Consequently the nonlinearity in its equation is uniformly bounded in L1.
Since `L1(R2)` embeds continuously in `H^{-s}(R2)` for `s>1`, and the
Laplacian term is bounded in H^{-1}, the time derivative of each secondary
field is uniformly bounded in H^{-s}. Each field has a unique terminal limit
in that weak Sobolev space.

Uniform H1 bounds and tightness make the secondary fields precompact in
global L2. Every L2 subsequential limit has the same H^{-s} limit, so the full
trajectory converges strongly in L2. Interpolation gives strong H^sigma for
every `0<=sigma<1`. In two dimensions this gives strong Lq for every finite
q>=2 and therefore strong Lp convergence of the secondary density for every
finite p>=1. The background retains its entire conserved finite Gram matrix.
There is no claim of strong H1 convergence; bounded kinetic energy can still
have a defect in that stronger topology.

## 4. Phase-current normalization

At the fixed-spectrum endpoint every common spatial phase preserves the
Gram matrix and nonnegative energy. With
`J=Im sum conjugate(u_j) grad u_j`, the exact energy polynomial is

```
E(exp(i s theta)U)
 = E+s integral J.grad theta+(s^2/2) integral rho |grad theta|^2.
```

The discriminant gives

```
|integral J.grad theta|^2 <= 2E integral rho |grad theta|^2.
```

The continuity equation is `partial_t rho+2 div J=0`, with this definition
of J. Thus for `Y=integral rho|grad theta|^2`,

```
2 integral J.grad theta <= sqrt(8E Y) <= Y/2+4E.
```

Both factors of two are necessary; they agree with the constants in the note.
The use of a common phase is essential. An independently phased component
would generally destroy Gram orthogonality.

## 5. Transport without finite individual second moments

For equal finite-mass measures and `c(x,y)=|x-y|^2/(2h)`, the dual orientation is
correct:

```
inf_pi integral c d pi
 = sup_{psi bounded Lipschitz}
     [ integral Q_h psi d nu - integral psi d mu ],
Q_h psi(y)=inf_x[psi(x)+c(x,y)].
```

Indeed `Q_h psi(y)-psi(x)<=c(x,y)`. For the reverse inequality, truncate
`c_N=min(c,N)`. This is bounded continuous and globally Lipschitz in each
variable. Taking its c-transforms makes bounded Lipschitz dual potentials
sufficient. Since the full-cost transform is at least the truncated-cost
transform, the full-cost bounded-test supremum dominates every truncated
optimal cost.

For completeness, the passage from truncated costs to the full cost is valid:
optimal truncated couplings lie in the tight, weakly compact set of couplings
with fixed marginals. For any fixed K, their limiting coupling has
`integral c_K` at most the limiting truncated optimum; monotone convergence
in K then proves the assertion, even when the cost is infinite.

Hopf--Lax solutions from bounded Lipschitz data are bounded and Lipschitz in
space and time and satisfy the Hamilton--Jacobi equation almost everywhere.
Interior mollification preserves the subsolution inequality by convexity of
`|p|^2/2`. Uniform endpoint limits justify their use as tests. Combining this
with the current estimate gives

```
W(mu_t,mu_s)^2/(2(s-t)) <=4E(s-t),
W(mu_t,mu_s)^2 <=8E(s-t)^2.
```

Here W is defined for the unnormalized measures of mass M. No extra factor of
M should be inserted. Tightness of both marginals and lower semicontinuity of
the nonnegative quadratic cost then give

```
W(mu_t,Mc delta_(x_*)+f dx)^2 <=8E(T-t)^2.
```

## 6. Extracting scale and center rates

For sufficiently small fixed c0, every ball of radius `c0 lambda(t)` contains
at most Mc/2 of the instantaneous total measure. This follows from the
bounded maximum of Q, the global intensity error `O(lambda)`, and the uniform
secondary ball bound. Every coupling to the terminal measure must send mass
Mc to its atom at x_*. At least Mc/2 must travel distance at least c0 lambda.
Thus the cost is bounded below by `Mc c0^2 lambda^2/2`, proving
`lambda<=C(T-t)`.

The center-rate argument also checks: the transport bound forces at least
3Mc/4 of the source mass inside a fixed multiple of `(T-t)` around x_*.
Secondary mass in that shrinking ball tends to zero. A fixed multiple of
lambda around x(t) contains more than 3Mc/4 of the primary mass. The two
balls must intersect because their primary masses sum to more than Mc. Hence
`|x(t)-x_*|<=C(T-t)`.

## 7. Extension to the new R16 occupation class

The independently audited R16 inequality permits `epsilon=max_{j>=2}t_j`
to be sufficiently small with unrestricted finite `sum t_j`. Every argument
above still works. In the crude optimizing-sequence step use `3 epsilon`
in place of the old total-secondary-occupation parameter. The new normalized
deficit has margin

```
C1(1+B)-F >= delta/2+C1 B/32.
```

The additional global deficit proof, independently checked in
[occupation-gap-details.md](occupation-gap-details.md), supplies this margin for every normalized
family, after shrinking the stability entry of epsilon0 to
`delta0/(8C1)`. Thus the energy decomposition holds at all times:

```
E(U) >= E_scalar(u_1)/2 + A_sec/64.
```

Consequently the useful absolute estimates become

```
A_sec <=64E,
E_scalar(u_1)<=2E,
integral rho_sec^2 <=6 epsilon A_sec <=384 epsilon E.
```

These are all-time estimates, not only asymptotic ones. Their constants are
independent of the number and total
mass of secondary modes. The conserved total mass M remains finite and enters
the bounded-Lipschitz tightness estimate as expected. This extension does not
alter the transport coefficient 8E or the qualitative conclusions.

## 8. Final full-trajectory decomposition

The final version also states, in the original component coordinates,

```
U(t)=c exp(i theta(t)) lambda(t)^(-1) Q((.-x(t))/lambda(t))+W+R(t),
||R(t)||_{H^sigma}->0 for every 0<=sigma<1,
sup_{t near T}||R(t)||_{H1}<infinity.
```

This is justified by the already verified estimates, with no new modulation
regularity assumption. The physical primary remainder has L2 norm O(lambda)
and bounded H1 norm, so interpolation gives H^sigma norm
O(lambda^(1-sigma)). The secondary remainder converges strongly in H^sigma
to its unique terminal field. In the diagonal Gram basis W has first
component zero; applying the fixed inverse unitary gives `c^*W=0` almost
everywhere and `integral WW^*=Gamma-Mc cc^*`.

The constant `I_cross<=66E` in the final version follows directly from
`I_cross<=2E+A_sec` and `A_sec<=64E`. All final constants and the final
unrestricted-secondary-trace hypothesis were checked. No additional gap was
found in this update.

## Scope of this derivation

The argument uses the previously stated local H1 theory, scalar GN stability,
and certified Townes spectral input. Existence at the non-pure endpoint is
proved in the companion construction and separately audited in
[endpoint-details.md](endpoint-details.md). This dynamics argument does not settle the exact
asymptotic rate of every threshold blowup, general scattering, or
equal-occupation rank-two sharpness.

