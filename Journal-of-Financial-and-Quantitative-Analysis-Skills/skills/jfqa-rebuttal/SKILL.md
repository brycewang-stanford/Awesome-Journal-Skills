---
name: jfqa-rebuttal
description: Use when planning the strategy and structure for a Journal of Financial and Quantitative Analysis (JFQA) revise-and-resubmit response — point-by-point replies to double-anonymous referees and the handling Managing Editor, new robustness/identification evidence, and code-archive readiness.
---

# JFQA Rebuttal (jfqa-rebuttal)

Use this skill to turn a **JFQA** revise-and-resubmit into an acceptance. The handling **Managing Editor** and the **double-anonymous** referees must see every concern addressed and the contribution sharpened.

## Structure of the response

- A short **cover letter** to the handling editor: thank them, summarize the main changes, and signal how the revision resolves the central concerns.
- A **point-by-point** response to each referee: quote the comment, give the response, and point to the exact revised text/table/figure (page and exhibit numbers).
- Where you disagree, do so respectfully and with evidence, not assertion.

## What JFQA referees typically push on

- **Identification / endogeneity** — add the design fix or a placebo/falsification, not just more controls (see jfqa-identification-strategy).
- **Inference** — clustering dimension, weak-IV-robust CIs, multiple-testing for anomalies.
- **Economic magnitude** — show the effect is economically, not just statistically, meaningful.
- **Robustness** — alternative samples/definitions/specifications.
- **Contribution** — re-state what is new vs. the closest rivals.

## Discipline

- Address **every** comment; an unaddressed point reads as defiance.
- Keep new analyses reproducible — fold them into the master script now so the eventual **JFQA Dataverse** archive stays consistent (see jfqa-replication-and-data-policy).
- Maintain anonymization in the revised PDF and metadata.
- Watch length — do not let the revision balloon past what the journal tolerates.

## Anti-patterns

- A defensive letter that argues rather than revises.
- Selectively answering only the easy comments.
- New results not yet wired into the reproducible pipeline.
- Re-introducing author identity in the revised file.

## Output format

```
【Editor letter】main changes summarized? [Y/N]
【Per-referee】every comment quoted + answered + located? [Y/N]
【New evidence】identification/robustness/magnitude added where asked? [Y/N]
【Reproducible】new analyses in the master script? [Y/N]
【Anonymized】revised PDF + metadata clean? [Y/N]
【Next step】resubmit via Editorial Manager
```
