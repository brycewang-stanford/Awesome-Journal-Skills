---
name: nejm-writing
description: Use to structure and tighten an NEJM Original Article into terse IMRAD — short main text (~2700 words), limited references, claim-first results, and a sober discussion with explicit limitations and calibrated clinical implications. Enforces NEJM's plain, concise house style.
---

# Main-Text Writing (nejm-writing)

## When to trigger

- The main text is bloated, or you are unsure of the article type.
- The Discussion over-states the implications or omits limitations.
- The Introduction starts with a literature review instead of the clinical question.
- Methods detail belongs in the protocol/supplement, not the body.

## Article type first

- **Original Article** — definitive trials / major studies; full IMRAD; structured abstract.
- **Brief Report** — a smaller but important finding; substantially shorter; fewer items.
- **Review** — commissioned/vetted clinical synthesis (different structure).

Confirm length and reference caps against the current author guidelines. For an Original Article, design for a **short main text (often ~2700 words)** and a **limited reference list (on the order of ~40)** — NEJM is deliberately terse.

## IMRAD, the NEJM way

### Introduction (short)
Two to three paragraphs. State the clinical problem, the gap, and the specific question the study answers. End with the objective. No exhaustive background — move detail to references.

### Methods
Design, setting, participants (eligibility), intervention/comparator, randomization and blinding, outcomes (primary pre-specified, then secondary), and the statistical analysis (ITT primary; multiplicity; pre-specified subgroups). Push full procedural detail to the **protocol and supplementary appendix**; the body states what a clinician needs to judge validity. Reference the reporting guideline (CONSORT/STROBE).

### Results
**Claim-first, numbers-led.** Open with enrollment and the analysis population (tie to the CONSORT flow diagram). Report the **primary outcome with effect size + 95% CI**, then key secondary outcomes, then safety/adverse events. Do not interpret here — that is the Discussion. Tables carry the detail; text states the headline.

### Discussion
- Open with what the study found, in one or two plain sentences.
- Place it among prior evidence — without re-reviewing the field.
- State **clinical implications soberly**: what should change, for whom, and what should not.
- A dedicated **limitations** paragraph is expected (generalizability, open-label bias, follow-up duration, missing data, power).
- Do **not** over-state: avoid causal language for observational data; do not extrapolate beyond the population studied.

## NEJM house style (terse and plain)

- Short sentences; plain words; minimal hedging stacks.
- Define each abbreviation once; avoid acronym soup.
- Past tense for what was done and found; present tense for established facts.
- No "novel", "robust", "interestingly" as filler; let the numbers carry the claim.
- Active voice where it reads naturally; first-person plural is acceptable.

## Over-claiming watch (NEJM-specific)

The fastest way to lose a clinical reviewer is a Discussion that outruns the data. Match every implication sentence to the strength of the design: a single trial supports a conclusion in its population, not a universal recommendation. Surrogate outcomes do not license patient-outcome claims.

## A word budget that fits ~2700

A workable allocation — a craft split, not a journal rule: Introduction ≈300–400 words; Methods ≈700–800 (detail pushed to protocol/appendix); Results ≈800–900; Discussion ≈600–700 including limitations. Cut inside the overrunning section first; the Discussion compresses, the Results rarely do.

## Worked micro-example — one Results sentence (before → after)

- Before: "Interestingly, the novel agent produced a robust, statistically significant improvement in the primary endpoint (P<0.05), suggesting a transformative role."
- After: "A primary-outcome event occurred in 98 of 1204 patients (8.1%) in the intervention group and in 134 of 1198 (11.2%) in the control group (hazard ratio, 0.71; 95% CI, 0.55 to 0.92)."

The rewrite deletes filler, evicts interpretation to the Discussion, and replaces a bare P with counts, percentages, and an effect estimate with CI. (Numbers invented.)

## Tightening moves that survive editing

- Convert "there was a significant difference in X between the groups" into "X was lower with A than with B (estimate; 95% CI)".
- Delete throat-clearing openers ("It is important to note that…") — the sentence that follows stands alone.

## Output format

```
【Article type】 Original Article / Brief Report / Review
【Main-text length】 N words vs target (~2700 for Original Article) → ok / over
【Reference count】 N vs ~40 cap → ok / over
【IMRAD check】 intro=question? methods→protocol? results claim-first+CI? discussion sober?
【Limitations paragraph present】 yes/no
【Over-claiming flags】 [...] (causal language / extrapolation / surrogate→outcome)
【Next】 nejm-statistics
```

## Anti-patterns

- **Do not** pad the Introduction into a mini-review — state the question and stop.
- **Do not** keep full procedural detail in the body when it belongs in the protocol/supplement.
- **Do not** interpret results inside the Results section.
- **Do not** omit the limitations paragraph or soften it into a throwaway sentence.
- **Do not** let the Discussion recommend practice changes the single study cannot support.
