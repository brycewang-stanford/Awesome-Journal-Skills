"""
event_study_plot.py —— 事件研究 / 平行趋势图（matplotlib，发表级）

输入：每个相对时点的系数与标准误（可从 Stata 估计后导出 CSV，或用 pyfixest 估计）。
风格对齐《经济研究》图形规范（er-tables-figures）：黑白 + 单主色、95% CI、
处理时点垂直虚线、基准期系数为 0、≥300 dpi、图题在图下方（投 Word 时手动置于图下）。
"""
from __future__ import annotations
import matplotlib.pyplot as plt
import pandas as pd

# 期望列：rel_time, coef, se（rel_time = -1 为基准期，coef=0, se=0）
es = pd.read_csv("output/event_study_coefs.csv")
es["ci_lo"] = es["coef"] - 1.96 * es["se"]
es["ci_hi"] = es["coef"] + 1.96 * es["se"]

plt.rcParams.update({"font.size": 11, "font.family": "serif",
                     "axes.linewidth": 0.8})

fig, ax = plt.subplots(figsize=(7, 4.2), dpi=300)
ax.axhline(0, color="black", lw=0.8)
ax.axvline(-0.5, color="0.4", ls="--", lw=1)            # 处理时点
ax.errorbar(es["rel_time"], es["coef"],
            yerr=[es["coef"] - es["ci_lo"], es["ci_hi"] - es["coef"]],
            fmt="o", color="#1f3b73", ecolor="#1f3b73",
            capsize=3, markersize=4, lw=1)
ax.set_xlabel("相对处理时点的年份")
ax.set_ylabel("处理效应")
ax.set_xticks(sorted(es["rel_time"].unique()))
fig.tight_layout()
fig.savefig("output/figures/event_study.png", dpi=300, bbox_inches="tight")
print("event_study.png 已保存（图题请在正文置于图下方）")
