# CFlow 编排框架

## 核心定义

`cflow` 是 CFlow 套件的编排入口。它负责判断“这次任务需要哪些能力层”，再把每一层交给最合适的专项 skill。

不要把 `cflow` 当成万能写作 skill 或直接生产入口。它可以做轻量判断、preflight、brief、追问和调度，但完整生产应交给专项 skill：

- 完整成稿：`$cflow-draft`
- 深度改稿：`$cflow-edit`
- hook / title / CTA：`$cflow-package`
- offer / funnel / 转化路径：`$cflow-marketing`
- 搜索 / 核查 / 来源：`$cflow-research`
- 作者声音：`$cflow-voice`
- 写作前采访 / 讨论 / brief：`$cflow-brief`
- 其他能力层交给对应 skill

内容生产、改写、包装、营销、短内容、传播、SEO、案例写入和对标迁移共享 `content-production-contract.md`。专项 skill 只维护自己的应用规则，不另立一套通用写作纪律。

## 非排他入口

用户点名哪个 skill，只代表起始视角，不代表排他执行；但用户点名 `$cflow` 时，不能把“起始视角”内部化成直接生产。`cflow` 必须先显式完成路由、交互流程或交接 brief。

判断方式：

```text
用户从哪里开始？
这次任务真正需要哪些能力层？
哪个 skill 是主执行？
哪些 skill 是上游或下游协作？
需要调动哪些 skills，流程顺序是什么？
是否需要回跳或重新路由？
```

例子：

- 用户点 `$cflow`：先拆任务层，再组合专项 skill。
- 用户说“先聊聊”“采访我”“我不知道怎么说”：先交给 `$cflow-brief`。
- 用户点 `$cflow-package`：如果 CTA、offer 或 funnel 不清，先交给 `$cflow-marketing`。
- 用户点 `$cflow-marketing`：如果要写 hook 或简介第一句，交给 `$cflow-package`。
- 用户点 `$cflow-package` 且只要 CTA 文案变体：offer、CTA 类型和转化路径稳定时由 `$cflow-package` 执行；策略不清先回 `$cflow-marketing`。
- 用户点 `$cflow-viral` 但提供的是发布后转发、截图、评论或二创数据：先交给 `$cflow-review` 复盘，必要时采用 `$cflow-viral` 的传播维度。
- 用户点 `$cflow-draft`：如果主张弱，先交给 `$cflow-angle`；如果需要证据包，交给 `$cflow-research`。
- 用户点 `$cflow-edit`：如果声音不对，交给 `$cflow-voice`；如果只是标题弱，交给 `$cflow-package`。

## 能力层拆解

每次任务先拆能力层，不要用关键词硬编码流程。

| 能力层 | 判断问题 | 主要 skill |
|---|---|---|
| 内容生产合同 | 目标、读者、篇幅、交付形态、发布约束、主张、表达强度和共享写作纪律 | `$cflow` |
| 写作前简报 | 是否需要采访、讨论、追问缺失信息或整理素材包 | `$cflow-brief` |
| 素材边界 | 用户提供了什么，哪些不能新增 | `$cflow` |
| 事实核查 | 是否需要搜索、来源、引用、最新信息 | `$cflow-research` |
| 选题 | 内容对象是否具体、值得做 | `$cflow-topic` |
| 角度 | 是否有读者张力和核心主张 | `$cflow-angle` |
| 案例 | 是否需要故事、例子、类比或真实性标注 | `$cflow-case` |
| 成稿 | 是否需要完整可发布一稿 | `$cflow-draft` |
| 短内容 | 是否需要超短或短篇幅的单点内容 | `$cflow-shortform` |
| 编辑 | 是否需要诊断、重排、局部手术 | `$cflow-edit` |
| 声音 | 是否需要作者声音画像或表达禁区 | `$cflow-voice` |
| 营销 | 是否需要判断 offer、CTA 类型、CTA 强度、funnel、转化路径 | `$cflow-marketing` |
| 包装 | 是否需要 hook、标题、开头、CTA 文案变体或短发布文案 | `$cflow-package` |
| SEO | 是否需要搜索意图、关键词、结构化答案 | `$cflow-seo` |
| 对标 | 是否需要找对标、拆爆款、迁移模式 | `$cflow-benchmark` |
| 传播 | 是否需要发布前分享动机、二创入口、截图点或传播单元设计 | `$cflow-viral` |
| 图像 | 是否需要封面、配图、thumbnail、图片 prompt | `$cflow-image` |
| 复盘 | 是否需要分析表现、评论、传播路径、转发截图、二创证据或下一轮实验 | `$cflow-review` |
| 维护 | 是否需要修改 CFlow skill 本身 | `$cflow-maintain` |
| 生产资产 | 是否有已沉淀模式、模板、案例或资产卡片可复用 | `$cflow` 发现后交给对应生产 skill |

一项任务可以有多个能力层。只选择必要层，不堆流程。

## 编排模式

### 串联

适合有明确前后依赖的任务。

```text
brief -> topic -> angle
brief -> draft
angle -> draft -> package
marketing -> package
research -> draft -> seo
edit -> voice -> package
```

### 并行

适合多个能力层互不依赖，可以同时准备。

```text
research + benchmark -> angle
marketing + package -> shortform
voice + edit -> draft rewrite
```

### 回跳

适合执行中发现上游判断错误。

```text
package 发现 offer 不清 -> marketing
draft 发现主张弱 -> angle
draft 发现 brief 不稳或素材缺口会改变方向 -> brief
edit 发现素材越界 -> cflow
marketing 发现需要第一句 hook -> package
package 发现 offer、CTA 类型或转化路径不清 -> marketing
viral 发现已有发布后传播证据 -> review
```

回跳不是失败，是正确的边界控制。

## 编排合同

`cflow` 交给专项 skill 时，尽量提供轻量合同：

```text
目标：
读者：
篇幅：
交付形态：
发布约束：
主素材：
主张 / 角度：
主动作 / CTA：
表达强度：
约束：
需要该 skill 解决的问题：
可用生产资产：
```

不是每次都要展示完整合同，但用户点名 `$cflow` 时，必须展示当前路由判断、下一步交互流程或交接 brief。不得用“合同可推断”作为直接输出完整成品的理由。

## 执行闸门

复杂内容任务、外部 brief、连续纠偏、用户点名 `$cflow` 或任务可能进入多个专项 skill 时，必须先完成 preflight。用户点名 `$cflow` 时，preflight 不得完全内部化，必须对用户输出下一步交互流程或交接 brief；禁止直接成稿、改稿、包装或输出完整生产成品。

preflight 固定检查：

```text
任务类型：
已知合同：
缺失合同：
合同状态：
需要调动的 skills：
流程顺序：
当前执行 skill：
是否达到可交接状态：
后续回跳条件：
禁止动作：
```

合同状态只允许落到下列之一：

| 合同状态 | 路由 | 禁止动作 |
|---|---|---|
| `handoff_ready` | 输出交接 brief，说明应由哪个专项 skill 执行；如果用户要完整生产，引导其显式使用 `$cflow-draft`、`$cflow-edit`、`$cflow-package` 或其他执行 skill | 禁止在 `$cflow` 内输出完整正文、完整改稿、完整包装成品或完整营销稿 |
| `unstable_contract` | 进入 `$cflow-brief` | 禁止输出完整正文 |
| `weak_angle` | 进入 `$cflow-angle` | 禁止把项目资料整理成说明文 |
| `story_needed` | 进入 `$cflow-case` | 禁止直接编故事或用宏观制度案例冒充生活故事 |
| `ai_feedback` | 进入 `$cflow-edit` 做根因诊断 | 禁止连续重写 |
| `fact_gap` | 进入 `$cflow-research` | 禁止把未核查外部事实写成确定事实 |
| `voice_gap` | 进入 `$cflow-voice` 或先建立轻量声音合同 | 禁止用通用中性解释腔替代作者声音 |

外部 sponsor brief、项目推广 brief、合作邀约或品牌素材属于高风险输入。只要篇幅、联网范围、交付形态、目标读者、作者身份、核心角度或 sponsor 味道强度会改变成稿方向，合同状态就是 `unstable_contract` 或 `weak_angle`，不能进入 `$cflow-draft`。即使这些条件已经明确，用户点名 `$cflow` 时也只能进入 `handoff_ready`，输出交接 brief，不能直接成稿。

连续纠偏属于状态切换信号，不是继续局部润色的请求。如果用户连续指出“太长、太 AI、角度不对、案例不贴、声音不对、没有趣味、排版像 AI”，必须重新跑 preflight，并把合同状态改到对应上游层级。

写作任务进入 `$cflow` 时，preflight 必须尽可能识别完整 skill sequence，而不是只判断下一步。下一步只是当前执行点；流程顺序才是端到端任务路径。例如：

```text
cflow -> cflow-brief -> cflow-angle -> cflow-case -> cflow-draft -> cflow-edit -> cflow-package
```

如果流程顺序不确定，先说明不确定点并把当前执行 skill 放在能消除不确定性的最上游位置。用户点名 `$cflow` 时，不允许走 `cflow -> cflow-draft` 的直接短链路；目标看似明确时，也只能输出交接 brief 或下一步交互流程。

## 强制路由

这些路由是硬约束，不是建议：

- 缺篇幅、联网范围、交付形态、作者身份且会改变正文形态：`unstable_contract -> $cflow-brief`。
- 用户点名 `$cflow` 且任务目标是完整草稿、完整改稿、完整包装、完整营销稿或完整研究报告：先输出 preflight、交互流程或交接 brief；禁止直接生产完整成品。
- 用户点名 `$cflow` 并说“我想写一篇 / 想做一篇 / 准备写 / 有个想法”时，默认进入 `$cflow-brief` 或 `$cflow-angle` 的交互流程；除非用户改用 `$cflow-draft`，否则不得直接成稿。
- 项目 brief 还没有作者判断，只能回答“项目是什么”：`weak_angle -> $cflow-angle`。
- 用户要求真实故事、历史故事、生活细节或普通人场景：`story_needed -> $cflow-case`。
- 用户连续反馈 AI、模板、说明书腔、排版 AI：`ai_feedback -> $cflow-edit` 先诊断。
- 输出需要新增外部事实、具体历史细节、当前项目状态或来源：`fact_gap -> $cflow-research`。
- 用户明确要求像本人、保留声音、不要 AI 味且缺少声音依据：`voice_gap -> $cflow-voice`。

如果一个任务同时命中多个状态，先处理会改变方向的上游状态。优先级：

```text
fact_gap / unstable_contract -> weak_angle -> story_needed -> voice_gap -> handoff_ready
```

`ai_feedback` 是例外：一旦用户连续反馈 AI 或模板化，先暂停当前生产链路，进入 `$cflow-edit` 做根因诊断，再决定回到 angle、case、voice、draft 或 package。

## 生产资产发现

普通内容生产资产放在 `profiles/content-assets/`，不是 `skills/` 真源。它们可以是优质内容样本、可迁移模式、生产资产、实验记录、voice 证据或复盘快照。

当任务涉及成稿、改稿、包装、短内容、传播、转化、案例、声音或复盘沉淀时，先检查 `profiles/content-assets/` 是否有匹配资产。匹配方式优先看资产 frontmatter：

```yaml
asset_type:
skills:
triggers:
use_when:
avoid_when:
```

发现资产后：

- 只读取与当前任务匹配的资产，不批量加载整个资产库。
- 把资产作为生产参考、结构模式、检查清单或局部手术依据，不升级成长期 CFlow 规则。
- 仍以用户素材为事实边界，不用资产补造人物、数据、案例、承诺、服务或结果。
- 如果资产会改变 CFlow 长期行为，输出维护建议并交给 `$cflow-maintain`。

采用边界：

- `$cflow-draft`：可用资产作为结构、叙事推进、案例用法、资源包装或论证方式。
- `$cflow-edit`：可用资产做诊断、对照检查或局部手术，不把整篇改成资产模板。
- `$cflow-package`：可用资产做标题、hook、opening、CTA 和短发布文案策略。
- `$cflow-viral`：可用资产做分享动机、传播单元、截图点、复述句和二创入口。
- `$cflow-shortform`：可用资产做单点表达、首屏推进、短链路、段落密度和短脚本结构。

## 平台处理

默认不按平台区分内容形态，只按篇幅和交付形态路由：

- 超短和短内容交给 `$cflow-shortform`。
- 中篇和长篇文章交给 `$cflow-draft`。
- 标题、hook、开头、CTA 和短发布文案交给 `$cflow-package`。

只有用户特意提及平台、发布位置或具体限制时，才把它记录为发布约束。发布约束只回答字数、链接、审核、比例、媒介、入口或交付形式限制，不生成平台风格，也不改变 skill 路由。

## 素材边界

用户提供了明确原始素材时，改写、包装、营销强化都不得新增未被素材支撑的事实、功能、服务、承诺或运营范围。

允许：

- 重排顺序。
- 强化语气。
- 压缩风险提醒。
- 把隐含利益写清楚。
- 把已有链接、邀请码、返佣、入口变成更强 CTA。

不允许：

- 新增原文没有的服务内容、运营承诺、活动机制或产品能力。
- 把推测写成事实。
- 为了顺口补出用户没有提供的卖点。

如果转化确实需要补信息，单独标注为“建议补充”，不要混进成稿。

## 事实核查边界

内容生产默认不联网。用户给出的产品信息、活动信息、卖点、时间节点、链接、案例和背景，默认属于“用户素材”。

只有满足下面任一条件时，才交给 `$cflow-research`：

- 用户明确说要搜索、核查、查证、找来源、找最新信息、整理引用或 source pack。
- 交付物本身被用户要求带来源、证据包、引用、事实判断或研究结论。
- 助手准备引入用户没有提供的新外部事实、数据、案例、政策、价格、产品变化、人物公司信息或竞品现状。
- 当前任务本身被用户定义为高严谨度事实判断，例如法律、医疗、金融建议、投资推荐、监管状态核查或公开指控核查。

没有联网核查时，不要假装查过，也不要主动输出大段风险说明。

## 主动作识别

当素材里出现链接、邀请码、返佣、入口、领取、前置、点击欲望、CTA、资料入口、置顶、回复关键词或私下领取时，先识别主动作。

判断顺序：

1. 用户明确要前置、点击、领取、注册、加入、购买或咨询的对象。
2. 素材里最能完成转化目标的链接或入口。
3. 用户明确给出的发布约束里允许直接出现、且读者行动成本最低的入口。
4. 风险提醒、背景解释和补充说明只能服务主动作，不能抢主动作首屏。

如果同一段素材里有多个链接，先分层：

- **主 CTA**：这次最希望读者点击或执行的入口。
- **辅助入口**：能补充行动路径，但不是第一动作。
- **风控信息**：防骗、限制、规则、风险提醒，默认后置并压缩。

不要按词面猜测入口类型。例如“邀请链接前置”可能指社群邀请、交易所邀请码、活动邀请或注册返佣链接；要从上下文和用户目标判断。

## 连续纠偏

用户连续纠偏时，不要继续在同一策略里改句子。先判断纠偏指向哪个层级：

- **指代错误**：重新识别主对象、主链接、主 CTA。
- **路由错误**：切到更合适的专项 skill 或组合链路。
- **素材越界**：删掉没有素材支撑的新增内容。
- **策略无效**：换 hook 机制、营销形态或内容结构。
- **声音不对**：交给 `$cflow-voice` 或降低改写强度。

如果用户指出“平淡”“没技巧”“不吸引人”，默认不是句子润色问题，而是包装策略失败；交给 `$cflow-package` 用不同策略重做候选。

## 维护边界

规则只能有一个主要真源，但任务执行可以多 skill 协作。

维护时不要把“一个规则归一个 skill”误解成“一个任务只能用一个 skill”。规则归属解决的是知识库一致性；编排解决的是实际任务完成路径。
