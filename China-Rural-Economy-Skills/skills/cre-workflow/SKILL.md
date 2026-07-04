---
name: cre-workflow
description: Use when deciding which cre-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for 《中国农村经济》 (China Rural Economy). Routes — does not replace — the specialized skills.
---

# 中国农村经济工作流（cre-workflow）

## 总览

这是路由器，它不替代任何专用 Skill。它告诉你**当前阶段应该用哪一个 cre-* skill**。

默认假设：除非用户明确说明目标期刊不是《中国农村经济》，否则按 CSSCI 一区、中国社会科学院农村发展研究所主办的《中国农村经济》编委口味处理。该刊聚焦"三农"（农业、农村、农民），以微观农户 / 村级数据的因果识别实证为主，姊妹刊为《中国农村观察》。

## 触发时机

- 用户问"我下一步该做什么？"
- 用户甩过来一份三农主题初稿，需要判断当前瓶颈
- 实证、写作、回复来回切，状态混乱
- 收到了《中国农村经济》的外审意见，需要切换到 rebuttal 模式

## 路由表

| 当前症状                                          | 下一个 Skill                  |
|----------------------------------------------|---------------------------|
| 选题想法模糊，不确定是否契合"三农"场景 / 边际贡献写不出     | `cre-topic-selection`     |
| 文献综述缺三农领域中文经典 / 缺理论文献                 | `cre-literature-review`   |
| 实证只有 OLS / 描述统计，担心识别策略不过关             | `cre-identification`      |
| 主结果有了，但没有农户微观机制                         | `cre-mechanism`           |
| 没切异质性 / 切分维度脱离农村场景                       | `cre-heterogeneity`       |
| 表格列数过多 / 注释不规范 / 不像《中国农村经济》风格      | `cre-tables-figures`      |
| 文末政策含义脱离乡村振兴 / 是"加强完善推进"四件套        | `cre-policy-implication`  |
| 摘要写成套话，没量化结果 / 中英文不对齐                 | `cre-abstract`            |
| 通篇空话套话 / 政策建议是"加强完善推进"四件套           | `cre-style`               |
| 准备投稿，需要 checklist                            | `cre-submission`          |
| 收到 R&R，需要写回复信                              | `cre-rebuttal`            |

## 默认顺序

1. `cre-topic-selection` — 先把"三农场景 + 理论贡献 + 中国农村政策现实"定下来
2. `cre-literature-review` — 中外并重，三农经典与权威文献必引
3. `cre-identification` — 农户 / 村级数据的准实验识别
4. `cre-mechanism` — 农户微观机制路径
5. `cre-heterogeneity` — 异质性切分（落到农村场景）
6. `cre-tables-figures` — 主表 / 主图最终化（三线表）
7. `cre-policy-implication` — 乡村振兴 / 农村政策含义（意义层但落到三农场景）
8. `cre-abstract` — 摘要五句法 + 黑名单短语清除
9. `cre-style` — 全文语言风格 polish
10. `cre-submission` — 投稿前 preflight
11. `cre-rebuttal` — 外审后

> `cre-abstract` 与 `cre-style` 是**后段 polish 阶段**触发，不要在识别策略未立住时去做。

## 阶段快照模板

把下面的快照复制到工作笔记，每完成一阶段更新对应行；**第一处空白即当前瓶颈**，对应右侧的 cre-* 入口：

```text
《中国农村经济》稿件阶段快照
选题定位：三农场景=____（农户/村级/县域）  边际贡献一句话=____
文献对话：三农中文经典已引 __ 篇；理论/英文对话文献已引 __ 篇
识别策略：数据=____  方法=____  内生性处理=已/未
机制检验：农户微观路径共 __ 条，已实证检验 __ 条
异质性　：切分维度=____（须落回农村场景，忌只切东中西）
表格规范：主表为三线表？是/否   注释含标准误聚类层级？是/否
政策含义：对应的农村政策抓手=____（禁"加强完善推进"四件套）
摘要风格：量化结果已写入摘要？是/否  "具有重要意义"命中 __ 处（目标 0）
投稿状态：submission checklist 已过 / 外审意见 __ 份待回复
```

- "我有 CFPS / CHFS 数据但没三农理论故事" → `cre-topic-selection`
- "综述里没引农户行为 / 土地制度 / 农业政策的经典文献" → `cre-literature-review`
- "我只跑了村级面板的描述统计 + OLS" → `cre-identification`
- "外出务工 / 入社是自选择，但我没处理内生性" → `cre-identification`
- "我只能说'我们认为可能是因为农户……'" → `cre-mechanism`
- "异质性只切了东中西" → `cre-heterogeneity`
- "主表 8 列以上" → `cre-tables-figures`
- "我建议政府重视乡村振兴" → `cre-policy-implication`
- "摘要里没有量化结果 / 全是套话" → `cre-abstract`
- "全文'具有重要意义'命中 ≥ 3 处" → `cre-style`
- "明天就要投了" → `cre-submission`
- "收到 2–3 份审稿意见" → `cre-rebuttal`

## 与姊妹刊《中国农村观察》的差异

两刊均由中国社会科学院农村发展研究所主办，但侧重不同：

- 《中国农村经济》：偏经济学实证、因果识别与机制，主流方法门槛高
- 《中国农村观察》：对质性研究、案例、调查报告与政策评论更包容

如果稿子偏案例 / 质性 / 政策观察，《中国农村观察》可能更契合（具体以两刊当年定位为准，建议到官网"投稿须知"核对）。

## 反模式

- **不要**跳过 `cre-literature-review` 直接进识别——审稿人首先看三农领域的理论定位与文献对话
- **不要**让 `cre-tables-figures` 在识别策略未立住时就美化表格
- **不要**让 `cre-rebuttal` 在你修订正文之前生成回复信
- **不要**把脱离三农场景的"通用"实证硬投本刊——学科契合是第一道关
