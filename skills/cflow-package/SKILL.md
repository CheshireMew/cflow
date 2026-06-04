---
name: cflow-package
description: CFlow 包装系统。用于为接近完成的内容创建 title、hook、opening、subtitle、CTA、caption、平台文本版本和发布包。触发场景包括：起标题、优化开头、短视频前三秒、LinkedIn headline、Twitter/X thread first post、newsletter/blog 标题、平台文案适配、提高点击和停留。
---

# CFlow Package

## 边界

只负责文本呈现和平台文案适配。除非包装过程暴露出核心主张不清，否则不要改内容主张；如果发现问题，只提出最小修法。封面、插图、配图、thumbnail text、cover text、视觉 brief 和图片 prompt 归 `$cflow-image`。硬广/软广、offer、funnel stage 和转化路径归 `$cflow-marketing`。作者人格、表达禁区和 voice profile 归 `$cflow-voice`。

包装应该放大内容真实价值，不制造假刺激。

包装前先判断正文质量。弱 hook 会杀死强内容，但强 hook 也救不了空内容；如果核心主张、证据、故事或读者收益不足，先指出缺口，不要继续生成更刺激的版本。

## 工作流

1. 明确平台、读者、核心主张和希望读者采取的行动。
2. 检查内容是否有可兑现的张力、证据和 payoff。
3. 从内容中提取最可点击但真实的张力。
4. 按类型生成包装选项：标题、hook、opening、subtitle、CTA、caption 或平台文本版本。
5. 每个选项标注策略来源，例如认知冲突、好奇缺口、身份代入、数字锚定、恐惧损失、结果承诺、社会证明、场景条件、行动号召。
6. 选项要策略不同，不要只是同义改写。
7. 标出最佳选项，并简要说明选择标准。
8. 如果标题、hook 或 CTA 明显不像作者，先交给 `$cflow-voice` 校准。
9. 如果 CTA 强度、offer 或转化路径不清，先交给 `$cflow-marketing`。
10. 发布后有数据时交给 `$cflow-review`。

## 输出

标题或 hook 请求：

- 最佳选项
- 备选项
- 每个选项的策略标签
- 为什么最佳
- 需要避免的风险

发布包请求：

- 标题或 headline
- 开头或 hook
- 必要的正文框架
- CTA
- 平台说明
- 策略说明

## 参考

当需要跨平台生成变体或避免 clickbait 时，读取 `references/package-patterns.md`。
