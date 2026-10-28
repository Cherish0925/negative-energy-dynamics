# R17 Proof details: global endpoint dynamics and quintic background

Date: 2026-10-09. Reviewed the current Sections 4--5 of [independent-foundation.md](independent-foundation.md) and Sections 1--7 of [quintic-dynamics.md](quintic-dynamics.md). The conclusions below are conditional on the occupation remainders explicitly stated in those notes. This review does not independently certify the external Read--Schulz preprint used to extend the one-dimensional remainder to every strict occupation gap.

## 1. The global two-dimensional Sigma dichotomy closes

Let U be a forward-global endpoint solution in Sigma under the R16 occupation assumptions. Use the compactification

    W(s,y)=|s|^(-1)exp(i|y|^2/(4s))U(-1/s,y/s), s<0.

For t=-1/s the exact inverse is

    U(t,x)=t^(-1)exp(i|x|^2/(4t))W(-1/t,-x/t).        (1)

The signs and normalization in the foundation note are correct. In particular,

    A(W)=||[x+2it grad]U||_2^2/4,
    E(W)=||xU(0)||_2^2/8.

W either extends in H1 through s=0 or blows up there by the usual H1 continuation alternative. If it extends, Sigma persistence gives a Sigma terminal state. The inverse conformal image of its free evolution is an exact free solution, and weighted convergence at the finite endpoint proves H1 scattering of the full U.

If W blows up, write its principal core as

    a_s(y)=exp(i theta_s)lambda^(-1)Q((y-x(s))/lambda),
    W_1(s)=a_s+r_s,
    lambda<=C|s|,
    ||r_s||_2=O(lambda),  ||grad r_s||_2=O(1),
    ||(y-x_*)r_s||_2=O(|s|).

The last bound follows from automatic primary variance and the Townes approximation. The inverse core has

    ell(t)=t lambda(-1/t)<=C,
    X(t)=-t x(-1/t),  v=-x_*.

The centroid argument independently audited in [momentum-details.md](momentum-details.md) applies to W. With P_*^W=P(W)-P(w_sec), it gives

    x(s)=x_*+(2P_*^W/Mc)s+o(|s|),
    X(t)=-x_*t+2P_*^W/Mc+o(1).                    (2)

Thus the constant intercept is positive 2P_*^W/Mc, with these transform conventions. The symbol P_*^W concerns the compactified field; it must not be conflated with the physical radiation-subtracted momentum below.

## 2. Absolute primary H1 error is uniform down to zero width

For the transformed remainder, (1) gives

    ||r_physical||_2=||r_s||_2=O(t^(-1)),
    ||grad r_physical||_2
       <=t^(-1)||grad r_s||_2+(1/2)||y r_s||_2
       =O(t^(-1)).                                      (3)

Indeed ||y r_s||_2<=||(y-x_*)r_s||_2+|x_*|||r_s||_2=O(t^(-1)). No lower bound on ell is used.

To remove the quadratic core phase, subtract the fixed Galilean phase v.x/2 and choose the scalar phase to make their difference zero at X. With x=X+ell z, the remaining phase difference is exactly

    delta_phase(z)
      =ell[(X/t-v).z]/2+ell^2|z|^2/(4t).                  (4)

Equation (2) gives |X/t-v|=O(t^(-1)). Consequently the L2 error is O(ell/t+ell^2/t)=O(t^(-1)). Differentiating the scaled Q profile costs ell^(-1), while (4) contains at least one factor ell; this gives an O(t^(-1)) gradient error against weighted Q derivatives. The derivative of the phase difference is also O(t^(-1)) against Q. All needed moments are finite by exponential decay. The carrier derivative is a fixed multiple of the L2 error.

Thus the primary approximation with the fixed Galilean phase has absolute H1 error O(t^(-1)), uniformly for every 0<ell<=C. This check addresses the potentially singular ell->0 case directly.

## 3. Secondary H1 radiation and physical momentum

The compactified secondary modes have bounded H1 norm. Their individual continuity equations yield uniformly bounded quadratic transport speed. Since W is in Sigma at each negative time, their density curves are Cauchy in finite-mass P2 as s->0. Their terminal states have convergent second moments. Strong unweighted complex L2 convergence plus convergence of the weighted norms yields strong weighted complex L2 convergence.

For W_lin(s)=exp(is Delta)w_sec, both the unweighted and weighted differences W_sec-W_lin tend to zero; the gradient difference stays bounded. Inverting the conformal map gives

    ||grad(U_sec-exp(it Delta)F_sec)||_2
       <=t^(-1)||grad(W_sec-W_lin)||_2
          +(1/2)||y(W_sec-W_lin)||_2 ->0.

Together with unweighted L2 convergence, this proves H1 scattering of every secondary component. Strong physical H1 convergence of the compactified endpoint was not assumed. The sub-H1 polynomial rates stated in the foundation note follow from its quantitative terminal L2 estimate and interpolation with uniform physical secondary H1 bounds.

Let C_t denote the physical primary Townes core with carrier exp(iv.x/2), and let e_t=u_1-C_t. Equation (3) and the phase replacement give ||e_t||_H1=O(t^(-1)). For momentum, integration by parts puts the derivative in both linear error terms on e_t:

    P(C_t+e_t)-P(C_t)
      =2 Im integral conjugate(C_t)grad e_t+P(e_t).

Hence its norm is at most

    2sqrt(Mc)||grad e_t||_2+||e_t||_2||grad e_t||_2
      =O(t^(-1)).

The estimate contains no gradient of C_t and remains valid when ell->0. Since P(C_t)=Mc v/2 and secondary H1 scattering preserves their limiting momenta, physical momentum conservation proves

    v=(2/Mc)[P(U)-sum_(j>=2)P(F_j)].                       (5)

The two alternatives are disjoint. The second retains positive primary mass in a ball of one fixed sufficiently large radius about X(t), because ell is uniformly bounded. Any free L2 Schrödinger solution has mass tending to zero uniformly over all balls of that radius; density of L1 cap L2 and the dispersive estimate prove this fact. Thus the second alternative cannot scatter even in L2.

**Verdict:** the stated global Sigma dichotomy, intercept, radiation, and absolute H1 approximation are valid under the displayed R16 inputs. They do not determine a positive limiting width or a phase law.

## 4. One-dimensional quintic extension: the new background argument passes

The quintic note explicitly assumes the one-dimensional remainder

    E>=a_epsilon E_1+b_epsilon A_secondary,
    a_epsilon,b_epsilon>0,

at principal mass Mc=pi sqrt(3)/2 and a strict leading-occupation gap. Its scalar concentration estimate, transport argument, and subsequent constants are consistent:

    I_1(t)<=8(E/a_epsilon)(T-t)^2,
    ||u_1'(t)||_2>=Mc/[4sqrt(2E/a_epsilon)(T-t)],
    lambda(t)<=4sqrt(E/(a_epsilon Mc))(T-t),
    E_scalar(v_1(s))<=4(E/a_epsilon)/s^2.

The secondary-background construction avoids the previously unavailable global estimate for the quintic cross forcing. The scalar residual has L2 norm O(lambda) and derivative norm O(1), so one-dimensional Sobolev interpolation gives its supremum norm O(sqrt(lambda)). The primary therefore vanishes uniformly on every compact set away from x_*. Secondary fields are uniformly bounded in H1 and hence in L-infinity.

For each fixed smooth compactly supported test away from x_*, the tested secondary equation has a uniformly bounded derivative near T. The test pairings converge. Such tests are dense in L2; the uniform L2 bound therefore gives a unique weak L2 terminal field on the entire trajectory. Individual secondary transport provides tightness without an initial moment assumption. Uniform H1 bounds, local Rellich compactness, and tightness upgrade the convergence to strong global L2, then to H^sigma for every sigma<1 and to uniform convergence. This reasoning is valid and does not require estimating the singular forcing globally.

Exact Gram orthogonality supplies the node. Dividing its primary-core contribution by sqrt(lambda) gives

    |integral Q(y)conjugate(u_j(x(t)+lambda y))dy|
       <=C sqrt(lambda).

The uniform H1 bound gives

    |u_j(x(t)+lambda y)-u_j(x(t))|
       <=C sqrt(lambda)|y|^(1/2).

Since integral Q>0 and its indicated moment is finite, u_j(x(t))=O(sqrt(lambda)). Uniform convergence and x(t)->x_* imply w_j(x_*)=0. The claimed full-time sub-H1 core-plus-background decomposition and exact background Gram matrix follow.

With finite secondary variance, the same transport-plus-weighted-norm argument yields strong weighted complex L2 convergence. The conformal free-scattering proof is dimension independent for mass-critical scaling: the derivative difference is bounded by h times the physical derivative difference plus half the physical weighted difference. Hence each conformal secondary scatters in H1, with its stated Gram matrix and kinetic energy.

Finally, the exact quintic energy expansion has the three nonnegative subtracted terms

    (1/2)integral rho_1^2 rho_s,
    (1/2)integral rho_1 rho_s^2,
    (1/6)integral rho_s^3.

Their sum is E_1+A_secondary/2-E and is bounded, so each is bounded. Critical conformal scaling multiplies each by h^2. Combined with the vanishing primary conformal scalar energy and secondary H1 scattering, this proves the displayed identity

    E(V)=(1/8)sum_(j>=2)||(x-x_*)w_j||_2^2.

**Verdict:** the completed quintic dynamical extension is correct conditional on its stated variational input. The range epsilon<1 relies on the explicitly identified external sharp one-dimensional theorem; this audit does not turn that dependency into an internally proved result. Exact primary speed and strong physical secondary H1 convergence remain unproved, as the note states.
