# 《World Politics》技能包

<p align="center">
  <img src="assets/cover.svg" alt="World Politics 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-World%20Politics-16604a)](https://wpj.princeton.edu/)
[![Field](https://img.shields.io/badge/field-比较政治%20%2B%20国际关系-1f6feb)](https://www.cambridge.org/core/journals/world-politics)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《World Politics》** 投稿的 Agent 技能栈。《World Politics》是 **比较政治与国际关系** 领域的顶尖
季刊，创刊于 **1948 年**，由 **普林斯顿大学国际与地区研究所（PIIRS）** 主办，**约翰斯·霍普金斯大学出版社
（Johns Hopkins University Press）** 出版（2022 年及之前由剑桥大学出版社承印）。该刊"致力于发表国际关系与
比较政治领域的杰出学术成果"——理论与原创实证并重，涵盖定量、定性、比较历史、实验与形式—实证等多种方法。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把综合性政治学包改个名字套用过来。
它是 **《World Politics》专属** 技能栈，围绕该刊最核心的定位构建：它是 **比较政治 + 国际关系的专门刊
（specialist）**。论文的贡献必须**跨越单一案例、能在不同案例或体系间迁移（travel）**，牢牢落在比较政治
或国际关系之内，并避开该刊明确不发表的类别。

---

## 《World Politics》是什么，为何需要专属技能栈？

它的约束既不同于全学科旗舰刊，也不同于纯国际关系刊：

| 约束 | World Politics | 含义 |
|------|----------------|------|
| 主办 / 出版方 | **PIIRS 普林斯顿** / **约翰斯·霍普金斯大学出版社**（剑桥 ≤ 2022） | 通过 **ScholarOne**（`mc.manuscriptcentral.com/wp`）投稿 |
| 范围 | **比较政治 + 国际关系**——是*专门刊*而非综合刊 | 问题须落在 CP/IR 且**能跨案例迁移** |
| 看重 | 推进**理论论争**的实质性问题 + 原创实证 | 不能迁移的单案例描述不合适 |
| 方法 | 定量/定性/比较历史/实验/形式化——各按其标准评判 | 方法须匹配一个跨案例的问题 |
| 评审模式 | **三向匿名（triple-blind）**（作者、读者、编辑） | 彻底匿名；匿名维持到决定作出 |
| 篇幅 | **≤ 12,500 词，含注释与参考文献**；表、图、附录不计入 | 注释与参考文献占用字数；把图表外移 |
| 在线补充材料 | **≤ 15 页**，须节制使用 | 不是无限附录——控制溢出 |
| 摘要 | **≤ 150 词** | 问题 + 方法 + 发现 |
| 文章类型 | **研究论文** + **综述论文**（后者通常为约稿） | 选对类型；综述论文 ≠ 书评 |
| 数据政策 | 定量数据 → **World Politics Dataverse**，录用后、出版前提交 | 边做边建可复现包；经批准可禁限 ≤ 2 年 |
| 不在范围 | 不发表观点/政策评论、独立的政治理论、历史类或新闻性叙述 | 这些是明确的非契合类别 |

易变的具体信息（现任出版方、编辑与任期、确切上限、禁限期、政策措辞）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记 **待核实**。出版方站点
常对自动抓取返回 HTTP 403，**请以官方页面为准。**

### 三点值得内化的差异

- **比较 + IR 专门刊——必须能迁移。** 与全学科的 **APSR / AJPS / JOP** 不同，《World Politics》是*专门
  刊*：贡献须落在比较政治或国际关系，并**跨越单一案例**而具普遍性。优秀的单国研究必须是"某类现象的一个
  案例"，而非只关乎那个国家。
- **比较，而非只做国际关系。** 与纯 IR 刊（如 *International Organization*）不同，《World Politics》把
  **比较政治与 IR 置于同等地位**，尤重二者交叉处的研究（国内制度 ↔ 国际行为）。纯 IR 理论、缺乏比较杠杆
  或实证的稿件契合度低。
- **两种文章类型，均三向匿名。** 除研究论文外，《World Politics》发表 **综述论文**：综合一组主题相关的
  著作**并重塑该领域的研究议程**（区别于书评；通常为约稿）。所有稿件——包括约稿——都经过三向匿名评审。

### 两种文章类型

- **研究论文（Research article）**——围绕一个能迁移的比较/IR 问题的完整原创研究（理论 + 原创实证），
  **≤ 12,500 词**，含注释与参考文献，在线补充材料 **≤ 15 页**。
- **综述论文（Review article）**——分析并比较一组主题相关的著作，*并*推进该领域未来研究的路径。
  **通常为约稿**；动笔前请与编辑确认（待核实）。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/wp-skills
/plugin install wp-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/wp-skills.git
cd wp-skills

mkdir -p ~/.claude/skills && cp -R skills/wp-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/wp-* ~/.codex/skills/
```

### 第一条提示

```
用 wp-workflow 告诉我，我的 World Politics 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
wp-topic-selection
        ▼
wp-literature-positioning
        ▼
wp-theory-building
        ▼
wp-research-design
        ▼
wp-data-analysis
        ▼
wp-tables-figures
        ▼
wp-writing-style          （润色）
        ▼
wp-transparency-and-data-policy
        ▼
wp-review-process
        ▼
wp-submission
        ▼
wp-rebuttal
```

`wp-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。它的首要任务是确认问题**能跨案例迁移**
并落在比较政治或国际关系之内；若准备 **综述论文**，会先把你导向文献定位与理论构建。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `wp-workflow` | 路由器——决定下一步调用哪个子技能 |
| `wp-topic-selection` | CP/IR 契合与"跨案例迁移"测试；研究论文 vs. 综述论文 |
| `wp-literature-positioning` | 把论文定位到活跃的跨案例 CP/IR 论争；打通比较 ↔ IR |
| `wp-theory-building` | 构建可迁移的论证——机制、范围条件、能迁移什么 |
| `wp-research-design` | 为设计辩护——比较历史、跨国定量、定性、形式化 |
| `wp-data-analysis` | 跨国推断、稳健性、可迁移的测量、三角互证 |
| `wp-tables-figures` | 自洽、可读的图表；≤ 15 页在线补充材料预算 |
| `wp-writing-style` | World Politics 体例；在 ≤ 12,500 词内跨案例表达 |
| `wp-transparency-and-data-policy` | World Politics Dataverse 复现包；禁限期；定性透明度 |
| `wp-review-process` | 三向匿名评审、评审规范、范围筛查、APSA 人类受试者 |
| `wp-submission` | ScholarOne 投稿前检查（匿名化、字数、摘要、双倍行距） |
| `wp-rebuttal` | 面向多位匿名评审 + 编辑的 R&R 回应备忘（≤ 约 5 页） |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 比较 + IR 数据源（V-Dem / Polity / COW / UCDP / ACLED / CSES / Manifesto Project）+ R / Stata / Python 与 QCA/CAQDAS 工具
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 PIIRS / JHU / 剑桥官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任出版方、现任编辑、确切上限、禁限期、政策措辞）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的问题是否能跨案例迁移——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [World Politics（PIIRS, 普林斯顿）](https://wpj.princeton.edu/) — 期刊主页、评审指南、Dataverse
- [World Politics（剑桥 Core）](https://www.cambridge.org/core/journals/world-politics) — 存档与作者须知

---

## 许可

MIT
