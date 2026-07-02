---
name: prl-submission
description: Use when running the final pre-submission preflight for a Physical Review Letters manuscript — length check, format, files, Supplemental Material, classification, author info, and metadata. Verifies submission readiness; does not write content.
---

# PRL Submission Preflight (prl-submission)

## When to trigger

- "Submitting tonight" — the last check before the upload button
- You are unsure which files the APS submission system expects
- You need to confirm the manuscript passes the automated length check
- You want a single gate before handing off to peer review

## Pre-submission checklist

### Length and format

- [ ] Manuscript passes the current APS automated **length check** (body + figures + equations + references; verify the limit)
- [ ] Prepared in REVTeX (the APS LaTeX class) or an accepted format
- [ ] Submitted in the **Letter** article type, not a regular article
- [ ] Abstract within the current length limit and self-contained
- [ ] Figures embedded for review; production-quality source files ready
- [ ] SI units, consistent significant figures, defined notation throughout

### Files

- [ ] Main Letter source (LaTeX/REVTeX) + a compiled PDF
- [ ] All figure files at production resolution (vector for line art)
- [ ] **Supplemental Material** as a separate file, clearly labeled
- [ ] Cover letter (see `prl-cover-letter`)
- [ ] Bibliography / .bib file as required

### Classification and metadata

- [ ] Subject area / editor track selected accurately
- [ ] Current APS subject classification applied (verify the scheme in use)
- [ ] Title, abstract, and author list entered consistently with the manuscript
- [ ] Funding / acknowledgments handled per APS instructions
- [ ] Any required statements (data availability, ethics if applicable) present

### Authors and integrity

- [ ] All authors meet authorship criteria and have approved submission
- [ ] Corresponding author and contact details correct
- [ ] ORCID / affiliations complete
- [ ] Originality / not-under-consideration-elsewhere confirmed
- [ ] Prior arXiv / conference version disclosed
- [ ] Competing-interest statement if required

### Referees

- [ ] Suggested referees entered (see `prl-referee-strategy`)
- [ ] Opposed referees entered with brief, professional rationale

### Self-consistency

- [ ] Every "see Supplemental Material" pointer resolves
- [ ] Figure/equation/reference numbering continuous and matching in-text callouts
- [ ] SM figures/tables use the S-prefix and are cited from the body
- [ ] The Letter stands alone without the SM (cross-check `prl-supplementary`)

## Submission-system notes

- Submit through the APS editorial system; verify the current portal URL and account requirements on the PRL author page.
- The automated length check runs at submission — fix overages *before* uploading (use `prl-length-management`).
- Keep the SM as a distinct upload, not appended to the Letter PDF.
- Review is single-blind with subject-area / divisional editor tracks; the classification you pick steers which desk triages the Letter.
- Fees are no blocker under the subscription route: the page charge is optional, CC-BY open access carries an APC (~$2,700 — confirm live), and SCOAP3 covers eligible high-energy-physics Letters.

## Night-before dry run

Run this sequence the evening before, not at the upload screen:

1. **Clean compile.** Build the REVTeX source from scratch in a fresh directory to catch machine-local dependencies.
2. **Length estimate.** Apply the current APS formula — body, figures by printed area, equations, references — and leave a margin below the limit.
3. **Pointer audit.** Confirm every "Supplemental Material" mention maps to real SM content, and no S-prefixed item goes uncited.
4. **Metadata dry-fill.** Draft the portal fields in a text file so the live session is transcription, not composition.
5. **Freeze.** No content edits after the dry run; any change reopens the length check and pointer audit.

## Desk-return triggers to eliminate

| Trigger                                    | Why editors bounce it                |
|--------------------------------------------|--------------------------------------|
| Fails the automated length check           | Hard gate; no editorial discretion   |
| Wrong article type (regular article)       | Routed off the Letter track entirely |
| Abstract in portal differs from manuscript | Ambiguous record of submission       |
| SM appended inside the Letter PDF          | Breaks separate-SM production        |

## Anti-patterns

- Discovering an over-length only when the automated check rejects it
- Uploading the SM glued onto the end of the Letter PDF
- Wrong article type (regular article instead of Letter)
- Broken "see SM" cross-references after last-minute trimming
- Outdated subject classification or missing required statements
- Forgetting to disclose a prior arXiv version

## Output format

```
【Length check】pass (per APS formula) / fix
【Format】REVTeX / accepted; article type = Letter?  yes / fix
【Files】Letter / figures / SM / cover letter / bib — all present?
【Classification】subject area + current scheme applied?  yes / fix
【Authors】criteria, ORCID, originality, prior-version disclosure
【Referees】suggested + opposed entered?  yes / fix
【Stands alone】yes / fix
【Next】await reports → prl-revision; plan referees → prl-referee-strategy
```

## Attached resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check across length / format / files / classification / authors / referees / self-consistency
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — Letter skeleton (title, abstract, body sections, figure/equation/reference budgeting, SM outline)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — REVTeX/LaTeX, figure tools, data repositories, and physics computation packages

> Portal URL, length formula, classification scheme, and required statements are volatile — verify all on the official APS / PRL author page before submitting.
