# Progress in Human Geography 技能包

<p align="center"><img src="assets/cover.svg" width="200" alt="Progress in Human Geography 技能包封面"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-PiHG-1f6a4a)](https://journals.sagepub.com/home/phg)
[![Index](https://img.shields.io/badge/index-review%20journal-1f6a4a)](https://journals.sagepub.com/home/phg)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://journals.sagepub.com/home/phg)

[English](README.md) | 简体中文

面向 **Progress in Human Geography（PiHG，《人文地理学进展》）** 的 **批判性综述、概念性介入与受邀进展报告** 的十二个智能体技能。PiHG 是 SAGE 旗下人文地理学领域的旗舰 **综述/前沿述评** 期刊（创刊于 1977 年），刊发对哲学、概念、理论、专题、方法论、伦理与政治议题的重大批判性综述，以及著名的、由编辑 **约稿** 的 **进展报告（progress reports）**，系统评述各子领域（经济、城市、政治、文化、女性主义、发展、超越人类等地理学）的演进。由于 PiHG **不发表原创实证结果或详细个案**，本技能包以 **综述写作技艺** 取代识别策略与复现包技艺：界定值得综合的争论、双重投稿路径（约稿报告 vs. 投稿综述）、跨理论传统的系统性批判性覆盖、以概念论证取代文献罗列、跨传统的公正与反身性、争论图谱型展品、权威而可读、以研究议程收尾的文风，以及学术装置与立场性（positionality）的透明度。

**官方依据核对于 2026-06**（提交前请复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要独立技能包？

| PiHG 的约束 | 它带来的要求 |
|-------------|--------------|
| 成果形态 | **批判性综述/概念性介入**，综合他人成果——没有识别策略，没有自有复现包 |
| 范围 | PiHG **不发表实证结果或详细个案**——贡献是批判性综合，绝非新数据 |
| 投稿路径 | **两条路径**：进展报告由 **编辑约稿**；综述/介入按内容栏目（Perspectives、Reviews、Opinions、Biographies、Key Publications）**投稿** |
| 读者 | 面向 **子领域之外的人文地理学者**，而非仅专家 |
| 主线 | 贡献是关于该领域处于何处、应往何处去的 **概念论证**——PiHG 是议程设定型期刊 |
| 平衡 | 对各理论传统（政治经济、女性主义、后结构、后殖民、超越人类、量化）公正而 **反身** 的处理；不可自我推销 |
| 透明度 | 质性/批判地理学规范——学术装置、立场性、叙述式覆盖说明（而非 PRISMA 清点） |
| 同类边界 | 区别于 **Annals of the AAG**（原创实证）、**Transactions of the IBG**（实证+部分综述）、**Antipode**（激进地理学） |

## 快速开始

```text
/plugin marketplace add ./Progress-in-Human-Geography-Skills
/plugin install progress-in-human-geography-skills
```

手动使用：从 [`skills/proghg-workflow/SKILL.md`](skills/proghg-workflow/SKILL.md) 开始。

## 默认工作流

```text
proghg-workflow → proghg-topic-selection → proghg-proposal-and-commissioning → proghg-literature-synthesis →
proghg-organizing-framework → proghg-comprehensiveness-and-balance → proghg-tables-figures → proghg-writing-style →
proghg-transparency-and-reproducibility → proghg-editor-strategy → proghg-submission → proghg-revision
```

## 技能一览

| # | 技能 | 作用 |
|---|------|------|
| 1 | [`proghg-workflow`](skills/proghg-workflow/SKILL.md) | PiHG 综述与进展报告的工作流路由器 |
| 2 | [`proghg-topic-selection`](skills/proghg-topic-selection/SKILL.md) | 该争论是否够 PiHG 规格？四项适配测试 |
| 3 | [`proghg-proposal-and-commissioning`](skills/proghg-proposal-and-commissioning/SKILL.md) | 约稿报告 vs. 投稿综述两条投稿路径 |
| 4 | [`proghg-literature-synthesis`](skills/proghg-literature-synthesis/SKILL.md) | 跨理论传统的系统性批判覆盖 |
| 5 | [`proghg-organizing-framework`](skills/proghg-organizing-framework/SKILL.md) | 构建概念论证主线（而非文献罗列） |
| 6 | [`proghg-comprehensiveness-and-balance`](skills/proghg-comprehensiveness-and-balance/SKILL.md) | 完整性、取舍与跨传统的公正/反身处理 |
| 7 | [`proghg-tables-figures`](skills/proghg-tables-figures/SKILL.md) | 争论图谱表与概念图 |
| 8 | [`proghg-writing-style`](skills/proghg-writing-style/SKILL.md) | 权威而可读的文风 + 前瞻议程收尾 |
| 9 | [`proghg-transparency-and-reproducibility`](skills/proghg-transparency-and-reproducibility/SKILL.md) | 学术装置、立场性、覆盖说明 |
| 10 | [`proghg-editor-strategy`](skills/proghg-editor-strategy/SKILL.md) | 与编辑协作：约稿 vs. 投稿 |
| 11 | [`proghg-submission`](skills/proghg-submission/SKILL.md) | SAGE ScholarOne 投稿前检查 |
| 12 | [`proghg-revision`](skills/proghg-revision/SKILL.md) | 回应编辑/审稿人对综述的意见 |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方链接与易变项复核
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、综合工具、存储库
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构的综述引言前后对照
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 候选 PiHG 文章 + 待核实槽位（同类期刊防混淆）

本技能包不含 `code/` 目录：PiHG 综述不报告原创估计，故无实证复现包。共享方法参考仅作背景——用于 *评估* 综述所综合的研究，而非自行开展分析。

## 与同类期刊的区别

| 期刊 | 与 PiHG 的关系 |
|------|----------------|
| **Annals of the AAG** | 四大领域的原创实证旗舰；PiHG 综述它们，并不与之竞争 |
| **Transactions of the IBG** | 原创实证 + 部分综述/评论；PiHG 仅做综述/前沿述评 |
| **Antipode** | 激进地理学（常含原创实证/行动主义工作）；PiHG 综述激进学术，但并非 Antipode |
| **Dialogues in Human Geography / Progress in Economic Geography** | 邻近的辩论/综述刊物；引用前请核对刊源 |

## 相关链接

- https://journals.sagepub.com/home/phg
- https://journals.sagepub.com/author-instructions/phg
- https://mc.manuscriptcentral.com/pihg

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
