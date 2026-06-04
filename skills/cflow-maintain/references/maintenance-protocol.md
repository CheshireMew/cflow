# 维护协议

## 输入分类

把用户提供的每一项归类为：

- **规则**：会长期约束行为的指令。
- **流程步骤**：可重复执行的动作序列。
- **决策标准**：用于在选项之间做选择的判断。
- **平台笔记**：小红书/RED、短视频、LinkedIn、Twitter/X、blog、newsletter 等平台专用规则。
- **声音准则**：关于保留或塑造作者声音的说明。
- **缺陷报告**：使用 CFlow skill 时观察到的失败。
- **测试用例**：可用于验证行为的真实例子。
- **删除请求**：应该移除的规则或资源。
- **架构请求**：边界、路由、命名或仓库结构变化。

## 归属判断

把每项内容放到最窄、最耐用的边界。

- 统筹、套件路由、任务编排和能力层拆解放 `cflow`。
- 写作前采访、讨论、追问缺失信息、素材盘点和 content brief 构建放 `cflow-brief`。
- 资料搜寻、事实核查、来源评估、证据包和引用整理放 `cflow-research`。
- 发现和评分放 `cflow-topic`。
- 内容对标、账号拆解、爆款结构拆解和 copywork 颗粒度检查放 `cflow-benchmark`。
- 分享动机、传播单元、二创入口、截图传播和病毒式传播复盘放 `cflow-viral`。
- SEO/GEO/AEO/LLMO、搜索意图、关键词、主题集群和 AI 可引用结构放 `cflow-seo`。
- 案例故事、真实性标注、未来预演、假设故事和支撑性例子放 `cflow-case`。
- 主张和读者张力放 `cflow-angle`。
- 从结构到草稿的指导放 `cflow-draft`。
- 短帖、短视频脚本、小红书图文、社交帖、短内容系列和长文拆短放 `cflow-shortform`。
- 修改诊断和声音保留放 `cflow-edit`。
- 作者声音画像、写作人格、灵魂倾向和表达禁区放 `cflow-voice`。
- 硬广/软广、offer、CTA 强度、funnel stage 和转化路径放 `cflow-marketing`。
- 标题、hook、CTA、caption 和平台文本变体放 `cflow-package`。
- 封面、插图、配图、文章头图、thumbnail text、cover text、视觉 brief 和图片 prompt 放 `cflow-image`。
- 表现学习和下一次实验放 `cflow-review`。
- 维护流程放 `cflow-maintain`。

## 源码布局

唯一可编辑真源是 monorepo：

```text
D:\Code\cflow
└── skills
    ├── cflow
    ├── cflow-brief
    ├── cflow-research
    ├── cflow-topic
    ├── cflow-benchmark
    ├── cflow-viral
    ├── cflow-seo
    ├── cflow-case
    ├── cflow-angle
    ├── cflow-draft
    ├── cflow-shortform
    ├── cflow-edit
    ├── cflow-voice
    ├── cflow-marketing
    ├── cflow-package
    ├── cflow-review
    └── cflow-maintain
```

`C:\Users\Lenovo\.codex\skills` 下可以有 Codex 发现链接，但不要通过链接编辑。修改 `D:\Code\cflow` 中的源码，然后校验并提交。

如果一条规则似乎适合多个 skill，先判断根行为。只添加一个主要规则；只有路由需要时才在其他 skill 加短提示。

## 缺陷归因

处理缺陷报告时，先命名根行为，不要按表面场景直接写规则。

常见根行为包括：

- **已有规则未执行**：skill 已经覆盖，但输出没有遵守。
- **规则缺失**：现有 skill 没有可执行约束。
- **路由缺失**：任务应进入另一个 skill，但入口没有触发。
- **边界冲突**：多个 skill 对同一行为给出不同方向。
- **素材越界**：输出新增了用户素材没有支撑的事实、功能、承诺、服务或运营范围。
- **测试用例不足**：规则存在，但缺少能暴露失败的真实样例。

只有确认根行为后，才决定新增、收紧、移动、删除规则或补测试用例。不能把执行失败自动当作 skill 缺规则。

## 泛化检查

从失败案例提炼规则时，禁止把案例里的具体平台、格式、对象、行业或文案场景直接固化为触发条件。

先做同类替换测试：

```text
把案例中的平台、格式、对象、行业或具体素材替换成同类变量后，这条规则是否仍成立？
```

如果仍成立，规则必须写成可迁移约束；具体案例只能作为测试用例或例子。

例子：

```text
不够好：群简介 / bio / 置顶简介改写时，不得新增原文没有的群功能。
更好：用户提供明确原始素材时，改写、包装、营销强化都不得新增未被素材支撑的事实、功能、承诺、服务或运营范围；如果转化需要补信息，必须标注为建议补充，而不是混进成稿。
```

维护计划里要分清：

- **长期规则**：可迁移到多个同类场景的行为约束。
- **测试用例**：这次暴露失败的具体素材和场景。
- **例子**：帮助理解规则，但不作为唯一触发条件。

## 语言规则

CFlow 使用中文作为唯一正文真源：

- `SKILL.md` 和 `references/` 用中文写规则。
- `name` 保持英文技术名。
- `description` 用中文描述，同时保留必要英文触发关键词。
- `agents/openai.yaml` 的展示文案用中文。
- 不维护中英双语全文，不创建平行 `zh` / `en` 真源。
- 如果未来需要英文版，作为独立导出版生成。

## 覆盖状态

使用这些标签：

- **已覆盖**：不用改。
- **部分覆盖**：收紧或扩展现有规则。
- **重复**：合并到最佳位置并删除重复。
- **冲突**：选择符合 CFlow 边界的规则；业务意图不清时问用户。
- **新规则**：添加到最窄 skill 或 reference。
- **过时**：不再符合架构时删除。

## 重构规则

- 每条规则只保留一个事实源。
- 迁移后不要保留旧 helper、旧流程或兼容解释。
- 优先移动规则，不复制规则。
- `SKILL.md` 保持精简，详细模式放 `references/`。
- 只有套件边界、编排规则或协作调度变化时才更新 `cflow`。
- 规则真源归属和任务执行协作不是一回事。每条规则只保留一个主要归属，是为了避免知识库漂移；一次用户任务可以由多个 skills 串联、并行或回跳协作完成。
- 只有展示 metadata 过时时才更新 `agents/openai.yaml`。

## 审批标准

用户必须批准：

- 受影响仓库或目录
- 要编辑的文件
- 要新增、移动、合并或删除的规则
- 校验计划
- 提交计划

如果用户修改计划，先重写计划并再次请求批准。

## 校验

运行：

```powershell
$env:PYTHONPATH='D:\Code\.codex-python-libs'
python 'C:\Users\Lenovo\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '<skill-path>'
```

校验所有变更 skill。只要套件路由、所有权边界或共享约定变化，就校验全部 CFlow skills。

## 提交

校验通过后再提交。commit message 保持聚焦：

- `Update <skill> <rule-area>`
- `Move <rule> into <skill>`
- `Refine CFlow routing`
- `Remove duplicate <rule-area> guidance`
- `Localize CFlow skills to Chinese source`

多个仓库变化时分别提交。当前 CFlow 是 monorepo，通常提交一次即可。
