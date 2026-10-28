# Exact Bessel moments for the all-scale angular bound

2026-10-15. These are identities used to bound the positive angular sum;
they do not alone prove its comparison with the negative radial amplitude.

Let M_n=integral_0^infinity r^(2n+1) K_0(r)^2 dr. Then

    M_n = 2^(2n-1) (n!)^4 / (2n+1)!, n>=0.

Proof: use K_0(r)=(1/2) integral_0^infinity exp(-t-r^2/(4t)) dt/t
twice. The r integral gives 2^(2n-1)n! times
integral exp(-s-t)(st)^n/(s+t)^(n+1) ds dt.
With u=s+t, v=s/(s+t), the remaining factors are Gamma(n+1)
and Beta(n+1,n+1). All integrands are nonnegative, so Tonelli applies.

For m>=0 and n>=m, the coefficient of z^(2n) in I_m(z)^2 is

    c_nm = (2n)!/[4^n (n!)^2 (n-m)! (n+m)!].

This follows by multiplying the I_m series and applying Vandermonde's identity.
Consequently

    c_nm M_n = [ (n!)^2 / ((n-m)!(n+m)!) ]/[2(2n+1)]
             <= 1/[2(2n+1)].

In particular, for 0<k<1,

    integral r K_0(r)^2 I_0(kr)^2 dr = atanh(k)/(2k),
    integral r K_0(r)^2 I_0(2kr) dr = arcsin(k)/(2k sqrt(1-k^2)),

and therefore the exact positive angular Born sum for a K_0 envelope is

    integral r K_0(r)^2 [I_0(2kr)-I_0(kr)^2] dr
      = [arcsin(k)/sqrt(1-k^2)-atanh(k)]/(2k).

The second formula follows from the displayed moment series, or by the
elementary beta-integral summation. The formulas have finite limit 1/2 for
the two separate integrals at k=0; their difference starts at k^2/6.

If Q<=A K_0, the formula controls the complete infinite angular Born sum
without truncating either the angular or radial tail. Any certified upper
moments of Q^2 smaller than A^2 M_n can improve it by subtracting finitely
many nonnegative coefficient differences. Such subtractions remain upper
bounds because the unused coefficients are bounded individually by the
envelope. This is a finite-computation device, not a substitution of the
envelope for the actual Townes profile.
