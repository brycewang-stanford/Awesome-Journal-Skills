# European Economic Review Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="European Economic Review Skills 封面"></p>

[English](README.md) | 简体中文

面向 **European Economic Review（EER）** 投稿的 12 个 agent skills。EER 是 Elsevier 旗下覆盖经济学所有领域的综合性期刊，既接收实证论文，也接收理论与模型论文。本包把稿件从综合性定位、文献贡献、识别或理论模型，经稳健性、图表、写作风格、复现包、审稿人策略，推进到 Editorial Manager 投稿终检与 R&R 回复。

**官方依据核验日期：2026-06**（费用、编辑、入口与政策细节均以官网为准）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 快速开始

```
/plugin marketplace add ./European-Economic-Review-Skills
/plugin install eer-skills
```

手动使用：先打开 [`skills/eer-workflow/SKILL.md`](skills/eer-workflow/SKILL.md)，再按路由表进入对应阶段。

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`eer-workflow`](skills/eer-workflow/SKILL.md) | 路由到当前最需要的 EER skill |
| 2 | [`eer-topic-selection`](skills/eer-topic-selection/SKILL.md) | 判断是否有综合性经济学读者价值 |
| 3 | [`eer-literature-positioning`](skills/eer-literature-positioning/SKILL.md) | 为综合性读者锚定边际贡献 |
| 4 | [`eer-identification`](skills/eer-identification/SKILL.md) | 压力测试实证识别与推断 |
| 5 | [`eer-theory-model`](skills/eer-theory-model/SKILL.md) | 打磨理论、机制或结构模型 |
| 6 | [`eer-robustness`](skills/eer-robustness/SKILL.md) | 组织规格、样本与推断稳健性 |
| 7 | [`eer-tables-figures`](skills/eer-tables-figures/SKILL.md) | 让图表清晰、标准误优先 |
| 8 | [`eer-writing-style`](skills/eer-writing-style/SKILL.md) | 打磨摘要、highlights 与引言 |
| 9 | [`eer-replication-package`](skills/eer-replication-package/SKILL.md) | 准备数据、代码与计算说明 |
| 10 | [`eer-referee-strategy`](skills/eer-referee-strategy/SKILL.md) | 预判范围、新意与可信度质疑 |
| 11 | [`eer-submission`](skills/eer-submission/SKILL.md) | 运行 Editorial Manager 投稿终检 |
| 12 | [`eer-rebuttal`](skills/eer-rebuttal/SKILL.md) | 起草回复信与修改计划 |

## 资源

- [`resources/official-source-map.md`](resources/official-source-map.md) — EER 事实依据表
- [`resources/code/`](resources/code/) — 实证 Stata/Python 代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
