---
name: jqte-forecasting
description: Use when a 《数量经济技术经济研究》 (JQTE) manuscript makes a forecasting or prediction claim — macro forecasting, business-cycle / sentiment indices, mixed-frequency nowcasting, or model-based prediction. Enforces genuine out-of-sample evaluation (RMSE / MAE / directional accuracy / Diebold-Mariano), a proper benchmark, and a recursive / rolling design. The fastest desk-reject here is reporting in-sample fit only.
---

# 预测评估（jqte-forecasting）

## 触发时机

- 文章声称"能预测"某宏观/行业指标或景气
- 只报了样本内拟合（R²、拟合图），没有样本外检验
- 没有对比基准模型，无法说明"预测得更好"

## 本刊铁律：样本外评估 + 基准对比

**只报样本内拟合是高频拒因。** 预测的价值在样本外，必须有真正的 out-of-sample 设计和一个像样的基准。

## 必备四件套

1. **样本划分**：训练/验证/测试明确，或采用递归 (recursive) / 滚动 (rolling) 窗口，避免用全样本信息预测过去（信息泄漏）。
2. **基准模型**：至少与随机游走 (RW)、AR(p)、或一个简单基准比较——"比 naive 模型好"是底线。
3. **误差度量**：点预测报 RMSE / MAE / MAPE；方向性预测报方向准确率 (directional accuracy) / 混淆矩阵；必要时报区间预测覆盖率。
4. **统计显著性**：用 Diebold-Mariano（或 Clark-West，嵌套模型）检验预测差异是否显著，而非只看数字大小。

## 设计要点

- 预测期 (horizon) h 明确，多步预测报各 h 的误差，不只报 h=1
- 实时数据 vs 修订后数据：宏观预测应说明用的是哪种（real-time vs revised）
- 混频/nowcasting：信息集随时间更新的方式交代清楚
- 若做政策模拟/情景预测，区分"条件预测"与"无条件预测"

## 自检清单

- [ ] 有真正的样本外评估，不是样本内拟合
- [ ] 样本划分/滚动窗口无信息泄漏
- [ ] 至少一个基准模型（RW / AR）对比
- [ ] 报告 RMSE/MAE 或方向准确率，按 horizon 分列
- [ ] 用 Diebold-Mariano 等检验预测优势的显著性
- [ ] 数据修订/实时性问题有交代（宏观）

## 反模式

- 用全样本估计、再"预测"样本内的点，号称预测能力
- 只与自己的另一版模型比，不与 naive 基准比
- 报一个好看的 RMSE 却不做显著性检验
- 多步预测只报 h=1，回避长期表现
- 用修订后数据假装实时预测

## 本刊预测类审稿期待表

《数量经济技术经济研究》对预测论文的判分核心是"测得好"——不是模型多花哨，而是样本外是否真的赢过像样基准、赢得是否显著。下表把期待落成可核对项。

| 审稿维度 | 达标线 | 高频拒因 |
|----------|--------|----------|
| 样本外设计 | 递归/滚动窗口，无信息泄漏 | 只报样本内 R²/拟合图 |
| 基准对照 | 至少 RW 或 AR，必要时多基准 | 只跟自己另一版模型比 |
| 误差度量 | 按 horizon 分列 RMSE/MAE/方向准确率 | 只报 h=1 的好看数字 |
| 显著性 | DM（嵌套用 Clark-West）检验差异 | 仅看数字大小不检验 |
| 数据实时性 | 宏观说明 real-time vs revised | 用修订后数据冒充实时 |

## 微型走查：宏观预测模型比较（示意稿件）

设想《大数据因子增广模型对中国 CPI 的短期预测》（数字为示意）：

1. **预测对象 + horizon**：月度 CPI 同比，h=1/3/6。
2. **样本划分**：2005–2015 估计，2016–2023 滚动外推，每期重估，杜绝用未来信息。
3. **基准**：RW、AR(4)、传统少量变量 ARDL。
4. **误差度量**：FAVAR 在 h=1 的 RMSE 较 AR(4) 降约 15%、h=6 降约 8%（示意），方向准确率 h=1 约 0.72。
5. **显著性**：对嵌套的 AR(4) 用 Clark-West（示意 t=2.3，p<0.05），对非嵌套用 DM。
6. **实时性**：注明用经修订数据，并讨论实时数据下增益可能缩水——本刊审稿常追这一点。

```text
【预测对象+horizon】月度 CPI，h=1/3/6
【样本划分】2016–2023 滚动重估（无泄漏 □）
【基准】RW / AR(4) / ARDL
【误差度量】h=1 RMSE↓15%、h=6 ↓8%、方向准确率 0.72（示意）
【显著性】Clark-West t=2.3（嵌套）/ DM（非嵌套）
【实时性】revised，已讨论实时数据下增益衰减
【下一步】jqte-sensitivity / jqte-tables-figures
```

## 审稿人追问模式 + 本刊语境修法

- **"机器学习预测是不是黑箱，赢在过拟合？"** → 补严格样本外、报各 horizon 误差、做变量重要性或与传统模型对照；强调本刊要的是稳健可解释的预测增益，而非样本内炫技。
- **"为什么只报 h=1？"** → 多步预测全列，长期表现差也如实报，并讨论原因；回避长 horizon 是高频疑点。
- **"基准太弱赢得不算数"** → 加强基准（AR + 一个领域常用模型），说明赢过的是公认难超的 naive 模型。

## 校准锚点

- 本刊预测类已刊论文通常把"滚动外推 + 多基准 + DM/Clark-West + 分 horizon 误差表"作为标配，并讨论数据修订影响——可据此校准评估设计的完整度。
- 实时数据库可得性、官方指标修订规则等会变，**以编辑部最新稿约与数据发布机构口径为准**。

## 输出格式

```
【预测对象 + horizon】<指标>，h = <…>
【样本划分】训练/测试 / 递归 / 滚动（无泄漏 □）
【基准】RW / AR / 其他 <…>
【误差度量】RMSE □ MAE □ 方向准确率 □
【显著性】Diebold-Mariano / Clark-West □
【实时性】real-time / revised
【下一步】jqte-sensitivity / jqte-tables-figures
```
