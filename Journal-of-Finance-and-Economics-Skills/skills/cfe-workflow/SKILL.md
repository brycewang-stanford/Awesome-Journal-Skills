---
name: cfe-workflow
description: Use when deciding which cfe-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for 《财经研究》 (Journal of Finance and Economics). Routes — does not replace — the specialized skills.
---

# 财经研究工作流（cfe-workflow）

## 总览

这是路由器，它不替代任何专用 Skill。它告诉你**当前阶段应该用哪一个 cfe-* skill**。

默认假设：除非用户明确说明目标期刊不是《财经研究》，否则按 CSSCI 综合性财经期刊《财经研究》（上海财经大学主办）的编委口味处理——偏好有理论贡献、用现代因果识别、回应中国现实问题的实证研究。

## 触发时机

- 用户问"我下一步该做什么？"
- 用户甩过来一份初稿，需要判断当前瓶颈
- 实证、写作、回复来回切，状态混乱
- 收到了《财经研究》的双盲外审意见，需要切换到 rebuttal 模式

## 路由表

| 当前症状                                          | 下一个 Skill                  |
|----------------------------------------------|---------------------------|
| 选题想法模糊，担心理论贡献不够或与中国现实脱节        | `cfe-topic-selection`     |
| 文献综述缺中文经典 / 缺理论文献                       | `cfe-literature-review`   |
| 实证只有 OLS，担心识别策略不过关                     | `cfe-identification`      |
| 主结果有了，但没机制分析                              | `cfe-mechanism`           |
| 没切异质性 / 切分维度过少                            | `cfe-heterogeneity`       |
| 表格列数过多 / 注释不规范 / 不像《财经研究》风格        | `cfe-tables-figures`      |
| 文末没有政策含义，或写得太"操作化"                    | `cfe-policy-implication`  |
| 摘要写成套话，没量化结果 / 中英文不对齐               | `cfe-abstract`            |
| 通篇空话套话 / 政策建议是"加强完善推进"四件套         | `cfe-style`               |
| 准备投稿，需要 checklist                            | `cfe-submission`          |
| 收到 R&R，需要写回复信                              | `cfe-rebuttal`            |

## 默认顺序

1. `cfe-topic-selection` — 先把"理论贡献 + 中国现实问题"定下来
2. `cfe-literature-review` — 中英文献并重，理论文献必引
3. `cfe-identification` — 准实验识别（DID / IV / RDD / DML / PSM）
4. `cfe-mechanism` — 机制路径
5. `cfe-heterogeneity` — 异质性切分
6. `cfe-tables-figures` — 主表 / 主图最终化
7. `cfe-policy-implication` — 政策含义（意义层）
8. `cfe-abstract` — 摘要五句法 + 黑名单短语清除
9. `cfe-style` — 全文语言风格 polish
10. `cfe-submission` — 投稿前 preflight
11. `cfe-rebuttal` — 双盲外审后

> `cfe-abstract` 与 `cfe-style` 是**后段 polish 阶段**触发，不要在识别策略未立住时去做。

## 决策口诀

- "我有数据但没理论故事 / 不知道为什么在中国值得做" → `cfe-topic-selection`
- "综述里没引该理论分支的经典文献 / 没引近 3 年同主题中文文献" → `cfe-literature-review`
- "DID 用了 TWFE 但没回应近年交错处理批评" → `cfe-identification`
- "我只能说'我们认为可能是因为...'" → `cfe-mechanism`
- "异质性只切了东中西或国企非国企" → `cfe-heterogeneity`
- "主表 8 列以上 / 数据写'公开渠道'" → `cfe-tables-figures`
- "我建议政府重视该问题" → `cfe-policy-implication`
- "摘要里没有量化结果 / 全是套话" → `cfe-abstract`
- "全文'具有重要意义'命中 ≥ 3 处" → `cfe-style`
- "明天就要投了" → `cfe-submission`
- "收到双盲审稿意见" → `cfe-rebuttal`

## 与《经济研究》Skills 的差异

如果稿子偏纯经济学理论或结构估计、政策含义偏宏观原理，[Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) 可能更合适。两者核心差异：

- 《财经研究》：综合性财经，偏**实证 + 现代因果识别 + 中国现实问题**，理论贡献服务于现实问题
- 《经济研究》：理论贡献优先，结构估计 / 理论实证占比更高

如果稿子偏管理学 / 案例 / 实务可操作政策，使用《管理世界》方向的技能更合适。

## 反模式

- **不要**跳过 `cfe-literature-review` 直接进识别——审稿人首先看理论定位与文献对话
- **不要**让 `cfe-tables-figures` 在识别策略未立住时就美化表格
- **不要**让 `cfe-rebuttal` 在你修订正文之前生成回复信

## 《财经研究》二次操作审查

先锁定核心问题、识别链条、机制证据和可执行的政策含义，再判断稿件是否回应中文财经学术审稿人会同时追问选题政策价值、识别可信度和本刊栏目适配。

- **Router pass**：Run fit gate, evidence gate, writing gate, source-map gate, and output contract; stop when a gate lacks evidence.
- **决策账本**：返回“主张 / 证据 / 阻断点 / 下一处改稿”四列，避免只给笼统建议。
- **改投比较**：对照《经济研究》用于更强理论/全国性贡献，《管理世界》用于管理实践与政策治理，《金融研究》用于金融专门议题；若相邻刊物拥有更强读者匹配，先建议改投而不是继续润色。
- **核验底线**：给投稿就绪判断前，必须重开 `resources/official-source-map.md`，列出仍可能改变建议的一个未核实事实。
