---
name: psci-writing-style
description: Use when drafting or polishing a Psychological Science manuscript to fit its distinctive word format (Introduction + Discussion + footnotes + acknowledgments + appendices <= 2,000 words combined; Method + Results excluded; 150-word structured abstract) in APA 7th-edition style. Tightens prose and format; it does not invent content.
---

# Writing Style (psci-writing-style)

Psychological Science has one of the most demanding formats in the field. Writing well here means
making a high-impact argument in **very few words**, in **APA 7th-edition** style, with a **structured
150-word abstract**. This skill is about fitting and polishing — not generating claims.

## When to trigger

- Drafting the Introduction/Discussion or doing final polish
- Over the word budget and needing to cut without losing the argument
- Writing the **150-word** abstract
- Aligning to APA 7th edition before submission

## The word format (know it cold)

- **Introduction + Discussion + Footnotes + Acknowledgments + Appendices ≤ 2,000 words combined.**
- **Method + Results do not count** toward that limit (but should typically stay under ~2,500 words).
- **150-word abstract** (excluded from the limit) that must state **sample sizes, participant
  populations, and important limitations of the research design**.
- ~**40 references** suffice for most Research Articles.

## Writing to the format

1. **Front-load ruthlessly.** The Introduction states the question, the gap, and the contribution in a
   few tight paragraphs (see `psci-literature-positioning`).
2. **Discussion earns every sentence.** Lead with what the result means and its breadth; keep
   limitations honest but concise. Intro + Discussion *share* the 2,000 words — budget them together.
3. **Put detail where it doesn't cost the budget.** Method and Results are outside the 2,000-word cap
   and can carry necessary procedural detail; move extended material to **supplemental online material**.
4. **Structured abstract.** In 150 words: the question, what you did, sample sizes + populations, the
   key finding (effect + direction), and a design limitation. This is content-bearing, not decorative.
5. **APA 7th edition.** Headings, statistics reporting (with effect sizes + CIs), bias-free language,
   and author-date citations; manage references with a tool and prune to the essentials.

## Worked micro-example — a 150-word structured abstract (illustrative)

For the two-study attention package, every clause earns its place; sample sizes, populations, and a
limitation are non-negotiable. Confirm the current abstract length against the journal's submission
guidelines.

```
[Question] Does a brief mindfulness induction reduce attentional capture by
emotional distractors? [What we did] Two preregistered experiments tested a
single induction against a control on a screen-based capture task.
[Samples] Study 1: 240 undergraduates; Study 2: 300 online adults.
[Result] The induction reduced capture cost (Study 1 d = 0.34, 95% CI
[0.08, 0.59]; Study 2 directly replicated, d = 0.29 [0.06, 0.51]).
[Limitation] Effects are limited to brief laboratory inductions in healthy
adults and may not extend to clinical anxiety. [≈ 95 words; expand to ~150.]
```

## Word-budget allocation (illustrative)

| Section | Counts toward 2,000? | Suggested share | Note |
|---------|----------------------|-----------------|------|
| Introduction | yes | ~55–60% | question, gap, contribution by paragraph two |
| Discussion | yes | ~35–40% | meaning + breadth first, limitations brief |
| Footnotes / acks / appendices | yes | keep minimal | they eat the same budget |
| Method + Results | no (≤ ~2,500) | as needed | procedural detail lives here, not the Intro |
| Supplemental online material | no | unlimited | robustness, full models, extra studies |

## Cutting-to-format playbook

- Move every robustness grid, full model table, and extra study to supplemental; cite in one sentence.
- Convert background prose into a single anchor citation (handoff to `psci-literature-positioning`).
- Replace dichotomous "significant" sentences with estimation phrasing — often shorter *and* more
  venue-appropriate.
- If the Discussion restates Results, delete the restatement; lead with interpretation and breadth.

## Prose-stage reviewer pushback and the venue fix

- "Reads like a review article" → cut chronological background; state the gap in two or three sentences.
- "Abstract missing limitations" → add one design-limitation clause; this venue expects it.
- "Stats without effect sizes" → report d/CI inline even when prose is tight; it is non-negotiable here.

## Anti-patterns

- A long literature review or theory section that blows the 2,000-word budget
- A Discussion that restates results instead of interpreting their meaning and breadth
- An abstract that omits sample sizes/populations/limitations or exceeds 150 words
- Padding Method/Results because they're "free" — they still must stay readable (~2,500)
- Stats reported without effect sizes / confidence intervals

## Output format

```
【Intro+Discussion budget】combined word count ≤ 2,000 (incl. footnotes/acks/appendices)?
【Method+Results】readable, ≤ ~2,500?
【Abstract】150 words; states sample sizes + populations + limitations?
【APA 7th】headings, stats (ES+CI), citations consistent? [Y/N]
【Cuts】what moved to supplemental online material
【Next】psci-open-science-and-transparency
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `papaja`, reference managers, reproducible reporting
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — word format, abstract rule, APA 7th edition
