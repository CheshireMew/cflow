---
name: cflow-package
description: CFlow 包装系统。用于为接近完成的内容创建 title、hook、opening、subtitle、CTA、caption、平台文本版本和发布包。触发场景包括：起标题、优化开头、短视频前三秒、LinkedIn headline、Twitter/X thread first post、newsletter/blog 标题、平台文案适配、提高点击和停留。
---

# CFlow Package

## 边界

只负责文本呈现和平台文案适配。默认可以为了点击、停留和行动压力重排表达；只有用户要求最小改动、严谨包装或作者声音时，才限制改动幅度。封面、插图、配图、thumbnail text、cover text、视觉 brief 和图片 prompt 归 `$cflow-image`。硬广/软广、offer、funnel stage 和转化路径归 `$cflow-marketing`。作者人格、表达禁区和 voice profile 归 `$cflow-voice`。

包装默认放大冲击力、点击欲和行动欲。强标题、强 hook、强 CTA、强刺激不是问题；只有用户要求严谨、合规、品牌安全或平台风控时，才检查承诺是否过度、正文是否完全兑现。

包装前先判断可放大的张力。弱 hook 会杀死内容；如果素材不够，先用现有素材生成最有冲击力的版本。广告、短视频、小红书、viral 和限时活动场景里，不要因为“刺激”就自动降温。

用户要求“更吸引人”“有点击欲”“反常识”“有技巧”，或反馈“平淡”“像提醒”“没有 hook”时，必须按不同策略重做候选。不要只把原句改顺；至少给出 3 种策略不同的 hook，并标注策略来源。

## 工作流

1. 明确平台、读者、核心主张和希望读者采取的行动。
2. 检查内容有哪些可放大的张力、利益和行动压力。
3. 从内容中提取最可点击、最能推动行动的张力。
4. 按类型生成包装选项：标题、hook、opening、subtitle、CTA、caption 或平台文本版本。
5. 每个选项标注策略来源，例如认知冲突、好奇缺口、身份代入、数字锚定、恐惧损失、结果承诺、社会证明、场景条件、行动号召。
6. 选项要策略不同，不要只是同义改写。
7. 如果用户已经反馈上一版平淡或没技巧，必须换策略组，不要沿用同一种提醒式表达。
8. 标出最佳选项，并简要说明选择标准。
9. 只有用户要求作者声音时，才把标题、hook 或 CTA 交给 `$cflow-voice` 校准。
10. 如果 CTA 强度、offer 或转化路径不清，先交给 `$cflow-marketing`。
11. 发布后有数据时交给 `$cflow-review`。

## 输出

标题或 hook 请求：

- 最佳选项
- 备选项
- 每个选项的策略标签
- 为什么最佳
- 可以继续加压的方向

发布包请求：

- 标题或 headline
- 开头或 hook
- 必要的正文框架
- CTA
- 平台说明
- 策略说明

## 参考

当需要跨平台生成变体、强 hook 或平台包装时，读取 `references/package-patterns.md`。
