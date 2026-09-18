"""Render a PDF into PNG pages using Poppler for visual QA."""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--dpi", type=int, default=150)
    args = parser.parse_args()

    renderer = shutil.which("pdftoppm")
    if renderer is None:
        raise SystemExit("pdftoppm is required for PDF visual QA but was not found on PATH.")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.output_dir / "page"
    subprocess.run(
        [renderer, "-png", "-r", str(args.dpi), str(args.pdf), str(prefix)],
        check=True,
    )


if __name__ == "__main__":
    main()
