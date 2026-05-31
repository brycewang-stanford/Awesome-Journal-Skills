---
name: smj-submission
description: Use when running the final pre-submission preflight for a Strategic Management Journal (SMJ) manuscript via ScholarOne — format, anonymization, files, and cover letter. Checks readiness; it does not write the paper or the rebuttal.
---

# Submission Preflight (smj-submission)

## When to trigger

- "I'm submitting tomorrow"
- Final check before clicking submit in ScholarOne Manuscripts
- Unsure which files and metadata the system needs
- Preparing the cover letter and reviewer suggestions

## Before anything: verify the live guidelines

SMJ is published by **Wiley on behalf of the Strategic Management Society (SMS)**. Submissions are handled through Wiley's workflow; legacy submissions and tracking live at **ScholarOne Manuscript Central (mc.manuscriptcentral.com/smj)**. Per the SMJ Author Instructions (last updated 23 May 2025), there is **no submission fee** (verify) — open access via Wiley OnlineOpen is optional and only applies after acceptance. Page limits, fee/open-access options, and required statements are periodically updated. **Verify the current Author Guidelines on the official SMJ page** before submitting — do not rely on remembered numbers. Use this skill for the durable process; confirm volatile specifics yourself.

## Manuscript readiness

- [ ] Structure complete: intro, theory & hypotheses, methods, results, discussion, references
- [ ] Contribution to strategy theory is explicit in the introduction
- [ ] Endogeneity / identification is addressed in the body (the most-scrutinized element)
- [ ] **Two abstracts**: a *research summary* (≤125 words, stands alone, no citations) **and** a *managerial summary* (≤125 words, plain practitioner language). This dual-abstract requirement is distinctive to SMJ — AMJ/ASQ require only one abstract
- [ ] **Five (5) keywords** selected; manuscript length within current guidelines (full articles ~40 pages incl. tables/figures/references; short research articles ~20 pages — verify)
- [ ] Tables/figures self-contained; secondary material in an online supplement
- [ ] References in **APA author-date** style (e.g., "(Collins, 2005a, 2005b)"); every in-text cite appears in the list and vice versa

## Anonymization (double-blind)

SMJ uses double-blind review. Before upload:

- [ ] Author names, affiliations, and acknowledgments removed from the manuscript file
- [ ] Self-citations phrased neutrally ("prior work shows (Author, 2021)"), not "in our earlier paper"
- [ ] Funding/acknowledgment details placed only where the system requests them, not in the main file
- [ ] File metadata/properties scrubbed of author identity
- [ ] File names contain no author or institution names
- [ ] No identifying data-provider or proprietary-dataset language that reveals the team

## Files & metadata in ScholarOne

- [ ] Anonymized main manuscript (with embedded or separate exhibits per guidelines)
- [ ] Title page with author details (separate, non-anonymized) if required
- [ ] Cover letter (see below)
- [ ] Online appendix / supplementary materials, if any
- [ ] Any required statements (data availability, conflict of interest, ethics) — confirm current requirements
- [ ] Suggested reviewers (and any opposed reviewers), if the system invites them
- [ ] Correct article type selected (Article vs. Research Note / short article vs. special issue)

## Cover letter

- Brief: state the title, the strategy contribution in 2–3 sentences, and why **SMJ** (not the SMS siblings SEJ or GSJ) is the right outlet.
- Confirm the work is original, not under review elsewhere, and that all authors approve.
- Note any special-issue call you are responding to.
- Do not oversell or summarize the whole paper; a Co-Editor screens it first and an action editor reads the manuscript.

## Anti-patterns

- Submitting one abstract when SMJ requires both a research summary and a managerial summary
- Leaving author identity in metadata or acknowledgments under double-blind review
- A reference list still in a default citation-manager style, not APA author-date
- A cover letter that pitches generic "management" relevance instead of the strategy (competitive-advantage / performance) contribution
- Forgetting required statements (data availability / conflicts) the system mandates
- Routing an entrepreneurship- or internationalization-first paper to SMJ when SEJ or GSJ fits better

## Output format

```
【Guidelines verified on official page】yes / TO DO
【Dual abstracts】research summary [n≤125] / managerial summary [n≤125]
【Keywords】[5]
【Anonymization】pass / fix: [...]
【Files staged】main, title page, cover letter, supplement, statements
【Reference style】APA author-date conformed / fix
【Article type】Article / Research Note / special issue: [name]
【Reviewer suggestions】[n]
【Next step】smj-review-process (then smj-rebuttal on decision)
```

## Templates & resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check (format, anonymization, identification, files, cover letter)
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — SMJ-style manuscript skeleton (research + managerial summary, hypotheses, variable table, identification section, APA references)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — strategy data sources (Compustat / CRSP / SDC / BoardEx / Orbis / patents) and Stata / R / Python packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official SMJ/SMS/Wiley URLs and what each verifies (editors, dual abstracts, page limits, reference style)
