"""Check that a structured draft has its basic lawyer-review fields."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FIELDS = ("court", "matter_type", "parties", "facts", "prayer", "language")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("draft_json", type=Path)
    args = parser.parse_args()
    data = json.loads(args.draft_json.read_text(encoding="utf-8"))
    missing = [field for field in REQUIRED_FIELDS if not data.get(field)]
    result = {
        "status": "needs factual confirmation" if missing else "ready for advocate review",
        "missing_required_fields": missing,
        "notice": "This validation does not establish legal correctness or filing readiness.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
