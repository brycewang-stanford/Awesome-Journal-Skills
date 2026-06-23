---
name: pnasnexus-abstract
description: Use to write the PNAS Nexus abstract — a single self-contained paragraph of up to 250 words, with no headings, quantified and accessible to a broad scientific audience. Distinguishes the abstract (what/how/found, for scientists) from the 50–120-word Significance Statement (why-it-matters, for everyone). Late-stage polish.
---

# Abstract (pnasnexus-abstract)

## When to trigger

- Fit, open access, structure, figures, stats, and data are settled (do this late).
- The abstract reads like a methods recap with no result.
- The abstract is being confused with, or duplicated from, the Significance Statement.
- The abstract is over 250 words, has subheadings, or is jargon-dense.

## The PNAS Nexus abstract: ≤250 words, single paragraph, no headings

- **Length:** up to **250 words** (PNAS Nexus states a 250-word maximum — confirm in current guidelines).
- **A single paragraph with no headings**, no reference citations, no figure/table callouts. (PNAS Nexus's wording: "They should appear as a single paragraph with no headings.")
- **Self-contained:** a reader who sees only the abstract should understand the question, what was done, what was found (quantified), and what it means.
- **Accessible** to the broad PNAS Nexus readership spanning biological/health/medical, physical sciences & engineering, and social & political sciences — define or avoid acronyms.

> The short, plain artifact PNAS Nexus requires is the **Significance Statement** (`pnasnexus-significance`, 50–120 words) — it is **separate** from the abstract. Do not merge them.

## Abstract vs Significance Statement (keep them distinct)

| Abstract | Significance Statement (`pnasnexus-significance`) |
|----------|----------------------------------------------------|
| **What/how/found**, for scientists | **Why it matters**, for everyone |
| ≤250 words, quantified, technical-but-clear | 50–120 words, plain language |
| Stands in for the paper | Stands in for the "so what" |

If the two read the same, the Significance Statement is wrong — fix it in `pnasnexus-significance`.

## Recommended five-move structure (no labels in the text)

1. **Context / stakes** (1–2 sentences) — the broad problem.
2. **Gap / question** (1 sentence) — what was unknown.
3. **What we did** (1–2 sentences) — approach, in plain terms.
4. **Key results, quantified** (2–3 sentences) — the advance, with numbers and uncertainty.
5. **Conclusion / implication** (1 sentence) — what it means for the field, ideally across fields.

## Hard constraints

- [ ] ≤ 250 words (confirm the current cap).
- [ ] Single paragraph, **no subheadings**, no citations, no figure/table references.
- [ ] Define any acronym on first use, or avoid it.
- [ ] At least one **quantified** result — magnitude + unit + uncertainty (CI/P), not "significantly increased".
- [ ] First sentence comprehensible to a scientist outside the field.
- [ ] Distinct in content and register from the Significance Statement.

## Jargon blacklist (rewrite on sight)

- "Herein we report…", "Importantly,", "Interestingly,", "Notably,"
- Strings of ≥2 undefined acronyms in one sentence.
- "elucidate", "delineate", "interrogate", "leverage" as filler verbs.
- Hedging stacks: "may potentially suggest that it could…".

## Output format

```
【Abstract】 single paragraph (word count: N ≤ 250)
【Single paragraph, no headings?】 yes/no
【Five moves present?】 context / gap / approach / quantified result / implication
【Quantified headline result?】 yes/no + the number
【Distinct from Significance Statement?】 yes/no
【Jargon hits removed】 [...]
【Next】 pnasnexus-citation
```

## Anti-patterns

- **Do not** reuse the 50–120-word Significance Statement as the abstract (or vice versa).
- **Do not** add subheadings — PNAS Nexus abstracts are single unstructured paragraphs.
- **Do not** open with method or organism; open with the stake.
- **Do not** end on "further work is needed" — end on the implication.
- **Do not** exceed 250 words "to be thorough".
