---
name: pnasnexus-significance
description: Use to write the PNAS Nexus Significance Statement — between 50 and 120 words, in plain language for a broad scientific audience, explaining why the work matters. Required for Research Reports and Stage 2 Registered Reports. Distinct from the abstract. One of the highest-value PNAS Nexus front-matter artifacts.
---

# Significance Statement (pnasnexus-significance)

## Why this is a flagship PNAS Nexus skill

Every PNAS Nexus **Research Report** (and **Stage 2 Registered Report**) must include a **Significance Statement** — a short, mandatory paragraph that explains, in plain language, **why the work matters to science and society**. It is read by editors at triage and by the broad, cross-disciplinary readership. It is **not** a second abstract. Getting it right is one of the highest-leverage things you can do, so draft it as soon as the central claim is locked.

## When to trigger

- The submission (Research Report / Stage 2 Registered Report) has no Significance Statement.
- The Significance Statement just restates or condenses the abstract.
- It is dense with jargon and undefined acronyms.
- It is **shorter than 50 words** or **longer than 120 words**.

## The hard rule: 50–120 words, written for a broad audience

- **Length:** **between 50 and 120 words.** PNAS Nexus states an explicit **minimum of 50** and **maximum of 120** words — so unlike a one-line summary, a too-short statement is also non-compliant. Confirm both bounds in the current PNAS Nexus author guidelines.
- **Audience:** an **educated scientist outside your field**. Write so a reader from another PNAS Nexus division (biological/health/medical, physical sciences & engineering, social & political) can follow it. (PNAS Nexus does not publish the exact flagship-PNAS "bright undergraduate" phrasing — but writing to roughly that level is a safe target.)
- **Test:** read it aloud to someone smart but not in your subfield. If they can say back *why the result matters*, it works.

## What it must do (and not do)

The Significance Statement answers **"so what, and who cares?"** — the abstract answers **"what did you do and find?"**

| Significance Statement | Abstract (`pnasnexus-abstract`) |
|------------------------|----------------------------------|
| Why it matters, for a broad reader | What/how/found, for scientists |
| Plain language, minimal jargon | Technical but accessible |
| The gap + the advance + the broader consequence | Context, methods, quantified results, conclusion |
| 50–120 words | ≤250 words |

## Template (a few short moves, no headings)

1. **The problem / gap (1–2 sentences).** What broad question or limitation does the field face? State the stakes plainly.
2. **What this work shows (1–2 sentences).** The advance, in non-technical terms — the result, not the method.
3. **Why it matters (1–2 sentences).** The consequence for the field, for other fields, or for society.
4. *(Optional)* one sentence on a concrete broader application or future direction.

> One paragraph. No citations, no figure references, no undefined acronyms, no equations. Keep it within 50–120 words.

## Worked shape

> *"[Broad phenomenon] underlies [important process], yet how [specific gap] remains unclear. Here we show that [plain-language advance], demonstrating that [general principle]. This finding [changes/explains/enables] [broad consequence], with implications for [adjacent field or application]."*

## The non-specialist rewrite drill

When a draft statement is too technical, run this pass:

1. Underline every word a researcher in another discipline would not know.
2. Replace each with a plain phrase, or cut the sentence it lives in.
3. Replace gene/protein/parameter names and acronyms with what they *do* ("a protein that controls cell division", not "CDK1").
4. Read what remains. If the "why it matters" is now gone, you were hiding it behind jargon — write it back in plainly.
5. **Check the word count is still ≥ 50** — if the cuts dropped it below the floor, add a sentence of plain consequence, not more jargon.

## Common failures (rewrite on sight)

- **Out of bounds** — under 50 or over 120 words; PNAS Nexus enforces **both** limits.
- **A restatement of the abstract** — editors notice immediately; it must be genuinely broader and plainer.
- **Too technical** — jargon, gene names, model parameters, acronyms.
- **Method-led** — leads with what you did rather than why it matters.
- **Over-claiming** — promising societal impact the data do not support (cross-check `pnasnexus-fit`).
- **No "so what"** — describes the result but never says why a non-specialist should care.

## Output format

```
【Word count】 N — within 50–120? (both bounds enforced)
【Reader test】 can a non-specialist from another division state why it matters? yes/no
【Moves present?】 gap / advance(plain) / why-it-matters / (optional) application
【Distinct from abstract?】 yes/no (if no, rewrite — not a condensed abstract)
【Jargon / acronym hits removed】 [...]
【Over-claiming check】 consequence supported by the data? (link pnasnexus-fit if not)
【Next】 pnasnexus-abstract
```

## Anti-patterns

- **Do not** copy-paste or compress the abstract into the Significance Statement.
- **Do not** write it for specialists — write it for a reader outside the field.
- **Do not** fall below 50 words or exceed 120 — PNAS Nexus enforces both.
- **Do not** lead with methods; lead with the problem and the consequence.
- **Do not** claim societal impact the evidence cannot back.
