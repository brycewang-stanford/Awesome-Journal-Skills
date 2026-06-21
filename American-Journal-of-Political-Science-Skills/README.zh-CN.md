# 美国政治科学杂志（AJPS）技能包

<p align="center">
  <img src="assets/cover.svg" alt="American Journal of Political Science 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AJPS-3d5229)](https://ajps.org/)
[![Field](https://img.shields.io/badge/field-政治学-1f6feb)](https://www.mpsanet.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《美国政治科学杂志》（American Journal of Political Science, AJPS）** 投稿的 Agent 技能栈。
AJPS 是 **中西部政治学会（MPSA）的旗舰期刊**，由 **Wiley** 出版。它是一份综合性但 **偏定量** 的
政治学期刊：版面以严谨的实证、实验、计算或形式—实证研究为主，覆盖美国政治、比较政治、国际关系、
政治行为、制度与方法论。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把 APSR 包改个名字。它是
**AJPS 专属** 技能栈，围绕该刊的招牌特征构建：**发表前对复现材料的强制第三方验证**——独立验证者会
重跑你提交的代码，确认其能复现**正文中的数值结果**之后，文章才进入发表流程，材料存入 **Harvard
Dataverse 上的 AJPS Dataverse**。

---

## AJPS 是什么，为何需要专属技能栈？

AJPS 的约束不同于全学科综述刊或方法刊：

| 约束 | AJPS | 含义 |
|------|------|------|
| 所有者 / 出版方 | **MPSA** / **Wiley** | 通过 **Editorial Manager**（`editorialmanager.com/ajps`）投稿 |
| 方法重心 | **偏定量** 的综合刊 | 实证识别与推断撑起论文 |
| 评审模式 | **双盲** | 完全匿名——不出现致谢、资助、会议信息 |
| 篇幅 | **Article ≤ 10,000 词**；**Research Note / Correspondence ≤ 4,000** | 字数写在**标题页** |
| 字数计入 | 脚注、夹注、**表/图标题与注释**、纸质附录 | 不含参考文献、摘要、在线 SI、数学符号 |
| 摘要 | **≤ 150 词** | 背景、假设、方法、发现、结论 |
| 体例 | **APSA 体例手册**（2018/2023 修订）**或** **Chicago 第 18 版** | 二选一；参考文献用全名 |
| 支撑信息(SI) | 原始投稿 **≤ 25 页**，以 "Appendix" 上传 | 把稳健性大表移出正文 |
| **验证** | **发表前第三方** 重跑代码核对正文数值 | 从第一天就工程化可复现——它是发表关口 |

**官方依据核对于 2026-06-20**：AJPS 稿件指南、准备指南、投稿页、录用稿指南、验证政策、AI 政策、
编辑名单、MPSA 与 Dataverse 页面。上传字段、Wiley 许可/开放获取选择和后续政策更新需在
[`resources/official-source-map.md`](resources/official-source-map.md) 所列官方页 live-check。

### 招牌差异点：第三方验证

许多期刊要求复现包；AJPS 则在**发表前独立重跑**它。接受后，你把数据与代码存入 **AJPS Dataverse**，
验证者确认代码能复现**正文中的数值结果**。发表的文章随后会附一句类似
*"The Cornell Center for Social Sciences verified that the data and replication code submitted to the
AJPS Dataverse replicates the numerical results reported in the main text of this article."* 的声明。
定性与混合方法工作应按 AJPS 定性检查表、访问控制与豁免路径处理，而不是套用通用开放数据模板。

### 三种投稿类型

- **Article**——完整原创研究，**≤ 10,000 词**。
- **Research Note**——**仅限方法学论文（含规范理论中的方法）与元分析**，**≤ 4,000 词**。不是短实证文。
- **Correspondence**——对**已在 AJPS 发表**工作的批评性回应，**≤ 4,000 词**。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/ajps-skills
/plugin install ajps-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/ajps-skills.git
cd ajps-skills

mkdir -p ~/.claude/skills && cp -R skills/ajps-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/ajps-* ~/.codex/skills/
```

### 第一条提示

```
用 ajps-workflow 告诉我，我的 AJPS 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
ajps-topic-selection
        ▼
ajps-literature-positioning
        ▼
ajps-theory-building
        ▼
ajps-research-design
        ▼
ajps-data-analysis
        ▼
ajps-tables-figures
        ▼
ajps-writing-style          （润色）
        ▼
ajps-replication-and-verification
        ▼
ajps-review-process
        ▼
ajps-submission
        ▼
ajps-rebuttal
```

`ajps-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。**在分析阶段就启动**
`ajps-replication-and-verification`，而不是等到接受：第三方验证者会重跑你的代码，临时拼凑、
没有脚本化的分析在 deadline 下无法补救。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `ajps-workflow` | 路由器——决定下一步调用哪个子技能 |
| `ajps-topic-selection` | 选题契合（清晰、可推广）；区分 Article / Research Note / Correspondence |
| `ajps-literature-positioning` | 在保持双盲的同时锚定贡献 |
| `ajps-theory-building` | 把想法转化为可检验假设与机制 |
| `ajps-research-design` | 为识别辩护——因果推断、实验、形式—实证、案例 |
| `ajps-data-analysis` | 分析规范、不确定性、稳健性、从第一行就可复现 |
| `ajps-tables-figures` | 自洽、可复现的图表；标题计入字数 |
| `ajps-writing-style` | 字数上限、APSA/Chicago 体例、完全匿名 |
| `ajps-replication-and-verification` | 提交 AJPS Dataverse 的第三方验证包（招牌技能） |
| `ajps-review-process` | 双盲评审、决定类别、接受后的验证流程 |
| `ajps-submission` | Editorial Manager 投稿前检查（匿名、字数、SI ≤ 25 页、IRB） |
| `ajps-rebuttal` | 面向多位评审 + 编辑、保持匿名且可重跑的 R&R 回应 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 政治学数据源（ANES / CES / V-Dem / CSES / COW / ACLED / MARPOR）+ R / Stata / Python 工具与复现包规范
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实和 live-check 项背后的 AJPS / MPSA / Wiley / Dataverse 官方 URL

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不冻结易变元数据（上传字段、Wiley 许可/APC 选项、后续政策更新）——投稿前请 live-check 官方页面
- 不替你跑或通过验证——那是第三方验证者的工作；本包只帮你准备好材料包

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [American Journal of Political Science（编辑部站点）](https://ajps.org/) — 投稿指南、复现与验证政策
- [中西部政治学会（MPSA）](https://www.mpsanet.org/) — 所有者

---

## 许可

MIT
