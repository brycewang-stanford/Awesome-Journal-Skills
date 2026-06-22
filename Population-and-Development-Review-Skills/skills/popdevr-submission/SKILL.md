---
name: popdevr-submission
description: Use when running the final pre-submission preflight for Population and Development Review (PDR, Wiley / Population Council) via ScholarOne Manuscripts — article-type selection, Free Format first-round submission, double-anonymized preparation, the data availability statement, ORCID, and confirmation that there are no author fees (no APC). Final checks; it does not draft content.
---

# Submission Preflight (popdevr-submission)

The last check before pressing submit on **ScholarOne Manuscripts**. PDR is **double-anonymized**, so the
most common avoidable failure is a manuscript that still identifies its authors. PDR uses **Free Format**
for the first round — strict formatting is deferred to revision — but the science, the anonymization, and
the statements must be in order. Verify volatile specifics on the Wiley author page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming the manuscript is anonymized and the right article type/length is chosen

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** **Population Council** (owner) / **Wiley** (publisher); quarterly; founded 1975.
- **Portal:** **ScholarOne Manuscripts** (confirm the current submission link). 待核实.
- **Review model:** **double-anonymized** — remove all identifying information about all co-authors; do
  not name yourself as author in the text or metadata.
- **Free Format (first round):** simplified submission — references may be in **any consistent style**,
  with strict formatting (APA-style house style) applied at revision. Confirm current Free Format scope. 待核实.
- **Article types:** Research Article (typically ~8,000–10,000 words), Notes & Commentary (short),
  Data & Perspectives, Archives, Book Reviews (usually invited).
- **Front matter:** abstract + keywords (confirm the current abstract word limit on the author page). 待核实.
- **Fees:** **no author fees** — no submission fee and **no article-processing charge (APC)** under the
  standard model (open-access/Online Open options may carry a separate Wiley APC if chosen). Consistent
  with the Wiley author guidelines as of 2026-06-22; re-verify on the author page before submission. 待核实.
- **ORCID + statements:** ORCID for the submitting author; **data availability statement**; funding,
  conflict-of-interest, and ethics declarations (see `popdevr-transparency-and-data`).

## Preflight checklist

### Type & length
- [ ] Article type chosen and its length norm met (Article ~8,000–10,000 words; Note short)
- [ ] Abstract and keywords present (within the current limit — 待核实)
- [ ] Exhibit set kept tight; extended material moved to supporting information

### Anonymity (double-anonymized)
- [ ] No author names, affiliations, or acknowledgments in the manuscript file
- [ ] No self-identifying references ("as we showed in…"); self-citations neutralized
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) title page prepared as ScholarOne requires

### Format & metadata (Free Format first round)
- [ ] References in one **consistent** style (APA-style applied at revision)
- [ ] Figures/tables self-contained and accessible (see `popdevr-tables-figures`)
- [ ] ORCID provided for the submitting author

### Compliance & files
- [ ] **Data availability statement** drafted; materials staged for a FAIR repository
      (see `popdevr-transparency-and-data`)
- [ ] Funding / conflict-of-interest / ethics declarations complete
- [ ] Confirmed: **no submission fee or APC** under the standard model (note any Online Open choice)

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-anonymized review)
- Sending a long paper to the Notes & Commentary track, or padding a Note to Article length
- Assuming a Wiley APC applies — under the standard model PDR has **no author fees** (verify)
- Skipping the data availability statement because "it's only needed at acceptance"
- Over-formatting the first round when Free Format is accepted (waste of effort; just keep it consistent)

## Compliance pre-screen: what the desk checks first (by article type)

PDR's editors/committee screen for fit and rigor before review; getting the basics right keeps the focus
on the science. Map your type to its norms (confirm current numbers on the Wiley author page):

| Item | Research Article | Notes & Commentary | Data & Perspectives |
|------|------------------|--------------------|---------------------|
| Length (norm) | ~8,000–10,000 words | short | focused on the data/indicator |
| Abstract / keywords | required (limit 待核实) | required | required |
| Double-anonymized | required | required | required |
| Data availability statement | required | required | required (central) |
| ORCID (submitting author) | required | required | required |

## Referee/editor pushback at the desk and the submission-side fix

- *"Self-identifying references compromise the double-anonymization."* -> Neutralize self-citations
  ("prior work [Author] showed" not "as we showed"), strip document-property metadata, split off a
  non-anonymous title page.
- *"This Note exceeds the short-form norm."* -> Trim to a focused Note or move it to the Research Article
  track; do not submit an over-length Note.
- *"The data availability statement is missing."* -> Stage the statement and FAIR-repository deposit now
  (see `popdevr-transparency-and-data`).
- *"Was this submitted through the right portal?"* -> Use ScholarOne Manuscripts; confirm the current link
  on the Wiley author page.

## Output format

```
【Type】Article / Note / Data & Perspectives (length norm met? Y/N)
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Abstract / keywords】present + within limit (待核实)? [Y/N]
【Free Format】references consistent (APA at revision)? [Y/N]
【Data statement + ORCID】drafted + repo staged + ORCID? [Y/N]
【Fees】confirmed no submission fee / APC under standard model? [Y/N]
【Next】await decision -> popdevr-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — the pre-submission self-check as a copyable list
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, FAIR repositories
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official PDR / Wiley URLs behind every fact in this pack
