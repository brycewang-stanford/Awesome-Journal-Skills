---
name: jfqa-writing-style
description: Apply the house writing style for a Journal of Financial and Quantitative Analysis (JFQA) manuscript — precise quantitative finance prose, the strict ≤100-word one-paragraph abstract, and the prescriptive 8.5x11 / 1-inch / 12-pt Times New Roman double-spaced layout submitted as a text-searchable PDF. Use to polish a draft to JFQA conventions before submission.
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

## Output format

```
【Prose】result-forward, magnitudes in finance units? [Y/N]
【Abstract】≤100 words, one paragraph? [Y/N]
【Formatting】8.5x11 / 1-in / 12-pt TNR / double-spaced / searchable PDF? [Y/N]
【Anonymized】body + metadata clean? [Y/N]
【Next step】jfqa-replication-and-data-policy
```
