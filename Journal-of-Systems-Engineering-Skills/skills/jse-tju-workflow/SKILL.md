---
name: jse-tju-workflow
description: Use when a manuscript is being planned, drafted, revised, or prepared for submission to 《系统工程学报》 (Journal of Systems Engineering, Tianjin University), especially when the author needs to identify the paper’s systems-engineering strand, diagnose the current lifecycle stage, and choose the next jse-tju skill without confusing this journal with Systems Engineering Theory and Practice or a purely mathematical management-science venue.
---

# 《系统工程学报》全流程路由（jse-tju-workflow）

## 触发时机

把稿件先定位为“什么系统、哪种证据、处于哪一阶段”，再调用专门 skill。不要把 12 个 skill
顺序机械跑一遍，也不要把《系统工程学报》缩减为供应链建模刊。官网范围与 30 篇近年样本显示，
本刊横跨理论、方法和应用；稳定事实与动态投稿要求见
[`official-source-map.md`](../../resources/official-source-map.md)，内容画像见
[`source-basis.md`](../../resources/source-basis.md)。

## 输入诊断

1. 一句话研究问题：决策者/系统、冲突、目标、环境。
2. 系统草图：主体或组件、层级、状态、信息流、反馈、边界。
3. 核心交付：定理、机制、算法、仿真、预测、实证、工程接口中的哪一种。
4. 当前材料：只有想法、已有模型、已有结果、完整初稿、投稿前或收到审稿意见。

缺少系统草图时，不要直接润色摘要；先路由到 `jse-tju-topic-selection`。

## 六条研究主线

| 主线 | 本刊式识别信号 | 首要证据 | 优先 skill |
|---|---|---|---|
| 系统理论与复杂系统 | 状态演化、级联失效、稳定性、可靠性、复杂网络 | 机制、稳定/边界、仿真或数据构网 | `system-modeling` → `theory-analysis` |
| 优化、运筹与决策 | 跨组件约束、定位路径、资源配置、评价/控制 | 数学规划、求解、基线、规模梯度 | `system-modeling` → `algorithm-computation` |
| 网络、博弈与协同系统 | 多主体策略互动、契约、协同、信息不对称 | 均衡、阈值、比较静态、福利 | `system-modeling` → `theory-analysis` |
| AI、数据驱动和预测 | 动态过程、时变控制、风险预测、计算实验 | 样本外、强基线、防泄漏、解释 | `validation` → `robustness-reproducibility` |
| 社会经济与金融系统 | 空间/网络依赖、金融动态、政策或企业系统 | 识别/估计、系统机制、异质性 | `validation`，必要时接共享执行桥 |
| 工程、交通、环境和应急 | MBSE、交通网络、能源环境、灾害响应 | 场景约束、接口/算法、案例或仿真 | `topic-selection` → `system-modeling` |

交叉稿件只能指定一条**主线**和一条**支撑线**。例如“应急配送 + 元启发式”主线是工程应急，
算法是支撑；“宏观变量驱动波动预测”主线是金融动态，预测是支撑。若反过来写，容易出现
方法压过系统问题的拒稿风险。

## 按阶段选下一步

### 只有选题或摘要

- 系统边界不清：`jse-tju-topic-selection`
- 不确定是否投本刊：`jse-tju-fit-positioning`
- 现象明确但贡献只写“采用新算法”：先 `topic-selection`，不要进入算法

### 文献和模型阶段

- 综述是作者列表：`jse-tju-literature-review`
- 主体、状态、约束或信息结构含混：`jse-tju-system-modeling`
- 已有公式但不知道能证明什么：`jse-tju-theory-analysis`

### 求解与证据阶段

- 优化、仿真或算法稿：`jse-tju-algorithm-computation`
- 需要选择数值/仿真/真数据/案例/预测证据：`jse-tju-validation`
- 结果只在单组参数成立：`jse-tju-robustness-reproducibility`

### 成稿与投稿阶段

- 公式、图表、中英文信息和体例：`jse-tju-writing-tables-figures`
- 官网账号、文件、费用、原创性、版权和防诈骗：`jse-tju-submission`
- 收到编辑或审稿意见：`jse-tju-rebuttal`

## 路由决策

```text
if 系统边界/反馈/相互作用说不清:
    next = jse-tju-topic-selection
elif 目标刊仍在比较:
    next = jse-tju-fit-positioning
elif 变量/约束/信息时序未闭合:
    next = jse-tju-system-modeling
elif 核心主张缺少相称证据:
    next = jse-tju-theory-analysis 或 algorithm-computation 或 validation
elif 结果对参数/数据/随机性脆弱:
    next = jse-tju-robustness-reproducibility
elif 尚未按官网体例统稿:
    next = jse-tju-writing-tables-figures
else:
    next = jse-tju-submission
```

## 反模式

- **名称误导**：把《系统工程学报》当成《系统工程理论与实践》。两刊是不同期刊、不同官网、
  不同刊号；必须使用 `jse.tju.edu.cn`。
- **局部问题伪装系统**：单企业单变量问题加“系统”二字，但删除网络、层级、反馈后模型不变。
- **证据错配**：定理稿只做一张数值图；预测稿只报训练误差；算法稿只与弱基线比；实证稿没有
  处理空间、网络、动态或主体相互依赖。
- **经验判断冒充官方规则**：内容画像是选刊启发式，费用/格式/投稿入口必须回查 source map。

## 输出格式

```text
【目标刊】《系统工程学报》 / 仍需比较
【主线】六条主线之一
【支撑线】可选一条
【系统性一句话】边界 + 相互作用/反馈 + 系统级结果
【当前阶段】选题 / 综述 / 建模 / 理论 / 算法 / 验证 / 稳健 / 写作 / 投稿 / 返修
【下一 skill】仅一个 jse-tju-* 名称
【进入条件】调用前必须补齐的 1–3 项材料
【最大拒稿风险】一个可验证问题
【官方复核】本次是否涉及动态事实；若涉及，列 source-map ID
```

一次只给一个下一 skill；完成其输出条件后再回到本路由器。
