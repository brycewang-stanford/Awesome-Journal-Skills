---
name: orgstud-submission
description: Use when running the final pre-submission preflight for Organization Studies (OS) via ScholarOne — double-anonymization, the 13,000-word cap, the 300-word unstructured abstract, the keyword rule, and SAGE house format. Final checks; it does not draft content.
---

# Submission Preflight (orgstud-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on ScholarOne
- Unsure which files and fields the OS ScholarOne form expects
- Confirming the manuscript is properly anonymized for double-anonymized review
- Checking length, abstract, and keyword rules against OS's actual limits

## Process facts (source map re-verified 2026-11-24; re-confirm on the SAGE OS and EGOS pages)

- OS is published by **SAGE for EGOS** (founded 1980; ISSN 0170-8406 print / 1741-3044 online; monthly; FT50 generalist-management list). Submission is via **ScholarOne Manuscripts** at `mc.manuscriptcentral.com/orgstudies`.
- **Review model: double-anonymized** — both author and reviewer identities are concealed. This drives the whole preflight: the manuscript must carry **no identifying information**, and author details go on a **separate title page** uploaded as a distinct file (检索于 2026-06；以官网为准).
- **Length: ≤13,000 words including references and appendices** (检索于 2026-06；以官网为准). This is generous by US standards and signals OS's tolerance for discursive, theoretically-developed prose — but the cap is inclusive of references/appendices, which surprises authors.
- **Abstract: unstructured, ≤300 words** (not a structured abstract) (检索于 2026-06；以官网为准).
- **Keywords: 5–7**, with **four selected from the OS ScholarOne keyword list** and the remainder free (检索于 2026-06；以官网为准).
- **Referencing: APA 7th edition, without exceptions** — OS switched from its SAGE-Harvard-based house style on **14 August 2025** (OS Style and Reference Guide, August 2025 revision; re-verified 2026-11-24；以官网为准).
- Managing editor (EGOS office): Sophia Tzagaraki (osofficek@gmail.com); Editors-in-Chief **John Amis and Tammar B. Zilber** (re-verified 2026-11-24 on the EGOS editors page; Renate Meyer, Paolo Quattrone and Daniel Hjorth are *former* co-EiCs, and EGOS is recruiting a new Co-EiC for a term from September 2027 — confirm the live masthead before naming an editor).
- **No submission fee.** Open-access/APC exact terms are **待核实** — confirm the OA option and any charge on the SAGE OS page before relying on them (checked 2026-06-22).

## Preflight checklist

### Anonymization (double-anonymized review)
- [ ] Manuscript file contains **no author names, affiliations, acknowledgements, or funding** that identify authors
- [ ] **Self-citations neutralized** (cite in third person; no "as we showed in...")
- [ ] Document properties / file metadata stripped of author identity
- [ ] Separate **title page** uploaded with full author details, affiliations, acknowledgements
- [ ] Site/organization identities masked if confidentiality requires (state the masking)

### Format & length
- [ ] Total **≤13,000 words including references and appendices**
- [ ] **Unstructured abstract ≤300 words**
- [ ] **5–7 keywords**, four from the OS ScholarOne list
- [ ] **APA 7th** referencing throughout (OS house rule since 14 Aug 2025)
- [ ] Figures/tables prepared to SAGE artwork specs; legible in greyscale
- [ ] Effect magnitudes/CIs interpreted (quant); data structure + process figures present (qual)

### Declarations & policy
- [ ] Not under review elsewhere; original work; AI not listed as an author (per SAGE policy)
- [ ] Ethics/consent statements for fieldwork; data-availability statement as required
- [ ] Conflict-of-interest and funding statement prepared (on the title page, not the blinded file)
- [ ] OA option / any APC checked on the SAGE OS page (待核实)

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue organization-studies-skills   # from a clone of the AJS repository
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

- Leaving author-identifying self-citations or acknowledgements in the blinded manuscript
- Treating the 13,000-word cap as excluding references/appendices (it does not)
- Submitting a structured abstract or exceeding 300 words
- Fewer than four keywords from the OS ScholarOne list
- Putting funding/COI in the blinded file instead of the title page
- Assuming an APC applies (or doesn't) without checking — mark 待核实

## Output format

```text
【Anonymization】no author info in manuscript; self-cites neutral; separate title page? [Y/N]
【Length】≤13,000 words incl. refs/appendices? [Y/N]
【Abstract】unstructured ≤300 words? [Y/N]
【Keywords】5–7, four from OS ScholarOne list? [Y/N]
【Referencing】APA 7th? [Y/N]
【Declarations】ethics / data / COI / funding on title page? [Y/N]
【Next step】submit via ScholarOne → orgstud-review-process for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
