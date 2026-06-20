# Comparative Political Studies 技能包

<p align="center">
  <img src="assets/cover.svg" alt="Comparative Political Studies cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-CPS-23457a)](https://journals.sagepub.com/home/cps)
[![Field](https://img.shields.io/badge/field-Comparative%20Politics-1f6feb)](https://journals.sagepub.com/author-instructions/cps)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向投稿 **Comparative Political Studies（CPS，《比较政治研究》）** 的智能体技能栈。CPS 由 **SAGE**
出版，创刊于 **1968 年**，是**比较政治学**领域的重要期刊，发表比较政治的方法、理论与实证论文：
**民主化与政体、政治制度、政治行为与参与、族群政治与冲突、比较政治经济学、政党与选举**——跨国家、
跨时段进行比较。它在方法上是多元的：大样本定量与因果推断设计、形式理论、定性与比较历史推断、以及
多方法研究都受欢迎，并各按其自身标准评判。

本仓库是有立场的。它**不是**通用社会科学写作工具箱，也**不是**把通用政治学技能包套用到比较研究上。
它是一个**CPS 专属**技能栈：要求具有**比较杠杆**（跨国家、次国家单元或跨时段）的论断、能**跨地区
迁移**的论证、按其自身方法标准辩护的研究设计、面向 SAGE Track 的**匿名化**准备，以及一份**存入 CPS
Dataverse 的复制材料包**——对定量论文而言，它是最终录用的前置条件。

**官方依据核对于 2026-06。** 易变细节（现任主编、确切字数上限、费用、政策措辞、投稿平台）均标注
**（检索于 2026-06；以官网为准）** 或 **待核实**，须在 SAGE 官方作者页面确认。

---

## 什么是 CPS，为什么需要专属技能栈？

CPS 的约束不同于综合性旗舰刊或国际关系刊：

| 约束             | CPS                                                                  | 含义                                                       |
|------------------|----------------------------------------------------------------------|------------------------------------------------------------|
| 范围             | **比较政治**（跨国与国内比较）                                        | 论文须有比较杠杆，而非单一截面快照                          |
| 看重             | 能跨地区/政体类型**迁移的可携带机制**                                 | 没有比较论断的单一案例区域研究不合适                        |
| 方法             | 定量、定性、形式理论、实验、多方法——各按其自身标准评判               | 不要把单一模板硬套到每篇论文上                              |
| 出版方           | **SAGE 出版社**（自 1968 年）                                         | 通过 **SAGE Track（ScholarOne）** 投稿                      |
| 评审模式         | **匿名**同行评审                                                      | 正文匿名化；身份信息放在单独的标题页                        |
| 篇幅             | 论文**最多 11,000 词**；参考文献、表格、图形**不计入**                | 把篇幅花在图表上；正文保持紧凑                              |
| 摘要             | **非结构化，约 150 词**                                               | 不是结构化摘要                                             |
| 体例             | **APA 式作者–年份**参考文献（SAGE 体例）                              | 非 APSA/Chicago；正文引用与文献表须一致                     |
| 标识符           | **投稿作者须提供 ORCID**                                              | 投稿前在 SAGE Track 关联                                    |
| 透明度           | **CPS Dataverse** 复制材料存放；须有**数据可得性声明**                | 定量论文的最终录用以材料存放为前置条件                      |
| 预注册           | **可选**：匿名预分析计划作为补充材料                                  | 鼓励而非强制；标明已注册 vs. 探索性分析                     |

未直接确认的条目在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标为 **待核实**。**请以官网为准。**

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/comparative-political-studies-skills
/plugin install comparative-political-studies-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/comparative-political-studies-skills.git
cd comparative-political-studies-skills

mkdir -p ~/.claude/skills && cp -R skills/cps-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/cps-* ~/.codex/skills/
```

### 第一条提示

```
用 cps-workflow 告诉我，我的 CPS 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
cps-topic-selection
        ▼
cps-literature-positioning
        ▼
cps-theory-building
        ▼
cps-research-design
        ▼
cps-data-analysis
        ▼
cps-tables-figures
        ▼
cps-writing-style          （润色）
        ▼
cps-transparency-and-data
        ▼
cps-review-process
        ▼
cps-submission
        ▼
cps-rebuttal
```

`cps-workflow` 是路由器——它根据你所处的阶段告诉你下一步该用哪个技能。它的首要任务是**比较适配检查**：
若论文没有比较杠杆、或其论断无法迁移，它会先把你送回 `cps-topic-selection` / `cps-research-design`。

---

## 技能清单

| 技能                           | 用途                                                                       |
|--------------------------------|----------------------------------------------------------------------------|
| `cps-workflow`                 | 路由器——确认比较适配，决定下一步调用哪个子技能                              |
| `cps-topic-selection`          | 比较杠杆与迁移性；相对 APSR/AJPS/WP/IO/BJPS 的选刊判断                       |
| `cps-literature-positioning`   | 把论文定位在某个比较论争中；点名竞争解释；跨地区广度                         |
| `cps-theory-building`          | 构建带边界条件、有区分性含义的可携带机制                                    |
| `cps-research-design`          | 辩护研究设计——跨国面板、案例比较、实验、多方法                              |
| `cps-data-analysis`            | 比较数据的陷阱、推断、稳健性、由理论驱动的异质性                            |
| `cps-tables-figures`           | 自洽、便于比较解读的图表；SAGE 出版规格                                     |
| `cps-writing-style`            | CPS 行文弧线、11,000 词上限、约 150 词摘要、APA 作者–年份参考文献           |
| `cps-transparency-and-data`    | CPS Dataverse 材料包、数据可得性声明、定性透明度                            |
| `cps-review-process`           | 案头筛选、匿名评审、决定类别、比较学者看重什么                              |
| `cps-submission`               | SAGE Track 投稿前检查（匿名化、字数、ORCID、摘要、数据可得性声明）          |
| `cps-rebuttal`                 | 面向多位评审与主编的 R&R 回复信策略                                         |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 比较政治数据源（V-Dem / Polity / CSES / Manifesto Project / QoG / ACLED / UCDP / Correlates of War）与 R / Stata / Python 及定性/CAQDAS 工具
- [`resources/official-source-map.md`](resources/official-source-map.md) — 支撑每条事实的官方 SAGE / CPS 链接，未核实条目标 待核实
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 经核实的真实 CPS 论文，按子领域 × 方法组织，附姊妹刊勿误标清单
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — CPS 风格引言的 改前→改后 示范（虚构教学例）
- [`resources/code/`](resources/code/) — 可复现的 Stata + Python 因果推断骨架（2026-06 内置）

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定主编或评审的口味
- 不断言易变元数据（现任主编与任期、确切字数、费用/APC、政策措辞）——请以官网为准；未核实项标 待核实
- 不替你判断你的问题是否具有真正的比较杠杆——那是研究者自己的判断

---

## 与姊妹期刊的区别

| 期刊 | 范围 | 为何不等同于 CPS |
|------|------|------------------|
| **APSR / AJPS** | 美国综合性政治学旗舰刊 | 面向整个学科；CPS 要的是*比较政治*的贡献 |
| **World Politics / International Organization** | 国际关系及与之相邻的比较研究 | 以国际关系为先；CPS 首先是国内比较政治 |
| **British Journal of Political Science** | 英国综合性广谱刊 | 综合性；CPS 是比较政治专门刊 |
| **Comparative Politics（CUNY）** | 比较政治，偏定性 | 不同期刊/出版方；CPS（SAGE）方法多元 |

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Comparative Political Studies（SAGE）](https://journals.sagepub.com/home/cps) — 出版方主页
- [CPS 投稿指南](https://journals.sagepub.com/author-instructions/cps) — 范围、篇幅、体例、数据政策
- [CPS Dataverse](https://dataverse.harvard.edu/dataverse/cps) — 复制材料库

---

## 许可证

MIT
