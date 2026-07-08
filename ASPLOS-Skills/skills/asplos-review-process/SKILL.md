---
name: asplos-review-process
description: Use when reasoning about how an ASPLOS submission will be judged — the two-page rapid-review screen and what it filters, full double-blind review, the author-response window, the Accept / Major Revision / Reject outcome set, how revisions are re-reviewed as submissions, and where authors actually hold leverage in each stage.
---

# ASPLOS Review Process

ASPLOS 2027 runs a staged pipeline that differs from every sibling venue in two
places: an explicit **rapid-review screen on the first two pages**, and a **Major
Revision** outcome with journal-like mechanics. Everything below is the 2027 cycle
as verified 2026-07-08; stage design is re-decided per edition.

## Stage map

| Stage | Who reads what | Author leverage |
|---|---|---|
| Rapid review | Committee members read **pages 1-2 only**, double-blind | Total — you wrote those pages |
| Full review | Full paper, double-blind, multiple reviewers | High before submission, zero during |
| Author response | Reviews + your rebuttal (reading expectation ≈ 800 words) | Moderate — corrections and answers land |
| Decision | Accept / **Major Revision** / Reject | None |
| Revision re-review | Revised paper + change note, judged as a submission | High — the requirements are written down |

## What the rapid review is for — in the CFP's own framing

The 2027 CFP models the screen on early triage at high-impact journals: most
submissions may not advance past it, and the point is to concentrate expert
reviewer effort on papers where the committee can review with high confidence. Two
consequences for authors:

- The screen **prioritizes work at the architecture-languages-OS intersection**.
  A paper that reads like a pure single-community result in its first two pages is
  the archetypal rapid casualty, whatever its page-7 content.
- Rapid rejection is cheap and fast for the PC but carries little diagnostic signal
  for you beyond "the first two pages did not make the case." Re-aim the framing
  before re-aiming the venue.

## Full review: what systems-intersection reviewers probe

A useful red-team script — have a non-author run it against the submitted PDF:

```text
R1  Is the claimed coupling real? Try to mentally re-implement each half
    without the other; if either succeeds, expect a "why not <single venue>?"
R2  Is the baseline the strongest deployed alternative, tuned, on the same
    platform? Find one stronger baseline the paper skipped.
R3  Does the evidence class match the claim (silicon vs FPGA vs simulator)?
    Flag any latency/energy claim resting on an unvalidated model.
R4  Attribution: is the win traced to the mechanism via ablation, or asserted?
R5  Generality: does anything survive a workload/technology parameter change?
R6  Are the citation and formatting rules met? (Reviewers do notice.)
```

## The Major Revision channel, precisely

- Offered to some submissions **in addition to** Accept and Reject.
- The revision is submitted **at the camera-ready deadline — six weeks after
  notification** — a short window that assumes the required work is already scoped.
- The revision **counts as a submission**: if it is not accepted and you later
  resubmit, your change note describes deltas **relative to the revision**, not the
  original. The process has memory; treat every revision commitment as on-record.
- Leverage is highest here of any stage: the decision letter enumerates what must
  change. Build the revision as a checklist against that letter and nothing else —
  unsolicited rewrites add risk without credit.

## Response window mechanics

The 2027 windows are short and fixed (April cycle: July 6-9, 2026; September cycle:
December 1-4, 2026), and the CFP scopes rebuttals to correcting factual errors and
answering reviewers' questions, with ~800 words of expected reader attention.
Strategy and drafting live in `asplos-author-response`; the process fact to hold
here is that **no new experiments can be demanded of reviewers' attention** — the
rebuttal reallocates credit across existing evidence, nothing more.

## Confidentiality and conduct facts

- Reviewing is double-blind in both directions; do not attempt reviewer
  identification, and keep review content off public channels.
- Program leadership rotates per edition — precedent from a previous year's chairs
  binds nothing this year.
- Decisions are final within a cycle; the sanctioned second chance is the September
  gate or the revision channel, not appeal.

## Reading a review packet for structure, not sentiment

When reviews arrive, extract three structural facts before reacting to tone:

- **Expertise distribution** — which community each reviewer writes from
  (vocabulary and the lane of related work they cite give it away). A packet with
  no reviewer from one of your two coupled communities means that half of the
  paper was under-audited; expect the discussion to defer to whoever is closest.
- **Convergence** — three reviewers independently naming the same gap is an
  evidence problem; three naming different gaps is usually a framing problem,
  fixable in prose.
- **The champion test** — does any review advocate ("this changes how X should
  be built") rather than merely tolerate? Committee outcomes at selective
  venues track advocacy; a response strategy (`asplos-author-response`) should
  aim to arm the most positive reviewer with answers they can repeat.

## The pipeline on a calendar

For the live September gate: submission September 9, 2026 → rapid + full review
through the autumn → author response December 1-4 → notification December 21 →
Major Revision (if offered) due at the camera-ready deadline ~6 weeks later →
conference April 11-15, 2027 in Heraklion. The structural implication: between
September and December, author leverage is zero — the productive use of that
window is preparing response infrastructure (claim-to-evidence index, appendix
pointer list) so the four-day response window spends itself on drafting, not
archaeology.

## Between-cycles calibration

A September submission is reviewed by the same edition's committee as an April
one, but the pool's load and the pile's composition differ per cycle in ways
nobody publishes. Do not infer per-cycle acceptance odds from folklore, and do
not delay a ready paper to chase a rumored easier round — the CFP's own framing
of the two deadlines is "submit when the work is ready," and the only variable
you control is readiness.

## Output format

```text
[Stage now] rapid / full / response / decision / revision
[Rapid-survival estimate] intersection visible in pp.1-2: Y/N + weakest element
[Red-team findings] R1-R6 one line each
[If Major Revision] letter-item checklist drafted: Y/N · 6-week plan feasible: Y/N
[Leverage remaining] what can still be influenced at this stage
[Cycle facts to re-verify] <URLs from the source map>
```
