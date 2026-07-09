---
name: icalp-workflow
description: Use when planning an ICALP (EATCS) campaign backward from its single annual February deadline, through abstract registration, the anonymous submission, the Track B rebuttal window, the April notification, and the LIPIcs camera-ready and presentation, and when coordinating a full-version (arXiv/ECCC) release alongside the anonymous submission.
---

# ICALP Workflow

Run the ICALP year backward from the **single annual February deadline**. ICALP posts one
research-paper deadline per year across its two tracks, so unlike a multi-deadline venue there is no
"next cycle in a few months" — a missed February means a full year lost. The calendar below is the
ICALP 2026 (53rd, Royal Holloway) cycle, verified 2026-07-09; reopen the live Important Dates page and
the correct track's HotCRP deadline before trusting any date.

## The one-cycle calendar (ICALP 2026 anchor)

```text
[early February]  Abstract registration (2026: 3 Feb, AoE) — title/abstract/authors/conflicts
[~3 days later]   Full submission     (2026: 6 Feb, AoE) — anonymized 15-page PDF + appendix
[late March]      Track B rebuttal    (2026: 21-24 Mar) — Track B only; Track A no general rebuttal
[late April]      Notification        (2026: 20 Apr)
[spring]          Camera-ready in LIPIcs (lipics-v2021); exact date 待核实 per cycle
[July]            Conference          (2026: 7-10 Jul, workshops 6 Jul), Royal Holloway
```

## Backward plan from the February deadline

- **T-12 to T-8 weeks:** prove the theorems. ICALP results are proofs, and a proof is not "almost
  done" until it is written in full — budget for the gap between "I believe it" and "it is on paper."
- **T-6 weeks:** decide the **track** (`icalp-topic-selection`) and settle the model and theorem
  statements; these anchor the whole paper.
- **T-4 weeks:** draft the 15-page body and the full proofs in the appendix / full version in
  parallel; the body sketches, the appendix proves (`icalp-supplementary`).
- **T-2 weeks:** anonymize for lightweight double-blind, rewrite self-citations in third person, and
  prepare (but do not necessarily post) the arXiv/ECCC full version.
- **T-1 week:** register the abstract; run `icalp-submission` on the near-final PDF.
- **Deadline day:** submit to the correct track's HotCRP server well before the AoE cutoff; flag
  student-only authorship if eligible.

## The Track B rebuttal (know if it applies to you)

The tracks diverge after submission:

- **Track A:** no general rebuttal. Authors are contacted **only** if reviewers find a **correctness
  issue** to resolve. Plan as if there is no author interaction.
- **Track B:** a **rebuttal window** (2026: 21-24 March) where authors view initial reviews and
  respond. Reserve those days; see `icalp-author-response`.

Do not assume both tracks behave alike, and do not count on a rebuttal for a Track A paper.

## Coordinating the full version

- A **full version on arXiv/ECCC/HAL is standard and encouraged** — it is how the community checks
  proofs the 15-page body only sketches. But during review, keep it from **breaking anonymity** (do
  not cite "our arXiv paper"); a separately hosted full version that a determined reviewer could find
  is acceptable under the lightweight regime, but do not advertise it.
- Post or update the public full version around **notification/camera-ready**, and make the LIPIcs
  version and the arXiv version consistent.

## After notification

- **Accept:** move to `icalp-camera-ready` — reformat to `lipics-v2021`, restore author names and
  acknowledgements (de-anonymize), and hit the LIPIcs production deadline. Arrange for at least one
  author to present.
- **Reject:** no appeal. Use `icalp-topic-selection`'s routing table — a strong result may fit
  STOC/FOCS/SODA/LICS or a journal on a nearer calendar; incorporate the reviews before resubmitting.

## Milestone checklist

```text
[ ] Track chosen and correct HotCRP server identified
[ ] Theorems fully proved (not just believed)
[ ] Abstract registered before the earlier February cutoff
[ ] 15-page body + complete appendix/full-version proofs
[ ] Lightweight double-blind sweep passed
[ ] Track B: rebuttal window reserved (Track A: none expected)
[ ] On accept: LIPIcs camera-ready + presenter arranged
```

## Output format

```text
[Cycle target] ICALP <year>, Track A / Track B
[Countdown] weeks to the February deadline; abstract-registration date
[Current stage] proving / drafting / anonymizing / submitted / rebuttal (B) / notified / camera-ready
[Track-specific] Track B rebuffer window reserved? / Track A correctness-contact readiness
[Next actions] <ordered, with dates tied to the single annual deadline>
```
