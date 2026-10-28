#!/usr/bin/env python3
"""Recompute every finite certificate used in the accompanying BNLS proof.

This runner consumes frozen exact data. It does not regenerate any profile,
perform time integration, trust convergence tables, or infer existence from
small floating-point residuals. Analytic deductions are in the manuscript.
"""
from pathlib import Path
import subprocess,sys,json,hashlib,time,platform
root=Path(__file__).resolve().parent
logs=root/'verification_logs';logs.mkdir(exist_ok=True)
commands=[('frozen_residual_and_ritz',['round2_verify_frozen_ritz.py']),('response',['round2_certificate_canonical.py']),('high_angular',['round2_radial_highangular.py'])]
commands += [('birman_channel_%d'%ell,['round2_certified_birman_hs.py',str(ell),'16']) for ell in [0,1,2,3,4]]
commands += [('analytic_implication',['round2_final_rational_implication.py'])]
results=[]
for name,args in commands:
 start=time.monotonic()
 with (logs/(name+'.log')).open('w') as f:
  result=subprocess.run([sys.executable]+args,cwd=root,stdout=f,stderr=subprocess.STDOUT)
 elapsed=time.monotonic()-start
 print(name, 'PASS' if result.returncode==0 else 'FAIL','%.2fs'%elapsed,flush=True)
 if result.returncode:raise SystemExit('Certificate failed; see '+str(logs/(name+'.log')))
 results.append({'component':name,'returncode':0,'seconds':elapsed})
def read(name):return json.loads((root/name).read_text())
ritz=read('round2_verify_frozen_ritz_results.json');assert ritz['verified'] and all(ritz['checks'].values())
response=read('round2_certificate_canonical_results.json');assert all(response['exact_boolean_checks'].values())
high=read('round2_radial_highangular_certificate.json');assert all(v['all_Bernstein_coefficients_positive'] for v in high['checks'])
bs=[read('round2_certified_birman_l%d_sub16.json'%ell) for ell in range(5)]
assert all(v['required_pass'] for v in bs)
imp=read('round2_final_rational_implication.json');assert imp['all_checks_pass']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
profile=root/'round2_radial_H4_exact_h1_16.json';profile_sha=sha(profile)
assert profile_sha=='c50a6f98682ce5f5bef9ab62ae2a93ba06b91522c8f3e29b859ac521afb8f627'
assert ritz['sha256']['profile']==profile_sha and high['sha256']==profile_sha
assert all(v['profile_sha256']==profile_sha for v in bs)
summary={'status':'ALL FINITE CERTIFICATES PASSED','note':'Together with the analytic proof in the manuscript, these establish the four-dimensional counterexample. This is not a formal proof-assistant verification or external peer review.','python':platform.python_version(),'canonical_profile_sha256':profile_sha,'components':results,'BS_required_enclosures':[{k:v[k] for k in ['ell','required_inequality','required_pass','HS_squared_upper_endpoint_enclosure','trace_upper_endpoint_enclosure']} for v in bs],'I_upper_exact':imp['values']['I_upper']['exact_fraction'],'data_and_verifier_hashes':{p.name:sha(p) for p in sorted(root.iterdir()) if p.suffix=='.py' or p.name in ['round2_radial_H4_exact_h1_16.json','round2_ritz_exact_data.json','round2_certificate_exact_rational_data.json']}}
(root/'VERIFICATION_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
print(summary['status'],flush=True)
print('I upper bound:',summary['I_upper_exact'],'< -175',flush=True)
