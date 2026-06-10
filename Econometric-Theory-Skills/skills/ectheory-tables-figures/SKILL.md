---
name: ectheory-tables-figures
description: Use for the exhibits in an Econometric Theory (ET) paper — Monte Carlo size/power/coverage tables, finite-sample and limit-behavior plots, with self-contained notes, ET figure-format specs (TIFF/EPS/PDF), and legibility at 50% reduction.
---

# Tables & Figures (ectheory-tables-figures)

## When to trigger

- Turning Monte Carlo output into publication tables (size, power, coverage, bias, RMSE)
- Building plots of finite-sample distributions, convergence to the limit, or rejection curves
- Preparing figure files to ET's format and resolution specs
- Checking that exhibits are self-contained and legible after print reduction

## What ET exhibits look like

ET is a theory journal, so most exhibits are **simulation tables and diagnostic plots that
illustrate the asymptotics**, not empirical-result tables. Common exhibits:

- **Size/power tables** — empirical rejection rates under the null (vs nominal level) and under
  alternatives, across DGPs and sample sizes.
- **Coverage / bias / RMSE tables** — for estimators, across n and DGP, against a benchmark method.
- **Distribution / convergence plots** — empirical vs limiting density (e.g., normal, mixed-normal,
  Brownian functional); QQ plots; rejection curves as a function of the alternative.
- **Rate plots** — a statistic against n on a scale that reveals the convergence rate.

## Construction standards

- **Self-contained notes.** Each table/figure note states the DGP, sample sizes, number of
  replications, nominal level, and what each column/curve is — readable without the main text.
- **Honest contrast.** Put your method beside the natural competitor in the same table; do not hide
  the comparison.
- **Legibility.** Exhibits must be legible at **50% reduction**; avoid chartjunk, 3D, and dense
  color. Keep table precision sensible (e.g., 3 decimals for rejection rates).
- **Figure files (ET specs).** Supply **TIFF** (line art >=600 dpi, greyscale >=300 dpi), **EPS**
  (fonts embedded), or **PDF**. Embed fonts; vector output for line art.
- **Numbering.** Tables and figures numbered and called out in order in the text.

## Checklist

- [ ] Each exhibit note states DGP, n, replications, nominal level, and column/curve definitions
- [ ] Size reported against the nominal level; power against stated alternatives
- [ ] Benchmark method shown alongside, not omitted
- [ ] Plots show convergence/limit behavior clearly; rate legible where claimed
- [ ] Legible at 50% reduction; no chartjunk; sensible decimal precision
- [ ] Figure files in TIFF/EPS/PDF with fonts embedded, at required resolution
- [ ] All exhibits numbered and referenced in order

## Anti-patterns

- A size table without the nominal level, so over-/under-rejection cannot be judged
- Notes that require the reader to hunt through the text to decode the columns
- Cherry-picked DGPs hiding the regime where the method underperforms
- Raster figures at low dpi that blur at print reduction
- 3D bars or rainbow palettes obscuring a simple size/power comparison


## Exhibit pass for Econometric Theory

Treat this skill as an executable review pass, not a prose hint. First lock the primitive assumptions, theorem statement, proof route, and example showing why the result matters; then judge whether the current manuscript answers the venue's real reader: econometric theorists who read for assumptions, theorem novelty, proof architecture, and relation to known asymptotics.

- **Do the pass:** For every table or figure, state the estimand or object, sample or case base, uncertainty display, and one sentence the exhibit proves for the venue audience.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Econometrics for applied-method reach, Quantitative Economics for theoretical economics, Econometrica for general theory-plus-economics contribution; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Exhibit】size / power / coverage / bias-RMSE / distribution / rate plot
【Self-contained note】DGP + n + reps + level stated? [Y/N]
【Benchmark shown】[Y/N]
【Legible at 50%】[Y/N]
【File format】TIFF / EPS / PDF, fonts embedded? [Y/N]
【Next step】ectheory-writing-style
```
