Core continuation research state, 19 October 2026

Objective: determine whether the mass-critical optical equation
i u_z = (-d_tau^2 + Delta_perp^2) u - |u|^2 u
has a finite-mass traveling wave with negative intrinsic Hamiltonian.
Status: NOT SOLVED. No new optical traveling wave or stability theorem was obtained.

The previous centroid-reversal and quartic-calibration calculations do not solve this problem. They should not be presented as the central physical breakthrough of the project.

Recorded computations:
1. Recovered the frozen three-dimensional excited radial seed from
BNLS_Dynamics_Proof_and_Data_20261007.zip,
Library ID libfile_05a1279d757c8191853eeee98e803390.
The frozen seed is verification/round4_n3_mixed_exact.json in that package.

2. Axisymmetric finite-volume continuation, even in tau and radial in (x,y):
a_s(xi,eta) = (1-s)(xi^2+|eta|^2)^2 + s(xi^2+|eta|^4),
alpha_s=(8-2s)/3 in |Q|^alpha_s Q.
This auxiliary path is not mass-critical for 0<s<1.
At n=128 per half-coordinate, half-domain lengths 24, the initial response
I=<Q_x,L_-^{-1} Q_x> was -2172.606856; ordinary continuation stopped near s=0.9766.
At s=0.975 the coarse response was -45.809645, but refinement to n=192 gave
+379.918221. The negative coarse-grid sign is not reliable evidence.
The n=192 continuation converged at s=0.985; later forward trials near 0.9855 failed.
Failure of this solver is not a nonexistence theorem.

3. A separate critical path first removes the quartic cross term while retaining
alpha=8/3, then would lower the temporal Fourier order p from 4 to 2 with
alpha=4p/(p+2). The n=128 calculation encountered a turning point before
completion of the first stage, near s=0.6566. Pseudo-arclength continuation
passed that turning point and followed the branch back to s=0.1132.
This is a finite-grid branch observation, not a certified bifurcation theorem.

4. Independent DCT/Bessel pseudospectral discretization: nt=256, nr=128,
half-domain lengths 24. Bessel transform matrices were orthogonalized by their
polar factors. Analytic Bessel derivatives supplied the angular-one response.
For the original seed at s=0, response I=-1321.740058, mass=10643.195937,
equation residual=1.13e-10, energy=-0.0018053. The earlier whole-space numerical
reference is approximately -1323.397; finite-window errors are not certified.
On the mixed auxiliary path:
s=0.980: I=435.723587, M=8610.942893, residual=8.96e-12;
s=0.985: I=321.249647, M=8513.779130, residual=1.27e-11;
s=0.990: I=28.345896, M=8399.978825, residual=3.41e-11;
s=0.991015625: I=40.959704, M=8373.804071, residual=1.63e-10.
Ordinary continuation then failed. These intermediate states are not solutions
of the target optical equation s=1. Negative intermediate energies must not be
represented as target-model counterexamples.

5. A bordered pseudospectral arclength computation was launched from the last
two spectral states. Its result was not retrieved because the execution service
disconnected. No successful result is claimed for that run.

Code and raw checkpoints were written under
/workspace/scratch/2d79348278a6/core_continuation/:
continue_core.py, critical_path.py, arclength.py, spectral_core.py,
spectral_arclength.py, with JSON logs and NPZ states.
Their persistence was not confirmed at the time of the service disconnect.

These calculations tested direct transfers of the negative-response
mechanism rather than adding unrelated optical illustrations. It did not close
the existence problem, establish nonexistence, or demonstrate a useful stable
optical device. The observed folds and resolution-sensitive signs are route
information only. Future work must not count them as completed physical innovations.
