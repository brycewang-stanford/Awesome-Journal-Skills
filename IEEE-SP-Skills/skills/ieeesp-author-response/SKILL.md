---
name: ieeesp-author-response
description: Use when drafting the IEEE S&P (Oakland) rebuttal for second-round papers or the response plan for a Revise decision, including triaging reviews under the ~5-day window, answering adaptive-attack and threat-model objections, handling ethics questions with documentation, and writing against the Revise expectations summary.
---

# IEEE S&P Author Response

Use this in two situations that S&P runs differently from most venues: the
short **rebuttal** offered only to papers that survive the first round, and
the **Revise response**, a full re-submission against a written expectations
summary. The 2027 Cycle 2 rebuttal window was five days — reviews out
Feb 11, rebuttal due Feb 16, 2027 (checked 2026-07-08) — so the work is
mostly done before reviews arrive or it does not get done.

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
- New experimental results: follow the current cycle's instructions on
  whether new numbers are allowed (待核实 each cycle); when unclear, phrase
  as verification of existing claims rather than new contributions.
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
→ ≤ <current cycle's length cap 待核实>; every point ends at a §/Table/date.
```

## Responding to a Revise decision

The Revise summary of expectations is a **contract, not a suggestion list**:

1. Extract each expectation into a numbered ledger; get co-author agreement
   on the interpretation of each *before* doing work.
2. Deliver every item or explicitly negotiate the ones you contest — silence
   on an expectation reads as failure to meet it.
3. Write a change document mapping expectation → change → location, so the
   returning reviewers can verify in minutes.
4. Do not add major unrequested material; new claims reopen review scope.
5. Confirm on the live cycle pages which cycle receives the revision and its
   deadline (待核实 — the 2027 mechanics were not published at check time).

## Failure modes seen at this venue

- Spending the five days on the novelty dispute instead of the fixable
  evidence objections.
- Answering an ethics question with philosophy instead of a timeline.
- Treating Revise as "minor revisions plus a cover letter" — it is re-reviewed
  as a major revision against the written expectations.
- Missing that the rebuttal's real audience is the reviewer **discussion**
  that follows it: write lines a sympathetic reviewer can quote.

## Output format

```text
[Mode] rebuttal (5-day) / revise response
[Ledger] <n> objections: misreading <n> · evidence <n> · taste <n> · ethics <n>
[Concessions] <what is honestly out of evaluated scope>
[Documentation block] disclosure dates ✓/✗ · IRB id ✓/✗ · artifact refs ✓/✗
[Word budget plan] <allocation across reviewers>
[Open 待核实] new-results policy / length cap / revise target cycle
```
