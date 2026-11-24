---
name: asq-submission
description: Use when running the final pre-submission preflight for an Administrative Science Quarterly (ASQ) manuscript — fit, anonymization, format, exhibits, references, and the editorial-system submission. Checks readiness; it does not write or revise the manuscript.
---

# Submission Preflight (asq-submission)

## When to trigger

- "I'm submitting tonight" — the last check before hitting submit
- You are unsure what files and metadata the editorial system requires
- You need a fit + anonymization + formatting sweep

> Volatile specifics (length norms, abstract cap, named editors) change over time. Treat them as durable norms and **verify the current Manuscript Submission Guidelines** at journals.sagepub.com/author-instructions/asq and the live portal at https://mc.manuscriptcentral.com/asq before submitting.
>
> **Fees.** ASQ is a *hybrid* journal with **no submission fee and no mandatory publication fee**. Optional gold open access costs an article processing charge (APC) of **US$3,000**, billed only *after* acceptance if you opt in. Do not budget a submission fee — there is none.
>
> **Reference style: APA.** As of January 2025, ASQ uses **APA style** for in-text citations and the reference list (this changed from its older in-house ASQ style — verify you are on the current APA convention).

## Fit pre-check (do not skip)

- [ ] The manuscript delivers a *surprising theoretical insight about organizations* (not just a finding)
- [ ] The contribution is theoretical, not methodological
- [ ] The phenomenon is in ASQ's wheelhouse (organization theory / sociology of organizations)
- [ ] You can name the conversation it joins and a few recent ASQ articles as anchors
- [ ] If it is a pure conceptual paper with no data, reconsider (AMR may fit better)

## Format

- [ ] Manuscript type selected correctly (research article vs. **book review** — ASQ runs a standing book review section, unusual among top management journals)
- [ ] One key point statable in a single sentence (ASQ: "each manuscript should contain one key point")
- [ ] Title page (with author info) is a **separate** file from the main document
- [ ] Abstract is **200 words or fewer**, jargon-free; keywords drawn from the ASQ ScholarOne keyword list
- [ ] Length near the suggested **35–45 pages of text** (12-pt Times New Roman, double-spaced, 1-inch margins) plus refs/tables/figures; over-long files get **unsubmitted** before review
- [ ] References in **APA style** (ASQ adopted APA in January 2025)
- [ ] Manuscript in **Word or PDF** (Word required later if accepted); supplemental material placed online and anonymized
- [ ] Data & Methods Transparency plan ready (a required ScholarOne item at submission)

## Anonymization (double-blind)

- [ ] Main document contains **no** author-identifying information
  - Self-citations phrased neutrally ("prior work (Author, 2020) shows…"), not "in our earlier study"
  - Acknowledgments, funding, and thanks removed from the main file (placed on the separate title page)
  - Field site / data provider not identifiable if that would reveal the authors
- [ ] File properties/metadata scrubbed of author names and affiliations
- [ ] File names contain no author names

## Exhibits & evidence

- [ ] Qualitative: data-structure figure and data-to-theory/evidence table included
- [ ] Quantitative: descriptives, correlations, and main tables complete and self-contained
- [ ] Every exhibit numbered, titled, noted, and referenced in text
- [ ] Online supplement / appendix prepared if used (interview guide, extra quotes, robustness)

## References & citations

- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Recent and canonical organization-theory works both engaged
- [ ] DOIs/page numbers complete; no "in press" left unresolved if now published

## Editorial system & metadata

- [ ] Account created at ASQ's ScholarOne portal (https://mc.manuscriptcentral.com/asq) — **no submission fee**
- [ ] Cover letter does **not** summarize the paper; it lists prior viewers/conflicts and discloses any data overlap with other work (ASQ's overlap rule is broad)
- [ ] Keywords from the ASQ ScholarOne keyword list; suggested reviewers named in the cover letter (the form no longer accepts them)
- [ ] Declarations done (originality, COPE ethics, data transparency)
- [ ] Not under review elsewhere and **not previously rejected by ASQ** (no resubmissions of rejected papers)

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue asq-skills   # from a clone of the AJS repository
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

- Submitting a thin-theory, sophisticated-method paper to a theory-first journal
- Forgetting to anonymize self-citations, acknowledgments, or file metadata (ASQ review is double-blind)
- A cover letter that summarizes the paper (ASQ says this is not useful) instead of disclosing overlap and conflicts
- Exhibits not self-contained; figures illegible in grayscale
- A bloated manuscript well past ~45 pages — length-to-contribution is an explicit evaluation criterion, and editors will unsubmit it
- Using old in-house ASQ references instead of **APA** (changed January 2025)
- Resubmitting a paper ASQ already rejected (not permitted)

## Output format

```
【Fit】surprising org-theory contribution? (yes/no)
【Anonymization】pass / fixes: [...]
【Format】matches current ASQ/SAGE guidelines? (verify)
【Exhibits】data-to-theory / main tables complete?
【References】in-text ↔ list reconciled?
【System ready】cover letter + metadata + declarations done?
【Next step】asq-review-process (await decision)
```

## Bundled resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check across 8 sections
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — ASQ-style manuscript skeleton for both qualitative and quantitative papers
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — qualitative/quantitative software, data sources, and writing tools
