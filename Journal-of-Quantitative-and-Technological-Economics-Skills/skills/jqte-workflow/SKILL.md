---
name: jqte-workflow
description: Use when deciding which jqte-* sub-skill to invoke next, or when sequencing manuscript work from fit positioning through rebuttal for 《数量经济技术经济研究》 (The Journal of Quantitative & Technological Economics, JQTE). Routes — does not replace — the specialized skills, and cross-routes to other journals when the contribution is clean causal, industrial-policy, or pure modeling.
---

# 数量经济技术经济研究工作流（jqte-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 jqte-* skill**。

默认假设：目标是《数量经济技术经济研究》（中国社会科学院数量经济与技术经济研究所主办，月刊，1984 年创刊）。本刊的评判核心是**测度准、方法对、结论稳、可复现**，而非干净因果的"故事性"。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能投 JQTE / 下一步做什么"
- 有测度/预测/分解结果，但不确定怎么组织成稿
- 纠结贡献是"测度/方法"还是"因果"
- 收到 R&R / 外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定贡献类型、对不对口 | `jqte-fit-positioning` |
| 选题太空 / 没有可量化的核心问题 | `jqte-topic-selection` |
| 文献只堆近年实证、没进方法脉络 | `jqte-literature-review` |
| TFP/效率/指数构造说不清、不透明 | `jqte-measurement` |
| 时间序列/面板/宏观计量设定不规范 | `jqte-econometric-methods` |
| 预测只报样本内拟合、没样本外评估 | `jqte-forecasting` |
| IO/CGE/SDA 数据、校准、闭合交代不清 | `jqte-io-cge` |
| 没做方法/参数敏感性，结论不稳 | `jqte-sensitivity` |
| 表格只有星号、缺量化解读 | `jqte-tables-figures` |
| 政策含义空泛 / 不足 1000 字 | `jqte-implications` |
| 准备投稿，需要体例与系统 checklist | `jqte-submission` |
| 收到外审意见，需要写回复 | `jqte-rebuttal` |

## 默认顺序

1. `jqte-fit-positioning` — 先定贡献类型（测度/预测/方法应用/因果），别硬凑因果
2. `jqte-topic-selection` — 把可量化的核心问题立住
3. `jqte-literature-review` — 进方法脉络 + 中国数据应用缺口
4. `jqte-measurement` 或 `jqte-econometric-methods` 或 `jqte-io-cge` — 按方法主线选其一为重头
5. `jqte-forecasting` — 若涉预测，做样本外评估
6. `jqte-sensitivity` — 方法/参数敏感性、稳健性
7. `jqte-tables-figures` — 量化解读
8. `jqte-implications` — 规划/预测/产业/技术决策含义
9. `jqte-submission` — 投稿前 preflight（脚注、政策篇幅、系统）
10. `jqte-rebuttal` — 外审后

## 决策口诀

- "贡献在测度/预测/分解" → 本刊对口，重头在方法节
- "我只能硬说这是因果" → 先 `jqte-fit-positioning`，多半别硬凑
- "预测只有 R²" → `jqte-forecasting`
- "DEA/CGE 跑完没交代设定" → `jqte-measurement` / `jqte-io-cge`

## 与其它期刊包的差异（跨刊改投）

- 干净因果 + 理论：转 economic-research / china-economic-quarterly
- 产业政策实证 + 厚稳健性：转 china-industrial-economics
- 数理模型/算法本身是贡献：转 journal-of-management-sciences-china
- 本刊要的是**测度/方法/预测的应用价值 + 可复现**，因果识别可选、不强求

## 反模式

- **不要**跳过 `jqte-fit-positioning` 就动笔——它最常救稿（避免硬凑因果）
- **不要**在方法节没立住时去抠表格和文风
- **不要**让 `jqte-rebuttal` 在正文未修订前生成回复
