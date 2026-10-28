"""Exploratory periodic gamma=1 Lieb--Thirring Galerkin search.

Potential sign convention H=-Delta-V, V>=0. Bloch averages are normalized
fractional reciprocal-cell averages. All Fourier coefficients of the
Galerkin density (including frequencies beyond the orbital cutoff) are
retained, so the next potential is a nonnegative trigonometric polynomial.
Floating-point values are not certified bounds. `patch_lower` also deducts
the explicit fixed-projector Bloch patch correction; only arithmetic errors
remain to be certified if this ever exceeds the proposed sharp constant.
"""
import argparse
import json
import time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh

class BlochProblem:
    def __init__(self, cutoff=6, nq=6, lattice="square"):
        self.cutoff, self.nq, self.lattice = cutoff, nq, lattice
        shape = np.eye(2) if lattice == "square" else np.array([[1., .5], [0., np.sqrt(3)/2]])
        self.cell = 2*np.pi*shape
        self.area = abs(np.linalg.det(self.cell))
        self.B = 2*np.pi*np.linalg.inv(self.cell).T
        ns = np.arange(-cutoff, cutoff+1)
        self.n = np.stack(np.meshgrid(ns, ns, indexing="ij"), axis=-1).reshape(-1, 2)
        self.nbasis = len(self.n)
        # 4m+1 represents all density Fourier modes without aliasing.
        self.ngrid = 4*cutoff+1
        dn = self.n[:, None, :] - self.n[None, :, :]
        self.diff0 = dn[..., 0] % self.ngrid
        self.diff1 = dn[..., 1] % self.ngrid
        qs = (np.arange(nq)+.5)/nq-.5
        self.qs = np.stack(np.meshgrid(qs, qs, indexing="ij"), axis=-1).reshape(-1, 2)
        self.kin = np.sum(((self.n[None, :, :]+self.qs[:, None, :]) @ self.B.T)**2, axis=-1)
        self.patch_cost = np.trace(self.B.T @ self.B)/(12*nq*nq)
        self.diag = np.diag_indices(self.nbasis)

    def initial(self, target_norm, width=.8, perturb=0., seed=0):
        frequencies = np.fft.fftfreq(self.ngrid)*self.ngrid
        ks = np.stack(np.meshgrid(frequencies, frequencies, indexing="ij"), axis=-1)
        g2 = np.sum((ks @ self.B.T)**2, axis=-1)
        hat = np.exp(-width**2*g2/2)
        values = np.fft.ifft2(hat).real*self.ngrid**2
        if perturb:
            rng = np.random.default_rng(seed)
            # Nonnegative real perturbation, no imposed point-group symmetry.
            values = np.maximum(values, 0)*(1+perturb*rng.random(values.shape))
        hat = np.fft.fft2(values)/self.ngrid**2
        return hat*np.sqrt(target_norm/(self.area*np.sum(abs(hat)**2)))

    def evaluate(self, hat, density=False):
        potential = hat[self.diff0, self.diff1]
        spectra, patch_spectra, ranks = [], [], []
        rho = np.zeros((self.ngrid, self.ngrid)) if density else None
        for kinetic in self.kin:
            H = -potential.copy()
            H[self.diag] += kinetic
            if density:
                vals, vecs = eigh(H, subset_by_value=(-np.inf, 0.), check_finite=False, driver="evr")
            else:
                vals = eigh(H, subset_by_value=(-np.inf, 0.), check_finite=False, driver="evr", eigvals_only=True)
            spectra.append(float(-vals.sum()))
            patch_spectra.append(float(np.maximum(0, -vals-self.patch_cost).sum()))
            ranks.append(len(vals))
            if density and len(vals):
                coeff = np.zeros((self.ngrid, self.ngrid, len(vals)), dtype=complex)
                coeff[self.n[:, 0] % self.ngrid, self.n[:, 1] % self.ngrid, :] = vecs
                waves = np.fft.ifft2(coeff, axes=(0, 1))*self.ngrid**2
                rho += np.sum(abs(waves)**2, axis=-1)/(self.area*len(self.qs))
        denominator = self.area*np.sum(abs(hat)**2)
        spectra, ranks = np.asarray(spectra), np.asarray(ranks)
        info = dict(ratio=float(spectra.mean()/denominator),
                    patch_lower=float(np.mean(patch_spectra)/denominator),
                    norm=float(denominator), mean_rank=float(ranks.mean()),
                    min_rank=int(ranks.min()), max_rank=int(ranks.max()),
                    lattice=self.lattice, cutoff=self.cutoff, nq=self.nq)
        return info, rho

    def optimize(self, target_norm, width=.8, steps=40, perturb=0., seed=0, initial_hat=None):
        hat = self.initial(target_norm, width, perturb, seed) if initial_hat is None else initial_hat.copy()
        history = []
        for iteration in range(steps):
            info, rho = self.evaluate(hat, density=True)
            history.append(info["ratio"])
            new = np.fft.fft2(rho)/self.ngrid**2
            new *= np.sqrt(target_norm/(self.area*np.sum(abs(new)**2)))
            change = float(np.linalg.norm(new-hat)/np.linalg.norm(hat))
            hat = new
            if change < 2e-8:
                break
        info, _ = self.evaluate(hat)
        info.update(iterations=iteration+1, change=change, initial_width=width,
                    monotone_min_step=float(np.min(np.diff(history))) if len(history)>1 else 0.)
        return hat, info

def resize_hat(hat, newgrid):
    oldgrid = len(hat)
    freq = np.rint(np.fft.fftfreq(oldgrid)*oldgrid).astype(int)
    result = np.zeros((newgrid, newgrid), dtype=complex)
    for i, n in enumerate(freq):
        for j, k in enumerate(freq):
            if abs(n) <= newgrid//2 and abs(k) <= newgrid//2:
                result[n % newgrid, k % newgrid] = hat[i, j]
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=6)
    parser.add_argument("--nq", type=int, default=6)
    parser.add_argument("--steps", type=int, default=40)
    parser.add_argument("--lattice", choices=["square", "triangular"], default="square")
    parser.add_argument("--norms", type=float, nargs="+", default=[4, 12, 24, 48, 96])
    parser.add_argument("--output", default="research/r28_periodic_square")
    args = parser.parse_args()
    problem = BlochProblem(args.cutoff, args.nq, args.lattice)
    results = []
    for norm in args.norms:
        start = time.time()
        width = min(1.5, np.sqrt(12/norm))
        hat, info = problem.optimize(norm, width, args.steps, perturb=.03, seed=28)
        info["seconds"] = time.time()-start
        results.append(info)
        np.savez(args.output+f"_D{norm:g}.npz", hat=hat, **info)
        print(json.dumps(info), flush=True)
    Path(args.output+".json").write_text(json.dumps(results, indent=2)+"\n")

if __name__ == "__main__":
    main()
