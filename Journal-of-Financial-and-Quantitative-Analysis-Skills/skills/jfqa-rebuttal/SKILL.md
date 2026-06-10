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

## Comment triage before drafting a word

| Comment type | Required artifact | Where it lands |
|---|---|---|
| Identification / endogeneity demand | new design element, placebo, or falsification table | main text, with the old spec moved to the appendix |
| Inference complaint | re-estimated tables under the requested SE scheme | main tables updated; alternates in an Internet Appendix |
| "Economically small" | scaling paragraph (one-SD, %-of-mean, dollar value) | intro and the main-table note |
| Missing rival paper | contrast paragraph plus, if needed, a horse-race column | literature positioning + one exhibit |
| Robustness fishing list | a consolidated robustness table, not ten new tables | Internet Appendix, summarized in one text paragraph |
| "Not interesting / not JFQA" | a reframed contribution case in the editor letter | cover letter; tables alone cannot fix this one |

Triage first, then budget: the identification items consume most of the calendar; the scaling and citation items are cheap and should never be the reason a deadline slips.

## Worked reply to an inference comment (numbers illustrative)

Referee: "Clustering by firm only likely understates the standard errors given common time shocks." Model response: agree without hedging; re-estimate every main table with two-way firm-and-year clustering; report that the headline t-statistic moves from 4.2 to 3.1 and the conclusion stands; add a wild-cluster-bootstrap panel as Internet Appendix Table IA.3 for the specifications with few clusters; end with the exact page and table numbers where the manuscript changed. The reply quotes the comment in full, leads with the new result rather than the rhetoric, and gives the referee a checkable location for every claim.

## Sequencing the JFQA revision

1. Identification and inference fixes first — they can change every downstream number.
2. Then re-scale magnitudes and refresh the exhibits (notes must reflect the new SE choices).
3. Then the framing edits: abstract still one paragraph at ≤ 100 words after all changes.
4. Last, regenerate everything from the master script and re-anonymize the PDF; an R&R at a journal that prints under 9% is an opportunity to over-deliver, not a promise.

## Output format

```
【Editor letter】main changes summarized? [Y/N]
【Per-referee】every comment quoted + answered + located? [Y/N]
【New evidence】identification/robustness/magnitude added where asked? [Y/N]
【Reproducible】new analyses in the master script? [Y/N]
【Anonymized】revised PDF + metadata clean? [Y/N]
【Next step】resubmit via Editorial Manager
```
