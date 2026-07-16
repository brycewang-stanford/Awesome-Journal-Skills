# 《中国管理科学》投稿 Skills（Chinese Journal of Management Science）

<p align="center">
  <img src="assets/cover.svg" alt="《中国管理科学》封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-%E4%B8%AD%E5%9B%BD%E7%AE%A1%E7%90%86%E7%A7%91%E5%AD%A6-0d5c63)](https://www.zgglkx.com/)
[![Index](https://img.shields.io/badge/index-FMS%20T1%20%7C%20CSSCI-1f6feb)](https://www.zgglkx.com/CN/column/column1.shtml)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《中国管理科学》** 投稿的智能体技能栈。本刊由数学家**华罗庚教授于 1984 年 12 月创办**（原名《优选与管理科学》，1993 年更名，2014 年起为月刊），**中国科学院主管**，中国优选法统筹法与经济数学研究会与中国科学院科技战略咨询研究院共同主办（ISSN 1003-207X，CN 11-2835/G3）。

这套技能栈是**有立场的**：它不是泛用的"中文经管写作"工具箱，更不是定理证明栈。本刊承袭华罗庚"把数学方法用到国民经济中去"的传统，要的是**应用建模 + 算例/实证**——把真实管理情境刻画成模型，解出来、算出来、跟基准比出来，最后落成可执行的管理启示。因此本栈按本刊三条现役主线（优化建模 / 数据驱动预测 / 金融工程实证）分路把关，硬性执行 12 页红线与公式编译器体例，并在选题阶段就拦下两类经典错配：定理厚的稿件该去《管理科学学报》，"回归 + 政策叙事"该去《管理世界》。

> 只固化稳定规范。主编、费用、系统与模板会变——投稿前务必以官网 **www.zgglkx.com** 最新页面为准（本包事实核验日期 2026-07-16，来源见 [`resources/official-source-map.md`](resources/official-source-map.md)）。

---

## 为什么需要单独的《中国管理科学》技能栈？

本刊的约束与数理姊妹刊、经验实证类管理期刊都不同"种"：

| 约束 | 《中国管理科学》 | 含义 |
|------|------------------|------|
| 使命 | 真实管理情境中的应用建模（华罗庚传统） | "教科书模型 + 中国背景"过不了审；情境必须塑造模型 |
| 交付物 | 模型 + 算法/方法 + 有标定的计算或真数据检验 | 纯回归与纯定理都不对口 |
| 主线 | 优化 / 预测 / 金融工程三线并行 | 建议必须分线给；检验门槛各不同 |
| 篇幅 | 论文不超过约 12 页（官方口径） | 图表密度是设计约束，不是事后压缩 |
| 体例 | 规定章节顺序、100–200 字摘要、中图分类号、公式编译器 | 形式审查先于内容审查 |
| 文献 | 顺序编码制，仅限直接阅读过的公开文献 | 引用顺序必须跟随论证顺序 |
| 通道 | 仅官网 www.zgglkx.com；编辑部反复警示代投 | 不接受邮箱或第三方投稿 |
| 费用/周期 | 公开口径互相冲突——本包如实标「待核实」 | 投前复核公告，勿信缓存数字 |
| 共同体 | NSFC 管理科学部 A 级重要期刊；FMS T1；中国管理科学学术年会 | 外审专家来自中文 OR/MS 共同体，须对话其近年成果 |

通用"科研写作"包，甚至姊妹刊《管理科学学报》的技能包，都不覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/cjms-skills
/plugin install cjms-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/cjms-skills.git
cd cjms-skills

mkdir -p ~/.claude/skills && cp -R skills/cjms-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/cjms-* ~/.codex/skills/
```

### 第一条指令

```
用 cjms-workflow 告诉我：我的《中国管理科学》稿件下一步该用哪个 skill。
```

---

## 默认工作流

```text
cjms-topic-selection（选题与对口）
        ▼
cjms-literature-review（双线综述）
        ▼
cjms-model-formulation（问题刻画与建模）
        ▼
cjms-solution-algorithm（求解与算法 · 优化线）
        ▼
cjms-empirical-validation（实证检验 · 预测/金融线）
        ▼
cjms-numerical-experiments（数值实验与算例）
        ▼
cjms-managerial-insights（管理启示）
        ▼
cjms-tables-figures（图表公式）
        ▼
cjms-writing-style（体例统稿）
        ▼
cjms-submission（投稿 preflight）
        ▼
cjms-rebuttal（外审回复）
```

`cjms-workflow` 是路由器——先判断稿件属于哪条主线（优化建模 / 数据驱动预测 / 金融工程实证），再指认当前阶段该用的 skill。

---

## 技能一览

| Skill | 用途 |
|-------|------|
| `cjms-workflow` | 路由器——按主线与阶段指认下一个 skill |
| `cjms-topic-selection` | 选题三问、栏目对位、姊妹刊分流 |
| `cjms-literature-review` | 中文/国际双线综述；可命名的方法增量 |
| `cjms-model-formulation` | 情境-模型映射；变量/约束/目标；编号且有辩护的假设 |
| `cjms-solution-algorithm` | 求解路线决策表；伪代码、性质分析、基线对比 |
| `cjms-empirical-validation` | 数据溯源、滚动样本外、基准电池、DM/MCS 检验 |
| `cjms-numerical-experiments` | 参数标定三来源、实验矩阵、敏感性与边界 |
| `cjms-managerial-insights` | "条件—决策—效果"三段式；口号黑名单 |
| `cjms-tables-figures` | 三线表、公式编译器、算法框、12 页密度管理 |
| `cjms-writing-style` | 规定章节顺序、100–200 字摘要、中图分类号、结语、顺序编码文献 |
| `cjms-submission` | zgglkx.com 投稿 preflight；费用/周期诚实口径；清单与结构模板 |
| `cjms-rebuttal` | 意见分类、先改稿后回复、逐条修改说明 |

### 资源层

- [`resources/external_tools.md`](resources/external_tools.md) —— 分主线工具箱（求解器与标准测试集、分解-预测-集成软件栈、金融数据库、顺序编码文献工具）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 全部已核实事实的官方来源（核验 2026-07-16），费用/主编/匿名模式等的「待核实」诚实台账
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 经官网 URL 核实的代表作清单（主题×形态），含姊妹刊辨析
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— 改写前 → 改写后的本刊式引言示范（虚构班轮联盟舱位互换论文）
- [`resources/code/`](resources/code/) —— 随包提供的 Stata + Python 因果推断骨架（服务实证支线）

---

## 与姊妹中文期刊的差异

| 维度 | 中国管理科学 | 管理科学学报 | 系统工程理论与实践 | 管理世界 |
|------|--------------|--------------|--------------------|----------|
| 主办 | 中科院 + 优选法研究会 | NSFC 管理科学部 + 天津大学 | 中国系统工程学会 | 国务院发展研究中心 |
| 交付物 | 应用模型 + 计算/实证 | 模型 + 证明 + 算法 | 系统方法论 + 工程应用 | 实证、案例、政策 |
| 衡量标准 | 方法在真实情境中管不管用 | 方法的数理严谨性 | 系统工程贡献 | 经验/政策贡献 |
| 致命错配 | 纯回归、纯定理 | 无可证性质的应用 | 单一企业业务问题 | 无经济叙事的模型 |

论文的落点若是定理，隔壁《管理科学学报》才是家；若是回归系数加政策话语，去《管理世界》；若是一个改变真实决策的可用方法，投本刊。

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊技能包总索引
- [Journal-of-Management-Sciences-in-China-Skills](https://github.com/brycewang-stanford) —— 数理姊妹刊《管理科学学报》技能包

---

## 许可证

MIT
