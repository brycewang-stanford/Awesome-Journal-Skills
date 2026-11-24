---
name: atc-author-response
description: Use when writing the ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) 72-hour author response, the resubmission change summary, or the shepherd's description-of-changes — the response that may only correct factual errors and answer reviewer questions (no new data or promises), the one-page summary of improvements for a previously rejected paper, and the point-by-point revision record a conditional-acceptance shepherd checks before final acceptance.
---

# ATC Author Response

ATC 2027 (call re-verified 2026-11-24) gives you three distinct writing moments, each with its own
job:

1. the **resubmission change summary** (at submission, for a paper rejected before — about one page,
   anonymized, shown to reviewers only after they finish their reviews);
2. the **author response** (a **72-hour** window, **3-5 April 2027**, open to every submission); and
3. the **description of changes** (after a **conditional accept**, for the **shepherd**).

Confusing them — adding results in the response, arguing in the shepherd round, or skipping the
change summary — is the classic failure.

## The author response (72 hours, 3-5 April 2027)

The call limits the response to **(a) correcting factual errors in the reviews** or **(b) directly
answering questions reviewers asked**. It **must not** include new experiments or data, describe
work completed since submission, or promise future work — and, because the PC need not read
supplementary material, it must not rely on that material either. Triage ruthlessly:

- **Correct factual misreadings** first — a reviewer who misread the testbed, the baseline, or the
  claim can be moved by a precise correction with a pointer to the section or figure.
- **Answer the questions actually asked**, from evidence already in the submitted paper: "Figure 7
  reports p99 at matched cost; the baseline is configured as in §5.1."
- **Concede cleanly** what the paper does not show — a crisp "correct; the paper's claim is bounded
  to X" buys more credibility than defending an overclaim.
- **Do not argue taste** — "the reviewer underrates the contribution" changes nothing.

Structure it as **reviewer/point → response**, lead with the highest-impact corrections, and keep
double-blind. Draft the likely answers before 3 April; 72 hours is editing time, not writing time.

## The resubmission change summary (at submission)

For a paper previously rejected elsewhere (or at ATC), upload via the form the prior-submission
information and a summary of the revisions — **about one page**, properly anonymized. Reviewers see
it after writing their reviews, so it helps a reviewer who saw the earlier draft credit the
improvements. List each major prior criticism → what changed → where.

## The description of changes (shepherd round)

After a conditional accept (notification **27 April 2027**), a PC member **shepherds** the paper:
final acceptance depends on the required revisions landing before the **28 May 2027** camera-ready.
Write the change record as a contract:

- **One row per required change:** reviewer/shepherd request → what you changed → where (section,
  figure, table) → the resulting text or result.
- **Make or explicitly decline** every requested change. A **silently skipped** required change is
  the fastest way to stall a conditional accept; if you decline, give the reason and the evidence.
- **Point to concrete artifacts of the change** — the new figure, the added experiment, the revised
  paragraph — not a promise to do it. (New measurements are allowed here, unlike in the response.)
- **Keep the shepherd's scope.** Do not reopen settled scope or add unrequested claims.

## Mapping requests to moves

| Reviewer request | In the 72-hour response | In the shepherd round |
|---|---|---|
| "Baseline is weak / unmatched" | Point to the configuration and operating point already reported | Add the well-configured baseline at a matched operating point |
| "No tail latency / variance" | Point to existing tail/variance data, or concede the bound | Add p99/p999 and multi-run variance |
| "Unclear how it's built / scales" | Clarify from the paper's own sections | Add implementation detail or a scaling experiment |
| "Costs not reported" | Point to where cost appears, or concede | Quantify the trade beside the gain at matched cost |
| A misreading | Correct precisely with a section/figure pointer | — |

## What moves an outcome vs. what does not

```text
[Moves it]     a factual correction; a direct answer from the submitted evidence; a clean concession
[Doesn't]      arguing the reviewer's taste; re-asserting the abstract; vague "we will consider"
[Backfires]    new data or promises in the response; scope creep; defensiveness; an anonymity leak
```

## Reverify each cycle

- The response window and its rules (72 hours, facts and questions only, in 2027).
- The resubmission-summary rule and its length guidance.
- The shepherding requirements and the camera-ready date (see `atc-camera-ready`).

## Output format

```text
[Response type] resubmission change summary / 72-hour author response / shepherd description-of-changes
[Triage] highest-impact corrections and direct answers listed first
[Per point] request -> response -> evidence/location; every required change made or declined-with-reason
[Rule check] response contains no new data, no promises, no reliance on supplementary material? yes/no
[Anonymity] no identity leak? yes/no
```
