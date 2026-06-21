# Field Crops Research（FCR）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Field Crops Research 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-FCR-a08a1e)](https://www.sciencedirect.com/journal/field-crops-research)
[![Field](https://img.shields.io/badge/field-农学%20%2F%20作物科学-3a5a1e)](https://www.sciencedirect.com/journal/field-crops-research)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《Field Crops Research》（FCR，大田作物研究）** 投稿的 Agent 技能栈。FCR 是由 **爱思唯尔
（Elsevier）** 出版的国际一流 **农学与作物科学** 期刊（ISSN **0378-4290**）。它发表关于 **作物生态、
作物生理、农学与作物改良** 的 **实验与建模研究**，对象是为 **粮食、纤维、饲料和生物燃料** 而种植的大田
作物，研究层次涵盖 **作物、田块、农场与景观**。期刊**鼓励纳入产量数据**，以展示田间试验如何揭示作物
生长、发育与产量形成背后的生物物理过程。

本仓库是**有主见的**。它**不是**通用生命科学写作工具箱，**也不是**把受控环境（温室）植物生物学包改个名字
套到大田上。它是 **FCR 专属** 技能栈，围绕期刊的核心要求构建：**真正基于大田、具有多季节和/或多环境意义的
农学研究**、**具有普遍意义的创新贡献**、**严谨的多环境试验设计**、**与设计相匹配的混合模型统计**，以及在
投稿时给出 **数据可得性声明** 的完整 **农学报告**。

---

## FCR 是什么，为何需要专属技能栈？

FCR 的约束不同于通用植物科学刊或受控环境刊：

| 约束 | Field Crops Research | 含义 |
|------|------|------|
| 范围 | **大田作物**：作物生态、生理、农学、作物改良 | 研究须与大田作物及其产量过程挂钩 |
| 环境 | **基于大田**，多季节 / 多环境 | 仅在受控环境完成的研究**不在范围内** |
| 多环境规则 | 田间试验须跨 **≥ 2 个季节和/或多个环境** | 单点单季试验通常通不过这道关 |
| 看重 | **具有普遍意义的新科学见解** + 产量/生物物理关联 | 印证性、描述性或仅地方性的工作会被拒 |
| 物种 | 粮/纤/饲/生物燃料大田作物 | 园艺、木本多年生、非栽培物种均不合适 |
| 出版方 / 投稿系统 | **Elsevier** / **Editorial Manager** | 非 OUP/剑桥；经 Editorial Manager 投稿 |
| 评审模式 | **单向匿名**，通常 ≥ 2 位评审 | 作者不匿名；预期接受农学专家评审 |
| 统计 | 与设计**相匹配**（混合模型、G×E） | 对合并小区做单因素方差分析过不了方法关 |
| 摘要 / 亮点 | 摘要 **≤ 400 词**；**3–5 条亮点**，每条 ≤ 85 字符 | 尽早准备；亮点是发现而非主题 |
| 数据政策 | 投稿时**声明数据可得性**；声明生成式 AI 使用 | 上传前先拟好声明 |

这些事实背后的官方来源见 [`resources/official-source-map.md`](resources/official-source-map.md)。
最终投稿周仍应打开 ScienceDirect / Elsevier 页面，核对编辑名单、价格、文件提示和文类菜单是否有变化。

### 范围边界（请先读）

FCR 明确**不予考虑**：

- **仅在受控条件下**完成的研究——温室、盆栽，或任何**限制根系生长**的系统。
- **单年、单地点/单环境**的田间研究（要求为 ≥ 2 个季节和/或多个环境）。
- **印证性、描述性或仅具地方意义**的工作。
- **园艺**（蔬菜/水果）、**木本多年生**、**药用**及**非栽培**物种，以及天然草地。

若你的项目落在上述任一禁区内，请在投入之前先修正选题框架或设计（见 `fcr-topic-selection`）。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/fcr-skills
/plugin install fcr-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/fcr-skills.git
cd fcr-skills

mkdir -p ~/.claude/skills && cp -R skills/fcr-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/fcr-* ~/.codex/skills/
```

### 第一条提示

```
用 fcr-workflow 告诉我，我的 Field Crops Research 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
fcr-topic-selection          （先过范围关）
        ▼
fcr-literature-positioning
        ▼
fcr-experimental-design
        ▼
fcr-data-analysis
        ▼
fcr-figures-and-tables
        ▼
fcr-reporting-and-data-policy
        ▼
fcr-writing-style            （润色）
        ▼
fcr-cover-letter
        ▼
fcr-review-process
        ▼
fcr-submission
        ▼
fcr-revision-and-rebuttal
```

`fcr-workflow` 是路由器——它先跑**范围关**（是否基于大田？是否多环境？是否大田作物？是否超越地方意义？），
再根据你所处阶段告诉你下一步用哪个技能。若范围关未过，它会在你动笔之前先把你送回
`fcr-topic-selection` 或 `fcr-experimental-design`。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `fcr-workflow` | 路由器——范围关 + 决定下一步调用哪个子技能 |
| `fcr-topic-selection` | 范围契合（基于大田、多环境、大田作物、普遍意义）；选定文类 |
| `fcr-literature-positioning` | 确立普遍意义的贡献；避免"地方性/描述性"被拒 |
| `fcr-experimental-design` | 多环境设计——随机化、重复、区组、G×E、建模 |
| `fcr-data-analysis` | 混合模型、G×E/稳定性、校正均值 + SED/LSD、模型评估 |
| `fcr-figures-and-tables` | 自洽图表，带单位与误差；响应曲线与双标图 |
| `fcr-reporting-and-data-policy` | 农学报告完整性；数据可得性声明；AI 声明 |
| `fcr-writing-style` | 结果简洁 + 讨论重在解释；摘要 ≤400 词；亮点 |
| `fcr-cover-letter` | 面向编辑、确立范围契合与创新贡献的投稿信 |
| `fcr-review-process` | 单向匿名评审、基于范围的桌面筛查、决定类别 |
| `fcr-submission` | Editorial Manager 投稿前检查（范围、格式、报告、声明） |
| `fcr-revision-and-rebuttal` | 面向多位评审 + 编辑的大/小修回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 农学数据源（GYGA / FAOSTAT / WorldClim / NASA POWER / SoilGrids）+ 设计、混合模型、G×E 与作物模型软件（agricolae / asreml / metan / APSIM / DSSAT / STICS）
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条期刊专属事实背后的 Elsevier / FCR 官方 URL 与投稿周 live-check 边界

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不冻结投稿周才应确认的元数据，例如编辑名单、价格、文件提示或文类菜单变化；投稿前以官方页面为准
- 不替你判断研究是否真正基于大田、是否具有普遍意义——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Field Crops Research（ScienceDirect）](https://www.sciencedirect.com/journal/field-crops-research) — 出版方主页、宗旨与范围
- [FCR 作者指南](https://www.sciencedirect.com/journal/field-crops-research/publish/guide-for-authors) — 投稿、文类、政策

---

## 许可

MIT
