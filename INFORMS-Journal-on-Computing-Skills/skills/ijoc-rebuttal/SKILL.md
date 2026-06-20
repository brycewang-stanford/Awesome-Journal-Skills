---
name: ijoc-rebuttal
description: Use when drafting the response to an INFORMS Journal on Computing (IJOC) decision letter — turning referee objections (especially about experiments and reproducibility) into a point-by-point response with re-run evidence. Builds the rebuttal and revision plan; it does not run new analysis on its own (route to ijoc-data-analysis).
---

# Rebuttal Strategy (ijoc-rebuttal)

## When to trigger

- An IJOC **major/minor revision** arrived and you need a response-letter strategy
- Referees challenge the **fairness, scale, or reproducibility** of the computational experiments
- You disagree with a referee on a method point and must push back **without alienating** the associate editor
- You need to convert a long, mixed decision letter into an ordered, checkable revision plan

## The IJOC rebuttal mindset

IJOC revisions are won with **evidence, not rhetoric**. Most consequential objections are computational ("the comparison is unfair," "instances too small," "cannot reproduce"), and the strongest response is a re-run that settles the question: more standard instances, a stronger baseline, more seeds, a performance profile, an updated deposit. Because the **associate editor is undisclosed and single-blind**, write to the substance of each report for a technical reader; never speculate about who wrote what. The AE is reading for whether you took the experiments seriously.

## Structure of the response

1. **Open with the changes that matter.** A short summary: the main new experiments, the strengthened baselines, the reproducibility fixes — so the AE sees the substantive work first.
2. **Point-by-point, quoting each comment.** Reproduce each referee point verbatim, then respond. Use a consistent tag: **[Done — with evidence]**, **[Done — text]**, **[Respectfully disagree — with reason]**.
3. **Show the evidence inline.** For computational objections, include the new table/profile or its key number and a pointer to where it now lives in the paper and the deposit. "We re-ran on the full MIPLIB-class set; the performance profile (new Fig. 5) shows we dominate beyond τ=1.4; updated in `results/` (illustrative)."
4. **Be honest about limits.** Where a competitor still wins a regime, say so and scope the claim rather than overclaiming — IJOC referees reward calibrated honesty.

## Mapping common IJOC objections to the response

| Objection | Winning response | Owning skill |
|-----------|------------------|--------------|
| "baseline is weak / outdated" | re-run vs. current solver/SOTA, symmetric tuning; show the new comparison | `ijoc-data-analysis` |
| "instances cherry-picked / too small" | full standard set + scaling plot; report losses too | `ijoc-data-analysis` |
| "results not statistically supported" | add Wilcoxon + performance profile; multiple-seed dispersion | `ijoc-data-analysis` |
| "no guarantee / correctness unclear" | add validity/complexity proof; reconcile theory with plots | `ijoc-theory-development` |
| "cannot reproduce your numbers" | fix and re-tag the deposit; align `results/` to tables; confirm it runs clean | `ijoc-data-analysis` |
| "contribution incremental" | sharpen claim + positioning vs. recent work | `ijoc-contribution-framing` / `ijoc-literature-positioning` |
| "out of scope" | re-argue computing-first fit, or reconsider venue | `ijoc-topic-selection` |

## Disagreeing well

You may push back, but with a reason a technical reviewer accepts: a misread of the method, a baseline that is not actually comparable, a request outside the paper's scope. Concede the framing ("the reviewer is right that X would strengthen the paper") even while declining ("but it changes the research question; we instead add Y, which addresses the underlying concern"). Flat refusal with no alternative is what loses AEs.

## Checklist

- [ ] Response opens with the substantive new experiments and reproducibility fixes
- [ ] Every referee point quoted and answered with a clear status tag
- [ ] Computational objections answered with re-run evidence, not prose
- [ ] New/updated exhibits pointed to in both the paper and the deposit
- [ ] The deposit re-tagged and confirmed to reproduce the revised results
- [ ] Disagreements carry a technical reason and an alternative
- [ ] Claims rescoped honestly where a competitor still wins
- [ ] Tone is professional; no speculation about the undisclosed AE/referees

## Anti-patterns

- Answering an experimental objection with words instead of a re-run
- Marking points "Done" without changing the paper or the deposit
- Updating the manuscript but leaving the GitHub deposit stale (a "cannot reproduce" relapse)
- Flat refusal of a reviewer request with no reason or alternative
- Overclaiming after revision instead of scoping to the regimes you actually win
- Guessing the AE's or reviewer's identity and writing to it

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-rebuttal
【Summary of changes】new experiments / baselines / reproducibility fixes
【Point-by-point】each comment quoted + status tag + evidence pointer
【Re-run evidence】profiles/tests/seeds added where challenged
【Deposit】re-tagged and reproduces revised results? [Y/N]
【Honest scoping】claims rescoped where a rival wins
【Next step】resubmit via ScholarOne → ijoc-review-process to track the new round
```
