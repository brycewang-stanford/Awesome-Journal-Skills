---
name: sci-abstract
description: Use when writing the two front-matter artifacts Science (AAAS) demands — the one-sentence summary for the table of contents and the ≤125-word single-paragraph abstract — both readable by any scientist and both leading with the quantified advance rather than the method. Late-stage polish skill for the flagship AAAS weekly.
---

# Abstract & One-Sentence Summary (sci-abstract)

## When to trigger

- Significance, framing, and format are settled (do this late).
- The abstract reads like a method recap with no result.
- There is no one-sentence summary, or it restates the title.
- The abstract exceeds ~125 words or is dense with jargon/acronyms.

## Two distinct artifacts Science requires

### 1. One-sentence summary (≤ ~125 characters)

A single declarative sentence for the table of contents and editors. It is **not** the title and **not** the first line of the abstract.

- States the finding and its general point.
- No undefined acronyms; readable by any scientist.
- Active voice. Example shape: "A single mutation rewires metabolism, explaining cold tolerance across insects."

### 2. Abstract (≈ 100–125 words, unstructured prose)

Science abstracts are short, single-paragraph, **no subheadings**. Target the educated general scientist, not the subfield.

Recommended five-move structure (no labels in the text):

1. **Context / stakes** (1 sentence) — the broad problem.
2. **Gap / question** (1 sentence) — what was unknown.
3. **What we did** (1 sentence) — approach, in plain terms.
4. **Key result, quantified** (1–2 sentences) — the advance, with numbers.
5. **Implication** (1 sentence) — why a broad community should care.

## Hard constraints

- [ ] ≤ ~125 words (check the current author guidelines for the exact cap; treat 125 as the ceiling).
- [ ] No subheadings, no citations, no figure/table references in the abstract.
- [ ] Define any acronym on first use, or avoid it.
- [ ] At least one **quantified** result — not "significantly increased" but "increased 2.4-fold (P < 0.001)".
- [ ] First sentence is comprehensible to a scientist outside the field.

## Jargon blacklist (rewrite on sight)

- "Herein we report…", "Importantly,", "Interestingly,", "Notably,"
- Strings of ≥2 undefined acronyms in one sentence.
- "elucidate", "delineate", "interrogate", "leverage" as filler verbs.
- Hedging stacks: "may potentially suggest that it could…".

## Quantification check

Every claim of effect must carry a number somewhere in the paper, and the headline effect should be in the abstract: magnitude + unit + uncertainty (CI or P). If the abstract has zero numbers, it is not finished.

## What the editorial board reads first

Because Science triages most submissions in-house before any referee sees them, your one-sentence summary and abstract are frequently the *only* prose a professional editor reads before deciding to read further. Calibrate to that reality:

| Editor's silent question | Where they look | What kills it |
|--------------------------|-----------------|---------------|
| "Would our general readership care?" | one-sentence summary | a subfield claim only specialists parse |
| "Is there a result, or just an approach?" | abstract sentences 3–4 | method recap with no quantified finding |
| "Is this overstated?" | abstract last sentence | an implication asserted, not demonstrated |
| "Can I send this summary to a referee verbatim?" | the whole summary | undefined acronyms, hedging stacks |

The abstract is one unstructured paragraph — unlike a structured clinical abstract (Background/Methods/Results/Conclusions). Do not import a NEJM/JAMA structured-abstract template; Science runs continuous prose with no labels.

## Worked micro-example (illustrative)

A team finds that a single gut bacterium's enzyme degrades a common drug, explaining why some patients respond and others do not. Walk the moves (numbers illustrative only):

- **One-sentence summary** (≈110 chars): "A single gut-microbial enzyme inactivates a widely used drug, explaining variable patient response."
- **Abstract** (≈120 words, prose): *Stake* — drug response varies unpredictably between patients. *Gap* — the gut microbiome was suspected but no mechanism was known. *Approach* — we screened 412 isolates and reconstituted the activity in vitro. *Result* — one enzyme reduced active-drug levels by 73% (95% CI 65–80%; P < 0.001), and its abundance predicted response in a 96-patient cohort (AUC 0.84). *Implication* — microbial enzymology may be a general, modifiable axis of drug variability.

Notice: the headline number (73%, CI, P) sits in the abstract, not buried in a figure; the last sentence reaches a broad audience (pharmacology, microbiology, clinical medicine) without claiming proof of causation in humans.

## Referee and editor pushback patterns

| Pushback you will hear | The Science-specific fix |
|------------------------|--------------------------|
| "The summary just restates the title." | Make it state the *consequence*, not the topic — the lesson a non-specialist takes away. |
| "I read the abstract and still don't know the result." | Put the quantified headline (magnitude + uncertainty) in sentences 4–5; delete one context sentence to fit. |
| "Reads like an abstract for a specialist journal." | Replace the field-internal opener with the broad stake; cut acronym chains. |
| "The last line over-claims." | Hedge to what the data show; "may be a general axis" not "is the cause" — confirm the claim survives `sci-fit`. |

## Calibration anchors (confirm against current author guidelines)

- One-sentence summary: target ≤ ~125 characters; it is a distinct required field, not the first abstract line.
- Abstract: target ≤ ~125 words, single paragraph, no subheadings, no citations, no figure references.
- Exactly one paragraph — the convention is firm even as the word ceiling may shift; verify the current cap.
- At least one quantified headline effect with uncertainty; zero-number abstracts are unfinished.

## Output format

```
【One-sentence summary】 "..." (char count: N ≤ 125)
【Abstract】 single paragraph (word count: N ≤ 125)
【Five moves present?】 context / gap / approach / quantified result / implication
【Quantified headline result?】 yes/no + the number
【Jargon hits removed】 [...]
【Next】 sci-citation
```

## Anti-patterns

- **Do not** make the one-sentence summary a paraphrase of the title.
- **Do not** open the abstract with method or organism; open with the stake.
- **Do not** end on "further work is needed" — end on the implication.
- **Do not** pad to sound comprehensive; the cap is a feature.
