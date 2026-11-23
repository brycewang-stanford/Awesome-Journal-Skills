# Physical Review Letters Skills

<p align="center">
  <img src="assets/cover.svg" alt="Physical Review Letters 期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Physical%20Review%20Letters-0b2d5c)](https://journals.aps.org/prl/)
[![Index](https://img.shields.io/badge/publisher-APS-1f6feb)](https://www.aps.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Physical Review Letters（PRL，物理评论快报）** 投稿的智能体技能栈——由美国物理学会（APS）出版的旗舰级物理学**快报**期刊，发表覆盖**全部**物理学领域（凝聚态、原子分子光学、粒子/核物理、引力/天体、统计/软物质、量子信息等）的简短、高影响力通讯。

本仓库是高度定制化的。它**不是**通用的物理写作工具箱，而是围绕 PRL 的核心约束构建的 **PRL 专用**技能栈：成果必须**重要**且对物理学家具有**广泛兴趣**，在严格的"可扣减"篇幅上限内**简洁**地传达，细节下放到补充材料（Supplemental Material）。

---

## 为什么需要独立的 PRL 技能栈？

PRL 的约束与专业化的 Physical Review 系列期刊（PR A–E、PR Research）有本质区别：

| 约束               | Physical Review Letters                                  | 含义                                                       |
|--------------------|----------------------------------------------------------|------------------------------------------------------------|
| 准入门槛            | 重要性**且**广泛兴趣（两者缺一不可）                     | 正确但增量的结果会因"广度不足"被拒                          |
| 读者群             | 全体物理学家，而非仅你的子领域                            | 开篇与摘要必须让子领域之外的读者也能读懂                    |
| 篇幅               | 简短——约 3750 词 / 约 4 页量级（请核实）                | 远短于 PR 正刊，需要无情精简                                |
| 篇幅计量            | **可扣减预算**：图、表、公式按词当量计入（参考文献、摘要不计） | 多一张图可能要付出一段正文的代价                            |
| 图                 | 仅少量高影响力图                                          | 图 1 必须让人一眼看懂中心结果                               |
| 补充材料            | 承载推导、扩展数据、方法细节                              | 正文必须在**不依赖**补充材料的情况下独立成立               |
| 中心论点            | 恰好**一个**核心结果                                      | 把项目所有结果都塞进去的"大杂烩"快报不契合                  |
| 投稿信              | 必须论证重要性 + 广泛兴趣                                  | 漏掉广度论证是最常见的失误                                  |
| 流程               | APS 编辑 + 审稿人；高度选择性                              | 即使正确也可能因重要性/广度被拒；存在申诉途径               |

通用的"科学写作"技能包无法应对可扣减篇幅预算、重要性/广度门槛，以及"正文独立成立"规则。

> 易变的具体数值（当前词数/图数/参考文献上限、篇幅公式、分类体系、投稿系统网址、费用）会变化——请务必在 APS / PRL 官方作者页面核实。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install prl-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Physical-Review-Letters-Skills

mkdir -p ~/.claude/skills && cp -R skills/prl-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/prl-* ~/.codex/skills/
```

### 首个提示词

```
用 prl-workflow 告诉我，我的 Physical Review Letters 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
prl-scope-fit
        ▼
prl-results-framing
        ▼
prl-methods
        ▼
prl-figures
        ▼
prl-supplementary
        ▼
prl-writing-style       （润色）
        ▼
prl-length-management   （适配可扣减上限）
        ▼
prl-cover-letter
        ▼
prl-submission
        ▼
prl-referee-strategy
        ▼
prl-revision
```

`prl-workflow` 是路由器——它根据你当前所处的阶段，告诉你下一步该用哪个技能。

---

## 技能列表

| 技能                     | 用途                                                                  |
|--------------------------|-----------------------------------------------------------------------|
| `prl-workflow`           | 路由器——决定下一步调用哪个子技能                                      |
| `prl-scope-fit`          | 重要性 + 广泛兴趣门槛；PRL 还是 PR A–E / PR Research                   |
| `prl-results-framing`    | 单一论点叙事、前置重要性的开篇、摘要打磨                              |
| `prl-methods`            | 正文只保留"取信最低限度"的方法；完整细节进补充材料                    |
| `prl-figures`            | 仅少量高影响力图；首图一眼传达结果                                    |
| `prl-supplementary`      | 把推导/扩展数据下放到补充材料；保证正文独立成立                       |
| `prl-writing-style`      | APS 文风、简洁、规范记号、跨子领域可读性                              |
| `prl-length-management`  | 适配可扣减预算（正文 + 图 + 表 + 公式；参考文献不计）                 |
| `prl-cover-letter`       | 向编辑论证重要性 + 广泛兴趣                                           |
| `prl-submission`         | 投稿前预检 + 快报模板（篇幅、格式、文件、元数据）                     |
| `prl-referee-strategy`   | 推荐 / 回避审稿人；预先化解可能的异议                                 |
| `prl-revision`           | 审稿意见回复、再投稿，以及 APS 申诉途径                               |

### 资源

- [`skills/prl-submission/templates/manuscript_template.md`](skills/prl-submission/templates/manuscript_template.md) —— 快报骨架（摘要、正文、图/公式/参考文献预算、补充材料提纲、投稿信）
- [`skills/prl-submission/templates/checklist.md`](skills/prl-submission/templates/checklist.md) —— 10 大类投稿前自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— REVTeX / LaTeX、绘图工具、计算软件包，以及数据仓库（Zenodo / arXiv / ADS / INSPIRE-HEP）

---

## 与专业化 Physical Review 期刊的差异

| 维度               | Physical Review Letters             | Phys. Rev. A–E / PR Research        |
|--------------------|-------------------------------------|-------------------------------------|
| 准入门槛           | 重要性 **+ 广泛兴趣**               | 严谨性 + 子领域相关性               |
| 读者群             | 全体物理学家                        | 特定子领域                          |
| 篇幅               | 简短、严格可扣减上限                | 宽裕；完整存档式处理                |
| 方法               | 正文取信最低限度；其余进补充材料    | 正文给出完整方法                    |
| 增量结果           | 因广度不足被拒                      | 恰当且受欢迎                        |

如果你的结果扎实但偏专业化或增量，`prl-scope-fit` 会建议改投合适的 PR 期刊，而不是硬碰广度门槛。

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Physical Review Letters](https://journals.aps.org/prl/) —— APS 官方期刊页面
- [American Physical Society](https://www.aps.org/) —— 出版方

---

## 许可证

MIT
