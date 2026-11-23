---
name: pnas-significance
description: Use to write the mandatory PNAS Significance Statement — ≤120 words, written so an educated reader outside the field (down to an undergraduate) understands why the work matters. Distinct from the abstract. The highest-value PNAS-specific artifact.
---

# Significance Statement (pnas-significance)

## Why this is a flagship PNAS skill

Every PNAS research article must include a **Significance Statement** — a short, mandatory, separately submitted paragraph that explains, in plain language, **why the work matters to science and society**. It appears prominently with the article and is read by editors at triage and by the broad readership. It is **not** a second abstract. Getting it right is one of the highest-leverage things you can do for a PNAS submission, so draft it as soon as the central claim is locked — do not leave it to the final upload.

## When to trigger

- The submission has no Significance Statement.
- The Significance Statement just restates or condenses the abstract.
- It is dense with jargon and undefined acronyms.
- It exceeds ~120 words.

## The hard rule: ≤120 words, written for a non-specialist

- **Length:** **≤ 120 words and at least 50 words**, with no references (PNAS main-manuscript template, re-checked 2026-11-23; treat 120 as the ceiling).
- **Audience:** an **educated scientist outside your field — down to a bright undergraduate**. If a chemistry undergraduate or a non-specialist colleague cannot follow it, rewrite it.
- **Test:** read it aloud to someone who is smart but not in your subfield. If they can say back *why the result matters*, it works.

## What it must do (and not do)

The Significance Statement answers **"so what, and who cares?"** — the abstract answers **"what did you do and find?"**

| Significance Statement | Abstract (`pnas-abstract`) |
|------------------------|----------------------------|
| Why it matters, for a broad reader | What/how/found, for scientists |
| Plain language, minimal jargon | Technical but accessible |
| The gap + the advance + the broader consequence | Context, methods, quantified results, conclusion |
| ≤120 words | ~250 words |

## Template (four short moves, no headings)

1. **The problem / gap (1–2 sentences).** What broad question or limitation does the field face? State the stakes plainly.
2. **What this work shows (1–2 sentences).** The advance, in non-technical terms — the result, not the method.
3. **Why it matters (1–2 sentences).** The consequence for the field, for other fields, or for society — what changes because of this.
4. *(Optional)* one sentence on broader application or future direction, only if it is concrete.

> Keep it to one paragraph. No citations, no figure references, no undefined acronyms, no equations.

## Worked shape

> *"[Broad phenomenon] underlies [important process], yet how [specific gap] has remained unclear. Here we show that [plain-language advance], demonstrating that [general principle]. This finding [changes/explains/enables] [broad consequence], with implications for [adjacent field or application]."*

## The undergraduate rewrite drill

When a draft statement is too technical, run this pass:

1. Underline every word a second-year undergraduate in another discipline would not know.
2. For each, replace it with a plain phrase, or cut the sentence it lives in.
3. Replace gene/protein/parameter names and acronyms with what they *do* ("a protein that controls cell division" not "CDK1").
4. Read what remains. If the "why it matters" is now gone, you were hiding it behind jargon — write it back in plainly.

> The cap is short (≤120 words) precisely to force this. You are not summarizing the paper; you are answering "why should a non-specialist care?"

## Common failures (rewrite on sight)

- **Too technical** — full of jargon, gene names, model parameters, or acronyms.
- **A restatement of the abstract** — reviewers and editors notice immediately; it must be genuinely broader and plainer.
- **Method-led** — leads with what you did rather than why it matters.
- **Over-claiming** — promising societal impact the data do not support (cross-check `pnas-fit`).
- **Over length** — anything past ~120 words signals the author did not engage with the genre.
- **No "so what"** — describes the result but never says why a non-specialist should care.

## Output format

```
【Word count】 N ≤ 120
【Reader test】 can a non-specialist / undergraduate state why it matters? yes/no
【Four moves present?】 gap / advance(plain) / why-it-matters / (optional) application
【Distinct from abstract?】 yes/no (if no, rewrite — not a condensed abstract)
【Jargon / acronym hits removed】 [...]
【Over-claiming check】 consequence supported by the data? (link pnas-fit if not)
【Next】 pnas-abstract
```

## Anti-patterns

- **Do not** copy-paste or compress the abstract into the Significance Statement.
- **Do not** write it for specialists — write it for a smart reader outside the field.
- **Do not** exceed ~120 words "to be thorough"; the cap is the point.
- **Do not** lead with methods; lead with the problem and the consequence.
- **Do not** claim societal impact the evidence cannot back.
