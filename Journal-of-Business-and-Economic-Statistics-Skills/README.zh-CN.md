# 《Journal of Business & Economic Statistics》(JBES) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Business & Economic Statistics 期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JBES-16487a)](https://www.tandfonline.com/journals/ubes20)
[![Society](https://img.shields.io/badge/society-ASA-1f6feb)](https://www.amstat.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Journal of Business & Economic Statistics（JBES，《商业与经济统计杂志》）** 投稿的 Agent Skill 工具栈。JBES 创刊于 1983 年，是一本计量经济学与统计学**方法论**期刊，由 **Taylor & Francis 代表美国统计学会（ASA）** 出版。

本仓库刻意**不通用**——它不是泛化的"计量写作助手"，而是围绕 JBES 的核心要求构建的方法论沉淀，即 **方法 + 实证（methods with empirics）**：一项新的或改进的统计/计量方法（明确欢迎对机器学习与数据科学方法的改造，以及计算上的改进），并且具有**清晰的实证相关性**，通常还配有一个**有分量的实证应用**。**只有理论而无实证动机**，或**只有应用而无方法创新**，都属于不符合范围（off-scope）。

> **投稿前必须核验 live T&F instructions。** 来源地图已于 2026-06-20 刷新。本包只固化稳定的官方事实（范围、ASA 归属、现任 Joint Editors、ASA 可复现政策），不把需要 live 作者须知页面确认的投稿系统、费用、篇幅/摘要上限、评审模式或格式规则写成硬事实。

---

## 为什么要为 JBES 单独做一套 Skills？

JBES 的约束维度与综合性经济学期刊或纯统计学期刊**显著不同**：

| 维度 | JBES | 隐含含义 |
|---|---|---|
| 核心要求 | 方法 **与** 应用，二者兼备 | 单腿论文（纯理论 / 纯应用）不符合范围 |
| 方法范围 | 新/改进方法，含 **机器学习 / 数据科学** 与计算改进 | 直接套用现成 ML、无计量创新者不合适 |
| 证据 | **渐近理论 + 蒙特卡洛 + 有分量的应用** | 推导加玩具式示例会被读作"未完成" |
| 所属学会 | **美国统计学会（ASA）** | 遵循 ASA 数据共享/伦理政策，而非 AEA Data Editor 体系 |
| 编辑 | **多位 Co-Editor / Joint Editor** 轮值（无单一主编） | 投稿信定位方式与单一主编期刊不同 |
| 数据/代码 | ASA **补充材料** + 数据可得性声明 | 不是 JAE Data Archive（那是另一本 Wiley 期刊） |
| 获取模式 | Taylor & Francis **Open Select**（混合 OA） | 仅在选择 OA 时才有可选 APC |
| 传统 | 受邀**讨论论文（discussion paper）** + 评论/回应 | 部分贡献可作为讨论论文形式呈现 |

通用的"科研写作"或"经济学写作"Skill 包不会处理这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jbes-skills
/plugin install jbes-skills
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/jbes-skills.git
cd jbes-skills

mkdir -p ~/.claude/skills && cp -R skills/jbes-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jbes-* ~/.codex/skills/
```

### 第一条 Prompt

```
用 jbes-workflow 告诉我这份 JBES 目标稿子下一步该用哪个 skill。
```

---

## 默认工作流

```text
jbes-topic-selection
        ▼
jbes-literature-positioning
        ▼
jbes-contribution-framing
        ▼
jbes-identification-strategy
        ▼
jbes-data-analysis
        ▼
jbes-tables-figures
        ▼
jbes-writing-style        （polish）
        ▼
jbes-replication-and-data-policy
        ▼
jbes-review-process
        ▼
jbes-submission
        ▼
jbes-rebuttal
```

`jbes-workflow` 是路由器，会根据当前阶段告诉你下一个该用哪个 Skill。

---

## Skill 一览

| Skill | 用途 |
|---|---|
| `jbes-workflow` | 路由器：判断当前阶段，推荐下一个 skill |
| `jbes-topic-selection` | "方法 + 实证"契合度检验（创新性 × 相关性） |
| `jbes-literature-positioning` | 对照既有计量/统计方法确立贡献增量 |
| `jbes-contribution-framing` | 一句话贡献：方法增量 + 实证后果 |
| `jbes-identification-strategy` | 假设、正则条件、渐近理论、蒙特卡洛设计 |
| `jbes-data-analysis` | 蒙特卡洛证据 + 有分量的实证应用 |
| `jbes-tables-figures` | 让 size / power / coverage 对两类读者都清晰 |
| `jbes-writing-style` | 方法优先、以应用为锚的行文与定理陈述 |
| `jbes-replication-and-data-policy` | 遵循 ASA 政策的可复现代码+数据补充材料 |
| `jbes-review-process` | 多 Co-Editor 评审路径与讨论论文传统 |
| `jbes-submission` | 面向 live T&F 投稿事实与 ASA supplement 准备度的投稿前 preflight |
| `jbes-rebuttal` | 方法类论文的 R&R 回复信策略 |

### 附属资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 仿真引擎、各方法族库（Stata / R / Python）、应用数据（FRED / CRSP / IPUMS）与可复现工具
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 2026-06-20 刷新的官方来源地图；投稿专属事实在打开 live T&F 页面前不编码

---

## 与相邻 Skill 包的差异

| 维度 | JBES | 综合性经济学期刊 | 纯统计学期刊 |
|---|---|---|---|
| 主线 | 方法 **加** 应用 | 一个实证/理论发现 | 一个定理 |
| 实证应用 | 必需（属于范围） | 论文本身 | 常常可选 |
| 方法创新 | 必需 | 常常缺失 | 必需 |
| 数据/伦理体系 | ASA 政策 | AEA Data Editor（经济学） | 各刊自定 |

---

## 关于这个仓库不做什么

- 不替你写出可以直接投稿的稿件
- 不模拟任何特定 Co-Editor 或审稿人的偏好
- 不在未打开 live T&F 作者须知时断言投稿系统、确切费用、篇幅上限、评审模式或格式规则
- 不评判你的方法是否真有原创性——这是研究者本人的判断

---

## 相关仓库

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊 Skill 索引
- [Journal of Business & Economic Statistics（官网）](https://www.tandfonline.com/journals/ubes20) —— Taylor & Francis，代表 ASA
- [ASA 数据共享与可复现政策](https://www.amstat.org/publications/q-and-as/asa-journal-policies-on-data-sharing-and-reproducibility)

---

## License

MIT
