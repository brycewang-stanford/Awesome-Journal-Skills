# 管理世界 Skills

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/期刊-管理世界-c0392b)](http://www.mwm.net.cn/)
[![Index](https://img.shields.io/badge/索引-CSSCI%20%2F%20北大核心-1f6feb)](http://www.mwm.net.cn/)
[![Workflow](https://img.shields.io/badge/工作流-识别策略+制度背景-blue)](skills/mw-workflow)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《管理世界》** 投稿的 Agent Skill 工具栈。覆盖**选题、文献综述、识别策略、制度背景、机制与异质性、表格、政策含义、投稿规范、修改回复**九大环节，配套 Stata / R / Python 模板。

本仓库刻意 **不通用**——它不是"中文经管写作助手"，而是一套**面向《管理世界》编委审稿口味**的方法论沉淀。

---

## 为什么要为《管理世界》单独做一套 Skills？

《管理世界》是中国管理学与应用经济学的事实头部刊物，对手稿的约束与 AER / SSCI 一区**显著不同**：

| 维度       | 《管理世界》要求              | 隐含含义                                 |
|----------|----------------------|------------------------------------|
| 选题       | 必须有"中国情境"或"中国制度"嵌入  | 纯方法论改进或纯海外样本极难发表                  |
| 引言       | 要明确写出"边际贡献"四到五条     | 不能像 AER 那样靠"problem → answer"叙事 |
| 文献综述     | 需独立成节，**中英文献并重**     | 缺中文经典文献会被审稿人直接挑出                  |
| 识别策略     | 偏好准实验（DID / IV / RDD / 双重机器学习） | 仅 OLS + 内生性讨论易被退稿                  |
| 制度背景     | 通常需要独立一节，说明政策 / 制度细节 | 海外读者视角不够，会被认为"故事不完整"            |
| 机制 / 异质性 | 实证文章几乎必备                | 没有机制检验的实证文章命中率很低                  |
| 政策含义     | 文末必须有政策启示，可操作        | 纯学术贡献而无政策落点会被审稿人提出补充           |
| 字数       | 正文约 1.5–2.5 万字（含图表）    | 比 AER 长得多，结构更完整                  |
| 摘要       | 中文摘要 300–500 字            | 必须先说"做了什么 + 结论"再说意义           |

通用的"科研写作"或"经济学写作"Skill 包并不会处理这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
# 添加 marketplace（一次性）
/plugin marketplace add https://github.com/brycewang-stanford/management-world-skills

# 安装插件
/plugin install management-world-skills

# 重载
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/management-world-skills.git
cd management-world-skills

# Claude Code（user 级）
mkdir -p ~/.claude/skills && cp -R skills/mw-* ~/.claude/skills/

# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/mw-* ~/.codex/skills/
```

### 第一条 Prompt

```
用 mw-workflow 告诉我这份《管理世界》目标稿子下一步该做什么。
```

---

## 默认工作流

```text
mw-topic-selection
        │   选题与中国情境匹配
        ▼
mw-literature-review
        │   中英文献并重综述
        ▼
mw-institutional-background
        │   政策 / 制度背景章节
        ▼
mw-identification
        │   准实验识别策略
        ▼
mw-mechanism-heterogeneity
        │   机制 + 异质性检验
        ▼
mw-tables-figures
        │   规范化表格图形
        ▼
mw-policy-implication
        │   政策启示与对策建议
        ▼
mw-submission
        │   投稿前 checklist
        ▼
mw-rebuttal
            修改回复信
```

`mw-workflow` 是路由器，会根据当前阶段告诉你下一个该用哪个 Skill。

---

## 九个 Skill 一览

| Skill                            | 用途                                  |
|---------------------------------|------------------------------------|
| `mw-workflow`                    | 路由器：判断当前阶段，推荐下一个 skill         |
| `mw-topic-selection`             | 选题 + 中国情境契合度 + 边际贡献四条句式      |
| `mw-literature-review`           | 中英文献综述结构，避免审稿人挑出经典缺失         |
| `mw-identification`              | 准实验设计（DID / IV / RDD / DML）       |
| `mw-institutional-background`    | 制度背景章节写法与政策时间线                |
| `mw-mechanism-heterogeneity`     | 机制识别 + 异质性切分维度                  |
| `mw-tables-figures`              | 表格三线 / booktabs、注释规范、图形美学      |
| `mw-policy-implication`          | 政策启示分层（短中长期 / 微宏观）           |
| `mw-submission`                  | 投稿前 checklist：格式、字数、查重、双盲     |
| `mw-rebuttal`                    | 修改回复信结构（致谢 → 逐条 → 修订对照）   |

---

## 关于这个仓库不做什么

- 不替你写出可以直接投稿的稿件
- 不模拟审稿人偏好（审稿人偏好高度异质）
- 不收录《管理世界》拒稿率、影响因子等元数据
- 不评估你的中国情境是否"真"——这是研究者本人的判断

---

## 相关仓库

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊 Skill 索引
- [AER-skills](https://github.com/brycewang-stanford/AER-skills) —— American Economic Review 投稿工具栈
- [economic-research-skills](https://github.com/brycewang-stanford/economic-research-skills) —— 《经济研究》投稿工具栈

---

## License

MIT
