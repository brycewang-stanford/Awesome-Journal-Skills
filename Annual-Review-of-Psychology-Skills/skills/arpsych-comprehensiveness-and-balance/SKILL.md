---
name: arpsych-comprehensiveness-and-balance
description: Use when checking that an Annual Review of Psychology (ARPsych) review covers the literature even-handedly — across labs, paradigms, and rival theories — weighs evidence by credibility, and avoids self-promotion. Audits coverage and fairness; it does not build the search (arpsych-literature-synthesis) or design the spine (arpsych-organizing-framework).
---

# Comprehensiveness & Balance (arpsych-comprehensiveness-and-balance)

## When to trigger

- The framework is set but coverage may be lopsided toward one camp or method
- The author's own work is cited far more than its share of the field
- Contested effects are presented as settled (or vice versa) without weighing evidence
- A rival theory or a contradicting literature is under-represented or dismissed in a line

## Why balance is editorial currency at ARPsych

ARPsych authors are chosen partly for the standing to be **even-handed**, and the Committee assesses delivered reviews for **accuracy, rigor, and balance** (检索于 2026-06；以官网为准). A review of record cannot read as advocacy for the author's lab or favored theory. The job here is to audit the draft against four failure modes specific to high-stakes psychology reviews.

### 1. Coverage balance (across labs and paradigms)
Use the evidence matrix's `lab/camp` and `paradigm` columns. If three groups or one method dominate the citations, ask whether that reflects the field or the author's reading. Actively seek the work you find *least congenial* — the strongest version of the opposing view, not a strawman.

### 2. Credibility weighting (not vote-counting)
Do not tally "12 studies found X, 4 found not-X." Weigh by **design strength, sample, and replication status**. A single large, preregistered, multi-site study can outweigh a dozen small underpowered ones. Post-replication-crisis, ARPsych readers expect you to flag effects that failed to replicate rather than reviewing them as established (检索于 2026-06；以官网为准).

| Signal | Up-weight | Down-weight |
|--------|-----------|-------------|
| Replication | direct + conceptual replications | single-lab, never replicated |
| Power/sample | large, well-powered, diverse | small, WEIRD-only, p≈.05 |
| Design | preregistered, controlled, longitudinal | post-hoc, cross-sectional, flexible analysis |
| Effect realism | meta-analytic, corrected for bias | uncorrected, funnel-asymmetric |

### 3. Theory balance
Present rival accounts at their strongest, then adjudicate on evidence — do not settle a live debate by authorial fiat. If the field is genuinely unresolved, *say so*; an honest "we don't yet know" is more authoritative than a forced verdict.

### 4. Self-promotion audit
Count citations to the author team versus comparable groups. The author's work belongs in the review in proportion to its place in the field, not as the center of gravity. Reviewers and the Committee notice citation self-concentration.

## Checklist

- [ ] Citation distribution checked: no single lab/camp dominates beyond its field share
- [ ] Strongest version of each rival view is represented (no strawmen)
- [ ] Evidence weighed by design/power/replication, not vote-counted
- [ ] Non-replicating or bias-prone effects flagged, not reviewed as settled
- [ ] WEIRD/sample-diversity limits of the literature acknowledged
- [ ] Live debates left open where the evidence is genuinely unresolved
- [ ] Self-citation is proportional to the author's actual place in the field
- [ ] Every framework cell is covered to a comparable depth

## Anti-patterns

- Advocacy review: marshaling the literature to support the author's theory
- Vote-counting effects instead of weighing by credibility
- Reviewing failed-to-replicate effects as if they were robust
- Strawmanning the rival account, then "refuting" it
- Disproportionate self-citation (the most-noticed ARPsych balance failure)
- Forcing a verdict on a debate the field has not settled
- Deep coverage of the author's favorite cell, thin coverage elsewhere

## Output format

```text
【Coverage balance】lab/paradigm concentration audited? dominant group share OK? Y/N
【Credibility weighting】weighed by design/power/replication (not vote-counted)? Y/N
【Replication hygiene】non-replicating effects flagged? Y/N
【Theory balance】rivals at strongest; debates left open where unresolved? Y/N
【Self-promotion】self-citation proportional to field place? Y/N
【Cell depth】all framework cells covered comparably? Y/N
【Next step】→ arpsych-tables-figures (summarize the balanced evidence)
```
