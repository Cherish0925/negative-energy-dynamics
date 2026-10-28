"""Aggregate the N3 certificates and check quantitative traveling-wave constants.
Run with --verify-all to rerun the constituent rigorous verifiers first.
No numerical provenance generation is required except the independently
Arb-checked finite-matrix eigensystem in the radial certificate.
"""
import sys,json,hashlib,subprocess
from flint import arb,ctx
ctx.prec=192
QHASH='5d2a86dc991fe960e7036ca651634c556ded9da4aa7d1ae357ab5f4f656d526b'
COUNTS={2:5,3:3,4:5,5:1,6:3,8:2,10:2,12:1,14:1}
if '--verify-all' in sys.argv:
 commands=[['round4_n3_verify_mixed.py','1'],['round5_n3_radial_certificate.py'],['round5_n3_pairing_hs.py'],['round5_n3_pairing_bs_verify.py'],['round5_n3_pairing_verify.py']]
 for ell,n in COUNTS.items():commands.extend([['round5_n3_channels_hs.py',str(ell)],['round5_n3_channels_verify.py',str(ell),str(n)]])
 commands.append(['round5_n3_channels_hs.py','16'])
 for cmd in commands:
  print('VERIFY',*cmd,flush=True);subprocess.run([sys.executable,*cmd],check=True)
def read(p):return json.load(open(p))
q=read('round4_n3_mixed_certificate_sub1.json');rad=read('round5_n3_radial_certificate.json');dip=read('round5_n3_pairing_bs_certificate.json');pair=read('round5_n3_pairing_certificate.json');high=read('round5_n3_channels_hs_l16_sub1.json')
assert hashlib.sha256(open('round4_n3_mixed_exact.json','rb').read()).hexdigest()==QHASH
for data,key in [(q,'profile_sha256'),(rad,'profile_sha256'),(dip,'q_sha256'),(pair,'q_sha256'),(high,'profile_sha256')]:assert data[key]==QHASH
rho=arb(4)/10**6;v=arb(1)/10**9;B=arb(200);G=arb(3)/5
assert arb(q['PDE_residual_Hminus2_Zdual_upper'])<arb(13)/10**8
assert arb(rad['whole_space_gap_lower'])>arb(1)/25
assert arb(q['Z_norm_upper'])+rho<137
assert arb(q['Linfty_upper'])+rho/4<arb('6.300001')
# Newton map at q on the rho ball.
assert 25*arb(13)/10**8+25*arb(211)/8*rho**2<rho
assert 25*arb(211)/4*rho<1
# Full real-even / imaginary-odd symmetry inverse.
assert dip['all_checks_pass'] and dip['Lminus_Q_ell1_inverse_norm_lt']==200
channel_rows=[]
for ell in COUNTS:
 row=read(f'round5_n3_channels_certificate_l{ell}.json');assert row['q_sha256']==QHASH and row['all_checks_pass']
 assert arb(row['Q_preconditioned_gap_lower'])>arb(1)/200
 if ell==5:assert row['Q_negative_index_per_angular_mode']==0
 channel_rows.append({'ell':ell,'operator':'plus' if ell%2==0 else 'minus','Q_gap_lower':row['Q_preconditioned_gap_lower'],'negative_index_per_mode':row['Q_negative_index_per_angular_mode']})
pluspert=arb(11)/3*arb(58)/10**6
highgap=1-arb(high['HS_squared_upper']).sqrt()-pluspert
assert highgap>arb(1)/200 and high['ell']==16
assert arb(rad['whole_space_gap_lower'])-pluspert>arb(1)/200
# Exact response z=Lminus(Q)^-1 partial_1 Q.
ztrial=arb(pair['norm_Z_trial_upper']);rq=arb(pair['exact_Q_response_residual_upper']);zbound=ztrial+B*rq
assert zbound<818 and arb(pair['I_Q_upper'])<-1280
# Complex-vector nonlinearity g(w)=|w|^(8/3)w has ||D²g|| <=(88/9)|w|^(5/3).
R=1000*v
assert arb(88)/9*(arb('6.300001')+R/4)**(arb(5)/3)<211
remcoef=B*(arb(211)/8*1000**2+G*1000)
mapbound=818*v+remcoef*v*v
lip=B*(arb(211)/4*R+G*v)
assert mapbound<R and lip<1
# w(v)=-ivz+r, ||w||Z<=1000|v|, ||r||Z<=remcoef v².
# P error <= sqrt(2)||Q||Z ||r||Z + ||w||Z²/sqrt(2).
pcoef=arb(2).sqrt()*137*remcoef+arb(1000**2)/arb(2).sqrt()
assert pcoef<arb(11)*10**11
energycoef=(2*arb(1280)-pcoef*v)/8
assert energycoef>180
out={'status':'complete quantitative N3 mass-critical nonradial negative-energy traveling-wave theorem, conditional only on validity of the supplied analytic proofs and reproducible arithmetic certificates','profile_sha256':QHASH,'exact_Q_Z_distance_lt':'4e-6','symmetry':'f(-x)=conjugate(f(x))','full_symmetry_linearization_inverse_lt':200,'dipole_inverse_pairing_lt':-1280,'exact_dipole_response_Z_norm_lt':818,'speed_range':'0<|v|<=1e-9','U_v_minus_Q_Z_norm_le':'1000|v|','energy_upper':'E(U_v)<-180 v^2','fixed_point_contraction_upper_at_endpoint':str(lip.upper()),'fixed_point_radius':'1000|v|','quadratic_correction_coefficient':str(remcoef),'momentum_quadratic_error_coefficient_upper':str(pcoef.upper()),'certified_energy_coefficient_lower':str(energycoef.lower()),'even_ell_ge16_Q_gap_lower':str(highgap.lower()),'odd_ell_ge5_Q_gap_lower':next(x['Q_gap_lower'] for x in channel_rows if x['ell']==5),'finite_channels':channel_rows,'all_checks_pass':True,'precision_bits':ctx.prec}
print(json.dumps(out,indent=2));open('round5_n3_theorem.json','w').write(json.dumps(out,indent=2)+'\n')
