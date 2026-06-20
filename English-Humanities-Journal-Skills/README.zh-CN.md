# 英文人文期刊 Skills（English Humanities Journal Skills）

<p align="center">
  <img src="assets/cover.svg" alt="英文人文期刊 Skills — 36 个旗舰人文期刊" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Index](https://img.shields.io/badge/index-AHR%20%C2%B7%20PMLA%20%C2%B7%20Phil%20Review%20%C2%B7%20Art%20Bulletin-1f6feb)](#)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **36 个旗舰英文人文期刊** 的 agent skill 合集 —— 专门补齐现有 breadth 合集偏薄的人文版图。覆盖历史（The American Historical Review、Past & Present、The Journal of Modern History）、哲学（The Philosophical Review、Mind、Noûs、Ethics、Philosophy & Public Affairs）、文学研究（PMLA、Critical Inquiry、New Literary History、Representations）、古典学（The Classical Quarterly、The Journal of Roman Studies）、艺术与建筑史（The Art Bulletin、Art History、October、The Burlington Magazine）、宗教学、语言学（Language、Linguistic Inquiry），以及音乐学与美学。

本合集是 [`English-SocialScience-Journal-Skills`](../English-SocialScience-Journal-Skills/) 与 [`English-NaturalScience-Journal-Skills`](../English-NaturalScience-Journal-Skills/) 的人文姊妹包。与姊妹包一致：**每刊一张自洽的「定位 + 写作风格」skill**，外加 `en-humanities-journal-workflow` 路由卡。每张 skill 回答：*我的论证是否对口该刊、该如何框定、该刊期待什么样的史料/文献功底与理论语汇、投稿前必须回官网复核哪些细则（文章类型、引用体例、双盲匿名、图像版权）。*

其中若干旗舰刊在母库另有自有**深度包**（The Art Bulletin、Critical Inquiry、PMLA、Mind、The American Historical Review）；本合集也以快速 fit 卡形态收录它们 —— 与 `american-economic-review` 同时双形态收录的做法一致。

## 覆盖

| 分组 | 数量 |
|---|--:|
| 历史 | 7 |
| 哲学 | 7 |
| 文学研究 | 6 |
| 古典学 | 2 |
| 艺术与建筑史 | 4 |
| 宗教学 | 3 |
| 语言学 | 4 |
| 音乐学与美学 | 3 |
| **单刊 skill 合计** | **36** |
| 路由 workflow（`en-humanities-journal-workflow`） | 1 |

## 怎么用

1. **先路由**：从 `en-humanities-journal-workflow` 起步，按子领域、贡献类型、研究路径分类，拿到候选短名单。
2. **再对口**：打开首选期刊的单刊 skill，检验 scope、论证框定、史料/文献功底要求、理论语汇、写作体例与最可能的 desk-reject 触发点。
3. **最后复核官网**：每张 skill 都以 official-submission checklist 收尾。投稿前打开该刊当前投稿须知与体例表（见 `resources/official-source-map.md`）—— **以官网为准**，出版社与体例会变。

## 设计铁律（与姊妹包一致）

- **不写易变事实**：不写影响因子、接受率、ISSN、精确字数/版面费/编辑姓名。
- **不捏造文献或引文**：学术脉络一律泛指；不对具体文章或在世学者的观点下断言。
- **只用稳定惯例**：仅用持久结构性事实（学会/出版社归属、各学科引用体例 Chicago/MLA/学科体例、双盲评审、图像版权）辅助判断对口。
- **官网优先**：官网现行规定与 skill 冲突时，以官网为准。

## 许可

MIT © 2026 Bryce Wang，见 [LICENSE](LICENSE)。
