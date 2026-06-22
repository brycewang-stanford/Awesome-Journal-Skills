---
name: devpsych-submission
description: Use when running the final pre-submission preflight for Developmental Psychology (APA) via Editorial Manager — length-tier compliance, the abstract and Public Significance Statement, APA 7th + JARS reporting, masked-review anonymization, the data-availability statement, and preregistration/data DOIs. Final checks; it does not draft content.
---

# Submission Preflight (devpsych-submission)

The last check before submitting through **Editorial Manager** (`editorialmanager.com/dvl`). Three things
sink Developmental Psychology submissions most often: the **developmental claim not being credible** (age
vs. cohort, invariance, attrition), **JARS/length-tier non-compliance**, and **weak transparency**. Verify
volatile specifics (length numbers, abstract ceiling, policy wording, editor) on the official page first.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure what the length tier, abstract, and transparency requirements demand
- Confirming the Public Significance Statement, anonymization, and deposits are in order

## Process facts (verify volatile items on the official page)

- **Publisher:** American Psychological Association (APA). **ISSN:** 0012-1649 (print); 1939-0599 (online).
- **Editor:** Koraly Pérez-Edgar (Penn State; editorship since 2023-01-01) *(web-verified 2026-06-22; re-verify before submission)*.
- **Portal:** **Editorial Manager**, `editorialmanager.com/dvl`.
- **Review:** **masked peer review** available on request — keep author identity out of the manuscript and
  out of shared links; submit a masked copy via a stable link or supplemental material.
- **Length tiers** *(检索于 2026-06；以官网为准)*: ~4,500 words (brief report), ~10,500 (larger report),
  ~15,000 (multi-study / comprehensive longitudinal); length counts cover page, abstract, text,
  references, tables, and figures.
- **Front matter:** APA-style abstract plus a **Public Significance Statement** (2–3 sentences, ~30–70
  words) on the abstract/keywords page.
- **Style:** **APA 7th edition**; **JARS** reporting (JARS-Quant / JARS-Qual / MARS).
- **Transparency:** **TOP** guidelines — data-availability statement, persistent identifiers (DOIs),
  preregistration where applicable, sample-size justification.

## Preflight checklist

### Format & front matter
- [ ] Manuscript within the chosen **length tier** (total counts cover page, abstract, text, refs, exhibits)
- [ ] APA-style **abstract** within the current ceiling; developmental change foregrounded
- [ ] **Public Significance Statement** present: 2–3 plain sentences (~30–70 words)
- [ ] **APA 7th edition** style; tables/figures and references formatted per APA

### Developmental credibility (JARS)
- [ ] Age vs. cohort addressed; change claim matched to the design
- [ ] **Measurement invariance** reported before interpreting change (configural→metric→scalar)
- [ ] **Attrition** analysis + principled missing-data model (FIML/MI)
- [ ] **Sample-size justification** for the change parameter (power/precision)
- [ ] Effect sizes + confidence intervals for major results; full JARS disclosure

### Masked review (if requested)
- [ ] No author names/affiliations in the masked manuscript
- [ ] Repository / preregistration links **anonymized** (e.g., OSF anonymized view; Databrary view link)
- [ ] Identifying file metadata stripped

### Transparency (TOP)
- [ ] **Data-availability statement** present (what is shared / restricted, why)
- [ ] **Data + scripts** deposited with DOIs (or a justified restricted-access archive); reproduce in a
      fresh session
- [ ] Minors'/identifiable data handled per consent/IRB (e.g., permission-based archive)
- [ ] Preregistration linked; confirmatory/exploratory consistent

## Worked micro-example — preflight verdict (illustrative)

Running the three-wave effortful-control package through the gate the night before upload:

```
Tier:       larger research report; total 9,800 / ~10,500 words → PASS
Abstract:   within ceiling; foregrounds within-person growth → PASS
Public Sig: 3 plain sentences, 58 words → PASS
Credibility: scalar invariance reported; FIML + attrition analysis;
            power simulation for the interaction → PASS
Stats:      slope and interaction carry effect sizes + 95% CIs → PASS
Mask:       no names; OSF anonymized-view + Databrary view links;
            PDF metadata stripped → PASS
Transparency: data-availability statement present; data/scripts DOI'd;
            video via Databrary; prereg linked → PASS
Verdict:    ready to upload to Editorial Manager (editorialmanager.com/dvl).
```

## Last-mile failure modes that trigger a return

| Failure | Caught by | Quick fix |
|---------|-----------|-----------|
| Over the length tier | format check | move robustness/full models to online supplemental material |
| No Public Significance Statement | front-matter check | add 2–3 plain sentences (~30–70 words) |
| Trajectory with no invariance test | credibility check | report configural→metric→scalar before change |
| Listwise deletion, real attrition | credibility check | refit with FIML/MI; add attrition analysis |
| OSF/Databrary link reveals author | masking check | switch to anonymized/view links before upload |
| "Data on request," no statement | transparency check | add a data-availability statement + DOIs |

> Volatile specifics (length numbers, abstract ceiling, accepted article types, current editor) change.
> Re-confirm every number above against the journal's current submission guidelines before relying on it.

## Anti-patterns

- Submitting over the length tier instead of using online supplemental material
- Missing or jargon-laden Public Significance Statement
- Interpreting change with no invariance test, or deleting dropouts
- Non-anonymized manuscript or links during masked review
- No data-availability statement / transient links instead of DOIs

## Output format

```
【Tier】within the chosen length limit? [Y/N]
【Front matter】abstract + Public Significance Statement (2–3 sentences)? [Y/N]
【Credibility】age/cohort + invariance + attrition + sample-size justification? [Y/N]
【APA 7th + JARS】style + ES/CI + full disclosure? [Y/N]
【Masked】manuscript + links + metadata anonymized? [Y/N]
【Transparency】data-availability statement + DOIs + preregistration? [Y/N]
【Next】await decision → devpsych-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — the full pre-submission checklist for this venue
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, DOIs, `papaja`, power and SEM tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Developmental Psychology URLs behind every fact in this pack
