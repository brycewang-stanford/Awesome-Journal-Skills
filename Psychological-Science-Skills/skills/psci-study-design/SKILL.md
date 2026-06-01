---
name: psci-study-design
description: Use when designing studies for a Psychological Science manuscript so they meet the journal's standards for power, sample-size justification, preregistration, and confound control. Strengthens the design and pre-analysis plan; it does not write code.
---

# Study Design (psci-study-design)

Psychological Science expects studies that are **adequately powered**, **transparently planned**, and
**robust to researcher degrees of freedom**. Authors must **justify sample size** (a formal power
analysis where appropriate). This skill hardens the design before data collection.

## When to trigger

- Planning a study or a multi-study package
- Writing a preregistration / pre-analysis plan or a Registered Report Stage 1
- A reviewer questioned power, design, confounds, or analytic flexibility
- Justifying sample size and stopping rules

## Design standards

1. **Sample-size justification.** Provide an explicit basis for N — a **power analysis** for the
   smallest effect of interest, a precision/AIPE rationale, or (for sequential/Bayesian designs) the
   decision rule. State the assumed effect size and where it came from.
2. **Preregister the confirmatory core.** Specify hypotheses, design, conditions, measures, exclusion
   rules, and the analysis plan in advance (OSF/AsPredicted, or a Registered Report Stage 1). This is
   what converts a claim from exploratory to confirmatory.
3. **Control researcher degrees of freedom.** Decide in advance: conditions, the full set of measures,
   exclusion criteria, covariates, and how stopping is determined. Undisclosed flexibility inflates
   false positives.
4. **Confounds and validity.** Address random assignment, manipulation/attention checks, order
   effects, demand characteristics; argue construct and external validity for the population claimed.
5. **Multi-study logic.** If using several studies, say what each adds (generalization, mechanism,
   boundary condition) — not just repetition.

## Registered Reports (strongest design path)

- Stage 1 reviews the **theory + design + analysis plan before data**; in-principle acceptance commits
  the journal regardless of outcome if you execute the plan. Ideal for confirmatory and replication
  work, and it neutralizes publication bias. For prior-collected data, use **RR with Existing Data**
  and declare provenance.

## Anti-patterns

- "We collected 50 per cell" with no power/precision justification
- Optional stopping or undisclosed exclusion rules
- Flexible measure/condition selection revealed only after results
- Underpowered single studies chasing a surprising effect
- A multi-study paper where studies are near-duplicates with no added inference

## Output format

```
【Sample size】N + justification (power for smallest effect of interest / precision / decision rule)
【Preregistration】confirmatory core preregistered? where?
【Degrees of freedom】conditions, measures, exclusions, covariates fixed in advance? [Y/N]
【Validity】confounds / checks / population addressed
【Design path】Research Article vs Registered Report (S1)
【Next】psci-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — G*Power, `simr`, `Superpower`, preregistration templates
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — sample-size-justification and preregistration policy
