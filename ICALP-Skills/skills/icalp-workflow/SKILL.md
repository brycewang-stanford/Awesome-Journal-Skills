---
name: icalp-workflow
description: Use when planning an ICALP (EATCS) campaign backward from its February deadline (or, for Track B since ICALP 2027, the earlier September round), through abstract registration, the anonymous submission, the Track B rebuttal window, notification, and the LIPIcs camera-ready and presentation, and when coordinating a full-version (arXiv/ECCC) release alongside the anonymous submission.
---

# ICALP Workflow

Run the ICALP year backward from the **February deadline**. Track A still has one research-paper
deadline per year, so a missed February means a full year lost. **Track B, from ICALP 2027, has two
rounds**: a September round (ICALP 2027: 15 September 2026, notification 8 December 2026) and the
usual February round; a paper may enter only one, and a round-1 reject cannot re-enter round 2. The
calendar below combines the ICALP 2027 Track B call (read 2026-11-24) with the ICALP 2026 anchor for
the February round, whose 2027 dates were still TBA; reopen the live site
(`https://icalp.uj.edu.pl/`) and the correct track's HotCRP deadline before trusting any date.

## The calendar (ICALP 2027, with the ICALP 2026 February-round anchor)

```text
[mid September]   Track B round 1 only (2027 edition: 15 Sep 2026, AoE) — rebuttal 5-9 Nov 2026,
                  notification 8 Dec 2026; final, no carry-over
[early February]  Abstract registration (2026: 3 Feb, AoE; 2027 round 2: TBA)
[~3 days later]   Full submission     (2026: 6 Feb, AoE; 2027: TBA, "early-mid February 2027")
                  — anonymized full version, no page limit, merits within the first ten pages
[late March]      Track B rebuttal    (2026: 21-24 Mar; 2027 round 2: TBA) — Track A: in 2026,
                  contacted only on correctness issues
[late April]      Notification        (2026: 20 Apr; 2027: TBA)
[May]             Camera-ready in LIPIcs (2026: 11 May; 2027: TBA)
[July]            Conference          (2027: 5-9 Jul, Kraków, in person; 2026: 7-10 Jul, Royal Holloway)
```

## Backward plan from the February deadline

- **T-12 to T-8 weeks:** prove the theorems. ICALP results are proofs, and a proof is not "almost
  done" until it is written in full — budget for the gap between "I believe it" and "it is on paper."
- **T-6 weeks:** decide the **track** (`icalp-topic-selection`) and settle the model and theorem
  statements; these anchor the whole paper.
- **T-4 weeks:** draft the first ten pages (merits, contributions, key ideas) and the full proofs
  in parallel; there is no page limit, so the submission *is* the full version
  (`icalp-supplementary`).
- **T-2 weeks:** anonymize for lightweight double-blind, rewrite self-citations in third person,
  write the AI-use disclosure if AI tools were used in the research (ICALP 2027), and prepare (but do
  not necessarily post) the arXiv/ECCC full version.
- **T-1 week:** register the abstract; run `icalp-submission` on the near-final PDF.
- **Deadline day:** submit to the correct track's HotCRP server well before the AoE cutoff; flag
  student-only authorship if eligible.

## The Track B rebuttal (know if it applies to you)

The tracks diverge after submission:

- **Track A:** in ICALP 2026, no general rebuttal — authors were contacted **only** if reviewers
  found a **correctness issue** to resolve. The ICALP 2027 Track A call is not yet posted; plan as if
  there is no author interaction until it says otherwise.
- **Track B:** a **rebuttal window** in each round (ICALP 2027 round 1: 5-9 November 2026; ICALP
  2026: 21-24 March) where authors view initial reviews and respond. Reserve those days; see
  `icalp-author-response`.

Do not assume both tracks behave alike, and do not count on a rebuttal for a Track A paper.

## Coordinating the full version

- A **full version on arXiv/ECCC/HAL is standard and encouraged** — it is how the community checks
  proofs. ICALP encourages it, and since there is no page limit the submission itself can be the
  full version. But during review, keep it from **breaking anonymity** (do
  not cite "our arXiv paper"); a separately hosted full version that a determined reviewer could find
  is acceptable under the lightweight regime, but do not advertise it.
- Post or update the public full version around **notification/camera-ready**, and make the LIPIcs
  version and the arXiv version consistent.

## After notification

- **Accept:** move to `icalp-camera-ready` — reformat to `lipics-v2021`, restore author names and
  acknowledgements (de-anonymize), and hit the LIPIcs production deadline. Arrange for at least one
  author to register and present **in person** (ICALP 2027 is planned as a physical event).
- **Reject:** no appeal. Use `icalp-topic-selection`'s routing table — a strong result may fit
  STOC/FOCS/SODA/LICS or a journal on a nearer calendar; incorporate the reviews before resubmitting.

## Milestone checklist

```text
[ ] Track chosen and correct HotCRP server identified
[ ] Theorems fully proved (not just believed)
[ ] Track B: round chosen (September or February) — one round only
[ ] Abstract registered before any earlier registration cutoff
[ ] Merits within the first ten pages + complete proofs (no page limit)
[ ] AI-use disclosure written if AI tools were used
[ ] Lightweight double-blind sweep passed
[ ] Track B: rebuttal window reserved (Track A: none expected)
[ ] On accept: LIPIcs camera-ready + presenter arranged
```

## Output format

```text
[Cycle target] ICALP <year>, Track A / Track B
[Countdown] weeks to the deadline (Track B: which round); abstract-registration date
[Current stage] proving / drafting / anonymizing / submitted / rebuttal (B) / notified / camera-ready
[Track-specific] Track B rebuttal window reserved? / Track A correctness-contact readiness
[Next actions] <ordered, with dates tied to the chosen deadline>
```
