# Population and Development Review 技能包

<p align="center">
  <img src="assets/cover.svg" alt="Population and Development Review 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-PDR-5a2a4a)](https://onlinelibrary.wiley.com/journal/17284457)
[![Field](https://img.shields.io/badge/field-Demography%20%2B%20Development-1f6feb)](https://popcouncil.org/population-and-development-review-journal/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Population and Development Review（PDR，人口与发展评论）** 投稿的智能体技能栈。PDR 由 **Wiley** 代表
**人口理事会（Population Council）** 出版，**季刊**，创刊于 **1975 年**，处于 **人口学与发展研究的交叉地带**。
PDR 致力于推进对 **人口与社会、经济、环境变迁之间关系** 的认识，并为相关的 **公共政策** 讨论提供平台：生育与
家庭变迁、死亡与健康、迁移与城市化、老龄化与人口结构、人口与环境/气候等。它既发表 **实证人口学**、**形式
人口学**，也以其分量厚重的 **综述性/概念性论文（synthetic essays）** 著称。

本仓库立场鲜明：它 **不是** 通用社会科学写作工具箱，也 **不是** 把方法导向的人口学技能包套用到发展研究上。
它是 **PDR 专属** 技能栈——一个真正的、具有广泛兴趣的 **人口—发展** 问题；一个能 **跨学科** 对话的论证
（经济学者或环境学者也应在意你的生育论文）；一个在 **人口学** 层面被严谨辩护、并明确点出其 **发展含义** 的研究
设计；**双向匿名（double-anonymized）** 准备；以及一份带 **可复现代码**、存入 FAIR 仓库的 **数据可得性声明**。

---

## PDR 是什么，为何需要专属技能栈？

PDR 的约束不同于方法导向的人口学期刊或发展经济学期刊：

| 约束       | Population and Development Review                                          | 含义                                               |
|------------|---------------------------------------------------------------------------|----------------------------------------------------|
| 范围       | **人口 ↔ 发展**——生育、死亡、迁移、老龄化、**环境**、政策                  | 论文须把人口过程与发展相连，而不仅仅使用人口数据   |
| 偏好       | **广泛兴趣** + 明确贡献，含 **综述性/概念性论文**                          | 狭窄的估计、或无落点的纯框架都属不合范围           |
| 方法       | 生命表、分解、事件史、APC、预测、因果——**并且** 概念性综合                 | 选用能回答"人口—发展"问题的方法                    |
| 出版方/所有方 | **Wiley**（出版）/ **人口理事会**（所有）；创刊 **1975**                  | 经 **ScholarOne** 投稿；参考文献采用 APA 体例      |
| 评审模式   | **双向匿名**（≥2 名审稿人），先经编辑/委员会初筛，约 3 个月给出首次决定    | 删除全部合著者标识；审稿人与作者互相匿名           |
| 投稿格式   | 首轮 **自由格式（Free Format）**——参考文献只需风格一致；修回时再套 APA    | 首轮不必过度排版，保持一致即可                     |
| 费用       | **无作者费用**——无投稿费，标准模式下 **无 APC**                            | 无需预算；若选 Online Open 可能另有 Wiley APC      |
| 篇幅       | 研究论文通常 **约 8,000–10,000 词**；Notes & Commentary 较短              | 视为惯例；以官网作者页确认是否有硬性上限           |
| 透明度     | **数据可得性声明** + 持久标识符；ORCID；可复现代码                         | PDR 不自设仓库——须自行存入 FAIR 仓库              |

易变信息（现任主编、摘要/篇幅上限、投稿链接、费用/Online Open 选项、政策措辞）会变动——未直接核实的条目在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记为 **待核实**。**请以官方期刊页面为准。**

### 文章类型

- **Research Article（研究论文）**——完整原创研究或分量厚重的综述性论文；通常 **约 8,000–10,000 词**。
- **Notes & Commentary（札记与评论）**——围绕当下人口议题的简短聚焦论证或回应。
- **Data & Perspectives（数据与视角）**——新数据集、指标或对人口统计的新解读。
- **Archives（档案）**——带框架解读的档案性人口文献或官方机构文本。
- **Book Review（书评）**——对人口/发展类著作的评议（通常为约稿）。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/population-and-development-review-skills
/plugin install population-and-development-review-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/population-and-development-review-skills.git
cd population-and-development-review-skills

mkdir -p ~/.claude/skills && cp -R skills/popdevr-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/popdevr-* ~/.codex/skills/
```

### 第一条提示

```
用 popdevr-workflow 告诉我，我的 PDR 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
popdevr-topic-selection
        ▼
popdevr-literature-positioning
        ▼
popdevr-theory-building
        ▼
popdevr-research-design
        ▼
popdevr-data-analysis
        ▼
popdevr-tables-figures
        ▼
popdevr-writing-style          （润色）
        ▼
popdevr-transparency-and-data
        ▼
popdevr-review-process
        ▼
popdevr-submission
        ▼
popdevr-rebuttal
```

`popdevr-workflow` 是路由器——根据你所处阶段指明下一步该用哪个技能。实证类 PDR 论文会在
**理论 ↔ 设计 ↔ 分析** 间反复迭代以打磨"人口—发展"论证；综述性论文则在
**文献定位 ↔ 理论构建 ↔ 写作风格** 间循环，因为其贡献在于框架，而非新估计。

---

## 技能列表

| 技能                            | 用途                                                              |
|---------------------------------|-------------------------------------------------------------------|
| `popdevr-workflow`              | 路由器——决定下一步调用哪个子技能                                  |
| `popdevr-topic-selection`       | 人口—发展契合度与广泛兴趣；选定文章类型                           |
| `popdevr-literature-positioning`| 既对话人口科学又对话发展辩论；立住贡献                            |
| `popdevr-theory-building`       | 把机制、更锐利的估计或综合框架打造成贡献                          |
| `popdevr-research-design`       | 选择并辩护方法（生命表、分解、事件史、APC、预测）                 |
| `popdevr-data-analysis`         | 率/暴露构建、不确定性、可比性、发展含义                           |
| `popdevr-tables-figures`        | 人口金字塔、年龄模式、生存曲线、预测扇形、比较型图表             |
| `popdevr-writing-style`         | 清晰的随笔式行文；摘要/关键词；自由格式；修回时套 APA            |
| `popdevr-transparency-and-data` | 数据可得性声明、FAIR 存储、DHS/普查授权、ORCID                   |
| `popdevr-review-process`        | 编辑初筛、双向匿名评审、约 3 个月决定                            |
| `popdevr-submission`            | ScholarOne 提交前检查（匿名化、自由格式、数据声明、无费用）       |
| `popdevr-rebuttal`              | 面向跨学科审稿人与决策主编的 R&R 回复策略                        |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 人口 + 发展数据源（HMD / HFD / WPP / IPUMS / DHS / WDI）+ R / Stata / Python 包（生命表、分解、生存分析、APC、预测）
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 Wiley / 人口理事会官方链接，未核实项标记 待核实
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 一篇虚构的 PDR 风格引言（修改前 → 修改后）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 经网络核实的真实 PDR 论文，按主题 × 贡献组织，附姊妹刊防误用提示
- [`resources/code/`](resources/code/) — 可复现的 Stata + Python 因果推断脚手架（外部移植、与期刊无关）

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定主编或审稿人的口味
- 不断言易变元数据（现任主编、确切上限、投稿链接、费用/Online Open 选项、政策措辞）——请以官网为准，未核实项标记 待核实
- 不替你判断问题是否具有广泛的人口—发展兴趣——这是研究者的判断
- 不假定 Wiley APC 适用——标准模式下 PDR 无作者费用

---

## 与姊妹期刊的差异

| 期刊 | 所有方 / 出版方 | 独特要求 | 本技能包立场 |
|------|------------------|----------|--------------|
| **Population and Development Review (PDR)** | 人口理事会 / Wiley | 人口 ↔ 发展 + 政策；**综述性论文**；广泛兴趣 | 把人口过程与发展相连；尊重随笔传统 |
| Demography | PAA / Duke UP | 方法导向的人口科学；双盲；S2O | 纯人口科学估计请用 `Demography-Skills` |
| Population Studies | 人口调查委员会 / T&F | 形式与实证人口学，方法严谨 | 若贡献偏方法而非面向发展，应改投 |
| Population Research and Policy Review | Springer | 应用型人口政策 | 若是无广泛人口—发展论证的应用政策，应改投 |
| Studies in Family Planning | 人口理事会 / Wiley | 生殖健康项目与评估 | 若聚焦项目/干预而非人口—发展关系，应改投 |

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [PDR @ Wiley Online Library](https://onlinelibrary.wiley.com/journal/17284457) — 出版方主页、当期、作者指南
- [PDR @ 人口理事会](https://popcouncil.org/population-and-development-review-journal/) — 所有方、范围、编辑监督
- [PDR @ JSTOR](https://www.jstor.org/journal/popudeverevi) — 1975 年至今的存档

---

## 许可证

MIT
