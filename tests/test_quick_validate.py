from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.build_registry import build_registry
from scripts.quick_validate import parse_agent_yaml, parse_frontmatter, validate_repository


class QuickValidateTests(unittest.TestCase):
    def test_parse_frontmatter_reads_name_and_description(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SKILL.md"
            path.write_text("---\nname: cflow-demo\ndescription: 示例\n---\n\n# Demo\n", encoding="utf-8")

            metadata, body, error = parse_frontmatter(path)

        self.assertIsNone(error)
        self.assertEqual(metadata["name"], "cflow-demo")
        self.assertEqual(metadata["description"], "示例")
        self.assertIn("# Demo", body)

    def test_parse_agent_yaml_reads_interface_mapping(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "openai.yaml"
            path.write_text(
                'interface:\n'
                '  display_name: "CFlow Demo"\n'
                '  short_description: "Demo"\n'
                '  default_prompt: "Use $cflow-demo"\n',
                encoding="utf-8",
            )

            data, error = parse_agent_yaml(path)

        self.assertIsNone(error)
        self.assertEqual(data["interface"]["display_name"], "CFlow Demo")

    def test_validate_repository_detects_missing_skill_reference(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = root / "skills" / "cflow"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: cflow\ndescription: 总入口\n---\n\nUse $cflow-missing\n",
                encoding="utf-8",
            )

            issues = validate_repository(root)

        self.assertTrue(any("references missing skill $cflow-missing" in issue.message for issue in issues))

    def test_validate_repository_accepts_minimal_valid_suite(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cflow = root / "skills" / "cflow"
            demo = root / "skills" / "cflow-demo"
            cflow.mkdir(parents=True)
            demo.mkdir(parents=True)
            (cflow / "SKILL.md").write_text(
                "---\nname: cflow\ndescription: 总入口\n---\n\n## CFlow Skills\n\n- `$cflow-demo`: Demo\n",
                encoding="utf-8",
            )
            (demo / "SKILL.md").write_text(
                "---\nname: cflow-demo\ndescription: 示例\n---\n\n# Demo\n",
                encoding="utf-8",
            )

            issues = validate_repository(root)

        self.assertEqual([], issues)

    def test_build_registry_extracts_skill_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cflow = root / "skills" / "cflow"
            demo = root / "skills" / "cflow-demo"
            cflow.mkdir(parents=True)
            demo.mkdir(parents=True)
            (cflow / "SKILL.md").write_text(
                "---\nname: cflow\ndescription: 总入口\n---\n\n## CFlow Skills\n\n- `$cflow-demo`: Demo\n",
                encoding="utf-8",
            )
            (demo / "references").mkdir()
            (demo / "references" / "demo.md").write_text("# Demo\n", encoding="utf-8")
            (demo / "SKILL.md").write_text(
                "---\nname: cflow-demo\ndescription: 示例\n---\n\n读取 `references/demo.md`。\n",
                encoding="utf-8",
            )

            registry = build_registry(root)

        demo_entry = next(skill for skill in registry["skills"] if skill["name"] == "cflow-demo")
        self.assertEqual("示例", demo_entry["description"])
        self.assertEqual(["references/demo.md"], demo_entry["references"])


if __name__ == "__main__":
    unittest.main()
