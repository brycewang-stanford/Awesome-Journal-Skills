# Lancet Skills

<p align="center">
  <img src="assets/cover.png" alt="The Lancet 封面卡" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-The%20Lancet-006272)](https://www.thelancet.com/)
[![Scope](https://img.shields.io/badge/定位-临床医学与全球健康-1f6feb)](https://www.thelancet.com/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **The Lancet（柳叶刀）** 投稿的 Agent Skill 工具栈——临床医学与全球健康旗舰刊。

本仓库刻意**不通用**。它不是泛化的"医学写作助手"，而是把柳叶刀的编辑底线——**临床/公共卫生重要、具有全球相关性、能改变实践或政策，且常带有公平性视角**——以及由此衍生的具体规范沉淀成一套方法论：临床试验前瞻性注册、研究方案 + 统计分析计划、EQUATOR 报告规范及强制的研究流程图、标志性的 **Research in context** 三段式面板、采用 **Findings / Interpretation / Funding** 标题的结构化摘要、临床统计、**利益声明（Declaration of interests）** 与 **资助来源作用（role of the funding source）** 声明、数据共享声明，以及 SAGER 性别与公平性报告。

---

## 为什么要为 The Lancet 单独做一套 Skills？

柳叶刀的约束维度与基础科学刊、乃至 NEJM / JAMA / BMJ 都**显著不同**：

| 维度        | The Lancet 要求                                              | 隐含含义                                       |
|-----------|-----------------------------------------------------------|--------------------------------------------|
| 编辑底线     | 临床/公共卫生重要、**全球相关**、能改变实践或政策、关注公平          | 选题窄或局限于单一地区的稿件**多数不送审、直接拒稿**     |
| 试验注册     | **前瞻性**注册（入组前完成）为强制要求；注册号须写入摘要              | 回顾性注册的试验可能不被受理                       |
| 报告规范     | 经 EQUATOR 套用 CONSORT / STROBE / PRISMA，并附**流程图**       | RCT 没有 CONSORT 流程图即未准备好投稿              |
| Research in context | **必备的三段式面板**，且基于有据可查的系统检索             | 没有系统检索的面板=非系统综述，露怯               |
| 摘要        | 结构化、≤ ~300 词，标题为 **Background / Methods / Findings / Interpretation / Funding** | 用 "Results / Conclusions" 不合体例           |
| 声明        | **利益声明** + **资助来源作用** + 数据共享声明                   | 缺少资助作用/数据共享声明会卡投稿                  |
| 公平性报告   | 视情况套用 **SAGER** 性别 + 种族/族裔 + PROGRESS-Plus           | 不按性别分层报告会被点名                          |
| 过度声称     | 语气审慎；不得超出研究设计下结论                                  | 结论不得超出证据                                |

通用的"医学写作"Skill 包不会编码这些"按刊定制"的约束——而基础科学那套框架（广泛意义、方法塞补充材料）在这里是错的范式。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install lancet-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Lancet-Skills

mkdir -p ~/.claude/skills && cp -R skills/lancet-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/lancet-* ~/.codex/skills/
```

### 第一条提示词

```
用 lancet-workflow 告诉我，针对 The Lancet 的稿子，下一步该用哪个 skill。
```

---

## 默认工作流

```text
lancet-fit                 （先过"临床/全球重要性·能否改变政策"这一关）
        ▼
lancet-study-design        （注册 + 研究方案 + 统计分析计划 + 设计严谨性）
        ▼
lancet-reporting           （CONSORT / STROBE / PRISMA + 流程图）
        ▼
lancet-statistics          （预设分析、ITT、置信区间、亚组）
        ▼
lancet-figures-tables      （Table 1、Kaplan–Meier、森林图、研究流程图）
        ▼
lancet-research-in-context （标志性三段式面板 + 系统检索）
        ▼
lancet-abstract            （结构化摘要：Findings / Interpretation / Funding ≤300 词）
        ▼
lancet-writing             （IMRaD 结构；审慎的讨论；≤3500 词，RCT 为 4500 词）
        ▼
lancet-ethics              （利益声明、资助来源作用、数据共享、SAGER）
        ▼
lancet-submission          （投稿前自检 + 投稿信）
        ▼
lancet-rebuttal            （送审之后——含统计审稿人）
```

`lancet-workflow` 是路由器——根据你所处阶段告诉你下一个该用哪个 skill。

---

## Skills 一览

| Skill                        | 作用                                                              |
|------------------------------|------------------------------------------------------------------|
| `lancet-workflow`            | 路由器——决定下一步调用哪个子 skill；柳叶刀与 NEJM/JAMA/BMJ 的差异     |
| `lancet-fit`                 | 初筛过滤：临床/全球重要性、能否改变实践或政策、公平性；选刊路由         |
| `lancet-study-design`        | 前瞻性试验注册、方案 + SAP、随机化/盲法/ITT、观察性设计                |
| `lancet-reporting`           | EQUATOR 规范（CONSORT/STROBE/PRISMA）+ 强制流程图 + 清单            |
| `lancet-research-in-context` | 标志性面板：Evidence before / Added value / Implications + 系统检索 |
| `lancet-abstract`            | 结构化摘要 ≤300 词：Background / Methods / **Findings** / **Interpretation** / Funding |
| `lancet-writing`             | IMRaD 结构、≤3500 词（RCT 4500 词）、30 条参考、审慎且具全球视野的讨论       |
| `lancet-statistics`          | 置信区间优先于裸 P、ITT + 符合方案、多重性、预设亚组 + 交互检验、绝对+相对效应 |
| `lancet-figures-tables`      | Table 1、带风险人数的 Kaplan–Meier、森林图、CONSORT/研究流程图、地图     |
| `lancet-ethics`              | 利益声明、资助来源作用、数据共享、ICMJE 署名、SAGER 与公平性           |
| `lancet-submission`          | 完整投稿前自检清单 + 模板（清单、投稿信）                            |
| `lancet-rebuttal`            | 决议分诊、统计审稿人专线、逐条回复、审慎的因果措辞                     |

### 资源

- [`skills/lancet-submission/templates/checklist.md`](skills/lancet-submission/templates/checklist.md) — 完整投稿前自检清单
- [`skills/lancet-submission/templates/cover_letter_template.md`](skills/lancet-submission/templates/cover_letter_template.md) — 以临床/全球重要性开场的投稿信脚手架
- [`resources/external_tools.md`](resources/external_tools.md) — 注册库、EQUATOR 报告标准、ICMJE/赫尔辛基宣言、GRADE、公平性（SAGER/PROGRESS-Plus）、统计/绘图工具，及柳叶刀作者页面

---

## 与 NEJM / JAMA / BMJ 的差异

| 维度      | The Lancet                          | NEJM                  | JAMA                | BMJ                   |
|---------|-------------------------------------|-----------------------|---------------------|-----------------------|
| 侧重      | 全球健康、公平、公共卫生、政策            | 临床权威、偏美国        | 临床 + 卫生政策       | 通科、循证、患者参与     |
| 标志件     | **Research in context** 面板（系统检索） | 无对应物              | 结构化摘要            | "What this paper adds" 框 |
| 摘要标题   | Findings / Interpretation（非 Results / Conclusions） | Conclusions   | Conclusions         | Conclusions           |
| 风格      | 国际化、明确的倡导声音                   | 保守                  | 偏方法学              | 开放获取、循证导向       |
| 何时切换    | —                                   | 权威 RCT、无公平视角    | 统计/政策契合更强      | 患者参与角度更强         |

Science 见 [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills)。柳叶刀系列内，可经 `lancet-fit` 考虑 *Lancet Global Health*、*Lancet Public Health*、各专科刊或 *EClinicalMedicine*。

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊定制 skill 包索引
- [Science-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Science-Skills) · [Cell-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Cell-Skills) · [PNAS-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/PNAS-Skills) · [NEJM-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/NEJM-Skills)

---

## 免责声明

本包为独立、社区构建的 skill 包，**与 The Lancet、Elsevier 或任何柳叶刀系列期刊无任何隶属、背书或合作关系**。所有指标（字数、参考文献上限、体例规则）均依据写作时公开的作者指南与 ICMJE 建议——**投稿前请务必以最新的 [Lancet 作者指南](https://www.thelancet.com/for-authors) 与 [ICMJE 建议](https://www.icmje.org/recommendations/) 为准**。

---

## 许可证

MIT
