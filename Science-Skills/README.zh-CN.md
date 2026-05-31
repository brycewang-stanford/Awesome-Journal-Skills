# Science Skills

<p align="center">
  <img src="assets/cover.png" alt="Science (AAAS) 封面卡" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-Science%20(AAAS)-b1141c)](https://www.science.org/journal/science)
[![Scope](https://img.shields.io/badge/定位-综合性顶刊-1f6feb)](https://www.science.org/journal/science)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Science（美国科学促进会 AAAS）** 投稿的 Agent Skill 工具栈——综合性自然科学旗舰刊。

本仓库刻意**不通用**。它不是泛化的"科研写作助手"，而是把 Science 的编辑底线——**广泛意义 + 跨学科普遍兴趣**——以及由此衍生的具体规范沉淀成一套方法论：Report 与 Research Article 的取舍、一句话总结与 ≤125 词摘要、图件预算、统计与可复现报告、强制的数据/代码/材料存档、Science 编号引用体例、以及"以意义开场"的投稿信。

---

## 为什么要为 Science 单独做一套 Skills？

Science 的约束维度与领域刊、乃至 Nature 都**显著不同**：

| 维度        | Science 要求                                               | 隐含含义                                       |
|-----------|---------------------------------------------------------|--------------------------------------------|
| 编辑底线     | 跨学科的广泛意义 + 普遍兴趣                                    | 专才向稿件**多数不送审、直接拒稿**                  |
| 文章类型     | Report（约 2500 词，≤4 图表）/ Research Article（约 4500 词，≤6） | 类型选错、超长即露怯                              |
| 一句话总结    | 必备，≤ ~125 字符，且不是标题                                  | 缺失或薄弱会在初筛吃亏                            |
| 摘要        | ≤ ~125 词，单段、无小标题、需量化                              | 长的结构化摘要不合体例                            |
| 方法位置     | Report 的方法放**补充材料**                                   | 方法塞正文会撑爆篇幅                              |
| 参考文献     | 编号制、按出现顺序、**正文与补充材料统一连续编号**、全作者列出           | 著者-年份/Nature 体例必须转换                     |
| 数据与代码   | 须存档并给登录号/DOI；"按需提供"不被接受                          | 没有登录号 = 没准备好投稿                         |
| 过度声称     | 送审后被拒的首要原因之一                                       | 结论不得超出证据                                |

通用的"科研写作"Skill 包不会编码这些"按刊定制"的约束。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install science-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Science-Skills

mkdir -p ~/.claude/skills && cp -R skills/sci-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/sci-* ~/.codex/skills/
```

### 第一条提示词

```
用 sci-workflow 告诉我，针对 Science 的稿子，下一步该用哪个 skill。
```

---

## 默认工作流

```text
sci-fit            （先过"广泛意义"这一关）
        ▼
sci-framing        （锁定核心进展 + 为什么是现在）
        ▼
sci-writing        （Report vs Research Article；守住篇幅）
        ▼
sci-figures        （图件控制在预算内）
        ▼
sci-statistics     （严谨性 + 可复现）
        ▼
sci-data           （数据/代码/材料可得性）
        ▼
sci-abstract       （一句话总结 + ≤125 词摘要——润色）
        ▼
sci-citation       （Science 编号体例——润色）
        ▼
sci-cover-letter   （以意义开场的投稿信）
        ▼
sci-submission     （投稿前自检）
        ▼
sci-rebuttal       （送审之后）
```

`sci-workflow` 是路由器——根据你所处阶段告诉你下一个该用哪个 skill。

---

## Skills 一览

| Skill              | 作用                                                          |
|--------------------|-------------------------------------------------------------|
| `sci-workflow`     | 路由器——决定下一步调用哪个子 skill                              |
| `sci-fit`          | 初筛过滤：广泛意义/普遍兴趣判定；选刊路由                          |
| `sci-framing`      | 锁定一句话进展、"为什么是现在"、陈述式标题                         |
| `sci-abstract`     | 一句话总结（≤125 字符）+ ≤125 词摘要                            |
| `sci-writing`      | Report vs Research Article；篇幅预算；方法移入补充材料             |
| `sci-figures`      | 图件预算、栏宽尺寸、≥6pt 字号、展示原始数据、色盲友好               |
| `sci-statistics`   | 效应量 + 置信区间 + n + 检验；重复性；随机化；可复现                |
| `sci-data`         | 仓库存档、登录号/DOI、可得性声明、材料共享                         |
| `sci-citation`     | Science 编号体例、按出现顺序、统一连续编号                        |
| `sci-cover-letter` | 以意义开场、面向编辑的投稿信                                     |
| `sci-submission`   | 完整投稿前自检清单 + 模板                                       |
| `sci-rebuttal`     | 决议分诊、实验优先级、逐条回复                                    |

### 资源

- [`skills/sci-submission/templates/checklist.md`](skills/sci-submission/templates/checklist.md) — 完整投稿前自检清单
- [`skills/sci-submission/templates/cover_letter_template.md`](skills/sci-submission/templates/cover_letter_template.md) — 以意义开场的投稿信脚手架
- [`resources/external_tools.md`](resources/external_tools.md) — 数据存档仓库、报告标准、图表/统计工具、Science 作者页面

---

## 与 Nature / Science Advances / PNAS 的差异

| 维度      | Science                | Nature              | Science Advances / PNAS        |
|---------|------------------------|---------------------|--------------------------------|
| 门槛      | 顶尖广泛意义              | 顶尖广泛意义           | 较宽，但仍重要                    |
| 标志件     | 一句话总结               | 总结段落              | PNAS：120 词 significance statement |
| 参考文献   | 编号、按出现顺序           | 另一种编号体例          | 各自体例                         |
| 方法      | 补充材料（Report）        | Methods 段落约定       | 视情况                          |
| 何时切换    | —                      | 转投前先改体例          | 若达不到顶尖广泛兴趣              |

Nature 见精选的 [nature-skills](https://github.com/Yuan1z0825/nature-skills)。PNAS / NEJM / Lancet / Cell 见 [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) 里的姊妹包。

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属 Skill 包索引
- [Cell-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Cell-Skills) · [PNAS-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/PNAS-Skills) · [NEJM-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/NEJM-Skills) · [Lancet-Skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Lancet-Skills)

---

## 免责声明

本包为独立、社区构建的 skill 包，**与 AAAS / Science 无任何隶属、背书或合作关系**。所有指标（字数、图件上限、体例规则）均依据写作时公开的作者指南——**投稿前请务必以最新的 [Science 作者指南](https://www.science.org/content/page/science-information-authors) 为准**。

---

## 许可证

MIT
