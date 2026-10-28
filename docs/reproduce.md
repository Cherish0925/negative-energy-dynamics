# Reproduce the archived work

## Restore exact original packages

From the repository root, using Python 3:

```sh
python3 scripts/restore_archives.py
python3 scripts/verify_integrity.py
```

Original ZIP files are stored directly when small, and in numbered byte parts when larger than 4 MiB. The restoration script joins parts in manifest order, checks SHA-256, checks member paths, extracts the complete original packages under `work/`, and checks every restored file against the source manifest. All original inputs remain available; the browsable text mirror is not a substitute for restoring the numerical packages.

## Main N3/N4 certificates

```sh
cd work/BNLS_Zero_Momentum_Proof_and_Data_20261007/BNLS_ZeroMomentum_Package_20261007
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python verify_n4.py --full
.venv/bin/python verify_n3.py --full
.venv/bin/python quartet/verify_quartet.py
```

Python 3.12 was used in the original work. `python-flint` supplies Arb interval arithmetic. NumPy/SciPy are used where witnesses are subsequently bounded rigorously. Read the package README for the distinction between full verification and faster checks that reuse frozen outputs.

The full analytic PDE conclusions also use the proof notes and manuscripts. Floating-point plots are not substitutes for interval inequalities.

Verifiers may rewrite output JSON or log files. Check integrity before rerunning them, or restore a fresh work directory when a byte-identical copy is needed. The repository archive and browsable mirrors remain unchanged by these runs.

## Other material

The [source index](../research/INDEX.md) maps all 15 packages. Earlier packages retain original commands and requirements. The 19 October continuation package is exploratory numerical code; rerunning it is not a certificate of mixed-model existence.
