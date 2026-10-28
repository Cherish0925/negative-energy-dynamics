"""Exact rational strengthening of the saved R15 Townes certificate.

This checks consequences of the existing outward-rounded ODE certificate;
it does not claim to be an independent ODE integration implementation.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

def main():
    source = Path(__file__).with_name("r15_townes_certificate.json")
    raw = source.read_bytes()
    z = json.loads(raw)
    assert z["certificate_passed"]
    assert z["lower_shot"]["status"] == "undershoot"
    assert z["lower_shot"]["positive_throughout"]
    assert z["upper_shot"]["status"] == "overshoot"
    assert z["upper_shot"]["negative_derivative_throughout"]
    assert z["whole_bracket"]["status"] == "reached"
    assert z["whole_bracket"]["r"] == 6
    a_upper = F(*z["a_upper_dyadic"])
    assert a_upper < F(221, 100)
    C = F(81, 16)
    origin = F(221, 100)**2 * (1+F(1, 16384))**2
    middle = F(z["whole_bracket"]["worst_envelope_coefficient"])
    tail = F(37, 200)**2
    assert max(origin, middle, tail) < C
    q6hi = F(float(z["whole_bracket"]["q"][1:-1].split(",")[1]))
    assert q6hi < F(1, 200)
    beta = 1-C/8
    kappa = beta/(1+beta)
    assert kappa == F(47, 175) and kappa > F(1, 4)
    return {
        "source_certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "envelope_C": str(C),
        "origin_bound": str(origin),
        "middle_bound_exact_dyadic": str(middle),
        "tail_bound": str(tail),
        "sphere_beta": str(beta),
        "homogeneous_kappa": str(kappa),
        "restricted_primary_Townes_pmax_min": str(1/(1+kappa)),
        "passed": True,
    }

if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
