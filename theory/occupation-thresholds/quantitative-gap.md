# An explicit homogeneous Townes gap from the sphere comparison

Date: 2026-10-09. This note strengthens the R15 homogeneous spectral conclusion without rerunning or modifying the validated ODE integrator. It uses the already certified whole-step enclosures and the monotonicity of the true ground state proved in the R15 shooting argument.

Let Q solve -Delta Q+Q-Q^3=0 in R^2, let Mc=integral Q^2, and write

    D[v]=integral |grad v|^2,
    h_Q[v]=D[v]-integral Q^2|v|^2.

Pohozaev and the equation give D[Q]=Mc and H Q=-Q for H=-Delta-Q^2.

## 1. A stronger rational envelope is already in the certificate

The R15 certificate proves the following three bounds for Q(r)^2(1+r^2)^2:

* On 0<=r<=1/128, Q is decreasing and Q(0)<=aU<221/100. Hence the coefficient is at most

      (221/100)^2 (1+1/16384)^2
        =524490263089/107374182400 <81/16.

* On 1/128<=r<=6, the already stored outward-rounded whole-tube upper bound is the exact binary64 value represented by 5.024646047563436, which is strictly below 81/16.

* On r>=6, the already proved exponential comparison gives a coefficient at most (37/200)^2=1369/40000<81/16.

Consequently the same certificate proves the stronger global estimate

    Q(r)^2 <= (81/16)/(1+r^2)^2.                      (1)

The helper r16_quantitative_gap.py verifies these exact rational comparisons against the saved certificate. This is a mathematical consequence of that certificate, not an independently implemented ODE verification.

## 2. Quantitative mean removal

More generally, suppose Q^2<=C/(1+r^2)^2 with C<8. Under stereographic projection the comparison form becomes

    h_ref[u]=D[u]-(C/4)||u||_{L2(S2)}^2.

For functions with zero sphere mean, the first nonzero sphere eigenvalue 2 gives

    h_ref[u]>=(1-C/8)D[u]=beta D[u],  beta=1-C/8>0.   (2)

Now let v in H1(R2) satisfy integral Q conjugate(v)=0. The zero sphere mean condition need not hold for v. Choose a complex scalar t so that u=v+tQ has zero sphere mean. This is possible because Q has strictly positive, finite sphere mean. The equation for Q and the plane orthogonality give exactly

    h_Q[u]=h_Q[v]-Mc |t|^2.

Using (1) or its C version and then (2),

    h_Q[v]>=beta D[u]+Mc |t|^2.

Since grad v=grad u-t grad Q and D[Q]=Mc, weighted Cauchy--Schwarz gives

    D[v] <= (sqrt(D[u])+sqrt(Mc)|t|)^2
         <= (1+1/beta)(beta D[u]+Mc|t|^2).

Therefore

    h_Q[v] >= (beta/(1+beta))D[v]
           = ((8-C)/(16-C))D[v].                     (3)

This proof is valid for complex functions and needs neither a positive L2 spectral gap nor a compactness argument. The sphere mean used to select t is well defined for H1(R2); the same proof extends to the anchored homogeneous space from R15.

For C=81/16, (3) gives the explicit conclusion

    integral Q^2|v|^2 <= (128/175) integral |grad v|^2
    whenever integral Q conjugate(v)=0.              (4)

Thus one may use kappa=47/175, or the simpler weaker kappa=1/4. The original weaker envelope with C=6 would already yield kappa=1/5 by exactly the same argument.

## 3. An explicit restricted occupation range

Let q=Q/sqrt(Mc), C1=2/Mc, and let an arbitrary orthonormal family have phi_1=q. No angular restriction is imposed on its secondary modes. Put S=sum_{j>=2} t_j |phi_j|^2, tau=sum t_j, B=sum t_j||grad phi_j||_2^2. Equation (4) and scalar vector-valued GN give

    integral(q^2+S)^2
      <= C1 + C1(1-kappa)B+C1 tau B.

Hence the scalar sharp constant is exact in this restricted family whenever

    tau<=47/175.

In normalized occupations this reads p_max>=175/222. A complementary bound follows from the self-contained secondary kinetic inequality proved in r16_occupation_gap.md:

    integral S^2<=3 C1 epsilon B,
    epsilon=max_{j>=2}t_j.

Thus the same fixed-primary family also has the exact scalar constant whenever epsilon<=47/525, with no bound on tau. The family restriction phi_1=q is not invariant under the NLS flow, so these are variational statements, not universal dynamical thresholds at those explicit occupation ratios. A stronger unrestricted theorem with small largest secondary occupation is developed separately in r16_occupation_gap.md.
