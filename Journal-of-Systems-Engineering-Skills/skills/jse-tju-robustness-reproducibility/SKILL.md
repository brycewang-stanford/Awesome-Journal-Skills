---
name: jse-tju-robustness-reproducibility
description: Use when stress-testing and packaging the reproducibility evidence for 《系统工程学报》 (Journal of Systems Engineering, Tianjin University), including parameter sensitivity, initial conditions, alternative models and metrics, extreme scenarios, Monte Carlo repetition, random seeds, software versions, data and code statements, and explicit failure boundaries.
---

# 《系统工程学报》稳健性与可复现性（jse-tju-robustness-reproducibility）

## 触发时机

当主验证已经建立，需要判断结论是否依赖单组参数、初值、模型、指标、随机样本或软件环境时使用。
稳健性不是在正文末尾追加若干表，而是对核心主张的有效域做压力测试；可复现性则让读者能够重建
输入、执行与输出。工具接口建议见 [`code/README.md`](../../resources/code/README.md)。

## 输入诊断

收集核心主张、主验证设计、数据/实例、参数表、代码入口、随机过程、软件环境、已有敏感性结果和
数据共享限制。先建立依赖清单：

- 哪些参数来自数据、文献、校准或任意设定？
- 哪些结论可能受初始状态、网络结构或情景生成影响？
- 哪些模型选择、变量口径或指标存在合理替代？
- 哪些步骤含随机性或人工处理？
- 哪些材料不能公开，原因和可替代复核路径是什么？

若主张本身未与证据匹配，先回到 `jse-tju-validation`，不要用稳健性掩盖主验证缺失。

## 五层压力测试

| 层 | 检验对象 | 典型动作 |
|---|---|---|
| 参数 | 系统参数、算法超参数、估计参数 | 单因素、联合设计、分区扫描 |
| 状态 | 初值、网络拓扑、需求/冲击路径 | 多初值、重抽样、结构扰动 |
| 模型 | 函数形式、行为规则、误差结构 | 替代模型、嵌套/非嵌套比较 |
| 指标 | 效率、风险、公平、预测/拟合指标 | 替代定义、阈值与分组 |
| 情景 | 正常、极端、故障、分布漂移 | 压力测试、反事实、尾部情景 |

不是每层都必须出现；选择能击中主张最脆弱假设的测试。

## 处理步骤

### 1. 建立主张—脆弱点映射

对每条主张写出最可能推翻它的参数、初值、模型选择和数据处理。优先测试能改变结论方向、阈值、
排序或可行性的因素，不把计算预算耗在无关小数位。

### 2. 设计敏感性

参数范围要有现实、数据或归一化依据。非线性与交互明显时使用联合设计、网格、拉丁超立方或全局
敏感性；不要仅将所有参数机械地上下浮动同一比例。区分数值误差与实质变化。

### 3. 检验初值和极端情景

动态/仿真稿覆盖多个吸引域、网络密度、冲击强度和恢复能力；优化稿覆盖容量紧张与宽松、规模和
不确定性；预测/实证稿覆盖时间、群体、区域与分布漂移。报告失稳、不可行和性能崩塌。

### 4. 使用替代模型和指标

替代模型应对应合理竞争解释，而不是随意更换估计器。替代指标要检验结论是否只依赖一种口径。
若结论变化，解释差异来自测量、识别还是系统机制，不用“总体稳健”掩盖。

### 5. 控制随机性

为数据切分、情景生成、初始化和随机算法分别设种子。Monte Carlo 或启发式重复报告次数、分布、
均值/中位数、区间和失败率。种子不是消除随机性，而是允许重现特定运行。

### 6. 固化环境和入口

列操作系统、语言、依赖、求解器、硬件、线程、容差和命令入口；保存配置、实例清单和原始到分析
数据的步骤。不要提交论文全文、凭据或无许可数据；受限数据给出字段字典和获得/复核方式。

### 7. 写失败边界

明确在哪些范围结论反转、模型失稳、算法超时、预测失准或政策含义不再成立。失败边界是系统工程
贡献的一部分，不应从图表中删除。

## 复现清单

```text
entrypoint: [command / notebook order]
inputs: [data, instances, schemas, licenses]
configuration: [system parameters, solver/model settings]
randomness: [seed locations, repetitions]
environment: [OS, language, packages, solver, hardware]
outputs: [tables/figures/result files and checksums if used]
expected diagnostics: [tolerance, range, status]
restricted material: [reason and independent verification path]
failure boundaries: [known non-convergence/infeasibility/drift]
```

## 微型示例

网络级联模型的主结论是“共享提高韧性”。应联合改变共享精度、网络集中度和恢复容量，使用多组初值
和冲击节点重复；用替代韧性指标检验排序；报告高集中、低容量区间中共享导致同步响应而反转的情形。
仅把传播率上下浮动 10% 并重复一张图，不足以支持稳健。

## 反模式

- 将任意参数统一上下浮动 5% 或 10%，不说明范围依据。
- 只保留支持主结论的随机种子。
- 只报平均改善，不报尾部、不可行和失败率。
- 代码依赖本机绝对路径、手工步骤或未记录的数据清洗。
- 声称“数据可按需提供”，却不说明许可与复核路径。
- 将结论反转写成数值异常。

## 期刊专属拒稿风险

复杂系统、网络、仿真、优化和预测结果常对结构与初值敏感；忽略这些边界会让系统级结论显得过度
概括。仓库不复制大型代码模板，也不意味着无需复现说明。官方是否要求特定附件属于动态事实，
必须查 [`official-source-map.md`](../../resources/official-source-map.md)。

## 输出格式

```text
【核心主张—脆弱点矩阵】
【参数与范围依据】
【初值 / 结构 / 极端情景】
【替代模型与替代指标】
【随机种子、重复与统计】
【环境、入口、输入与输出】
【数据/代码可用性说明】
【反转、失稳、超时和外推边界】
【正文 / 附录 / 仓库分配】
【最大拒稿风险】
```
