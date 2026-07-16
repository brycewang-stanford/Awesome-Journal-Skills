---
name: cte-workflow
description: Use when deciding which cte-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for 《财贸经济》 (Finance & Trade Economics). Routes — does not replace — the specialized skills.
---

# 财贸经济工作流（cte-workflow）

## 总览

这是路由器，不替代任何专用 Skill。它判断你**当前处在哪个阶段、下一步该调用哪一个 cte-* skill**。

默认假设：除非用户明确说明目标不是《财贸经济》，否则按中国社会科学院财经战略研究院主办、CSSCI 与北大核心收录的《财贸经济》（月刊，创刊 1980）编委口味处理。该刊聚焦**财政、税收、金融、贸易、流通、消费**等宏观与应用经济学议题，偏好紧扣中国重大财经政策、有严谨因果识别（DID / IV / RDD / 断点 / DML）与清晰机制检验的实证研究。

## 触发时机

- 用户问"我下一步该做什么？"
- 用户甩来一份财税 / 金融 / 贸易主题初稿，需要判断当前瓶颈
- 实证、写作、回复来回切，状态混乱
- 收到《财贸经济》外审意见，需要切到 rebuttal 模式

## 路由表

| 当前症状 | 下一个 Skill |
|---|---|
| 选题模糊，不确定是否契合本刊财经议题 / 边际贡献写不出 | `cte-topic-selection` |
| 文献综述缺财经领域权威中文文献 / 缺理论对话 | `cte-literature-review` |
| 实证只有描述统计 + OLS，识别策略不过关 | `cte-identification` |
| 主结果有了，但缺机制、政策"为什么起作用"讲不清 | `cte-mechanism` |
| 没切异质性 / 切分维度脱离中国财经制度场景 | `cte-heterogeneity` |
| 表格列数过多 / 注释不规范 / 数据来源不透明 | `cte-tables-figures` |
| 文末政策含义空泛、是"加强完善推进"四件套 | `cte-policy-implication` |
| 摘要写成套话，没量化结果 / 中英文不对齐 | `cte-abstract` |
| 通篇空话套话 / 方法炫耀多于结果阐释 | `cte-style` |
| 准备投稿，需要 checklist | `cte-submission` |
| 收到 R&R，需要写回复信 | `cte-rebuttal` |

## 默认顺序

1. `cte-topic-selection` — 先把"财经议题 + 理论贡献 + 中国政策现实"定下来
2. `cte-literature-review` — 中外并重，财经领域权威文献必引
3. `cte-identification` — 因果识别（DID / IV / RDD / 断点 / DML）
4. `cte-mechanism` — 机制路径（落到微观主体 / 市场 / 制度渠道）
5. `cte-heterogeneity` — 异质性切分（落到中国财经制度场景）
6. `cte-tables-figures` — 主表 / 主图最终化（三线表 + 透明数据来源）
7. `cte-policy-implication` — 财经政策含义（意义层但落到具体政策抓手）
8. `cte-abstract` — 摘要五句法 + 黑名单短语清除
9. `cte-style` — 全文语言风格 polish
10. `cte-submission` — 投稿前 preflight
11. `cte-rebuttal` — 外审后

> `cte-abstract` 与 `cte-style` 是**后段 polish 阶段**触发，识别策略未立住前不要先做。

## 阶段快照模板

把下面的快照复制到工作笔记，每完成一阶段更新对应行；**第一处空白即当前瓶颈**，对应右侧 cte-* 入口：

```text
《财贸经济》稿件阶段快照
选题定位：财经议题=____（财政/税收/金融/贸易/流通/消费）  边际贡献一句话=____
文献对话：财经中文权威已引 __ 篇；理论/英文对话文献已引 __ 篇
识别策略：数据=____  方法=____  内生性处理=已/未
机制检验：机制路径共 __ 条，已实证检验 __ 条
异质性　：切分维度=____（须落回中国财经制度场景）
表格规范：主表为三线表？是/否   数据来源点名到库？是/否
政策含义：对应的财经政策抓手=____（禁"加强完善推进"四件套）
摘要风格：量化结果已写入摘要？是/否  "具有重要意义"命中 __ 处（目标 0）
投稿状态：submission checklist 已过 / 外审意见 __ 份待回复
```

- "我有 CSMAR / WIND 数据但没财经理论故事" → `cte-topic-selection`
- "综述里没引财政分权 / 货币政策 / 贸易的经典文献" → `cte-literature-review`
- "我只跑了城市面板的描述统计 + OLS" → `cte-identification`
- "税收征管 / 金融改革是内生的，但我没处理" → `cte-identification`
- "我只能说'我们认为可能是因为企业……'" → `cte-mechanism`
- "异质性只切了东中西" → `cte-heterogeneity`
- "主表 8 列以上" → `cte-tables-figures`
- "我建议政府重视财税改革" → `cte-policy-implication`
- "摘要里没有量化结果 / 全是套话" → `cte-abstract`
- "全文'具有重要意义'命中 ≥ 3 处" → `cte-style`
- "明天就要投了" → `cte-submission`
- "收到 2–3 份审稿意见" → `cte-rebuttal`

## 改投边界

若稿件更契合相邻刊物，先建议改投而非继续润色：

- 更一般的理论贡献、非财经专属 → 《经济研究》《管理世界》
- 纯金融资产定价 / 公司金融 → 《金融研究》
- 国际贸易 / 开放宏观 → 《世界经济》《国际贸易问题》
- 更专门的财政 / 税收政策 → 《财政研究》《税务研究》

## 反模式

- **不要**跳过 `cte-literature-review` 直接进识别——审稿人首先看财经理论定位与文献对话
- **不要**让 `cte-tables-figures` 在识别策略未立住时就美化表格
- **不要**让 `cte-rebuttal` 在你修订正文之前生成回复信
- **不要**把脱离中国财经制度背景的"通用"实证硬投本刊——制度契合是第一道关
