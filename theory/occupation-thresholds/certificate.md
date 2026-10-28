# Townes one-bound-state problem: independent spectral reduction

Date: 2026-10-09. Status updated after the initial analytic reductions: the rational Townes envelope has now passed an outward-rounded interval Taylor certificate. The complete certificate and analytic connection are in Section 7. The compressed trace value itself is still only an exploratory numerical value and is not needed for the completed envelope route.

Let Q be the positive radial solution of -Delta Q+Q-Q^3=0 on R^2, and H=-Delta-Q^2. Write m=int_0^infinity r Q(r)^2 dr=M(Q)/(2*pi).

## 1. Angular modes are already excluded analytically

For angular momentum ell>=1 the zero-energy Birman--Schwinger kernel, in L^2((0,infinity),r dr), is

    Q(r) Q(s) (min(r,s)/max(r,s))^ell /(2 ell).

It is positive trace class and its trace is m/(2 ell). The scalar sharp Gagliardo--Nirenberg variational characterization and a Gaussian test give M(Q)<4*pi: the Gaussian quotient gives <=4*pi, and strictness follows because a Gaussian is not an Euler--Lagrange optimizer. Hence m<2, so this trace is strictly less than one for every ell>=1. There are no negative eigenvalues or decaying zero-energy resonances in any of these angular sectors. No numerical value of Q is needed for this conclusion.

## 2. Independent derivation of the compressed radial trace

Let chi=Q in L^2(r dr), P=I-|chi><chi|/m, and

    K_kappa=Q(-Delta_rad+kappa^2)^(-1)Q.

Its kernel is Q(r) I_0(kappa min(r,s)) K_0(kappa max(r,s)) Q(s). The diverging constant term as kappa tends to zero has rank one in direction chi and disappears after compression by P. The limiting compressed positive operator is

    Kbar=P Q G_0 Q P,       G_0(r,s)=-log(max(r,s)).

Additive constants in G_0 are irrelevant. On chi-perpendicular vectors this quadratic form is positive: after the coordinate change x=log r, it is the inverse one-dimensional Laplacian applied to a source of integral zero. Its trace is

    T= (1/(2m)) int int r Q(r)^2 s Q(s)^2 |log(r/s)| dr ds
     = int_0^infinity F(r)(m-F(r))/(m r) dr,
    F(r)=int_0^r s Q(s)^2 ds.

Indeed, Tr(PAP)=Tr A-<chi,A chi>/m with A kernel -Q(r)log(max(r,s))Q(s); expanding log(max(r,s))=(log r+log s+|log(r/s)|)/2 cancels the one-variable terms. One can make this calculation on finite cutoffs first and then use the logarithmic moment and exponential tail of Q.

For every kappa>0, the compressed resolvent is bounded above by Kbar in quadratic form (monotonicity of the free resolvent on the zero-mean sources). Min--max then gives

    lambda_2(K_kappa) <= ||P K_kappa P|| <= ||Kbar|| <= T.

Consequently, T<1 implies that H has at most one radial negative eigenvalue. Since H Q=-Q, it has exactly one negative eigenvalue globally.

## 3. The same strict bound also excludes radial threshold resonance

This is an additional consequence not requiring a numerical shooting derivative. Suppose psi is a regular bounded radial solution of H psi=0. Exponential decay of Q implies that psi(r)=a+b log r+o(1) at infinity. Boundedness forces b=0. Integrating (r psi')'=-r Q^2 psi thus gives

    int_0^infinity r Q(r)^2 psi(r) dr=0.

Set f=Q psi. Then f belongs to L^2(r dr) and f is orthogonal to chi. The radial Green representation is psi=c+G_0(Qf); multiplying by Q and projecting gives

    f=Kbar f.

If T<1 this forces f=0, hence psi=0. The same argument includes a zero eigenfunction. The logarithmically growing generic zero-energy solution is not a bounded resonance and is not being excluded.

## 4. A second exact route: a rational potential and the sphere

A particularly simple sufficient inequality is

    Q(r)^2 <= 6/(1+r^2)^2 for all r>=0.                         (E)

Once (E) is certified (see Section 7), H has at most one negative eigenvalue without computing T. Under stereographic projection to the unit two-sphere,

    int_R2 |grad u|^2 dx = int_S2 |grad v|^2 dOmega,
    int_R2 6/(1+|x|^2)^2 |u|^2 dx = (3/2) int_S2 |v|^2 dOmega.

The sphere Laplacian has eigenvalues 0,2,6,... . Thus the quadratic form on the right has negative index one. Its restriction to stereographic images of H^1(R^2) has negative index at most one. By form comparison H also has index at most one, and H Q=-Q supplies the one negative eigenvalue.

More generally any envelope a*b/(1+b*r^2)^2 with 0<a<8 works, because the corresponding sphere form is int|grad v|^2-(a/4)int|v|^2. This argument only counts negative eigenvalues; a further argument is needed if threshold regularity is required.

## 5. What the floating-point exploration actually shows

Using the existing [r15_townes_profile.npz](../../computations/occupation-computations/r15_townes_profile.npz) sampled BVP profile, straightforward quadrature gives

    m approximately 1.86225552,
    T approximately 0.74017,
    max_r Q(r)(1+r^2)/sqrt(6) approximately 0.90260.

The maximum in the last expression is near r=0.37. The ordinary median-centered Bargmann integral is about 1.03513, so that simpler bound narrowly fails, whereas the compressed bound leaves a substantial margin. These are exploratory floating-point values, not interval enclosures, and do not establish T<1 or (E).

There is no valid maximum-principle proof of (E) merely from plugging U=sqrt(6)/(1+r^2) into the nonlinear equation: its residual is

    -Delta U+U-U^3 = sqrt(6) (r^4-2r^2-1)/(1+r^2)^3,

which changes sign, and the nonlinearity does not provide the needed global comparison principle. This tempting shortcut must not be used.

## 6. Certificate construction

A validated ODE construction can be deliberately coarse because both proposed inequalities have large margins:

1. Bracket Q(0) by certified undershooting and overshooting regular solutions of Q''+Q'/r=Q-Q^3; the uniqueness/shooting characterization then places the ground-state initial value in that interval.
2. Propagate that interval to a moderate radius, for example R=6, with interval Taylor arithmetic, accounting for the regular singular point at r=0 via the even power series.
3. If 0<Q(R)<=delta<1 is enclosed, monotonicity and the maximum principle give the rigorous tail bound

       Q(r)<=delta exp(-sqrt(1-delta^2)(r-R)),  r>=R.

   Indeed, (-Delta+1-delta^2)Q=(Q^2-delta^2)Q<=0, whereas the exponential majorant has positive residual sqrt(1-delta^2) W/r.
4. Use interval quadrature and the tail bound to enclose T below one, or verify the rational envelope on each interval and on the tail.

The following section completes this construction by the rational-envelope route.

## 7. Completed interval enclosure and its analytic consequences

The executable is [r15_validated_townes.py](../../computations/occupation-computations/r15_validated_townes.py); the recorded output is [r15_townes_certificate.json](../../computations/occupation-computations/r15_townes_certificate.json). Its dependencies are only the Python standard library. This is an interval IVP proof, not an error estimate reported by a floating-point ODE solver. Each finite float supplied as an endpoint is interpreted as its exact dyadic rational. Every addition, multiplication, or division used in interval bounds is widened outward with `math.nextafter`.

Single-command reproduction:

    python research/r15_validated_townes.py --certificate

The command asserts every numerical part of the argument and prints `certificate_passed: true` only after all checks succeed. It additionally checks the analytic origin constants with exact `fractions.Fraction` arithmetic. The execution used here completed in about 1.8 seconds.

### Origin and interval Taylor step

For a in [2.20,2.21], consider the complex radial integral equation

    q(r)=a+r^2 int_0^1 t log(1/t) [q(rt)-q(rt)^3] dt.

On |r|<=1/10 it maps the ball |q-a|<=1/10 strictly into itself and is a contraction: use |q|<=231/100, int_0^1 t log(1/t)dt=1/4, and the Lipschitz bound 1+3*(231/100)^2. Thus it gives the analytic regular solution, and Cauchy bounds the coefficients of its even power series. The exact recurrence is

    4(n+1)^2 c_(n+1)=c_n-(c*c*c)_n.

The code evaluates through c_20 at r0=1/128. Bounds 10^(-39) and 10^(-35) for the omitted q and q' terms are deliberately larger than the Cauchy sums, using r0/(1/10)<.101. The same analytic ball proves q>1 and q'<0 for real 0<r<=r0.

Away from the origin the system is q'=p, p'=q-q^3-p/r. For each step, interval Picard inclusion first encloses the entire solution on the step in a rectangle Y. Interval polynomial recursion obtains Taylor coefficients through degree 15 at the left endpoint. Applying the same derivative recursion with r in the whole time interval and (q,p) in Y encloses the degree-16 Taylor--Lagrange remainder. The time mesh is dyadic, with all mesh points multiples of 1/1024 in the executed runs, so time additions are exact. The maximum step is 1/64.

### Shooting bracket and identification of the ground state

The exact starting amplitudes are

    a_L=2483961342750117/1125899906842624,
    a_U=620990338502279/281474976710656.

They display in decimal as 2.20620086 and 2.20620087. The lower shot satisfies q>0 over every validated tube up to r=11.3125, where

    q in [0.000026934056557557638,0.000028600655723127073],
    q' in [0.00000036965594458552179,0.0000021154101607102182].

Thus it has turned upward before any zero. The upper shot satisfies q'<0 over every validated tube up to r=11.1875, where

    q in [-0.0000017489017019513853,-0.00000030660444458244678].

Thus it crosses zero while still decreasing. These first-exit classifications exclude a missed oscillation.

For completeness, shooting brackets the positive decaying solution as follows. For any a between these endpoints, start with q>0 and q'<0. A first exit occurs either through q=0 or through q'=0 with 0<q<1; these alternatives are disjoint and open under changes of a. They cannot cover the connected interval because both alternatives occur at its endpoints. A non-exiting solution remains positive and decreasing globally, with limit ell>=0. The equation forces ell=0 or ell=1. The latter is impossible: if q decreases to one, w=q-1 stays positive and satisfies

    w''+w'/r+q(q+1)w=0,

where q(q+1)>=2; Sturm comparison (or the standard oscillation theorem after multiplying by sqrt(r)) excludes an eventually positive solution. Consequently a non-exiting solution decays to zero and is the unique positive radial ground state. Therefore Q(0) belongs to [a_L,a_U]. This step uses the classical uniqueness of the positive radial solution, already part of the definition and background for Q.

### Global rational envelope

Propagating the entire starting interval [a_L,a_U] to R=6 gives

    Q(6) in [0.0027004838668358466,0.0042832814841662929],
    sup_{r0<=r<=6} Q(r)^2 (1+r^2)^2 <= 5.024646047563436 <6.

The supremum bound is taken over all whole-step Picard rectangles, not over sampled endpoints. For 0<=r<=r0, the analytic ball gives the rational bound

    Q(r)^2(1+r^2)^2 <= (231/100)^2 (1+1/16384)^2 <6.

For r>=6, monotonicity gives Q(r)<delta=1/200. Set W(r)=delta exp(-(r-6)/2). Then

    (-Delta+1/4)Q=(Q^2-3/4)Q<=0,
    (-Delta+1/4)W=W/(2r)>0.

The exterior maximum principle gives Q<=W. Finally

    d/dr log(W(r)(1+r^2))=-1/2+2r/(1+r^2)<=-1/2+2/r<=-1/6,

and W(6)(1+36)=37/200<sqrt(6). This proves the required inequality (E) on the entire half-line.

### Spectral conclusion, including zero

The stereographic comparison in Section 4 proves that H has exactly one negative eigenvalue, namely -1 with eigenfunction Q. It also excludes a bounded zero resonance. Indeed, the sphere operator

    A=-Delta_S2-(1+r^2)^2 Q(r)^2/4

has second eigenvalue at least 2-3/2=1/2 by min--max and has first eigenvalue strictly negative, since Q provides a negative form direction. Thus zero is not an eigenvalue of A. Any bounded zero-energy solution of H, or more generally a finite-Dirichlet-energy solution whose sphere image lies in H^1(S^2), extends across the stereographic pole as a weak solution of A v=0. The removable-point step follows from the finite-energy cutoff argument in dimension two. It must vanish.

No claim is made here that this spectral property is a new historical result. The contribution within the present calculation is a short independently executable envelope proof and a direct stereographic comparison that closes the specific spectral input needed by the other branches of this research.

## 8. Direct connection to anchored homogeneous positivity

An even more direct consequence, pointed out in the independent geometric review, avoids using threshold resonances as an intermediary. Let v have finite Dirichlet energy, stereographic image in H^1(S^2), and satisfy int_R2 Q v=0. If the H quadratic form of a nonzero v were nonpositive, then span{Q,v} would be a two-dimensional nonpositive space: the cross term is <H Q,v>=-<Q,v>=0 and the Q direction is strictly negative. But the sphere reference form int|grad v|^2-(3/2)int|v|^2 is no larger than the H form and has nonpositive index exactly one. This is impossible. Thus H[v]>0 for every such nonzero anchored v.

To obtain a uniform lower bound H[v]>=kappa int|grad v|^2, one additionally uses the compact embedding of the anchored homogeneous space into L^2(Q^2 dx). The separate geometric-review branch supplies that compactness argument and its precise function-space formulation; the present note establishes the required strict positivity input.
