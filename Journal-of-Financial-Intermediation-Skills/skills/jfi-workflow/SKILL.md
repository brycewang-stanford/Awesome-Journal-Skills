---
name: jfi-workflow
description: Use when routing a Journal of Financial Intermediation (JFI) manuscript through its lifecycle — given where you are in the banking/intermediation paper pipeline, it names the next jfi-* skill to invoke and separates the theory-led path from the empirics-led path. It coordinates; it does not draft content.
---

# JFI Workflow Router (jfi-workflow)

## When to trigger

- "I'm writing a JFI paper — where do I start?"
- You finished one stage and want the next jfi-* skill
- You are unsure whether your project is theory-led or empirics-led at JFI

## What JFI is (orient first)

Journal of Financial Intermediation (JFI) is an **Elsevier** journal (ISSN 1042-9573) on **banking,
financial intermediation, and the economics of financial institutions and markets**. It publishes **both
theory and empirics**: bank behavior, intermediary frictions, corporate finance, regulation, and related
financial-economics topics. So the router first asks whether the paper's core contribution is a **model
(theory)** or an **empirical design** — this changes how `jfi-identification-strategy`,
`jfi-data-analysis`, and `jfi-replication-and-data-policy` are applied.

## Routing map

| Where you are | Next skill |
|---|---|
| Choosing / sharpening the question | `jfi-topic-selection` |
| Placing it against the intermediation frontier | `jfi-literature-positioning` |
| Empirical causal design OR theory assumptions/proofs | `jfi-identification-strategy` |
| Running bank/loan-panel analysis OR numerical examples | `jfi-data-analysis` |
| Articulating the mechanism / "why intermediaries matter" | `jfi-contribution-framing` |
| Building exhibits | `jfi-tables-figures` |
| Polishing prose, author–date style, numbered sections | `jfi-writing-style` |
| Preparing Option C data sharing + Data Statement | `jfi-replication-and-data-policy` |
| Understanding single-blind / desk-reject / final decision | `jfi-review-process` |
| Final preflight + fee + abstract/keywords + AI disclosure | `jfi-submission` |
| Responding to referees on an R&R | `jfi-rebuttal` |

## Default sequence

topic-selection → literature-positioning → identification-strategy → data-analysis →
contribution-framing → tables-figures → writing-style → replication-and-data-policy → review-process →
submission → rebuttal.

## Two lifecycle profiles through this router

- **Empirics-led** (e.g., a register-based lending-channel paper): topic-selection settles the mechanism;
  `jfi-identification-strategy` is the heaviest stop (demand confounds, within-firm design);
  `jfi-data-analysis` builds the battery; `jfi-review-process` matters **early**, because the desk screen
  is the binding constraint, not the referee round.
- **Theory-led** (e.g., a model of run-prone shadow funding): `jfi-identification-strategy` becomes
  assumptions-and-propositions discipline; `jfi-data-analysis` shrinks to a numerical illustration;
  `jfi-writing-style` carries more weight, since proof exposition is the surface the referee actually
  reads.

## Symptom → skill routing

| Symptom | Route to |
|---|---|
| "A referee could say it's all borrower demand" | `jfi-identification-strategy` |
| Abstract reads like generic banking | `jfi-contribution-framing` |
| Closest citations are all JF/JFE general finance | `jfi-literature-positioning`, then re-test fit |
| Exhibits do not show the mechanism | `jfi-tables-figures` |
| Worried about paying the non-refundable fee | `jfi-review-process` + the gates in `jfi-submission` |
| Restricted register data, sharing plan unclear | `jfi-replication-and-data-policy` |

## Stage gates before money and goodwill are spent

1. **Gate A** (after literature-positioning): the delta is a mechanism, not merely a new dataset.
2. **Gate B** (after identification/data-analysis): a within-firm or equivalent demand control exists, or
   the theory's propositions are fully proved with stated boundaries.
3. **Gate C** (before submission): the desk-screen self-audit passes — mechanism in the abstract, design
   defended in the introduction, the <=250-word abstract and 1-7 English keywords are ready, and the
   US$500 new-submission fee is justified. Re-confirm fees against the journal's current author
   guidelines before filing.

## A routing pass, worked (illustrative)

An author arrives with loan-level evidence that small banks cut credit after a deposit outflow.
`jfi-topic-selection`: strong fit once anchored to liquidity transformation. `jfi-literature-positioning`:
closest papers are the deposits-channel line; the delta is the relationship-borrower margin.
`jfi-identification-strategy`: outflow exposure may proxy local demand — gate B forces a within-firm
design before any drafting continues. `jfi-data-analysis`: battery planned around that threat. Only then
do framing, exhibits, and style run, and `jfi-submission` clears the fee gates. The router's value is
refusing to let writing start before gate B — at JFI the design objection, not the prose, kills papers.
On an R&R, re-enter the map at the skill matching the referee's heaviest comment, then exit via
`jfi-rebuttal`.

## Anti-patterns

- Treating JFI as purely empirical when your contribution is a model (or vice versa)
- Skipping `jfi-review-process` and being surprised by desk-rejection or a narrow appeal path
- Forgetting the US$500 fee until `jfi-submission` — see the source map and re-confirm before filing

## Output format

```
【Stage】<your current stage>
【Paper type】theory / empirical / both
【Next skill】jfi-<role>
【Then】<the one after>
```
