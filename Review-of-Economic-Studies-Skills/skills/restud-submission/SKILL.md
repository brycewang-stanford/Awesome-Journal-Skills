---
name: restud-submission
description: Use when running the final pre-submission preflight for a The Review of Economic Studies (REStud) manuscript — title page and author information, the ~45-page limit and 150-word abstract, Harvard author-date references, online appendix, the USD submission fee, and the Editorial Express portal. Last gate before submitting; does not assess the science. Verify current limits and fee on the journal's official page.
---

# REStud Submission Preflight (restud-submission)

## When to trigger

- Within 48 hours of submission
- After every R&R, before resubmission
- When unsure which files the portal requires
- After a rejection elsewhere, when routing into REStud

## Durable norms (verify current specifics)

REStud is run by the Review of Economic Studies Ltd and published by Oxford University Press. The mechanics below are taken from the journal's current author guidelines (re-verified 2026-11-23); the **fee and any length limits can change — re-confirm on https://www.restud.com/submissions/ and the Editorial Express portal before submitting**.

- **References:** **Harvard (author-date)** style throughout — *not* numbered references.
- **Review / identity:** **not anonymized** — the official submission guidelines (re-checked 2026-11-23) ask for each author's name, department, and institution on the title page and do not mention blind review. Do not strip author identity unless the live page says otherwise.
- **Online appendix:** REStud routes full proofs, extra robustness, and supplementary material to an Online Appendix, which **should not exceed 30 pages**. Keep the main text lean.
- **Replication:** data and code are checked for reproducibility **before publication** by the journal's Data Editor (see `restud-replication-package`).

## Format checklist

- [ ] Manuscript compiles to a single clean **PDF** for review (LaTeX/Word are supplied only once accepted)
- [ ] References in **Harvard author-date** style; every in-text cite appears in the list and vice versa
- [ ] Tables use professional rules; figures are vector with self-contained notes
- [ ] Equations numbered; symbols glossed on first use
- [ ] Online appendix / supplementary file prepared separately (proofs, extra robustness)
- [ ] **JEL classification codes** included (required by REStud/OUP)
- [ ] **Abstract ≤150 words** and **keywords** included (both required on restud.com)
- [ ] Main manuscript within the **~45-page limit** (title page, tables, figures, references, appendices included; ~1.5 line spacing, 12pt, ≥1in margins) — confirm the current limit on restud.com

## Title page & author information (no anonymization requested)

- [ ] Title page: first name, initial(s), and surname of each author, followed by department and institution; corresponding author's contact details
- [ ] Acknowledgements / funding on the title page (address changes may go next to Affiliations or Acknowledgements)
- [ ] Self-citations phrased neutrally ("Smith (2020) shows") as a matter of style
- [ ] Single PDF containing title page, abstract, text, figures, and tables

## Files to prepare

- [ ] Main manuscript as a **single PDF** with the title page (author names and affiliations) included
- [ ] Online Appendix (≤30 pages; proofs, supplementary robustness)
- [ ] Cover letter (only if there is substantive information — **data/code-policy exemption requests must be made here at first submission**, comments on published papers, COI, related submissions)
- [ ] Conflict-of-interest / disclosure statement per the current policy
- [ ] Suggested / opposed referees (from `restud-referee-strategy`) if the portal asks
- [ ] Replication materials planned (the Data Editor's reproducibility check happens before publication, not at first submission)

## Submission system & fee

- REStud submits through **Editorial Express** at **http://editorialexpress.com/restud** — confirm the live link on the official page.
- The corresponding author submits; keep ORCID and contact details current.
- **Submission fee is charged in USD: USD 250** for a new submission, with a **reduced USD 150** rate when *every* author meets at least one of (i) current student, (ii) within six years of completing the PhD, or (iii) residence in a World Bank low- or middle-income economy (rate effective 1 June 2026; corrected 2026-06-23 — the prior USD 200 / 120 schedule held 1 July 2023–31 May 2026). Supporting evidence (CV / website link) is required to claim the reduced rate. Re-confirm the current figures on restud.com rather than quoting a stale number.
- Editorial pre-screening is real here: editors desk-reject roughly **20–23%** of initial submissions before refereeing (lower than QJE/REStat), so the manuscript must clear the bar on the first page.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue restud-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Anti-patterns

- Stripping author names and affiliations as if REStud were double-anonymous (the official title-page rules require them)
- **Numbered-reference** style when REStud uses Harvard author-date
- Forgetting JEL codes (REStud/OUP require them)
- A long cover letter that pitches the contribution (the abstract does that)
- Stuffing proofs into the main text instead of the online appendix
- Quoting a stale fee (it is USD 250 / 150 from 1 June 2026, charged in dollars, not sterling) or treating the ~45-page cap as a guarantee — always send the user to verify on restud.com

## Output format

```
【LENGTH】main text X pages / abstract Y — vs ~45-page limit (verify on restud.com)
【TITLE PAGE】names + affiliations + contact; abstract ≤150 words + keywords: pass / fixes: [...]
【REFERENCES】Harvard author-date confirmed; in-text ↔ list reconciled
【JEL】codes present
【ONLINE APPENDIX】prepared / n/a
【FILES READY】[...]
【FEE / PORTAL】USD 250 (or 150 reduced) via Editorial Express; user pointed to verify
【READY TO SUBMIT】yes / no — blockers
【NEXT SKILL】await decision → restud-rebuttal
```

## Resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — REStud manuscript skeleton (abstract, model/empirics structure, Harvard author-date references, online-appendix layout)
- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check across format, title page, exhibits, references, appendix, and the Editorial Express portal
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — econ data sources and Stata / R / Python packages for REStud-track empirical and structural work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official REStud/OUP URLs with what each verifies and the access date
