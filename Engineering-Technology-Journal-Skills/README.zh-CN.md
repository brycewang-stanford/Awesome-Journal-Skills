# 工程与技术期刊 Skills（Engineering & Technology Journal Skills）

<p align="center">
  <img src="assets/cover.svg" alt="工程与技术期刊 Skills — 40 个旗舰工程技术期刊" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Index](https://img.shields.io/badge/index-IEEE%20%C2%B7%20Automatica%20%C2%B7%20Optica%20%C2%B7%20Acta%20Materialia-1f6feb)](#)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **40 个旗舰英文工程技术期刊** 的 agent skill 合集 —— 专门补齐自然科学合集留白的工程版图。覆盖 IEEE Transactions / Proceedings 家族（控制、信息论、信号处理、通信、电力、工业电子、天线、机器人、医学影像、生医工程），Automatica 与 IJRR，光学/光子学旗舰（Optica、Light: Science & Applications、Laser & Photonics Reviews），Nature Electronics 与 Nature Biomedical Engineering，力学/流体/制造/航空，AIChE 及化工/过程与能源工程，以及材料工程与土木/交通旗舰。

本合集是 [`English-NaturalScience-Journal-Skills`](../English-NaturalScience-Journal-Skills/) 与 [`English-SocialScience-Journal-Skills`](../English-SocialScience-Journal-Skills/) 的工程姊妹包。与姊妹包一致：**每刊一张自洽的「定位 + 写作风格」skill**，外加 `en-engtech-journal-workflow` 路由卡。每张 skill 回答：*我的稿件是否对口、该如何框定、该刊期待什么方法/验证/可复现性、投稿前必须回官网复核哪些细则。*

## 覆盖

| 分组 | 数量 |
|---|--:|
| 电气·控制·通信·信号·电力（IEEE + Automatica） | 12 |
| 机器人·光子学·电子·生医工程 | 10 |
| 力学·流体·制造·航空 | 7 |
| 化工·过程·能源工程 | 7 |
| 材料工程·土木·交通 | 4 |
| **单刊 skill 合计** | **40** |
| 路由 workflow（`en-engtech-journal-workflow`） | 1 |

## 怎么用

1. **先路由**：从 `en-engtech-journal-workflow` 起步，按子学科、贡献类型、验证形态分类，拿到候选期刊短名单。
2. **再对口**：打开首选期刊的单刊 skill，检验 scope、框定、方法/验证门槛、写作风格与最可能的 desk-reject 触发点。
3. **最后复核官网**：每张 skill 都以 official-submission checklist 收尾。投稿前打开该刊当前作者须知（见 `resources/official-source-map.md`）—— **以官网为准**。

## 设计铁律（与姊妹包一致）

- **不写易变事实**：不写影响因子、接受率、ISSN、精确字数/版面费/编辑姓名 —— 这些在官网且会变。
- **不捏造文献**：文献一律泛指。
- **只用稳定惯例**：仅用持久的结构性事实（IEEE 双栏与文章类型体系、Automatica 的 IFAC 归属、Progress-in / Proceedings 系的综述性质、标准数据/代码/可复现性要求）辅助判断对口。
- **官网优先**：官网现行规定与 skill 冲突时，以官网为准。

## 许可

MIT © 2026 Bryce Wang，见 [LICENSE](LICENSE)。
