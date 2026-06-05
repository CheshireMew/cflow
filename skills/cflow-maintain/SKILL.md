---
name: cflow-maintain
description: CFlow skill 套件维护系统。用于根据新的写作准则、流程缺陷、用户反馈、使用失败或流程改进，更新、重构、合并、删除或重新组织 CFlow skills。触发场景包括：判断新规则应该加入哪个 skill、检测重复或冲突规则、提出删除/合并方案、生成更新计划、正式编辑前征求用户明确批准、应用变更、校验 skills、提交维护 commit。
---

# CFlow Maintain

## 边界

只负责 CFlow skill 系统本身的变更，不维护整个项目。不要用本 skill 写内容、改内容、做标题或复盘普通内容，除非这些操作是为了诊断 skill 缺陷。

唯一真实源码是当前仓库根目录下的 `skills/`。先检查这里的源码，再提出更新计划。`$HOME\.codex\skills\cflow-*` 只是 Codex 发现用的链接，不是编辑入口；其他 AI Agent 或工具可以按自己的发现机制兼容。

允许处理的范围：

- `skills/` 真源里的 skill 规则、reference 和 agent metadata。
- skill 路由、规则归属、边界、命名和目录结构。
- 直接服务 skill 生命周期的 schema、校验脚本、registry/sync 脚本、测试和 README 相关段落。

排除范围：

- 个人复盘资产、截图、指标、评论、私有案例和普通内容产物。
- 普通 Git hygiene、环境配置、应用代码或与 skill 生命周期无关的仓库工程。
- 用户没有明确纳入维护计划的项目文件。

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

## 归属边界

`cflow-maintain` 管通用 skill 架构，不管作者个人声音资产。维护输入里出现以下信号时，必须先做作者画像分流，不得直接写入通用 skill：

- “我讨厌 / 我喜欢 / 以后别 / 以后都 / 记住这个”
- “这不像我 / 这才是我的写法 / 正确但不像本人”
- “我改了一下 / 我稍微修改了 / 这样写才对 / 参考我这个版本”
- 用户亲自修改标题、hook、opening、CTA 或短发布文案
- 对固定词、句式、排版密度、语气、文章入口方式的个人偏好
- 对某类 AI 味、技术文档化、平台腔、报告腔、废话灌水的个人反感

分流结果必须至少分成：

```text
通用规则：
作者画像：
单篇 brief：
候选证据：
拒绝沉淀：
```

- **通用规则**：跨用户、跨题材成立的流程、权限、边界或判断标准，才进入 `skills/`。
- **作者画像**：用户个人表达偏好、禁用表达、思维动作、节奏和价值判断，交给 `$cflow-voice` 更新唯一 `profiles/voice-profile.md`。
- **单篇 brief**：只服务当前文章、当前项目、当前题材的素材和角度，不进入 `skills/` 或 voice 核心画像。
- **候选证据**：单次样本、单次反感、尚未稳定复现的作者偏好，交给 `$cflow-voice` 写入候选证据。
- **拒绝沉淀**：一次性情绪、执行失误、已被现有规则覆盖的问题，不新增规则。

`cflow-maintain` 防止个人偏好污染通用 skill；`cflow-voice` 防止流程规则污染 `voice-profile.md`。两者冲突时，先保留证据并向用户说明归属，不要两边都写。

## 工作流

1. **盘点**：列出相关 CFlow skills，读取 `SKILL.md` 和必要 reference。
2. **拆分复合输入**：如果用户材料是一篇文章、账号拆解、课程笔记、反馈合集、转录或长素材，先拆成独立信息单元，不要整段归到一个 skill。至少区分写作技巧、用户自己的账号资料、外部对标账号资料、引流方式、转化技巧、事实资料、作者偏好、发布环境观察、案例和维护请求。
3. **分类输入**：逐个判断信息单元是规则、流程步骤、决策标准、发布环境笔记、声音准则、写作机制、缺陷报告、测试用例、删除请求或 skill 系统架构请求。
4. **作者画像分流**：维护输入里如果能判断出用户稳定的表达偏好、反感表达、句子节奏、价值判断、写作禁区或“以后都这样”的偏好，先按“归属边界”分桶，生成 voice handoff，交给 `$cflow-voice` 更新唯一 `profiles/voice-profile.md`。不要把个人写法直接写成通用 skill 规则，除非它能跨用户成立。
   用户提供亲自修订后的正文或包装资产时，把它当成高优先级样本：先比较 AI 版本被用户改掉的方向，再分成通用写作机制、包装规则、作者画像证据、单篇 brief 和拒绝沉淀。
5. **识别写作价值**：如果输入涉及写作方法论、对标材料、用户反馈或内容效果，先判断它改善的是选题、角度、结构、hook、短内容、声音、转化、视觉、传播、SEO、案例还是复盘；不要过早只讨论流程、边界和归属。
6. **专项分析委托**：如果某个信息单元需要内容能力判断，先交给对应专项 skill 的规则来分析机制，再回到 maintain 判断是否沉淀。用户自己的账号诊断交给 `cflow-account`，外部对标账号资料交给 `cflow-benchmark`，引流和转化交给 `cflow-marketing`，标题、hook、CTA 交给 `cflow-package`，短内容结构交给 `cflow-shortform`，事实和来源交给 `cflow-research`，作者画像和表达禁区交给 `cflow-voice`。
7. **语料型 skill 分层**：如果维护对象含原始语料、作者风格、对标样本、训练数据、评估集、合成样本或生成脚本，先按 `references/maintenance-protocol.md` 的“语料型 skill 维护”做资源分层，确认真源和污染源。
8. **缺陷归因**：如果输入来自失败案例，先命名根行为，区分是已有规则未执行、规则缺失、路由缺失、边界冲突还是测试用例不足。
9. **泛化检查**：禁止把失败案例里的具体发布环境、交付形态、对象、行业或文案场景直接固化为规则条件。先做同类替换测试，能跨场景成立的必须写成可迁移规则；原案例只作为测试用例或例子。
10. **反膨胀审计**：默认不新增规则。先判断能否已覆盖、合并、移动、删除、收紧、作为例子、作为测试用例、分流到 profile/用户资产，或拒绝沉淀。
11. **特殊情况分流**：单次案例、作者偏好、账号私有资料、特定业务资产、发布环境短期经验、外部方法论整包或已有规则未执行，都先分流处理，不直接写进通用 skill。
12. **定位边界**：每条规则只分配一个主要归属。只有路由需要时才在第二个 skill 中交叉引用。
13. **检查覆盖**：判断是否已覆盖、部分覆盖、冲突、重复、过时、应删除、应合并、应分流或确实需要新增。
14. **规划重构**：优先一次性迁移，不保留兼容层。规则属于别处就移动，不复制；能替换旧规则就不叠加新规则。
15. **请求批准**：给出具体修改计划，等待用户明确批准。
16. **应用变更**：只修改批准范围内的文件。按计划删除过时或重复规则。
17. **同步发现入口**：只有创建、删除或重命名 skill 时，才运行 `powershell -ExecutionPolicy Bypass -File scripts/sync_personal_skills.ps1 -PruneStale`，补齐新增 skill 的个人 junction，并清理已删除 skill 的 stale junction。
18. **校验**：对所有变更 skill 跑 `quick_validate.py`；如果路由或共享边界变化，校验全部 CFlow skills。
19. **提交**：只有用户明确要求提交，或批准计划包含提交时，才在校验通过后提交清晰 commit。

## 路由边界

- `cflow`：CFlow 总入口、任务编排、能力层拆解、协作调度和端到端边界维护。
- `cflow-brief`：写作前采访、讨论、追问缺失信息、素材盘点和 content brief 构建。
- `cflow-research`：资料搜寻、事实核查、来源评估、证据包和引用整理。
- `cflow-topic`：选题发现、选题评分、内容栏目、选题池。
- `cflow-benchmark`：内容对标、账号拆解、爆款结构拆解、copywork 颗粒度检查。
- `cflow-account`：用户自己账号的定位、主页表达、栏目组合、数据反馈、转化路径和生产系统诊断。
- `cflow-viral`：分享动机、传播单元、二创入口、截图传播和病毒式传播复盘。
- `cflow-seo`：SEO/GEO/AEO/LLMO、搜索意图、关键词、主题集群和 AI 可引用结构。
- `cflow-case`：案例故事、真实性标注、未来预演、假设故事、支撑性例子。
- `cflow-angle`：读者张力、核心主张、角度选择、premise 强化。
- `cflow-draft`：从 brief、笔记、转录或素材写完整一稿。
- `cflow-shortform`：超短、短内容、短脚本、短发布文案、短内容系列和长文拆短。
- `cflow-edit`：已有草稿诊断、编辑深度、声音保留、AI 指纹诊断和基于作者偏好的改稿。
- `cflow-voice`：作者声音画像、写作人格、灵魂倾向、表达禁区。
- `cflow-marketing`：硬广/软广、offer、CTA、funnel stage、转化路径。
- `cflow-package`：标题、hook、开头、CTA 和短发布文案。
- `cflow-image`：封面、插图、配图、文章头图、thumbnail text、cover text、视觉 brief 和图片 prompt。
- `cflow-review`：发布后学习、指标解释、反馈循环。
- `cflow-maintain`：CFlow skill 系统架构、规则归属、重构和校验。

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
Rules to merge:
Rules to move:
Rules to delete:
Rules to refuse:
Special-case routing:
Net size impact:
Validation plan:
Personal skill sync plan:
Commit plan:
Approval needed:
```

计划后必须请求明确批准。模糊同意不算批准；等待用户清楚表示同意后才能执行。

## 参考

当需要分类规则、规划重构、判断合并/删除，或准备审批计划时，读取 `references/maintenance-protocol.md`。
