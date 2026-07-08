---
name: stoc-author-response
description: Use when planning author-side communication for a STOC (ACM Symposium on Theory of Computing) submission, where no standing rebuttal phase exists — covering pre-emptive writing that answers objections in advance, chair-mediated technical clarifications if the PC asks, and the FOCS resubmission letter after a rejection.
---

# STOC Author Response

Set expectations first: the STOC 2026 Call for Papers announced no author-response
or rebuttal round, and the decision timeline ran directly from the November 4,
2025 deadline to notification on or before February 1, 2026 (checked 2026-07-08).
Historically STOC decisions arrive without authors ever seeing the reviews before
the outcome. Whether any given cycle adds a feedback experiment is a per-year
choice: 待核实 against the live CFP and PC-chair announcements each fall. This
skill therefore covers the three channels that actually exist.

## Channel 1: the response you write before submitting

At a no-rebuttal venue, every anticipated objection must be answered inside the
submission itself, because there is no second chance. Build an objection ledger
during the final month and discharge each row into the paper:

| Predictable objection | Where to discharge it in a STOC submission |
|---|---|
| "Is this not implied by [known result]?" | A "Comparison with prior work" paragraph that names the result and states the formal gap |
| "The improvement is only in the exponent/log factor" | An explicit "Why this barrier matters" passage citing the known obstruction |
| "The technique looks standard" | A technical-overview section isolating the genuinely new step |
| "Does the proof of Lemma X really work?" | Full proof in the appendix plus a one-line proof idea at the statement |
| "Why STOC and not SODA/CCC/ITCS?" | First-page framing that names the cross-area consequence |
| "The model seems contrived" | A remarks subsection defending the model with prior uses |

A useful drill: have a colleague write three hostile review sentences, then verify
the submission already contains the counter-text at a location the table of
contents makes findable.

## Channel 2: chair-mediated clarification

Theory PCs sometimes route a narrow technical question to authors through the PC
chair when correctness of a specific step is the deciding issue. You cannot
solicit this contact; you can only be ready for it. If it comes:

- Answer only the question asked. This is not a rebuttal; volunteered advocacy
  reads poorly and may be discarded.
- Point to line numbers and displayed equations in the submitted PDF, not to a
  revised draft the committee has never seen.
- If the questioned step is actually broken, say so and state precisely what
  survives — theory committees have accepted papers whose authors honestly
  downgraded one lemma, and rejected papers whose authors papered over a gap.

```text
Reply skeleton (keep under ~300 words, anonymous if the cycle is double-blind):
1. Restate the question in one line.
2. The direct answer: the step holds because <argument>, see p.<n>, Eq. (<k>).
3. If a hypothesis was implicit: name it, confirm it is satisfied where used.
4. If repair is needed: the corrected statement, and what changes downstream.
```

## Channel 3: the post-decision letter to yourself

Reviews arrive with the decision. The productive response is a resubmission memo
written within a week, while the reviews are fresh:

- Sort review points into: correctness challenges (must resolve before any
  resubmission), significance challenges (need reframing or a stronger result),
  and presentation complaints (cheap to fix).
- The default next stop is **FOCS**, whose deadline sits roughly five months after
  STOC notification (FOCS 2026: April 1, 2026, 21:00 UTC, for a November 2026
  conference in New York — verified 2026-07-08 at `focs.computer.org/2026/`). The
  same community reviews both venues; an unchanged resubmission is frequently
  re-reviewed by an overlapping pool, so visible improvement is strategy, not
  courtesy.
- If reviewers questioned significance rather than correctness, consider whether
  the result is better amortized into a stronger merged paper than resubmitted
  alone.

## Reading theory reviews accurately

STOC reviews released with decisions vary from a paragraph to several pages.
Decode them before reacting:

- A long, detailed review with line-level proof comments means a subreviewer
  invested real verification effort — its technical points are usually right
  and always worth fixing, whatever the outcome.
- "I could not verify Section 5" is not a neutral remark; at this venue an
  unverified central section is a rejection reason by itself, and the repair is
  exposition, not indignation.
- "Better suited to <venue>" is the breadth axis talking. It is often the most
  actionable sentence in the review: the mathematics passed, the framing or
  the routing failed.
- Contradictory reviews (one calls it deep, another incremental) usually mean
  the technical overview let readers form divergent models of the
  contribution; that is a writing bug with a known fix (`stoc-writing-style`).

## What not to do

- Do not email PC members or the chair to argue a decision; theory norms treat
  this as a serious breach, and decisions are final.
- Do not post a public rebuttal thread attacking anonymous reviewers while the
  companion journal version is under review with the same community.
- Do not treat the absence of rebuttal as license to leave known weaknesses
  unaddressed "unless asked" — at STOC, unasked is unanswered.

## Timing the channels

- Objection-ledger work belongs in the last month before the deadline, once
  the results are frozen — earlier, and the objections target statements that
  will change; later, and the discharge text has no pages left to live in.
- A chair-mediated query, if it comes, tends to arrive mid-cycle
  (December–January in the 2026 calendar) with a short fuse; keep the proof
  sources and the corrections file warm rather than reconstructing context
  under a 48-hour clock.
- The resubmission memo has a one-week half-life: written immediately, it
  captures what the reviews actually said; written a month later, it captures
  what you wish they had said.

## Cycle-volatility warnings

- Any experiment adding an author-visible feedback step will be announced in the
  CFP or on the HotCRP site for that year; do not assume continuity (待核实).
- The chair-mediated clarification practice is a community custom, not a
  documented right; some cycles use it, some never do.

## Output format

```text
[Channel in play] pre-emptive writing / chair query received / post-decision triage
[Objection ledger] <objection -> discharge location in the PDF>
[Query reply plan] <question, answer location, honesty check>
[Resubmission target] FOCS <deadline> / SODA / journal / strengthen first
[Risk] <the one unresolved reviewer concern>
```
