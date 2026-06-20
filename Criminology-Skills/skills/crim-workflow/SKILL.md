---
name: crim-workflow
description: Use as the entry point for any Criminology (ASC / Wiley) manuscript. Routes to the right crim sub-skill based on where you are in the lifecycle and whether the paper is a full Article or a Research Note. Criminology is theory-forward and interdisciplinary, so the router first checks that the paper makes a criminological contribution, not just reports a crime correlation. It dispatches; it does not draft content.
---

# Criminology Workflow Router (crim-workflow)

The orchestrator for a *Criminology* submission. Figure out the stage and the **article type**, then
send the user to the matching skill. *Criminology* is the **interdisciplinary flagship of the American
Society of Criminology** — the router's first job is to make sure the paper advances a **theoretical
or measurement contribution** about crime, not just a finding about a crime dataset.

## When to trigger

- Starting a new *Criminology* paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding between a full **Article** and a **Research Note**
- Returning with a decision letter (route to `crim-rebuttal`)

## First question: which article type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full original study advancing theory/measurement | **Article** | normal pipeline below |
| One focused, self-contained contribution | **Research Note** | normal pipeline, tighter scope |
| Re-examining / reproducing a published finding | replication-style study | `crim-research-design` + `crim-data-and-transparency` |
| Prospective design, data not yet collected | preregister first | `crim-data-and-transparency` (preregistration) early |

> If your design is prospective, lock the pre-analysis plan **before** you see outcomes — that is what
> protects against the "fishing" critique expert reviewers will raise.

## Routing map (stage → skill)

```text
Idea / fit?                       → crim-topic-selection
Where does it sit in the field?   → crim-literature-positioning
What's the theory / mechanism?    → crim-theory-building
Is the design defensible?         → crim-research-design
Are the analyses sound?           → crim-data-analysis
Are the exhibits clear?           → crim-tables-figures
Does it read for criminology?     → crim-writing-style
Data + transparency ready?        → crim-data-and-transparency
How will it be judged?            → crim-review-process
Ready to submit?                  → crim-submission
Got an R&R / decision?            → crim-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → data-and-transparency → review-process → submission → rebuttal`

Iterate: most criminology papers loop theory ↔ design ↔ analysis several times (e.g., refitting a
trajectory model or recidivism survival) before writing-style.

## Anti-patterns

- Treating *Criminology* as a place for a bare crime-data correlation with no theoretical payoff
- Forcing a quantitative template onto qualitative or ethnographic work (the journal is interdisciplinary)
- Choosing the Research Note type for a paper that needs a full Article's evidentiary load
- Leaving the data/transparency package until acceptance instead of building it as you go

## Symptom-to-skill triage (route by the complaint you heard)

Reviewers, advisers, and co-authors describe problems in their own words; the router maps each phrase to
the skill that fixes it. These are the recurring flags for the ASC flagship.

| What was said | Underlying gap | Route to |
|---------------|----------------|----------|
| "atheoretical / just a finding" | mechanism not built | crim-theory-building |
| "selection / not causal" | identification weak | crim-research-design |
| "official records, not offending" | measurement validity | crim-data-analysis |
| "missed key work / wrong debate" | positioning | crim-literature-positioning |
| "belongs at CPP" | scope/fit | crim-topic-selection |
| "can't reproduce this" | transparency | crim-data-and-transparency |

A Research Note routes through the same chain with a tighter scope; the pack does not encode a numeric
cap, so check it against the journal's current submission guidelines before committing to the type.

## Router pass for Criminology

Treat this skill as an executable review pass, not a prose hint. First lock the crime/justice process, measurement validity, research design, and policy consequence; then judge whether the current manuscript answers the venue's real reader: criminology reviewers who expect theory-linked crime, justice, or harm mechanisms plus transparent measurement.

- **Do the pass:** Run the pack as a sequence: fit gate, evidence gate, writing gate, source-map gate, and final output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Justice Quarterly for applied justice, Journal of Quantitative Criminology for methods focus, Social Problems for broader sociological framing; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Article / Research Note / replication-style
【Route to】crim-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — crime data + criminology software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Criminology / ASC / Wiley URLs behind every fact in this pack
