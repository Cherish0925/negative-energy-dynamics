#!/usr/bin/env python3
"""Verify the repository snapshot and any restored source files."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]

def main():
    manifest = json.loads((ROOT / 'provenance/repository-files.json').read_text())
    for item in manifest['files']:
        data = (ROOT / item['path']).read_bytes()
        if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
            raise ValueError('Repository file differs: ' + item['path'])
    print('Verified', len(manifest['files']), 'repository files.')
    source = json.loads((ROOT / 'provenance/sources.json').read_text())
    count = 0
    for archive in source['archives']:
        base = ROOT / 'work' / archive['bundle']
        if not base.exists():
            continue
        for item in archive['files']:
            data = (base / item['path']).read_bytes()
            if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
                raise ValueError('Restored file differs: ' + str(base / item['path']))
            count += 1
    print('Verified', count, 'restored original files.')

if __name__ == '__main__':
    main()
