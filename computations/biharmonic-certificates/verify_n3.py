#!/usr/bin/env python3
"""Run the aggregate N3 certificate; --full reruns every constituent verifier."""
from pathlib import Path
import argparse,subprocess,sys
ROOT=Path(__file__).resolve().parent
D=ROOT/'verification'/'N3'
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--full',action='store_true',help='Rerun all mixed-residual, radial, dipole and angular certificates.')
a=p.parse_args()
cmd=[sys.executable,str(D/'round5_n3_theorem.py')]
if a.full:cmd.append('--verify-all')
subprocess.run(cmd,cwd=D,check=True)
