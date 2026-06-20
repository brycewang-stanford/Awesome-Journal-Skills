# 美国经济学杂志：微观经济学 技能包

<p align="center">
  <img src="assets/cover.svg" alt="AEJ: Microeconomics 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AEJ%3A%20Micro-3a2b6b)](https://www.aeaweb.org/journals/mic)
[![Field](https://img.shields.io/badge/field-Microeconomic%20Theory-1f6feb)](https://www.aeaweb.org/journals/mic)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向投稿 **《美国经济学杂志：微观经济学》（American Economic Journal: Microeconomics，AEJ: Micro）** 的
十二个智能体技能。AEJ: Micro 是 **美国经济学会（AEA）** 的季刊（创刊于 2009 年，AEA 四本领域期刊之一），
聚焦 **微观经济理论及其应用**（印刷版 ISSN 1945-7669 / 电子版 ISSN 1945-7685），通过 AEA 投稿系统提交。

本仓库立场鲜明，且 **以理论为先**。AEJ: Micro “既发表理论工作，也发表带有理论框架的实证与实验工作”，
其录用标准是一个 **干净、一般、动机充分、具有广泛吸引力的微观理论结果**——博弈论、机制与市场设计、
产业组织理论、契约理论、信息经济学、决策与行为理论，以及以理论为基础的实验。**核心技能是
`aejmic-theory-model`**（模型设定、均衡概念、证明策略、一般性与可处理性的取舍）。实证、结构与实验工作
**只有在理论是重点时** 才属于本刊。

官方依据核对于 2026-06：aeaweb.org 上的 AEJ: Micro 期刊主页、编辑名单、投稿指南与编辑政策，以及
AEA 数据与代码可得性政策 / AEA 数据编辑办公室。参见
[`resources/official-source-map.md`](resources/official-source-map.md)。

---

## 为什么需要独立的 AEJ: Micro 技能栈？

AEJ: Micro 的约束与实证旗舰期刊、专业理论期刊都有实质差异：

| 约束             | AEJ: Micro                                            | 含义                                                       |
|------------------|-------------------------------------------------------|------------------------------------------------------------|
| 核心交付物       | 一个 **干净、广受关注的定理 / 刻画**                   | 没有核心理论结果的回归系数不符合定位                       |
| 范围门槛         | 理论为先；实证/实验需 **带理论框架**                   | 纯实证应用微观应投 **AEJ: Applied**                        |
| 受众             | **广泛** 的微观兴趣 + **AEA 流程**                     | 追求极致一般性、仅面向小圈子的工作更适合 **JET / GEB**     |
| “识别”           | 哪个 **假设在起作用**；结果为何紧致                     | 纯理论没有因果设计——可信度来自证明本身                     |
| 行文风格         | 带编号的命题；**证明置于附录**；数值算例                | 叙述式实证排版会显得不合模板                                |
| 统计呈现         | **标准误 / 置信集，而非显著性星号**                     | 星号表是 AEA 行文风格的反模式                              |
| 评审             | **单盲**（审稿人知道作者；审稿人对作者匿名）            | 无需匿名化——论文靠严谨而非匿名取胜                         |
| 摘要             | **不超过 100 词**                                      | 摘要过长会通不过格式检查                                    |
| 数据 / 复现      | **AEA 数据与代码可得性政策**（AEA 数据编辑；openICPSR）| 实证/模拟/实验工作在 **录用前** 验证；理论需提交数值算例代码 |

易变细节——**当前投稿费**、**JEL 要求的确切措辞**、**创刊年份表述**——已尽可能核对于 2026-06，否则标注
**待核实**。参见 [`resources/official-source-map.md`](resources/official-source-map.md)。

> **投稿费与版面费勿混淆：** AEJ: Micro 收取 **投稿费**（AEA 会员按国家收入 $200 / $100 / $0，非会员更高
> ——易变），并 *另外* 在校样阶段按 **每排版页 $15** 收取版面费。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/aej-microeconomics-skills
/plugin install aej-microeconomics-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/aej-microeconomics-skills.git
cd aej-microeconomics-skills

mkdir -p ~/.claude/skills && cp -R skills/aejmic-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/aejmic-* ~/.codex/skills/
```

### 第一条指令

```
用 aejmic-workflow 告诉我，我的 AEJ: Micro 理论论文下一步该用哪个技能。
```

---

## 默认工作流

```text
aejmic-topic-selection         （是否属于广受关注的微观理论？非 JET/GEB/TE/AEJ:Applied）
        ▼
aejmic-literature-positioning  （相对最接近结果的“定理级”增量）
        ▼
aejmic-theory-model            ★ 核心：模型、均衡概念、证明策略
        ▼
aejmic-identification          （哪个假设在起作用 / 数据识别了什么）
        ▼
aejmic-robustness              （扩展、边界情形、实证稳健性）
        ▼
aejmic-tables-figures          （命题、数值算例、实验表格）
        ▼
aejmic-writing-style           （理论论文引言弧线；最后润色）
        ▼
aejmic-replication-package     （证明附录 + 数值/结构/实验代码）
        ▼
aejmic-referee-strategy        （预判理论审稿人会提的反对意见）
        ▼
aejmic-submission              （AEA 系统投稿前检查：单盲、100 词摘要、费用）
        ▼
aejmic-rebuttal                （单盲 R&R 回复信）
```

`aejmic-workflow` 是路由器——它会根据你所处阶段告诉你下一步用哪个技能。

---

## 技能列表

| 技能                            | 用途                                                                       |
|---------------------------------|----------------------------------------------------------------------------|
| `aejmic-workflow`               | 路由器——决定下一步调用哪个子技能                                            |
| `aejmic-topic-selection`        | 理论为先、广泛兴趣的范围门槛（区分 JET/GEB、TE/Econometrica、AEJ:Applied）   |
| `aejmic-literature-positioning` | 相对最接近结果的“定理级”增量                                                |
| `aejmic-identification`         | 结果为何紧致（理论）/ 数据识别了什么（结构/实验）                           |
| `aejmic-theory-model`           | **核心**——模型设定、均衡概念、证明策略、一般性取舍                          |
| `aejmic-robustness`             | 扩展、边界情形、扰动；实证/实验稳健性                                       |
| `aejmic-tables-figures`         | 命题、数值算例、示意图、实证表格                                            |
| `aejmic-writing-style`          | AEA 行文风格与理论论文引言弧线                                              |
| `aejmic-replication-package`    | 证明附录 + AEA 数据编辑的代码/数据存档（含数值算例）                        |
| `aejmic-referee-strategy`       | 预判专家审稿人的反对意见；理解单盲流程                                      |
| `aejmic-submission`             | AEA 系统投稿前检查（单盲、100 词摘要、JEL、费用、数据政策）                  |
| `aejmic-rebuttal`               | R&R 回复策略（正确性 / 一般性 / 表述）                                      |

### 资源

- [`resources/README.md`](resources/README.md) —— 能力层索引；理论与实证子集的分工
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的官方 AEA / AEJ: Micro 链接，含 `待核实` 标注
- [`resources/external_tools.md`](resources/external_tools.md) —— LaTeX/证明工具链，以及结构/实证/实验工具
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 按领域分类、经网络核验的真实 AEJ: Micro 论文（`10.1257/mic` DOI 前缀）
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— AEJ: Micro 风格理论论文引言“前后对比”
- [`resources/code/`](resources/code/) —— 仅适用于实证/结构子集的 Stata/Python 可运行骨架

---

## 与其他技能栈的差异

| 维度           | AEJ: Micro                          | JET / GEB（专业理论）         | AEJ: Applied（实证）        |
|----------------|-------------------------------------|-------------------------------|-----------------------------|
| 以什么开篇     | 一个广受关注的定理                  | 一般/技术性的理论进展         | 一个因果实证发现            |
| “识别”         | 哪个假设在起作用                    | 假设 + 极致一般性             | 设计（RCT/DID/IV/RDD）      |
| 受众 / 流程    | 广泛微观 + AEA 编辑流程             | 专业理论圈                    | 应用微观 + AEA 流程         |
| 评审           | **单盲**                            | 各刊单/双盲不一               | 单盲                        |
| 数据 / 复现    | AEA 数据编辑；openICPSR             | 鼓励，因刊而异                | AEA 数据编辑；openICPSR     |
| 行文风格       | 带编号命题；标准误而非星号          | 定理-证明，出版社 LaTeX       | 作者-年份；标准误而非星号   |

---

## 本仓库不做什么

- 不替你写出可投稿的证明或稿件
- 不检验你的定理是否正确——那是作者与审稿人的职责
- 不断言易变元数据（当前费用、JEL 确切措辞、创刊年份）——这些标注为 `待核实` 或注明 2026-06；请到官方页面核实
- 不评判你的贡献是否真正原创或具有广泛吸引力——那是研究者自己的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专属技能包索引
- [AEJ: Microeconomics（官方）](https://www.aeaweb.org/journals/mic) —— 美国经济学会

---

## 许可证

MIT —— Copyright (c) 2026 Bryce Wang。参见 [LICENSE](LICENSE)。
