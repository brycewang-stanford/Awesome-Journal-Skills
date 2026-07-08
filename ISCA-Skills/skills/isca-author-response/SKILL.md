---
name: isca-author-response
description: Use when ISCA reviews arrive and the rebuttal-plus-revision window opens — triaging objections by what a three-week window can actually fix, deciding between textual rebuttal and a revised PDF with new experiments, structuring responses that arm a champion at the PC meeting, and avoiding window-burning mistakes.
---

# ISCA Author Response

ISCA 2026 gave authors a combined **rebuttal/revision period, February 16 to
March 6** — three weeks in which the team could both argue and *change the
paper*. That design rewards teams that treat the window as an engineering sprint
with a triage phase, and punishes teams that spend it composing indignation.
Everything here assumes that verified 2026 structure; the 2027 window's
existence, length, and rules are 待核实 until the new CFP posts.

## Day 1-2: triage before any writing or computing

Read all reviews twice: once fast for temperature, once slow building the
objection ledger. Classify every distinct point:

| Class | Definition | Window response |
|---|---|---|
| **F** — factual error | Reviewer misread something present in the PDF | Quote page/section/figure; one sentence; zero new work |
| **E** — evidence gap, closable | Missing experiment your infrastructure can run in days | Run it; report in response; fold into revision if permitted |
| **E∞** — evidence gap, not closable | Needs silicon, months, or data you lack | Concede scope honestly; state what the existing evidence does cover |
| **D** — design objection | "This breaks under X" / "cost is understated" | Analyze X concretely; if real, add the limitation; if not, show why |
| **P** — premise objection | "This problem doesn't matter" | Strongest countermeasure is motivation data; if you have none beyond the paper, one calm paragraph and move on |
| **T** — taste | "I'd have designed it differently" | Acknowledge once; do not redesign the paper |

Then rank by *leverage*: an F held by two reviewers outranks an E held by one;
anything a likely champion needs to defend the paper outranks everything else
(`isca-review-process` explains why the champion is the audience).

## Day 2: freeze the experiment plan

Pick at most three new experiments — the ones that convert the highest-leverage
E-class objections into numbers. Assign owners and a hard finish date one week
before window close, leaving prose time. The classic window failure is five
half-finished experiments and a response that promises rather than shows.

```text
window-plan.md
  R2.O3  (E, leverage=high)  "no comparison vs LazyMerge at equal storage"
         -> run: lazymerge @ 18KB/core, full suite; owner: MK; due Feb 27
  R1.O1  (F, leverage=high)  "warm-up unstated"
         -> answer: §5.1 para 2, 50M inst; also add to config table in revision
  R3.O2  (D, leverage=med)   "decay threshold fragile"
         -> run: sweep T in {2K..64K}; expect plateau; owner: JL; due Feb 25
  R3.O5  (T, leverage=low)   "why not epoch-based?"
         -> one paragraph, cite §4.2 rationale; no experiment
```

## Writing the response document

Structure for committee reading, not reviewer combat:

1. **Opening block (5-6 lines):** thank, then list the concrete changes/results
   produced during the window — the things a champion can repeat in the room.
2. **Per-objection sections keyed to review IDs**, highest-leverage first.
   Each: restate the objection in one neutral line, answer with evidence
   (number, table row, or PDF pointer), stop.
3. **Shared-objection consolidation:** answer once, cross-reference the copies —
   it shows the committee the objection set is smaller than it looks.

Tone rules that survive contact with real committees: concede real limitations
in plain declarative sentences (concessions buy credibility that transfers to
your rebuttals); never speculate about reviewer expertise or identity; never
claim "all reviewers agree" about anything they don't.

## Using the revision half of the window

If the cycle permits an updated PDF (2026's window was named rebuttal/revision):

- Make surgical edits keyed to objections: the missing baseline column, the
  config-table row, the limitation paragraph, the clarified walk-through.
- Do not restructure the paper — reviewers re-reading diff mentally against
  their memory, and a rewritten paper resets their evaluation instead of
  repairing it.
- Maintain a change log mapping edit → objection; if the process provides no
  place to submit it, embed the mapping in the response document.
- Keep the paper inside all format rules; a revision that breaks the 11-page
  budget converts goodwill into a violation. This is what the half-page of slack
  from `isca-writing-style` was for.

## What not to spend the window on

- **New contributions.** Results beyond the paper's claimed scope read as a
  different paper and invite "needs another round of review" — the phrase that
  kills borderline papers.
- **Rebutting every sentence.** A 15-point response to a 3-objection review
  buries your leverage. Committees skim; make the skim land the top three.
- **Premise litigation at length.** One paragraph of motivation defense with
  data; more looks defensive and reads worse each repetition.
- **Simulator relitigating.** If a reviewer distrusts your instrument globally,
  the fix is the validation anchor you either have (point to it) or don't
  (concede and scope) — not an essay on simulation philosophy.

## Window-close checklist

- [ ] Every review ID answered or explicitly consolidated
- [ ] Top-3 objections answered with *numbers produced this window*
- [ ] All F-class errors corrected with pointers, tone neutral
- [ ] Revision (if permitted) diff-minimal, format-legal, change-mapped
- [ ] A colleague outside the project read the response cold and could state
      your three key answers back to you
- [ ] Submitted with margin — the window closes AoE like everything else

## The three weeks on a calendar

Using the 2026 window (Feb 16 - Mar 6) as the shape:

| Days | Activity |
|---|---|
| 1-2 | Triage; objection ledger; leverage ranking; no computing yet |
| 2 | Experiment plan frozen: ≤3 runs, owners, due dates |
| 3-12 | Experiments execute; response skeleton drafted in parallel |
| 13-15 | Results in; response written against real numbers |
| 16-18 | Revision edits (if permitted), diff-minimal, format-checked |
| 19-20 | Cold read by an outside colleague; tone pass; consolidation pass |
| 21 | Submit with hours to spare, AoE-checked |

After the window, silence until decisions; outcome handling branches in
`isca-review-process`, and calendar context lives in `isca-workflow`. Verified
dates: `../../resources/official-source-map.md` (2026-07-08).
