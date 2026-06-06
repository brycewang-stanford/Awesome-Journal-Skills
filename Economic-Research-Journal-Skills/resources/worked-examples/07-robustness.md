# 稳健性检验（发表级范文）

> 本文件为教学构造范例，数字为示意，非真实论文数据。

本节对应案例：**税收征管数字化与企业全要素生产率——来自"金税三期"工程的证据**。基准 TWFE 回归显示金税三期（GTP3）上线使企业全要素生产率（`tfp_lp`，Levinsohn-Petrin 法）显著提升，`D` 的系数为 0.041（se 0.013）；异质性稳健主结果（Callaway-Sant'Anna / Borusyak-Jaravel-Spiess）ATT≈0.038（se 0.011）。下面给出可直接放入论文的"稳健性检验"成稿。

本节**按每项检验所回应的识别威胁**组织，而非无差别罗列。每一段固定句式："为回应[威胁]，本文[做法]，结果见表 X，核心结论[不变 / 方向一致、量级相近]"。需强调的是，下列检验回答的都是同一个问题——**换一种方式做主回归，结论变不变**；它们既不是机制分析，也不是异质性分析（后两者分别见 [`05-mechanism.md`](05-mechanism.md)、[`06-heterogeneity.md`](06-heterogeneity.md)）。

---

## 一、稳健性检验（按识别威胁组织，成稿）

**测量误差：替换全要素生产率度量。** 基准回归以 Levinsohn-Petrin（2003）法估计企业全要素生产率，而生产函数估计对方法选择敏感，可能引入系统性测量误差并使处理效应被高估或低估。为回应这一威胁，本文分别改用 Olley-Pakes（1996）法与"OLS 残差法"（以普通最小二乘估计生产函数后取残差）重新度量被解释变量，再重做基准回归。结果见表 7，`D` 的系数落在 0.035—0.040 区间，均在 1% 水平显著，与基准的 0.041 方向一致、量级相近，核心结论不变；这表明本文识别出的效应并非源于特定生产率算法的人为偏误。

**同期政策干扰：剥离"营改增"的混淆。** 金税三期分批上线的 2013—2016 年，恰与"营改增"试点的全面铺开（2012—2016 年）在时间上高度重叠；若营改增独立地提升了企业效率，则基准估计会把营改增的效应错误地归因于金税三期。为回应这一威胁，本文构造营改增上线虚拟变量，并将其与年份固定效应交互一并纳入回归，以吸收营改增在不同年度的差异化冲击。结果见表 8，在控制营改增及其时间交互后，`D` 的系数仍为 0.036（se 0.012），在 1% 水平显著，与基准方向一致、量级相近，核心结论不变；金税三期的效应不能被同期营改增改革所解释。

**异质性处理效应偏误：用现代估计量替换双向固定效应。** 在交错上线情境下，双向固定效应（TWFE）会以"已处理单位互为对照"形成"坏比较"，当处理效应随时间或队列变化时，TWFE 估计量可能被负权重污染，乃至与真实平均效应反号。为回应这一威胁，本文先报告 Goodman-Bacon（2021）分解，结果显示本文 TWFE 估计的权重以"已处理 vs. 未处理"的好比较为主导、"晚处理 vs. 早处理"的坏比较权重很小，说明偏误风险有限；进一步，本文采用三种异质性稳健估计量重估平均处理效应：Callaway and Sant'Anna（2021）的组—时 ATT 聚合得 0.038、Borusyak, Jaravel and Spiess（2024）的插补估计得 0.040、Sun and Abraham（2021）的队列加权事件研究重估亦给出一致结果。结果见表 9，三者均与基准 TWFE 的 0.041 方向一致、量级相近，核心结论不变；本文效应不是 TWFE 负权重制造的假象。

**随机化处理（安慰剂）：真实效应是否为偶然。** 即便满足平行趋势，仍可能担心某些不可观测的、与上线时点偶然相关的省级冲击驱动了结果。为回应这一威胁，本文进行随机化安慰剂检验：在保持各省被处理这一事实不变的前提下，将各省金税三期的上线年份在样本期内随机重新指派，并重复估计 500 次。结果见图 1，500 个伪系数构成的核密度分布以 0 为中心、近似对称，绝大多数落在 [-0.02, 0.02] 区间内；而本文真实估计值 0.041（图中垂直虚线）位于该分布的最右尾，仅有不到 1% 的伪系数超过它（经验 p<0.01）。这表明基准结果难以由随机因素或与上线时点偶然相关的遗漏冲击解释，核心结论不变。

> **图 1：安慰剂系数分布（文字描述）。** 横轴为 500 次随机指派上线年份后重估得到的 `D` 系数，纵轴为核密度。分布形态钟形、峰值在 0 附近，向两侧迅速衰减；右侧以一条垂直虚线标注本文真实估计值 0.041，该虚线明显落在密度几乎为零的最右尾外侧，直观显示真实效应是安慰剂分布中的极端离群值。

**样本选择：匹配后再估与剔除特殊样本。** 处理组与控制组企业在规模、杠杆、盈利能力等特征上可能存在系统差异，若这些差异同时影响生产率增长，则基于全样本的估计会混入选择偏误。为回应这一威胁，本文先按企业特征（`size`、`lev`、`roa`、`age` 等）作倾向得分匹配，在共同支撑域内重做交错 DID（PSM-DID），得到 ATT 为 0.037；同时考虑到直辖市在征管资源与企业结构上的特殊性，剔除四个直辖市子样本后重估。结果见表 10，两套检验下 `D` 的系数均与基准方向一致、量级相近，核心结论不变；效应并非由处理组与控制组的可观测特征失衡或少数特殊地区驱动。

**少聚类推断：wild cluster bootstrap。** 本文的处理在省级层面发生，全样本仅覆盖 31 个省份，聚类数远低于渐近理论所要求的约 40 个门槛，常规聚类稳健标准误在此情形下会低估、导致过度拒绝。为回应这一威胁，本文按 Roodman et al.（2019）建议，在省级聚类下采用野群自助（wild cluster bootstrap）重新进行推断，并同时报告企业级与省级两种聚类的常规标准误以作对照。结果见表 11，野群自助给出 `D` 的 bootstrap p 值为 0.003，企业级与省级聚类下的系数与显著性均与之一致，核心结论不变；本文的显著性不是由少聚类下标准误被低估造成的假阳性。

**不可观测选择：Oster（2019）边界。** 即使加入了丰富的可观测控制变量，仍无法排除某些不可观测的企业禀赋同时影响是否（先）受处理与生产率水平，构成遗漏变量威胁。为回应这一威胁，本文计算 Oster（2019）的 δ 系数：以受控回归 R² 的 1.3 倍设定 R_max，估算"要使处理效应归零，不可观测选择相对于可观测选择需达到的重要性比例"。结果见表 12，δ=1.7>1，意味着不可观测变量需比本文已纳入的全部可观测变量重要 1.7 倍，才足以解释掉所估计的效应；按 Altonji, Elder and Taber（2005）以来的惯例，δ>1 表明结果对不可观测选择稳健，核心结论不变。

上述检验从测量、同期政策、估计量、偶然性、样本选择、推断与不可观测选择七个角度，对基准结果施加了独立而互补的压力测试，结论始终方向一致、量级相近，**上述检验表明核心结论稳健**。需再次强调，稳健性检验回答的是"主效应稳不稳"，而非"为什么有效应"（机制）或"在什么条件下更强"（异质性）——后两类分析及其结论分别见 [`05-mechanism.md`](05-mechanism.md) 与 [`06-heterogeneity.md`](06-heterogeneity.md)，不应混入本节。

---

## 二、稳健性检验一览

| 检验 | 回应的识别威胁 | `D` 系数 | se / p | 结论 |
|---|---|---:|---|---|
| 基准 TWFE | —（参照） | 0.041 | se 0.013 | — |
| 替换 TFP（OP 法、OLS 残差法） | 测量误差 | 0.035—0.040 | 1% 显著 | 不变 |
| 加营改增虚拟变量及时间交互 | 同期政策干扰 | 0.036 | se 0.012 | 不变 |
| Callaway-Sant'Anna | 异质性处理效应偏误 | 0.038 | se 0.011 | 不变 |
| Borusyak-Jaravel-Spiess 插补 | 异质性处理效应偏误 | 0.040 | 1% 显著 | 不变 |
| Sun-Abraham 重估 | 异质性处理效应偏误 | 方向量级一致 | 1% 显著 | 不变 |
| Goodman-Bacon 分解 | 异质性处理效应偏误（诊断） | 好比较权重主导 | — | 偏误风险有限 |
| 随机指派上线年份 500 次（安慰剂） | 随机化处理 / 偶然性 | 真实值 0.041 落最右尾 | 经验 p<0.01 | 不变 |
| PSM-DID | 样本选择 | 0.037 | 1% 显著 | 不变 |
| 剔除直辖市子样本 | 样本选择 | 方向量级一致 | 1% 显著 | 不变 |
| wild cluster bootstrap（省级聚类） | 少聚类推断 | 0.041 | bootstrap p=0.003 | 不变 |
| Oster（2019）δ 边界 | 不可观测选择 | δ=1.7>1 | — | 不变 |

> 注：表中"基准 TWFE"为参照行；R_max 取受控回归 R² 的 1.3 倍。正文聚焦回应审稿人最可能质疑的识别威胁，缩尾比例（1% vs. 5% vs. 不缩尾）、聚类层次逐项对照等次要敏感性检验置于附录，正文以一句话索引。

---

## 参考文献（节选，著者—出版年制）

- Altonji, J. G., Elder, T. E., and Taber, C. R. (2005). Selection on Observed and Unobserved Variables: Assessing the Effectiveness of Catholic Schools. *Journal of Political Economy*.
- Borusyak, K., Jaravel, X., and Spiess, J. (2024). Revisiting Event-Study Designs: Robust and Efficient Estimation. *Review of Economic Studies*.
- Callaway, B., and Sant'Anna, P. H. C. (2021). Difference-in-Differences with Multiple Time Periods. *Journal of Econometrics*.
- Goodman-Bacon, A. (2021). Difference-in-Differences with Variation in Treatment Timing. *Journal of Econometrics*.
- Levinsohn, J., and Petrin, A. (2003). Estimating Production Functions Using Inputs to Control for Unobservables. *Review of Economic Studies*.
- Olley, G. S., and Pakes, A. (1996). The Dynamics of Productivity in the Telecommunications Equipment Industry. *Econometrica*.
- Oster, E. (2019). Unobservable Selection and Coefficient Stability: Theory and Evidence. *Journal of Business & Economic Statistics*.
- Roodman, D., Nielsen, M. Ø., MacKinnon, J. G., and Webb, M. D. (2019). Fast and Wild: Bootstrap Inference in Stata Using boottest. *The Stata Journal*.
- Sun, L., and Abraham, S. (2021). Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects. *Journal of Econometrics*.

---

> 本节示范了 `er-robustness` 所要求的写法——按"回应何种识别威胁"组织、每段固定句式并报量级、安慰剂取分布形式（500 次）、少聚类用 wild cluster bootstrap、不可观测选择报 Oster δ>1，且全程与全库案例数字统一。完成稳健性交代后，下一步进入摘要写作：见 [`08-abstract.md`](08-abstract.md)，对应 `er-abstract`。
