---
name: jue-topic-selection
description: Use when deciding whether a question is a genuinely spatial, urban-economics contribution that fits the Journal of Urban Economics (JUE) rather than a sibling venue. Locks the spatial question and outlet fit before positioning; it does not write the literature review or design the identification.
---

# Topic Selection (jue-topic-selection)

## When to trigger

- The question is interesting but it is unclear it is *spatial* — could it be a labor or public-finance paper that merely uses geographic data?
- The paper sits on a boundary with **RSUE, Journal of Regional Science, JEG (OUP), or JPubE** and you must decide where it belongs
- A reviewer or coauthor asks "why is this urban economics?" and the answer is thin
- You have a clean result but no urban *mechanism* — only a geographic correlation
- You are choosing between a full JUE article and the short-paper **JUE: Insights** track

## Is this a JUE paper? The spatial-mechanism test

JUE publishes work where **space is constitutive of the economics**, not a label on the data. The question should turn on at least one spatial primitive: agglomeration economies, housing supply elasticity, land use & zoning, commuting/transportation, local public finance & Tiebout sorting, neighborhood effects, or spatial sorting/equilibrium. Run the manuscript through three gates:

1. **Mechanism gate.** Can you name a spatial mechanism — capitalization, agglomeration spillover, sorting across locations, congestion, market access — that *generates* the result? If the mechanism is a-spatial (it would hold with units relabeled non-geographically), it is not a JUE paper.
2. **Equilibrium gate.** Does the question respect that people and firms *move*? A partial result that ignores spatial reallocation (workers/firms/residents re-sorting) will draw the JUE referee's first objection. The contribution should engage spatial equilibrium even if reduced-form.
3. **Marginal-contribution gate.** Urban economics is mature; "X affects house prices / city size / wages" is rarely enough. The novelty must be a new mechanism, a new spatial design, novel geocoded data, or a quantitatively important magnitude for urban policy.

## Sibling-boundary decision table

| If the paper's core is... | It belongs at... | because... |
|---------------------------|------------------|------------|
| a spatial mechanism with urban data and an urban audience | **JUE** | the field flagship for urban & regional economics |
| methods/theory of regional science, broader spatial econometrics | **RSUE** or **J. of Regional Science** | JUE leads with the economics, not the spatial method per se |
| economic-geography framing, clusters, evolutionary geography | **JEG (OUP)** | JEG is geography-leaning and non-Elsevier |
| the tax/spending design dominates; geography is the setting | **JPubE** | a place-based result is not automatically a public-finance contribution |
| a broad applied-micro causal result with a city setting | **AEJ: Applied** | AEJ rewards the design; JUE wants the spatial mechanism too |

## Choosing the article format

- **Full JUE article** — a complete contribution: design, mechanism, magnitudes, robustness, policy reading.
- **JUE: Insights** — a focused, well-identified short result. Cap ≤6,000 words and ≤5 exhibits (each exhibit below five buys +200 words; a zero-exhibit paper ≤7,000 words) (检索于 2026-06；以官网为准). Use it for a single sharp finding (a clean policy evaluation, a measurement contribution) that does not need a full model. The track was launched to publish timely, tightly-identified short papers; do not pad a Insights-sized result into a full article to look weightier.

## What gets desk-rejected at JUE

JUE is a high-volume field flagship and the editors desk-reject freely. The recurring desk-reject patterns are worth designing against from the start:

- **No spatial mechanism** — a result that uses geographic units but whose economics is a-spatial (a labor or finance result that happens to be measured by city).
- **Setting mistaken for contribution** — "the first study of [city/country]" with no new mechanism, design, data, or magnitude.
- **Wrong venue** — a tax-design paper (JPubE), a spatial-method paper (RSUE), or an economic-geography paper (JEG) sent to JUE because it is "about cities."
- **Identification not credible for space** — a cross-location OLS that any urban referee will read as sorting, presented as causal.
- **Stale question with no new angle** — re-confirming a well-established urban regularity without moving the frontier.

## Timeliness and the JUE: Insights niche

The Insights track was built for results that are sharp and timely — a clean evaluation of a recent policy, a measurement contribution, a decisive null. If your finding is one well-identified estimate that does not need a model and would lose force if delayed by a multi-year full-article cycle, Insights is the right home. Reserve the full article for contributions that need a model, a battery of mechanisms, or a quantitative-spatial counterfactual. Misjudging this — padding an Insights result or compressing a full contribution — is itself a fit error referees notice.

## Worked vignette (illustrative)

A team has clean admin data showing firms near a new university campus pay higher wages. Tempting framing: "agglomeration raises wages." But the mechanism gate exposes a sorting story — high-wage firms may have located near the campus. The JUE-viable reframing pins a *mechanism*: use the staggered campus openings as a shock to local knowledge spillovers, decompose the wage gain into sorting vs true spillover, and report the spillover magnitude relevant to place-based innovation policy. That is an agglomeration contribution; "firms near campuses pay more" is a desk-reject.

## Checklist

- [ ] A spatial mechanism is named in one sentence, and the result would not survive relabeling units non-geographically
- [ ] The paper engages spatial equilibrium / reallocation rather than assuming a closed location
- [ ] The marginal contribution is more than "X affects an urban outcome"
- [ ] The sibling boundary (RSUE / JRS / JEG / JPubE / AEJ:Applied) is explicitly resolved
- [ ] Format chosen (full article vs JUE: Insights) matches the scope of the result
- [ ] The urban-policy or theory audience who would cite this paper is identifiable
- [ ] The spatial resolution the design needs exists and is accessible (and depositable)
- [ ] The result is not a known urban regularity re-confirmed with no new angle

## Anti-patterns

- A national/firm-level result run on county or city data with no spatial mechanism ("geographic data ≠ urban economics")
- Ignoring that agents re-sort, so the estimated effect double-counts or omits general-equilibrium reallocation
- Pitching to JUE a paper whose real contribution is a tax design (→ JPubE) or a spatial-econometrics method (→ RSUE)
- Forcing a thin result into a full article when JUE: Insights fits better, or vice versa
- Claiming "first paper to study X city" as if novelty of setting were novelty of contribution

## Data-availability shapes feasibility — decide early

Urban questions are often constrained by what geography you can observe. Before committing, confirm the spatial resolution you need actually exists and is accessible: parcel/address-level for capitalization and boundary designs, establishment-level for agglomeration, tract/block for neighborhood effects, network/GTFS for transport. A question that requires geocoded individual data you cannot obtain (or cannot deposit under JUE's replication policy) is a topic-selection problem, not a later logistics detail — fold the data path and the replication route into the topic decision, and loop in `jue-replication-package` if the data is restricted.

## Output format

```text
【Spatial mechanism】one sentence — what space does in the economics
【JUE vs sibling】JUE / RSUE / JRS / JEG / JPubE / AEJ:Applied + one-line reason
【Format】full article / JUE: Insights
【Marginal contribution】mechanism / design / data / magnitude (pick the real one)
【Equilibrium engagement】how reallocation is handled
【Next skill】jue-literature-positioning
```

> If the spatial-mechanism test fails, the fastest fix is rarely a new dataset — it is reframing the existing result around the spatial primitive (capitalization, sorting, agglomeration) that was always implicit but never made the point of the paper.
