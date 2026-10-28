# A certified exact N3 standing profile

The frozen rational profile is the `q` defined in [round4_n3_mixed_exact.json](../../computations/biharmonic-certificates/verification/N3/round4_n3_mixed_exact.json), with SHA-256 `5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b`. All conclusions below concern the whole radial energy space, rather than a finite box equation.

## 1. The new certified estimate

For `Z=H²_rad(R³)` with squared norm `||Δf||₂²+||f||₂²`, let

`L+(q)=Δ²+1−(11/3)|q|^(8/3)`.

The certificate proves the preconditioned spectral gap

`dist(1, spec[(Δ²+1)^(−1/2) (11/3)|q|^(8/3) (Δ²+1)^(−1/2)]) > 0.04230627284`.

Consequently `L+(q): Z→Z*` is invertible with inverse norm less than `25`.

Combining this with the previously certified whole-space distributional residual `||Δ²q+q−|q|^(8/3)q||Z* < 1.3×10^(−7)`, the quantitative Newton argument in the round4 notes gives a unique exact real radial solution `Q` inside the closed ball `||Q−q||Z≤4×10^(−6)`. Uniqueness here means within that small radial ball. The construction does not yet assert nonradial invertibility or the existence of an N3 traveling branch.

## 2. Radial reduction and the whole-space / finite-box comparison

The unitary radial map is `y(r)=sqrt(4π) r f(r)`, from radial L²(R³) to L²(0,∞). The positive radial Laplacian becomes `H=−d²/dr²` with the Dirichlet condition at zero. Therefore `Δ²+1` becomes `H²+1`. Set `V=(11/3)|q|^(8/3)`, whose support lies in `[0,54]`.

The Birman--Schwinger operator is

`K∞=sqrt(V) (H²+1)^(−1) sqrt(V)`.

Let `HR` be the Dirichlet Laplacian on `(0,R)`, with `R=64`. Its square corresponds to Navier conditions. The comparison is between resolvents with the same potential, not between a finite-box nonlinear solution and the exact whole-space profile.

With `κ=(1+i)/sqrt(2)`, the Green kernel of `(H+i)^(−1)` is

`g∞(r,s)=sinh(κ min(r,s)) exp(−κ max(r,s))/κ`.

For `r,s∈(0,R)`, direct subtraction of the Dirichlet-box Green kernel gives

`g∞−gR = [exp(−κR)/(κ sinh(κR))] sinh(κr) sinh(κs)`.

Since `(H²+1)^(−1)=−Im(H+i)^(−1)`, and the norm of the imaginary part of a complex operator is at most its complex operator norm,

`||K∞−KR|| ≤ [2/(exp(sqrt(2)R)−1)] ∫ V(r)exp(sqrt(2)r)dr`.

Here KR is extended by zero to the half-line; both potentials vanish before the boundary. Every rational profile cell contributes an Arb enclosure of its part of the integral. The certified bound is below `6.162×10^(−31)`. It uses the actual exponentially small potential, rather than replacing it everywhere by its maximum.

## 3. Potential interpolation and exact cosine moments

On a uniform mesh with `n=65536` intervals and `h=R/n=1/1024`, let Vh be the continuous piecewise linear interpolant of the exact values of V. Since `|s|^(8/3)` is C², the standard interpolation bound applies even across zeros of q:

`||V−Vh||∞ ≤ h² ||V''||∞/8`.

Each frozen polynomial cell provides rigorous enclosures of q, q', q''. The identity

`V''=(11/3)[(8/3)(5/3)|q|^(2/3)(q')² +(8/3)|q|^(2/3)q q'']`

therefore proves `||V''||∞<3665.983` and interpolation error below `0.000437020`.

For the sine basis `e_j(r)=sqrt(2/R)sin(jπr/R)`, write `C_k=∫Vh(r)cos(kπr/R)dr`. The exact piecewise linear interpolation formula is

`C_k=(h/2) sinc²(kπ/(2n)) DCT-I(V(0),...,V(R))_k`.

The verifier computes this DCT by an explicit radix-two FFT using complex Arb balls; no floating FFT or numerical quadrature is used. All sine-basis potential entries are thus enclosed by

`<e_i,Vh e_j>=(C_|i−j|−C_(i+j))/R`.

## 4. Finite-rank approximation with no uncontrolled cross block

Let `d_j=[1+(jπ/R)^4]^(−1/2)`. For m=640 define the rigorously enclosed symmetric matrix

`B_ij=d_i d_j <e_i,Vh e_j>`.

It has the same nonzero spectrum as the positive finite-rank operator

`sqrt(Vh) Σ_(j≤m) d_j² |e_j><e_j| sqrt(Vh)`.

The remainder in the resolvent series is positive, with operator norm at most

`||Vh||∞/[1+((m+1)π/R)^4] < 0.000486654`.

This is why an uncontrolled Schur-complement cross block is absent. The truncation is made in the positive resolvent before multiplication by sqrt(Vh), not by deleting rows of the preconditioned potential operator and ignoring its off-diagonal block.

The change from V to Vh can separately be bounded using the isospectral preconditioned representation `(HR²+1)^(−1/2) V (HR²+1)^(−1/2)`. Its norm difference is at most `||V−Vh||∞`, since the free resolvent norm is at most one. Applying spectral perturbation in these isospectral representations successively is legitimate; no common eigenvectors are assumed.

## 5. Certification of the finite matrix eigensystem

SciPy proposes approximate eigenvalues Λ and an eigenvector matrix O. Their IEEE entries are then interpreted as exact rationals. Arb matrix multiplication certifies

`||O^T O−I||F < 7.820×10^(−13)`,

`||BO−OΛ||F < 3.227×10^(−14)`.

In particular O is invertible and `||O^(−1)||≤[1−||O^TO−I||]^(−1/2)`. The identity

`O^(−1)BO = Λ+O^(−1)(BO−OΛ)`

and the elementary resolvent estimate for the real diagonal matrix Λ imply that every eigenvalue of B is within `3.227×10^(−14)` of one of the stored diagonal entries. The minimum distance of these exact entries from one exceeds `0.0432299459089`.

Including the zero eigenvalue of the finite-rank operator, all successive operator and spectral errors total less than `0.0009236730598`. Thus the whole-space gap exceeds `0.0423062728491`, and in particular exceeds `1/25`.

## 6. Reproduction

Run `python3 round5_n3_radial_certificate.py` with Python, NumPy, SciPy and python-flint 0.9.0. The computation took about seven seconds in this workspace. The frozen q input is not modified. Floating eigensystem generation only supplies a witness; all spectral claims are checked by Arb. If a different BLAS produces a slightly different witness, the same final rigorous inequalities must pass.

Files: [round5_n3_radial_certificate.py](../../computations/biharmonic-certificates/verification/N3/round5_n3_radial_certificate.py), [round5_n3_radial_certificate.json](../../computations/biharmonic-certificates/verification/N3/round5_n3_radial_certificate.json), and the optional generated `round5_n3_radial_spectral_witness.npz`. The verifier can regenerate its witness and does not rely on the optional file for correctness.
