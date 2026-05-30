---
name: jfe-submission
description: Use when running the final pre-submission preflight for a Journal of Financial Economics (JFE) manuscript — formatting, anonymity, references, exhibits, code/data deposit, the editorial system, and the submission fee. Checks submission readiness; it does not revise the science.
---

# Submission Preflight (jfe-submission)

## When to trigger

- "We are submitting this week"
- Final check before pressing submit in the editorial system
- Unsure which files and statements the system requires

## Pre-submission checklist

### Manuscript & format
- [ ] Title page separate from the anonymized manuscript (verify the journal's current anonymity policy)
- [ ] Abstract concise and result-forward; JEL codes and keywords included
- [ ] Sections, tables, and figures numbered consistently; every in-text reference resolves
- [ ] Equations numbered; notation consistent throughout
- [ ] Reference style matches the journal's current author guidelines

### Anonymity (verify current policy on the official page)
- [ ] No author-identifying content in the manuscript body
- [ ] Self-citations phrased neutrally, not "in our prior work"
- [ ] Acknowledgments and funding moved off the anonymized file
- [ ] File metadata (document properties) scrubbed of author names

### Exhibits & Internet Appendix
- [ ] Main-text exhibits triaged; the long tail is in the Internet Appendix
- [ ] Every "untabulated" / "see Internet Appendix" pointer resolves
- [ ] Internet Appendix self-contained and numbered in its own IA series

### Code & data deposit
- [ ] Replication code and data prepared per the journal's current data-availability policy (verify)
- [ ] Data sources and access restrictions documented
- [ ] A reader could in principle reproduce the headline tables from the deposit

### References
- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Recent top-3 finance work on the topic is cited
- [ ] No broken DOIs / incomplete entries

### Editorial system & fee
- [ ] Submit via the journal's editorial system (verify current portal)
- [ ] Submission fee handled — confirm the current amount and any waivers on the official page
- [ ] Cover letter states the contribution and fit briefly; suggested/opposed referees as the system allows
- [ ] Conflict-of-interest and prior-presentation disclosures completed

## Submission-system pointers

- Confirm the current submission portal, file-size limits, and accepted formats on the journal's official page before uploading.
- Have the anonymized manuscript, title page, Internet Appendix, and code/data ready as separate files.
- Double-check that the version uploaded is the final one (not a tracked-changes draft).

## Anti-patterns

- Submitting a manuscript whose metadata still names the authors
- "See Internet Appendix" pointers that go nowhere
- Forgetting the submission fee or assuming last year's amount
- Reference list still in a foreign journal's default style
- Uploading a draft with visible tracked changes or comments
- No code/data deposit prepared when the policy requires one

## Output format

```
【Anonymity】pass / fix: [...]
【Exhibits + IA】pointers resolve? yes/no
【Code/data deposit】ready? (per current policy)
【References】in-text == list? yes/no
【Fee & portal】confirmed on official page? yes/no
【Cover letter】contribution + fit stated? yes/no
【Next】await decision -> jfe-referee-strategy (pre-empt) / jfe-rebuttal (on R&R)
```

## Resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JFE-style manuscript skeleton (abstract, variable-definition table, exhibit and reference conventions)
- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check across format, anonymity, exhibits, code/data, references, and system
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — finance data sources (CRSP / Compustat / TAQ / WRDS) and Stata / R / Python packages
