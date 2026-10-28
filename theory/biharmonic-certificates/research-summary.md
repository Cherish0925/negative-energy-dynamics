# BNLS: zero-momentum dynamics, three-dimensional waves, and averaged-control spreading

Research materials, 7 October 2026. The package contains mathematical proofs, frozen exact inputs, interval-arithmetic verifiers, and their recorded outputs. The 13-page main manuscript and its LaTeX source are included at the package root. Earlier proof notes retain their original hypotheses and historical status; the round-5 notes state the strengthened results.

## Reading the proofs

- [gluing-general.md](../zero-momentum/gluing-general.md): finite-rank almost-conserved energy and arbitrarily slow outgoing multiwave construction, including zero momentum, finite variance, and compact spatial symmetries. This argument removes the former SC hypothesis and does not require the unresolved-at-round-4 radial quartet.
- [radial-analytic.md](../zero-momentum/radial-analytic.md): independent proof of the localizable corrected metric and a separate quantitative finite-block criterion for the radial Hamiltonian spectrum.
- [analytic-dynamics.md](../zero-momentum/analytic-dynamics.md): intrinsic spreading and averaged kinetic grow-up; the first-moment transport endpoint gives a full interval of separated states.
- [n3-full-theorem.md](../zero-momentum/n3-full-theorem.md): complete three-dimensional mass-critical traveling-wave theorem. The companion radial, dipole and angular notes detail its continuum spectral inputs.
- [n4-refinement.md](../zero-momentum/n4-refinement.md): a sharper enclosure of the unchanged four-dimensional exact stationary profile, using a mixed energy-dual residual.
- [refinement-and-transport-details.md](../zero-momentum/refinement-and-transport-details.md): independent checks of the new residual, Newton identification, mass-transport endpoint, and weighted gluing extension.
- The selected round-4 notes and `paper_sources/` provide earlier analytic dependencies. The older conditional gluing discussion is historical; the round-5 proof supplies its replacement argument.

The three-dimensional theorem's currently certified explicit range is `0 < |v| <= 1e-9`, with `E(U_v) < -180 v^2`. Its stationary profile enclosure is `||Q-q||_Z < 4e-6`. The four-dimensional refinement proves `||Q-q||_Z < 3e-7` for the same frozen profile and same exact solution as the earlier certificate. These numerical constants do not replace the analytic proofs.

## Runtime

Python 3.12 was used. Install the recorded dependencies in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

`python-flint` supplies outward-rounded Arb arithmetic. NumPy and SciPy are used only where a finite-matrix witness is generated and subsequently checked by rigorous inequalities; floating-point eigenvalue output alone is never the certificate. No copied environment, symbolic link, BVP solution, or external paper is required to run the verifiers.

## Reproduce the arithmetic

From this package directory:

```sh
.venv/bin/python verify_n4.py --full
.venv/bin/python verify_n3.py --full
.venv/bin/python quartet/verify_quartet.py
```

The N4 entry point recomputes frozen rational polynomial/Ritz bounds, the response certificate, all five Arb Hilbert–Schmidt integrals, the Morse count, and the new residual/Newton refinement. The N3 entry point runs the mixed residual, radial finite-matrix enclosure and full-space gap, dipole pairing, all required finite angular channels, the infinite-angular closure, and the final quantitative traveling-wave implications. The N3 full run took approximately 4–5 minutes in the research environment; timing depends on the machine.

For faster downstream checks using the supplied certified HS and N3 output files:

```sh
.venv/bin/python verify_n4.py
.venv/bin/python verify_n3.py
```

These faster runs do not independently recompute every interval integral. The N4 mixed refinement alone can be rerun directly:

```sh
cd verification/N4
python3 round5_n4_mixed_residual.py
python3 round5_n4_refinement_certificate.py
```

Within `verification/N3`, the original unified entry is `python3 round5_n3_theorem.py --verify-all`. Run that command from its own directory because the constituent scripts use local relative input paths.

Verification rewrites output JSON files. Some outputs include timing or platform metadata, so their file hashes may change even when every certified inequality is identical. Frozen mathematical inputs are identified by hashes within the verifiers. Some JSON files record several optional tighter thresholds as `false`; only the explicitly required inequalities and script assertions determine success.

## Integrity and completeness

After final assembly, create a complete file inventory and check it with:

```sh
python3 generate_manifest.py
python3 generate_manifest.py --check
```

`SHA256SUMS.txt` excludes itself, Python bytecode and cache directories. It should be checked before rerunning verifiers that rewrite their outputs. The package intentionally excludes exploratory BVP/mesh runs, failed attempts, copied dependencies, and downloaded external articles. The final radial-quartet certificate, full analytic proof and Proof details are included in `quartet/`. Its contour contains one algebraically simple continuum eigenvalue; the final Rouché bound is below 0.365771. For sufficiently small nonzero speed the stable and unstable dimensions are therefore exactly 31. The proof also implies a positive critical-chain pairing and a radial zero Jordan chain of length four. These conclusions are separate from the gluing argument, which does not require that spectral exhaustion.

The verifiers establish the displayed arithmetic and spectral bounds. The PDE conclusions also use the analytic arguments in the manuscripts.

## Final independent reruns

For the mathematical disagreement with the published cylindrical statement, read main-manuscript Section 8 together with [gou-details.md](../dispersion-extensions/gou-details.md); the missing uniform axial-moment bound is explicit. The proof does not treat that published-proof gap as a substitute for its own construction.
