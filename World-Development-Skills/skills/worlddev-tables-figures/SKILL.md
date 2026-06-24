---
name: worlddev-tables-figures
description: Use when exhibits in a World Development (WD) manuscript are dense, asterisk-laden, or fail a multidisciplinary reader — including maps and qualitative displays. Makes every exhibit answer a development question; it does not invent evidence or citations.
---

# Tables, Figures & Qualitative Displays (worlddev-tables-figures)

## When to trigger

- Tables report significance with asterisks instead of standard errors / confidence intervals
- Coefficients are shown in model units a non-economist cannot interpret (log points, latent indices)
- A geographic study has no map, or a busy map that communicates nothing
- A qualitative paper has no systematic display — just block quotes scattered through prose
- The main exhibits do not, on their own, let a reader reconstruct the paper's argument

## The WD exhibit standard

WD's readership is multidisciplinary and policy-facing, so exhibits must clear a higher legibility bar than in a specialist economics journal: **a development scholar from another field, or an informed practitioner, should grasp the headline from the exhibit and its note alone.** That changes priorities. Effect sizes in interpretable units beat starred coefficients; a clean figure beats a dense table; a well-built map or qualitative matrix can carry an argument that prose cannot.

### Tables

- **Report uncertainty, not stars.** Standard errors or confidence intervals in parentheses; no `***`. WD's audience reads magnitudes, and asterisks invite dichotomous "significant/not" thinking that the journal's evidence culture resists.
- **Translate to real units.** Convert log points to percent; index effects to a meaningful benchmark (a standard deviation, a mean, a poverty-line equivalent). State the comparison ("relative to the control mean of X").
- **One question per table.** The title states the question; the note states the sample, the units, the inference, and what is being held fixed.
- **Show the magnitude that matters for policy**, not only the cleanest specification.

### Figures

- **Prefer figures for the headline.** Coefficient plots, event-study leads/lags, dose-response curves, and distributional plots communicate to a broad audience faster than tables.
- **Maps for spatial development data** — choropleths for outcomes/treatment, with clear classification, projection, and a note on the unit. A map should answer a question, not decorate.
- Design for **grayscale and color-blind safety** (Elsevier prints and renders both); never rely on red/green alone.

### Qualitative displays

Qualitative WD papers should *display* evidence, not only narrate it. Use:

- **Coding/thematic matrices** (themes × cases or × informant groups) to show pattern across the corpus.
- **Process-tracing timelines** linking events to mechanism steps.
- **Illustrative-quote tables** that tie each quote to a theme and a source identifier — including, where it matters, a disconfirming quote.
- **Typologies** that organize cases along the dimensions the argument turns on.

## A worked fix (illustrative)

A table reports "0.18***" for a transfer program on consumption. The WD fix: report "0.18 (0.05)" and add a note — "an 18% increase relative to the control-group mean of 1,420 PPP$; clustered at the village level (N=86 clusters)." Better still, move it to a coefficient plot with the control-mean reference line, so a public-health reader sees the magnitude and its precision at a glance.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). World Development is multidisciplinary development studies; the chain serves its quantitative-causal lane, mixed-methods work uses its own standards.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] No significance asterisks anywhere; SEs / CIs reported
- [ ] Effects in interpretable units, benchmarked to a meaningful quantity
- [ ] Each table/figure answers one stated question; notes give sample, units, inference
- [ ] Headline result available as a figure, not buried in a wide table
- [ ] Spatial data shown on a legible, well-classified map where relevant
- [ ] Qualitative evidence displayed systematically (matrix/timeline/quote table), not only quoted in prose
- [ ] Grayscale- and color-blind-safe; figures readable at print size

## Anti-patterns

- Asterisk-driven tables that train the reader to read "significant vs. not" instead of magnitude
- Coefficients in raw model units no cross-disciplinary reader can interpret
- A decorative map that conveys no comparison, or a missing map for clearly spatial data
- Kitchen-sink regression tables with twelve columns and no signposted headline
- Qualitative evidence reduced to cherry-picked block quotes with no systematic display

## Output format

```text
【Journal】World Development (WD)
【Skill】worlddev-tables-figures
【Verdict】reader-ready / revise
【Asterisks】removed; SEs/CIs present? [Y/N]
【Units】effects translated + benchmarked? [Y/N]
【Headline exhibit】figure / map carrying the main result
【Qual display】matrix / timeline / quote table present? [Y/N / n/a]
【Source status】verified URL / 待核实 / not asserted
【Next skill】worlddev-writing-style
```
