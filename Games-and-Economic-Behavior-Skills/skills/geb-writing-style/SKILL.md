---
name: geb-writing-style
description: Use when polishing prose, abstract, and introduction for a Games and Economic Behavior (GEB) manuscript so the model and result land for a general game-theory reader. Enforces the 250-word abstract cap and elsarticle conventions. Polishes exposition; it does not change results.
---

# Writing Style (geb-writing-style)

## When to trigger

- The introduction reaches the theorem only after pages of setup and notation
- The abstract is over 250 words, or states the model but not the result
- The proof idea is invisible behind algebra
- Prose is dense even for a specialist game-theory reader

## GEB house style: precise, idea-first, specialist-but-broad

GEB is read across the game-theory community — economics, political science, biology, computer science, mathematics, and psychology — so the writing must be **rigorous yet legible beyond one sub-field**. Lead with the idea and the result; push heavy algebra into proofs and appendices. State theorems precisely but motivate them in words first. The reader is a game theorist, so you can assume the vocabulary of equilibrium and mechanisms, but not the details of your specific construction.

Format facts that shape the writing:

- **Abstract must not exceed 250 words** — concise and factual; state the contribution and the main result, not just the topic.
- **References:** no strict style is imposed at submission as long as it is **consistent**; the published style is **elsarticle-num**. (Avoid mixing styles.)
- **Generative-AI use** must be disclosed in a section titled *"Declaration of generative AI and AI-assisted technologies..."* (待核实 — Elsevier uses both "...in the writing process" and "...in the manuscript preparation process"; copy the exact heading from the live Guide for Authors), placed **before the reference list** (basic grammar/spell tools exempt) — keep the prose your own and the declaration accurate.
- This is a **late-stage** skill: polish only once theorems, assumptions, and (if any) experiments are settled.

## The introduction arc (GEB template)

1. **The question / phenomenon** — the strategic problem, in plain terms.
2. **Why it was open** — what prior solution concepts or results could not deliver.
3. **The result** — state the main theorem/finding early, in words, then formally.
4. **The key idea** — the one move (construction, mechanism, design) that makes it work.
5. **Scope & relation to the literature** — generality and the delta against the nearest result.
6. **Roadmap** — brief.

## Abstract: state the result (≤250 words)

- Open with the setting and the question, then **state the main result** — the theorem, the mechanism, or the experimental finding.
- Name the advance ("we characterize", "we prove existence", "we show equilibrium play converges to ...").
- No throat-clearing; a game theorist should know what you proved from the abstract alone. Keep it under the 250-word cap.

## Sentence-level craft

- Define notation once; do not force the reader to hold many symbols to parse a sentence.
- Active voice; short declaratives for theorem statements and key claims.
- Motivate before formalizing; give the proof's idea before its steps.
- Calibrated claims — say exactly how general the result is, no more.

## Anti-patterns

- An abstract over 250 words, or one that states the model but never the result
- Opening the intro with notation and assumptions instead of the question and result
- A proof with no stated idea, only symbols
- Mixed/inconsistent reference styles
- Forgetting the generative-AI declaration when AI tools were used

## Output format

```
【Abstract】states the result + ≤250 words? [Y/N] — fix: ...
【Intro arc】question / why-open / result / key idea / scope present? [Y/N each]
【Result stated early】in words then formally? [Y/N]
【References】consistent (elsarticle-num target)? [Y/N]
【AI declaration】needed? present + placed before references? [Y/N / NA]
【Next step】geb-replication-and-data-policy or geb-review-process
```
