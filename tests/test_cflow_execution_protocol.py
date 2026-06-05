from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class CFlowExecutionProtocolTests(unittest.TestCase):
    def test_framework_defines_preflight_gate_and_contract_states(self) -> None:
        framework = read_text("skills/cflow/references/cflow-framework.md")

        self.assertIn("## 执行闸门", framework)
        self.assertIn("preflight 固定检查", framework)
        for field in ["需要调动的 skills", "流程顺序", "当前执行 skill", "后续回跳条件"]:
            self.assertIn(field, framework)
        for state in [
            "stable_contract",
            "unstable_contract",
            "weak_angle",
            "story_needed",
            "ai_feedback",
            "fact_gap",
            "voice_gap",
        ]:
            self.assertIn(state, framework)

    def test_cflow_entry_requires_skill_sequence_before_writing(self) -> None:
        cflow = read_text("skills/cflow/SKILL.md")
        framework = read_text("skills/cflow/references/cflow-framework.md")

        self.assertIn("skill sequence", cflow)
        self.assertIn("按流程顺序推进", cflow)
        self.assertIn("不是只判断下一步", framework)
        self.assertIn("目标看似明确时，也只能输出交接 brief", framework)

    def test_sponsor_project_brief_requires_preflight_not_direct_draft(self) -> None:
        framework = read_text("skills/cflow/references/cflow-framework.md")
        cflow = read_text("skills/cflow/SKILL.md")

        self.assertIn("外部 sponsor brief", framework)
        self.assertIn("不能进入 `$cflow-draft`", framework)
        self.assertIn("执行闸门先完成 preflight", cflow)

    def test_draft_no_longer_contains_old_direct_generation_default(self) -> None:
        draft = read_text("skills/cflow-draft/SKILL.md")

        self.assertNotIn("默认直接生成可发布一稿", draft)
        self.assertIn("上游已经产出明确交接 brief", draft)
        self.assertIn("禁止成稿", draft)

    def test_ai_feedback_failure_state_is_hard_route(self) -> None:
        framework = read_text("skills/cflow/references/cflow-framework.md")
        edit = read_text("skills/cflow-edit/SKILL.md")

        self.assertIn("ai_feedback -> $cflow-edit", framework)
        self.assertIn("AI feedback failure state", edit)
        self.assertIn("不能直接给新版正文", edit)

    def test_story_opening_has_hard_check(self) -> None:
        case = read_text("skills/cflow-case/SKILL.md")

        self.assertIn("故事开头硬检查", case)
        for requirement in ["人", "动作", "阻碍", "具体物件", "现场顺序"]:
            self.assertIn(requirement, case)
        self.assertIn("前 120 字", case)

    def test_marketing_and_package_have_separate_cta_boundaries(self) -> None:
        marketing = read_text("skills/cflow-marketing/SKILL.md")
        package = read_text("skills/cflow-package/SKILL.md")
        framework = read_text("skills/cflow/references/cflow-framework.md")

        self.assertIn("转化策略层", marketing)
        self.assertIn("CTA 类型", marketing)
        self.assertIn("CTA 强度", marketing)
        self.assertIn("包装表达层", package)
        self.assertIn("CTA 策略", package)
        self.assertIn("文案变体", package)
        self.assertIn("策略不清先回 `$cflow-marketing`", framework)

    def test_viral_post_publish_review_routes_to_review(self) -> None:
        viral = read_text("skills/cflow-viral/SKILL.md")
        review = read_text("skills/cflow-review/SKILL.md")
        framework = read_text("skills/cflow/references/cflow-framework.md")

        self.assertIn("不负责发布后复盘主权", viral)
        self.assertIn("发布后传播表现也归 `$cflow-review`", review)
        self.assertIn("viral 发现已有发布后传播证据 -> review", framework)


if __name__ == "__main__":
    unittest.main()
