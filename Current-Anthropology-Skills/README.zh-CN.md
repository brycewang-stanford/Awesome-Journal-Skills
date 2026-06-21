# Current Anthropology 技能包

<p align="center">
  <img src="assets/cover.svg" alt="Current Anthropology 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Current%20Anthropology-7a2a2a)](https://www.journals.uchicago.edu/journals/ca/about)
[![Field](https://img.shields.io/badge/field-Anthropology-1f6feb)](https://wennergren.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向投稿 **Current Anthropology（CA，《当代人类学》）** 的智能体技能栈。CA 是跨国、**覆盖人类学全部分支**
的期刊，由 **芝加哥大学出版社（University of Chicago Press）代表 Wenner-Gren 人类学研究基金会
（Wenner-Gren Foundation for Anthropological Research）出版**，由 Sol Tax 于 **1959 年** 创办。CA 发表
横跨**整个人类学**的研究：**社会文化人类学、考古学、生物／体质人类学、语言人类学**，并兼及民族史、史前史与
应用研究，以理论性、综合性、面向全球读者的"塑造领域议程"的论文见长。

CA 与所有同类期刊最根本的不同在于 **CA✩ Treatment（CA✩ 评议机制）**：当一篇 **Major Article（重要论文）**
被接收后，编辑会向国际范围内的人类学者**约请具名评议（Comments）**，并将这些评议**与论文一同刊出**，同时附上
**作者的回应（Reply）**。被接收的论文是连同其批评者与作者回应**一起公开发表**的。这一"评议—回应"机制贯穿整个
写作生命周期——你要写得**足够大胆、值得他人评议**，同时**足够稳健、经得起具名公开批评**。

本仓库立场鲜明。它**不是**通用的社会科学写作工具箱，也**不是**把计量经济学套件改头换面用于人类学。它是
**CA 专用**技能栈：追求**面向全部分支、能塑造议程的重要性**，论文要**跨越本分支说话**并**经得起 CA✩ 评议**，
将**民族志与质性推断视为一等公民**，明确呈现**反身性与立场性**，并以**研究伦理与问责**为核心——知情同意、
匿名化、对脆弱社群的保护、遗产／归还义务，以及 **Wenner-Gren 著作权转让**。

---

## 什么是 CA，为何需要专用技能栈？

CA 的约束不同于单一分支期刊或量化社会科学期刊：

| 约束维度        | Current Anthropology                                                   | 含义                                              |
|-----------------|-----------------------------------------------------------------------|---------------------------------------------------|
| 范围            | 人类学**全部分支**，跨国                                                | 论文必须超越本分支                                |
| 标志性流程      | **CA✩ Treatment**——具名公开评议 + 作者回应（仅 Major Article）          | 论证要既能引发评议、又经得起公开批评              |
| 看重            | **能塑造领域议程、值得国际辩论的重要干预**                              | 狭窄的、仅限本分支的描述不适合作 Major Article    |
| 方法            | **民族志／质性为一等公民**；亦含材料、实验室、计算方法                  | 不要把民族志硬塞进"假设检验"模板                  |
| 出版方／资助    | **芝加哥大学出版社** 代表 **Wenner-Gren 基金会**                        | 经 **Editorial Manager** 投稿；Wenner-Gren 著作权 |
| 篇幅            | **Major Article 6,000–10,000** 词；**Report 3,000–5,000**；**摘要 ≤ 200** | 词数含参考文献与尾注                              |
| 文章类型        | Major Article · Report · Forum · Discussion/Comment（≤ 800 词）· Current Applications | 仅 Major Article 获得完整 CA✩ 评议       |
| 文件            | **`.doc`/`.rtf`** 正文 + **单独的 TIFF/EPS** 图（不要嵌入 PDF）        | 常见且可避免的上传失误                            |
| 体例            | 接受 **free-format** 投稿；定稿用 **Chicago 作者—年份**，文献按字母排序  | 文献含 DOI；不鼓励行话；非专家亦可读懂            |
| 伦理            | **知情同意、匿名化、遗产／归还、问责**为核心                            | 伦理须前置设计，且会暴露于公开评议                |

> **官方依据核于 2026-06** —— 事实锚定于 CA 投稿须知（芝加哥大学出版社）、Wenner-Gren 编辑页面与期刊
> About 页。在线 Editorial Manager 提示、编辑团队、匿名评审模式与录用率会变动；请在投稿时以官网为准。

### 文章类型一览

- **Major Article（重要论文）**——塑造领域议程的干预，**6,000–10,000 词**，摘要 ≤ 200，图表 ≤ 12。
  **获得 CA✩ Treatment**（公开评议 + 回应）。
- **Report（报告）**——尖锐发现／论争／新框架，**3,000–5,000 词**，图表 ≤ 4。
- **Forum（论坛）**——围绕紧迫议题的多作者策展辩论。
- **Discussion / Comment（讨论／评议）**——对近期 CA 文章的回应或批评，**≤ 800 词**（含参考文献）。
- **Current Applications**——连接学术与应用人类学的开放获取栏目。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/current-anthropology-skills
/plugin install current-anthropology-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/current-anthropology-skills.git
cd current-anthropology-skills

mkdir -p ~/.claude/skills && cp -R skills/curranthro-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/curranthro-* ~/.codex/skills/
```

### 第一条指令

```
用 curranthro-workflow 告诉我，我的 Current Anthropology 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
curranthro-topic-selection
        ▼
curranthro-literature-positioning
        ▼
curranthro-theory-building
        ▼
curranthro-research-design
        ▼
curranthro-data-analysis
        ▼
curranthro-tables-figures
        ▼
curranthro-writing-style          （润色）
        ▼
curranthro-transparency-and-data  （伦理与问责——也要尽早运行）
        ▼
curranthro-review-process         （含 CA✩ Treatment）
        ▼
curranthro-submission
        ▼
curranthro-rebuttal               （R&R 回复信，以及公开的 CA✩ Reply）
```

`curranthro-workflow` 是路由器——根据你的阶段、分支与文章类型告诉你下一步该用哪个技能。**伦理与问责**技能
（`curranthro-transparency-and-data`）应**尽早**运行、并在投稿前再次运行。从一开始就要问：*在 CA✩ Treatment
下，谁会被约请来评议？他们会说什么？*

---

## 技能列表

| 技能                                | 用途                                                                       |
|-------------------------------------|----------------------------------------------------------------------------|
| `curranthro-workflow`               | 路由器——按阶段／分支／类型决定下一步调用哪个子技能                          |
| `curranthro-topic-selection`        | 全分支契合度；塑造议程、值得评议的干预；选定文章类型                        |
| `curranthro-literature-positioning` | 跨越本分支说话；跨国引用政治；预判评议人                                    |
| `curranthro-theory-building`        | 为 CA✩ 评议打造可迁移、可争议的概念 + 反身性论证                            |
| `curranthro-research-design`        | 为设计辩护——田野、档案／材料、实验室／量化——以抵御公开批评                  |
| `curranthro-data-analysis`          | 有纪律的阐释；诚实的证据；生物／考古的量化严谨                              |
| `curranthro-tables-figures`         | 图表展品：同意、授权、遗产；图表上限 + TIFF/EPS 格式                        |
| `curranthro-writing-style`          | free-format → Chicago 作者—年份；触达全部分支；少行话的文风                  |
| `curranthro-transparency-and-data`  | 伦理与问责：同意、匿名化、归还、Wenner-Gren 著作权                          |
| `curranthro-review-process`         | 初筛、同行评审，以及标志性的 CA✩ 评议—回应机制                              |
| `curranthro-submission`             | Editorial Manager 投稿前检查（篇幅、文件格式、伦理、Wenner-Gren 著作权）    |
| `curranthro-rebuttal`               | R&R 回复信 **以及** 公开发表的 CA✩ Reply（对评议的回应）                   |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 按分支分类的人类学数据源、档案与软件（CAQDAS、转写、GIS、实验室／量化）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 支撑本包每条事实的官方 CA / Wenner-Gren / 芝大社链接与实时核查提示
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— CA 风格引言的修改前→后示例（虚构）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 经网络核实的真实 CA 论文（按分支 × 方法），附同类期刊辨别

---

## 与同类期刊的差异

| 期刊                       | 范围／形式                                                       | 本包的辨别 |
|----------------------------|-----------------------------------------------------------------|-----------|
| **Current Anthropology (CA)** | **全分支**、跨国；**CA✩ 评议—回应** 机制；Wenner-Gren／芝大社   | 本包的对象 |
| *American Anthropologist* (AA) | 四领域 AAA 旗舰（Wiley）；**无**评议机制                        | CA 有 CA✩ 评议 + 回应，AA 没有；出版方／投稿系统也不同 |
| *American Ethnologist* (AE) | 社会文化民族志（AAA/AES）                                        | CA 覆盖全分支，而非 AE 的社会文化专注 |
| *Cultural Anthropology* (CulAnth) | 社会文化、理论先行（SCA），常开放获取                       | CA 覆盖全分支并有 CA✩ 机制，而非 CulAnth 的社会文化专属 |

---

## 本仓库不做的事

- 不替你写出可投稿的成稿
- 不模拟任何特定编辑、评审或评议人的口味
- 不发放伦理豁免，也不替代 IRB／社群审查
- 不硬编码超出可溯源事实的易变元数据；请在官网核实 Editorial Manager 提示、编辑团队、匿名模式与录用率

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Current Anthropology（芝加哥大学出版社）](https://www.journals.uchicago.edu/journals/ca/about) —— 期刊主页、投稿须知
- [Wenner-Gren 基金会](https://wennergren.org/) —— 资助方；编辑公告

---

## 许可

MIT
