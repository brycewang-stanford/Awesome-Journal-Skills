---
name: iccv-author-response
description: Use when ICCV reviews arrive and the one-page rebuttal must be drafted inside the one-week May window, covering the official template's constraints, evidence selection when no attachments or links are allowed, addressing reviewers who are themselves deadline-crushed authors, and writing for the meta-review that follows.
---

# ICCV Author Response

In the 2025 cycle (verified 2026-07-08), reviews reached authors on May 9 and the
rebuttal closed May 16: seven days to answer every reviewer in **one page**, using
the rebuttal template from the official author kit. Decisions followed in late
June with no further author input. This skill turns that week into a production
schedule and the page into an argument budget.

## Constraints that define the genre

- One page, official template, PDF. Over-length or reformatted responses are
  disregarded at CVF venues — squeezing margins is the same as writing nothing.
- Anonymous, no external links, no attachments. A number you cannot state in a
  sentence or a tiny table does not exist for this rebuttal.
- No new contributions. The rebuttal corrects errors, supplies requested
  clarifications, and reports small requested checks — it does not extend the
  paper.
- The audience is layered: reviewers first, then the AC writing the meta-review
  during the discussion that runs after your window closes. Write sentences an AC
  can lift verbatim.

## The seven days, scheduled

| Day | Work | Anti-pattern being prevented |
|---|---|---|
| 1 | Read everything once; no drafting; log each objection with reviewer ID and a fixability tag | Rage-drafting that leaks tone into the final text |
| 2 | Decide the page's allocation; launch any small requested runs (they must finish by day 5) | Discovering on day 6 that the decisive number needs three days of GPU |
| 3–4 | Draft; every paragraph = quoted objection → paper location → fact | Essays about the paper's importance |
| 5 | Freeze experiments; integrate numbers; cut to one page by deleting whole items, not words | Ten answers at three lines each, all too thin to land |
| 6 | Cold read by a coauthor who did not draft; check template compliance | In-group blindness to a condescending sentence |
| 7 | Upload early; the deadline hour is for failures, not first uploads | Panic edits after midnight |

## Choosing what fits the page

Not every objection earns space. Rank by *expected score movement times
credibility of your answer*:

1. **A reviewer misstates the paper** — highest priority, cheapest to win: quote
   their sentence, quote yours, cite section and line. Every downstream weakness
   built on the misreading falls with it.
2. **A requested number you can produce** — small ablation, runtime on named
   hardware, a matched-backbone re-run. Report it as a two-to-five-row table.
3. **A fairness challenge to your comparisons** — answer with protocol facts
   (same splits, same pretraining, same schedule) or concede the asterisk and
   scope the claim; a precise concession reads as strength during discussion.
4. **Novelty skepticism** — two sentences of mechanism-level delta against the
   named prior work. Never argue "first"; argue *different and consequential*.
5. **Requests for a new benchmark, a new method variant, human studies** —
   decline in one polite line as out of rebuttal scope. Reviewers know the rules;
   the AC certainly does.

Anything ranked below the fold gets one clause or nothing. A one-page rebuttal
that lands three arguments beats one that gestures at nine.

## Formatting the page for a skimming AC

```latex
% Inside the official rebuttal template — structure by objection, not by reviewer
\noindent\textbf{[R2,R4] Backbone fairness.} R2: ``gains may come from the
stronger encoder.'' All rows of Tab.~2 share ViT-B/16 initialized from the same
checkpoint (Sec.~4.1). Under R2's requested ResNet-50 setting: ours 41.3 vs
baseline 39.8 mIoU (3 seeds, std 0.2).

\noindent\textbf{[R1] ``No occlusion analysis.''} Sec.~5.3 and Fig.~6 report
exactly this; we will make the pointer explicit in the caption.

\noindent\textbf{[R4] Concurrent work X (arXiv, Feb).} Posted three weeks before
the deadline; we will cite as concurrent. Mechanism differs: X re-ranks
proposals, we modify the matching cost (no proposal stage).
```

Shared objections get one merged heading with both reviewer IDs — answering the
same point twice wastes the scarcest resource the format has.

## Tone rules with venue-specific reasons

Your reviewers are simultaneously authors sweating their own submissions, and the
2025 cycle showed chairs act on reviewer misconduct (LLM-written or careless
reviews were desk-reject grounds for the *reviewer's* papers). Two consequences.
First, if a review is demonstrably negligent or machine-generated, the rebuttal is
not the place to litigate it — state facts flatly there, and raise the conduct
evidence through the confidential channel (see `iccv-review-process`). Second,
assume good faith in the text itself: "R3 may have missed Sec. 4.2" survives
discussion week; sarcasm gets quoted against you.

## What the rebuttal cannot do

If all reviews converge on absent evidence — the missing dataset, the unmatched
comparison — the page cannot manufacture it, and reviewers are not permitted to
demand major new experiments anyway. Spend a day of the week, not all seven, then
redirect the team to the fallback ladder (`iccv-workflow`): ECCV's next spring
deadline, CVPR in November, or (if it recurs) the Findings outlet for sound work.

## Numbers etiquette inside the page

Small-run results reported in a rebuttal carry review-period obligations: state
seeds and settings in the table caption even at miniature scale ("3 seeds,
matched schedule"), never contradict the paper's own protocol silently, and
carry every rebuttal number into the camera-ready if accepted — the promise
diff in `iccv-camera-ready` starts from this page. A rebuttal number that later
vanishes from the paper is remembered by exactly the people who requested it.

## Reverify each cycle

- Rebuttal existence, exact window, and page cap for 2027 — 待核实 until posted.
- Template location in the current author kit.
- Whether any interactive discussion with reviewers exists (2025 was one PDF, no
  back-and-forth).

## Output format

```text
[File or fold] rebuttal worth filing: yes/no (reason)
[Page allocation] <objection → lines> summing to one page
[Runs launched] <experiment → finishes by day 5? owner>
[Misreads to kill] <review quote → paper location>
[Concessions] <what we scope down, in one sentence each>
[Conduct channel] anything for confidential escalation: no / summary
```
