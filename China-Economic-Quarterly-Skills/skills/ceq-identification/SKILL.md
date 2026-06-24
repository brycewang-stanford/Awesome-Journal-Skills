---
name: ceq-identification
description: Use when the identification strategy is the bottleneck for a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript — either a structural model with credible parameters, or a clean quasi-experiment (DID / IV / RDD / event-study). CEQ is the strictest Chinese econ journal here; identification assumptions must be made explicit and each defended. Stress-test the design before drafting exhibits.
---

# 识别策略（ceq-identification）

## 触发时机

- 实证主体仅 OLS + 控制变量，把相关性当因果
- 有处理/外生变异，但识别假设没写清、没逐条辩护
- 拿不准走结构估计还是准实验路线

## CEQ 的铁律：要么结构，要么准实验

CEQ 不接受"加一堆控制变量就声称因果"。两条合法路径：

- **结构估计**：微观基础清晰、识别假设显式、参数有经济含义、能做反事实。
- **准实验**：DID / IV / RDD / event-study，外生变异来源可信、识别假设可检验。

**识别假设必须显式写出，并逐条给经验支持**——这是 CEQ 与多数国内刊的最大差异。

## 设计优先级（强 → 弱）

1. 政策冲击 + DID（含交错/连续处理，须过 `ceq-modern-did`）
2. 断点回归（清晰政策门槛）
3. 工具变量（强工具 + 排他性论证）
4. 倾向得分匹配 + DID
5. 合成控制法
6. 双重机器学习 / 因果森林
7. OLS + 严密内生性讨论（仅在结构/理论实证文章中可接受）

## 分支自检

### DID（→ 详见 ceq-modern-did）
- [ ] 交错处理已用 Callaway–Sant'Anna / de Chaisemartin–D'Haultfœuille / Sun–Abraham
- [ ] 平行趋势：事件研究图必画（见 `ceq-figures`）
- [ ] 安慰剂（随机处理时点/对象）已做

### IV
- [ ] 第一阶段 F 报告，弱工具走 weak-IV-robust（见 `ceq-inference`）
- [ ] 排他性论证 ≥ 3 段（理论/制度/安慰剂）
- [ ] 报告了 reduced form；工具本身外生性有论证

### RDD
- [ ] McCrary / 密度操纵检验
- [ ] 最优带宽（CCT）+ ≥3 个带宽稳健性
- [ ] 协变量在断点处平滑

### 结构估计
- [ ] 识别假设逐条列出并辩护
- [ ] 参数有经济含义、估计稳定
- [ ] 提供反事实 / 福利分析

## 通用必查

- [ ] 识别假设**显式成文**，每条配经验支持
- [ ] 标准误聚类层级有理由（见 `ceq-inference`）
- [ ] 回应"被处理者预期/提前反应"问题
- [ ] 安慰剂/平行趋势/敏感性是**标配而非加分**

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《经济学(季刊)》是中文经济学旗舰，实证以因果识别为核心——交错 DID、IV、RDD 与机制检验。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 反模式

- "我们认为该政策外生"却无任何证据
- TWFE + 交错处理不讨论异质性偏误
- IV 用"外生事件 × 上一期内生变量"，说不清为何上一期不影响当期
- RDD 用截断带宽但不汇报带宽敏感性
- 把稳健性当摆设，不汇报不利结果

## CEQ 识别审稿的退稿触发表

下表把本刊审稿人最常据以退稿的识别缺陷，映射到"显式辩护应写什么"。CEQ 与多数国内刊的分水岭是：识别假设必须成文且逐条配经验支持。具体尺度因稿件而异，以编辑部最新稿约与外审为准。

| 识别缺陷 | 审稿人退稿理由 | 应写入的显式辩护 |
|----------|----------------|------------------|
| OLS+控制称因果 | 遗漏变量/反向因果未排除 | 改用准实验或结构，写明外生来源 |
| "政策外生"无证据 | 选择性试点未排除 | 用分批/门槛规则证明排序外生 |
| IV 排他性靠一句话 | 工具可能直接影响 Y | ≥3 段（理论/制度/安慰剂）论证 |
| RDD 不报带宽敏感 | 结论靠特定带宽 | CCT 最优带宽 + ≥3 带宽稳健 |
| 安慰剂/平行趋势缺位 | 把标配当加分 | 补齐并汇报，含不利结果 |

## 微型走查：把"政策外生"落到可辩护设计

虚构稿件《税收征管数字化与企业避税》。初稿写"金税三期上线是外生冲击"，但未辩护。按设计优先级与分支自检走一遍（示意）：

```
初稿主张：金税三期上线 → 企业避税 ↓（OLS+年份FE，β=-0.05**）
诊断：上线时点全国分批 → 有交错外生变异，但作者当成单一冲击
显式识别假设（逐条写出 + 经验支持）：
  H1 分批时点不由企业避税水平决定
      支持：上线顺序按省级税务系统就绪度，与企业避税无系统相关（平衡检验）
  H2 无预期性提前调整
      支持：事件研究前置系数 t=-3..-1 ∈ [-0.01,0.01] 跨 0
  H3 同期无其他征管改革混淆
      支持：控制"营改增"时点后系数稳定（0.05→0.047）
现代 DID：用 Callaway–Sant'Anna，ATT≈-0.043，与 OLS 同号但更可信
安慰剂：随机打乱上线时点 500 次，真实估计落在分布尾部（p<0.02）
```

走查要点：从"声称外生"到"三条假设各配一项经验证据"，识别才在 CEQ 站得住。注意 H1–H3 都成文并可检验——这是本 skill 的硬要求。下一步过 `ceq-modern-did` 处理交错异质性。

## 审稿人追问模式与本刊语境修法

- "你凭什么说政策外生？"——修法：把分批/门槛规则讲透，用平衡检验证明排序与结果变量无关，而非断言。
- "工具变量的排他性怎么保证？"——修法：给理论、制度、安慰剂三类论证，并报 reduced form。
- "稳健性只报了对你有利的？"——修法：汇报不利或边缘的稳健性结果，诚实优于粉饰（接 `ceq-rebuttal` 的回应纪律）。

## 输出格式

```
【识别策略】结构 / DID / IV / RDD / DML / 仅相关（需补）
【识别假设是否显式】是 / 否 <补>
【已完成检验】[平行趋势, 安慰剂, 弱工具, 密度, ...]
【缺失检验】[...]
【下一步】ceq-modern-did（若 DID）/ ceq-inference / ceq-mechanism
```
