#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261125.

Writes the checked-in entry.png (a 1024x1024 summary of 25 November
2026 world news) to /output/entry.png. Standard library only, no
network, no randomness, no timestamps: two runs write identical bytes.

Usage:
    python3 main.py                 # writes /output/entry.png
    python3 main.py <output-path>   # or OUTPUT_PATH=<path> python3 main.py
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    dest = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.png")
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    print(f"wrote {dest}")


if __name__ == "__main__":
    main()
