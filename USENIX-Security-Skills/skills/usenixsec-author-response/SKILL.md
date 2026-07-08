---
name: usenixsec-author-response
description: Use when reviews arrive from a USENIX Security Symposium cycle and the authors must respond — writing the rebuttal that survives online PC discussion, handling required ethics-content revisions flagged mid-review, and working with a shepherd after an "Accepted on Shepherd Approval" decision.
---

# USENIX Security Author Response

USENIX Security gives authors two distinct speaking moments, and they obey different
rules: the mid-review response to reviewers, and the post-decision exchange with a
shepherd. This skill covers both. Mechanics shift per cycle — the '25 model was
documented in detail on the reviewing-model page, the '26 model partially, and the
'27 mechanics are 待核实 — so confirm the current instructions in HotCRP before
drafting.

## Where the response sits in the pipeline

In the '25 model (the last fully documented one): two reviews in round one; papers
survive to round two if at least one reviewer sees a path to acceptance after online
discussion; round two adds two more reviews; **then** authors respond; reviewers
discuss again and decide. Two consequences follow:

- By the time you respond, four reviewers have read the paper but the committee has
  not settled. The response's real audience is the discussion that follows it.
- Papers cut at the early-reject notification never get a response window at all.
  There is no appeal lane inside the cycle; the recovery move is a revised
  resubmission (see `usenixsec-review-process` for the restriction rules).

One more '25-documented pattern worth planning for: submissions with inadequate
ethics discussions were flagged during review, and authors were **required** to
supply revised ethics content in the response phase. Treat an ethics question in a
review as a compliance demand, not an opinion to debate.

## Sorting the reviews before writing

| Objection type | What it usually means at this venue | Response move |
|---|---|---|
| Threat model unrealistic | Reviewer rejects the attacker capabilities | Defend with deployment evidence, or narrow the claim explicitly |
| Ethics gap / disclosure question | Compliance flag, possibly chair-visible | Answer completely; state disclosure timeline and vendor contact status |
| Evaluation missing an adaptive attacker | Defense papers' most common kill | Present the adaptive experiment if it exists; commit precisely if it fits shepherding scope |
| Overlap with concurrent work | Cycle collision, common with two cycles/year | Date the overlap, differentiate mechanism and evidence |
| "Measurement may be artifact of vantage point" | Methodology doubt | Show cross-vantage or cross-time consistency numbers |

Answer the compliance-shaped items first and fully; a brilliant technical rebuttal
does not offset an unanswered disclosure question.

## Drafting rules that fit this venue

- Number every point and quote the review fragment being answered; the discussion
  phase skims, and unanchored prose gets skipped.
- Give evidence that already exists (a table row, an appendix reference, a number)
  priority over promises. Since '26 the largest change a paper can absorb after
  decision is a **two-week shepherding pass** — never promise revisions bigger than
  that window can hold.
- Keep anonymity discipline: no identifying links, no "in our lab" phrasing.
- If a reviewer misread, demonstrate the misreading with a page/section pointer and
  move on without scoring the point.

```text
# Response skeleton (per review point)
[R2.3] "the scanner may overload targets"
  Facts: Section 5.2 caps probe rate at 1 req/s/host; opt-out honored within 24h
         (Appendix: Ethical Considerations, para 2).
  Change offered: none needed — pointer only.

[R1.4] "no adaptive attacker"
  Facts: new experiment, gradient-aware evader, detection drops 94%→81% (table below).
  Change offered: add as Sec 6.4 (~0.5 page); fits shepherding scope.
```

## After the decision: shepherd mode

"Accepted on Shepherd Approval" (the '26 outcome replacing major revisions) means
the committee wants the paper but conditions publication on named changes —
clarifications, limitation discussions, toned-down claims — that are unlikely to
change enthusiasm. Working rules:

1. Convert the decision letter into a change matrix (request → edit → location) and
   send it to the shepherd before editing, so scope is agreed once.
2. Deliver inside the two-week window; the shepherd's sign-off is the acceptance.
3. Do not smuggle in new results the committee never reviewed; flag anything beyond
   the requested list explicitly and let the shepherd rule on it.
4. Track every edit against the camera-ready deadline for your cycle — shepherding
   and final-paper preparation overlap (see `usenixsec-camera-ready`).

## Reverify each cycle

- Whether the current cycle includes an author response phase at all, its length,
  and its format (HotCRP field vs PDF) — '27 values 待核实.
- The shepherding window length and whether "Accepted on Shepherd Approval" remains
  the intermediate outcome.
- Any word/character limit on responses.

## Output format

```text
[Phase] mid-review response / shepherd exchange
[Compliance items] ethics or disclosure questions + answers drafted: yes/no
[Point map] review point → evidence → offered change (within shepherding scope?)
[Risk] points conceded or narrowed, and the wording
[Next deadline] response or shepherd deadline, camera-ready implications
```
