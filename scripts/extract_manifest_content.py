from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_INPUT = Path.home() / "Desktop" / "manifest.json"
DEFAULT_OUTPUT = Path.home() / "Desktop" / "manifest_content.txt"


def extract_contents(manifest_path: Path) -> list[str]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    notes = data.get("notes")
    if not isinstance(notes, list):
        raise ValueError("manifest.json must contain a top-level notes list")

    contents: list[str] = []
    for index, note in enumerate(notes, start=1):
        if not isinstance(note, dict):
            raise ValueError(f"notes[{index}] must be an object")

        content = note.get("content")
        if content is None:
            continue
        if not isinstance(content, str):
            raise ValueError(f"notes[{index}].content must be a string")

        contents.append(content)

    return contents


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract notes[*].content from a manifest JSON file."
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"Manifest JSON path. Default: {DEFAULT_INPUT}",
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
    contents = extract_contents(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n---\n\n".join(contents), encoding="utf-8")
    print(f"Wrote {len(contents)} content fields to {args.output}")


if __name__ == "__main__":
    main()
