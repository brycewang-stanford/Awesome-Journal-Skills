---
name: jacs-revision
description: Use when a decision letter/referee reports arrive for a Journal of the American Chemical Society (JACS) manuscript, to plan experiments and draft the point-by-point response. Structures the revision and rebuttal — it does not fabricate data or guarantee acceptance.
---

# Revision and Response to Reviewers (jacs-revision)

## When to trigger

- A decision letter (major/minor revision, or reject-with-encouragement) arrived
- You need to triage referee comments into experiments vs edits vs rebuttals
- You are drafting the point-by-point response letter
- You must decide whether to appeal or to resubmit elsewhere

## Triage the reports first

Sort every numbered comment into one bucket:

| Bucket | Action |
|--------|--------|
| **Data-required** | A control, extra characterization, X-ray, kinetics, or scope substrate is genuinely needed → do the experiment |
| **Clarification** | A real point the text/figure can fix without new data → edit + point to the change |
| **Defensible disagreement** | Reviewer is mistaken or asks beyond scope → rebut politely with evidence |
| **Optional/over-reach** | Nice-to-have; address briefly or explain why out of scope |

Address the **rigor-critical** comments (purity, characterization, mechanism
support, reproducibility) first — these are the ones that block acceptance at JACS.

## Response-letter structure

1. **Opening** — thank the editor/reviewers; summarize the main changes and any new data/figures/SI added.
2. **Point by point** — quote each comment, then respond. For each: state the change, where it is in the revised manuscript/SI (section, figure, page), and the new evidence.
3. **Quote the new text** — paste added/changed passages so reviewers don't hunt.
4. **Rebuttals** — for disagreements, be respectful and evidence-based; concede where the reviewer improves the paper.
5. **Marked manuscript** — provide a tracked/colored version if requested.

## Doing the new chemistry well

- New experiments must meet the same rigor bar: full characterization, controls,
  CCDC deposition for any new structure, reproducible procedures (route to `jacs-methods`).
- New compounds → add full SI entries and spectra copies (route to `jacs-supplementary`).
- If a requested experiment fails or contradicts a claim, report it honestly and
  adjust the claim rather than hiding it.

## Tone

- Professional, specific, and complete; never dismissive even when disagreeing.
- Make the reviewer's job easy: cross-reference every change to a location.
- If a comment is based on a misreading, fix the text so the next reader can't misread it too.

## JACS revision ledger

Before drafting prose, make a revision ledger that separates **editor-critical chemistry** from
ordinary cleanup. JACS revisions fail when a response looks complete but leaves one evidence gap
unclosed. Track each item with four fields:

| Field | JACS-specific check |
|-------|---------------------|
| Claim under review | What exact novelty, scope, mechanism, selectivity, or structure claim did the referee challenge? |
| New evidence | Which experiment, characterization trace, spectrum, crystallographic deposit, kinetic run, or control now supports it? |
| Manuscript/SI location | Main-text figure/table, scheme, or SI page where the reader can verify the fix without searching. |
| Claim adjustment | Whether the language is strengthened, narrowed, or hedged because the new evidence changed the inference. |

Use the ledger to decide whether a comment is truly answered. A reviewer asking for "more evidence"
is not answered by a paragraph; it is answered by a trace, table, structure, or explicitly narrowed
claim. Conversely, a referee misunderstanding that came from ambiguous prose should produce both a
response-letter explanation and a revised sentence in the manuscript so the same misreading cannot
recur in the next round.

## Checklist

- [ ] Every numbered comment has a response — none skipped
- [ ] Rigor-critical comments addressed with real data, not words
- [ ] New compounds/structures fully characterized and deposited (CCDC)
- [ ] Each response cites the exact location of the change
- [ ] Added/changed text quoted in the letter
- [ ] Disagreements rebutted with evidence and courtesy
- [ ] Claims softened or revised where new data require it
- [ ] Marked-up manuscript prepared if requested

## Anti-patterns

- Responding "we have addressed this" without saying where or how
- Adding new compounds without adding their SI characterization
- Arguing with a referee instead of fixing the ambiguous text
- Quietly dropping an inconvenient result instead of reporting it
- Over-claiming again in the revision after softening in round one
- Ignoring a rigor request and hoping the editor overrides the referee

## Output format

```
【Decision】major / minor / reject-with-encouragement
【Triage】data-required: [...]; clarify: [...]; rebut: [...]
【New experiments】done? characterized + deposited? Y/N
【Response letter】point-by-point complete? Y/N
【Claims adjusted】[...]
【Next】resubmit via Paragon Plus → await decision
```

## Related resources

- [`jacs-methods`](../jacs-methods/SKILL.md) — rigor bar for new experiments
- [`jacs-supplementary`](../jacs-supplementary/SKILL.md) — adding SI for new compounds
- [`jacs-referee-strategy`](../jacs-referee-strategy/SKILL.md) — anticipated objections to map onto the actual reports
