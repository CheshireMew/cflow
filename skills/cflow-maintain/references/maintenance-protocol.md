# 维护治理协议

本协议只维护 CFlow skill 系统的治理规则。新材料吸收、内容方法论提炼、样稿迁移和生产能力升级归 `$cflow-absorb`。

## 治理对象

允许治理：

- `skills/` 里的 `SKILL.md`、`references/`、`agents/openai.yaml`。
- skill 路由、边界、命名、目录结构和发现入口。
- 直接服务 skill 生命周期的 schema、校验脚本、registry/sync 脚本、测试和 README 相关段落。
- 旧架构、旧 helper、旧导出、旧恢复逻辑和不再使用的兼容层。

排除治理：

- 普通内容产物。
- 个人复盘、截图、指标、私有案例和账号资料。
- 作者声音画像和普通内容生产资产，除非它们被明确纳入治理计划。
- 普通项目工程、环境配置或与 skill 生命周期无关的文件。

## 唯一事实源

每条规则只能有一个主要真源。

判断顺序：

1. 套件编排、profile 发现、运行资产发现：`skills/cflow/references/cflow-framework.md`。
2. 跨生产 skill 的写作纪律：`skills/cflow/references/content-production-contract.md`。
3. 专项生产方法：对应专项 skill 的 `SKILL.md` 或 `references/`。
4. 作者表达偏好：唯一 `profiles/voice-profile.md`，由 `$cflow-voice` 维护。
5. 普通生产资产：`profiles/content-assets/`，只作为运行资产，不是通用规则真源。
6. skill 治理流程：`skills/cflow-maintain/`。
7. 吸收进化流程：`skills/cflow-absorb/`。

如果一条规则似乎适合多个 skill，先判断根行为。只保留一个主要原则真源；只有路由需要时才在第二个 skill 写短提示，不复制完整规则。

## 三层规则结构

共享合同不能被当作生产时一定会读取和执行的运行依赖。跨 skill 写作纪律按三层维护：

1. **共享合同**：保留底层原则、通用反模式、素材和事实边界。
2. **专项 skill 本地闸门**：保留该场景最容易失败、必须当场执行的短规则。
3. **回归样例**：保留高频失败输入和合格 / 失败输出形态，防止规则写了但再次犯。

治理判断：

- 原则不复制，仍以 `content-production-contract.md` 为真源。
- 执行闸门可以在专项 skill 局部重复，但必须短、硬、可检查。
- 回归样例放在最容易失败的专项 skill，不放进共享合同。
- 禁止把共享合同全文复制到各 skill；只下沉高风险失败点。
- 如果某条共享规则连续在某个生产 skill 里失效，优先补该 skill 的本地闸门或回归样例，而不是继续强化共享合同。

## 覆盖状态

使用这些标签：

- **已覆盖**：不用改。
- **部分覆盖**：收紧或扩展现有规则。
- **重复**：合并到最佳位置并删除重复。
- **冲突**：选择符合 CFlow 边界的规则；业务意图不清时问用户。
- **新规则**：添加到最窄真源。
- **过时**：不再符合架构时删除。
- **应移动**：规则有价值，但放错文件。
- **应删除**：规则无效、误导、重复或属于旧架构。
- **应分流**：不进通用 skill，转给 profile、用户资产、发布环境笔记、review 经验、例子或测试用例。

## 反膨胀审计

反膨胀属于治理阶段，不是吸收阶段。它不能用来阻止 `$cflow-absorb` 提炼可迁移机制；只能在已经明确“要改哪里”后，检查修改是否造成无必要膨胀。

新增前依次检查：

1. 现有规则是否已经覆盖，只是执行时没遵守。
2. 是否能收紧一条已有规则，而不是新增平行规则。
3. 是否能合并相邻规则。
4. 是否应移动到另一个真源。
5. 是否有旧规则因为这次变更需要删除。
6. 是否只是例子、测试用例或生产资产，不应成为长期规则。
7. 是否属于作者画像、业务资产、发布环境短期经验或私有素材。

只有上面都不成立，才新增长期规则。新增规则必须说明它替代、合并或强化了什么；净新增必须说明收益大于维护成本。

## 语料型 skill 治理

维护含原始语料、作者风格、对标样本、案例库、训练数据、评估集、合成样本或生成脚本的 skill 时，先做资源分层。

资源可信顺序：

1. 原始语料。
2. 人工蒸馏。
3. 派生训练 / 评估样本。
4. 合成样本。
5. 生成脚本。
6. 测试输出。

原始语料与人工蒸馏、训练数据、合成样本或生成脚本冲突时，以原始语料为真源。派生资源只能在证明不污染行为时保留；如果它们持续诱发错误输出，应删除、重建或降级为测试材料。

如果旧训练集、合成样本、生成脚本或参考文件已经成为错误行为来源，应把它们视为旧架构的一部分处理。重构完成后不要保留旧 helper、旧派生样本、旧模板或旧恢复路径。

## 重构规则

- 按根因收口，不按现象修补。
- 先确定单一来源和唯一真实边界，再迁移所有调用点。
- 迁移后不要保留旧 helper、旧流程、旧导出或兼容解释。
- 优先移动原则规则，不复制完整规则；但高风险生产闸门可以在专项 skill 局部重复。
- 优先合并和替换，不叠加相邻规则。
- 大改时追求净减少、净合并或净清晰。
- `SKILL.md` 保持精简，详细模式放 `references/`。
- 只有套件边界、编排规则或协作调度变化时才更新 `cflow`。
- 只有展示 metadata 过时时才更新 `agents/openai.yaml`。

## 发现入口同步

唯一可编辑真源是当前仓库：

```text
<repo-root>/skills/
```

`$HOME\.codex\skills` 下可以有 Codex 发现链接，但不要通过链接编辑。

创建、删除或重命名 skill 后，必须同步 Codex 个人 skill 发现入口：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/sync_personal_skills.ps1 -PruneStale
```

同步脚本只创建缺失 junction，并且只删除 stale 的 CFlow junction：名字是 `cflow*`、类型是 junction、target 指向本仓库 `skills`、且 target 已不存在。

## 校验

运行：

```powershell
python scripts\quick_validate.py
```

只要创建、删除、重命名 skill，或改动套件路由、所有权边界、共享约定，就校验全部 CFlow skills。

如果创建、删除或重命名了 skill，同步个人 skill 链接后再校验一次：

```powershell
powershell -ExecutionPolicy Bypass -File scripts\sync_personal_skills.ps1 -PruneStale
python scripts\quick_validate.py
```

## 提交

只有用户明确要求提交，或批准计划包含提交时，才在校验通过后提交。commit message 保持聚焦：

- `Update <skill> governance`
- `Move <rule> into <skill>`
- `Refine CFlow routing`
- `Remove duplicate <rule-area> guidance`
- `Add cflow-absorb`
