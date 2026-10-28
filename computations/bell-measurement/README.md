# Six-mode linear-optical Bell measurement

Exact reproduction of Olivo–Grosshans, *Investigating the optimality of ancilla-assisted linear optical Bell measurements*, Phys. Rev. A 98, 042323 (2018), Section IV.C. [Primary paper](https://arxiv.org/abs/1806.01243).

The model has four equiprobable dual-rail Bell states, two separable ancillary photons, passive lossless optics, and ideal photon-number-resolving detectors. The 126 output patterns yield conditional success probabilities 1/4, 1/4, 1, 1 and mean 5/8. This is a reproduction of the known scheme.

Run `python3 verify_bell_5over8.py`; SymPy is required. `baseline_report.json` contains the exact mode matrix and every outcome probability.
