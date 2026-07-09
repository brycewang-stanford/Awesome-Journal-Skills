---
name: ecai-experiments
description: Use when designing or auditing the evidence in an ECAI paper — choosing proof versus experiment by claim shape across ECAI's breadth (theory/KR, planning/search, ML, multi-agent, applied), fair baselines, seeds and spread, honest ablations, and provenance, all supporting a claim inside a 7-page body.
---

# ECAI Experiments

The ECAI question is always the same: **is the evidence proportional to the claim?** But ECAI spans
symbolic and applied AI, so "evidence" ranges from a **proof** to a **fair empirical comparison**.
Choosing the right *kind* of evidence for your claim shape is the first and most important decision.

## Choose the evidence type by claim shape

| Claim | Primary evidence | Common ECAI failure |
|---|---|---|
| "Complete / sound / optimal / (1+ε)-bounded" | A **proof**, all assumptions explicit | Asserting it empirically only |
| "More efficient / fewer expansions / faster" | A **controlled comparison** on standard instances, with spread | One lucky run; unfair baseline tuning |
| "Learns/generalizes/calibrates better" | Fair comparison + a *reason why*, seeds, significance | A single benchmark delta with no mechanism |
| "Handles a broader class / new setting" | A construction/encoding + worked cases | Toy examples only |
| "Works in the real world" | A credible deployment demonstration (**PAIS**) | Benchmark abstraction standing in for deployment |

A provable claim needs a proof; an empirical claim needs a fair, seeded comparison; a claim about
*understanding* needs an explanation, not just a number.

## For theory / KR / planning / argumentation

- **Prove it, completely.** The body sketches; the supplement carries full proofs
  (`ecai-reproducibility`). State every assumption (finiteness, admissibility, language fragment).
- **Standard instances for empirical planning/search.** Use recognized domains/benchmarks
  (e.g. the community's standard planning domains) so node/quality numbers are comparable; report
  per-domain results, not just an aggregate.
- **Complexity claims** get the reduction or the algorithm, not a hand-wave.

## For ML / learning-based contributions

- **Fair baselines, fairly tuned.** Give the baseline the same tuning budget as your method; a
  hobbled baseline is the fastest way to lose a reviewer.
- **Seeds and spread.** Report mean and variance/CI across multiple seeds; a single run is not
  evidence. State the number of runs.
- **Explain the win.** ECAI rewards *why* a method works (an ablation isolating the responsible
  component, a theoretical reason) over a leaderboard delta.
- **Contamination and leakage.** For LLM/pretrained components, check train/test overlap and
  document model identifiers with dates; cache outputs so results reproduce.

## For multi-agent contributions

- Specify the **environment, agents, episodes, and metrics** exactly; multi-agent results are
  notoriously protocol-sensitive.
- Compare against the right baselines for the setting (cooperative/competitive), and report across
  seeds and environment variations, not one map.
- If the contribution is fundamentally about agent interaction, sanity-check whether **AAMAS** is
  the better-matched pool (`ecai-topic-selection`).

## For applied AI (PAIS)

- Lead with the **real-world claim** and constraints (data availability, latency, cost, safety),
  not a benchmark score.
- Show the method survives *real* conditions; a deployment story that only reports offline accuracy
  under-delivers on the PAIS bar.

## Ablations and honesty

- **Ablate the mechanism you credit.** If you attribute the gain to component C, remove C and show
  the drop.
- **Report negative and null results** where they bound the claim — in a single-round process,
  self-reported limits cost less than reviewer-discovered ones (`ecai-review-process`).
- **No cherry-picking** domains, seeds, or metrics; report the protocol that generated every number.

## Fit the 7-page body

Evidence a reviewer needs to *judge* the claim (the proof idea, the key comparison, the main table)
stays in the body; full proofs, extra domains, and ablation grids go to the supplement
(`ecai-supplementary`). Do not exile the decision-critical comparison to save space.

## Output format

```text
[Claim -> evidence] each claim mapped to proof / controlled comparison / deployment demo
[Proof completeness] provable claims proved with explicit assumptions? yes/no
[Baseline fairness] baselines tuned comparably? seeds + spread reported?
[Why it works] mechanism explained (ablation/theory), not just a number? yes/no
[Provenance] datasets/models/seeds pinned; outputs cached? gaps: <list>
[Body/supplement] decision-critical evidence inside 7 pages? yes/no
```
