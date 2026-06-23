---
name: restud-submission
description: Use when running the final pre-submission preflight for a The Review of Economic Studies (REStud) manuscript — double-anonymity, the ~45-page limit, Harvard author-date references, online appendix, the USD submission fee, and the Editorial Express portal. Last gate before submitting; does not assess the science. Verify current limits and fee on the journal's official page.
---

# REStud Submission Preflight (restud-submission)

## When to trigger

- Within 48 hours of submission
- After every R&R, before resubmission
- When unsure which files the portal requires
- After a rejection elsewhere, when routing into REStud

## Durable norms (verify current specifics)

REStud is run by the Review of Economic Studies Ltd and published by Oxford University Press. The mechanics below are taken from the journal's current author guidelines (verified 2026-05-30); the **fee and any length limits can change — re-confirm on https://www.restud.com/submissions/ and the Editorial Express portal before submitting**.

- **References:** **Harvard (author-date)** style throughout — *not* numbered references.
- **Review:** **double-anonymous (double-blind)** — both author and referee identities are hidden, so the manuscript must be fully anonymized at first submission.
- **Online appendix:** REStud routes full proofs, extra robustness, and supplementary material to an online appendix / supplementary file. Keep the main text lean.
- **Replication:** data and code are checked for reproducibility **before publication** by the journal's Data Editor (see `restud-replication-package`).

## Format checklist

- [ ] Manuscript compiles to a single clean **PDF** for review (LaTeX/Word are supplied only once accepted)
- [ ] References in **Harvard author-date** style; every in-text cite appears in the list and vice versa
- [ ] Tables use professional rules; figures are vector with self-contained notes
- [ ] Equations numbered; symbols glossed on first use
- [ ] Online appendix / supplementary file prepared separately (proofs, extra robustness)
- [ ] **JEL classification codes** included (required by REStud/OUP)
- [ ] Keywords and abstract included
- [ ] Main manuscript within the **~45-page limit** (title page, tables, figures, references, appendices included; ~1.5 line spacing, 12pt, ≥1in margins) — confirm the current limit on restud.com

## Anonymity checklist (REStud is double-anonymous)

- [ ] Author names, affiliations, and acknowledgements removed from the manuscript
- [ ] Self-citations phrased neutrally ("Smith (2020) shows", not "in our earlier work")
- [ ] File metadata stripped of author identity
- [ ] Funding / acknowledgement notes moved out of the anonymized file
- [ ] Links to personal websites / repositories that reveal identity removed or anonymized

## Files to prepare

- [ ] Main manuscript PDF, **fully anonymized** (double-anonymous review)
- [ ] Online appendix / supplementary file (proofs, supplementary robustness)
- [ ] Cover letter (only if there is substantive information — COI, data-access limits, related submissions)
- [ ] Conflict-of-interest / disclosure statement per the current policy
- [ ] Suggested / opposed referees (from `restud-referee-strategy`) if the portal asks
- [ ] Replication materials planned (the Data Editor's reproducibility check happens before publication, not at first submission)

## Submission system & fee

- REStud submits through **Editorial Express** at **http://editorialexpress.com/restud** — confirm the live link on the official page.
- The corresponding author submits; keep ORCID and contact details current.
- **Submission fee is charged in USD: USD 250** for a new submission, with a **reduced USD 150** rate when *every* author meets at least one of (i) current student, (ii) within six years of completing the PhD, or (iii) residence in a World Bank low- or middle-income economy (rate effective 1 June 2026; corrected 2026-06-23 — the prior USD 200 / 120 schedule held 1 July 2023–31 May 2026). Supporting evidence (CV / website link) is required to claim the reduced rate. Re-confirm the current figures on restud.com rather than quoting a stale number.
- Editorial pre-screening is real here: editors desk-reject roughly **20–23%** of initial submissions before refereeing (lower than QJE/REStat), so the manuscript must clear the bar on the first page.

## Anti-patterns

- Leaving author-identifying metadata or acknowledgements in the file when review is double-anonymous
- **Numbered-reference** style when REStud uses Harvard author-date
- Forgetting JEL codes (REStud/OUP require them)
- A long cover letter that pitches the contribution (the abstract does that)
- Stuffing proofs into the main text instead of the online appendix
- Quoting a stale fee (it is USD 250 / 150 from 1 June 2026, charged in dollars, not sterling) or treating the ~45-page cap as a guarantee — always send the user to verify on restud.com

## Output format

```
【LENGTH】main text X pages / abstract Y — vs ~45-page limit (verify on restud.com)
【ANONYMITY】double-anonymous pass / fixes: [...]
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
- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check across format, double-anonymity, exhibits, references, appendix, and the Editorial Express portal
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — econ data sources and Stata / R / Python packages for REStud-track empirical and structural work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official REStud/OUP URLs with what each verifies and the access date
