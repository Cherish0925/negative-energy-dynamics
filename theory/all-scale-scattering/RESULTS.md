# A compact equal-occupation shell and its relative-scale descent

2026-10-15. This is a numerical stationary-state construction with an exact
variation formula. It is not a proof of existence by interval methods, a
classification theorem, or a solution of the sharp two-dimensional inequality.

## Model and construction

For -Delta u_j-rho u_j=-e_j u_j, rho=sum u_j^2, take

    u_0=f(r), u_1=g(r) cos(theta), u_2=g(r) sin(theta).

The density f^2+g^2 is radial, but the occupied family is not a family of radial
functions. The equations are

    -f''-f'/r-(f^2+g^2)f=-f,
    -g''-g'/r+g/r^2-(f^2+g^2)g=-e g.

We impose 2 pi int r f^2 = pi int r g^2 = beta. Angular integration enforces
all off-diagonal Gram constraints exactly. The variable g=r v removes the
origin singularity. A cumulative mass-difference variable enforces equality
of occupations. At the outer boundary use the free K_0 and K_1 logarithmic
derivatives. These are exponentially accurate approximations, not exact
infinite-domain boundary conditions.

At R=35, tolerance 1e-7, three different initial widths converged to the same
nonzero branch. A fourth initialization failed and is retained in the logs.
At R=65, tolerance 2e-10, the computed parameters are

    e = 0.06222748425517942
    beta_0 = 12.80583924019625
    beta_1 = beta_2 = 12.805839240091066
    f(0) = 1.8713165821156565
    max |g| approximately 0.57629724
    T = 14.399589559378649
    F = 28.799179119578184.

The largest collocation residual reported by solve_bvp is 2.0e-10.
The R=35 and R=65 occupations differ by approximately 1.23e-7. Quadratures
use 20001 radial samples. The identity F=2T holds to approximately 8.2e-10.
These checks do not enclose the error to an exact whole-plane solution.

Since beta exceeds M_c approximately 11.7008965, this branch does not violate
the target inequality. Normalizing each component to mass one gives the
quotient F/(beta T) approximately 0.15618, below 2/M_c approximately 0.17093.
The branch is compact rather than the escaping diffuse component found by
the earlier radial maximizations.

## An explicit variation, rather than only a matrix eigenvector

For any exact decaying solution of this shell ansatz define

    f_s(r)=exp(s) f(exp(s) r), g_t(r)=exp(t) g(exp(t) r).

Both occupations and every Gram constraint are preserved for all s,t.
Write E=T-F/2 and Lambda h=h+r h'. Common scaling gives
E(s+a,t+a)=exp(2a) E(s,t). At a stationary critical profile E=0 and its first
derivatives vanish. Consequently the two-by-two Hessian annihilates (1,1).
The only mixed contribution is -int f_s^2 g_t^2, so

    partial_s partial_t E(0,0) = -4 I,
    I = 2 pi int_0^infinity r f Lambda(f) g Lambda(g) dr.

It follows exactly that

    E(s,t) = 2 I (s-t)^2 + o(s^2+t^2).

Thus I<0 for an exact profile would prove it is not a constrained local energy
minimum, and equivalently not a local maximum of the density/kinetic quotient.
This is an energetic statement; no dynamical instability theorem is asserted.

For the computed branch,

    I approximately -0.396106094328671,
    2 I approximately -0.792212188657342.

Direct symmetric differences of the energy along f_s with g fixed give
-0.79226946, -0.79221750, -0.79221526 at steps 1e-2, 3e-3, 1e-3.
They agree with the sign and size of the exact formula. Because the profile
is numerical, this is not an interval-certified instability of an exact state.

## Full constrained quadratic calculation

For real perturbations satisfying int(u_i h_j+u_j h_i)=0, the quadratic form is

    Q(h)=sum_i int [|grad h_i|^2+(e_i-rho)h_i^2]
         -2 int (sum_i u_i h_i)^2.

The supplied script evaluates this in angular Fourier modes through m=3 and
radial Laguerre polynomials with scale 2. It projects out all six linear Gram
constraints, not just the three individual mass constraints. The three lowest
matrix eigenvalues at radial degrees 18, 30, 45, 60 are approximately

    18: -0.223362, -0.205661, -0.205661
    30: -0.248367, -0.209172, -0.209172
    45: -0.251172, -0.209571, -0.209571
    60: -0.251403, -0.209603, -0.209603.

Near-zero modes decrease with increasing basis size. Negative eigenvalues are
not a count of the entire continuum negative spectrum: angular modes beyond
the cutoff and numerical errors have not been exhaustively controlled.

Individual kinetic integrals are T_0 approximately 8.52131 and
T_1=T_2 approximately 2.93914. In particular the earlier identity T_i=e_i M_i
for entirely radial components does NOT apply to these angular components.

## Scope and next unresolved mathematical step

This calculation demonstrates a concrete failure of a proposed optimizer:
equal occupation and common localization alone do not imply optimality;
relative concentration supplies an admissible energy-lowering direction here.
It does not establish a negative relative-scale direction for every shell,
every nonradial stationary state, or every rank. For general nonradial
families, independent scaling also changes off-diagonal Gram entries and
requires additional corrections. No universal sign has been derived.

The all-scale sign of the earlier distant-well scattering coefficient also
remains unproved; the positive radial partner alone does not compare its
negative radial amplitude with all positive angular amplitudes.

Prior context: Frank, Gontier, Lewin, arXiv:2002.04964; Levitt, J. Spectr.
Theory 4 (2014), 153-175. Multicomponent solitary waves and constrained
second variations are established subjects. The results here must not be
described as the first construction or the resolution of a historical problem.

## Reproduction

With Python, NumPy and SciPy, run from this directory:

    python r24_shell.py
    python r24_shell_refine.py
    python r24_hessian.py

The refined run overwrites r24_shell.npz intentionally; run it before the
Hessian script. JSON files retain failed starts, converged parameters and
the basis-size comparison. Earlier R23 files have not been modified.
