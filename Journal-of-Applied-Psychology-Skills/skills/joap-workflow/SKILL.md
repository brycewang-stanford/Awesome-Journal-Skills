---
name: joap-workflow
description: Use when starting or navigating any Journal of Applied Psychology (JAP) manuscript and you are unsure which sub-skill applies. Use when choosing among article types or returning with a decision letter. Routes by lifecycle stage and article type (Feature Article, Research Report, theory-development article, integrative review, qualitative, meta-analysis), and flags JAP's twin gates — a real I-O theoretical contribution and measurement/design rigor. It dispatches; it does not draft content.
---

# Journal of Applied Psychology Workflow Router (joap-workflow)

The orchestrator for a JAP submission. JAP is the **APA flagship of industrial-organizational (I-O)
psychology**, and it accepts almost nothing on rigor alone: a paper must make a **theoretical
contribution to I-O science** *and* clear a high bar on **construct validity, design, and
measurement**. The router makes sure both gates are addressed early, then sends you to the matching
skill.

## When to trigger

- Starting a new JAP paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Choosing among article types
- Returning with a decision letter (route to `joap-rebuttal`)

## First question: article type

| Situation | Type | Route note |
|-----------|------|-----------|
| Full programmatic empirical contribution | **Feature Article** | main pipeline below; length commensurate with contribution |
| Focused, shorter empirical contribution | **Research Report** | tighter page budget (待核实 exact cap); often a multi-study package |
| New conceptual/theory contribution, no new data | **Theory-development article** | `joap-theory-and-hypotheses` is the spine; design/analysis lighter |
| Cumulative synthesis of an effect | **Integrative review / meta-analysis** | `joap-data-analysis` (meta-analytic methods) + transparency for coding |
| Qualitative I-O contribution | **Qualitative research** | `joap-study-design` (trustworthiness) + `joap-writing-style` |

> JAP weighs theory and measurement together. A clean field study with no theoretical advance, and an
> elegant model with weak measurement, are both common desk rejects — confirm current article types and
> any length caps on the official APA page.

## Routing map (stage → skill)

```text
Idea / fit for I-O science?            → joap-topic-selection
Theory + hypotheses (model first)?     → joap-theory-and-hypotheses
Where does it sit in the field?        → joap-literature-positioning
Design / measurement / CMV / nesting?  → joap-study-design
SEM / HLM / mediation / meta sound?    → joap-data-analysis
Exhibits (APA, path/CFA, HLM tables)?  → joap-tables-figures
Fits APA style + length?               → joap-writing-style
Data/materials/code + TOP + prereg?    → joap-open-science-and-transparency
How will masked reviewers judge it?    → joap-review-process
Ready to submit (Editorial Manager)?   → joap-submission
Got an R&R / decision?                 → joap-rebuttal
```

## Default order

`topic-selection → theory-and-hypotheses → literature-positioning → study-design → data-analysis →
tables-figures → writing-style → open-science-and-transparency → review-process → submission → rebuttal`

Theory comes **before** literature positioning here on purpose: JAP wants the theoretical mechanism
fixed first, then the literature marshaled to show why that mechanism is new. For meta-analyses and
theory-development articles the spine shifts — pull `data-analysis` (meta) or `theory-and-hypotheses`
(theory) forward.

## Worked micro-example — routing a live project (illustrative)

A team has a two-wave field study (N = 612 employees nested in 74 teams) testing whether servant
leadership raises team performance via psychological safety, plus a lab experiment for causal
identification. The router walks them:

```
Type:    Feature Article (programmatic; field + experiment, multilevel + mediation).
Entry:   not idea-stage; theory and data exist → start at theory-and-hypotheses
         to lock the model, then design/analysis.
Route:   theory-and-hypotheses (mechanism + multilevel hypotheses)
         → study-design (CMV, nesting, temporal separation) → data-analysis
         (multilevel SEM mediation, ICC, indirect-effect CIs)
         → tables-figures (path diagram + HLM table) → writing-style
         → open-science-and-transparency (TOP, data/code, prereg of the lab study)
         → review-process → submission ; on R&R → rebuttal.
Flag:    The cross-level mediation needs a 1-1-2 / 2-2-2 design statement and a
         CMV remedy declared up front, or Reviewer 2 will lead with it.
```

## Stage-triage table (symptom → skill)

| What the author says | Stage | Route to |
|----------------------|-------|----------|
| "Is this even right for JAP?" | fit | `joap-topic-selection` |
| "Reviewers say no theoretical contribution" | theory | `joap-theory-and-hypotheses` |
| "Same-source self-report — common method bias?" | design | `joap-study-design` |
| "My mediation/HLM is questioned" | analysis | `joap-data-analysis` |
| "Where do I put data and code?" | transparency | `joap-open-science-and-transparency` |
| "I have an R&R from three reviewers" | revision | `joap-rebuttal` |

## Routing pitfalls specific to this venue

- Sending a paper straight to `joap-data-analysis` when the deeper problem is that no **theoretical
  contribution** has been articulated — JAP rejects rigorous-but-atheoretical work; fix theory first.
- Deferring `joap-study-design` until after data: common-method variance, temporal separation, and
  nesting are design decisions; you cannot fully repair them at the analysis stage.
- Treating `joap-open-science-and-transparency` as a formality — JAP holds submissions to the TOP
  framework; deposits and statements should be built early, not promised at acceptance.

## Anti-patterns

- A rigorous field study with no advance in I-O theory (rigor is necessary, not sufficient)
- Cross-sectional single-source self-report offered as the whole evidentiary base
- Hypotheses stated after the results were known (HARKing)
- Leaving construct validity and measurement to an afterthought
- Confusing JAP with a sibling venue (Personnel Psychology, AMJ, OBHDP, JOB) and writing to the wrong bar

## Output format

```
【Stage】idea / theory / positioning / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Feature Article / Research Report / theory-development / integrative review / qualitative / meta-analysis
【Route to】joap-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — SEM/HLM/meta-analysis software, preregistration, repositories, APA tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official APA Journal of Applied Psychology URLs behind every fact in this pack
