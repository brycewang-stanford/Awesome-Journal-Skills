---
name: nejm-reporting
description: Use to select and enforce the correct EQUATOR reporting guideline for a clinical study headed to NEJM — CONSORT for RCTs (with the participant flow diagram), STROBE for observational, PRISMA for systematic reviews — and to build the required checklist and diagram before submission.
---

# Reporting Guidelines (nejm-reporting)

## When to trigger

- You must pick the reporting checklist that matches the study type.
- A trial write-up has no **CONSORT participant flow diagram**.
- A reviewer or editor will ask for a completed reporting checklist with page/line references.
- An observational study or systematic review needs STROBE / PRISMA compliance.

## Match the study type to the guideline (EQUATOR Network)

The [EQUATOR Network](https://www.equator-network.org/) indexes reporting guidelines by study type. The core ones NEJM cares about:

| Study type                              | Guideline | Required artifact(s)                                   |
|-----------------------------------------|-----------|--------------------------------------------------------|
| Randomized controlled trial             | **CONSORT** | 25-item checklist **+ participant flow diagram**      |
| Observational (cohort/case-control/XS)  | **STROBE**  | 22-item checklist (often a flow/eligibility diagram)  |
| Systematic review / meta-analysis       | **PRISMA**  | checklist **+ study-selection flow diagram**          |
| Trial protocol                          | **SPIRIT**  | protocol-reporting checklist                          |
| Case report                             | **CARE**    | case-report checklist                                 |
| Diagnostic accuracy study               | **STARD**   | checklist + flow diagram                              |
| Cluster / non-inferiority / pragmatic   | CONSORT **extension** | the relevant CONSORT extension                |

> Match the extension, not just the base guideline: a cluster-randomized or non-inferiority trial uses the corresponding CONSORT extension.

## The CONSORT participant flow diagram (mandatory for RCTs)

For an RCT, the flow diagram is not optional. It traces participants through four stages:

1. **Enrollment** — assessed for eligibility; excluded (with reasons); randomized.
2. **Allocation** — allocated to each arm; received allocated intervention or not.
3. **Follow-up** — lost to follow-up and discontinued (with reasons), per arm.
4. **Analysis** — analyzed; excluded from analysis (with reasons), per arm.

Numbers must reconcile with Table 1, the analysis populations, and the text. Mismatched denominators across the flow diagram, Table 1, and results are a frequent reviewer catch.

## What to deliver for each study type

- **RCT** → completed CONSORT checklist (item → page/line), the flow diagram, and confirmation that registration number, protocol, and SAP are present (see `nejm-study-design`).
- **Observational** → completed STROBE checklist; define cohort entry, follow-up, and how confounders were handled.
- **SR/MA** → completed PRISMA checklist, the selection flow diagram, the search strategy, and (ideally) a PROSPERO registration number.

## Running the checklist so it survives revision

Treat the completed checklist as a living index, not a one-time export:

- Fill each item with a **page + line reference** plus a short quote that re-locates the item after re-pagination.
- Mark "not applicable" only with a one-line justification; silent N/A rows read as unread items.
- Re-run the page/line pass after every revision round; one author owns the checklist.

### Worked micro-example — one checklist row (before → after)

- Before (too thin): `Item 8a — Sequence generation: "Methods"`
- After: `Item 8a — Sequence generation: p. 6, lines 112–115 — "randomization was performed centrally in permuted blocks, stratified by site"`

## Reconciliation arithmetic (do it on paper)

Force the sums across the four stages: assessed − excluded = randomized; randomized = the sum of the arms; each arm's allocated n − (lost + discontinued) traces to the analyzed n with every exclusion named, then check the same numbers against Table 1 headers and primary-outcome denominators. Fictional example: 1042 assessed − 562 excluded = 480 randomized = 241 + 239; if Table 1 shows 240 + 239, the missing participant must be explained in the diagram.


## Operating pass for New England Journal of Medicine

Use this as a second-pass capability check. First lock the clinical question, population, endpoint, effect size, safety signal, and practice implication; then test whether the manuscript addresses clinical-medicine reviewers who expect practice-changing evidence, patient relevance, safety, and exact reporting discipline.

- **Primary move:** Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JAMA for broad clinical medicine, Lancet for global-health/public-health reach, specialty journals for narrower disease domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Study type】 ...
【Guideline + extension】 CONSORT (+ cluster/non-inferiority?) / STROBE / PRISMA / SPIRIT / CARE / STARD
【Required diagram】 CONSORT flow / PRISMA selection / STROBE eligibility — present? yes/no
【Checklist status】 completed with page/line refs? yes/no — gaps: [...]
【Number reconciliation】 flow diagram ↔ Table 1 ↔ analysis populations consistent? yes/no
【Next】 nejm-writing
```

## Anti-patterns

- **Do not** submit an RCT without a CONSORT participant flow diagram.
- **Do not** use the base CONSORT checklist for a cluster or non-inferiority trial — use the extension.
- **Do not** let the flow-diagram denominators disagree with Table 1 or the analysis populations.
- **Do not** treat the checklist as paperwork — reviewers verify items against the actual text.
