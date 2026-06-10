# ML Experiment Matrix

Use this matrix before recommending submission to a selective AI/ML conference.
Every central claim should have visible evidence in the main paper or an allowed
appendix/supplement.

| Claim type | Required evidence | Common failure |
|---|---|---|
| New method improves performance | Strong baselines, matched compute, multiple seeds, confidence/variance where appropriate, ablations isolating the new component | Only compares against weak or outdated baselines |
| New representation or architecture insight | Diagnostic experiments, controlled comparisons, scaling or stress tests, negative cases | Treats leaderboard gain as explanation |
| Theory or estimator result | Assumptions, theorem statements, proof path, simulation or empirical illustration when useful | Proof is detached from practical contribution |
| Dataset or benchmark | Collection protocol, annotation quality, licenses, leakage checks, splits, metrics, intended use and limitations | Dataset release without evaluation discipline |
| Systems or efficiency contribution | Wall-clock, memory, throughput, hardware, implementation details, fair compute accounting, reproducible commands | Claims speedup without matched hardware or baselines |
| Responsible-AI or safety claim | Threat model, affected stakeholders, evaluation protocol, failure modes, governance/ethics limits | Ethical language without measurable evidence |

## Minimal Output

```text
[Main claim] <one sentence>
[Evidence in paper] <table/figure/theorem/appendix>
[Missing comparator] <baseline, ablation, dataset, proof, or stress test>
[Reproducibility hook] <command, config, seed, artifact, or proof script>
[Reviewer risk] <why an AC/reviewer may still discount the evidence>
```
