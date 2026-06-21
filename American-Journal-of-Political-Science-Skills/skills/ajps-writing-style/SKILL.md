---
name: ajps-writing-style
description: Use when drafting or polishing an American Journal of Political Science (AJPS) manuscript so it fits the word caps (Articles <= 10,000 words; Research Notes and Correspondence <= 4,000; abstract <= 150 words), follows the APSA Style Manual or Chicago 18th edition, and stays fully anonymized for double-blind review. Tightens prose and format; it does not invent content.
---

# Writing Style (ajps-writing-style)

An AJPS paper must be tightly argued, formatted to one accepted style, disciplined to the word cap, and
**fully anonymized** for double-blind review. This skill is about clarity, format, and the AJPS-specific
counting rules — not about generating claims.

## When to trigger

- Drafting the introduction, framing the contribution, or final polish
- Over the word cap and needing to cut without losing the argument
- Writing the **<= 150-word abstract**
- Aligning citations/format to APSA or Chicago style before submission

## Write tight and lead with the contribution

1. **Front-load the contribution.** By the end of the introduction the reader knows the question, the
   argument, the design, the finding, and why it matters. Do not bury the "so what."
2. **Argument-first prose.** Lead with claims; use evidence to support them. Avoid "the data show..."
   without saying what they show and why it matters.
3. **Reach a broad readership.** AJPS spans subfields; define niche jargon on first use and spell out
   acronyms.
4. **Signpost.** Clear section structure so a reader can navigate the argument.

## Format and the AJPS word-count rule

- **Style**: **APSA Style Manual for Political Science** (rev. 2018, updated 2023) **or** **Chicago
  Manual of Style (18th ed.)** — pick one and apply it consistently; references use authors' **full
  first and last names**. Double-spaced, 12-point, >= one-inch margins.
- **Abstract**: **<= 150 words**, covering background, hypotheses, methodological approach, findings,
  and conclusions.
- **Word count** (put it on the title page along with the abstract): **includes** the main body, notes,
  parenthetical references, print appendices, and **table/figure headers and notes**; **excludes** the
  title page, abstract, reference list, online Supporting Information, and mathematical notation.
  - Articles **<= 10,000**; Research Notes and Correspondence **<= 4,000**.

## Stay double-blind in the prose

- No author names, affiliations, **acknowledgments, funding statements, or conference mentions** in the
  manuscript.
- **Third-person self-citation** only — never "as we showed" / "in our prior work."
- Put the abstract and word count on the title page; the manuscript file itself stays anonymous.

## Fit the word cap

- Move balance tables, full specs, and extended robustness to the **Supporting Information** (<= 25 pp for original submissions).
- Tighten footnotes and exhibit notes — they count toward the limit.
- Cut throat-clearing and the literature dump; engage the debate, not every paper (see
  `ajps-literature-positioning`).

## Word-budget triage table (where to cut first at AJPS)

| If over the cap... | Cut/move here first | Why it works at AJPS |
|--------------------|---------------------|----------------------|
| Long literature section | Engage the debate, drop the citation pile | Generalist readership wants the argument, not a survey |
| Robustness grids in body | Move to SI (<= 25 pp for original submissions) | SI is excluded from the word count |
| Bloated exhibit notes / throat-clearing intro | Tighten notes; front-load the contribution | Headers and notes count; reviewers reward an early "so what" |

## Worked micro-example (illustrative)

A first draft runs 11,300 words against the 10,000 cap for an Article *(illustrative)*. The fix: a
three-paragraph literature dump collapses into one debate-framing paragraph (-600), two robustness tables
move to the SI (-500), and footnotes tighten (-200). The intro is rewritten so its last sentence gives the
reader the question, design, finding, and stakes. A self-cite "as we showed in 2021" becomes a third-person
citation. Final body lands near 9,900 words, abstract at 138 *(illustrative)*.

## Referee-pushback patterns and the venue-specific fix

- *"The contribution is buried."* -> State the question, argument, design, and finding by the end of the
  introduction; AJPS reviewers expect the payoff up front.
- *"References mix styles / use last-name-plus-initial."* -> Pick APSA or Chicago 18th and apply it
  consistently with full first and last names; spell out acronyms for the cross-subfield AJPS audience.

Calibration anchor: AJPS caps Articles at 10,000 words and the abstract at 150, counting notes and exhibit
captions but excluding the reference list and online SI; confirm the exact caps and accepted style against
the journal's current guidelines.

## Anti-patterns

- An abstract over 150 words or one that hides the finding
- Burying the contribution in the middle of the paper
- Mixing APSA and Chicago styles, or last-name-plus-initial references
- Acknowledgments, funding lines, or first-person self-references that break anonymity
- Letting exhibit notes and footnotes silently push the paper over the cap

## Output format

```
【Contribution stated by end of intro?】[Y/N]
【Abstract】word count (<=150), states finding?
【Word count】Article <=10,000 / Note|Correspondence <=4,000 (incl. notes + table/figure captions)?
【Style】APSA or Chicago 18th, applied consistently? full names in refs?
【Anonymized】no names/affiliations/acknowledgments/funding; third-person self-cites? [Y/N]
【Next】ajps-replication-and-verification
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — word/abstract caps, APSA-or-Chicago style, anonymizing rules
