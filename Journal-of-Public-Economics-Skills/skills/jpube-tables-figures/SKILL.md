---
name: jpube-tables-figures
description: Use when designing the exhibits for a Journal of Public Economics (JPubE) manuscript — bunching density plots, event-study and RD/RKD graphs, incidence and distributional figures, and self-contained tables. Makes the public-finance design visible; it does not run the analysis (use jpube-data-analysis).
---

# Tables & Figures (jpube-tables-figures)

## When to trigger

- The identifying variation is buried in a regression table instead of shown in a graph
- A bunching, RD, or event-study result has no picture
- Tables are dense, under-noted, or not callable in order
- You need exhibits that make a policy elasticity legible to a referee

## Why figure-forward at JPubE

JPubE's identification often *is* a picture — a spike of excess mass at a tax kink, a jump at an eligibility cutoff, a clean break at a reform date. Because referees are public-finance specialists assessing design credibility, **the headline of a JPubE empirical paper is frequently one transparent graph** that lets the reader see the response before any regression. Build exhibits so the design is self-evident.

## Exhibit norms

- **Lead with the design figure.** Bunching: observed density vs. smooth counterfactual around the kink/notch, with the excluded region marked. RD/RKD: binned scatter with the fitted discontinuity/kink and CIs. DID: event-study plot with leads and zero-line.
- **Show, then estimate.** A figure that makes the response visible earns more trust than a coefficient; the table quantifies what the figure shows.
- **Distributional / incidence plots** where the contribution is about who bears a tax or gains from a transfer.
- **Self-contained notes.** Each table/figure note states the sample, data source (and restricted-access caveat), the estimator, the inference (clustering level), and the units — readable without the text.
- **Clean tables.** Report the policy parameter (elasticity, MVPF, take-up) prominently; avoid 10-column kitchen-sink tables; put diagnostics in clearly labeled panels.
- **Print quality.** Vector output (PDF/EPS); legible at print size; minimal chartjunk (no 3D, restrained color); confidence bands shown.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPubE is public economics — tax/transfer/program designs; DiD/IV/RDD and bunching are central, magnitudes in policy units.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] A design figure leads the empirical section (bunching / RD / event-study)
- [ ] The policy parameter (elasticity / MVPF / take-up) is prominent in the main table
- [ ] Every exhibit is callable in order and self-contained via its note
- [ ] Notes state sample, source + access caveat, estimator, clustering, units
- [ ] Distributional / incidence exhibit included where the contribution warrants
- [ ] Vector graphics, confidence bands shown, chartjunk removed

## Anti-patterns

- Hiding a bunching or RD result inside a regression table with no plot
- Figures with no confidence bands or no marked counterfactual / excluded region
- Notes that omit the data source or the restricted-access caveat
- A 10-column main table where the key elasticity is one buried row


## Lead-figure choice by design (decision grid)

The headline exhibit should let a referee see the response before any regression.

| Design | Lead figure | Must show |
|--------|-------------|-----------|
| Bunching / notch | Observed vs. smooth counterfactual density | Excluded region marked, excess mass |
| RD / RKD | Binned scatter with fitted jump/kink | CIs, bandwidth, polynomial order |
| Reform DID | Event-study plot | Leads/lags, zero line, pre-trend flat |
| Incidence | Distributional bars by income/eligibility | Who bears the tax / gains the transfer |

A vignette: a draft hides a kink-bunching result (elasticity **e = 0.25**, illustrative) inside a six-column regression table. The exhibit fix promotes the density plot — observed mass spiking above the smooth counterfactual at the kink, excluded region shaded — to Figure 1, and demotes the regression to a quantifying table. The referee sees the identification, then reads the number.

Hedge: exact figure-count or color conventions are production matters — confirm against the current Elsevier artwork guidelines.

## Exhibit pass for Journal of Public Economics

Treat this skill as an executable review pass, not a prose hint. First lock the policy instrument, affected margin, identification design, and welfare or incidence interpretation; then judge whether the current manuscript answers the venue's real reader: public economists who ask whether policy design, fiscal incidence, or welfare interpretation is credible.

- **Do the pass:** For every table or figure, state the estimand or object, sample or case base, uncertainty display, and one sentence the exhibit proves for the venue audience.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against JDE for development policy, JIE for cross-border policy, AEJ Economic Policy for broad policy readership; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Lead figure】bunching / RD / RKD / event-study — present? [Y/N]
【Key parameter visible】elasticity / MVPF / take-up in main table? [Y/N]
【Notes self-contained】sample/source/estimator/clustering/units? [Y/N]
【Distributional exhibit】[present / not needed]
【Print quality】vector + bands + low chartjunk? [Y/N]
【Next step】jpube-writing-style
```
