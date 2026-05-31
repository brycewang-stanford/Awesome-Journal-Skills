---
name: nbr-workflow
description: Use when deciding which nbr-* sub-skill to invoke next, or when sequencing manuscript work from fit judgment through rebuttal for 《南开管理评论》 (Nankai Business Review). Routes — does not replace — the specialized skills, and re-routes math-model or macro-policy papers to sibling journal stacks.
---

# 《南开管理评论》工作流（nbr-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 nbr-* skill**。

默认假设：目标是工商管理学科高端平台《南开管理评论》（教育部主管、南开大学商学院主办）。核心评判是**理论贡献 + 中国情境 + 测量规范（问卷-SEM / 实验 / 多案例）**，而非因果识别的"干净"。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能投《南开管理评论》/ 下一步做什么"
- 手头是构念间关系（中介/调节/被调节的中介）但讲不出理论缺口
- 不确定该投本刊、《管理世界》还是《管理科学学报》
- 收到 R&R 外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定对不对口、可能是数理模型/宏观政策 | `nbr-fit-positioning` |
| 有发现但讲不清理论缺口与贡献 | `nbr-theory-gap` |
| 假设凭直觉、缺机理推演 | `nbr-hypothesis-development` |
| 量表没信效度 / 没做共同方法偏差 | `nbr-measurement` |
| 问卷数据，要跑中介/调节/多层 | `nbr-survey-sem` |
| 用实验法，担心操纵/随机化/效应量 | `nbr-experiment` |
| 质性多案例 / 扎根理论，编码与饱和不清 | `nbr-qualitative-case` |
| 中国情境只是采样地、没进理论 | `nbr-china-context` |
| 讨论部分没回扣理论、不知如何推进 | `nbr-discussion-contribution` |
| 准备投稿，需要体例与系统 checklist | `nbr-submission` |
| 收到 R&R，需要写回复 | `nbr-rebuttal` |

## 默认顺序

1. `nbr-fit-positioning` — 先判断对口，别把数理/政策稿硬投本刊
2. `nbr-theory-gap` — 立住理论缺口与贡献形态
3. `nbr-hypothesis-development` — 每条假设配机理
4. `nbr-measurement` — 信效度 + CMV（问卷类前置工程）
5. `nbr-survey-sem` / `nbr-experiment` / `nbr-qualitative-case` — 按方法三选一
6. `nbr-china-context` — 让情境进入理论
7. `nbr-discussion-contribution` — 讨论回扣并推进理论
8. `nbr-submission` — 投稿前 preflight（体例、摘要字数、在线系统）
9. `nbr-rebuttal` — 外审后

## 决策口诀

- "构念关系 + 问卷/实验/案例 + 理论建构" → 本刊对口，进 `nbr-theory-gap`
- "假设全是'应该正相关'" → `nbr-hypothesis-development`
- "量表照搬国外、没算 α/AVE" → `nbr-measurement`
- "中国情境只在样本描述里出现" → `nbr-china-context`
- "讨论只复述结果" → `nbr-discussion-contribution`

## 与本仓库其它期刊包的差异（改投判断）

- 数理模型 + 定理/算法/最优化 → **管理科学学报**（journal-of-management-sciences-china）
- 宏观政策实证 + 政策评估/政策含义 → **管理世界** / 中国工业经济
- 公司治理偏资本市场/财务实证 → **会计研究**（accounting-research）/ **金融研究**（journal-of-financial-research）
- NBR 要的是**管理理论建构 + 测量规范 + 情境化**，方法服务理论

## 反模式

- **不要**跳过 `nbr-fit-positioning` 就动笔——它最常救稿（避免投错门）
- **不要**在理论缺口未立时就抠 SEM 拟合指标或摘要
- **不要**让 `nbr-rebuttal` 在正文未修订前生成回复
