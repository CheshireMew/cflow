---
name: cflow-draft
description: CFlow 成稿系统。用于从 brief、angle、大纲、原始笔记、转录、诊断结果或素材中写出可发布的一稿。适用于文章、帖子、thread、newsletter、脚本、短视频脚本、小红书/RED、LinkedIn、Twitter/X、blog 等。触发场景包括：帮我写成一篇、根据素材成稿、从 brief 写 draft、把转录整理成内容。
---

# CFlow 成稿

## 边界

只负责第一版完整草稿。除非完成草稿必须需要，否则不要生成大量选题或标题。硬广/软广、offer、CTA 强度和转化路径先交给 `$cflow-marketing` 判断。作者声音画像不清时先交给 `$cflow-voice`。

从稳定 brief 开始写。如果选题或角度明显弱，先做轻量修复并说明假设。

## 工作流

1. 确认或推断目标、读者、平台、格式、主张、证据、voice profile 和约束。
2. 选择一个适合格式的结构。
3. 围绕主张抽取并排序素材。
4. 先写具体例子，再抽象总结。
5. 按 voice profile 保留作者声音，去掉泛泛的填充。
6. 检查是否只有一个主张、是否适配平台、是否有证据、结尾是否成立。
7. 如果内容有转化目标，先确认 `$cflow-marketing` 已定义 offer、CTA 和 funnel stage。
8. 深度修改交给 `$cflow-edit`；标题和 hook 交给 `$cflow-package`。

## 输出

写长内容时返回：

- brief 假设
- 草稿
- 缺失证据或高风险主张
- 下一步编辑或包装建议

短内容直出时，先给草稿，说明保持最少。

## 参考

当需要选择结构或跨平台成稿时，读取 `references/draft-structures.md`。
