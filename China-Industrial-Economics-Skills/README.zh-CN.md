# 《中国工业经济》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《中国工业经济》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-中国工业经济-c0392b)](https://ciejournal.ajcass.com/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://ciejournal.ajcass.com/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《中国工业经济》(China Industrial Economics)** 投稿的 agent skill 集合——中国社会科学院工业经济研究所主办，国内产业经济 / 企业与创新实证顶刊（月刊；ISSN 1006-480X；CN 11-3536/F）。

本包**有观点**：不是通用实证工具箱，而是围绕该刊的核心标志——**实证工程化**——专门构建：干净的中国政策准实验、做满的稳健性"军备竞赛"、机制+异质性（带经济含义）、**可落地的产业政策含义**。办刊理念是**"理论顶天，实践立地"**。

该刊以发表**方法操作规范名篇**著称——最具代表性的是 **江艇（2022），《中国工业经济》2022 年第 5 期，中介效应与调节效应**——因此本包对"三步法中介"持保留态度。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

《中国工业经济》的约束与同类经济学刊（经济研究 / 管理世界 / 金融研究 / 世界经济）显著不同：

| 约束 | 中国工业经济 | 含义 |
|------|--------------|------|
| 画像 | 实证工程化 | 纯理论 / 单表实证不对口 |
| 识别 | 多期 DID / 事件研究 | TWFE 用于交错处理而不上异质性稳健估计 = 退稿 |
| 机制 | 分渠道 / 调节 | 三步中介被保留质疑（江艇 2022） |
| 异质性 | 多维 + 经济含义 | 只切"东中西"太薄 |
| 稳健性 | 军备竞赛，做满 | 稳健性单薄一定退修 |
| 表格 | 报经济量级 | 只报星号显著不够 |
| 政策 | 可操作：谁、哪环节、做什么 | 区别于《经济研究》的意义层 |
| 摘要 | 450—500 字，3—5 关键词 | 创新点前置 |
| 注释 | 页下注（脚注）+ 参考文献"实引" | 尾注 / 纯夹注不合体例 |
| 可复现 | 录用需交数据 + 代码 | 投稿前先备好 |

---

## 十三个 Skill

| Skill | 作用 |
|-------|------|
| `cie-workflow` | 路由器——下一步用哪个；交叉引用同类期刊包 |
| `cie-fit-positioning` | 是否对口？理论重 / 偏管理 / 偏金融 / 偏贸易就改投 |
| `cie-topic-selection` | 政策准实验 / 企业行为 / 产业组织 / 数字经济 + 3—5 条边际贡献 |
| `cie-literature-review` | 述评不足，而非堆引用 |
| `cie-institutional-background` | 政策细节、试点名单、时点讲准 |
| `cie-did-identification` | 多期 DID / 事件研究；平行趋势 + 安慰剂 + 异质性稳健估计（强制） |
| `cie-mechanism` | 分渠道 / 调节；慎用三步中介 |
| `cie-heterogeneity` | 多维切分 + 经济含义 |
| `cie-robustness` | 招牌：稳健性"军备竞赛" |
| `cie-tables-figures` | 三线表 + 每张关键表后的经济量级解读 |
| `cie-policy-implication` | 可操作：谁、在哪个环节、做什么 |
| `cie-submission` | 投稿前：页下注、实引、投稿系统、数据代码、匿名 |
| `cie-rebuttal` | 外审 / R&R 回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install china-industrial-economics-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/cie-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/cie-* ~/.codex/skills/
```

---

> 编辑政策会变。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照 [ciejournal.ajcass.com](https://ciejournal.ajcass.com/) 最新《投稿（修改）指南》核实。
