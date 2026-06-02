---
name: ajs-data-analysis
description: Use when planning or auditing the analysis of an American Journal of Sociology (AJS) manuscript so the evidence credibly supports the theoretical claim. Covers analysis norms, uncertainty, robustness, and triangulation across quantitative, comparative-historical, and ethnographic work. Improves the analysis chain; it does not fabricate results.
---

# Data Analysis (ajs-data-analysis)

At AJS the analysis exists to make the **theoretical claim credible** — not to display technique. A
generalist, double-blind reviewer will ask whether the evidence actually warrants the claim and whether
candor about uncertainty is present. This skill stress-tests the analysis chain in the idiom of your
work.

## When to trigger

- Planning the analysis, or auditing it before writing up
- A reader doubts robustness, the evidence-to-claim link, or the handling of uncertainty
- Reconciling multiple methods or data sources into one coherent argument
- Deciding which analyses are confirmatory vs. exploratory

## Analysis norms (by tradition)

### Quantitative
- Report **uncertainty honestly** (intervals, not just stars); avoid implying causality the design
  cannot support.
- Show that results are **not artifacts**: principled robustness (alternative specifications,
  samples, measures), not a fishing expedition; keep seeds and pinned versions.
- Distinguish **preregistered/confirmatory** from **exploratory** analyses where applicable.

### Comparative-historical
- Make the **inferential logic** explicit (necessary/sufficient conditions, sequence, conjuncture);
  show how disconfirming evidence was sought and weighed.
- Cite primary sources so a reader could follow the trail.

### Ethnographic / interview
- Show the **analytic procedure**: how codes/themes were built, how negative cases were handled, how
  representativeness within the case is judged.
- Quote enough to let the reader assess the inference from data to claim.

## Triangulation (an AJS strength)

AJS often rewards **convergent evidence** — a mechanism shown through more than one window
(e.g., statistics + cases, or interviews + administrative data). When methods disagree, say so and
theorize the discrepancy rather than hiding it.

## Anti-patterns

- Stars-only reporting; implying causation from association
- Robustness theater (a wall of tables that never tests the load-bearing assumption)
- Cherry-picked quotes or cases that ignore negative evidence
- Presenting exploratory results as if confirmatory
- Technique foregrounded over the theoretical question it serves

## Output format

```
【Claim under test】from theory-building
【Primary evidence】the analysis that carries the claim
【Uncertainty】how it is reported and bounded
【Robustness / negative cases】load-bearing checks done? [Y/N]
【Triangulation】convergent evidence across windows? [Y/N/NA]
【Confirmatory vs. exploratory】labeled where relevant? [Y/N]
【Next】ajs-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — analysis packages (R / Stata / Python / CAQDAS / QCA)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AJS evidence expectations (and the 待核实 note on data policy)
