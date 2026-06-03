# 美国历史评论（AHR）技能包

<p align="center">
  <img src="assets/cover.svg" alt="The American Historical Review 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AHR-6b3a2e)](https://academic.oup.com/ahr)
[![Field](https://img.shields.io/badge/field-历史学-8a5a3b)](https://www.historians.org/news-publications/american-historical-review/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《美国历史评论》（The American Historical Review, AHR）** 投稿的 Agent 技能栈。AHR 是
**历史学界的旗舰期刊**，也是 **美国历史学会（AHA）的官方刊物**，创刊于 **1895 年**，自 2023 年起由
**牛津大学出版社** 出版。它发表覆盖 **一切时段、一切地域** 的历史研究——从古代到当代；涵盖非洲、亚洲、
大洋洲、拉丁美洲、中东、欧洲与美洲——读者遍及各个领域的历史学家。

本仓库是**有主见的**，而且属于**人文学科，而非社会科学**。这里**没有数据可得性/可复现政策**、**没有
统计显著性门槛**、**也没有结果表**。一篇 AHR 文章是建立在**一手史料**之上、经过批判性阅读、以**清晰文笔**
和 **芝加哥体例脚注** 展开的**史学介入（historiographical intervention）**。本技能栈**不是**把社会科学
模板改名套到历史学上——它讲的是**论证、档案、阐释与史家手艺**。

---

## AHR 是什么，为何需要专属技能栈？

AHR 的约束既不同于社会科学期刊，也不同于专门史期刊：

| 约束 | AHR | 含义 |
|------|------|------|
| 范围 | **一切时段、一切地域** 的历史；英文 | 文章必须超越自身子领域，对其他历史学家也有意义 |
| 看重 | 建立在一手史料上的**史学介入** | 史料堆砌或仅限本地的发现不合适 |
| 方法 | 社会史/文化史/思想史/政治史/全球史/微观史——各按其标准评判 | 不要硬套模板；历史学没有单一"方法" |
| 出版方 / 所有者 | **牛津大学出版社** / **AHA** | 通过 **ScholarOne** 投稿，而非社会科学投稿系统 |
| 评审模式 | **双向匿名**，**至少 6 位评审** | 稿件须匿名；预期密集而专业的评审意见 |
| 周期 / 录用率 | **6–8 个月**出决定；录用率约 **8–10%** | 周期长；意义与手艺在早期就被定夺 |
| 篇幅 | 正文理想 **≤ 8,000 词**，**不含注释** | 大量注释不计入正文篇幅目标 |
| 体例 | **芝加哥体例**脚注；**无参考文献表**、无文内引用 | 非作者—年份；所有引证都在注释里 |
| 史料 | **一手史料批判** 是核心功夫 | 来源、偏见、沉默、代表性都重要 |
| 图像 | 作者自行清理**版权许可**；每幅图须有 **alt 文本** | 预留版权时间；提前写好 alt 文本 |
| 费用 | **不收作者处理费** | 投稿/发表不要预算 APC |

易变的具体信息（现任编辑与任期、确切词数/注释比例、是否需要摘要、OA/APC 选项、评审人数与周期）会变化——
未直接核实项在 [`resources/official-source-map.md`](resources/official-source-map.md) 中标记 **待核实**。
**请以官方期刊页面为准。**

### AHR 发表什么

- **研究论文（Research articles）**——原创、以论证为驱动的历史研究，正文理想 **≤ 8,000 词**。
- **评论（Reviews）**——规模庞大的**约稿**栏目（每年约 650 篇），评介图书、展览、影片、播客、电子游戏与
  数字史学。评论由编辑部**邀请**，不接受作者自荐承担。
- **特色栏目**——如 *History Unclassified*、*History Lab*、*AHR Syllabus*、*Art as Historical Method*
  等，探索历史书写与呈现的新形式。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/ahr-skills
/plugin install ahr-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/ahr-skills.git
cd ahr-skills

mkdir -p ~/.claude/skills && cp -R skills/ahr-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/ahr-* ~/.codex/skills/
```

### 第一条提示

```
用 ahr-workflow 告诉我，我的 AHR 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
ahr-topic-selection
        ▼
ahr-historiography-positioning
        ▼
ahr-argument-development
        ▼
ahr-sources-and-archives
        ▼
ahr-interpretation-and-method
        ▼
ahr-structure-and-exposition
        ▼
ahr-writing-style              （润色）
        ▼
ahr-citation-and-style
        ▼
ahr-review-process
        ▼
ahr-submission
        ▼
ahr-revision-and-response
```

`ahr-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。历史研究很少是直线推进的：多数项目会在
**论证 ↔ 史料 ↔ 阐释** 之间反复循环，待档案"回话"之后，结构与文笔才最终定型。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `ahr-workflow` | 路由器——决定下一步调用哪个子技能 |
| `ahr-topic-selection` | 面向整个学科的意义；这是不是一个 AHR 级别的问题？ |
| `ahr-historiography-positioning` | 把文章定位为一次"介入"，而非"报告" |
| `ahr-argument-development` | 把档案发现锻造成持续、可被质疑的论点 |
| `ahr-sources-and-archives` | 一手与二手；史料批判；档案引证；图像版权 |
| `ahr-interpretation-and-method` | 选择并为某种阐释视角与尺度辩护 |
| `ahr-structure-and-exposition` | 在约 8,000 词目标内交织叙事与分析 |
| `ahr-writing-style` | 面向各领域历史学家的清晰、富叙事感的文笔 |
| `ahr-citation-and-style` | 芝加哥脚注——无参考文献表、无文内引用；注释体系 |
| `ahr-review-process` | 双向匿名评审、≥6 位评审、6–8 个月、8–10% 录用 |
| `ahr-submission` | ScholarOne 投稿前检查（匿名、篇幅、注释、格式、alt 文本、独占性） |
| `ahr-revision-and-response` | 面向多位专家评审 + 编辑的回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 档案与检索工具（ArchiveGrid / WorldCat / 各国国家档案馆）、数字化数据库（JSTOR / Gale / EEBO-ECCO）、转录/OCR（Transkribus），以及芝加哥脚注的文献管理工具（Zotero / BibLaTeX）
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 AHA / 牛津官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的文章，也绝不臆造或粉饰任何史料
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑与任期、确切词数/注释比例、是否需要摘要、OA/APC 选项）——请以官方页面为准；
  未核实项标 待核实
- 不替你判断你的问题是否具有普遍的历史意义——那是历史学者的判断
- 不套用社会科学模板（假设、数据章节、复现材料包）——AHR 根本没有这些

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [The American Historical Review（牛津 Academic）](https://academic.oup.com/ahr) — 出版方主页
- [AHA 上的 AHR](https://www.historians.org/news-publications/american-historical-review/) — 所有者、投稿指南、评论栏目

---

## 许可

MIT
