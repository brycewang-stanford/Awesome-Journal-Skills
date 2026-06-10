---
name: jfr-workflow
description: Use when deciding which jfr-* sub-skill to invoke next, or when sequencing manuscript work from fit positioning through rebuttal for 《金融研究》 (Journal of Financial Research). Routes — does not replace — the specialized skills, and cross-refs sibling journal packs.
---

# 《金融研究》工作流（jfr-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 jfr-* skill**。

默认假设：目标是国内金融学第一刊《金融研究》（中国金融学会主办，中国人民银行金融研究所编辑出版，月刊）。衡量标准是**严谨识别 + 对中国金融体系/政策的现实意义**。该刊有两大支流：**宏观金融**（货币政策、银行、金融稳定、监管）与**微观公司金融**（公司金融、资本市场、治理）。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能冲《金融研究》/ 下一步做什么"
- 题目摇摆在宏观金融与微观公司金融之间，叙事不一致
- 有实证发现但讲不清金融渠道
- 收到 R&R 外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定对不对口、是宏观还是微观线 | `jfr-fit-positioning` |
| 选题模糊、金融贡献立不住 | `jfr-topic-selection` |
| 文献只堆近年实证、缺金融经典与机制文献 | `jfr-literature-review` |
| 制度背景写不准（监管口径/市场分层/所有制） | `jfr-institutional-background` |
| 实证只有 OLS、缺政策冲击或识别策略 | `jfr-identification` |
| 主结果有了但停在"促进/抑制"、无金融渠道 | `jfr-mechanism` |
| 没切异质性 / 切分维度太粗 | `jfr-heterogeneity` |
| 主表列数过多 / 注释与编号不合体例 | `jfr-tables-figures` |
| 政策含义空泛、没落到具体金融主体 | `jfr-policy-implication` |
| 准备投稿，需要体例与系统 checklist | `jfr-submission` |
| 收到 R&R，需要写回复 | `jfr-rebuttal` |

## 默认顺序

1. `jfr-fit-positioning` — 先定线别与匹配度，别把产业/会计题硬投金融刊
2. `jfr-topic-selection` — 把金融问题与贡献立住
3. `jfr-literature-review` — 进入金融脉络，中英文并重
4. `jfr-institutional-background` — 把中国金融制度细节讲准
5. `jfr-identification` — 政策冲击/高频识别/DID/IV
6. `jfr-mechanism` — 落到金融渠道
7. `jfr-heterogeneity` — 按所有制/银行类型/市场分层切分
8. `jfr-tables-figures` — 主表/主图终化
9. `jfr-policy-implication` — 面向货币当局/监管/机构
10. `jfr-submission` — 投稿前 preflight（注释、摘要/JEL、系统）
11. `jfr-rebuttal` — R&R 后

## 决策口诀

- "货币/银行/监管/系统性风险" → 宏观金融线（先 `jfr-fit-positioning`）
- "上市公司融资/投资/治理" → 微观公司金融线
- "DID 用了 TWFE 但没回应异质性处理批评" → `jfr-identification`
- "只能说'缓解了融资约束'" → `jfr-mechanism`
- "读起来像产业政策实证" → 见下方改投

## 与本仓库其它期刊包的差异

- 偏干净因果 + 理论：转 [economic-research](https://github.com/brycewang-stanford/awesome-journal-skills)
- 偏前沿计量 + 理论实证：转 [china-economic-quarterly](https://github.com/brycewang-stanford/awesome-journal-skills)
- 落点在产业升级而非金融机理：转 [china-industrial-economics](https://github.com/brycewang-stanford/awesome-journal-skills)
- 落点在公司治理的管理学理论 / 案例：转 [nankai-business-review](https://github.com/brycewang-stanford/awesome-journal-skills)
- 落点在会计信息、审计、盈余质量：转 [accounting-research](https://github.com/brycewang-stanford/awesome-journal-skills)
- 《金融研究》要的是**金融机理 + 可信识别 + 制度准确**，三者缺一不可

## 阶段健康度自检（投稿前回看路由是否走全）

按下列状态机自检：每个阶段未达绿灯前，不要前推到下游 skill。本刊最常见的"半成品退稿"是**线别没定就抠识别**、或**识别没立住就堆异质性**，导致全文返工。

| 阶段 | 红灯（回炉） | 绿灯（可前推） |
|------|--------------|----------------|
| 定位 | 宏观/微观两线混叙 | 单一主线 + 金融机理清晰 |
| 选题 | "X 影响 Y"无机理 | 渠道 × 制度抓手 × 增量齐 |
| 识别 | 仅 OLS 谈因果 | 冲击 + 平行趋势 + 安慰剂 |
| 机制 | 停在"促进/抑制" | 渠道命名 + 竞争渠道排除 |
| 异质性 | 只切东中西 | 机制预测 + 组间差异检验 |
| 政策 | "加强完善"四件套 | 对象 + 工具 + 边界 |

## 微型走查：一篇"利率市场化改革对银行风险承担"的稿子如何过路由

示意，数字均为虚构演示：

1. **定位**：因变量是银行风险承担，属宏观金融线"银行与信贷" → `jfr-fit-positioning` 判"高匹配、宏观线"。
2. **选题**：渠道=风险承担；制度抓手=LPR 改革（2019）；增量="中小银行风险承担更敏感"这一被忽略主体异质。
3. **识别**：以 LPR 并轨为冲击做 DID，事件研究图显示改革前系数不显著（绿灯）。
4. **机制**：高风险贷款占比上升约 2.3 个百分点、贷款利率上行（排除需求侧竞争渠道）。
5. **异质性**：城商/农商系数约为国有大行 1.8 倍，组间差异 5% 显著，与机制一致。
6. **政策**：对宏观审慎部门——建议中小银行差异化逆周期资本缓冲（对象/工具/边界齐）。

```text
ROUTE TRACE  (示意稿：LPR 改革 → 银行风险承担)
  fit-positioning    → 宏观金融线 · 高匹配         [绿]
  topic-selection    → 风险承担 × LPR并轨 × 主体异质 [绿]
  identification     → DID · 前趋势平 · 安慰剂待补   [黄→绿]
  mechanism          → 风险承担渠道 · 已排需求侧     [绿]
  heterogeneity      → 银行类型 · 组间差异5%显著     [绿]
  policy-implication → 宏观审慎 · 差异化逆周期缓冲   [绿]
  NEXT: jfr-tables-figures → jfr-submission
```

## 反模式

- **不要**跳过 `jfr-fit-positioning` 就动笔——线别错了全文都歪
- **不要**在识别策略未立住时去美化表格或抠摘要
- **不要**让 `jfr-rebuttal` 在正文未修订前生成回复
- **不要**在某阶段亮红灯时强行前推——下游产出会随上游返工作废
