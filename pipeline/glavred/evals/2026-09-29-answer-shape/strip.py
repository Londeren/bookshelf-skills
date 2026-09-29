"""Write a grading copy of each answer with its closing basis block cut.

Usage: python3 strip.py <out_dir> <graded_dir>
"""
import sys
from pathlib import Path

from metrics import split

out_dir, graded_dir = Path(sys.argv[1]), Path(sys.argv[2])
graded_dir.mkdir(exist_ok=True)
for f in sorted(out_dir.glob("*.md")):
    body, block = split(f.read_text())
    (graded_dir / f.name).write_text(body.rstrip() + "\n")
    print(f"{f.name}: basis block {'cut' if block else 'none'}")
