# 美国宗教学会会刊（JAAR）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Journal of the American Academy of Religion 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JAAR-5b2b52)](https://academic.oup.com/jaar)
[![Field](https://img.shields.io/badge/field-宗教研究-1f6feb)](https://aarweb.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《美国宗教学会会刊》（Journal of the American Academy of Religion, JAAR）** 投稿的 Agent 技能栈。
JAAR 是 **宗教研究领域的旗舰期刊**，是 **美国宗教学会（AAR）**——该领域最大的学术团体——的官方刊物，
由 **牛津大学出版社** 出版。JAAR 发表覆盖 **世界各宗教传统全谱系** 的顶尖学术，以及 **研究宗教的方法论**
本身的研究。

本仓库是**有主见的**。它**不是**通用人文学科工具箱，**也不是**把社会科学包改名——JAAR **没有数据集、
统计或复现政策**。它是 **JAAR 专属** 的宗教学术技能栈：一个对**整个宗教研究领域具有广泛而根本意义**的
论证、对**原始文本与传统**的审慎处理、**方法自觉且反身性（非护教/非信仰宣示）**的学术，以及 JAAR 独特的
**正文内 author-date（作者—年份）** 引用体例。

---

## JAAR 是什么，为何需要专属技能栈？

JAAR 的约束既不同于宗教学的专门刊，也不同于任何社会科学刊：

| 约束 | JAAR | 含义 |
|------|------|------|
| 所有者 / 出版方 | **美国宗教学会（AAR）** / **牛津大学出版社** | 通过 **ScholarOne**（`mc.manuscriptcentral.com/jaarel`）投稿 |
| 立意门槛 | 必须触及**对整个宗教研究领域广泛而根本的关切** | 仅限子领域的稿件会在送审前**被退回重新立意** |
| 看重 | 一篇**“有论点（has a point）”**的文章——带可争议论点的分析 | 描述/综述不合适 |
| 方法 | 文本、历史、哲学、比较、民族志——以及对**方法本身**的研究 | 方法自觉、反身性、**非护教** |
| 评审模式 | **双盲（双向匿名）** | 匿名正文 + 单独标题页 |
| 录用率 | **约 90% 拒稿**（每期约 8 篇、每年约 32 篇） | 领域级意义不可妥协 |
| 篇幅 | **约 8,000–12,000 词**，含参考文献与脚注 | 脚注计入字数；只用于实质性补充 |
| 摘要 | **≤ 150 词** | 简述问题、论证、贡献 |
| 引用 | **正文内 author-date**（**不是**脚注引用）；CMOS 为兜底 | 脚注仅作实质性说明 |
| 书评 | **仅约稿**（不接受自荐；不刊研究生书评） | 不是投稿入口 |

易变信息（编辑与任期、确切篇幅、CMOS 版本、OA APC）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标 **待核实**。
**请以官方期刊页面为准。**

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jaar-skills
/plugin install jaar-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/jaar-skills.git
cd jaar-skills

mkdir -p ~/.claude/skills && cp -R skills/jaar-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jaar-* ~/.codex/skills/
```

### 第一条提示

```
用 jaar-workflow 告诉我，我的 JAAR 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
jaar-topic-selection          （在此为广泛意义重新立意）
        ▼
jaar-scholarly-positioning
        ▼
jaar-argument-development
        ▼
jaar-sources-and-evidence
        ▼
jaar-theory-and-method
        ▼
jaar-structure-and-exposition
        ▼
jaar-writing-style            （润色）
        ▼
jaar-citation-and-style       （正文内 author-date）
        ▼
jaar-review-process
        ▼
jaar-submission
        ▼
jaar-revision-and-response
```

`jaar-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。第一道门永远是 **立意测试**：
用一句话说清你的文章给**整个宗教研究领域**带来了什么。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `jaar-workflow` | 路由器——决定下一步调用哪个子技能 |
| `jaar-topic-selection` | 契合 + 重新立意，使其对宗教研究有广泛而根本的意义 |
| `jaar-scholarly-positioning` | 跨传统、跨方法地定位学术介入 |
| `jaar-argument-development` | 打造“有论点”的、论题驱动的论证 |
| `jaar-sources-and-evidence` | 严谨的原始文本、文献与田野证据 |
| `jaar-theory-and-method` | 方法自觉、反身、非护教的框架；负责任的比较 |
| `jaar-structure-and-exposition` | 在字数预算内搭建人文论文结构 |
| `jaar-writing-style` | 清晰、分析性的散文；性别中立、序列逗号、外来词斜体 |
| `jaar-citation-and-style` | **正文内 author-date** 引用；CMOS 兜底；按年份编排的参考文献表 |
| `jaar-review-process` | 编辑初筛、双盲评审、约 90% 拒稿、时间线 |
| `jaar-submission` | ScholarOne 投稿前检查（匿名正文 + 标题页、立意、摘要） |
| `jaar-revision-and-response` | 回应来自不同传统/方法审稿人的意见 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 原始文献数据库（ATLA / TLG / CBETA / Sefaria…）、语言/转写、理论与方法参考、文献管理工具
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 AAR / OUP 官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的文章
- 不模拟任何特定编辑或审稿人的口味
- 不臆断易变元数据（现任编辑与任期、确切篇幅、CMOS 版本、OA APC）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的研究是否对宗教研究具有广泛而根本的意义——那是学者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Journal of the American Academy of Religion（牛津）](https://academic.oup.com/jaar) — 作者指南、体例表、政策
- [美国宗教学会（AAR）](https://aarweb.org/) — 所有者，宗教研究的学术团体

---

## 许可

MIT
