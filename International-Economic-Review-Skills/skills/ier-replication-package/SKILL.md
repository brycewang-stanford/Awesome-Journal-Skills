---
name: ier-replication-package
description: Use when assembling the data/code deposit and proof appendix for an International Economic Review (IER) manuscript under its AER-style data availability policy. Covers the deposit, README, data availability statement, and self-contained proofs; it does not write the analysis code.
---

# Replication Package and Proof Appendix (ier-replication-package)

## When to trigger

- The paper has empirical, simulation, or experimental work and acceptance will hinge on a compliant deposit
- You are at conditional acceptance and the letter asks for data, programs, and a README
- Key proofs are scattered in the body, in footnotes, or assumed — and the appendix is not self-contained
- A referee questions whether the results can be reproduced from what you provide
- You need to know exactly what IER's data policy requires vs. what is optional

## IER's policy, precisely

IER **adopted the American Economic Review (AER) data availability policy effective January 1, 2022** (检索于 2026-06；以官网为准). The operative facts:

- It is journal policy to publish a paper only if its data are **clearly documented and readily available to any researcher for replication**.
- On **conditional acceptance**, authors deposit data, programs, and enough detail to permit replication in **electronic form at a standard public repository** the acceptance letter names, and include a **data availability statement with a link to the repository** in the final paper.
- If data are **proprietary** or the requirement otherwise cannot be met, the **Editor must be notified at the time of submission** — not at acceptance.

### What the deposit must contain, by paper type

| Paper type | Required in the deposit |
|------------|--------------------------|
| Econometric / simulation | Final analysis datasets; all programs; documentation of how intermediate/constructed data were created from raw sources; a **README PDF** describing every file's purpose and giving step-by-step replication instructions |
| Experimental | Original experimental instructions; subject eligibility/selection information; computer programs and scripts; the raw experimental data |

This is a **post-acceptance deposit**, not a submission-time upload — but assemble it early, because a clean package is also the most persuasive robustness evidence to a referee mid-review.

### The proof appendix (the theory/structural obligation)

Because IER tilts theory/structural, the **proof appendix is part of the contribution**, not boilerplate. The standard a referee holds it to:

- **Self-contained.** Every proof states the result, the assumptions invoked, and runs without the reader reconstructing steps. Do not prove a key result only in a footnote or by "similar to above."
- **Each formal claim has a proof or a precise citation.** Lemmas used must be proved or referenced to a stated source.
- **Numerical/computational appendix.** For structural work, document the solution algorithm, grids, tolerances, solver, and seeds so the counterfactual is reproducible — this complements the code deposit.
- **Online vs. main appendix.** Move long proofs and secondary derivations to an online appendix to respect the ≤50-page main-text ceiling, but the main results must remain provable from the main paper plus appendix.

### Why the deposit is also a mid-review asset

The AER-style deposit is formally a post-acceptance requirement, but assembling it early pays off during review, not just after. A referee who can see a clean, runnable replication package is far more likely to trust the empirical claims and the robustness section — the package is itself the strongest possible answer to "can this be reproduced?" Authors who wait until conditional acceptance to build the package often discover that constructed variables cannot be traced to raw data, or that a result depended on an undocumented manual step; finding that during review (when you can still fix it) is far better than at acceptance (when it delays publication).

### Worked example (illustrative)

A structural paper's counterfactual is computed by a solver with hand-tuned starting values and an unrecorded grid. At conditional acceptance the authors try to assemble the deposit and cannot reproduce their own headline welfare number to the second decimal. The lesson IER's policy enforces: the computational appendix (algorithm, grids, tolerances, solver, seeds) is not paperwork — it is the only thing that makes the result a *result* rather than a one-time output. Documenting it while the code is fresh, and depositing the exact scripts, is what lets a referee — and a future reader — regenerate the number on demand.

### The proprietary-data trap (flag it at submission, not acceptance)

The detail authors most often miss in IER's AER-style policy is the *timing* of the proprietary-data disclosure. If your data are confidential, restricted-access, or otherwise cannot be deposited for open replication, the Editor must be told **at the time of submission** — not when the conditional-acceptance letter arrives. Discovering at acceptance that you cannot meet the deposit requirement can stall or derail publication. So audit the data early: for every source, ask whether you can legally and practically deposit it; if not, plan the alternative the policy permits (e.g., depositing code plus access instructions, or a synthetic/derived dataset) and disclose the constraint up front.

### README discipline that actually permits replication

A README that lists files is not a README that permits replication. The IER/AER standard is an *ordered, runnable* set of instructions: which script to run first, what raw inputs it expects, what intermediate files it produces, and how to reach each table and figure in the paper from the raw data. A reviewer or future researcher should be able to clone the repository, follow the README top to bottom, and regenerate every number. Document software versions and any manual steps (ideally eliminate manual steps entirely). For constructed variables, the chain from raw source to analysis variable must be code, not prose.

## Checklist

- [ ] If data are proprietary or restricted, the Editor is notified **at submission** (not acceptance)
- [ ] Deposit planned for a standard public repository with a data availability statement + link in the final paper
- [ ] Econometric/simulation: final data + programs + construction documentation + **README PDF** with replication steps
- [ ] Experimental: instructions + subject selection info + programs/scripts + raw data
- [ ] Constructed variables are reproducible from raw sources via documented code
- [ ] Proof appendix is self-contained; every formal claim has a proof or a precise citation
- [ ] Structural: solution algorithm, grids, tolerances, solver, and seeds documented
- [ ] Long proofs/derivations in an online appendix; main results provable from paper + appendix

## Anti-patterns

- Treating the deposit as an acceptance-day chore when proprietary data should have been flagged at submission
- A README that lists files but gives no runnable, ordered replication instructions
- Constructed data with no code linking it back to raw sources ("data available on request")
- A key theorem proved only in a footnote or dismissed as "analogous to the above"
- Lemmas invoked without proof or citation
- A structural counterfactual whose grid/solver/seeds are undocumented, so the number cannot be reproduced

## Output format

```text
【Journal】International Economic Review
【Skill】ier-replication-package
【Paper type】econometric/simulation / experimental / theory-only
【Proprietary data?】if yes, Editor notified at submission? [Y/N]
【Deposit plan】repository + data availability statement + README PDF ready? [Y/N]
【Construction docs】constructed vars reproducible from raw via code? [Y/N]
【Proof appendix】self-contained; every claim proved or cited? [Y/N]
【Computational appendix】algorithm/grids/tolerances/seeds documented? [Y/N]
【Verdict】compliant / gaps-listed
【Next skill】ier-referee-strategy
```
