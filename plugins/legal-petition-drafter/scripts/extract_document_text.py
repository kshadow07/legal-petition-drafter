"""Extract UTF-8 text from a PDF for review; OCR is deliberately not treated as proof."""
from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    reader = PdfReader(args.pdf)
    text = "\n\n".join(
        f"--- PAGE {index} ---\n{page.extract_text() or ''}"
        for index, page in enumerate(reader.pages, start=1)
    )
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
