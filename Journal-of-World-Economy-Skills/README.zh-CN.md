# 《世界经济》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《世界经济》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-世界经济-c0392b)](https://www.jweonline.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://www.jweonline.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《世界经济》(The Journal of World Economy)** 投稿的 agent skill 集合——中国社会科学院主管，中国世界经济学会与中国社会科学院世界经济与政治研究所（IWEP）共同主办，国内国际经济学 / 开放宏观第一刊（月刊；ISSN 1002-9621；CN 11-1138/F）。

本包**有观点**：不是通用实证经济学写作工具箱，而是围绕该刊的核心门槛——**国际 / 开放维度与明确的传导渠道，而非"贴一句全球化"的国内政策评估**——专门构建。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

《世界经济》的约束与国内学科刊（经济研究 / 中国工业经济 / 金融研究 / 经济学季刊）显著不同：

| 约束 | 世界经济 | 含义 |
|------|----------|------|
| 视角 | 国际 / 开放是身份标识 | 纯国内文章再干净也不对口 |
| 问题 | 开放经济中的因果问题 | "国内政策评估"框架偏题 |
| 机制 | 贸易 / 投资 / 金融 / 预期渠道 | "促进了出口"不说渠道太薄 |
| 文献 | 国际贸易 / 国际金融经典 + 前沿 | 只引国内实证不算对话 |
| 数据 | 海关微观 / 跨国面板 / GVC / 投入产出 | 一般省级面板多半不对口 |
| 识别 | 外部冲击 + shift-share / 引力 | 须回应现代 shift-share 推断批评 |
| 政策 | 对外开放政策（贸易 / 汇率 / 资本账户） | 国内操作化建议错了层级 |
| 注释 | 脚注（页下注），参考文献置文末 | 尾注 / 纯文中夹注不合体例 |
| 摘要 | 内容提要 ≤ 300 字，3–5 关键词 | 摘要前置开放经济发现 |

---

## 十二个 Skill

| Skill | 作用 |
|-------|------|
| `jwe-workflow` | 路由器——下一步用哪个 |
| `jwe-fit-positioning` | 开放维度立得住吗？立不住就改投 |
| `jwe-topic-international` | 用国际视角看的因果问题 |
| `jwe-literature-review` | 与国际贸易 / 国际金融经典与前沿对话 |
| `jwe-data-sources` | 海关微观、跨国面板、GVC / 投入产出（KWW、MRIO） |
| `jwe-identification` | 外部冲击 + shift-share / 引力（含推断批评） |
| `jwe-transmission-channel` | 贸易 / 投资 / 金融 / 预期渠道 |
| `jwe-heterogeneity` | 按暴露度 / 企业 / 国别 / 边际切分 |
| `jwe-tables-figures` | 主表主图与体例 |
| `jwe-policy-implication` | 落在开放政策层，不写操作清单 |
| `jwe-submission` | 投稿前：页下注、www.jweonline.cn、匿名 |
| `jwe-rebuttal` | R&R 回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install journal-of-world-economy-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/jwe-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/jwe-* ~/.codex/skills/
```

---

> 编辑政策会变。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照官方编辑部网站 [www.jweonline.cn](https://www.jweonline.cn/) 最新《投稿须知》核实。该刊投稿系统曾迁移，网络上存在第三方"代投"站点，请只认官方入口。
