# Showcase — 看得见的自动实证 / Automated Empirical Research, Executed

本目录是这个仓库「自动实证」能力的**证据层**：每条案例都是一次真实的端到端运行——
研究问题 → 设计识别 → 估计 → 稳健性审计 → 论文级结论——所有数字都来自
**实际执行的 StatsPAI MCP 工具调用**，不是伪代码、不是「示意输出」。

Every case here is a real end-to-end run executed through the StatsPAI MCP
execution layer that the skill packs in this repo wire into
([`shared-resources/empirical-methods/execution-with-mcp.md`](../shared-resources/empirical-methods/execution-with-mcp.md)).
Numbers are verbatim tool output, reproducible from the listed calls.

## 与 skill 体系的关系

- 各实证 depth pack 的分析类 skill 在「该跑出数字」的节点引用共享执行手册；
- [`Research-Toolkit-Skills/skills/rt-execution-bridge`](../Research-Toolkit-Skills/skills/rt-execution-bridge/SKILL.md)
  是跨期刊的执行入口；
- 本目录展示这条链路真实跑通后的样子——给用户看，也给 skill 作者当验收基准。

## 案例索引

| # | 设计 | 案例 | 数据 | 状态 |
|---|---|---|---|---|
| 1 | 合成控制 (SCM / ASCM / SDID) | [加州 Prop 99 禁烟法案](scm-california-prop99/README.md) | Abadie et al. 2010 基准面板 | ✅ 已运行 (2026-07-01) |
| 2 | 交错 DiD (Callaway–Sant'Anna + Honest DiD) | [Castle Doctrine 法案与凶杀率](did-castle-doctrine/README.md) | Cheng & Hoekstra 2013（Mixtape 公开数据） | ✅ 已运行 (2026-07-02) |
| 3 | 工具变量 (2SLS/LIML + AR/CLR/tF 弱 IV 面板) | [Card 1995 大学距离与教育回报](iv-card-college-proximity/README.md) | NLS Young Men（Mixtape 公开数据） | ✅ 已运行 (2026-07-02) |
| 4 | 断点回归 (rdrobust + rddensity + 安慰剂断点) | [差额胜选与议员投票行为](rdd-close-elections/README.md) | Lee–Moretti–Butler 2004（Mixtape 公开数据） | ✅ 已运行 (2026-07-02) |
| 5 | 双重机器学习 (DML-PLR，含方法边界示范) | [教育回报的 DML 估计](dml-returns-to-schooling/README.md) | 同案例 3 | ✅ 已运行 (2026-07-02) |

五条案例覆盖共享执行手册的全部五个设计族；案例 3/5 共用同一数据，
刻意演示「函数形式 vs 内生性」的方法论分界。

## 复现纪律

1. 数据来源必须写明（内置基准数据集或公开数据），并附加载方式。
2. 每一步记录实际调用的工具名与关键参数；输出数字**逐字**摘录。
3. 稳健性不是装饰：至少两条独立稳健性检查（备择估计量 / 安慰剂 / 敏感性）。
4. 运行中遇到的工具缺陷如实记录（见案例内「运行备注」），不粉饰。
