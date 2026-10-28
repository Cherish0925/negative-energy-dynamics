# Three-dimensional BNLS: certified negative dipole inverse pairing

Research proof and reproducible certificate, 7 October 2026.

Let Z=H²(R³) with norm squared ||Δf||₂²+||f||₂². Write A=Δ²+1 and
L₋(Q)=A−|Q|^(8/3). The exact real radial solution Q is the solution produced by the separate radial certificate [round5_n3_radial_certificate.py](../../computations/biharmonic-certificates/verification/N3/round5_n3_radial_certificate.py), using the canonical frozen approximation q and the bound ||Q−q||Z<4×10⁻⁶. This note proves the remaining dipole inverse and its sign, without assuming either from floating eigenvalues.

The completed conclusion is

- L₋(Q) in each degree-one spherical-harmonic channel is invertible Z→Z*, with inverse norm strictly less than 200;
- it has exactly three negative directions in each such radial channel;
- I=⟨∂₁Q,L₋(Q)⁻¹∂₁Q⟩<−1280.

The degree-one spherical-harmonic multiplicity in R³ is three. The inverse pairing here concerns one Cartesian component; radial symmetry gives the same answer for every unit direction.

## 1. Mixed response certificate

Define explicit compactly supported exact rational splines f,h, and set Z₀(x)=x₁f(|x|), H₀(x)=x₁h(|x|). The input is [round5_n3_pairing_exact.json](../../computations/biharmonic-certificates/verification/N3/round5_n3_pairing_exact.json), SHA256 `cfb526600b18373ba274a8960909ef2e10a3a5939dde1150c4d755387677635f`. The functions use the canonical q nodes, degree-five C² Hermite interpolation, an even degree-six origin cell, and vanish beyond radius54.

The reduced Laplacian is D₅f=f″+4f′/r, because Δ(x₁f)=x₁D₅f. Thus

L₋(q)Z₀−∂₁q = Δ[x₁(D₅f−h)] + x₁[D₅h+(1−|q|^(8/3))f−q′/r].

This is an identity of distributions on all of R³. C² continuity of f,h prevents a spurious Laplacian interface measure. Higher interface distributions are already accounted for by applying Δ to the L² first defect.

The square L² norm of x₁a(r) is (4π/3)∫r⁴a²dr. Consequently the two residuals are computed by integrating the squares of the nonsingular expressions

r²f″+4rf′−r²h,

r²h″+4rh′+r²f−r²|q|^(8/3)f−rq′.

The two-dimensional Cauchy–Schwarz inequality in (||φ||₂,||Δφ||₂) gives their Euclidean sum as a Z* residual bound. Integer polynomial terms are integrated exactly up to rigorous Arb rounding. The noninteger potential is expanded to degree8 on cells away from q=0, with an explicit Taylor remainder. Cells meeting zero use the direct |q|^(8/3) upper bound. The origin and compact support cutoff are included.

The 192-bit Arb verifier establishes

||Z₀||Z<808.262,

r_q:=||L₋(q)Z₀−∂₁q||Z*<0.000182258,

⟨∂₁q,Z₀⟩∈[−1323.397026287657,−1323.397026287656].

This is a whole-space residual theorem, not a sampled differential defect.

## 2. The degree-one inverse: four rigorous spectral inclusions and one global remainder

The energy-space compact positive Birman–Schwinger operator is K=A⁻¹V on Z, where V=|q|^(8/3). Equivalently use the positive L² operator V^(1/2)A⁻¹V^(1/2), which has the same nonzero eigenvalues and Hilbert–Schmidt norm. An eigenvalue μ of K corresponds to the generalized differential equation

Aφ−μ⁻¹Vφ=0.

Four exact rational mixed spline trials φ_j(x)=x₁f_j(r) are frozen in [round5_n3_pairing_bs_exact.json](../../computations/biharmonic-certificates/verification/N3/round5_n3_pairing_bs_exact.json), SHA256 `87268005abaaa0877486045ce6ee6178d358bd5aa78557fa72e783a702094db7`. Their exact rational μ_j values are the stored hexadecimal numbers, approximately

2.117776675809995,
1.228173574919057,
1.006666747520584,
0.988464630706685.

The same mixed residual calculation, now without the inhomogeneous q′/r source and with potential V/μ_j, gives

||Kφ_j−μ_jφ_j||Z/||φ_j||Z
≤ μ_j ||Aφ_j−Vφ_j/μ_j||Z*/||φ_j||Z.

The certified right sides are respectively below

3.50×10⁻⁵, 2.99×10⁻⁵, 2.38×10⁻⁵, 5.43×10⁻⁶.

The self-adjoint spectral theorem therefore puts an eigenvalue in each of the four disjoint intervals [μ_j−10⁻⁴,μ_j+10⁻⁴]. These statements require neither exact orthogonality of the trial functions nor an assumed count of eigenvalues.

The independent whole-space Green-kernel verifier [round5_n3_pairing_hs.py](../../computations/biharmonic-certificates/verification/N3/round5_n3_pairing_hs.py) gives

||K||HS²<8.171158<8.18.

Subtracting the squares of the four lower interval endpoints leaves less than0.198. Every other eigenvalue is therefore below sqrt(0.198)<0.445. This both controls the entire omitted infinite-dimensional spectrum and excludes an extra eigenvalue in any of the four intervals. In particular

dist(1,spec K)>0.006,

and exactly three eigenvalues exceed1. Hence L₋(q) has three negative directions and inverse norm below1/0.006 in this channel.

For completeness, the Green kernel in reduced L²(dr) uses ν=3/2 and κ=exp(iπ/4):

G(r,s)=−√(rs) Im[I_ν(κ min(r,s)) K_ν(κ max(r,s))].

The squared Hilbert–Schmidt integral is reduced to three cumulative integrals of real and imaginary Bessel factors, as in the earlier four-dimensional certificate. Midpoint evaluations use rigorous complex Arb Bessel functions; ODE enclosures bound the second-derivative quadrature errors over every cell. Here V=q²|q|^(2/3),

V′=(8/3)q|q|^(2/3)q′,

V″=(8/3)[(5/3)|q|^(2/3)(q′)²+q|q|^(2/3)q″],

so there is no negative power at q=0. Zero-containing balls use the interval [0,sup|q|^(2/3)]. The omitted origin segment [0,10⁻⁷] is bounded by the positive resolvent inequality (H²+1)⁻¹≤(2H)⁻¹, where H=−d²/dr²+2/r². Its HS contribution is below7.43×10⁻⁹.

The q→Q perturbation is controlled by the exact embedding ||w||∞<||w||Z/4. With ρ=4×10⁻⁶ and ||q||∞<6.3,

δV:=|| |Q|^(8/3)−|q|^(8/3) ||∞
≤(8/3)(6.3+ρ/4)^(5/3)ρ/4 <0.000057307.

Thus the energy-space spectral gap remains larger than0.006−0.000058>1/200. The exact-Q inverse and its negative index now follow.

## 3. A residual-squared identity certifies the inverse pairing

For any self-adjoint invertible L, source g and trial z, write r=g−Lz. Then

⟨g,L⁻¹g⟩=2⟨g,z⟩−⟨Lz,z⟩+⟨r,L⁻¹r⟩.

This exact identity is more effective than bounding L⁻¹g−z and then pairing with g: the inverse norm multiplies the square of the response residual.

Here ||∂₁(Q−q)||Z*≤(3/5)ρ=:δg, since sup_{s≥0}s/(1+s⁴)=3^(3/4)/4<3/5. Therefore

r_Q≤r_q+δg+δV||Z₀||Z <0.046504.

Set B=200, the inverse bound certified in Section2. The exact identity gives

I ≤ ⟨∂₁q,Z₀⟩ + r_q||Z₀||Z
     +2δg||Z₀||Z +δV||Z₀||Z²+B r_Q².

All quantities on the right are certified scalar bounds. Substitution gives I<−1280. The full Arb output records the tighter bound. In particular the sign is separated from zero by over1280; it does not rely on rounding a floating value near zero.

As a useful robustness observation, even the far weaker inverse norm B=500000 would preserve the negative sign under the same Q radius. The separate spectral proof gives B<200, so this observation is not used as an unproved hypothesis.

## 4. Reproduction and scope

Install python-flint==0.9.0, use the canonical q input and the three new verifiers in this order:

    python3 round5_n3_pairing_hs.py
    python3 round5_n3_pairing_bs_verify.py
    python3 round5_n3_pairing_verify.py

They take about one minute total on the current CPU. The numerical samplers and SciPy BVP calculations are only provenance and are not required to verify the frozen exact input. No FFT, finite-difference convergence estimate or box eigenvalue count is used in these three verifiers.

The exact-Q existence assertion also requires the separate radial certificate and previous canonical residual certificate. A full traveling-wave implicit-function theorem further requires the remaining even real and odd imaginary channels, addressed separately. This note completes the dipole inverse and negative pairing, not those other channels.
