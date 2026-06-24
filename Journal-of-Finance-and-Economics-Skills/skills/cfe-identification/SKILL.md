---
name: cfe-identification
description: Use when the empirical identification strategy is the bottleneck for a Journal-of-Finance-and-Economics manuscript — quasi-experimental designs (DID incl. staggered, IV, RDD, DML, PSM, event study). Stress-tests the design before drafting tables.
---

# 因果识别策略（cfe-identification）

## 触发时机

- 实证主体仅有 OLS + 控制变量
- DID 用了 TWFE 但没回应近年异质性处理批评（Goodman-Bacon, de Chaisemartin, Sun-Abraham, Callaway-Sant'Anna）
- IV 第一阶段 F 弱 / 工具变量内生性疑虑
- 用了 PSM 但没回应"匹配后仍可能存在不可观测异质性"
- 准备用双重机器学习但不确定怎么报告

## 设计优先级

《财经研究》编委对识别策略的偏好排序（强 → 弱），综合财经实证语境：

1. **政策 / 制度冲击 + DID（含 staggered / continuous treatment）**——最受欢迎，契合中国政策密集出台的现实
2. **断点回归（清晰的政策门槛，如规模、年龄、考核线）**
3. **工具变量（强工具 + 排他性论证）**
4. **倾向得分匹配 + DID（PSM-DID）**
5. **合成控制法（地区 / 城市级政策评估）**
6. **双重机器学习 / 因果森林（高维控制变量场景）**
7. OLS + 严密内生性讨论（在数据极难找到外生冲击、且理论机制清晰时可接受，但需充分论证）

## 分支路径

### 分支 A：DID

- 是否 staggered？→ 必须用 Goodman-Bacon 分解诊断 + Callaway-Sant'Anna 或 Sun-Abraham 稳健估计
- 平行趋势检验：事件研究图必须画（处理前各期系数不显著）
- 安慰剂：随机分配处理组 / 处理时点 500–1000 次
- 是否报告 Bacon 分解的"坏比较"权重？
- 连续型处理（continuous DID）需说明剂量定义与可比性

### 分支 B：IV

- 第一阶段 F **应足够强**（弱工具 → 用 Anderson-Rubin 或 weak-IV-robust CI）
- 排他性论证至少需要 3 段：理论 / 制度 / 安慰剂
- 是否报告了 reduced form？
- 工具变量本身的内生性论证？（避免"外生事件 × 上一期内生变量"硬凑）

### 分支 C：RDD

- 是否做了 McCrary / rddensity 操纵检验？
- 带宽：是否使用最优带宽（Calonico-Cattaneo-Titiunik）+ 至少 3 个带宽稳健性？
- 协变量在断点处的平滑性检验
- 模糊断点需报告第一阶段跳跃

### 分支 D：PSM / PSM-DID

- 匹配前后协变量平衡性检验（标准化偏差 < 10%）
- 共同支撑域（common support）说明
- 多种匹配方法稳健性（近邻 / 核 / 半径）
- 强调 PSM 只解决可观测选择，需配合 DID 处理不可观测异质性

### 分支 E：DML / 因果森林

- 报告 sample-split 数 + cross-fitting
- 报告 nuisance 函数选择（lasso / random forest / xgboost）
- 至少给出 3–5 种不同 ML 学习器的稳健性

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《财经研究》是财经类实证刊，企业/政策因果设计为主；识别与稳健性优先。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 必查清单

- [ ] 平行趋势 / 平滑性 / 弱工具 / 平衡性 检验都做了（按设计）
- [ ] 安慰剂检验做了（处理时点随机 / 处理对象随机）
- [ ] 主回归标准误聚类层次合理（个体 / 个体+时间 / 处理层级，如城市 / 行业）
- [ ] 是否回应了"被处理者预期 / 提前反应"问题
- [ ] 数据来源点名到数据库（不写"公开渠道"）

## 反模式

- TWFE + staggered 但不讨论异质性处理偏误
- IV 用"外生事件 × 上一期内生变量"——审稿人会问"为何上一期不影响当期"
- "我们认为该政策外生于企业决策"但没给证据
- RDD 用了截断带宽但不汇报带宽敏感性
- PSM 后直接当作随机实验，忽略不可观测选择

## 输出格式

```
【识别策略】DID / IV / RDD / PSM-DID / DML / 其他
【是否 staggered】是 / 否（是→是否做 Bacon 分解 + 稳健估计）
【已完成检验】[平行趋势, 安慰剂, 弱工具, 平衡性, ...]
【缺失检验】[...]
【聚类层次】...
【下一步】cfe-mechanism
```

## 《财经研究》二次操作审查

先锁定核心问题、识别链条、机制证据和可执行的政策含义，再判断稿件是否回应中文财经学术审稿人会同时追问选题政策价值、识别可信度和本刊栏目适配。

- **Operating pass**：Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **决策账本**：返回“主张 / 证据 / 阻断点 / 下一处改稿”四列，避免只给笼统建议。
- **改投比较**：对照《经济研究》用于更强理论/全国性贡献，《管理世界》用于管理实践与政策治理，《金融研究》用于金融专门议题；若相邻刊物拥有更强读者匹配，先建议改投而不是继续润色。
- **核验底线**：给投稿就绪判断前，必须重开 `resources/official-source-map.md`，列出仍可能改变建议的一个未核实事实。
