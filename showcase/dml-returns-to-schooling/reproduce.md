# 复现契约 · 案例 5：双重机器学习 · 教育回报的 DML-PLR 估计

> 本文件把 [`README.md`](README.md) 中的"实际运行"打包成可复验的最小操作步骤。
> **本案例与案例 3 共用同一数据集，刻意演示「函数形式 vs 内生性」的方法论分界——**
> DML 放松的是函数形式假设，不是无混杂假设；面对能力偏误，灵活 ML 不能替代 IV。

## 元数据

| # | 项 | 值 |
|---|---|---|
| 1 | 复现等级 | **Level 2** — 数据 + 完整 MCP 工具调用清单 |
| 2 | StatsPAI MCP 服务 | 工具：`dml`（model=`plr`）、`interpret_result`、可选 `cate_eval`/`policy_tree`（若扩 heterogeneity） |
| 3 | 公开基准数据 | `scunning1975/mixtape` 的 `card.dta`（与案例 3 共享） |
| 4 | 依赖 skill | `Research-Toolkit-Skills/skills/rt-execution-bridge/SKILL.md` |
| 5 | 预计用时 | 2–4 分钟（DML 一次性 fit，无 bootstrap） |

## 0. 环境前置

```text
mcp server 'statspai' 已配
Python: pandas / numpy / scikit-learn（GradientBoosting 默认 nuisance）
```

## 1. 数据加载与协变量

```text
数据加载同案例 3：pd.read_stata('/tmp/mixtape/card.dta')
y       = lwage
treat   = educ
covariates = [exper, expersq, black, south, smsa]  # 不含工具 nearc4
n       = 3010
```

## 2. MCP 工具调用清单

| Step | 工具 (MCP) | 关键参数 | 期望返回主关键值 | 与 `README.md` § 2 比对 |
|---|---|---|---|---|
| 1 | `dml` | y=`lwage`, treat=`educ`, covariates=`[exper, expersq, black, south, smsa]`, model=`plr`, n_folds=5 | θ ≈ **0.0741**, SE ≈ 0.0037 | ✅ 主估计 |
| 2 | `interpret_result` | result_id=dml_result, audience=`researcher`, question="DML 与 IV 差多少？" | 自然语言解读「DML ≈ OLS ≈ 7.4%，IV ≈ 13.2%——分界正在能力偏误」 | （配套文档，不在数字对账内） |

## 3. 数字对账

- DML θ = 0.0741（≈ 7.41%/年），SE = 0.0037 → README 同值
- 与对照：OLS = 0.0740（案例 3）、IV = 0.1323（案例 3）
- **解读一致性**：DML ≈ OLS >> 与 IV 分离——这正是「函数形式 vs 内生性」的方法论分界

容差：θ ±0.003（GradientBoosting 默认 seed 复现稳定）。

## 4. 已知差异 / 工具缺陷

- `dml_sensitivity`（基于 Cinelli–Hazlett OVB）对 PLR 模型在 `ResultHandle` 解析上
  在服务端有兼容性问题（2026-07-02 复现）。本案例未跑 sensitivity——若需，
  可改用：`regress(y, treat + covariates, robust=hc1)` 拿到 result 后 `sensemakr`。
- `interpret_result` 抽样受 LLM 影响，措辞可不同，但含义一致。

## 5. 失败模式与提示

| 现象 | 可能原因 | 处理 |
|---|---|---|
| DML θ 与 OLS 偏差 > 0.005 | GradientBoosting 复杂度太低 | 加 `n_estimators=500` 或 `max_depth=5` |
| DML 报「nuisance R² 接近 0」 | 协变量无信号 | 检查 X 是否真与 y/treat 相关 |
| θ 与 README 偏差 > 0.01 | 随机 seed 漂移 | 锁 `random_state=0` 在 MCP 调用侧 |

## 6. 方法论教学点（如实保留）

本案例**刻意不**与案例 3 做横向加权综合。DML-PLR 估计的是条件期望函数「flexible」后的
偏线性系数 θ，与 IV 估计的「local」处理效应 τ_complier 不可同一而论：
- θ_DML ≈ θ_OLS（因为 OLS 控制函数形式后偏误不大，DML 同样如此）
- θ_IV ≠ θ_DML（IV 解的是同一问题上的内生性，不是函数形式）

这是案例 3 vs 案例 5 共享数据集要传达的核心——**别把 DML 当万能 IV 替代**。

— 复现契约 5/N 结束。回到 [`README.md`](README.md) 看完整解读。