# 《社会学研究》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《社会学研究》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-社会学研究-c0392b)](https://shxyj.ajcass.com/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://shxyj.ajcass.com/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《社会学研究》(Sociological Studies)** 投稿的 agent skill 集合——中国社会科学院社会学研究所主办，国内社会学第一刊（双月刊；ISSN 1002-5936；CN 11-1100/C）。

本包**有观点**：不是通用实证方法工具箱，而是围绕该刊的核心门槛——**社会学问题意识 + 与社会学理论的实质对话，优先于干净因果识别与政策评估**——专门构建。

该刊**同时接纳定量**（CGSS / CFPS / CLDS 等大型社会调查的统计分析）**与定性**（田野民族志 / 深度访谈 / 扩展个案 / 扎根理论）两条传统。本包对两条传统都给出规范，拒绝把社会学塌缩成计量经济学。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

《社会学研究》的约束与经济学刊（经济研究 / 中国工业经济）、与跨学科旗舰（中国社会科学）都不同：

| 约束 | 社会学研究 | 含义 |
|------|------------|------|
| 问题 | 社会学问题意识（机制/结构） | "X 影响 Y"的政策框架显得不对学科 |
| 理论 | 与经典及当代社会学对话 | 验证国外理论 ≠ 贡献 |
| 方法 | 定量 + 定性双传统 | 两者皆收，但都要做到规范 |
| 定量目标 | 系数 → 社会过程 | 识别军备竞赛不是重点 |
| 定性目标 | 材料厚度 + 概念提炼 | 只复述故事、无概念会被拒 |
| 摘要 | 中文不超过 200 字；关键词 3–5 个 | 命题/问题前置，别先铺背景 |
| 注释 | 文中夹注（作者, 年: 页）+ 文末参考文献 | 尾注/数字脚注做引文出处不合体例 |

---

## 十二个 Skill

| Skill | 作用 |
|-------|------|
| `socs-workflow` | 路由器——下一步用哪个；并交叉指向其它期刊包 |
| `socs-fit-positioning` | 社会学问题意识 vs 经济学式政策评估；后者就改投 |
| `socs-problematic` | 立住社会学问题意识（问题意识） |
| `socs-theory-dialogue` | 进入经典与当代社会学理论脉络 |
| `socs-quantitative` | CGSS/CFPS/CLDS；回归 / Logit / 多层 / 事件史 / 序列分析——配社会学解释 |
| `socs-qualitative` | 田野民族志 / 访谈 / 扩展个案 / 扎根理论；材料厚度、编码透明、反身性 |
| `socs-mechanism-social-process` | 把系数/材料翻译成社会过程（谁、经由什么、形成什么结构） |
| `socs-concept-building` | 从材料提炼概念/机制，与理论往返 |
| `socs-style` | 学理文风；既去政策汇报腔，也去纯技术腔 |
| `socs-abstract-keywords` | 摘要不超过 200 字 + 3–5 关键词，按本刊规范 |
| `socs-submission` | 投稿前：文中夹注、文末参考文献、投稿系统、匿名 |
| `socs-rebuttal` | R&R 回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install sociological-studies-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/socs-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/socs-* ~/.codex/skills/
```

---

> 编辑政策会变。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照 [shxyj.ajcass.com](https://shxyj.ajcass.com/) 最新《投稿指南》核实。官网是本刊唯一投稿渠道。
