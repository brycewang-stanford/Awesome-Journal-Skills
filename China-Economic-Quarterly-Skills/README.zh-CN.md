# 《经济学(季刊)》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《经济学(季刊)》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-经济学(季刊)%20CEQ-c0392b)](https://www.nsd.pku.edu.cn/cbw/jjxjk/index.htm)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://www.nsd.pku.edu.cn/cbw/jjxjk/index.htm)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《经济学(季刊)》(China Economic Quarterly, CEQ)** 投稿的 agent skill 集合——北京大学中国经济研究中心（CCER，今国家发展研究院 NSD）主办，是国内**最贴近国际主流经济学范式**的中文刊（2001 年创办；自 2021 年起全年六期；ISSN 2095-1086；CN 11-6010/F）。

本包**有观点**：不是通用计量工具箱，而是围绕该刊的核心门槛——**可信识别 + 国际可对话优先于一切**——专门构建。CEQ 是国内经济学刊中**对方法规范性要求最高、对政策口号容忍度最低**的一家。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

CEQ 的约束与同门经济学刊（经济研究 / 中国工业经济 / 金融研究 / 世界经济）显著不同：

| 约束 | 经济学(季刊) | 含义 |
|------|--------------|------|
| 范式 | 国际主流；审稿人多有海外训练 | "国内实证套路"叙事显过时 |
| 识别 | 要么结构、要么干净准实验 | OLS+控制当因果会被退稿 |
| 现代 DID | 交错/异质性检验是标配 | 裸 TWFE 跑交错处理＝退稿 |
| 推断 | 聚类理由、弱工具稳健、多重检验 | 默认稳健标准误不够 |
| 贡献 | 对标到具体 field 文献 | "丰富了相关研究"不算贡献 |
| 图表 | 图优于表（事件研究/bin-scatter） | 只放表会低估设计价值 |
| 摘要 | 英文摘要 ≤ 100 词，须让 field 同行读懂 | 很多读者只读英文摘要+图 |
| 引用 | 正文作者—年份**页内夹注**、3 个 JEL 号 | 脚注式引用不合体例 |

---

## 十二个 Skill

| Skill | 作用 |
|-------|------|
| `ceq-workflow` | 路由器——下一步用哪个 |
| `ceq-fit-positioning` | 是否对口 CEQ？不对口就改投 |
| `ceq-topic-selection` | 干净因果/可建模/国际可对话的选题 |
| `ceq-literature-review` | 对标具体 field 文献谈贡献；中英文献 |
| `ceq-identification` | 结构估计或准实验；识别假设显式化 |
| `ceq-modern-did` | 交错/异质性处理效应合规 |
| `ceq-inference` | 聚类、弱工具稳健、多重检验、标准误 |
| `ceq-mechanism` | 渠道/机制证据 |
| `ceq-figures` | 事件研究/bin-scatter/拟合图——图优于表 |
| `ceq-abstract-english` | 英文摘要 + 对标 field 的贡献陈述 |
| `ceq-submission` | 投稿前：系统、体例、可复现、匿名 |
| `ceq-rebuttal` | R&R 外审回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install china-economic-quarterly-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/ceq-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/ceq-* ~/.codex/skills/
```

---

> 编辑政策与刊期会变（刊名虽为"季刊"，但自 2021 年起全年六期）。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照 [nsd.pku.edu.cn/cbw/jjxjk](https://www.nsd.pku.edu.cn/cbw/jjxjk/index.htm) 最新《投稿须知》与 [`resources/journal-profile.md`](resources/journal-profile.md) 核实。
