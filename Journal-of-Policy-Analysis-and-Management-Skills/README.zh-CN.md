# 政策分析与管理期刊技能包（JPAM Skills）

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Policy Analysis and Management 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JPAM-8a5a12)](https://onlinelibrary.wiley.com/journal/15206688)
[![Field](https://img.shields.io/badge/field-Public%20Policy-1f6feb)](https://www.appam.org/news/jpam/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《政策分析与管理期刊》（Journal of Policy Analysis and Management, JPAM）** 投稿的智能体技能栈。JPAM
是**公共政策分析协会（APPAM）**的**跨学科公共政策分析旗舰期刊**，创刊于 **1981 年**（由 *Policy Analysis*
与 *Public Policy* 合并而来），由 **Wiley** 出版。JPAM 横跨**经济学、政治学与公共管理学**，发表对各政策领域
（教育、健康、劳动与福利、住房、犯罪与司法、环境、移民、社会政策）中**政策与项目的严谨因果评估**，尤其看重
**可信的因果识别**与**把证据转化为清晰、不夸大的政策含义**。

本仓库立场鲜明：它**不是**通用社会科学写作工具箱，也**不是**把经济学技能包改头换面用于政策研究。它是
**JPAM 专属**技能栈：**可信识别的政策/项目效应**（RCT、DiD/事件研究、断点回归 RD、工具变量 IV、合成控制）、
**成本—收益与分配分析**、**不夸大的政策含义**、**双盲匿名**准备、**APPAM 会员资格或投稿费**门槛，以及可复现的
**已归档复制包**。

> **官方信息核验于 2026-06-20** —— 事实锚定于 APPAM 的 JPAM 页面、Wiley 期刊/作者入口、Wiley
> 2026 年 editor note 的检索呈现，以及 RePEc `wly:jpamgt` 记录。投稿入口与文件要求会变化，正式上传前
> 以 Wiley Research Exchange 的实时提示为准。

---

## JPAM 是什么，为何需要专属技能栈？

JPAM 的约束不同于经济学领域期刊或公共管理期刊：

| 约束 | JPAM | 含义 |
|------|------|------|
| 范围 | **跨学科政策分析**（经济学 + 政治学 + 公共管理） | 论文须面向跨领域的真实政策决策 |
| 核心看重 | 政策/项目效应的**可信因果识别** | 仅靠可观测变量控制通常达不到门槛 |
| 独特层次 | **成本—收益 + 分配分析**——谁受益、谁付费 | 仅有效应量不够，还要回答"是否值得做" |
| 写作风格 | **清晰、不夸大的政策含义** | 论断须与估计量匹配，并明示边界 |
| 出版方 / 所有者 | **Wiley** / **APPAM** | 经 Wiley Authors / **Research Exchange** 投稿 |
| 评审模式 | **双盲 / 匿名化预检** | 匿名化正文；准备单独标题页 |
| 投稿门槛 | **APPAM 会员资格 或 投稿费**（可申请减免） | 会员免费；非会员 **USD 100 专业 / USD 40 学生** |
| 透明度 | **归档数据 + 代码；数据可得性声明** | 对受限行政数据要尽早规划 |
| 独特栏目 | **Point/Counterpoint**（约稿，非同行评审）+ Policy Insights | 先选对文章类型 |

易变项会变动。来源图区分已经由 APPAM/Wiley 支撑的事实与上传时必须复核的 Research Exchange 实时提示。

### 文章类型

- **Feature Research Articles** —— 完整、可信识别的政策评估（核心格式）。
- **Methods for Policy Analysis** —— 面向政策分析者的方法学进展（同行评审）。
- **Policy Retrospectives** —— 对某政策或文献的回顾性反思。
- **Point/Counterpoint** —— **约稿、非同行评审**，就时事政策议题展开学术辩论。
- **Policy Insights** —— **约稿、非同行评审**，短文（≤ 3,000 词）快速回应。
- **Book Reviews** —— 约稿/编辑组稿。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jpam-skills
/plugin install jpam-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/jpam-skills.git
cd jpam-skills

mkdir -p ~/.claude/skills && cp -R skills/jpam-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jpam-* ~/.codex/skills/
```

### 第一句提示词

```
用 jpam-workflow 帮我判断：我的 JPAM 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
jpam-topic-selection
        ▼
jpam-literature-positioning
        ▼
jpam-theory-building
        ▼
jpam-research-design
        ▼
jpam-data-analysis
        ▼
jpam-tables-figures
        ▼
jpam-writing-style          (打磨)
        ▼
jpam-transparency-and-data
        ▼
jpam-review-process
        ▼
jpam-submission
        ▼
jpam-rebuttal
```

`jpam-workflow` 是路由器——它根据你所处阶段与适配的**文章类型**告诉你下一步用哪个技能。若拟投约稿类型
（Point/Counterpoint、Policy Insights），动笔前请先确认约稿与篇幅规则。

---

## 技能清单

| 技能 | 用途 |
|------|------|
| `jpam-workflow` | 路由器——决定下一步调用哪个子技能 |
| `jpam-topic-selection` | 判断政策相关性与可识别性的适配；选对文章类型 |
| `jpam-literature-positioning` | 在经济学 / 政治学 / 公共管理文献中定位贡献 |
| `jpam-theory-building` | 构建变革理论 / 逻辑模型、机制与适用条件 |
| `jpam-research-design` | 可信识别——RCT、DiD/事件研究、RD、IV、合成控制 |
| `jpam-data-analysis` | 估计 + 成本—收益 + 分配分析、稳健性、不确定性 |
| `jpam-tables-figures` | 决策可读的图表：效应、不确定性、设计有效性、分配 |
| `jpam-writing-style` | 清晰、不夸大的政策含义；跨学科可读性 |
| `jpam-transparency-and-data` | 复制包 + 数据可得性声明；受限数据路径 |
| `jpam-review-process` | 双盲评审、桌拒筛查、文章类型、决定类别 |
| `jpam-submission` | Research Exchange 投稿前检查（匿名化、会员/费用、ORCID、数据声明） |
| `jpam-rebuttal` | 面向"识别评审人"与"政策评审人"的修回回复 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 政策评估数据源（CPS / SIPP / NCES / CMS / UCR / HUD / ACS）+ R / Stata / Python 与成本—收益 / MVPF 工具
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的 Wiley / APPAM 官方链接与实时复核守则
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— JPAM 风格引言"修改前→修改后"示例（虚构、示意）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 经网络核验的真实 JPAM 论文，按领域 × 方法编排，并附姊妹期刊防混淆清单
- [`resources/code/`](resources/code/) —— 内置 Stata + Python 因果推断脚手架（DiD / IV / RD / DML）

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定主编或评审人的口味
- 不把易变元数据写死为永久规则；正式上传前请复核 Research Exchange 的实时提示
- 不替你判断选题是否具有政策相关性、设计是否可信——这是研究者的责任

---

## 与姊妹期刊的差异

| 期刊 | 它是什么 | JPAM 的差异 |
|------|----------|-------------|
| **AEJ: Economic Policy** / **J. of Public Economics** | 经济学**领域**政策期刊 | JPAM 跨学科，突出政策决策 + 成本—收益 + 分配，而非仅经济学 |
| **Public Administration Review** / **JPART** | 公共管理 / 行政学期刊 | JPAM 以可信识别的**项目效应**为中心，而非管理理论 |
| **APSR / AJPS** | 政治学综合/领域期刊 | JPAM 的门槛是政策评估与决策相关性，而非学科理论贡献 |
| **JPAM** | **APPAM 的跨学科政策分析旗舰** | 可信识别**加上**面向经济/政治/公管混合读者的、经校准的政策含义 |

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专属技能包索引
- [JPAM（Wiley Online Library）](https://onlinelibrary.wiley.com/journal/15206688) —— 出版方主页
- [JPAM（APPAM）](https://www.appam.org/news/jpam/) —— 所有者、作者指南、文章类型与费用

---

## 许可证

MIT
