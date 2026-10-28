#!/usr/bin/env python3
"""Generate SHA256SUMS.txt, or check it with --check. No symlinks are accepted."""
from pathlib import Path
import argparse,hashlib
ROOT=Path(__file__).resolve().parent
DEST=ROOT/'SHA256SUMS.txt'
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--check',action='store_true')
a=p.parse_args()
def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
if a.check:
 rows=DEST.read_text().splitlines()
 for row in rows:
  sha,name=row.split('  ',1)
  path=ROOT/name
  if path.is_symlink() or not path.is_file() or digest(path)!=sha:raise SystemExit('FAILED '+name)
 print(f'PASS: {len(rows)} file hashes match.')
else:
 files=[]
 for path in ROOT.rglob('*'):
  if path.is_symlink():raise SystemExit('Symlink not permitted: '+str(path))
  if not path.is_file() or path==DEST or '__pycache__' in path.parts or path.suffix=='.pyc':continue
  files.append(path)
 DEST.write_text(''.join(f'{digest(path)}  {path.relative_to(ROOT).as_posix()}\n' for path in sorted(files)))
 print(f'Wrote {len(files)} hashes to {DEST.name}.')
