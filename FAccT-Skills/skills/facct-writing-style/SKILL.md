---
name: facct-writing-style
description: Use when revising an ACM FAccT paper so that a fairness/accountability/transparency contribution is legible on the first page to a mixed CS+law+social-science reviewer pool, claims are scoped to who is affected, limitations and harms are argued rather than recited, the interdisciplinary framing is native, and the acmart page budget and endmatter statements are used well.
---

# FAccT Writing Style

Use this when revising the main paper. FAccT papers are read by a **deliberately mixed panel** —
a computer scientist, a lawyer, and a qualitative social scientist may each land on your paper — so
the writing must make a **fairness, accountability, or transparency contribution legible to all
three** and must be honest about who is affected and how. The failure this skill prevents is a
paper that is excellent inside one discipline and illegible or naive to the others.

## Revision rules

- **Lead with the FAccT contribution.** The first page names the socio-technical problem, who bears
  the harm or holds the accountability, why the current state is inadequate, the contribution
  (method, audit, framework, critique, study, or legal analysis), and what changes for people —
  before any model or doctrinal detail.
- **Scope claims to a population, not the world.** "Reduces bias" is not a FAccT claim; "reduces the
  false-positive-rate gap between groups A and B on dataset D, under measure M" is. Name the
  subgroups, the fairness/transparency construct, and the operationalization.
- **Argue limitations and adverse impacts; do not recite them.** State the harms, failure modes, and
  who could be hurt if the work is deployed or misread — and what you did about each. A boilerplate
  "limitations" paragraph is a tell that the author has not stressed their own claims. This is also
  where the **Adverse Impacts** endmatter statement earns its keep.
- **Make the interdisciplinarity native.** If you borrow a construct from law or the social sciences,
  use it the way that field uses it, cite its real origin, and carry it through the analysis — not
  as a one-line garnish.
- **Respect the acmart page budget as a design constraint.** FAccT 2026 allows up to 14 content
  pages (+1 endmatter page; 15 if Revised/accepted), references unlimited — generous but finite. A
  paper that only fits by shrinking its limitations or method is over-scoped.
- **Preserve mutual anonymity** in self-citations, system names, acknowledgements, funding, and —
  critically — keep the **Positionality** statement out of the anonymous submission entirely.

## The FAccT paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Sociotechnical problem, who is affected, contribution, what changes — first page | Leads with a model/benchmark, not a harm or accountability question |
| Background / motivation | Why this matters now, grounded across the relevant disciplines | Motivation by assertion; one-discipline framing |
| Approach / method / argument | The technique, study design + protocol, or the conceptual/legal argument | Method too thin to re-run, or critique with no engagement with the artifact |
| Findings / evaluation | Disaggregated results, coded themes, or a defended argument | Aggregate-only numbers that hide subgroup harm |
| Limitations & adverse impacts | The harms and threats that actually bite, each bounded | Generic list untethered from this work |
| Related work | Cross-disciplinary, delta-first positioning | Cites only one lane; misses the obvious neighbor in another field |

## Sentence-level rewrites

| Draft pattern | FAccT-safe rewrite |
|---|---|
| "Our method is fair." | "our method equalizes <metric> across <groups> on <dataset>, within <bound>; residual gaps in §5" |
| "We improve transparency." | "we surface <what> to <whom> for <decision>, and we test whether they can act on it" |
| "The model is accurate on a large dataset." | "accuracy disaggregated by <subgroup> (Table 2); the largest error falls on <group>" |
| "This raises ethical concerns." | "this risks <specific harm> to <specific population>; we mitigate by <action>, residual risk in the Adverse Impacts statement" |
| "Prior work is limited." | "<work> measured X but not the deployment outcome Y that governs harm; we measure Y" |

## Limitations-and-harm discipline

```text
[Construct]     does the fairness/transparency metric mean what you claim for the affected group?
[Population]    which groups are in and out of scope; who is invisible in your data?
[Deployment]    what goes wrong if this ships or is cited as license to deploy? who is hurt?
[Reflexivity]   whose standpoint shaped the framing? (state it in Positionality upon acceptance)
-> for each that bites: state it, then state the mitigation, next to the affected result
```

## Vignette: compressing an audit paper

A draft auditing a commercial system, with aggregate accuracy up front and a short ethics
paragraph at the end: move the **disaggregated** subgroup results to the first result table, put the
worst-affected group in the abstract, argue the construct-validity threat (does your proxy for the
protected attribute mean what you claim?) beside that table, and move method minutiae to
supplementary. The test of a good cut: a mixed reviewer can answer "who is harmed, by how much, and
how sure are we?" from the body alone.

## Output format

```text
[Writing diagnosis] clear / under-motivated / over-claimed / single-discipline / harm-blind / over-scoped
[First-page fix] <new framing leading with the FAccT contribution and who is affected>
[Claim audit] <claim -> population + construct + operationalization -> scoped? yes/no>
[Harm fix] <adverse impact that bites -> mitigation to add, placed by the result>
[Anonymity edits] <system names / self-citations / positionality kept out of the anonymous PDF>
```
