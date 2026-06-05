from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_INPUT = Path.home() / "Downloads" / "atoms.jsonl"
DEFAULT_OUTPUT = Path.home() / "Downloads" / "atoms_original.txt"


def extract_originals(jsonl_path: Path) -> list[str]:
    originals: list[str] = []

    with jsonl_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            stripped = line.strip()
            if not stripped:
                continue

            data = json.loads(stripped)
            if not isinstance(data, dict):
                raise ValueError(f"line {line_number} must be a JSON object")

            original = data.get("original")
            if original is None:
                continue
            if not isinstance(original, str):
                raise ValueError(f"line {line_number} original must be a string")

            originals.append(normalize_original_text(original))

    return originals


def normalize_original_text(text: str) -> str:
    return text.replace("\\r\\n", "\n").replace("\\n", "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract original fields from an atoms JSONL file."
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"Atoms JSONL path. Default: {DEFAULT_INPUT}",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output text path. Default: {DEFAULT_OUTPUT}",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    originals = extract_originals(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n---\n\n".join(originals), encoding="utf-8")
    print(f"Wrote {len(originals)} original fields to {args.output}")


if __name__ == "__main__":
    main()
