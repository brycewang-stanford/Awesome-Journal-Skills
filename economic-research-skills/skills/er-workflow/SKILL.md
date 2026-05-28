---
name: er-workflow
description: Use when deciding which er-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for 《经济研究》 (Economic Research Journal). Routes — does not replace — the specialized skills.
---

# 经济研究工作流（er-workflow）

## 总览

这是路由器，它不替代任何专用 Skill。它告诉你**当前阶段应该用哪一个 er-* skill**。

默认假设：除非用户明确说明目标期刊不是《经济研究》，否则按 CSSCI 一区《经济研究》的编委口味处理。

## 触发时机

- 用户问"我下一步该做什么？"
- 用户甩过来一份初稿，需要判断当前瓶颈
- 实证、写作、回复来回切，状态混乱
- 收到了《经济研究》的外审意见，需要切换到 rebuttal 模式

## 路由表

| 当前症状                                          | 下一个 Skill                  |
|----------------------------------------------|---------------------------|
| 选题想法模糊，担心理论贡献不够                       | `er-topic-selection`      |
| 文献综述缺中文经典 / 缺理论文献                       | `er-literature-review`    |
| 实证只有 OLS，担心识别策略不过关                     | `er-identification`       |
| 主结果有了，但没机制分析                              | `er-mechanism`            |
| 没切异质性 / 切分维度过少                            | `er-heterogeneity`        |
| 表格列数过多 / 注释不规范 / 不像《经济研究》风格        | `er-tables-figures`       |
| 文末没有政策含义，或写得太"操作化"                    | `er-policy-implication`   |
| 准备投稿，需要 checklist                            | `er-submission`           |
| 收到 R&R，需要写回复信                              | `er-rebuttal`             |

## 默认顺序

1. `er-topic-selection` — 先把"理论贡献 + 中国问题"定下来
2. `er-literature-review` — 中英文献并重，理论文献必引
3. `er-identification` — 准实验识别
4. `er-mechanism` — 机制路径
5. `er-heterogeneity` — 异质性切分
6. `er-tables-figures` — 主表 / 主图最终化
7. `er-policy-implication` — 政策含义（意义层）
8. `er-submission` — 投稿前 preflight
9. `er-rebuttal` — 外审后

## 决策口诀

- "我有数据但没理论故事" → `er-topic-selection`
- "综述里没引 North / Acemoglu / 林毅夫" → `er-literature-review`
- "DID 用了 TWFE 但没回应近年异质性处理批评" → `er-identification`
- "我只能说'我们认为可能是因为...'" → `er-mechanism`
- "异质性只切了东中西" → `er-heterogeneity`
- "主表 8 列以上" → `er-tables-figures`
- "我建议政府重视该问题" → `er-policy-implication`
- "明天就要投了" → `er-submission`
- "收到 3 份审稿意见" → `er-rebuttal`

## 与《管理世界》Skills 的差异

如果稿子偏管理学 / 案例 / 实务，使用 [management-world-skills](https://github.com/brycewang-stanford/management-world-skills) 更合适。两者的核心差异：

- 《经济研究》：理论贡献优先，政策含义偏意义层
- 《管理世界》：实践契合优先，政策建议偏可操作

## 反模式

- **不要**跳过 `er-literature-review` 直接进识别——审稿人首先看理论定位
- **不要**让 `er-tables-figures` 在识别策略未立住时就美化表格
- **不要**让 `er-rebuttal` 在你修订正文之前生成回复信
