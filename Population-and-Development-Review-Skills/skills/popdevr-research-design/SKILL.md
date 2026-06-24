---
name: popdevr-research-design
description: Use when defending the research design of a Population and Development Review (PDR, Wiley / Population Council) manuscript — choosing among demographic methods (life tables, decomposition, event-history, age-period-cohort, projections) and, where the question is causal, defending identification, with the population-and-development linkage made explicit. PDR judges each method on its own terms and asks what it shows about development. Strengthens the design; it does not write code.
---

# Research Design (popdevr-research-design)

PDR accepts a wide range of approaches — empirical demography, formal demography, and conceptual
synthesis — but is demanding about each, and it asks one extra question: **does the design illuminate the
population-and-development linkage**, not just a demographic quantity? The design must credibly connect
the argument (`popdevr-theory-building`) to evidence a broad readership will trust. This skill is
method-aware: pick the section that matches your question and defend it against the strongest rival.

## When to trigger

- Choosing the method that actually answers a population-and-development question
- A reviewer questioned the rate construction, the identification, or the development linkage
- Specifying a decomposition, event-history, age-period-cohort, or projection design
- Justifying why your design adjudicates the rival account from `popdevr-literature-positioning`

## Match the method to the question

- **Life tables** — for survival, life expectancy, and exposure: period vs. cohort, abridged vs.
  complete; multiple-decrement (cause-specific) where the development story is cause-specific.
- **Decomposition** — to attribute a difference or change in a rate to components: Kitagawa
  (rate vs. composition), Arriaga (age contributions to e0), Das Gupta (multi-factor). Say exactly **what
  each component means** and which maps to a development channel.
- **Event-history / survival** — for timing and transitions (first birth, migration, mortality), with
  **competing risks** where several destinations matter; check the proportional-hazards assumption.
- **Age-period-cohort** — confront the **identification problem head-on**: state the constraint or
  modeling assumption (and its justification); do not present a single "identified" APC partition as
  assumption-free.
- **Projections / cohort-component** — make transition rates, the base population, and assumptions
  (closed/open, period/cohort, policy scenarios) explicit; report sensitivity to key assumptions; PDR
  values scenario projections tied to development or policy futures.

## When the question is causal (population ↔ development)

- **Identification first.** State the estimand and the assumptions licensing a causal reading
  (ignorability, parallel trends, exclusion, continuity); defend them, do not assert them.
- **Selection and exposure** are demographic hazards: mortality selection, migration selection, and
  differential exposure can masquerade as effects — address them explicitly.
- **Two-way causation.** Population and development often co-move; name the direction you claim and the
  observable that separates it from the reverse (reverse causation, institutional confounding).
- **Inference.** Cluster at the right level (household, region, country); use survey/design weights;
  report uncertainty for derived quantities.
- **Sensitivity.** How strong must an unobserved confounder (or a violated assumption) be to overturn it?

## The adjudication test (PDR-specific)

For the **single strongest rival explanation** (e.g., reverse causation, compositional change, selection,
institutional confounding), write one sentence: *"If the rival were true rather than my account, the
pattern would look like ___; instead it looks like ___."* If you cannot, the design does not yet identify
the population-and-development contribution.

## Cross-country comparability (a recurring PDR design problem)

PDR papers often compare countries or development contexts, and a cross-national contrast is only as good
as its comparability. Before reading a between-country gap as a development effect, settle three things:

1. **Definitions and coverage.** Are the demographic concepts (a "birth," a "migrant," an age cutoff) and
   the denominators measured the same way across settings? Vital-registration coverage and census quality
   vary with development level — and that variation can *create* the gradient you are studying.
2. **Data class and vintage.** Mixing a high-quality register with a single DHS round, or different WPP
   vintages, can manufacture artefactual differences. Hold the data class and vintage as constant as the
   question allows, and report what you could not harmonize.
3. **Like-with-like comparison.** Where full comparability is impossible, restrict to the subset that is
   comparable, or model the measurement difference explicitly rather than absorbing it into the estimate.

State which of these you have controlled and which remain a caveat in `popdevr-tables-figures` notes.

## When the contribution is a synthetic essay (no new estimate)

If the paper's contribution is a framework rather than an analysis, the "design" is the **argument
architecture**: the propositions, the evidence marshaled for each, and the boundary where the framework
stops applying. Route the rigor through `popdevr-theory-building` and `popdevr-writing-style` instead of
this skill's estimation machinery, but still pass the adjudication test against the prior framework it
revises.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). PDR is population studies blending quantitative and policy work; apply the chain to its empirical-causal papers.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference, `romano_wolf` for many-outcome
  family-wise control, and `mediate` for mediation (not naive controlling-away).
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the effect size in interpretable units; route the full battery to the
appendix/supplement. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Running a regression when the question calls for a life table, a decomposition, or an event-history model
- Presenting an APC decomposition without naming the identifying constraint
- Period rates read as cohort experience (or vice versa) without justification
- Ignoring mortality/migration selection or the population↔development direction of causation
- Projections whose assumptions are buried instead of varied and reported

## Output format

```
【Method】life table / decomposition / event history / APC / projection / causal
【Quantity / estimand】what is measured or identified + its development linkage
【Key assumption(s)】and how each is defended (name the APC constraint if used)
【Rival ruled out】the adjudication sentence (incl. reverse causation if relevant)
【Robustness/sensitivity】planned checks
【Next】popdevr-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — life-table, decomposition, survival, APC, and projection packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — PDR scope and methodological breadth
