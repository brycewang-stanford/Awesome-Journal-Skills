---
name: orgstud-review-process
description: Use when calibrating expectations for the Organization Studies (OS) review cycle — desk-screen odds, the developmental double-anonymized process, decision types, and how to read what reviewers and the handling editor are signalling. Sets expectations and reading strategy; it does not draft the response (see orgstud-rebuttal).
---

# Review Process (orgstud-review-process)

## When to trigger

- You want to calibrate desk-reject odds and timeline before or after submitting
- A decision letter arrived and you need to read what the editor is *actually* signalling
- You are unsure whether an R&R is "major-but-encouraging" or "high-risk reject-with-resubmission"
- You are deciding whether to revise for OS or reposition to a sibling journal

## How OS review works (and how it differs)

OS runs a **double-anonymized**, **developmental** review handled by a co-editor with (typically) 2–3 reviewers drawn from the relevant conversation. The European, theory-first culture shapes what reviewers do: they engage your **theoretical contribution and your use of social theory** as the primary axis — not just method execution. Reviewers here often *co-develop* the theory across rounds, which is why OS R&Rs can be intellectually demanding and multi-round, but also why a serious R&R is a genuine signal of interest. Expect reviewers who know the canonical works in your conversation intimately.

**Desk-screen** is real and theory-driven. The most common desk-rejects are not method failures but **"interesting phenomenon, no theoretical contribution,"** wrong-fit ("belongs at a sibling journal"), or superficial engagement with the literature it claims to advance. A clean dataset will not save a paper with a thin theoretical move.

## Reading the decision

| Outcome | What it usually means | Your move |
|---------|----------------------|-----------|
| **Desk reject** | Fit/contribution problem caught pre-review | Re-diagnose with `orgstud-topic-selection` / `orgstud-contribution-framing`; consider sibling fit |
| **Reject (post-review)** | Reviewers see a fatal theoretical or evidentiary gap | Read for whether the core idea survives; usually reposition, don't resubmit |
| **Reject & resubmit / high-risk R&R** | Promising but currently not a contribution | Treat as a near-rewrite of the theory; only proceed if you can make the move land |
| **Major revision** | The contribution is real; theory/evidence need substantial development | The expected good outcome; plan a multi-issue revision (`orgstud-rebuttal`) |
| **Minor revision** | Rare on first round; contribution accepted, polishing needed | Address precisely; do not reopen settled points |

## Reading the reviewers and editor

- **The editor's letter is the binding instruction.** When reviewers conflict, the co-editor usually signals which threads are essential — prioritize those.
- **Theory comments outrank cosmetic ones.** A reviewer asking you to "engage [conversation] more deeply" or "clarify the mechanism" is naming the contribution bar; treat it as central, not as a citation chore.
- **Distinguish "develop this" from "drop this."** OS reviewers frequently push you to *develop* an underdeveloped idea — that is an invitation, not a rejection of it.
- **Reflexivity / positionality requests** are substantive at OS, not box-ticking.

## Deciding to revise vs. reposition

- Revise for OS if the contribution is real and the reviewers' essential asks are *achievable* without breaking the paper.
- Reposition if the core asks would turn it into a different paper, or if the fit critique (too descriptive, wrong conversation, sibling-shaped) is fundamental — `orgstud-workflow` can route the repositioning.

## Checklist

- [ ] You have separated *essential* asks (editor-flagged, theory-level) from optional ones
- [ ] You can state, in one line, whether the contribution survives the reviews
- [ ] Theory/mechanism/literature comments are treated as central, not cosmetic
- [ ] The outcome type is correctly read (R&R encouragement vs. high-risk resubmission)
- [ ] Revise-vs-reposition decision is made deliberately, not by default
- [ ] Timeline expectations are realistic (multi-round developmental review)

## Anti-patterns

- Reading a "reject & resubmit" as a minor revision (or vice versa)
- Treating deep-engagement/theory requests as optional polish
- Cherry-picking easy reviewer points while dodging the editor's essential threads
- Resubmitting a desk-rejected paper to a sibling without fixing the contribution problem
- Ignoring reflexivity/positionality requests as if they were pro forma

## Worked vignette: reading an ambiguous letter (illustrative)

A letter reads: "The phenomenon is fascinating and the fieldwork is impressive, but the contribution to institutional theory remains underdeveloped; we invite a resubmission if the authors can sharpen the theoretical move." Two authors read this oppositely — one as encouragement, one as a polite reject. The correct read at OS: this is a **high-risk reject-and-resubmit**, not a routine major revision. The praise is for the empirics; the binding problem is the *theoretical contribution*, which means the revision is closer to a partial rewrite than a polish. Proceed only if you can genuinely make the institutional-theory move land (route to `orgstud-theory-development` and `orgstud-contribution-framing`); otherwise reposition. Treating it as a minor revision and resubmitting with cosmetic edits is the fast path to a final reject.

## Output format

```text
【Outcome】desk reject / reject / reject-resubmit / major / minor
【Contribution survives?】yes / needs rebuild / no
【Editor's essential threads】the must-address asks
【Theory-level asks】mechanism / literature / reflexivity items flagged central
【Decision】revise for OS / reposition (which sibling)
【Next skill】orgstud-rebuttal (if revising)
```
