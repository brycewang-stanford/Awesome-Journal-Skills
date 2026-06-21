---
name: smr-workflow
description: Use when sequencing a Sociological Methods & Research (SMR) manuscript from method-contribution fit through derivation and properties, Monte Carlo simulation, real-data empirical illustration, released software, ScholarOne submission, double-anonymized review, and rebuttal. Routes to the right SMR skill; does not itself draft sections.
---

# SMR Workflow

Use this as the router for Sociological Methods & Research (SMR), the SAGE quantitative- and
statistical-methodology flagship. SMR publishes papers that **develop, evaluate, or critically
assess** methods; a pure application with no methodological contribution is out of scope. Reopen
the live SAGE author instructions before any deadline-ready advice — review model, fees, and policy
wording can change.

## Route map

- Fit unclear, or the "method" is really just an application: use `smr-topic-selection`.
- The new estimator/design/diagnostic and what it fixes are fuzzy: use `smr-method-contribution`.
- Methods-literature placement weak or sibling-journal confusion: use `smr-literature-positioning`.
- Assumptions, identification, bias/consistency/efficiency not pinned down: use `smr-derivation-and-properties`.
- Monte Carlo design thin or competitors missing: use `smr-simulation-studies`.
- No real-data demonstration that the method matters substantively: use `smr-empirical-illustration`.
- Exhibits crowded, not self-contained, or hiding the simulation grid: use `smr-tables-figures`.
- Prose buries the contribution or violates ASA/abstract rules: use `smr-writing-style`.
- Code/package not released or not reproducible: use `smr-software-and-reproducibility`.
- Ready for ScholarOne: use `smr-submission`.
- Decision letter arrived: use `smr-rebuttal`.

## Resource loading rule

Use the resource layer when routing:

- `resources/worked-examples/01-introduction.md` for the methods-paper opening arc (problem → why
  existing methods fail → the contribution → properties → simulation + illustration → software).
- `resources/exemplars/library.md` for benchmark style and **web-verified** SMR papers by method family.
- `resources/official-source-map.md` before any review-model, abstract-limit, citation-style,
  data-policy, or fee claim.

Never answer a volatile submission question from memory. If the source map marks a fact 待核实, say so
and recheck the official SAGE page before advising a final submission.

## Stop conditions

Pause the route and repair before moving forward if:

- the paper has **no methodological contribution** — it applies an existing method to a new dataset;
- the analytical properties (bias, consistency, efficiency, or the conditions for validity) are asserted
  but not derived or argued;
- the simulation does not include the **competing methods** an SMR reviewer would expect, or never
  shows where the new method breaks;
- there is no real-data empirical illustration showing the method changes a substantive conclusion;
- no usable software/code is released — SMR readers expect to run the method.

## Stage gates keyed to the SMR pipeline

| Gate | Pass condition | Skill that repairs failure |
|---|---|---|
| Fit gate | Method contribution and the problem it solves vs. existing methods stated in one sentence each | `smr-topic-selection`, `smr-method-contribution` |
| Theory gate | Assumptions, identification, and analytical properties traceable and derived | `smr-derivation-and-properties` |
| Evidence gate | Monte Carlo with named competitors and a real-data illustration; each property has a finite-sample check | `smr-simulation-studies`, `smr-empirical-illustration` |
| Exhibit/prose gate | Exhibits self-contained; abstract ≤150 words, no parenthetical citations; ASA style | `smr-tables-figures`, `smr-writing-style` |
| Software gate | Released package/scripts reproduce the main tables, figures, and simulation | `smr-software-and-reproducibility` |
| Conformance gate | ScholarOne fields, double-anonymization, availability statement, AI disclosure verified live | `smr-submission` |
| Post-decision gate | Point-by-point response assembled; revision clock tracked | `smr-rebuttal` |

A later gate never compensates for an earlier one: polished exhibits cannot rescue a paper whose
"method" is an application, and released code cannot rescue an underived property.

## Worked routing pass

Illustrative vignette: an author arrives with a new estimator for peer effects in network panels,
strong intuition, one simulation against OLS only, no real data, and code in a private folder.

- The fit gate passes (genuine estimator), but the **theory gate fails first**: the consistency claim
  rests on an unstated network-sparsity condition. Route to `smr-derivation-and-properties`.
- The **evidence gate fails next**: the Monte Carlo compares only to naive OLS, not to the standard
  network-autocorrelation and instrumental approaches a reviewer expects, and there is no real-data
  illustration. Route to `smr-simulation-studies`, then `smr-empirical-illustration`.
- The **software gate** is deferred but flagged: the package must be public and reproduce the grid
  before submission. Route to `smr-software-and-reproducibility` once results stabilize.
- Conformance items (ScholarOne, anonymization, availability statement) wait until the science gates
  close.

Ordering principle: secure properties before evidence, evidence before exhibits, and software before
portal mechanics.

## Venue facts that gate every route

Keep these SMR constants loaded while routing, reverifying volatile ones on live pages:

- A **SAGE** journal; the quantitative/statistical-methodology flagship in sociology — distinct from
  *Sociological Methodology* (ASA annual), *Psychological Methods* (APA), and *Political Analysis*.
- Submission via **ScholarOne Manuscripts**; **double-anonymized** review (separate title page).
- **ASA** in-text and reference style; **DataCite** for dataset references; abstract **≤150 words with
  no parenthetical citations** (检索于 2026-06；以官网为准).
- A **data-and-code availability statement** is required, with code/materials in a trusted repository;
  a **generative-AI disclosure** in the back matter when AI tools were used.
- No submission fee; Sage Choice open access is a paid option (检索于 2026-06；以官网为准).

## Output format

```text
[Current stage] idea / theory / simulation / illustration / drafting / software / submission / review / R&R / accepted
[Next SMR skill] <skill name>
[Main bottleneck] <fit, properties, simulation, illustration, exhibits, software, conformance, or response>
[Anonymization risk] <any text that would deanonymize under double-anonymized review>
[Next action] <single concrete task>
```
