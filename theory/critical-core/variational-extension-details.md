# Proof details of the R17 one-dimensional extension

Date: 2026-10-09.
Scope: [variational-extension.md](variational-extension.md), including its explicit spectral gap,
local all-state remainder, concavity propagation and threshold scaling.

The deductions below use the Read--Schulz theorem as an external input.

1. **External endpoint.** The primary HTML source
   https://arxiv.org/html/2609.10478v2 was opened directly. Theorem 1 states
   the scalar-potential constant 4/(3sqrt(3)pi), and equation (1.1) states
   exactly the kinetic inequality with coefficient pi^2/4. Its inverse is
   C=4/pi^2. Fractional occupations follow from the stated finite Bernoulli
   selection plus Jensen argument; complex fields follow by scalar-potential
   spectral duality. These uses do not require the stronger matrix-valued
   theorem.

2. **Homogeneous gap.** With z=tanh(2x), the derivative form is
   D=2 integral(1-z^2)|f_z|^2 and the potential form is
   (3/2)integral|f|^2. Legendre mean zero therefore gives h>=(5/8)D.
   Shifting u=v+tQ for v perpendicular to Q gives
   h[v]>=beta D[u]+Mc|t|^2 and
   D[v]<=(1/beta+1/2)(beta D[u]+Mc|t|^2), because D[Q]=Mc/2.
   The resulting beta/(1+beta/2)=10/21 is correct. The Q-orthogonality and
   Legendre mean are not conflated.

3. **Secondary density.** The Fourier projector has diagonal sqrt(E)/pi.
   The layer-cake integral is integral_0^1(1-z^(1/4))^2 dz=1/15, yielding
   integral S^3<=15 epsilon^2 B/pi^2. The low/high frequency vector bounds
   sqrt(epsilon R/pi) and sqrt(B/(pi R)) yield
   ||S||_infinity<=4sqrt(epsilon B)/pi. These constants are correct for
   arbitrary orthonormal families and do not depend on their total trace.

4. **Projection and nonlinear constants.** The weakened kappa=1/4 gap,
   D[q]=1/2 and h[q]=-1 give
   h[phi]>=D[phi]/8-(9/8)|<q,phi>|^2. Therefore the potential coefficient
   9/8 and the leading kinetic coefficient7/8 in the note are correct.
   The convex fourth-power bound uses (65/64)^3<=15/14 and 65^3. The
   accumulated scalar-deficit coefficient is
   135/112+12*65^3=3295501+23/112<3295502.

5. **All-state contradiction.** Write L=3(1/2)^(2/3)(15/4)^(1/3), so
   L^3=405/16. With beta>1/2, the alleged remainder failure implies
   B<(L/beta)^(3/2)epsilon<sqrt(405/2)epsilon<16epsilon.
   Maximizing L epsilon^(2/3)B^(1/3)-beta B gives
   delta<sqrt(15/beta) C epsilon<sqrt(30) C epsilon<6Cepsilon.
   Thus both uses of scalar stability and Kdelta<=1 are valid with the
   declared reduced delta_0. The final absorption yields exactly
   D>=delta/2+CB/32.

6. **Interpolation.** For fixed S and nonnegative a,
   t -> C(a_1+tB)-integral(a+tS)^3 is concave. Interpolating the positive
   remainder at t_0 and the inherited nonnegative endpoint at1 gives the
   two displayed positive coefficients for every epsilon<1. This extends
   the remainder range, while the sharp endpoint remains inherited.

7. **Physical normalization.** Multiplication of the normalized quintic
   functional deficit by Mc^3/6 produces E(U). The secondary term CB/32
   becomes A_secondary(U)/64. The scaled primary error has squared H1
   size O(lambda^2), so the displayed O(lambda) norm error is correct.
   No exact blowup rate or fixed-background convergence is needed for that
   conclusion, and neither is imported into the note.

No correction was required in the reviewed mathematical statements. The
unknown scalar-stability constants K and delta_0 prevent a certified
numerical occupation interval; the note states that limitation explicitly.
The published one-dimensional endpoint input is clearly credited and is
not counted as a newly proved conjecture of this project.
