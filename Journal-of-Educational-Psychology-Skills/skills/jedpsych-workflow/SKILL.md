---
name: jedpsych-workflow
description: Use when starting or navigating any Journal of Educational Psychology manuscript and you are unsure which sub-skill applies. Use when choosing among manuscript types (primary empirical study, multi-study package, exceptionally important meta-analysis) or returning with a decision letter. Routes by lifecycle stage and flags the journal's masked review, 12,000-word format, APA 7th style, and Transparency and Openness requirements. It dispatches; it does not draft content.
---

# Journal of Educational Psychology Workflow Router (jedpsych-workflow)

The orchestrator for a Journal of Educational Psychology (JEP) submission. JEP is the APA's flagship
outlet for **original, primary psychological research on learning and instruction across all ages**.
Its defining features are **masked review**, an **educational-relevance bar** (the result must matter
for real learners in real settings), and a credibility regime built on **APA 7th**, **JARS reporting
standards**, and a required **Transparency and Openness** subsection — the router makes sure each is
handled from the start, then sends you to the matching skill.

## When to trigger

- Starting a new JEP paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Choosing among manuscript types (single study, multi-study, meta-analysis)
- Returning with a decision letter (route to `jedpsych-rebuttal`)

## First question: manuscript type

| Situation | Type | Route note |
|-----------|------|-----------|
| Completed experiment / field trial / longitudinal study | **Primary empirical article** | main pipeline below |
| Several studies building one cumulative claim | **Multi-study article** | each study must add inference, not repeat |
| Cluster-randomized / classroom intervention, not yet run | **Prospective field trial** | pull `jedpsych-study-design` + `jedpsych-review-process` forward; consider preregistration |
| Exceptionally important synthesis | **Meta-analysis** | follow APA MARS; `jedpsych-data-analysis` (meta route) |
| Reliability/validity of one test | **Usually out of scope** | JEP does not typically publish single-instrument validation |

## Routing map (stage → skill)

```text
Fits JEP's learning/education scope?  → jedpsych-topic-selection
Theory + hypotheses stated up front?  → jedpsych-theory-and-hypotheses
Where does it sit in the field?       → jedpsych-literature-positioning
Design / nesting / power / measures?  → jedpsych-study-design
Multilevel/SEM sound + effect sizes?  → jedpsych-data-analysis
Exhibits (APA 7th, models, growth)?   → jedpsych-tables-figures
Fits 12,000 words, masked, APA?       → jedpsych-writing-style
Data/materials/code + TOP statement?  → jedpsych-open-science-and-transparency
How will it be judged?                → jedpsych-review-process
Ready to submit (Editorial Manager)?  → jedpsych-submission
Got an R&R / decision?                → jedpsych-rebuttal
```

## Default order

`topic-selection → theory-and-hypotheses → literature-positioning → study-design → data-analysis →
tables-figures → writing-style → open-science-and-transparency → review-process → submission → rebuttal`

For a **prospective cluster-randomized trial**, pull `study-design` and `review-process` forward — power
for nesting and a registration/analysis plan should be settled *before* schools are recruited.

## Worked micro-example — routing a live project (illustrative)

A team has a cluster-randomized reading-comprehension intervention (48 classrooms, ~1,100 students),
pretest covariate, and a reviewer worried about power and clustering. The router walks them:

```
Type:    Primary empirical article (field trial, results in hand).
Entry:   not idea-stage → skip topic-selection; they are at design/analysis.
Route:   study-design (nesting, ICC, cluster-level power, baseline equivalence)
         → data-analysis (multilevel model, cluster-robust inference, effect size)
         → tables-figures (model table + growth/forest exhibit)
         → writing-style (fit 12,000 words, APA 7th, masked)
         → open-science-and-transparency (TOP subsection, deposit + IDs)
         → submission (Editorial Manager preflight) ; on R&R → rebuttal.
Flag:    power and the effect size must be at the CLUSTER level; a student-level
         power claim is the classic JEP design error.
```

## Stage-triage table (symptom → skill)

| What the author says | Stage | Route to |
|----------------------|-------|----------|
| "Is this educational enough for JEP?" | fit | `jedpsych-topic-selection` |
| "My intro reads like a textbook chapter" | positioning | `jedpsych-literature-positioning` |
| "Reviewer says I ignored clustering" | design/analysis | `jedpsych-study-design` + `jedpsych-data-analysis` |
| "What goes in the Transparency statement?" | transparency | `jedpsych-open-science-and-transparency` |
| "My paper is 14,500 words" | format | `jedpsych-writing-style` |
| "I have an R&R" | revision | `jedpsych-rebuttal` |

## Routing pitfalls specific to this venue

- Sending a classroom-intervention project straight to `jedpsych-data-analysis` before `jedpsych-study-design`
  has fixed the nesting and cluster-level power — at JEP the multilevel structure must be designed in, not
  patched in analysis.
- Treating the result as interesting psychology with no argument for why it matters for **learning,
  teaching, or educational practice** — JEP's scope screen is educational relevance, not psychology alone.
- Deferring `jedpsych-open-science-and-transparency` to the end; the Transparency and Openness subsection
  is built from live deposits and persistent identifiers, not promised at acceptance.

## Anti-patterns

- Powering and reporting at the student level when randomization was at the classroom/school level
- A finding with no clear implication for education (better fits a general psychology outlet)
- Forgetting the Transparency and Openness subsection (data, materials, analysis code availability)
- Submitting a single-instrument reliability/validity study (typically out of scope for JEP)

## Output format

```
【Stage】fit / theory / positioning / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Primary empirical / Multi-study / Prospective trial / Meta-analysis
【Route to】jedpsych-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — power for nested designs, multilevel/SEM software, preregistration, repositories
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official APA Journal of Educational Psychology URLs behind every fact in this pack
