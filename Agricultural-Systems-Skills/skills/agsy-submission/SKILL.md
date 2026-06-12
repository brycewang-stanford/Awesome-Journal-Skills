---
name: agsy-submission
description: Use when running the final pre-submission preflight for Agricultural Systems (AgSy) via Editorial Manager — article-type selection, abstract <= 250 words, Highlights, graphical abstract, CRediT and declaration-of-interest statements, ORCID, reference style, and data/code/model availability. Final checks; it does not draft content.
---

# Submission Preflight (agsy-submission)

The last check before pressing submit on **Editorial Manager**. AgSy is **single anonymized**, so there
is no manuscript-anonymization step — but the front matter (abstract, Highlights, graphical abstract,
declarations) and the data/code/model availability statement are where avoidable failures happen.
Verify volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming the article type's guideline length is met and all front matter is prepared

## Process facts (verify volatile items on the official page)

- **Publisher:** Elsevier (ISSN 0308-521X print / 1873-2267 online).
- **Portal:** **Editorial Manager** (legacy `ees.elsevier.com/agsy` redirects there — confirm current URL).
- **Review model:** **single anonymized** — no manuscript anonymization required (待核实).
- **Article types:** Research paper (~8,000 words), Short communication (~4,000), Perspective (~2,000,
  rapid review), Comment (~1,000), Review (verify) — no hard word cap, but stay near the guideline.
- **Abstract:** **≤ 250 words.**
- **Highlights** + **graphical abstract:** prepared.
- **Declarations:** **CRediT** author-contribution statement; **declaration of competing interest**;
  **ORCID** for authors.
- **Data/code/model:** repository deposit + data-availability statement (Elsevier research-data policy).
- **Fee:** subscription journal with a hybrid Gold OA option; confirm any APC after acceptance (待核实).

## Preflight checklist

### Article type & length
- [ ] Article type chosen; length near its guideline (research ~8,000 / short comm ~4,000 / perspective ~2,000 / comment ~1,000)
- [ ] Abstract ≤ 250 words; states purpose, principal results, major conclusions
- [ ] Highlights drafted; graphical abstract prepared

### Systems content (fit)
- [ ] The systems question (interactions / hierarchical levels / trade-offs) is explicit
- [ ] Model described, calibrated, and independently evaluated; sensitivity/uncertainty reported
- [ ] Decision / management / policy relevance stated (see `agsy-impact-and-implications`)

### Format & declarations
- [ ] References in the journal's style; consistent throughout
- [ ] **CRediT** roles + **declaration of competing interest** completed
- [ ] **ORCID** for authors; corresponding author and contact details correct
- [ ] Figures/tables self-contained and accessible (see `agsy-figures-and-tables`)

### Data, code & compliance
- [ ] Data + code + model deposited; **data-availability statement** in the manuscript
      (see `agsy-reproducibility-and-data-policy`)
- [ ] Ethics / funding / conflict declarations complete
- [ ] Original work; preprint status checked against Elsevier sharing policy

## Anti-patterns

- Abstract over 250 words; missing Highlights or graphical abstract
- No CRediT / competing-interest statement; missing ORCID
- A single-factor field trial sent to a systems journal (fit failure — see `agsy-review-process`)
- A black-box model with no calibration/evaluation or no data/code/model deposit
- Sending a full study to the Perspective track (wrong type and length)

## Worked micro-example (illustrative)

A crop–livestock simulation study with scenario analysis is readied for upload; the preflight catches
three avoidable failures:

- **Abstract = 268 words** → over the 250 cap. Trimmed to 242 by cutting two methods sentences and one
  caveat, keeping purpose, principal result, and the trade-off conclusion.
- **No graphical abstract** → a conceptual crop–livestock system diagram is prepared, satisfying the
  requirement and doubling as the framing exhibit.
- **Model deposited, run scripts not** → Elsevier counts code and models as research data, so run
  scripts and parameter files are added to the deposit and the data-availability statement links the
  DOI, pre-empting a late reproducibility hold (see `agsy-review-process`).

Result: a clean upload rather than three Editorial Manager bounce-backs.

## Desk-reject patterns this preflight catches

- *Fit failure.* A single-factor field trial with no interactions, model, or trade-off reads as an
  agronomy paper at a systems journal — reframe via `agsy-topic-selection` or re-route.
- *Black-box model.* No version, calibration, evaluation, or deposit → the model cannot be assessed.
- *Wrong track.* A full study compressed into Perspective length, or a Perspective padded into a
  research paper — type/length mismatch is an early screen.
- *Incomplete front matter.* Missing Highlights, graphical abstract, CRediT, COI, or ORCID stalls the
  submission before review starts.

## Calibration anchors (hedged where policy is volatile)

- The ≤250-word abstract, Highlights, and graphical abstract are standing Elsevier front-matter
  expectations; confirm exact wording and any new fields on the current author guidelines.
- The portal is Editorial Manager; legacy `ees.elsevier.com/agsy` links redirect — confirm the current
  submission URL (待核实).
- Any APC for the hybrid Gold OA option is set by the publisher — confirm after acceptance, not from
  memory.

## Output format

```
【Article type】Research / Short comm / Perspective / Comment / Review (length near guideline? Y/N)
【Abstract】word count (≤250); Highlights + graphical abstract? [Y/N]
【Systems content】question + model + evaluation + decision relevance? [Y/N]
【Declarations】CRediT + COI + ORCID? [Y/N]
【Data/code/model】deposited + availability statement? [Y/N]
【References】journal style consistent? [Y/N]
【Next】await decision → agsy-revision-and-rebuttal on revision
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, typesetting, repositories
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AgSy URLs behind every fact in this pack
