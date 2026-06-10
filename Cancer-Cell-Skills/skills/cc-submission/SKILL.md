---
name: cc-submission
description: Use when running the final pre-submission preflight for Cancer Cell (Cell Press) — file completeness, STAR Methods / Key Resources Table, deposition accessions, statistics reporting, ethics statements, figure integrity, and portal logistics. It is the last gate before submitting.
---

# Pre-Submission Preflight (cc-submission)

## When to trigger

- About to click submit
- Unsure which files / statements the portal needs
- Final consistency pass across manuscript, figures, KRT, and declarations

## Pre-submission checklist

### Files & format

- [ ] Manuscript file (DOC/DOCX or PDF per current spec), line/page numbers on
- [ ] Figures at required resolution and format (TIFF/EPS/PDF); each cited in order
- [ ] Supplemental items packaged; supplemental tables/data referenced in text
- [ ] Graphical abstract file (if used) at required size/resolution
- [ ] Cover letter attached (from `cc-cover-letter`)
- [ ] Highlights and eTOC blurb included (from `cc-structured-abstract`)

### STAR Methods & rigor

- [ ] STAR Methods headings complete; **Key Resources Table** at the top
- [ ] Every antibody / cell line / organism / plasmid / software has source + RRID
- [ ] Cell lines authenticated; mycoplasma-negative stated
- [ ] Animal section: sample size, randomization, blinding, exclusions

### Statistics

- [ ] `n` defined per panel as biological replicates; no pseudo-replication
- [ ] Tests named; multiple comparisons / FDR corrected
- [ ] Error bars defined (SD/SEM/CI) in every legend; exact p where feasible

### Figures & integrity

- [ ] Each representative image paired with replicate quantification
- [ ] Uncropped blots in supplement; no undisclosed splicing; linear adjustments
- [ ] Scale bars and labeled axes/markers present

### Ethics & availability

- [ ] IACUC approval + protocol # (if animals); IRB + consent + Helsinki (if human)
- [ ] Data and code availability statement complete; accessions match the KRT
- [ ] Deposition records created (GEO/SRA/PRIDE/PDB) with reviewer tokens if needed
- [ ] Competing interests, funding, and author contributions stated; ORCIDs linked

### Front matter & consistency

- [ ] Summary within word limit; Highlights within count/length
- [ ] Gene/protein nomenclature consistent across text, figures, front matter
- [ ] Every in-text figure/table/reference citation resolves; reference style correct
- [ ] Claims match evidence (no therapeutic claim without in vivo/human support)

## Portal logistics

- Submit through the Cell Press portal linked from the Cancer Cell author page (verify current URL).
- Have suggested/excluded reviewers ready; complete all required metadata fields.
- Confirm corresponding author and all co-author details/affiliations.
- Verify volatile items (word/figure limits, fees, required statements) on the live author page — they change.

## Anti-patterns

- Submitting with sequencing/proteomics data "available on request"
- Key Resources Table missing or with reagents lacking RRIDs
- Cell lines unauthenticated / no mycoplasma statement
- Representative images with no quantification
- Mismatched accessions between KRT and availability statement
- Figures not cited in order; broken cross-references


## Submission readiness pass for Cancer Cell

Use this as a second-pass capability check. First lock the cancer context, mechanism, model system, validation chain, and translational boundary; then test whether the manuscript addresses cancer-biology reviewers who expect mechanistic oncology, translational relevance, and strong multi-modal validation.

- **Primary move:** Verify portal, article type, anonymity, declarations, files, data/code, and current source-map facts; return blockers before formatting advice.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Cell for broader biology, Nature Cancer for oncology breadth, Clinical Cancer Research for clinical translation; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Files】manuscript / figures / supplement / graphical abstract / cover letter complete?
【STAR Methods + KRT】complete? RRIDs present?
【Rigor】authentication / mycoplasma / animal rigor OK?
【Statistics】n / tests / multiplicity / error bars OK?
【Integrity】quantification / raw blots / scale bars OK?
【Ethics & data】approvals + accessions + code DOI present?
【Front matter】Summary / Highlights / nomenclature consistent?
【Next step】Submit → await reviews → cc-peer-review-revision
```

## Related resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — Cell Press manuscript skeleton (Summary, Highlights, STAR Methods, Key Resources Table, data availability)
- [`templates/checklist.md`](templates/checklist.md) — Full pre-submission self-check across scope, rigor, statistics, figures, ethics, and deposition
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Repositories (GEO/SRA/PRIDE/PDB), reporting frameworks, and bioinformatics / imaging software
