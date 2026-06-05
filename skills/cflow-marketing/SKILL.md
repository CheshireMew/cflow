---
name: cflow-marketing
description: CFlow 营销转化系统。用于判断内容如何服务转化，而不是普通写作。触发场景包括：硬广、软广、advertorial、native ad、direct response、offer 表达、CTA 设计、转化路径、funnel stage、冷流量/暖流量/高意向人群、lead magnet、私信转化、预约、购买、landing page、sales page、广告脚本、品牌内容和销售内容之间的边界判断。
---

# CFlow 营销

## 边界

负责“内容如何服务转化”。不要替代 `cflow-draft` 写完整正文，也不要替代 `cflow-package` 批量生成标题、hook 或 CTA 文案变体。

`cflow-marketing` 是转化策略层，不是包装文案层。offer、funnel stage、CTA 类型、CTA 强度、主转化路径和异议处理归 `$cflow-marketing`；标题、hook、opening、短发布文案和已经确定策略后的 CTA 文案包装归 `$cflow-package`。如果用户只要“这句话怎么写得更吸引人 / CTA 怎么表达”，且 offer 和转化路径已稳定，交给 `$cflow-package`。

营销文案默认表现力优先。强 urgency、强利益、强对比、强承诺和强 CTA 可以保留并打磨；不要因为“太营销、太广告、太刺激”而自我降温。只有用户要求合规、品牌安全、发布限制或严谨事实时，才处理过度浮夸、不可兑现承诺、证据无法承载的确定性和明显诈骗感。

个人引流资产按 `$cflow` 的 profile 发现规则调用。`cflow-marketing` 可以使用 `profiles/leadgen-profile.md` 判断主引流动作，但不维护具体链接、邀请码或私有入口。

营销层先决定：

- 这是硬广、软广、原生广告还是普通内容？
- 读者处于哪个 funnel stage？
- offer 是什么？
- CTA 应该多强？
- 转化路径是什么？
- 需要什么欲望、利益、压迫感和行动路径？

## 工作流

1. **判断意图**：明确目标是曝光、建立信任、收集线索、预约、购买、复购还是转介绍。
2. **判断人群阶段**：区分冷流量、暖流量、高意向、老用户或内部受众。
3. **选择营销形态**：硬广、软广、advertorial、native ad、direct response、内容种草、案例、sales page、landing page。
4. **定义 offer**：明确给谁、解决什么问题、得到什么结果、为什么现在行动。
5. **设计 CTA**：选择低摩擦、中摩擦或高摩擦动作。
6. **补转化桥**：决定从内容到行动之间需要哪些利益、情绪、故事、异议处理、社会证明或机制解释。
7. **保护销售温度**：处理异议和边界时融入正文，不默认添加泄气的风控尾巴。
8. **交付给生产层**：正文交给 `$cflow-draft`；标题、hook、opening、短发布文案和 CTA 文案变体交给 `$cflow-package`；发布后转化数据交给 `$cflow-review`。

## 输出

返回：

- 营销目标
- 受众阶段
- 推荐形态
- Offer 表达
- CTA 类型和文案方向
- 可以继续放大的卖点
- 需要处理的异议
- 转化路径
- 应交给哪个 CFlow skill 执行下一步

## 参考

当需要判断硬广/软广、offer、CTA、funnel、转化路径或销售页面结构时，读取 `references/marketing-system.md`。
