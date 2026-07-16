# 财贸经济 Skills

<p align="center">
  <img src="assets/cover.svg" alt="《财贸经济》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-财贸经济-6b3f2a)](http://naes.org.cn/)
[![Index](https://img.shields.io/badge/索引-CSSCI-1f6feb)](http://naes.org.cn/)
[![Workflow](https://img.shields.io/badge/工作流-识别+机制+异质性-blue)](skills/cte-workflow)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《财贸经济》** 投稿的 Agent Skill 工具栈。该刊由**中国社会科学院财经战略研究院**主办（月刊，创刊 1980），是财经领域的顶级 CSSCI 来源期刊，聚焦**财政、税收、金融、贸易、流通、消费**等宏观与应用经济学议题，偏好紧扣中国重大财经政策现实、有严谨因果识别（DID / IV / RDD / DML）与清晰机制检验的实证研究。本工具栈覆盖**财经选题、文献综述、因果识别、机制分析、异质性、表格、政策含义、投稿规范、修改回复**等环节，配套 CNKI / CSMAR / WIND / CEIC 等财经数据与 Stata / R / Python 模板。

本仓库刻意**不通用**——它是面向《财贸经济》编委审稿口味的方法论沉淀，不是泛化的"中文经济学写作助手"。

---

## 为什么要为《财贸经济》单独做一套 Skills？

《财贸经济》的约束维度与综合性经济学期刊**显著不同**：

| 维度 | 《财贸经济》要求 | 隐含含义 |
|---|---|---|
| 学科定位 | 财政 / 税收 / 金融 / 贸易 / 流通 / 消费 | 脱离财经场景的"通用"实证不适合 |
| 选题 | 理论贡献 + 一项具体的中国财经政策现实 | 第一段就要说明"为什么是财经问题、为什么现在做" |
| 制度扎根 | 落到中国财税 / 金融 / 贸易制度 | 无国别的可移植故事易被退稿 |
| 边际贡献 | 引言必须明确写出，3–5 条 | "本文有以下创新"段落必须精炼 |
| 数据 | 企业 / 城市 / 银行 / 居民微观数据，点名到库 | "公开渠道"表述被视为数据不透明 |
| 识别策略 | 准实验，处理政策内生性 | 纯描述统计 / OLS 易被退稿 |
| 机制 | 几乎必备，且落到可识别渠道 | "机制黑箱"命中率低 |
| 异质性 | 强烈推荐，且贴合中国财经制度场景 | 只切"东中西"会被视为偷懒 |
| 政策含义 | 意义层，但落到具体政策抓手 | "加强完善推进"四件套套话会被挑刺 |
| 字数 | 正文约 1.5–2.5 万字（含图表，以官网为准） | 结构完整 |

通用的"科研写作"或"经济学写作"Skill 包不会处理这些约束。

> 准确性提示：确切字数、参考文献条数、图表数量、投稿网址、评审流程等会随年度调整。本工具栈描述的是持久规范，**具体数字请以《财贸经济》官网"投稿须知"为准**。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/cte-skills
/plugin install cte-skills
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/cte-skills.git
cd cte-skills

mkdir -p ~/.claude/skills && cp -R skills/cte-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/cte-* ~/.codex/skills/
```

### 第一条 Prompt

```
用 cte-workflow 告诉我这份《财贸经济》目标稿子下一步该做什么。
```

---

## 默认工作流

```text
cte-topic-selection
        ▼
cte-literature-review
        ▼
cte-identification
        ▼
cte-mechanism
        ▼
cte-heterogeneity
        ▼
cte-tables-figures
        ▼
cte-policy-implication
        ▼
cte-abstract      （polish）
        ▼
cte-style         （polish）
        ▼
cte-submission
        ▼
cte-rebuttal
```

`cte-workflow` 是路由器，会根据当前阶段告诉你下一个该用哪个 Skill。

---

## Skill 一览

| Skill | 用途 |
|---|---|
| `cte-workflow` | 路由器：判断当前阶段，推荐下一个 skill |
| `cte-topic-selection` | 财经议题契合 + 理论贡献 + 边际贡献四句式 |
| `cte-literature-review` | 中外并重 + 财经经典必引 + 对话式综述 |
| `cte-identification` | 政策冲击准实验设计（DID / IV / RDD / DML）+ 政策内生处理 |
| `cte-mechanism` | 落到可识别渠道的机制分析（打开机制黑箱） |
| `cte-heterogeneity` | 贴合中国财经制度场景的异质性切分（超越"东中西"） |
| `cte-tables-figures` | 三线表、变量定义表、数据来源透明、图形美学 |
| `cte-policy-implication` | 政策含义（意义层但落到具体财经政策抓手） |
| `cte-abstract` | 摘要五句法 + 黑名单短语清除 |
| `cte-style` | 全文语言 polish：空话套话 / 四件套 → 具体 |
| `cte-submission` | 投稿 checklist + 稿件模板（格式、匿名、查重） |
| `cte-rebuttal` | 修改回复信结构（致谢 → 逐条 → 修订对照） |

### 附属资源

- [`skills/cte-submission/templates/manuscript_template.md`](skills/cte-submission/templates/manuscript_template.md) —— 稿件结构骨架（中英摘要、变量定义表、参考文献格式）
- [`skills/cte-submission/templates/checklist.md`](skills/cte-submission/templates/checklist.md) —— 投稿前 8 类自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— 财经数据资源（CNKI / CSMAR / WIND / CEIC / 工业企业 / 海关 / 统计年鉴等）+ Stata / R / Python 包速查
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 官方事实（主办、主编、费用、匿名评审）及核验日期
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 校准本刊实证范式的经典文献（按方法×主题）
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— 本刊房风格引言 before→after 改写

---

## 与相邻财经刊的差异

| 维度 | 《财贸经济》 | 相邻刊物 |
|---|---|---|
| 纯资产定价 / 公司金融 | 非核心 | 《金融研究》 |
| 国际贸易 / 开放宏观 | 接受但非核心 | 《世界经济》 |
| 更专门的财政 / 税收政策 | 接受 | 《财政研究》《税务研究》 |
| 更一般的理论贡献 | 不对口 | 《经济研究》《管理世界》 |
| 共同门槛 | 中国政策扎根 + 可信识别 + 机制 | —— |

---

## 关于这个仓库不做什么

- 不替你写出可以直接投稿的稿件
- 不模拟审稿人偏好
- 不收录《财贸经济》历年拒稿率、影响因子等元数据
- 不评估你的"理论贡献"是否真有原创性——这是研究者本人的判断

---

## 相关仓库

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊 Skill 索引
- [China-Rural-Economy-Skills](https://github.com/brycewang-stanford/china-rural-economy-skills) —— 《中国农村经济》投稿工具栈

---

## License

MIT
