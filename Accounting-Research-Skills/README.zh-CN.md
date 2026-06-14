# 《会计研究》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《会计研究》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-会计研究-c0392b)](https://www.asc.net.cn/AccountingResearch/MagazineProfile.aspx?type=profile)
[![Index](https://img.shields.io/badge/index-CSSCI%20%7C%20NSFC%20A-1f6feb)](https://www.asc.net.cn/AccountingResearch/MagazineProfile.aspx?type=profile)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《会计研究》(Accounting Research)** 投稿的 agent skill 集合——财政部主管、中国会计学会主办，CSSCI 来源期刊中**惟一的会计类学术期刊**，国家自然科学基金委管理科学 A 类重要期刊（月刊；1980 年创刊；ISSN 1003-2886；CN 11-1078/F）。

本包**有观点**：不是通用财务实证工具箱，而是围绕该刊的核心门槛——**资本市场档案式实证 + 准确的会计制度/准则细节 + 信息机制，且须与一般公司金融区分**——专门构建。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

《会计研究》的约束与金融/管理/经济学科刊（金融研究 / 南开管理评论 / 经济研究）显著不同：

| 约束 | 会计研究 | 含义 |
|------|----------|------|
| 落点 | 会计信息/披露/审计/准则 | 落到金融机理就不对口——改投 |
| 制度细节 | 准则条款 + 执行时点须精确 | 含糊的"政策背景"显得粗疏 |
| 度量 | 会计度量须透明构造 | 直接拿现成代理而不交代 = 拒稿风险 |
| 识别 | 优先准则/监管外生变更 | 纯 OLS 很难过审 |
| 机制 | 信息渠道（不对称/披露/盈余管理） | 纯定价渠道属于金融刊 |
| 贡献 | 理论**与**准则制定者/监管者实务 | "丰富了文献"不够 |
| 注释 | 当页下注（脚注），每页 ①②… 单独排序 | 尾注/纯文中引用不合体例 |
| 参考文献 | 著者—出版年制；先中文后外文 | 编号 [1][2] 制不合体例 |

---

## 十三个 Skill

| Skill | 作用 |
|-------|------|
| `acr-workflow` | 路由器——下一步用哪个 |
| `acr-fit-positioning` | 是会计议题还是金融机理？是金融就改投 |
| `acr-topic-selection` | 立会计学贡献，而非一般效应 |
| `acr-literature-review` | 进入会计脉络（盈余质量/审计/披露） |
| `acr-institutional-standards` | 准确的准则/监管：条款、执行时点 |
| `acr-measurement` | 可操纵性应计（修正 Jones）、稳健性（C-Score）、披露指数 |
| `acr-identification` | 准则/监管外生变更（事件研究/DID）/ PSM / Heckman |
| `acr-mechanism` | 信息机制：降低不对称、提高披露、约束盈余管理 |
| `acr-robustness` | 替换度量、控制治理/制度变量、安慰剂 |
| `acr-tables-figures` | 经济意义量级解读 |
| `acr-implications` | 对准则/监管/实务的启示 |
| `acr-submission` | 投稿前：页下注、文献体例、投稿系统、匿名 |
| `acr-rebuttal` | R&R 回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install accounting-research-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/acr-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/acr-* ~/.codex/skills/
```

---

> 编辑政策会变。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照 [asc.net.cn](https://www.asc.net.cn/AccountingResearch/MagazineProfile.aspx?type=tgzn) 最新《投稿指南》核实。
