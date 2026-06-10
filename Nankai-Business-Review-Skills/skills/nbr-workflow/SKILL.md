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

## 阶段闸门与产出物

| 阶段 | 闸门产出物 | 未达标则 |
|------|-----------|----------|
| 对口判断 | 匹配度判定（高/中/低）+ 改投建议 | 停止，先定去向 |
| 理论缺口 | "理论 T 欠什么"一句话 + 贡献形态 | 不进入假设写作 |
| 假设推演 | 每条 H 的机理链 | 不进入数据分析 |
| 测量 | α/CR/AVE 列表 + CMV 双重证据 | 不跑结构模型 |
| 方法主线 | SEM 结果 / 实验质控 / 编码证据链（三选一） | 不写讨论 |
| 情境化 | 情境进入模型的证明（调节或构念重构） | 讨论缺情境贡献 |
| 投稿 | preflight 全勾 + 摘要四要素 | 不点提交 |

## 路由走查示例

用户说："我有 800 份员工问卷，发现算法监控与离职意愿正相关，想投南开管理评论。"
路由：构念关系 + 问卷 → 对口（可跳过改投）→ 但"正相关"无缺口表述 → 先 `nbr-theory-gap`；量表自译且单时点 → 排队 `nbr-measurement`；员工嵌套于 40 家企业 → 提示 `nbr-survey-sem` 查 ICC。一次对话给出三站路线，而非只回答下一步。

## 状态报告格式

```
【稿件】<一句话：构念关系 + 方法>
【已过闸】对口□ 缺口□ 机理□ 测量□ 分析□ 情境□
【当前站】nbr-<skill>（理由：<症状>）
【后续队列】nbr-<…> → nbr-<…>
【风险】<最可能被本刊审稿人打回的一处>
```

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

## 二手数据稿件的路由说明

CSMAR/Wind 类企业实证（治理、创新、战略）同样可走本流程：缺口与贡献照走 `nbr-theory-gap` / `nbr-discussion-contribution`；"测量"站替换为变量构造与内生性处理（工具变量、PSM、DID 已成此类稿件的审稿标配），具体口径见 `nbr-fit-positioning` 的二手数据细则；情境化与投稿站不变。

## 反模式

- **不要**跳过 `nbr-fit-positioning` 就动笔——它最常救稿（避免投错门）
- **不要**在理论缺口未立时就抠 SEM 拟合指标或摘要
- **不要**让 `nbr-rebuttal` 在正文未修订前生成回复
