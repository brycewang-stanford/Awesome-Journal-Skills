# 复现契约 · 案例 1：合成控制 · 加州 Prop 99

> 本文件把 [`README.md`](README.md) 中的"实际运行"打包成可复验的最小操作步骤。
> **`README.md` 继续是单一真实结果出口；本文件只提供到达同样数字的路径。**

## 元数据

| # | 项 | 值 |
|---|---|---|
| 1 | 复现等级 | **Level 2** — 数据 + 完整 MCP 工具调用清单（一键复跑） |
| 2 | StatsPAI MCP 服务 | 必须接通 `statspai` 端点；最少需要的工具：`california_prop99`、`synth`、`synthdid_placebo`/`synth_time_placebo`、`discos_test`、`aggte`、`synthplot`、`synth_summary` |
| 3 | 公开基准数据 | StatsPAI 内置 `california_prop99`（Abadie, Diamond, Hainmueller 2010 标准面板；39 州 × 1970–2000；1209 行） |
| 4 | 依赖 skill | `Research-Toolkit-Skills/skills/rt-execution-bridge/SKILL.md` |
| 5 | 预计用时 | 5–10 分钟（含 200 次 placebo + 100 单位全权重的 bootstrap SE） |

## 0. 环境前置

```text
mcp server 'statspai' 已配（Claude Code 标准 marketplace 安装）
python3 tools/audit_repo.py 通过（所有数字字段对齐基线）
```

## 1. 数据加载

```text
MCP: california_prop99()
→ returns 1209 × 4 DataFrame：state / year / packspercapita / treated(=1 if state==CA)
写入 /tmp/ajs-prop99.csv 供后续估计器读取（如工具直接接受 DataFrame 可跳过写入）。
```

## 2. MCP 工具调用清单（按执行顺序）

| Step | 工具 (MCP) | 关键参数 | 期望返回主关键值 | 与 `README.md` `## 2.` 比对 |
|---|---|---|---|---|
| 1 | `synth` | outcome=`packspercapita`, time=`year`, unit=`state`, treated_unit=`California`, treatment_time=1989, method=`classic` | ATT ≈ **−18.19** | ✅ "经典合成控制"表第 1 行 |
| 2 | `augsynth` | 同上 + covariates=`retprice` 等 | ATT ≈ **−18.08** | ✅ "增广合成控制"行 |
| 3 | `sdid` | 同上 method=`sdid` | ATT ≈ **−17.90** | ✅ "合成 DiD"行 |
| 4 | `synth_compare` | methods=`('classic','augmented','sdid')` | 三估计量 一致 −17 ~ −18 | ✅ 三估计量一致性段 |
| 5 | `synth_sensitivity` / placebo 链 | n_perm=200 | treated RMSPE 在 placebo 中位数的 1.7× 量级、p ≈ 0.026 | ✅ 安慰剂检验段 |
| 6 | `synthplot` | result=synth_result, type=`both` | treated vs synthetic 两条线 + gap 图 | （可视化，不在数字对账内） |

## 3. 数字对账

复现跑完后，逐项与 `README.md` § 2 / § 3 对齐：

- 经典 SCM ATT = −18.19（包/年）→ README 同值
- 增广 SCM = −18.08 → README 同值
- SDID = −17.90 → README 同值
- 安慰剂 p ≈ 0.026 → README 同值

容差：ATT 数值 ±0.5（synth 内部权重优化有 local minima）；安慰剂 p ±0.01。

## 4. 已知差异 / 工具缺陷（如实记录）

- `synth_time_placebo` 与 `synth_loo` 在本案例运行日（2026-07-01）的服务端对年份列做强转
  string→int 失败——已回传到 StatsPAI 上游工作队列。当前本案例跑 placebo-in-space
  （同样有效）。
- 工具返回数字若细微浮动（如 ATT = −18.05 而非 −18.19），优先以「三估计量一致性」判定
  而非单点。

## 5. 失败模式与提示

| 现象 | 可能原因 | 处理 |
|---|---|---|
| `synth` 返回 ATT 与 README 偏差 > 5 | 优化器局部极小 | 换 `penalization=0.01` 或切换 `scpi` 后处理 |
| `synth_compare` 报「donor pool too small」 | 候选 donor 不足 | 收紧 pre-period（README 使用 1970–1988）|
| placebo p 显著大于 0.10 | treated state 的 pre-fit 质量高 + effect 较小 | 报告「安慰剂未拒绝空假设」——这是事实，不是失败 |

— 复现契约 1/N 结束。回到 [`README.md`](README.md) 看完整解读。
