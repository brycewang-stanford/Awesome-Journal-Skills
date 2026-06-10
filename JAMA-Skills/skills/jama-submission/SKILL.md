---
name: jama-submission
description: Use when running the final pre-submission preflight for a JAMA manuscript — word/format limits, required statements, checklist and flow-diagram files, disclosures, and portal steps. Verifies completeness; it does NOT write or analyze content.
---

# Pre-Submission Preflight (jama-submission)

## When to trigger

- "Submitting tomorrow" — last check before the portal
- Unsure which files and statements JAMA's system requires
- Confirming the manuscript matches the article type's limits

> Word counts, reference caps, and exhibit limits change. **Verify every number on JAMA's current Instructions for Authors page**; the items below are durable requirements, not fixed figures.

## Format & limits

- [ ] Manuscript matches the chosen article type and its word limit (verify current number)
- [ ] Abstract follows the JAMA structured headings and word ceiling (verify)
- [ ] Key Points box present where required (Question / Findings / Meaning)
- [ ] References within the cap for the article type; AMA reference style
- [ ] Figures + tables within the exhibit limit (verify)
- [ ] Line numbers and page numbers on the manuscript
- [ ] Title page with full author list, affiliations, corresponding author

## Required statements (in the manuscript)

- [ ] Trial Registration line (trials) with registry + identifier; PROSPERO for reviews
- [ ] IRB/ethics approval and Declaration of Helsinki; informed-consent statement
- [ ] ICMJE authorship + contributorship statement
- [ ] Conflict-of-interest disclosures for all authors
- [ ] Funding source and role of the funder/sponsor
- [ ] Data-sharing statement
- [ ] Access-to-data / statistical-responsibility statement (trials)

## Required uploaded files

- [ ] Main manuscript (with structured abstract, Key Points, body, references)
- [ ] Completed EQUATOR checklist (CONSORT / STROBE / PRISMA / STARD) with item locations
- [ ] Required flow diagram (CONSORT/PRISMA/STARD) as a figure
- [ ] Trial protocol + statistical analysis plan (trials)
- [ ] Cover letter
- [ ] ICMJE COI disclosure forms for each author
- [ ] Tables and figures per the journal's file specs (resolution, format)
- [ ] Supplement / online-only materials if applicable

## Disclosure & integrity

- [ ] Manuscript is original and not under consideration elsewhere
- [ ] Any preprint / prior presentation disclosed
- [ ] Plagiarism / text-overlap self-checked
- [ ] Reporting standard items all locatable in the text

## Portal operation

- Submit through JAMA's editorial-manager-style portal (verify the current URL on the journal site).
- Confirm author order, corresponding author, and ORCID where requested.
- Add suggested / non-preferred reviewers if the portal allows.
- Select the correct article type and category.

## Anti-patterns

- Pasting a generic abstract instead of the JAMA structured one
- Missing the EQUATOR checklist or flow-diagram upload
- Trial Registration line omitted, or registration was retrospective
- COI forms not collected for every author
- Reference style left as another journal's format
- Exhibit/word counts exceeding the article-type limit (because numbers were assumed, not verified)


## Submission pass for JAMA

Run this as a concrete capability pass. First lock the clinical question, patient population, estimand or endpoint, safety/ethics issue, and reporting checklist; then test whether the manuscript addresses clinical reviewers who ask whether the evidence changes patient care, policy, or medical decision-making while satisfying reporting standards.

- **Primary move:** Treat current official instructions as volatile; verify portal, file format, anonymity, length, data, ethics, and disclosure requirements before saying ready.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against NEJM for field-changing clinical medicine, Lancet for global-health breadth, specialty journals for narrower clinical domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Article type + within limits】yes / over: ...
【Structured abstract + Key Points】present
【Required statements】complete / missing: ...
【Checklist + flow diagram uploaded】yes / no
【COI forms for all authors】yes / no
【Cover letter attached】yes / no
【Next step】awaiting decision → jama-peer-review-revision
```

## Resources

- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check across format, statements, files, and integrity
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JAMA manuscript skeleton (structured abstract, Key Points, IMRaD, required statements)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — EQUATOR guidelines, registries, statistics software, and reference/figure tools
