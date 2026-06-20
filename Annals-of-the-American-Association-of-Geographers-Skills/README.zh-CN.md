# 美国地理学家协会会刊（Annals of the AAG）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Annals of the AAG 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Annals%20of%20the%20AAG-1f6a4a)](https://www.tandfonline.com/journals/raag21)
[![Field](https://img.shields.io/badge/field-Geography-1f6feb)](https://www.aag.org/journal/annals-of-the-aag/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《美国地理学家协会会刊》（Annals of the American Association of Geographers，简称 Annals of the
AAG）** 投稿的智能体技能包。该刊是**地理学的旗舰期刊**，创刊于 **1911 年**（原名 *Annals of the
Association of American Geographers*），由 **Taylor & Francis（Routledge）** 代表 **美国地理学家协会
（AAG）** 出版。会刊发表覆盖**整个地理学科**的最优秀成果，按**四大领域**外加一个跨学科方向组织：
**地理方法（Geographic Methods，含 GIScience、空间分析、建模）**、**人文地理（Human Geography）**、
**自然与社会（Nature and Society）**，以及 **自然地理、地球与环境科学（Physical Geography, Earth, and
Environmental Sciences）**——定量/空间、GIScience、遥感、定性与混合方法均在其列。

本仓库立场鲜明：它**不是**通用社科写作工具箱，也**不是**把经济学包或 GIS 软件手册套用到地理学。它是
**针对 Annals 的专用技能栈**：研究问题须以**空间、地方、尺度为核心载体**；论证须扎根于**地理学理论**并能
跨四大领域对话；研究设计须**按各自传统自证**（空间自相关、MAUP/尺度、验证、立场性）；**地图须达到制图学
标准**；采用**双向匿名**准备；并诚实处理**空间数据来源与地理隐私**。

---

## Annals 是什么？为何需要专用技能栈？

会刊的约束不同于地理学专门期刊或方法期刊：

| 约束维度       | Annals of the AAG                                                          | 含义                                                   |
|----------------|---------------------------------------------------------------------------|--------------------------------------------------------|
| 范围           | **整个学科**，按**四大领域** + 综合地理组织                                | 论文须跨领域有意义，而非局限于某一子领域               |
| 看重           | **地理学意义**（空间/地方/尺度为载体）+ 地理学理论                         | “带张地图的领域研究”属于错位投稿                       |
| 方法           | 空间定量、GIScience、遥感、定性、混合——各按其传统评判                      | 不要把单一模板套到所有论文上                           |
| 出版方 / 所有者 | **Taylor & Francis（Routledge）** / **AAG**                                | 经 **ScholarOne Manuscripts** 投稿                     |
| 评审模式       | **双向匿名**；1–3 名审稿人（其中一人为编辑或其指定人）                     | 匿名化正文与研究地点细节                               |
| 编辑           | **每个领域设主题编辑** + 综合 + **制图编辑（Cartography Editor）**；任期四年 | 须声明领域，它决定编辑与评判标准                       |
| 篇幅           | **正刊文章 ≤ 11,000 词，*含* 摘要、参考文献、注释、表格、图注**            | 须为整篇预算字数，而非仅正文                           |
| 其他体例       | **论坛（Forum，总计 ≤ 25,000 词）** 与 **评论（Commentary，< 2,000 词）** | 须提前选定体例                                         |
| 文体           | **《芝加哥手册》**（作者-年份制）；3–5 个斜体关键词                        | 非通用文体；关键词须斜体并按字母排序                   |
| 图表           | **地图须达到制图学标准**（投影、分级、图例）                              | 设制图编辑审阅；图表计入字数上限                       |
| 透明度         | 空间数据**来源 + 地理隐私**；遵循 T&F 数据政策                            | 记录来源/坐标系/处理流程；对敏感位置做掩蔽             |

易变信息（编辑及任期、确切字数上限、摘要长度、费用/APC、数据政策措辞）会变化——未直接核实的条目在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记为 **待核实**。
**官方信息核对于 2026-06。请以官网为准。**

### 四大领域（须声明其一）

- **地理方法** —— GIScience、空间分析、建模、地理计算。
- **人文地理** —— 社会/文化/经济/政治/城市地理，常为定性研究。
- **自然与社会** —— 人-环境耦合系统、政治生态学、灾害、土地变化。
- **自然地理、地球与环境科学** —— 地貌学、生物地理学、气候学、环境遥感。
- **综合地理（跨学科）** —— 跨越多领域的贡献。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/annals-aag-skills
/plugin install annals-aag-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/annals-aag-skills.git
cd annals-aag-skills

mkdir -p ~/.claude/skills && cp -R skills/aaag-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/aaag-* ~/.codex/skills/
```

### 第一条提示词

```
使用 aaag-workflow 告诉我，我的 Annals of the AAG 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
aaag-topic-selection
        ▼
aaag-literature-positioning
        ▼
aaag-theory-building
        ▼
aaag-research-design
        ▼
aaag-data-analysis
        ▼
aaag-tables-figures
        ▼
aaag-writing-style          （打磨）
        ▼
aaag-transparency-and-data
        ▼
aaag-review-process
        ▼
aaag-submission
        ▼
aaag-rebuttal
```

`aaag-workflow` 是路由器——它根据你所处阶段以及论文所属的**四大领域**，告诉你下一步用哪个技能。多数论文
在进入 writing-style 之前会在 理论 ↔ 设计 ↔ 分析 之间往返多次。

---

## 技能清单

| 技能                             | 用途                                                                          |
|----------------------------------|-------------------------------------------------------------------------------|
| `aaag-workflow`                  | 路由器——决定下一步调用哪个子技能；选定领域与体例                              |
| `aaag-topic-selection`           | 地理学意义匹配 + 领域声明（方法/人文/自然与社会/自然地理/综合）               |
| `aaag-literature-positioning`    | 进入跨领域、跨学科的地理学对话                                                |
| `aaag-theory-building`           | 构建可迁移的地理学论证（地方、尺度、时空、自然-社会）                         |
| `aaag-research-design`           | 自证设计——空间/定量与 GIS、遥感/自然地理、定性、混合                         |
| `aaag-data-analysis`             | 空间诚实的分析（自相关、MAUP、验证）、不确定性、稳健性                        |
| `aaag-tables-figures`            | 达制图学标准的地图；图表控制在含图注字数上限内                                |
| `aaag-writing-style`            | 芝加哥作者-年份制；11,000 词含全部上限；斜体关键词；读起来像地理学            |
| `aaag-transparency-and-data`     | 空间数据来源、可复现性，以及地理隐私 / 人类受试者伦理                         |
| `aaag-review-process`            | 按领域双向匿名评审；决定类别；初审退稿触发点                                  |
| `aaag-submission`                | ScholarOne 投稿前检查（领域/体例、匿名化、字数、关键词、ORCID）               |
| `aaag-rebuttal`                  | 面向主题编辑 + 1–3 名跨领域审稿人的修回回复                                   |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 地理数据源（Census/IPUMS/OSM/Landsat/Sentinel/DEM/GBIF）+ GIS / 空间统计 / 遥感 / 定性工具
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的 AAG / Taylor & Francis 官方链接，未核实项标 待核实
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 经网络核实的真实 Annals 论文，按 领域 × 方法 组织，附姊妹刊防混淆清单
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— Annals 文体的引言前后对照（虚构、示范用）

---

## 与姊妹期刊的区别

| 期刊 | 定位 | 何时改用本技能包 |
|------|------|------------------|
| **Annals of the AAG** | AAG **四大领域综合旗舰**，原创研究 | ……你的地理性是核心载体且跨领域可达 |
| *Progress in Human Geography* | 综述/议程文章 | ……你写的是原创实证而非综述 |
| *Geographical Analysis* | 形式化空间分析方法 | ……你的方法贡献比 GA 更宽泛/更应用 |
| *IJGIS* | GIScience 方法/算法 | ……主导的是地理问题而非算法 |
| *The Professional Geographer* / *Transactions of the IBG* | AAG 短篇报告 / 英国旗舰 | ……你想投 AAG 的综合长文旗舰 |

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或审稿人的口味
- 不断言易变元数据（现任编辑及任期、确切字数上限、费用/APC、政策措辞）——请以官网为准；未核实项标 待核实
- 不替你判定地理性是否为核心载体、该归哪个领域——这是研究者的判断

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Annals of the AAG（Taylor & Francis Online）](https://www.tandfonline.com/journals/raag21) —— 出版方主页
- [AAG 的 Annals 页面](https://www.aag.org/journal/annals-of-the-aag/) —— 所有者、领域、作者指南

---

## 许可证

MIT
