---
name: jegeo-tables-figures
description: Use when exhibits — especially maps — for a Journal of Economic Geography (JEG) manuscript are dense, decorative, or do not answer the spatial question. Makes maps and tables argue; it does not invent results.
---

# Tables and Figures (jegeo-tables-figures)

## When to trigger

- The paper has maps that are pretty but make no argument (a choropleth that just shows where the data are)
- A key spatial pattern lives in a table of coefficients when a map or gradient plot would carry it
- Regression tables are dense, use significance asterisks, or hide the spatial-inference choices (W, cutoff, scale)
- A geographer reviewer cannot see the geography and an economist reviewer cannot see the magnitudes

## Maps must argue, not decorate

JEG is one of the few economics outlets where **the map is often the central exhibit**, and referees from the geography side judge cartographic craft. A map earns its place only if it makes a point a table cannot:

- **Show the variation the paper exploits**, not just where observations sit — e.g., the spatial discontinuity at a border, the treated vs. control regions, the gradient that motivates the mechanism.
- **Classification is an argument:** the choropleth break scheme (quantiles, Jenks, equal-interval) changes the visual story — choose deliberately and say which, because a reviewer can re-bin and reach a different conclusion.
- **Honest projection and scale:** a national choropleth visually inflates large rural regions; consider cartograms or rates-per-area where the unit-size distortion matters.
- **Map the residual, not just the raw outcome** when the claim is about the part the model explains.
- **Pair the map with a number** so the economist audience can size the effect — a map of the gradient plus the estimated slope.

## Tables in JEG house style

- **No significance asterisks.** Report coefficients with standard errors (and ideally confidence intervals); let magnitudes and precision speak. State the SE type (Conley/clustered) and, for spatial models, the W and cutoff in the note.
- **One table answers one question.** A reader should know from the title what spatial claim it supports.
- **Surface the spatial choices** that drive results in the table note: spatial scale/unit, weight matrix, cutoff distance, treatment timing.
- **Direct vs. indirect (spillover) effects** must be reported separately for spatial-lag/SDM models — a single coefficient is uninterpretable there.

## Event-study and gradient plots

- For spatial DID, the **event-study leads/lags plot** is more persuasive than a DID coefficient table — show the flat pre-trend.
- For distance-based mechanisms, a **coefficient-by-distance-ring plot** makes the spatial decay visible and is exactly what a JEG referee wants to see.

## Common map mistakes that draw a geographer's red pen

- **Raw counts on a choropleth** when the claim is about rates or intensity — large or populous regions dominate visually and mislead; map a rate or density instead.
- **A rainbow color ramp** for a sequential variable — it implies thresholds that are not in the data and fails in grayscale; use a perceptually ordered sequential or diverging ramp matched to the variable.
- **No scale bar, north arrow, or unit definition** — minor in economics tables, but a geography referee reads their absence as carelessness about space.
- **Mercator (or an unstated projection) for an area or distance claim** — distorts exactly the quantity the paper is about; pick an equal-area projection when area matters.
- **Over-plotted point maps** where thousands of geocoded points become an ink blob — bin to a hex grid or aggregate to show the pattern.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEG is spatial economics — spatial dependence and sorting; emphasize identification and Conley/spatial-robust inference.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every map makes an argument the text names (variation exploited, treatment, gradient, residual)
- [ ] Choropleth classification scheme stated and chosen deliberately
- [ ] Unit-size/projection distortion considered (cartogram or rate where needed)
- [ ] Central map paired with the estimated magnitude
- [ ] No significance asterisks; SEs/CIs reported; SE type and W/cutoff in the note
- [ ] Spatial-lag/SDM tables report direct vs. indirect effects separately
- [ ] Event-study or distance-ring plot used where it beats a coefficient table
- [ ] Exhibits readable in grayscale and within JEG's figure specs (检索于 2026-06；以官网为准)

## Anti-patterns

- A decorative choropleth that shows where the data live but proves nothing
- A break scheme chosen to maximize visual contrast, undisclosed and reversible by a referee
- Significance asterisks instead of standard errors
- A spatial-lag model reported as one coefficient with no direct/indirect split
- Burying the paper's main spatial pattern in a coefficient table when a map would carry it
- Color-only maps that collapse in grayscale or for color-blind readers

## Worked vignette (illustrative)

A paper claims knowledge spillovers decay sharply with distance, but the evidence is a single interaction coefficient in Table 3. The fix is a distance-ring plot: estimate the effect within 0–25km, 25–50km, 50–100km, 100km+ and plot the coefficients with CIs. The decay — strong within 25km, gone by 100km — becomes the figure that *is* the argument, legible to economists (magnitudes, CIs) and geographers (the spatial gradient) at once. The accompanying map then shows the actual clusters and their catchments, with the break scheme named and the estimated decay slope in the caption.

## Choosing the right exhibit for the spatial claim

| The claim is about... | The exhibit that carries it |
|------------------------|------------------------------|
| where activity concentrates | a choropleth/heat map with a stated break scheme, paired with a concentration index |
| how an effect decays with distance | a coefficient-by-distance-ring plot with CIs |
| a treatment rolled out across regions | a map of treatment timing + an event-study leads/lags plot |
| a sharp change at a border | a spatial-RDD plot (outcome against distance to border) plus a locator map |
| spillovers from a spatial-lag model | a table separating direct and indirect effects, not a single coefficient |
| a network/relational structure | a flow map or network diagram, not a table of dyads |

## Referee reactions a strong exhibit pre-empts

- The geographer asks "where is the geography?" — a map that shows the *variation you exploit* answers it before it is asked.
- The economist asks "how big is this?" — a magnitude in the caption or a CI-bearing plot answers it.
- Either asks "would this flip with a different break scheme / scale?" — stating the classification and showing the distance-ring pattern shows you already checked.

## Output format

```text
【Journal】Journal of Economic Geography
【Skill】jegeo-tables-figures
【Central exhibit】which map/figure carries the argument + what it proves
【Map craft】classification scheme / projection-distortion handling
【Magnitude pairing】number attached to the map
【Table style】no asterisks; SE type + W/cutoff in note; direct vs indirect if SDM
【Spatial plot】event-study leads / distance-ring decay where it beats a table
【Next skill】jegeo-writing-style
```
