#!/usr/bin/env python3
"""Exact verification of a KNOWN 5/8 linear-optical Bell measurement.

This is a baseline reproduction, NOT a new optical design, optimization result,
or proof of optimality. The model contains four equiprobable dual-rail Bell
states, two additional separable single photons, six optical modes, passive
lossless optics, and ideal photon-number-resolving detectors. There is no
feed-forward, postselected ancilla preparation, squeezing, or nonlinearity.

Run:
    python verify_bell_5over8.py
    python verify_bell_5over8.py --output baseline_report.json
Dependency: sympy

Reference: A. Olivo and F. Grosshans, Phys. Rev. A 98, 042323 (2018),
https://arxiv.org/abs/1806.01243 , especially Section IV.C and Figure 1.
Our equivalent mode convention uses real Hadamard beam-splitter matrices.
"""
from __future__ import annotations

import argparse
import json
from math import comb, factorial
from pathlib import Path
from typing import Iterator

try:
    import sympy as sp
except ImportError as exc:
    raise SystemExit("This verifier needs SymPy. Install it with: python -m pip install sympy") from exc

M = 6
Q = 4
X = sp.symbols("x1:7")
SQRT2 = sp.sqrt(2)
LABELS = ("Phi+", "Phi-", "Psi+", "Psi-")
# 1-based physical gate labels, in application order.
GATES = ((1, 3), (2, 4), (5, 6), (1, 5), (2, 6))

def occupations(total: int, modes: int) -> Iterator[tuple[int, ...]]:
    if modes == 1:
        yield (total,)
        return
    for n in range(total + 1):
        for tail in occupations(total - n, modes - 1):
            yield (n,) + tail

def beam_splitter(i: int, j: int) -> sp.Matrix:
    """Real balanced beam splitter; accepts zero-based mode indices."""
    b = sp.eye(M)
    b[i, i] = b[i, j] = b[j, i] = 1 / SQRT2
    b[j, j] = -1 / SQRT2
    return b

def verify() -> dict:
    # Convention: a_i^dagger -> sum_j U[i,j] c_j^dagger.
    u = sp.eye(M)
    for i, j in GATES:
        u = u * beam_splitter(i - 1, j - 1)
    u = sp.simplify(u)
    if sp.simplify(u * u.conjugate().T) != sp.eye(M):
        raise AssertionError("The optical mode matrix is not exactly unitary.")

    bell = {
        "Phi+": (X[0]*X[2] + X[1]*X[3]) / SQRT2,
        "Phi-": (X[0]*X[2] - X[1]*X[3]) / SQRT2,
        "Psi+": (X[0]*X[3] + X[1]*X[2]) / SQRT2,
        "Psi-": (X[0]*X[3] - X[1]*X[2]) / SQRT2,
    }
    substitutions = {X[i]: sum(u[i, j]*X[j] for j in range(M)) for i in range(M)}
    all_n = tuple(occupations(Q, M))
    if len(all_n) != comb(Q + M - 1, Q):
        raise AssertionError("Incorrect Fock-basis enumeration.")

    probabilities: dict[str, dict[tuple[int, ...], sp.Expr]] = {}
    norm: dict[str, sp.Expr] = {}
    for label, p in bell.items():
        # Exactly one ancillary photon in each of input modes 5 and 6.
        p_in = sp.expand(p * X[4] * X[5])
        p_out = sp.Poly(sp.expand(p_in.subs(substitutions, simultaneous=True)), *X)
        probabilities[label] = {}
        for n in all_n:
            coef = p_out.coeff_monomial(n)
            # The monomial is unnormalized. The Fock amplitude includes sqrt(prod n_i!).
            amplitude = sp.simplify(coef * sp.sqrt(sp.prod(factorial(k) for k in n)))
            probability = sp.simplify(amplitude * sp.conjugate(amplitude))
            probabilities[label][n] = probability
        norm[label] = sp.simplify(sum(probabilities[label].values()))
        if norm[label] != 1:
            raise AssertionError(f"Output state {label} is not exactly normalized.")

    success = dict.fromkeys(LABELS, sp.Integer(0))
    records = []
    for n in all_n:
        # Exact algebraic zeros, not a numerical threshold.
        support = [label for label in LABELS if probabilities[label][n] != 0]
        conclusive_label = support[0] if len(support) == 1 else None
        if conclusive_label is not None:
            success[conclusive_label] += probabilities[conclusive_label][n]
        records.append({
            "photons_per_output_mode": n,
            "probabilities": {label: str(probabilities[label][n]) for label in LABELS},
            "conclusive_label": conclusive_label,
        })
    success = {label: sp.simplify(p) for label, p in success.items()}
    mean = sp.simplify(sum(success.values()) / 4)
    expected = {"Phi+": sp.Rational(1, 4), "Phi-": sp.Rational(1, 4),
                "Psi+": sp.Integer(1), "Psi-": sp.Integer(1)}
    if success != expected or mean != sp.Rational(5, 8):
        raise AssertionError("Known baseline was not reproduced.")

    return {
        "status": "Exact reproduction of a known baseline; no novelty or optimality claim.",
        "modes": M,
        "total_photons": Q,
        "number_of_possible_detection_patterns": len(all_n),
        "balanced_beam_splitters_in_application_order": GATES,
        "unitary_convention": "a_i^dagger -> sum_j U[i,j] c_j^dagger",
        "U": [[str(u[i, j]) for j in range(M)] for i in range(M)],
        "state_normalizations": {label: str(p) for label, p in norm.items()},
        "unambiguous_success_by_Bell_state": {label: str(p) for label, p in success.items()},
        "equal_prior_mean_success": str(mean),
        "detection_records": records,
    }

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional path for the complete exact report.")
    args = parser.parse_args()
    report = verify()
    print("Known baseline reproduced with exact arithmetic.")
    print(f"Modes: {M}; total photons: {Q}; output patterns: {report['number_of_possible_detection_patterns']}")
    print("Conditional unambiguous success:", report["unambiguous_success_by_Bell_state"])
    print("Equal-prior success:", report["equal_prior_mean_success"])
    print("This is not a new result and does not establish an upper bound.")
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Report written to: {args.output}")

if __name__ == "__main__":
    main()
