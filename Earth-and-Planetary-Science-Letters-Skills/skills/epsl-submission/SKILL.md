---
name: epsl-submission
description: Use when running the final pre-submission preflight for Earth and Planetary Science Letters (EPSL) via Editorial Manager — letters-format length check, title page and highlights, declarations (competing interests, authorship, AI use), data-availability statement with repository DOIs, and figure/table file compliance. Final checks; it does not draft content.
---

# Submission Preflight (epsl-submission)

The last pass before uploading to **Editorial Manager**, EPSL's Elsevier submission and peer-review
system. The avoidable failures at this stage are mechanical: a main text over the letters cap, a
missing data-availability statement, undeposited data, or incomplete declarations — each can bounce
the manuscript before any science is read. Exact requirements (word cap, highlights, file formats)
are volatile; re-check them on the official Guide for Authors the week you submit.

Templates in this skill: [`templates/checklist.md`](templates/checklist.md) and
[`templates/manuscript_template.md`](templates/manuscript_template.md).

## When to trigger

- Final pass before upload to Editorial Manager
- Unsure which files, statements, and metadata EPSL expects
- Verifying the letters-format constraints are actually met

## Process facts (re-check volatile items on the official page)

- **Publisher / system:** Elsevier; submission through **Editorial Manager** (the journal's entry link
  is on the ScienceDirect journal page).
- **Format:** a Letter — main text (introduction through conclusions) capped near **6,500 words**
  (re-check); concise titles; companion papers discouraged.
- **Article types:** Letters; invited **Frontiers Papers** (do not self-select without invitation);
  Comments/Replies; Errata/Corrigenda; Special-Issue papers.
- **Data:** Elsevier research-data policy — a **data-availability statement**, discipline-repository
  deposition (EarthChem, PANGAEA, IRIS/EarthScope, MagIC, NASA PDS, Zenodo), linked at submission.
- **Declarations:** competing interests, authorship/CRediT contributions, funding, and generative-AI
  use per Elsevier policy; ORCID for the corresponding author.
- **References:** Elsevier author–date house style (re-check the current instructions); DOIs included.
- **Supplement:** uploaded with the manuscript and reviewed with it.

## Preflight checklist

### Format & length
- [ ] Main text within the letters cap (count introduction → conclusions; re-check the figure)
- [ ] Title concise and process-forward; abstract self-contained with the headline number
- [ ] Highlights prepared if the current guide requires them (re-check)

### Files
- [ ] Manuscript source file per the guide; figures at required resolution/format, vector line art
- [ ] Supplementary material assembled and internally referenced (Fig. S1, Table S1…)
- [ ] Full data tables deposited; DOIs/accessions resolve

### Statements & metadata
- [ ] Data-availability statement with repository DOIs
- [ ] Competing-interest, authorship-contribution, funding, and AI-use declarations written
- [ ] Corresponding-author ORCID linked; all coauthors approved this version
- [ ] Suggested (and any opposed) reviewers entered; cover letter final (see `epsl-cover-letter`)

## Bounce-at-upload gates

| Gate | Pass condition | Fixed in |
|------|----------------|----------|
| Letters length | main text within cap | `epsl-writing-style` |
| Data statement | present, identifiers resolve | `epsl-reporting-and-reproducibility` |
| Declarations | COI / CRediT / funding / AI complete | this skill |
| Figure files | format, resolution, colormaps compliant | `epsl-figures-and-tables` |
| Article type | Letter (Frontiers only if invited) | `epsl-workflow` |

## Worked micro-example (illustrative — the night-before pass on the slab-fluid Letter)

- **Length:** main text 6,140 words introduction→conclusions — under the cap with margin for
  revision growth. Pass.
- **Data:** EarthChem DOI for the boron dataset resolves; the tomography model archived with a Zenodo
  DOI; both cited in the statement. Pass.
- **Declarations:** CRediT roles drafted per author; no competing interests; AI-use statement covers
  the language-editing tool per Elsevier policy.
- **The near-miss:** the supplement still cited "Figure S6," deleted two drafts ago — a broken
  internal reference reviewers reliably notice. Caught by a final cross-reference sweep.

## Anti-patterns

- Counting only the abstract-to-references span and discovering the cap violation after format checks
- "Data available on request" in the statement field
- Declarations copied from another journal's template with the wrong policy names
- Self-selecting the Frontiers type to look invited
- Uploading supplement and manuscript versions that disagree on a number

## Output format

```
【Length】main-text words vs cap (re-check) [count / cap]
【Files】manuscript + figures + supplement compliant? [Y/N]
【Data statement】DOIs resolve? [Y/N]
【Declarations】COI / CRediT / funding / AI / ORCID? [Y/N]
【Reviewers + cover letter】entered and final? [Y/N]
【Next】await decision → epsl-revision-and-rebuttal
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — the full itemized preflight
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — a letters-format manuscript skeleton
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Guide for Authors and Editorial Manager entry links
