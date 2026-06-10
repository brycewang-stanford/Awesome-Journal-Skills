---
name: mw-workflow
description: Use when deciding which mw-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for 《管理世界》 (Management World). Routes — does not replace — the specialized skills.
---

# 管理世界工作流（mw-workflow）

## 总览

这是路由器，它不替代任何专用 Skill。它告诉你**当前阶段应该用哪一个 mw-* skill**。

默认假设：除非用户明确说明目标期刊不是《管理世界》，否则按 CSSCI / 北大核心 一区《管理世界》的编委口味处理。

## 触发时机

- 用户问"我下一步该做什么？"
- 用户甩过来一份初稿，需要判断当前瓶颈
- 实证、写作、回复来回切，状态混乱
- 收到了《管理世界》的外审意见，需要切换到 rebuttal 模式

## 路由表

| 当前症状                                         | 下一个 Skill                       |
|---------------------------------------------|---------------------------------|
| 选题想法模糊，不确定能否冲《管理世界》              | `mw-topic-selection`            |
| 文献综述不知怎么平衡中外引用                       | `mw-literature-review`          |
| 政策背景没说清，海外读者视角不够                    | `mw-institutional-background`   |
| 实证只有 OLS，担心识别策略不过关                   | `mw-identification`             |
| 主结果有了，但缺机制 / 缺异质性切分                 | `mw-mechanism-heterogeneity`    |
| 表格列数过多 / 注释不规范 / 不像《管理世界》风格    | `mw-tables-figures`             |
| 文末没有政策启示，或政策建议太空                    | `mw-policy-implication`         |
| 准备投稿，需要 checklist                          | `mw-submission`                 |
| 收到 R&R，需要写回复信                            | `mw-rebuttal`                   |
| 条件录用后要交数据与代码复现包                       | `mw-replication`                |

## 默认顺序

对大多数实证投稿《管理世界》的稿件，按下列顺序：

1. `mw-topic-selection` — 先把"中国情境 + 边际贡献"句式定下来
2. `mw-literature-review` — 中英文献综述并重
3. `mw-institutional-background` — 政策 / 制度章节
4. `mw-identification` — 准实验识别
5. `mw-mechanism-heterogeneity` — 机制 + 异质性
6. `mw-tables-figures` — 主表 / 主图最终化
7. `mw-policy-implication` — 政策启示分层
8. `mw-submission` — 投稿前 preflight
9. `mw-rebuttal` — 外审后
10. `mw-replication` — 条件录用后，向编辑部提交数据与代码包

## 决策口诀

- 想发但讲不清"中国故事在哪" → `mw-topic-selection`
- 综述里全是英文文献 → `mw-literature-review`
- 政策时间线只用一句话带过 → `mw-institutional-background`
- DID 用了 TWFE 但没回应异质性处理 → `mw-identification`
- 机制只有"我们认为可能是因为..." → `mw-mechanism-heterogeneity`
- 主表 8 列以上 → `mw-tables-figures`
- 政策建议只有"建议政府重视" → `mw-policy-implication`
- 明天就要投了 → `mw-submission`
- 收到 3 份审稿意见 → `mw-rebuttal`
- 收到录用通知，编辑部要数据和代码 → `mw-replication`

## 本刊路由决策表

《管理世界》由国务院发展研究中心主办，是管理学与经济学并重、服务国家重大战略的 CSSCI 权威顶级综合期刊。路由时除判断"当前瓶颈"外，还要在每一阶段反问"是否仍服务国家战略导向、是否守住中国情境与政策落点"。下表锚定本刊语境下的阶段诊断信号：

| 阶段症状（本刊语境） | 路由结论 | 本刊特有把关点 |
|---|---|---|
| 选题讲不清"服务哪项国家战略" | `mw-topic-selection` | 战略相关性 + 边际贡献四句 |
| 综述本土顶刊文献缺位 | `mw-literature-review` | 中文文献占比与对话性 |
| 政策时间线一句话带过 | `mw-institutional-background` | 制度背景独立成节 |
| staggered DID 未诊断偏误 | `mw-identification` | 异质性处理偏误 |
| 只说"有效"未说"为何/对谁有效" | `mw-mechanism-heterogeneity` | 机制 + 分层异质性 |
| 政策建议只剩"建议政府重视" | `mw-policy-implication` | 分层 + 战略对接 |

### 常见退稿模式（流程层面）

- 识别策略未立住就忙于美化表格，本末倒置
- 跳过制度背景直接讲实证——这是本刊与海外期刊最大的差异之一
- 修订正文之前先写回复信，导致承诺与正文脱节
- 全流程不回扣国家战略与政策落点，最终政策含义空泛

## 微型走查示例：一份数字化转型初稿的路由

虚构用户甩来一份初稿，按路由逻辑走查：

- **现状**：有 OLS 主结果 + 控制变量，制度背景仅一段，无机制，政策建议一句话。
- **第一诊断**：识别策略最薄弱（OLS）→ 优先 `mw-identification`，把"企业上云"试点改造成 staggered DID。
- **第二诊断**：制度背景不独立 → `mw-institutional-background` 补政策文号与时间线表。
- **第三诊断**：缺机制 → `mw-mechanism-heterogeneity` 补"数字化→TFP"中介与三维异质性。
- **第四诊断**：政策建议空 → `mw-policy-implication` 重写分层建议、对接"数字中国"战略。
- **收尾**：`mw-tables-figures` 最终化主表 → `mw-submission` 双盲与查重 preflight。

```
【当前阶段】识别策略薄弱（仅 OLS）
【建议路由】mw-identification → mw-institutional-background → mw-mechanism-heterogeneity
【本刊把关】国家战略相关性 ✓ / 中国情境 ✓ / 政策落点 待补
【下一步】先立识别，再回扣政策含义
```

## 审稿人追问模式 + 本刊语境修法

- 追问"你的流程为何先识别后表图？" → 本刊语境：表图是结论的呈现层，识别不立住则表图无意义，故路由强制识别优先。
- 追问"为何如此强调制度背景独立成节？" → 修法：制度背景是本刊识别策略的地基与"研究是否扎实"的第一信号，路由器默认在实证前插入该步。
- 追问"流程末尾如何保证政策含义不空？" → 修法：每轮路由结束回扣"是否服务国家战略 + 是否可导出部门可执行建议"，未达标则回流 `mw-policy-implication`。

## 校准锚点

本刊已刊实证论文的成稿路径普遍遵循"选题（战略+贡献）→ 综述（中外并重）→ 制度背景（独立成节）→ 识别（准实验+偏误诊断）→ 机制与异质性 → 表图 → 政策启示（分层+战略对接）→ 投稿"。各 skill 的具体阈值与本刊年度要求以编辑部最新稿约为准。

## 反模式

- **不要**直接跳到 `mw-tables-figures` 美化表格，如果识别策略还没立住
- **不要**跳过 `mw-institutional-background` 直接讲实证 —— 这是《管理世界》和 AER 最大的差异
- **不要**让 `mw-rebuttal` 在你修订正文之前生成回复信
