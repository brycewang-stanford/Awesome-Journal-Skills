---
name: rfs-submission
description: Use when running the final pre-submission preflight for a The Review of Financial Studies (RFS) manuscript — ScholarOne/Manuscript Central portal, cover letter, formatting, Internet Appendix, fee, and SFS norms. Checks readiness; does NOT write the paper or the rebuttal.
---

# Submission Preflight (rfs-submission)

## When to trigger

- "We submit this week"
- Final check before clicking submit on the portal
- Unsure which files the portal expects (manuscript, IA, cover letter, code/data)

## Portal & process (verify current details on the RFS site)

- RFS uses **Manuscript Central / ScholarOne** for submissions. Create/verify your account and ORCID.
- There is typically a **submission fee** and **SFS-related norms** (e.g., membership/discipline expectations). The exact amount and conditions change — **verify the current fee and policy on the official RFS page before submitting**; do not assume a number.
- Expect a **demanding multi-round review** with an editor and multiple referees.
- Do not assert current named editors or exact fees here — confirm them on the journal site at submission time.

## Pre-submission checklist

### Manuscript format
- [ ] Anonymized for double-blind review: no author names, affiliations, or identifying self-citations in the main file
- [ ] Self-citations phrased neutrally ("X (2021) shows" not "in our earlier work")
- [ ] Acknowledgments, grant info, and thanks removed from the blinded file
- [ ] Title page with author info uploaded as a **separate** file (per portal instructions)
- [ ] Abstract, keywords, and JEL codes present and within limits
- [ ] References complete and consistently formatted; every in-text cite is in the list and vice versa
- [ ] Figures/tables in the format the portal requires (vector figures; high resolution)

### Internet Appendix & data
- [ ] Internet Appendix prepared as a separate file, cross-referenced from the main text
- [ ] Data and code availability statement consistent with current RFS policy (verify)
- [ ] Replication package staged if/where required

### Cover letter
- [ ] States the question, the contribution, and why it fits RFS (novelty + rigor)
- [ ] Names the most related RFS/JF/JFE papers and the delta
- [ ] Notes any prior presentation / working-paper version
- [ ] Discloses related submissions and conflicts; no dual submission
- [ ] Suggested and opposed referees prepared (see `rfs-referee-strategy`)

### Administrative
- [ ] Submission fee handling confirmed (amount/policy verified on site)
- [ ] All coauthors approve the submission
- [ ] ORCID and contact details current in ScholarOne
- [ ] File naming follows portal conventions

## Anti-patterns

- Leaving an identifying self-citation or acknowledgment in the blinded file.
- Assuming last year's fee or data policy still applies — RFS norms change; verify.
- Submitting the IA inside the main PDF instead of as the portal-specified file.
- A cover letter that summarizes the paper but never states the RFS-specific novelty.
- In-text citations that do not match the reference list.

## Output format

```
【Blinding】pass / fixes: [...]
【Files staged】manuscript / title page / IA / cover letter / code
【Abstract+JEL+keywords】complete? yes/no
【Fee & SFS policy】verified on site? yes/no
【Cover letter】states RFS-specific novelty? yes/no
【Next step】rfs-referee-strategy → submit → await decision → rfs-rebuttal
```

## Related resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — RFS-style manuscript skeleton (abstract, sections, variable table, references)
- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — finance data sources (CRSP / Compustat / TAQ / WRDS, etc.) and Stata / R / Python packages
