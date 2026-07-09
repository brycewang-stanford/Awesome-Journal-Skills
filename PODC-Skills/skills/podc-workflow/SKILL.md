---
name: podc-workflow
description: Use when planning an ACM PODC campaign end to end — running the single annual cycle backward from the February deadline through abstract registration, lightweight double-blind review, the late-April notification, the May camera-ready, and the arXiv full version — and coordinating the regular-paper-vs-Brief-Announcement decision along the way.
---

# PODC Workflow

Plan the year backward from the deadline. PODC runs a **single annual cycle** with a
straightforward accept/reject decision and **no journal-style revision round**, so unlike a
multi-cycle or major-revision venue, you get one shot per year — the leverage is all in what you
submit, not in a second read. Dates below are the PODC 2026 cycle (read 2026-07-09 via renderings;
see `resources/official-source-map.md`); reopen the live Important Dates page each year.

## The PODC 2026 calendar (one cycle)

| Milestone | Date (23:59 AoE) | What it gates |
|---|---|---|
| Abstract registration | **11 February 2026** | Title/abstract/authors/conflicts locked; no PDF accepted later without it |
| Full-paper submission | **16 February 2026** | The anonymized PDF (regular or Brief Announcement) |
| Notification | **29 April 2026** | Accept / reject |
| Camera-ready | **20 May 2026** | Final ACM proceedings PDF + rights forms |
| Conference | **6-10 July 2026** | In-person presentation at Royal Holloway, University of London |

## Running the year backward

```text
[Jul 2026]        present in person at Royal Holloway (co-located with SPAA); a paid registration
                  by one author is required
[May 20]          camera-ready: de-anonymize, compress to <=10 proceedings pages, ACM rights
[Apr 29 -> May]   notification -> if accepted, camera-ready + post the full version to arXiv
[Feb 16]          full-paper submission (regular or Brief Announcement), double-blind
[Feb 11]          abstract registration (hard prerequisite)
[Dec-Jan]         finish proofs; run podc-writing-style + podc-experiments; decide the track
[Sep-Nov]         prove the result; fix the model; run podc-topic-selection to confirm PODC vs DISC/SPAA
```

The scarce resource is **proof-closing time before mid-February**. A result that is "almost proved"
in January is a Brief Announcement in February, not a regular paper — plan the proof timeline, not
just the writing timeline.

## Where the leverage is (and is not)

- **Largest lever — the topic/abstract at registration.** A precise abstract and the right topic
  tags route your paper to reviewers who work in your model. A mismatched abstract sends a
  shared-memory paper to message-passing reviewers.
- **Second lever — the regular-vs-Brief-Announcement choice.** If the proof will not close by
  16 February, a Brief Announcement timestamps the result now and keeps a full paper open for a
  later venue; forcing an unfinished result into a regular paper spends the slot on a rejection.
- **No revision lever.** PODC gives accept/reject; there is no Major Revision to rescue a
  borderline paper. Everything that would have gone into a revision must be in the initial
  submission.
- **Possible rebuttal lever (待核实).** Whether the cycle runs an author-response phase varies —
  confirm on the call; if it exists, see `podc-author-response`.

## Coordinating the co-located venues

PODC 2026 is co-located with **SPAA 2026** at the same venue and dates. If your result straddles
distributed and parallel computing, decide the target *before* the February deadline (SPAA and PODC
have separate submission processes and committees) using `podc-topic-selection` — do not assume one
submission reaches both.

## The full-version / arXiv track (parallel to the whole cycle)

- You may post the full version (with all proofs) on **arXiv** at any time — before, during, or after
  review. PODC does not treat a preprint as dual submission.
- During **double-blind review**, an arXiv link that de-anonymizes you is a risk; either post
  without pointing the submission at it, or rely on the community norm and keep the submission PDF
  self-contained. Confirm the cycle's exact expectation.
- After acceptance, the arXiv full version is where the proofs the 10 proceedings pages cannot hold
  actually live; keep it in sync with the camera-ready.

## Common calendar mistakes

- **Missing abstract registration** (11 Feb) and discovering on 16 Feb that no PDF slot exists.
- **Treating notification as the finish line** — camera-ready (20 May) has its own ACM rights and
  compression work; block time for it.
- **Assuming a revision round exists** — it does not; budget the proof to be *done* at submission.
- **Projecting last year's dates** — the split abstract/paper deadlines and the double-blind wording
  are decided per edition.

## Output format

```text
[Cycle] PODC <year>; key dates (registration / submission / notification / camera-ready / conference)
[Track plan] regular paper / brief announcement, with the proof-completion date that justifies it
[Backward plan] milestone -> owner -> date, from conference back to today
[Leverage] topic/abstract routing; track choice; (rebuttal if the cycle has one)
[arXiv] full-version posting plan and its double-blind implications
[Risks] proof not closing by Feb; missed registration; wrong sibling venue
```
