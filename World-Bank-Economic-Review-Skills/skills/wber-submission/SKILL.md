---
name: wber-submission
description: Use when running the final pre-submission preflight for The World Bank Economic Review (WBER) via the ScholarOne ManuscriptCentral portal — the 40-page total cap, single-anonymized title page, abstract/JEL, data availability statement with DOI, and house format. Final checks; it does not draft content.
---

# Submission Preflight (wber-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on ManuscriptCentral
- Unsure which files and format rules the WBER portal expects
- Confirming the 40-page cap, single-anonymized title page, and data availability statement are in order
- Deciding between the full-length and short-format track

## Process facts (检索于 2026-06；以官网为准)

- WBER is published by **Oxford University Press for the World Bank**; submission is through the **ScholarOne ManuscriptCentral** portal (`mc.manuscriptcentral.com/wber`), as **PDF**.
- **Editors (verified 2026-06-22): Eric Edmonds and Nina Pavcnik (both Dartmouth College)**, with co-editors including Leora Klapper, David McKenzie, Emanuela Galasso, Norman Loayza, and Roy van der Weide. Re-verify on the OUP editorial-board page before naming an editor.
- **Length cap:** standard submissions **must not exceed 40 pages total**, at 12-point font, double-spaced, Times New Roman (or similar), one-inch margins — and the 40 pages **include all content subject to review**: tables, figures, references, footnotes, and appendices. (Confirm the current limit on the OUP author guidelines.)
- **Review model:** **single-anonymized** — only referees are anonymous. **Author names and affiliations go on the title page.** Do not blind the manuscript as if it were double-blind.
- **Data availability statement:** required on the title page / author-affiliation footnote, with a **persistent (preferably DOI) link** to the data in a repository. Public release of data and code is a **condition of publication**.
- **Tracks:** WBER publishes full-length articles **and short-format papers** (timely, policy-relevant, rigorous). Choose the track deliberately.
- **Editorial independence:** consistency with World Bank policy plays no role in selection — do not pitch the paper as endorsing a Bank position.
- **Abstract length, exact JEL/keyword rules, fees/APC, and reference style** are **待核实** — confirm on the live author guidelines before submitting.

## Preflight checklist

### Format & length
- [ ] One **PDF**; font **12 point**; **double spaced**; Times New Roman or similar; **one-inch margins**
- [ ] **≤40 pages total**, counting tables, figures, references, footnotes, and appendices
- [ ] Figures/tables legible at print size; notes self-contained (source, estimator, clustering, units)
- [ ] **No significance asterisks**; standard errors / confidence intervals reported

### Title page & front matter
- [ ] **Author names + affiliations on the title page** (single-anonymized — not blinded)
- [ ] **Data availability statement with a persistent DOI link** in the affiliation footnote
- [ ] Abstract present (word limit 待核实); keywords and JEL codes (rules 待核实)
- [ ] Track chosen: full-length vs. short-format

### Files & policy
- [ ] Data + code package prepared (or restricted-data access path + synthetic extract documented)
- [ ] Field instruments included for own-data studies
- [ ] Cover letter names the development question, the magnitude, and "why WBER"
- [ ] Confirmed not under review elsewhere; conflicts/funding disclosed; AI not listed as an author

## Last decisions before you press submit

- **Track:** full-length vs. short-format — confirm the paper's scope matches the track and you are not padding or amputating.
- **Cover letter:** does it open with the development question and the policy decision, state the headline magnitude, name the identification in one line, and answer "why WBER, not JDE/World Development/Research Observer"?
- **Suggested reviewers (if the portal asks):** span both the identification and policy archetypes; disclose genuine conflicts.
- **Disclosures:** funding, conflicts, and the confirmation the paper is not under review elsewhere; AI is not an author.
- **Data availability:** the statement and DOI link are *in the manuscript*, not just promised — public release of data and code is a condition of publication, so the deposit should exist before submission, not after acceptance.
- **Final read of the PDF:** exhibits legible at print size, no broken cross-references, page count confirmed ≤40.

## Anti-patterns

- Blinding the manuscript as if review were double-blind (it is single-anonymized; names go on the title page)
- Exceeding 40 pages because appendices/references were assumed not to count — they do
- Submitting with no data availability statement or no DOI repository link
- Significance asterisks instead of standard errors / confidence intervals
- Pitching the paper as aligned with World Bank policy (selection is independent)
- Padding a clean single-result paper into a full article when the short-format track fits
- A cover letter that restates the abstract and never says "why WBER"
- Promising the data/code deposit "at acceptance" rather than having it ready at submission

## Why papers get returned before review

The fastest WBER rejections rarely concern the science — they concern fit and format the editor screens in minutes: a rich-country setting (out of scope), a survey better suited to the Research Observer, an over-length manuscript that ignored the 40-page cap, a missing data availability statement, or a blinded manuscript that mistook the review model. Clearing this preflight does not guarantee review on the merits, but failing it guarantees a return without review. Treat the preflight as the gate that gets your paper *to* the referees, not as the review itself.

## Worked preflight (illustrative)

A paper is "ready" at 46 pages because the authors assumed the appendix and references did not count toward the limit. The WBER preflight catches it: the 40-page cap **includes** tables, figures, references, footnotes, and appendices, so they move four secondary specification tables and a long data-construction note to a supplementary file, trimming the main PDF to 39 pages. They then notice the manuscript was blinded (author names stripped) as if for double-blind review — wrong model; WBER is single-anonymized, so they restore names and affiliations on the title page and add the data availability statement with the openICPSR DOI in the affiliation footnote. Asterisks in two tables are replaced with standard errors. Only then do they upload to ManuscriptCentral.

## Output format

```text
【Format】PDF / 12pt / double-spaced / 1in margins? [Y/N]
【Length】≤40 pages total incl. tables/figures/refs/appendices? [Y/N]
【Title page】author names + affiliations (single-anon)? [Y/N]
【DAS + DOI】data availability statement with persistent link? [Y/N]
【Abstract/JEL】present (limits 待核实)? [Y/N]
【Exhibits】no asterisks; SE/CI reported? [Y/N]
【Track】full-length / short-format chosen
【Cover letter】question + magnitude + why-WBER? [Y/N]
【Next step】submit via ScholarOne → wber-rebuttal after the decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official OUP / WBER URLs and volatile facts
