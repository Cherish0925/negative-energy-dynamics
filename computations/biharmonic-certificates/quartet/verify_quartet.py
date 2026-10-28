#!/usr/bin/env python3
"""Recompute all new quartet interval certificates from frozen exact inputs."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
for cmd in [["round5_n4_mixed_residual.py"],["round5_n4_refinement_certificate.py"],["round5_radial_verify_block.py","2"],["round5_radial_contour.py"],["round5_radial_quartet_certificate.py"]]:
    subprocess.run([sys.executable,*cmd],cwd=root,check=True)
print("PASS: exact-Q radial quartet certificate; see the accompanying theorem for analytic/base dependencies.")
