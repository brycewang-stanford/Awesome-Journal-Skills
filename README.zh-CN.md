# Awesome Journal Skills

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

按**期刊**组织的社科 Agent Skill 包索引——涵盖选题、识别策略、引言写作、表格规范、复制包准备、修改回复。

每个 pack 都是**针对单一期刊**的方法论沉淀：它编码了某一本期刊的编委偏好、格式规范、识别标准和审稿文化。通用的"科研写作"Skill 包做不到这一点。

---

## 为什么要"按期刊"做 Skills？

不同顶刊对手稿的约束**显著不同**：

- **AER** 退稿点常在识别策略（TWFE、弱 IV、naive RDD）
- **《管理世界》** 退稿点常在缺中国制度背景
- **《经济研究》** 退稿点常在缺经典理论文献

一套"经济学写作"Skill 不可能同时编码这些差异。本索引下的每个 pack 都是按期刊定制的。

---

## Skill Pack 一览

| 期刊                                | 仓库                                                                                          | 学科                       | 状态    |
|-----------------------------------|---------------------------------------------------------------------------------------------|---------------------------|---------|
| **American Economic Review** + AER:Insights + AEJ 系列 | [AER-skills](https://github.com/brycewang-stanford/AER-skills)                              | 经济学（Top-5）             | v1.0    |
| **《管理世界》**                       | [management-world-skills](https://github.com/brycewang-stanford/management-world-skills)    | 管理学 + 应用经济           | v0.1    |
| **《经济研究》**                       | [economic-research-skills](https://github.com/brycewang-stanford/economic-research-skills)  | 经济学（中国 CSSCI 顶级）    | v0.1    |

---

## 如何使用

### 方式 A —— Claude Code 插件（推荐）

按需安装：

```bash
# AER
/plugin marketplace add https://github.com/brycewang-stanford/AER-skills
/plugin install aer-skills

# 管理世界
/plugin marketplace add https://github.com/brycewang-stanford/management-world-skills
/plugin install management-world-skills

# 经济研究
/plugin marketplace add https://github.com/brycewang-stanford/economic-research-skills
/plugin install economic-research-skills

/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/AER-skills.git
git clone https://github.com/brycewang-stanford/management-world-skills.git
git clone https://github.com/brycewang-stanford/economic-research-skills.git

mkdir -p ~/.claude/skills
cp -R AER-skills/skills/aer-* ~/.claude/skills/
cp -R management-world-skills/skills/mw-* ~/.claude/skills/
cp -R economic-research-skills/skills/er-* ~/.claude/skills/
```

### 第一条 Prompt

```
用 aer-workflow（或 mw-workflow / er-workflow）告诉我这份目标[期刊]的稿子下一步该做什么。
```

---

## Pack 选择速查

| 你的稿子是…                                  | 用这个 pack                  |
|------------------------------------------|---------------------------|
| 因果识别为主的实证文章，目标 top-5 经济学           | `AER-skills`              |
| 中国情境实证 + 政策可操作                          | `management-world-skills` |
| 中国情境 + 理论贡献突出                            | `economic-research-skills`|

---

## 路线图

后续可能加入的 pack（不做承诺）：

- **QJE / JPE / RES / Econometrica** —— top-5 经济学补充
- **《经济学（季刊）》 / CEQ** —— 偏方法论的中文经济学顶刊
- **《管理科学学报》** —— 中文管理学方法论顶刊
- **JF / JFE / RFS** —— 金融三大
- **AMJ / AMR / ASQ** —— 管理学三大

如果你希望优先支持某本期刊，欢迎在本 repo 提 issue。

---

## 贡献

每个 pack 都在自己的仓库里。要为某个 pack 贡献内容，请到对应仓库提 PR。要提议新增 pack，请在本仓库提 issue。

收录到本索引的质量门槛：

1. 必须按期刊定制（不是通用 pack）
2. 中英文双语 README（针对中国相关期刊）
3. 至少有一个 `*-workflow` 路由 skill
4. 含 plugin manifest（`.claude-plugin/plugin.json` + `marketplace.json`）
5. MIT 协议

---

## 相关项目

通用的科研写作 skill 包（与本索引定位不同）：

- [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills)
- [nature-skills](https://github.com/Yuan1z0825/nature-skills)

---

## License

MIT
