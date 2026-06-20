# 《管理科学》(Management Science) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Management Science 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Management%20Science-1b3a6b)](https://pubsonline.informs.org/journal/mnsc)
[![Publisher](https://img.shields.io/badge/publisher-INFORMS-1b3a6b)](https://www.informs.org/)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20UTD24-1f6feb)](https://pubsonline.informs.org/journal/mnsc)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《管理科学》(Management Science)** 投稿的 Agent 技能栈 —— 该刊是 **INFORMS**（美国运筹学与管理科学学会）的旗舰期刊，**1954 年**由其前身管理科学研究所 (TIMS) 创办。

本仓库是有立场的。它**不是**通用的"管理学写作"工具箱，而是围绕《管理科学》核心特征打造的**专用**技能栈：该刊刻意保持**双方法论**取向，把严谨的**分析/定量**建模（运筹学、最优化、随机过程、博弈与经济理论）与**实证**研究（计量经济学、实验室/田野实验、行为研究、数据科学）**并置**，覆盖所有职能领域 —— 会计、金融、市场营销、运营、信息系统、战略、创业、组织、行为经济学。稿件通过**学部/领域编辑 (Department / area-editor)** 结构分流，统一标准是：**严谨性，外加一个能跨学部传播的、与决策相关的贡献**。

> 仅描述持久规范。主编、投稿费、确切页数限制、学部名单及各项政策会变化 —— 请务必以 INFORMS PubsOnline 上《管理科学》官方投稿指南与 Code and Data Disclosure Policy 页面为准。

---

## 为什么需要单独的《管理科学》技能栈？

相比单一方法或纯理论期刊，《管理科学》的约束有本质差异：

| 约束维度       | 《管理科学》(Management Science)                                  | 含义                                                       |
|----------------|------------------------------------------------------------------|------------------------------------------------------------|
| 方法论         | **双方法论** —— 分析建模与实证研究地位等同                          | 选对赛道，并达到该赛道的严谨标准                            |
| 分流           | **学部/领域编辑**结构；学部编辑掌握初筛                            | 选错学部或文献，就送错了案头                                |
| 核心标准       | 严谨性**外加**能跨学部传播的、与决策相关的洞见                      | 模型再正确，若无管理含义，便不契合本刊宗旨                  |
| 契合度         | 须属于本刊，而非姊妹刊 **Operations Research / M&SOM / Marketing Science** | 学部编辑/副编辑先筛部门契合度与贡献                         |
| 评审           | **双盲匿名**；通过初筛后由副编辑邀请评审                            | 彻底匿名；会议论文版本须匿名披露                            |
| 透明度         | **代码与数据披露政策** + AsCollected 项目页                          | 第一天起就构建可一键重生结果的复现包                        |
| 费用           | 每次投稿 **$79**（2025-08-01 起），会员/低收入经济体/荣誉制豁免     | 缴费或申请豁免；荣誉制豁免无需说明理由                      |
| 篇幅           | 初投无硬性限制；偏好**短而聚焦**；受邀修改稿设页数上限              | 精简符号与正文；超出部分移入在线附录                        |
| 体例           | **作者—年份**引用；11 号字、1 英寸页边距；摘要 ≤ 250 词，3–5 关键词 | 将文献管理器配置为 name–date 风格                          |

通用的"科研写作"或"社科方法"技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/mgsci-skills
/plugin install mgsci-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/mgsci-skills.git
cd mgsci-skills

mkdir -p ~/.claude/skills && cp -R skills/mgsci-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/mgsci-* ~/.codex/skills/
```

### 第一条提示词

```
用 mgsci-workflow 告诉我，我的《管理科学》稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
mgsci-topic-selection（选题与契合度）
        ▼
mgsci-theory-development（理论/模型构建）
        ▼
mgsci-literature-positioning（文献定位）
        ▼
mgsci-methods（方法与设计）
        ▼
mgsci-data-analysis（分析与验证）
        ▼
mgsci-contribution-framing（贡献提炼）
        ▼
mgsci-tables-figures（图表）
        ▼
mgsci-writing-style（文风打磨）
        ▼
mgsci-submission（投稿前检查）
        ▼
mgsci-review-process（评审流程）
        ▼
mgsci-rebuttal（R&R 答复）
```

`mgsci-workflow` 是路由器 —— 它告诉你下一步用哪个技能，以及你处在哪条赛道（分析 vs 实证）。

---

## 技能清单

| 技能                           | 用途                                                                             |
|--------------------------------|----------------------------------------------------------------------------------|
| `mgsci-workflow`               | 路由器 —— 决定下一步用哪个技能，并判定所在赛道                                     |
| `mgsci-topic-selection`        | 决策相关性标准 + 学部契合度（对比 Operations Research / M&SOM / Marketing Science）|
| `mgsci-theory-development`     | 分析模型（假设 → 命题 → 比较静态）**或**先验假设                                   |
| `mgsci-literature-positioning` | 加入正确学部的对话；问题化而非找空白；作者—年份引用                                |
| `mgsci-methods`                | 让分析或实证设计匹配问题与学部标准                                                 |
| `mgsci-data-analysis`          | 证明+数值 **或** 识别/估计+稳健性；复现包                                          |
| `mgsci-contribution-framing`   | 能跨学部传播的、与决策相关的洞见；契合度论证                                       |
| `mgsci-tables-figures`         | 比较静态图/结果表；自洽、符号精简的图表                                            |
| `mgsci-writing-style`          | 前置结论、符号配以直觉解释、作者—年份体例                                          |
| `mgsci-submission`             | ScholarOne 七步投稿前检查：匿名化、费用/豁免、披露包                               |
| `mgsci-review-process`         | 学部初筛、高拒稿率、双盲评审、契合度门槛                                           |
| `mgsci-rebuttal`               | R&R 修改与逐条答复；页数上限与披露包更新                                           |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 分析工具（Gurobi / CPLEX / JuMP / Mathematica）与实证工具（Stata / R / Python / oTree / Prolific），以及数据与代码披露包配方
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 当前流程事实背后的 INFORMS/《管理科学》官方网址（访问于 2026-06-20）

---

## 已核实事实（请核对当前值）

- **出版方/沿革：** INFORMS；**1954 年**由前身管理科学研究所 (TIMS) 创办。
- **主编：** Christoph H. Loch，任期 **2024-01-01 至 2026-12-31**。
- **投稿系统：** ScholarOne，**mc.manuscriptcentral.com/mnsc**；七步上传。
- **摘要：** ≤ **250 词**；**3–5 个关键词**。
- **体例：** **作者—年份**正文引用（如 Norman 1977）；11 号字、1 英寸页边距；建议 PDF。
- **篇幅：** 初投无硬性限制；受邀修改稿 ≤ **47 页双倍行距**或 **32 页 1.5 倍行距**，在线附录不计入。
- **费用：** 每次原始投稿 **$79**（2025-08-01 起）；INFORMS 会员、低/中低收入经济体、荣誉制豁免。
- **透明度：** **代码与数据披露政策**（2019-06-01 生效，2026-04-20 修订）；作者投稿时提供 **AsCollected** 项目页 URL，含数值/计算工作的录用稿在生产前提供足以复现结果的数据、程序与细节。

详见 [`resources/official-source-map.md`](resources/official-source-map.md) 中的 INFORMS 官方来源链。

---

## 与姊妹刊 (INFORMS) 的差异

| 维度       | 《管理科学》                                       | Operations Research          | M&SOM                          | Marketing Science            |
|------------|----------------------------------------------------|------------------------------|--------------------------------|------------------------------|
| 核心贡献   | 能**跨学部传播**的、与决策相关的洞见                | 新的运筹方法/理论            | 供应链与服务运营               | 定量营销模型                 |
| 方法论     | 分析**与**实证并置                                  | 以分析/运筹为主              | 运营管理的分析+实证            | 消费者/企业行为模型          |
| 最佳契合   | 跨学部的管理科学结果                                | 运筹方法学进展              | 运营管理主题                   | 营销主题                     |

若核心贡献是缺乏管理含义的方法学，宜投 **Operations Research**；若是供应链/服务运营，宜投 **M&SOM**；若是定量营销，宜投 **Marketing Science**。

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引

---

## 许可证

MIT
