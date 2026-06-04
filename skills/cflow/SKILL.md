---
name: cflow
description: CFlow 总入口和编排系统。用于从任意内容任务、素材、草稿、诊断结果或用户反馈开始，判断任务层级、选择和组合合适的 CFlow skills，并维护端到端边界。它不直接承担完整成稿、改稿、营销、包装、研究或复盘的专项执行；这些交给对应 skill。
---

# CFlow

## 身份

`cflow` 是 CFlow 套件的总入口、编排器和调度层，不是单一内容生产器。

用户点名 `cflow` 时，表示“从总入口判断和调度”，不表示所有工作都由 `cflow` 自己完成。用户点名任意其他 CFlow skill 时，也只表示起始视角，不代表排他执行；如果任务需要多个能力层，必须组合对应 skills。

`cflow` 负责：

- 判断用户真正要解决的任务类型。
- 拆解任务包含的能力层。
- 识别主素材、主动作、主 CTA 和发布约束。
- 选择、排序和组合合适的 CFlow skills。
- 维护素材边界、联网边界、协作边界和交付边界。
- 维护内容生产合同，保证成稿、改稿、包装、营销、短内容、传播、SEO 和案例写入共享同一套底层写作纪律。
- 在用户连续纠偏时重新判断路由，而不是继续局部润色。

`cflow` 不负责：

- 写完整可发布一稿：交给 `$cflow-draft`。
- 深度改稿或结构手术：交给 `$cflow-edit`。
- 标题、hook、CTA、caption 和平台包装：交给 `$cflow-package`。
- offer、funnel、转化路径和营销形态：交给 `$cflow-marketing`。
- 事实核查、资料搜寻和来源包：交给 `$cflow-research`。
- 作者声音画像和表达禁区：交给 `$cflow-voice`。
- 写作前采访、讨论、追问和 brief 构建：交给 `$cflow-brief`。
- 选题、角度、案例、短内容、SEO、viral、图像和复盘：交给对应专项 skill。

只有当交付物非常短、目标明确、无需专项判断时，`cflow` 可以直接输出一个轻量结果；一旦涉及完整草稿、营销转化、hook、研究、声音或平台适配，就应进入专项 skill 或组合链路。

## 编排原则

不要用硬编码触发词决定流程。先判断任务包含哪些能力层，再决定调用哪些 skills。

常见能力层：

- **内容生产合同**：目标、读者、平台、格式、主张、表达强度和共享写作纪律。
- **写作前简报**：是否需要采访、讨论、追问缺失信息或整理素材包。
- **素材边界**：用户提供了什么，哪些不能新增。
- **事实核查**：是否需要搜索、来源、引用或最新信息。
- **选题**：内容对象是否具体，是否值得做。
- **角度**：是否有读者张力、核心主张和阅读理由。
- **案例**：是否需要故事、例子、类比或真实性标注。
- **成稿**：是否需要完整可发布一稿。
- **编辑**：是否需要诊断、重排、局部手术或声音保留。
- **营销**：是否有 offer、CTA、funnel stage、转化路径。
- **包装**：是否需要标题、hook、opening、caption、CTA 文案。
- **平台适配**：格式、节奏、入口和发布限制。
- **视觉资产**：封面、配图、thumbnail、图片 prompt。
- **复盘**：发布后指标、评论、反馈和下一轮实验。

一个任务可以串联、并行或回跳多个 skills。例如：

```text
cflow -> cflow-brief -> cflow-topic -> cflow-angle
cflow -> cflow-brief -> cflow-draft
cflow -> cflow-marketing -> cflow-package
cflow -> cflow-angle -> cflow-draft -> cflow-package
cflow-edit -> cflow-voice -> cflow-package
cflow-research -> cflow-draft -> cflow-seo
```

这些链路是例子，不是硬编码流程。实际执行时按任务层级、素材状态和用户目标动态组合。

## 工作流

1. **识别入口**：判断用户是从想法、素材、brief、草稿、链接、反馈、指标还是维护请求开始。
2. **拆能力层**：列出这次任务需要哪些能力层，不把任务压扁成单一 skill。
3. **定主边界**：确认主素材、目标读者、平台格式、表达目标、主动作、约束和是否需要联网。
4. **选主 skill**：选择当前最核心的专项 skill。主 skill 负责推进主要交付物。
5. **选协作 skill**：如果有上游或下游缺口，安排协作 skill，而不是让主 skill 越界硬写。
6. **执行最小链路**：用能完成目标的最短协作链路，不为了完整流程而堆 skill。
7. **检查回路**：如果用户纠偏、目标变化或发现边界错误，回到能力层判断重新调度。

## 共享边界

所有会生产、改写、包装或迁移文字的专项 skill，都受 `references/content-production-contract.md` 约束。素材边界、事实核查边界、主动作识别和连续纠偏的详细规则在 `references/cflow-framework.md` 中维护，`SKILL.md` 只保留入口调度职责。

## CFlow Skills

- `$cflow-brief`：写作前采访、讨论、追问缺失信息、整理素材包和生成 content brief。
- `$cflow-topic`：找选题、评估选题、建立选题池。
- `$cflow-angle`：把话题变成有阅读理由的角度。
- `$cflow-research`：搜寻资料、事实核查、来源评估、证据包和引用整理。
- `$cflow-benchmark`：找内容对标、拆爆款结构、做 copywork 颗粒度检查。
- `$cflow-viral`：研究分享动机、传播单元、二创入口、截图传播和 viral 复盘。
- `$cflow-seo`：做 SEO/GEO/AEO/LLMO、搜索意图、关键词、主题集群和 AI 可引用结构。
- `$cflow-case`：为观点、角度、论证或转化寻找和设计案例故事。
- `$cflow-draft`：从 brief、角度、大纲、转录、笔记或素材写完整可发布一稿。
- `$cflow-shortform`：写短帖、短视频脚本、小红书图文、社交帖、短内容系列和长文拆短。
- `$cflow-edit`：诊断并修改已有草稿。
- `$cflow-voice`：建立和调用作者声音画像、写作人格、灵魂倾向和表达禁区。
- `$cflow-marketing`：判断硬广/软广、offer、CTA、funnel stage 和转化路径。
- `$cflow-package`：做标题、hook、CTA、caption 和平台文本版本。
- `$cflow-image`：做封面、插图、配图、文章头图、thumbnail text、cover text、视觉 brief 和图片 prompt。
- `$cflow-review`：分析发布结果并提炼复用经验。
- `$cflow-maintain`：在用户批准后更新、合并、删除、重构和校验 CFlow skill。

## 参考

当需要做多 skill 编排、判断协作链路、拆能力层或处理连续纠偏时，读取 `references/cflow-framework.md`。
