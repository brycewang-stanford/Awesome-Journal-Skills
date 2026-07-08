---
name: sigmod-review-process
description: Use when reasoning about how a SIGMOD research paper moves through a PACMMOD round, covering double-anonymous CMT reviewing, the author feedback phase, accept/reject/revision verdicts, the one-month revision window, the 12-month rejection embargo, and how database PC members actually weigh evidence.
---

# SIGMOD Review Process

A SIGMOD research submission enters a journal pipeline with a conference
cadence: papers submitted to a PACMMOD round are reviewed double-anonymously
through Microsoft CMT, authors get a mid-round feedback window, and the first
verdict is three-valued — accept, reject, or revise. Understanding which
lever moves which outcome is most of review-stage strategy. Mechanics shift
by cycle; reconfirm against the live CFP before relying on any date.

## Anatomy of a round (SIGMOD 2027 Round 3 as the concrete case)

```text
Jul 10, 2026   Abstract + conflict declarations close
Jul 17, 2026   Paper deadline (11:59 PM AoE)
Sep 10-17      Author feedback phase: reviews visible, short reply window
Oct 19, 2026   Verdict: accept / reject / major or minor revision
Nov 19, 2026   Revised paper + 4-page letter due (revision cases)
Dec 12, 2026   Final accept/reject on revisions
```

Roughly three months from PDF to first verdict, five to final — faster than
most journals, slower than a rebuttal-only conference, and repeatable four
times a year.

## The three verdicts, decoded

| Verdict | What it means operationally | Author's real decision |
|---|---|---|
| Accept | Into the round's PACMMOD issue; camera-ready port begins | None — execute |
| Revision (minor/major) | A contract: enumerated requirements, +1 page, one month | Can every requirement land in 30 days? |
| Reject | 12-month embargo from SIGMOD research track (≈3 rounds) | PVLDB / ICDE / rework, not a quick resubmit |

Two consequences deserve emphasis. First, a revision verdict is genuinely
winnable — the requirements are written down, and reviewers judge compliance
rather than re-litigating taste. Second, the embargo makes "just resubmit
next round" impossible, so a rejected SIGMOD paper's next stop is usually a
different venue (see `sigmod-topic-selection`).

## Who is reading

The PC is dominated by database systems researchers and industrial engine
builders. Predictable evaluation reflexes:

- They benchmark mentally: the first skim looks for the workload table and
  the hardware paragraph before the design section gets full attention.
- They know the baselines personally — sometimes literally, as authors or
  maintainers — so an untuned competitor is recognized on sight.
- Architecture claims are audited against systems they have built:
  "this cannot be lock-free as described" is a common decisive comment.
- Novelty is measured against both recent PACMMOD/PVLDB output and decades
  of systems history; rediscovering a 1990s technique under a new name is a
  classic kill.

## Feedback phase leverage

The mid-round window is short and asymmetric: reviewers have already scored,
and you are trying to change specific minds before the PC discussion. Highest
expected value, in order: correcting an outright factual misreading;
answering a direct question with a pointer to a specific table; resolving an
apparent contradiction between two of your own sections. Near-zero value:
arguing significance, promising future work, or thanking reviewers at length
inside a tight character budget.

## Reading a split panel

- One detailed negative review plus shallow positives → the verdict follows
  the detailed one; answer it line by line in the feedback phase.
- Universal "interesting but evaluation thin" → expect major revision;
  start the missing experiments before the verdict arrives.
- A correctness objection from a builder of a rival system → treat as the
  round's decisive issue even if other scores are high.
- Complaints about clarity of the problem statement → often masks a fit
  problem; consider whether the framing buried the data-management core.

## Round vocabulary, decoded

Terms that trip up newcomers to the PACMMOD model:

- **Round** — one of the year's submission batches; your paper lives its
  whole life inside a single round unless rejected.
- **Issue** — the PACMMOD journal number your round's acceptances publish
  in; citable independently of the conference.
- **Feedback phase** — the mid-round reply window; not a rebuttal in the
  score-flipping sense, and not the revision.
- **Revision** — a formal verdict with enumerated requirements, not an
  informal second chance; compliance is what gets re-reviewed.
- **Embargo** — the 12-month bar on returning to the research track after
  rejection or late withdrawal.
- **Shepherd** — when assigned, the PC member who verifies promised
  camera-ready changes; treat their notes as binding.

## Etiquette with teeth

Confidentiality and anonymity bind for the whole round: no tweeting the
submission, no updating a named preprint mid-round in a way that links to
the anonymous version, no contacting suspected reviewers. Violations here
are policy matters for chairs, not style points.

## After the final decision

Close the loop regardless of outcome. On acceptance, archive the full
review thread beside the paper — the shepherding and ARI stages quote it.
On rejection, hold a one-hour post-mortem within a week while memory is
fresh: classify each objection as fixable-evidence, fixable-writing, or
fit, and let that classification pick the next venue rather than pride or
sunk cost. Reviews from a SIGMOD round are unusually actionable input for
a PVLDB or ICDE resubmission precisely because the reviewer pools overlap.

## Output format

```text
[Round position] submitted / feedback window / awaiting verdict / revising
[Panel read] per-reviewer stance and the decisive reviewer
[Verdict forecast] accept / revision / reject, with the driving issue
[Feedback plan] top corrections worth the character budget
[Revision feasibility] 30-day workload if a revision lands
[Embargo contingency] next venue if rejected
```
