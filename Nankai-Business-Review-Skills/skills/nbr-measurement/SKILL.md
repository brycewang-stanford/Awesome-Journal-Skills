---
name: nbr-measurement
description: Use for measurement rigor in 《南开管理评论》 (Nankai Business Review) survey studies — reliability (Cronbach's α, composite reliability), validity (convergent via AVE, discriminant via Fornell-Larcker / HTMT), and common-method-bias diagnosis (Harman single-factor, marker variable, common latent factor). Use whenever a paper uses self-report scales, especially if measures were borrowed or single-source.
---

# 测量规范（nbr-measurement）

## 触发时机

- 用了量表（个体或企业层级自报）
- 量表照搬国外/他文，未做本土化与心理测量
- 单一来源、同一时点测自变量与因变量（CMV 高风险）

## 信度（Reliability）

- **Cronbach's α** ≥ 0.70（探索性 0.60 可商榷，需说明）
- **组合信度 CR** ≥ 0.70
- 报告每个构念的题项数、均值/标准差、来源出处

## 效度（Validity）

| 类型 | 指标 | 经验门槛 |
|------|------|----------|
| 收敛效度 | 标准化载荷显著且较高；**AVE** | 载荷 > 0.50（宜 > 0.70）；AVE > 0.50 |
| 区分效度 | Fornell-Larcker：√AVE > 构念间相关 | 或 **HTMT** < 0.85（严格 0.90） |
| 内容效度 | 量表来源、专家评议、预测试 | 翻译-回译，本土化适配 |
| 结构效度 | 验证性因子分析（CFA）拟合 | 见 nbr-survey-sem 拟合标准 |

## 量表本土化作业流

```
原始英文量表
→ 翻译（A 译者）→ 回译（B 译者，未见原文）→ 差异逐条核对
→ 专家评议（领域学者 + 企业实践者）确认语义与情境适配
→ 小样本预测试（如 n≈100）：跑 α、EFA、题项-总分相关
→ 删改题项留痕（删了哪条、为什么）→ 正式施测 + CFA
```

跳过任何一步都可能被本刊审稿人要求补做，尤以"回译记录"与"预测试删题留痕"最常被追索。

## 走查示例：借来的敬业度量表

设想稿件直接用 UWES-9 中文版测制造业一线工人敬业度：
- 风险点 1：原量表语境是知识员工，"工作让我有干劲"在流水线情境含义漂移——需专家评议加预测试确认
- 风险点 2：自变量（主管支持）与因变量（敬业度）同源同时点自报——CMV 高危，应分两时点（间隔数周）采集
- 风险点 3：只报 α=0.88、不报 CR/AVE——按本刊惯例补齐三件套并列表
处理后输出：α/CR 均 ≥ 0.70、AVE > 0.50、HTMT 最大值 < 0.85、时滞设计加标记变量检验——CMV 结论才立得住。

## 共同方法偏差（CMV / CMB）

自报、单源、同时点测量必须**事前防范 + 事后检验**：
- **事前**：自变量/因变量分时点或分来源；匿名；反向题；不同量尺
- **事后（任选并报告）**：
  - **Harman 单因子**：未旋转首因子方差 < 50%（最弱证据，别只用它）
  - **标记变量（marker variable）**：引入理论无关变量做局部调整
  - **共同潜因子（CLF / ULMC）**：加方法因子，比较载荷变化
- 结论要写明"CMV 不构成实质威胁"的依据，而非一句"做了 Harman"

## 执行桥（StatsPAI / Stata MCP）

把稳健性 battery **跑出来**，而不是只罗列。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《南开管理评论》是中国情境实证管理刊；实验用随机化推断 + 多重检验，问卷-SEM 与测量循其规范，定性案例另循其标准。

- **多结果 / 多设定：**`romano_wolf`（逐步 FWER）或 `benjamini_hochberg`，报告校正后阈值。
- **遗漏变量敏感性：**`oster_delta` / `sensemakr`。
- **推断：**少聚类用 `wild_cluster_bootstrap`；视依赖结构用 `twoway_cluster` / `conley`。
- **从一个 handle 复跑：**`audit_result(result_id)` 列出缺失检查及对应 `suggest_function`。
- **出表：**`etable` / `did_summary_to_latex` 直接从 handle 生成，不手抄数字。

正文留决定性检查，详尽 battery 进附录。执行链见 [JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。
## 自检清单

- [ ] 每个构念报告 α 与 CR（≥ 0.70）
- [ ] 报告 AVE（> 0.50）证收敛效度
- [ ] 用 Fornell-Larcker 或 HTMT 证区分效度
- [ ] 量表注明来源、是否本土化、预测试
- [ ] 自报数据做了 CMV 事前设计 + 至少一种事后检验（勿只靠 Harman）
- [ ] 控制变量的测量同样交代清楚

## 反模式

- 只报 α，不报 CR/AVE
- 借用量表不验证、不本土化，直接套
- CMV 只做 Harman 单因子就宣称"无偏差"
- 区分效度只看相关系数，不与 √AVE 比较

## 信效度呈现惯例（校准锚）

- 本刊已刊问卷文章普遍设"信效度检验"表：每构念一行，列题项数、α、CR、AVE
- 相关系数矩阵对角线放 √AVE（常加粗），便于 Fornell-Larcker 目检
- CFA 竞争模型比较表（单因子 / 合并因子 vs 目标模型）常作为区分效度与 CMV 的双重证据
- 表式细节以期刊最新投稿指南与近期刊文为准

## 评审质疑应对

| 质疑 | 应对 |
|------|------|
| "Harman 单因子不足为凭" | 补标记变量或 CLF/ULMC，并报告载荷变化幅度 |
| "量表是否适配中国企业情境" | 出示回译记录、专家评议结论与预测试删题留痕 |
| "两构念相关过高（r > 0.7），区分效度存疑" | 报 HTMT，并做合并因子的嵌套模型 Δχ² 比较 |
| "个体作答聚合到团队/企业层是否合理" | 报告 rwg 与 ICC(1)/ICC(2)，说明聚合所依据的构念组成模型 |

## 输出格式

```
【信度】构念 α / CR 列表（最低值 <…>）
【收敛】AVE 列表（最低 <…> 是否 > 0.50）
【区分】Fornell-Larcker / HTMT：通过□ 风险□
【量表来源】本土化□ 预测试□
【CMV】事前设计：<…>｜事后：Harman <%> + <标记/CLF> ｜结论：<…>
【下一步】nbr-survey-sem
```
