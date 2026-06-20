# 美国教育研究杂志（AERJ）技能包

<p align="center">
  <img src="assets/cover.svg" alt="American Educational Research Journal 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AERJ-a85d1b)](https://journals.sagepub.com/home/aer)
[![Field](https://img.shields.io/badge/field-教育研究-1f6feb)](https://www.aera.net/Publications/Journals/American-Educational-Research-Journal)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《美国教育研究杂志》（American Educational Research Journal, AERJ）** 投稿的 Agent 技能栈。AERJ 是
**美国教育研究协会（AERA）的旗舰期刊**，创刊于 **1964 年**，由 **SAGE** 出版。它发表覆盖
**整个教育研究领域** 的同行评审原创研究——跨越所有子领域、各级教育与人的全生命周期、各种学习形式——
**定量、定性与混合方法** 兼收并蓄。

AERJ 在结构上的独特之处在于：它是**整合后的全领域旗舰期刊**。AERJ 曾有 SIA/TLHD 两个板块，
但 AERA 已在 2015 年对新稿件启用整合后的 AERJ。现行投稿不应按旧板块路由，而应说明问题为何能
跨教育研究领域产生意义，不论主导视角是政策/制度、教学/学习、人的发展，还是跨领域设计。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把经济学或心理学包改个名字套到教育学。
它是 **AERJ 专属** 技能栈：一个对**整个教育研究领域都有广泛意义**的问题、面向**整合后的 AERJ 读者**、一个锚定在
**概念或理论框架**上的论证、一个能在**各自方法论标准**下站得住的研究设计（定量/定性/混合）、按 **APA 第 7 版**
体例完成的**匿名（masked）**稿件准备，以及符合 **AERA 实证社会科学研究报告标准** 的报告规范。

---

## AERJ 是什么，为何需要专属技能栈？

AERJ 的约束不同于窄领域专刊或方法刊：

| 约束 | AERJ | 含义 |
|------|------|------|
| 范围 | **整个教育研究领域**，各级教育与各类方法 | 论文必须超越单一子领域才有意义 |
| 结构 | **整合后的全领域期刊**（旧 SIA/TLHD 新稿件分流已于 2015 年结束） | 清楚说明主导教育研究视角 |
| 看重 | **广泛意义** + 清晰的概念/理论框架 | 仅做窄范围描述的结果不合适 |
| 方法 | 定量/定性/混合——各按其标准评判 | 不要把同一模板硬套到所有论文 |
| 出版方 / 所有者 | **SAGE** / **AERA** | 通过 **ScholarOne Manuscript Central** 投稿 |
| 评审模式 | **匿名（masked）** | 稿件须匿名化，作者姓名仅出现在题名页文件 |
| 费用 | 官方说明**投稿与发表不收费**；SAGE Choice 金色开放获取需付费 | 不要预算投稿费；开放获取费用以官网为准 |
| 篇幅 | 稿件 **最多 50 页**（双倍行距、12 号字、1 英寸页边距，含所有内容） | 篇幅须含表、图、注释、参考文献 |
| 摘要 | **100–120 词** | 紧凑、结构化的摘要 |
| 体例 | **APA 第 7 版**（作者—年份） | 非 Chicago/自定体例；通讯作者须 ORCID |
| 报告标准 | **AERA 报告标准**（实证社会科学；另有人文取向配套标准） | 按与你方法相符的标准来报告 |

易变的具体信息（编辑名单、SAGE Choice 费用、投稿门户行为、政策措辞）会变化。正式上传前请以
SAGE/AERA 官方页面为准。

### 契合视角

- **政策 / 制度 / 组织**：治理、公平、系统、资源与教育组织。
- **教学 / 学习 / 人的发展**：教学、课程、学习过程、认知、动机与发展。
- **跨领域研究**：明确主导视角，同时说明贡献如何超越单一子领域。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/aerj-skills
/plugin install aerj-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/aerj-skills.git
cd aerj-skills

mkdir -p ~/.claude/skills && cp -R skills/aerj-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/aerj-* ~/.codex/skills/
```

### 第一条提示

```
用 aerj-workflow 告诉我，我的 AERJ 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
aerj-topic-selection         （全领域契合）
        ▼
aerj-literature-positioning
        ▼
aerj-theory-and-framework
        ▼
aerj-research-design         （定量 / 定性 / 混合）
        ▼
aerj-data-analysis
        ▼
aerj-tables-figures
        ▼
aerj-writing-style           （润色）
        ▼
aerj-transparency-and-data-policy
        ▼
aerj-review-process
        ▼
aerj-submission
        ▼
aerj-rebuttal
```

`aerj-workflow` 是路由器——根据你所处阶段，以及主导教育研究视角和全领域贡献是否清楚，告诉你下一步用哪个技能。
若设计是**前瞻性**的，尽早走 `aerj-research-design` 考虑**预注册**；若贡献偏概念或方法，则倚重
`aerj-theory-and-framework` 与 `aerj-literature-positioning`。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `aerj-workflow` | 路由器——决定下一步调用哪个子技能；提示 AERJ 契合 |
| `aerj-topic-selection` | 跨全领域的广泛意义契合；明确主导教育研究视角 |
| `aerj-literature-positioning` | 跨越子领域对话；回应 AERJ 读者期待的文献 |
| `aerj-theory-and-framework` | 打造统领贡献的概念/理论框架 |
| `aerj-research-design` | 为设计辩护——教育中的定量、定性或混合方法 |
| `aerj-data-analysis` | 分析规范（多层、IRT、定性编码）、不确定性、稳健性 |
| `aerj-tables-figures` | APA 第 7 版格式下可读、自洽的图表 |
| `aerj-writing-style` | APA 第 7 版；在篇幅上限内触达整个领域 |
| `aerj-transparency-and-data-policy` | AERA 报告标准；数据可得性；定性透明度 |
| `aerj-review-process` | 匿名评审、桌面筛查、全领域契合、决定类别 |
| `aerj-submission` | ScholarOne 投稿前检查（匿名化、篇幅、摘要、APA、ORCID、题名页） |
| `aerj-rebuttal` | 面向多位评审 + 处理编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 教育研究数据源（NCES / ECLS / NAEP / SEDA / PISA / TIMSS / 州级 SLDS / QDR）+ R / Stata / Mplus / HLM 与定性/CAQDAS 工具
- [`resources/official-source-map.md`](resources/official-source-map.md) — 当前流程事实背后的 AERA / SAGE 官方 URL

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不把易变元数据（现任编辑、SAGE Choice 费用、投稿门户行为、政策措辞）当作永久事实——请以官方页面为准
- 不替你判断你的问题是否对教育研究有广泛意义——那是研究者的判断
- 不替你选择旧板块——它帮你面向整合后的 AERJ 框定主导教育研究视角

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [American Educational Research Journal（SAGE Journals）](https://journals.sagepub.com/home/aer) — 出版方主页
- [AERA 上的 AERJ](https://www.aera.net/Publications/Journals/American-Educational-Research-Journal) — 所有者、编辑、政策

---

## 许可

MIT
