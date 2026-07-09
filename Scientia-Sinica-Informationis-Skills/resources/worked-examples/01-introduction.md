> **教学示例（虚构）**：下文的论文、方法、数据与全部数字均为**虚构**，仅用于演示
> 《中国科学：信息科学》(Scientia Sinica Informationis, SSI) 的中文写作范式。
> 不陈述任何真实论文事实，也不杜撰任何刊物政策。对应技能：
> [`ssi-writing-style`](../../skills/ssi-writing-style/SKILL.md)、
> [`ssi-topic-selection`](../../skills/ssi-topic-selection/SKILL.md)、
> [`ssi-experiments`](../../skills/ssi-experiments/SKILL.md)。

# 范例：一篇 SSI 论文的"中英文摘要 + 引言"（改写前 → 改写后）

本例演示 `ssi-writing-style` 的**首页弧线**：
**信息科学问题 → 现状为何不足 → 贡献（方法/理论/发现）→ 证据（实验或理论依据）→
对信息科学的意义**；并体现 SSI 的三条硬要求：贡献是**有科学价值的信息科学贡献**、
证据**与主张相称**、**中英文双语摘要**均达到发表水平。

**虚构论文**：《面向边缘设备的低功耗神经网络推理加速器设计与验证》。
虚构成果：一种在资源受限边缘芯片上以确定性时延完成推理的加速器架构与调度方法。

---

## 改写前（埋没科学贡献 —— 典型初稿摘要 + 引言）

> **摘要.** 深度学习改变了信息技术。我们设计了一种神经网络加速器，采用先进工艺并结合
> 一种新颖的数据流。实验表明我们的方法在一个数据集上取得了很高的性能，优于基线，
> 展示了 AI 芯片的巨大潜力。
>
> **Abstract.** Deep learning has changed information technology. We design an accelerator
> and it achieves high performance, outperforming baselines.
>
> **引言.** 神经网络很重要。很多工作研究加速器。本文提出一种加速器，在数据集上评估，
> 结果很好。第 2 节相关工作，第 3 节方法，第 4 节实验，第 5 节结论。

**问题（对照 `ssi-writing-style` / `ssi-topic-selection` / `ssi-experiments`）：**

- **首页没有信息科学问题**：以"深度学习改变 IT"和一句性能取胜开场，而非边缘推理领域
  从业者能识别的具体难题。SSI 要求把**科学价值与创新点**放在前面。
- **主张形状错误**："很高的性能"缺少与主张相称的量化证据（时延确定性、功耗、面积）。
- **英文摘要过于单薄**：SSI 要求中英文双语摘要，英文摘要是国际可见性的关键，不能敷衍。
- **创新高度不明**：若把这套数据流换成已有方法，科学结论是否仍成立？读者无法判断。
- **过度路标**：用"第 X 节讲 Y"的罗列代替论证。

---

## 改写后（SSI 弧线 —— 问题 → 不足 → 贡献 → 证据 → 意义）

> **摘要.** 边缘设备上的神经网络推理要求**确定性时延**与**极低功耗**，而现有加速器多为
> 吞吐量优化、时延抖动大，难以满足实时控制类应用。本文提出 **DetEdge** 加速器架构与
> 一种时延感知的静态调度方法，在编译期给出可证明的时延上界。在 3 类典型边缘网络与
> 2 款硅后原型上评估：在满足确定性时延约束下，能效较对比架构显著提升（报告均值与置信区间），
> 并给出面积-功耗-时延的帕累托分析与消融实验。*（问题 → 不足 → 贡献 → 真实证据 → 意义，
> 全部落在首页。）*
>
> **Abstract.** Neural-network inference on edge devices demands **deterministic latency**
> and ultra-low power, yet throughput-oriented accelerators exhibit latency jitter unsuitable
> for real-time control. We present **DetEdge**, an accelerator architecture with a
> latency-aware static scheduler that yields a provable latency bound at compile time.
> Across three edge networks and two post-silicon prototypes, DetEdge improves energy
> efficiency under a hard-latency constraint, with Pareto and ablation analyses reported
> with confidence intervals. *(problem → gap → contribution → real evidence → significance.)*
>
> **引言.** *（第 1 段——从业者问题，开门见山。）* 在实时控制与工业感知场景，边缘推理的
> 瓶颈往往不是峰值吞吐，而是**时延的确定性**：一次超时可能导致控制回路失稳。因此工程问题
> 不是"能否更快"，而是**"能否在给定功耗与面积预算下，保证每次推理的时延上界"**。
>
> *（第 2 段——现状为何不足。）* 现有加速器以吞吐量为目标，依赖动态调度与缓存，
> 时延分布长尾；已有确定性方案又牺牲能效或通用性。没有工作在**真实硅后原型**上，
> 同时给出可证明时延上界与有竞争力的能效。
>
> *（第 3 段——贡献，以信息科学主张陈述。）* 本文有两点贡献：其一，**DetEdge 架构**
> 将计算与访存解耦，使时延可在编译期静态确定；其二，**时延感知静态调度算法**，
> 在满足时延上界的前提下最小化能耗，并给出复杂度与最优性分析（理论依据）。
>
> *（第 4 段——证据，逐条对应主张。）* 每个主张都配证据：时延上界由形式化推导给出并在
> 原型上实测验证；能效提升在 3 类网络、2 款原型上报告均值与置信区间；帕累托前沿说明
> 面积-功耗-时延的权衡；消融实验隔离调度算法的独立贡献。数据、RTL 与测试脚本见补充材料。
>
> *（第 5 段——意义与威胁。）* 我们直言主要威胁：原型工艺与商用节点存在差异，
> 故补充了跨工艺的敏感性分析而非直接外推。意义在于：为实时边缘智能提供了
> **可证明时延 + 高能效**的设计路径。第 2 节述问题与背景；第 3 节架构；第 4 节调度算法；
> 第 5 节评估；威胁与结果一并讨论，不单列走过场。*（简短路标，不过度签名。）*

---

## 为何"改写后"达到 SSI 门槛

对照技能清单：

- **科学贡献在首页**：摘要与第 1 段先给出边缘推理的确定性时延难题与工程问题，
  再谈架构细节（`ssi-writing-style`："先讲信息科学贡献"）。
- **证据与主张相称**：主张是"可证明时延 + 高能效"，证据即形式化推导 + 硅后实测 +
  置信区间 + 帕累托/消融，而非单一数据集的一个数字（`ssi-experiments`）。
- **中英文双语摘要均达标**：英文摘要不是中文的机翻残句，而是可独立阅读的高质量摘要，
  满足 SSI 对国际可见性的要求（`ssi-writing-style`）。
- **创新高度可辨**：把静态调度换成动态调度，"可证明时延上界"这一科学结论会消失——
  说明贡献不可替代（`ssi-topic-selection` 的换核检验）。
- **威胁就地论证**：工艺差异这一构念效度威胁在第 5 段点明并以敏感性分析约束，
  而非留到结尾走过场（`ssi-writing-style`）。

> 下一步：见 [`../exemplars/library.md`](../exemplars/library.md) 了解 SSI 各栏目
> （评述/论文/快报）的写作范式坐标，以及 [`../official-source-map.md`](../official-source-map.md)
> 的投稿政策与中英文姊妹刊关系说明。
