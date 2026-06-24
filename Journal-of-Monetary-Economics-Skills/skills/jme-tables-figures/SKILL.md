---
name: jme-tables-figures
description: Use when designing the main-text exhibits of a Journal of Monetary Economics (JME) manuscript under the strict 40-page / no-more-than-10-tables-and-figures-combined cap — impulse-response plots, FEVDs, moment tables — and deciding what to push to the online supplementary appendix.
---

# Tables & Figures (jme-tables-figures)

## When to trigger

- The main text has more than 10 tables and figures combined
- IRF plots are cluttered, mislabeled, or missing bands
- You must decide which exhibits stay in the body and which go online
- The paper risks exceeding the 40-page accepted-length cap

## The JME exhibit constraint

JME enforces a hard rule: **accepted papers must not exceed 40 pages of text, references, and footnotes, and must include no more than 10 tables and figures combined.** Online supplementary appendices are **exempt** from this limit. This is a defining JME discipline — you cannot keep adding robustness exhibits to the body. Plan the **≤10** main exhibits as the load-bearing story (the headline IRF, the key FEVD or moment-fit table, one or two robustness panels) and route everything else to the **online supplement on ScienceDirect**.

Formatting conventions: tables and figures are **numbered consecutively with Arabic numerals**, with self-contained notes. The reference list sits **after appendices but before tables and figures**. Submissions carry **line numbers** and use **footnotes (superscript Arabic numerals), not endnotes**.

## Exhibit design (monetary-macro)

- **Impulse-response plots**: show confidence/credible bands; label the shock unit (e.g., a 100-bp or one-SD policy shock); keep horizons consistent across panels; overlay VAR vs. LP where it is the point.
- **FEVD exhibits**: a compact bar chart or table; report the share of variance the identified shock explains.
- **Moment / fit tables** (DSGE): data vs. model second moments; mark which moments were targeted vs. untargeted.
- **Estimation tables**: coefficients with standard errors that match the inference (HAC/cluster/posterior); avoid 9-column kitchen-sink tables — split into a clean main table plus an online appendix.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JME is monetary macro — SVAR, local projections, high-frequency identification; `local_projections`/`irf` are in StatsPAI, DSGE/calibration is outside this toolchain.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Combined tables + figures in the main text ≤ **10**
- [ ] Main text on track for ≤ **40 pages** (text/refs/footnotes)
- [ ] Every IRF has bands and a labeled shock unit
- [ ] Tables/figures numbered with Arabic numerals; notes self-contained
- [ ] Robustness and derivations moved to the **online supplement** (exempt from the cap)
- [ ] Reference list placed after appendices, before tables/figures; line numbers on

## Anti-patterns

- A body with 14 figures, betting reviewers will not count toward the 10-exhibit cap
- IRFs without confidence bands or with inconsistent shock units across figures
- A dense moment table that hides which moments were targeted
- Endnotes instead of footnotes; abbreviated journal titles leaking into figure notes


## Exhibit pass for Journal of Monetary Economics

Use this as a second-pass capability check. First lock the main macro object, the identifying variation, and the policy-relevant counterfactual; then test whether the manuscript addresses macro and monetary economists who expect the shock, mechanism, and policy margin to be visible early.

- **Primary move:** For every table or figure, state the object, sample/case base, uncertainty display, and one sentence the exhibit proves for this venue.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JIE for open-economy trade/finance emphasis, RED for dynamic macro theory, AEJ Macro for broader field positioning; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Exhibit count】tables + figures in body = N (≤10?)
【Page estimate】~N pages (≤40?)
【IRFs】bands + shock unit on every panel? Y/N
【Moved online】[list of exhibits pushed to the supplement]
【Formatting】Arabic numerals / footnotes / line numbers? Y/N
【Next step】jme-writing-style
```
