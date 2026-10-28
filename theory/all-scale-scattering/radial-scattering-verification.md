# Proof of the all-scale radial scattering bound

15 October 2026. This checks the proposed inequality

    a_0(k) < -1/log(1/k),          0<k<1,

for the radial scattering coefficient of h=-Delta-Q^2 in two dimensions, where Q is the Townes ground state normalized by -Delta Q+Q-Q^3=0. The proof below derives the origin expansions, Wronskian signs, and normalization independently. It does not establish the sign of the sum over all angular channels.

## The comparison potentials

Write B(r)=K_0(r), q=Q'/Q, b=B'/B and D_Q=partial_r-q, D_B=partial_r-b. The partner potentials are

    U_Q = r^(-2)-Q^2-2q',
    U_B = r^(-2)-2b'.

The radial equations give

    r(Q'B-QB') = int_r^infinity s Q(s)^3 B(s) ds > 0.

The boundary term at infinity vanishes by the exponentially decaying asymptotics of Q and B. Thus Q/B is strictly increasing. The positive integral expressions are

    U_Q(r) = [r Q(r)^2]^(-1)
               int_r^infinity [Q(s)^2/s^2+Q(s)^4] ds,
    U_B(r) = [r B(r)^2]^(-1)
               int_r^infinity B(s)^2/s^2 ds.

For s>r, monotonicity gives Q(s)/Q(r)>B(s)/B(r). Each first integral therefore has the strict comparison required to conclude

    U_Q(r)>U_B(r)>0  for every r>0.                    (1)

These formulas can alternatively be checked by differentiating r Q^2 U_Q and r B^2 U_B. No comparison based only on a formal singular operator domain is being made.

## Exact choice of the comparison solution at the origin

Fix 0<k<1, put ell=log(1/k), and define

    w_B(r)=I_0(kr)-K_0(kr)/ell,       v_B=D_B w_B.

Let L_0(r)=log(2/r)-EulerGamma. The explicit Bessel expansions give

    B(r)=L_0+(r^2/4)(L_0+1)+O(r^4 L_0),
    I_0(kr)=1+k^2r^2/4+O(r^4),
    K_0(kr)=L_0+ell+(k^2r^2/4)(L_0+ell+1)+O_k(r^4L_0).

Consequently

    w_B = -B/ell + (1-k^2)r^2(L_0+1)/(4ell)
                    +O_k(r^4L_0),
    v_B = (1-k^2)r L_0/(2ell) (1+O_k(1/L_0)) > 0     (2)

for sufficiently small r. This is the correct regular partner branch. The other local branch behaves as 1/(r L_0). That branch is locally square integrable against r dr, but has infinite quadratic-form energy. Thus one should not justify the endpoint condition by an incorrect limit-point assertion; (2) explicitly selects the finite-energy branch and cancels the singular branch.

The formal intertwining is valid on r>0 and gives

    -v_B''-r^(-1)v_B'+U_B v_B=-k^2 v_B.

Its form (r v_B')'=r(U_B+k^2)v_B and (2) show that v_B remains positive and increasing for all r: while it is positive, r v_B' is strictly increasing and starts positive, preventing a first zero.

## The regular Townes solution and its positive partner

Let w_Q solve the radial original equation, be regular at zero, and have incoming coefficient one:

    w_Q(r)=I_0(kr)+a_0(k)K_0(kr)+o(K_0(kr)).

The single-well result from R23 ensures that -k^2 is not an eigenvalue for 0<k<1, so this normalization exists. Exponential decay of Q^2 gives the stated expansion and its differentiated version: the forced correction decays like exp(-(2-k)r) times a polynomial, which is o(K_0(kr)) because k<1.

Write A=w_Q(0), which is nonzero by uniqueness of the regular radial ODE solution. Taylor expansion gives

    v_Q:=D_Qw_Q = -(1-k^2) A r/2 + O_k(r^3).           (3)

This solution obeys (r v_Q')'=r(U_Q+k^2)v_Q. At infinity it has positive growing coefficient because D_Q I_0(kr)~(1+k)I_0(kr). If A were positive, (3) would make v_Q negative with negative derivative near zero; the positive potential would keep it negative and decreasing, contradicting that positive growing coefficient. Therefore A<0, and (3), followed by the same ODE monotonicity argument, proves

    v_Q(r)>0 for every r>0.                            (4)

Equations (2)--(3) also give directly

    lim_{r->0} r[v_B v_Q'-v_B'v_Q]=0.                  (5)

More explicitly, v_B=c_B r L_0(1+O(1/L_0)) and v_Q=c_Q r+O(r^3), so the leading boundary expression is O(r^2).

## Wronskian at infinity, including the factor 1-k^2

For W(f,g)=fg'-f'g, set F=D_B I_0(kr), G=D_B K_0(kr). The transformation from (f,f') to (D_Bf,(D_Bf)') for a free solution f''+r^(-1)f'=k^2f is the matrix

    [ -b,          1 ;
      k^2-b',     -r^(-1)-b ].

Its determinant is b'+b/r+b^2-k^2=1-k^2, since B solves B''+r^(-1)B'=B. Hence

    r W(F,G)=(1-k^2)rW(I_0(kr),K_0(kr))=-(1-k^2).     (6)

The previous Wronskian formula for Q/B gives q-b=O(exp(-2r)/r). Therefore

    v_Q=F+a_0(k)G+o(K_0(kr)),
    v_B=F-ell^(-1)G.

The remainders and their first derivatives give zero after multiplication against the growing solution in the limiting Wronskian; the remaining error is O(exp(-2(1-k)r)) times a polynomial. From (6),

    lim_{r->infinity} r W(v_B,v_Q)
       =-(1-k^2)[a_0(k)+ell^(-1)].                    (7)

Finally the partner equations give the exact identity

    [rW(v_B,v_Q)]'=r(U_Q-U_B)v_Bv_Q.

The integrand is positive. It is integrable near zero by (2)--(3) and the displayed partner formulas, and at infinity because U_Q-U_B=O(exp(-2r)/r) while v_Qv_B grows at most as exp(2kr) times a polynomial. Using (5) and (7) yields

    -(1-k^2)[a_0(k)+ell^(-1)]
       =int_0^infinity r(U_Q-U_B)v_Bv_Q dr > 0.

Thus

    a_0(k)<-1/log(1/k),      every 0<k<1.              (8)

The strict sign and the factor 1-k^2 in the proposed comparison are correct. The point-potential comparison is justified by explicit ODE solutions and endpoint expansions, rather than by treating K_0 as a regular whole-plane ground state.

Equation (8) bounds only the m=0 scattering coefficient. The full forward scattering quantity contains the positive terms 2 sum_{m>=1} a_m(k); their comparison against the radial negative term remains a separate required step.
