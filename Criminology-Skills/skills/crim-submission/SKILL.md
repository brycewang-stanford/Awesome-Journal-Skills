---
name: crim-submission
description: Use when running the final pre-submission preflight for Criminology (ASC / Wiley) via the Wiley Research Exchange portal — anonymized main document plus separate title page, APA-based formatting, bias-free language, single-submission commitment, and (待核实) length/abstract caps and ORCID. Final checks; it does not draft content.
---

# Submission Preflight (crim-submission)

The last check before pressing submit on the **Wiley Research Exchange** portal
(`wiley.atyponrex.com/journal/CRIM`). *Criminology* uses a **blinded/anonymized** workflow, so the most
common avoidable failure is an under-anonymized main document. Verify volatile specifics on the
official page before relying on them (many are 待核实).

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Research Exchange expects
- Confirming the manuscript is anonymized and formatted to the journal's APA-based style

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** American Society of Criminology (ASC) / Wiley.
- **Portal:** **Wiley Research Exchange** — `https://wiley.atyponrex.com/journal/CRIM`; track status at
  `submission.wiley.com` → "My Submissions".
- **Files:** at least **one title page** + **one anonymized main document** (blinded workflow).
- **Style:** **a form of APA**; fall back to **APA (6th ed.)** for anything unspecified; author-date,
  alphabetical reference list; everything **double-spaced**.
- **Author bio:** a short biography (**< 100 words**) per author on the title page.
- **Language:** **APA bias-free, person-first** language for justice-involved populations.
- **Exclusivity:** **one journal at a time** — simultaneous submission is not allowed.
- **Length / abstract caps:** specific word/page and abstract limits for *Criminology* are 待核实 — confirm
  on the live author-guidelines page.
- **ORCID:** Wiley commonly requests it for the corresponding author (待核实 whether mandatory).
- **Fee:** no submission fee identified; only an **optional OA APC** on acceptance (待核实).

## Preflight checklist

### Files & length
- [ ] Separate **title page** (authors, affiliations, < 100-word bios) prepared as its own file
- [ ] **Anonymized main document** uploaded separately
- [ ] Length/abstract within the journal's current cap (待核实 — confirm on live page)

### Anonymity (blinded workflow)
- [ ] No author names, affiliations, or acknowledgments in the main document
- [ ] No obvious self-references ("as we showed in…"); self-citations neutralized
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Restricted-data acknowledgments/grant numbers kept off the main document

### Format & language
- [ ] APA-based style; consistent author-date citations; double-spaced throughout
- [ ] **Bias-free, person-first** language for offenders, victims, justice-involved people
- [ ] Figures/tables/maps self-contained and accessible (see `crim-tables-figures`)
- [ ] Corresponding-author **ORCID** ready (待核实 whether required)

### Compliance & files
- [ ] Ethics / IRB / human-subjects + data-use agreements in order
- [ ] **Single-submission** commitment honored (not under review elsewhere)
- [ ] Data-availability statement + reproducibility package staged (see `crim-data-and-transparency`)

## Anti-patterns

- Author identifiers left in the main document, acknowledgments, or file metadata (breaks anonymity)
- Mixing citation styles or single-spacing the manuscript
- Stigmatizing labels instead of person-first language
- Submitting while the paper is under review at another journal (prohibited)
- Sending a policy-evaluation paper here instead of *Criminology & Public Policy*

## Anonymity failure modes that trip the desk (Criminology specifics)

Because *Criminology* runs a blinded workflow, the most common avoidable bounce-back at the ASC/Wiley
desk is a main document that quietly de-anonymizes the author. Crime research has its own leak channels.
Scan for each before upload.

| Leak channel | Criminology-specific example | Fix before submit |
|--------------|------------------------------|-------------------|
| Self-citation phrasing | "as we found in our Philadelphia cohort study" | neutralize to third person, cite plainly |
| Restricted-data acknowledgment | named NACJD enclave grant or agency MOU in text | move to title page / cover note |
| Named field site | the specific police department in a hot-spot trial | generalize ("a large U.S. municipal agency") |
| File metadata | author name in the .docx properties or track-changes | strip document properties and comments |
| Cohort/IRB protocol number | tying the sample to one identifiable PI | remove from main document |

## Worked vignette: a one-page preflight (illustrative)

A team uploading a recidivism survival study splits the file into a title page (authors, affiliations,
three < 100-word bios) and an anonymized main document; confirms double-spacing across the 6 tables and
references; converts "felons" to "people with a prior conviction"; strips the agency name from methods;
and stages the NACJD access note off the main document. They leave the length check at 待核实 and do not
press submit until the current word cap is verified on the live page.

## Referee/editor-desk pushback at submission (the Criminology fix)

- *"Anonymity is broken in section 3."* Fix: third-person self-reference; identifying details to the cover note.
- *"Citation style is inconsistent."* Fix: one APA-based style end to end via a reference manager.
- *"Stigmatizing labels throughout."* Fix: APA bias-free, person-first language for justice-involved people.

## Output format

```
【Files】title page + anonymized main document both prepared? [Y/N]
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Length/abstract within cap (待核实)】[Y/N]
【APA-based style + double-spaced】[Y/N]
【Bias-free / person-first language】[Y/N]
【Single submission + ethics/DUA】[Y/N]
【Data + transparency staged】[Y/N]
【Next】await decision → crim-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Research Exchange portal, APA-based style, anonymized files, caps/fee (待核实)
