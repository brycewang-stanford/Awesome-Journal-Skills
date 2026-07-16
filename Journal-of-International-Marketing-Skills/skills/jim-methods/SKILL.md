---
name: jim-methods
description: Use when designing a multi-country or cross-cultural study for a Journal of International Marketing (JIM) manuscript — country selection, sampling and translation equivalence, measurement-invariance planning, cross-cultural experiments, and export/entry-mode secondary data. It designs; jim-data-analysis estimates and reports.
---

# Multi-Country Research Design (jim-methods)

## When to trigger

- Countries, samples, or data sources are being chosen for a JIM-bound study
- Scales developed in one language are about to be fielded in others
- A cross-cultural experiment or an export panel is on the table
- A reviewer asks why *these* countries, or whether samples are comparable

## Country selection is a theoretical act

Countries are your levels of the theoretical variable — pick them the way an experimentalist picks conditions:

- **Theory-driven contrast.** Choose countries that sit far apart on the focal dimension (e.g., high vs. low uncertainty avoidance; strong vs. weak contract enforcement) while as similar as possible on rivals. Two well-chosen countries beat six convenient ones.
- **Confound audit.** For every focal dimension, list the country characteristics that co-vary with it (income, language family, region, market maturity) and state how the design or the models separate them.
- **Many-country designs (10+).** Move from contrast logic to variable logic: measure the country dimension continuously, plan multilevel estimation, and check that the country sample spans the dimension's range rather than clustering at one pole.
- Justify the count either way: with 2–4 countries, country-level "effects" are illustrations, not tests; say so honestly and lean on theory-driven contrast.

## Equivalence before comparison — the JIM discipline

Cross-national comparison is meaningless unless the instrument travels. Build equivalence into the design, in this order:

1. **Construct equivalence.** Does the construct exist and mean the same thing in every country? Qualitative pre-work (interviews, pilot focus groups) is cheap insurance; an emic construct forced into an etic scale fails later at the latent level.
2. **Translation equivalence.** Committee translation plus back-translation by independent bilinguals; reconcile discrepancies formally; pretest each language version. Document the protocol — JIM reviewers ask.
3. **Sampling equivalence.** Match samples across countries on the frame (students vs. panel vs. probability), demographics, and recruitment channel. A U.S. Prolific sample against a Chinese student sample confounds country with everything else.
4. **Measurement invariance plan.** Pre-commit the MGCFA sequence — configural → metric → scalar — and the decision rules (ΔCFI ≤ .01 alongside χ² difference), *before* fielding. Plan for partial invariance fallbacks and, with many groups, the alignment method. Steenkamp and Baumgartner (1998, *JCR*) remains the reference protocol; execution lives in `jim-data-analysis`.
5. **Response-style protection.** Acquiescence and extreme-response styles differ systematically across cultures. Design against them (balanced keying, some anchoring vignettes or forced-choice items where feasible) and plan statistical controls.

## Design lanes

### Multi-country survey (the JIM staple)
Everything above, plus: common-method-variance protection (temporal separation, marker variable) in *each* country; a priori power in the *smallest* country sample; informant-quality screens for firm-level surveys (export managers who actually make the decision).

### Cross-cultural experiment
Location is not a manipulation. Either (a) manipulate the cultural mechanism directly (e.g., prime self-construal) and show country moderates as theorized, or (b) measure the individual-level cultural orientation and treat country as the macro layer. Stimuli must be equivalence-checked (brands, prices, and scenarios pretested for familiarity/realism per country); randomize within country; power the *interaction*.

### Export / entry-mode secondary data
Firm-level export panels, customs data, subsidiary databases, or matched country statistics (World Bank, WTO, Euromonitor-type sources). The gate is identification: exporting and entry-mode choices are endogenous strategy decisions. Name the strategy — firm fixed effects with within-firm variation, DiD around policy shocks (tariff changes, FTA entry), IV, or selection models (export-market entry is selected) — and defend its key assumption. Cluster inference at the country or firm level to match the variation.

### Meta-analysis of cross-national effects
Code country context (dimension scores, development indicators) for every primary study a priori; model them as moderators; report search protocol and inter-coder reliability; publication-bias diagnostics are expected.

## Execution bridge (StatsPAI / Stata MCP)

For quasi-experimental and panel lanes, run the design checks rather than merely listing them. Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Typical JIM chain: `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` for the owed diagnostics — staggered-policy DiD via `callaway_santanna` plus `honest_did_from_result`, IV via `effective_f_test`, few-country clustering via `wild_cluster_bootstrap`. Invariance and multilevel execution details are in `jim-data-analysis`.

## Checklist

- [ ] Country choice justified on the focal dimension; confound audit written
- [ ] Construct, translation, and sampling equivalence documented (protocols, not assertions)
- [ ] Invariance sequence and decision rules pre-committed; partial-invariance fallback planned
- [ ] Response-style and CMV protections designed in per country
- [ ] Experiment: mechanism manipulated/measured, stimuli equivalence-pretested, interaction powered
- [ ] Secondary data: identification strategy named; endogeneity of the international choice addressed
- [ ] Smallest-country sample passes the power analysis

## Anti-patterns

- Countries chosen by coauthor passports, with the cultural rationale reverse-engineered
- One-shot single translation with no back-translation record
- Comparing latent means without any invariance testing planned — a desk-reject trigger at JIM
- Treating data-collection location as a cultural manipulation
- Export-performance regressions that ignore self-selection into exporting
- Pooling countries into one sample and calling the study cross-national

## Output format

```text
【Design lane】multi-country survey / cross-cultural experiment / secondary panel / meta
【Countries】list + focal-dimension contrast + confound audit result
【Equivalence】construct / translation / sampling: protocol status for each
【Invariance plan】configural→metric→scalar, ΔCFI rule, partial fallback: committed?
【Identification (if secondary)】strategy + key assumption
【Power】smallest-country sample vs. target effect: pass/fix
【Next skill】jim-data-analysis
```
