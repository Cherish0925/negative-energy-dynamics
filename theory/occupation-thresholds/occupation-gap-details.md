# R16 Proof details: a separated top occupation, without a trace restriction

Date: 2026-10-09.

## Conclusion

The replacement of the R15 assumption `sum_{j>=2} t_j small` by
`sup_{j>=2} t_j small` is mathematically valid. It gives a genuinely larger
class of occupation spectra: the sum of the secondary occupations can be
arbitrarily large. This audit checks the complete nonlinear inequality, rather
than a formal variation around the Townes state.

The theorem still concerns sufficiently separated first and second occupation
numbers; it does not include two equal occupations. The final numerical value
of the allowed occupation ratio is not yet explicit because the scalar
Gagliardo--Nirenberg stability constants remain nonnumerical.

## 1. Normalization and elementary operator estimate

Let `q=Q/sqrt(Mc)`, `C1=2/Mc`, and let `{phi_j}` be orthonormal in
`H1(R2)`. Normalize the largest occupation to one and the first kinetic
energy to one. Set

```
S = sum_{j>=2} t_j |phi_j|^2,
B = sum_{j>=2} t_j ||grad phi_j||_2^2,
epsilon = sup_{j>=2} t_j,
delta = C1 - integral |phi_1|^4.
```

For every positive density operator `0<=gamma<=epsilon I`, a Fourier cutoff
at kinetic energy `E` has low-frequency density at most
`epsilon E/(4 pi)`. The Hilbert-space triangle inequality at each spatial
point therefore gives

```
rho_{>E}(x) >= (sqrt(rho(x))-sqrt(epsilon E/(4 pi)))_+^2.
```

Integrating first in `E` and then in `x` yields

```
Tr(-Delta gamma) >= (2 pi/(3 epsilon)) integral rho_gamma^2.
```

The coefficient follows from `integral_0^1 (1-sqrt(s))^2 ds=1/6`.
Consequently

```
integral S^2 <= (3/(2 pi)) epsilon B <= 3 C1 epsilon B,
```

where the last comparison uses the strict classical bound `Mc<4 pi`.
This argument requires no bound on `Tr(gamma)`. For the trace-class statement
of the theorem, all terms follow directly by spectral truncation and monotone
convergence. The estimate is a standard elementary proof of a nonsharp
Lieb--Thirring inequality, not a newly claimed sharp constant.

## 2. Any counterexample is forced close to the scalar orbit

Suppose

```
integral (|phi_1|^2+S)^2 > C1(1+B).
```

Cauchy--Schwarz and the preceding operator bound imply

```
delta/C1 < 2 sqrt(3 epsilon B) - (1-3 epsilon) B,
B < 12 epsilon/(1-3 epsilon)^2,
delta < 3 C1 epsilon/(1-3 epsilon).
```

Thus for `epsilon<=1/12` we have `B=O(epsilon)` and
`delta<4 C1 epsilon`. If additionally `epsilon<=delta0/(4 C1)`, R15's
normalized scalar stability estimate applies:

```
phi_1=q+eta,  ||eta||_{H1}^2 <= K delta,
```

after phase and translation adjustment. No closeness assumption is imposed on
the original initial state; closeness follows from the hypothetical violation.

## 3. The crucial weighted Bessel step

Let `alpha_j=<q,phi_j>=-<eta,phi_j>` and
`chi_j=phi_j-alpha_j q`. Since `0<=sum_{j>=2} t_j |phi_j><phi_j|<=epsilon I`,

```
sum_{j>=2} t_j |alpha_j|^2 <= epsilon ||eta||_2^2 <= epsilon K delta.
```

This is the precise point that removes the sum of secondary occupations from
the proof. Replacing each summand by a uniform estimate and then summing would
lose the improvement; Bessel's inequality must be applied before summation.

Write `h[v]=||grad v||_2^2-integral Q^2|v|^2`. The Townes equation gives
`h[q]=-1` and `h[q,chi_j]=0`. If

```
h[chi] >= kappa ||grad chi||_2^2  for chi perpendicular to q,
```

then

```
h[phi_j] >= (kappa/2) ||grad phi_j||_2^2 - (1+kappa)|alpha_j|^2.
```

For the certified `kappa>=1/4`, this gives

```
I_q := integral q^2 S <= (7 C1/16) B + (5 C1 K/8) epsilon delta.
```

The error-density term is controlled without the trace:

```
J := integral |eta|^2 S
  <= ||eta||_4^2 ||S||_2
  <= (C1 K delta/2) sqrt(3 epsilon B)
  <= 4 C1 K epsilon delta,
```

where `epsilon<=1/12` was used in the last step.

## 4. Check of the constants and closure

Pointwise Young with `s=1/14` gives

```
integral |q+eta|^2 S <= (15/14) I_q + 15 J.
```

Therefore

```
integral (|phi_1|^2+S)^2 - C1(1+B)
 <= -(1-(6795/56) C1 K epsilon) delta
    -C1(1/16-3 epsilon) B.
```

The coefficient was checked independently:
`(15/7)(5/8)+30*4 = 75/56+120 = 6795/56`.
With

```
epsilon0 = min{1/96, delta0/(8 C1), 28/(6795 C1 K)},
```

the right side is at most `-delta/2-C1 B/32`. This contradicts a positive
excess and proves the sharp scalar constant on this entire occupation class.
For nonzero secondary occupation it also proves nonattainment, since a
normalized H1 function has strictly positive kinetic energy.

### Stronger global deficit

The denominator eight in the definition above is a later strengthening of
the sufficient denominator four for the sharp-constant theorem alone. It
ensures, for EVERY normalized family, the global estimate

```
D := C1(1+B)-integral (|phi_1|^2+S)^2
   >= delta/2+C1 B/32.
```

Indeed, if this failed, the crude density estimate would imply

```
delta/2+C1[(31/32-3epsilon)B-2sqrt(3epsilon B)]<0.
```

At `epsilon<=1/96`, write `b=31/32-3epsilon>=15/16`. Then
`B<12epsilon/b^2<(64/3)epsilon` and
`delta<6C1 epsilon/b<8C1 epsilon<=delta0`.
Scalar stability therefore applies, and the bound on B is precisely enough
to retain `J<=4C1 K epsilon delta`. The refined estimate already checked
above contradicts the assumed failure. Thus the global deficit needs no
near-extremality assumption on the family.

At physical primary mass Mc this gives, at every time of an H1 solution,

```
E(U) >= E_scalar(u_1)/2 + A_sec/64.
```

The restriction to sufficiently late times is consequently unnecessary for
the secondary kinetic bound. Scalar closeness itself still follows at late
times if a blowup occurs.

## 5. Explicit homogeneous spectral gap: the anchor issue and its resolution

The spherical Poincare estimate initially applies to spherical-mean-zero
functions, not to functions satisfying `<v,Q>_{L2(R2)}=0`. These conditions
must not be identified. The following correct argument bridges them.

Suppose the certified envelope is `Q(r)^2<=C/(1+r^2)^2`, `C<8`.
Set `beta=1-C/8`. For any `v` perpendicular to Q, choose a constant `t`
so that `u=v+t Q` has zero spherical mean. The mean of Q is positive,
so this choice exists. Stereographic projection and the first nonzero sphere
eigenvalue, two, give

```
h[u] >= beta ||grad u||_2^2.
```

Since `h[Q,v]=-<Q,v>=0`, `h[Q]=-Mc`, and `||grad Q||_2^2=Mc`,

```
h[v] = h[u]+Mc |t|^2
     >= beta ||grad u||_2^2+Mc |t|^2
     >= (beta/(1+beta)) ||grad v||_2^2.
```

The final step is the weighted Hilbert-space triangle inequality. Already the
R15 envelope with `C=6` proves `kappa>=1/5`, without any new computation.
The stronger envelope `C=81/16` extracted by the R16 certificate branch gives
`beta=47/128` and hence `kappa>=47/175>1/4`, as required above.
This audit checks that implication; validation that every region satisfies
the improved envelope belongs to the certificate/code audit.

## 6. Operator and dynamical scope

For a positive trace-class operator with largest two eigenvalues
`n1>=n2` and finite kinetic energy, the conclusion is

```
n2/n1 <= epsilon0
    implies
integral rho_gamma^2 <= C1 n1 Tr(-Delta gamma).
```

There is no bound on `(Tr(gamma)-n1)/n1`, rank, or number of weak modes.
For every fixed finite occupation spectrum, the R15 dilute-mode construction
establishes sharpness, and the energy/virial argument gives the exact strict
two-sided collapse boundary `M_*(p)=Mc/p1`.

In particular, take spectrum `(1,epsilon,...,epsilon)` with N secondary
modes. Every `epsilon<=epsilon0` is covered for every finite N, while the
old trace condition fails when `N epsilon` is large. Normalizing the spectrum
makes the largest fraction `p1=1/(1+N epsilon)`, which can tend to zero.
Thus "near pure state" no longer describes the new theorem's range.

This statement does not prove equal-occupation rank-two sharpness,
classification of solutions exactly on the dynamical threshold, or an
experimentally calibrated value of epsilon0.

## 7. Novelty boundary

The constituent ingredients are classical: sharp scalar GN and its normalized
stability, spectral decomposition, Bessel's inequality, and a nonsharp
Lieb--Thirring bound. Weighted occupation-number formulations and nonlinear
spectral duality already occur in Dolbeault--Felmer--Loss--Paturel (2006);
finite-rank optimization and binding are treated by
Frank--Gontier--Lewin (2021, 2025). Their strict binding range excludes
the present `d=2, gamma=1` endpoint.

Targeted searches in both search engines on 2026-10-09 did not identify a
theorem with the exact separated-top-eigenvalue hypothesis above and no trace
restriction. This is not a proof of historical priority. The defensible claim
is the stated stronger theorem under a separated largest occupation.

