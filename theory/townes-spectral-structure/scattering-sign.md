# A positive radial Darboux partner and the small-scale scattering sign

15 October 2026. Analytic research note. The identities and arguments below are independent of floating-point computations. Historical priority has not been established. This does not prove the two-dimensional Lieb–Thirring conjecture or determine the scattering sign at every scale ratio.

Let Q be the positive decaying radial solution of

    -Q'' - r^(-1) Q' + Q - Q^3 = 0,

and let h=-Delta-Q^2 on R^2. Put M=int_R2 Q^2. The previously derived unequal-well coefficient is

    A(k)=int_R2 Q^2 exp(2 k x_1)
         +<Q^2 exp(k x_1),(h+k^2)^(-1)Q^2 exp(k x_1)>.

The results here remove the previously unproved single-well spectral restriction and establish A(k)<0 for all sufficiently small positive k. Together with the previous pole calculation near k=1, both ends of (0,1) are covered. No uniform sign is obtained on its remaining compact middle.

## 1. Exact positive partner identity

Work first in the radial space L^2((0,infinity),r dr). Define q=Q'/Q and the closed first-order operator

    D=partial_r-q,     D*= -partial_r-r^(-1)-q.

With the regular/Friedrichs domains,

    D*D=h_0+1,
    DD*=h_partner+1,
    h_partner=-partial_r^2-r^(-1)partial_r+U(r),

where

    U(r)=r^(-2)+2q/r+2q^2+Q^2-2.

This expression has an exact strictly positive integral representation:

    U(r) = [r Q(r)^2]^(-1)
           int_r^infinity [Q(s)^2/s^2+Q(s)^4] ds  > 0.       (1)

To verify it, put g=r^2 U. The Riccati equation

    q'=1-Q^2-q/r-q^2

gives, by direct differentiation,

    [(Q^2/r)g]' = -Q^2/r^2-Q^4.                           (2)

The boundary term at infinity vanishes: Q is exponentially decreasing and its logarithmic derivative is -1-1/(2r)+O(r^(-2)). Integrating (2) gives (1). In particular the near-origin singularity is the positive centrifugal term U=r^(-2)+O(1), and U=1/(2r^3)+O(r^(-4)) at infinity.

The domain issue does not require a formal claim of unitary equivalence. If h_0 u=lambda u with -1<lambda<0, the regular eigenfunction satisfies u'(0)=0, so Du=O(r) at zero and decays at infinity. It is an allowed nonzero partner eigenfunction satisfying h_partner Du=lambda Du. Equation (1) makes that impossible. Eigenvalues below -1 are excluded by D*D>=0, and ker D is exactly span{Q}. Thus h_0 has precisely one negative eigenvalue, namely -1.

For an alternative direct form argument, the nonzero spectral parts of D*D and DD* coincide by polar decomposition; DD*>=1 implies the spectrum of h_0 away from its simple ground state lies in [0,infinity).

## 2. Absence of a radial zero-energy resonance

Suppose h_0 y=0 has a nonzero solution regular at the origin and bounded at infinity. Short-range ODE asymptotics give y=a+o(1), y'=o(r^(-1)), and exponential errors in the original equation. Set v=Dy. Near the origin,

    v(r)=-y(0) r/2+O(r^3).

At infinity v is bounded, while h_partner v=0. Choose its sign so v(r)>0 for small r. The equation

    (r v')'=r U v

and U>0 show that v stays positive and increasing. Once r v' is positive at any radius, it remains bounded below by a positive constant; hence v grows at least logarithmically. This contradicts boundedness. Therefore no nonzero bounded regular radial solution exists. The same positive-form argument excludes a radial zero eigenfunction.

## 3. All nonzero angular sectors are nonnegative and regular at zero

For integer m>=1, the zero-energy free radial Green kernel is

    G_m(r,s)=(1/(2m))(min(r,s)/max(r,s))^m.

The Birman–Schwinger operator with potential Q^2 is positive and has trace

    Tr K_m(0)= (1/(2m)) int_0^infinity r Q(r)^2 dr
             =M/(4 pi m)<1.                              (3)

The strict scalar bound M<4 pi follows without numerical evaluation: the sharp scalar Gagliardo–Nirenberg constant is 2/M, while a Gaussian gives 1/(2 pi), and a Gaussian does not satisfy the equality equation. Thus its quotient is strictly below the scalar optimum.

Equation (3) excludes negative eigenvalues in every m>=1 sector, and also bounded/decaying zero solutions through the zero-energy integral equation. The positive-energy free resolvents satisfy K_m(k)<=K_m(0) as forms, so the inverses 1-K_m(k) are uniformly positive for k>=0.

Consequently h has exactly one negative eigenvalue -1 and zero is regular. In particular (h+k^2)^(-1) exists for every 0<k<1. This removes the spectral qualification in the previous fixed-k unequal-well construction.

## 4. A(k) is negative at sufficiently small k

Expand exp(k r cos theta) in modified Bessel functions. Radial symmetry gives

    A(k)=2 pi [a_0(k)+2 sum_(m>=1) a_m(k)],
    a_m(k)=<Q I_m(k r),(1-K_m(k))^(-1)Q I_m(k r)>_(r dr).

The m=0 inverse is indefinite; its negative direction must be retained. All m>=1 terms are nonnegative. From (3),

    0<=2 sum_(m>=1) a_m(k)
      <=[1-M/(4 pi)]^(-1)
         int_0^infinity r Q^2 [I_0(2kr)-I_0(kr)^2] dr
      =O(k^2).                                          (4)

The equality of the Bessel sums follows by integrating exp(2 k r cos theta); the final estimate follows from Q's exponential decay and the Taylor expansion at k=0.

For the m=0 sector, the free resolvent kernel is

    I_0(k min(r,s)) K_0(k max(r,s)).

Its weighted operator expansion is a rank-one logarithmic term plus a bounded logarithmic kernel:

    K_0(k)=log(1/k)|Q><Q|+K_reg+o(1),
    K_reg(r,s)=Q(r)[log 2-EulerGamma-log max(r,s)]Q(s),

where brackets use r dr. Here is the needed invertibility step explicitly. Let P project onto span{Q} in this weighted space and let T=1-K_reg. If f in Q-perp satisfies (1-P)T(1-P)f=0, then Tf=cQ for a constant c. Set y=c+G_reg(Qf), where G_reg is the logarithmic radial kernel displayed above without its Q factors. Then f=Qy, -Delta_rad y=Qf=Q^2y, and <Q,f>=0 removes the logarithmic growth at infinity. Thus y is a bounded regular zero solution, excluded by section 2. Since K_reg is compact on the exponentially weighted radial space, the compressed operator is invertible. Inverting the rank-one logarithmic block, and using Q I_0(kr)=Q+O(k^2) in the weighted space, gives

    a_0(k)=-1/log(1/k)+O(log(1/k)^(-2)).                  (5)

For a more intrinsic constant, let the regular zero-energy radial solution be

    y_0(r)=a+b log r+o(1), b!=0,
    a_sc=exp(-a/b).

Matching I_0(kr)+a_0(k)K_0(kr) to y_0 in the overlap region yields the denominator

    a_0(k) ~ -1/[log(2/(k a_sc))-EulerGamma].

Only the leading expression (5) is needed; no quantitative error for this refined scattering-length formula is asserted here.

Combining (4) and (5),

    A(k)=-2 pi/log(1/k)+O(log(1/k)^(-2))<0

for every sufficiently small k>0. This is a logarithmic low-energy effect. It is not visible by simply discarding the ground-state pole or replacing the resolvent by a positive one.

## 5. A broader radial identity

For a positive decaying radial solution of -Delta Q+Q-Q^p=0 in dimension d, set q=Q'/Q and

    U_d=(d-1)/r^2+2(d-1)q/r+2q^2+Q^(p-1)-2,
    g_d=r^2 U_d,
    z=-r q.

Direct differentiation gives

    [Q^2 r^(d-3) g_d]'
      =Q^2 r^(d-4) [(d-1)(d-3)
          -(d-1)r^2 Q^(p-1)+(3-p)z r^2 Q^(p-1)].        (6)

For 1<=d<=3, p>=3, and decreasing Q, the right side is nonpositive. Integrating from infinity gives U_d>=0 (strict except d=1,p=3). Thus the same radial spectral exclusion holds in this range whenever such a decaying ground state exists. This statement concerns the scalar radial Schrödinger operator -partial_r^2-(d-1)r^(-1)partial_r-Q^(p-1), not the full matrix linearization of NLS and not arbitrary angular modes in other dimensions. In d=1 the radial space is the even sector with the induced odd partner domain.

## 6. What remains

The identity supplies a rigorous single-well spectral structure and the previously missing k-down-to-zero sign. It does not compare the negative m=0 scattering amplitude with the sum of positive m>=1 channels at every intermediate k. That comparison is the exact remaining obstacle for this specific unequal distant-well family. Even a complete A(k)<0 result would not establish the full arbitrary-potential Lieb–Thirring inequality.

Historical novelty is unverified. First-order ground-state factorization and low-energy logarithmic scattering are established methods. The particular integral representation (1), its general form (6), and their use here require comparison with the spectral literature before any originality claim.

One primary comparison was checked directly: Dong Li and Kai Yang, *On the gap property of a linearized NLS operator*, arXiv:2110.14393v2 (6 March 2026), https://arxiv.org/html/2110.14393v2 . Their theorem proves the full three-dimensional cubic L_+ and L_- gap property. Their introduction and section 7 describe a comparison proof for radial L_- using quantitatively controlled ground-state approximations; the earlier radial result of Costin, Huang and Schlag used a Wronskian strategy. Consequently the three-dimensional radial spectral consequence above is a previously known result, regardless of whether (6) provides a distinct proof. No claim that this note settles a previously open spectral conjecture is made.
