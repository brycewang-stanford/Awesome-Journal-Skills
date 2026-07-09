---
name: percom-submission
description: Use when auditing an IEEE PerCom research-track submission for HotCRP readiness, covering the mandatory paper-registration step, the IEEEtran 9+1 two-column page budget, double-blind anonymization, the open-data / human-subjects plan, IEEE Xplore publication, and desk-reject triage before the AoE cutoff.
---

# PerCom Submission

Run this audit before uploading to the PerCom HotCRP site (`percom2027.hotcrp.com` for the current
cycle). PerCom research papers publish in **IEEE Xplore** and are reviewed **double-blind**, so the
submission must be both anonymous and complete on its own — the bounded rebuttal cannot add new
experiments later. Every number below was read from the PerCom 2027 Call for Papers and Dates pages
on 2026-07-09 via search renderings of the `percom.org` URLs (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first.

## The two-step deadline

PerCom separates **paper registration** from **paper submission**, and both are AoE:

- **Registration** locks in title, abstract, authors, and topic areas about a week early (PerCom
  2027: **4 September 2026**). Miss it and the system will not accept the PDF later.
- **Submission** uploads the anonymized PDF (PerCom 2027: **11 September 2026**, 23:59 AoE).

Register with the *real* title and abstract, not a placeholder — the abstract drives TPC bidding,
and a registered abstract that diverges from the final paper quietly worsens your reviewer match.

## Format and page budget

- **IEEEtran, `\documentclass[10pt, conference, compsocconf]{IEEEtran}`**, US-letter, two-column —
  the IEEE Computer Society conference format. This is the IEEE path, not ACM `acmart`.
- **Page budget (verify per cycle):** **at most 9 pages** of technical content — text, figures,
  tables, and appendices all count — **plus up to 1 additional page for references only**. There is
  no unlimited appendix inside the paper; anything reviewers must read to judge it lives in the 9.
- Margins, font, and column geometry are fixed by the template; **editorial compression, not
  template tampering, is how you recover space.** A shrunk font or narrowed margin is a named
  desk-reject ground at IEEE venues.

## Double-blind sweep

PerCom runs **double-blind** review: authors anonymize in good faith and **cite their own prior
work in the third person** (do not omit it — omission is itself a tell). Because ubicomp papers
lean on datasets, testbeds, and deployments, the leak surface is wide:

```bash
# Mechanical pass on the submission PDF and any anonymized dataset/artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|ieee-dataport|zenodo\.org/record|acknowledg|IRB|university' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
grep -rni 'our (lab|testbed|deployment)|@[a-z0-9.]*\.edu' artifact/ --include='*.md' | head
```

The ubicomp-specific leaks: a testbed or smart-home named after your lab, a photo of the sensor
rig showing a building or a face, a dataset link pointing at a personal repository, an IRB protocol
number tied to your institution, and a "we deployed in our department" phrasing. Re-host datasets
behind an anonymizing link *before* upload.

## Open data and human subjects at submission time

PerCom's community expects a credible data story and, for human-subjects sensing, an ethics story:

- State an **open-data plan**: what dataset exists, whether/where it will be released after
  acceptance, and — for anything you cannot share (privacy, IRB limits) — exactly why.
- Provide an **anonymized** dataset/code link or upload anonymized material for the reviewers.
- State **IRB/ethics approval and consent** for human-subjects data collection, and the
  de-identification done — a missing ethics note is a scored weakness, not a neutral omission.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Over 9 pages of technical content | Desk-reject-grade | Cut or move to the dataset/artifact; the reference page does not absorb body text |
| Template altered (10pt/`compsocconf` changed, margins, shrunk font) | Named desk-reject ground | Recompile clean, recover space editorially |
| Identity leak in PDF, dataset link, testbed name, or a photo | Anonymity violation | Re-anonymize and re-host; scrub PDF metadata |
| Own prior work omitted for "anonymity" | Double-blind done wrong | Restore the citation in the third person |
| Abstract/authors not registered by the earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| No open-data plan, no ethics note for human data | Scored against the paper | Add the plan + IRB/consent statement |
| Same study under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Freeze the body early; references can churn, the argument cannot.
2. Register title/abstract/authors/topics well before the registration cutoff.
3. Build the anonymized dataset/artifact link and place the open-data plan and ethics note in the
   paper.
4. Run the mechanical anonymity checks on the *final* PDF and the *final* archive, not drafts.
5. Fill every HotCRP field — topics that match your evidence, conflicts for every coauthor's
   institution and recent collaborators — a day early; late conflicts are the classic midnight
   failure.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The exact dates, the rebuttal window, and the early-rejection wording.
- The page budget and the required IEEEtran options (PerCom 2027 posts 9+1 with `compsocconf`).
- WiP/demo/industry/workshop deadlines (separate), dual-submission wording, whether a
  reproducibility track runs, and any AI-disclosure rule — all cycle-volatile.

## Output format

```text
[PerCom submission status] ready / blocked / needs work
[Registration] title/abstract/authors/topics locked by the earlier deadline? yes/no
[Format] pages used (body/refs), IEEEtran compsocconf compliance
[Anonymity] clean / leaks: <where>
[Open data + ethics] dataset link present? open-data plan? IRB/consent stated?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
