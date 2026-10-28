# A finite amplitude merger of the entire occupied family

2026-10-16. This investigation tests one concrete finite-amplitude strategy
for a least-rank improving optimizer: merge the amplitudes of all occupied
modes, while retaining exact orthogonality, and optimize a complete finite
rotation using the criterion already proved in R26_finite_rank, Section 5.
The finite-rotation identity is not an R27 result. This note does not
establish a negative competitor under the target hypotheses. The calculation also determines the
sign of the simplest merge-then-fission endpoint: that endpoint has strictly
positive energy under those hypotheses, rather than negative energy.

## 1. Target and normalization

Let phi_1,...,phi_N be real orthonormal functions, with phi_1>0, satisfying

    H phi_i=-e_i phi_i,
    H=-Delta-a rho, rho=sum_i phi_i²,
    e_1>=...>=e_N>0.

Assume they occupy the lowest N eigenvalues, with a strict gap above them.
For a putative strict improvement of the scalar sharp constant,

    a=2/C_N<M_c,
    J_a(P)=T-(a/2)F=0,
    T=sum_i ||grad phi_i||², F=int rho².

Here P is the rank-N occupied projection. The equality J_a=0 follows from
mass-preserving spatial scaling at the self-consistent stationary state.
The scalar sharp inequality is int |f|^4 <= (2/M_c)||f||²||grad f||².
The question is whether a finite competitor with the same full Gram matrix
can be shown to have J_a<0.

## 2. Why the direct merger followed by equal-mass fission has the opposite sign

Set r=sqrt(rho), so ||r||²=N, and T_r=int |grad r|². The most direct merger
forms the common positive amplitude r. To restore N occupations equal to
one, take N remote, disjoint copies of r/sqrt(N). More precisely, truncate
and normalize r first, separate the compact copies, and then pass to the
H1 limit. The limiting energy is exactly

    J_fission=T_r-(a/(2N))F=T_r-T/N.

The scalar sharp inequality applied to r gives

    F <= (2N/M_c)T_r,
    T_r >= (M_c/a)T/N.

Therefore, at the putative counterexample,

    J_fission >= (M_c/a-1)T/N > 0.                  (1)

The original state has energy zero. Thus this particular finite merger and
fission raises energy by a definite amount. This is an exact implication of
the target subcritical hypothesis; it does not rely on an approximate
stationary profile or on a separated-core description of the original state.
The scalar inequality cannot be used with mass one before dividing r by
sqrt(N): doing so would erase precisely the factor that determines (1).

This does not preclude a nonmonotone path with a lower intermediate energy.
It is why the next construction retains the occupied subspace and checks
an entire finite path instead of comparing only a fission endpoint.

## 3. Exact Gram-preserving merger into the positive total amplitude

Let

    p=Pr, q=(I-P)r,
    b=||p||², m=||q||²=N-b.

Since phi_1>0 and r>=phi_1, <r,phi_1>>0 and b>0. If m=0, the proposed
merger does not change the occupied space. Suppose m>0 and define

    u=p/sqrt(b), w=q/sqrt(m).

Then u is a normalized occupied function, w is a normalized unoccupied
function, and r/sqrt(N)=sqrt(b/N)u+sqrt(m/N)w. Although u generally combines
several occupied eigenfunctions, every member of Ran(P) perpendicular to u
is also perpendicular to r. Consequently

    P_merge=P-|u><u|+|r/sqrt(N)><r/sqrt(N)|           (2)

is exactly a rank-N orthogonal projection. It merges the amplitudes of all
modes into one positive orbital while preserving all remaining orthogonal
occupations. No small parameter, moment condition on phi_j/phi_1, spatial
symmetry, or approximate Gram correction is used.

The changed density is particularly simple:

    rho_merge-rho=rho/N-u².                         (3)

For any rank-N competing projection P', self-consistency gives the exact
finite identity

    J_a(P')-J_a(P)
      =Tr H(P'-P)-(a/2)||rho_(P')-rho||².             (4)

Put

    alpha=<w,Hw>-<u,Hu>.

The occupied spectral ordering gives alpha>=gap>0. Equations (2)-(4) yield

    J_a(P_merge)-J_a(P)
      =(m/N)alpha-(a/2)int(rho/N-u²)².               (5)

Thus the merger compares a positive, exactly computed spectral replacement
cost with a negative, exactly computed density gain. Neither term may be
dropped. Positivity of the first occupied eigenfunction ensures that the
construction is defined; it does not determine this comparison.

## 4. Applying the existing R26 finite-rotation criterion

For the specific pair u=Pr/||Pr|| and w=(I-P)r/||(I-P)r||, apply
research/r26_finite_rank.md, Section 5, with psi=u and chi=w. That existing
criterion tests all replacements u_theta=cos(theta)u+sin(theta)w through

    B = [ 4 int u²w²,              2 int uw(w²-u²)
          2 int uw(w²-u²),         int(w²-u²)² ].

A negative finite-angle competitor exists exactly when
(a/2)lambda_max(B)>alpha. The merger (2) is one angle in that same family,
with sin²(theta)=m/N. No new finite-angle identity or necessary condition
is claimed here; the R27 calculation is the evaluation of that existing
test on this particular total-amplitude direction.

The target hypotheses have not been shown to force the required strict
inequality. Scalar GN gives upper bounds on separate fourth moments,
whereas this test needs a lower bound on a density contrast relative to
the spectral replacement cost. Also, -<u,Hu> cannot be replaced by e_1
unless Pr is actually proportional to phi_1.

## 5. Actual test on the existing compact three-mode stationary profile

This is only a test of the proposed competitor, using the previously saved
R24 profile; it is not a new stationary-state construction or a proof about
an exact continuum solution. The input is research/r24/r24_shell.npz:

    U=(f(r),g(r)cos(theta),g(r)sin(theta)),
    beta approximately 12.8058392402 > M_c.

Normalize the three components by sqrt(beta), so a=beta. Radial symmetry
makes Pr proportional to the central mode. Thus u=f/sqrt(beta), and the
construction above is evaluated with ordinary radial quadrature. The
calculated quantities are

    <r,u> approximately 1.32927210718,
    m approximately 1.23303566507,
    <w,Hw> approximately -0.00825780514,
    alpha approximately 0.99174219486,

    B approximately
       [ 0.03186812557   0.05272815879
         0.05272815879   0.10332878124 ].

The two eigenvalues of (a/2)B are approximately

    0.02500043310, 0.84065449412.

Hence the computed finite-angle margin is

    alpha-(a/2)lambda_max(B) approximately 0.15108770074>0.

The entire real rotation family from R26, not merely the merger point, therefore
has nonnegative calculated energy difference. Direct evaluation of the
positive-amplitude merger gives a physical energy increase approximately
1.407461262, agreeing with (5) after multiplying the normalized energy by
beta. The quadrature used the stored 20001-point R24 profile; no interval
error bound is asserted here.

This state was already shown in R24 to have a different, independent-scale
negative direction. Thus the present finite merger fails to detect even
that known saddle. Its modal mass is above M_c, so this calculation is not
a counterexample to a theorem restricted to subcritical optimizing states;
it simply supplies an actual test of the chosen route rather than an
unexamined sign assumption.

## 6. Outcome

No least-rank subcritical optimizer has been excluded and no violating
orthogonal family has been constructed. The direct merge-and-fission
endpoint has the strictly positive energy (1) under the very hypotheses it
was meant to contradict. The exact rank-preserving nonlinear merger is a
legitimate finite competitor. Applying the existing R26 finite-angle test
to it has not yielded the required sign from the stationary and minimal-rank
assumptions; this application is not a new general variational criterion. This branch therefore supplies no new result
on the full sharp constant. Its formulas and the actual test are retained
to avoid repeating the same finite-merger proposal without its Gram and
spectral costs.
