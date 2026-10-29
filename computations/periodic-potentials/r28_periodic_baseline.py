"""Constant-shift optimization of saved periodic Galerkin potentials.

All matrix eigenvalues are retained. The Fourier potential is kept fixed;
only its constant coefficient changes. Results remain floating-point.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from r28_periodic_search import BlochProblem, resize_hat

def best_shift(eigenvalues, area, integral, norm, nonnegative=False):
    """Globally optimize finite-spectrum S(b)/(area*b*b+2*integral*b+norm)."""
    vals = np.sort(np.asarray(eigenvalues).ravel())
    nq = len(eigenvalues)
    sums = np.concatenate(([0.], np.cumsum(vals)))
    counts = np.arange(1, len(vals)+1)
    mu = sums[1:]/counts
    rad = mu*mu+(norm+2*mu*integral)/area
    roots = mu+np.sqrt(np.maximum(rad, 0.))
    upper = np.concatenate((vals[1:], [np.inf]))
    good = (rad >= 0) & (roots >= vals) & (roots <= upper)
    candidates = np.concatenate((vals, roots[good], [0.]))
    if nonnegative:
        candidates = candidates[candidates >= 0]
    k = np.searchsorted(vals, candidates, side="left")
    numerator = (k*candidates-sums[k])/nq
    denominator = area*candidates*candidates+2*integral*candidates+norm
    ratios = np.divide(numerator, denominator, out=np.full_like(numerator, -np.inf),
                       where=denominator > max(1., norm)*1e-14)
    idx = np.argmax(ratios)
    return dict(shift=float(candidates[idx]), ratio=float(ratios[idx]),
                numerator=float(numerator[idx]), denominator=float(denominator[idx]),
                mean_rank=float(k[idx]/nq))

def audit(path, cutoff=None, nq=None):
    saved = np.load(path)
    lattice = str(saved["lattice"])
    cutoff = int(saved["cutoff"]) if cutoff is None else cutoff
    nq = int(saved["nq"]) if nq is None else nq
    p = BlochProblem(cutoff, nq, lattice)
    if p.ngrid < len(saved["hat"]):
        raise ValueError("Cannot shrink the saved potential Fourier support")
    hat = resize_hat(saved["hat"], p.ngrid)
    potential = hat[p.diff0, p.diff1]
    spectra = []
    for kinetic in p.kin:
        H = -potential.copy()
        H[p.diag] += kinetic
        spectra.append(eigh(H, eigvals_only=True, check_finite=False))
    spectra = np.array(spectra)
    d = float(p.area*np.sum(abs(hat)**2))
    u = float(p.area*hat[0, 0].real)
    raw = best_shift(spectra, p.area, u, d)
    patch = best_shift(spectra+p.patch_cost, p.area, u, d)
    raw_pos = best_shift(spectra, p.area, u, d, nonnegative=True)
    patch_pos = best_shift(spectra+p.patch_cost, p.area, u, d, nonnegative=True)
    return dict(file=str(path), cutoff=cutoff, nq=nq, lattice=lattice,
                original_ratio=float(np.maximum(-spectra, 0).sum()/len(spectra)/d),
                original_patch_lower=float(np.maximum(-spectra-p.patch_cost, 0).sum()/len(spectra)/d),
                signed_shift=raw, signed_shift_patch_lower=patch,
                nonnegative_shift=raw_pos, nonnegative_shift_patch_lower=patch_pos,
                arithmetic_certified=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    parser.add_argument("--cutoff", type=int)
    parser.add_argument("--nq", type=int)
    parser.add_argument("--output", default="r28_periodic_baseline.json")
    args = parser.parse_args()
    rows = []
    for path in args.files:
        row = audit(path, args.cutoff, args.nq)
        rows.append(row)
        print(json.dumps(row), flush=True)
    Path(args.output).write_text(json.dumps(rows, indent=2)+"\n")

if __name__ == "__main__":
    main()
