# 《中国社会科学》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《中国社会科学》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-中国社会科学-c0392b)](https://sscp.cssn.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://sscp.cssn.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《中国社会科学》(Social Sciences in China)** 投稿的 agent skill 集合——中国社会科学院主办，国内综合性、跨学科社科第一刊（月刊；ISSN 1002-4921；CN 11-1211/C）。

本包**有观点**：不是通用社科写作工具箱，而是围绕该刊的核心门槛——**思想分量与原创理论贡献优先于方法复杂度**——专门构建。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

《中国社会科学》的约束与学科刊（经济研究 / 管理世界 / 社会学研究）显著不同：

| 约束 | 中国社会科学 | 含义 |
|------|--------------|------|
| 学科 | 综合性跨学科旗舰 | 单学科细分实证多半不对口 |
| 问题层级 | 重大理论与现实问题（制度/文明/治理） | "政策评估"框架像工作论文 |
| 贡献 | 原创概念/命题/框架 | "发现 X 影响 Y"不够 |
| 知识体系 | 中国自主知识体系；理论对话 | 验证国外理论 ≠ 贡献 |
| 方法 | 多元；方法服务论题 | 技术不能替代理论论证 |
| 摘要 | 200–300 字，3–5 关键词 | 命题前置，别先铺背景 |
| 注释 | 页下注（脚注） | 尾注/夹注不合体例 |

---

## 十一个 Skill

| Skill | 作用 |
|-------|------|
| `ssc-workflow` | 路由器——下一步用哪个 |
| `ssc-fit-positioning` | 是否对口？不对口就改投 |
| `ssc-topic-problematic` | 上移为"重大问题/问题意识" |
| `ssc-theory-contribution` | 原创概念/命题/框架；自主知识体系 |
| `ssc-literature-dialogue` | 进入理论脉络，而非堆引用 |
| `ssc-argumentation` | 概念严谨 + 论证链 |
| `ssc-evidence` | 定量/定性/历史——方法服务论题 |
| `ssc-style` | 学理文风；去政策汇报腔 |
| `ssc-abstract-keywords` | 摘要 200–300 字 + 3–5 关键词 |
| `ssc-submission` | 投稿前：页下注、投稿系统、匿名 |
| `ssc-rebuttal` | 外审回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install social-sciences-in-china-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/ssc-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/ssc-* ~/.codex/skills/
```

---

> 编辑政策会变。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照 [sscp.cssn.cn](https://sscp.cssn.cn/) 最新《投稿须知》核实。
