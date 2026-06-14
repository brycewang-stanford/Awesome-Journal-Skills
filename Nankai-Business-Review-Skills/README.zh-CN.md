# 《南开管理评论》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《南开管理评论》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-南开管理评论-c0392b)](https://nbr.nankai.edu.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://nbr.nankai.edu.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《南开管理评论》(Nankai Business Review, NBR)** 投稿的 agent skill 集合——教育部主管、南开大学（商学院）主办的工商管理学科高端学术平台（1998 年由《国际经贸研究》更名；ISSN 1008-3448；CN 12-1288/F）。

本包**有观点**：既不是通用管理学写作工具箱，也不是计量识别工具箱。它围绕该刊的核心门槛——**理论贡献 + 中国情境 + 测量规范**——专门构建，落地于问卷-SEM、实验法、多案例 / 扎根理论三类方法。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

NBR 的约束与经济学 / 宏观政策刊（经济研究 / 管理世界 / 中国工业经济）以及数理建模刊（管理科学学报）显著不同：

| 约束 | 南开管理评论 | 含义 |
|------|--------------|------|
| 学科 | 理论建构型管理学（组织行为/战略/人力/营销/治理） | 宏观政策评估框架不对口 |
| 贡献 | 推进某管理理论的概念/命题/框架 | "回归显著"不是贡献 |
| 假设 | 每条都有理论机理支撑 | "我觉得正相关"会被退稿 |
| 测量 | 信度（α、CR）+ 效度（收敛/区分、AVE）+ 共同方法偏差检验 | 照搬量表、不做心理测量过不了审 |
| 方法 | 问卷-SEM / 实验 / 多案例——服务理论 | 因果识别"干净"不是评判标准 |
| 中国情境 | 情境必须进入理论 | "用了中国样本" ≠ 情境化 |
| 摘要 | 100–300 字，3–8 关键词，中英文 | 命题前置，别先铺背景 |

---

## 十二个 Skill

| Skill | 作用 |
|-------|------|
| `nbr-workflow` | 路由器——下一步用哪个；交叉引用同仓兄弟期刊包 |
| `nbr-fit-positioning` | 是否对口？数理模型 / 宏观政策改投他刊 |
| `nbr-theory-gap` | 讲清理论缺口与理论贡献 |
| `nbr-hypothesis-development` | 每条假设有机理，不是经验直觉 |
| `nbr-measurement` | 信度（α、CR）、效度（AVE）、共同方法偏差检验 |
| `nbr-survey-sem` | SEM / 中介 / 调节 / 被调节的中介 / 多层（HLM） |
| `nbr-experiment` | 操纵检验、随机化、效应量 |
| `nbr-qualitative-case` | 多案例比较 / 扎根编码 / 理论饱和与可信度 |
| `nbr-china-context` | 中国情境如何改变构念关系 |
| `nbr-discussion-contribution` | 讨论回扣并推进某理论 |
| `nbr-submission` | 投稿前：体例、摘要字数、在线系统 |
| `nbr-rebuttal` | R&R 回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install nankai-business-review-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/nbr-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/nbr-* ~/.codex/skills/
```

---

> 编辑政策会变。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照 [nbr.nankai.edu.cn](https://nbr.nankai.edu.cn/) 最新《来稿规范说明》核实。
