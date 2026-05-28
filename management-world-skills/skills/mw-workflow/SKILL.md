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

## 反模式

- **不要**直接跳到 `mw-tables-figures` 美化表格，如果识别策略还没立住
- **不要**跳过 `mw-institutional-background` 直接讲实证 —— 这是《管理世界》和 AER 最大的差异
- **不要**让 `mw-rebuttal` 在你修订正文之前生成回复信
