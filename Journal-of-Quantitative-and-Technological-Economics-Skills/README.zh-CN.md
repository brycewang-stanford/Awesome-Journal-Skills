# 《数量经济技术经济研究》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《数量经济技术经济研究》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-数量经济技术经济研究-c0392b)](https://www.jqte.net/)
[![Index](https://img.shields.io/badge/index-CSSCI%20%7C%20EconLit-1f6feb)](https://www.jqte.net/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《数量经济技术经济研究》(The Journal of Quantitative & Technological Economics, JQTE)** 投稿的 agent skill 集合——中国社会科学院数量经济与技术经济研究所主办，兼容数量经济学与技术经济学（月刊，1984 年创刊；ISSN 1000-3894；CN 11-1087/F；CSSCI / 北大核心 / EconLit 收录）。

本包**有观点**：不是通用计量工具箱，而是围绕该刊的核心门槛——**测度透明、方法应用价值与可复现性优先于硬凑的因果叙事**——专门构建。这里的贡献通常是"量得准不准、预测得好不好、分解得清不清、能不能复现"，而非"识别干不干净"。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

JQTE 看重的贡献形态与干净因果旗舰（经济研究 / 中国经济学季刊 / 中国工业经济）不同：

| 约束 | 数量经济技术经济研究 | 含义 |
|------|----------------------|------|
| 贡献 | 测度 / 方法应用 / 预测 | "发现 X 导致 Y"不是唯一路径——硬凑弱因果反而扣分 |
| 方法节 | 方法节是重头 | 构造必须透明、可复现 |
| 稳健性 | 对方法/参数选择的敏感性 | "换个 DEA/SFA 设定结论还成立吗"比安慰剂更关键 |
| 预测 | 样本外评估 | 只报样本内拟合 = desk reject 风险 |
| IO / CGE | 数据来源、校准、闭合、情景 | 黑箱软件跑出来不交代设定会被拒 |
| 注释 | 脚式编排、每页重新编号 | 尾注/夹注不合体例 |
| 政策建议 | 不少于 1000 字（纯方法类除外） | 含义要落到规划/预测/产业决策 |

> **不要**给测度类论文硬套因果故事。若识别本身是真贡献且干净，请改投经济研究 / 中国经济学季刊。

---

## 十三个 Skill

| Skill | 作用 |
|-------|------|
| `jqte-workflow` | 路由器——下一步用哪个；跨刊改投 |
| `jqte-fit-positioning` | 测度/预测/方法应用 vs 干净因果——据此组织全文 |
| `jqte-topic-selection` | 选一个有价值的测度/预测/评价问题 |
| `jqte-literature-review` | 方法脉络 + 中国数据应用缺口，而非堆引用 |
| `jqte-measurement` | TFP / Malmquist / DEA / SFA / 指数构建——透明 + 敏感性 |
| `jqte-econometric-methods` | 时间序列/协整/混频/面板/宏观计量 |
| `jqte-forecasting` | 样本外评估（RMSE / 方向准确率） |
| `jqte-io-cge` | 投入产出/CGE/结构分解（SDA）——可复现 |
| `jqte-sensitivity` | 测度/参数敏感性、稳健性 |
| `jqte-tables-figures` | 量化解读，不止显著性星号 |
| `jqte-implications` | 规划/预测/产业/技术决策含义 |
| `jqte-submission` | 投稿前：脚注、政策篇幅、投稿系统 |
| `jqte-rebuttal` | R&R 回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install journal-of-quantitative-and-technological-economics-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/jqte-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/jqte-* ~/.codex/skills/
```

---

> 编辑政策会变。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照 [jqte.net](https://www.jqte.net/) 最新《投稿须知》核实。
