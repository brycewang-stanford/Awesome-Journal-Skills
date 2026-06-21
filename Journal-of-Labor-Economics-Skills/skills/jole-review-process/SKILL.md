---
name: jole-review-process
description: Use to understand how the Journal of Labor Economics (JOLE) actually reviews a paper — single-blind refereeing, the non-refundable submission fee, Editorial Manager, the SOLE society tie, and what labor referees expect. Explains the process; it does not draft the manuscript.
---

# Review Process (jole-review-process)

## When to trigger

- You are unsure whether JOLE is double-blind (it is not) and how that changes the submission
- You need to budget for the submission fee and understand when the decision is released
- You want to know what labor-economics referees and editors look for before you submit
- You are calibrating expectations for an R&R versus a reject

## How JOLE review works

- **Single-blind (single-anonymized).** Referees are anonymous, but they **know the authors' identities**. Because of this the manuscript is **not** anonymized: it begins with a title page naming all co-authors, their institutions, and emails, and references are **not** blinded. Do not strip identifying material — that is correct for double-blind journals but wrong here.
- **Submission via Editorial Manager** (`editorialmanager.com/jole`), with a cover letter. JOLE is the official journal of the **Society of Labor Economists (SOLE)** and is published by the **University of Chicago Press**.
- **Non-refundable submission fee (since July 1, 2018): $100 for SOLE members, $175 for non-members.** It is charged **even if the paper is desk-rejected**, and the **decision is not released until the fee is paid** — so the fee gates your result, not just your submission. SOLE membership is the cheaper path.
- **Publication-ethics regime:** UChicago Press / **COPE** guidelines, with explicit attention to confidential data and research on vulnerable / human subjects. Flag proprietary data or human-subjects concerns up front.
- **Review clock:** do not promise the author a specific turnaround time; this pack has no current official review-clock source encoded.
- **Editor:** the current Editor-in-Chief is **Peter Kuhn, UC Santa Barbara**. Confirm the live board page before naming any editor or conflict in a cover letter.

## What labor referees expect

JOLE referees are labor economists judging a general-interest labor audience. They reward:

1. A **first-order labor question** (wages/earnings, employment, human capital, labor supply/demand, family, discrimination, unions, migration, institutions/policy) that matters beyond one niche.
2. **Credible identification** matched to labor data (DID / event study with modern estimators, IV including shift-share, RDD at eligibility thresholds, RCTs, AKM firm–worker designs).
3. **Disciplined data work** — appropriate sample construction from CPS/ACS/registers, correct standard errors, robustness that a labor referee would otherwise demand.
4. **A replicable empirical core** — JOLE publishes empirical/simulation/experimental papers only if data are documented and available, with deposit to the JOLE Dataverse after acceptance (see jole-replication-and-data-policy).
5. **Word economy** — the ~20,000-word soft cap (full-page exhibit = 500 words) signals that referees value a tightly argued paper, not a sprawling one.

## Checklist

- [ ] Manuscript is **non-anonymized** (single-blind): title page names all authors
- [ ] Submission fee budgeted; you know the decision is withheld until it is paid
- [ ] SOLE membership considered (lower fee)
- [ ] Proprietary-data / human-subjects issues flagged to the editor at submission
- [ ] Identification and robustness pre-empt the obvious labor-referee objections
- [ ] Live board checked before naming an editor or conflict

## Anti-patterns

- Treating JOLE as double-blind and stripping author identity from the manuscript
- Forgetting the fee blocks the decision, then being surprised no result arrives
- Promising a specific review turnaround
- Naming an editor or conflict without checking the live board page
- Submitting an empirical paper with no plan to make the data available

## Output format

```
【Review model】single-blind, manuscript NOT anonymized [confirmed Y/N]
【Fee】$100 SOLE / $175 non-member, non-refundable, gates the decision [budgeted Y/N]
【Society】SOLE membership considered for lower fee [Y/N]
【Ethics】proprietary data / human subjects flagged [Y/N/NA]
【Referee readiness】labor question + identification + replication ready [Y/N each]
【Next step】jole-submission preflight
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JOLE URLs, source evidence, and live-check items
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — labor data sources and packages
