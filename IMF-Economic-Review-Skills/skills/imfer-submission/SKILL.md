---
name: imfer-submission
description: Use when running the final pre-submission preflight for an IMF Economic Review (IMFER) manuscript via Editorial Manager — double-blind anonymization, italicized abstract with JEL codes, Chicago style, separate author-bio file, and the data-availability statement. Final checks; it does not draft content (imfer-writing-style) or plan the rebuttal (imfer-rebuttal).
---

# Submission Preflight (imfer-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Unsure which files IMFER expects (anonymized main file, separate title/bio file, supplementary appendix)
- Confirming house style: italicized abstract, JEL codes, Chicago citations, American spelling
- Confirming the double-blind requirements are met and no author traces remain in the main file

## Process facts (检索于 2026-06；以官网为准)

- IMFER is the **IMF's flagship scholarly journal**, published by **Palgrave Macmillan / Springer Nature** for the International Monetary Fund (Online via Springer Nature Link, journal 41308); successor to *IMF Staff Papers*. Submission is via the journal's **online system (Editorial Manager)** — confirm the live portal on the official page.
- **Editor (verified 2026-06-22): Jesús Fernández-Villaverde (Penn); Co-Editor: Emine Boz (IMF).** Earlier Gourinchas/Kose listings are stale. Re-verify on the live Palgrave board before naming an editor.
- **Double-blind review:** the main article file and all table/figure files **must not contain any author-identifying information**; anonymize self-citations.
- **Author information separate:** full contact details and author biographies go in a **separate file**; biographies **≤80 words per author**.
- **Abstract + JEL:** the paper opens with an **italicized abstract** followed by **JEL classification codes**.
- **Style:** essentially **The Chicago Manual of Style**; **American spelling**, punctuation, and syntax.
- **Data & code:** prepare a data-availability statement and replication package; restricted IMF/central-bank inputs handled with access instructions, not redistribution (see `imfer-replication-package`). Confirm exact deposit requirements on the official pages — **待核实**.
- **Fees / open access / exact length & abstract-word limits:** **待核实** — not asserted here; confirm on the Springer Nature IMFER submission-guidelines page before relying on them.

## Preflight checklist

### Double-blind & files
- [ ] Main article file and every table/figure file are **free of author names, affiliations, acknowledgments, and grant numbers**
- [ ] Self-citations anonymized in text and references
- [ ] **Separate file** with full contact details (corresponding author) and author bios **≤80 words each**
- [ ] Supplementary / online appendix prepared as a separate file if used
- [ ] Replication package / data-availability statement ready (restricted-data access instructions included)

### Format & house style
- [ ] Abstract is **italicized**, compact, self-contained, with a policy-unit magnitude
- [ ] **JEL codes** present immediately after the abstract
- [ ] **Chicago Manual of Style** citations/references; **American spelling**
- [ ] Figures/tables: transparent country coverage; **no significance asterisks**; SEs/CIs reported
- [ ] Acronyms (CFM, DSA, GFC) defined on first use

### Substance gate (before the portal)
- [ ] Policy "so what" explicit in intro and abstract; implication bounded to the evidence
- [ ] Identification + country-composition checks visible in the main paper
- [ ] Not under review elsewhere; AI not listed as an author

### File-by-file upload map
Editorial Manager expects the manuscript split across files; have them ready and correctly typed before you start the session, because the system will not let you finish without them.

- **Main manuscript (anonymized PDF):** abstract (italic) + JEL + body + exhibits + references, no author traces
- **Title / author file (separate):** title, all authors, affiliations, corresponding-author contacts, ≤80-word bios, acknowledgments, grant numbers
- **Supplementary / online appendix (separate):** secondary proofs, reserve robustness, extended tables
- **Replication / data-availability material:** the statement plus package or access instructions (per `imfer-replication-package`)
- **Cover letter:** the contribution in two sentences and the policy relevance; suggested/excluded referees if invited

## Anti-patterns

- Submitting a main file that still names the authors or institution (breaks double-blind)
- Putting bios/contact details in the main file instead of a separate file
- A non-italicized abstract or missing JEL codes
- Asterisks/boldface for significance; opaque country coverage
- British spelling / non-Chicago references against house style
- Asserting a fee, word limit, or deposit rule that is actually 待核实
- Leaving acknowledgments, grant numbers, or a self-naming working-paper footnote that de-anonymizes the file

## The double-blind sweep (do this last)

Anonymization is the most common IMFER desk-return trigger, and it is easy to half-do. Before upload, sweep the main file and every exhibit file for: author names and initials; institutional affiliations; acknowledgments and thanks; grant and IRB numbers; "as we showed in [our prior paper]" self-references; working-paper series footnotes that name the authors; and file metadata/properties that embed the author. Self-citations should read in the third person. The title page, full contacts, and ≤80-word bios live in the *separate* file the system asks for — never in the manuscript.

## Worked vignette (illustrative)

A paper is otherwise ready but the PDF's first-page footnote thanks a discussant "at our department seminar," the acknowledgments name the grant, and Table 1's note says "see Smith and Lee (2024), our companion paper." All three break double-blind. The fix: move acknowledgments and the grant to the separate title file, rewrite the companion-paper note in the third person, strip PDF metadata, and confirm the abstract is italicized with JEL codes beneath it. Now the main file is clean for Editorial Manager.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-submission
【Double-blind】main + exhibit files anonymized; self-cites blinded? [Y/N]
【Separate file】contacts + bios (≤80 words)? [Y/N]
【Abstract+JEL】italicized abstract + JEL codes? [Y/N]
【House style】Chicago + American spelling; no asterisks? [Y/N]
【Replication】data-availability statement + restricted-data access path? [Y/N]
【Volatile facts】fees / limits / deposit rules confirmed or 待核实
【Next step】submit via Editorial Manager → imfer-rebuttal after the decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
