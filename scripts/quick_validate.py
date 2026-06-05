from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
LOCAL_REF_RE = re.compile(r"`((?:(?:\.\./[a-z0-9-]+/)?(?:references|agents))/[^`]+?)`")
SKILL_REF_RE = re.compile(r"\$((?:cflow)(?:-[a-z0-9]+)*)\b")
CFLOW_LIST_RE = re.compile(r"-\s+`\$((?:cflow)(?:-[a-z0-9]+)*)`")
NAME_RE = re.compile(r"^cflow(?:-[a-z0-9]+)*$")
ASSET_REQUIRED_SCALARS = {
    "asset_name",
    "asset_type",
    "use_when",
    "avoid_when",
    "evidence_level",
    "overuse_risk",
    "source",
}
ASSET_REQUIRED_LISTS = {"skills", "triggers"}


@dataclass(frozen=True)
class Issue:
    level: str
    path: Path
    message: str

    def format(self, root: Path) -> str:
        try:
            display_path = self.path.relative_to(root)
        except ValueError:
            display_path = self.path
        return f"{self.level} {display_path}: {self.message}"


def parse_simple_mapping(raw: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        data[key.strip()] = value
    return data


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str, str | None]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text, "missing frontmatter block"
    return parse_simple_mapping(match.group(1)), text[match.end() :], None


def parse_asset_mapping(raw: str) -> dict[str, str | list[str]]:
    data: dict[str, str | list[str]] = {}
    current_list_key: str | None = None

    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        stripped = line.strip()
        if stripped.startswith("- ") and current_list_key:
            value = stripped[2:].strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1]
            existing = data.setdefault(current_list_key, [])
            if isinstance(existing, list):
                existing.append(value)
            continue

        current_list_key = None
        if ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]

        if value:
            data[key] = value
        else:
            data[key] = []
            current_list_key = key

    return data


def parse_agent_yaml(path: Path) -> tuple[dict[str, dict[str, str]], str | None]:
    lines = path.read_text(encoding="utf-8").splitlines()
    data: dict[str, dict[str, str]] = {}
    current_section: str | None = None

    for line_number, line in enumerate(lines, start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if ":" not in stripped:
            return data, f"line {line_number} is not a key-value pair"

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()

        if indent == 0:
            if value:
                return data, f"line {line_number} top-level key must be a mapping"
            current_section = key
            data[current_section] = {}
            continue

        if indent != 2 or current_section is None:
            return data, f"line {line_number} has unsupported indentation"

        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        data[current_section][key] = value

    return data, None


def find_skill_dirs(skills_dir: Path) -> list[Path]:
    if not skills_dir.exists():
        return []
    return sorted(path for path in skills_dir.iterdir() if path.is_dir())


def validate_skill(skill_dir: Path, skill_names: set[str]) -> list[Issue]:
    issues: list[Issue] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return [Issue("FAIL", skill_dir, "missing SKILL.md")]

    metadata, body, frontmatter_error = parse_frontmatter(skill_md)
    if frontmatter_error:
        issues.append(Issue("FAIL", skill_md, frontmatter_error))
    else:
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not name:
            issues.append(Issue("FAIL", skill_md, "frontmatter missing name"))
        elif not NAME_RE.match(name):
            issues.append(Issue("FAIL", skill_md, f"invalid skill name {name!r}"))
        elif name != skill_dir.name:
            issues.append(Issue("FAIL", skill_md, f"name {name!r} does not match directory {skill_dir.name!r}"))

        if not description.strip():
            issues.append(Issue("FAIL", skill_md, "frontmatter missing description"))

    for match in LOCAL_REF_RE.finditer(body):
        relative_ref = match.group(1).replace("/", "\\")
        target = skill_dir / relative_ref
        if not target.exists():
            issues.append(Issue("FAIL", skill_md, f"missing local reference {match.group(1)!r}"))

    for match in SKILL_REF_RE.finditer(body):
        ref = match.group(1)
        if ref not in skill_names:
            issues.append(Issue("FAIL", skill_md, f"references missing skill ${ref}"))

    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if agent_yaml.exists():
        agent_data, yaml_error = parse_agent_yaml(agent_yaml)
        if yaml_error:
            issues.append(Issue("FAIL", agent_yaml, yaml_error))
        else:
            interface = agent_data.get("interface")
            if interface is None:
                issues.append(Issue("FAIL", agent_yaml, "missing interface mapping"))
            else:
                required = {"display_name", "short_description", "default_prompt"}
                extra = set(interface) - required
                missing = required - set(interface)
                if missing:
                    issues.append(Issue("FAIL", agent_yaml, f"missing interface keys: {', '.join(sorted(missing))}"))
                if extra:
                    issues.append(Issue("FAIL", agent_yaml, f"unknown interface keys: {', '.join(sorted(extra))}"))
                for key in required:
                    if not interface.get(key, "").strip():
                        issues.append(Issue("FAIL", agent_yaml, f"interface.{key} is empty"))

    return issues


def validate_cflow_index(skills_dir: Path, skill_names: set[str]) -> list[Issue]:
    cflow_md = skills_dir / "cflow" / "SKILL.md"
    if not cflow_md.exists():
        return []

    _, body, _ = parse_frontmatter(cflow_md)
    listed = set(CFLOW_LIST_RE.findall(body))
    expected = skill_names - {"cflow"}
    issues: list[Issue] = []

    missing_from_index = expected - listed
    if missing_from_index:
        issues.append(Issue("FAIL", cflow_md, "CFlow Skills list missing: " + ", ".join(sorted(missing_from_index))))

    stale_in_index = listed - expected
    if stale_in_index:
        issues.append(Issue("FAIL", cflow_md, "CFlow Skills list has stale entries: " + ", ".join(sorted(stale_in_index))))

    return issues


def validate_content_assets(root: Path, skill_names: set[str]) -> list[Issue]:
    assets_dir = root / "profiles" / "content-assets"
    if not assets_dir.exists():
        return []

    issues: list[Issue] = []
    for path in sorted(assets_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        if not match:
            issues.append(Issue("FAIL", path, "content asset missing frontmatter block"))
            continue

        metadata = parse_asset_mapping(match.group(1))
        for key in sorted(ASSET_REQUIRED_SCALARS):
            value = metadata.get(key)
            if not isinstance(value, str) or not value.strip():
                issues.append(Issue("FAIL", path, f"content asset frontmatter missing non-empty {key}"))

        for key in sorted(ASSET_REQUIRED_LISTS):
            value = metadata.get(key)
            if not isinstance(value, list) or not any(item.strip() for item in value):
                issues.append(Issue("FAIL", path, f"content asset frontmatter missing non-empty list {key}"))

        skills = metadata.get("skills")
        if isinstance(skills, list):
            for skill in skills:
                if skill and skill not in skill_names:
                    issues.append(Issue("FAIL", path, f"content asset references missing skill {skill!r}"))

    return issues


def validate_repository(root: Path) -> list[Issue]:
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return [Issue("FAIL", root, "missing skills directory")]

    skill_dirs = find_skill_dirs(skills_dir)
    skill_names = {path.name for path in skill_dirs}
    issues: list[Issue] = []

    if not skill_dirs:
        issues.append(Issue("FAIL", skills_dir, "no skill directories found"))

    for skill_dir in skill_dirs:
        if not NAME_RE.match(skill_dir.name):
            issues.append(Issue("FAIL", skill_dir, f"invalid skill directory name {skill_dir.name!r}"))
        issues.extend(validate_skill(skill_dir, skill_names))

    issues.extend(validate_cflow_index(skills_dir, skill_names))
    issues.extend(validate_content_assets(root, skill_names))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate CFlow skill suite structure.")
    parser.add_argument("root", nargs="?", default=".", help="repository root, defaults to current directory")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    issues = validate_repository(root)
    failures = [issue for issue in issues if issue.level == "FAIL"]

    if failures:
        for issue in failures:
            print(issue.format(root))
        print(f"FAIL {len(failures)} issue(s) found")
        return 1

    skill_count = len(find_skill_dirs(root / "skills"))
    print(f"OK {skill_count} skills found")
    print("OK all CFlow structural checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
