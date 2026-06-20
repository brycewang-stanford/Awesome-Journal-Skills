---
name: jru-replication-package
description: Use when assembling the data, code, and experiment materials for a Journal of Risk and Uncertainty (JRU) manuscript and writing its Data Availability Statement. Builds a transparent, reproducible package; it does not invent evidence or citations.
---

# Replication Package (jru-replication-package)

## When to trigger

- The paper has experimental or field results and you need a Data Availability Statement for the Springer submission
- z-Tree / oTree / Qualtrics materials and the structural estimation code exist but are not organized for a stranger to run
- A referee or the editor asks whether the elicitation could be reproduced from the materials provided
- Decisions about what data can be shared (human-subjects constraints) versus what must be documented are unsettled

## What JRU / Springer expect

JRU requires a **Data Availability Statement** on original research articles, and Springer strongly encourages sharing the underlying research data (deposit in a recognized repository, with a citable DOI where possible). For this journal the package has two faces that generic econ replication advice misses: the **experiment must be reproducible as a procedure** (instructions, screens, incentive rules — not just the resulting dataset), and the **structural estimation must be re-runnable** (code that recovers the reported parameters). Exact policy wording and any mandatory-deposit details are 待核实 — verify on the official submission guidelines.

### The two-face package

| Component | Experimental paper | Structural/empirical paper |
|-----------|--------------------|----------------------------|
| Materials | full instructions, decision screens, comprehension checks, the incentive/payment protocol | data source + access terms, construction of the risk-exposure variable |
| Code | z-Tree/oTree/Qualtrics source + analysis scripts | estimation code (MLE/GMM/MSM), from raw data to every reported parameter |
| Data | subject-level choices (de-identified), session metadata, randomization seeds | analysis dataset or a clear access path if proprietary (e.g., admin/insurer data) |
| Reproducibility | a stranger can re-run the experiment AND re-derive the estimates | one script regenerates every table/figure from raw inputs |

### Human-subjects and proprietary data

- De-identify subject data; document the IRB/ethics approval. If raw data cannot be shared, share the **derived** analysis data plus enough documentation to reproduce results.
- For insurer/administrative VSL-type data, state the access terms and provide the code so the pipeline is auditable even if the data are restricted.
- Pre-registration (if the study was pre-registered): link the registry and report deviations.

### Layout that a stranger can run

A clean package for a JRU elicitation or estimation paper has a predictable shape:

- `/instructions` — participant-facing text, decision screens, comprehension checks, payment protocol
- `/experiment` — z-Tree/oTree/Qualtrics source, with the random-incentive rule visible in code
- `/data` — de-identified subject choices, session metadata, randomization seeds, codebook
- `/code` — a single `master` script that runs raw → cleaned → every table/figure, plus the structural estimation
- `README` — software versions, run order, expected outputs, and the data-access path for any restricted inputs

The test is blunt: a colleague with the repository and nothing else should be able to (a) re-run the experiment and (b) reproduce every reported parameter.

### Writing the Data Availability Statement

- Match the statement to reality: if data are restricted, say so and give the access route, do not over-promise.
- Cite the deposit with its DOI/repository where one exists; a citable archive is stronger than "available on request."
- Cross-check the statement against the actual deposit before submission — a mismatch is a common, avoidable editorial flag.

## Checklist

- [ ] A Data Availability Statement is drafted and matches what is actually deposited
- [ ] Experiment: full instructions, screens, comprehension checks, and incentive rules are included (procedure reproducible)
- [ ] Experiment software source (z-Tree/oTree/Qualtrics) and randomization seeds provided
- [ ] One master script regenerates every table and figure from raw inputs
- [ ] Structural code recovers the reported parameters; environment/versions documented
- [ ] Data de-identified; IRB/ethics approval documented; proprietary-data access terms stated
- [ ] Pre-registration linked and deviations reported (if applicable)
- [ ] Policy specifics verified against official guidelines or marked 待核实

## Common reproducibility failures in risk papers

- **Seeds not saved**, so the randomized lottery sequence cannot be regenerated — the experiment is not reproducible even with the software.
- **Hand-edited intermediates** between raw choices and the estimation, leaving a gap no script bridges.
- **Estimation that does not converge to the reported numbers** on a clean machine because tolerances, starting values, or package versions were not pinned.
- **Comprehension-check data dropped silently** in cleaning, so a stranger cannot reproduce the analysis sample.

A quick self-test: clone the package into a fresh directory, run the master script end to end, and confirm it reproduces the headline parameter without manual intervention.

## Anti-patterns

- Depositing the dataset but not the **instructions** — for an elicitation paper the procedure *is* the method
- A "results.do" that assumes hand-edited intermediate files no one else has
- Sharing identifiable subject data, or omitting the IRB statement
- A Data Availability Statement that promises data not actually in the package
- Treating Springer's data policy as optional; the statement is required even when data are restricted

## Worked vignette (illustrative)

An ambiguity-elicitation paper deposits only the cleaned choice matrix. A referee cannot tell whether the matching-probabilities task was incentive-compatible as run. The JRU-ready package adds the oTree source, the on-screen instructions and comprehension checks, the random-incentive payment rule, the session seeds, and a single script that goes from raw choices to the reported α-MEU estimate — so the elicitation and the estimate are both reproducible.

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-replication-package
【Verdict】ready / complete materials / fix access
【DAS drafted】matches deposit [Y/N]
【Experiment reproducible】instructions+screens+incentives+seeds [Y/N]
【Code reproducible】master script regenerates all exhibits [Y/N]
【Ethics/data】IRB documented; de-identified; access terms stated [Y/N]
【Policy status】verified / 待核实
【Next skill】jru-referee-strategy
```
