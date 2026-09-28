"""Smoke metrics for the hormozi answer-shape change.

Usage: python3 metrics.py <sheets_dir> <answer.md> [<answer.md> ...]
For each answer: words, the basis block (a line naming «Основания» or "Basis"),
rule numbers above it and inside it, existence of every cited rule in the
sheets, "метод" and source years in the body.
"""
import re
import sys
from pathlib import Path

RULE = re.compile(r"(?<![\d.])(0[1-9]|1[0-6])\.([1-9]\d?)(?![\d])")
BASIS = re.compile(r"^\W*(основания|basis)\b", re.IGNORECASE)
YEAR = re.compile(r"\b20(2[1-5])\b")
METHOD = re.compile(r"метод", re.IGNORECASE)


def headings(sheets_dir):
    found = set()
    for f in Path(sheets_dir).glob("*.md"):
        for m in re.finditer(r"^#### (\d\d\.\d+)\.", f.read_text(), re.MULTILINE):
            found.add(m.group(1))
    return found


def split(text):
    lines = text.splitlines()
    for i in range(len(lines) - 1, -1, -1):
        if BASIS.match(lines[i].replace("*", "").replace("#", "").strip()):
            return "\n".join(lines[:i]), "\n".join(lines[i:])
    return text, ""


def main():
    known = headings(sys.argv[1])
    for path in sys.argv[2:]:
        text = Path(path).read_text()
        body, block = split(text)
        body_rules = [f"{a}.{b}" for a, b in RULE.findall(body)]
        block_rules = [f"{a}.{b}" for a, b in RULE.findall(block)]
        cited = sorted(set(body_rules + block_rules))
        missing = [r for r in cited if r not in known]
        block_lines = [l for l in block.splitlines()[1:] if l.strip()]
        print(f"== {Path(path).name}")
        print(f"  words total {len(text.split())}, body {len(body.split())}")
        print(f"  basis block: {'yes' if block else 'no'}, lines {len(block_lines)}")
        print(f"  rule numbers in body {len(body_rules)}, in block {len(block_rules)}, distinct {len(cited)}")
        print(f"  rules not in the sheets: {missing or 'none'}")
        print(f"  'метод' in body {len(METHOD.findall(body))}, source years in body {len(YEAR.findall(body))}")


if __name__ == "__main__":
    main()
