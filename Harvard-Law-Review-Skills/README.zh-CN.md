# 哈佛法律评论技能包（Harvard Law Review Skills）

<p align="center">
  <img src="assets/cover.svg" alt="Harvard Law Review cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-HLR-6a1f2b)](https://harvardlawreview.org/)
[![Field](https://img.shields.io/badge/field-Law-1f6feb)](https://harvardlawreview.org/about/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《哈佛法律评论》（Harvard Law Review, HLR）** 投稿的法学论文写作智能体技能栈。HLR 是美国历史最悠久的
**学生主编（student-edited）** 法律评论之一（创刊于 **1887 年 4 月 15 日**），覆盖全部法律领域，由
**哈佛法律评论协会（Harvard Law Review Association）** 出版，隶属 **哈佛法学院（Harvard Law School）**。
HLR 刊发校外作者的 **论文（Articles）、随笔（Essays）、书评（Book Reviews）**，由学生编辑撰写的 **不署名
Notes**，以及每年 11 月的 **联邦最高法院专辑**（含标志性的 **Foreword 前言**）。

本仓库立场鲜明：它 **不是** 把同行评议流程套用到法学上的通用包，也 **不是** 泛泛的学术写作工具箱，而是一套
**专为 HLR** 打造、围绕美国法律评论独特生态的技能栈：你提交的是一篇 **接近定稿、脚注密集** 的论文；动笔前先做
**抢先发表检索（preemption check）**；通过 **Scholastica** 同时投给多家期刊；用一份录用要约去 **加急（expedite）**
撬动排名更高的期刊；在 **2-3 月主季** 与较小的 **8 月季** 内择时投稿；按 **《蓝皮书》（The Bluebook，HLR 是共同
出版方）** 引注；最后熬过学生编辑的高强度编辑，以及逐条核对每个脚注来源的 **cite-check / source-pull**。

---

## HLR 是什么，为何需要专门的技能栈？

HLR 的约束与同行评议期刊不同：

| 约束维度       | HLR                                                  | 含义                                                   |
|----------------|------------------------------------------------------|--------------------------------------------------------|
| 评审模式       | **学生主编**（非同行评议）                            | 面向聪明的法学院学生通才，预期高强度的动手编辑          |
| 范围           | **通才**——覆盖全部法律领域                           | 论点必须超出某一专门领域                                |
| 关键溢价       | 一个 **原创、规范性** 的论点，并讲清其后果            | 单纯描述性的教义梳理不契合                              |
| 原创性检验     | 动笔前的 **抢先发表检索**（SSRN / Westlaw / HeinOnline） | 写完才发现论点已被他人发表＝白费一个夏天                |
| 投稿模式       | 经 **Scholastica** **多投 + 加急**（部分用 ExpressO）  | 只投一家＝放弃唯一的筹码                                |
| 时机           | **2-3 月主季** + 较小的 **8 月季**                    | 尽早投；顶刊席位最先填满                                |
| 引注           | **《蓝皮书》**（HLR 为共同出版方）——带精确页码的脚注 | 不带精确页码的松散引注过不了 source-pull               |
| 编辑           | 高强度实质 + 技术编辑；**逐条 cite-check / source-pull** | 投稿前就要做到来源可调取；回复要快                      |
| 刊发体裁       | 论文、随笔、书评；学生 Notes；最高法院 Foreword       | Notes 由内部撰写；Foreword 系受邀                       |
| 所有方 / 出版方 | **哈佛法律评论协会** / 哈佛法学院                     | 经 Scholastica 投稿，而非同行评议门户                   |

易变细节（确切篇幅指引、费用、投稿渠道、加急/七天政策、当届编辑名单）会变化——未直接确认的项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记为 **待核实**。**请以官网为准。**

### HLR 刊发哪些体裁

- **论文（Articles）**——篇幅长、脚注密集、含规范性论点的原创法学论证。
- **随笔（Essays）**——更短、更聚焦、介入某一活跃争论的干预性文章。
- **书评（Book Reviews）**——由近期某书引发的 **独立论点**，而非内容概述。
- **Notes 与评注**——**由学生撰写且不署名**（内部体裁，非校外作者投稿渠道）。
- **最高法院专辑（11 月）**——**Foreword 前言**（通常由顶尖学者受邀撰写）、教授 Case Comment，以及学生对当年
  重要判决的 Case Notes；另有每年 4 月的 **Developments in the Law** 专辑。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/harvard-law-review-skills
/plugin install harvard-law-review-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/harvard-law-review-skills.git
cd harvard-law-review-skills

mkdir -p ~/.claude/skills && cp -R skills/hlr-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/hlr-* ~/.codex/skills/
```

### 第一条提示

```
用 hlr-workflow 告诉我，我的哈佛法律评论论文下一步该用哪个技能。
```

---

## 默认工作流

```text
hlr-topic-selection
        ▼
hlr-thesis-and-contribution
        ▼
hlr-preemption-check          （尽早做——动笔之前）
        ▼
hlr-argument-structure
        ▼
hlr-sources-and-bluebook
        ▼
hlr-footnotes-and-cite-check
        ▼
hlr-writing-style             （润色）
        ▼
hlr-placement-strategy
        ▼
hlr-submission
        ▼
hlr-student-editor-review     （收到要约之后）
        ▼
hlr-revision-and-editing
```

`hlr-workflow` 是路由器，根据你所处阶段告诉你下一步用哪个技能。**抢先发表检索要尽早做**；在润色文字之前先在
论点 ↔ 论证 ↔ 引注之间反复打磨；上传之前就要规划好投稿组合与加急策略。

---

## 技能清单

| 技能                           | 用途                                                                   |
|--------------------------------|------------------------------------------------------------------------|
| `hlr-workflow`                 | 路由器——决定下一步调用哪个子技能                                       |
| `hlr-topic-selection`          | 选出及时、通才可读、可成功落刊的选题                                    |
| `hlr-thesis-and-contribution`  | 提炼原创规范性论点及其后果，并尽早陈明                                  |
| `hlr-preemption-check`         | 论点是否已被发表？动笔前检索 SSRN / Westlaw / HeinOnline                |
| `hlr-argument-structure`       | 教义 → 理论 → 规范性主张 的论证骨架                                     |
| `hlr-sources-and-bluebook`     | 精确页码引注、权威位阶、《蓝皮书》                                      |
| `hlr-writing-style`            | 面向通才、学生主编的文风；正文与脚注的分工                              |
| `hlr-placement-strategy`       | Scholastica 多投 + 加急机制 + 投稿季时机                                |
| `hlr-student-editor-review`    | 与学生编辑协作；cite-check / source-pull；回应速度                      |
| `hlr-submission`               | Scholastica 投前自检（接近定稿、脚注、加急设置）                        |
| `hlr-revision-and-editing`     | 多轮高强度编辑直至清样付印                                              |
| `hlr-footnotes-and-cite-check` | 密集脚注体系 + source-pull 可调取就绪                                   |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 法律检索数据库（Westlaw / Lexis / HeinOnline / SSRN）、引注工具（《蓝皮书》/ Shepard's / KeyCite / Perma.cc）与投稿生态（Scholastica / ExpressO）
- [`resources/official-source-map.md`](resources/official-source-map.md) — 本包每条事实背后的 HLR 官方链接，未核实项标注 待核实
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 一篇 HLR 风格引言的 before→after（虚构示例）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 按 领域 × 体裁 整理、经网络核实的真实 HLR 文章

**官方依据核对于 2026-06。** 易变细节请以 HLR 官方投稿页为准。

---

## 与兄弟法律评论的差异

| 维度       | 哈佛法律评论（HLR）                  | 耶鲁 / 哥大 / 宾大 / 斯坦福 法律评论            |
|------------|-------------------------------------|------------------------------------------------|
| 模式       | 学生主编、通才                      | 同为学生主编、通才（流程相近）                  |
| 《蓝皮书》 | **共同出版方**                      | YLJ、哥大、宾大同为共同出版方；其余不是         |
| 标志体裁   | 每年的 **最高法院 Foreword**        | 各旗舰各有其标志性栏目                          |
| 落刊机制   | Scholastica 多投 + 加急             | 同一生态——HLR 是顶级冲刺目标                   |

本包专门面向 **HLR**。投稿机制在美国各法律评论间是通用的，但
[`resources/exemplars/library.md`](resources/exemplars/library.md) 中的「切勿张冠李戴」护栏可避免把兄弟期刊的
名篇误记为 HLR 文章。

---

## 本仓库不做什么

- 不替你写出可直接投稿的论文
- 不模拟任何具体学生编辑的口味，也绝不断言当届编辑名单
- 不断言易变元数据（篇幅指引、费用、渠道、加急/七天政策）——请以官网为准；未核实项标注 待核实
- 不替你跑抢先发表检索——它只告诉你如何、在哪里去跑

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 各期刊专属技能包索引
- [Harvard Law Review](https://harvardlawreview.org/) — 期刊官网
- [HLR 投稿页](https://harvardlawreview.org/homepage/submissions/) — 作者须知、Scholastica、加急政策
- [The Bluebook](https://www.legalbluebook.com/) — HLR 共同出版的引注手册

---

## 许可证

MIT
