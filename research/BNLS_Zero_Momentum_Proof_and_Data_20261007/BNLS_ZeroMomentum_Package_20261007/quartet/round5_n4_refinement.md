# Sharpening the same four-dimensional exact profile

7 October 2026. This note sharpens the enclosure of the *same* exact Q; it does not substitute a different numerical solution.

Let Z=H²(R⁴), ||h||Z²=||Δh||₂²+||h||₂², A=Δ²+1, and F(q)=Aq−q³. The frozen q has SHA256 c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627, ||q||Z<104. The old proof enclosed an exact radial Q within .006 of q.

## 1. A mixed residual using no new floating solution

At every positive frozen mesh node r, define exact rational auxiliary jets

z=q''+3q'/r,
z'=q'''+3q''/r−3q'/r²,
z''=q³−q−3z'/r,
z'''=(3q²−1)q'−3z''/r+3z'/r².

At r=0 use z=4q'', z'=z'''=0, z''=(q³−q)/4. Interpolate these four jets by the unique septic Hermite polynomial on each original interval. The final jets vanish, so z is compactly supported; q,z belong to H². The formulas involving the differential equation merely define an auxiliary function: they do not assume q solves that equation.

Put d1=Δq−z and d2=Δz+q−q³. In distributions F(q)=Δd1+d2. Hence

||F(q)||Z* ≤ sqrt(||d1||₂²+||d2||₂²).

In four radial dimensions the squared integrals reduce to polynomial integrals:

||d1||₂²=2π²∫r(rq''+3q'−rz)² dr,
||d2||₂²=2π²∫r(rz''+3z'+rq−rq³)² dr.

The 256-bit Arb evaluation of exact rational polynomial coefficients proves

||d1||₂ < 1.921e−8,
||d2||₂ < 4.181e−8,
||F(q)||Z* < 4.601e−8.

The auxiliary z is C³ across interfaces; the distributional identity includes the derivative structure at interfaces and the compact endpoint. Every interval, including the final [32,36] cutoff interval, is integrated. No quadrature samples are used as bounds.

## 2. A sharper radial inverse from already frozen inequalities

For K=3A^−1/2 q² A^−1/2 on the real radial space, the prior exact Ritz inequalities give μ1≥5.395 and μ2>2.999. The independently rerun Arb Hilbert–Schmidt bound gives ||K||HS²<38.80. Therefore

μ3² < 38.80−5.395²−2.999² < .84².

The whole spectrum of I−K stays farther than .16 from zero. Thus

||(A−3q²)^−1||Z*rad→Zrad < 25/4.

This follows from the full-space compact-operator spectrum, not the spectrum of a finite matrix.

## 3. Newton closure and identity with the old Q

The certified cubic product bound is

||fgh||Z* ≤ (1/256)||f||Z||g||Z||h||Z.

With h=Q−q and B=(A−3q²)^−1, use

T(h)=−BF(q)+B(3qh²+h³).

For ρ=3e−7 and ||h||Z≤ρ,

||T(h)||Z ≤ (25/4)[4.601e−8+(1/256)(312+ρ)ρ²] < ρ,

Lip(T) ≤ (25/4)(1/256)(624ρ+3ρ²) < 1e−5.

The exact scalar verifier checks these inequalities with rational arithmetic. Thus a unique exact radial solution exists in this ball. The same T has Lipschitz constant below one throughout the old ball of radius .006. Both the old certified Q and the refined fixed point lie in that ball and solve the same equation, so they coincide.

Consequently the actual improved enclosure is

||Q−q||Z < 3e−7,

and the coefficient-one potential transfer becomes

||A^−1/2(Q²−q²)A^−1/2||
 ≤ (1/256)(208ρ+ρ²)
 =6240000009/25600000000000000
 <2.438e−7.

For coefficient three multiply this bound by three. This substantially reduces the profile-transfer term in non-self-adjoint spectral certification, while leaving every prior frozen input and every prior theorem intact.

## 4. Reproduction

Run round5_n4_mixed_residual.py, then round5_n4_refinement_certificate.py. The former imports only exact frozen-profile parsing and polynomial routines plus python-flint; it needs no numerical BVP. The latter uses the prior radial Ritz inequalities, the Arb radial HS output, and the new residual output. The analytic steps connecting these certificates are given above.
