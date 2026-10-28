#!/usr/bin/env python3
"""Build the research manuscripts, keeping TeX auxiliaries outside the sources."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def build(source, build_root):
    work = build_root / source.parent.name / source.stem
    work.mkdir(parents=True, exist_ok=True)
    command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
               "-file-line-error", "-output-directory=" + str(work), source.name]
    for run in (1, 2):
        result = subprocess.run(command, cwd=source.parent, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, timeout=120)
        (work / f"pass-{run}.txt").write_text(result.stdout)
        if result.returncode:
            return False, f"FAILED {source.relative_to(ROOT)}\n{result.stdout[-2500:]}"
    destination = source.with_suffix(".pdf")
    shutil.copy2(work / destination.name, destination)
    return True, str(destination.relative_to(ROOT))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--build-dir", type=Path)
    parser.add_argument("sources", nargs="*", help="Optional paths relative to the repository")
    args = parser.parse_args()
    if shutil.which("pdflatex") is None:
        parser.error("pdflatex is required")
    sources = [ROOT / s for s in args.sources] if args.sources else sorted(
        p for p in (ROOT / "manuscripts").rglob("*.tex")
        if "\\documentclass" in p.read_text()[:500])
    with tempfile.TemporaryDirectory(prefix="focusing-manuscripts-") as temporary:
        build_root = (args.build_dir or Path(temporary)).resolve()
        with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as executor:
            results = list(executor.map(lambda p: build(p, build_root), sources))
        for _, message in results:
            print(message)
        if not all(ok for ok, _ in results):
            raise SystemExit(1)


if __name__ == "__main__":
    main()
