---
name: jama-structured-abstract
description: Use when writing or auditing the JAMA structured abstract and the Key Points box for a JAMA manuscript. Enforces the exact JAMA heading set and quantified results; it does NOT design the study or run statistics.
---

# Structured Abstract & Key Points (jama-structured-abstract)

## When to trigger

- The abstract is a single block paragraph rather than JAMA's structured headings
- Results in the abstract lack effect sizes / 95% CIs
- A trial abstract has no Trial Registration line
- The manuscript lacks a Key Points box (required for many article types)

## The JAMA structured-abstract headings (Original Investigation)

Use these headings in order. The abstract is concise — verify the current word ceiling (commonly around 350 words) on the Instructions for Authors page.

1. **Importance** — why the clinical question matters to a broad audience (1–2 sentences).
2. **Objective** — the precise question/hypothesis, ideally one sentence.
3. **Design, Setting, and Participants** — study type, dates, setting (and number of sites), eligibility, sample size, follow-up duration.
4. **Interventions** (trials) or **Exposures** (observational) — what was given/compared or what was studied.
5. **Main Outcomes and Measures** — the **pre-specified primary outcome** and key secondary outcomes, defined; state if any outcome was post hoc.
6. **Results** — sample numbers and key demographics; the primary outcome with **effect size and 95% CI**; salient secondary outcomes and harms. Lead with numbers, not adjectives.
7. **Conclusions and Relevance** — what the primary outcome supports and its clinical implication. Do **not** overstate; do not promote a secondary outcome.
8. **Trial Registration** — for clinical trials, the registry name and trial identifier (e.g., ClinicalTrials.gov NCT number).

For systematic reviews/meta-analyses, use the matching structured set (Importance; Objective; Data Sources; Study Selection; Data Extraction and Synthesis; Main Outcomes and Measures; Results; Conclusions and Relevance), and report the registration (e.g., PROSPERO).

## Key Points box

Many JAMA articles require a short **Key Points** box, separate from the abstract:

- **Question** — the study question in one sentence.
- **Findings** — the main result, with the key number and whether it was statistically significant; note the design (e.g., "In this randomized trial of N patients …").
- **Meaning** — the clinical takeaway in one restrained sentence.

Keep it tight (Key Points is brief — verify the current word limit). It must agree exactly with the abstract and the body.

## Worked example: a JAMA Results line and Key Points (illustrative)

Vignette (illustrative): a multicenter randomized clinical trial, N = 1,900 adults with heart failure with preserved ejection fraction, exercise program vs usual care; pre-specified primary outcome 6-minute walk distance at 12 weeks.

- Abstract Results line: "Among 1,900 participants (mean age, 71 years; 54% women), 12-week 6-minute walk distance increased by a mean of 31 m (95% CI, 18-44 m) vs usual care; heart-failure hospitalization did not differ (absolute risk difference, -0.9 percentage points [95% CI, -3.2 to 1.4])."
- Key Points: Question — does the program improve functional capacity in HFpEF? Findings — 6-minute walk distance improved by 31 m. Meaning — exercise may improve capacity, though hospitalization was unchanged.

The Conclusions stay bound to the primary outcome and the Key Points agree with the abstract.

## Reviewer pushback and the JAMA fix

- "Results give adjectives, not effect sizes." Fix: replace "markedly improved" with the estimate + 95% CI.
- "Conclusion rests on a secondary outcome." Fix: re-anchor Conclusions and Relevance on the primary outcome.
- "Key Points contradict the abstract." Fix: reconcile the number and design statement; add any missing registration line.

Calibration anchors (hedge where uncertain): the structured-heading set, numbers-first Results, and the Key Points box are durable JAMA features; word ceilings are volatile — confirm against current author guidelines.

## Checklist

- [ ] All required headings present and in order
- [ ] Importance frames general medical relevance, not just novelty
- [ ] Design/Setting/Participants gives dates, setting, eligibility, N, follow-up
- [ ] Primary outcome named and pre-specified; post hoc analyses flagged
- [ ] Primary result reported with effect size + 95% CI
- [ ] Conclusion matches the primary outcome — no spin, no secondary-outcome promotion
- [ ] Trial Registration line present for trials (or PROSPERO for reviews)
- [ ] Key Points box present (Question / Findings / Meaning) and consistent with the body
- [ ] Within the word limits (verify current numbers)

## Anti-patterns

- Block-paragraph abstract ignoring JAMA's headings
- Results section with adjectives ("markedly improved") but no numbers/CIs
- Conclusion that overstates or rests on a secondary/post hoc outcome
- Missing Trial Registration line on a trial
- Key Points that contradict the abstract or omit the design
- Reporting only a p-value for the primary outcome in the abstract

## Output format

```
【Headings present & ordered】yes / no
【Primary result + 95% CI in abstract】...
【Conclusion matches primary outcome】yes / spin to fix: ...
【Trial Registration / PROSPERO line】present / missing / n.a.
【Key Points box (Q/F/M)】present + consistent / missing
【Word counts vs limits】abstract X / Key Points X (verify)
【Next skill】jama-ethics-registration
```
