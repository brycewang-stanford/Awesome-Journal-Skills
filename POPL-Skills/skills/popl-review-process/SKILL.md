---
name: popl-review-process
description: Use when interpreting where a POPL submission stands — the full double-blind pipeline from the July HotCRP deadline through reviews, the optional author response, October conditional-acceptance decisions, the mandatory revision gate, Distinguished Paper selection, and publication as PACMPL Issue POPL in January.
---

# POPL Review Process

POPL's pipeline is a conference cycle that ends in a journal issue. The shape below
is the POPL 2027 process as posted (read 2026-07-08 via search renderings; author
response window and revision deadline were not fully rendered — 待核实).

## Pipeline

| Stage | POPL 2027 anchor | What is actually being decided |
|---|---|---|
| Submission | July 9, 2026 AoE, `popl27.hotcrp.com`, no abstract deadline | Format compliance (summary rejection is real) and reviewer assignment |
| Reviewing | full double-blind, as in POPL 2023-2026 | Correctness plausibility, novelty of the formal idea, significance to PL principles |
| Author response | optional, multi-day, concise | Whether standing objections survive your best factual answer |
| Decision | notification October 5, 2026 | Reject vs **conditional acceptance** — no unconditional accept exists |
| Revision gate | deadline set by the committee (待核实 for 2027) | Whether the revision satisfies the committee's stated conditions; failure risks rejection |
| Publication | PACMPL Issue POPL (Vol 10 = 2026, published Jan 8, 2026) | Journal article, presented at the January symposium (2027: Mexico City, Jan 10-16) |

## How a POPL committee reads

- The first question is *what is the formal contribution* — a semantics, a type
  system, a logic, a proof technique — and whether it is stated precisely enough to
  be wrong. Papers that never risk a sharp claim are marked "unclear contribution."
- Correctness is probed by attempted counterexample. Expect at least one reviewer to
  push on the strangest corner of your calculus: open terms, empty contexts,
  non-termination, the interaction of two features you analyzed separately.
- Significance at POPL means the idea travels: another researcher can apply your
  logical relation, your translation, your proof method to *their* language.
  A theorem locked to one artifact language travels poorly.
- Full double-blind changes the sociology: nobody is extending credit to a famous
  group's proof style. Identities unblind only after conditional-acceptance
  decisions, and only for the papers that crossed.

## Reading the decision

Conditional acceptance arrives with explicit conditions — typically clarifications,
scoping of overclaims, or presentation surgery. Treat the condition list as a
contract: the Review Committee re-checks each item, and the call states the revision
must be satisfactory "or risk rejection." Rejection reviews, in turn, sort into
fix-and-resubmit (misread contribution, presentation collapse) versus fundamental
(the theorem is true but nobody at this venue needs it) — `popl-topic-selection`
handles the second kind.

Distinguished Papers are capped at 10% of acceptances, chosen by the committee for
relevance, originality, significance, and clarity (POPL 2026 call wording); at least
one 2026 award is publicly attested. It is not something authors apply for.

## Output format

```text
[Stage] pre-submission / under review / response window / awaiting decision / revision gate / production
[Next event] <date + source URL, or 待核实>
[Live risks] <correctness doubt / significance doubt / condition list items>
[Recommended posture] <what to prepare now for the next stage>
```
