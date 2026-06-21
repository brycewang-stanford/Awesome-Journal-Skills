# Sociological Methods & Research — Exemplars Library (method family × contribution)

> **Verified via the Crossref API against the SMR journal record (ISSN 0049-1241), access date
> 2026-06.** Every paper below was confirmed to carry an SMR DOI of the form `10.1177/0049124...` /
> `10.1177/00491241...` with the year, volume/issue, and page range returned by Crossref for the
> *Sociological Methods & Research* journal record. Papers that could not be fully verified as SMR were
> **omitted** — this is deliberately a clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard.** SMR is **NOT** *Sociological Methodology* (the **ASA annual**, also
> SAGE; different editorial model), *Psychological Methods* (APA), *Political Analysis* (poli-sci
> methods), *Structural Equation Modeling*, or the *Journal of Educational and Behavioral Statistics*.
> Every entry's `10.1177/...49124...` DOI and SAGE/SMR imprint were checked to avoid attributing a
> sibling-journal paper to SMR.
>
> **Use principle (zero hallucination):** this file gives **contribution positioning only**. It does
> not reproduce or invent theorems, simulation numbers, or coefficients — read the original on SAGE
> before citing any result. For SMR-specific policy and scope, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method family × contribution type** is closest to yours, then study how that
paper makes a *method* (not a finding) the result — develop, evaluate, or critically assess — and how
it pairs the contribution with simulation and/or a real-data demonstration (the SMR bar; see
[`../../skills/smr-topic-selection/SKILL.md`](../../skills/smr-topic-selection/SKILL.md) and
[`../../skills/smr-method-contribution/SKILL.md`](../../skills/smr-method-contribution/SKILL.md)).
For each, ask the self-check before claiming your paper is "SMR-shaped." Model your introduction on
[`../worked-examples/01-introduction.md`](../worked-examples/01-introduction.md).

---

## By method family

### Causal inference (critique + corrected practice)

- **Cinelli, Forney & Pearl, "A Crash Course in Good and Bad Controls," Sociological Methods & Research 2024, 53(3):1071–1104.** DOI `10.1177/00491241221099552`.
  - **Why it is an exemplar:** a *critically-assess* paper — it exposes a pervasive misuse (which
    covariates to adjust for) and gives a corrected, graph-based decision rule practitioners can apply.
    The contribution is a fix, not a finding.
  - **Self-check:** does your critique end in a usable corrected procedure, not just a warning?

### Causal inference with panel data (evaluation + recommendation)

- **Leszczensky & Wolbring, "How to Deal With Reverse Causality Using Panel Data? Recommendations for Researchers Based on a Simulation Study," Sociological Methods & Research 2022, 51(2):837–865.** DOI `10.1177/0049124119882473`.
  - **Why it is an exemplar:** a Monte Carlo *evaluation* that tells the field when common panel
    estimators recover (or fail to recover) effects under reverse causality, ending in concrete
    recommendations — the canonical "evaluate and guide practice" SMR paper.
  - **Self-check:** does your simulation cover the realistic regimes and end in a decision rule?

### Missing data (evaluation / comparison)

- **Little, Carpenter & Lee, "A Comparison of Three Popular Methods for Handling Missing Data: Complete-Case Analysis, Inverse Probability Weighting, and Multiple Imputation," Sociological Methods & Research 2024, 53(3):1105–1135.** DOI `10.1177/00491241221113873`.
  - **Why it is an exemplar:** a systematic comparison of the methods practitioners actually use,
    clarifying when each is appropriate — evidence that changes practice rather than a new estimator.
  - **Self-check:** is your comparison set the methods people really run, with conditions for each?

- **von Hippel, "How Many Imputations Do You Need? A Two-stage Calculation Using a Quadratic Rule," Sociological Methods & Research 2020, 49(3):699–718.** DOI `10.1177/0049124117747303`.
  - **Why it is an exemplar:** a small, closed-form *develop* contribution (a rule for the number of
    imputations) that is immediately adoptable — "small idea, wide use."
  - **Self-check:** is your rule cheap, closed-form, and a drop-in for what practitioners already do?

### Structural equation models / model fit (develop + finite-sample evaluation)

- **Kenny, Kaniskan & McCoach, "The Performance of RMSEA in Models With Small Degrees of Freedom," Sociological Methods & Research 2015, 44(3):486–507.** DOI `10.1177/0049124114543236`.
  - **Why it is an exemplar:** identifies a concrete failure regime of a workhorse fit index (RMSEA at
    small df) and tells users when to trust it — a leading-case evaluation with direct applied payoff.
  - **Self-check:** does your evaluation pin a named statistic's failure to a regime users hit?

### Measurement invariance (develop / methodological synthesis)

- **Muthén & Asparouhov, "Recent Methods for the Study of Measurement Invariance With Many Groups," Sociological Methods & Research 2018, 47(4):637–664.** DOI `10.1177/0049124117701488`.
  - **Why it is an exemplar:** advances usable methodology for invariance testing across many groups —
    a develop/synthesis contribution with software practitioners can run.
  - **Self-check:** does your invariance method scale to the realistic many-group setting and ship code?

### Regression interpretation / decomposition (develop, drop-in tool)

- **Breen, Karlson & Holm, "A Note on a Reformulation of the KHB Method," Sociological Methods & Research 2021, 50(2):901–912.** DOI `10.1177/0049124118789717`.
  - **Why it is an exemplar:** a compact reformulation of a widely-used decomposition (the KHB method)
    — a precise, adoptable refinement of a tool sociologists already report.
  - **Self-check:** is your refinement a clean drop-in improvement to a method in wide use?

### Age–period–cohort (develop, new model)

- **Luo & Hodges, "The Age-Period-Cohort-Interaction Model for Describing and Investigating Inter-cohort Deviations and Intra-cohort Life-course Dynamics," Sociological Methods & Research 2022, 51(3):1164–1210.** DOI `10.1177/0049124119882451`.
  - **Why it is an exemplar:** confronts the notorious APC identification problem with a new modeling
    strategy and shows what it can and cannot recover — a develop paper that is honest about its
    boundary.
  - **Self-check:** does your model state plainly what it can and cannot identify?

### Computational social science / text-as-data (develop, framework + workflow)

- **Nelson, "Computational Grounded Theory: A Methodological Framework," Sociological Methods & Research 2020, 49(1):3–42.** DOI `10.1177/0049124117729703`.
  - **Why it is an exemplar:** proposes a reproducible workflow integrating computational text methods
    with interpretive analysis — a methodological framework with a demonstrated real-data application.
  - **Self-check:** does your framework deliver a concrete, reproducible workflow, not just a manifesto?

### Social networks (develop, new measure)

- **Phillips, Levy & Sampson, "The Social Integration of American Cities: Network Measures of Connectedness Based on Everyday Mobility Across Neighborhoods," Sociological Methods & Research 2021, 50(3):1110–1149.** DOI `10.1177/0049124119852386`.
  - **Why it is an exemplar:** develops network measures of neighborhood connectedness and demonstrates
    them on real mobility data — a new measurement tool with a substantive demonstration.
  - **Self-check:** does your new measure travel beyond the one dataset that motivated it?

---

## Method-family table (each cell is a verified SMR paper above)

| Method family | Verified SMR exemplar | Year / vol(issue) : pages | Contribution type |
| --- | --- | --- | --- |
| Causal inference (controls) | Cinelli, Forney & Pearl, "Good and Bad Controls" | 2024, 53(3):1071–1104 | Critique + fix |
| Causal inference (panel) | Leszczensky & Wolbring, "Reverse Causality With Panel Data" | 2022, 51(2):837–865 | Evaluation + recommendation |
| Missing data | Little, Carpenter & Lee, "Three Methods for Missing Data" | 2024, 53(3):1105–1135 | Evaluation / comparison |
| Missing data | von Hippel, "How Many Imputations Do You Need?" | 2020, 49(3):699–718 | Develop (closed-form rule) |
| SEM / model fit | Kenny, Kaniskan & McCoach, "RMSEA With Small df" | 2015, 44(3):486–507 | Evaluation (failure regime) |
| Measurement invariance | Muthén & Asparouhov, "Invariance With Many Groups" | 2018, 47(4):637–664 | Develop / synthesis |
| Decomposition | Breen, Karlson & Holm, "Reformulation of the KHB Method" | 2021, 50(2):901–912 | Develop (drop-in tool) |
| Age–period–cohort | Luo & Hodges, "Age-Period-Cohort-Interaction Model" | 2022, 51(3):1164–1210 | Develop (new model) |
| Computational text | Nelson, "Computational Grounded Theory" | 2020, 49(1):3–42 | Develop (framework + workflow) |
| Social networks | Phillips, Levy & Sampson, "Social Integration of American Cities" | 2021, 50(3):1110–1149 | Develop (new measure) |

---

## Omitted for lack of full verification (do not attribute to SMR without re-checking)

To keep the list zero-hallucination:

- Any candidate whose only hits were on **Sociological Methodology** (the ASA annual), *Psychological
  Methods*, *Political Analysis*, *Structural Equation Modeling*, or the *Journal of Educational and
  Behavioral Statistics* pages was excluded by the sibling-confusion guard, regardless of topical fit.
- Classic, heavily-cited items that surface under the SMR record (e.g., older SEM fit-index and
  sampling-weight papers) are real SMR articles but are decades old; prefer the recent exemplars above
  for current house style, and re-confirm any older paper on SAGE before citing.

Before adding any new paper to this library, confirm it on the SAGE SMR record (article page or
Crossref `journals/0049-1241`) with volume/issue and a `10.1177/...49124...` DOI, and update the
access-date header. When in doubt, omit.
