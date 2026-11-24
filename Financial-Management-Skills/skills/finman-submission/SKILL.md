---
name: finman-submission
description: Use when running the final pre-submission preflight for Financial Management (FM) via the FMA portal and ScholarOne — submission fee and membership tiers, format and anonymization rules, and the FMA-specific process quirks. Final checks; it does not draft content.
---

# Submission Preflight (finman-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the FMA form / ScholarOne
- Unsure which fee tier applies and whether membership is bundled
- Confirming format, anonymization, and house-style rules are FM-compliant
- Assembling the files and declarations the FMA→ScholarOne flow expects

## Process facts (检索于 2026-06；以官网为准)

- FM is the **FMA's flagship quarterly**, published by **Wiley** (Online ISSN 1755-053X). Submission begins on the **FMA submissions page**, where you complete a form and pay the fee, and are then **forwarded to ScholarOne** for the manuscript upload.
- **Submission fee (per manuscript; re-verified 2026-11-24 on fma.org/financial-management-submissions — the PhD nonmember tier rose from $280 to $290):** **$250** for professional or PhD **FMA members**; **$350** for professional **nonmembers**; **$290** for PhD **nonmembers**. The $350 and $290 nonmember fees **include a one-year FMA membership** for the submitting author. On a desk rejection the journal **refunds all but $100** of the submission fee; the FMA membership fee is nonrefundable (FM Editorial Philosophy page). (Re-confirm amounts and tiers on the FMA submissions page before submitting.)
- **Editorial criteria:** originality, rigor, timeliness, practical relevance, and quality; the editors target a **median 6–8 week turnaround** including desk rejections and commit to explanatory feedback on every submission.
- **Originality declaration:** manuscripts are reviewed on the understanding they are **not under review elsewhere**, are the authors' **original work**, and have **not been previously published** in whole or in part.
- **Editors (re-verified 2026-11-24 on the fma.org editorial-board page):** Michael Goldstein (Babson College) and Kathleen Kahle (Wake Forest University). Shawn Thomas (University of Pittsburgh) is now listed among past editors (2022–2025). Re-verify the masthead before relying on it in a cover letter.
- **Data and code (FM policy for initial submissions after 1 March 2023):** after acceptance, authors are *encouraged* to provide replication programs (and data, or pseudo-data if restricted) for the Financial Management Dataverse; nothing is required at initial submission.
- **AI use:** authors follow Wiley's guidelines on generative-AI tools; manuscripts under review must not be uploaded to AI tools by reviewers or editors (FM Editorial Philosophy page, re-verified 2026-11-24).
- **Review model / anonymization, abstract word limit, and exact manuscript length limit: 待核实** — these are not confirmed from the official pages in this pack and must be read off the Wiley author guidelines before submission.

## Preflight checklist

### Format & style
- [ ] Manuscript in the format Wiley specifies (PDF or Word) — **confirm on the author guidelines (待核实)**
- [ ] Abstract within the stated word limit — **limit 待核实**
- [ ] Figures and tables prepared to Wiley specs; notes self-contained
- [ ] References in the journal's house style — **confirm exact style (待核实)**
- [ ] If review is anonymous, the manuscript is fully de-identified (no author names, acknowledgments, or self-citation tells) — **blinding model 待核实**

### Files & fees for the FMA→ScholarOne flow
- [ ] Correct fee tier identified (member $250 / professional nonmember $350 / PhD nonmember $290; re-verified 2026-11-24)
- [ ] Payment method ready on the FMA form; note nonmember fee bundles a one-year membership
- [ ] Main manuscript + internet appendix; replication code/data are encouraged after acceptance for the FM Dataverse (not required at submission)
- [ ] Cover letter framing the contribution and the general-interest fit

### Declarations
- [ ] Originality/exclusivity statement (not under review elsewhere; not previously published)
- [ ] Conflict-of-interest / funding disclosure per Wiley policy
- [ ] Author contributions / ORCID as required by Wiley

## The FMA → ScholarOne flow, step by step

The submission path is two-stage and trips up first-time FM authors who expect a single Wiley portal:

1. **Start on the FMA submissions page**, not on ScholarOne directly — you complete a submission form there first.
2. **Pay the fee** at the FMA step, choosing the correct tier; note that the nonmember tiers bundle a one-year membership for the submitting author.
3. **Get forwarded to ScholarOne**, FM's submission partner, where you upload the manuscript files and metadata.
4. **Confirm the manuscript and files arrived in ScholarOne** — the two-stage handoff is where uploads occasionally fail silently.
Skipping the FMA form and trying to go straight to ScholarOne is the most common process error.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue financial-management-skills   # from a clone of the AJS repository
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

- Uploading to ScholarOne without first completing the FMA form and fee step
- Choosing the wrong fee tier (or missing that the nonmember fee includes membership)
- Naming yourself in the manuscript before confirming whether review is anonymous
- Treating the abstract limit, length limit, or citation style as known when they are 待核实
- Submitting work that overlaps a prior publication, breaching the originality declaration

## What to expect after submitting

Set the author's expectations so the wait is read correctly:

- **Fast clock.** The editors target a **median 6–8 week turnaround including desk rejections**, so silence past a couple of months is unusual — but median is not maximum.
- **Desk-reject is common and quick.** With 300+ submissions a year and sub-10% acceptance, a fit/interest desk-reject can come within days; the explanatory note tells you whether to re-target (fit) or revise (execution).
- **Feedback on every submission.** FM commits to explanatory feedback even on rejections — treat it as a free referee read before spending a second fee elsewhere.
- **The fee is per submission.** A rejection means a new fee on resubmission (and the nonmember tiers already bundled a year of membership), so use the feedback before re-engaging.

## Final go / no-go gate

Do not submit if any of these is unresolved: the headline result is still moving; identification's leading alternative is undefended; the abstract does not lead with the finding; the fee tier or anonymization rule is unverified. A fast desk-reject on an avoidable flaw wastes the fee and the clock.

## Output format

```
【Route】FMA form + fee → ScholarOne upload confirmed? [Y/N]
【Fee tier】member $250 / prof nonmember $350 / PhD nonmember $290 (re-verified 2026-11-24) — chosen? [Y/N]
【Format】Wiley format + abstract limit + citation style verified or 待核实
【Anonymization】blinding model confirmed; manuscript de-identified if required (待核实)
【Files】main + internet appendix + data/code per policy? [Y/N]
【Declarations】originality / disclosure / contributions ready? [Y/N]
【Next step】submit → finman-rebuttal when the decision letter arrives
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
