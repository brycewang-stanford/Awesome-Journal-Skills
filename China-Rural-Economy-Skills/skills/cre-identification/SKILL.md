---
name: cre-identification
description: Use when the empirical identification strategy is the bottleneck for a 《中国农村经济》 manuscript — micro-household / village-level quasi-experimental designs (DID, IV, RDD, PSM). Stress-tests the design and the rural-specific endogeneity before drafting tables.
---

# 因果识别策略（cre-identification）

## 触发时机

- 实证主体仅有描述统计 + OLS + 控制变量
- 自变量是农户的**自选择行为**（入合作社、外出务工、采用新技术、参与流转），但没处理自选择内生性
- DID 用了 TWFE 但没回应近年异质性处理批评（Goodman-Bacon, de Chaisemartin, Sun-Abraham, Callaway-Sant'Anna）
- IV 第一阶段 F 弱 / 工具变量排他性疑虑
- PSM 只做了匹配但没讨论"不可观测的选择性"

## 设计优先级

《中国农村经济》编委对农村微观研究的偏好排序（强 → 弱）：

1. **农村政策冲击 + DID（含 staggered / continuous treatment）**——如某项试点改革、确权、补贴政策的分批推行
2. **断点回归**——清晰的政策门槛（如贫困县划定线、补贴资格线、年龄门槛）
3. **工具变量**——强工具 + 排他性论证（处理农户自选择的核心武器）
4. **倾向得分匹配 + DID（PSM-DID）**——农村横截面 / 短面板的常见组合
5. **合成控制法**——村级 / 县级政策评估
6. OLS + 严密的自选择讨论（仅在有强外生性论证或结构 / 理论实证时可接受）

## 农村数据的内生性专项

农村微观研究最常见的内生性来源，审稿人必查：

- **自选择进入处理**：是否更"能干 / 风险偏好 / 资源禀赋好"的农户才入社 / 流转 / 务工？
- **反向因果**：是收入高才参与，还是参与带来收入？
- **测量误差**：农户自报的收入 / 土地面积 / 用工常有偏差
- **遗漏的村级 / 家庭固定特征**：村庄区位、宗族网络、家庭社会资本

针对性策略至少给出一条：固定效应 + IV / 准实验冲击 / 匹配 + 安慰剂 / 双稳健（Heckman 仅作辅助，不能单独立住识别）。

## 分支路径

### 分支 A：DID

- 是否 staggered？→ 必须用 Goodman-Bacon 分解 + Callaway-Sant'Anna 或 Sun-Abraham
- 平行趋势检验：事件研究图必须画
- 安慰剂：随机分配处理村 / 处理户 500–1000 次
- 是否报告 Bacon 分解的"坏比较"权重？

### 分支 B：IV

- 第一阶段 F **必须 ≥ 10**（弱工具 → 用 Anderson-Rubin 或 weak-IV-robust CI）
- 排他性论证至少需要 3 段：理论 / 制度 / 安慰剂；说明工具只通过处理变量影响农户结果
- 农村常用工具（地理 / 历史 / 政策外生）的内生性也要论证，不能"看起来外生就行"
- 是否报告了 reduced form？

### 分支 C：RDD

- 是否做了 McCrary / 密度检验（防止农户在门槛附近操纵，如人为划线进贫困户）？
- 带宽：最优带宽（Calonico-Cattaneo-Titiunik）+ 至少 3 个带宽稳健性
- 协变量平滑性检验

### 分支 D：PSM / PSM-DID

- 报告匹配前后的协变量平衡性检验
- 报告共同支撑域（common support）
- **明确讨论"不可观测选择性"**——PSM 只能处理可观测变量，需补 IV 或敏感性分析（Rosenbaum bounds）
- 优先 PSM-DID 而非纯横截面 PSM

### 分支 E：结构估计 / 理论实证

- 农户决策模型的微观基础是否清晰？
- 识别假设是否明确列出？
- 是否提供反事实（如政策模拟）？

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《中国农村经济》是三农实证刊，政策评估与微观面板为主；突出识别与选择性偏误处理。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 必查清单

- [ ] 平行趋势 / 平滑性 / 弱工具 / 匹配平衡 检验都做了
- [ ] 农户自选择内生性有明确处理（不是一句"我们假设外生"）
- [ ] 安慰剂检验做了（处理时点随机 / 处理村或户随机）
- [ ] 标准误聚类层次合理（农户 / 村 / 县 / 政策推行层级）
- [ ] 是否回应了"被处理农户预期"问题（如预期确权而提前调整行为）

## 反模式

- 纯描述性统计 + OLS 就下因果结论
- 自变量是农户自选择行为（入社 / 务工 / 流转）却不处理自选择
- TWFE + staggered 但不讨论异质性处理偏误
- PSM 只报匹配结果，回避"不可观测选择性"
- IV 用"村级历史变量"但不论证它不通过其他渠道影响当代农户结果
- RDD 用了门槛但不做密度检验（农户可能操纵分组）

## 输出格式

```
【识别策略】DID / IV / RDD / PSM-DID / 结构估计 / 其他
【自选择处理】方式：[...]
【已完成检验】[平行趋势, 安慰剂, 弱工具, 匹配平衡, ...]
【缺失检验】[...]
【聚类层次】农户 / 村 / 县 / ...
【下一步】cre-mechanism
```
