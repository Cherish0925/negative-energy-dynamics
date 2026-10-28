# Exact sum rule for quadratic potential tests and their separated-core limitation

This note concerns the two-dimensional sharp orthonormal GN conjecture. It
does not prove a new lower bound for its constant or exclude a violating
optimizer. Its purpose is to determine what the proposed finite-dimensional
potential family actually measures, retaining the full unoccupied spectrum.

Let real orthonormal orbitals satisfy

$$
 H\phi_i=-e_i\phi_i,\qquad H=-\Delta-a\rho,\qquad
 \rho=\sum_{i=1}^N\phi_i^2,
$$

and occupy the first N levels with a gap above them. Write P for their
projection, Pi=I-P, and

$$
 A_i=\Pi(H+e_i)\Pi>0,\qquad
 \mathcal R(W)=\sum_i\langle\Pi(W\phi_i),A_i^{-1}\Pi(W\phi_i)\rangle.
$$

At an optimizing candidate the necessary response inequality is
$\mathcal R(W)\le L\|W\|_2^2$, with $L=1/(2a)$.
The inverse above includes all unoccupied bound states and continuum.

## 1. A continuum-complete lower bound

Set

$$
 K(W)=\int\rho W^2-\sum_{ij}\left(\int W\phi_i\phi_j\right)^2,
 \qquad D(W)=\int\rho|\nabla W|^2.
$$

Then, whenever the expressions are finite,

$$
 \boxed{\mathcal R(W)\ge K(W)^2/D(W).}                 \tag{1}
$$

The convention at D=0 is zero: the gap then implies K=0. Indeed, with
$u_i=\Pi(W\phi_i)$, one has $K=\sum_i\|u_i\|^2$. The exact f-sum
identity is

$$
 \sum_i\langle u_i,A_i u_i\rangle=D(W).
$$

Before projection, integration by parts gives
$\langle W\phi_i,(H+e_i)W\phi_i\rangle=\int\phi_i^2|\nabla W|^2$.
The occupied correction sums to
$\sum_{ij}(e_i-e_j)|\int W\phi_i\phi_j|^2=0$.
Cauchy–Schwarz in the direct sum of the spectral spaces proves (1).
Consequently every stable candidate satisfies

$$
 K(W)^2\le L\|W\|_2^2 D(W).                           \tag{2}
$$

## 2. The complete traceless-quadratic trace

Let $A_\alpha$ be a Frobenius-orthonormal basis of real symmetric
traceless N by N matrices and put $W_\alpha=\Phi^T A_\alpha\Phi$.
Write

$$
 p(x,y)=\sum_i\phi_i(x)\phi_i(y),\quad
 \tau=\sum_i|\nabla\phi_i|^2,\quad
 \eta=\sum_i e_i\phi_i^2,\quad F=\int\rho^2.
$$

The basis identity
$\sum_\alpha W_\alpha(x)W_\alpha(y)=p(x,y)^2-\rho(x)\rho(y)/N$
gives exactly

$$
 \sum_\alpha\|W_\alpha\|_2^2=(1-1/N)F,
$$

$$
 \mathsf K:=\sum_\alpha K(W_\alpha)
 =(1-1/N)\int\rho^3
 -\iint p(x,y)^4
 +\frac1N\iint\rho(x)\rho(y)p(x,y)^2,                  \tag{3}
$$

$$
 \mathsf D:=\sum_\alpha D(W_\alpha)
 =2\int\rho^2\tau+(1/2-1/N)\int\rho|\nabla\rho|^2.    \tag{4}
$$

For (4), differentiate the rank-one matrix $\Phi\Phi^T$ and subtract
its trace part. Its squared Frobenius norm is
$2\rho|\partial\Phi|^2+(1/2-1/N)|\partial\rho|^2$.
The self-consistent equation also gives

$$
 \mathsf D=2a\int\rho^4-2\int\rho^2\eta
 -(3/2+1/N)\int\rho|\nabla\rho|^2.                    \tag{5}
$$

To obtain (5), use $\Delta\rho=2\tau-2a\rho^2+2\eta$, multiply by
$\rho^2$, and integrate by parts. Exponential decay of optimizer
orbitals justifies these steps. Summing (1) and applying Cauchy–Schwarz
once more yields the necessary inequality

$$
 \boxed{\mathsf K^2\le L(1-1/N)F\,\mathsf D.}         \tag{6}
$$

The fourth-order projector kernel in (3) is essential. There is no
established bound here that turns (6) into a contradiction for a<M_c.
Replacing (3) by its first term would have the wrong direction.

## 3. A strict amplitude gap and the separated-core limitation

Let R denote the response operator, so $\langle W,RW\rangle=\mathcal
R(W)$. For every finite-rank stable optimizer,

$$
 \boxed{\mathcal R(\rho)<L\|\rho\|_2^2.}              \tag{7}
$$

This uses no classification of the Hessian nullspace. If equality held,
positivity of LI-R would give Rrho=Lrho. But

$$
 RW=\sum_i\phi_i h_i,\qquad
 h_i=A_i^{-1}\Pi(W\phi_i)\perp\operatorname{Ran}P,
$$

so $\int RW=\sum_i\langle\phi_i,h_i\rangle=0$. The integral is
well-defined by Cauchy–Schwarz. In contrast $L\int\rho=LN>0$, a
contradiction.

In particular let $\phi=Q/\sqrt{M_c}$ be a scalar Townes optimizer,
$\rho_*=\phi^2$, $L_1=1/(2M_c)$, and define

$$
 r_* =\frac{\mathcal R_*(\rho_*)}{\|\rho_*\|_2^2}<L_1.
$$

The ratio r_* is invariant under translations and mass-preserving
two-dimensional scalings. Consider the exact direct-sum model of N
independent scalar Townes problems. Every nonzero quadratic potential on
its occupied space has the form $W=\bigoplus_j c_j\rho_{*,j}$, since
cross-component products vanish. Direct-sum response and scale invariance
give

$$
 \frac{\mathcal R_{\oplus}(W)}{\|W\|_2^2}=r_*<L_1,     \tag{8}
$$

also when $\sum_j c_j=0$, the traceless condition. Thus the quadratic
family has a fixed strict margin at this exact decoupled model. It does
not see the separate translation and dilation zero modes of the cores.

The direct-sum model is a limiting model, not an actual connected-plane
counterexample or a self-consistent violating optimizer. Equation (8)
does not exclude instability in other potential directions, and no
uniform passage to all normalized off-diagonal products of finite-distance
cores is asserted. Its implication for the proof strategy is precise:
including the full continuum does not by itself make constant-matrix
quadratic potentials detect the modes that become critical at separated
Townes configurations. A proof using this family must obtain additional
optimizer-specific information beyond the sum rule (1).

All calculations above are direct consequences of the established
finite-rank optimizer Hessian and the scalar sharp GN inequality. No
historical novelty claim is made for spectral sum rules or response
identities.
