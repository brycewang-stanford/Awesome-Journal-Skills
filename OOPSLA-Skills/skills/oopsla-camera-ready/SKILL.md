---
name: oopsla-camera-ready
description: Use when converting an accepted OOPSLA paper into its PACMPL journal article — final acmsmall formatting within the 25-page revision cap, de-anonymization and Data-Availability Statement updates, ACM open-access and rights steps, hitting the OOPSLA1 (April) or OOPSLA2 (October) issue, and planning the SPLASH talk.
---

# OOPSLA Camera-Ready

An accepted OOPSLA paper does not go into "conference proceedings" — it
becomes a journal article in PACMPL (Proceedings of the ACM on Programming
Languages), Gold Open Access, in the issue matching its acceptance round:
Round 1 acceptances of the 2027 volume appear as **Issue OOPSLA1**
(published no earlier than April 1, 2027; camera-ready due March 5, 2027);
Round 2 acceptances form **Issue OOPSLA2** (no earlier than October 1, 2027;
camera-ready due August 27, 2027). The talk then happens in person at
SPLASH — for 2027, Prague, October 10–15 (remote presentation is not
possible). Detailed production instructions arrive by email from ACM/the
chairs: treat the acceptance letter as the calendar.

## What changes between acceptance and print

| Item | Submission state | Published-article state |
| --- | --- | --- |
| Class options | `acmsmall,screen,review,anonymous` | `acmsmall,screen` per production instructions |
| Authors | Hidden | Full names, affiliations, ORCIDs, CCS concepts |
| Acknowledgments | Absent | Funders, grant numbers, contributors |
| Data-Availability Statement | Anonymized archive | Real archive — ideally the DOI-stamped Zenodo deposit from artifact evaluation |
| Citations to your own PACMPL-era work | Third person | May remain third person; only add identity where required |
| Page budget | 23 pages | At most 25 pages, plus at most 1 page for data-availability, funding and acknowledgments, plus references; appendices go to supplementary material or Zenodo; no page purchase |

## Reviewer-commitment reconciliation

For papers that passed through Minor Revision, the final version is checked
against the concern list, so build the reconciliation table before touching
LaTeX:

```text
| # | Reviewer requirement | Where satisfied (section/page) | Evidence |
|---|----------------------|--------------------------------|----------|
| 1 | Add baseline B to Table 3 | §5.2, p.14 | artifact run 2026-xx-xx |
| 2 | Clarify Thm 2 side condition | §3.4, p.8 | rewritten statement |
...every row filled before upload; unfillable rows escalated to the chairs.
```

Silently dropping a commitment is the single fastest way to sour the same
committee that will see your group's next submission.

## ACM production specifics to expect

- **Rights and open access.** PACMPL is Gold OA; the rights form determines
  the CC license line printed on page one. The OOPSLA 2027 call states that
  authors at ACM Open institutions pay no APC; others pay the subsidized 2027
  APC of $500 (ACM/SIG members) or $750 (non-members) unless granted a
  (rare) waiver — recheck `dl.acm.org/journal/pacmpl/open-access` before
  advising anyone on cost, and route institutional questions to ACM Open.
- **Metadata is citation-critical.** The article gets a volume, issue
  (OOPSLA1/OOPSLA2), and article number — e.g. the form `PACMPL 10(OOPSLA1)`
  — and that is how others must cite it (`oopsla-related-work`). Get title
  capitalization and author-name forms right in the ACM form, not just the
  PDF, because the DL record is generated from the form.
- **Badges print on the paper.** Artifact badges awarded through the SPLASH
  process appear on the published article; coordinate the artifact timeline
  (`oopsla-artifact-evaluation`) so the deposit DOI exists before the
  camera-ready statement references it.

## Talk planning is part of camera-ready

Accepted papers present in person at SPLASH; for 2027 that means registering
for Prague (October 10–15) and preparing for a PL audience that has already
had access to the published April article for months in the OOPSLA1 case —
the talk should assume the paper is *read*, and spend its minutes on the
mechanism and the demo, not the related-work slide. An accepted-paper poster
is additionally encouraged at SPLASH and is cheap conference-hallway leverage.

## Output format

```text
[Issue target] OOPSLA1 / OOPSLA2, volume <n>
[Reconciliation] <rows total / rows satisfied / escalations>
[De-anonymization] complete: names, ORCID, acks, statement, links
[Rights] form status + license line + APC/waiver status (待核实 items flagged)
[Talk] registration, slot, poster decision
```
