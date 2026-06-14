# 《管理科学学报》Skills

<p align="center">
  <img src="assets/cover.svg" alt="《管理科学学报》期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-管理科学学报-c0392b)](https://jmsc.tju.edu.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI%20%7C%20FMS--A-1f6feb)](https://jmsc.tju.edu.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《管理科学学报》(Journal of Management Sciences in China, JMSC)** 投稿的 agent skill 集合——**国家自然科学基金委员会管理科学部**与**天津大学**共同主办的数理/定量管理科学顶刊（月刊；ISSN 1007-9807；CN 12-1275/G3）。

本包**有观点**：不是通用管理写作工具箱，而是围绕该刊的核心门槛——**严谨模型 + 已证命题 + 可分析的算法 + 数值洞见，而非回归系数与政策口号**——专门构建。

已联网核实的期刊事实见 [`resources/journal-profile.md`](resources/journal-profile.md)（附来源链接）。

---

## 为什么要单独一套？

JMSC 是**数理刊**，门槛与经验因果刊（管理世界 / 经济研究）、理论建构刊（南开管理评论）显著不同：

| 约束 | 管理科学学报 | 含义 |
|------|--------------|------|
| 交付物 | 模型 + 证明 + 算法 | "发现 X 影响 Y"不对口 |
| 贡献 | 新模型/新性质/新算法 | 方法贡献，非政策 |
| 严谨度 | 假设显式、命题有证 | 有模型无证明 = 拒 |
| 算法 | 复杂度/收敛性分析 | "跑得快"不算分析 |
| 验证 | 数值/仿真研究 | 验证理论性质 + 给管理洞见 |
| 管理含义 | 从模型导出的决策规律 | 不是"加强完善推进"口号 |
| 摘要/篇幅 | ≤300 字；≤8000 字（综述 ≤12000） | 模型与结论前置 |
| 引用 | 序号〔1〕，按出现先后 | 文中作者-年份不合体例 |

---

## 十二个 Skill

| Skill | 作用 |
|-------|------|
| `jmsc-workflow` | 路由器——下一步用哪个；关键分叉是 数理 vs 经验实证 |
| `jmsc-fit-positioning` | 是否对口？回归+政策 / 问卷-SEM → 改投 |
| `jmsc-problem-formulation` | 形式化决策问题 |
| `jmsc-model-building` | 决策变量/约束/目标/假设全部显式 |
| `jmsc-proofs` | 命题/定理给出证明；逻辑完整 |
| `jmsc-algorithm` | 算法设计；复杂度/收敛性分析 |
| `jmsc-numerical-experiments` | 仿真验证理论性质 + 管理洞见 |
| `jmsc-behavioral-om` | 行为运作：实验设计、操纵检验、模型识别 |
| `jmsc-managerial-insights` | 从模型导出决策规律，而非政策口号 |
| `jmsc-notation-style` | 记号统一、假设显式、证明入附录 |
| `jmsc-submission` | 投稿前：公式/定理排版、投稿系统 |
| `jmsc-rebuttal` | R&R 回复信 |

---

## 快速开始

### 方式 A — Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install journal-of-management-sciences-in-china-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
mkdir -p ~/.claude/skills && cp -R skills/jmsc-* ~/.claude/skills/
# 或 Codex
mkdir -p ~/.codex/skills && cp -R skills/jmsc-* ~/.codex/skills/
```

---

> 编辑政策会变。请把这些 skill 当作有观点的启发式，而非官方政策——投稿前务必对照 [jmsc.tju.edu.cn](https://jmsc.tju.edu.cn/) 最新《投稿指南/来稿须知》核实。
