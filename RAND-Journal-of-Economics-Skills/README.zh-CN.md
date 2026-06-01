# RAND Journal of Economics（RJE）Skills

<p align="center">
  <img src="assets/cover.svg" alt="RAND Journal of Economics 期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-RJE-13315c)](https://www.rje.org/)
[![Field](https://img.shields.io/badge/field-Industrial%20Organization-1f6feb)](https://www.rje.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **The RAND Journal of Economics（RJE，《兰德经济学杂志》）** 投稿的 Agent Skill 工具栈。RJE 是**产业组织（IO）领域的旗舰期刊**，由 **兰德公司（RAND Corporation，位于圣莫尼卡）** 拥有并资助，与 **Wiley** 合作出版，其前身为 **Bell Journal of Economics（贝尔经济学杂志）**。期刊的宗旨原文为："to support and encourage research in the behavior of regulated industries, the economic analysis of organizations, and more generally, applied microeconomics"（支持并鼓励对受管制行业的行为、组织的经济分析、以及更广义的应用微观经济学的研究）。

本仓库刻意**不通用**——它不是泛化的"经济学写作助手"，而是面向 **RJE 与产业组织** 的方法论沉淀：以"一个关于市场或企业如何运行的一阶问题 + 结构模型或可信的简约式设计 + 关于竞争/管制/福利的启示"为核心，并严格遵循 RJE 体例（Style Guide）、压在期刊的**硬性页数上限**之内。

---

## 为什么要为 RJE 单独做一套 Skills？

RJE 的约束维度与综合性顶刊（QJE）或方法类期刊（Econometrica）**显著不同**：

| 约束        | RJE                                                          | 隐含含义                                       |
|-----------|--------------------------------------------------------------|--------------------------------------------|
| 范围       | **刻意狭窄**——以**产业组织为核心**的应用微观                       | 泛微观或宏观问题不符合定位                       |
| 篇幅       | **硬性页数上限**：正文 <=40 页，总计 <=50 页，双倍行距             | 管理的是**页数**而非字数；投稿时强制执行           |
| 摘要       | **<=100 词**                                                 | 不能用 250 词的摘要                            |
| 投稿费     | 每篇文章 **$100**，且自 2026 年 1 月 1 日起**不退还**             | 需预算；不要指望退款（确切金额 待核实）            |
| 投稿门户    | **Wiley Research Exchange**（`wiley.atyponrex.com/journal/RAND`） | 自 2025 年 4 月 23 日起强制使用（取代 Editorial Express）|
| 评审       | 编辑初筛（可能 desk reject）→ **两位匿名审稿人**                  | IO 卖点必须在第一页就清晰可见                    |
| 体例       | 作者—年份制，**不含页码**、**不含期号**，子小节**不编号**          | 编号/脚注式引用显得不合规                       |
| 用词规则    | 因果用 because/as 而非 *since*；转折用 whereas/although 而非 *while*；用 **"article"** 而非 *"paper"* | 文字编辑会强制执行                 |
| 补充材料    | **"一般情况下不鼓励"**；期刊不直接托管；可能被拒收                  | 核心结果应留在正文 + 附录                       |

通用的"科研写作"或"经济学写作"Skill 包不会处理这些约束。所有易变的具体信息（编辑、确切投稿费、页数上限、门户 URL、数据政策）会随时间变化——请**到 rje.org 与 Wiley For Authors 页面核实**。本工具栈无法从官方页面确认的条目均标注为 **待核实**。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/rje-skills
/plugin install rje-skills
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/rje-skills.git
cd rje-skills

mkdir -p ~/.claude/skills && cp -R skills/rje-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/rje-* ~/.codex/skills/
```

### 第一条提示词

```
用 rje-workflow 告诉我，针对我的 RJE 稿件，下一步应该用哪个 skill。
```

---

## 默认工作流

```text
rje-topic-selection
        ▼
rje-contribution-framing
        ▼
rje-literature-positioning
        ▼
rje-identification-strategy
        ▼
rje-data-analysis
        ▼
rje-tables-figures
        ▼
rje-writing-style          （润色）
        ▼
rje-replication-and-data-policy
        ▼
rje-review-process
        ▼
rje-submission
        ▼
rje-rebuttal
```

`rje-workflow` 是路由器——它根据你所处的阶段告诉你下一步该用哪个 skill。

---

## Skills 一览

| Skill                            | 作用                                                                   |
|----------------------------------|------------------------------------------------------------------------|
| `rje-workflow`                   | 路由器——决定下一步调用哪个子 skill                                       |
| `rje-topic-selection`            | 对照 RJE 刻意狭窄的范围检验 IO 适配度                                     |
| `rje-contribution-framing`       | 一句话讲清 IO 贡献，让编辑初筛一眼看懂                                    |
| `rje-literature-positioning`     | 对准 IO 前沿定位贡献（不做独立综述）                                      |
| `rje-identification-strategy`    | 结构式需求/行为/进入/拍卖，或并购/管制的简约式设计                         |
| `rje-data-analysis`              | IO 估计诊断、稳健性与受约束的反事实分析                                   |
| `rje-tables-figures`             | 按 RJE 体例呈现参数/弹性/加成/福利图表                                    |
| `rje-writing-style`              | 作者—年份引用 + RJE 用词规则                                            |
| `rje-replication-and-data-policy`| 可复现材料包 + RJE 对补充材料的"不鼓励"规则                              |
| `rje-review-process`             | 编辑初筛 → 两位匿名审稿人 → 主审编辑                                     |
| `rje-submission`                 | 页数上限、100 词摘要、$100 投稿费、Wiley Research Exchange 投前自检       |
| `rje-rebuttal`                   | 在硬性页数上限内回复两位审稿人 + 编辑                                     |

### 资源

- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的 RJE / Wiley 官方 URL，含访问日期与 待核实 标记
- [`resources/external_tools.md`](resources/external_tools.md) —— IO 数据源（Nielsen/Kilts、FSRDC、FCC/FERC/DOT/CMS）与 Stata / R / Python 包（`pyblp`、`BLPestimatoR`、`csdid`、`fixest`）

---

## 与其它经济学工具栈的差异

| 维度       | RJE                                | QJE（综合性）              | Econometrica          |
|----------|------------------------------------|--------------------------|-----------------------|
| 范围      | 狭窄——产业组织                       | 全经济学、综合性           | 方法 / 理论            |
| 篇幅控制   | **硬性页数上限**（40/50 页）          | 无硬上限；超长附录          | 无硬上限               |
| 主打      | 市场/企业机制 + 福利启示              | 一个大的实证微观问题        | 一个方法 / 定理        |
| 方法      | 结构式**或**简约式 IO                | 自然实验、图形优先          | 估计量性质             |
| 体例      | 作者—年份，不含页码/期号              | 作者—年份（Chicago）       | 定理—证明式严谨        |

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何具体编辑或审稿人的口味
- 不臆断易变元数据（现任编辑、确切投稿费、页数上限、数据政策）——请到 rje.org 核实；未确认条目标注 待核实
- 不评判你的 IO 问题是否真正"一阶重要"——这是研究者自己的判断

---

## 相关项目

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专属 Skill 包索引
- [RAND Journal of Economics（官方）](https://www.rje.org/) —— 兰德公司 / Wiley

---

## 许可证

MIT
