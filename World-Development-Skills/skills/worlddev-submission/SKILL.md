---
name: worlddev-submission
description: Use when running the final pre-submission preflight for World Development (WD) via Elsevier Editorial Manager — double-anonymized formatting, abstract/keyword limits, declarations, data statement, and house style. Final checks; it does not draft content.
---

# Submission Preflight (worlddev-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to Elsevier Editorial Manager
- Unsure which files and declarations the WD submission requires
- Confirming the manuscript is correctly anonymized for double-anonymized review
- Confirming abstract, keywords, and structure meet WD/Elsevier requirements

## Process facts (检索于 2026-06；以官网为准)

- WD is **Elsevier's** multidisciplinary development-studies journal (ISSN 0305-750X; online 1873-5991), founded 1973, published monthly. Submission is through **Elsevier Editorial Manager** (verify the live link). Co-Editors-in-Chief (verified 2026-06-22): **Jampel Dell'Angelo and Angelika Rettberg** — Arun Agrawal (EiC 2013–2021) has since stepped down. Re-confirm on the live journal page before naming an editor.
- **Review model: double-anonymized.** Author and reviewer identities are mutually concealed — this drives the anonymization requirements below.
- **Abstract ≤250 words**, single unstructured paragraph; **3–6 keywords** in English; abstract must stand alone (no undefined abbreviations, no in-text references).
- **Article length / word limit: 待核实.** WD full articles are substantial; confirm the current maximum on the live Guide for Authors before relying on any number — do not assume a short limit borrowed from a sibling title.
- **"Your Paper Your Way":** initial submission formatting is flexible (single file, references in any consistent style accepted at first round); strict Elsevier reference formatting is applied at revision/acceptance. Re-verify.
- **Open-access option** available (APC) alongside the subscription route; exact fees and waivers (e.g., Research4Life country waivers) are **待核实**.
- **Declarations** expected per Elsevier policy: declaration of competing interests, funding sources, CRediT author-contribution statement, data-availability statement, and ethics/consent approval for human-subjects research.

## Preflight checklist

### Anonymization (double-blind — do this first)
- [ ] Title page with author names/affiliations is a **separate file**; the manuscript itself is identity-free
- [ ] No "in our previous work" / self-citations phrased to unmask; third-person where unavoidable
- [ ] Acknowledgments, funding IDs, and identifying local-institution names removed from the blinded file
- [ ] Data-availability statement is **review-safe** (no identifying repository URL until acceptance)
- [ ] File metadata / properties scrubbed of author name

### Format & style
- [ ] Abstract **≤250 words**, single paragraph, stands alone; **3–6 keywords**
- [ ] No significance asterisks; standard errors / confidence intervals reported in exhibits
- [ ] Tables and figures legible at print size; grayscale- and color-blind-safe; maps clearly classified
- [ ] Effect sizes in interpretable, development-relevant units
- [ ] References in a single consistent style (Elsevier formatting can wait for revision); confirm length against live limit (待核实)

### Files & declarations for Editorial Manager
- [ ] Blinded main manuscript + separate title page
- [ ] Cover letter: development contribution, fit for WD (not JDE/WBER/JDS/EDCC), and why it suits a multidisciplinary readership
- [ ] Declaration of competing interests; funding statement; CRediT contributions
- [ ] Data-availability statement (matched to reality; review-safe)
- [ ] Ethics/IRB approval and consent statements for human-subjects or qualitative fieldwork
- [ ] Suggested/opposed reviewers if the form invites them (span the relevant disciplines)
- [ ] Confirm not under review elsewhere; AI not listed as an author

## Anti-patterns

- Uploading a manuscript that unmasks the authors (self-citation, acknowledgments, identifying institutions, live repo link)
- Asterisks for significance, or numbers with no development-relevant interpretation
- Abstract over 250 words or that lists methods without the development finding
- A cover letter that pitches the paper as JDE-style methods rather than WD-style development relevance
- Asserting a word limit, fee, or editor name not confirmed on the live page (mark 待核实)

## Output format

```text
【Anonymization】blinded file + separate title page; no unmasking? [Y/N]
【Abstract】≤250 words + 3–6 keywords + stands alone? [Y/N]
【Exhibits】no asterisks; units interpretable? [Y/N]
【Declarations】COI / funding / CRediT / data statement / ethics ready? [Y/N]
【Cover letter】states WD development contribution + sibling boundary? [Y/N]
【Volatile facts】word limit / fees / editors re-verified or marked 待核实? [Y/N]
【Next step】submit via Editorial Manager → worlddev-rebuttal for the decision letter
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
