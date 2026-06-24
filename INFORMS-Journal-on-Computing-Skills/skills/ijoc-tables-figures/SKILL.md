---
name: ijoc-tables-figures
description: Use when the computational exhibits — performance profiles, runtime-vs-size plots, and results tables — are dense, misleading, or do not answer the question for an INFORMS Journal on Computing (IJOC) manuscript. Designs exhibits that make the computational claim legible; it does not generate the underlying results.
---

# Performance Exhibits (ijoc-tables-figures)

## When to trigger

- Your results are in giant tables of times and gaps that no reader can parse
- You are comparing several methods across many instances and need a single legible exhibit
- A referee says the figures "do not show the claimed advantage" or are hard to read
- You need to show **scaling** and cannot tell whether the growth is linear, polynomial, or exponential

## The IJOC exhibit toolkit

IJOC exhibits exist to make a *computational* claim legible at a glance. Choose the exhibit to the claim:

- **Performance profile (Dolan–Moré).** The default for "our solver dominates across an instance set." Plot the fraction of instances solved within a factor τ of the best solver; the curve that is highest-and-leftmost wins. Far more honest and readable than a table of per-instance times.
- **Runtime / memory vs. instance size.** Use **log scales** (often log–log or semilog) so polynomial vs. exponential growth is visible as a slope. Overlay the theoretical complexity from `ijoc-theory-development` so theory and experiment are seen together.
- **Time-to-target / quality-over-time plots.** For anytime algorithms and heuristics, show solution quality as a function of wall-clock; this exposes whether a method is fast-but-poor or slow-but-exact.
- **Gap-closure / convergence plots.** For exact methods, show primal–dual gap over time or over nodes.
- **Box/violin plots across seeds.** For stochastic methods, show the distribution, not a bar of means.

## Tables that earn their space

Tables are for precise numbers a profile cannot give: final gaps, node counts, instance characteristics. Make them readable:

- Report **dispersion** for stochastic results (mean ± sd, or median [IQR]), not bare means.
- State the **time limit, hardware, and units** in the caption — a "time" column is meaningless without them.
- Define every metric (how the gap is computed, what "solved" means) in the caption or a note.
- Bold or mark the best per row sparingly and consistently; do **not** use significance asterisks — IJOC results are about magnitudes and statistical tests reported in text, not starred cells.
- Aggregate: a summary table plus a deposited full-results file (in the GitHub `results/`) beats a 12-page raw dump.

## Make the exhibit answer the claim

Every exhibit should map to a sentence in the paper. If the claim is "we scale better," the scaling plot must show diverging slopes; if it is "we dominate across instances," the performance profile must show the dominant curve. An exhibit that does not visibly support its claim invites the referee to doubt the claim itself. Reproducibility extends here too: the script that produces each figure should live in the deposit's `scripts/`, so a reviewer can regenerate it.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). INFORMS JoC is computing / algorithms and methodology; the causal-inference chain below applies only to its empirical-evaluation papers, not to algorithm design.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Multi-method, multi-instance comparison shown as a performance profile, not a mega-table
- [ ] Scaling shown on log axes with the theoretical complexity overlaid
- [ ] Anytime/heuristic results shown as quality-over-time where relevant
- [ ] Stochastic results show distribution/dispersion, not means alone
- [ ] Every table caption states time limit, hardware, units, and metric definitions
- [ ] No significance asterisks; best-per-row marked consistently and sparingly
- [ ] Each exhibit visibly supports the specific claim it serves
- [ ] Figure-generating scripts are in the deposit and regenerate the exhibit

## Anti-patterns

- A 50-row table of per-instance times where a performance profile would settle the comparison
- Linear axes hiding exponential growth in a scaling plot
- Bare means for randomized methods, with no dispersion or distribution
- Time columns with no stated time limit, hardware, or units
- Significance asterisks imported from a social-science template
- An exhibit whose visible message does not match the claim it is cited for
- Figures that cannot be regenerated from the deposited scripts

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-tables-figures
【Claim → exhibit】each claim mapped to its exhibit type
【Profiles/scaling】performance profile + log-axis scaling present? [Y/N]
【Dispersion】distributions shown for stochastic results? [Y/N]
【Captions】time limit / hardware / units / metric defined? [Y/N]
【No asterisks】confirmed [Y/N]
【Reproducible】figure scripts in deposit? [Y/N]
【Next skill】ijoc-writing-style
```
