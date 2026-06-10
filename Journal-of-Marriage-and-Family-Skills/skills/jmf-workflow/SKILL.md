---
name: jmf-workflow
description: Use as the entry point for any Journal of Marriage and Family (JMF) manuscript. Routes to the right JMF sub-skill based on where you are in the lifecycle and whether the work fits a full article or a brief report. JMF is the interdisciplinary flagship of family science; the router's first job is to confirm a genuine family-science contribution. It dispatches; it does not draft content.
---

# JMF Workflow Router (jmf-workflow)

The orchestrator for a JMF submission. Figure out the stage and the **format** (full article vs. brief
report), then send the user to the matching skill. JMF publishes family-science research across
sociology, psychology, demography, and family studies — the router keeps the paper pointed at a
**families-and-close-relationships** contribution, not a generic social-science result.

## When to trigger

- Starting a new JMF paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding between a **full article** and a **brief report**
- Returning with a decision letter (route to `jmf-rebuttal`)

## First question: which format?

| Situation | Format | Route to |
|-----------|--------|----------|
| Full original study, broad family-science significance | **Article** (≤ ~35 pp.) | normal pipeline below |
| Focused single contribution, replication, innovative design, or important null finding | **Brief Report** (≤ ~25 pp.) | normal pipeline, tighter scope |
| Re-running / reassessing a published family finding | Replication (often a brief report) | `jmf-research-design` + `jmf-transparency-and-data-policy` |
| Prospective design, not yet collected/analyzed | Preregister / consider OSF | `jmf-research-design` (PAP) early |

> Brief reports are not "short articles you padded down" — they are crisp, complete contributions.

## Routing map (stage → skill)

```text
Idea / fit?                        → jmf-topic-selection
Where does it sit in the field?    → jmf-literature-positioning
What's the framework?              → jmf-theory-and-conceptual-framework
Is the design defensible?          → jmf-research-design
Are the analyses sound?            → jmf-data-analysis
Are the exhibits clear?            → jmf-tables-figures
Does it read in modified APA?      → jmf-writing-style
Repro package & data statement?    → jmf-transparency-and-data-policy
How will it be judged?             → jmf-review-process
Ready to submit?                   → jmf-submission
Got a revise-and-resubmit?         → jmf-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-and-conceptual-framework → research-design →
data-analysis → tables-figures → writing-style → transparency-and-data-policy → review-process →
submission → rebuttal`

Iterate: most papers loop framework ↔ design ↔ analysis several times before writing-style.

## Anti-patterns

- Treating JMF like a general sociology or psychology journal — the contribution must advance **family
  science** (families, couples, parents, children, kin)
- Ignoring the **unit of analysis** (individual vs. dyad vs. family) when picking the next skill
- Padding a complete focused study into a full article when a brief report would land harder
- Skipping the data availability statement and repro package until the end


## Router pass for Journal of Marriage and Family

Treat this skill as an executable review pass, not a prose hint. First lock the family process, population/sample frame, measurement validity, and longitudinal or comparative leverage; then judge whether the current manuscript answers the venue's real reader: family scholars who inspect measurement, household process, longitudinal design, and implications for family theory.

- **Do the pass:** Run the pack as a sequence: fit gate, evidence gate, writing gate, source-map gate, and final output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Demography for population-process emphasis, Social Forces for general sociology, Child Development for child-centered outcomes; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Stage】idea / positioning / framework / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Format】Article / Brief Report / Replication
【Route to】jmf-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — family-science data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JMF/NCFR/Wiley URLs behind every fact in this pack
