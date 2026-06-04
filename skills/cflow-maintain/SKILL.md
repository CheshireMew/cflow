---
name: cflow-maintain
description: CFlow skill 套件维护系统。用于根据新的写作准则、流程缺陷、用户反馈、使用失败或流程改进，更新、重构、合并、删除或重新组织 CFlow skills。触发场景包括：判断新规则应该加入哪个 skill、检测重复或冲突规则、提出删除/合并方案、生成更新计划、正式编辑前征求用户明确批准、应用变更、校验 skills、提交维护 commit。
---

# CFlow Maintain

## 边界

只负责 CFlow skill 套件本身的变更。不要用本 skill 写内容、改内容、做标题或复盘普通内容，除非这些操作是为了诊断 skill 缺陷。

唯一真实源码是 `D:\Code\cflow\skills`。先检查这里的源码，再提出更新计划。`C:\Users\Lenovo\.codex\skills\cflow-*` 只是 Codex 发现用的链接，不是编辑入口。

## 语言规则

CFlow 以中文为真源。

- `name` 保持英文技术名。
- `description`、`SKILL.md` 正文、`references/` 用中文书写。
- 保留必要英文关键词，例如 hook、title、CTA、brief、draft、review、retention、copywriting。
- 不维护中英双份全文，避免规则漂移。
- 如果将来需要英文版，应生成独立发布版本，而不是在主 skill 内维护双语正文。

## 硬门槛

在用户明确批准具体更新计划前，禁止修改任何 CFlow skill 文件。

批准前允许：

- 读取 CFlow skill 文件
- 分类新准则
- 检测重复、冲突、过时规则和缺失流程
- 提出 patch 计划
- 说明预计修改的文件和位置

批准前禁止：

- 修改 `SKILL.md`
- 修改 `references/`
- 删除或合并文件
- 提交 commit
- 重新生成 metadata

## 工作流

1. **盘点**：列出相关 CFlow skills，读取 `SKILL.md` 和必要 reference。
2. **分类输入**：判断用户材料是规则、流程步骤、决策标准、平台笔记、声音准则、缺陷报告、测试用例或删除请求。
3. **定位边界**：每条规则只分配一个主要归属。只有路由需要时才在第二个 skill 中交叉引用。
4. **检查覆盖**：判断是否已覆盖、部分覆盖、冲突、重复或需要新增。
5. **规划重构**：优先一次性迁移，不保留兼容层。规则属于别处就移动，不复制。
6. **请求批准**：给出具体修改计划，等待用户明确批准。
7. **应用变更**：只修改批准范围内的文件。按计划删除过时或重复规则。
8. **校验**：对所有变更 skill 跑 `quick_validate.py`；如果路由或共享边界变化，校验全部 CFlow skills。
9. **提交**：校验通过后提交清晰 commit。

## 路由边界

- `cflow-content`：总入口、端到端路由、事实源维护。
- `cflow-topic`：选题发现、选题评分、内容栏目、选题池。
- `cflow-angle`：读者张力、核心主张、角度选择、premise 强化。
- `cflow-draft`：从 brief、笔记、转录或素材写完整一稿。
- `cflow-edit`：已有草稿诊断、编辑深度、声音保留、降低 AI 味。
- `cflow-package`：标题、hook、CTA、封面文案、平台发布版本。
- `cflow-review`：发布后学习、指标解释、反馈循环。
- `cflow-maintain`：CFlow 架构、规则归属、重构、校验、提交。

## 审批计划格式

编辑前返回：

```text
Proposed update:
Input classification:
Affected skills:
Existing coverage:
Conflicts or duplicates:
Files to change:
Rules to add:
Rules to move:
Rules to delete:
Validation plan:
Commit plan:
Approval needed:
```

计划后必须请求明确批准。模糊同意不算批准；等待用户清楚表示同意后才能执行。

## 参考

当需要分类规则、规划重构、判断合并/删除，或准备审批计划时，读取 `references/maintenance-protocol.md`。
