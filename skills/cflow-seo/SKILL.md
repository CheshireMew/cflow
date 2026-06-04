---
name: cflow-seo
description: CFlow 搜索可发现性系统。用于让内容更容易被搜索引擎、AI answer、GEO、AEO、LLMO 和读者检索系统发现、理解、引用和点击。触发场景包括：SEO、GEO、AEO、LLMO、关键词、搜索意图、主题集群、SEO brief、AI 引用优化、FAQ、结构化答案、SERP 竞品、meta title、meta description、H1/H2、内部链接、搜索复盘。名字叫 SEO，但功能不只限于传统 SEO。
---

# CFlow SEO

## 边界

负责内容的“可发现性”和“可被搜索/AI 系统理解”。名字叫 SEO，但功能覆盖传统 SEO、GEO、AEO、LLMO、AI answer 可引用结构和搜索结果点击。

`cflow-seo` 不是联网搜索工具本身。需要实时 SERP、竞品页面、关键词趋势、政策、价格、人物、产品或事实核查时，使用当前环境可用的联网工具；没有联网工具时，只能做离线结构优化，并明确标注“未联网验证”。

不要替代 `$cflow-draft` 写完整草稿；不要替代 `$cflow-package` 做普通标题包装；不要替代 `$cflow-marketing` 设计 offer 和转化路径；不要替代 `$cflow-benchmark` 做完整竞品内容拆解。

## 工作流

1. **判断任务**：确认用户要的是关键词/搜索意图、SEO brief、GEO 结构、内容优化、SERP 竞品判断、发布前检查还是搜索复盘。
2. **判断数据状态**：区分已联网验证、用户提供来源、离线假设和待核查信息。
3. **识别搜索意图**：判断 informational、commercial、transactional、navigational、local、comparison、troubleshooting 或 mixed intent。
4. **建立主题结构**：确定主关键词、长尾词、实体、同义表达、相关问题、主题集群和内部链接方向。
5. **设计可发现内容结构**：给出 H1/H2、摘要、定义、步骤、比较、FAQ、证据、可引用段落和结论前置。
6. **优化 AI 可引用性**：让内容包含清楚定义、边界、列表、表格、来源、例子、判断条件和简洁答案。
7. **交接生产**：需要成稿交给 `$cflow-draft`；需要标题变体交给 `$cflow-package`；需要竞品深拆交给 `$cflow-benchmark`；需要转化目标交给 `$cflow-marketing`。
8. **复盘闭环**：发布后把收录、排名、CTR、query、AI 引用痕迹、转化和内容缺口交给 `$cflow-review`。

## 输出

SEO / GEO brief 输出：

- 目标读者
- 搜索意图
- 主关键词和长尾方向
- 主题集群
- 内容标题 / H1
- H2 结构
- 摘要或直接答案
- FAQ
- 需要补的事实或来源
- AI 可引用段落建议
- 内部链接建议
- 交接给哪个 CFlow skill

优化已有内容时输出：

- 当前可发现性问题
- 搜索意图是否匹配
- 结构修法
- 缺失问题或 FAQ
- 可引用性修法
- 标题 / meta / 摘要建议
- 待联网核查项

## 联网状态标注

涉及实时搜索结果、排名、竞品页面、关键词趋势、AI answer 倾向、政策、价格、产品、人物、公司、数据或事实时，必须标注：

```text
联网状态：已联网核查 / 用户提供来源 / 未联网验证
来源或依据：
仍需核查：
```

未联网验证的信息不能写成确定事实。

## 参考

当需要 SEO brief、GEO/AEO 结构、AI 引用优化、关键词和主题集群或搜索复盘时，读取 `references/seo-system.md`。
