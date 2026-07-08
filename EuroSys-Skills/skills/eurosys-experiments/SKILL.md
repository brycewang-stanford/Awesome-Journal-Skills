---
name: eurosys-experiments
description: Use when designing or auditing the evaluation of a EuroSys paper — choosing workloads that earn the word realistic, tuning baselines beyond their defaults, decomposing end-to-end wins into per-mechanism gains, measuring overheads and worst cases, and sizing experiments to the claims the paper actually makes.
---

# EuroSys Experiments

Use this while the evaluation is still designable. EuroSys reviewers treat the
evaluation as the paper's testimony about itself: the design section says what
should happen, and §Evaluation is cross-examination. Plan it as a set of
questions with falsifiable answers, not as a benchmark tour.

## The four-layer evidence stack

| Layer | Question it answers | Typical EuroSys instrument |
|---|---|---|
| End-to-end | Does the system win where users live? | Full application or serving workload, realistic scale |
| Decomposition | Which mechanism buys which fraction? | Factor analysis: enable components one at a time |
| Cost | What does the win spend? | Memory/CPU/network overhead, code and ops complexity |
| Boundary | Where does it stop winning? | Adversarial mixes, saturation, failure injection |

A submission with only the first layer reads as a demo; the middle layers are
what convert "it is faster" into "we understand why it is faster", which is
the systems-research standard of proof.

## Workload realism, argued not asserted

- Prefer published traces and standard suites with named versions; when using
  a synthetic generator, calibrate it against a real distribution and say how.
- Match the workload to the claim's regime: a memory-efficiency claim needs
  memory pressure; a tail-latency claim needs load near saturation, not at 30%.
- Scale honestly: if the pitch is rack-scale, a two-node result needs an
  explicit extrapolation argument or a scoped-down claim.
- Report the workload's own parameters (skew, read ratio, arrival process) so
  the experiment is reconstructible without your cluster.

## Baseline fairness — the venue's sharpest knife

The reflexive EuroSys reviewer question is "did they tune the baseline?"
Answer it before it is asked:

- Run baselines at their documented best configuration for your hardware, and
  cite where that configuration comes from.
- Include the strongest *deployed* alternative, not only research prototypes —
  losing to a well-tuned production system on some axis is survivable;
  omitting it is not.
- Same hardware, same workload generator, same measurement harness for every
  system; any asymmetry gets a sentence of justification.
- When your system loses a metric, plot it anyway and explain the tradeoff.

## Experiment matrix as an artifact

Freeze the plan in a machine-checkable form before running:

```yaml
# eval-matrix.yaml — one row per claim the paper will make
- claim: "cuts p99 GET latency ≥40% under skewed load"
  figure: fig8
  workload: {trace: twitter-cache-2020, skew: zipf-0.99, load: 0.85sat}
  systems: [ours@v1.4, baselineA@3.2-tuned, baselineB@1.9-tuned]
  reps: 10
  metrics: [p50, p99, p999, throughput]
  status: pending
```

The matrix doubles as the reproducibility ledger (`eurosys-reproducibility`)
and later as the artifact's claims map (`eurosys-artifact-evaluation`).

## Result invalidators to design out early

Each of these has sunk otherwise strong EuroSys evaluations; each is cheap
to prevent and expensive to discover in a review:

- Measuring through a bottleneck that is not the system under test — a
  saturated client, a slow log disk, a debug build of a dependency.
- Comparing your warm system against cold baselines (or vice versa)
  because warm-up policy was never standardized across systems.
- A "scalability" curve whose x-axis grows load and resources together,
  so nothing about scaling behavior is actually isolated.
- Reporting means over runs that include documented failures — decide the
  failure-handling policy for measurements before running them.
- Config drift between the end-to-end and decomposition experiments, so
  the component gains do not sum to anything resembling the headline.

## Sizing runs for the claim

- Comparative bar charts: ≥5–10 repetitions with dispersion shown; single-run
  bars invite a one-line rejection rationale.
- Tail latencies: enough requests that the quoted percentile has support —
  a p999 from 10k requests is ten samples of noise.
- Ablations: vary one factor per experiment; a config delta of two changes
  attributes nothing.
- Timeboxing: reserve cluster time for the boundary layer explicitly; it is
  always the layer teams drop under deadline pressure and the layer reviewers
  miss loudest.

## Reporting floor for the paper

- Hardware and topology for every experiment, once, in a table the
  reader can find (§Evaluation setup), with per-figure deviations noted.
- Software versions for every system in every comparison, including yours.
- Load points quoted with the metric ("85% of measured peak throughput"),
  never as bare client counts whose meaning depends on the cluster.
- Repetition count and dispersion type in every caption that shows a
  comparison.
- A sentence on measurement methodology for anything subtle: how latency
  is timestamped, where the measurement harness sits, what it costs.

## Output format

```text
[Claim -> evidence map] <each paper claim: figure, workload, systems, reps>
[Stack coverage] end-to-end / decomposition / cost / boundary: present or missing
[Baseline fairness] <tuning provenance and deployed-alternative status>
[Realism audit] <trace provenance, load regime, scale honesty>
[Highest-value missing run] <the one experiment to schedule next>
```
