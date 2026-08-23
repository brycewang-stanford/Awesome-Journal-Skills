---
name: jse-tju-algorithm-computation
description: Use when designing, reporting, or auditing an exact, decomposition, heuristic, simulation, or learning-based solution route for 《系统工程学报》 (Journal of Systems Engineering, Tianjin University), including pseudocode, convergence or complexity, baselines, ablations, parameter settings, computing environment, scalability, and reproducible computational evidence.
---

# 《系统工程学报》算法与计算（jse-tju-algorithm-computation）

## 触发时机

当模型已定义但求解路线、算法增量或计算证据仍不完整时使用。算法必须回应系统结构带来的困难，
不能因为换用一个热门元启发式就自动成为贡献。本刊近年样本包含优化、网络、仿真和预测研究；
内容画像见 [`source-basis.md`](../../resources/source-basis.md)，可复现接口见
[`code/README.md`](../../resources/code/README.md)。

## 输入诊断

提供数学模型或计算任务、输入输出、实例规模、结构性质、精度/时间目标、候选算法、已有代码与结果。
先判定：

- 难点来自组合规模、非凸性、动态不确定、分布式信息还是仿真成本？
- 是否存在可作为小规模真值的精确方法或解析解？
- 新算法利用了哪项系统结构？
- 输出用于解释机制、求最优策略、预测还是支持工程决策？
- 失败、超时或不可行实例是否被保留？

没有明确计算任务时，不先写伪代码；模型若尚未闭合，返回 `jse-tju-system-modeling`。

## 求解路线选择

| 问题结构 | 首选路线 | 必须说明 |
|---|---|---|
| 小中规模线性/整数模型 | 商用或开源求解器、精确算法 | 最优间隙、时间限制、求解状态 |
| 可分结构 | Benders、列生成、拉格朗日或 ADMM | 分解依据、上下界、停止准则 |
| 动态/随机决策 | 动态规划、近似 DP、滚动优化 | 状态、情景、非预见性与误差 |
| 大规模组合问题 | 启发式/元启发式 | 可行性保持、基线、重复与统计 |
| 网络/动力系统 | 数值积分、事件仿真、谱/迭代方法 | 步长、稳定、初值和误差 |
| 数据驱动任务 | 统计/机器学习模型 | 数据切分、泄漏防控、强基线 |

复杂方法不是优先级；能用精确或标准方法回答问题时，不添加无必要的算法层。

## 处理步骤

### 1. 从结构推导算法

把模型结构与算法模块一一对应：耦合约束为何需要分解，网络稀疏性如何利用，动态状态如何更新，
异质主体如何并行。若模块删除后算法仍等同通用模板，谨慎声称算法创新。

### 2. 写可执行伪代码

列出输入、初始化、循环/递归、可行性修复、随机操作、终止条件和输出。符号与模型一致；每一步
能在实现中定位。不要用“更新解”“优化参数”掩盖关键过程。

### 3. 给理论或诊断保证

精确/分解方法报告有限收敛、界或最优性间隙；迭代方法报告收敛条件或经验残差；启发式无法给
全局保证时明确性质，并用小规模最优解、上下界和多次重复评价误差。

### 4. 设计基线

至少覆盖：简单决策规则、领域常用方法、最接近方法、可行时的小规模精确真值。统一数据、预算、
停止条件与硬件；不能让本方法获得更多时间或调参信息而不披露。

### 5. 做消融与参数实验

每个声称有贡献的模块至少一个消融。参数实验区分算法超参数与系统参数：前者检验稳定和调参成本，
后者解释系统机制。避免把超参数敏感性写成管理结论。

### 6. 报告规模和环境

列实例数、变量/约束/节点/时期规模、随机种子、重复次数、语言与版本、求解器与版本、CPU/GPU、
内存、时间限制、容差和并行设置。动态要求回查官方格式；计算环境本身按研究可复现性完整报告。

## 伪代码最小模板

```text
Algorithm: [名称]
Input: instance I, system parameters θ, tolerance ε, budget B, seed s
Initialize: feasible state/solution x0; incumbent; bounds/residuals
while stopping rule is false:
    update the system state or subproblem
    generate and evaluate candidate decisions
    preserve/repair feasibility
    update incumbent, bounds, residuals, or model
return decision x*, objective/trajectory, status, diagnostics
```

## 计算证据矩阵

| 主张 | 最低证据 |
|---|---|
| 解质量更高 | 强基线、同预算、间隙/统计区间 |
| 速度更快 | 多规模、同环境、时间与失败率 |
| 可扩展 | 规模梯度、内存、超时边界 |
| 模块有效 | 消融、交互消融、代价分析 |
| 结构有价值 | 与不利用结构的算法比较 |
| 结果稳定 | 多随机种子、分布、参数敏感性 |

## 微型示例

对动态应急配送，若提出“改进遗传算法”，需要说明滚动状态和公平约束如何进入编码、交叉与修复；
小规模与 MIP 最优解比较，大规模与滚动贪心和标准遗传算法同预算比较；报告中断强度、网络规模、
重复分布和超时。仅给一条收敛曲线不能支持优越性。

## 反模式

- 以算法名称新、参数多或曲线平滑证明创新。
- 基线过弱，或给本方法更多运行时间和调参机会。
- 只报告平均值，不报告波动、失败和不可行率。
- 伪代码与模型符号、实际实现不一致。
- 用单一实例声称可扩展。
- 不区分系统参数与算法超参数。

## 期刊专属拒稿风险

算法稿若不能解释系统结构为何要求该求解设计，会被视为通用算法套用；若只有计算改善而没有
系统级含义，也难以建立本刊专属性。算法证据与稿件类型的总体验证应交给 `jse-tju-validation`，
随机性和环境复现交给 `jse-tju-robustness-reproducibility`。

## 输出格式

```text
【计算任务与结构难点】
【路线选择及被排除方案】
【算法输入—步骤—输出】
【收敛 / 复杂度 / 诊断保证】
【基线与公平预算】
【消融与参数设计】
【规模梯度与失败边界】
【计算环境和复现清单】
【系统级解释】
【最大拒稿风险】
```
