# Independent final derivation of the intrinsic-spreading section

Target: [BNLS-Dynamics-20261007.tex](../../manuscripts/biharmonic-certificates/BNLS-Dynamics-20261007.tex), read on 2026-10-07. The requested section is currently numbered Section 1, not Section 2.

## Outcome

The stated mass-critical theorem, general-momentum defect inequality, and mass-supercritical energy-subcritical corollary are mathematically consistent with the supplied proof. No substantive gap was found in the radius bookkeeping, signs, or interval quantifiers.

Two small exposition corrections are recommended:

1. The phrase “tailGN and Jensen's inequality” must distinguish q<=1 from q>1. Jensen gives the displayed bound when q<=1. When q>1 use m^q<=M^(q-1)m. The displayed formula is correct in both cases.
2. After increasing C to C>=16M|E|, note that negative energy and the critical GN inequality give |E|<=C_N M^(4/N)K^2. This explicitly preserves the theorem's claimed dependence of C only on N,M,K.

An optional simpler cutoff description is phi(r)=integral_0^r s a(s) ds, where a is smooth, nonincreasing, one on [0,4] and zero on [8,infinity). Its Hessian eigenvalues are a(r)+ra'(r)<=1 and a(r)<=1. Thus the required smooth cutoff exists exactly as stated.

## Checks performed

- With M=||u||_2^2 and K=sup||Delta u||_2, interpolation gives ||grad u||_2<=M^(1/4)K^(1/2). The product-rule quantity H_R controls Delta(chi_R u).
- The localized critical GN estimate has mass exponent 4/N and second-derivative norm exponent 2. The localized gradient estimate has mass exponent 1/2 before its final square root in the interaction estimate.
- D^2 phi_R<=Identity bounds the fourth-order kinetic term above by 8||Delta u||_2^2, without radiality or kinetic-tail smallness. The nonlinearity contributes -2 beta N/(beta+2) times its full integral, giving 16E at beta=8/N.
- The mass identity is rho_t=2 Im(conjugate(u)Delta^2u). Tested against f, it gives exactly the two terms printed in the manuscript.
- The derivative falling on rho(y) contributes +4 D^2 Delta phi_R[j(x),j(y)] and -8 D^2 phi_R[j(x),w(y)], where w=Im(Delta u grad conjugate(u)). Splitting the Hessian gives -8P dot W, with the stated sign.
- The Hessian error is supported at pair separation >4R. Product-space Cauchy--Schwarz gives GK sqrt(B_R). The cutoff gradient bound at scale 2R gives B_R<=H_(2R)sqrt(MD_(2R))<=H_(2R)sqrt(MD_R). Thus the error is bounded by a constant times d_R^(1/4).
- The nonlinear double integral is bounded by a constant times d_R^min(4/N,1). Combining with the preceding term gives theta=min(4/N,1/4).
- Integrating I_R'<=16ME-8P dot W+errors and using both endpoint bounds gives the defect -16ME+8P dot avg W. The sign is correct. For a localized exact wave W=Mv/4 and E=v dot P/8, the defect is zero.
- The endpoint bound is uniform in every time. Therefore A,B,C do not depend on S, and all choices of c,epsilon,delta,eta,T0 work simultaneously for every S>=0.
- From avg d^theta>=epsilon and 0<=d<=1, delta=(epsilon/2)^(1/theta) gives a set of measure at least (epsilon/2)T. At every time in that set, D_(cT)>=delta M^2.
- D_(2r)<=2M m_r(a) holds for every center a simultaneously. Applying it with r=cT/2 yields the printed infimum-over-centers conclusion without a choice of measurable center.
- Uniform mass tightness modulo arbitrary centers implies sup_t D_(2R)<=2M sup_t inf_a m_R(a), so the confinement corollary follows.
- For general beta, the main expression is 2N beta E-(N beta-8)||Delta u||_2^2. The localized nonlinear mass exponent is gamma=1-beta(N-4)/8. It is positive precisely throughout the claimed energy-subcritical range, and the proof retains its sign when beta>=8/N. The excluded energy-critical endpoint is correctly excluded.

The theorem supplies a necessary dynamical behavior. It does not establish existence or nonexistence of all negative-energy zero-momentum global bounded solutions, and the manuscript states that limitation correctly.
