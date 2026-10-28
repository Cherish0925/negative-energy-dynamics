#!/usr/bin/env python3
"""Run the N4 certificate chain; --full also recomputes all Arb HS integrals."""
from pathlib import Path
import argparse,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent
D=ROOT/'verification'/'N4'
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--full',action='store_true',help='Recompute all five interval HS integrations before downstream checks.')
a=p.parse_args()
def run(name,*args,cwd=D):
 print('VERIFY',name,*args,flush=True)
 subprocess.run([sys.executable,str(cwd/name),*map(str,args)],cwd=cwd,check=True)
run('round2_verify_frozen_ritz.py')
run('round2_certificate_canonical.py')
run('round2_radial_highangular.py')
if a.full:
 work=D/'round4_morse_work'
 for ell in range(5):
  run('round2_certified_birman_hs.py',ell,16,cwd=work)
  name=f'round2_certified_birman_l{ell}_sub16.json'
  shutil.copy2(work/name,D/name)
run('round2_final_rational_implication.py')
run('round4_ell3_rayleigh.py')
run('round4_verify_morse.py')
run('round5_n4_mixed_residual.py')
run('round5_n4_refinement_certificate.py')
print('N4 verification chain completed; HS integrals '+('recomputed.' if a.full else 'read from supplied interval outputs; use --full to recompute.'))
