from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from quick_validate import LOCAL_REF_RE, SKILL_REF_RE, find_skill_dirs, parse_agent_yaml, parse_frontmatter
except ModuleNotFoundError:
    from scripts.quick_validate import LOCAL_REF_RE, SKILL_REF_RE, find_skill_dirs, parse_agent_yaml, parse_frontmatter


def build_registry(root: Path) -> dict[str, list[dict[str, object]]]:
    skills_dir = root / "skills"
    registry: dict[str, list[dict[str, object]]] = {"skills": []}

    for skill_dir in find_skill_dirs(skills_dir):
        skill_md = skill_dir / "SKILL.md"
        metadata, body, _ = parse_frontmatter(skill_md)

        agent_path = skill_dir / "agents" / "openai.yaml"
        agent = None
        if agent_path.exists():
            agent, _ = parse_agent_yaml(agent_path)

        references = sorted({match.group(1) for match in LOCAL_REF_RE.finditer(body)})
        skill_refs = sorted({match.group(1) for match in SKILL_REF_RE.finditer(body)})

        registry["skills"].append(
            {
                "name": metadata.get("name", skill_dir.name),
                "path": str(skill_dir.relative_to(root)).replace("\\", "/"),
                "description": metadata.get("description", ""),
                "references": references,
                "agent": agent,
                "skill_refs": skill_refs,
            }
        )

    return registry


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a JSON registry from CFlow skills.")
    parser.add_argument("root", nargs="?", default=".", help="repository root, defaults to current directory")
    parser.add_argument("--output", "-o", help="write registry JSON to this file")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    registry = build_registry(root)
    payload = json.dumps(registry, ensure_ascii=False, indent=2) + "\n"

    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = root / output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
