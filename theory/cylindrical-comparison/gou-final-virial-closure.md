# Exact derivation of the cylindrical virial closure

Date: 2026-10-07. This is an independent examination of the final inference in
Gou, arXiv:2205.08167v3, Theorem 1.2. It does not assume that the present
project's computer-assisted traveling-wave construction is correct.

## 1. Sources and scope

The inspected public full text is the author's v3, dated 4 November 2024:
https://arxiv.org/html/2205.08167v3 and https://arxiv.org/pdf/2205.08167v3.
The journal page confirms publication in Proceedings of the Edinburgh
Mathematical Society 67(4) (2024), 1085–1098, DOI
10.1017/S001309152400066X, online 3 October 2024. The journal PDF URL redirected
to the access-limited abstract page during this audit; the journal typeset
full text was NOT independently compared with v3. A title/DOI search did not
surface a correction, which is not proof that none exists.

Gou defines, for x=(y,z) in R^(d-1) x R,

  Sigma_d = { u in H^2 : u(y,z)=u(|y|,z), z u in L^2 },
  phi_R(y,z) = psi_R(|y|) + z^2/2,
  M_R(u) = 2 Im integral conjugate(u) grad(phi_R).grad(u).

Theorem 1.2 assumes d>=4, sigma=4/d, mu>=0, u_0 in Sigma_d and E_mu(u_0)<0.
For mu=0 it asserts finite- or infinite-time blowup, and for mu>0 finite-time
blowup. Its mu=0 proof ends after (2.29), by invoking the proof of
Boulenger–Lenzmann Theorem 3. For mu>0 the first sentence of the proof makes
the same appeal after Lemma 2.2.

The relevant BL source is https://arxiv.org/pdf/1503.01741, equation (7.15)
on PDF page 29 (printed page 29), and equations (7.3)–(7.4) for mu>0.

## 2. The precise unavailable bound

For a real bounded-gradient weight phi one has, directly by Cauchy–Schwarz,

  |M_phi(u)| <= 2 ||grad phi||_infinity ||u||_2 ||grad u||_2
             <= 2 ||grad phi||_infinity ||u||_2^(3/2) ||Delta u||_2^(1/2).

Together with mass conservation, a strictly negative uniform derivative of
M_phi forces growth of the Laplacian norm. This is BL (7.15)'s mechanism.

For Gou's weight, grad(phi_R)=(grad_y psi_R,z) is unbounded. The correct bound is

  |M_R(u)| <= 2 ||grad_y psi_R||_infinity ||u||_2 ||grad_y u||_2
              + 2 ||z u||_2 ||partial_z u||_2.                 (A)

Finite initial ||z u_0||_2 is not a time-uniform bound on ||z u(t)||_2.
Thus the transferred BL step is unavailable. The following exact test
shows that no bound depending only on R and translation-invariant H^2 data
can replace it, even within negative-energy, zero-momentum, smooth data.

## 3. One-packet algebraic test

Choose a nonzero real f in C_c^infinity(R^d), radial in y, even in z,
supported in |z|<1. Fix k!=0 and A>0. For a>1 set

  w_a(y,z) = A exp(i k z) f(y,z-a).

All translation-invariant Sobolev norms, mass, and energy are independent
of a: w_a is a translate of A exp(i k z)f, up to a constant phase. Write
m=||f||_2^2. Direct calculation, with no PDE input, gives

  P_z(w_a)= k A^2 m,
  M_R(w_a)=2 k a A^2 m,
  ||z w_a||_2^2=A^2(||z f||_2^2+a^2 m).

The transverse current is zero because the amplitude is real and the
phase depends only on z. The odd first moment of |f|^2 vanishes.

For any fixed mu>=0 and exponent 2sigma+2>2,

  E_mu(w_a)= (A^2/2) K_mu(k,f)
            - A^(2sigma+2)/(2sigma+2) ||f||_(2sigma+2)^(2sigma+2),
  K_mu(k,f)=||Delta(exp(i k z)f)||_2^2
            +mu||grad(exp(i k z)f)||_2^2.

K_mu is finite and independent of a. Taking A sufficiently large makes
this energy strictly negative, uniformly in a. Hence the virial is
unbounded above and below (choose the sign of k), while mass, energy and
H^2 norms are fixed and every w_a has finite spatial variance.

## 4. Exact zero-momentum test

For a>1 the two supports below are disjoint. Put

  u_a(y,z)=A[exp(i k z)f(y,z-a)+exp(-i k z)f(y,z+a)].

Then u_a is smooth, cylindrically symmetric and even in z. Disjointness
removes all cross terms in mass, energy, Sobolev norms and momentum.
The two packets have opposite momenta and equal energies. Therefore

  P(u_a)=0,
  M(u_a)=2 A^2 m,
  E_mu(u_a)=2 E_mu(w_a)<0,
  ||u_a||_(H^2)^2=2||w_0||_(H^2)^2,
  M_R(u_a)=4 k a A^2 m,
  ||z u_a||_2^2=2A^2(||z f||_2^2+a^2m).

In particular, choosing k<0 sends M_R(u_a) to minus infinity while all
unweighted quantities in a putative BL-type lower bound stay fixed.
Zero momentum does not repair the missing estimate.

These u_a are STATIC TEST FUNCTIONS. No claim is made that a prescribed
time-dependent substitution a=a(t) solves BNLS. Consequently these tests
disprove the required functional estimate, but do NOT by themselves
disprove the theorem's dynamical conclusion.

## 5. Why retaining the moment does not close the original argument

Even accepting Gou's differential inequalities, a bound M_R'(t)<=-c<0
is consistent with bounded H^2 and linearly growing ||z u(t)||_2 in (A).
The scalar bounds M_R(t)=-ct, ||grad u(t)||_2=constant and
||z u(t)||_2 proportional to 1+t have no contradiction.

For a genuine traveling wave W(y,z-vt), if W has a finite first moment,
one has the exact identities

  M_R(e^(i omega t) W(y,z-vt))=M_R(W)+2vt P_z(W),
  ||z W(y,z-vt)||_2^2=||zW||_2^2+2vt integral z|W|^2
                     +v^2t^2 M(W).

In the pure mass-critical equation its profile scaling identity is
E(W)=vP_z(W)/8, so the virial slope would be 16E(W)<0 with constant H^2.
This is an exact consistency check CONDITIONAL ON SUCH A PROFILE EXISTING.
Its existence is precisely what must be certified separately.

## 6. A genuine limited repair

Assume enough regularity for the cylindrical virial identity and finite
axial moments at each finite time. If a global negative-energy solution
has uniformly bounded H^2, Gou's Lemma 2.2 (with the axial lower-order
error retained in its O(R^-2 ||grad u||_2^2) term) permits one fixed large
R for which M_R'(t)<=-c<0. Inequality (A) then implies

  ||z u(t)||_2 >= c_1 t-c_2

for suitable positive constants. Thus the method gives axial escape
under bounded H^2, not a contradiction. Adding an assumption of uniform
axial-moment boundedness would instead rule out uniformly bounded global
H^2 dynamics. For mu>0, such a uniform moment bound also restores the
bounded prefactor needed by the BL Riccati argument.

This repair changes the hypotheses or the conclusion. It is not a proof
of Theorem 1.2 as stated. Additional H^2-to-weighted-space propagation
issues are deliberately not used in this audit: the decisive tests are
smooth and the potential traveling waves have ample weighted regularity.

## 7. Lower-order transcription issue, not the decisive conclusion

Immediately after (2.10), the term involving Delta^2 psi_R is reduced to
transverse indices. With the standard operator-composition convention,

  sum_{j=1}^d <u,partial_j[(Delta_y^2 psi_R)partial_j u]>
    = - integral (Delta_y^2 psi_R)|grad u|^2,

which contains the axial contribution

  - integral (Delta_y^2 psi_R)|partial_z u|^2.

The corresponding factor-2 term is absent from (2.21). It is bounded in
absolute value by C R^-2 ||partial_z u||_2^2 and can be retained as an
error. No assertion is made here that the displayed (2.21) upper bound
cannot be salvaged using other negative terms. This issue is secondary
and is not the basis of the conclusion in Sections 2–6.

## 8. Verdict available from this derivation alone

The bounded-gradient closure imported from BL is invalid for the
cylindrical multiplier. There is an exact elementary obstruction, even
for smooth zero-momentum negative-energy finite-variance data. Therefore
the publicly inspected proof does not establish the claimed theorem by
its cited argument. Whether the theorem itself is false is a separate
existence question. The project's negative-energy traveling-wave
certificate, if correct, supplies that stronger conclusion; this audit
does not assume or replace verification of that certificate.
