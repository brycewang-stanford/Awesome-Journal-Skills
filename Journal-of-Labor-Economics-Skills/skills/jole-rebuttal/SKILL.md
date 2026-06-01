---
name: jole-rebuttal
description: Use when drafting a response letter to a Journal of Labor Economics (JOLE) revise-and-resubmit — addressing single-blind labor referees point by point under the journal's word economy. Strategy and structure; it does not run new estimations for you.
---

# R&R Rebuttal Strategy (jole-rebuttal)

## When to trigger

- A JOLE decision letter arrives with referee reports and an invitation to revise
- You have new results and need to convert them into a referee-by-referee response
- Referees disagree with each other and you must reconcile their demands
- You are unsure how much to concede versus defend on a labor-identification critique

## The JOLE rebuttal context

JOLE review is **single-blind**: referees know who you are, and you are responding to named-but-anonymous labor economists. The revised manuscript stays **non-anonymized** (title page with all co-authors), and it must still respect the **~20,000-word** soft cap with each full-page table/figure counting as **500 words** — so you cannot answer every comment by bolting on five new exhibits; some responses belong in the letter or a tightly bounded online appendix rather than the body. References remain **Chicago author-date**. Because the submission fee already gated the first decision, treat the R&R as the scarce, valuable channel it is.

## Structure of the response

1. **Cover note to the editor** — summarize the 2–3 most important changes and how they address the editor's framing. Keep it short; labor editors triage many revisions.
2. **Per-referee sections** — restate each comment in your own words, then answer. Use a stable numbering (R1.1, R1.2 …) so the referee can map your replies to their report.
3. **Point-by-point format** — for each: (a) quote/paraphrase the comment, (b) what you changed, (c) where in the revised manuscript (section/table/figure/page), (d) the result if it moved.
4. **Reconcile conflicts** — when two referees disagree, state both views, explain your choice, and show it does not undermine the other referee's concern.

## Substantive moves for labor papers

- **Identification challenges** (the most common): if a referee doubts parallel trends, the instrument's exclusion, or AKM limited-mobility bias, answer with diagnostics, not rhetoric — event-study leads, falsification, weak-IV-robust CIs, leave-out / bias-corrected firm effects (see jole-identification-strategy, jole-data-analysis).
- **Robustness demands**: add the check, report it, and say plainly whether the headline holds; do not hide a fragile result.
- **"Is this new for labor?"**: tighten the contribution against the labor literature (see jole-contribution-framing, jole-literature-positioning) rather than adding scope.
- **Magnitude / interpretation**: if asked, recompute and report the effect with units; do not over-claim.
- **Word economy**: relocate long defenses to a bounded online appendix; keep the body within the limit.

## Checklist

- [ ] Cover note states the 2–3 headline changes for the editor
- [ ] Every referee comment has a numbered, point-by-point reply
- [ ] Each reply names the exact location of the change in the revised manuscript
- [ ] Identification critiques answered with diagnostics, not assertion
- [ ] Conflicts between referees reconciled explicitly
- [ ] Revised manuscript still **non-anonymized** and within the ~20,000-word economy
- [ ] No new over-claiming introduced by the revisions

## Anti-patterns

- A defensive letter that argues without changing the manuscript
- Re-anonymizing the manuscript (JOLE is single-blind)
- Adding so many new full-page exhibits that the paper blows the word cap
- Conceding a fatal identification flaw with words instead of evidence
- Ignoring one referee because another disagrees
- Silently dropping a result a referee questioned instead of addressing it

## Output format

```
【Editor note】2–3 headline changes summarized? [Y/N]
【Coverage】every comment answered point-by-point with locations? [Y/N]
【Identification replies】answered with diagnostics? [Y/N]
【Conflicts】reconciled explicitly? [Y/N]
【Compliance】non-anonymized + within ~20,000 words? [Y/N]
【Next step】jole-submission re-check before resubmitting
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — packages for the robustness checks referees request
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JOLE URLs and verification status
