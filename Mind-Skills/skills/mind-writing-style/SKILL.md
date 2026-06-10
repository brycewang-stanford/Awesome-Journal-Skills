---
name: mind-writing-style
description: Use when drafting or polishing the prose of a Mind article so the argument is maximally clear to a broad philosophical readership within the ~8,000-word limit. Mind asks that even technical material be accompanied by informal exposition. Tightens sentences and clarity; it does not generate the argument (see mind-thesis-and-argument).
---

# Writing Style (mind-writing-style)

Mind prizes prose that makes a rigorous argument **easy to follow**. Authors are explicitly asked to
present arguments so they are **accessible to a broad readership among philosophers**, and where
technical material appears, to **accompany it with informal exposition**. This skill is about clarity
and economy at the sentence level — not about generating claims (that is `mind-thesis-and-argument`).

## When to trigger

- Drafting the introduction or doing a final clarity pass
- A reader said the prose is "dense," "hard to follow," or "only specialists can read it"
- A formal passage needs an informal gloss
- Over the word limit and needing to cut words without losing the argument

## Write for a broad philosophical readership

1. **Plain, exact prose.** Short declarative sentences for the key moves. Say the claim, then support
   it. Avoid ornament that hides the inference.
2. **Gloss every technicality.** When you introduce symbolism, a formal definition, or a term of art,
   immediately restate the point in ordinary language. A philosopher outside your subfield should
   follow the argument.
3. **Argument-first sentences.** Lead with the claim, then the reason — not a wind-up that buries it.
   Make the logical connective explicit ("so," "because," "but," "therefore").
4. **Define on first use; one term per concept.** Do not let a concept drift across two words, or one
   word cover two concepts (guards against the equivocation `mind-conceptual-analysis-and-method` flags).
5. **Quote sparingly and purposefully.** Use a quotation to fix the target view precisely, not to fill
   space; analyze every quotation you include.

## Mechanics

- Prefer the active voice and concrete subjects; name who claims what.
- Numbered premises or labeled claims (P1, P2, …) aid the reader when the argument is intricate.
- Keep footnotes for genuine qualifications and sources, not for a parallel essay.
- One consistent citation style throughout (full conversion to MIND house style happens in
  `mind-citation-and-style`).

## Fit the ~8,000-word limit

- Cut hedging, throat-clearing, and re-explanation of views the reader knows.
- Replace a long paraphrase of an opponent with one precise sentence (or a short quotation).
- Every sentence should advance or clarify the argument; delete decoration.
- Tighten footnotes — discursive notes are where the word count quietly grows.

## Anti-patterns

- Dense, clause-stacked sentences that hide the inference
- Formalism with no plain-language gloss (against Mind's stated expectation)
- Burying the thesis in qualifications before it is even stated
- Long block quotations left unanalyzed
- A term that shifts meaning mid-paper


## Style execution pass for Mind

Use this as a second-pass capability check. First lock the target thesis, argument map, objection sequence, and dialectical payoff; then test whether the manuscript addresses analytic-philosophy reviewers who expect a precise thesis, live objection, argument structure, and contribution to an active debate.

- **Primary move:** Rewrite the opening and transitions so the venue-level claim, evidence object, and contribution are visible before technical detail.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Philosophical Review for broader top philosophy, Nous for analytic breadth, Ethics for normative/political theory; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Reads for a broad audience?】jargon glossed / formalism explained? [Y/N]
【Thesis clear early?】[Y/N]
【Argument-first prose?】connectives explicit? [Y/N]
【Within ~8,000 words?】[Y/N] — where to trim
【Quotations purposeful + analyzed?】[Y/N]
【Next】mind-citation-and-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — typesetting (LaTeX `lineno`, Word) and reference managers
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Mind's accessibility expectation and word limit
