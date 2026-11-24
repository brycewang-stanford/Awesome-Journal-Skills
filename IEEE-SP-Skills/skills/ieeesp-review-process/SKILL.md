---
name: ieeesp-review-process
description: Use when reasoning about IEEE S&P (Oakland) peer review, including the rounds inside each cycle, early-reject notices, the non-interactive or interactive rebuttal for second-round papers, the Accept/Reject decision set, the Research Ethics Committee, public meta-reviews and shepherding of accepted papers, and the one-year resubmission embargo.
---

# IEEE S&P Review Process

Use this to model what happens to an S&P submission after upload and where
author effort still moves the outcome. The structural constant across recent
cycles is a **round structure inside each cycle** ending in an Accept or
Reject decision; the dates below are the verified Cycle 2 timetable for
S&P 2027 (sp2027.ieee-security.org/cfpapers.html, re-verified 2026-11-24; the
CFP warns Cycle 2 dates may shift if submissions exceed plan).

## Rounds inside a cycle

| Stage | 2027 Cycle 2 date | What actually happens |
|---|---|---|
| Submission closes | Nov 17, 2026 | Record frozen; REC screening begins where flagged |
| First round | — | A subset of the PC reads; weakest papers cut |
| Early-reject notice | Jan 18, 2027 | Cut papers exit **without rebuttal** |
| Reviews released | Feb 11, 2027 | Surviving papers see full reviews |
| Rebuttal due | Feb 16, 2027 | 750 words; second-round papers only |
| Interactive period | Feb 17-26, 2027 | Only papers assigned an interactive rebuttal: requested results + revised PDF |
| Decision | Mar 5, 2027 | Accept / Reject |
| Shepherd submission | Mar 26, 2027 | Accepted papers address meta-review concerns |
| Camera-ready | Apr 8, 2027 | Final PDF with ethics section and meta-review |

The asymmetry to plan around: **first-round papers never get to answer their
reviewers.** The introduction, threat model, and evaluation summary must
survive a skeptical first read on their own — that is why `ieeesp-writing-style`
front-loads the adversary and the evidence map.

## Two outcomes, and where the "revision" now lives

- **Accept** comes with a draft **public meta-review** (< 500 words: why the
  PC accepted, and its remaining concerns) and a **shepherd** who strikes each
  concern once the camera-ready resolves it. Authors may publish a response of
  < 500 words alongside it.
- **Reject** starts the one-year embargo from the original submission date;
  a paper from the same or similar authors with a very similar intellectual
  contribution counts as a resubmission, however rewritten.
- There is **no Revise / major-revision outcome and no conditional
  acceptance** in the 2026 or 2027 CFPs. Papers are judged on the submitted
  version plus whatever reviewers explicitly requested during an
  **interactive rebuttal** — the one place to show new results, together
  with a revised manuscript PDF, because there is no later revision round.

Treat an interactive-rebuttal assignment as the venue's only second chance:
deliver exactly the requested material, in a revised PDF, inside the window,
and add nothing unrequested — unrequested new material means immediate
rejection.

## The Research Ethics Committee is a separate track

S&P registers an **Ethics Considerations** entry for every paper at
registration time ("None" plus reasoning if none; the section itself is added
at camera-ready, outside the page limit), and papers raising concerns are
routed to a Research Ethics
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
                             (750 words, ~5 days: pre-draft the objections)
  Interactive period    ██████ only if assigned: requested results + revised PDF
  Reviewer discussion   ─ only via the rebuttal already filed
  Camera-ready          ███ shepherd negotiation over meta-review concerns
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
[Stage] pre-submission / round 1 / rebuttal / interactive period / decision wait / shepherding
[Next transition] <date from current cycle pages> (待核实 if unverified)
[Survival read] early-reject risk: low / med / high (why)
[Objection forecast] claim: <..> · evidence: <..> · ethics: <..>
[Rebuttal mode] non-interactive / interactive (requested items listed?)
```
