# Accounting, Organizations and Society (AOS) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Accounting, Organizations and Society 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AOS-29434e)](https://www.sciencedirect.com/journal/accounting-organizations-and-society)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20ABDC%20A*-1f6feb)](https://www.sciencedirect.com/journal/accounting-organizations-and-society)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Accounting, Organizations and Society (AOS)** 投稿的 Agent 技能栈 —— AOS 是跨学科会计研究的旗舰期刊，由 **Anthony Hopwood** 于 **1976 年**创办，**Elsevier** 出版（ISSN 0361-3682）。

本仓库是有立场的。它**不是**通用的"会计写作"工具箱，更不是资本市场研究的技能栈。AOS 的使命是研究会计的**社会、组织、行为与制度**面向：定性田野研究、实验/行为会计、问卷调查、历史与批判研究，以及真正承载社会理论的档案研究。该刊最典型的直接拒稿类型，就是没有任何组织/社会理论化的 JAR/JAE/TAR 式档案—金融经济学论文 —— 因此本技能栈以理论为先，按思想传统导航（制度理论、治理术/福柯、布迪厄、行动者网络理论、实践理论、心理过程理论），并内置该刊亲手立下的定性研究严谨性标准（Ahrens & Chapman 2006）。

> 仅描述持久规范。主编、投稿系统行为、文章类型与开放获取定价都会变化 —— 请务必以 ScienceDirect/Elsevier 官方页面及 Editorial Manager 为准（本包事实核查于 2026-07-16）。

---

## 为什么需要单独的 AOS 技能栈？

AOS 的约束与美国档案派会计期刊、乃至管理学期刊都存在**性质上**的差异：

| 约束维度       | Accounting, Organizations and Society (AOS)                    | 含义                                                      |
|----------------|----------------------------------------------------------------|-----------------------------------------------------------|
| 期刊使命       | 会计的社会、组织、行为与制度面向                                | 无社会理论化的资本市场论文会被直接拒稿                     |
| 方法立场       | 多元：田野研究、实验、问卷、历史研究、档案+理论                | 建议必须按传统分支，且各传统的标准互不相同                 |
| 理论           | 理论为先：概念性主张就是论文的产品                              | 制度理论／福柯／布迪厄／ANT／实践理论／JDM 必须真正发挥作用 |
| 学术脉络       | 期刊自身 50 年的经典文库定义了对话                              | 定位须对准 AOS 自己的脉络，而非 JAR/TAR 的争论              |
| 主编           | 三位联合主编横跨各传统（Annisette / Messner / Tan）             | 分诊按传统进行；要为可能力挺你的主编写作                    |
| 评审           | 双向匿名、跨学科审稿人                                          | 同一篇论文可能同时由社会学读者与 JDM 读者评审               |
| 篇幅           | 未公布固定字数上限；长篇阐释性论文属常态                        | 自由即纪律 —— 每一页都必须承重                              |
| 费用           | 未发现投稿费（请复核）；可选混合 OA，APC 按作者情境个性化定价    | 仅在选择金色 OA 时需预算；投稿系统内确认 APC                 |
| 田野数据透明度 | 知情同意与田野匿名限制共享                                      | 精确披露语料规模；绝不夸大可共享性                          |

通用的"科研写作"或单一传统的方法技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/aos-skills
/plugin install aos-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/aos-skills.git
cd aos-skills

mkdir -p ~/.claude/skills && cp -R skills/aos-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/aos-* ~/.codex/skills/
```

### 第一条指令

```
用 aos-workflow 告诉我，我这篇 AOS 稿子下一步该用哪个 skill。
```

---

## 默认工作流

```text
aos-topic-selection（选题与契合度）
        ▼
aos-theory-development（理论透镜）
        ▼
aos-literature-positioning（文献定位）
        ▼
aos-methods（研究设计与伦理）
        ▼
aos-data-analysis（编码／分析／估计）
        ▼
aos-contribution-framing（概念性贡献）
        ▼
aos-tables-figures（图表与证据表）
        ▼
aos-writing-style（文风打磨）
        ▼
aos-submission（投稿前自检）
        ▼
aos-review-process（理解评审流程）
        ▼
aos-rebuttal（R&R 答复）
```

`aos-workflow` 是路由器 —— 它根据你所处阶段、以及论文所属的思想传统（定性田野／实验行为／问卷／历史批判／档案+理论）告诉你下一步用哪个 skill。

---

## 技能列表

| Skill                        | 用途                                                                     |
|------------------------------|--------------------------------------------------------------------------|
| `aos-workflow`               | 路由器 —— 按思想传统决定下一步调用哪个子技能                              |
| `aos-topic-selection`        | 与 AOS 社会/组织使命的契合度；"没有证券价格"测试                          |
| `aos-theory-development`     | 选定并真正驾驭一个理论传统（制度／福柯／布迪厄／ANT／实践／JDM）           |
| `aos-literature-positioning` | 进入 AOS 自身 50 年的学术对话；诚实引用跨学科一手文献                      |
| `aos-methods`                | 田野研究、实验、问卷与历史研究设计；伦理与田野匿名                         |
| `aos-data-analysis`          | 定性编码与证据链；实验/问卷估计；分析留痕                                  |
| `aos-contribution-framing`   | 改变对话的概念性主张 —— 并向所借理论"反哺"                                 |
| `aos-tables-figures`         | 数据清单表与证据表、单元均值表、承载理论的图                               |
| `aos-writing-style`          | 论证式长文写作；无上限下的篇幅纪律；匿名化                                 |
| `aos-submission`             | Editorial Manager 投稿前自检（匿名文件、标题页、各项声明、OA 决策）        |
| `aos-review-process`         | 联合主编分诊、跨学科审稿人、解读决定信                                     |
| `aos-rebuttal`               | R&R 修改方案 —— 重新编码、新实验条件、重建理论 —— 与逐条答复信              |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 按传统组织的工具箱（NVivo/ATLAS.ti 与证据登记表；Qualtrics/Prolific/oTree；问卷心理测量；Stata/R 档案研究栈）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 本技能包每条已核实事实背后的 Elsevier/ScienceDirect 官方链接（核查于 2026-07-16）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 按传统 × 主题组织的 AOS 经典文库，每篇附自检问题
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— AOS 风格引言的前后对照改写（虚构田野研究）

---

## 与 JAR / JAE / TAR / CAR 的差异

| 维度       | AOS                                      | JAR / JAE                    | TAR                | CAR                        |
|------------|-------------------------------------------|-------------------------------|---------------------|-----------------------------|
| 出版方     | Elsevier（Hopwood 1976 年创办）           | 芝加哥 Booth–Wiley / Elsevier | 美国会计学会        | CAAA / Wiley                |
| 核心问题   | 会计的社会与组织运作                      | 市场与契约中的会计            | 宽口径、偏档案      | 不绑定方法的会计研究        |
| 理论基础   | 社会学、组织理论、心理学                  | 金融经济学                    | 经济学/心理学混合   | 经济学 + 心理学             |
| 主流方法   | 定性田野研究；实验                        | 档案                          | 档案                | 档案为主、大帐篷            |
| 致命错配   | 无社会理论化的资本市场论文                | 阐释性田野研究                | ——                  | 披着会计外衣的纯金融        |

如果论文的落点是定价或盈余质量系数，AOS 就是错误的目标；如果落点是改变我们对会计在组织与社会中**做什么**的理解，那么没有比它更对的目标。

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Contemporary-Accounting-Research-Skills](https://github.com/brycewang-stanford) —— CAR 技能包（不绑定方法的姊妹刊）

---

## 许可证

MIT
