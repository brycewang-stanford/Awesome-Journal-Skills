# 复现契约 · 案例 4：断点回归 · 差额胜选与 ADA 得分

> 本文件把 [`README.md`](README.md) 中的"实际运行"打包成可复验的最小操作步骤。

## 元数据

| # | 项 | 值 |
|---|---|---|
| 1 | 复现等级 | **Level 2** — 数据 + 完整 MCP 工具调用清单 |
| 2 | StatsPAI MCP 服务 | 工具：`rdrobust`、`rddensity`、`rdplot`、`honest_did_from_result`/`rd_honest` |
| 3 | 公开基准数据 | `scunning1975/mixtape` 的 `lmb-data.dta`：美国众议院 1946–1995，13,577 行；列：`score / margin / democrat / ...` |
| 4 | 依赖 skill | `Research-Toolkit-Skills/skills/rt-execution-bridge/SKILL.md` |
| 5 | 预计用时 | 3–5 分钟 |

## 0. 环境前置

```text
mcp server 'statspai' 已配
Python: pandas / numpy
```

## 1. 数据加载与构造

```text
git clone https://github.com/scunning1975/mixtape /tmp/mixtape
pd.read_stata('/tmp/mixtape/lmb-data.dta')
→ 派生 margin = democrat − 0.5（运行变量：民主党得票率 − 0.5）
→ sharp RD：treated = 1 if margin ≥ 0 else 0
→ y = 当期 score（ADA 得分 0–100）
→ 13,577 行（有效样本）
```

## 2. MCP 工具调用清单

| Step | 工具 (MCP) | 关键参数 | 期望返回主关键值 | 与 `README.md` § 2 / § 3 比对 |
|---|---|---|---|---|
| 1 | `rdrobust` | y=`score`, x=`margin`, c=0, kernel=`triangular`, bwselect=`mserd` | Conv = **46.18**（SE 2.15）；Robust = **43.85**（SE 3.14）；95% CI = [37.70, 50.00]；h = 0.0491 | ✅ 主估计表 |
| 2 | `rddensity` | x=`margin`, c=0, h=None（auto） | T = 0.363，**p = 0.717** | ✅ 操纵检验段 |
| 3 | `rdrobust`（安慰剂 c = +0.10） | y=`score`, x=`margin`, c=+0.10 | estimate ≈ −0.92（p ≈ 0.878） | ✅ 安慰剂 c=+0.10 行 |
| 4 | `rdrobust`（安慰剂 c = −0.10） | y=`score`, x=`margin`, c=−0.10 | estimate ≈ +8.45（p ≈ 0.033） | ✅ 安慰剂 c=−0.10 行 |
| 5 | `rdplot` | x=`margin`, y=`score`, c=0, binselect=`esmv` | 双侧局部多项式拟合 + CI 带 | （可视化，不在数字对账内） |

## 3. 数字对账

- Conventional = 46.18、Robust = 43.85、h = 0.0491 → README 同值
- CJM 操纵检验 p = 0.717 → README 同值
- 安慰剂 c=+0.10: −0.92；c=−0.10: +8.45 → README 同值

容差：ATT ±0.5；h ±0.005。

## 4. 已知差异 / 工具缺陷

- `rdplacebo` 工具在本数据上导致服务端连接中断（2026-07-02 复现一次）。本案例改用
  同一 `rdrobust` 工具在 ±0.10 假断点手工执行——结果等价且更透明。
- 本案例用当期 `score`；LMB 原文核心表用 t+1 期 ADA 区分「选举效应 vs 收敛效应」，
  量级略有差异（原文 20–48 分），方向与解释一致——README § 运行备注已如实记录。

## 5. 失败模式与提示

| 现象 | 可能原因 | 处理 |
|---|---|---|
| 操纵检验 p 显著（< 0.05） | 真实操纵 或 数据有少数「刚好赢」聚类 | 用 `rdplotdensity` 复检；若是真操纵，应弃用 sharp RD |
| 安慰剂 c=−0.10 显著但 |0.10 不显著 | 已报告：ADA 数据在深负差额区有质点；如实记录 |
| 带宽 h 跳到 ≤ 0.02 | 样本中贴近断点数据稀少 | 锁 `bwselect=mserd`，禁用 `cerrd` |

— 复现契约 4/N 结束。回到 [`README.md`](README.md) 看完整解读。