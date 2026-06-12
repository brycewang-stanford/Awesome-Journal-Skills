---
name: jama-reporting-standards
description: Use when selecting and completing the EQUATOR-network reporting checklist and flow diagram for a JAMA manuscript (CONSORT, STROBE, PRISMA, STARD, and design-specific guidelines). Maps design to checklist; it does NOT design the study or write the statistics.
---

# Reporting Standards (jama-reporting-standards)

## When to trigger

- You know the design and need the matching EQUATOR checklist
- A flow diagram is missing (participant flow for RCTs, study selection for reviews)
- You are unsure which guideline applies (CONSORT vs STROBE vs PRISMA vs STARD)
- Preparing the checklist file required at submission

## Design → guideline map

| Design                                   | EQUATOR guideline | Mandatory diagram                          |
|------------------------------------------|-------------------|--------------------------------------------|
| Randomized clinical trial                | CONSORT           | CONSORT participant-flow diagram           |
| Observational (cohort, case-control, cross-sectional) | STROBE | Participant-flow diagram strongly expected |
| Systematic review ± meta-analysis        | PRISMA            | PRISMA study-selection flow diagram        |
| Diagnostic-accuracy study                | STARD             | STARD participant-flow diagram             |
| Study protocol                           | SPIRIT            | Schedule of enrollment/assessments         |
| Prediction model                         | TRIPOD            | —                                          |
| Quality-improvement study                | SQUIRE            | —                                          |
| Other designs                            | The matching EQUATOR guideline | per guideline                 |

Always check the EQUATOR Network and JAMA's Instructions for Authors for the current guideline list and any JAMA-specific extensions or required checklist file.

## What each core guideline forces you to report

### CONSORT (RCTs)
- Title states "randomized"; structured abstract follows CONSORT-for-abstracts
- Trial design, allocation ratio, eligibility, settings; any changes after start
- Randomization (sequence, concealment, implementation) and blinding
- Numbers randomized, received intervention, analyzed, and lost — in the **flow diagram**
- Primary/secondary outcomes with estimated effect size and precision (CI)
- Harms, registration number, protocol availability, funding

### STROBE (observational)
- Study design stated early; setting, eligibility, sources, follow-up
- All variables (outcomes, exposures, confounders, effect modifiers) defined
- Bias mitigation, sample-size logic, statistical methods incl. confounding
- Numbers at each stage, descriptive data, and unadjusted **and** adjusted estimates

### PRISMA (systematic reviews / meta-analyses)
- Protocol/registration; explicit eligibility and information sources
- Full reproducible search strategy; selection and data-extraction process
- Risk-of-bias methods; synthesis methods; the **study-selection flow diagram**
- Certainty-of-evidence assessment (e.g., GRADE)

### STARD (diagnostic accuracy)
- Index test and reference standard with rationale and thresholds
- Participant flow and timing; cross-tabulation of results vs reference
- Estimates of accuracy with CIs; handling of indeterminate results

## Checklist

- [ ] Correct guideline chosen for the design
- [ ] Completed checklist file prepared with page/line numbers for each item
- [ ] Required flow diagram drafted (CONSORT / PRISMA / STARD / STROBE)
- [ ] Title and abstract conform to the abstract-level extension where one exists
- [ ] Registration number and protocol availability reported where required
- [ ] Adjusted and unadjusted estimates both reported (observational)
- [ ] Certainty-of-evidence / risk-of-bias reported (reviews, observational)

## Anti-patterns

- Submitting an RCT with no CONSORT flow diagram
- A systematic review with no PRISMA diagram or no reproducible search
- Filling the checklist with page numbers that do not match the text
- Picking STROBE for a randomized trial (or CONSORT for a cohort)
- Reporting only adjusted estimates in an observational study
- Ignoring the abstract-level extension (e.g., CONSORT-for-abstracts)


## Worked example: matching design to checklist (illustrative)

Vignette (illustrative): a multicenter randomized clinical trial, N = 2,800 adults with sepsis, primary outcome 90-day mortality, absolute risk difference -3.1 percentage points (95% CI, -5.8 to -0.4). At the Journal of the American Medical Association this maps to CONSORT with a mandatory participant-flow diagram accounting for everyone screened, randomized, and analyzed; the completed CONSORT checklist must carry page/line locations, the title must state "randomized," and the abstract follows CONSORT-for-abstracts. Had the same question been answered by a cohort, the map would shift to STROBE with both unadjusted and adjusted estimates; a systematic review would shift to PRISMA with a study-selection diagram and a GRADE certainty assessment.

## Reviewer pushback and the JAMA fix

- "Reporting incomplete (CONSORT/PRISMA item X)." Fix: add the item and update the checklist's page/line location to match the revised text.
- "Picked STROBE for a randomized trial." Fix: re-map to CONSORT; the design, not convenience, fixes the guideline.
- "Only adjusted estimates reported (observational)." Fix: report unadjusted and adjusted estimates per STROBE.

Calibration anchors (hedge where uncertain): the design-to-guideline mapping and the mandatory flow diagram for RCTs and reviews are durable; JAMA-specific extensions and required checklist files evolve — confirm against the EQUATOR Network and current author guidelines.

## Reporting pass for JAMA

Run this as a concrete capability pass. First lock the clinical question, patient population, estimand or endpoint, safety/ethics issue, and reporting checklist; then test whether the manuscript addresses clinical reviewers who ask whether the evidence changes patient care, policy, or medical decision-making while satisfying reporting standards.

- **Primary move:** Tie every reporting checklist item to a manuscript location; missing registration, denominator, consent, data, or code statements must be explicit blockers.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against NEJM for field-changing clinical medicine, Lancet for global-health breadth, specialty journals for narrower clinical domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Design】...
【Guideline】CONSORT / STROBE / PRISMA / STARD / other
【Flow diagram drafted】yes / no
【Checklist file complete with locations】yes / no
【Items still unreported】...
【Next skill】jama-statistics
```
