#!/usr/bin/env python3
"""Restore and verify the original research source packages."""
from pathlib import Path
import hashlib
import io
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    manifest = json.loads((ROOT / 'provenance/sources.json').read_text())
    count = 0
    for archive in manifest['archives']:
        chunks = []
        for part in archive['parts']:
            data = (ROOT / part['path']).read_bytes()
            if len(data) != part['bytes'] or digest(data) != part['sha256']:
                raise ValueError('Archive part differs: ' + part['path'])
            chunks.append(data)
        raw = b''.join(chunks)
        if len(raw) != archive['bytes'] or digest(raw) != archive['sha256']:
            raise ValueError('Archive differs: ' + archive['archive'])
        destination = ROOT / 'work' / archive['bundle']
        expected = {f['path']: f for f in archive['files']}
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            actual = [i.filename for i in z.infolist() if not i.is_dir()]
            if set(actual) != set(expected) or len(actual) != len(expected):
                raise ValueError('Archive membership differs: ' + archive['archive'])
            for name in actual:
                rel = Path(name)
                if rel.is_absolute() or '..' in rel.parts:
                    raise ValueError('Unsafe archive path: ' + name)
                data = z.read(name)
                record = expected[name]
                if len(data) != record['bytes'] or digest(data) != record['sha256']:
                    raise ValueError('Source differs: ' + name)
                out = destination / rel
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(data)
                count += 1
        print('Restored:', archive['bundle'], '(' + str(len(actual)) + ' files)')
    print('Verified and restored', count, 'original files in', len(manifest['archives']), 'packages.')

if __name__ == '__main__':
    main()
