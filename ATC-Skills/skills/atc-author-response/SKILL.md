---
name: atc-author-response
description: Use when writing the ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) rebuttal and the shepherd's description-of-changes — the short round-two response that corrects factual misreadings and supplies requested measurements, and the point-by-point revision record a conditional-acceptance shepherd checks before final acceptance.
---

# ATC Author Response

ATC gives you two distinct writing moments after review, and they have different jobs. The
**rebuttal** (a short, roughly one-page window during round two) is for correcting misreadings and
supplying a measurement a reviewer said was missing. The **description of changes** (after a
**conditional accept**, for the **shepherd**) is a point-by-point record proving every required
revision was made. Confusing the two — arguing in the shepherd round, or over-promising in the
rebuttal — is the classic failure.

## The rebuttal (round two, ~1 page)

Its job is narrow and its space is tiny, so triage ruthlessly:

- **Correct factual misreadings** first — a reviewer who misread the testbed, the baseline, or the
  claim can be moved by a precise correction with a pointer to the section/figure.
- **Supply the one number that matters** — if a reviewer said "no tail latency" or "no matched-cost
  comparison," and you have or can add it, state the result concisely. Systems reviewers move on
  evidence, not on rhetoric.
- **Concede cleanly** what you cannot fix this cycle — a crisp "correct; here is the honest bound"
  buys more credibility than defending an overclaim.
- **Do not argue taste** — "the reviewer underrates the contribution" changes nothing; the PC
  discussion decides.

Structure it as **reviewer/point → response**, lead with the highest-impact corrections, and never
introduce unsupported new claims (which read as scope creep). Keep double-blind: the rebuttal must
not reveal identity.

## The description of changes (shepherd round)

After a conditional accept, a PC member **shepherds** the paper: final acceptance depends on the
required revisions landing. Write the change record as a contract:

- **One row per required change:** reviewer/shepherd request → what you changed → where (section,
  figure, table) → the resulting text or result.
- **Make or explicitly decline** every requested change. A **silently skipped** required change is
  the fastest way to stall a conditional accept; if you decline, give the reason and the evidence.
- **Point to concrete artifacts of the change** — the new figure, the added experiment, the revised
  paragraph — not a promise to do it.
- **Keep the shepherd's scope.** The shepherd enforces the required revisions, not a new round of
  wishes; do not reopen settled scope or add unrequested claims that invite fresh review.

## Mapping requests to moves

| Reviewer request | Strong response |
|---|---|
| "Baseline is weak / unmatched" | Add the well-configured baseline at a matched operating point; report the new comparison |
| "No tail latency / variance" | Add p99/p999 and multi-run variance; point to the updated figure |
| "Unclear how it's built / scales" | Add implementation detail or a scaling experiment; cite the new section |
| "Costs not reported" | Quantify the trade beside the gain at matched cost |
| "Reproducibility unclear" | Point to the anonymized artifact and the claim-to-experiment map |
| A misreading | Correct precisely with a section/figure pointer; do not over-explain |

## What moves an outcome vs. what does not

```text
[Moves it]     a factual correction; a requested measurement supplied; a clean concession + bound
[Doesn't]      arguing the reviewer's taste; re-asserting the abstract; vague "we will consider"
[Backfires]    unsupported new claims; scope creep; defensiveness; an anonymity leak
```

## Reverify each cycle

- Whether a formal rebuttal window exists and its length (about one page is the reported norm —
  confirm on the call).
- The shepherding requirements and the change-record format for the current edition.
- The camera-ready deadline relative to the shepherd sign-off (see `atc-camera-ready`).

## Output format

```text
[Response type] round-two rebuttal / shepherd description-of-changes
[Triage] highest-impact corrections and requested measurements listed first
[Per point] request -> response -> evidence/location; every required change made or declined-with-reason
[Anonymity] no identity leak in the response? yes/no
[Forbidden] unsupported new claims / taste arguments / silently skipped required changes: absent?
```
