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

## Upload gate

Use a three-state decision before any file enters Editorial Manager:

- **GO:** blinded manuscript, separate title page, cover letter, declarations, ethics/consent text, and data-availability statement are all present; author identity is absent from the blinded file and metadata; all volatile facts in the cover letter or manuscript have been re-checked or marked **待核实** outside the submitted prose.
- **CONDITIONAL HOLD:** the manuscript package is complete, but one external fact still needs live confirmation (for example current word limit, APC/waiver detail, portal label, or editor name). Do not invent the fact; either verify it on the official page or remove the assertion from the upload package.
- **HOLD:** any anonymization leak, missing declaration, over-limit abstract, identifying repository URL, unclear data-access route, or cover letter that cannot explain WD fit without pitching the paper as a narrow JDE/WBER-style econometrics article.

The gate is deliberately stricter than "all checklist boxes mostly done." A final preflight that returns HOLD should output the exact blocker and the file/section where it appears, not a generic request to "review submission materials."

## Editorial Manager package order

Assemble the upload set in this order so anonymization errors are caught early:

1. **Blinded manuscript:** no title-page identities, acknowledgments, funding IDs, author initials in file names, repository URLs, institutional ethics-board names that identify the team, or first-person self-citation phrasing.
2. **Separate title page:** full author details, corresponding author, acknowledgments, funding, conflicts, and any non-blinded data or ethics details required by the portal.
3. **Cover letter:** one paragraph each for development problem, evidence/design, contribution to WD's multidisciplinary readership, and sibling-boundary fit.
4. **Tables/figures/supplement:** labels match the manuscript, file names are anonymous, maps and qualitative exhibits do not expose restricted sites or participants.
5. **Declarations/data statement:** review-safe wording in the blinded package; camera-ready repository links held separately until acceptance.

## WD fit test for the cover letter

Before submission, force the cover letter through this test:

- **Development problem:** names the population, place, institution, or policy setting and explains why the issue matters for development practice or theory.
- **Evidence warrant:** states the design or inference logic plainly, including whether the paper is quant-causal, qualitative, mixed-methods, political-economy, or policy/practice oriented.
- **Sibling boundary:** explains why WD is the right home rather than Journal of Development Economics, World Bank Economic Review, Journal of Development Studies, Economic Development and Cultural Change, or World Development Perspectives.
- **Reader promise:** tells a cross-disciplinary WD reader what they will learn that changes understanding of poverty, inequality, institutions, livelihoods, governance, sustainability, or policy implementation.

If the letter cannot pass all four checks in plain language, route back to `worlddev-topic-selection` or `worlddev-writing-style` before upload.

## Volatile-fact handling

Do not let source uncertainty leak into the submission package. Use this rule:

| Fact type | Submission action |
|-----------|-------------------|
| Word limit / article type / portal field | Verify live in the Guide for Authors or leave out of the cover letter; do not copy a sibling journal limit |
| Editor names | Re-check live before naming anyone; otherwise address the editors generically |
| APC, waiver, or open-access fee | Treat as budget/admin information, not manuscript content, unless verified on the current official page |
| Data and ethics policy | State what the project will provide and why; if a WD-specific rule is uncertain, cite Elsevier policy generically and mark the WD-specific detail 待核实 in the internal output |
| Review model | Keep the blinded package conservative even if a portal field seems optional; double-anonymized review is the binding workflow assumption |

## Anti-patterns

- Uploading a manuscript that unmasks the authors (self-citation, acknowledgments, identifying institutions, live repo link)
- Asterisks for significance, or numbers with no development-relevant interpretation
- Abstract over 250 words or that lists methods without the development finding
- A cover letter that pitches the paper as JDE-style methods rather than WD-style development relevance
- Asserting a word limit, fee, or editor name not confirmed on the live page (mark 待核实)
- Treating a complete upload folder as submission-ready when the cover letter still cannot distinguish WD from its development-economics or development-studies siblings
- Submitting a review package with camera-ready repository links, acknowledgments, or funding details that should have stayed in the separate title-page/admin materials

## Output format

```text
【Gate】GO / CONDITIONAL HOLD / HOLD
【Anonymization】blinded file + separate title page; no unmasking? [Y/N]
【Abstract】≤250 words + 3–6 keywords + stands alone? [Y/N]
【Exhibits】no asterisks; units interpretable? [Y/N]
【Declarations】COI / funding / CRediT / data statement / ethics ready? [Y/N]
【Cover letter】development problem + evidence warrant + sibling boundary + reader promise? [Y/N]
【Volatile facts】word limit / fees / editors / portal facts re-verified, removed, or internally marked 待核实? [Y/N]
【Blockers】file/section-specific issues that prevent upload, or "none"
【Next step】submit via Editorial Manager → worlddev-rebuttal for the decision letter
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
