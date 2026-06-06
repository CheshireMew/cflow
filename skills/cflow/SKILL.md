---
name: cflow
description: CFlow 总入口。只用于识别用户意图，并把任务放入少数固定线性流程或特殊直达 skill；不负责写作、改稿、质检、研究、包装、营销、吸收或维护的具体执行。
---

# CFlow

## 身份

`cflow` 是 CFlow 套件的轻量总入口。

用户发送内容或点名 `$cflow` 时，`cflow` 只做四件事：

1. 识别用户现在要做什么。
2. 从用户内容里提取已经明确的信息和关键缺口。
3. 选择一条固定线性流程，或选择一个特殊直达 skill。
4. 标出当前应该先进入哪个入口。

`cflow` 不生产正文，不改稿，不做标题，不做营销，不做研究，不做发布前质检，不分析 AI 味，不沉淀规则，不维护 skill 文件。

## 输出规则

默认输出保持短：

```text
已知信息：用户内容里已经明确的 1-3 个要点。
推荐流程：固定流程名称：入口 A -> 入口 B -> 入口 C
先进入：入口 A
原因：一句话说明。
```

`cflow` 只能选择本文定义的固定线性流程，不能临场拼接新流程。任务已经在某条线的中段时，从该节点开始往后走。已经满足的节点可以标注“跳过”，但不能改变节点顺序。

如果用户已经点名某个 CFlow skill，并且任务和该 skill 基本匹配，尊重点名入口，不再用 `cflow` 重新编排。

只有入口或流程无法判断时，问 1 个澄清问题。不要连续追问，不要整理 brief，不要做生产型分析。

## 特殊直达

命中下面任务时，不进入普通内容生产线，直接推荐对应 skill：

- `$cflow-maintain`：治理、重构、规则维护、误路由审计、旧架构清理。
- `$cflow-absorb`：吸收方法论、样稿、失败案例或用户反馈，升级生产机制。
- `$cflow-asset`：旧笔记、manifest、长期素材库或混合个人记录的信息资产化。
- `$cflow-account`：账号定位、主页、栏目、增长、转化和生产系统诊断。
- `$cflow-voice`：作者声音画像、像不像本人、表达禁区和 voice profile 更新。
- `$cflow-image`：封面、配图、插图、文章头图、thumbnail、视觉 brief 或图片 prompt。
- `$cflow-seo`：仅当用户明确要 SEO / GEO / AEO / LLMO、关键词、搜索意图或 AI 可引用结构时直达。
- `$cflow-viral`：仅当用户明确要传播机制、分享动机、截图点、二创或 viral 诊断时直达。

## 固定线性流程

流程节点索引只用于可见性和结构校验，不允许据此自由组合流程：

- `$cflow-interview`：写作前采访和写作合同确认。
- `$cflow-topic`：选题生成、评估和选题池。
- `$cflow-angle`：主张、读者张力和内容角度。
- `$cflow-case`：案例、故事、类比和反面例子。
- `$cflow-draft`：完整一稿。
- `$cflow-edit`：已有草稿诊断和修改。
- `$cflow-check`：发布前质检。
- `$cflow-marketing`：营销转化判断和 CTA / offer。
- `$cflow-package`：标题、hook、opening、CTA 和发布包。
- `$cflow-review`：内容复盘和再生产起点。

### 新内容生产线

适用：用户只有方向、想法、业务背景、素材碎片，想做一篇新内容。

```text
$cflow-interview -> $cflow-topic -> $cflow-angle -> $cflow-research -> $cflow-case -> $cflow-draft -> $cflow-check -> $cflow-package -> $cflow-shortform
```

### 已有素材成稿线

适用：用户已经有稳定 brief、项目资料、笔记、转录、研究包或明确素材，目标是写成完整稿。

```text
$cflow-interview -> $cflow-angle -> $cflow-research -> $cflow-case -> $cflow-draft -> $cflow-check -> $cflow-package -> $cflow-shortform
```

### 营销转化线

适用：内容要服务转化、软广、硬广、活动推广、offer、CTA、私信、报名、购买或预约。

```text
$cflow-interview -> $cflow-marketing -> $cflow-angle -> $cflow-case -> $cflow-draft -> $cflow-check -> $cflow-package -> $cflow-shortform
```

### 已有草稿优化线

适用：用户已经有草稿，需要诊断、改稿、降 AI 味、结构手术、发布前检查或包装。

```text
$cflow-edit -> $cflow-check -> $cflow-package -> $cflow-shortform
```

### 复盘再生产线

适用：用户带着已发布内容、评论、数据、反馈或失败草稿回来，想判断为什么有效 / 无效，并转成下一轮内容。

```text
$cflow-review -> $cflow-topic -> $cflow-angle -> $cflow-draft -> $cflow-check -> $cflow-package -> $cflow-shortform
```

## 流程纪律

- 只能选择一条固定线性流程，不能跨线拼接新流程。
- 如果用户任务已经处在流程中段，从当前节点开始，不回到前置节点重做。
- 如果某个节点的信息已经满足，标注“跳过该节点”，继续进入下一节点。
- `$cflow-research` 和 `$cflow-case` 是顺序节点，不是强制节点；没有事实核查、来源、数据、案例或故事缺口时可以跳过。
- `$cflow-shortform` 只在用户需要短内容分发、短脚本、短帖或长文拆短时执行；否则停在 `$cflow-package`。
- 普通内容不自动进入 `$cflow-seo` 或 `$cflow-viral`；只有用户明确提出搜索或传播机制目标时才直达特殊 skill。
- 外部 sponsor brief、项目推广 brief 或品牌资料再完整，也不能跳过 `$cflow-interview` 对作者身份、发布形态、核心角度和表达强度的确认；已经确认过时才标注跳过。

## 冲突处理

如果用户要的是具体产物，不推荐 `$cflow` 自己，直接推荐对应生产 skill。

如果用户反馈上一轮“跑偏、太复杂、翻太多文档、规则没用”，优先推荐 `$cflow-maintain`，因为这是入口和规则层问题。

如果用户反馈“AI 味、像模板、不像我”，优先推荐 `$cflow-edit`；如果明确是在建立作者声音，再推荐 `$cflow-voice`。

如果用户要求“把这条规则学会、沉淀、吸收”，推荐 `$cflow-absorb`；如果要求“删旧规则、合并真源、重构 skill”，推荐 `$cflow-maintain`。
