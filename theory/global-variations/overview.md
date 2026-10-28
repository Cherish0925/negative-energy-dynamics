# Two-dimensional sharp Lieb–Thirring research

16 October 2026.

The target remains F(P) <= (2/M_c) T(P) for every finite orthogonal
projection on R², where F=int rho_P² and M_c is the Townes mass.
This attempt does not prove the target, construct a violating projection,
or improve the unrestricted two-dimensional constant.

## Positive estimate obtained in this attempt

[slice-compatibility.md](slice-compatibility.md) proves

    T >= pi³/(4 sqrt(2)) F = 5.481187124996578 F

for all finite orthonormal families phi_i(x,y)=a_i(x)b_i(y), with b_i an
arbitrary orthonormal H1(R) family and

    a_i²=(lambda_i/pi) sech(lambda_i(x-x_i)), lambda_i>0.

Ranks, centers, scales, and transverse overlaps are unrestricted within
this class. These are exact saturation examples for the first, Hilbert-valued
one-dimensional step of the existing lifting proof. The estimate follows
from a weighted Holder consequence of Read–Schulz's one-dimensional sharp
inequality and exact scalar soliton integrals. Historical novelty is not
claimed for this consequence.

The class-specific coefficient exceeds the lifted coefficient
sqrt(3) pi=5.441398092702653 by 0.03978903229392472. It is still smaller
than the target M_c/2, approximately 5.85044825. More importantly, it has
not been extended to arbitrary planar orthonormal families. Therefore
this is neither a new unrestricted bound nor a solution of the conjecture.

The same note retains a quantitative matrix remainder and its precise
alpha-to-pi endpoint correction. A near-equality extension must use the
joint two-direction deficits, or a weaker one-sided energy/density
comparison. Small first-direction deficit alone does not imply full H1
proximity to product channels; the final section gives a rank-one example.

## Other attempted routes

[collective.md](collective.md), [global-competitor.md](global-competitor.md), [flow.md](flow.md), and
[rank-global.md](rank-global.md) record the finite collective variation, merger,
diffusion, and rank-changing calculations. None excludes a smallest-rank
violating optimizer. They are retained as unsuccessful calculations,
not counted as further sharp-constant results. Earlier R26 finite-angle
formulas and published finite-rank reductions remain attributed to their
original sources.

## Exploratory check of a proposed auxiliary inequality

The stronger proposed weighted one-dimensional estimate

    3 [int (sum c_i |b_i|²)²]² <= (sum c_i⁴) sum ||b_i'||²

is NOT used in the proof. [r27_weighted1d_probe.py](../../computations/global-variations/r27_weighted1d_probe.py) searches this separate
statement in a Hermite basis, retaining exact Gram normalization and the
complete derivative of the polar map. Its JSON and NPZ files are
exploratory floating-point outputs. For rank 2, cutoff 36, seed 53, the
left/right quotient is 1.0001008498358952. A direct physical-space Simpson
integration on [-24,24] with 24001 points gives 1.0001008498359163 and
Gram error 8.45e-16. These calculations indicate failure of that auxiliary
estimate but are not an interval certificate. They are not a counterexample
to the original planar conjecture. The proved class estimate above uses
the rigorously derived coefficient 2/pi instead.

The unrestricted sharp problem remains unresolved in this work.
