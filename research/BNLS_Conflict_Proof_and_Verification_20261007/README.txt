BNLS cylindrical-claim adjudication, 7 October 2026

Read BNLS_Cylindrical_Claim_Adjudication_20261007.pdf first.
It identifies the invalid virial closure and supplies the exact-counterexample implication, including finite axial moments and every prescribed positive second-order coefficient.

The checked external statement is Gou arXiv:2205.08167v3, Theorem 1.2.
No line-by-line comparison with the inaccessible publisher final full text is claimed.

The foundational manuscript is included. Its old statements about extensions to other dimensions are historical; only its N=4 construction is needed here.

Fresh logs and exact outputs are in verification/. All nine original verifiers were rerun from frozen data. FRESH_OUTPUT_SUMMARY_20261007.json checks those outputs.

To reproduce, install Python 3.12 and python-flint 0.9.0, then run:
  cd verification
  python3 run_verification.py
The runner regenerates outputs and writes its own VERIFICATION_SUMMARY.json.

The analytic proof and finite arithmetic are both necessary. The computations rely on exact rational arithmetic and documented outward-rounded Arb special-function enclosures. A PASS flag alone is not a replacement for the analytic reductions.
