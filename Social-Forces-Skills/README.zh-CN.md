# Social Forces 技能包

<p align="center">
  <img src="assets/cover.svg" alt="Social Forces 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Social%20Forces-2f6b58)](https://academic.oup.com/sf)
[![Field](https://img.shields.io/badge/field-社会学-1f6feb)](https://sociology.unc.edu/social-forces/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《社会力量》（Social Forces, SF）** 投稿的 Agent 技能栈。SF 创刊于 **1922 年**（由 Howard
Odum 创办），由 **牛津大学出版社（Oxford University Press）** 与 **北卡罗来纳大学教堂山分校（UNC）
社会学系** 合作出版。SF 自称 **"社会研究类期刊的全球领跑者"**，发表 **"面向一般社会科学读者的论文"**。
它以社会学为核心，但明确是多学科取向——社会分层与流动、人口学、比较历史社会学、社会心理学与宏观研究、
政治与经济社会学、社会网络、计算社会科学——并延伸至心理学、人类学、政治学、历史学与经济学。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把《美国社会学评论》（ASR）或
《美国社会学杂志》（AJS）技能包改个名字。三者同为综合性社会学旗舰，但 SF 自成一格：一本 **牛津大学
出版社** 的期刊，采用 **含参考文献在内的 10,000 词上限**、硬性的 **10 个表格与图面板** 展示限制、
**《芝加哥手册》第 17 版作者—年份** 体例、经 **ScholarOne Manuscript Central** 的 **双向匿名** 评审、
**50 美元投稿处理费**，并以 **方法严谨、理论扎根的经验研究** 著称，且面向广泛的社会科学读者。

---

## Social Forces 是什么，为何需要专属技能栈？

SF 的约束不同于领域刊、方法刊，也不同于它的社会学姊妹刊：

| 约束 | Social Forces | 含义 |
|------|---------------|------|
| 范围 | **一般社会科学**，以社会学为核心，多学科延伸 | 论文须对一般读者有意义，而非仅限子领域 |
| 看重 | **方法严谨** + 理论扎根、可迁移的贡献 | 窄结果或识别不足的结果不合适 |
| 方法 | 定量/人口学/比较历史/民族志/网络/计算——各按其标准评判 | 不要把同一模板硬套到所有论文 |
| 出版方 / 所有者 | **牛津大学出版社** / **UNC 教堂山**（社会学系） | 通过 **ScholarOne** 投稿，非 Sage Track 或 Editorial Manager |
| 评审模式 | **双向匿名**——匿名稿件 + **独立标题页** | 把姓名、单位、致谢、资助信息移出正文 |
| 费用 | **50 美元**不可退处理费（**学生独著**为 **20 美元**） | 须预算；区别于 ASR 的 25 美元、AJS 的 30 美元 |
| 篇幅 | **≤ 10,000 词，含正文、尾注与参考文献** | 参考文献计入——异常严格；须控制引用量 |
| 展示 | 表格与图面板合计 **≤ 10 个**；补充材料 **≤ 10 页** | 每个展示都要物有所值 |
| 体例 | 终稿用 **《芝加哥手册》第 17 版**（作者—年份） | **不是** ASA 体例，**也不是** AJS 自有体例 |
| 透明度 | **必须提供数据可得性声明**；在伦理可行时存放数据 | 是必备声明，而非编辑部复现核验 |

易变的具体信息（编辑与任期、确切上限、费用/APC、摘要长度、数据政策）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记 **待核实**。
**请以官方页面为准。**

### Social Forces vs. ASR vs. AJS 速览

- **Social Forces** — OUP / UNC；面向一般社会科学读者、重方法严谨；经 ScholarOne 双向匿名；
  **50 美元费**（学生 20）；**10,000 词含参考文献**；**≤ 10 个表/图面板**；**芝加哥第 17 版作者—年份**；
  必备数据可得性声明。
- **ASR** — SAGE / ASA；全学科旗舰；经 Sage Track 匿名（masked）；**25 美元费**；**约 15,000 词**
  （含参考文献，但上限更高）；**ASA 体例**；ASA 数据共享规范。
- **AJS** — 芝加哥大学出版社；重理论；双盲、学生主导分稿；**30 美元费**；**无固定词数上限**；
  **自有体例**；评论—回应（Comment-and-Reply）传统。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/sf-skills
/plugin install sf-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/sf-skills.git
cd sf-skills

mkdir -p ~/.claude/skills && cp -R skills/sf-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/sf-* ~/.codex/skills/
```

### 第一条提示

```
用 sf-workflow 告诉我，我的 Social Forces 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
sf-topic-selection
        ▼
sf-literature-positioning
        ▼
sf-theory-building
        ▼
sf-research-design
        ▼
sf-data-analysis
        ▼
sf-tables-figures
        ▼
sf-writing-style          （润色）
        ▼
sf-data-and-transparency
        ▼
sf-review-process
        ▼
sf-submission
        ▼
sf-rebuttal
```

`sf-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。由于 **10,000 词上限包含参考文献**、
展示限于 **10 个面板**，多数 SF 论文会在理论 ↔ 设计 ↔ 分析之间循环数次，并在投稿前于
`sf-writing-style` 与 `sf-tables-figures` 上下真功夫做删减。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `sf-workflow` | 路由器——决定下一步调用哪个子技能 |
| `sf-topic-selection` | 一般社会科学意义 + 严谨且可迁移的贡献 |
| `sf-literature-positioning` | 把贡献置于一般 SF 读者能识别的论争中 |
| `sf-theory-building` | 打造可迁移的理论论证，而非仅一个发现 |
| `sf-research-design` | 为设计辩护——定量、人口学、比较历史、民族志、网络 |
| `sf-data-analysis` | 跨 SF 方法范围的分析规范、不确定性、稳健性 |
| `sf-tables-figures` | 在硬性 **10 个表/图面板** 上限内做展示 |
| `sf-writing-style` | 芝加哥第 17 版作者—年份；在 **含参考文献的 10,000 词** 内完成 |
| `sf-data-and-transparency` | 必备 **数据可得性声明**；文档；受限数据路径 |
| `sf-review-process` | 双向匿名评审、决定类别、评审人看重什么 |
| `sf-submission` | ScholarOne 投稿前检查（50 美元费、标题页匿名化、词数 + 面板上限） |
| `sf-rebuttal` | 面向多位评审 + 编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 社会学数据源（GSS / PSID / IPUMS / LIS / Add Health / V-Dem）+ R / Stata / Python 与 CAQDAS/QCA 工具
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 Oxford Academic / UNC 官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑与任期、确切上限、费用/APC、摘要长度、数据政策）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的问题是否具有广泛的社会科学意义——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Social Forces（Oxford Academic）](https://academic.oup.com/sf) — 出版方主页、投稿说明、政策
- [UNC 上的 Social Forces](https://sociology.unc.edu/social-forces/) — 编辑部主页、社会学系

---

## 许可

MIT
