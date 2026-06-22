---
name: mind-citation-and-style
description: Use when formatting references and applying the MIND house style to a Mind article. Mind provides a MIND Stylesheet and requires accepted papers to be prepared in its house style; line numbering is required for review. Handles citation mechanics and formatting; it does not write the argument.
---

# Citation & MIND House Style (mind-citation-and-style)

Mind has its **own house style** and supplies a downloadable **MIND Stylesheet**. A generic Chicago or
APA export is not the house style — accepted papers must be prepared in **MIND style**, and the review
copy must meet Mind's preparation rules (notably **line numbering**). This skill handles the mechanics
so formatting never becomes the reason for friction.

## When to trigger

- Setting up references at the start, to avoid a painful conversion later
- Preparing the **review copy** (line numbers, anonymization) before submission
- Converting an accepted manuscript to the **MIND house style** post-acceptance
- A referee or editor flagged inconsistent or non-house-style references

## What Mind expects

1. **MIND house style for the final version.** Download and follow the **MIND Stylesheet**. Accepted
   authors prepare the final copy in this style; do not assume your default manager output matches it.
2. **Line numbering for review.** Number the lines of the submitted document — in LaTeX via the
   `lineno` package, in Word via the line-numbering option. This is a stated requirement.
3. **Consistency from the start.** Pick one citation style and apply it uniformly (Zotero / BibTeX /
   EndNote). Even before the house-style conversion, mixed styles read as careless.
4. **Anonymized references for review.** Neutralize self-identifying citations ("in my [2021]…") so the
   review copy is prepared for **triple-anonymous** refereeing (see `mind-submission`). This is not
   optional: **papers not prepared for anonymous refereeing will not be read**.
5. **Accurate attribution.** Quote and cite precisely; every quotation has a locatable source. Misquoting
   the target view is both a scholarly and a dialectical error.

## Mechanics

- Keep a clean reference database; let the manager generate the list, then **convert to MIND style**.
- Page-cite quotations and close paraphrases of specific arguments.
- Provide alt text for any figures and declare funding (CrossRef Funder Registry) where applicable.
- Confirm the **exact current house-style details on the live Stylesheet** — formatting conventions
  change (待核实 on specifics).

## Anti-patterns

- Submitting the review copy without line numbers (a stated preparation requirement)
- Leaving self-identifying citations in a triple-anonymous review copy
- Assuming a default Chicago/APA export is the MIND house style
- Inconsistent reference formatting across the manuscript
- Quotations with no page reference, or paraphrases that misstate the source


## Citation pass for Mind

Use this as a second-pass capability check. First lock the target thesis, argument map, objection sequence, and dialectical payoff; then test whether the manuscript addresses analytic-philosophy reviewers who expect a precise thesis, live objection, argument structure, and contribution to an active debate.

- **Primary move:** Audit references and notes as evidence discipline: each source should position, document, or delimit a claim.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Philosophical Review for broader top philosophy, Nous for analytic breadth, Ethics for normative/political theory; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【House style】MIND Stylesheet followed for final copy? [Y/N]
【Line numbering】present on review copy? [Y/N]
【Consistency】one style applied throughout? [Y/N]
【Anonymized refs】self-identifying citations neutralized? [Y/N]
【Attribution】quotations page-cited and accurate? [Y/N]
【Next】mind-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, LaTeX `lineno`, the MIND Stylesheet
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — MIND house style, line-numbering, and anonymization requirements
