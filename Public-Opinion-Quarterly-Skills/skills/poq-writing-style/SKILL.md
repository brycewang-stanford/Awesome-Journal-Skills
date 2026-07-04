---
name: poq-writing-style
description: Use when drafting or polishing a Public Opinion Quarterly (POQ) manuscript so it reads for a public-opinion and survey-methodology audience and fits the type caps (Original Article ≤ 6,500 words of text and notes; Research Note < 3,000; Polls in Context ≤ 2,500). POQ word counts cover text and notes but exclude figures, tables, references, and appendices. Tightens prose and format; it does not invent content.
---

# Writing Style (poq-writing-style)

A POQ paper must be readable by both substantive opinion scholars and survey methodologists, and
disciplined to the cap for its type. The word count covers **text and notes** but **excludes figures,
tables, references, and appendices** — so the AAPOR disclosure appendix and exhibits do not count
against you. This skill is about reaching the POQ audience and respecting format — not generating claims.

## When to trigger

- Drafting the introduction, framing the contribution, or final polish
- Over the word cap and needing to cut without losing the argument
- Writing the abstract (confirm the current requirement — 待核实 on exact cap)
- Aligning citations and format before submission

## Reach the POQ audience

1. **Front-load the contribution.** By the end of the introduction the reader knows the question, the
   data, the finding, and whether the contribution is to **opinion theory, current opinion, or survey
   validity**. Do not bury the "so what."
2. **Name the methodological move plainly.** State the survey design and the error source you address;
   POQ readers expect to see coverage/nonresponse/wording/mode/weighting handled, not glossed.
3. **Define jargon on first use.** A communication scholar should follow a methods paper and vice
   versa; spell out acronyms (AAPOR, TSE, RR, DEFF, AMCE, MRP) on first appearance.
4. **Argument-first prose.** Lead with claims; use design-based evidence to support them. Avoid "the
   data show…" without saying what they show and why it matters.

## Format & front matter

- **Citations**: keep one consistent reference style (manage with Zotero/BibTeX); references excluded
  from the word count.
- **Disclosure**: ensure the **"Appendix A: Disclosure Elements"** is present and referenced (see
  `poq-survey-design-and-measurement`); it does not count toward the cap.
- **Anonymize**: POQ is **double-blind** — no author names/affiliations/acknowledgments in the
  manuscript, no obvious self-references, strip identifying file metadata.
- **Data Availability Statement**: plan the DAS for the endmatter (see `poq-transparency-and-data-policy`).

## Fit the type cap (text + notes; excludes figures, tables, references, appendices)

- Move detailed methods, full specifications, and extended robustness to **appendices** (excluded).
- Cut throat-clearing and literature dumps; engage the debate, not every paper (see
  `poq-literature-positioning`).
- Tighten footnotes — they **count** toward the limit (notes are in the cap).
- Prefer one decisive trend figure to three redundant tables.

## Micro-rewrites in the POQ register

- **Claim-first, not data-first.** *Before:* "The data show significant differences across
  demographic groups (p < .05)." → *After:* "Partisanship, not education, drives the gap: the
  partisan difference is 23 points versus 4 points across education levels." POQ readers want the
  substantive magnitude, then the inference.
- **Name the error source, don't gesture.** *Before:* "We account for potential survey biases." →
  *After:* "Because the panel under-covers non-internet households, we benchmark against the CPS and
  weight on the coverage-related variables." A survey scientist can now evaluate the fix.
- **Un-bury the contribution.** *Before:* an intro that spends four paragraphs on the history of
  polarization research. → *After:* paragraph two ends with "We show that item wording, not true
  attitude change, produced the apparent trend — a measurement contribution." State the lane
  (opinion theory / current opinion / survey validity) in the intro, in those terms.

Two referee tics worth pre-empting: POQ methodologists flag any inference language ("significant,"
"effect") that outruns the design (cross-sectional, nonprobability), and substantive referees flag
acronym walls — one undefined DEFF or AMCE in the intro reads as writing for insiders only.

## Anti-patterns

- An intro that never states whether the contribution is to opinion or to survey methods
- Burying the methodological move (how error was handled) deep in the paper
- Padding a Research Note (< 3,000) or Polls in Context (≤ 2,500) toward Article length
- Acknowledgments or self-references that break double-blind anonymity
- Putting disclosable methods in long footnotes (which count) instead of Appendix A (which does not)

## Output format

```
【Contribution stated by end of intro?】opinion / current-opinion / survey-validity [Y/N]
【Methodological move named?】error source + design plain? [Y/N]
【Abstract】present + within current requirement (待核实)
【Word count】Article ≤6,500 / Note <3,000 / Polls ≤2,500 (text + notes)?
【Anonymized + DAS planned + Appendix A referenced】[Y/N]
【Next】poq-transparency-and-data-policy
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers and writing tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — type caps, what the word count includes, double-blind anonymity
