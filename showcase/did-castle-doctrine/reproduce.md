# 复现契约 · 案例 2：交错 DiD · Castle Doctrine

> 本文件把 [`README.md`](README.md) 中的"实际运行"打包成可复验的最小操作步骤。

## 元数据

| # | 项 | 值 |
|---|---|---|
| 1 | 复现等级 | **Level 2** — 数据 + 完整 MCP 工具调用清单 |
| 2 | StatsPAI MCP 服务 | 工具：`callaway_santanna`、`aggte`（事件研究聚合，本案例下被绕开）、`honest_did_from_result`、`sensitivity_rr` |
| 3 | 公开基准数据 | `scunning1975/mixtape` 的 `castle.dta`：50 州 × 2000–2010 = 550 州-年观测 |
| 4 | 依赖 skill | `Research-Toolkit-Skills/skills/rt-execution-bridge/SKILL.md` + 实证深度包 `did-castle-doctrine`（共享执行手册 § 4.2） |
| 5 | 预计用时 | 3–5 分钟（无 bootstrap） |

## 0. 环境前置

```text
mcp server 'statspai' 已配
Python: pandas / numpy（数据加载）
```

## 1. 数据加载与预处理

```text
git clone https://github.com/scunning1975/mixtape /tmp/mixtape
pd.read_stata('/tmp/mixtape/castle.dta')             # 550 × N 面板
→ 派生 cohort 列：g = effyear if effyear>0 else 0   # 5 个采纳队列，29 个 never-treated
→ 结果变量：l_homicide = np.log(homicide_rate)
```

## 2. MCP 工具调用清单

| Step | 工具 (MCP) | 关键参数 | 期望返回主关键值 | 与 `README.md` § 2 / § 3 比对 |
|---|---|---|---|---|
| 1 | `callaway_santanna` | y=`l_homicide`, i=`sid`, t=`year`, g=`g`, estimator=`dr`, control_group=`nevertreated` | 总 ATT = **+0.1104**, SE = 0.0386, p = 0.0042 | ✅ 全文 ATT 行 |
| 2 | `callaway_santanna` | 同上 control_group=`notyettreated` | 总 ATT = **+0.1094**, SE = 0.0386, p = 0.0046 | ✅ "对照组换 not-yet-treated" 行 |
| 3 | `pretrends_test`（或逐组-时 ATT 手动 t-检验） | result=cs_result | pre-period ATTs jointly zero (p > 0.10) | ✅ "平行趋势直观证据"段 |
| 4 | `honest_did_from_result` | e=0, m_bar=magnitude 网格 | M ≈ 0.0189 起 CI 含零；M=0 时 CI [0.023, 0.171] | ✅ Rambachan–Roth 段 |

## 3. 数字对账

- 总 ATT = +0.1104（log points，≈ +11.7%），SE=0.0386, p=0.0042 → README 同值
- not-yet-treated 对照：ATT = +0.1094 → README 同值
- Rambachan–Roth 边界 M ≈ 0.0189 → README 同值

容差：ATT 数值 ±0.005（同一 estimator 复现）。

## 4. 已知差异 / 工具缺陷

- `aggte` 对 result_id 句柄的解析在服务端 `'str' object has no attribute 'detail'`（2026-07-02 复现）。
  本案例的事件研究聚合以主调用返回的组-时 ATT 明细替代——结果等价、更透明。这是
  StatsPAI 上游 P0 缺陷（已回传）。
- `honest_did_from_result` 句柄链路正常。

## 5. 失败模式与提示

| 现象 | 可能原因 | 处理 |
|---|---|---|
| 总 ATT 显著偏小（< 0.05） | `effyear=0` 行未剔除 | 强制 `g = np.where(effyear>0, effyear, 0)` |
| Honest DID 边界比 README 小得多 | `m_bar` 网格太粗 | 加 `n_grid=50`，重做一次 |
| not-yet-treated 组 ATT 跳到 0.02 | 数据集版本不一致（Mixtape 偶发 commit 改动） | 锁定 `mixtape` 仓库 commit hash |

— 复现契约 2/N 结束。回到 [`README.md`](README.md) 看完整解读。
