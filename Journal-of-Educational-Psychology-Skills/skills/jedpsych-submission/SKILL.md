---
name: jedpsych-submission
description: Use when running the final pre-submission preflight for the Journal of Educational Psychology via Editorial Manager — masked-review anonymization, the 12,000-word format and 250-word abstract, APA 7th-edition style, JARS reporting, and the Transparency and Openness subsection with data/materials/code identifiers. Final checks; it does not draft content.
---

# Submission Preflight (jedpsych-submission)

The last check before submitting through **Editorial Manager** (`editorialmanager.com/edu`). The things
that most often sink a Journal of Educational Psychology submission are **broken masking**, **busting the
word format**, and **incomplete transparency/JARS reporting**. Verify volatile specifics (format numbers,
policy wording, current editor, portal) on the official APA page first (检索于 2026-06；以官网为准).

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure what the format, masking, and transparency requirements demand
- Confirming the abstract, anonymization, Transparency and Openness subsection, and deposits are in order

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** American Psychological Association (APA).
- **Portal:** **Editorial Manager**, `editorialmanager.com/edu` (Word `.docx`, or LaTeX `.tex` zip + PDF).
- **Review:** **masked** — both author and reviewer identities are masked.
- **Length:** manuscripts generally **≤ 12,000 words** (≈ 40 double-spaced pages, **12-pt Times New
  Roman**), **excluding** references, tables, figures, and appendices.
- **Abstract:** **≤ 250 words** on a separate page.
- **Style:** **APA 7th edition** (APA Publication Manual, 7th ed.), double-spaced.
- **Transparency:** a **Transparency and Openness subsection** stating data, materials, and analysis-code
  availability with **persistent identifiers** (or justified unavailability).
- **Standards:** **JARS** (quantitative/qualitative/mixed) and **JARS-REC**; **preregistration encouraged
  but not mandatory** (disclose status, provide links); **Open Science Badges** (Open Data, Open Data with
  Protected Access, Open Materials, Preregistered, Preregistered+Analysis Plan) available with a signed
  disclosure form.
- **Fee / open access:** **no submission fee** (verified 2026-06-22; "submitting a manuscript for peer
  review is free of charge"); peer review is free. Any **post-acceptance open-access / APC** charge is
  set by APA if you choose OA — confirm the current figure on the APA author pages.
- **Types:** primary empirical articles; occasional exceptionally important meta-analyses; single-
  instrument validation studies are typically out of scope.

## Preflight checklist

### Format & abstract
- [ ] Body **≤ 12,000 words** (excluding references, tables, figures, appendices)
- [ ] Abstract **≤ 250 words** on a separate page
- [ ] APA 7th edition, double-spaced, 12-pt Times New Roman; statistics with effect sizes + CIs

### Masked review (anonymization)
- [ ] First page omits author names/affiliations; includes title + submission date
- [ ] No identifying grant numbers, IRB/institution/site/district names
- [ ] Self-citations phrased in the third person (not "our prior work")
- [ ] Repository / preregistration links **anonymized**; file metadata stripped

### Transparency & standards
- [ ] **Transparency and Openness subsection**: data, materials, analysis code availability + DOIs (or
  justified restriction)
- [ ] **Analysis code** deposited; reproduces results in a fresh session
- [ ] **Preregistration** disclosed + linked (if applicable); deviations noted (encouraged, not mandatory)
- [ ] **JARS / JARS-REC** items complete for the design; participant/context reporting done
- [ ] Badge disclosure form signed (if applying for Open Science Badges)

### Design & stats
- [ ] Nesting modeled (multilevel/SEM) where students are nested; cluster-level inference
- [ ] Effect sizes + CIs + educational interpretation for major results
- [ ] Sample-size justification at the right level; full disclosure of exclusions/attrition

## Worked micro-example — preflight verdict (illustrative)

Running the cluster-randomized reading trial through the gate the night before upload:

```
Length:    body 10,840 / 12,000 words (refs/tables/figures excluded) → PASS
Abstract:  236 words; states design (48 classrooms), effect (g = 0.23,
           95% CI [0.06, 0.40]), and the implication → PASS
APA:       7th edition, double-spaced; ES + CI throughout → PASS
Masked:    no names/affiliations; grant# and district name removed; self-
           cites third-person; OSF anonymized-view links; metadata stripped → PASS
Transparency: data (de-identified) + materials + code each have a DOI;
           restricted raw data has an access path; subsection present → PASS
Standards: JARS quantitative + JARS-REC items complete; prereg linked → PASS
Stats:     two-level model, ICC reported, mediation; cluster-level power → PASS
Verdict:   ready to upload to Editorial Manager.
```

## Last-mile failure modes that trigger a return

| Failure | Caught by | Quick fix |
|---------|-----------|-----------|
| Body 13,500 words | length check | move secondary material to online supplement; tighten |
| Abstract 280 words | abstract check | cut to ≤ 250; keep design + effect + implication |
| Grant number / district name visible | masking check | remove all identifying cues before upload |
| "Our previous study showed…" | masking check | rephrase self-citations in the third person |
| "Data available on request" | transparency check | deposit with a DOI or document an access path |
| Clustered data, single-level model | rigor check | refit multilevel; report ICC (route to `jedpsych-data-analysis`) |

> Volatile specifics (exact word/abstract limits, portal, current editor, badge wording) change.
> Re-confirm every number above against the journal's current submission guidelines before relying on it.

## Anti-patterns

- Submitting over the 12,000-word body limit or with a 250+ word abstract
- Identity leaks (names, grant numbers, sites, first-person self-cites) under masked review
- Missing or empty Transparency and Openness subsection
- Incomplete JARS / JARS-REC reporting
- Clustered data not modeled with multilevel/SEM methods

## Output format

```
【Length】body ≤ 12,000 words (excl. refs/tables/figures/appendices)? [Y/N]
【Abstract】≤ 250 words + design + effect + implication? [Y/N]
【APA 7th + double-spaced】[Y/N]
【Masked】names/affiliations/grant#/site/IRB/self-cites/links/metadata? [Y/N]
【Transparency】data + materials + code + DOIs + subsection? [Y/N]
【Standards】JARS / JARS-REC complete; preregistration disclosed? [Y/N]
【Design/stats】nesting modeled; effect sizes + CIs + interpretation? [Y/N]
【Next】await decision → jedpsych-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — the full pre-submission self-check for this venue
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, DOIs, JARS checklists, `papaja`, multilevel/SEM tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official APA Journal of Educational Psychology URLs behind every fact in this pack
