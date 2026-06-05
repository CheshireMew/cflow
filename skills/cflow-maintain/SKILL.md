---
name: cflow-maintain
description: CFlow skill 套件治理维护系统。用于清理、合并、删除、重构和校验 CFlow skills，处理唯一事实源、规则重复、边界冲突、过时规则、旧架构迁移和发现入口同步。吸收新方法论、样稿、对标和失败反馈的生产能力升级，优先使用 cflow-absorb。
---

# CFlow Maintain

## 边界

`cflow-maintain` 是 CFlow skill 系统的治理维护工具，不再承担“吸收优质内容方法论、升级生产能力”的主入口。新材料、样稿、课程笔记、内容方法论、对标拆解、用户反馈和失败案例，先交给 `$cflow-absorb` 提炼可迁移机制；只有进入去重、冲突、迁移、删除、同步或校验阶段时，才回到 `cflow-maintain`。

唯一真实源码是当前仓库根目录下的 `skills/`。`$HOME\.codex\skills\cflow-*` 只是 Codex 发现用的链接，不是编辑入口。

允许处理：

- `skills/` 真源里的 skill 规则、reference 和 agent metadata。
- skill 路由、规则归属、边界、命名和目录结构。
- 规则重复、冲突、过时、误导、事实源分裂和旧架构残留。
- 直接服务 skill 生命周期的 schema、校验脚本、registry/sync 脚本、测试和 README 相关段落。

不负责：

- 从优质内容、外部方法论或样稿里主动提炼生产机制。
- 写内容、改内容、做标题、成稿、包装或复盘普通内容。
- 维护作者声音画像、账号私有资产或普通内容资产。

## 与 cflow-absorb 的分工

- `$cflow-absorb`：发现好信息，把它转成生产能力升级方案。
- `$cflow-maintain`：治理知识库，把升级方案落到唯一事实源，并清掉旧结构、重复规则和冲突边界。

如果用户的输入同时包含新方法论和治理请求，先由 `$cflow-absorb` 识别“哪些值得吸收”；再由 `cflow-maintain` 审计“怎么合并、移动、删除和校验”。

## 硬门槛

在用户明确批准具体更新计划前，禁止修改任何 CFlow skill 文件。

批准前允许：

- 读取 CFlow skill 文件。
- 检查重复、冲突、过时规则、旧 helper、旧导出和旧恢复逻辑。
- 判断唯一事实源。
- 提出治理和重构计划。

批准前禁止：

- 修改 `SKILL.md`。
- 修改 `references/`。
- 删除、移动或合并文件。
- 提交 commit。
- 重新生成 metadata。

## 工作流

1. **确认任务类型**：判断这是治理维护，还是吸收进化。吸收进化转交 `$cflow-absorb`。
2. **盘点事实源**：列出相关 skill、reference、agent metadata、profile 或脚本，确认哪个文件是唯一真源。
3. **检测问题**：标记重复、冲突、过时、放错位置、兼容层残留、旧 helper、旧导出、旧恢复逻辑、测试缺口和同步缺口。
4. **选择治理动作**：合并、移动、删除、收紧、拆分、重命名、同步发现入口或补校验。
5. **一次性迁移**：按根因收口，不保留兼容层、旧类型、旧 helper、旧恢复逻辑或旧导出。禁止停在半迁移状态。
6. **请求批准**：给出具体治理计划，等待用户明确批准。
7. **应用变更**：只修改批准范围内的文件。原则规则属于别处就移动，不复制；高风险执行规则可以下沉成专项 skill 的短硬闸门；能替换旧规则就不叠加新规则。
8. **同步发现入口**：只有创建、删除或重命名 skill 时，运行 `powershell -ExecutionPolicy Bypass -File scripts/sync_personal_skills.ps1 -PruneStale`。
9. **校验**：运行 `python scripts\quick_validate.py`；如果路由、边界或 skill 列表变化，校验全部 CFlow skills。
10. **提交**：只有用户明确要求提交，或批准计划包含提交时，才在校验通过后提交。

## 审批计划格式

编辑前返回：

```text
Proposed governance update:
Task type:
Affected skills:
Current truth sources:
Duplicate or conflict:
Outdated rules:
Files to change:
Rules to merge:
Rules to move:
Rules to delete:
Rules to keep:
Compatibility layers to remove:
Validation plan:
Personal skill sync plan:
Commit plan:
Approval needed:
```

计划后必须请求明确批准。模糊同意不算批准；等待用户清楚表示同意后才能执行。

## 参考

治理、去重、唯一事实源、语料分层、旧架构迁移和校验规则见 `references/maintenance-protocol.md`。
