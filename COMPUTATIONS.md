# Computations

Programs and numerical inputs are stored directly under `computations/`. Run each program from its own package directory unless its help text specifies otherwise. Output files already present in the repository record the original calculations.

## Environment

From the repository root:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

The pinned environment covers the exact/interval verifiers, exploratory solvers, plotting, and the Bell calculation.

## Biharmonic continuum certificates

```sh
cd computations/biharmonic-certificates
python verify_n4.py --full
python verify_n3.py --full
python quartet/verify_quartet.py
```

The full commands recompute the interval enclosures. Without `--full`, the entry points reuse some stored integral outputs. Python/Arb arithmetic certifies numerical inequalities; the accompanying analytic derivations connect them to the PDE statements.

The [recorded N4 profile figure](computations/excited-waves/figures/N4-excited-profile.pdf) accompanies the original axial-profile calculations.

## Townes and occupation calculations

```sh
cd computations/occupation-computations  # from the repository root
python3 r15_validated_townes.py --certificate
python3 r16_quantitative_gap.py
python3 r17_tangent_certificate.py
```

The examples for different studies start at the repository root. Use the supplied exact inputs and command-line options. NumPy and SciPy searches are separate from Arb profile enclosures. The [full contents](CONTENTS.md) link each study to its derivation.

## Research figures

From the repository root:

~~~sh
OPENBLAS_NUM_THREADS=1 python scripts/build_research_figures.py
~~~

This reads the saved profiles, Hermite coefficients and continuation records and generates six SVG/PNG figures. [Figure definitions and sources](figures/README.md) distinguish computed fields, exact formulae and schematic diagrams.

## Hermite and periodic studies

Each block starts from the repository root. Programs use their computation directory directly. The Hermite readers also accept the original filenames stored in the old JSON records.

~~~sh
cd computations/hermite-optimization
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python r21_orbital_search.py --cut 16 --steps 650
python r21_orbital_refine.py
python r21_orbital_inspect.py
~~~

~~~sh
cd computations/periodic-potentials
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python r28_periodic_search.py --cutoff 10 --nq 10 --steps 25 --lattice square --norms 12 24 48 96 --output r28_periodic_square_refined
python r28_periodic_verify.py
~~~

The [mixed-dispersion continuation guide](theory/mixed-dispersion-continuation/README.md) gives the five solvers, saved endpoints and commands for that study.

## Other studies

| Directory | Purpose |
|---|---|
| `computations/all-scale-scattering/` | Validated Townes profile, angular sums, all-scale scattering bounds |
| `computations/hermite-optimization/` | Full-orbital Hermite searches and independent integration checks |
| `computations/periodic-potentials/` | Periodic potential searches and fixed-potential resolution comparisons |
| `computations/full-response/` | Continuum spectral response and restricted-variation calibration |
| `computations/mixed-dispersion-continuation/` | Optical-model continuation, profiles, parameters, and stopping logs |
| `computations/bell-measurement/` | Exact SymPy reproduction of the known 5/8 Bell measurement |

The Bell calculation runs with `python3 verify_bell_5over8.py`. It enumerates all 126 four-photon outcomes in six modes and checks normalization and exact success probabilities.

## Manuscripts

```sh
python3 scripts/build_manuscripts.py
```

The build requires a TeX installation with the packages used by the sources. Each output is written next to its main `.tex` file; auxiliary build files are kept outside the source tree.

Some numerical programs rewrite their outputs. Use a separate working copy when preserving the original recorded outputs is important. The file catalogue records source locations and numerical inputs independently of the navigation documents.
