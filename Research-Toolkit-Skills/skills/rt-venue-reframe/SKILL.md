---
name: rt-venue-reframe
description: Use after a rejection, or when switching target journals, to turn a manuscript framed for one venue into one framed for another. Produces a concrete reframing diff — introduction arc, contribution claim, evidence to add or cut, house style, format — by reading both venues' own packs. Complements rt-journal-match, which picks the venue; this one does the rewrite plan.
---

# Cross-Venue Reframe (rt-venue-reframe)

`rt-journal-match` answers *which venue next*. This answers the question that
immediately follows and that nothing else in the repository covers: **what actually has
to change in the paper.**

Authors do this after almost every rejection, and they do it badly — usually by
swapping the journal name in the cover letter and resubmitting. A real reframe is a
diff across five layers, and both endpoints are already documented in this repo: the
source venue's pack and the target venue's pack.

## When to trigger

- A paper was rejected at venue A and the next rung is venue B.
- The author is choosing between two live targets and wants to know the cost of each.
- An editor or referee said "this reads like a *<other venue>* paper".
- A paper written for an international venue is being re-aimed at a Chinese venue, or
  the reverse — the largest reframe distance in this repository.

## Inputs

1. **From venue** and **to venue** — as `venue_id`s in
   [`venue-index.tsv`](../../../shared-resources/journal-selection/venue-index.tsv).
   If the author only names a rejection, take the next rung from
   [`ladder.tsv`](../../../shared-resources/journal-selection/ladder.tsv) — filter to
   `same_discipline = yes` and prefer high `mentions`, then sanity-check against
   `rt-journal-match`.
2. **The manuscript** — at minimum the title, abstract, intro, and the main table.
3. **The rejection signal**, if any — desk reject, referee reject, or "not a fit".

## Method — diff five layers, in this order

Read the **to** venue's fit/topic-selection and writing-style skills first; read the
**from** venue's only to identify what the paper currently optimizes for. Where a venue
is a breadth-bundle profile, its single `SKILL.md` (`profile_path`) carries the same
five layers in condensed form.

| Layer | Read | Produce |
|---|---|---|
| **1. Contribution claim** | both packs' `*-topic-selection` / `*-contribution-framing` | the one sentence the paper must now be able to answer "why does this matter?" with. This is the layer that decides acceptance; the rest is execution. |
| **2. Introduction arc** | both packs' `*-writing-style` | what moves to the first page, what drops to §2, what leaves entirely. General-interest venues want the surprising result early; field venues want the literature debt paid first. |
| **3. Evidence bar** | the to-venue's `*-identification` / `*-robustness` / `*-experiments` | which robustness the new venue treats as baseline and the paper lacks, and which existing appendix material is now dead weight. |
| **4. House style & format** | the to-venue's `*-writing-style` + `resources/official-source-map.md` | length, abstract style, exhibit conventions, citation style, appendix policy. **Read the source map live — never quote a page cap or format rule from memory.** |
| **5. Policy & package** | the to-venue's `*-replication-package` / data policy in the source map | what the data-and-code deposit now requires; proprietary-data disclosure differences. |

Then **rank the diff by cost × necessity**: a reframe that needs a new identification
strategy is a different paper, and the honest answer may be "this is not a reframe,
pick a different rung."

## Hard rules

1. **Read both packs. Never reframe from memory of a venue's reputation.**
2. **All volatile facts (length, format, fees, data policy) come from the to-venue's
   `resources/official-source-map.md` at reframe time.**
3. **Defer fit judgement to the to-venue's own topic-selection skill** — this skill
   sequences and diffs, it does not overrule the venue's pack.
4. **Say when a reframe is not worth it.** If layer 1 or 3 requires new evidence the
   author cannot produce, state that plainly and route back to `rt-journal-match` for a
   different rung. Framing cannot rescue an identification problem.
5. **Preserve the paper's honesty.** Reframing changes emphasis, structure and claim
   *scope* — never the findings, magnitudes, or caveats. If a target venue's bar seems
   to require overstating a result, that is a signal the venue is wrong, not the result.

## Output format

```
【From → To】venue A → venue B  (ladder evidence: n mentions | manual)
【Distance】small / moderate / different-paper — one line of why
【1 Contribution claim】before → after (the new "why it matters" sentence)
【2 Introduction arc】move / cut / add, in order
【3 Evidence bar】missing-and-required · now-dead-weight
【4 House style】length · abstract · exhibits · citations   (source-map read: <date>)
【5 Policy】data-and-code deltas
【Cost-ranked plan】1..n, each with an effort estimate
【Do not do this reframe if】the condition that makes it futile
```

## Anti-patterns

- Rewriting only the introduction. Layer 1 usually implies layer 3, and a paper whose
  claim moved but whose evidence did not gets desk-rejected faster than the original.
- Reframing "upward" after a referee reject without addressing the binding objection —
  route through the from-venue's `*-robustness` skill first.
- Treating a Chinese ↔ English move as a translation task. The contribution grammar
  (制度背景, 边际贡献, policy salience vs. general-interest novelty) differs, and both
  packs document their own.
- Quoting the target's page cap or fee from memory instead of the source map.

Next: `rt-desk-reject-risk` to score the reframed draft against the new venue, then
`rt-submission-readiness` for the mechanical bar.
