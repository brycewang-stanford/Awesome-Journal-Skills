# Review of Economics and Statistics Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Review of Economics and Statistics Skills 封面"></p>

[English](README.md) | 简体中文

面向 **The Review of Economics and Statistics（REStat）** 投稿的 12 个 agent skills。REStat 是 MIT Press 的应用经济学与应用计量经济学期刊。本包以实证为核心，覆盖选题契合度、文献定位、识别、理论/模型约束、稳健性、图表、写作风格、复现包、审稿人策略、投稿终检与回复修改。

**官方依据核验日期：2026-06-20**：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 快速开始

```
/plugin marketplace add ./Review-of-Economics-and-Statistics-Skills
/plugin install restat-skills
```

手动使用：先打开 [`skills/restat-workflow/SKILL.md`](skills/restat-workflow/SKILL.md)。

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`restat-workflow`](skills/restat-workflow/SKILL.md) | 路由 REStat 稿件 |
| 2 | [`restat-topic-selection`](skills/restat-topic-selection/SKILL.md) | 判断应用经济学与测量契合度 |
| 3 | [`restat-literature-positioning`](skills/restat-literature-positioning/SKILL.md) | 定位实证贡献 |
| 4 | [`restat-identification`](skills/restat-identification/SKILL.md) | 压力测试因果设计与推断 |
| 5 | [`restat-theory-model`](skills/restat-theory-model/SKILL.md) | 约束理论或模型部分 |
| 6 | [`restat-robustness`](skills/restat-robustness/SKILL.md) | 组织稳健性检查 |
| 7 | [`restat-tables-figures`](skills/restat-tables-figures/SKILL.md) | 准备可读图表 |
| 8 | [`restat-writing-style`](skills/restat-writing-style/SKILL.md) | 执行 REStat 简洁实证文风 |
| 9 | [`restat-replication-package`](skills/restat-replication-package/SKILL.md) | 准备数据与代码材料 |
| 10 | [`restat-referee-strategy`](skills/restat-referee-strategy/SKILL.md) | 预判审稿人质疑 |
| 11 | [`restat-submission`](skills/restat-submission/SKILL.md) | 运行投稿终检 |
| 12 | [`restat-rebuttal`](skills/restat-rebuttal/SKILL.md) | 起草回复信与修改计划 |

## 资源

- [`resources/official-source-map.md`](resources/official-source-map.md) — REStat 官方来源
- [`resources/external_tools.md`](resources/external_tools.md) — 数据与软件工具
- [`resources/code/`](resources/code/) — 实证 Stata/Python 代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
