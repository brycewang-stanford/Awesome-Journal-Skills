---
name: aos-data-analysis
description: Use when analyzing the material of an Accounting, Organizations and Society (AOS) manuscript — coding and interpreting qualitative field data, estimating experimental and survey models, or running theory-laden archival analyses, with an audit trail appropriate to each tradition. Analyzes and reports; it does not design the study (aos-methods).
---

# Analysis & Evidence Craft (aos-data-analysis)

## When to trigger

- Interviews, observations, and documents are collected and must become findings
- Experimental or survey data are in and the estimation plan is unsettled
- A mixed-methods paper needs its qualitative and quantitative strands reconciled
- Reviewers will probe the traceability of interpretations or the fit of the statistics

## Qualitative analysis (field / historical material)

- **Code with the lens on.** First-order codes stay close to informants' language; second-order categories translate them into the paper's theoretical vocabulary; the movement between the two is the analysis. Keep the codebook versioned so you can show how categories evolved.
- **Work the anomalies.** The abductive engine: catalog episodes the current theory cannot absorb, and let them force conceptual revision — this is where AOS papers earn their contribution.
- **Build the evidentiary chain.** Every conceptual claim should trace to identifiable material (interview number, meeting observed, document). Maintain a claim → evidence register; reviewers increasingly expect a data-structure or evidence table.
- **Weigh counter-evidence.** Report material that resists the interpretation and say why the reading survives; interpretive rigor at AOS is demonstrated, not asserted.
- **Historical work:** corroborate across independent archives; date claims precisely; distinguish what the sources show from what the genealogy argues.

## Experimental and survey analysis

- Match the model to the randomized design: ANOVA/ANCOVA with planned contrasts for factorial experiments; report cell means, standard deviations, per-cell n, and effect sizes, not p-values alone.
- Test the theorized **process**: mediation with bootstrapped confidence intervals; moderation exactly as predicted, with simple-effects follow-ups.
- Respect the randomization unit; report manipulation-check results and pre-specified exclusions transparently.
- Surveys: reliability and validity evidence (alpha/CR, factor structure), common-method-bias diagnostics, and models matched to the nesting of the data.

## Archival-with-theory analysis

- Standard panel hygiene (fixed effects suited to the institutional claim, standard errors clustered to the data structure, documented sample screens) — but keep the estimand tied to the *organizational/institutional* construct, and interpret magnitudes in the theory's terms rather than as pricing effects.

## Execution bridge (StatsPAI / Stata MCP)

For the **quantitative lane** of an AOS paper — experiments, surveys, and archival-with-theory
designs — execute and audit rather than only specify. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md).
AOS is mixed-methods: route only the statistical strand through this bridge, and let the
qualitative strand keep its own audit trail (codebook, evidence register) outside it.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to enumerate
  the checks the design owes before a reviewer asks.
- **Experiments / many outcomes:** randomization-based inference plus `romano_wolf` or
  `benjamini_hochberg` for the multi-outcome families behavioral reviewers flag.
- **Surveys / nested data:** cluster at the right level; `wild_cluster_bootstrap` when
  clusters are few.
- **Institutional-shift panels:** `callaway_santanna` / `sun_abraham` with
  `bacon_decomposition` and pre-trend evidence if a staggered adoption carries the claim;
  `oster_delta` / `sensemakr` for OVB sensitivity.
- **Exhibits:** `etable` / `plot_from_result` straight from the fitted handle — never
  retype numbers into tables.

Keep decisive checks in the body, the battery in an appendix, and reconcile every printed
number with the script that produced it.

## Reproducibility and the audit trail

- Qualitative: retain the coded corpus, codebook versions, and the claim–evidence register for the life of the project (subject to consent terms); describe the analytic process in the paper concretely enough to be assessed.
- Quantitative: scripts regenerate every exhibit from raw data; exclusions, transformations, and winsorizing documented; share instruments and code where consent and confidentiality allow, and state any restrictions honestly.

## Checklist

- [ ] (Qualitative) codebook versioned; claim → evidence register complete; counter-evidence weighed
- [ ] (Qualitative) second-order categories do theoretical work beyond labeling
- [ ] (Experiment) cell means, effect sizes, process tests with bootstrap CIs reported
- [ ] (Survey) reliability/validity and method-bias diagnostics reported
- [ ] (Archival) clustering, screens, and estimand documented; interpretation stays institutional
- [ ] Every exhibit regenerates from scripts or traces to the register

## Anti-patterns

- **Quote-stitching**: colorful excerpts arranged to illustrate a story decided in advance.
- **Counting qualitative data** as if frequency were meaning ("mentioned in 63% of interviews").
- **Stars without process** in experiments — a significant main effect with no mediator evidence.
- **Untraceable interpretation**: findings a skeptic cannot follow back to specific material.

## Output format

```
【Strand(s)】qualitative / experimental / survey / archival — analysis state ...
【Evidence chain】codebook + claim-evidence register OR scripts + audit status ...
【Process tests】mediation / moderation / pre-trends as applicable ...
【Counter-evidence】weighed and reported? ...
【Reproducibility】what regenerates, what is restricted and why ...
【Next step】aos-contribution-framing
```
