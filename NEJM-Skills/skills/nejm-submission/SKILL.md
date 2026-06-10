---
name: nejm-submission
description: Use as the final preflight before submitting to NEJM — a complete clinical checklist across significance, registration, reporting guidelines, abstract, statistics, display items, ethics, references, and required files. Bundles a checklist and a clinical cover-letter template.
---

# Submission Preflight (nejm-submission)

## When to trigger

- The manuscript is "done" and you're about to upload.
- You want a single gate that confirms every other nejm-* skill's output landed.
- A revision is going back and you need to confirm nothing regressed.

## Master preflight checklist

### Significance & venue
- [ ] Clears the practice-changing / clinical-impact bar (`nejm-fit` rung ≥ 4; all three gates).
- [ ] Patient-important primary outcome (not surrogate-only).
- [ ] Article type chosen (Original Article / Brief Report) and within its length/reference caps.

### Registration, protocol & SAP
- [ ] Trial **prospectively registered** (ClinicalTrials.gov / WHO ICTRP) before enrollment; **registration number** in hand.
- [ ] Registered primary outcome matches the reported primary outcome.
- [ ] **Protocol** and **statistical analysis plan** finalized, dated, and ready as a supplement.

### Reporting guidelines
- [ ] Correct EQUATOR guideline (CONSORT / STROBE / PRISMA, + any extension) with completed checklist.
- [ ] **CONSORT participant flow diagram** (RCT) / PRISMA selection diagram (SR-MA) present.
- [ ] Flow-diagram numbers reconcile with Table 1 and the analysis populations.

### Abstract
- [ ] Structured, four sections (Background / Methods / Results / Conclusions), ≤250 words.
- [ ] Primary outcome with **effect estimate + 95% CI**; ITT and per-group n stated.
- [ ] **Registration number** and **funding source** in the abstract.

### Statistics
- [ ] CIs reported with effect estimates (not P alone); exact P values.
- [ ] ITT primary analysis; per-protocol as sensitivity (both for non-inferiority).
- [ ] Multiplicity controlled; exploratory endpoints labeled.
- [ ] Subgroups pre-specified with interaction tests (forest plot).
- [ ] Absolute risk + NNT alongside relative measures; missing-data handling stated.

### Display items
- [ ] Table 1 by group, **no baseline P values** (standardized differences if used).
- [ ] Kaplan–Meier with **numbers-at-risk**; forest plots for subgroups/meta.
- [ ] Figures de-identified; CIs shown; colorblind-safe; standalone legends.

### Ethics & integrity
- [ ] IRB/ethics approval + informed consent stated; Declaration of Helsinki / GCP.
- [ ] **ICMJE disclosure forms** for all authors; competing-interests statement.
- [ ] ICMJE **authorship criteria** met; contributors acknowledged; medical writers disclosed.
- [ ] **Role-of-the-funding-source** statement; data access/vouching for sponsored trials.
- [ ] **Data-sharing statement** (ICMJE) — what / when / to whom / how.

### References
- [ ] Vancouver / ICMJE numbered style, ordered by appearance.
- [ ] First six authors then et al.; NLM journal abbreviations; within reference cap.
- [ ] All in-text superscript numbers resolve; no gaps/duplicates.

### Required files & metadata
- [ ] Main text (title page, structured abstract, IMRAD, references).
- [ ] Figures + legends; tables (incl. Table 1) and the CONSORT flow diagram.
- [ ] Supplementary appendix: **protocol + SAP**, supp tables/figures.
- [ ] Cover letter (clinical importance + what's practice-changing).
- [ ] Authors, affiliations, ORCIDs, corresponding author; CRediT/contributions.
- [ ] Completed reporting checklist (CONSORT/STROBE/PRISMA).
- [ ] Disclosure forms; data-sharing statement; funding statement.

## Final integrity sweep

- [ ] No over-claiming beyond the evidence (re-read abstract Conclusions and Discussion).
- [ ] Causal language only where the design supports it (cautious for observational).
- [ ] Registration number, denominators, and primary-outcome numbers consistent across abstract, text, tables, and flow diagram.
- [ ] Single-blind convention assumed unless instructed otherwise (confirm).

## Templates

- `templates/checklist.md` — copyable clinical preflight checklist.
- `templates/cover_letter_template.md` — clinical cover-letter scaffold.


## Submission readiness pass for New England Journal of Medicine

Use this as a second-pass capability check. First lock the clinical question, population, endpoint, effect size, safety signal, and practice implication; then test whether the manuscript addresses clinical-medicine reviewers who expect practice-changing evidence, patient relevance, safety, and exact reporting discipline.

- **Primary move:** Verify portal, article type, anonymity, declarations, files, data/code, and current source-map facts; return blockers before formatting advice.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JAMA for broad clinical medicine, Lancet for global-health/public-health reach, specialty journals for narrower disease domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Blocking gaps】 [...]  (must fix before upload — e.g., unregistered trial, missing CONSORT diagram)
【Warnings】 [...]       (should fix)
【Files ready】 main / figures+tables / CONSORT diagram / protocol+SAP / cover letter / disclosures / data-sharing
【Verdict】 GO / NO-GO + the top 3 fixes
【Next】 submit | nejm-rebuttal (after decision)
```

## Anti-patterns

- **Do not** upload a trial that was never prospectively registered without flagging it as a blocker.
- **Do not** submit an RCT without the CONSORT flow diagram and completed checklist.
- **Do not** omit the data-sharing statement or the role-of-the-funding-source statement.
- **Do not** rely on memory; run the checklist top to bottom.
