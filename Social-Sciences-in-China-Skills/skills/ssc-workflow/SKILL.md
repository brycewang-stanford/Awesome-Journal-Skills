---
name: ssc-workflow
description: Use when deciding which ssc-* sub-skill to invoke next, or when sequencing manuscript work from problematic framing through rebuttal for 《中国社会科学》 (Social Sciences in China). Routes — does not replace — the specialized skills.
---

# 《中国社会科学》工作流（ssc-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 ssc-* skill**。

默认假设：目标是中国社科最高综合平台《中国社会科学》（中国社会科学院主办，月刊）。衡量标准是**思想分量与原创理论贡献**，而非方法复杂度。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能冲《中国社会科学》/ 下一步做什么"
- 手头有实证发现但讲不出"大问题/原创命题"
- 学科归属摇摆，不知往哪个学科叙事靠
- 收到外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定稿子够不够格、对不对口 | `ssc-fit-positioning` |
| 问题太小 / 立不住"重大问题" | `ssc-topic-problematic` |
| 有发现没"原创理论命题"、不知如何谈贡献 | `ssc-theory-contribution` |
| 文献只堆近年实证、没进理论脉络 | `ssc-literature-dialogue` |
| 论证跳跃 / 思辨不严谨 / 概念界定含糊 | `ssc-argumentation` |
| 经验材料（定量/定性/历史）与论题脱节 | `ssc-evidence` |
| 通篇政策汇报腔 / 口号化 / 炫技 | `ssc-style` |
| 摘要写成套话 / 不合 200–300 字规范 | `ssc-abstract-keywords` |
| 准备投稿，需要体例与系统 checklist | `ssc-submission` |
| 收到外审意见，需要写回复 | `ssc-rebuttal` |

## 默认顺序

1. `ssc-fit-positioning` — 先判断匹配度，别把细分实证硬投综合刊
2. `ssc-topic-problematic` — 把"重大问题/问题意识"立住
3. `ssc-theory-contribution` — 提炼原创理论命题与自主知识体系定位
4. `ssc-literature-dialogue` — 进入理论脉络对话
5. `ssc-argumentation` — 论证链与思辨规范
6. `ssc-evidence` — 经验证据服务论题（方法多元）
7. `ssc-style` — 学理文风，去口号化
8. `ssc-abstract-keywords` — 摘要 200–300 字 + 3–5 关键词
9. `ssc-submission` — 投稿前 preflight（页下注、投稿系统）
10. `ssc-rebuttal` — 外审后

## 一次完整走查示例

设来稿为"数字监管与平台经济"的实证稿。走查路径：`ssc-fit-positioning` 判中（问题够大、命题偏验证）→ `ssc-theory-contribution` 把"监管成本"发现提炼为"监管权再分配"命题 → `ssc-topic-problematic` 把引言从政策背景改写为与监管型国家理论的争论 → `ssc-literature-dialogue` 补政治学与法学的对话对象 → `ssc-argumentation` 删一节材料铺陈、增一节反例处理 → `ssc-evidence` 给每个实证段补"因此"句 → `ssc-style` 清政策腔 → `ssc-abstract-keywords` 摘要命题前置 → `ssc-submission` 体例与匿名 preflight。全程通常两轮迭代，第二轮从论证环节起步即可，不必从头再走。

## 决策口诀

- "我有发现但没命题" → `ssc-theory-contribution`（命题立不住就别投）
- "问题像是某行业的细分评估" → `ssc-topic-problematic`（上移到制度/文明层）
- "文献全是近五年回归" → `ssc-literature-dialogue`
- "读起来像政策文件" → `ssc-style`

## 学科叙事摇摆时的定锚法

跨学科稿常在"按经济学叙事还是社会学叙事"之间摇摆。定锚顺序：先问材料的硬底在哪个学科（数据、田野还是文本），再问命题与哪个学科的理论争论真正接得上，最后让另一学科作为对话对象而非主叙事。两边都想当主叙事的稿子，在本刊的跨学科评审中容易两边失分；锚定之后再走默认顺序的第 2–4 步。

## 与本仓库其它期刊包的差异

- 偏干净因果 + 理论：转 economic-research / china-economic-quarterly
- 偏产业政策实证：转 china-industrial-economics
- 偏定量/定性社会学：转 sociological-studies
- 《中国社会科学》要的是**跨学科的大问题 + 原创理论**，方法只是证据之一

## 常见卡点与回退规则

- 命题提炼超过两轮仍立不住：多半是选题层级问题，回退 `ssc-topic-problematic`，而非继续打磨命题措辞
- 文风改了又改仍像汇报：病根常在论证缺层级，先回 `ssc-argumentation` 再谈句子
- 摘要写不进 200–300 字：通常是命题不清的下游症状，回 `ssc-theory-contribution`
- 各环节都过了仍心虚：用"五年后是否有人引用此命题"做终检，答不上来回到第 2 步

## 反模式

- **不要**跳过 `ssc-fit-positioning` 就动笔——它最常救稿（避免投错门）
- **不要**在没有原创命题时去抠摘要和文风
- **不要**让 `ssc-rebuttal` 在正文未修订前生成回复

## 阶段诊断输出

每次路由后给出：

```
【阶段】fit / problematic / theory / literature / argument / evidence / style / abstract / submission / rebuttal
【症状】<一句话>
【调用】ssc-<skill>
【门槛】通过后方可进入下一阶段的判据：<…>
【回退】若 <情形>，回到 ssc-<skill>
```
