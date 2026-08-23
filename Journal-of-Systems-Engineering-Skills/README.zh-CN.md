# 《系统工程学报》Skills

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-系统工程学报-c0392b)](https://jse.tju.edu.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《系统工程学报》(Journal of Systems Engineering)** 投稿的 agent skill 集合。期刊由中国系统工程学会主办、天津大学承办。

本包不是通用论文写作工具箱，而是依据官网定位和近年目录，为系统理论与复杂系统、优化运筹与决策、网络博弈与协同、数据驱动与预测、社会经济与金融系统，以及工程应用建立的投稿生命周期工具包。

稳定事实和易变投稿要求见 [`resources/official-source-map.md`](resources/official-source-map.md)，近年内容依据见 [`resources/source-basis.md`](resources/source-basis.md)。

---

## 为什么要单独一套？

只有当系统边界、相互作用、反馈或跨层约束实质改变模型与证据时，稿件才具有本刊专属性。

| 相邻期刊 | 出现以下情况时改投 |
|---|---|
| 《系统工程理论与实践》 | 核心是更宽泛的经济管理或政策研究，系统结构不是主要增量 |
| 《管理科学学报》 | 核心交付是模型、定理证明和算法理论，应用主要作例证 |
| 《中国管理科学》 | 核心是局部管理决策模型与计算应用，而非系统级机制 |
| 《系统工程与电子技术》 | 雷达、通信、航天、装备体系或硬件性能是主对象 |
| 《控制与决策》 | 控制器、观测器、状态估计或控制算法性能是主贡献 |
| 《运筹与管理》 | 成熟运筹方法解决局部排程、路径或库存问题，系统机制可删除 |

以上是基于公开证据的分流启发式，不是编辑部规则。

---

## 十二个 Skill

| Skill | 作用 |
|---|---|
| `jse-tju-workflow` | 按阶段和研究主线路由 |
| `jse-tju-fit-positioning` | 判断匹配度并给出可操作改投规则 |
| `jse-tju-topic-selection` | 构造可检验的系统问题 |
| `jse-tju-literature-review` | 连接国内、国际与本刊近年文献 |
| `jse-tju-system-modeling` | 闭合边界、变量、约束、信息和可解性 |
| `jse-tju-theory-analysis` | 设计命题、证明、比较静态和边界 |
| `jse-tju-algorithm-computation` | 设计算法与公平计算证据 |
| `jse-tju-validation` | 匹配数值、仿真、数据、案例、预测、优化或实证证据 |
| `jse-tju-robustness-reproducibility` | 压力测试并记录复现条件 |
| `jse-tju-writing-tables-figures` | 按当前模板统一写作、公式和图表 |
| `jse-tju-submission` | 核对官网投稿入口、文件和流程 |
| `jse-tju-rebuttal` | 修改正文并逐条回复 |

默认路由：

```text
workflow → fit-positioning → topic-selection → literature-review
→ system-modeling → theory-analysis / algorithm-computation
→ validation → robustness-reproducibility
→ writing-tables-figures → submission → rebuttal
```

只调用稿件当前阶段需要的 Skill。

---

## 快速开始

### Claude Code 插件

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install jse-tju-skills
/reload-plugins
```

### Claude Code 或 Codex 手动安装

```bash
mkdir -p ~/.claude/skills && cp -R skills/jse-tju-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jse-tju-* ~/.codex/skills/
```

从 `jse-tju-workflow` 开始，提供研究问题、系统边界、核心交付、当前阶段和可用证据。

---

## 来源与维护

- [`official-source-map.md`](resources/official-source-map.md)：官方事实、易变投稿信息、未核实项和使用位置。
- [`source-basis.md`](resources/source-basis.md)：六期三十篇公开元数据形成的内容画像。
- [`exemplars/library.md`](resources/exemplars/library.md)：仅含公开元数据，不保存论文全文。
- [`external_tools.md`](resources/external_tools.md)：研究与执行工具。
- [`code/README.md`](resources/code/README.md)：复现接口，不复制大型模板。

投稿政策和格式会变化，投稿前须以期刊官网当前信息为准。

## License

[MIT](LICENSE)
