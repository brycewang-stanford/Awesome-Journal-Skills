---
name: rfs-submission
description: Use when running the final pre-submission preflight for a The Review of Financial Studies (RFS) manuscript — the SFS Editorial Express portal, cover letter, formatting, Internet Appendix, submission fee, and SFS norms. Checks readiness; does NOT write the paper or the rebuttal.
---

# Submission Preflight (rfs-submission)

## When to trigger

- "We submit this week"
- Final check before clicking submit on the portal
- Unsure which files the portal expects (manuscript, IA, cover letter, code/data)

## Portal & process

- RFS submits through the **SFS Editorial Express portal** (editorialexpress.com), reached from sfs.org/review-of-financial-studies/submit-a-paper — **not** ScholarOne or Editorial Manager. Create/verify your account.
- The handling structure is an **Executive Editor (Tarun Ramadorai, LSE, 2024–2027) → handling Editor → referees**. An Editor desk-screens before sending out; many manuscripts never reach referees.
- **Submission fee** (tiered by World Bank income band and SFS membership; schedule effective 8 July 2024, **re-verified 2026-11-23** on sfs.org; the same fees apply to resubmissions): high-income economies **$400 SFS member / $460 non-member**; middle-income (all coauthors resident) **$260 / $320**; low-income **waived**. Desk-reject refund **$200** (high-income) / **$130** (middle-income); an appeal costs **$860**. SFS membership lets you submit to any SFS journal at the member rate, so joining is often cheaper than the non-member differential. The fee is **waived for current-year SFS members on a conditionally accepted paper** and for invited dual submissions (first round); **re-verify the current figures on sfs.org/review-of-financial-studies/submit-a-paper before submitting**.
- **Two RFS-specific on-ramps JF/JFE lack:** (1) **Registered Reports** — Stage 1 design-only review and in-principle acceptance (`rfs-identification`); RFS has run these as dedicated calls, and the OUP Registered Reports page returned 404 on 2026-11-23, so confirm an open RFS call on sfs.org before choosing this route; (2) **dual submission with the SFS Cavalcade** — the conference reviews the paper and forwards it with reviews to RFS *at no charge*; do not also submit it to RFS directly while that is pending. For an invited Cavalcade dual submission, the **first-round fee is waived**.
- **Code-release condition:** RFS requires authors to **publicly release all code** underlying a published paper as a condition of publication. The **Code and Data Sharing Policy** (applies to papers conditionally accepted on/after **1 October 2025**) requires a full replication **package — data (or documented non-public data plus pseudo data), code, README with a Data Availability Statement, and a license** — which the **RFS Data Editors** verify by reproducing the key tables and figures before final acceptance; the package is published in the RFS Dataverse. If you need to withhold code or data, request it **at submission** — name the portions, the withholding period, and the justification, uploaded in Editorial Express Step 4 (do not request exemptions merely for licensed, non-public data).
- **AI assistance:** by submitting, authors take full responsibility for the content under the AFA Code of Professional Conduct and Ethics; AI assistance does not absolve that responsibility (SFS submit page).

## Pre-submission checklist

### Manuscript format
- [ ] Anonymized manuscript PDF (SFS: "must be anonymous"): no author names, affiliations, acknowledgments, or identifying self-citations in the main file
- [ ] Self-citations phrased neutrally ("X (2021) shows" not "in our earlier work")
- [ ] Acknowledgments, grant info, and thanks removed from the blinded file
- [ ] **Cover page PDF** (title; name, affiliation and email of each author; optional acknowledgments) uploaded **separately** from the manuscript PDF
- [ ] Abstract **≤ 100 words** (RFS returns manuscripts whose abstract exceeds 100 words), plus keywords and JEL codes
- [ ] Manuscript **double-spaced, ≤ 28 lines per page, font size ≥ 11** (RFS returns non-conforming files)
- [ ] References in **Chicago Manual of Style author-date** format; every in-text cite is in the list and vice versa
- [ ] Internet Appendix included with author information removed
- [ ] **Alt text underneath every figure caption** (SFS guideline); **no endnotes** (footnotes only); no boilerplate table-of-contents paragraph at the end of the introduction
- [ ] Figures/tables in the format the portal requires (vector figures; high resolution)

### Internet Appendix & data
- [ ] Internet Appendix **inside the manuscript PDF** (SFS: do NOT upload appendices separately), clearly marked, without author names, cross-referenced from the main text
- [ ] **Code and Data Sharing Policy** acknowledged in the portal: replication package (data, code, README, license) will be delivered to the Data Editors at conditional acceptance, OR a withholding/exemption request is uploaded at submission (Step 4)
- [ ] Data and code availability statement drafted; replication package staged

### Cover letter
- [ ] States the question, the contribution, and why it fits RFS (novelty + rigor)
- [ ] Names the most related RFS/JF/JFE papers and the delta
- [ ] Notes any prior presentation / working-paper version / SFS Cavalcade submission
- [ ] Discloses related submissions and conflicts; no concurrent submission at another journal (distinct from the *permitted* RFS–Cavalcade dual submission)
- [ ] If code cannot be released, the reason is stated here (per RFS policy)
- [ ] Suggested and opposed referees prepared (see `rfs-referee-strategy`)

### Administrative
- [ ] Submission fee handled; SFS-member rate used if applicable (high-income $400 member vs. $460 non-member; middle-income $260/$320; low-income waived); waiver checked (conditionally accepted / low-income economy / invited Cavalcade first round)
- [ ] All coauthors approve the submission
- [ ] Contact details current in the Editorial Express account
- [ ] File naming follows portal conventions

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue rfs-skills   # from a clone of the AJS repository
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

- Leaving an identifying self-citation or acknowledgment in the blinded file.
- Submitting without a plan to publicly release code — RFS treats code release as a condition of publication, not an afterthought.
- Paying the non-member fee when SFS membership would have been cheaper and renewable.
- Submitting the IA inside the main PDF instead of as the portal-specified file.
- A cover letter that summarizes the paper but never states the RFS-specific novelty.
- In-text citations that do not match the reference list.

## Output format

```
【Blinding】pass / fixes: [...]
【Format】abstract ≤100 words? double-spaced ≤28 lines, font ≥11? yes/no
【Files staged】anonymized manuscript PDF (IA inside, de-identified) / cover page PDF / disclosures / cover letter if needed
【Abstract+JEL+keywords】complete? yes/no
【Fee】SFS-member rate used (high-income $400/$460; mid $260/$320) / waiver applies? yes/no
【Code-release】replication package planned, or exemption uploaded at submission? yes/no
【Route】standard / Registered Report / SFS Cavalcade dual submission
【Cover letter】states RFS-specific novelty? yes/no
【Next step】rfs-referee-strategy → submit (Editorial Express) → await decision → rfs-rebuttal
```

## Related resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — RFS-style manuscript skeleton (abstract, sections, variable table, references)
- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — finance data sources (CRSP / Compustat / TAQ / WRDS, etc.) and Stata / R / Python packages
