# 《金融研究》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《金融研究》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-金融研究-c0392b)](http://www.jryj.org.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](http://www.jryj.org.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《金融研究》(Journal of Financial Research, JFR)** 投稿的 agent skill 集合——中国金融学会主办，中国人民银行金融研究所《金融研究》编辑部编辑出版，国内**金融学第一刊**（月刊；ISSN 1002-7246；CN 11-1268/F）。

本包**有观点**：不是通用金融写作工具箱，而是围绕该刊的核心门槛——**严谨识别 + 对中国金融体系的现实意义**——以及它的两大支流（**宏观金融**与**微观公司金融**）专门构建。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

《金融研究》处在干净因果经济学刊与管理学刊之间，约束与两者都不同：

| 约束 | 金融研究 | 含义 |
|------|----------|------|
| 学科 | 金融旗舰，两条线 | 宏观金融与微观公司金融叙事不同 |
| 识别 | 政策冲击 / 高频意外 | OLS 跑相关性会被退稿 |
| 机制 | 金融渠道 | "促进/抑制"无渠道不够 |
| 制度细节 | 中国金融体系，须讲准 | 监管口径/市场分层写错即出局 |
| 政策含义 | 货币当局/监管/机构 | 比《经济研究》更具操作性 |
| 摘要 | 二百字左右，3–5 关键词，3 个 JEL | 结论与渠道前置 |
| 注释 | 编号注（①②③），连续编号 | 纯文中夹注不合体例 |

---

## 十二个 Skill

| Skill | 作用 |
|-------|------|
| `jfr-workflow` | 路由器——下一步用哪个；交叉引用同仓库其它刊 |
| `jfr-fit-positioning` | 宏观金融 vs 微观公司金融；偏产业/会计就改投 |
| `jfr-topic-selection` | 定金融问题与贡献 |
| `jfr-literature-review` | 进入金融脉络，中英文并重 |
| `jfr-institutional-background` | 中国金融制度细节，讲准 |
| `jfr-identification` | 政策冲击（MPA/资管新规/LPR/注册制）、高频意外、DID、IV |
| `jfr-mechanism` | 金融渠道：信贷/风险承担/资产负债表/信息 |
| `jfr-heterogeneity` | 按所有制、银行类型、地区、市场分层切分 |
| `jfr-tables-figures` | 主表/主图终化，合该刊体例 |
| `jfr-policy-implication` | 面向货币当局/监管/金融机构 |
| `jfr-submission` | 投稿前：注释、摘要/关键词/JEL、投稿系统、匿名 |
| `jfr-rebuttal` | R&R 回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install journal-of-financial-research-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/jfr-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/jfr-* ~/.codex/skills/
```

---

> 编辑政策会变。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照 [www.jryj.org.cn](http://www.jryj.org.cn/) 最新《来稿须知》核实。
