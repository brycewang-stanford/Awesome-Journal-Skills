---
name: qje-writing-style
description: Use when polishing prose, abstract, and introduction for a Quarterly Journal of Economics (QJE) manuscript so the big idea lands fast for a general-interest reader. Reflects QJE's house style — long, ambitious, narrative-driven empirical papers. Polishes exposition; it does not change results or design.
---

# Writing Style (qje-writing-style)

## When to trigger

- The prose buries the idea; a reader cannot find the contribution quickly
- The abstract does not state the finding, or leads with method
- The introduction wanders before reaching the question and the result
- Sentences are technical-jargon-dense for a general-interest audience

## QJE house style: ambitious, narrative, long

QJE is read across all of economics, and its papers are characteristically **long, narrative-driven, and ambitious** — there is **no hard page limit**, and an extensive online appendix is the norm. That freedom is a trap: the *body* must still make a **big idea legible to a smart non-specialist** in the first two pages, with the heavy machinery pushed to the appendix. The model is the canonical QJE empirical-micro paper (e.g., Chetty, Hendren, Kline & Saez on mobility, QJE 2014): a sharp question stated plainly, a clean source of variation, a memorable headline number, and a broad lesson — all before the reader hits the data section. Format facts that shape the writing: the **abstract is short (~150 words)**, citations are **author-date (Chicago)**, and double-blind review means the prose must not out the authors. Late-stage skill: only polish once identification and results are settled.

## The introduction arc (QJE template)

1. **The question** — one or two sentences, plain language, stakes clear.
2. **Why it is hard** — the identification problem that has blocked a clean answer.
3. **The setting & variation** — the natural experiment / data that solves it, in one paragraph.
4. **The headline result** — the number, with units, stated early and memorably.
5. **Interpretation & mechanism** — what it means; the conceptual frame in a sentence.
6. **Contribution & broad lesson** — placement in the literature + "beyond this setting."
7. **Roadmap** — brief; do not over-signpost.

## Abstract: state the finding (hard cap 250 words; aim shorter)

- Open with the question and the design in one breath, then **state the result with a number**.
- Close with the broad lesson. No throat-clearing, no "this paper studies the important issue of."
- QJE's official cap is **no more than 250 words**, with no reference citations and the JEL codes at the end of the abstract; a tight ~150-word abstract usually reads best. A general-interest reader should know what you found from the abstract alone.

## Sentence-level craft

- Active voice; short declaratives for the key claims.
- Define notation once; do not make the reader hold five symbols to parse a sentence.
- Quantify ("raises earnings by 8%") rather than vague intensifiers ("substantially affects").
- Hedge only where the evidence requires it; calibrated confidence reads as competence.
- The license to write long is not a license to wander — every long stretch should earn its place, with technical detail relocated to the online appendix.

## Checklist

- [ ] Abstract states the actual finding with a number, not just the topic, is ≤250 words (ideally ~150), and cites no references
- [ ] The question is on page one in plain language
- [ ] The headline result appears early in the introduction, with units
- [ ] The broad lesson ("beyond this setting") is explicit
- [ ] Jargon minimized; a non-specialist top-5 reader can follow the intro
- [ ] Claims are quantified, not vaguely intensified
- [ ] Author-date (Chicago) citations; numbers and units consistent throughout

## Anti-patterns

- An abstract that describes the topic but never states the result (or runs past the 250-word cap)
- Leading the intro with method ("We use a Sun–Abraham estimator ...") instead of the question
- "This paper is the first to study the important question of ..." throat-clearing
- Using QJE's no-page-limit freedom to ramble instead of relocating detail to the appendix
- Vague magnitude language ("significantly", "substantially") with no number
- Notation overload in the introduction

## Output format

```
【Abstract verdict】states finding+number, ≤250 words (ideally ~150)? [Y/N] — fix: ...
【Intro arc】question / hardness / variation / result / interpretation / contribution present? [Y/N each]
【Headline number in intro】present + units? [Y/N]
【Broad lesson stated】[Y/N]
【Jargon flags】[...]
【Next step】qje-replication-package or qje-referee-strategy
```
