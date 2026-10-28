Purpose: direct attempts to continue a known three-dimensional negative-response
excited state into the cubic mixed optical model. No target-model negative-energy
traveling wave was obtained. Read Core_Continuation_State_20261019.txt first.

Requirements: Python 3, NumPy, SciPy. Run commands from the unzipped root.

Finite-volume path:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 core_continuation/continue_core.py --n 128 --L 24 --out new_run

Independent spectral starting-state check:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 core_continuation/spectral_core.py --nt 256 --nr 128 --start 0 --end 0 --seed core_continuation/run128/core_0.000000.npz --out new_baseline

The config.json files retain arguments for completed ordinary continuation runs.
The arclength scripts accept --first and --second NPZ files and an output folder.
The final spectral_arclength run was interrupted by an execution-service failure;
only its recorded failed trials and code are retained. It supplies no new solution.

All reported equation residuals are discretized residuals. No interval certificate,
infinite-domain enclosure, spectral-stability theorem or optical experiment is
claimed. The mixed auxiliary path is subcritical at intermediate parameter values.
Do not interpret negative energy there as a counterexample for the target model.

The input seed is included at the original relative path required by continue_core.py.
It comes from the project's frozen 7 October data. This archive does not rerun or
replace the earlier proof certificates. See manifest.json for this run's file hashes.
