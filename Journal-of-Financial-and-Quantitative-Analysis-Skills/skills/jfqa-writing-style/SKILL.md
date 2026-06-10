---
name: jfqa-writing-style
description: Use when applying the house writing style for a Journal of Financial and Quantitative Analysis (JFQA) manuscript — precise quantitative finance prose, the strict ≤100-word one-paragraph abstract, and the prescriptive 8.5x11 / 1-inch / 12-pt Times New Roman double-spaced layout submitted as a text-searchable PDF. Use to polish a draft to JFQA conventions before submission.
---

# JFQA Writing Style (jfqa-writing-style)

Use this skill to bring a **JFQA** draft up to house style. JFQA is a quantitative finance journal; the prose should be precise, economical, and result-forward.

## Voice and structure

- Write for a **finance audience** — assume fluency in asset pricing and corporate finance, but state the economic intuition behind every result.
- Lead each section with its point; report **economic magnitudes** in plain finance units (bps, monthly alpha, percentage of a SD).
- Avoid over-claiming: conclusions must not exceed what the design supports.
- Keep the paper from drifting over-long — JFQA discourages excessive length and may desk-reject it.

## The abstract and formatting (JFQA-specific, enforced)

- **Abstract**: one paragraph, **no more than 100 words** (see jfqa-contribution-framing). This is a hard cap; trim ruthlessly.
- **Layout**: 8.5 × 11 paper, **1-inch margins**, **12-pt Times New Roman**, **double-spaced** body and appendices.
- Submit a single **text-searchable PDF** (not image-only).
- **Anonymize** for double-anonymous review: remove author names, affiliations, acknowledgments, and identifying self-references; scrub PDF metadata.
- No specific named citation style (APA/Chicago) is mandated at initial submission (待核实); accepted papers follow the JFQA "Style Guide for Accepted and Conditionally Accepted Papers." Keep references internally consistent now.

## Anti-patterns

- An abstract over 100 words or in multiple paragraphs.
- Single-spacing, non-TNR fonts, or wrong margins (formatting strikes).
- Author identity left in the text or PDF metadata under double-anonymous review.
- Significance language with no economic magnitude.

## Sentence-level repair rules

- Replace "is associated with" with the design language the paper can defend: predicts, prices, shifts,
  identifies, bounds, or correlates.
- Attach a finance unit to every main result: basis points, abnormal return, spread, leverage ratio,
  turnover, default probability, or dollar value.
- Put the sample and design before the headline number when selection is the likely referee attack.
- Cut any sentence that would still be true in a generic economics journal; JFQA prose should sound like
  finance, not a methods placeholder.

## Before/after rewrites from a hypothetical corporate-finance draft (numbers illustrative)

| Before | After (JFQA register) |
|---|---|
| "Leverage is significantly associated with investment." | "A one-SD increase in book leverage predicts a 1.4 pp lower investment rate, 11% of its mean." |
| "We find strong evidence consistent with our hypothesis." | "Spreads widen 18 bps in the quarter the covenant binds, and only for firms near the threshold — the pattern the collateral channel predicts." |
| "Results are robust to a battery of checks." | "The estimate moves between 1.2 and 1.6 pp across alternative samples, definitions, and clustering (Table IA.2)." |
| "This paper contributes to several literatures." | "We revise the documented buyback effect downward by half once institutional crowding is measured." |

The pattern in every rewrite: a finance unit, a scaling benchmark, and a checkable location replace adjectives.

## Length and section calibration for a JFQA draft

- Introduction: typically four to six double-spaced pages carrying the question, the answer with numbers, the design preview, and the rival contrast — there is no codified rule, so calibrate to recent JFQA issues and confirm against the journal's current author guidelines before relying on any limit.
- Data and variable construction come before results, with the sample-construction detail that lets a referee reconstruct the filters.
- Robustness that repeats the main table's message belongs in an Internet Appendix; remember the journal's stated impatience with over-long manuscripts.

## Consistency sweep before the PDF freezes

- One name per variable everywhere — text, equations, table headers, and the archive read-me; "BLEV," "book leverage," and "leverage ratio" must not coexist.
- Numbers quoted in prose must match the exhibits to the digit; regenerate prose numbers from the master script output rather than retyping them.
- Verb tense discipline: results in the present tense, sample construction in the past, uniformly.
- Re-run the anonymization pass after the consistency sweep, since late edits are where acknowledgments and identifying phrases sneak back in.

## Output format

```
【Prose】result-forward, magnitudes in finance units? [Y/N]
【Abstract】≤100 words, one paragraph? [Y/N]
【Formatting】8.5x11 / 1-in / 12-pt TNR / double-spaced / searchable PDF? [Y/N]
【Anonymized】body + metadata clean? [Y/N]
【Next step】jfqa-replication-and-data-policy
```
