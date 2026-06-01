---
name: red-replication-and-data-policy
description: Use to build the Review of Economic Dynamics (RED) data-and-code archive to the journal's actual "Availability of Data and Computer Code for Published Papers" policy — covering computational and empirical papers, the specific readme.txt requirements, .zip/.gz/.gzip submission to the RED code editor, posting on the RED site, RePEc Computer Codes indexing, and the proprietary-data exemption.
---

# Replication & Data/Code Policy for RED (red-replication-and-data-policy)

## When to trigger

- Preparing the materials that must be in place **before final acceptance**
- A computational paper unsure whether code-only (no data) still triggers the policy (it does)
- Handling proprietary/confidential data and the exemption process

## RED's policy (verified)

RED enforces an **Availability of Data and Computer Code for Published Papers** policy. Before final
acceptance, authors must provide data and code sufficient for others to replicate the results. RED's
culture is **code-first** — the policy covers **computational as well as empirical** papers, and
archives are first-class, citable objects.

- **Empirical papers**: final datasets **plus** the code that manipulates them and, if applicable, how
  the final dataset was derived from original sources.
- **Computational / theoretical papers**: the **final programs** that generate the results.
- **readme.txt (required)** — must specify the **software/OS used**, **program execution order**,
  **expected computation time**, and **random seeds** where applicable. These requirements are notably
  specific, reflecting reproducibility norms for simulation-heavy work.
- **Format & delivery**: package as **open-standard archives — .zip, .gz, or .gzip** — to the RED
  data/code editor **Christian Zimmermann**.
- **Posting & indexing**: materials are posted on the **RED website** and indexed on **RePEc** (the RED
  **"Computer Codes"** series at IDEAS/RePEc).
- **Exemptions**: proprietary/confidential-data exemptions must be **approved by the Coordinating Editor
  at the time of submission** — note this in the cover letter, not after acceptance.

*(The policy's effective/start date is not stated on the current policy page — 待核实 — so do not cite one.)*

## Checklist

- [ ] Final data (empirical) or final programs (computational), with a master run-all script
- [ ] readme.txt lists software/OS, execution order, expected runtime, and random seeds
- [ ] Packaged as .zip/.gz/.gzip; addressed to the RED code editor
- [ ] Proprietary-data exemption (if any) flagged to the Coordinating Editor at submission
- [ ] Archive verified to reproduce headline tables/figures from scratch

## Anti-patterns

- Assuming a code-only computational paper is exempt (it is not)
- A readme missing seeds, runtime, or execution order
- Raising a proprietary-data exemption after acceptance instead of at submission

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — policy URL and the RePEc Computer Codes series
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — environment-capture and archive tooling
