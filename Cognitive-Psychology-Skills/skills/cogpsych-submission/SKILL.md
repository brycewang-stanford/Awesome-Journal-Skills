---
name: cogpsych-submission
description: Use when running the final pre-submission preflight for Cognitive Psychology (Elsevier) via Editorial Manager — scope/length fit, abstract and keywords, APA-style reporting, model-comparison completeness, reproducible model/analysis code, and the Elsevier research-data and competing-interest declarations. Final checks; it does not draft content. Verify volatile specifics on the official guide for authors.
---

# Submission Preflight (cogpsych-submission)

The last check before submitting through **Elsevier Editorial Manager**. Two things sink Cognitive
Psychology submissions most often: a **wrong-shape contribution** (single effect, no model/theory, or a
model that is never compared) and **non-reproducible modeling** (fits that can't be regenerated, no code
deposit). Verify volatile specifics (length, abstract limit, review model, current editor, declarations)
on the official guide for authors first (检索于 2026-06；以官网为准).

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure what the scope, format, and declaration requirements demand
- Confirming the abstract, exhibits, model comparison, code deposit, and declarations are in order

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** Elsevier. (检索于 2026-06；以官网为准)
- **Portal:** **Elsevier Editorial Manager** (linked from the ScienceDirect guide for authors).
- **Identity:** a leading cognitive-science journal favoring **longer, integrative, model-driven**
  articles; multi-experiment programs combined with formal/computational modeling.
- **Scope:** attention, perception, memory, learning, language, categorization, reasoning,
  problem-solving, judgment and decision-making; modeling/neuroscientific approaches and substantive
  reviews welcome.
- **Style:** APA-style statistical reporting and references; Elsevier formatting via the guide for
  authors. Confirm the current reference style and any structured-abstract requirement.
- **Open science:** authors are strongly encouraged to share **data, model/analysis code, and
  materials**; complete the Elsevier **research-data statement** and **declaration of competing
  interest**.
- **Review model / length / abstract limits:** volatile — confirm single- vs. double-anonymized review,
  any word/length guidance, and the abstract limit on the live page. 待核实.

## Preflight checklist

### Scope & shape
- [ ] Contribution is a **theoretical advance** carried by a program (multi-experiment and/or a model)
- [ ] If a model is central, it is **fit and compared** to a rival under matched flexibility
- [ ] Not a single-effect / atheoretical paper better suited to a short-report venue

### Front matter & format
- [ ] Abstract present (confirm length/structure on the official page); keywords included
- [ ] APA-style statistics (effect sizes + intervals; model-comparison criteria) and references
- [ ] Exhibits show observed data + model fit (not bars of means); model-comparison table included
- [ ] Manuscript follows Elsevier formatting/section conventions per the guide for authors

### Modeling & disclosure
- [ ] Model comparison reported (AIC/BIC/BF or cross-validation) with free-parameter counts
- [ ] Parameter + model recovery reported
- [ ] Mixed/hierarchical structure where the design demands it, with diagnostics
- [ ] Confirmatory vs. exploratory clearly separated

### Open science & declarations
- [ ] Data deposited + DOI + codebook (or justified restriction)
- [ ] **Model/analysis code** deposited; fits regenerate in a fresh session (run log)
- [ ] Materials deposited + DOI
- [ ] Elsevier **research-data statement** + **competing-interest declaration** + funding/contributions
- [ ] Preregistration linked where applicable

## Worked micro-example — preflight verdict (illustrative)

Running the recognition-memory program through the gate the night before upload:

```
Shape:      3 experiments + UVSD vs. DPSD comparison → theoretical advance → PASS
Model:      both models fit (matched flexibility); dBIC + BF reported;
            parameter + model recovery included → PASS
Hierarchy:  hierarchical Bayesian; R-hat ~ 1.00, ESS adequate → PASS
Exhibits:   z-ROC figure overlays observed data + both model curves; model-
            comparison table with free-parameter counts → PASS
Open sci:   data + model code + materials each have a DOI; fits regenerate
            in a fresh session (run log attached) → PASS
Declarations: competing interest (none) + research-data statement + funding
            completed in Editorial Manager → PASS
Verdict:    ready to upload to Editorial Manager.
```

## Last-mile failure modes that trigger a return

| Failure | Caught by | Quick fix |
|---------|-----------|-----------|
| Model fit but never compared | scope/shape check | fit the rival; add the comparison table |
| Fits don't regenerate from code | reproducibility check | deposit seeded code + a fresh-session run log |
| Bars of means, no model overlay | exhibit check | redraw with observed data + model fit |
| "Data on request" instead of a DOI | open-science check | deposit and mint a persistent identifier |
| Competing-interest/data statement blank | declaration check | complete the Elsevier declarations before upload |

> Volatile specifics (length guidance, abstract limit, review model, current editor, exact declarations)
> change. Re-confirm every item above against the journal's current guide for authors before relying on
> it (检索于 2026-06；以官网为准).

## Anti-patterns

- Submitting a single-effect/atheoretical paper to a model-driven, long-form venue
- A central model that is fit but never compared to a rival
- Modeling that cannot be reproduced from the deposited code
- Exhibits that hide the fit (bars of means) or assert "best fit" with no table
- Missing Elsevier research-data / competing-interest declarations

## Output format

```
【Shape】theoretical advance via a program; model fit + compared? [Y/N]
【Format】abstract + keywords + APA-style reporting + Elsevier formatting? [Y/N]
【Modeling】comparison + recovery + hierarchy + diagnostics? [Y/N]
【Open science】data + model code (reproducible) + materials + DOIs? [Y/N]
【Declarations】competing interest + research-data + funding? [Y/N]
【Next】await decision → cogpsych-rebuttal on revision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — the eight-section pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, DOIs, modeling/reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Cognitive Psychology / Elsevier URLs behind every fact in this pack
