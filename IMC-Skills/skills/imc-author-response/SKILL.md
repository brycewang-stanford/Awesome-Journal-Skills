---
name: imc-author-response
description: Use when drafting ACM IMC author responses, covering the initial-review rebuttal and — distinctively — the One-Shot-Revision resubmission that must address a bounded set of action points, keep double-blind anonymity, satisfy the reviewer champion, and be re-judged by the same reviewers at the next deadline.
---

# IMC Author Response

Use this after IMC reviews are released. IMC has **two distinct speaking turns**, and conflating
them is a common mistake: a short initial rebuttal, and — if you receive a **One-Shot-Revision** —
a revised paper plus a change summary that the *same* reviewers re-read at the *next* deadline
against a *bounded* set of action points. Both must respect double-blind anonymity: no author,
institution, testbed, or vantage-point identity may leak.

## Triage (both turns)

- Answer what affects the decision: significance of the finding, vantage-point representativeness,
  ground truth, methodology soundness, confounds/limitations, **ethics**, and artifact
  availability.
- Use evidence that already exists or that the revision will concretely add — never a vague
  promise.
- Correct factual misreadings first; a reviewer who misread your coverage or your ethics handling
  is often persuadable.
- Keep every word anonymous. Do not name your tool, institution, AS, probe account, or a private
  dataset URL, even to strengthen a point.

## Turn 1 — the initial rebuttal

Short and decision-focused. One decision-critical point per reviewer beats an exhaustive reply.
Concede what is true, correct what is misread, and point to exactly where the answer lives in the
submitted paper or appendix. For measurement papers the highest-value clarifications are usually:
**why the vantage points are representative enough**, **why a snapshot generalizes (or how long
the window was)**, and **why the active measurement was safe**. Do not paste large new results the
reviewers cannot verify.

## Turn 2 — the One-Shot-Revision (the distinctive IMC move)

A One-Shot-Revision is a **bounded contract**: the reviewers (with at least one champion) named a
small number of action points — up to a few concrete additions/changes — and the resubmission is
judged narrowly on whether each was done. Structure a change summary as an explicit ledger:

```text
[A1] Action point (quoted briefly): "add a mobile-carrier vantage point"
     -> DONE  | added 8 carrier vantage points across 3 regions; §4.2, Table 3; dataset v2
[A2] Action point: "address the diurnal confound"
     -> DONE  | added a time-of-day controlled analysis; Fig. 5; the effect persists
[A3] Action point: "clarify the probing safety review"
     -> DONE  | expanded the Ethics appendix with the opt-out and rate-limit design (§A.1)
```

The rules that turn a One-Shot-Revision into an acceptance:

- **Do exactly the named action points** — all of them, visibly. A silent omission or a
  "we disagree" without a documented alternative is what the second read punishes.
- **Do not scope-creep.** Reopening the whole paper or adding unrequested claims signals you
  misread the bounded contract and risks the champion's support.
- **Keep the champion's confidence.** The revision succeeds by delivering the specific things the
  advocate needs to defend it in discussion.

## Reviewer pushback patterns

| Pushback | What it signals | IMC-ready response |
|---|---|---|
| "Vantage points are not representative" | External-validity doubt | Add vantage points or quantify and bound the coverage gap; state residual limits |
| "This could be a snapshot artifact" | Temporal-validity doubt | Add a longitudinal slice or show stability across your window |
| "No ground truth for the labels" | Construct-validity doubt | Add a validated subsample or a second data source; bound the error |
| "The active measurement may cause harm" | Ethics objection | Document safety design, opt-out, rate limits, disclosure; expand the Ethics section |
| "The artifact is unavailable/undocumented" | Availability gap | Fix and re-anonymize the dataset/tool; correct the declaration |

## Anonymity in the response (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe new vantage points and datasets without linking an identity-revealing account, testbed,
  or repository.
- Do not thank a named operator, provider, or funder inside the response.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- Length and format norms for both turns vary by cycle; confirm the current instructions.
- The PC discussion decides; write for the champion, and make the revised paper — not the summary —
  carry the evidence.

## Output format

```text
[Turn] initial rebuttal / one-shot-revision resubmission
[Priority issue] <reviewer concern>
[Decision dimension] significance / vantage points / ground truth / method / ethics / availability
[Action ledger] <action point -> DONE + where in paper/dataset> (One-Shot-Revision)
[Scope check] <no unrequested scope creep: passed/issues>
[Anonymity check] <no identity/infrastructure leak: passed/issues>
```
