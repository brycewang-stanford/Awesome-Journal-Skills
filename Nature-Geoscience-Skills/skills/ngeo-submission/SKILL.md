---
name: ngeo-submission
description: Use when running the final pre-submission preflight for a Nature Geoscience manuscript — word/display-item limits, format, files, online Methods, Supplementary Information, Reporting Summary, data/code availability, and Editorial Manager metadata. Verifies submission readiness; does not write content.
---

# Nature Geoscience Submission Preflight (ngeo-submission)

## When to trigger

- "Submitting tonight" — the last check before uploading to Editorial Manager
- You are unsure which files the Nature Portfolio system expects
- You need to confirm the Reporting Summary and data/code-availability statements are complete
- You want a single gate before handing off to the in-house editor

## Pre-submission checklist

### Scope and length

- [ ] The manuscript clears the broad-interest Earth-system gate (see `ngeo-scope-fit`)
- [ ] Main text within the ~3,000-word Article limit (excluding abstract/Methods/refs/legends)
- [ ] Abstract ≤ ~200 words, unreferenced, and uses "Here we show"
- [ ] Title ≤ ~90 characters
- [ ] Display items within the 4–6 ceiling; references near/under ~50

### Format and structure

- [ ] Correct content type selected (Article or Brief Communication)
- [ ] Online **Methods** section present, divided by topical subheadings
- [ ] Results/Discussion organised with 3–4 topical subheadings (Article)
- [ ] SI units, consistent significant figures, every quantity with uncertainty
- [ ] Every acronym/symbol defined on first use; notation consistent throughout
- [ ] Nature reference style applied

### Compliance files (these gate acceptance, not just submission)

- [ ] **Data availability** statement: repository + accession/DOI (community repo where available, e.g. PANGAEA)
- [ ] **Code availability** statement for custom analysis code
- [ ] **Nature Portfolio Reporting Summary** completed and consistent with Methods
- [ ] Any required ethics / sample-provenance / permit statements (fieldwork, cores, meteorites)
- [ ] Competing-interests statement
- [ ] Author-contributions (CRediT-style) statement

### Files to upload

- [ ] Main manuscript (main text + online Methods, per the current template)
- [ ] All figures at production resolution (vector for line art; high-res raster for imagery)
- [ ] Supplementary Information file(s), items labeled Fig. Sn / Table Sn
- [ ] Reporting Summary
- [ ] Cover letter (justifies broad interest; not seen by reviewers — see `ngeo-cover-letter`)
- [ ] Source data for main figures if required

### Editorial Manager metadata

- [ ] Corresponding author, ORCID, and all affiliations complete
- [ ] Title / abstract / author list entered consistently with the manuscript
- [ ] Suggested and excluded referees entered (see `ngeo-referee-strategy`)
- [ ] Double-blind review opt-in selected (and manuscript anonymised) if chosen
- [ ] Related manuscripts under consideration disclosed
- [ ] Prior preprint (ESSOAr / EarthArXiv) disclosed

### Self-consistency

- [ ] Every "see Supplementary" / "see Methods" pointer resolves
- [ ] Figure/table/reference numbering continuous and matching in-text callouts
- [ ] SI items use the S-prefix and are each cited from the main text or Methods
- [ ] The main text stands alone without the SI (cross-check `ngeo-supplementary`)

## Submission-system notes

- Submit through the **Nature Portfolio Editorial Manager** manuscript-tracking system; verify the current portal and account requirements on the author pages.
- **No presubmission enquiries** are accepted — the cover letter carries the full case (see `ngeo-cover-letter`).
- The in-house editor triages on interest **before** review; most submissions are declined without review, so scope and cover letter are decisive.
- Keep the Reporting Summary and availability statements accurate — they are checked and can hold up acceptance.
- Open-access: Nature Geoscience offers an OA option with an APC (re-check the current figure on the official site); a subscription route also exists.

## Night-before dry run

Run this sequence the evening before, not at the upload screen:

1. **Limit audit.** Word count (main text only), abstract words, title characters, display-item count, reference count — all under their ceilings.
2. **Compliance sweep.** Reporting Summary complete; data DOI live; code repository accessible; ethics/permit statements present.
3. **Pointer audit.** Every "Methods"/"Supplementary" mention maps to real content; no S-prefixed item uncited.
4. **Metadata dry-fill.** Draft the Editorial Manager fields (referees, contributions, disclosures) in a text file so the live session is transcription, not composition.
5. **Freeze.** No content edits after the dry run; any change reopens the limit and pointer audits.

## Desk-return / hold triggers to eliminate

| Trigger                                       | Why it stalls or bounces               |
|-----------------------------------------------|----------------------------------------|
| Broad-interest case absent in the cover letter | Editorial reject before review         |
| Over the word / display-item / reference limit | Returned for reformatting              |
| Missing or inconsistent Reporting Summary      | Held before acceptance                 |
| "Data available on request" only               | Non-compliant data statement           |
| Custom code with no availability statement     | Held before acceptance                 |
| Main text depends on the SI                    | Referee friction / editorial return    |

## Anti-patterns

- Treating the Reporting Summary and data/code statements as afterthoughts
- Submitting a regional study with no broad-interest argument (editorial reject)
- Over-length discovered only at the upload screen
- Deposit-on-request data instead of a repository DOI
- SI items uncited or the main text silently depending on them
- Forgetting to disclose a preprint the editor will find

## Output format

```
【Scope + length】gate cleared; main text ≤~3,000 / abstract ≤~200 / title ≤~90?  yes / fix
【Content type】Article / Brief Communication correct?  yes / fix
【Methods】online Methods with subheadings present?  yes / fix
【Compliance】data DOI / code / Reporting Summary / ethics — all present?
【Files】manuscript / figures / SI / Reporting Summary / cover letter — present?
【Editorial Manager metadata】ORCID / referees / disclosures / double-blind?
【Stands alone】yes / fix
【Next】await reports → ngeo-revision; plan referees → ngeo-referee-strategy
```

## Attached resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check across scope / length / format / compliance / files / metadata / self-consistency
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — Article skeleton (title, "Here we show" abstract, main text, online Methods, availability statements, SI outline, cover letter)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reanalysis/satellite/proxy data sources, repositories, and the geospatial software stack

> Portal, content types, word/display-item limits, Reporting Summary, and required statements are volatile — verify all on the official Nature Geoscience author pages before submitting (Checked: 2026-07-16).
