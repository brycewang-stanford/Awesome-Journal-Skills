---
name: amann-submission
description: Use when running the final pre-submission preflight for an Academy of Management Annals (Annals) proposal or invited full review via the Manuscript Central portal — proposal-vs-invited-review route, deadlines, formatting, CV, and anonymity. Final checks; it does not draft content.
---

# Submission Preflight (amann-submission)

## When to trigger

- A deadline is near — last check before uploading a proposal to Manuscript Central
- A proposal was accepted and you are submitting the invited full review
- Confirming format, CV, and anonymity requirements for the right route
- Unsure which files the portal expects for a proposal vs. a full review

## Process facts (source map re-verified 2026-11-24；以官网为准 — re-confirm on the AOM/Annals pages)

- **Publisher / venue.** Annals is the Academy of Management's review-of-the-field journal, published by the **Academy of Management** on its own platform (journals.aom.org) — the official AOM pages re-read 2026-11-24 make no mention of Taylor & Francis. It is distinct from AMR (original theory) and AMJ (empirical). Submission is via **Manuscript Central**: `https://mc.manuscriptcentral.com/aomannals`.
- **Two routes, in order.** (1) **Proposal** — the mandatory gate: **≤5 pages, single-spaced, 1-inch margins, 12pt**, with the four headings (Focus of the review / Related reviews / Review scope and process / New insights); references and visuals do not count. (2) **Invited full review** — submitted only after a proposal is accepted; typically **~50 pages** of text plus tables/figures/refs.
- **Deadlines.** Proposals are on a twice-yearly cycle — **April 1 and October 1**; not reviewed until the deadline passes; decisions **~6 weeks after** the deadline. Two issues publish per year (January and July).
- **Anonymity.** **Proposals are double-blind** (reviewed by the Associate Editors) — anonymize the proposal. The **invited full review forgoes double-blind** (read by the Associate Editor and Editor), so anonymity requirements differ between the two routes — confirm current rules on the portal.
- **CV.** A current CV may be required for the **editors' eyes only** (not seen by reviewers) — confirm at submission (待核实).
- **Style / format.** Follow the **AOM Editorial Style Guide** (Word file, Times New Roman 12 pt, double-spaced body; abstract **≤200 words** with the title on page 2; footnotes, not endnotes; three levels of bold headings; title page only for accepted papers) — re-verified 2026-11-24 on aom.org. The proposal itself follows the proposal rules above (single-spaced).
- **AI policy.** Work must be the authors' own; disclose any AI use **in the cover letter and in the article acknowledgements**, and confirm you have read AOM's AI policy (re-verified 2026-11-24).
- **Cover letter.** Not required, but recommended (Manuscript Central directions, re-verified 2026-11-24).
- **Fees / APC.** **AOM does not charge any fees for author submissions** (re-verified 2026-11-24; beware predatory sites claiming to act for Annals — submit only via `mc.manuscriptcentral.com/aomannals`). Any OA charge for an accepted article is 待核实; do not assert an amount.

## Preflight checklist

### Route & files
- [ ] Route chosen: **proposal** (≤5pp, four headings) **or** **invited full review** (after acceptance)
- [ ] Proposal uses the four required headings verbatim and meets the ≤5pp / single-spaced / 1-in / 12pt limit
- [ ] Targeting the correct April 1 / October 1 deadline
- [ ] Full review (if invited) within the expected ~50-page norm; tables/figures/refs prepared

### Front matter
- [ ] Title, abstract (review-style — contribution to the field), and keywords present
- [ ] Author affiliations complete; CV prepared if required (editors-only)

### Anonymity & declarations
- [ ] Proposal anonymized for double-blind review (proposal route)
- [ ] Full-review anonymity handled per current rules (it forgoes double-blind)
- [ ] Confirmed not under review elsewhere (and no earlier Annals proposal on the same literature); AI not listed as an author; any AI use disclosed in cover letter + acknowledgements

### Volatile re-confirms
- [ ] Portal specifics, CV requirement, OA charge — re-checked on AOM/Annals pages (portal, no-fee rule, house style and anonymity re-verified 2026-11-24)

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue academy-of-management-annals-skills   # from a clone of the AJS repository
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

- Uploading a full review without an accepted proposal — out of process at Annals
- A proposal that exceeds 5 pages or omits one of the four required headings
- Missing the April 1 / October 1 window because intake was assumed to be rolling
- Asserting a fee/APC or editor name from memory rather than the live page
- Failing to anonymize the proposal (it is double-blind) or mishandling the full-review anonymity difference
- A primary-paper abstract on a review submission

## Output format

```text
【Route】proposal (≤5pp, 4 headings) / invited full review (~50pp)
【Deadline】targeting April 1 / October 1? <which>
【Proposal headings】Focus / Related reviews / Scope & process / New insights present? Y/N
【Anonymity】proposal anonymized (double-blind); full-review rule confirmed? Y/N
【CV】prepared if required (editors-only)? Y/N
【Volatile re-confirms】portal / fee / style / anonymity checked on AOM page? Y/N
【Next step】submit via Manuscript Central → amann-review-process for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
