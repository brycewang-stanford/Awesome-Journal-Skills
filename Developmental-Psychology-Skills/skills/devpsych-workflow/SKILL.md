---
name: devpsych-workflow
description: Use when starting or navigating any Developmental Psychology (APA) manuscript and you are unsure which sub-skill applies. Use when choosing a manuscript length tier or returning with a decision letter. Routes by lifecycle stage and by the developmental design (cross-sectional, longitudinal/cohort, micro-genetic, experiment with minors); it dispatches, it does not draft content.
---

# Developmental Psychology Workflow Router (devpsych-workflow)

The orchestrator for a Developmental Psychology submission. This APA journal publishes empirical work on
**development across the life span**, and its defining demand is a credible claim about **developmental
change** — age effects, within-person change, or trajectories — reported under **APA 7th + JARS**, with
**masked review** and **Transparency and Openness Promotion (TOP)** expectations. The router makes sure
the developmental claim, the design, and the open-science package are all handled, then dispatches.

## When to trigger

- Starting a new Developmental Psychology paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Choosing a length tier (brief report vs. larger report vs. multi-study/longitudinal report)
- Returning with a decision letter (route to `devpsych-rebuttal`)

## First question: what kind of developmental claim and design?

| Situation | Design | Route note |
|-----------|--------|-----------|
| Age differences at one time point | **Cross-sectional** | name the age/cohort confound early (`devpsych-study-design`) |
| Within-person change over time | **Longitudinal / cohort** | attrition + measurement invariance are load-bearing |
| Process of change in close-up | **Micro-genetic** | dense sampling; justify granularity |
| Causal manipulation with minors | **Experiment** | ethics/assent + age-appropriate task validity |
| Re-using a large panel (e.g., NICHD, ECLS) | **Secondary analysis** | declare provenance, derived measures, version |

## Routing map (stage → skill)

```text
Idea / fit + age scope?            → devpsych-topic-selection
Developmental theory + hypotheses? → devpsych-theory-and-hypotheses
Where does it sit in the field?    → devpsych-literature-positioning
Design / power / invariance / age? → devpsych-study-design
Growth-curve / multilevel / SEM?   → devpsych-data-analysis
Trajectory exhibits (APA)?         → devpsych-tables-figures
APA 7th + Public Significance?     → devpsych-writing-style
Data/materials + preregistration?  → devpsych-open-science-and-transparency
How will it be judged (masked)?    → devpsych-review-process
Ready to submit (Editorial Mgr)?   → devpsych-submission
Got an R&R / decision?             → devpsych-rebuttal
```

## Default order

`topic-selection → theory-and-hypotheses → literature-positioning → study-design → data-analysis →
tables-figures → writing-style → open-science-and-transparency → review-process → submission → rebuttal`

If the design is **prospective and confirmatory**, pull `study-design` and `open-science-and-transparency`
forward so a preregistration and a sample-size justification exist *before* data collection.

## Worked micro-example — routing a live project (illustrative)

A team has a three-wave accelerated longitudinal study of self-regulation (ages 4, 6, 8; some attrition),
fitting growth curves, and a reviewer-anticipated worry about measurement invariance. The router walks them:

```
Claim:   within-person growth in effortful control, age 4→8.
Design:  longitudinal/cohort (accelerated) → invariance + attrition are central.
Entry:   not idea-stage; they are at design hardening + analysis.
Route:   study-design (invariance test plan; attrition/FIML; age-vs-cohort)
         → data-analysis (latent growth / multilevel; time coding)
         → tables-figures (spaghetti + mean-trajectory plot, CIs)
         → writing-style (APA 7th; Public Significance Statement)
         → open-science-and-transparency (data/scripts; prereg if confirmatory)
         → submission (masked preflight) ; on R&R → rebuttal.
Flag:    test longitudinal measurement invariance BEFORE interpreting change.
```

## Stage-triage table (symptom → skill)

| What the author says | Stage | Route to |
|----------------------|-------|----------|
| "Is age difference enough, or do I need change?" | fit | `devpsych-topic-selection` |
| "Reviewer: is your construct the same at every age?" | design/analysis | `devpsych-study-design` + `devpsych-data-analysis` |
| "Cross-sectional age effect — but is it cohort?" | design | `devpsych-study-design` |
| "Where does the Public Significance Statement go?" | writing | `devpsych-writing-style` |
| "Do I need to share data and preregister?" | transparency | `devpsych-open-science-and-transparency` |
| "I have an R&R" | revision | `devpsych-rebuttal` |

## Routing pitfalls specific to this venue

- Sending an age-comparison straight to `devpsych-data-analysis` without first separating **age from
  cohort** and confirming **measurement invariance** — the change claim collapses if the construct shifts.
- Deferring `devpsych-open-science-and-transparency`; under TOP, deposits and a preregistration are far
  cheaper to build before data than to retrofit at acceptance.

## Anti-patterns

- Treating a cross-sectional age difference as developmental change without addressing cohort confounds
- Interpreting trajectories before establishing longitudinal measurement invariance
- Forgetting the Public Significance Statement (an APA requirement on the abstract page)
- Ignoring masked-review anonymization in the manuscript or in shared links

## Output format

```
【Stage】idea / theory / positioning / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Design】cross-sectional / longitudinal-cohort / micro-genetic / experiment / secondary
【Route to】devpsych-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — longitudinal/SEM tooling, power, preregistration, developmental data archives
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Developmental Psychology URLs behind every fact in this pack
