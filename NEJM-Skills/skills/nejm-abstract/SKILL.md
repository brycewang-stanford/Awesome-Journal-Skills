---
name: nejm-abstract
description: Use to write the NEJM structured abstract — four headed sections (Background, Methods, Results, Conclusions), ≤250 words, with the trial registration number and funding source, leading the Results with the primary outcome reported as an effect size with a 95% CI. Late-stage polish skill.
---

# Structured Abstract (nejm-abstract)

## When to trigger

- Significance, design, reporting, and statistics are settled (do this late).
- The abstract is unstructured prose, or exceeds the word cap.
- The Results section reports P values but not the primary outcome with its effect size and CI.
- The trial registration number and funding source are missing.

## The four required sections (Background, Methods, Results, Conclusions)

NEJM uses a **structured abstract, ≤250 words**, with four headed sections. Confirm the exact cap against the current author guidelines; design for 250 as the ceiling.

### Background
One or two sentences: the clinical problem and the specific question. State why the question matters in practice — no extended literature review.

### Methods
Design (e.g., "randomized, double-blind, placebo-controlled trial"), population and setting, intervention/comparator, randomization, the **pre-specified primary outcome** and key secondary outcomes, and the analysis population (intention-to-treat).

### Results
Lead with the **primary outcome**. Report the **effect size with a 95% confidence interval** — absolute difference and/or relative measure (hazard ratio, risk ratio, odds ratio) — plus the P value if used. Give the number analyzed per group. Report key secondary outcomes and serious adverse events. Numbers, not adjectives.

### Conclusions
One or two sentences answering the question, **calibrated to the evidence**. Name the comparator. End with the **trial registration number** and the **funding source**.

## Hard constraints

- [ ] ≤ ~250 words across the four sections (confirm against current guidelines).
- [ ] Four headed sections present: Background / Methods / Results / Conclusions.
- [ ] Primary outcome reported with **effect estimate + 95% CI** (not P alone).
- [ ] Analysis population (ITT) and per-group n stated.
- [ ] **Trial registration number** included (e.g., "ClinicalTrials.gov number, NCT00000000").
- [ ] **Funding source** stated (e.g., "Funded by …").
- [ ] No undefined acronyms; no citations; no figure/table references.

## Concrete template (RCT)

```
BACKGROUND
[Clinical problem]. It is unknown whether [intervention] improves [patient-important
outcome] in [population].

METHODS
We conducted a [design, e.g., multicenter, randomized, double-blind, placebo-controlled]
trial. We randomly assigned [N] patients with [condition] to [intervention] or
[comparator]. The primary outcome was [outcome] at [time]. Analyses were performed
according to the intention-to-treat principle.

RESULTS
The primary outcome occurred in X of N patients ([x.x]%) in the [intervention] group and
in Y of N ([y.y]%) in the [comparator] group (absolute difference, [z.z] percentage points;
95% CI, [a] to [b]; hazard ratio, [h]; 95% CI, [c] to [d]; P=[p]). [Key secondary outcome].
[Serious adverse events by group].

CONCLUSIONS
Among patients with [condition], [intervention] [did/did not] [effect on outcome] as
compared with [comparator]. (Funded by [funder]; [TrialName] ClinicalTrials.gov number,
NCT00000000.)
```


## Operating pass for New England Journal of Medicine

Use this as a second-pass capability check. First lock the clinical question, population, endpoint, effect size, safety signal, and practice implication; then test whether the manuscript addresses clinical-medicine reviewers who expect practice-changing evidence, patient relevance, safety, and exact reporting discipline.

- **Primary move:** Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JAMA for broad clinical medicine, Lancet for global-health/public-health reach, specialty journals for narrower disease domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Word count】 N ≤ 250
【Four sections present】 Background / Methods / Results / Conclusions — yes/no
【Primary outcome with effect + 95% CI】 yes/no + the numbers
【ITT + per-group n stated】 yes/no
【Registration number present】 yes/no (NCT…)
【Funding source present】 yes/no
【Acronym / citation hits removed】 [...]
【Next】 nejm-citation
```

## Anti-patterns

- **Do not** write an unstructured single-paragraph abstract — NEJM uses the four headed sections.
- **Do not** report only a P value for the primary outcome — give the effect estimate and 95% CI.
- **Do not** lead the Results with a secondary or subgroup finding.
- **Do not** omit the registration number or funding source — both belong in the Conclusions sentence.
- **Do not** state conclusions that outrun the data (over-claiming is a top rejection reason).
