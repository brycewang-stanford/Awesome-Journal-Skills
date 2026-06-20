---
name: jbf-workflow
description: Use when routing a Journal of Banking & Finance (JBF) manuscript to the right JBF sub-skill across the lifecycle — topic fit, literature positioning, identification, bank-panel data work, exhibits, Elsevier Editorial Manager submission, double-anonymized review, and R&R rebuttal strategy.
---

# JBF Workflow Router (jbf-workflow)

Use this skill to decide which JBF sub-skill to invoke next for a *Journal of
Banking & Finance* manuscript. JBF is an Elsevier journal (est. 1977, monthly,
ISSN 0378-4266) for empirical and theoretical research on banking, financial
intermediation, financial institutions, capital markets, investments, corporate
finance, and financial regulation — with a strong empirical, bank-focused
orientation. This pack is tuned to that nature, not to generic finance writing.

## Default order

1. `jbf-topic-selection` — is the question a fit for a bank/intermediation-focused finance journal?
2. `jbf-literature-positioning` — stake the contribution against the banking/finance frontier.
3. `jbf-identification-strategy` — credible causal/empirical design for this field (bank panels, policy shocks, IV, event studies).
4. `jbf-data-analysis` — sample construction, estimation, and the robustness JBF referees expect.
5. `jbf-tables-figures` — clear exhibits with self-contained notes.
6. `jbf-contribution-framing` — make the "so what" land for banking/finance readers and policy audiences.
7. `jbf-writing-style` — concise, results-forward prose plus numbered-reference readiness.
8. `jbf-replication-and-data-policy` — Elsevier Option C data statement plus deposit/link-or-explain package.
9. `jbf-review-process` — what double-anonymized review and the desk screen involve.
10. `jbf-submission` — Editorial Manager preflight: USD 350 fee, anonymized manuscript + title page, 250-word abstract, keywords, Highlights, AI declaration, data statement.
11. `jbf-rebuttal` — response-letter strategy for an R&R.

## Quick routing

- Brand-new idea → `jbf-topic-selection`
- "Why JBF over a top-3 finance journal?" → `jbf-contribution-framing`
- Worried about endogeneity in a bank panel → `jbf-identification-strategy`
- Submitting this week → `jbf-submission` (then `jbf-review-process`)
- Got an R&R → `jbf-rebuttal`

Verify volatile specifics (fee, editor roster, special-issue instructions) on the official
ScienceDirect Guide for Authors — see `resources/official-source-map.md`.

## Router diagnostics

- Scope is generic finance, not banking/intermediation -> `jbf-topic-selection`.
- Endogeneity or bank-panel design is weak -> `jbf-identification-strategy`.
- Licensed-data path is not reproducible -> `jbf-replication-and-data-policy`.
- Tables omit units, clustering, or economic magnitudes -> `jbf-tables-figures`.
- Results read as significance-only -> `jbf-writing-style`.

## Stage gates for a JBF lifecycle

Place the manuscript at a gate before routing; do not advance until the exit condition holds.

| Gate | Exit condition | Skill |
| --- | --- | --- |
| G0 idea | question names a bank/intermediation/regulation margin, not "finance in country X" | jbf-topic-selection |
| G1 positioning | closest intermediation-strand papers named with a stated delta | jbf-literature-positioning |
| G2 design | identifying variation survives the "regulation is endogenous" objection | jbf-identification-strategy |
| G3 pipeline | bank-panel sample, filters, and clustering documented end to end | jbf-data-analysis |
| G4 exhibits | baseline → identification → mechanism tables with self-contained notes | jbf-tables-figures |
| G5 narrative | contribution lands in finance units and policy terms without overreach | jbf-contribution-framing, jbf-writing-style |
| G6 package | data statement plus Editorial Manager preflight complete | jbf-replication-and-data-policy, jbf-submission |
| G7 decision | status interpreted; R&R triaged | jbf-review-process, jbf-rebuttal |

## Illustrative routing pass

A draft asks whether the Basel III liquidity coverage ratio shifted bank lending toward short maturities, using a bank-quarter Call Reports panel.

- The question is squarely bank-regulatory, so G0 passes without rerouting.
- The introduction cites a broad liquidity literature but no closest paper on the LCR and credit supply — route to `jbf-literature-positioning`.
- Identification leans on plain TWFE around a single adoption date with no untreated banks; `jbf-identification-strategy` flags the missing size-threshold contrast (the rule binds for large banks first) before any table work starts.
- Only after G2 holds does the pipeline-to-exhibit chain (`jbf-data-analysis` → `jbf-tables-figures`) begin; running it earlier wastes a robustness battery on a design that will change.

## Common misroutes

- Sending an R&R straight to `jbf-writing-style`: triage with `jbf-rebuttal` first — prose fixes cannot answer identification comments.
- Building exhibits before G2 holds: staggered-DID corrections re-cut every table.
- Treating the data statement as submission-day paperwork: licensed bank-data documentation starts at G3, not G6.
- Pitching breadth ("banking and markets and fintech"): JBF rewards one anchored intermediation margin per paper.

## Routing output

```text
[Gate] G0-G7 position
[Blocking symptom] ...
[Route] jbf-... sub-skill
[Re-entry check] which gate to re-test after the fix
[Volatile facts] fee / editor roster / calls — re-verify via official-source-map
```
