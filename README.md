# Negative-Energy Global Solutions and Traveling-Wave Mass Gaps in Mass-Critical Dispersive Equations

**Shuxing Yang · Personal research repository · 28 October 2026**

[中文说明](README.zh-CN.md) · [Complete results index](docs/results.md) · [Prior-work correspondence](docs/prior-work.md) · [Reproduction](docs/reproduce.md)

## Abstract

Negative energy is central to blowup criteria for focusing dispersive equations, but its consequences beyond radial symmetry depend on the interaction between dispersion and momentum. We construct nonradial, global negative-energy solutions of the mass-critical biharmonic Schrödinger equation in dimensions three and four by continuing excited standing waves with negative momentum response. Computer-assisted estimates certify the required profile and spectral inputs. In four dimensions, nonlinear gluing produces zero-total-momentum, forward-global solutions with uniformly bounded Sobolev norms, both as separating two-wave states and as a single coherent core coupled to momentum-cancelling radiation. For a prescribed core, we determine the exact infimum of the radiation mass compatible with negative total energy. Complementing these constructions, we prove a uniform positive gap between the critical mass and the mass of every negative-energy traveling profile for real-even, positive elliptic homogeneous dispersion. A quantitative residual estimate extends this obstruction to approximate profiles without spatial-moment assumptions. The same phase-coercivity mechanism yields a uniform intrinsic-energy mass gap for a three-dimensional cubic mixed-dispersion model with nonnegative transverse quadratic corrections. Spectral instability, conserved-quantity geometry, and localized transport further constrain the resulting dynamics. The constructions rule out an unconditional nonradial extension of negative-energy blowup or growup, while the mass-gap results separate this coherent mechanism from the critical variational threshold.

## One scientific question

**How can negative energy persist globally in mass-critical focusing dynamics, and how close can its coherent mechanisms come to the critical mass?**

The construction and exclusion theorems answer complementary parts of this question. Excited-state phase response supplies negative-energy motion; momentum cancellation produces exact zero-momentum dynamics; phase coercivity near variational optimizers creates a uniform traveling-wave mass gap. The mixed-dispersion extension tests the same mechanism in an anisotropic model relevant to optical modeling.

## Read the work

| Material | Entry point |
|---|---|
| Unified title and abstract | [English](paper/abstract.md), [Chinese](paper/abstract.zh-CN.md), [LaTeX](paper/title-and-abstract.tex) |
| Complete theorem and dependency map | [Results](docs/results.md) |
| Constructions, generalization, and dynamical extensions | [Research source index](research/INDEX.md) |
| Existing manuscript PDFs | [Manuscripts](manuscripts/INDEX.md) |
| Full original inputs, code, logs, and certificates | [Archive manifest](provenance/sources.json); restore with `python3 scripts/restore_archives.py` |
| Open questions and optical continuation | [Research status](docs/research-status.md) |

This repository collects the **first research class**, including its original proof packages and subsequent coherent-dynamics extensions. The manuscript PDFs are successive research manuscripts; the unified title and abstract identify one integrated work. A fully merged journal submission is not represented as already assembled.

## Reproduce

```sh
python3 scripts/restore_archives.py
python3 scripts/verify_integrity.py
```

The first command verifies every archive and reconstructs the original packages under `work/`, including all numerical inputs. See [the reproduction guide](docs/reproduce.md) for the N3/N4 interval verifiers. `research/` provides byte-identical, browsable copies of text sources; the complete original packages, including large data, are in `archives/`.

The mathematical statements use the accompanying analytic arguments and, where specified, computational certificates. Internal checks and recorded verifier outputs are preserved; external peer review and historical-priority assessment remain separate. The latest optical continuation is exploratory and has not established a negative-intrinsic-energy wave in the mixed model.

Copyright © 2026 Shuxing Yang. All rights reserved. This private research snapshot grants no open-source license.
