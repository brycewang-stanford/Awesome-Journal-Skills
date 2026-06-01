---
name: jfi-workflow
description: Use as the router for a Journal of Financial Intermediation manuscript — given where you are in the banking/intermediation paper lifecycle, it names the next jfi-* skill to invoke. It coordinates; it does not draft content.
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
| Preparing data sharing + Data Statement | `jfi-replication-and-data-policy` |
| Understanding single-blind / desk-reject / final decision | `jfi-review-process` |
| Final preflight + fee + JEL/keywords + AI disclosure | `jfi-submission` |
| Responding to referees on an R&R | `jfi-rebuttal` |

## Default sequence

topic-selection → literature-positioning → identification-strategy → data-analysis →
contribution-framing → tables-figures → writing-style → replication-and-data-policy → review-process →
submission → rebuttal.

## Anti-patterns

- Treating JFI as purely empirical when your contribution is a model (or vice versa)
- Skipping `jfi-review-process` and being surprised by desk-rejection or a final, unappealable decision
- Forgetting the US$500 fee until `jfi-submission` — see the source map; the exact amount is **待核实**

## Output format

```
【Stage】<your current stage>
【Paper type】theory / empirical / both
【Next skill】jfi-<role>
【Then】<the one after>
```
