# American Anthropologist 技能包

<p align="center">
  <img src="assets/cover.svg" alt="American Anthropologist 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-American%20Anthropologist-7a4a1a)](https://anthrosource.onlinelibrary.wiley.com/journal/15481433)
[![Field](https://img.shields.io/badge/field-Anthropology-1f6feb)](https://www.americananthro.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **American Anthropologist（AA，《美国人类学家》）** 投稿的智能体技能包。AA 是 **美国人类学会
（AAA）的旗舰四领域期刊**，创刊于 **1888 年**，由 **Wiley** 出版。AA 发表横跨**整个人类学**的优秀
学术成果：**社会文化人类学、考古学、生物／体质人类学、语言人类学**，以及**反身性与公共人类学**。该刊
以**民族志与质性研究**为主，但同样发表材料／考古以及定量的生物人类学工作，并在**理论、反身性、伦理与
写作**方面尤为突出。

本仓库立场鲜明。它**不是**通用社会科学写作工具箱，也**不是**把计量经济学包套用到人类学上。它是一套
**AA 专属**的技能栈：具备**四领域意义**的贡献、能**超越本子领域**对话的论证、将**民族志与质性推断视为
一等公民**、把**反身性与立场性（positionality）**讲清楚、按**匿名评审**准备稿件，并把**研究伦理与
问责**置于核心——知情同意、匿名化、对脆弱社群的保护，以及遗产／文物归还（repatriation）义务，遵循
AAA《职业责任准则》（Principles of Professional Responsibility）与一种**关怀伦理（ethics of care）**。

---

## AA 是什么，为何需要专属技能栈？

AA 的约束不同于单一子领域期刊或定量社会科学期刊：

| 约束维度        | American Anthropologist                                              | 含义                                                |
|-----------------|---------------------------------------------------------------------|-----------------------------------------------------|
| 范围            | 人类学**四大领域** + 反身性／公共人类学                              | 论文须超越本子领域产生意义                          |
| 看重            | **四领域意义** + 可迁移的概念，并带反身性                            | 仅限本子领域的描述性研究不契合                      |
| 方法            | **民族志／质性为一等公民**；亦含材料、实验室、计算方法               | 不要把民族志硬塞进假设检验模板                      |
| 出版方／所有方  | **Wiley** ／ **AAA**                                                | 经 **Research Exchange** 平台投稿（2025 年 4 月起） |
| 评审模式        | **匿名**同行评审，秉持**关怀伦理**                                  | 正文**与文件名**均匿名；单独提供标题页              |
| 费用            | **无投稿费与发表费**                                                | 不要预算费用（仅选开放获取时有 OnlineOpen APC）     |
| 篇幅            | 研究论文 **≤ 8,000 词**；**摘要 200 词**；短栏目各有上限             | 字数含图、表、参考文献与脚注                        |
| 体例            | **芝加哥作者—年份**；接受**自由格式**首投；参考文献附 DOI            | 首投无需严格套模板；ORCID 依 Wiley 要求             |
| 伦理            | **知情同意、匿名化、遗产／归还、问责**为核心                        | 伦理须在设计阶段嵌入，并影响能否发表                |
| 特色栏目        | Vital Topics Forum · World／Public／Multimodal Anthropologies · 书评 | 提前选对栏目                                         |

> **官方依据核对于 2026-06-20** —— 事实锚定于 AA 编辑部网站、AAA 伦理与新闻页面、
> AnthroSource/Wiley，以及 Wiley Author Compliance Tool。Research Exchange 实时提示、APC 与编辑团队
> 会变化，正式上传或接收后开放获取付款前请复核官网。

### 栏目一览

- **Research Articles（研究论文）** —— 完整研究，**≤ 8,000 词**（接收后可酌情扩至约 10,500 词）。
- **Vital Topics Forums** —— 就重大议题组织的多作者论坛（通常为约稿／提案）。
- **World Anthropologies** —— 来自英语中心之外的人类学，去中心化经典。
- **Public Anthropologies** —— 介入式、行动主义、面向公众的学术。
- **Multimodal Anthropologies** —— 以图像／声音／影像本身作为论证，被视为独立的学术形式。
- **Essays／Commentaries／Interviews／Review Essays／Book Reviews** —— 各有字数上限的短篇形式。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/american-anthropologist-skills
/plugin install american-anthropologist-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/american-anthropologist-skills.git
cd american-anthropologist-skills

mkdir -p ~/.claude/skills && cp -R skills/amanthro-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/amanthro-* ~/.codex/skills/
```

### 首个提示词

```
请用 amanthro-workflow 告诉我，针对我的 American Anthropologist 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
amanthro-topic-selection
        ▼
amanthro-literature-positioning
        ▼
amanthro-theory-building
        ▼
amanthro-research-design
        ▼
amanthro-data-analysis
        ▼
amanthro-tables-figures
        ▼
amanthro-writing-style          （打磨）
        ▼
amanthro-transparency-and-data  （伦理与问责——也应尽早运行）
        ▼
amanthro-review-process
        ▼
amanthro-submission
        ▼
amanthro-rebuttal
```

`amanthro-workflow` 是路由器，依据阶段、子领域与栏目告诉你下一步该用哪个技能。**伦理与问责**技能
（`amanthro-transparency-and-data`）应**尽早**运行，并在投稿前再次运行：知情同意、匿名化与遗产义务
都是设计决策，而非最后一步的核对项。

---

## 技能列表

| 技能                               | 用途                                                                       |
|------------------------------------|----------------------------------------------------------------------------|
| `amanthro-workflow`                | 路由器——按阶段／子领域／栏目决定下一步技能                                |
| `amanthro-topic-selection`         | 横跨人类学的四领域契合度；选对栏目                                          |
| `amanthro-literature-positioning`  | 超越本子领域对话；去中心化经典；引用政治                                    |
| `amanthro-theory-building`         | 构建可迁移概念 + 反身性论证（从民族志到生物人类学）                         |
| `amanthro-research-design`         | 论证研究设计——田野、档案／材料、实验室／定量、多模态                      |
| `amanthro-data-analysis`           | 严谨的诠释；诚实呈现证据；生物／考古的定量严谨                              |
| `amanthro-tables-figures`          | 民族志 + 多模态展示物：知情同意、版权、替代文本                            |
| `amanthro-writing-style`           | 芝加哥作者—年份；面向四领域；关怀性、包容性语言                            |
| `amanthro-transparency-and-data`   | 伦理与问责：知情同意、匿名化、遗产／归还                                    |
| `amanthro-review-process`          | 匿名评审、关怀伦理、筛查、栏目、决定类别                                    |
| `amanthro-submission`              | Research Exchange 投稿前核查（匿名、字数、伦理声明、ORCID）                |
| `amanthro-rebuttal`                | 面向跨子领域评审人与主编的 R&R 回复信策略                                  |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 按子领域整理的人类学数据源、档案与软件（CAQDAS、转写、GIS、实验室／定量）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 本包每条事实背后的 AA／AAA／Wiley 官方网址与实时复核守则
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— AA 体例的前后对照引言示例（虚构）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 经网络核实的真实 AA 论文，按子领域 × 方法整理，附姊妹刊防混淆清单

---

## 与姊妹刊的区别

| 期刊                       | 范围／形式                                                       | 本包的防混淆点 |
|----------------------------|-----------------------------------------------------------------|----------------|
| **American Anthropologist (AA)** | **四领域 AAA 旗舰**；民族志 + 材料 + 生物 + 语言               | 本包目标 |
| *American Ethnologist* (AE) | 社会文化民族志（AAA/AES）                                        | AA 更宽的四领域，而非 AE 的社会文化聚焦 |
| *Cultural Anthropology* (CA)| 社会文化、理论先行（SCA），常开放获取                            | AA 是四领域，而非 CA 的纯社会文化范围 |
| *Current Anthropology*      | 四领域，但有独特的 **CA✩ 评论—回应** 形式（Wenner-Gren／芝加哥） | AA 无 CA✩ 形式；切勿混淆 |

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定主编或评审人的口味
- 不发放伦理豁免，也不替代 IRB／社群审查
- 不把易变元信息写死为永久规则；Research Exchange 提示、APC 与编辑团队变更须以官网为准

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专属技能包索引
- [American Anthropologist（Wiley Online Library）](https://anthrosource.onlinelibrary.wiley.com/journal/15481433) —— 出版方主页
- [American Anthropologist 编辑部网站](https://www.americananthropologist.org/) —— 栏目、投稿方式、编辑政策
- [American Anthropological Association](https://www.americananthro.org/) —— 所有方；伦理准则

---

## 许可证

MIT
