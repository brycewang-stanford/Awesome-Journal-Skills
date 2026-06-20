# 美国社会学杂志（AJS）技能包

<p align="center">
  <img src="assets/cover.svg" alt="American Journal of Sociology 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AJS-2f3e5c)](https://www.journals.uchicago.edu/journals/ajs)
[![Field](https://img.shields.io/badge/field-社会学-1f6feb)](https://www.journals.uchicago.edu/journals/ajs)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《美国社会学杂志》（American Journal of Sociology, AJS）** 投稿的 Agent 技能栈。AJS 是该学科
**历史最悠久** 的期刊，**1895 年** 由 **Albion Small** 创办，自创刊起一直设在 **芝加哥大学社会学系**，
由 **芝加哥大学出版社**（**不是** SAGE/ASA）出版。AJS 是综合性社会学刊，以 **理论雄心** 与
**比较历史** 研究著称，欢迎定量、定性、民族志、网络与形式化研究，覆盖社会学及相邻社会科学。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把《美国社会学评论》(ASR) 改名。
AJS 与 ASR 同为社会学旗舰，却是非常不同的期刊：出版方不同（芝大社 vs SAGE/ASA）、体例不同
（AJS 自有体例 vs ASA Style Guide）、独特的 **学生参与的双盲** 评审、**30 美元投稿费**、**无固定字数上限**，
以及悠久的 **Comment-and-Reply（评论与回应）** 传统。

---

## AJS 是什么，为何需要专属技能栈？

AJS 的约束不同于 ASR，也不同于领域刊/方法刊：

| 约束 | AJS | 含义 |
|------|------|------|
| 所有者 / 出版方 | **芝加哥大学**（社会学系）/ **芝加哥大学出版社** | 非 SAGE/ASA；通过 Editorial Manager 投稿 |
| 看重 | **理论雄心** + 与当代社会学对话 | 仅有发现或观点文章不合适（会被 AJS "preject"） |
| 方法 | 定量、比较历史、民族志、网络、形式——各按其标准 | 不要把同一模板硬套所有论文 |
| 评审模式 | **双盲**、学生参与分配；不用作者关系网内的评审 | 稿件匿名化；封面页为**单独文件** |
| 费用 | **30 美元投稿费**；**单一作者研究生** 可免 | 非研究生须预算此费 |
| 篇幅 | **无固定字数上限**；鼓励精炼（超过约 18,000 词评审更费时）| 容忍长文但不鼓励；**摘要约 150 词** |
| 体例 | **AJS 自有 author-date 体例** | **不是** ASA Style Guide；具体格式核对官方页 |
| 透明度 | **未宣称强制的编辑部核验复现存储** | 充分记录；声明存储门槛前核对现行政策 |
| 特色 | **Comment-and-Reply** 传统；可观的 **书评** 栏目；Roger V. Gould 奖 | 投稿前选对文章类型 |

易变信息（现任编辑与任期、确切费用/豁免、篇幅与摘要要求、引用体例细节、任何数据政策）会变化。
[`resources/official-source-map.md`](resources/official-source-map.md) 为每条事实标出芝加哥大学出版社、
Editorial Manager 或芝加哥大学的官方来源路径；投稿前请在浏览器中即时核对这些操作性细节。

### AJS vs. ASR 一览

- **AJS**——芝大社；理论优先、比较历史见长；双盲、学生参与评审；30 美元费（研究生单作者免）；无字数上限；**自有体例**；Comment-and-Reply。
- **ASR**——SAGE / ASA；全学科旗舰；masked 评审；25 美元费（ASA 学生免）；约 15,000 词上限；**ASA Style Guide**。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/ajs-skills
/plugin install ajs-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/ajs-skills.git
cd ajs-skills

mkdir -p ~/.claude/skills && cp -R skills/ajs-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/ajs-* ~/.codex/skills/
```

### 第一条提示

```
用 ajs-workflow 告诉我，我的 AJS 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
ajs-topic-selection
        ▼
ajs-literature-positioning
        ▼
ajs-theory-building
        ▼
ajs-research-design
        ▼
ajs-data-analysis
        ▼
ajs-tables-figures
        ▼
ajs-writing-style          （润色）
        ▼
ajs-data-and-transparency
        ▼
ajs-review-process
        ▼
ajs-submission
        ▼
ajs-rebuttal
```

`ajs-workflow` 是路由器——根据你所处阶段、以及是 **研究论文**、**Comment/Reply** 还是 **书评**，
告诉你下一步用哪个技能。AJS 论文通常在 writing-style 前多次循环 理论 ↔ 设计 ↔ 分析；
理论贡献往往到后期才打磨清晰。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `ajs-workflow` | 路由器——决定下一步调用哪个子技能 |
| `ajs-topic-selection` | 契合：与当代社会学对话 + 可迁移的理论收益 |
| `ajs-literature-positioning` | 把贡献定位到活跃的社会学论争（含 Comment/Reply） |
| `ajs-theory-building` | 把发现提升为可迁移的理论（定量/比较历史/民族志/形式） |
| `ajs-research-design` | 按各自方法论标准为设计辩护 |
| `ajs-data-analysis` | 分析规范、不确定性、稳健性、三角互证 |
| `ajs-tables-figures` | AJS 图表规范；离散编号；强制图 alt text |
| `ajs-writing-style` | 使用 AJS 自有体例（非 ASA Style Guide）；通才可读的文风 |
| `ajs-data-and-transparency` | 数据/材料文档与共享；不夸大强制要求（无核验存储） |
| `ajs-review-process` | 双盲、学生参与评审；"preject"；决定类别 |
| `ajs-submission` | Editorial Manager 投稿前检查（30 美元费、单独封面页、摘要、alt text） |
| `ajs-rebuttal` | R&R 回应信 + Comment-and-Reply 传统下的作者 Reply |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 社会学数据源（GSS / IPUMS / PSID / V-Dem / 网络与定性数据）+ R / Stata / Python 与 CAQDAS/QCA 工具
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的芝大社 / AJS 官方 URL，以及易变项目的 live-check 提示

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不在缺少当前官方来源路径时臆断易变元数据（现任编辑与任期、确切费用/豁免、篇幅/摘要规则、引用体例、数据政策）；投稿前请以官方页面即时核对
- 不替你判断你的工作是否对 AJS 足够有理论雄心——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [American Journal of Sociology（芝加哥大学出版社）](https://www.journals.uchicago.edu/journals/ajs) — 出版方主页、投稿说明、编辑政策
- [AJS 投稿说明](https://www.journals.uchicago.edu/journals/ajs/instruct) — 当前作者指南与投稿机制

---

## 许可

MIT
