"""
event_study_plot.py —— Event-study / parallel-trends plot (matplotlib, publication-grade)

Input: per-relative-period coefficients and standard errors (export to CSV from a
Stata estimate, or estimate with pyfixest). Style: black-and-white + a single
accent color, 95% CI, vertical dashed line at the treatment point, base-period
coefficient = 0, >= 300 dpi, caption placed below the figure (when submitting to
Word, position the caption beneath the figure manually).
"""
from __future__ import annotations
import matplotlib.pyplot as plt
import pandas as pd

# Expected columns: rel_time, coef, se (rel_time = -1 is the base period, coef=0, se=0)
es = pd.read_csv("output/event_study_coefs.csv")
es["ci_lo"] = es["coef"] - 1.96 * es["se"]
es["ci_hi"] = es["coef"] + 1.96 * es["se"]

plt.rcParams.update({"font.size": 11, "font.family": "serif",
                     "axes.linewidth": 0.8})

fig, ax = plt.subplots(figsize=(7, 4.2), dpi=300)
ax.axhline(0, color="black", lw=0.8)
ax.axvline(-0.5, color="0.4", ls="--", lw=1)            # treatment point
ax.errorbar(es["rel_time"], es["coef"],
            yerr=[es["coef"] - es["ci_lo"], es["ci_hi"] - es["coef"]],
            fmt="o", color="#1f3b73", ecolor="#1f3b73",
            capsize=3, markersize=4, lw=1)
ax.set_xlabel("Years relative to treatment")
ax.set_ylabel("Treatment effect")
ax.set_xticks(sorted(es["rel_time"].unique()))
fig.tight_layout()
fig.savefig("output/figures/event_study.png", dpi=300, bbox_inches="tight")
print("event_study.png saved (place the caption beneath the figure in the text)")
