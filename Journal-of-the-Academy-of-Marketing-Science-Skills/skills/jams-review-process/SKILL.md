---
name: jams-review-process
description: Use when understanding how Journal of the Academy of Marketing Science (JAMS) review and decisions work — the Springer Editorial Manager flow, the double-anonymized developmental review, the area-editor structure, the dual theory-and-managerial evaluation bar, and how to read a decision letter. Explains the process and reads the letter; it does not draft the response (jams-rebuttal).
---

# Review Process (jams-review-process)

## When to trigger

- Before submitting, to set realistic expectations about JAMS review
- A decision letter arrived and you need to interpret it before responding
- You are unsure who decides at JAMS and what reviewers are told to weigh
- You want to know what conditional acceptance triggers (data/code deposit)

## How JAMS review works

- **Double-anonymized.** Authors and reviewers are concealed from each other; keep every round anonymized, including revised files and any preregistration links.
- **Developmental philosophy.** JAMS, like the AMS journals, runs a **developmental review** — area editors and reviewers aim to improve promising papers across rounds, not merely gatekeep. A well-run R&R is the realistic best case; first-round acceptance is essentially unheard of.
- **Decision structure.** Manuscripts are handled by an **Area / Associate Editor** under the Co-Editors-in-Chief (Stephanie M. Noble and Charles H. Noble, University of Tennessee, since June 2024 — verified 2026-06-22; re-verify the masthead before submission). Your keyword/area choices in Editorial Manager influence routing, so choose them to reach the right editor and reviewers.
- **What reviewers weigh.** JAMS's evaluation is **dual**: (1) a genuine **theoretical contribution** to a broad marketing-science question, and (2) a clear **managerial contribution** — what a decision maker should do. Expect probes on construct validity / CMV (survey), endogeneity / identification (secondary data), mechanism and power (experiments), and on whether the contribution is more than a new-context replication.
- **Integrity.** Springer plagiarism screening; no concurrent submission; research-data and ethics policies apply.

## Likely decisions

| Decision | What it means |
|---|---|
| Desk reject | Out of scope, not a broad marketing-science contribution, or no managerial relevance |
| Reject (after review) | Theoretical or managerial contribution, or identification/validity, judged insufficient |
| Major revision (R&R) | Promising core; substantial work required (often multi-round) |
| Minor revision | Contribution sound; targeted fixes |
| Conditional acceptance | Triggers final transparency steps — data/code availability statement and any required deposit |

## Reading the decision letter

- **Read the AE/editor letter first** — it states the path to acceptance and which concerns are decisive ("must address") versus secondary.
- **Cluster reviewer comments** by theme: theoretical contribution, managerial relevance, construct validity/measurement, identification/analysis, positioning, exposition.
- **Flag the gatekeeping themes** — any comment touching the **theoretical-contribution** or **managerial-relevance** bar is top priority; these are JAMS's twin gates.
- **Separate new-data/analysis requests from reframing requests** — they have very different timelines.
- **Anticipate transparency** — if nearing conditional acceptance, prepare the data/code availability statement and any repository deposit.

## Calibrate expectations before you submit

- **First-round R&R, not acceptance, is the goal.** JAMS's developmental review means most successful papers go through two or more revision rounds; budget months, not weeks, between rounds.
- **Desk-reject risk is highest on scope and relevance.** A paper that is narrow, modeling-first, purely consumer-psychology, or missing a managerial implication is the most common early casualty — fix fit (`jams-topic-selection`) before submitting.
- **Reviewer continuity matters.** The same reviewers usually see your revision, so a response that visibly addresses *their* concern (not a generic improvement) is what advances the paper.
- **Routing is partly in your hands.** Keyword and area-of-interest choices in Editorial Manager steer the manuscript toward an area editor whose domain matches the paper; a mismatch slows the process and risks an unsympathetic read.

## Where JAMS differs from the siblings' processes

- **vs. JM (AMA):** JM is double-anonymized via ScholarOne with a Coeditor structure and a hard page limit; JAMS runs on Springer Editorial Manager with an area-editor structure and article-type guidance rather than one fixed page cap.
- **vs. JMR:** JMR enforces exact three-digit p-values and a Web Appendix convention; JAMS emphasizes construct validity and the managerial contribution more than a single statistics-reporting rule.
- **vs. Marketing Science / JCR:** those weigh modeling rigor or consumer-theory depth respectively; JAMS will not accept a paper strong on one of those but thin on the managerial takeaway.

## After the decision: the immediate moves

- **Desk reject:** re-evaluate fit before resubmitting elsewhere — a scope/relevance desk reject usually means the paper needs `jams-topic-selection` and `jams-contribution-framing` work, not a quick reformat.
- **Reject after review:** mine the reports for the decisive flaw; if it is fixable (identification, validity, a missing study), the work may suit a sibling or a later JAMS resubmission as a new paper — but do not re-submit the same paper to JAMS without a fundamental change.
- **R&R (major/minor):** move straight to `jams-rebuttal`; revise the manuscript before drafting the letter, and lead with the editor's decisive concerns.
- **Conditional acceptance:** finalize the data/code availability statement and any repository deposit, confirm declarations, and complete the production checklist.

Throughout, keep the manuscript and all correspondence anonymized until a decision releases that requirement; reviewers see your revisions, and a slip that reveals identity can compromise the round.

## Checklist

- [ ] AE/editor letter parsed: decisive vs. secondary concerns identified
- [ ] Reviewer comments clustered by theme
- [ ] Theoretical-contribution and managerial-relevance comments flagged top priority
- [ ] New-data vs. reframing requests separated for timeline planning
- [ ] Validity/identification concerns (CMV, endogeneity) mapped to specific fixes
- [ ] Conditional-acceptance transparency steps anticipated (data/code statement)

## Anti-patterns

- Treating all reviewer comments as equal, ignoring the editor's stated priorities
- De-anonymizing yourself in a response or a revised file
- Reading a major R&R as a near-accept and doing superficial edits
- Neglecting the managerial-contribution comments because the theory comments feel weightier
- Deferring data/code-availability prep until after conditional acceptance

## Output format

```text
【Decision】desk reject / reject / major R&R / minor / conditional accept
【Editor priorities】must-address: [...]; secondary: [...]
【Comment clusters】theory / managerial / measurement / identification / positioning / exposition
【Gatekeeper flags】theoretical + managerial contribution comments: [...]
【New data vs. reframing】[...]
【Transparency next】data/code availability + deposit readiness: [...]
【Next step】jams-rebuttal
```
