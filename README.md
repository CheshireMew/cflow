# CFlow

CFlow 是一套中文内容工作流 skills，用来把选题、资料、角度、成稿、改稿、营销、包装、视觉和复盘组织成可协作的内容生产系统。

仓库中的 `skills/` 是唯一真实源码；不要直接编辑 Codex 发现目录里的链接副本，例如 `$HOME\.codex\skills\cflow-*`。

## 适合什么

CFlow 适合处理这些任务：

- 从模糊想法整理出可写的 content brief。
- 判断一个选题是否值得做，并找到更有读者张力的 angle。
- 把笔记、转录、素材或 brief 写成可发布草稿。
- 对已有草稿做结构诊断、改稿、降 AI 味和声音保留。
- 为内容设计标题、hook、opening、CTA、caption 和平台版本。
- 判断内容是否承担营销转化，并设计 offer、funnel 和主动作。
- 诊断内容账号的定位、主页表达、栏目组合、表现反馈、转化路径和生产系统。
- 为观点找案例、故事、类比、反例和可标注真实性的素材。
- 为内容做研究、事实核查、来源包和 SEO/GEO/AEO/LLMO 结构。
- 把长内容拆成短帖、短视频脚本、小红书图文、thread 或私域文案。
- 为内容设计封面、配图、thumbnail、视觉 brief 和图片 prompt。
- 分析发布后的表现、评论、指标和下一轮实验。
- 维护 CFlow skill 系统本身，包括规则迁移、重复清理和结构校验。

## 使用方式

最稳妥的入口是 `$cflow`。它会先判断任务需要哪些能力层，再决定调用哪些专项 skill。

```text
Use $cflow 帮我判断这个任务需要哪些 CFlow skills 协作，并推进到合适的交付物。
```

如果你已经知道要做什么，可以直接点名专项 skill：

```text
Use $cflow-brief 先采访我，帮我把这个想法整理成可写作的 brief。
Use $cflow-angle 帮我为这个选题找到最强角度。
Use $cflow-draft 根据这个 brief 和素材写一版可发布草稿。
Use $cflow-edit 帮我诊断并修改这篇草稿，同时保留我的声音。
Use $cflow-package 为这篇内容生成标题、hook 和平台发布版本。
Use $cflow-marketing 帮我判断这条内容应该做软广、硬广还是完整转化路径。
```

点名某个 skill 只代表“从这个视角开始”，不代表排他执行。比如 `$cflow-package` 发现 offer 不清时，应该回跳 `$cflow-marketing`；`$cflow-draft` 发现主张弱时，应该先用 `$cflow-angle`。

## 常见链路

```text
cflow -> cflow-brief -> cflow-topic -> cflow-angle
cflow -> cflow-brief -> cflow-draft
cflow -> cflow-angle -> cflow-draft -> cflow-package
cflow -> cflow-account -> cflow-topic -> cflow-package
cflow -> cflow-marketing -> cflow-package
cflow-research -> cflow-draft -> cflow-seo
cflow-edit -> cflow-voice -> cflow-package
cflow-benchmark -> cflow-angle -> cflow-draft
cflow-review -> cflow-topic -> cflow-package
```

这些是常见组合，不是硬编码流程。实际执行时按用户目标、素材状态、事实边界和交付物决定最短链路。

## Skill 清单

| Skill | 什么时候用 | 示例 |
|---|---|---|
| `$cflow` | 总入口、任务编排、能力层拆解、素材边界和端到端交付边界。 | `Use $cflow 帮我判断这件事该怎么拆成内容生产流程。` |
| `$cflow-brief` | 想法还模糊，需要采访、讨论、追问、盘点素材或生成 content brief。 | `Use $cflow-brief 先问我问题，把这个想法整理成 brief。` |
| `$cflow-topic` | 需要生成选题、评估选题、建立选题池、把模糊方向变成具体 topic。 | `Use $cflow-topic 从这些业务背景里找 10 个值得写的选题。` |
| `$cflow-angle` | 选题太平，需要主张、矛盾、读者张力、premise 或更 hookable 的 angle。 | `Use $cflow-angle 帮我比较这几个角度哪个最有阅读理由。` |
| `$cflow-research` | 需要查资料、核查事实、找来源、找数据、整理 source pack 或 research brief。 | `Use $cflow-research 帮我查证这个说法，并整理可引用来源。` |
| `$cflow-benchmark` | 需要找对标、拆爆款、拆账号、做 copywork、迁移别人的内容模式。 | `Use $cflow-benchmark 帮我找 5 个值得模仿的账号并拆结构。` |
| `$cflow-account` | 需要诊断自己的账号定位、主页、栏目、数据反馈、转化路径或生产系统。 | `Use $cflow-account 帮我看看这个账号为什么没起色。` |
| `$cflow-viral` | 需要提高分享、转发、截图传播、二创、讨论度或设计 viral 机制。 | `Use $cflow-viral 诊断这条内容为什么不容易被转发。` |
| `$cflow-seo` | 需要 SEO/GEO/AEO/LLMO、关键词、搜索意图、FAQ、结构化答案或 AI 可引用结构。 | `Use $cflow-seo 把这篇文章改成更容易被搜索和 AI answer 引用的结构。` |
| `$cflow-case` | 观点太干，需要真实案例、假设故事、类比、反面案例、微场景或未来预演。 | `Use $cflow-case 给这个观点找 3 个不同类型的案例。` |
| `$cflow-draft` | 已经有 brief、angle、大纲、笔记、转录或素材，需要写完整一稿。 | `Use $cflow-draft 根据这份 brief 写一篇 newsletter 草稿。` |
| `$cflow-shortform` | 需要短帖、短视频脚本、小红书图文、X/Twitter、LinkedIn、thread 或长文拆短。 | `Use $cflow-shortform 把这篇长文拆成 5 条 LinkedIn 短帖。` |
| `$cflow-edit` | 已有草稿，需要结构手术、段落重排、清晰化、降 AI 味、保留作者声音。 | `Use $cflow-edit 诊断这篇草稿的问题，并做最小必要修改。` |
| `$cflow-voice` | 需要建立 voice profile、提炼作者声音、判断不像本人之处、整理表达禁区。 | `Use $cflow-voice 从这些样稿里提炼我的写作声音。` |
| `$cflow-marketing` | 内容要服务转化，需要判断硬广/软广、offer、CTA、funnel、lead magnet 或购买路径。 | `Use $cflow-marketing 帮我设计这条内容的主 CTA 和转化路径。` |
| `$cflow-package` | 内容接近完成，需要标题、hook、opening、subtitle、CTA、caption 或平台发布包。 | `Use $cflow-package 给这篇文章起标题并写 5 个开头。` |
| `$cflow-image` | 需要封面、插图、配图、文章头图、社交图、thumbnail text、视觉 brief 或图片 prompt。 | `Use $cflow-image 为这篇内容设计封面方案和图片生成 prompt。` |
| `$cflow-review` | 内容已经发布或草稿失败，需要复盘指标、评论、受众反馈和下一轮实验。 | `Use $cflow-review 分析这次发布为什么表现不好。` |
| `$cflow-maintain` | 需要维护 CFlow skill 系统：新增规则、移动规则、合并重复、删除过时内容和结构校验。 | `Use $cflow-maintain 判断这条新规则应该更新到哪个 skill。` |

## 事实和素材边界

CFlow 默认不联网。用户提供的产品信息、活动信息、卖点、链接、案例和背景，默认作为原始素材使用。

只有这些情况进入 `$cflow-research`：

- 用户明确要求搜索、核查、查证、找来源、找最新信息或整理引用。
- 交付物要求带来源、证据包、引用或严谨事实判断。
- 生产内容时必须引入用户没有提供的新外部事实、数据、案例、政策、价格、产品变化或竞品现状。

基于用户素材改写、包装或营销强化时，不得新增素材没有支撑的事实、功能、服务、承诺或运营范围。确实需要补信息时，应单独标成“建议补充”，不要混进成稿。

## 维护原则

- 先判断问题类型，再决定修法。
- 按根因收口，不按现象修补。
- 每条规则只保留一个主要真源，不复制到多个 skill。
- 迁移调用点后删除旧规则、旧 helper、旧恢复逻辑和兼容层。
- `SKILL.md` 保持精简，详细模式放到对应 `references/`。
- 修改 skill 系统前先按 `$cflow-maintain` 给出计划，获得明确批准后再编辑。
- 不维护中英双语全文；CFlow 以中文为规则真源，只保留必要英文关键词。

## 仓库结构

```text
cflow/
  skills/              # skill 真源，中文规则继续放这里
  scripts/             # 校验、索引、迁移、生成等维护脚本
  tests/               # 结构校验和回归测试
  schemas/             # skill metadata / agent yaml / registry 结构文档
  pyproject.toml       # Python 工程入口
```

每个 skill 通常包含：

```text
skills/cflow-xxx/
  SKILL.md             # skill 入口、边界、工作流和 reference 指针
  references/          # 详细规则、模式、协议或方法库
  agents/openai.yaml   # 可选，Codex/OpenAI agent 展示文案
```

## 快速校验

运行：

```powershell
python scripts/quick_validate.py
```

校验内容包括：

- 每个 skill 目录都有 `SKILL.md`。
- `SKILL.md` frontmatter 包含 `name` 和 `description`。
- `name` 和目录名一致。
- `references/...`、`agents/...` 引用的本地文件真实存在。
- `$cflow-*` 引用指向真实 skill。
- `agents/openai.yaml` 结构满足 CFlow agent metadata 约定。
- `cflow` 总入口列出的 `$cflow-*` 与实际 skill 目录一致。

## 生成索引

运行：

```powershell
python scripts/build_registry.py --output build/cflow-registry.json
```

索引由 `skills/` 真源生成，包含 skill 名称、description、reference 文件、agent metadata 和正文中引用到的 `$cflow-*`。

## 同步 Codex 个人 Skill 链接

这一节只适用于 Codex 的个人 skill 发现机制。

当前仓库把 CFlow 真源放在“仓库根目录的 `skills/`”里，没有直接放进 Codex 个人 skill 目录，所以需要在 `$HOME\.codex\skills` 下创建 junction 链接，方便 Codex 发现 `$cflow-*`。如果你的部署方式是把 skill 目录本身直接放到 Codex 个人 skill 目录里，就不需要运行这个同步脚本。

其他 AI Agent 或 AI 工具不受这个脚本约束；它们可以按自己的插件、工具、skills 或 prompt 发现机制自行兼容 CFlow 的 `skills/` 真源。

检查将要创建和删除的链接：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/sync_personal_skills.ps1 -DryRun -PruneStale
```

补齐缺失链接，并删除已经失效的 CFlow junction：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/sync_personal_skills.ps1 -PruneStale
```

脚本会创建缺失的 Codex junction。带 `-PruneStale` 时，只删除满足这些条件的旧链接：名字是 `cflow*`、类型是 junction、target 指向本仓库 `skills/`、且 target 已不存在。如果目标位置已经存在但不是指向本仓库真源的 junction，会直接失败，不会覆盖。

脚本默认从自身位置推导仓库根目录，并使用 `$HOME\.codex\skills` 作为 Codex 个人 skill 目录。路径不同可以显式传参：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/sync_personal_skills.ps1 -RepoRoot "你的仓库路径" -PersonalSkillsDir "你的 Codex 个人 skill 目录" -PruneStale
```

## 测试

运行：

```powershell
python -m unittest discover -s tests
```

当前测试覆盖校验器的核心解析、失败路径和 registry 生成。新增维护脚本时，应补对应测试。

## 推荐维护流程

1. 判断用户输入是规则、流程、缺陷报告、测试用例、平台笔记、声音准则、删除请求还是 skill 系统架构请求。
2. 读取相关 `SKILL.md` 和必要 `references/`，确认已有覆盖、重复、冲突或缺失。
3. 给出明确修改计划，说明要改哪些 skill 文件或直接服务 skill 生命周期的工具链文件、移动什么、删除什么、如何校验。
4. 用户明确批准后再编辑 skill 文件。
5. 运行 `python scripts/quick_validate.py`。
6. 创建、删除或重命名 skill 后运行 `powershell -ExecutionPolicy Bypass -File scripts/sync_personal_skills.ps1 -PruneStale`。
7. 涉及脚本时运行 `python -m unittest discover -s tests`。
8. 只有用户明确要求提交，或批准计划包含提交时，才在校验通过后提交。
