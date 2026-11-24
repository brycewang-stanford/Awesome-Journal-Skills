---
name: ieeesp-author-response
description: Use when drafting the IEEE S&P (Oakland) rebuttal for second-round papers — the 750-word non-interactive rebuttal or the interactive rebuttal with requested results and a revised PDF — including triaging reviews under the ~5-day window, answering adaptive-attack and threat-model objections, handling ethics questions with documentation, and the optional response to an accepted paper's public meta-review.
---

# IEEE S&P Author Response

Use this for the **rebuttal** S&P offers only to papers that survive the
first round. The PC assigns each paper one of two modes (2027 CFP,
re-verified 2026-11-24): a **non-interactive rebuttal** of 750 words limited
to factual errors and reviewers' concrete questions, with no new results; or
an **interactive rebuttal** — the same 750-word text, then a HotCRP comment
with new results or material the reviewers explicitly requested, plus a
revised manuscript PDF. There is no later revision round. The 2027 Cycle 2
text window was five days — reviews out Feb 11, rebuttal due Feb 16, 2027,
interactive period Feb 17-26 — so the work is mostly done before reviews
arrive or it does not get done.

## Pre-draft before reviews land

Between the early-reject notice and review release, write the skeleton:

- The three objections your own red-team read would raise (usually: an
  adaptive-attacker gap, a threat-model realism question, a
  measurement-validity question).
- The exact section/figure references answering each.
- The ethics documentation block: disclosure dates, vendor responses,
  IRB determination ID — assembled, dated, ready to paste.

## Triage the review set in the first hour

| Objection type | Response strategy | Win probability |
|---|---|---|
| Misreading of mechanism or threat model | Quote the submission, cite section, restate in two lines | High |
| Missing experiment you actually have | Point to appendix/artifact location | High |
| Adaptive-attack gap that is real | Concede scope precisely; state what the evaluated adversary covers | Medium — honesty is scored |
| Threat-model taste ("attacker unrealistic") | Ground in incidents/measurements, not adjectives | Medium |
| Ethics record question | Dates, IDs, named approvals — documentation only | Binary: docs exist or not |
| Fundamental novelty dispute | One paragraph on the delta; do not relitigate | Low — spend words elsewhere |

Spend the budget in proportion to win probability times decision weight, and
answer **every reviewer at least once** — an ignored reviewer in the
post-rebuttal discussion is a vote you conceded.

## Rules of engagement in the rebuttal

- Answer the objection actually written, not the friendlier one nearby.
- New experimental results: **none** in a non-interactive rebuttal; in an
  interactive one, only what reviewers explicitly requested, delivered in the
  follow-up comment with a revised PDF. Over-length text or unrequested new
  material means immediate rejection.
- Never argue that a security concern "is out of scope" without saying whose
  scope — restate the threat model's boundary and why it is the right one.
- Keep the anonymous voice; disclosure specifics stay venue-neutral.
- No links out of HotCRP unless the CFP explicitly permits them.

## Rebuttal skeleton

```text
Common response (all reviewers):
  C1. Threat model boundary: <2 lines + §ref>
  C2. Adaptive-adversary coverage: <what was evaluated, §ref>
  C3. Ethics record: disclosed <date>, IRB <id/waiver>, data handling <§ref>

Reviewer A:
  A1 [misreading] The attack does not require <X>; see §3.2 ¶2.
  A2 [evidence]  The <n>-target evaluation is in Table 4; per-target
      breakdown in Appendix C.
Reviewer B:
  B1 [concession] Correct: we do not evaluate <adversary class>. Our claims
      are scoped to <boundary> (§2); extending is future work.
→ ≤ 750 words; every point ends at a §/Table/date.
```

## Working an interactive rebuttal

The reviewers' explicit requests are a **contract, not a suggestion list**,
and the window is about a week (Feb 17-26, 2027 for Cycle 2):

1. Extract each explicit request into a numbered ledger; get co-author
   agreement on the interpretation of each *before* doing work.
2. Deliver every requested item or say plainly, in the 750-word text, which
   you cannot and why — silence on a request reads as failure to meet it.
3. Post the follow-up HotCRP comment mapping request → result → location in
   the revised PDF, so reviewers can verify in minutes.
4. Add nothing unrequested; the CFP treats that as grounds for immediate
   rejection.

## After acceptance: the public meta-review

Accepted papers publish a meta-review (< 500 words) listing the PC's reasons
and concerns; authors may add a response (< 500 words) that is published with
it. Write it as a factual record of what the camera-ready changed, not a
second rebuttal (`ieeesp-camera-ready`).

## Failure modes seen at this venue

- Spending the five days on the novelty dispute instead of the fixable
  evidence objections.
- Answering an ethics question with philosophy instead of a timeline.
- Using an interactive rebuttal to add a favourite unrequested experiment —
  it is grounds for immediate rejection.
- Missing that the rebuttal's real audience is the reviewer **discussion**
  that follows it: write lines a sympathetic reviewer can quote.

## Output format

```text
[Mode] non-interactive rebuttal (750 words) / interactive rebuttal (+ requested results, revised PDF) / meta-review response
[Ledger] <n> objections: misreading <n> · evidence <n> · taste <n> · ethics <n>
[Concessions] <what is honestly out of evaluated scope>
[Documentation block] disclosure dates ✓/✗ · IRB id ✓/✗ · artifact refs ✓/✗
[Word budget plan] <allocation across reviewers>
[Requested items] <n> explicit reviewer requests · delivered <n>
```
