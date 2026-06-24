---
name: wber-robustness
description: Use when results for a The World Bank Economic Review (WBER) manuscript may be sensitive to specification, sample, measurement, or inference choices — and you need a threat-organized robustness plan rather than an appendix dump. Organizes checks by identifying threat and by data-quality risks specific to developing-country data; it does not run the estimation.
---

# Robustness Strategy (wber-robustness)

## When to trigger

- The headline result moves under reasonable alternative specifications
- A referee could question measurement quality (survey error, recall, attrition, undercoverage)
- Inference is shaky: few clusters, spatial correlation, multiple outcomes
- The robustness appendix is a long mechanical list with no logic
- You need to know which checks are load-bearing before submission

## The WBER robustness philosophy

WBER referees are sophisticated about *both* econometric threats *and* the realities of **developing-country data** — surveys with recall and measurement error, administrative records with coverage gaps, sampling frames that miss the informal sector, attrition in panels. So robustness here has two axes: the standard **identification-threat** axis (does the estimate survive plausible violations of the design's key assumption?) and a **data-quality** axis (does the result survive how the data were actually constructed and measured?). Organize the section by *threat*, not by a checklist; each check should answer "if a skeptic believed X, would my conclusion change?"

## Organize by threat, not by appendix

| Threat the referee has in mind | The check that answers it |
|--------------------------------|----------------------------|
| "Your design assumption is violated" | Design-specific sensitivity: honest-DiD bounds (parallel trends), bandwidth/donut (RD), Anderson–Rubin (weak IV), Oster δ / coefficient stability (selection on unobservables) |
| "It's driven by a few units/regions/years" | Leave-one-out (drop each cluster/region/wave); influential-observation checks |
| "Your key variable is mismeasured" | Alternative survey waves/sources; reconcile admin vs. survey; bound classical and non-classical measurement error |
| "The sample is selected / undercovers" | Reweight to a known population; bound for non-coverage of the informal/rural sector; differential-attrition bounds |
| "Inference is too optimistic" | Wild-cluster bootstrap (few clusters); spatial-HAC (Conley) for geographic correlation; multiple-hypothesis adjustment (Romano–Wolf / sharpened q-values) |
| "Results are p-hacked across specs" | Specification curve / multiverse showing the headline is modal, not cherry-picked |

## Data-quality robustness (the development-specific layer)

- **Measurement:** consumption, income, and yields in LDC surveys are noisy and often non-classically mismeasured (e.g., underreporting). Show the result survives alternative recall windows, deflators, or an independent data source.
- **Coverage and frame:** if the sampling frame misses the informal sector or remote areas, bound how much that could move the estimate.
- **Currency/price comparability:** when pooling across countries or years, show robustness to PPP conversion, deflator choice, and exchange-rate regime.
- **Seasonality:** agricultural and labor outcomes are seasonal; show timing of measurement does not drive the result.

## Sequencing the robustness section

Order matters for how a WBER referee reads the section:

1. **Lead with the design-violation sensitivity** — the check that addresses the headline identifying assumption (honest-DiD, RD bandwidth, Oster δ). This is what the identification referee turns to first.
2. **Then the data-quality checks** — measurement, coverage, currency — the development-specific layer the policy referee scrutinizes.
3. **Then influence and inference** — leave-one-out, wild bootstrap, spatial-HAC, multiple testing.
4. **Close with the specification curve** — a single figure that says "the headline is modal, not cherry-picked."

State in the main text which one or two checks are *load-bearing*; relegate the mechanical remainder to the appendix (which still counts against the 40-page cap).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). WBER is development economics — RCTs and observational designs in low/middle-income settings; randomization inference + DiD/IV, magnitude in policy units.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Section is organized by identifying *threat*, each with a one-line "if skeptic believes X" rationale
- [ ] Design-specific sensitivity reported (honest-DiD / RD bandwidth / weak-IV-robust / Oster)
- [ ] Leave-one-out across the dimension a referee would suspect (region/cohort/wave)
- [ ] Key variable's measurement stress-tested against an alternative source or definition
- [ ] Inference hardened for few clusters and spatial correlation; multiple testing adjusted
- [ ] A specification curve shows the headline is modal, not hand-picked
- [ ] Cross-country/year comparisons robust to PPP/deflator/seasonality
- [ ] The main text states which one or two checks are load-bearing

## Anti-patterns

- A 30-row robustness appendix with no statement of which threat each row addresses
- Reporting only specifications that strengthen the result (no specification curve)
- Ignoring few-cluster / spatial inference and over-reporting precision
- Treating LDC survey data as if it were clean administrative data (no measurement-error check)
- Pooling countries without checking PPP/deflator sensitivity
- Burying a result-killing check in the appendix instead of confronting it in the text

## Worked vignette (illustrative)

A poverty-targeting paper finds a transfer raises consumption by 11%. A referee suspects the result is an artifact of consumption being measured with a 7-day recall in treated rounds and a 30-day recall in control rounds. Rather than add a generic robustness row, the authors re-estimate within rounds that share a recall window, show the effect holds (10%, illustrative), and bound the recall-induced bias. They then run leave-one-region-out (effect stable except in one district they flag), wild-cluster bootstrap for the 14 clusters, and a specification curve showing the 11% is modal across deflator and outlier-trim choices. Each check is tied to a named skeptic.

## Distinguishing robustness from a sensitivity analysis

WBER referees separate two things the appendix often conflates:

- **Robustness** asks "is my *point estimate* stable across reasonable choices?" — alternative specs, samples, definitions. The answer should be "yes, the headline is modal."
- **Sensitivity** asks "how far can the *identifying assumption* fail before my *conclusion* flips?" — honest-DiD breakdown, Oster's δ, weak-IV-robust sets. The answer is a quantified bound on how much violation the result survives.

Both belong in a WBER paper, but they answer different referee worries; label them as such. A long list of point-estimate-stable specifications does not address an identification-violation worry, and a single sensitivity bound does not show the result is not specification-mined.

## Output format

```text
【Headline result】point estimate + inference
【Threats addressed】design-violation / few-units / measurement / coverage / inference / p-hacking
【Design sensitivity】honest-DiD / RD bandwidth / weak-IV / Oster δ
【Data-quality checks】recall/source/coverage/PPP/seasonality results
【Inference hardening】wild bootstrap / Conley / multiple-testing
【Load-bearing checks】the 1–2 that matter most
【Next step】wber-tables-figures
```
