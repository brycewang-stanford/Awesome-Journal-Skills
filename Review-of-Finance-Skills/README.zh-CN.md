# Review of Finance (《金融评论》) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Review of Finance 期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Review%20of%20Finance-0b3d5c)](https://academic.oup.com/rof)
[![Society](https://img.shields.io/badge/society-EFA-1f6feb)](https://revfin.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Review of Finance（RoF）** 投稿的 Agent Skill 工具栈。RoF 是 **欧洲金融学会（European Finance Association, EFA）的官方期刊**，由 **牛津大学出版社（OUP）** 出版，刊载**面向综合读者、达到金融学前三大刊水平的实证与理论金融研究**。

本仓库刻意**不通用**——它不是泛化的"金融写作助手"，而是面向 RoF 编委口味的方法论沉淀，同时覆盖**实证金融**（资产定价、公司金融、银行、家庭金融、市场微观结构）与**理论金融**（资产定价理论、证券/契约设计、微观结构理论），并围绕期刊的实际规则构建：硬性 60 页上限、150 词摘要上限、Chicago 引用、双盲评审、两轮决定原则、真实且分档的投稿费（含可选 Fast-Track），以及 Code Sharing and Data Availability Policy。

官方依据核验日期：**2026-06-01**。来源见 [`resources/official-source-map.md`](resources/official-source-map.md)，含 OUP author guidelines、RoF/EFA 页面、fee categories、editorial policy、code-sharing policy、FAQ 与 editorial-board updates。

---

## 为什么要为 RoF 单独做一套 Skills？

RoF 的约束维度与一般金融期刊**显著不同**：

| 维度          | Review of Finance                                          | 隐含含义                              |
|-------------|------------------------------------------------------------|-----------------------------------|
| 读者         | 面向全金融的综合读者，**实证与理论兼有**                          | 只对小圈子有意义的结论不适合              |
| 标准         | 审稿人按**金融学前三大刊标准**评判                              | 仅"做得对"不够                       |
| 篇幅         | **硬性 60 页上限**，含附录、参考文献、图、表                     | 臃肿的稿件会被拒；图表空间要精打细算       |
| 摘要         | **不超过 150 词**                                            | 过长摘要显得不合规                    |
| 参考文献      | **Chicago** 格式                                            | 编号/脚注式引用显得不合规               |
| 评审         | **双盲**，**两轮**决定原则                                     | 第一轮是关键；第二轮新提的问题可能被忽略    |
| 投稿费        | **EUR 350**（EFA 会员 EUR 300）；**Fast-Track EUR 900，14 天**决定 | 需预算费用；EFA 会员更便宜             |
| 引用义务      | 作者**必须**检索并引用相关工作；不知情不构成抗辩                   | 遗漏可能被处罚                        |
| 策略性投稿     | 未披露的再投或一稿多投 → **两年禁投**                            | 须在 cover letter 中披露            |
| 复制材料      | code/data 政策是**发表的前置条件**                             | 边做边攒复制包                       |

所有易变的具体信息（现任编辑、确切费用、退款金额、页数/摘要上限、政策措辞）会随时间变化——请**到期刊官网核实**。本工具栈无法用单一一手来源确认的条目，已在 `resources/official-source-map.md` 中标注 **待核实**。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/rof-skills
/plugin install rof-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/rof-skills.git
cd rof-skills

mkdir -p ~/.claude/skills && cp -R skills/rof-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/rof-* ~/.codex/skills/
```

### 第一个提示词

```
用 rof-workflow 告诉我，我的 Review of Finance 稿件下一步该用哪个 skill。
```

---

## 默认工作流

```text
rof-topic-selection
        ▼
rof-contribution-framing
        ▼
rof-literature-positioning
        ▼
rof-identification-strategy   （实证：因果设计 | 理论：假设/结论）
        ▼
rof-data-analysis
        ▼
rof-tables-figures            （注意 60 页上限）
        ▼
rof-writing-style             （摘要 ≤150 词；最后润色）
        ▼
rof-replication-and-data-policy
        ▼
rof-review-process
        ▼
rof-submission                （Editorial Express；regular 或 Fast-Track）
        ▼
rof-rebuttal
```

`rof-workflow` 是路由器——它根据你所处的阶段告诉你下一步该用哪个 skill。

---

## Skills

| Skill                             | 用途                                                              |
|-----------------------------------|-----------------------------------------------------------------|
| `rof-workflow`                    | 路由器——决定下一个该调用的子 skill                                  |
| `rof-topic-selection`             | 判断是否为面向综合读者的一流金融问题（实证或理论）                       |
| `rof-contribution-framing`        | 明确前三大刊审稿人会认可的边际金融贡献                                 |
| `rof-literature-positioning`      | 对照金融前沿定位；履行严格的引用义务                                   |
| `rof-identification-strategy`     | 因果设计（实证）**或**假设/结论/证明（理论）                          |
| `rof-data-analysis`               | 样本、变量、估计、标准误、稳健性（或可复现的数值计算）                    |
| `rof-tables-figures`              | 在硬性 60 页上限内做自洽的图表                                       |
| `rof-writing-style`               | 用 ≤150 词摘要讲清贡献；Chicago 格式                                |
| `rof-replication-and-data-policy` | code/data 复制包、伪数据 + 日志、Data Availability Statement       |
| `rof-review-process`              | 双盲、Screen Reports、两轮逻辑、策略性投稿规则                        |
| `rof-submission`                  | Editorial Express 投前检查 + regular/Fast-Track 费用抉择            |
| `rof-rebuttal`                    | 两轮 R&R 回复信策略                                                |

### 资源

- [`skills/rof-submission/templates/cover_letter.md`](skills/rof-submission/templates/cover_letter.md) —— RoF cover letter 模板，含必备披露
- [`skills/rof-submission/templates/checklist.md`](skills/rof-submission/templates/checklist.md) —— 投前自查清单
- [`resources/external_tools.md`](resources/external_tools.md) —— 金融数据源（CRSP / Compustat / TRACE / OptionMetrics / Call Reports）+ Stata / R / Python 包，以及理论/数值工具
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的 RoF/EFA 官方链接，核验日期 2026-06-01

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何具体编辑或审稿人的口味
- 不断言易变元数据（现任编辑、确切费用、退款金额）——请到官网核实
- 不判断你的想法是否真正"一流"——这是研究者自己的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专属 skill 包索引
- [Review of Finance（官方）](https://academic.oup.com/rof) —— Oxford University Press
- [European Finance Association / RoF](https://revfin.org/) —— 学会与期刊站点

---

## 许可

MIT
