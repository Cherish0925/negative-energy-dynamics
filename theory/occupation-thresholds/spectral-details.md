# Proof details of the Townes envelope and homogeneous spectral gap

Date: 2026-10-09. The interval bounds and their analytic implications are derived below.

## Conclusion and precise scope

Subject to the ordinary IEEE-754 binary64 semantics stated in [r15_validated_townes.py](../../computations/occupation-computations/r15_validated_townes.py), its verified outputs, together with the analytic arguments below, establish

    Q(r)^2 <= 6/(1+r^2)^2  for every r>=0,

for the positive radial ground state of -Delta Q+Q-Q^3=0 in R². This envelope implies:

1. H=-Delta-Q² has exactly one negative eigenvalue, namely -1 with eigenfunction Q;
2. H has no nonzero finite-Dirichlet-energy zero solution;
3. there is a kappa>0 such that

       integral Q²|v|² <= (1-kappa) integral |grad v|²
       whenever v in H¹(R²), integral Q conjugate(v)=0.

The third conclusion is precisely hypothesis (S) of [imbalanced.md](imbalanced.md). Its proof requires the anchored homogeneous-space compactness lemma given below; ordinary whole-space H¹ compactness would be an invalid substitute.

No proof of the full equal-occupation, rank-two Lieb--Thirring conjecture follows. What this supplies is the local spectral input needed for the small-secondary-occupation theorem.

## A. Interval arithmetic and Taylor propagation

The program interprets every input float as its exact dyadic value. Addition, multiplication and reciprocal endpoints are widened with `math.nextafter`; interval subtraction is addition of an exact sign-reversed interval. Interval multiplication takes the minimum and maximum of all four endpoint products and widens them. These operations enclose the corresponding exact real operations under correctly rounded IEEE-754 arithmetic. The mesh uses exact dyadic points with denominator 1024 and bounded numerators; the added assertions explicitly verify this mesh property.

The helper `tube` verifies that the integral Picard map sends the box of continuous paths taking values in its proposed rectangle Y back into that rectangle:

    y0 + [0,h] F([r,r+h],Y) subset Y.

Since the differential equation is smooth for r>0, this gives a valid existence enclosure on the whole step (for example by the compact integral-map fixed-point argument and ODE uniqueness). The test is an enclosure of whole trajectories, not just endpoint samples.

The jets are Taylor coefficients of q'=p and p'=q-q³-p/r. The reciprocal recurrence generates coefficients of 1/(r+s). The step uses terms of orders 0,...,N-1 at the incoming endpoint plus the order-N coefficient enclosed over the entire tube, multiplied by h^N. This is the componentwise Taylor theorem with remainder; it does not assume the formal Taylor polynomial is the exact solution.

No uncovered division by an interval containing zero occurs: each step has r>=1/128, and the reciprocal helper rejects a zero-containing denominator. There were no failed tube or width checks in the independently repeated runs below.

### Regular singular origin

For a in [2.20,2.21], the regular radial solution has an even expansion

    q_a(r)=sum_{n>=0} c_n r^(2n),  c_0=a,
    c_(n+1)=(c_n-sum_{i+j+k=n}c_i c_j c_k)/(4(n+1)^2).

On the complex disk |r|<=1/10, the integral equation maps |q-a|<=1/10 into itself because

    (1/400) [(231/100)+(231/100)^3] < 1/10.

Its Lipschitz constant is at most (1/400)[1+3(231/100)^2]<1. Thus the regular solution is analytic there and has modulus at most 231/100. Cauchy estimates bound the omitted coefficients.

At r0=1/128, using the deliberately larger ratio rho=101/1000, the degree-40 value tail is at most

    (231/100) rho^42/(1-rho²) < 1e-39,

and the derivative tail is at most

    (231/10) (2/rho) (rho²)^21 [21-20rho²]/(1-rho²)^2 < 1e-35.

These two inequalities were also checked with exact Python rational arithmetic, against the actual dyadic floats used for the errors. Their respective upper bounds are approximately 3.545e-42 and 1.475e-38. Thus the origin remainders have substantial slack.

For real 0<=r<=r0 the analytic disk enclosure puts q above 2.10. Consequently (r q')'=r(q-q³)<0, so q'<0 for 0<r<=r0. This supplies the initial positive/decreasing segment used by the shooting classification. The origin disk also proves the envelope there, since

    (231/100)^2 (1+1/16384)^2 < 6.

## B. The bracket really contains the ground state

The exact initial values are

    aL=2483961342750117 / 1125899906842624,
    aU=620990338502279 / 281474976710656.

The independent rerun reproduced the certificate JSON:

* At aL, all intervening tubes have q>0. At r=11.3125 the endpoint has q in [2.6934056557557638e-5,2.8600655723127073e-5] and q' in [3.6965594458552179e-7,2.1154101607102182e-6]. Hence this trajectory has turned while remaining positive.
* At aU, all intervening tubes have q'<0. At r=11.1875 the endpoint has q in [-1.7489017019513853e-6,-3.0660444458244678e-7]. Hence this trajectory has crossed zero while still decreasing.

Here is why these checks imply a ground-state bracket, rather than merely opposite signs in two unrelated IVPs.

Start each solution with a in [aL,aU] in the positive-decreasing region q>0,q'<0. Its first finite exit is either:

* q=0 with q'<0 (overshoot), or
* q'=0 with 0<q<1 (undershoot).

At a turning point q''=q-q³; a first exit from negative derivative therefore requires q<=1. Equality q=1,q'=0 would force the constant solution by uniqueness and is impossible for a>2.20. At a zero crossing, simultaneous q=q'=0 is likewise impossible. Both exits are transverse, so the two first-exit parameter classes are relatively open and disjoint. The endpoint checks put aL in the undershoot class and aU in the overshoot class. The connected interval cannot be the union of these two disjoint nonempty open classes. Some a* has no finite exit.

There is no hidden finite-time ODE blowup before an exit. While 0<q<=a, the decreasing radial mechanical energy

    (q')²/2-q²/2+q^4/4,  derivative = -(q')²/r,

also bounds q'. Therefore the no-exit solution is global, positive and decreasing. Its limit ell must satisfy ell-ell³=0: otherwise integrating (r q')'=r(q-q³) contradicts bounded monotone convergence. Thus ell is 0 or 1.

The value ell=1 is impossible. In that case w=q-1>0 satisfies

    w''+w'/r+q(q+1)w=0,  q(q+1)>=2.

Sturm comparison with a radial Helmholtz solution forces a zero. Equivalently, a positive solution would give a nonnegative ground-state-transformed quadratic form for -Delta_rad-q(q+1) on every large annulus, contradicted by a large annular test function with Dirichlet quotient below 2.

Hence ell=0. An exterior linear comparison then gives exponential decay, and the no-exit solution is the positive radial H¹ ground state. The standard uniqueness theorem for this scalar ground state identifies it with Q. This uses only existence of a no-exit parameter in the bracket, not any unsupported monotonicity of the solution as a function of a.

## C. Whole-bracket enclosure and global tail

The interval IVP with the entire initial bracket [aL,aU] reaches r=6. The rerun gives

    q(6) in [0.0027004838668358466,0.0042832814841662929],
    max_tubes q(r)^2 (1+r²)^2 <= 5.024646047563436 < 6.

Because the true Q initial value lies in this bracket, this is an enclosure for Q on every point of [1/128,6], not just the listed output mesh. Section A supplies [0,1/128].

For the tail use the exact rational delta=1/200. The displayed endpoint enclosure gives Q(6)<delta. Ground-state monotonicity gives Q(r)<=delta for r>=6. Put

    W(r)=delta exp(-(r-6)/2).

Then on r>=6,

    (-Delta+1/4) Q=(Q²-3/4)Q<0,
    (-Delta+1/4) W=W/(2r)>0.

Both functions tend to zero, and Q(6)<=W(6). The exterior maximum principle yields Q<=W. Moreover

    d/dr log[W(r)(1+r²)] = -1/2 + 2r/(1+r²)
                         <= -1/2+12/37 <0.

Thus

    Q(r)^2(1+r²)^2 <= delta²(1+6²)^2 =1369/40000<6.

This proves the global rational envelope. The proof does not use a false nonlinear supersolution comparison with sqrt(6)/(1+r²).

## D. The sphere comparison: negative index and threshold exclusion

Let D consist of functions with finite plane Dirichlet energy and finite integral |u|²/(1+|x|²)^2. Under stereographic projection their images belong to H¹(S²); the missing sphere point is removable for H¹, since a point has zero H¹ capacity in dimension two. Conformal invariance gives

    integral_R² |grad u|² = integral_S² |grad_S v|²,
    integral_R² [6/(1+|x|²)^2]|u|² = (3/2) integral_S² |v|².

Consequently the comparison form

    h_ref[u]=integral |grad u|²-integral [6/(1+|x|²)^2]|u|²

has exactly one nonpositive direction on D: the sphere eigenvalues are 0,2,6,..., so h_ref has one negative eigenvalue -3/2 and no zero eigenvalue. In particular no two-dimensional subspace of D has h_ref<=0 everywhere. The envelope implies h_ref[u]<=h_Q[u], where h_Q is the form of H=-Delta-Q².

Since H Q=-Q, the H¹ operator has at least one negative eigenvalue. The comparison shows its negative index is at most one, so -1 is the unique negative eigenvalue, with multiplicity one.

The same comparison also controls threshold modes; it is stronger than an assertion about the negative index alone. If a nonzero finite-energy zero solution v existed, the form identity would give h_Q[v]=0 and h_Q[Q,v]=0. Therefore span{Q,v} would be a two-dimensional nonpositive subspace for h_Q, and hence for h_ref, a contradiction. The needed form identity follows by the logarithmic cutoff argument in Section E. Q and v cannot be proportional since their eigenvalues differ.

## E. Anchored homogeneous compactness and the gap (S)

Define

    X={v in H¹_loc(R²): grad v in L², integral Qv=0}.

All assertions below hold for real or complex functions. The gradient norm is a genuine norm on X because the anchor removes constants.

Annular Poincare inequalities and telescoping annular means give, for a fixed central average a0,

    integral_{R<|x|<2R}|v-a0|²
        <= C R²(1+log R) integral |grad v|²,  R>=2.

Pairing with the exponentially decaying Q and using the anchor gives |a0|<=C||grad v||₂. It follows that bounded subsets of X are bounded in H¹ on each fixed disk and that their L²(Q²dx) tails are uniformly exponentially small. Local Rellich compactness plus this tail estimate proves

    X -> L²(Q²dx) compactly.

The same estimates give X subset D, as required in Section D. They also show completeness of X in the gradient norm.

For completeness, the cutoff approximation must use dimension two correctly. For each fixed finite-energy function the distant annular means grow as o(sqrt(log R)): split the telescoping sum at a fixed radius, use Cauchy--Schwarz on the remaining annuli, and make the tail Dirichlet energy arbitrarily small. A logarithmic cutoff chi_R, equal to one on B_R and zero outside B_(R²), therefore satisfies ||v grad chi_R||₂->0. Thus chi_R v converges in Dirichlet energy and in L²(Q²dx). Subtracting

    beta_R Q,  beta_R=(integral Q chi_R v)/Mc ->0,

restores the anchor and gives H¹ approximants. This justifies integration against finite-energy functions and use of the form identities above. No positive L² spectral gap at the continuum threshold is being assumed.

There is also a direct route from the envelope to (S) that avoids separately discussing zero solutions. If nonzero v in X satisfied h_Q[v]<=0, then

    h_Q[Q,v]=-integral Q conjugate(v)=0.

The subspace span{Q,v} would again contradict the one-dimensional nonpositive index of h_ref. Hence h_Q[v]>0 for every nonzero v in X.

Now set

    c=sup_{v in X, ||grad v||₂=1} integral Q²|v|².

The supremum is finite and is attained by the compact embedding (a nonzero maximizing limit can be normalized if necessary). If c>=1, an optimizer would satisfy h_Q[v]<=0, which has just been excluded. Therefore c<1, and kappa=1-c>0 establishes (S).

## F. Remaining distinctions

The interval certificate and the analytic proof close the previously identified local spectral hypothesis. They do not supply an explicit numerical value of the resulting homogeneous gap kappa, nor of the small-occupation cutoff tau0 in the nonlinear theorem. That theorem nevertheless has a strictly positive, rank-independent existence conclusion.

Historical originality is a separate literature question. The sphere comparison is a classical conformal/spectral mechanism, and standard scalar ground-state uniqueness and quadratic GN stability remain external inputs. This audit establishes the mathematical chain used here; it does not claim that the one-bound-state property or the resulting local-occupation theorem has never appeared elsewhere.
