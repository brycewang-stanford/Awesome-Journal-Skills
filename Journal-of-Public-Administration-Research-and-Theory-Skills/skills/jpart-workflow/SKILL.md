---
name: jpart-workflow
description: Use as the entry point for any Journal of Public Administration Research and Theory (JPART) manuscript. Routes to the right JPART sub-skill based on the lifecycle stage and forces the journal's defining test — a public-management theory contribution, not a bare empirical finding. It dispatches; it does not draft content.
---

# JPART Workflow Router (jpart-workflow)

The orchestrator for a JPART submission. Figure out the stage, then send the user to the matching
skill. JPART is the **theory-and-research flagship of public administration** — the owning society is
the **Public Management Research Association (PMRA)** and the publisher is **Oxford University Press**.
The router's first job is to make sure the paper *builds or tests public-management theory*, not just
report an estimate.

## When to trigger

- Starting a new JPART paper and unsure where to begin
- Mid-project and unsure which skill applies next
- A reviewer or co-author said the paper is "atheoretical" or "reads like a policy report"
- Returning with a decision letter (route to `jpart-rebuttal`)

## First question: is there a theoretical contribution?

JPART rejects strong empirics with no theory. Before routing anywhere, force this gate:

| Symptom | What it means | Route to |
|---------|---------------|----------|
| Clean estimate, thin "so what" | finding without a theory move | `jpart-theory-building` |
| "We test X in setting Y" only | descriptive, no mechanism | `jpart-topic-selection` |
| Strong PA theory, weak identification | claim outruns design | `jpart-research-design` |
| Theory + design solid, prose buries it | contribution hidden | `jpart-writing-style` |

> JPART's own author guidance asks the abstract to state the **theoretical approach** first, then method,
> data, results, and **implications for theory**. If you cannot fill the theory slot, do not route forward.

## Routing map (stage → skill)

```text
Idea / fit for PA theory?         → jpart-topic-selection
Where does it sit in the field?   → jpart-literature-positioning
What's the theoretical argument?  → jpart-theory-building
Is the design defensible?         → jpart-research-design
Are the analyses sound?           → jpart-data-analysis
Are the exhibits clear?           → jpart-tables-figures
Does it read as theory + rigor?   → jpart-writing-style
Data + code release ready?        → jpart-transparency-and-data
How will it be judged?            → jpart-review-process
Ready to submit?                  → jpart-submission
Got an R&R / decision?            → jpart-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: most JPART papers loop theory ↔ design ↔ analysis several times before writing-style.

## Router stop conditions

Do not advance to the next skill when any of these are true:

| Stop | Why it matters | Route back |
|------|----------------|------------|
| The theory slot is a topic label, not a mechanism | JPART screens for contribution to PA theory | `jpart-theory-building` |
| The paper would still work if every agency, employee, or citizen detail were removed | The public-management setting is incidental | `jpart-topic-selection` |
| The design identifies an effect but not the claimed mechanism | Reviewers will read the contribution as overclaimed | `jpart-research-design` |
| Exhibits show coefficient grids but no magnitude, uncertainty, or mechanism | The result is not reviewable from the paper itself | `jpart-tables-figures` |
| Data/code release is impossible or ethically underspecified | Publication requires a public reproducibility path | `jpart-transparency-and-data` |

The router should return a single next action, not a full rewrite plan. JPART work improves fastest when
each pass fixes the highest-risk gate before polishing lower-risk prose.

## Sibling-journal routing check (do not misfile)

JPART is **not** PAR, **not** JPAM, **not** Governance. One-minute check before drafting:

| If the paper is really… | It belongs at… | Route if weak |
|-------------------------|----------------|---------------|
| A broad essay / practitioner-facing piece | Public Administration Review (PAR) | `jpart-topic-selection` |
| A policy-analysis / program-evaluation result | JPAM | `jpart-topic-selection` |
| Comparative-government / institutions, less management theory | Governance | `jpart-literature-positioning` |
| A public-management theory tested with rigorous (often experimental/causal) empirics | **JPART** | continue pipeline |

## Anti-patterns

- Treating JPART like a policy-evaluation outlet — it wants a **public-management theory** contribution
- Submitting a strong identification result with no mechanism or theoretical payoff
- Confusing JPART with PAR (broad/practitioner) or JPAM (policy analysis) — different fit, different reviewers
- Skipping the data-and-code release plan until acceptance — JPART requires it as a condition of publication

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Theory gate】contribution to PA theory stated? [Y/N]
【Stop condition】none / theory / incidental PA setting / mechanism-design mismatch / exhibit opacity / transparency gap
【Route to】jpart-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — public-administration data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JPART URLs behind every fact in this pack
