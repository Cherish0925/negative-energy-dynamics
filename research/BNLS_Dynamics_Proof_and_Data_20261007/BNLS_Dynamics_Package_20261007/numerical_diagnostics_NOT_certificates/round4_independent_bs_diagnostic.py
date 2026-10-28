"""Independent floating-point cross-check; NOT a rigorous certificate.

Uses the frozen trial's endpoint derivatives and SciPy directly, importing none
of the interval or exact polynomial certificate implementation.
"""
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import BPoly
from scipy.linalg import eigvalsh
from scipy.special import iv, kv, roots_legendre

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "round2_radial_H4_exact_h1_16.json"
data = json.loads(INPUT.read_text())
nodes = np.array([a / b for a, b in data["nodes"]])
jets = np.array([[float.fromhex(z) for z in row] for row in data["jets_hex"]])
profile = BPoly.from_derivatives(nodes, jets)
x, weights = roots_legendre(600)
radii = 18 * (x + 1)
weights = 18 * weights
values = profile(radii)
z = np.exp(1j * np.pi / 4) * radii
indices = np.arange(len(radii))
smaller = np.minimum(indices[:, None], indices[None, :])
larger = np.maximum(indices[:, None], indices[None, :])
prefactor = np.sqrt(weights * radii) * values
out = {}
for ell, coefficient in [(0, 3), (1, 1), (2, 3), (3, 1), (4, 3)]:
    regular, decaying = iv(ell + 1, z), kv(ell + 1, z)
    matrix = (
        -coefficient * prefactor[:, None] * prefactor[None, :]
        * np.imag(regular[smaller] * decaying[larger])
    )
    eigenvalues = eigvalsh(matrix)
    out[str(ell)] = {
        "largest": eigenvalues[-4:][::-1].tolist(),
        "trace": float(np.trace(matrix)),
        "HS_squared": float(np.sum(matrix * matrix)),
        "certified": False,
    }
output = json.dumps(out, indent=2)
(ROOT / "round4_independent_bs_diagnostic.json").write_text(output + "\n")
print(output)
