# AEJ：经济政策技能包（AEJ: Economic Policy Skills）

<p align="center">
  <img src="assets/cover.svg" alt="American Economic Journal: Economic Policy — Agent Skills 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AEJ%3A%20Economic%20Policy-8a5a12)](https://www.aeaweb.org/journals/pol)
[![Index](https://img.shields.io/badge/publisher-American%20Economic%20Association-1f6feb)](https://www.aeaweb.org/journals/pol)
[![Skills](https://img.shields.io/badge/skills-12-blue)](skills/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **American Economic Journal: Economic Policy（AEJ：经济政策，简称 AEJ: Policy）** 投稿的智能体技能包——
该刊是美国经济学会（AEA）旗下专注于**政策的经济学分析**的季刊。**12 个技能**覆盖从"政策问题优先"的选题，到可信的
准实验识别、福利／成本—收益解读、AEA 数据编辑可复现性检查，直至 R&R 回应信的完整生命周期，并随附一套**可运行的
Stata + Python 代码库**。

每个技能的主线都是**政策相关性**：选题与贡献框定突出**政策问题及其反事实／福利含义**；识别聚焦于**可信的准实验与
随机对照（RCT）政策评估**；写作风格则讲授如何在**不过度宣称**的前提下，把估计结果翻译成清晰的政策结论。

它**不是**通用的应用微观写作工具箱，而是一套 **AEJ: Policy 专属**的方法论技能栈。

官方依据核对于 **2026-06**，对照 AEA／AEJ: Policy 页面（期刊主页、投稿指南、AEA 数据与代码可得性政策、AEA 利益披露
政策）。详见 [`resources/official-source-map.md`](resources/official-source-map.md)。易变事实（投稿费、编辑名单、
具体格式上限）均标注 *(检索于 2026-06；以官网为准)*，无法由一手抓取确认者标注 **待核实**。

---

## 为什么需要独立的 AEJ: Policy 技能栈？

AEJ: Policy 的约束与领域型公共经济学期刊、其他 AEJ 子刊及 AER 都存在实质差异（标 **[官方]** 的行已对照 AEA 来源核实）：

| 约束 | AEJ：经济政策 | 含义 |
|---|---|---|
| 主线 | 一个带**福利／成本—收益／分配**解读的**政策问题** | 只有干净估计、缺乏政策"so what"即为不匹配 |
| 范围 [官方] | 政策的经济学分析（公共经济、环境/能源、健康、教育、劳动/福利、监管、发展/政策政治经济学） | 纯方法或无政策杠杆的应用微观不匹配 |
| 识别 | 对政策的可信准实验／RCT 评估 | 交错 TWFE／OLS+控制变量会被快速质疑 |
| 福利解读 | 估计 → MVPF／成本—收益／分配归宿 | 仅断言"这是福利改进"不够 |
| 评审 [官方] | 经 AEA 投稿系统**双盲**评审 | 正文与图表须匿名化 |
| 代码 [官方] | 必填 **JEL 代码 + 关键词** | 缺失即为格式错误 |
| 显著性 [官方] | **报告标准误／置信区间，不用星号**（AEA 体例） | 禁止 `***`，应报告 SE |
| 数据与代码 [官方] | AEA 数据与代码可得性政策；**AEA 数据编辑**在**发表前**核查；存储于 **openICPSR** | 复现包应边做边建 |
| 受限数据 [官方] | 至少保存 5 年、公开代码、记录来源；"按需提供"**不可接受** | 须给出真实的获取路径 |

> 以上每条事实均在 [`resources/official-source-map.md`](resources/official-source-map.md) 中核实并标注来源。
> 凡期刊未公布硬性上限（字数／页数）之处，工具一律按"经验法则——以现行 AEA 指南为准"处理，绝不作硬性断言。

---

## 快速开始

### 作为 Claude Code 插件

```
/plugin marketplace add brycewang-stanford/aej-economic-policy-skills
/plugin install aej-economic-policy-skills
```

随后即可发问，例如：*"我对税收抵免扩张的估计很干净，但审稿人说没有政策落点"*——`aejpol-workflow` 会把你路由到
`aejpol-theory-model`（福利解读）与 `aejpol-writing-style`（政策结论句）。

### 手动使用

让你的智能体指向本目录并按名调用技能（从 `aejpol-workflow` 开始），或直接阅读 [`skills/`](skills/) 下的
`SKILL.md` 文件。

---

## 默认工作流

```
aejpol-workflow（路由器）
   │
   ├─ aejpol-topic-selection ........ 锁定政策问题 + 福利落点
   ├─ aejpol-literature-positioning . 把贡献立为"更好的政策答案"
   ├─ aejpol-identification ......... 可信的准实验／RCT 政策评估
   ├─ aejpol-theory-model .......... 把估计映射为福利／成本—收益对象
   ├─ aejpol-robustness ............ 针对各类威胁守住政策数字
   ├─ aejpol-tables-figures ........ 图表（无星号）+ 一张政策头条图
   ├─ aejpol-writing-style ......... 把估计翻译为政策结论（引言/摘要最后写）
   ├─ aejpol-replication-package ... AEA 数据编辑／openICPSR 存档
   ├─ aejpol-referee-strategy ...... 预先化解审稿人会提的异议
   ├─ aejpol-submission ............ AEA 系统投稿前检查（匿名 + JEL + 披露）
   └─ aejpol-rebuttal .............. R&R 后的回应信与修改计划
```

---

## 12 个技能

| 技能 | 用途 |
|---|---|
| `aejpol-workflow` | 路由器——决定下一步调用哪个子技能 |
| `aejpol-topic-selection` | 政策问题匹配（对比 JPubE／AEJ:Applied／AER）+ 福利落点 |
| `aejpol-literature-positioning` | 把贡献立为"更锐利的政策答案" |
| `aejpol-identification` | 对政策的可信准实验／RCT 评估（DID／IV／RDD／RCT） |
| `aejpol-theory-model` | 把估计映射为福利／成本—收益／分配对象（充分统计量、MVPF） |
| `aejpol-robustness` | 针对设定、推断、识别威胁守住政策头条数字 |
| `aejpol-tables-figures` | AEA 体例图表（无星号）+ 一张自洽的政策头条图 |
| `aejpol-writing-style` | 在不过度宣称下把估计翻译为清晰的政策结论 |
| `aejpol-replication-package` | AEA 数据与代码可得性政策／AEA 数据编辑／openICPSR 存档 |
| `aejpol-referee-strategy` | 预判并化解 AEJ: Policy 审稿人的异议；校准预期 |
| `aejpol-submission` | AEA 系统投稿前检查：匿名、JEL、数据声明、披露 |
| `aejpol-rebuttal` | R&R 后的回应信策略与修改计划 |

---

## 资源

- [`resources/code/`](resources/code/) —— 可运行的 Stata + Python 因果推断骨架（已内置）。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) ——
  虚构的 AEJ: Policy 引言"前→后"改写示例。
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 按政策领域整理的、经网络核实的真实
  AEJ: Policy 论文（已验证 `10.1257/pol…` DOI）。
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的官方 AEA 链接。
- [`resources/external_tools.md`](resources/external_tools.md) —— 数据源、软件、福利／成本—收益工具。
- 共享中心：
  [`reviewer-objection-checklist`](../shared-resources/empirical-methods/reviewer-objection-checklist.md) ·
  [`reporting-standards`](../shared-resources/empirical-methods/reporting-standards.md)。

---

## 与同门期刊的差异

| | AEJ：经济政策 | AEJ：应用经济学 | J. Public Economics | AER |
|---|---|---|---|---|
| 核心诉求 | 广泛关注的政策问题 + 福利解读 | 识别驱动的应用微观 | 领域型公共财政贡献 | 一阶、广泛关注的成果 |
| 政策杠杆 | 必需（真实工具） | 可选／附带 | 常见但偏专业 | 可选 |
| 福利／成本—收益解读 | 期望（MVPF／归宿） | 不要求 | 常有，但面向专业读者 | 视情况 |
| 读者 | 广泛的 AEA 政策读者 | 应用微观读者 | 公共财政领域 | 顶级综合读者 |
| 篇幅 | 领域领先的政策论文 | 应用微观论文 | 领域论文 | 更长，top-5 规模 |
| 流程 | AEA 双盲、openICPSR 数据编辑 | AEA 双盲、openICPSR 数据编辑 | Elsevier、单/双盲 | AEA 双盲、openICPSR 数据编辑 |

> 当**政策结论就是头条**、且广泛的 AEA 读者会关心时，选 AEJ: Policy；当自然实验本身是重点时，选 AEJ:Applied；
> 当读者是公共财政领域时，选 JPubE；当贡献更大、更长时，选 AER。

---

## 相关链接

- 官方：[AEJ: Economic Policy](https://www.aeaweb.org/journals/pol) ·
  [AEA 数据与代码可得性政策](https://www.aeaweb.org/journals/policies/data-code)
- 本仓库同门技能包：`AEJ-Applied-Economics-Skills/`、`Quantitative-Economics-Skills/`。

---

## 许可证

[MIT](LICENSE) © 2026 Bryce Wang。
