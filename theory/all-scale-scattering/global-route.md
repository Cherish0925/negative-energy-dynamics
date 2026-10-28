# Exact deletion of a radial occupied state

Date: 2026-10-15. This calculation addresses compact, overlapping common-density states. It does not establish the two-dimensional sharp Lieb–Thirring inequality. The positive remainder below is proved directly; its virial sign is not proved. The numerical branch calculations test that sign and falsify two stronger pointwise shortcuts at floating-point accuracy.

## 1. Setting and transformed orbitals

Let smooth real radial profiles, exponentially decaying with their derivatives, satisfy

    -u_i''-(1/r)u_i'-rho u_i=-e_i u_i,
    rho=sum_i u_i^2,
    e_1>e_j>0 for j>=2,
    u_1=w>0.

All integrals below use planar measure 2 pi r dr. Distinct frequencies imply orthogonality by self-adjointness; equal frequencies cannot have independent regular radial solutions. No equality of the component masses is required for the deletion identity.

Put

    g=w'/w,
    a_j=sqrt(e_1-e_j),
    v_j=(u_j'-g u_j)/a_j,  j>=2,
    S=sum_(j>=2) v_j^2.

The first-order operator D=partial_r-g acts on L2(r dr), with adjoint D*=-partial_r-1/r-g. Its factorizations are

    D*D=-partial_r^2-(1/r)partial_r-rho+e_1,
    DD*=-partial_r^2-(1/r)partial_r+U+e_1,
    U=1/r^2+2g/r+2g^2+rho-2e_1.

Consequently

    (-partial_r^2-(1/r)partial_r+U)v_j=-e_j v_j,
    int v_i v_j=int u_i u_j  for i,j>=2.                 (1)

The second assertion follows by applying D*D to u_j. The transformed profiles are O(r) at the origin and exponentially decaying at infinity. Their radial extensions are in H1(R2), even though they need not be smooth functions of Cartesian coordinates at zero. The singular partner potential has leading term 1/r^2; v_j=O(r) is the regular admissible boundary behavior.

## 2. A positive self-consistent remainder

Use the component first integral from R23,

    G_1=w'^2-e_1 w^2+(1/2)w^2 rho
        +(1/2)sum_(j>=2)(w u_j'-w' u_j)^2/(e_1-e_j).

Its derivative is

    G_1'=-(w^2/r)(2g^2+S).

Define

    W=1/r^2+2g/r+2G_1/w^2.

Since 2G_1/w^2=2g^2-2e_1+rho+S, this gives U=W-S. Direct differentiation, using

    g'=e_1-rho-g^2-g/r,

then yields

    W'+(2g+1/r)W=-(rho+S)/r-1/r^3,
    (r w^2 W)'=-w^2(rho+S+1/r^2).                     (2)

Exponential decay gives r w^2 W -> 0 at infinity. Integrating (2) proves the exact formula

    W(r) = 1/[r w(r)^2]
           int_r^infinity w(s)^2 [rho(s)+S(s)+1/s^2] ds > 0.    (3)

Thus deletion of the lowest radial bound state preserves the masses and orthogonality of the other orbitals and produces

    -Delta_rad v_j + W v_j - S v_j = -e_j v_j,          (4)

with an explicitly positive external potential W. This holds for fully overlapping states; no dilute-core limit or small amplitude assumption enters.

At the origin W=1/r^2-e_1+O(r^2). At infinity W=O(r^-3) plus exponentially small terms. These behaviors justify all integrations below: in particular r^2 W S tends to zero at both endpoints.

## 2a. Radial curvature and the one-dimensional closure

The same calculation for the cubic common-density system in dimension d uses a=d-1 and measure r^a dr. The component first integral obeys

    G_1'=-(a/r)w^2(2g^2+S),
    g'=e_1-rho-g^2-a g/r.

Set W=a/r^2+2a g/r+2G_1/w^2. Then exactly

    (r^a w^2 W)'=a r^a w^2[(a-2)/r^3-(rho+S)/r].       (10)

Consequently, for d=1 the decaying full-line or appropriate radial solution has W=0, which is the nonlinear Darboux closure of the one-dimensional cubic system. For d=2,3,

    W(r)=a/[r^a w(r)^2] int_r^infinity
            s^a w(s)^2[(2-a)/s^3+(rho(s)+S(s))/s] ds > 0. (11)

Thus (3) is the d=2 member of an exact radial identity. In d=3 the term involving 2-a vanishes but the density term is positive. These assertions require existence and exponential decay of the stated profiles, positivity of the first component, and strict frequency separation as above. They concern the radial scalar differential operators and do not imply a nonradial spectral transformation. The two-dimensional virial issue (7) remains untouched by (10).

## 3. Exact remaining scalar quantity for a radial induction

For (4), mass-preserving scaling in two dimensions gives

    T_v-(1/2)int S^2 = (1/2) int r W'(r) S(r),          (5)
    T_v=sum_(j>=2) int |grad v_j|^2.

Suppose the original family has equal masses beta, and the sharp rank-(N-1) orthonormal inequality is known. By (1), v_j/sqrt(beta) is an orthonormal family, so

    T_v-(1/2)int S^2 >= (1-beta/M_c) T_v.               (6)

Hence proving

    int r W' S <= 0                                   (7)

for these exact self-consistent transformed families would exclude a radial equal-mass state with beta<M_c. This would be an actual induction on radial occupied rank. It would not by itself establish nonradial sharp Lieb–Thirring, and it would not cover radial projectors occupying nonzero angular sectors without additional work.

Formula (3) alone does not prove (7): a positive external potential can have a positive scaling derivative. The stronger assertion W'<=0 is false numerically even within stationary families described below. The weaker integrated sign (7) survived the computed branch, but remains unproved.

Two further exact identities are

    C=sum_(j>=2) a_j u_j v_j,
    rho'=2g rho+2C,
    S'=-2(g+1/r)S-2C,
    (rho+S)'=2g(rho-S)-2S/r.                           (8)

Integration by parts rewrites the left side of (7) as

    int r W'S = 4 pi int_0^infinity r^2 W(g S+C) dr.    (9)

Neither integrand in (7) or (9) has an established sign. In particular rho>=S cannot be silently imposed: it fails numerically on the stationary branch below.

## 4. Computing actual compact stationary profiles

A radial two-component branch was constructed by starting at the scalar one-node solution

    -Delta q+q-q^3=0,
    q(0)=3.3319892669865383 approximately.

The radial operator -Delta-q^2 has a ground eigenvalue approximately -1.8617, below the occupied scalar one-node level -1. A finite-volume tridiagonal eigenproblem supplies an initial ground eigenfunction. Boundary-value continuation then solves the full coupled equations with e_2=1, prescribed u_1(0)=A, and unknown e_1.

The final equations use scipy.solve_bvp, radial singular terms supplied explicitly, tolerance 1e-7, outer radius 25, and Bessel-K Robin conditions. These are floating-point approximations, not interval-certified existence proofs. The outer boundary error for the e_2=1 component is exponentially small; no theorem about a whole branch follows from numerical convergence.

Selected computed values:

| A | e_1 | mass u_1 | mass u_2 | max W' on tested interior | min(rho-S) | int r W'S |
|---|---:|---:|---:|---:|---:|---:|
| 0.1 | 1.862429159 | 0.011911353 | 77.150699461 | +0.664406 | -3.895876 | -137.801957 |
| 1.0 | 1.942025304 | 1.144685478 | 74.997303837 | +0.586748 | -3.776744 | -130.055348 |
| 4.0 | 4.063163479 | 9.135990325 | 54.376951712 | -0.0000732 | -2.480936 | -67.689423 |
| 10.0 | 20.869635808 | 11.472138393 | 37.295714636 | -0.0015160 | -1.335160 | -30.818137 |

The 'max' and 'min' columns use 0.03<r<15 and w>1e-8, avoiding endpoint cancellation. For A=0.1,1,4,10, evaluating (5) independently via

    v'=-(g+1/r)v-sqrt(e_1-e_2)u_2

agrees with the W' integral to within 4.3e-7. The transformed mass agrees with the original second mass to within 3.5e-7. The mass integrals omit the interval [0,1e-4]; the leading omitted original mass is pi u_i(0)^2 1e-8, which explains the largest apparent component-virial error at A=10. No inference about equal masses is made: the displayed branch has highly unequal masses and is not a candidate optimizer for the target inequality.

These calculations have a specific analytic use: they remove W'<=0 and rho>=S as viable general lemmas, while retaining the strictly weaker weighted integral (7) as the relevant unproved statement. Numerical negativity of (7) is not a proof of the desired induction.

## 5. Files and status

- r24_radial_branch.py: scalar excited profile, eigenfunction initialization, coupled stationary continuation, and transformed quantities.
- r24_radial_branch.json: all sixteen successful continuation points.
- r24_radial_branch_checks.json: independent mass/virial evaluations at four points.
- r24_radial_branch_amp*.npz: computed profiles, frequencies, and transformed functions.

The initial unrelated direct Gaussian seeds in r24_radial_stationary_probe.py all failed to converge and furnish no exclusion result. They should not be counted as research progress or successful stationary profiles.

The analytical result is (1)-(4), including the positive integral remainder for compact radial self-consistent families. It is stronger than the previous single-Townes partner identity in its class of potentials, but does not finish the integrated sign (7) or establish a global sharp constant. Historical priority for this specific deletion formula has not been investigated in this note.
