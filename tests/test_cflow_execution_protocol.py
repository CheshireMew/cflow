from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class CFlowExecutionProtocolTests(unittest.TestCase):
    def test_cflow_entry_defines_current_routing_protocol(self) -> None:
        cflow = read_text("skills/cflow/SKILL.md")

        self.assertIn("特殊直达", cflow)
        self.assertIn("固定线性流程", cflow)
        for field in ["已知信息：", "推荐流程：", "先进入：", "原因："]:
            self.assertIn(field, cflow)
        self.assertIn("只能选择本文定义的固定线性流程", cflow)
        self.assertIn("不能临场拼接新流程", cflow)
        self.assertIn("流程节点索引只用于可见性和结构校验", cflow)

    def test_cflow_entry_routes_without_producing_content(self) -> None:
        cflow = read_text("skills/cflow/SKILL.md")

        self.assertIn("`cflow` 不生产正文", cflow)
        self.assertIn("如果用户已经点名某个 CFlow skill", cflow)
        self.assertIn("如果用户要的是具体产物，不推荐 `$cflow` 自己", cflow)
        self.assertIn("直接推荐对应生产 skill", cflow)

    def test_sponsor_project_brief_routes_to_interview_not_direct_draft(self) -> None:
        cflow = read_text("skills/cflow/SKILL.md")
        interview = read_text("skills/cflow-interview/SKILL.md")
        draft = read_text("skills/cflow-draft/SKILL.md")

        self.assertIn("外部 sponsor brief、项目推广 brief 或品牌资料再完整", cflow)
        self.assertIn("不能跳过 `$cflow-interview`", cflow)
        self.assertIn("不要把长 brief 的完整性误判成稳定写作合同", interview)
        self.assertIn("外部 sponsor brief、项目推广 brief 或产品资料必须先分层", draft)
        self.assertIn("不得整包吸收", draft)

    def test_draft_no_longer_contains_old_direct_generation_default(self) -> None:
        draft = read_text("skills/cflow-draft/SKILL.md")

        self.assertNotIn("默认直接生成可发布一稿", draft)
        self.assertIn("稳定 brief、角度、大纲、笔记、转录、研究包", draft)
        self.assertIn("只有目标、读者、交付形态、核心主张或素材边界缺失到会写成完全不同作品时", draft)
        self.assertIn("成稿前先把输入整理成合同", draft)

    def test_ai_feedback_failure_state_is_hard_route(self) -> None:
        cflow = read_text("skills/cflow/SKILL.md")
        edit = read_text("skills/cflow-edit/SKILL.md")

        self.assertIn("AI 味、像模板、不像我", cflow)
        self.assertIn("优先推荐 `$cflow-edit`", cflow)
        self.assertIn("连续负反馈", edit)
        self.assertIn("没有明确授权，不继续试新版本", edit)
        self.assertIn("用户说“像 AI”", edit)
        self.assertIn("`cflow-edit` 必须先做根因诊断和最小下一刀", edit)

    def test_story_opening_has_hard_check(self) -> None:
        case = read_text("skills/cflow-case/SKILL.md")

        self.assertIn("故事开头硬检查", case)
        for requirement in ["人", "动作", "阻碍", "具体物件", "现场顺序"]:
            self.assertIn(requirement, case)
        self.assertIn("前 120 字", case)

    def test_marketing_and_package_have_separate_cta_boundaries(self) -> None:
        marketing = read_text("skills/cflow-marketing/SKILL.md")
        package = read_text("skills/cflow-package/SKILL.md")

        self.assertIn("负责“内容如何服务转化”", marketing)
        self.assertIn("CTA 类型", marketing)
        self.assertIn("CTA 强度", marketing)
        self.assertIn("决定 offer、funnel stage、主 CTA、转化路径或引流资产策略", package)
        self.assertIn("CTA 策略", package)
        self.assertIn("交给 `$cflow-marketing`", package)
        self.assertIn("策略明确后，CTA 和入口表达由 `cflow-package` 自己写好", package)

    def test_viral_post_publish_review_routes_to_review(self) -> None:
        viral = read_text("skills/cflow-viral/SKILL.md")
        review = read_text("skills/cflow-review/SKILL.md")

        self.assertIn("发布后数据、评论、转发、截图、二创、跨环境搬运或传播路径证据的完整复盘", viral)
        self.assertIn("交给 `$cflow-review`", viral)
        self.assertIn("发布后复盘归 `$cflow-review`", viral)
        self.assertIn("转发高：可能有替读者表达的判断、提醒或信息差", review)


if __name__ == "__main__":
    unittest.main()
