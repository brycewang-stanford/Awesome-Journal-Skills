---
name: icde-submission
description: Use when auditing an IEEE ICDE research-track submission for round choice, Microsoft CMT setup, conflict declarations, the IEEE 12-page format, single-blind requirements, supplemental-material availability, the June/November two-round calendar, desk-reject triggers, and final-week sequencing for a data-engineering systems paper.
---

# ICDE Submission

Use this for an ICDE research-track submission audit. Reopen the current edition's Call for
Research Papers, Important Dates, and Submission Guidelines before giving deadline-ready
advice; ICDE re-declares its rules on a fresh site each year.

## Submission audit

- Confirm the target track. ICDE runs a **research track**, an **industry and applications
  track**, plus demos/tutorials — route with `icde-topic-selection` before formatting.
- Pick the **round** consciously. Each ICDE edition takes research papers in **two rounds**
  (ICDE 2027: Round 1 paper deadline June 11, 2026; Round 2 November 11, 2026). A paper
  rejected in Round 1 is **not** eligible for Round 2 — it waits for the next edition. Choose
  the round you can actually be ready for, not the nearest one.
- Set up **Microsoft CMT** early: every co-author needs a CMT profile, and conflicts (domain
  and individual) are author-declared in CMT. A missing conflict is a review-integrity issue,
  not a formatting nit.
- Apply the **IEEE double-column template** without margin, font, or spacing edits. Long
  research papers run to **12 pages plus unlimited references** (short papers 6 pages plus
  references, per the ICDE 2026 wording — re-confirm for the current edition).
- ICDE is **single-blind**: author names stay on the paper. Do **not** anonymize author
  identity, self-citations, or the repository — that is a SIGMOD reflex, wrong here.
- Attach **supplemental material** (code, data, artifacts). Availability is explicitly
  considered in the evaluation, so an empty supplement is a scored weakness.
- Check the **original-work** rule: no prior publication longer than roughly four double-column
  pages covering the same work.

## Blocking risks

- Submitting to a round the paper cannot be ready for, then being locked out of the same
  edition's second round after a Round 1 reject.
- Overlength main text or an altered IEEE template.
- Missing or wrong CMT conflict declarations for any co-author.
- No supplemental material where the call expects availability evidence.
- A systems claim with no operating point, tuned baselines missing, or cost undisclosed.

## Desk-reject and triage table

| Trigger | Severity at ICDE | Repair window |
|---|---|---|
| Overlength main text | Desk reject | None after the deadline |
| IEEE template tampering | Desk reject or chair flag | None |
| Missing CMT conflict for a co-author | Integrity flag, possible desk reject | Only before the deadline |
| Empty or unrunnable supplement | Scored weakness | Fixable before the deadline |
| Round-1 reject re-sent to Round 2 | Administrative reject | None — wait for next edition |
| Unfalsifiable performance claim | Review-stage damage | Fixable in the writing/experiments pass |

## Final-week sequence for a systems paper

1. Freeze the mechanism description and the claims map so every figure has a home in the text.
2. Regenerate each figure and table from logged runs so the PDF and supplement cannot diverge.
3. Fill the supplement: `run_all.sh`, `run_small.sh`, a README that orients a reviewer in a
   minute, and the workload generators with their seeds.
4. Verify every co-author's CMT profile exists and all conflicts are filed.
5. Confirm the abstract in CMT matches the PDF abstract, and the paper is within 12 pages.

## Format anchors

- IEEE two-column layout is tight; wide system diagrams, algorithm blocks, and multi-series
  throughput plots that fit a one-column draft routinely overflow — compress early.
- Every number in the pack (page limit, deadlines, blind policy) describes a specific edition;
  treat all of them as provisional and re-check the current call.

## Output format

```text
[ICDE readiness] Ready / Needs fixes / Not ready
[Round + track] <research/industry, Round 1 or Round 2, with source date>
[Blocking checks] <round-eligibility / page / CMT-conflicts / supplement / IEEE-format>
[Evidence risk] <one systems-evaluation issue>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before the round deadline>
```
