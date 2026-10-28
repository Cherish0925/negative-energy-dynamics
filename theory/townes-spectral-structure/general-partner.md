# A radial spectral gap from the nonlinear profile equation

Research derivation, 15 October 2026. The factorization used here is classical. The weighted identity is derived below; historical priority for this identity has not been determined.

## Statement

Let d=2 or 3, a=d-1, and omega>0. Suppose Q is a positive, smooth, strictly decreasing radial profile, regular at zero, exponentially decreasing at infinity, satisfying

    Q''+(a/r)Q'=omega Q-V(Q)Q.

Assume V is continuously differentiable on the range of Q, V(0)=0, and

    V(s)>=0,     s V'(s)>=2 V(s).

Define the radial scalar Schroedinger operator

    h_rad=-partial_r^2-(a/r)partial_r-V(Q)

on the regular radial domain in L2((0,infinity),r^a dr). Then its only negative eigenvalue is -omega, with eigenfunction Q, and

    <f,h_rad f> >=0       for f perpendicular to Q.

In d=2 there is no nonzero bounded regular zero-energy solution. In d=3 there is no regular zero-energy resonance with the usual 1/r decay. The latter statement does not exclude bounded zero-energy scattering solutions approaching a nonzero constant.

This result concerns h_rad, or equivalently L_-=h_rad+omega. It does not concern the full Hamiltonian matrix linearization or L_+.

## Weighted identity and positivity

Write p=Q'/Q and D=partial_r-p. In the radial measure,

    D*=-partial_r-a/r-p,
    D*D=h_rad+omega,
    DD*=h_partner+omega,
    h_partner=-partial_r^2-(a/r)partial_r+U,
    U=a/r^2+2ap/r+2p^2+V(Q)-2omega.

The profile equation gives p'=omega-V(Q)-p^2-ap/r. Differentiating U, without imposing any explicit formula for Q, gives the identity

    (r^a Q^2 U)'
      =r^a Q^2 [a(a-2)/r^3-a V(Q)/r
                   +p (Q V'(Q)-2V(Q))].                 (1)

Every term on the right is nonpositive when d=2 or 3. The exponentially weighted boundary term at infinity vanishes. Consequently

    U(r)=1/[r^a Q(r)^2] int_r^infinity s^a Q(s)^2
       [a(2-a)/s^3+a V(Q(s))/s
                   -(Q'(s)/Q(s))(Q(s)V'(Q(s))-2V(Q(s)))] ds.   (2)

It is strictly positive in d=2. In d=3 it is nonnegative, and strictly positive for pure powers V(s)=s^sigma. General nonlinearities may vanish for sufficiently small s, in which case U can vanish outside a finite radius. Nonnegativity is enough for the spectral conclusion. The resonance argument below needs only that the regular partner solution starts with positive slope and U>=0, not strict positivity at every radius.

Near zero, U=a/r^2+O(1). For a radial regular eigenfunction f, Df=O(r) at zero. Thus its image has precisely the regular partner boundary behavior. If h_rad f=lambda f with -omega<lambda<0, then Df is a nonzero partner eigenfunction at lambda. This contradicts

    <v,h_partner v>=int_0^infinity (|v'|^2+U|v|^2)r^a dr>=0.

Eigenvalues below -omega are excluded by D*D>=0, and ker D=span{Q}. Equivalently, polar decomposition identifies the nonzero spectral parts of D*D and DD*, and DD*>=omega.

## Zero-energy behavior

For a regular solution h_rad y=0,

    Dy(r)=-(omega/d)y(0) r+O(r^3).

A nontrivial regular solution has y(0) nonzero. Choose the sign of v=Dy so that v>0 near zero. The partner equation yields

    (r^a v')'=r^a U v.

Hence v remains positive and increasing. For d=2 it grows at least logarithmically, contradicting bounded y, since Q'/Q tends to -sqrt(omega) and bounded zero solutions have y'=o(1/r). For d=3 a resonant y=O(1/r) gives v=O(1/r), contradicting the positive increasing partner solution. A zero eigenfunction is also excluded by the positive partner quadratic form and intertwining.

## Powers and the two-dimensional cubic case

For V(s)=s^sigma, the condition is sigma>=2. Therefore the radial statement applies to all such profiles that exist, with no numerical evaluation of Q. The familiar pure-power existence restrictions still apply; this proposition does not assert profile existence for every sigma and dimension.

For d=2, omega=1, V(Q)=Q^2, (2) simplifies to

    U(r)=1/[r Q(r)^2] int_r^infinity [Q(s)^2/s^2+Q(s)^4] ds>0.

For d=3, omega=1, V(Q)=Q^2, it becomes

    U(r)=2/[r^2 Q(r)^2] int_r^infinity s Q(s)^4 ds>0.

The three-dimensional cubic radial L_- gap is an established conclusion in earlier work, including Costin-Huang-Schlag and Li-Yang. This formula gives a direct route to that part of the conclusion; it does not replace their results about L_+ or all nonradial sectors.

For the two-dimensional cubic Townes profile, the angular Birman-Schwinger trace argument in r23_scattering_sign.md also excludes every nonzero angular sector. Thus in this particular case the statement becomes

    sigma(-Delta-Q^2)={-1} union [0,infinity),
    <f,(-Delta-Q^2)f>>=0 for all f perpendicular to Q,

with -1 simple and no zero-energy resonance. The displayed set equality follows from the exclusion below zero and the standard essential spectrum [0,infinity); no claim about the full NLS linearization is implicit.

## Source comparison

- Chang-Gustafson-Nakanishi-Tsai, *Spectra of Linearized Operators for NLS Solitary Waves*, arXiv:math/0611483, Section 3: classical Darboux factorization and the explicit one-dimensional hierarchy. https://arxiv.org/pdf/math/0611483
- Costin-Huang-Schlag, *On the spectral properties of L_{+-} in three dimensions*, arXiv:1107.0323: radial gap for both scalar linearized operators. https://arxiv.org/abs/1107.0323
- Li-Yang, *On the gap property of a linearized NLS operator*, arXiv:2110.14393v2, Section 7: three-dimensional L_- gap through comparison and quantitatively controlled ground-state information. https://arxiv.org/html/2110.14393v2

This note identifies a proved profile-to-spectrum implication under explicit assumptions. It neither resolves the two-dimensional sharp Lieb-Thirring constant nor claims historical originality without further literature comparison.
