---
name: ieeesp-review-process
description: Use when reasoning about IEEE S&P (Oakland) peer review, including the rounds inside each cycle, early-reject notices, the rebuttal for second-round papers, the Accept/Revise/Reject decision set, the Research Ethics Committee, shepherding of accepted papers, and the one-year resubmission embargo.
---

# IEEE S&P Review Process

Use this to model what happens to an S&P submission after upload and where
author effort still moves the outcome. The structural constant across recent
cycles is a **round structure inside each cycle** ending in a three-way
decision; the dates below are the verified Cycle 2 timetable for S&P 2027
(sp2027.ieee-security.org/cfpapers.html, checked 2026-07-08).

## Rounds inside a cycle

| Stage | 2027 Cycle 2 date | What actually happens |
|---|---|---|
| Submission closes | Nov 17, 2026 | Record frozen; REC screening begins where flagged |
| First round | — | A subset of the PC reads; weakest papers cut |
| Early-reject notice | Jan 18, 2027 | Cut papers exit **without rebuttal** |
| Reviews released | Feb 11, 2027 | Surviving papers see full reviews |
| Rebuttal due | Feb 16, 2027 | ~5 days; second-round papers only |
| Decision | Mar 5, 2027 | Accept / Revise / Reject |

The asymmetry to plan around: **first-round papers never get to answer their
reviewers.** The introduction, threat model, and evaluation summary must
survive a skeptical first read on their own — that is why `ieeesp-writing-style`
front-loads the adversary and the evidence map.

## The three-way decision, and why Revise is the signature

- **Accept** comes with a draft meta-review listing remaining concerns and a
  **shepherd** who strikes each concern once the camera-ready resolves it —
  acceptance at S&P is conditional in substance even when not in name.
- **Revise** invites a limited set of papers to submit a structured major
  revision against a written summary of expectations, re-reviewed (ideally by
  the same reviewers). It is the venue's mechanism for "the contribution is
  real, the evidence is not finished." Which later cycle a Revise resubmits
  into is cycle-specific — 待核实 on the live pages every time.
- **Reject** starts the one-year embargo from the original submission date;
  a future submission with roughly ≥40% overlap counts as a resubmission.

Treat a Revise as the best non-accept outcome in security publishing: the
expectations document is a contract. Deliver exactly what it lists, map each
expectation to a change, and do not use the revision to add unrequested new
material that reopens settled questions.

## The Research Ethics Committee is a separate track

S&P registers an **Ethics Considerations** entry for every paper at
submission time, and papers raising concerns are routed to a Research Ethics
Committee that can recommend rejection on ethical grounds regardless of
technical merit. The named baseline is the **Menlo Report**. Reviewers also
expect IRB approval/waiver status disclosed where human subjects or user data
are involved, and harm-mitigation discussion whenever PII is touched. The REC
evaluates what you *did* — disclosure sent, data minimized, approvals
obtained — months before submission; nothing written during review can
substitute for actions not taken.

## Where author leverage lives

```text
Leverage map (S&P cycle):
  Before registration   ████████ abstract routes reviewers; ethics record set
  First round           ─ none: paper speaks alone; no rebuttal if cut
  Rebuttal window       ████ high on misreadings, moderate on evidence gaps
                             (5 days: pre-draft the likely objections)
  Reviewer discussion   ─ only via the rebuttal already filed
  Revise window         ██████ a written contract you can fully satisfy
  Camera-ready          ███ shepherd negotiation over concrete concerns
```

## Reading reviews from this PC

The S&P pool reads adversarially by profession. Expect objections shaped as:
"the adaptive attacker breaks this defense," "the threat model assumes
capabilities that make the attack uninteresting," "the measurement sample is
biased toward <population>," "the ethics section does not say who approved
this." Classify each review point by whether it disputes the **claim**, the
**evidence**, or the **ethics record** — the three need different responses
(`ieeesp-author-response`).

## Process misfires

- A review that misstates the paper's mechanism is rebuttal material: quote
  the submission with section numbers, without heat.
- Ethics allegations are answered with documentation (dates, approval IDs,
  disclosure timelines), never with indignation.
- Suspected reviewer misconduct goes privately to the PC chairs.
- After a final Reject there is no appeal track; the embargo clock and a
  sibling venue are the real options.

## Output format

```text
[Stage] pre-submission / round 1 / rebuttal / decision wait / revise / shepherding
[Next transition] <date from current cycle pages> (待核实 if unverified)
[Survival read] early-reject risk: low / med / high (why)
[Objection forecast] claim: <..> · evidence: <..> · ethics: <..>
[If Revise] expectations doc summarized? resubmission cycle confirmed?
```
