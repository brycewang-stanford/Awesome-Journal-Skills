---
name: emnlp-writing-style
description: Use when revising an EMNLP draft for the venue's empirical voice — phenomenon-first framing, claims scoped to tested languages and domains, examples tied to counted errors, a Limitations section with content, honest hedging calibrated to evidence strength, and ACL two-column discipline for long and short formats.
---

# EMNLP Writing Style

Use this during revision. EMNLP's house voice is that of a careful experimentalist: the
paper reports what was measured, in prose that never outruns the tables. The most common
style failure at this venue is not bad English — it is *claim inflation*, where the
abstract promises "understanding" and the evidence delivers accuracy on four datasets.

## The scoping discipline

Every empirical claim carries an implicit quantifier, and EMNLP reviewers expand it:

| Draft sentence | What a reviewer hears | Scoped rewrite |
|---|---|---|
| "LLMs cannot track negation" | All LLMs, all negation, all languages | "The three 7-13B models we test fail on double negation in English and German (Table 4)" |
| "Our method improves summarization" | Everywhere, always | "…improves faithfulness on news summarization in two of three datasets; gains do not transfer to dialogue (§6.3)" |
| "This is a multilingual benchmark" | Typologically broad | "…covering five Indo-European languages; we discuss this limit in §Limitations" |
| "significantly better" | A statistical test exists | "+1.8 F1, paired bootstrap p<0.01 over 5 seeds" — or delete "significantly" |

The rewrites are not weaker papers; they are the same paper with its evidence and its
prose in agreement — which is precisely what the soundness score measures.

## Examples must be load-bearing

NLP papers live on examples, and EMNLP reviewers distinguish two uses sharply.
Decorative: a cherry-picked output demonstrating the method at its best. Load-bearing:
an example *representing a counted category* — "the model hedges the modal verb, an
error type accounting for 34% of failures (Table 6, row 2)." Convert every decorative
example to a load-bearing one or cut it; an example without a frequency is an anecdote,
and the CFP-era reviewer culture treats anecdotes as filler.

## First-page architecture

The opening should let a tired area chair reconstruct the paper: the phenomenon or task
failure (with a number), why existing evaluation misses it, what you did, what you
found, and where it breaks. Two structural rules follow. First, name the *language
behavior* before the model: "summarizers delete speaker commitments" precedes any
mention of architecture. Second, contribution bullets must be falsifiable — "we show X
holds in Y setting but not Z" survives review; "we propose a novel framework" is
unfalsifiable and reads as such.

## Writing the Limitations section

The mandatory, uncounted Limitations section is the most misused free real estate in
the format. Ritual limitations ("results may not generalize") waste it. Content
limitations do reviewer-defusing work:

```text
Weak:   "Our approach may not work for all languages."
Strong: "All six test languages are written in Latin or Hangul scripts with
        whitespace tokenization; our segmentation-dependent method has no
        evidence for Thai or Chinese. Annotator pool was US-based crowdworkers,
        so the politeness judgments encode one cultural frame (§5.4)."
```

The strong version names the boundary, the mechanism behind it, and where the paper
already discusses it. Reviewers routinely check whether the Limitations section admits
the weakness they independently found — matching it is credibility; missing it is a
soundness deduction.

## Hedging calibration

Empirical prose needs exactly one hedging level per claim, chosen by evidence:

- Demonstrated on your data: indicative mood, no hedge — "the effect reverses on
  dialogue data."
- Supported but unproven mechanism: "consistent with", "suggests" — once, not stacked.
- Speculation: fence it explicitly ("we speculate…") or move it to future work.

Stacked hedges ("may potentially suggest") and false confidence ("proves") are equal
and opposite failures; both misreport evidence strength.

## Titles and abstracts, venue idiom

EMNLP titles carry information, and the program is searched by task: name the
phenomenon or task in the title, not just the system ("Pragmatic Drift in Multilingual
Summarizers" beats "PoliteSumm: A Novel Framework for Better Summaries"). System names
are fine as prefixes when the system is the release; they are dead weight when the
finding is the contribution. In abstracts, the venue idiom is *numbers early*: the
best EMNLP abstracts contain the headline measurement, the languages or datasets, and
the significance posture — a reader should be able to referee the claim's scope from
the abstract alone.

## Terminology honesty

Two lexical habits mark careful empirical writing here:

- **"Understanding," "reasoning," "knows"** — mentalistic verbs applied to models get
  flagged unless operationalized; prefer the measured behavior ("answers correctly
  under paraphrase") or define the construct once and stick to it.
- **"State-of-the-art"** — a comparative claim against a moving population; if used,
  date it and bound it ("among open models under 13B evaluated on X as of May 2026"),
  or replace it with the actual comparison made.

## Two-column craft, ACL flavor

- Long papers get 8 content pages, short papers 4, references free, Limitations and
  ethics uncounted — design the argument for the cap instead of compressing at the end.
- Wide comparison tables dominate NLP papers: prefer one decision-relevant table in the
  body and push completeness grids to the appendix, cross-referenced.
- Non-Latin script examples need declared fonts and romanization plus gloss; an example
  the reviewer cannot read is an example that does not exist.
- Short papers: one claim, stated in the first paragraph, with the strongest single
  table — a short paper that "surveys" its own contribution has already failed.

## The revision pass, ordered

Run the passes separately — combined passes miss things: (1) claim-scope pass over
every abstract and section-opening sentence; (2) example audit tying each excerpt to a
counted category; (3) hedge calibration; (4) Limitations content check against the
weaknesses you privately know; (5) format sweep for scripts, table widths, and the
uncounted sections. The first pass matters most and is best done by the coauthor who
did *not* run the experiments — attachment to results is what inflates their
description.

## Output format

```text
[Voice diagnosis] scoped / inflated / over-hedged / anecdotal
[Claim-scope repairs] <sentence -> scoped rewrite>
[Example audit] <decorative examples -> counted category or cut>
[Limitations quality] ritual / content — with the missing admissions
[Format risks] <tables, scripts, page-cap pressure>
```
