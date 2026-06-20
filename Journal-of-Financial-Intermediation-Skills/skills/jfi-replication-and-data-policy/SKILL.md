---
name: jfi-replication-and-data-policy
description: Use when preparing the research-data materials a Journal of Financial Intermediation (JFI) submission expects under Elsevier Option C — deposited, cited, and linked research data where possible; an explanation where sharing is impossible; a Data Statement; [dataset]-tagged references; and a credible access route for restricted supervisory or credit-register data. It prepares the package; it does not deposit for you.
---

# Replication & Data Policy (jfi-replication-and-data-policy)

## When to trigger

- Preparing data/code materials before submitting or at acceptance
- Writing the Data Statement or handling restricted/proprietary banking data

## What JFI actually requires (verified 2026-06-20; re-confirm on the official page)

JFI follows Elsevier **Option C** for research data. Research data here includes **software, code, models,
algorithms, protocols, and methods** — not just datasets. Authors are required to:

- **Deposit research data in a relevant repository and cite/link it**, or explain why data cannot be
  shared.
- Provide a **Data Statement** on data availability when relevant; it is supported in the submission flow
  and published with the article.
- Cite datasets in the text and reference list using the **`[dataset]` tag**.

Crucially, JFI has **no journal-specific mandatory replication-code archive** — there is no equivalent of
the Journal of Applied Econometrics Data Archive or the American Economic Review replication mandate. Do
not invent a JFI-only archive requirement, but do treat deposit/cite/link-or-explain as the live Elsevier
data-policy obligation.

## How to prepare

- **Empirical papers:** write a clear Data Statement (sources, access conditions, what is shared); deposit
  shareable data and code in a general-purpose repository (Mendeley Data, Zenodo, ICPSR/openICPSR) and link
  it. For **restricted bank/supervisory data** (Call Reports extracts under license, FR Y-14, DealScan),
  state the access route and share the code plus any constructed, non-proprietary derivatives.
- **Theory papers:** lighter — share the **code that generates numerical examples/figures** so they are
  reproducible (fixed seeds/parameters); a Data Statement can note that no empirical data underlie the
  results.

## Restricted banking data: the disclosure ladder

| Data tier | Typical examples | What you can realistically share |
|---|---|---|
| Public | Call Reports, HMDA, FDIC Summary of Deposits | Full data plus code — deposit everything |
| Commercial license | DealScan, Orbis/Bankscope, branch-rate databases | Code, construction steps, and access instructions; never raw data |
| Supervisory / central-bank | Credit registers, FR Y-14, examination data | Code, variable definitions, the application route, and cleared aggregates |

For the supervisory tier, the Data Statement should name the granting institution and the access route so
a referee believes replication is possible **in principle** — credibility matters disproportionately at a
venue where the best identification lives inside restricted registers. Repository specifics and any
evolving Elsevier requirements: confirm against the journal's current author guidelines.

## Worked Data Statement skeleton (credit-register paper, illustrative)

```
Data statement: Loan-level records are from the [country] credit register,
accessed on-site under agreement [ref]; they cannot leave the central bank.
We deposit: (i) all construction and estimation code; (ii) variable
definitions and sample filters; (iii) bank-level aggregates cleared for
release; (iv) instructions for applying for register access. Public inputs
(Call Reports, HMDA) are included in the repository. Datasets are cited
with [dataset] tags in the reference list.
```

## Friction points editors and referees raise

- "Data available on request" with no named route reads as evasion — name the institution and process.
- Code that hard-codes paths inside the central-bank enclave — ship a config file and a README mapping
  enclave paths to placeholders.
- Cleared aggregates that cannot reproduce a single exhibit — clear at least the headline table's inputs.
- A theory paper claiming "no data" while its calibrated figures depend on undisclosed parameter files —
  the numerical-example code and parameter values are the reproducibility object at JFI.

## Anti-patterns

- Treating Option C as optional or replacing it with "data available on request"
- Asserting a mandatory JFI-specific archive that the Guide does not name
- A Data Statement that hides restricted-data access conditions
- Citing datasets in prose without the `[dataset]` reference tag
- Depositing data but never linking it in Editorial Manager

## Output format

```
【Data Statement】drafted, access conditions stated? [Y/N]
【Deposit / explain】repository chosen and linked in EM, or restriction explained? [Y/N]
【[dataset] tags】data cited in references? [Y/N]
【Restricted data】access route + shareable code noted? [Y/N]
【Note】Option C applies; no JFI-specific archive is named
【Next skill】jfi-review-process
```
