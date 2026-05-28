# 经济研究 Skills

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-经济研究-c0392b)](http://www.erj.cn/)
[![Index](https://img.shields.io/badge/索引-CSSCI%20%2F%20国务院学位委员会-1f6feb)](http://www.erj.cn/)
[![Workflow](https://img.shields.io/badge/工作流-识别+机制+异质性-blue)](skills/er-workflow)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《经济研究》** 投稿的 Agent Skill 工具栈。覆盖**选题、文献综述、识别策略、机制分析、异质性、表格、政策含义、投稿规范、修改回复**十大环节，配套 Stata / R / Python 模板。

本仓库刻意**不通用**——它是面向《经济研究》编委审稿口味的方法论沉淀，不是泛化的"中文经济学写作助手"。

---

## 为什么要为《经济研究》单独做一套 Skills？

《经济研究》是国务院学位委员会经济学评议组指定的中国经济学最高水平刊物，约束维度与 AER / 海外顶刊**显著不同**：

| 维度       | 《经济研究》要求               | 隐含含义                                          |
|----------|-----------------------|---------------------------------------------|
| 学科定位    | 经济学（含宏观、制度、计量、产业、金融） | 偏纯管理学 / 案例的稿件不适合                       |
| 选题       | 强调理论贡献 + 中国问题            | 仅"政策评估"易被认为"工作论文"                      |
| 边际贡献    | 引言必须明确写出，3–5 条               | "本文有以下创新"段落必须精炼                        |
| 文献综述    | 中英文献并重，**理论文献必引**            | 缺经典理论文献会被审稿人挑出                          |
| 识别策略    | 准实验 + 严密的内生性讨论              | OLS + 控制变量易被退稿                           |
| 机制       | 几乎必备                          | 没有机制的实证文章命中率低                          |
| 异质性     | 强烈推荐                          | 缺异质性切分常会被要求补做                          |
| 政策含义    | 必备，但写法偏"政策意义"而非操作建议      | 与《管理世界》"政策建议"的可操作度有差异              |
| 字数       | 正文 1.5–2.5 万字（含图表）            | 比 AER 长，结构完整                              |
| 摘要       | 中文摘要 200–400 字                   | 必须先说"做了什么 + 结论"再说意义                  |

通用的"科研写作"或"经济学写作"Skill 包不会处理这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/economic-research-skills
/plugin install economic-research-skills
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/economic-research-skills.git
cd economic-research-skills

mkdir -p ~/.claude/skills && cp -R skills/er-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/er-* ~/.codex/skills/
```

### 第一条 Prompt

```
用 er-workflow 告诉我这份《经济研究》目标稿子下一步该做什么。
```

---

## 默认工作流

```text
er-topic-selection
        ▼
er-literature-review
        ▼
er-identification
        ▼
er-mechanism
        ▼
er-heterogeneity
        ▼
er-tables-figures
        ▼
er-policy-implication
        ▼
er-abstract      （polish）
        ▼
er-style         （polish）
        ▼
er-submission
        ▼
er-rebuttal
```

`er-workflow` 是路由器，会根据当前阶段告诉你下一个该用哪个 Skill。

---

## Skill 一览

| Skill                     | 用途                                  |
|--------------------------|------------------------------------|
| `er-workflow`             | 路由器：判断当前阶段，推荐下一个 skill     |
| `er-topic-selection`      | 选题 + 理论贡献定位 + 边际贡献四句式      |
| `er-literature-review`    | 中英文献并重 + 理论文献必引 + 对话式综述  |
| `er-identification`       | 准实验设计（DID / IV / RDD / DML）       |
| `er-mechanism`            | 机制分析三种主流路径与写作模板            |
| `er-heterogeneity`        | 异质性切分五维度优先级                    |
| `er-tables-figures`       | 三线表、变量定义表、图形美学              |
| `er-policy-implication`   | 政策含义（《经济研究》偏意义层面而非操作）  |
| `er-abstract`             | 摘要五句法（约 300 字） + 黑名单短语清除  |
| `er-style`                | 全文语言 polish：空话套话 → 具体贡献      |
| `er-submission`           | 投稿 checklist + 稿件模板（格式、字数、双盲、查重）|
| `er-rebuttal`             | 修改回复信结构（致谢 → 逐条 → 修订对照） |

### 附属资源

- [`skills/er-submission/templates/manuscript_template.md`](skills/er-submission/templates/manuscript_template.md) —— 稿件结构骨架（中英摘要、变量定义表、参考文献格式）
- [`skills/er-submission/templates/checklist.md`](skills/er-submission/templates/checklist.md) —— 投稿前 8 类自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— 数据资源（CSMAR / Wind / CNRDS / CFPS / CHARLS 等）+ Stata / Python / R 包速查

---

## 与《管理世界》Skill 包的差异

| 维度        | 《经济研究》              | 《管理世界》              |
|----------|-----------------------|----------------------|
| 学科定位    | 经济学（宏观 / 制度偏多）        | 管理 + 应用经济             |
| 政策含义    | "政策意义"，偏定性 / 宏观启示    | "政策建议"，偏可操作 / 部门级 |
| 案例 / 质性 | 较少接受                     | 接受                    |
| 理论文献    | **必引**                     | 可选                    |
| 写作风格    | 偏理论严谨                    | 偏实践契合                |

---

## 关于这个仓库不做什么

- 不替你写出可以直接投稿的稿件
- 不模拟审稿人偏好
- 不收录《经济研究》历年拒稿率、影响因子等元数据
- 不评估你的"理论贡献"是否真有原创性——这是研究者本人的判断

---

## 相关仓库

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊 Skill 索引
- [AER-skills](https://github.com/brycewang-stanford/AER-skills) —— American Economic Review 投稿工具栈
- [management-world-skills](https://github.com/brycewang-stanford/management-world-skills) —— 《管理世界》投稿工具栈

---

## License

MIT
