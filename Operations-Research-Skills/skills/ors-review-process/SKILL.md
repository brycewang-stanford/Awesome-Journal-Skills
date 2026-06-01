---
name: ors-review-process
description: Use when navigating the Operations Research (OR) editorial process — the departmental area-editor routing, the soft double-anonymous model with asymmetric transparency, decision types, and how to read a decision letter from the handling Area Editor. Explains how review works and how to read a decision; it does not draft the response (ors-rebuttal) or run the preflight (ors-submission).
---

# Review Process (ors-review-process)

## When to trigger

- You want to understand how *Operations Research* routes and decides on a manuscript.
- A decision letter arrived and you need to parse roles, signals, and the path forward.
- You are unsure who sees your identity and whose names you can see.

## How OR review is organized

*Operations Research* uses a **departmental** structure run by **INFORMS**:

- **Area-editor routing.** At submission you select one of the journal's named
  editorial areas; the manuscript is handled within that department by an **Area
  Editor (AE-area)**, who assigns an **Associate Editor**, who recruits **reviewers**.
  Areas publish **Area Editors' Statements** defining scope, so a mismatched area can
  cost you a re-route (see `ors-topic-selection`).
- **Soft double-anonymous with asymmetric transparency.** Author names are omitted from
  the submission. **Reviewers cannot see authors.** The **Area Editor and Associate
  Editor can** see author names. Distinctively, **authors can see the handling Area
  Editor's name** but **not** the Associate Editor or reviewers. This asymmetry
  distinguishes OR from fully blinded or fully open models.

## Reading the decision letter

Typical decision types and what they signal:

| Decision | Read it as |
|----------|-----------|
| Reject (or desk reject) | Fit/area mismatch, thin methodological contribution, or a fatal flaw |
| Major revision | The core idea has promise; substantial proof/experiment work expected |
| Minor revision | Results stand; address specific gaps and presentation |
| Accept | Rare on first round; expect at least one revision cycle |

When you read the letter:

- **Identify the synthesis** from the Area/Associate Editor — it ranks which reviewer
  points are binding versus optional. Prioritize the editor's emphasis.
- **Separate proof concerns from exposition concerns.** A "gap in the proof of Theorem
  X" is binding; a request to restructure is presentational.
- **Note reproducibility requests.** Expect questions tied to the **ORJournal
  code/data** review (pull-request workflow, README/LICENSE, runnable scripts).
- **Watch conference/copyright items.** If a prior conference version exists, the
  editor may probe the incremental contribution and copyright.

## Expectations as an OR author

- Engage the **technical substance**: strengthen assumptions, tighten bounds/rates, add
  the missing baseline or instance set — not cosmetic edits.
- Respect the **page tiers** and the **e-companion ≤ manuscript** rule when expanding.
- Keep the introduction **equation-free** through revisions.

## Anti-patterns

- Treating every reviewer point as equal and ignoring the editor's synthesis.
- Arguing with a reviewer instead of fixing a genuine proof gap.
- Expanding the paper past its page tier to answer reviewers.
- Assuming reviewers can see your identity (they cannot) or that you can see theirs (you cannot).

## Output format

```
【Decision】reject / major / minor / accept
【Editor synthesis】binding points (proof vs. exposition vs. reproducibility)
【Identity map】reviewers blind to you; you see AE-area only
【Conference/copyright】flagged? 
【Plan】what to fix, in priority order
【Next step】ors-rebuttal
```
