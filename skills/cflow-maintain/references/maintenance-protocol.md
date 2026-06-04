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

- 统筹和套件路由放 `cflow-content`。
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
- 标题、hook、CTA 和平台发布变体放 `cflow-package`。
- 表现学习和下一次实验放 `cflow-review`。
- 维护流程放 `cflow-maintain`。

## 源码布局

唯一可编辑真源是 monorepo：

```text
D:\Code\cflow
└── skills
    ├── cflow-content
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
- 只有套件边界变化时才更新 `cflow-content` 路由。
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
